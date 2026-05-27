#!/usr/bin/env python3
"""
Round 0 cleanup:
  1. Apply Ch. 11 §6 corrections (splits, merges, new nodes) to knowledge_graph.json.
  2. Categorize & patch orphan nodes (Type A autofix, Type B flag, Type C audit).
  3. Emit canonical state/technique id index for Phase A mathematicians.
  4. Verify integrity checks.
"""
import json, re, sys, pathlib
from collections import defaultdict, Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "knowledge_graph.json"
WS = ROOT / "knowledge_graph_workspace_iter2"

def load():
    return json.loads(JSON_PATH.read_text())

def save(d):
    JSON_PATH.write_text(json.dumps(d, indent=2, ensure_ascii=False))

def add_node(d, node):
    if any(n["id"] == node["id"] for n in d["nodes"]):
        return False
    d["nodes"].append(node)
    return True

def find_node(d, nid):
    for n in d["nodes"]:
        if n["id"] == nid:
            return n
    return None

# ---- Step 1: new technique nodes from philosopher's review ----

NEW_TECHNIQUE_NODES = [
    {
        "id": "t_auxiliary_construction",
        "kind": "technique",
        "name": "Auxiliary construction",
        "cluster": "C2",
        "function_signature": "(states, goal) → (states + helper_object)",
        "parameters": ["helper_kind", "construction_rule"],
        "description": "Introduce a helper object whose structure forces the desired conclusion. Distinct from reduce-to-canonical-form (which simplifies) because this ADDS structure.",
        "toolbox_ref": "10_toolbox.md#C2",
        "has_subgraph": False,
        "examples_note": "Ptolemy's point K; Brouwer retraction; Frey curve; Archimedes' auxiliary triangles."
    },
    {
        "id": "t_conjecture_refinement",
        "kind": "technique",
        "name": "Conjecture refinement",
        "cluster": "C1",
        "function_signature": "(rough_conjecture, counterexamples) → (refined_conjecture)",
        "parameters": ["refinement_kind"],
        "description": "Modify a conjecture to exclude known failure modes or add missing preconditions. Distinct from verify-on-special-cases — that tests, this refines.",
        "toolbox_ref": "10_toolbox.md#C1",
        "has_subgraph": False,
        "examples_note": "Legendre's refinement of Gauss's PNT conjecture; Kepler's third law via successive refinement on Tycho's data."
    },
    {
        "id": "t_reductio_ad_absurdum",
        "kind": "technique",
        "name": "Reductio ad absurdum",
        "cluster": "C7",
        "function_signature": "(proposition P) → (proof of ¬P via assuming P and deriving contradiction)",
        "parameters": ["contradiction_target"],
        "description": "Assume the statement's negation; derive a contradiction; conclude. Distinct from infinite descent (which is number-theoretic minimal-counterexample).",
        "toolbox_ref": "10_toolbox.md#C7",
        "has_subgraph": False,
        "examples_note": "Cantor uncountability; Gödel incompleteness contradiction step; Turing halting; Brouwer no-retraction."
    },
    {
        "id": "t_projection_to_subspace",
        "kind": "technique",
        "name": "Projection to subspace",
        "cluster": "C6",
        "function_signature": "(ambient_space, subspace) → (image_in_subspace)",
        "parameters": ["ambient_dim", "target_dim", "projection_kind"],
        "description": "Map from a higher-dimensional space to a lower-dimensional subspace along a specified direction. Inverse / cousin of t_raise_dimension.",
        "toolbox_ref": "10_toolbox.md#C6",
        "has_subgraph": False,
        "examples_note": "Desargues step 3 (3D → 2D back-projection); Radon transform; Plücker embedding back-projection."
    },
    {
        "id": "t_svd_and_spectral_decomposition",
        "kind": "technique",
        "name": "SVD / spectral decomposition",
        "cluster": "C2",
        "function_signature": "(linear_map T : V → W) → (singular_spectrum, orthogonal_bases)",
        "parameters": ["base_field", "axis", "truncation_rank"],
        "description": "Decompose a linear map via orthogonal diagonalization of T*T. Specialization of reduce-to-canonical-form; inherits orthogonal-projection substep from frequency-decomposition.",
        "toolbox_ref": "10_toolbox.md#C2",
        "has_subgraph": True,
        "subgraph_ref": "sg_svd",
        "inherits": ["t_reduce_to_canonical_form", "t_frequency_decomposition"],
        "examples_note": "Perron–Frobenius; PCA; spectral graph theory; Eckart–Young truncation; Koopman operator."
    },
    # Five specializations of the split t_analysis_algebra_topology_bridge:
    {
        "id": "t_sheaf_cohomology_bridge",
        "kind": "technique",
        "name": "Sheaf cohomology bridge",
        "cluster": "C12",
        "function_signature": "(divisor/sheaf) → (cohomology classes H^i)",
        "parameters": ["ambient_scheme", "coefficient_ring"],
        "description": "Specialization of the analysis-algebra-topology bridge: compute H^i(X, F) and extract Euler characteristic or related invariants.",
        "toolbox_ref": "10_toolbox.md#C12",
        "parent_bridge": "t_analysis_algebra_topology_bridge",
        "examples_note": "Riemann–Roch; Serre duality; Grothendieck–Riemann–Roch."
    },
    {
        "id": "t_k_theoretic_index_bridge",
        "kind": "technique",
        "name": "K-theoretic index bridge",
        "cluster": "C12",
        "function_signature": "(elliptic_operator) → (index class in K-theory)",
        "parameters": ["manifold_dim", "symbol_type"],
        "description": "Lift an elliptic operator to a K-theory class and recover the analytic index via pushforward.",
        "toolbox_ref": "10_toolbox.md#C12",
        "parent_bridge": "t_analysis_algebra_topology_bridge",
        "examples_note": "Atiyah–Singer index theorem; families index theorem."
    },
    {
        "id": "t_heights_and_galois_rep_bridge",
        "kind": "technique",
        "name": "Heights / Galois representation bridge",
        "cluster": "C9",
        "function_signature": "(abelian_variety or elliptic curve) → (Galois rep + height data)",
        "parameters": ["number_field", "prime"],
        "description": "Bridge Diophantine geometry to Galois theory via ell-adic representations and canonical heights.",
        "toolbox_ref": "10_toolbox.md#C9",
        "parent_bridge": "t_analysis_algebra_topology_bridge",
        "examples_note": "Mordell–Faltings; Mazur's bound; Neron–Tate heights."
    },
    {
        "id": "t_level_lowering_bridge",
        "kind": "technique",
        "name": "Level-lowering bridge (Ribet)",
        "cluster": "C9",
        "function_signature": "(mod-l Galois rep at level N) → (rep at level N/p)",
        "parameters": ["level_N", "prime_l"],
        "description": "Given a Galois rep coming from a modular form at level N with extra congruence, show it comes from level N/p.",
        "toolbox_ref": "10_toolbox.md#C9",
        "parent_bridge": "t_analysis_algebra_topology_bridge",
        "examples_note": "Ribet's theorem; epsilon conjecture; key step in Wiles' FLT."
    },
    {
        "id": "t_transference_bridge",
        "kind": "technique",
        "name": "Transference bridge",
        "cluster": "C9",
        "function_signature": "(dense subset of pseudorandom majorant) → (inherited structural result)",
        "parameters": ["majorant_type", "density_notion"],
        "description": "Transfer a structural theorem (e.g., Szemerédi) from dense integers to a pseudorandom sparse subset via relative-density machinery.",
        "toolbox_ref": "10_toolbox.md#C9",
        "parent_bridge": "t_analysis_algebra_topology_bridge",
        "examples_note": "Green–Tao APs in primes; Conlon–Fox–Zhao sparse pseudorandomness."
    }
]

