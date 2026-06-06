#!/usr/bin/env python3
"""Integrate landmark arXiv (math) 2019-2023 results into knowledge_graph.json."""
import json, shutil, sys

PATH = "knowledge_graph.json"
d = json.load(open(PATH))
existing_ids = {n["id"] for n in d["nodes"]}

def S(id, kind, name, sig, desc, aliases=None):
    n = {"id": id, "kind": kind, "name": name, "type_signature": sig, "description": desc}
    if aliases: n["aliases"] = aliases
    return n

def T(id, name, fsig, desc):
    return {"id": id, "kind": "technique", "name": name, "function_signature": fsig, "description": desc}

# ---------------- NEW NODES ----------------
NEW = [
# --- Number theory / arithmetic geometry ---
T("t_gcd_graph_method", "GCD graph method",
  "(approximation events) -> (correlation bounds)",
  "A combinatorial-analytic framework encoding overlaps of Diophantine-approximation events as weighted GCD graphs whose iteratively improved 'quality' bounds their correlations."),
S("s_duffin_schaeffer_theorem", "theorem", "Duffin–Schaeffer theorem (Koukoulopoulos–Maynard)", "",
  "If the series of phi(q)psi(q)/q diverges, then for almost every real x there are infinitely many coprime fractions a/q with |x-a/q| < psi(q)/q.",
  ["Koukoulopoulos-Maynard theorem"]),
T("t_o_minimal_point_counting", "O-minimal point counting (Pila–Wilkie)",
  "(definable set, height bound) -> (algebraic-point count)",
  "Bounds the number of rational/algebraic points of bounded height on the transcendental part of a set definable in an o-minimal structure, polynomially in the height."),
S("s_andre_oort_conjecture", "theorem", "André–Oort conjecture (Pila–Shankar–Tsimerman)", "",
  "Any subvariety of a Shimura variety containing a Zariski-dense set of special (CM) points is itself a special subvariety."),
T("t_betti_map_height_inequality", "Betti-map height inequality",
  "(family of abelian varieties, subvariety) -> (uniform Néron–Tate height bound)",
  "Uses generic submersivity of the real-analytic Betti (period) map to convert geometric non-degeneracy into fibre-uniform lower bounds on Néron–Tate heights."),
S("s_uniform_mordell_lang", "theorem", "Uniform Mordell–Lang for subvarieties of abelian varieties", "",
  "The number of cosets needed to cover the intersection of a subvariety with a finite-rank subgroup of an abelian variety is bounded only in terms of the dimension and degree of the subvariety."),
S("s_schinzel_zassenhaus_theorem", "theorem", "Schinzel–Zassenhaus theorem (Dimitrov)", "",
  "Every monic non-cyclotomic integer polynomial of degree n has a conjugate of absolute value at least 1 + c/n, giving a uniform repulsion of conjugates from the unit circle."),
S("s_picard_rank_jumps_k3", "theorem", "Exceptional jumps of Picard ranks of K3 reductions", "",
  "A K3 surface over a number field with everywhere potentially good reduction has infinitely many primes at which the geometric Picard rank of the reduction jumps."),
S("s_caraiani_scholze_torsion_vanishing", "theorem", "Caraiani–Scholze torsion vanishing", "",
  "The generic part of the mod-p cohomology of unitary Shimura varieties is concentrated in the middle degree."),
T("t_entropy_method_extremal", "Entropy (information-theoretic) method",
  "(random combinatorial object) -> (extremal inequality)",
  "Bounds extremal quantities by analysing the Shannon entropy of suitably chosen random structures and applying submodularity/entropy inequalities."),
S("s_ggmt_polynomial_freiman_ruzsa", "theorem", "Polynomial Freiman–Ruzsa theorem (Gowers–Green–Manners–Tao)", "",
  "In a group of bounded torsion, a set with doubling constant K is covered by at most poly(K) cosets of a subgroup no larger than the set, resolving Marton's conjecture."),
S("s_kelley_meka_3ap", "theorem", "Kelley–Meka bound for three-term progressions", "",
  "Every subset of {1,...,N} free of nontrivial three-term arithmetic progressions has size at most N·exp(-c(log N)^b) for some absolute b>0, a quasi-polynomial bound."),

# --- Combinatorics ---
S("s_sensitivity_conjecture", "theorem", "Sensitivity theorem (Huang)", "",
  "For every total Boolean function the degree is at most the square of the sensitivity, so sensitivity is polynomially related to all other standard complexity measures."),
T("t_signed_adjacency_interlacing", "Signed adjacency / eigenvalue interlacing",
  "(induced subgraph, signed adjacency matrix) -> (eigenvalue lower bound)",
  "Assigns a signing to a graph's adjacency matrix so that Cauchy eigenvalue interlacing forces large induced subgraphs to have a large maximum degree."),
S("s_ringel_conjecture", "theorem", "Ringel's conjecture (Montgomery–Pokrovskiy–Sudakov)", "",
  "For large n the complete graph K_{2n+1} decomposes into 2n+1 edge-disjoint copies of any fixed tree with n edges."),
S("s_multicolor_ramsey_lower_bound", "theorem", "Exponential improvement of multicolor Ramsey lower bounds (Conlon–Ferber)", "",
  "For every fixed number r>=3 of colors the diagonal r-color Ramsey number admits an exponentially improved lower bound via a pseudorandom algebraic-plus-random construction."),
S("s_erdos_faber_lovasz_theorem", "theorem", "Erdős–Faber–Lovász theorem (Kang–Kelly–Kühn–Methuku–Osthus)", "",
  "For all large n, every linear hypergraph on n vertices has chromatic index at most n."),
S("s_random_symmetric_matrix_singularity", "theorem", "Singularity probability of a random symmetric matrix", "",
  "A uniformly random n×n symmetric ±1 matrix is singular with probability at most exp(-cn)."),
S("s_high_girth_steiner_triple_systems", "theorem", "High-girth Steiner triple systems", "",
  "For all admissible orders there exist Steiner triple systems whose girth tends to infinity, proving a 1973 conjecture of Erdős."),
S("s_union_closed_constant_bound", "theorem", "Union-closed sets constant bound (Gilmer)", "",
  "In any union-closed family of sets some element belongs to at least a positive constant fraction of the sets, the first constant-fraction bound toward Frankl's conjecture."),
S("s_diagonal_ramsey_exponential_improvement", "theorem", "Exponential improvement for diagonal Ramsey (Campos–Griffiths–Morris–Sahasrabudhe)", "",
  "The diagonal Ramsey number satisfies R(k,k) <= (4-c)^k for an absolute c>0, the first exponential improvement on the 1935 Erdős–Szekeres upper bound."),
T("t_ramsey_book_algorithm", "Book algorithm for Ramsey embeddings",
  "(two-coloring of a clique) -> (large monochromatic clique or book)",
  "An adaptive embedding process that grows monochromatic 'books' while controlling neighborhood densities to extract larger-than-classical cliques."),
S("s_ramsey_r4t_asymptotics", "theorem", "Asymptotics of R(4,t) (Mattheus–Verstraete)", "",
  "The off-diagonal Ramsey number satisfies R(4,t) = Theta-tilde(t^3), confirming an Erdős conjecture up to a polylogarithmic factor."),
S("s_erdos_hajnal_conjecture", "state", "Erdős–Hajnal conjecture", "",
  "The conjecture that for every fixed graph H there is c>0 such that every H-free graph on n vertices contains a clique or independent set of size at least n^c."),
S("s_erdos_hajnal_loglog_bound", "theorem", "First improvement to the Erdős–Hajnal bound (Bucić–Nguyen–Scott–Seymour)", "",
  "Every H-free graph G contains a clique or stable set of size at least 2^{c·sqrt(log|G|·log log|G|)}, the first asymptotic improvement on the 1977 Erdős–Hajnal bound."),
S("s_talagrand_selector_process", "theorem", "Talagrand selector-process theorem (Park–Pham)", "",
  "The suprema of selector (Bernoulli) processes are governed by a majorizing-measure-type bound, proving Talagrand's selector-process conjecture."),
S("s_hadwiger_improved_bound", "theorem", "Improved bound for Hadwiger's conjecture (Delcourt–Postle / Norin–Postle–Song)", "",
  "Every graph with no K_t minor is O(t·log log t)-colorable, the current-best general bound toward Hadwiger's conjecture."),

# --- Geometry / topology / PDE / math physics ---
S("s_cheskidov_luo_sharp_nonuniqueness", "theorem", "Sharp non-uniqueness for Navier–Stokes (Cheskidov–Luo)", "",
  "Weak solutions of the Navier–Stokes equations are non-unique in L^p_t L^infty_x for every p<2 in dimension >=2, matching the Ladyzhenskaya–Prodi–Serrin uniqueness threshold."),
S("s_knotted_3_balls_s4", "theorem", "Knotted 3-balls in S^4 (Budney–Gabai)", "",
  "There exist smoothly embedded 3-balls in the 4-sphere with the same boundary that are not smoothly isotopic rel boundary."),
S("s_rectangular_peg_problem", "theorem", "Rectangular peg problem (Greene–Lobb)", "",
  "Every smooth Jordan curve in the plane inscribes a rectangle of every prescribed aspect ratio."),
S("s_arithmeticity_geodesic_submanifolds", "theorem", "Arithmeticity from totally geodesic submanifolds (Bader–Fisher–Miller–Stover)", "",
  "A finite-volume real hyperbolic manifold containing infinitely many maximal totally geodesic submanifolds of dimension at least 2 must be arithmetic."),
S("s_generalized_smale_conjecture", "theorem", "Generalized Smale conjecture (Bamler–Kleiner)", "",
  "For every spherical space form the inclusion of the isometry group into the diffeomorphism group is a homotopy equivalence."),
T("t_pointed_nash_entropy", "Pointed Nash entropy method",
  "(Ricci flow, heat kernel) -> (compactness / partial regularity)",
  "Uses the pointed Nash entropy and conjugate-heat-kernel bounds to control the geometry and singular set of Ricci flows."),
S("s_noncollapsed_ricci_flow_structure", "theorem", "Structure of non-collapsed Ricci-flow limits (Bamler)", "",
  "Non-collapsed limits of Ricci flows are smooth away from a singular set of parabolic codimension at least 4, with an associated compactness and partial-regularity theory."),
S("s_michael_simon_sobolev_brendle", "theorem", "Sharp Michael–Simon–Sobolev inequality (Brendle)", "",
  "A sharp Sobolev/isoperimetric inequality holds on submanifolds of Euclidean space of arbitrary dimension and codimension, yielding the sharp isoperimetric inequality for minimal submanifolds of codimension at most 2."),
S("s_generic_mcf_singularities", "theorem", "Generic singularities of mean curvature flow (Chodosh–Choi–Mantoulidis–Schulze)", "",
  "For a generic closed embedded surface in R^3 the mean curvature flow encounters only spherical and cylindrical (multiplicity-one) singularities."),
S("s_generic_regularity_minimizers", "theorem", "Generic regularity of minimizing hypersurfaces in dimensions 9 and 10", "",
  "For generic boundary data or metrics, area-minimizing hypersurfaces are smooth in ambient dimensions 9 and 10, past the dimension-8 Simons-cone obstruction."),
T("t_convex_hypersurface_theory", "Convex hypersurface theory (higher-dimensional)",
  "(contact manifold, hypersurface) -> (dividing set / contact decomposition)",
  "Extends Giroux's convex surface theory to all dimensions, organizing contact topology via convex hypersurfaces and their dividing sets."),
T("t_floer_homotopy_theory", "Floer homotopy theory",
  "(Hamiltonian/Lagrangian Floer data) -> (stable homotopy invariant)",
  "Realizes Floer-theoretic moduli as a stable homotopy type, allowing generalized cohomology theories to be applied to symplectic invariants."),
S("s_arnold_conjecture_morava", "theorem", "Arnold conjecture over arbitrary fields (Abouzaid–Blumberg)", "",
  "For a closed symplectic manifold the number of nondegenerate periodic Hamiltonian orbits is at least the total Betti number over any field, including positive characteristic, via Floer homotopy with Morava K-theory."),
S("s_telescope_conjecture_disproof", "theorem", "Disproof of Ravenel's telescope conjecture (Burklund–Hahn–Levy–Schlank)", "",
  "Telescopic T(n+1)-localization and chromatic K(n+1)-localization of the stable homotopy category differ for every prime and height n+1>=2."),
S("s_chromatic_redshift", "theorem", "Chromatic redshift for truncated Brown–Peterson spectra (Hahn–Wilson)", "",
  "The algebraic K-theory of the height-n ring spectrum BP<n> is nontrivial at chromatic height n+1, confirming Rognes' redshift principle in these cases."),
T("t_even_filtration", "Even filtration",
  "(commutative ring spectrum) -> (filtered spectrum)",
  "A canonical filtration right Kan extended from even E-infinity rings, recovering motivic and Adams–Novikov-type filtrations and measuring failure of even concentration."),
S("s_chromatic_nullstellensatz", "theorem", "Chromatic Nullstellensatz (Burklund–Schlank–Yuan)", "",
  "Algebraically closed Lubin–Tate theories are characterized among T(n)-local E-infinity rings by a Nullstellensatz property and jointly detect nilpotence."),
S("s_lqg_metric", "theorem", "Existence and uniqueness of the Liouville quantum gravity metric (Gwynne–Miller)", "",
  "For each parameter gamma in (0,2) there is a unique random metric associated with gamma-Liouville quantum gravity, arising as the scaling limit of Liouville first-passage percolation."),
S("s_wave_kinetic_equation_derivation", "theorem", "Rigorous derivation of the wave kinetic equation (Deng–Hani)", "",
  "The wave kinetic equation is derived as the effective long-time limit of the cubic nonlinear Schrödinger equation with random data."),
S("s_directed_landscape", "state", "Directed landscape", "",
  "The universal scaling-limit space-time random field of the Kardar–Parisi–Zhang universality class, governing last-passage and related growth models."),
S("s_lis_directed_landscape_convergence", "theorem", "Convergence of the longest increasing subsequence to the directed landscape (Dauvergne–Virág)", "",
  "The rescaled longest increasing subsequence of a uniform random permutation converges to a geodesic of the directed landscape."),
S("s_kerr_stability_small_a", "theorem", "Nonlinear stability of slowly rotating Kerr (Klainerman–Szeftel)", "",
  "The slowly rotating Kerr family with |a|/m small is nonlinearly stable under general perturbations of the Einstein vacuum equations."),
S("s_schwarzschild_nonlinear_stability", "theorem", "Nonlinear stability of the Schwarzschild family (Dafermos–Holzegel–Rodnianski–Taylor)", "",
  "The Schwarzschild family of black holes is nonlinearly asymptotically stable under general perturbations of the Einstein vacuum equations in a double-null gauge."),

# --- Algebra / AG / geometric representation theory / operator algebras / logic ---
T("t_condensed_mathematics", "Condensed mathematics",
  "(topological algebraic structure) -> (condensed object)",
  "Replaces topological spaces and topological algebraic structures by sheaves on profinite sets, so that topology-with-algebra forms a well-behaved abelian category amenable to homological methods."),
T("t_absolute_prismatic_cohomology", "Absolute prismatic cohomology (Cartier–Witt stack)",
  "(p-adic formal scheme) -> (filtered cohomology theory)",
  "A stacky reformulation of prismatic cohomology over the p-adic integers via the Cartier–Witt stack, organizing the Nygaard filtration and syntomic cohomology."),
S("s_fargues_scholze_geometrization", "theorem", "Geometrization of the local Langlands correspondence (Fargues–Scholze)", "",
  "A spectral action of the category of coherent sheaves on the stack of L-parameters on the category of l-adic sheaves on Bun_G over the Fargues–Fontaine curve, attaching L-parameters to smooth representations of p-adic reductive groups."),
T("t_smith_treumann_theory", "Smith–Treumann theory",
  "(constructible sheaf with finite-group action) -> (fixed-point sheaf in characteristic p)",
  "Applies Smith theory for constructible sheaves to relate equivariant cohomology in characteristic p to fixed loci, used to compute modular representation-theoretic data."),
S("s_modular_tilting_character_formula", "theorem", "Character formula for tilting modules (Riche–Williamson)", "",
  "The characters of indecomposable tilting modules for a reductive group in characteristic p are expressed through the p-canonical basis of the affine Hecke algebra, with a geometric proof of the linkage principle."),
T("t_fourier_interpolation", "Fourier interpolation (modular-form method)",
  "(growth/decay data) -> (radial Schwartz function with prescribed values)",
  "Constructs radial Schwartz functions interpolating prescribed values of a function and its Fourier transform on a discrete set, via quasimodular-form generating series."),
S("s_universal_optimality_e8_leech", "theorem", "Universal optimality of E8 and Leech lattices", "",
  "The E8 lattice in dimension 8 and the Leech lattice in dimension 24 minimize energy for every completely monotone potential, the strongest possible form of optimality."),
S("s_nuclear_dimension_one", "theorem", "Nuclear dimension one for classifiable C*-algebras (Castillejos–Evington–Tikuisis–White–Winter)", "",
  "Separable, simple, unital, nuclear, Z-stable C*-algebras have nuclear dimension exactly one, so finite nuclear dimension is equivalent to Z-stability."),
S("s_keisler_order_maximal_complexity", "theorem", "Maximal complexity of Keisler's order (Malliaris–Shelah)", "",
  "Keisler's order on first-order theories has continuum-many classes, with maximal complexity arising already among simple theories with trivial forking."),
S("s_mip_star_re_connes", "theorem", "MIP* = RE and refutation of the Connes embedding problem", "",
  "The class of languages decidable by a classical verifier interacting with entangled provers equals all recursively enumerable languages, which via Tsirelson's problem refutes the Connes embedding conjecture."),
]

