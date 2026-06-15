"""
Search tree data structure for theorem discovery.

Nodes are mathematical states (intermediate results).
Edges are technique applications.
The tree grows as the orchestrator explores paths through the knowledge graph.
"""

from __future__ import annotations

import heapq
import json
import time
from collections import deque
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional


class NodeStatus(str, Enum):
    FRONTIER = "frontier"
    PARTIAL = "partial"  # popped & some candidates tried, but untried ones remain
    EXPANDED = "expanded"
    PRUNED = "pruned"
    GOAL = "goal"
    DEPTH_LIMIT = "depth_limit"


# Statuses that mean "still has work to do" — eligible to (re)enter expansion.
ACTIVE_STATUSES = (NodeStatus.FRONTIER, NodeStatus.PARTIAL)


@dataclass
class MathState:
    """A mathematical state — an intermediate or final result."""

    description: str
    formal: str = ""
    graph_nodes_used: list[str] = field(default_factory=list)
    graph_nodes_produced: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "description": self.description,
            "formal": self.formal,
            "graph_nodes_used": self.graph_nodes_used,
            "graph_nodes_produced": self.graph_nodes_produced,
        }

    @classmethod
    def from_dict(cls, d: dict) -> MathState:
        return cls(
            description=d.get("description", ""),
            formal=d.get("formal", ""),
            graph_nodes_used=d.get("graph_nodes_used", []),
            graph_nodes_produced=d.get("graph_nodes_produced", []),
        )


@dataclass
class WorkerResult:
    """Output from a worker LLM trying a technique on a state."""

    new_state: MathState
    confidence: float
    proof_sketch: str
    impossible: bool = False
    impossible_reason: str = ""
    technique_id: str = ""

    def to_dict(self) -> dict:
        return {
            "new_state": self.new_state.to_dict(),
            "confidence": self.confidence,
            "proof_sketch": self.proof_sketch,
            "impossible": self.impossible,
            "impossible_reason": self.impossible_reason,
            "technique_id": self.technique_id,
        }


@dataclass
class SearchNode:
    """A node in the search tree."""

    id: str
    state: MathState
    parent_id: Optional[str] = None
    technique_applied: Optional[str] = None
    confidence: float = 1.0
    status: NodeStatus = NodeStatus.FRONTIER
    depth: int = 0
    pruned_reason: Optional[str] = None
    proof_sketch: str = ""
    children_ids: list[str] = field(default_factory=list)
    created_at: float = field(default_factory=time.time)
    # --- attempt ledger: which techniques were tried at this node ---
    candidates: list[str] = field(default_factory=list)  # ordered techniques chosen for this node
    attempts: dict[str, dict] = field(default_factory=dict)
    # attempts: technique_id -> {"outcome": "child"|"pruned"|"impossible",
    #                            "child_id": str|None, "reason": str, "confidence": float}

    def untried(self) -> list[str]:
        """Candidate techniques not yet attempted at this node (BFS resume order)."""
        return [t for t in self.candidates if t not in self.attempts]

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "state": self.state.to_dict(),
            "parent_id": self.parent_id,
            "technique_applied": self.technique_applied,
            "confidence": self.confidence,
            "status": self.status.value,
            "depth": self.depth,
            "pruned_reason": self.pruned_reason,
            "proof_sketch": self.proof_sketch,
            "children_ids": self.children_ids,
            "candidates": self.candidates,
            "attempts": self.attempts,
        }