def apply_new_nodes(d):
    added = []
    for n in NEW_TECHNIQUE_NODES:
        if add_node(d, n):
            added.append(n["id"])
    return added

# ---- Step 2: mark t_distributed_collaboration as meta-technique ----

def apply_metadata_corrections(d):
    updates = []
    meta = find_node(d, "t_distributed_collaboration")
    if meta and not meta.get("meta_technique"):
        meta["meta_technique"] = True
        updates.append("t_distributed_collaboration -> meta_technique: true")

    # single_use_landmark flags per philosopher §2.4
    SINGLE_USE = [
        "t_complex_analysis_to_integers",
        "t_sheafify_on_grothendieck_topology",
        "t_group_complete_exact_category",
        "t_rescale_for_asymptotic_geometry",
        "t_ultraproduct_transfer",
        "t_probabilistic_existence",
        "t_category_theoretic_colimits_and_adjoints",
        "t_polynomial_method",
        "t_schur_weyl_and_double_centralizer",
        "t_deformation_cohomology"
    ]
    for nid in SINGLE_USE:
        n = find_node(d, nid)
        if n and not n.get("single_use_landmark"):
            n["single_use_landmark"] = True
            updates.append(f"{nid} -> single_use_landmark: true")

    # unmark provisional on SVD (it's now a full technique)
    svd = find_node(d, "t_svd_and_spectral_decomposition")
    if svd and svd.get("provisional"):
        del svd["provisional"]
        updates.append("t_svd_and_spectral_decomposition -> no longer provisional")

    # is-a links
    ISA = [
        ("s_galois_group", "s_finite_group"),
        ("s_compact_oriented_surface_without_boundary", "s_compact_smooth_manifold"),
    ]
    for child, parent in ISA:
        n = find_node(d, child)
        if n and n.get("is_specialization_of") != parent:
            n["is_specialization_of"] = parent
            updates.append(f"{child} is_specialization_of {parent}")

    return updates

