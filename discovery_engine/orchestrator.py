"""
Orchestrator — the main discovery loop.

Parses a problem into start nodes, selects techniques, dispatches workers,
evaluates results, manages the search frontier, and detects when the goal
is reached.
"""

from __future__ import annotations

import json
import os
import signal
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

from .graph import KnowledgeGraph
from .pruner import Pruner
from .search_tree import MathState, NodeStatus, SearchNode, SearchTree, WorkerResult
from .worker import CLIWorker, MockWorker, Worker

ORCHESTRATOR_SYSTEM = """\
You are a mathematical research director. You will be given a problem \
statement and access to a knowledge graph of mathematical truths. Your job \
is to:
1. Identify which existing nodes in the graph are relevant starting points.
2. Describe the goal state (what a solution looks like).
3. Return structured JSON.

Return ONLY a JSON object:
{
  "start_node_ids": ["s_...", "s_...", ...],
  "start_description": "...",
  "start_formal": "...",
  "goal_description": "...",
  "relevant_keywords": ["...", "..."]
}"""

GOAL_CHECK_SYSTEM = """\
You are a mathematical proof verifier. Given a claimed result and the \
original goal, decide if the goal has been reached.

Return ONLY a JSON object:
{
  "goal_reached": true/false,
  "explanation": "..."
}"""

TECHNIQUE_SELECT_SYSTEM = """\
You are a mathematical strategist. Given a current state and a goal, \
select the most promising techniques to try next from the candidate list.

Consider:
- Which technique's input type matches the current state?
- Which technique moves closest toward the goal?
- Cross-field techniques (from a different cluster) get bonus for novelty.

Return ONLY a JSON object:
{
  "selected": ["t_...", "t_...", ...],
  "reasoning": "..."
}"""


