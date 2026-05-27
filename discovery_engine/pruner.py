"""
Pruner — kills branches that are 100% impossible, demotes uncertain ones.

Hard prunes: type mismatch, known impossibility theorems, logical contradiction.
Soft demotions: low confidence, unusual technique class, far from goal.
Anti-pruning: never prune cross-cluster bridges or early-depth nodes.
"""

from __future__ import annotations

from .search_tree import MathState, WorkerResult

IMPOSSIBILITY_THEOREMS = {
    "abel_ruffini": "No general radical formula for polynomial equations of degree >= 5",
    "godel_incompleteness": "No consistent formal system can prove its own consistency",
    "turing_halting": "No algorithm can decide whether an arbitrary program halts",
    "mrdp": "No algorithm can decide whether an arbitrary Diophantine equation has solutions",
    "rice": "No algorithm can decide any nontrivial semantic property of programs",
    "cantor_diagonal": "No surjection from a set to its power set",
    "brouwer_nonretraction": "No continuous retraction from disk to boundary",
    "banach_tarski_requires_ac": "Paradoxical decomposition requires Axiom of Choice",
}

IMPOSSIBILITY_KEYWORDS = {
    "general radical formula for degree 5": "abel_ruffini",
    "quintic formula": "abel_ruffini",
    "decide halting": "turing_halting",
    "solve arbitrary diophantine": "mrdp",
    "prove own consistency": "godel_incompleteness",
    "semantic property of programs": "rice",
    "surjection onto power set": "cantor_diagonal",
    "retract disk to boundary": "brouwer_nonretraction",
}


class PruneDecision:
    """Result of a pruning check."""

    def __init__(
        self,
        should_prune: bool,
        reason: str = "",
        confidence_multiplier: float = 1.0,
    ):
        self.should_prune = should_prune
        self.reason = reason
        self.confidence_multiplier = confidence_multiplier

    def __repr__(self):
        if self.should_prune:
            return f"PRUNE({self.reason})"
        if self.confidence_multiplier < 1.0:
            return f"DEMOTE(x{self.confidence_multiplier:.1f}, {self.reason})"
        return "KEEP"


class Pruner:
    """Evaluates whether a search branch should be pruned or demoted."""

    def __init__(self, graph):
        self.graph = graph

    def check(
        self,
        state: MathState,
        technique_id: str,
        result: WorkerResult,
        depth: int,
    ) -> PruneDecision:
        if result.impossible and self._confirm_impossible(result):
            return PruneDecision(
                should_prune=True,
                reason=f"Worker confirmed impossible: {result.impossible_reason}",
            )

        impossibility = self._check_impossibility_theorems(result)
        if impossibility:
            return PruneDecision(
                should_prune=True,
                reason=f"Violates {impossibility}: {IMPOSSIBILITY_THEOREMS[impossibility]}",
            )

        if self._check_contradiction(result):
            return PruneDecision(
                should_prune=True,
                reason="Output contradicts a known theorem in the graph",
            )

        if self._is_anti_pruned(technique_id, depth):
            return PruneDecision(should_prune=False, confidence_multiplier=1.0)

        multiplier = 1.0

        if result.confidence < 0.2:
            multiplier *= 0.3

        cluster = self.graph.get_cluster(technique_id)
        state_clusters = self._state_clusters(state)
        if cluster and state_clusters and cluster not in state_clusters:
            pass  # cross-cluster is good, no penalty
        elif not cluster:
            multiplier *= 0.8

        if result.impossible and not self._confirm_impossible(result):
            multiplier *= 0.3

        return PruneDecision(
            should_prune=False,
            confidence_multiplier=multiplier,
            reason="soft demotion" if multiplier < 1.0 else "",
        )

    def _confirm_impossible(self, result: WorkerResult) -> bool:
        """Only confirm impossibility if the worker's reason is definitive."""
        reason = result.impossible_reason.lower()
        definitive_markers = [
            "100%",
            "fundamentally impossible",
            "provably cannot",
            "type mismatch",
            "contradicts",
            "violates",
            "by gödel",
            "by abel",
            "by turing",
            "no such",
            "undefined",
        ]
        return any(marker in reason for marker in definitive_markers)

    def _check_impossibility_theorems(self, result: WorkerResult) -> str | None:
        """Check if the result's claim violates a known impossibility."""
        text = (
            result.new_state.description + " " + result.proof_sketch
        ).lower()
        for keyword, theorem_key in IMPOSSIBILITY_KEYWORDS.items():
            if keyword in text:
                return theorem_key
        return None

    def _check_contradiction(self, result: WorkerResult) -> bool:
        """Check if the result contradicts a known theorem."""
        text = result.proof_sketch.lower()
        contradiction_markers = [
            "this contradicts the fundamental theorem",
            "violates cantor",
            "impossible by gödel",
            "this would imply p = np",
            "contradicts the prime number theorem",
        ]
        return any(m in text for m in contradiction_markers)

    def _is_anti_pruned(self, technique_id: str, depth: int) -> bool:
        """Certain branches must never be pruned."""
        if depth < 3:
            return True

        cluster = self.graph.get_cluster(technique_id)
        cross_cluster_techniques = self.graph.bridge_techniques()
        if technique_id in cross_cluster_techniques:
            return True

        return False

    def _state_clusters(self, state: MathState) -> set[int]:
        """Infer which clusters the current state is associated with."""
        clusters: set[int] = set()
        for nid in state.graph_nodes_used + state.graph_nodes_produced:
            for tid in self.graph.techniques_from(nid):
                c = self.graph.get_cluster(tid)
                if c:
                    clusters.add(c)
        return clusters