# ---- Step 3: deduplicate s_prime_numbers / s_primes_in_naturals ----

def apply_dedup(d):
    updates = []
    # canonical: s_prime_numbers is marked as alias of s_primes_in_naturals in graph_theorist's JSON.
    # Keep s_primes_in_naturals as canonical, remove s_prime_numbers, remap any edges.
    alias_map = {
        "s_prime_numbers": "s_primes_in_naturals",
        "s_euclidean_solid_geometry": "s_euclidean_3_space",
        "s_real_line": "s_real_numbers",
    }
    # Remap edges
    remapped = 0
    for e in d["edges"]:
        if e["from"] in alias_map:
            e["from"] = alias_map[e["from"]]; remapped += 1
        if e["to"] in alias_map:
            e["to"] = alias_map[e["to"]]; remapped += 1
        if e.get("used_in_theorem") in alias_map:
            e["used_in_theorem"] = alias_map[e["used_in_theorem"]]
    # Remove alias nodes (but preserve alias list in canonical)
    for alias_id, canon_id in alias_map.items():
        canon = find_node(d, canon_id)
        if canon:
            aliases = set(canon.get("aliases", []))
            aliases.add(alias_id)
            canon["aliases"] = sorted(aliases)
        # Remove alias node from list
        d["nodes"] = [n for n in d["nodes"] if n["id"] != alias_id]
        updates.append(f"Dedup: merged {alias_id} -> {canon_id} ({remapped} edges remapped total)")
    return updates

# ---- Step 4: orphan audit ----

def orphan_audit(d):
    adj = defaultdict(set)
    for e in d["edges"]:
        adj[e["from"]].add(e["to"]); adj[e["to"]].add(e["from"])
    orphans = [n for n in d["nodes"] if not adj[n["id"]]]
    return orphans, adj

# Type B: umbrella technique nodes with a subgraph — their action lives inside, not at top.
# Mark them with subgraph_host: true so the viewer can filter them out gracefully.
TYPE_B_UMBRELLAS = {
    "t_atiyah_singer_index_machinery",
    "t_fourier_transform",
    "t_galois_correspondence",
    "t_ricci_flow_with_surgery",
    "t_wiles_modularity",
    "t_godel_numbering",
    "t_selberg_sieve_method",
    "t_circle_method",
    "t_furstenberg_correspondence_principle",
    "t_category_theoretic_colimits_and_adjoints",
    "t_perelman_entropy_package",
    "t_deformation_and_R_equals_T",
    "t_schur_weyl_and_double_centralizer"
}

