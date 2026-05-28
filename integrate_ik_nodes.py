#!/usr/bin/env python3
"""
Integrate Iwaniec-Kowalski new nodes and edges into the knowledge graph.

Steps:
1. Read knowledge_graph.json
2. Read iwaniec_kowalski_new_nodes.json
3. Skip duplicate node IDs
4. Create edges following bipartite rule (state/axiom/theorem <-> technique only)
5. Append new nodes and edges
6. Validate (no dup IDs, all edge endpoints exist)
7. Write updated graph
"""

import json
import sys
from pathlib import Path

KG_PATH = Path("knowledge_graph.json")
NEW_NODES_PATH = Path("knowledge_graph_workspace/iwaniec_kowalski_new_nodes.json")

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Written to {path}")

def main():
    # --- 1. Load ---
    print("Loading knowledge graph...")
    kg = load_json(KG_PATH)
    nodes = kg["nodes"]
    edges = kg["edges"]
    print(f"  Existing nodes: {len(nodes)}")
    print(f"  Existing edges: {len(edges)}")

    print("Loading new nodes...")
    new_nodes_raw = load_json(NEW_NODES_PATH)
    print(f"  New nodes in file: {len(new_nodes_raw)}")

    # --- 2. Build ID sets ---
    existing_ids = set(n["id"] for n in nodes)
    existing_edge_ids = set(e["id"] for e in edges)

    # --- 3. Deduplicate ---
    new_nodes = []
    skipped = []
    for n in new_nodes_raw:
        if n["id"] in existing_ids:
            skipped.append(n["id"])
        else:
            new_nodes.append(n)
    if skipped:
        print(f"  Skipped {len(skipped)} duplicate node IDs: {skipped}")
    else:
        print(f"  No duplicate node IDs found.")
    print(f"  Nodes to add: {len(new_nodes)}")

    # Add new nodes to the graph
    nodes.extend(new_nodes)
    # Rebuild the full ID set
    all_ids = set(n["id"] for n in nodes)
    # Build kind lookup
    kind_map = {n["id"]: n["kind"] for n in nodes}

    # --- 4. Determine next edge ID ---
    max_edge_num = 0
    for e in edges:
        eid = e["id"]
        if eid.startswith("e_"):
            try:
                num = int(eid[2:])
                if num > max_edge_num:
                    max_edge_num = num
            except ValueError:
                pass
    next_edge = max_edge_num + 1
    print(f"  Next edge ID: e_{next_edge}")

    # Helper to create edges
    new_edges = []

    def make_edge(from_id, to_id, role, used_in_theorem=""):
        nonlocal next_edge
        # Validate endpoints exist
        if from_id not in all_ids:
            print(f"  WARNING: from_id '{from_id}' not found, skipping edge")
            return
        if to_id not in all_ids:
            print(f"  WARNING: to_id '{to_id}' not found, skipping edge")
            return
        # Validate bipartite: one endpoint must be technique, the other must not be
        from_kind = kind_map[from_id]
        to_kind = kind_map[to_id]
        if role == "input":
            # input: state/axiom/theorem -> technique
            if to_kind != "technique":
                print(f"  WARNING: input edge to non-technique '{to_id}' (kind={to_kind}), skipping")
                return
            if from_kind == "technique":
                print(f"  WARNING: input edge from technique '{from_id}', skipping")
                return
        elif role == "output":
            # output: technique -> state/axiom/theorem
            if from_kind != "technique":
                print(f"  WARNING: output edge from non-technique '{from_id}' (kind={from_kind}), skipping")
                return
            if to_kind == "technique":
                print(f"  WARNING: output edge to technique '{to_id}', skipping")
                return

        eid = f"e_{next_edge:04d}" if next_edge < 10000 else f"e_{next_edge}"
        next_edge += 1
        new_edges.append({
            "id": eid,
            "from": from_id,
            "to": to_id,
            "role": role,
            "parameter_binding": {},
            "used_in_theorem": used_in_theorem
        })

    # --- 5. Create edges per specification ---
    print("\nCreating edges...")

    # t_selberg_delange_method
    make_edge("s_perron_formula", "t_selberg_delange_method", "input")
    make_edge("s_riemann_zeta_function", "t_selberg_delange_method", "input")
    make_edge("t_selberg_delange_method", "s_wirsing_theorem", "output")

    # t_heath_brown_identity
    make_edge("s_von_mangoldt_function", "t_heath_brown_identity", "input")
    make_edge("s_mobius_function", "t_heath_brown_identity", "input")
    make_edge("t_heath_brown_identity", "s_type_i_sum", "output")
    make_edge("t_heath_brown_identity", "s_type_ii_sum", "output")

    # t_linnik_identity
    make_edge("s_von_mangoldt_function", "t_linnik_identity", "input")
    make_edge("t_linnik_identity", "s_type_i_sum", "output")
    make_edge("t_linnik_identity", "s_type_ii_sum", "output")

    # t_vaughan_identity (existing technique)
    make_edge("t_vaughan_identity", "s_type_i_sum", "output")
    make_edge("t_vaughan_identity", "s_type_ii_sum", "output")

    # t_rosser_iwaniec_sieve
    make_edge("s_sifting_function", "t_rosser_iwaniec_sieve", "input")
    make_edge("s_sieve_dimension", "t_rosser_iwaniec_sieve", "input")
    make_edge("s_buchstab_identity", "t_rosser_iwaniec_sieve", "input")
    make_edge("t_rosser_iwaniec_sieve", "s_linear_sieve", "output")
    make_edge("t_rosser_iwaniec_sieve", "s_sieve_limit_functions", "output")

    # t_semilinear_sieve
    make_edge("s_sifting_function", "t_semilinear_sieve", "input")
    make_edge("s_sieve_dimension", "t_semilinear_sieve", "input")
    make_edge("t_semilinear_sieve", "s_friedlander_iwaniec_theorem", "output")

    # t_bombieri_asymptotic_sieve
    make_edge("s_level_of_distribution", "t_bombieri_asymptotic_sieve", "input")
    make_edge("s_bombieri_vinogradov", "t_bombieri_asymptotic_sieve", "input")
    make_edge("t_bombieri_asymptotic_sieve", "s_chen_theorem", "output")

    # t_asymptotic_sieve_for_primes
    make_edge("s_type_i_sum", "t_asymptotic_sieve_for_primes", "input")
    make_edge("s_type_ii_sum", "t_asymptotic_sieve_for_primes", "input")
    make_edge("s_level_of_distribution", "t_asymptotic_sieve_for_primes", "input")
    make_edge("s_parity_problem_sieve", "t_asymptotic_sieve_for_primes", "input")
    make_edge("t_asymptotic_sieve_for_primes", "s_friedlander_iwaniec_theorem", "output")

    # t_van_der_corput_a_process
    make_edge("s_exponential_sum", "t_van_der_corput_a_process", "input")
    make_edge("t_van_der_corput_a_process", "s_exponent_pair", "output")

    # t_van_der_corput_b_process
    make_edge("s_exponential_sum", "t_van_der_corput_b_process", "input")
    make_edge("t_van_der_corput_b_process", "s_exponent_pair", "output")

    # t_method_of_exponent_pairs
    make_edge("s_exponent_pair", "t_method_of_exponent_pairs", "input")
    make_edge("t_method_of_exponent_pairs", "s_exponent_pair", "output")

    # t_vinogradov_method_exponential_sums
    make_edge("s_vinogradov_mean_value_theorem", "t_vinogradov_method_exponential_sums", "input")
    make_edge("t_vinogradov_method_exponential_sums", "s_vinogradov_korobov_zero_free_region", "output")

    # t_stepanov_method
    make_edge("s_riemann_hypothesis_for_curves", "t_stepanov_method", "input")
    make_edge("t_stepanov_method", "s_bombieri_proof_rh_curves", "output")

    # t_square_sieve
    make_edge("s_large_sieve_inequality", "t_square_sieve", "input")
    make_edge("t_square_sieve", "s_friedlander_iwaniec_theorem", "output")

    # t_bombieri_iwaniec_method
    make_edge("s_large_sieve_inequality", "t_bombieri_iwaniec_method", "input")
    make_edge("s_exponent_pair", "t_bombieri_iwaniec_method", "input")
    make_edge("t_bombieri_iwaniec_method", "s_exponent_pair", "output")

    # t_deshouillers_iwaniec_method
    make_edge("s_kloosterman_sum", "t_deshouillers_iwaniec_method", "input")
    make_edge("s_kuznetsov_trace_formula", "t_deshouillers_iwaniec_method", "input")
    make_edge("t_deshouillers_iwaniec_method", "s_fouvry_theorem", "output")

    # t_linnik_dispersion_method
    make_edge("s_bombieri_vinogradov", "t_linnik_dispersion_method", "input")
    make_edge("t_linnik_dispersion_method", "s_fouvry_theorem", "output")

    # t_amplification_method
    make_edge("s_spectral_large_sieve", "t_amplification_method", "input")
    make_edge("s_l_function_of_modular_form", "t_amplification_method", "input")
    make_edge("t_amplification_method", "s_subconvexity_gl2", "output")

    # t_spectral_mean_value_estimates
    make_edge("s_kuznetsov_trace_formula", "t_spectral_mean_value_estimates", "input")
    make_edge("s_spectral_decomposition_l2_gamma_h", "t_spectral_mean_value_estimates", "input")
    make_edge("t_spectral_mean_value_estimates", "s_nonvanishing_l_functions_at_center", "output")
    make_edge("t_spectral_mean_value_estimates", "s_fourth_moment_zeta", "output")

    # t_rankin_selberg_method
    make_edge("s_real_analytic_eisenstein_series", "t_rankin_selberg_method", "input")
    make_edge("s_cusp_form", "t_rankin_selberg_method", "input")
    make_edge("s_petersson_inner_product", "t_rankin_selberg_method", "input")
    make_edge("t_rankin_selberg_method", "s_rankin_selberg_l_function", "output")

    # t_farey_dissection
    make_edge("s_exponential_sum", "t_farey_dissection", "input")
    make_edge("t_farey_dissection", "s_singular_integral_circle_method", "output")

    # t_kloosterman_refinement
    make_edge("s_kloosterman_sum", "t_kloosterman_refinement", "input")
    make_edge("t_kloosterman_refinement", "s_hardy_littlewood_asymptotic_waring", "output")

    # t_delta_method
    make_edge("s_kloosterman_sum", "t_delta_method", "input")
    make_edge("s_voronoi_summation_formula", "t_delta_method", "input")
    make_edge("t_delta_method", "s_shifted_convolution_sums", "output")

    # t_zero_detecting_polynomial
    make_edge("s_mean_value_theorem_dirichlet_polynomials", "t_zero_detecting_polynomial", "input")
    make_edge("t_zero_detecting_polynomial", "s_huxley_zero_density_estimate", "output")
    make_edge("t_zero_detecting_polynomial", "s_log_free_zero_density_estimate", "output")

    # t_turan_power_sum_method
    make_edge("s_riemann_zeta_function", "t_turan_power_sum_method", "input")
    make_edge("t_turan_power_sum_method", "s_deuring_heilbronn_repulsion", "output")

    # t_halasz_montgomery_method
    make_edge("s_halasz_montgomery_inequality", "t_halasz_montgomery_method", "input")
    make_edge("s_large_sieve_inequality", "t_halasz_montgomery_method", "input")
    make_edge("t_halasz_montgomery_method", "s_huxley_zero_density_estimate", "output")

    # t_mollifier_method
    make_edge("s_approximate_functional_equation", "t_mollifier_method", "input")
    make_edge("s_mean_value_theorem_dirichlet_polynomials", "t_mollifier_method", "input")
    make_edge("t_mollifier_method", "s_nonvanishing_l_functions_at_center", "output")

    # t_levinson_method
    make_edge("s_approximate_functional_equation", "t_levinson_method", "input")
    make_edge("s_riemann_zeta_function", "t_levinson_method", "input")
    # output: proportion of zeros on critical line
    make_edge("t_levinson_method", "s_proportion_zeros_critical_line", "output")

    # t_half_dimensional_sieve
    make_edge("s_sifting_function", "t_half_dimensional_sieve", "input")
    make_edge("s_sieve_dimension", "t_half_dimensional_sieve", "input")
    make_edge("t_half_dimensional_sieve", "s_friedlander_iwaniec_theorem", "output")

    # t_switching_principle_sieve
    make_edge("s_buchstab_identity", "t_switching_principle_sieve", "input")
    make_edge("t_switching_principle_sieve", "s_chen_theorem", "output")

    # t_dyadic_decomposition - general purpose, no specific edges per spec
    # t_smooth_partition_of_unity - general purpose, no specific edges per spec

    # t_circle_method (existing)
    make_edge("t_circle_method", "s_hardy_littlewood_asymptotic_waring", "output")
    make_edge("t_circle_method", "s_singular_integral_circle_method", "output")

    # t_selberg_sieve (existing)
    make_edge("t_selberg_sieve", "s_sieve_limit_functions", "output")

    # --- Theorem input edges via intermediate techniques ---
    # These need a technique intermediary per the bipartite rule.
    # We create "conceptual" technique nodes only where necessary,
    # or wire through existing techniques.

    # s_spectral_decomposition_l2_gamma_h uses: s_maass_cusp_form,
    #   s_real_analytic_eisenstein_series, s_continuous_spectrum_gamma_h,
    #   s_discrete_spectrum_gamma_h
    # These are components of the spectral decomposition.
    # The spectral decomposition is a theorem built from its constituent parts.
    # We need a technique to mediate. Use t_spectral_mean_value_estimates as a
    # related technique, but that doesn't semantically fit. Better: these are
    # definitional components. We can wire: each component -> technique that
    # produces the decomposition. But there's no explicit technique for "proving
    # the spectral decomposition". We'll skip technique->theorem edges that
    # don't have a natural technique intermediary, as the spec says
    # "state/axiom/theorem <-> technique only".
    #
    # Actually, re-reading the spec more carefully: "Also create some key input
    # edges for theorems" followed by specific wiring instructions. Let me
    # interpret these as creating edges that route through techniques where
    # possible, or skip where no technique exists.

    # s_convexity_bound_l_functions uses: s_completed_l_function -> technique -> s_convexity_bound_l_functions
    # No explicit technique named. We could use a generic "Phragmen-Lindelof" technique.
    # Since no technique node exists for this, skip per spec guidance.

    # s_petersson_trace_formula uses: s_poincare_series_modular, s_petersson_inner_product, s_kloosterman_sum
    # These are ingredients. The Petersson trace formula is derived by unfolding
    # Poincare series inner products. No explicit technique node for "unfolding".
    # Skip direct wiring.

    # s_kuznetsov_trace_formula uses: s_maass_cusp_form, s_kloosterman_sum
    # Same issue - no technique intermediary. Skip.

    # s_atkin_lehner_theory uses: s_petersson_inner_product, s_cusp_form, s_oldform
    # No technique intermediary. Skip.

    # s_duke_equidistribution uses: s_subconvexity_gl2
    # Route through t_amplification_method which is the technique producing subconvexity
    # But duke_equidistribution is produced FROM subconvexity, not from the amplification technique directly.
    # Actually, the paradigm is: subconvexity -> implies equidistribution.
    # We can't make state->state edges. So we need a technique.
    # The natural technique is the "subconvexity implies equidistribution" paradigm,
    # but s_subconvexity_implies_equidistribution is a theorem, not a technique.
    # Skip this edge.

    print(f"\n  New edges created: {len(new_edges)}")

    # --- 6. Append edges ---
    edges.extend(new_edges)

    # --- 7. Validate ---
    print("\nValidating...")
    all_node_ids = set(n["id"] for n in nodes)
    all_edge_ids = set()
    errors = 0

    # Check duplicate node IDs
    seen_node_ids = set()
    for n in nodes:
        if n["id"] in seen_node_ids:
            print(f"  ERROR: Duplicate node ID '{n['id']}'")
            errors += 1
        seen_node_ids.add(n["id"])

    # Check duplicate edge IDs and endpoint validity
    for e in edges:
        if e["id"] in all_edge_ids:
            print(f"  ERROR: Duplicate edge ID '{e['id']}'")
            errors += 1
        all_edge_ids.add(e["id"])

        if e["from"] not in all_node_ids:
            print(f"  ERROR: Edge {e['id']} from '{e['from']}' - node not found")
            errors += 1
        if e["to"] not in all_node_ids:
            print(f"  ERROR: Edge {e['id']} to '{e['to']}' - node not found")
            errors += 1

    # Validate bipartite rule on new edges
    for e in new_edges:
        from_kind = kind_map.get(e["from"])
        to_kind = kind_map.get(e["to"])
        if from_kind and to_kind:
            is_bipartite = (from_kind == "technique") != (to_kind == "technique")
            if not is_bipartite:
                print(f"  ERROR: Edge {e['id']} violates bipartite rule: {e['from']}({from_kind}) -> {e['to']}({to_kind})")
                errors += 1

    if errors:
        print(f"\n  VALIDATION FAILED with {errors} errors!")
        sys.exit(1)
    else:
        print("  Validation passed!")

    # --- 8. Final counts ---
    print(f"\nFinal counts:")
    print(f"  Nodes: {len(nodes)} (was {len(nodes) - len(new_nodes)}, added {len(new_nodes)})")
    print(f"  Edges: {len(edges)} (was {len(edges) - len(new_edges)}, added {len(new_edges)})")

    # --- 9. Write ---
    print("\nWriting updated graph...")
    kg["nodes"] = nodes
    kg["edges"] = edges

    # Update metadata
    kg["metadata"]["iwaniec_kowalski_integration"] = {
        "date": "2026-05-28",
        "new_node_count": len(new_nodes),
        "new_edge_count": len(new_edges),
        "source": "iwaniec_kowalski_new_nodes.json"
    }

    save_json(KG_PATH, kg)
    print("\nDone!")

if __name__ == "__main__":
    main()