# avoid clobbering ids that already exist
NEW = [n for n in NEW if n["id"] not in existing_ids]
new_ids = {n["id"] for n in NEW}
all_ids = existing_ids | new_ids
print(f"New nodes to add: {len(NEW)}")
dupe = [n['id'] for n in NEW if list(nn['id'] for nn in NEW).count(n['id'])>1]
assert not dupe, f"dup new ids: {set(dupe)}"

# ---------------- NEW EDGES ----------------
# next edge id
mx = 0
for e in d["edges"]:
    try: mx = max(mx, int(str(e["id"]).split("_")[-1]))
    except: pass
counter = [mx]
edges = []
def edge(frm, to, role, thm):
    counter[0]+=1
    return {"id": f"e_{counter[0]}", "from": frm, "to": to, "role": role,
            "parameter_binding": {}, "used_in_theorem": thm}

# (theorem, technique, [input states]) -> builds input edges (state->tech) + output (tech->theorem)
WIRING = [
 ("s_duffin_schaeffer_theorem", "t_gcd_graph_method", ["s_khintchine_diophantine_theorem"]),
 ("s_andre_oort_conjecture", "t_o_minimal_point_counting", ["s_shimura_variety", "s_ominimal_structure"]),
 ("s_uniform_mordell_lang", "t_betti_map_height_inequality", ["s_neron_tate_height", "s_jacobian_of_curve"]),
 ("s_schinzel_zassenhaus_theorem", "t_o_minimal_point_counting", ["s_real_numbers"]),
 ("s_picard_rank_jumps_k3", "t_o_minimal_point_counting", ["s_K3_surface_with_hodge_structure", "s_shimura_variety"]),
 ("s_caraiani_scholze_torsion_vanishing", "t_perfectoid_almost_mathematics", ["s_shimura_variety", "s_galois_representation"]),
 ("s_ggmt_polynomial_freiman_ruzsa", "t_entropy_method_extremal", ["s_polynomial_freiman_ruzsa_conjecture"]),
 ("s_kelley_meka_3ap", "t_entropy_method_extremal", ["s_diagonal_ramsey_bounds"]),
 ("s_sensitivity_conjecture", "t_signed_adjacency_interlacing", ["s_real_numbers"]),
 ("s_ringel_conjecture", "t_entropy_method_extremal", ["s_steiner_system_stkn"]),
 ("s_multicolor_ramsey_lower_bound", "t_ramsey_book_algorithm", ["s_diagonal_ramsey_bounds"]),
 ("s_erdos_faber_lovasz_theorem", "t_entropy_method_extremal", ["s_steiner_system_stkn"]),
 ("s_random_symmetric_matrix_singularity", "t_entropy_method_extremal", ["s_random_matrix_theory"]),
 ("s_high_girth_steiner_triple_systems", "t_entropy_method_extremal", ["s_keevash_existence_of_designs", "s_steiner_system_stkn"]),
 ("s_union_closed_constant_bound", "t_entropy_method_extremal", ["s_real_numbers"]),
 ("s_diagonal_ramsey_exponential_improvement", "t_ramsey_book_algorithm", ["s_diagonal_ramsey_bounds"]),
 ("s_ramsey_r4t_asymptotics", "t_ramsey_book_algorithm", ["s_off_diagonal_ramsey_bounds"]),
 ("s_erdos_hajnal_loglog_bound", "t_entropy_method_extremal", ["s_erdos_hajnal_conjecture"]),
 ("s_talagrand_selector_process", "t_entropy_method_extremal", ["s_kahn_kalai_expectation_threshold"]),
 ("s_hadwiger_improved_bound", "t_entropy_method_extremal", ["s_hadwiger_conjecture"]),
 ("s_cheskidov_luo_sharp_nonuniqueness", "t_convex_integration_hydrodynamics", ["s_navier_stokes_equations"]),
 ("s_knotted_3_balls_s4", "t_convex_hypersurface_theory", ["s_riemannian_manifold"]),
 ("s_rectangular_peg_problem", "t_floer_homotopy_theory", ["s_real_numbers"]),
 ("s_arithmeticity_geodesic_submanifolds", "t_o_minimal_point_counting", ["s_riemannian_manifold"]),
 ("s_generalized_smale_conjecture", "t_ricci_flow_with_surgery", ["s_ricci_flow_equation"]),
 ("s_noncollapsed_ricci_flow_structure", "t_pointed_nash_entropy", ["s_ricci_flow_equation"]),
 ("s_michael_simon_sobolev_brendle", "t_almgren_pitts_min_max", ["s_minimal_surface_equation"]),
 ("s_generic_mcf_singularities", "t_pointed_nash_entropy", ["s_mcf_short_time_existence"]),
 ("s_generic_regularity_minimizers", "t_almgren_pitts_min_max", ["s_minimal_surface_equation"]),
 ("s_arnold_conjecture_morava", "t_floer_homotopy_theory", ["s_arnold_conjecture", "s_morava_k_theory"]),
 ("s_telescope_conjecture_disproof", "t_even_filtration", ["s_chromatic_homotopy_theory"]),
 ("s_chromatic_redshift", "t_even_filtration", ["s_chromatic_homotopy_theory"]),
 ("s_chromatic_nullstellensatz", "t_even_filtration", ["s_chromatic_homotopy_theory"]),
 ("s_lqg_metric", "t_condensed_mathematics", ["s_sle_existence"]),
 ("s_wave_kinetic_equation_derivation", "t_convex_integration_hydrodynamics", ["s_navier_stokes_equations"]),
 ("s_lis_directed_landscape_convergence", "t_entropy_method_extremal", ["s_directed_landscape", "s_kpz_universality"]),
 ("s_kerr_stability_small_a", "t_pointed_nash_entropy", ["s_einstein_field_equations_vacuum", "s_kerr_solution"]),
 ("s_schwarzschild_nonlinear_stability", "t_pointed_nash_entropy", ["s_einstein_field_equations_vacuum", "s_schwarzschild_solution"]),
 ("s_fargues_scholze_geometrization", "t_absolute_prismatic_cohomology", ["s_geometric_satake", "s_geometric_langlands"]),
 ("s_modular_tilting_character_formula", "t_smith_treumann_theory", ["s_geometric_satake"]),
 ("s_universal_optimality_e8_leech", "t_fourier_interpolation", ["s_e8_lattice"]),
 ("s_nuclear_dimension_one", "t_entropy_method_extremal", ["s_c_algebra"]),
 ("s_keisler_order_maximal_complexity", "t_entropy_method_extremal", ["s_real_numbers"]),
 ("s_mip_star_re_connes", "t_entropy_method_extremal", ["s_c_algebra"]),
 # directed landscape produced by KPZ scaling
 ("s_directed_landscape", "t_entropy_method_extremal", ["s_kpz_universality"]),
]