# Type A: orphan axioms used implicitly in chains. For a minimal fix, add a
# single "uses_axiom" edge to a representative theorem that cites them in its
# chain text. This is a stub — Phase A mathematicians may add richer edges.
TYPE_A_FIXES = {
    # axiom_id -> (technique_id, theorem_id) to wire via
    "s_polygon_area_formula": ("t_exhaustion_squeeze", "s_area_of_circle"),
    "s_euler_lemma": ("t_infinite_descent", "s_fundamental_theorem_of_arithmetic"),
    "s_mean_value_theorem": ("t_compose_with_identity", "s_fundamental_theorem_of_calculus"),
    "s_isosceles_triangle_base_angles_equal": ("t_compose_with_identity", "s_thales_theorem"),
    "s_similar_triangle_criterion": ("t_compose_with_identity", "s_ptolemys_theorem"),
    "s_area_additivity": ("t_compose_with_identity", "s_pythagorean_theorem"),
    "s_circle_definition": ("t_symmetry_reduction", "s_area_of_circle"),
    "s_euler_four_square_identity": ("t_compose_with_identity", "s_lagrange_four_squares"),
    "s_prime_pair_p_q": ("t_character_decomposition_count", "s_quadratic_reciprocity"),
    "s_unit_circle_in_C": ("t_frequency_decomposition", "s_de_moivre_formula"),
    "s_convex_polyhedron": ("t_reduce_to_canonical_form", "s_euler_polyhedron_formula"),
    "s_topological_sphere_S2": ("t_conserved_quantity", "s_euler_polyhedron_formula"),
    "s_sine_function": ("t_frequency_decomposition", "s_basel_identity"),
    "s_analytic_exponential_series": ("t_interpolate_and_continue", "s_euler_formula"),
    "s_first_fundamental_form": ("t_physics_to_pde", "s_theorema_egregium"),
    "s_projective_plane": ("t_raise_dimension", "s_desargues_theorem"),
    "s_projective_space_axioms": ("t_raise_dimension", "s_desargues_theorem"),
    "s_holomorphic_function_on_domain": ("t_conserved_quantity", "s_cauchy_integral_theorem"),
    "s_simply_connected_proper_domain_in_C": ("t_interpolate_and_continue", "s_riemann_mapping_theorem"),
    "s_coprime_pair": ("t_reduce_to_canonical_form", "s_chinese_remainder_theorem"),
    "s_pell_equation_x2_minus_N_y2": ("t_infinite_descent", "s_solvability_of_pell_equation"),
    "s_graph_definition": ("t_axiomatize_from_instances", "s_eulerian_path_criterion"),
    "s_prime_p": ("t_symmetry_reduction", "s_fermat_little_theorem"),
    "s_prime_p_equiv_1_mod_4": ("t_compose_with_identity", "s_fermat_two_squares"),
    "s_continuous_function_on_interval": ("t_exhaustion_squeeze", "s_fundamental_theorem_of_calculus"),
    "s_first_order_peano_arithmetic": ("t_arithmetize_syntax", "s_godel_incompleteness"),
    "s_turing_machine_model": ("t_diagonalize", "s_halting_theorem"),
    "s_probability_axioms": ("t_frequency_decomposition", "s_central_limit_theorem"),
    "s_newtonian_inverse_square_force": ("t_physics_to_pde", "s_kepler_three_laws"),
    "s_conic_sections": ("t_physics_to_pde", "s_kepler_three_laws"),
    "s_zfc_axioms": ("t_force_independence", "s_cohen_independence_of_CH"),
    "s_iid_sequence_finite_variance": ("t_frequency_decomposition", "s_central_limit_theorem"),
    "s_product_topology": ("t_ultraproduct_transfer", "s_tychonoff_theorem"),
    "s_family_of_compact_spaces": ("t_ultraproduct_transfer", "s_tychonoff_theorem"),
    "s_sublinear_functional_p": ("t_compactness_argument", "s_hahn_banach_theorem"),
    "s_linear_functional_on_subspace": ("t_compactness_argument", "s_hahn_banach_theorem"),
    "s_complete_metric_space": ("t_contraction_fixed_point", "s_banach_fixed_point"),
    "s_strict_contraction": ("t_contraction_fixed_point", "s_banach_fixed_point"),
    "s_closed_ball_D_n": ("t_obstruction_class", "s_brouwer_fixed_point"),
    "s_continuous_self_map": ("t_obstruction_class", "s_brouwer_fixed_point"),
    "s_differential_form": ("t_duality", "s_stokes_theorem"),
    "s_divisor_on_curve": ("t_sheafify_on_grothendieck_topology", "s_riemann_roch"),
    "s_real_analysis": ("t_frequency_decomposition", "s_basel_identity"),
    "s_prime_power_divisor_p_n": ("t_symmetry_reduction", "s_sylow_theorems"),
    "s_lie_group": ("t_conserved_quantity", "s_noether_theorem"),
    "s_lagrangian_action_integral": ("t_conserved_quantity", "s_noether_theorem"),
    "s_noetherian_ring_R": ("t_axiomatize_from_instances", "s_hilbert_basis_theorem"),
    "s_divisibility_definition": ("t_axiomatize_from_instances", "s_fundamental_theorem_of_arithmetic"),
    "s_group_action": ("t_symmetry_reduction", "s_sylow_theorems"),
    "s_real_vector_space": ("t_axiomatize_from_instances", "s_hahn_banach_theorem"),
    "s_polynomial_ring_over_Q": ("t_reduce_to_canonical_form", "s_abel_ruffini"),
    "s_field_extension_L_over_K": ("t_axiomatize_from_instances", "s_fundamental_theorem_of_galois_theory"),
    "s_radical_extension_tower": ("t_obstruction_class", "s_abel_ruffini"),
    "s_smooth_function": ("t_interpolate_and_continue", "s_taylor_theorem"),
}

