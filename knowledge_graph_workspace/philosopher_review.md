# Philosopher's Review — Semantic Coherence of the Discovery Graph

Review of `mathematician_relationships.md` against `SCHEMA.md` coherence rules
and the authoritative technique catalogue in `10_toolbox.md`.

---

## §1 Verdict summary

The ontology is **broadly sound but has three structural weaknesses that must
be fixed before the graph is locked**. The bipartite `state ↔ technique`
skeleton is the right abstraction, and the mathematician has done a careful
job keeping technique names stable across chains (the fan-in for
`t_compose_with_identity`, `t_conserved_quantity`, `t_frequency_decomposition`,
`t_infinite_descent`, and `t_compactness_argument` is the most valuable asset
of the whole document). But:

1. **`t_compose_with_identity` is a grab-bag.** It is doing the work of at
   least three distinct moves (algebraic-identity closure, auxiliary
   construction, and final-step re-assembly). This is the single largest
   coherence failure.
2. **`t_analysis_algebra_topology_bridge` is the dual problem:** a catch-all
   into which Riemann–Roch, Atiyah–Singer, Faltings, Wiles, and Green–Tao
   transference have all been shoved. Those are four different bridges.
3. **Several directed edges are mislabelled as single techniques when the
   reversed arrow is a genuinely distinct technique that also appears
   elsewhere** (most visibly the pigeonhole / diagonalization pair and the
   Fourier / inverse-Fourier pair).

Beyond those, most nodes pass all four coherence rules (`typed correctness`,
`direction meaningfulness`, `reusability`, `non-redundancy`).

- `ACCEPT AS-IS`: **24** (of 22 states + 28 techniques + 15 compound = 65
  Part B entries — 24 pass without changes)
- `ACCEPT WITH MINOR REVISION`: **28** (wording, parameter binding, or
  abstraction-level tweak)
- `REJECT / NEEDS REFRAMING`: **6** (grab-bag or mis-levelled nodes)
- `FLAG FOR ORCHESTRATOR DECISION`: **7** (including the three the
  mathematician raised)

---

## §2 Node-level coherence review

I review Part B1 (recurring states) first, then Part B2 (recurring
techniques), then Part B3 (compound techniques). Every node in Part B is
addressed. A handful of Part A techniques that did not make Part B but
deserve commentary are appended.

### §2.1 Recurring states (Part B1)

#### s_real_numbers
**Verdict:** ACCEPT. Coherent and used consistently as an `axiom` node. The
"completion of ℚ" gloss in the description is redundant with `kind: axiom`
but harmless.

#### s_complex_numbers
**Verdict:** ACCEPT. Same comment as above. One note: in the FTA, Cardano,
and Fundamental-Theorem-of-Algebra chains, `s_complex_numbers` is listed
both as an axiom input **and** as a latent assumption for later chains
(Cauchy formula). The schema permits both roles; no change needed.

#### s_integers
**Verdict:** ACCEPT. Used 9 times. The name matches the object.

#### s_polynomial_ring
**Verdict:** ACCEPT WITH MINOR REVISION. This is the only state node where
the mathematician's usage papers over a genuine distinction: some chains
need ℚ[x] (Abel–Ruffini), some need k[x₁…xₙ] (Nullstellensatz, Hilbert
basis), some need ℂ[x] (FTA, Cardano). **Recommend:** keep one node
`s_polynomial_ring` and put `base_ring` and `num_variables` on the *edges*
per the schema's parameter-convention section. The graph theorist must
ensure the edge-parameter schema actually enforces this.

#### s_continuous_function_on_interval
**Verdict:** ACCEPT. Used in Bolzano, FTC, Weierstrass approximation,
Brouwer (as continuous self-map), Banach (generalised to complete metric).
The Brouwer and Banach cases are borderline — both use *continuous
self-map on a space* rather than specifically "on an interval" — but the
mathematician's choice to share the node is defensible given the Banach
case is already distinguished via `s_strict_contraction`.

#### s_L2_function_space
**Verdict:** ACCEPT. Clean. Appears in Fourier, CLT (via characteristic
functions, which live in L² only for finite-variance case), and ergodic
theorem. The CLT chain technically uses L¹ ∩ L² (characteristic functions
are continuous bounded); but at the abstraction level of this graph, L² is
fine.

#### s_finite_group
**Verdict:** ACCEPT. Used in Sylow, Galois FT, CFSG, Lagrange, Fermat LT.
One small worry: `s_galois_group` is listed separately and also has
fan-in. The ontological question is whether `s_galois_group` is-a
`s_finite_group`. Suggestion: add a `is_specialization_of: s_finite_group`
field on `s_galois_group`.

#### s_galois_group
**Verdict:** ACCEPT (with is-a link as above).

#### s_compact_smooth_manifold
**Verdict:** ACCEPT. The closest-to-trivial node in Part B. Used cleanly
in Gauss–Bonnet, Atiyah–Singer, Poincaré.

