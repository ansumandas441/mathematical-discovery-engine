#!/usr/bin/env python3
"""Integrate Quanta Magazine (Mathematics, 2019-2023) missing nodes/edges into the knowledge graph."""
import json, shutil, sys

GRAPH = "knowledge_graph.json"
BACKUP = "knowledge_graph.json.pre_quanta.bak"

new_nodes = [
    # --- THEOREMS ---
    {"id": "s_hedetniemi_disproof", "kind": "theorem", "name": "Hedetniemi's conjecture disproof (Shitov)",
     "type_signature": "", "aliases": ["Shitov counterexample to Hedetniemi's conjecture"],
     "description": "There exist finite graphs G, H with chi(G x H) < min(chi(G), chi(H)), refuting Hedetniemi's conjecture that the chromatic number of a categorical graph product equals the minimum of its factors' chromatic numbers (Shitov, 2019)."},
    {"id": "s_conway_knot_not_slice", "kind": "theorem", "name": "Conway knot is not slice (Piccirillo)",
     "type_signature": "", "aliases": ["Piccirillo theorem on the Conway knot"],
     "description": "The Conway knot is not smoothly slice (bounds no smooth disk in the 4-ball) although it is topologically slice, proved via a knot trace whose Rasmussen invariant is nonzero (Piccirillo, 2020)."},
    {"id": "s_keller_graph", "kind": "state", "name": "Keller graph",
     "type_signature": "", "aliases": ["Keller graph G_{n,s}"],
     "description": "The graph on labelings in {0,...,2s-1}^n encoding faulty cube tilings, in which a clique of size 2^n corresponds to a face-free tiling of n-space by unit cubes."},
    {"id": "s_keller_conjecture_resolution", "kind": "theorem", "name": "Keller's conjecture in dimension seven",
     "type_signature": "", "aliases": ["resolution of Keller's conjecture"],
     "description": "Every tiling of seven-dimensional space by translated unit cubes contains two cubes sharing a complete codimension-one face, completing Keller's conjecture in all dimensions (Brakensiek-Heule-Mackey-Narvaez, 2020)."},
    {"id": "s_metric_tsp_below_three_halves", "kind": "theorem", "name": "Metric TSP approximation below 3/2",
     "type_signature": "", "aliases": ["beating Christofides for metric TSP"],
     "description": "A randomized algorithm approximates the metric traveling-salesperson problem within a factor 3/2 - epsilon for a fixed epsilon > 0, the first improvement over Christofides' bound (Karlin-Klein-Oveis Gharan, 2020)."},
    {"id": "s_sum_three_cubes_42", "kind": "theorem", "name": "42 as a sum of three cubes",
     "type_signature": "", "aliases": ["sum of three cubes for 42 and 33"],
     "description": "Every integer below 1000 not congruent to +-4 (mod 9), including 42 and 33, is expressible as a sum of three integer cubes, established by large-scale distributed computation (Booker-Sutherland, 2019)."},
    {"id": "s_peluse_polynomial_progressions", "kind": "theorem", "name": "Polynomial progressions in dense sets (Peluse)",
     "type_signature": "", "aliases": ["Peluse polynomial Szemeredi bounds"],
     "description": "Subsets of {1,...,N} of non-vanishing density contain a nontrivial polynomial progression x, x+P_1(y), ..., x+P_m(y) for polynomials of distinct degrees with zero constant term, with effective bounds (Peluse, 2019-2020)."},
    {"id": "s_eigenvector_eigenvalue_identity", "kind": "theorem", "name": "Eigenvector-eigenvalue identity",
     "type_signature": "", "aliases": ["eigenvalue-eigenvector identity", "Denton-Parke-Tao-Zhang identity"],
     "description": "For a Hermitian matrix the squared modulus of each eigenvector component equals a ratio of characteristic polynomials of the matrix and its principal minor, |v_{i,j}|^2 prod_{k!=i}(lambda_i - lambda_k) = prod_k(lambda_i - mu_k) (Denton-Parke-Tao-Zhang, 2019)."},
    {"id": "s_van_der_waerden_galois_conjecture", "kind": "theorem", "name": "Van der Waerden conjecture on Galois groups (Bhargava)",
     "type_signature": "", "aliases": ["van der Waerden conjecture for Galois groups"],
     "description": "The number of monic degree-n integer polynomials with coefficients bounded by H whose Galois group is a proper subgroup of S_n is O(H^{n-1}), so almost all such polynomials have Galois group S_n (Bhargava, 2021/2023)."},
    {"id": "s_erdos_graham_egyptian_conjecture", "kind": "theorem", "name": "Erdos-Graham conjecture on unit fractions (Bloom)",
     "type_signature": "", "aliases": ["Erdos-Graham unit-fraction conjecture"],
     "description": "Every set of integers of positive upper density contains a finite subset whose reciprocals sum to exactly 1, confirming the Erdos-Graham conjecture (Bloom, 2021)."},
    {"id": "s_negative_pell_density", "kind": "theorem", "name": "Density of solvable negative Pell equations (Stevenhagen conjecture)",
     "type_signature": "", "aliases": ["Stevenhagen conjecture", "Koymans-Pagano negative Pell theorem"],
     "description": "The proportion of squarefree d for which the negative Pell equation x^2 - d y^2 = -1 is solvable equals the explicit Stevenhagen constant (about 0.5805 among admissible d), proved by Koymans-Pagano (2022)."},
    {"id": "s_carmichael_short_intervals", "kind": "theorem", "name": "Carmichael numbers in short intervals (Larsen)",
     "type_signature": "", "aliases": ["bounded gaps between Carmichael numbers"],
     "description": "For all large x the interval [x, x + x^{0.7}] contains a Carmichael number, giving the first nontrivial upper bound on gaps between consecutive Carmichael numbers (Larsen, 2022)."},
    {"id": "s_patterson_cubic_gauss_sums", "kind": "theorem", "name": "Patterson conjecture on cubic Gauss sums",
     "type_signature": "", "aliases": ["Kummer-Patterson conjecture (cubic case)"],
     "description": "Cubic Gauss sums summed over primes have a secondary main term of size about p^{5/6} with the bias predicted by Patterson, confirming the cubic case of the Kummer-Patterson conjecture (David-Dunn-Radziwill, 2022)."},
    {"id": "s_brill_noether_interpolation", "kind": "theorem", "name": "Interpolation for Brill-Noether curves (Larson-Vogt)",
     "type_signature": "", "aliases": ["Brill-Noether interpolation problem"],
     "description": "A general Brill-Noether curve of degree d and genus g in projective r-space passes through n general points precisely when an explicit numerical inequality holds, resolving the interpolation problem for such curves (Larson-Vogt, 2022)."},
    {"id": "s_measurable_circle_squaring", "kind": "theorem", "name": "Measurable Tarski circle-squaring (Mathe-Noel-Pikhurko)",
     "type_signature": "", "aliases": ["Borel circle squaring"],
     "description": "A disk and a square of equal area are equidecomposable into finitely many Lebesgue-measurable pieces using only translations, with pieces taken Borel and bounded by Jordan curves, strengthening Tarski's circle-squaring (Mathe-Noel-Pikhurko, 2022)."},
    {"id": "s_multi_bubble_isoperimetry", "kind": "theorem", "name": "Multi-bubble isoperimetric theorem (Milman-Neeman)",
     "type_signature": "", "aliases": ["triple bubble theorem", "multi-bubble conjecture"],
     "description": "The least-perimeter partition of n-dimensional Euclidean or Gaussian space into q+1 prescribed volumes is the standard symmetric multi-bubble cluster for q <= 5 (Milman-Neeman, 2022)."},
    {"id": "s_euler_3d_finite_time_blowup", "kind": "theorem", "name": "Finite-time blowup for 3D Euler (Chen-Hou)",
     "type_signature": "", "aliases": ["Chen-Hou Euler singularity"],
     "description": "Smooth finite-energy solutions of the 3D incompressible Euler equations in a cylindrical domain can develop a self-similar finite-time singularity from smooth initial data, established by a computer-assisted stability proof (Chen-Hou, 2022)."},
    {"id": "s_sticky_kakeya_three_dim", "kind": "theorem", "name": "Sticky Kakeya conjecture in three dimensions (Wang-Zahl)",
     "type_signature": "", "aliases": ["sticky Kakeya theorem"],
     "description": "Every sticky Kakeya set in three-dimensional space has full Hausdorff dimension 3, resolving the sticky special case of the 3D Kakeya conjecture (Wang-Zahl, 2022)."},
    {"id": "s_low_surface_area_foams", "kind": "theorem", "name": "Low-surface-area foams (spherical cubes)",
     "type_signature": "", "aliases": ["spherical cubes", "foam problem"],
     "description": "Euclidean d-space admits a partition into unit-volume cells whose average surface area is O(sqrt(d)), far below the linear-in-d surface area of cubic cells (Kindler-O'Donnell-Rao-Wigderson; Naor-Regev)."},
    {"id": "s_kaplansky_unit_conjecture_disproof", "kind": "theorem", "name": "Disproof of Kaplansky's unit conjecture (Gardam)",
     "type_signature": "", "aliases": ["Gardam counterexample to the unit conjecture"],
     "description": "There is a torsion-free group and a field whose group algebra contains a nontrivial unit, refuting Kaplansky's unit conjecture (Gardam, 2021)."},
    {"id": "s_tikhomirov_singularity_probability", "kind": "theorem", "name": "Singularity probability of random sign matrices (Tikhomirov)",
     "type_signature": "", "aliases": ["singularity probability of Bernoulli matrices"],
     "description": "An n-by-n matrix with independent uniform +-1 entries is singular with probability (1/2 + o(1))^n, matching the conjectured leading-order rate (Tikhomirov, 2020)."},
    {"id": "s_higher_dimensional_black_hole_topologies", "kind": "theorem", "name": "Infinitely many black-hole horizon topologies in higher dimensions",
     "type_signature": "", "aliases": ["black lens / black ring families"],
     "description": "In spacetime dimension five and higher the stationary vacuum Einstein equations admit black-hole horizons of infinitely many distinct topologies, unlike the unique spherical horizon in four dimensions (Khuri-Rainone and collaborators, 2023)."},
    {"id": "s_resolvent_degree_bounds", "kind": "theorem", "name": "Resolvent-degree bounds for Hilbert's 13th problem",
     "type_signature": "", "aliases": ["resolvent degree", "Hilbert 13th problem bounds"],
     "description": "The roots of the general degree-n polynomial can be expressed through algebraic functions of fewer variables than classical bounds for several n (e.g. degree 9 in four variables), sharpening Hilbert's 13th problem via resolvent degree (Farb-Wolfson; Sundaram, 2020-2021)."},
    {"id": "s_bourgain_slicing_resolution", "kind": "theorem", "name": "Resolution of Bourgain's slicing problem (Klartag-Lehec)",
     "type_signature": "", "aliases": ["hyperplane conjecture", "isotropic constant bound", "Bourgain slicing problem"],
     "description": "The isotropic constant of every convex body in n-space is bounded above by a universal constant, resolving Bourgain's slicing (hyperplane) problem via stochastic localization following the near-resolution of the KLS conjecture (Klartag-Lehec, 2022-2023; Chen, 2021)."},
    {"id": "s_bubeck_sellke_robustness_law", "kind": "theorem", "name": "Universal law for robust interpolation (Bubeck-Sellke)",
     "type_signature": "", "aliases": ["overparametrization for robustness"],
     "description": "Smoothly (Lipschitz) interpolating n data points in d dimensions requires about n*d parameters, a universal law explaining why robust neural networks must be far larger than the data they fit (Bubeck-Sellke, 2021)."},
    # --- STATES ---
    {"id": "s_matrix_multiplication_exponent", "kind": "state", "name": "Matrix multiplication exponent omega",
     "type_signature": "", "aliases": ["omega", "exponent of matrix multiplication"],
     "description": "The exponent omega, the infimum of tau such that two n-by-n matrices can be multiplied in O(n^tau) arithmetic operations, satisfying 2 <= omega < 2.372 via the laser method and its refinements."},
    {"id": "s_aperiodic_monotile_hat", "kind": "state", "name": "Aperiodic monotile 'the hat'",
     "type_signature": "", "aliases": ["the hat", "einstein tile", "spectre monotile"],
     "description": "A single 13-sided polygon (an aperiodic monotile or 'einstein') that tiles the plane only non-periodically, together with its chiral reflection-free relative the 'spectre' (Smith-Myers-Kaplan-Goodman-Strauss, 2023)."},
    {"id": "s_relative_langlands_duality", "kind": "state", "name": "Relative Langlands duality (Ben-Zvi-Sakellaridis-Venkatesh)",
     "type_signature": "", "aliases": ["relative Langlands program", "BZSV duality"],
     "description": "A conjectural duality organizing automorphic periods and L-functions into dual pairs of Hamiltonian G-spaces, extending the Langlands program with structures inspired by mirror symmetry and electric-magnetic duality (Ben-Zvi-Sakellaridis-Venkatesh, 2023)."},
    {"id": "s_symplectic_ellipsoid_infinite_staircase", "kind": "state", "name": "Infinite staircase of symplectic ellipsoid embeddings",
     "type_signature": "", "aliases": ["Fibonacci staircase", "symplectic infinite staircase"],
     "description": "The function describing when a symplectic ellipsoid embeds into a one-parameter family of targets exhibits an infinite Fibonacci-related staircase of sharp obstructions detected by embedded contact homology capacities (McDuff-Magill-Weiler, 2022)."},
    # --- AXIOM ---
    {"id": "s_homotopy_type_theory", "kind": "axiom", "name": "Univalent foundations / homotopy type theory",
     "type_signature": "", "aliases": ["univalent foundations", "HoTT"],
     "description": "A foundation of mathematics in which types are interpreted as homotopy types (infinity-groupoids) and propositional equality as paths, governed by Voevodsky's univalence axiom identifying equivalent types."},
    # --- TECHNIQUE ---
    {"id": "t_sat_solver_proof", "kind": "technique", "name": "SAT-solver / exhaustive certificate proof",
     "cluster": "01_experimental_and_numerical",
     "function_signature": "(Finite combinatorial conjecture) -> (Resolved instance with machine-checkable certificate)",
     "parameters": ["encoding", "solver"], "has_subgraph": False, "toolbox_ref": "",
     "description": "Encode a finite combinatorial statement as a Boolean satisfiability instance and resolve it via a SAT solver or exhaustive search, yielding a machine-checkable certificate."},
]