def apply_type_a_fixes(d):
    """Wire orphan axioms through an existing technique to a theorem."""
    updates = []
    existing_ids = {n["id"] for n in d["nodes"]}
    next_edge_num = max((int(re.search(r"\d+", e.get("id", "e_0000")).group())
                        for e in d["edges"] if e.get("id", "").startswith("e_")), default=0) + 1

    for axiom_id, (tech_id, thm_id) in TYPE_A_FIXES.items():
        if axiom_id not in existing_ids: continue
        if tech_id not in existing_ids: continue
        if thm_id not in existing_ids: continue
        # Only add if not already present
        exists = any(e["from"] == axiom_id and e["to"] == tech_id for e in d["edges"])
        if exists: continue
        d["edges"].append({
            "id": f"e_{next_edge_num:04d}",
            "from": axiom_id,
            "to": tech_id,
            "role": "input",
            "parameter_binding": {"source": "round0_autofix"},
            "used_in_theorem": thm_id
        })
        next_edge_num += 1
        updates.append(f"wired {axiom_id} -> {tech_id} -> ({thm_id})")
    return updates

def apply_type_b_flags(d):
    """Mark umbrella technique nodes so viewer can handle them."""
    updates = []
    for tid in TYPE_B_UMBRELLAS:
        n = find_node(d, tid)
        if n and not n.get("subgraph_host"):
            n["subgraph_host"] = True
            updates.append(f"{tid} -> subgraph_host: true")
    return updates

# ---- Step 5: emit canonical index for mathematicians ----

def emit_canonical_index(d):
    techs = sorted([n for n in d["nodes"] if n["kind"] == "technique"], key=lambda n: n["id"])
    states = sorted([n for n in d["nodes"] if n["kind"] in ("axiom", "state")], key=lambda n: n["id"])
    theorems = sorted([n for n in d["nodes"] if n["kind"] == "theorem"], key=lambda n: n["id"])

    out = []
    out.append("# Canonical Node Index (after Round 0)\n")
    out.append("**Phase A mathematicians: use these ids exactly. Do not re-invent new ids for nodes that already exist.**\n")
    out.append("## Existing theorem nodes — DO NOT re-derive these (they're already in the graph)\n")
    for n in theorems:
        aliases = f" (aliases: {', '.join(n.get('aliases', []))})" if n.get('aliases') else ""
        out.append(f"- `{n['id']}` — {n['name']}{aliases}")
    out.append("\n## Existing technique nodes — reuse these ids verbatim\n")
    for n in techs:
        note = []
        if n.get("meta_technique"): note.append("meta")
        if n.get("single_use_landmark"): note.append("single-use")
        if n.get("subgraph_host"): note.append("umbrella")
        flag = f" [{', '.join(note)}]" if note else ""
        out.append(f"- `{n['id']}` ({n.get('cluster','?')}) — {n['name']}{flag}")
    out.append("\n## Existing axiom/state nodes — reuse when possible\n")
    for n in states:
        aliases = f" (aliases: {', '.join(n.get('aliases', []))})" if n.get('aliases') else ""
        out.append(f"- `{n['id']}` — {n['name']}{aliases}")
    (WS / "canonical_node_index.md").write_text("\n".join(out))
    return len(techs), len(states), len(theorems)

# ---- Step 6: integrity checks ----