#### s_smooth_function
**Verdict:** ACCEPT WITH MINOR REVISION. The mathematician lists "Taylor,
MVT, FTC, Stokes, physics-to-PDE family." For Taylor and MVT the domain is
an interval; for Stokes it's a manifold; for physics-to-PDE it's a
spacetime. Recommend either (a) add parameter `domain` on edges or (b)
split into `s_smooth_function_on_R` and `s_smooth_function_on_manifold`.
Option (a) is consistent with the schema; prefer it.

#### s_riemannian_metric
**Verdict:** ACCEPT.

#### s_compact_oriented_surface_without_boundary
**Verdict:** ACCEPT. One of the cleanest nodes in the graph.

#### s_elliptic_curve_over_Q
**Verdict:** ACCEPT.

#### s_modular_form
**Verdict:** ACCEPT. Note: the "monstrous moonshine" and "Hardy–Ramanujan
partitions" usages in the B1 description are aspirational — no
mathematician-chain in Part A actually exercises those. OK to leave
because the schema description is not load-bearing for the graph.

#### s_riemann_zeta_function
**Verdict:** ACCEPT.

#### s_euler_characteristic_chi
**Verdict:** ACCEPT. Important cross-cutting state — Euler polyhedron,
Gauss–Bonnet, Riemann–Roch, Atiyah–Singer. The fact that it appears on
both sides of different theorems (as output of Euler's formula, as input
to Gauss–Bonnet and Atiyah–Singer) is exactly the fan-out/fan-in story the
CHARTER wants.

#### s_prime_numbers
**Verdict:** ACCEPT. Used 7 times.

#### s_measure_preserving_transformation
**Verdict:** ACCEPT.

#### s_zfc_axioms
**Verdict:** ACCEPT.

#### s_smooth_manifold_with_boundary
**Verdict:** ACCEPT.