new_edges_spec = [
    ("s_kls_conjecture", "t_stochastic_localization_eldan", "input", "s_bourgain_slicing_resolution"),
    ("t_stochastic_localization_eldan", "s_bourgain_slicing_resolution", "output", "s_bourgain_slicing_resolution"),
    ("s_keller_graph", "t_sat_solver_proof", "input", "s_keller_conjecture_resolution"),
    ("t_sat_solver_proof", "s_keller_conjecture_resolution", "output", "s_keller_conjecture_resolution"),
    ("s_hadwiger_nelson_problem", "t_sat_solver_proof", "input", "s_de_grey_chromatic_plane_bound"),
    ("t_sat_solver_proof", "s_de_grey_chromatic_plane_bound", "output", "s_de_grey_chromatic_plane_bound"),
    ("s_group_ring", "t_sat_solver_proof", "input", "s_kaplansky_unit_conjecture_disproof"),
    ("t_sat_solver_proof", "s_kaplansky_unit_conjecture_disproof", "output", "s_kaplansky_unit_conjecture_disproof"),
    ("t_self_similar_imploding_profile", "s_euler_3d_finite_time_blowup", "output", "s_euler_3d_finite_time_blowup"),
]

def main():
    with open(GRAPH) as f:
        d = json.load(f)
    nodes, edges = d["nodes"], d["edges"]
    existing_ids = {n.get("id") for n in nodes}

    # max numeric edge id
    mx = 0
    for e in edges:
        eid = e.get("id", "")
        if isinstance(eid, str) and eid.startswith("e_"):
            try: mx = max(mx, int(eid.split("_")[1]))
            except ValueError: pass
    print("current max edge id:", mx, "| nodes:", len(nodes), "| edges:", len(edges))

    # validate + append nodes
    added_nodes = 0
    for n in new_nodes:
        if n["id"] in existing_ids:
            print("SKIP existing node:", n["id"]); continue
        nodes.append(n); existing_ids.add(n["id"]); added_nodes += 1

    # build edges, validating endpoints
    added_edges = 0
    nid = mx + 1
    for frm, to, role, thm in new_edges_spec:
        if frm not in existing_ids:
            print("ERROR missing edge endpoint:", frm); sys.exit(1)
        if to not in existing_ids:
            print("ERROR missing edge endpoint:", to); sys.exit(1)
        edges.append({"id": f"e_{nid:04d}", "from": frm, "to": to, "role": role,
                      "parameter_binding": {}, "used_in_theorem": thm})
        nid += 1; added_edges += 1

    # validate JSON + uniqueness
    ids = [n.get("id") for n in nodes]
    assert len(ids) == len(set(ids)), "duplicate node ids!"
    eids = [e.get("id") for e in edges]
    assert len(eids) == len(set(eids)), "duplicate edge ids!"

    shutil.copyfile(GRAPH, BACKUP)
    with open(GRAPH, "w") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

    from collections import Counter
    kinds = Counter(n["kind"] for n in new_nodes if n["id"] in existing_ids)
    print(f"ADDED nodes: {added_nodes}  edges: {added_edges}")
    print("by kind:", dict(Counter(n["kind"] for n in new_nodes)))
    print("graph totals -> nodes:", len(nodes), "edges:", len(edges))

if __name__ == "__main__":
    main()
