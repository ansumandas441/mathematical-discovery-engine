"""
Knowledge graph database layer.

Loads knowledge_graph.json into a NetworkX directed graph and provides
query methods for the orchestrator: neighborhood search, technique lookup,
path finding, and bridge-technique identification.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import networkx as nx

CLUSTER_MAP = {
    "t_spot_pattern_in_table": 1,
    "t_verify_on_special_cases": 1,
    "t_complete_the_square": 2,
    "t_reduce_to_canonical_form": 2,
    "t_compose_with_identity": 2,
    "t_symmetry_reduction": 3,
    "t_conserved_quantity": 3,
    "t_duality": 3,
    "t_character_decomposition_count": 3,
    "t_double_centralizer_decompose": 3,
    "t_koszul_dual_operad_swap": 3,
    "t_exhaustion_squeeze": 4,
    "t_interpolate_and_continue": 4,
    "t_frequency_decomposition": 4,
    "t_dyadic_decomposition": 4,
    "t_fourier_transform": 4,
    "t_svd_and_spectral_decomposition": 4,
    "t_axiomatize_from_instances": 5,
    "t_structural_isomorphism": 5,
    "t_ultraproduct_transfer": 5,
    "t_raise_dimension": 6,
    "t_obstruction_class": 6,
    "t_compactness_argument": 6,
    "t_deformation_cohomology": 6,
    "t_rescale_for_asymptotic_geometry": 6,
    "t_diagonalize": 7,
    "t_arithmetize_syntax": 7,
    "t_force_independence": 7,
    "t_contraction_fixed_point": 8,
    "t_infinite_descent": 8,
    "t_flow_with_surgery": 8,
    "t_mountain_pass_minimax": 8,
    "t_nash_moser_fast_newton": 8,
    "t_physics_to_pde": 9,
    "t_complex_analysis_to_integers": 9,
    "t_analysis_algebra_topology_bridge": 9,
    "t_major_minor_arc_decomposition": 9,
    "t_ergodic_correspondence": 9,
    "t_finite_case_check": 10,
    "t_formal_verify": 10,
    "t_distributed_collaboration": 10,
    "t_probabilistic_existence": 11,
    "t_pigeonhole_collision": 11,
    "t_polynomial_method": 11,
    "t_sieve_by_optimized_quadratic": 11,
    "t_shearer_entropy_count": 11,
    "t_group_complete_exact_category": 12,
    "t_sheafify_on_grothendieck_topology": 12,
    "t_representable_functor_trick": 12,
    "t_sheaf_cohomology_bridge": 12,
    "t_k_theoretic_index_bridge": 12,
    "t_spectral_sequence_compute": 12,
    "t_diagram_chase": 12,
}

COMPOSITE_TECHNIQUES = {
    "t_selberg_sieve_method",
    "t_circle_method",
    "t_furstenberg_correspondence_principle",
    "t_galois_correspondence",
    "t_ricci_flow_with_surgery",
    "t_wiles_modularity",
    "t_godel_numbering",
    "t_atiyah_singer_index_machinery",
    "t_category_theoretic_colimits_and_adjoints",
}

META_TECHNIQUES = {
    "t_auxiliary_construction",
    "t_conjecture_refinement",
    "t_reductio_ad_absurdum",
    "t_projection_to_subspace",
    "t_heights_and_galois_rep_bridge",
    "t_level_lowering_bridge",
    "t_transference_bridge",
}


class KnowledgeGraph:
    """Wrapper around the knowledge graph with query helpers."""

    def __init__(self, json_path: str | Path | None = None):
        if json_path is None:
            json_path = Path(__file__).resolve().parent.parent / "knowledge_graph.json"
        self.json_path = Path(json_path)
        self._raw: dict = {}
        self.G = nx.DiGraph()
        self.nodes: dict[str, dict] = {}
        self.edges: list[dict] = []
        self.techniques: dict[str, dict] = {}
        self._load()

    def _load(self):
        with open(self.json_path) as f:
            self._raw = json.load(f)

        raw_nodes = self._raw.get("nodes", [])
        self.edges = self._raw.get("edges", [])

        for n in raw_nodes:
            nid = n["id"]
            self.nodes[nid] = n
            self.G.add_node(nid, **n)
            if n.get("kind") == "technique":
                self.techniques[nid] = n

        for e in self.edges:
            self.G.add_edge(
                e["from"],
                e["to"],
                id=e.get("id"),
                role=e.get("role"),
                used_in_theorem=e.get("used_in_theorem"),
                parameter_binding=e.get("parameter_binding", {}),
            )

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def neighborhood(self, node_ids: list[str], radius: int = 2) -> dict[str, dict]:
        """Return all nodes within *radius* undirected hops of *node_ids*."""
        valid_ids = [nid for nid in node_ids if nid in self.G]
        if not valid_ids:
            return {}
        visited: set[str] = set(valid_ids)
        frontier: set[str] = set(valid_ids)
        for _ in range(radius):
            next_frontier: set[str] = set()
            for nid in frontier:
                if nid not in self.G:
                    continue
                for nbr in set(self.G.successors(nid)) | set(self.G.predecessors(nid)):
                    if nbr not in visited:
                        visited.add(nbr)
                        next_frontier.add(nbr)
            frontier = next_frontier
        return {nid: self.nodes[nid] for nid in visited if nid in self.nodes}

    def techniques_from(self, node_id: str) -> list[str]:
        """Return technique IDs reachable in one hop from *node_id*."""
        if node_id not in self.G:
            return []
        out: list[str] = []
        for nbr in self.G.successors(node_id):
            if nbr in self.techniques:
                out.append(nbr)
        for nbr in self.G.predecessors(node_id):
            if nbr in self.techniques:
                out.append(nbr)
        return list(set(out))

    def technique_neighbors(self, technique_id: str) -> dict[str, list[dict]]:
        """Return inputs and outputs of a technique (nodes connected to it)."""
        inputs = []
        outputs = []
        for e in self.edges:
            if e["to"] == technique_id:
                node = self.nodes.get(e["from"])
                if node:
                    inputs.append(node)
            elif e["from"] == technique_id:
                node = self.nodes.get(e["to"])
                if node:
                    outputs.append(node)
        return {"inputs": inputs, "outputs": outputs}

    def shortest_path(self, source: str, target: str) -> list[str] | None:
        """Shortest undirected path between two nodes, or None."""
        ug = self.G.to_undirected()
        try:
            return nx.shortest_path(ug, source, target)
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return None

    def graph_distance(self, source: str, target: str) -> int:
        """Undirected shortest-path length, or 999 if unreachable."""
        path = self.shortest_path(source, target)
        return len(path) - 1 if path else 999

    def get_cluster(self, technique_id: str) -> int:
        """Return cluster number for a technique, 0 if unknown."""
        return CLUSTER_MAP.get(technique_id, 0)

    def bridge_techniques(self) -> list[str]:
        """Techniques whose neighbors span multiple clusters."""
        bridges = []
        for tid in self.techniques:
            nbrs = self.technique_neighbors(tid)
            all_nbrs = nbrs["inputs"] + nbrs["outputs"]
            clusters_touched: set[int] = set()
            for n in all_nbrs:
                for t2 in self.techniques_from(n["id"]):
                    c = self.get_cluster(t2)
                    if c:
                        clusters_touched.add(c)
            if len(clusters_touched) >= 3:
                bridges.append(tid)
        return bridges

    def search_nodes(self, keywords: list[str], max_results: int = 20) -> list[dict]:
        """Search nodes by keyword in name or description."""
        results = []
        for n in self.nodes.values():
            text = (n.get("name", "") + " " + str(n.get("description", ""))).lower()
            if any(kw.lower() in text for kw in keywords):
                results.append(n)
                if len(results) >= max_results:
                    break
        return results

    def proof_chain(self, theorem_id: str) -> list[dict]:
        """Return the ordered edges for a specific theorem's proof chain."""
        chain = [e for e in self.edges if e.get("used_in_theorem") == theorem_id]
        return sorted(chain, key=lambda e: e.get("id", ""))

    def stats(self) -> dict:
        counts = {"axiom": 0, "state": 0, "theorem": 0, "technique": 0}
        for n in self.nodes.values():
            k = n.get("kind", "?")
            counts[k] = counts.get(k, 0) + 1
        return {
            "nodes": len(self.nodes),
            "edges": len(self.edges),
            "techniques": len(self.techniques),
            **counts,
        }