class SearchTree:
    """
    The search tree that grows during discovery.

    Uses a priority queue (max-heap via negated scores) to pick
    the most promising frontier node at each iteration.
    """

    def __init__(self, mode: str = "best_first"):
        self.nodes: dict[str, SearchNode] = {}
        self.root_id: Optional[str] = None
        self._counter = 0
        self._frontier: list[tuple[float, int, str]] = []  # (-score, tiebreak, node_id)
        self._tiebreak = 0
        self.mode = mode  # "best_first" (priority heap) or "bfs" (FIFO, level-order)
        self._bfs: deque[str] = deque()

    def _next_id(self) -> str:
        self._counter += 1
        return f"sn_{self._counter:04d}"

    def create_root(self, state: MathState) -> SearchNode:
        nid = self._next_id()
        node = SearchNode(id=nid, state=state, depth=0, status=NodeStatus.EXPANDED)
        self.nodes[nid] = node
        self.root_id = nid
        return node

    def add_child(
        self,
        parent: SearchNode,
        result: WorkerResult,
        status: NodeStatus = NodeStatus.FRONTIER,
        pruned_reason: str | None = None,
    ) -> SearchNode:
        nid = self._next_id()
        child = SearchNode(
            id=nid,
            state=result.new_state,
            parent_id=parent.id,
            technique_applied=result.technique_id,
            confidence=result.confidence,
            status=status,
            depth=parent.depth + 1,
            pruned_reason=pruned_reason,
            proof_sketch=result.proof_sketch,
        )
        self.nodes[nid] = child
        parent.children_ids.append(nid)
        return child

    def push_frontier(self, node: SearchNode, score: float):
        if self.mode == "bfs":
            self._bfs.append(node.id)
        else:
            self._tiebreak += 1
            heapq.heappush(self._frontier, (-score, self._tiebreak, node.id))

    def requeue_front(self, node: SearchNode):
        """Put a partially-expanded node back at the *front* so resume tries its
        remaining (untried) techniques before descending a level."""
        if self.mode == "bfs":
            self._bfs.appendleft(node.id)
        else:
            self._tiebreak += 1
            # most-negative key == highest priority in the min-heap
            heapq.heappush(self._frontier, (-1e18, self._tiebreak, node.id))

    def pop_frontier(self) -> SearchNode | None:
        if self.mode == "bfs":
            while self._bfs:
                nid = self._bfs.popleft()
                node = self.nodes.get(nid)
                if node and node.status in ACTIVE_STATUSES:
                    return node
            return None
        while self._frontier:
            neg_score, _, nid = heapq.heappop(self._frontier)
            node = self.nodes.get(nid)
            if node and node.status in ACTIVE_STATUSES:
                return node
        return None

    def frontier_size(self) -> int:
        if self.mode == "bfs":
            return sum(
                1
                for nid in self._bfs
                if nid in self.nodes and self.nodes[nid].status in ACTIVE_STATUSES
            )
        return sum(
            1
            for _, _, nid in self._frontier
            if nid in self.nodes and self.nodes[nid].status in ACTIVE_STATUSES
        )

    def extract_path(self, node: SearchNode) -> list[SearchNode]:
        """Walk from node back to root, return root-first path."""
        path = []
        current: SearchNode | None = node
        while current is not None:
            path.append(current)
            current = self.nodes.get(current.parent_id) if current.parent_id else None
        path.reverse()
        return path

    def mark_goal(self, node: SearchNode):
        node.status = NodeStatus.GOAL

    def find_goal(self) -> SearchNode | None:
        """Return the node marked GOAL, if any."""
        for n in self.nodes.values():
            if n.status == NodeStatus.GOAL:
                return n
        return None

    def best_node(self) -> SearchNode | None:
        """Best node to write up when no goal was reached: deepest, then highest
        confidence. Used as a fallback for proof synthesis on an unsolved run."""
        candidates = [n for n in self.nodes.values() if n.id != self.root_id]
        if not candidates:
            return self.nodes.get(self.root_id)
        return max(candidates, key=lambda n: (n.depth, n.confidence))

    def mark_pruned(self, node: SearchNode, reason: str):
        node.status = NodeStatus.PRUNED
        node.pruned_reason = reason

    def summary(self) -> dict:
        status_counts: dict[str, int] = {}
        for n in self.nodes.values():
            s = n.status.value
            status_counts[s] = status_counts.get(s, 0) + 1
        max_depth = max((n.depth for n in self.nodes.values()), default=0)
        return {
            "total_nodes": len(self.nodes),
            "frontier_size": self.frontier_size(),
            "max_depth": max_depth,
            "status_counts": status_counts,
        }

    def to_dict(self, include_frontier: bool = False) -> dict:
        d = {
            "root_id": self.root_id,
            "mode": self.mode,
            "nodes": {nid: n.to_dict() for nid, n in self.nodes.items()},
            "summary": self.summary(),
        }
        if include_frontier:
            d["_frontier"] = list(self._frontier)
            d["_bfs"] = list(self._bfs)
            d["_counter"] = self._counter
            d["_tiebreak"] = self._tiebreak
        return d

    @classmethod
    def from_dict(cls, d: dict) -> SearchTree:
        tree = cls(mode=d.get("mode", "best_first"))
        tree.root_id = d.get("root_id")
        tree._counter = d.get("_counter", 0)
        tree._tiebreak = d.get("_tiebreak", 0)
        for nid, nd in d.get("nodes", {}).items():
            tree.nodes[nid] = SearchNode(
                id=nd["id"],
                state=MathState.from_dict(nd["state"]),
                parent_id=nd.get("parent_id"),
                technique_applied=nd.get("technique_applied"),
                confidence=nd.get("confidence", 1.0),
                status=NodeStatus(nd.get("status", "frontier")),
                depth=nd.get("depth", 0),
                pruned_reason=nd.get("pruned_reason"),
                proof_sketch=nd.get("proof_sketch", ""),
                children_ids=nd.get("children_ids", []),
                candidates=nd.get("candidates", []),
                attempts=nd.get("attempts", {}),
            )
        raw_bfs = d.get("_bfs", [])
        raw_frontier = d.get("_frontier", [])
        if tree.mode == "bfs":
            if raw_bfs:
                tree._bfs = deque(raw_bfs)
            else:
                for nid, node in tree.nodes.items():
                    if node.status in ACTIVE_STATUSES:
                        tree._bfs.append(nid)
        else:
            if raw_frontier:
                tree._frontier = [tuple(entry) for entry in raw_frontier]
                heapq.heapify(tree._frontier)
            else:
                for nid, node in tree.nodes.items():
                    if node.status in ACTIVE_STATUSES:
                        tree._tiebreak += 1
                        heapq.heappush(tree._frontier, (-node.confidence, tree._tiebreak, nid))
        return tree

    @classmethod
    def load(cls, path: str | Path) -> SearchTree:
        with open(path) as f:
            return cls.from_dict(json.load(f))

    def save(self, path: str | Path, include_frontier: bool = False):
        with open(path, "w") as f:
            json.dump(self.to_dict(include_frontier=include_frontier), f, indent=2)

    def print_tree(self, node_id: str | None = None, indent: int = 0):
        """Print the tree structure to stdout."""
        if node_id is None:
            node_id = self.root_id
        if node_id is None:
            return
        node = self.nodes[node_id]
        status_icon = {
            NodeStatus.FRONTIER: "○",
            NodeStatus.PARTIAL: "◐",
            NodeStatus.EXPANDED: "◉",
            NodeStatus.PRUNED: "✗",
            NodeStatus.GOAL: "★",
            NodeStatus.DEPTH_LIMIT: "⊘",
        }
        icon = status_icon.get(node.status, "?")
        technique = node.technique_applied or "ROOT"
        conf = f" ({node.confidence:.0%})" if node.technique_applied else ""
        prefix = "  " * indent
        desc = node.state.description[:80]
        print(f"{prefix}{icon} [{technique}]{conf} {desc}")
        for cid in node.children_ids:
            self.print_tree(cid, indent + 1)

    def attempt_report(self) -> dict[int, list[dict]]:
        """Group every recorded technique attempt by tree depth (level).

        Returns ``{depth: [{"node": id, "technique": tid, "outcome": ...,
        "reason": ...}, ...]}`` — i.e. exactly which technique was tried at
        which level and how it turned out (child / pruned / impossible).
        """
        by_level: dict[int, list[dict]] = {}
        for node in self.nodes.values():
            for tid, rec in node.attempts.items():
                by_level.setdefault(node.depth, []).append(
                    {
                        "node": node.id,
                        "technique": tid,
                        "outcome": rec.get("outcome", "?"),
                        "reason": rec.get("reason", ""),
                        "confidence": rec.get("confidence", 0.0),
                    }
                )
        return dict(sorted(by_level.items()))

    def print_attempts(self):
        """Human-readable per-level ledger of what has been tried."""
        report = self.attempt_report()
        if not report:
            print("  (no technique attempts recorded yet)")
            return
        outcome_icon = {"child": "○", "pruned": "✗", "impossible": "⊘"}
        for depth, attempts in report.items():
            print(f"  Level {depth}:")
            for a in attempts:
                ic = outcome_icon.get(a["outcome"], "?")
                reason = f" — {a['reason'][:60]}" if a["reason"] else ""
                print(f"    {ic} [{a['technique']}] on {a['node']} ({a['outcome']}){reason}")
        # show what is still pending
        pending = [
            (n.depth, n.id, t)
            for n in self.nodes.values()
            for t in n.untried()
            if n.status in ACTIVE_STATUSES
        ]
        if pending:
            print("  Pending (untried, will run on resume):")
            for depth, nid, t in sorted(pending):
                print(f"    · Level {depth}: [{t}] on {nid}")