class Orchestrator:
    """Main discovery loop."""

    def __init__(
        self,
        graph: KnowledgeGraph,
        worker: Worker | MockWorker | None = None,
        max_depth: int = 7,
        max_iterations: int = 200,
        max_parallel_workers: int = 5,
        candidates_per_step: int = 4,
        model: str = "claude-sonnet-4-20250514",
        verbose: bool = True,
        checkpoint_dir: str | None = None,
        checkpoint_every: int = 5,
    ):
        self.graph = graph
        self.worker = worker or MockWorker()
        self.pruner = Pruner(graph)
        self.tree = SearchTree()
        self.max_depth = max_depth
        self.max_iterations = max_iterations
        self.max_parallel = max_parallel_workers
        self.candidates_per_step = candidates_per_step
        self.model = model
        self.verbose = verbose
        self.goal_description = ""
        self._api_key = os.environ.get("ANTHROPIC_API_KEY")
        self.token_stats = {"orchestrator_input": 0, "orchestrator_output": 0, "orchestrator_calls": 0}
        self.checkpoint_dir = Path(checkpoint_dir) if checkpoint_dir else None
        self.checkpoint_every = checkpoint_every
        self._interrupted = False
        self._resume_iteration = 0

    # ------------------------------------------------------------------
    # LLM calls for orchestration decisions
    # ------------------------------------------------------------------

    def _call_llm(self, system: str, user: str) -> str:
        import anthropic

        client = anthropic.Anthropic(api_key=self._api_key)
        resp = client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=[
                {
                    "type": "text",
                    "text": system,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            messages=[{"role": "user", "content": user}],
        )
        usage = resp.usage
        self.token_stats["orchestrator_input"] += getattr(usage, "input_tokens", 0)
        self.token_stats["orchestrator_output"] += getattr(usage, "output_tokens", 0)
        self.token_stats["orchestrator_calls"] += 1
        return resp.content[0].text

    def _parse_json(self, text: str) -> dict:
        text = text.strip()
        if text.startswith("```"):
            lines = text.split("\n")
            lines = [l for l in lines if not l.strip().startswith("```")]
            text = "\n".join(lines)
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {}

    # ------------------------------------------------------------------
    # Phase 1: Parse the problem
    # ------------------------------------------------------------------

    def parse_problem(self, problem: str) -> tuple[MathState, str]:
        """Use LLM to identify start nodes and goal from a problem statement."""
        available = self.graph.search_nodes(problem.split()[:10], max_results=30)
        node_list = "\n".join(
            f"- {n['id']}: [{n.get('kind','')}] {n.get('name','')}"
            for n in available
        )

        user_prompt = (
            f"## Problem\n{problem}\n\n"
            f"## Available nodes in the knowledge graph (sample):\n{node_list}\n\n"
            f"## Full graph stats: {json.dumps(self.graph.stats())}\n\n"
            "Identify start nodes and goal."
        )

        raw = self._call_llm(ORCHESTRATOR_SYSTEM, user_prompt)
        parsed = self._parse_json(raw)

        start_ids = parsed.get("start_node_ids", [])
        valid_ids = [sid for sid in start_ids if sid in self.graph.nodes]

        if not valid_ids:
            results = self.graph.search_nodes(
                parsed.get("relevant_keywords", problem.split()[:5])
            )
            valid_ids = [n["id"] for n in results[:5]]

        start_state = MathState(
            description=parsed.get("start_description", problem),
            formal=parsed.get("start_formal", ""),
            graph_nodes_used=valid_ids,
        )
        goal = parsed.get("goal_description", problem)
        return start_state, goal

    def parse_problem_mock(self, problem: str, start_node_ids: list[str], goal: str) -> tuple[MathState, str]:
        """Manual start node selection — no LLM call needed."""
        valid_ids = [sid for sid in start_node_ids if sid in self.graph.nodes]
        start_state = MathState(
            description=problem,
            graph_nodes_used=valid_ids,
        )
        return start_state, goal

    # ------------------------------------------------------------------
    # Phase 2: Select techniques
    # ------------------------------------------------------------------

    def _valid_state_ids(self, state: MathState) -> list[str]:
        """Filter state node IDs to only those that exist in the graph."""
        return [
            nid for nid in state.graph_nodes_used + state.graph_nodes_produced
            if nid in self.graph.nodes
        ]

    def select_techniques(self, state: MathState) -> list[str]:
        """Score and rank techniques for the current state."""
        all_techniques_from_state: set[str] = set()
        for nid in self._valid_state_ids(state):
            all_techniques_from_state.update(self.graph.techniques_from(nid))

        if not all_techniques_from_state:
            all_techniques_from_state = set(list(self.graph.techniques.keys())[:20])

        scored: list[tuple[float, str]] = []
        for tid in all_techniques_from_state:
            score = self._score_technique(tid, state)
            scored.append((score, tid))

        scored.sort(reverse=True)
        return [tid for _, tid in scored[: self.candidates_per_step]]

    def select_techniques_llm(self, state: MathState) -> list[str]:
        """Use LLM to pick techniques (more expensive but smarter)."""
        all_techniques_from_state: set[str] = set()
        for nid in self._valid_state_ids(state):
            all_techniques_from_state.update(self.graph.techniques_from(nid))

        candidate_list = "\n".join(
            f"- {tid}: {self.graph.techniques[tid].get('name', tid)} "
            f"(cluster {self.graph.get_cluster(tid)})"
            for tid in all_techniques_from_state
            if tid in self.graph.techniques
        )

        user = (
            f"## Current State\n{state.description}\n\n"
            f"## Goal\n{self.goal_description}\n\n"
            f"## Candidate Techniques\n{candidate_list}\n\n"
            f"Select up to {self.candidates_per_step} techniques."
        )

        raw = self._call_llm(TECHNIQUE_SELECT_SYSTEM, user)
        parsed = self._parse_json(raw)
        selected = parsed.get("selected", [])
        valid = [t for t in selected if t in self.graph.techniques]
        if not valid:
            return self.select_techniques(state)
        return valid[: self.candidates_per_step]

    def _score_technique(self, technique_id: str, state: MathState) -> float:
        """Heuristic scoring from Ch. 13."""
        w1, w2, w3, w4, w5 = 0.30, 0.25, 0.15, 0.20, 0.10

        # Proximity: how many of the technique's neighbors overlap with the goal keywords
        nbrs = self.graph.technique_neighbors(technique_id)
        all_nbr_names = " ".join(
            n.get("name", "") for n in nbrs["inputs"] + nbrs["outputs"]
        ).lower()
        goal_words = self.goal_description.lower().split()
        proximity = sum(1 for w in goal_words if w in all_nbr_names) / max(len(goal_words), 1)

        # Precondition match: overlap between technique inputs and state nodes
        input_ids = {n["id"] for n in nbrs["inputs"]}
        state_ids = set(self._valid_state_ids(state))
        precond = len(input_ids & state_ids) / max(len(input_ids), 1)

        # Historical: edge count as a proxy for how often the technique is used
        edge_count = len(nbrs["inputs"]) + len(nbrs["outputs"])
        historical = min(edge_count / 500, 1.0)

        # Bridge potential
        state_clusters = set()
        for nid in self._valid_state_ids(state):
            for tid in self.graph.techniques_from(nid):
                c = self.graph.get_cluster(tid)
                if c:
                    state_clusters.add(c)
        t_cluster = self.graph.get_cluster(technique_id)
        bridge = 1.0 if (t_cluster and t_cluster not in state_clusters) else 0.2

        score = w1 * proximity + w2 * precond + w3 * historical + w4 * bridge
        return score

    # ------------------------------------------------------------------
    # Phase 3: Check goal
    # ------------------------------------------------------------------

    def check_goal(self, state: MathState) -> bool:
        """Use LLM to check if the goal has been reached."""
        user = (
            f"## Claimed Result\n{state.description}\n\n"
            f"Formal: {state.formal}\n\n"
            f"## Original Goal\n{self.goal_description}\n\n"
            "Has the goal been reached?"
        )
        raw = self._call_llm(GOAL_CHECK_SYSTEM, user)
        parsed = self._parse_json(raw)
        return bool(parsed.get("goal_reached", False))

    def check_goal_mock(self, state: MathState) -> bool:
        """Keyword-based goal check for dry runs."""
        goal_words = set(self.goal_description.lower().split())
        state_words = set(state.description.lower().split())
        overlap = len(goal_words & state_words) / max(len(goal_words), 1)
        return overlap > 0.6

    # ------------------------------------------------------------------
    # Checkpointing
    # ------------------------------------------------------------------

    def save_checkpoint(self, path: str | Path, iteration: int, stats: dict,
                        problem: str, start_node_ids: list[str] | None,
                        goal: str | None, use_llm: bool):
        checkpoint = {
            "version": 1,
            "iteration": iteration,
            "stats": stats,
            "goal_description": self.goal_description,
            "token_stats": self.token_stats,
            "tree": self.tree.to_dict(include_frontier=True),
            "params": {
                "problem": problem,
                "start_node_ids": start_node_ids,
                "goal": goal,
                "use_llm_for_orchestration": use_llm,
                "max_depth": self.max_depth,
                "max_iterations": self.max_iterations,
                "candidates_per_step": self.candidates_per_step,
                "model": self.model,
            },
            "saved_at": time.time(),
        }
        path = Path(path)
        tmp = path.with_suffix(".tmp")
        with open(tmp, "w") as f:
            json.dump(checkpoint, f, indent=2)
        tmp.rename(path)
        self._log(f"  💾 Checkpoint saved: {path}")

    @classmethod
    def load_checkpoint(cls, path: str | Path) -> dict:
        with open(path) as f:
            return json.load(f)

    def _restore_from_checkpoint(self, ckpt: dict):
        self.tree = SearchTree.from_dict(ckpt["tree"])
        self.goal_description = ckpt["goal_description"]
        self.token_stats = ckpt.get("token_stats", self.token_stats)
        self._resume_iteration = ckpt["iteration"]

    def _checkpoint_path(self, iteration: int) -> Path | None:
        if not self.checkpoint_dir:
            return None
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        return self.checkpoint_dir / "checkpoint_latest.json"

    def _install_signal_handler(self):
        def _handler(sig, frame):
            self._log("\n⚠ Interrupt received — will save checkpoint after current iteration.")
            self._interrupted = True
        signal.signal(signal.SIGINT, _handler)

    # ------------------------------------------------------------------
    # Main loop
    # ------------------------------------------------------------------

    def discover(
        self,
        problem: str,
        start_node_ids: list[str] | None = None,
        goal: str | None = None,
        use_llm_for_orchestration: bool = False,
        resume_from: str | None = None,
    ) -> dict:
        """
        Run the discovery loop.

        Args:
            problem: Natural language problem statement.
            start_node_ids: Override start nodes (skips LLM parsing if provided).
            goal: Override goal description.
            use_llm_for_orchestration: If True, use LLM for technique selection
                and goal checking (more expensive). If False, use heuristics.
            resume_from: Path to a checkpoint file to resume from.

        Returns:
            Dict with 'path' (if found), 'tree', and 'stats'.
        """
        self._interrupted = False
        self._install_signal_handler()

        if resume_from:
            ckpt = self.load_checkpoint(resume_from)
            self._restore_from_checkpoint(ckpt)
            params = ckpt.get("params", {})
            problem = params.get("problem", problem)
            start_node_ids = params.get("start_node_ids", start_node_ids)
            goal = params.get("goal", goal)
            use_llm_for_orchestration = params.get("use_llm_for_orchestration", use_llm_for_orchestration)
            stats = ckpt["stats"]
            start_iter = self._resume_iteration + 1
            self._log(f"Resumed from checkpoint at iteration {self._resume_iteration}")
            self._log(f"  Tree: {self.tree.summary()}")
            self._log(f"  Goal: {self.goal_description}")
        else:
            self._log(f"Problem: {problem}")
            self._log(f"Graph: {self.graph.stats()}")

            if start_node_ids and goal:
                start_state, self.goal_description = self.parse_problem_mock(
                    problem, start_node_ids, goal
                )
            elif use_llm_for_orchestration:
                start_state, self.goal_description = self.parse_problem(problem)
            else:
                start_state = MathState(
                    description=problem,
                    graph_nodes_used=self._auto_find_start_nodes(problem),
                )
                self.goal_description = goal or problem

            self._log(f"Start nodes: {start_state.graph_nodes_used}")
            self._log(f"Goal: {self.goal_description}")

            root = self.tree.create_root(start_state)
            self.tree.push_frontier(root, 1.0)
            root.status = NodeStatus.FRONTIER

            stats = {"iterations": 0, "worker_calls": 0, "pruned": 0, "goal_found": False}
            start_iter = 1

        for iteration in range(start_iter, self.max_iterations + 1):
            if self._interrupted:
                self._log(f"\n⚠ Interrupted at iteration {iteration}.")
                self._save_if_checkpointing(iteration, stats, problem, start_node_ids, goal, use_llm_for_orchestration)
                stats["tokens"] = self._collect_token_stats()
                return {
                    "found": False,
                    "interrupted": True,
                    "path": None,
                    "tree": self.tree.to_dict(),
                    "stats": stats,
                }

            stats["iterations"] = iteration

            current = self.tree.pop_frontier()
            if current is None:
                self._log("Frontier exhausted.")
                break

            if current.depth >= self.max_depth:
                current.status = NodeStatus.DEPTH_LIMIT
                self._log(f"  Depth limit at {current.id}")
                continue

            if current.state.description.startswith(("[TIMEOUT]", "[ERROR]", "[PARSE ERROR]")):
                current.status = NodeStatus.PRUNED
                current.pruned_reason = "Dead state (timeout/error)"
                self._log(f"  ✗ Skipping dead node {current.id}: {current.state.description[:60]}")
                continue

            current.status = NodeStatus.EXPANDED

            self._log(
                f"\n--- Iteration {iteration} | "
                f"Expanding {current.id} (depth {current.depth}) | "
                f"Frontier: {self.tree.frontier_size()} ---"
            )
            self._log(f"  State: {current.state.description[:100]}")

            # Select techniques
            if use_llm_for_orchestration:
                candidates = self.select_techniques_llm(current.state)
            else:
                candidates = self.select_techniques(current.state)

            self._log(f"  Candidates: {candidates}")

            # Dispatch workers
            results = self._dispatch_workers(current.state, candidates)
            stats["worker_calls"] += len(results)

            # Process results
            for technique_id, result in results:
                if result.impossible:
                    child = self.tree.add_child(
                        current, result, NodeStatus.PRUNED, result.impossible_reason or "Worker marked impossible"
                    )
                    stats["pruned"] += 1
                    self._log(f"  ✗ IMPOSSIBLE {technique_id}: {result.impossible_reason[:80] if result.impossible_reason else 'no reason'}")
                    continue

                prune_decision = self.pruner.check(
                    current.state, technique_id, result, current.depth + 1
                )

                if prune_decision.should_prune:
                    child = self.tree.add_child(
                        current, result, NodeStatus.PRUNED, prune_decision.reason
                    )
                    stats["pruned"] += 1
                    self._log(f"  ✗ PRUNED {technique_id}: {prune_decision.reason}")
                    continue

                adjusted_confidence = result.confidence * prune_decision.confidence_multiplier
                result.confidence = adjusted_confidence

                child = self.tree.add_child(current, result, NodeStatus.FRONTIER)

                self._log(
                    f"  ○ {technique_id} -> {child.id} "
                    f"(conf={adjusted_confidence:.0%}) "
                    f"{result.new_state.description[:60]}"
                )

                # Check goal
                if use_llm_for_orchestration:
                    reached = self.check_goal(result.new_state)
                else:
                    reached = self.check_goal_mock(result.new_state)

                if reached:
                    self.tree.mark_goal(child)
                    path = self.tree.extract_path(child)
                    stats["goal_found"] = True
                    stats["tokens"] = self._collect_token_stats()
                    self._log(f"\n★ GOAL REACHED at {child.id}!")
                    self._log_path(path)
                    return {
                        "found": True,
                        "path": [n.to_dict() for n in path],
                        "tree": self.tree.to_dict(),
                        "stats": stats,
                    }

                # Score and push to frontier
                score = self._score_technique(technique_id, result.new_state)
                score *= adjusted_confidence
                self.tree.push_frontier(child, score)

            # Periodic checkpoint
            if self.checkpoint_dir and iteration % self.checkpoint_every == 0:
                self.save_checkpoint(
                    self._checkpoint_path(iteration),
                    iteration, stats, problem, start_node_ids, goal, use_llm_for_orchestration,
                )

        self._log(f"\nSearch complete. No proof found in {stats['iterations']} iterations.")
        stats["tokens"] = self._collect_token_stats()
        return {
            "found": False,
            "path": None,
            "tree": self.tree.to_dict(),
            "stats": stats,
        }

    def _save_if_checkpointing(self, iteration, stats, problem, start_node_ids, goal, use_llm):
        ckpt_path = self._checkpoint_path(iteration)
        if ckpt_path:
            self.save_checkpoint(ckpt_path, iteration, stats, problem, start_node_ids, goal, use_llm)
        else:
            fallback = Path("checkpoint_interrupted.json")
            self.save_checkpoint(fallback, iteration, stats, problem, start_node_ids, goal, use_llm)

    def _dispatch_workers(
        self, state: MathState, technique_ids: list[str]
    ) -> list[tuple[str, WorkerResult]]:
        """Run workers in parallel."""
        results: list[tuple[str, WorkerResult]] = []

        if isinstance(self.worker, MockWorker):
            for tid in technique_ids:
                r = self.worker.apply_technique(state, tid, self.goal_description, self.graph)
                results.append((tid, r))
            return results

        if isinstance(self.worker, CLIWorker):
            max_p = self.worker.max_parallel
            with ThreadPoolExecutor(max_workers=max_p) as pool:
                futures = {}
                for tid in technique_ids:
                    f = pool.submit(
                        self.worker.apply_technique,
                        state, tid, self.goal_description, self.graph,
                    )
                    futures[f] = tid
                for f in as_completed(futures):
                    tid = futures[f]
                    try:
                        result = f.result()
                    except Exception as exc:
                        result = WorkerResult(
                            new_state=MathState(description=f"[ERROR] {exc}"),
                            confidence=0.0, proof_sketch="",
                            impossible=True, impossible_reason=str(exc),
                            technique_id=tid,
                        )
                    results.append((tid, result))
            return results

        with ThreadPoolExecutor(max_workers=self.max_parallel) as pool:
            futures = {}
            for tid in technique_ids:
                f = pool.submit(
                    self.worker.apply_technique,
                    state,
                    tid,
                    self.goal_description,
                    self.graph,
                )
                futures[f] = tid

            for f in as_completed(futures):
                tid = futures[f]
                try:
                    result = f.result()
                except Exception as exc:
                    result = WorkerResult(
                        new_state=MathState(description=f"[ERROR] {exc}"),
                        confidence=0.0,
                        proof_sketch="",
                        impossible=True,
                        impossible_reason=str(exc),
                        technique_id=tid,
                    )
                results.append((tid, result))

        return results

    def _auto_find_start_nodes(self, problem: str) -> list[str]:
        """Keyword search for start nodes — no LLM needed."""
        words = [w.lower().strip(".,;:!?") for w in problem.split() if len(w) > 3]
        results = self.graph.search_nodes(words, max_results=10)
        return [n["id"] for n in results]

    def _collect_token_stats(self) -> dict:
        """Merge orchestrator + worker token stats."""
        worker_stats = getattr(self.worker, "token_stats", {})
        return {
            "orchestrator": self.token_stats.copy(),
            "workers": worker_stats.copy() if worker_stats else {},
            "total_input": (
                self.token_stats.get("orchestrator_input", 0)
                + worker_stats.get("input", 0)
            ),
            "total_output": (
                self.token_stats.get("orchestrator_output", 0)
                + worker_stats.get("output", 0)
            ),
            "cache_read": worker_stats.get("cache_read", 0),
            "cache_create": worker_stats.get("cache_create", 0),
        }

    def _log(self, msg: str):
        if self.verbose:
            print(msg)

    def _log_path(self, path: list[SearchNode]):
        self._log("\n=== DISCOVERED PATH ===")
        for i, node in enumerate(path):
            technique = node.technique_applied or "START"
            self._log(
                f"  Layer {i}: [{technique}] -> {node.state.description[:80]} "
                f"(conf={node.confidence:.0%})"
            )
        self._log("=== END ===\n")