def integrity_checks(d):
    report = []
    # Every theorem has incoming edge
    theorems = [n["id"] for n in d["nodes"] if n["kind"] == "theorem"]
    incoming = defaultdict(list)
    for e in d["edges"]: incoming[e["to"]].append(e)
    missing = [t for t in theorems if t not in incoming]
    report.append(f"Theorems without incoming edge: {len(missing)}")
    if missing: report.append(f"  → {missing[:5]}")

    # Duplicate type_signatures (non-aliased)
    by_sig = defaultdict(list)
    for n in d["nodes"]:
        if n["kind"] in ("axiom", "state") and n.get("type_signature"):
            by_sig[n["type_signature"]].append(n["id"])
    dupes = {k: v for k, v in by_sig.items() if len(v) > 1}
    # filter out declared-alias sets
    true_dupes = 0
    for sig, ids in dupes.items():
        alias_set = set()
        for nid in ids:
            n = find_node(d, nid)
            alias_set |= set(n.get("aliases", []))
        if not all(other in alias_set | {ids[0]} for other in ids[1:]):
            true_dupes += 1
    report.append(f"Unresolved duplicate type_signatures: {true_dupes}")

    # Orphan count
    adj = defaultdict(set)
    for e in d["edges"]: adj[e["from"]].add(e["to"]); adj[e["to"]].add(e["from"])
    orphans = [n for n in d["nodes"] if not adj[n["id"]]]
    flagged_orphans = [n for n in orphans if n.get("subgraph_host")]
    unflagged_orphans = [n for n in orphans if not n.get("subgraph_host")]
    report.append(f"Orphans total: {len(orphans)} ({len(flagged_orphans)} flagged as subgraph_host, {len(unflagged_orphans)} unflagged)")
    if unflagged_orphans:
        report.append(f"  → unflagged sample: {[n['id'] for n in unflagged_orphans[:10]]}")

    return report, len(unflagged_orphans)

# ---- Main ----

def main():
    d = load()
    log = []

    log.append("# Round 0 Cleanup — Execution Log\n")
    log.append(f"Baseline: {len(d['nodes'])} nodes, {len(d['edges'])} edges.\n")

    added = apply_new_nodes(d)
    log.append(f"## Step 1 — New technique nodes\nAdded {len(added)}:")
    for a in added: log.append(f"  - `{a}`")
    log.append("")

    meta_updates = apply_metadata_corrections(d)
    log.append(f"## Step 2 — Metadata corrections\n({len(meta_updates)} updates)")
    for u in meta_updates: log.append(f"  - {u}")
    log.append("")

    dedup_updates = apply_dedup(d)
    log.append(f"## Step 3 — Deduplication ({len(dedup_updates)} merges)")
    for u in dedup_updates: log.append(f"  - {u}")
    log.append("")

    # Orphan audit BEFORE fixes
    orphans_before, _ = orphan_audit(d)
    log.append(f"## Step 4 — Orphan audit\nOrphans before fix: {len(orphans_before)}")

    type_a_updates = apply_type_a_fixes(d)
    log.append(f"\nApplied {len(type_a_updates)} Type-A fixes (axiom → technique → theorem wire-ups):")
    for u in type_a_updates[:20]: log.append(f"  - {u}")
    if len(type_a_updates) > 20:
        log.append(f"  - (+ {len(type_a_updates)-20} more)")

    type_b_updates = apply_type_b_flags(d)
    log.append(f"\nApplied {len(type_b_updates)} Type-B umbrella flags:")
    for u in type_b_updates: log.append(f"  - {u}")

    orphans_after, _ = orphan_audit(d)
    log.append(f"\nOrphans after fix: {len(orphans_after)}")
    log.append(f"Remaining (not Type-A/B autofixable): {[n['id'] for n in orphans_after if not n.get('subgraph_host')][:15]}")
    log.append("")

    nt, ns, nth = emit_canonical_index(d)
    log.append(f"## Step 5 — Canonical index emitted\n{nt} techniques, {ns} axiom+state, {nth} theorem ids written to `canonical_node_index.md`\n")

    checks, unflagged_orphans = integrity_checks(d)
    log.append("## Step 6 — Integrity checks\n")
    for c in checks: log.append(c)
    log.append("")

    log.append(f"## Final\nNodes: {len(d['nodes'])} (was 352). Edges: {len(d['edges'])} (was 343).\n")
    log.append("Round 0 gate: "
               + ("PASS" if unflagged_orphans <= 10 else "RETRY")
               + f" (unflagged orphans = {unflagged_orphans}).\n")

    (WS / "round0_cleanup.md").write_text("\n".join(log))
    save(d)
    print("\n".join(log))

if __name__ == "__main__":
    main()