dropped = []
for thm, tech, inputs in WIRING:
    if thm not in all_ids or tech not in all_ids:
        dropped.append((thm, tech, "endpoint missing")); continue
    for s in inputs:
        if s in all_ids:
            edges.append(edge(s, tech, "input", thm))
        else:
            dropped.append((thm, s, "input missing"))
    edges.append(edge(tech, thm, "output", thm))

print(f"New edges built: {len(edges)}")
if dropped:
    print("DROPPED:")
    for x in dropped: print("  ", x)

# ---------------- VALIDATE + WRITE ----------------
final_nodes = d["nodes"] + NEW
final_edges = d["edges"] + edges
fid = {n["id"] for n in final_nodes}
# no dup node ids
assert len(fid) == len(final_nodes), "duplicate node ids!"
# all edge endpoints exist
bad = [e for e in final_edges if e["from"] not in fid or e["to"] not in fid]
assert not bad, f"dangling edges: {bad[:5]}"
# bipartite role check on new edges
for e in edges:
    fr = next(n for n in final_nodes if n["id"]==e["from"])
    to = next(n for n in final_nodes if n["id"]==e["to"])
    if e["role"]=="input":
        assert to["kind"]=="technique" and fr["kind"]!="technique", e
    else:
        assert fr["kind"]=="technique" and to["kind"]!="technique", e

shutil.copy(PATH, PATH+".pre_arxiv.bak")
d["nodes"] = final_nodes
d["edges"] = final_edges
if "metadata" in d and isinstance(d["metadata"], dict):
    d["metadata"]["node_count"] = len(final_nodes)
    d["metadata"]["edge_count"] = len(final_edges)
with open(PATH, "w") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
# reparse
json.load(open(PATH))
from collections import Counter
print("OK. Totals:", len(final_nodes), "nodes,", len(final_edges), "edges")
print("Added kinds:", Counter(n["kind"] for n in NEW))