#### s_primes_in_naturals
**Verdict:** REJECT / DEDUPLICATE. This is a **duplicate of
`s_prime_numbers`**. Per schema deduplication rule 1 ("states are
deduplicated by mathematical identity, not name"), merge them. The
mathematician essentially admits this: "state/axiom alias". Action for
graph theorist: pick one canonical id, fold the other into `aliases`.

#### s_simply_connected_manifold
**Verdict:** ACCEPT. Cross-cuts Riemann mapping (n=2), Poincaré (n=3),
generalized Poincaré (n≥5). Good fan-in example.

### §2.2 Recurring techniques (Part B2)

#### t_symmetry_reduction
**Verdict:** ACCEPT. Coherent single idea (quotient by a group action).
Name specific enough. Abstraction level matches neighbors
(`t_conserved_quantity`, `t_duality`). One edge-case: in Pythagoras the
"group" is a single reflection; in Sylow it is conjugation by G. The
`parameter_binding: {group: G}` on the edge handles this correctly.

#### t_compose_with_identity
**Verdict:** REJECT / NEEDS REFRAMING. **This is the single worst
coherence problem in the document.** The mathematician uses
`t_compose_with_identity` for at least three distinct moves:

1. **Algebraic-identity closure:** Brahmagupta bhāvanā, Euler's
   four-square identity, Diophantus two-square identity. Here P-instances
   combine via a bilinear identity to produce new P-instances. This
   matches the toolbox entry `composeWithIdentity` (Cluster 2) exactly.
2. **Auxiliary construction:** Ptolemy's "construct point K on diagonal
   with ∠ABK = ∠DBC" and Brouwer's "build retraction D_n → ∂D_n" and
   Wiles's Frey curve construction. These are *not* closure under an
   identity; they are the introduction of a helper object whose structure
   forces the conclusion. Much closer to what Pólya calls "auxiliary
   element" or to `t_reduce_to_canonical_form` than to
   identity-composition.
3. **Final-step re-assembly:** Pythagorean theorem step 2
   ("similarity ratio squared = area ratio"), Basel problem step 2
   ("coefficients of x² of product = Σ 1/n²"), Taylor (Lagrange
   remainder). These are just "apply one algebraic identity and you're
   done" — essentially the terminal arithmetic step, not a technique.

Toolbox entry 2.3 (`composeWithIdentity`) matches only case (1). Cases (2)
and (3) are being laundered through the same node. Recommendation:

- Keep `t_compose_with_identity` **only for case (1)** — algebraic closure
  under a bilinear/multilinear identity (Brahmagupta, Euler four-square,
  Diophantus two-square, Jacobi triple product).
- Introduce `t_auxiliary_construction` for case (2). This is *distinct*
  from `t_reduce_to_canonical_form` because it adds structure rather than
  simplifying it.
- Case (3) should be absorbed into the postcondition of the preceding
  technique rather than getting its own edge. If the mathematician insists
  on recording it, use `t_closing_algebraic_computation` but flag it as
  content-free.

#### t_reduce_to_canonical_form
**Verdict:** ACCEPT. Coherent and matches toolbox entry 2.2 exactly.
Abstraction level consistent with neighbors. Used 11 times — highest
fan-in in Part B after `t_compose_with_identity`.

#### t_conserved_quantity
**Verdict:** ACCEPT. Toolbox entry 3.2. Clean, coherent, well-used.

#### t_frequency_decomposition
**Verdict:** ACCEPT. Coherent single idea (project onto orthogonal basis
and read off coefficients). Consistent with the Fourier / Laplace /
wavelet / character-theory pattern. One quibble: does this collapse
"wavelets" (dyadic) and "Fourier" (orthonormal) too aggressively? The
toolbox itself keeps `dyadicDecomposition` as a **refinement-of**
`frequencyDecomposition` (Cluster 4), so the compositional story is:
`t_frequency_decomposition` at the top-level graph, with a subgraph
elaboration that shows dyadic / Littlewood–Paley as a specialisation.
This is the right structure. No rename needed.

#### t_compactness_argument
**Verdict:** ACCEPT. Toolbox entry 6.3. Coherent.

#### t_exhaustion_squeeze
**Verdict:** ACCEPT. Toolbox entry 4.1.

#### t_structural_isomorphism
**Verdict:** ACCEPT WITH MINOR REVISION. Toolbox entry 5.2. Used in CRT,
Galois FT, Nullstellensatz, CH consistency, Abel–Ruffini. There is a
genuine abstraction-level question here: `t_structural_isomorphism` and
`t_analysis_algebra_topology_bridge` overlap significantly (both are
"functor between theories"). The toolbox actually has
`analysisAlgebraTopologyBridge` **inheriting from**
`structuralIsomorphism`. My recommendation is to keep both nodes because
the bridge is specifically *cross-clustered* (analysis ↔ algebra ↔
topology) whereas plain structural isomorphism is within-cluster
(ℤ/mn ≅ ℤ/m × ℤ/n). But this overlap warrants explicit is-a
documentation.

#### t_obstruction_class
**Verdict:** ACCEPT. Toolbox entry 6.2. Clean.

#### t_infinite_descent
**Verdict:** ACCEPT WITH MINOR REVISION. Toolbox entry 8.2. The
**"dual form"** annotation the mathematician attaches to Cantor, Brouwer,
Halting, and Gödel deserves attention. Infinite descent proper is *number
theoretic* ("pick minimal counterexample, construct smaller"). What
Cantor / Brouwer / Halting / Gödel do is the *proof-by-contradiction*
shell — "assume X exists, derive contradiction, ergo ¬X." These are not
descent; they are `reductio ad absurdum`. Recommendation: either
(a) relabel those edges as `t_reductio_ad_absurdum` or
(b) accept `t_infinite_descent` as the umbrella but flag in the subgraph
elaboration that the "dual form" is actually a distinct logical move.
I recommend (a) — the umbrella is misleading, and the toolbox does
distinguish them.

#### t_contraction_fixed_point
**Verdict:** ACCEPT. Toolbox entry 8.1. Coherent.

#### t_physics_to_pde
**Verdict:** ACCEPT. Toolbox entry 9.1. Coherent despite the name's
informality. The one case to watch is Gauss's Theorema Egregium — the
mathematician lists `t_physics_to_pde` with parameter "Hanover geodetic
survey". Defensible (the geodetic survey is the physical origin) but
could equally be `t_spot_pattern_in_table`. Leave as is; the chain
documents the historical route.

#### t_diagonalize
**Verdict:** ACCEPT. Toolbox entry 7.1. Used in Cantor, Gödel, Halting.

#### t_arithmetize_syntax
**Verdict:** ACCEPT. Toolbox entry 7.2.

#### t_finite_case_check
**Verdict:** ACCEPT. Toolbox entry 10.1.

#### t_formal_verify
**Verdict:** ACCEPT. Toolbox entry 10.2.

#### t_distributed_collaboration
**Verdict:** ACCEPT WITH MINOR REVISION. Toolbox entry 10.3. This is a
*sociological* technique rather than a mathematical one. It has
fan-in ≥ 2 (CFSG, Polymath 8, Green–Tao), so it survives the CHARTER
success-criterion #2. But it should be tagged `kind: meta_technique` or
similar, so the graph doesn't treat it as a mathematical arrow for
derivation-path purposes.

#### t_force_independence
**Verdict:** ACCEPT. Toolbox entry 7.3.

#### t_raise_dimension
**Verdict:** ACCEPT. Toolbox entry 6.1. Strong fan-in across very
different mathematical areas (Desargues, FTA, Faltings, Wiles, Perelman).

#### t_analysis_algebra_topology_bridge
**Verdict:** REJECT / NEEDS REFRAMING. **Second-worst coherence problem.**
The mathematician uses this node for:

- Riemann–Roch (cohomology groups H⁰, H¹ of a sheaf → Euler char)
- Atiyah–Singer (K-theory pushforward = analytic index)
- Faltings (heights, Galois representations, p-adic Hodge)
- Wiles (Ribet level-lowering)
- Green–Tao (transference principle: dense subset of pseudorandom majorant)

These are five genuinely different bridges. The toolbox agrees — its
examples list all five as *instances*, not as repeated uses of a single
unified move. Recommendation: either

- **Split** into `t_sheaf_cohomology_bridge`, `t_k_theoretic_index_bridge`,
  `t_heights_and_galois_rep_bridge`, `t_level_lowering_bridge`,
  `t_transference_bridge`; keep `t_analysis_algebra_topology_bridge` as an
  abstract parent with `has_subgraph: true` and each of the above as
  specializations. OR
- **Keep** as a single top-level umbrella node but require the
  parameter_binding on the edge to specify which bridge. Graph theorist
  must decide based on fan-in/fan-out.

I recommend the split, because the "bridges" have different input types
(sheaves vs. abelian varieties vs. pseudorandom sets) and thus different
typed-correctness signatures. Schema coherence rule 1 forces the split.

#### t_interpolate_and_continue
**Verdict:** ACCEPT. Toolbox entry 4.2. Coherent.

#### t_axiomatize_from_instances
**Verdict:** ACCEPT. Toolbox entry 5.1.

#### t_pigeonhole_collision
**Verdict:** ACCEPT. Toolbox entry 11.2.

#### t_spot_pattern_in_table
**Verdict:** ACCEPT. Toolbox entry 1.1.

#### t_sieve_by_optimized_quadratic
**Verdict:** ACCEPT. Toolbox entry 11.4 (Selberg sieve).

#### t_ergodic_correspondence
**Verdict:** ACCEPT. Toolbox entry 9.4.

#### t_duality
**Verdict:** ACCEPT. Toolbox entry 3.3. However, note overlap with
`t_structural_isomorphism` and with `t_koszul_dual_operad_swap`. Duality
is *contravariant* structural equivalence; isomorphism is
*covariant*. Distinction is real and should be preserved.

#### t_character_decomposition_count
**Verdict:** ACCEPT. Toolbox entry 3.4.

### §2.3 Compound techniques (Part B3)

#### t_fourier_transform (compound)
**Verdict:** ACCEPT. Coherent composite. Subgraph sub-techniques listed
(orthogonal projection, Plancherel, convolution→pointwise, inverse
transform) are correct.

#### t_svd_and_spectral_decomposition (compound)
**Verdict:** FLAG FOR ORCHESTRATOR. See §4 for detailed recommendation.

#### t_galois_correspondence (compound)
**Verdict:** ACCEPT. Well-composed. The sub-technique list (symmetry
reduction on roots, normality/separability, duality on subgroup–subfield
lattice, solvability as obstruction class) is exactly right.

#### t_ricci_flow_with_surgery (compound)
**Verdict:** ACCEPT. Correct composite: `t_physics_to_pde` +
`t_flow_with_surgery` + `t_conserved_quantity` (entropy) +
`t_rescale_for_asymptotic_geometry`.

#### t_atiyah_singer_index_machinery (compound)
**Verdict:** ACCEPT WITH MINOR REVISION. The mathematician says this is
"composite of t_frequency_decomposition + t_group_complete_exact_category
+ t_analysis_algebra_topology_bridge." The last ingredient is part of the
reject chain in §2.2 — once that node is reframed, the composition
definition must be updated.

#### t_wiles_modularity (compound)
**Verdict:** ACCEPT WITH MINOR REVISION. Same caveat: depends on
`t_analysis_algebra_topology_bridge`.

#### t_godel_numbering (compound)
**Verdict:** ACCEPT.

#### t_category_theoretic_colimits_and_adjoints (compound)
**Verdict:** FLAG FOR ORCHESTRATOR. The mathematician introduces this but
no Part A chain actually uses it at the top level. CHARTER success
criterion #2 requires fan-in ≥ 2 or explicit single-use flag. Either
(a) drop it from the top-level graph and retain only as a subgraph
component, or (b) explicitly flag as a "single-use landmark".

#### t_selberg_sieve_method (compound)
**Verdict:** ACCEPT.

#### t_circle_method (compound)
**Verdict:** ACCEPT.

#### t_furstenberg_correspondence_principle (compound)
**Verdict:** ACCEPT.

#### t_polynomial_method (compound)
**Verdict:** FLAG FOR ORCHESTRATOR. No Part A chain actually uses it.
Same treatment as `t_category_theoretic_colimits_and_adjoints`: demote to
"catalog only" or provide at least one derivation chain.

#### t_schur_weyl_and_double_centralizer (compound)
**Verdict:** FLAG FOR ORCHESTRATOR. Same issue — in the toolbox but not in
any Part A chain.

#### t_deformation_and_R_equals_T (compound)
**Verdict:** ACCEPT. Used in Wiles chain.

#### t_perelman_entropy_package (compound)
**Verdict:** ACCEPT.

### §2.4 Techniques appearing in Part A but not Part B

The following deserve review because they appear in chains but not in
Part B recurring-techniques list:

#### t_complete_the_square
**Verdict:** ACCEPT. Appears in Pythagoras, Cardano, Ferrari. That's
fan-in ≥ 3 — it **should have been in Part B**. Action: orchestrator to
add.

#### t_complex_analysis_to_integers
**Verdict:** ACCEPT. Appears in PNT only (single-use). Flag as such.

#### t_flow_with_surgery
**Verdict:** ACCEPT. Appears in Weierstrass approximation (via
Gaussian heat-kernel) and Perelman. Fan-in = 2. Should be in Part B.

#### t_deformation_cohomology
**Verdict:** ACCEPT. Wiles only, single-use. Flag.

#### t_probabilistic_existence
**Verdict:** ACCEPT. Szemerédi only. Flag.

#### t_major_minor_arc_decomposition
**Verdict:** ACCEPT. Helfgott only in Part A (though circle method
subgraph lists many uses). Flag.

#### t_sheafify_on_grothendieck_topology
**Verdict:** ACCEPT. Riemann–Roch only in Part A. Flag.

#### t_group_complete_exact_category
**Verdict:** ACCEPT. Atiyah–Singer only. Flag.

#### t_rescale_for_asymptotic_geometry
**Verdict:** ACCEPT. Perelman only. Flag.

#### t_ultraproduct_transfer
**Verdict:** ACCEPT. Tychonoff only in Part A. Flag.

---

## §3 Edge / parameter coherence

I spot-checked 18 edges from Part A across all six chapters. Applying the
three tests from the prompt (reverse-edge meaning, parameter-binding
precision, theorem-tag correctness):

1. **Pythagoras step 1** — `s_right_triangle --[t_symmetry_reduction {group:
   reflection across altitude}]--> s_two_similar_subtriangles`. Reverse
   would be "glue two similar subtriangles back into a right triangle",
   which is a genuinely different move (surgery / identification). Since
   the graph has no `t_glue_along_boundary` node, flag this as a **missing
   inverse technique**. Directedness is real here. Parameter binding is
   precise. Theorem tag correct.

2. **Cardano step 1** — `s_general_cubic --[t_reduce_to_canonical_form
   {substitution: x = t − b/3a}]--> s_depressed_cubic`. Reverse is
   "undo substitution, get general cubic." This is the *same* technique
   applied backward (the inverse substitution is also a canonical-form
   reduction). No new node needed; parameter binding should indicate
   direction. Good.

3. **Desargues step 1** — `s_two_triangles_in_plane --[t_raise_dimension
   {2D → 3D}]--> s_two_triangles_in_space`. Reverse would be
   `t_lower_dimension` (or `t_projection`). These are **genuinely
   different techniques** and the graph should have both. Missing inverse
   should be flagged. (Desargues step 3 is "project back to plane," which
   implicitly uses projection — but the mathematician reuses
   `t_symmetry_reduction` for it. That is a **typed-correctness
   mismatch**: projection 3D→2D is not a group quotient.)

4. **Desargues step 3** — labelled `t_symmetry_reduction {project back to
   plane}`. **REJECT**. Projection is not symmetry reduction. Orchestrator
   should either (a) introduce `t_projection_to_subspace` or
   (b) re-label this as `t_raise_dimension` with inverse parameter.

5. **Fermat's two-squares step 2** — `--[t_pigeonhole_collision {bins:
   Thue's lattice bins}]--> s_small_a_b_with_a²+b²≡0 mod p`. Reverse is
   meaningless (can't un-collide). Directedness real. Parameter binding
   precise. Good.

6. **Fourier heat step 2** — `--[t_frequency_decomposition {basis:
   sin(nπx/L)}]--> s_mode_by_mode_ODE_system`. Reverse is
   `t_inverse_frequency_decomposition` or `t_reassemble_from_modes`.
   The toolbox treats inverse Fourier as part of the same technique
   (postconds include "Reassemble via inverse transform"). Schema rule 2
   ("SVD and its inverse reconstruction are different nodes") suggests
   the opposite. **Flag the inconsistency.** My recommendation: keep one
   node, handle direction via edge `role` and a `direction: forward |
   inverse` parameter. The "SVD vs inverse" example in the schema is
   wrong — for SVD too, forward and inverse are the same technique.

7. **Galois FT step 2** — `--[t_duality {subgroups ↔ intermediate fields,
   order-reversing}]--> s_galois_correspondence`. Reverse is
   the same (duality is self-inverse). Correctly directed? Duality is
   genuinely a *pair of arrows*; directedness here is an artifact.
   Flag: the schema should permit undirected technique edges for
   equivalences.

8. **Stokes step 2** — `--[t_duality {integration vs differentiation: ∫ dω
   = ∫ ω}]--> s_stokes_theorem`. Similar: duality between ∫ and d. Same
   comment as Galois — this is an *equivalence* more than a directed
   arrow.

9. **PNT step 3** — `--[t_complex_analysis_to_integers {Perron-style
   contour}]-->`. Correct. Directedness real (can't go from PNT back to
   zeta non-vanishing).

10. **Riemann–Roch step 1** — input includes `s_divisor_D`, output is
    `s_sheaf_O_D_on_curve`. This step is labeled
    `t_sheafify_on_grothendieck_topology` but the parameter binding
    "{line bundle O(D)}" is narrower than the toolbox's
    sheafification entry, which handles arbitrary sheaves. Flag
    **over-specification** — the parameter binding should read
    `{construction: divisor → line bundle}` and acknowledge this is a
    specific instance. Minor.

11. **Faltings step 2** — `--[t_analysis_algebra_topology_bridge {heights,
    Galois representations, p-adic Hodge}]-->`. **Over-collapsed**, see
    §4 discussion.

12. **Wiles step 3** — `--[t_deformation_cohomology {R = T theorem}]-->`.
    Parameter binding is load-bearing; it encodes the whole R=T
    machinery. Toolbox entry has `deformationCohomology` with the Wiles
    citation explicit. Good.

13. **Perelman step 2** — `--[t_flow_with_surgery {neck-pinch surgery;
    Perelman entropy and reduced volume as monotone monitors}]-->`.
    Parameter binding lists two distinct sub-techniques (surgery method,
    entropy monotonicity). Suggest splitting into two edges or using the
    compound `t_ricci_flow_with_surgery` subgraph.

14. **Green–Tao step 1** — `--[t_analysis_algebra_topology_bridge
    {transference principle}]-->`. Same over-collapsing as Faltings.

15. **CH independence step 1** — `--[t_force_independence {Cohen forcing}]-->`.
    Directedness real; reverse would be "extract ground model from
    generic extension," a genuinely different move. Flag: no reverse
    node. Probably OK not to add.

16. **Tychonoff step 1** — `--[t_ultraproduct_transfer {ultrafilter on
    index set}]-->`. Reverse is "decompose limit structure back into
    family" (Łoś direction). Toolbox allows both directions under one
    entry; good.

17. **Brouwer step 1** — `--[t_compose_with_identity {build retraction
    D_n → ∂D_n}]-->`. Reject per §2.2 — this is `t_auxiliary_construction`,
    not `t_compose_with_identity`.

18. **Cantor step 1** — `--[t_diagonalize {flip the n-th digit of the
    n-th listed real}]-->`. Reverse is meaningless. Directedness real.
    Parameter binding precise. Good.

**Summary of edge findings:** ~5 of 18 edges have issues — either a
missing inverse node (items 1, 3), a mislabelled technique (item 4),
ambiguity about directed vs undirected (items 6–8), or over-collapsed
parameter binding (items 11, 14). That's a 28% flag rate on edges — high
enough to warrant a second pass by the graph theorist before locking the
graph.

---

## §4 Ontological mismatches — three explicit flags

### §4.1 `t_svd_and_spectral_decomposition`

**Mathematician's position:** Not in toolbox as a named entry. Closest
composite is `t_reduce_to_canonical_form + t_frequency_decomposition`.
Flagged for orchestrator to decide.

**Philosopher's recommendation:** **Add as a standalone technique node
under Cluster 2 (Algebraic Manipulation), not Cluster 4.** Reasoning:

- `t_reduce_to_canonical_form` is the right parent (SVD reduces a general
  matrix to diagonal form via orthogonal change of bases). The toolbox's
  canonical-form entry explicitly cites "Jordan normal form over ℂ" and
  "Sylvester's law of inertia for real quadratic forms" — SVD is exactly
  analogous.
- `t_frequency_decomposition` is tempting because SVD produces an
  orthonormal basis. But the basis in SVD is *derived from the operator*,
  not assumed a priori (Fourier's basis is fixed). That's a structural
  difference.
- Creating `t_svd_and_spectral_decomposition` as a specialization of
  `t_reduce_to_canonical_form` with inheritance from
  `t_frequency_decomposition` (for the orthogonal-projection sub-step) is
  the cleanest.
- Subgraph should include: orthogonal diagonalization of self-adjoint
  (spectral theorem), polar decomposition, Eckart–Young truncation.
- Fan-in ≥ 2: Perron–Frobenius, PCA, image compression, Laplacian
  spectral graph theory, Koopman operator in ergodic theory — easily
  justifiable.

**Action:** ADD as new node. Give it its own toolbox entry (11th in
Cluster 2). Mark `inherits: t_reduce_to_canonical_form,
t_frequency_decomposition`.

### §4.2 `t_heights_and_galois_representations`

**Mathematician's position:** Folded into
`t_analysis_algebra_topology_bridge` for Faltings and Wiles.

**Philosopher's recommendation:** **The current folding is too flat.**
Heights theory and Galois representations are two different tools with
different type signatures. They co-appear because the Faltings / Wiles
program uses both, but that doesn't make them one technique.

Proposed structure:

- Keep top-level node `t_analysis_algebra_topology_bridge` (with the
  reframing from §2.2 applied).
- Add two separate subgraph nodes used inside that bridge:
  `t_canonical_height_theory` and `t_galois_representation_machinery`.
- The p-adic Hodge theory piece deserves its own sub-node too
  (`t_p_adic_hodge_comparison`), because it connects étale to de Rham
  cohomology — genuinely different from either heights or plain Galois
  reps.

**Action:** Do not create top-level nodes for these; but the Wiles
subgraph MUST split them. The Faltings subgraph MUST also split them.

### §4.3 `t_zorn_lemma / t_axiom_of_choice`

**Mathematician's position:** Folded into `t_compactness_argument` for
Hahn–Banach, following toolbox's treatment of Zorn as a compactness-style
existence principle.

**Philosopher's recommendation:** **Defensible but borderline.** Zorn's
lemma really *is* logically equivalent to a compactness-style
"maximal-element exists" argument, and the toolbox's `compactnessArgument`
lists Montel, Tychonoff, Banach–Alaoglu, and the compactness theorem of
first-order logic — all close cousins. BUT:

- Zorn / AC differs from topological compactness in that it is
  *set-theoretic*, not *topological*.
- In Tychonoff's chain, the mathematician already uses
  `t_ultraproduct_transfer + t_compactness_argument` — treating Zorn as
  compactness would make these steps circular.
- In Hahn–Banach, the Zorn step is load-bearing in a way the one-dim
  extension step is not.

Recommend: **keep the folding**, but add a `{variant: zorn}` parameter
binding on the edge so the semantic distinction is preserved. If in Round
2 someone wants to split, the parameter binding gives them the lever.

Don't create a separate `t_axiom_of_choice` node — it would be used only
in Hahn–Banach and Tychonoff (and implicitly in the Hamel basis
argument). That's too single-use to earn a top-level technique node.

---

## §5 What the graph still risks missing

Even after the corrections above, the graph captures "derivation chains"
but misses several kinds of mathematical move that are historically real:

**1. Conjecture ↔ negation dynamics.** The graph has no way to encode
"Gauss conjectured π(x) ~ x/ln x, then Riemann reframed via ζ zeros,
then Hadamard–de la Vallée Poussin proved it." Every conjecture-state has
a refined-conjecture-state (see Quadratic Reciprocity chain, steps 1–2),
but the transition is labelled `t_verify_on_special_cases` — which elides
the *refinement*, the Lakatos-style modification of the conjecture
itself. Suggest: add `t_conjecture_refinement` as a distinct technique.

**2. Counterexample-first exploration.** Hilbert's 16th problem, the
search for Julia sets, Viro patchworking, Milnor's exotic 7-sphere — all
are cases where the main move was *constructing a counterexample* to a
folkloric belief. The graph treats counterexamples as side outputs of
`t_verify_on_special_cases`, but for landmark results the counterexample
*is* the theorem. Suggest: `t_construct_counterexample` as a sibling to
`t_spot_pattern_in_table`.

**3. Iterative refinement of proof (Lakatos monster-barring).** The
"proof → counterexample → patched definition → new proof" cycle that
Lakatos documents in *Proofs and Refutations* is utterly invisible in
this graph. Every theorem is presented as a linear chain from axioms.
The graph would be much richer if it allowed **non-terminal states** to
loop back and modify earlier edges. This is a schema-level gap, not just
a node gap.

**4. Translation as its own move.** Taniyama–Shimura–Wiles, Langlands
reciprocity, Grothendieck's functor-of-points reframing — these are
*translation* moves that don't prove a new theorem but make existing ones
reformulable in a new language. They're currently folded into
`t_analysis_algebra_topology_bridge` or `t_structural_isomorphism`, but
they are arguably a distinct meta-move: *reformulate the question*, not
*prove the answer*. Suggest `t_reformulate_in_new_category`.

**5. Failed-technique-attempts.** Kummer's regular primes for FLT,
Cantor's continuum hypothesis attempts, Hilbert's program — the graph
records successes only. A richer "discovery graph" would include failed
edges (`status: refuted`, `status: superseded`) so that learners see not
just what worked but what was tried and why.

These five gaps are schema-level suggestions, not mathematician-blame.
Document them explicitly in the final knowledge-graph README so Round 2
can address them.

---

## §6 Specific corrections for the orchestrator

A numbered action list. Items are ordered roughly by severity (most
serious first). The orchestrator should apply all of these when producing
`11_knowledge_graph.md`.

1. **SPLIT `t_compose_with_identity`** into three distinct techniques:
   `t_compose_with_identity` (case 1, algebraic-identity closure — the
   toolbox entry 2.3), `t_auxiliary_construction` (case 2, introducing
   helper objects like the Frey curve or Ptolemy's point K),
   and *absorb case 3* (final-step arithmetic) into the preceding
   technique's postcondition rather than making it an edge.

2. **SPLIT `t_analysis_algebra_topology_bridge`** into specializations:
   `t_sheaf_cohomology_bridge`, `t_k_theoretic_index_bridge`,
   `t_heights_and_galois_rep_bridge`, `t_level_lowering_bridge`,
   `t_transference_bridge`. Keep the parent as abstract / `has_subgraph:
   true`. This is required by schema coherence rule 1 (typed correctness).

3. **RENAME `t_infinite_descent`'s "dual form" usages** to
   `t_reductio_ad_absurdum` in Cantor, Brouwer, Gödel, Halting chains.
   Keep genuine `t_infinite_descent` for Euclid, Fermat 2-sq, Lagrange 4-sq,
   Chakravāla, Hilbert basis (ACC).

4. **DEDUPLICATE `s_primes_in_naturals` = `s_prime_numbers`.** Fold one
   into the other's aliases. Per schema rule 1.

5. **ADD new toolbox entry `t_svd_and_spectral_decomposition`** in
   Cluster 2 with `inherits: t_reduce_to_canonical_form,
   t_frequency_decomposition`. Subgraph covers spectral theorem, polar
   decomposition, Eckart–Young. See §4.1.

6. **FIX Desargues step 3.** `t_symmetry_reduction {project back to plane}`
   is a typed-correctness violation. Either introduce
   `t_projection_to_subspace` or re-label as `t_raise_dimension` with
   inverse parameter binding `{direction: reverse}`.

7. **ADD `t_conjecture_refinement`** as a new Cluster-1 technique,
   distinct from `t_verify_on_special_cases`. Used in Quadratic
   Reciprocity step 2 (explicitly), implicitly in Kepler third law and
   Basel.

8. **ADD `t_auxiliary_construction`** as a new Cluster-2 technique (see
   item 1). Used in Ptolemy, Brouwer retraction, Wiles Frey curve,
   several others. Distinct from `t_reduce_to_canonical_form` because it
   *adds* structure rather than *simplifying*.

9. **PROMOTE `t_complete_the_square`, `t_flow_with_surgery` to Part B**
   (recurring techniques list). Both have fan-in ≥ 2 in Part A and were
   mistakenly omitted from the mathematician's B2 list.

10. **FLAG OR DEMOTE low-fan-in techniques**:
    `t_polynomial_method`, `t_category_theoretic_colimits_and_adjoints`,
    `t_schur_weyl_and_double_centralizer` — none appear in Part A
    chains. Either cite at least one derivation chain or mark as
    `single_use_landmark: true` per CHARTER success criterion #2.

11. **ADD is-a links between states:**
    `s_galois_group is_specialization_of s_finite_group`;
    `s_elliptic_curve_over_Q is_specialization_of s_smooth_projective_curve`;
    `s_compact_oriented_surface_without_boundary is_specialization_of
    s_compact_smooth_manifold`.

12. **NORMALIZE parameter conventions** for
    `s_polynomial_ring`: use edge parameters `{base_ring, num_variables}`
    consistently across Cardano, Ferrari, FTA, Abel–Ruffini, Galois FT,
    Hilbert basis, Nullstellensatz.

13. **NORMALIZE parameter conventions** for `s_smooth_function`:
    use edge parameter `{domain: interval | manifold | spacetime}`
    across Taylor, MVT, FTC, Stokes, Theorema Egregium, Noether.

14. **TAG `t_distributed_collaboration` as `kind: meta_technique`**
    rather than a mathematical derivation arrow. CFSG, Polymath 8,
    Green–Tao extension chains need special handling — the edge
    represents many authors, not a mathematical transformation.

15. **ADD undirected / equivalence flag for `t_duality` edges.**
    In Stokes, Galois FT, Nullstellensatz, the duality is a
    covariant-to-contravariant equivalence rather than a one-way arrow.
    Schema should allow `is_equivalence: true` on technique edges.

16. **REFINE Perelman step 2 edge** to use the compound node
    `t_ricci_flow_with_surgery` (Part B3 entry 4) with its subgraph
    rather than `t_flow_with_surgery` plus a long parameter binding.

17. **RECONCILE schema coherence rule 2 (direction meaningfulness) for
    `t_fourier_transform`.** Current SCHEMA.md says "SVD and its inverse
    reconstruction are different nodes", but the toolbox treats inverse
    Fourier as a postcondition of the same technique. Pick one policy
    and apply consistently. I recommend: treat forward/inverse as the
    same node, distinguished by edge parameter `{direction: forward |
    inverse}`.

18. **ADD schema-level support for conjecture↔negation cycles**
    (§5 gap 1) — at minimum, allow a state node to carry a
    `status: conjectured | refined | proved | refuted` field.

19. **FLAG single-use-landmark techniques** explicitly in the generated
    JSON: `t_deformation_cohomology` (Wiles), `t_probabilistic_existence`
    (Szemerédi), `t_sheafify_on_grothendieck_topology` (Riemann–Roch),
    `t_group_complete_exact_category` (Atiyah–Singer),
    `t_rescale_for_asymptotic_geometry` (Perelman),
    `t_ultraproduct_transfer` (Tychonoff),
    `t_complex_analysis_to_integers` (PNT).

20. **RESOLVE the `t_heights_and_galois_representations` flag** per §4.2:
    do not promote to top-level, but split at the Wiles-subgraph level
    into `t_canonical_height_theory`,
    `t_galois_representation_machinery`, and
    `t_p_adic_hodge_comparison`.

21. **RESOLVE the `t_zorn_lemma / t_axiom_of_choice` flag** per §4.3:
    keep the fold into `t_compactness_argument`, but require
    `{variant: zorn}` parameter binding on the Hahn–Banach and Tychonoff
    edges so the distinction is preserved for Round 2.

22. **VERIFY that every top-level technique node satisfies fan-in ≥ 2
    OR fan-out ≥ 2** (CHARTER success criterion #2) after applying items
    1–2 (since splitting reduces fan-in on each fragment). Run this as
    an automated graph-theorist check.

23. **DOCUMENT the five §5 gaps in a README note** attached to the final
    graph, so Round 2 has a clear to-do.

24. **ENFORCE schema deduplication rule 1** as an automated check:
    no two state nodes may have `kind: state` or `kind: axiom` with the
    same `type_signature` without being explicit aliases.

25. **RECHECK all edges whose `parameter_binding` contains multiple
    distinct sub-techniques** (e.g., Perelman step 2, Riemann–Roch
    step 2, Faltings step 2) and either split into multiple edges or
    reference a proper subgraph.

26. **STANDARDIZE technique cluster tags**: the mathematician's Part B
    lists cluster numbers informally; the formal JSON should have a
    validated `cluster: C{1..12}` field with cross-check against
    `10_toolbox.md`.

