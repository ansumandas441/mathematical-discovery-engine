# Reconnaissance — Discovery Leverage Points in `knowledge_graph.json`

**Source**: `/Users/primetrce/Documents/maths/knowledge_graph.json`
**Graph size**: 752 nodes (115 axioms + 239 states + 336 theorems + 62 techniques) · 1258 edges · 12 compound subgraphs
**Purpose**: Surface the places in the graph where new theorems are most likely to be produced by re-applying existing techniques to existing states. Every candidate below cites explicit node IDs.

---

## §1 — Edge state nodes (territory reached but not pushed further)

"Edge nodes" are state nodes produced inside a theorem chain with zero or one outgoing edge to a technique. These are forward boundaries: the theorist reached this intermediate object, used it once, and stopped. Pushing any *new* technique onto them yields a candidate theorem.

**Strict edge (zero outgoing techniques):**

1. `s_point_in_affine_n_space` — produced by `t_structural_isomorphism` in `s_nullstellensatz`. Type `Element(kⁿ)`. Never visited by `t_sheafify_on_grothendieck_topology`, `t_obstruction_class`, `t_compactness_argument`, `t_sheaf_cohomology_bridge`, `t_galois_correspondence`, `t_deformation_cohomology`. Next moves: sheafify these points into Spec, or attach obstruction cohomology to moduli of such points.
2. `s_third_law` — Kepler's empirically verified 3rd law, produced by `t_verify_on_special_cases`. Never fed into `t_physics_to_pde`, `t_conserved_quantity`, `t_symmetry_reduction`, `t_axiomatize_from_instances`. Axiomatising T²∝a³ into an inverse-square law is exactly the Newton/Noether step — the graph shows this seam is live.
3. `s_four_color_theorem_machine_certified` and `s_kepler_conjecture_machine_certified` — fed only by `t_formal_verify`. Never re-ingested by `t_axiomatize_from_instances`, `t_reduce_to_canonical_form`, `t_structural_isomorphism`, `t_analysis_algebra_topology_bridge`.
4. `s_pair_of_injections_with_orphans` — CBS intermediate; never touched by `t_duality`, `t_diagonalize`, `t_obstruction_class`, `t_raise_dimension`.

**Near-edge (exactly one outgoing technique) — richest candidates (of 167 total):**

5. `s_galois_group_S5` (in `s_abel_ruffini`) — only `t_obstruction_class` applied. Never by `t_character_decomposition_count`, `t_representable_functor_trick`, `t_sheafify_on_grothendieck_topology`, `t_duality`, `t_ergodic_correspondence`. Character-sum on S₅ orbits on the splitting field is a missing modular-form attack.
6. `s_topological_index_class_in_K_of_point` (Atiyah-Singer) — only `t_analysis_algebra_topology_bridge`. Never by `t_sheaf_cohomology_bridge`, `t_deformation_cohomology`, `t_force_independence`, `t_ergodic_correspondence`, `t_circle_method`.
7. `s_galois_correspondence` — only `t_structural_isomorphism`. Never by `t_ultraproduct_transfer`, `t_representable_functor_trick`, `t_category_theoretic_colimits_and_adjoints`, `t_duality` (despite being an anti-iso!), `t_furstenberg_correspondence_principle`. A categorical colimit of Galois correspondences → Grothendieck-Galois theorem.
8. `s_curve_inside_abelian_variety` (C ↪ J_C in Mordell-Faltings) — only `t_analysis_algebra_topology_bridge`. Never by `t_ergodic_correspondence`, `t_infinite_descent`, `t_frequency_decomposition`, `t_polynomial_method`, `t_obstruction_class`.
9. `s_ramification_stratification_of_elliptic_curves` — only `t_wiles_modularity`. Never by `t_sheaf_cohomology_bridge`, `t_deformation_cohomology` (despite literally being deformation data), `t_furstenberg_correspondence_principle`, `t_ergodic_correspondence`.
10. `s_ultrafilter_spectrum_Spec_B`, `s_compact_totally_disconnected_stone_space` (Stone) — never touched by `t_force_independence`, `t_sheafify_on_grothendieck_topology`, `t_arithmetize_syntax`, `t_galois_correspondence`, `t_representable_functor_trick`.
11. `s_maximal_gamma_set_on_M` (Zermelo) — only `t_reductio_ad_absurdum`. Never by `t_force_independence`, `t_ultraproduct_transfer`, `t_arithmetize_syntax`.
12. `s_infinitesimal_action_variation` (δS in `s_noether_theorem`) — only `t_conserved_quantity`. Never by `t_frequency_decomposition`, `t_fourier_transform`, `t_raise_dimension`, `t_obstruction_class`.
13. `s_limit_characteristic_function_equals_gaussian` (CLT) — only `t_compactness_argument`. Never by `t_sieve_by_optimized_quadratic`, `t_circle_method`, further `t_frequency_decomposition`, or `t_diagonalize`.
14. `s_canonical_quotient_by_kernel_map` (Noether iso) — only `t_structural_isomorphism`. Never by `t_category_theoretic_colimits_and_adjoints`, `t_representable_functor_trick`, `t_duality`. First-iso-as-adjunction is missing.
15. `s_finiteness_of_isogeny_class` (Mordell-Faltings) — only `t_obstruction_class`. Never by `t_heights_and_galois_rep_bridge`, `t_level_lowering_bridge`, `t_sieve_by_optimized_quadratic`.

---

## §2 — Highest-fanout techniques (master keys) and the clusters they skipped

Fanout here = **number of distinct theorems the technique contributed to**. Cluster attribution assigns each theorem to the canonical toolbox cluster (01..12) most heavily represented among its techniques.

| # | Technique | Own cluster | #thms | Clusters covered (of 12) | MISSING clusters |
|---|-----------|-------------|-------|--------------------------|------------------|
| 1 | `t_compactness_argument` | 06 | 43 | 3 | 01, 02, 03, 07, 08, 09, 10, 11, 12 |
| 2 | `t_reduce_to_canonical_form` | 02 | 37 | 6 | 01, 07, 08, 09, 11, 12 |
| 3 | `t_compose_with_identity` | 02 | 35 | 4 | 03, 04, 05, 07, 08, 09, 11, 12 |
| 4 | `t_structural_isomorphism` | 05 | 30 | 4 | 01, 03, 04, 07, 08, 10, 11, 12 |
| 5 | `t_conserved_quantity` | 03 | 30 | 5 | 01, 05, 07, 08, 10, 11, 12 |
| 6 | `t_axiomatize_from_instances` | 05 | 28 | 5 | 01, 04, 07, 09, 10, 11, 12 |
| 7 | `t_obstruction_class` | 06 | 25 | 4 | 01, 03, 05, 08, 09, 10, 11, 12 |
| 8 | `t_exhaustion_squeeze` | 04 | 23 | 3 | 03, 05, 06, 07, 08, 09, 10, 11, 12 |
| 9 | `t_auxiliary_construction` | C2 | 23 | 4 | 01, 04, 07, 08, 09, 10, 11, 12 |
| 10 | `t_duality` | 03 | 22 | 5 | 01, 07, 08, 09, 10, 11, 12 |

Observations:
- Every master key is MISSING from cluster 12 (homological/categorical). That is the single largest gap: the modern categorical language has not been run against the classical techniques yet.
- Clusters 07 (self-reference) and 11 (probabilistic) are next-rarest as targets for master keys. Applying `t_conserved_quantity` to self-referential objects (e.g. making a conservation law out of Gödel's β-function) is a standing unused move.
- `t_compactness_argument` has been used 43 times, all clustered around analytic/topological territory. It has NEVER been applied to an object classified under cluster 02 (algebraic manipulation). Compactness on polynomial rings via the Zariski topology is structurally begging to be added.
- `t_exhaustion_squeeze` is shockingly narrow in scope: 23 theorems but only 3 clusters, all of them analytic. Its "squeeze between upper and lower" structure was never used outside analysis.

---

## §3 — Under-used techniques (bottom 10 by fanout)

Techniques appearing in ≤1 theorem:

| Technique | Cluster | #thms | Has subgraph? | Likely reason |
|-----------|---------|-------|---------------|---------------|
| `t_polynomial_method` | 11 | 0 | No | Under-explored. The polynomial method solved cap-set, finite field Kakeya, joints. It should touch cluster 02 (algebra) and 11 (counting) — not yet wired in. |
| `t_galois_correspondence` | 05 | 0 top-level | Yes (sg_galois) | The compound is structured but the top-level node is never used as an edge terminal; it is implicitly there via `t_structural_isomorphism` only. |
| `t_godel_numbering` | 07 | 0 top-level | Yes | Subgraph exists but is not invoked as an atomic arrow anywhere. |
| `t_atiyah_singer_index_machinery` | 12 | 0 top-level | Yes | Same pattern: the subgraph is there, the top-level atomic node is orphan. |
| `t_furstenberg_correspondence_principle` | 09 | 0 top-level | Yes | Exists in subgraph form but not invoked as a discrete step. |
| `t_deformation_cohomology` | 06 | 1 | Yes | Used only inside `s_fermat_last_theorem`. Deformation cohomology deserves to appear for moduli of curves, representations, sheaves. |
| `t_major_minor_arc_decomposition` | 09 | 1 | Yes | Only `s_vinogradov` uses it. Circle-method arc decomposition is reusable everywhere harmonic analysis meets counting. |
| `t_group_complete_exact_category` | 12 | 1 | No | K-theory tool used once. Over-specialized in the graph, but not in reality. |
| `t_sheafify_on_grothendieck_topology` | 12 | 1 | No | Only one use. Should touch every "local-to-global" state node, of which there are dozens. |
| `t_representable_functor_trick` | 12 | 1 | Yes | Yoneda-style trick used once in `s_mordell_faltings`. Natural for every "moduli" state. |
| `t_double_centralizer_decompose` | 03 | 1 | No | Used once. Should apply to any (G, H)-bimodule state (none exist as separate nodes, hence under-used). |
| `t_ricci_flow_with_surgery` | 08 | 1 | Yes | Used only for `s_poincare_conjecture`. Mean-curvature-flow variants on other classifiable manifolds are unused. |
| `t_wiles_modularity` | 06 | 1 | Yes | Just `s_full_modularity_theorem_BCDT`. Modularity lifts to other Galois representations (Hilbert modular, Bianchi, totally-real fields) are not in the graph. |
| `t_selberg_sieve_method` | 11 | 1 | Yes | Only `s_zhang_bounded_gaps`. Every prime-counting theorem is a candidate. |
| `t_category_theoretic_colimits_and_adjoints` | 12 | 1 | Yes | Broad machinery with narrow deployment. |

The cluster-12 sextet (`t_group_complete_exact_category`, `t_sheafify_on_grothendieck_topology`, `t_representable_functor_trick`, `t_category_theoretic_colimits_and_adjoints`, `t_k_theoretic_index_bridge`, `t_sheaf_cohomology_bridge`) collectively touches only ~6 theorems. These are **under-explored**, not over-specialised: every moduli, every cohomological obstruction, every local-to-global argument in the graph can be re-run through them. `t_polynomial_method`, `t_furstenberg_correspondence_principle`, `t_major_minor_arc_decomposition` are the three most promising reuse candidates.

---

## §4 — Compound technique gaps

Compound techniques ordered by theorem appearances:

| Compound | Top-level usages |
|----------|------------------|
| `t_svd_and_spectral_decomposition` | 7 |
| `t_arithmetize_syntax` | 5 |
| `t_sieve_by_optimized_quadratic` | 5 |
| `t_flow_with_surgery` | 3 |
| `t_fourier_transform` | 2 |
| `t_ergodic_correspondence` | 2 |
| `t_circle_method` | 2 |
| `t_deformation_cohomology` | 1 |
| `t_major_minor_arc_decomposition` | 1 |
| `t_representable_functor_trick` | 1 |
| `t_ricci_flow_with_surgery` | 1 |
| `t_wiles_modularity` | 1 |
| `t_selberg_sieve_method` | 1 |
| `t_category_theoretic_colimits_and_adjoints` | 1 |
| `t_galois_correspondence` | 0 top-level (but hit via atomic substitute) |
| `t_godel_numbering` | 0 top-level |
| `t_atiyah_singer_index_machinery` | 0 top-level |
| `t_furstenberg_correspondence_principle` | 0 top-level |

**Highest-leverage compound gaps** (subgraph exists, top-level invocations ≤ 1):

1. `t_deformation_cohomology` (sg_deformation_r_equals_t) — R=T machine. One use (FLT). Candidates: `s_galois_group`, `s_ramification_stratification_of_elliptic_curves`, plus all moduli-like states.
2. `t_wiles_modularity` — Hilbert-modular lifts, Sato-Tate, Serre's conjecture, BSD all reachable from the same subgraph.
3. `t_major_minor_arc_decomposition` — every sum-of-powers or ternary-additive theorem (Goldbach weak, Waring r>3) is a candidate.
4. `t_selberg_sieve_method` — PNT in arithmetic progressions, Bombieri-Vinogradov, prime k-tuples all reachable.
5. `t_ricci_flow_with_surgery` — dim-4 geometric structures and Kähler-Ricci-flow attacks on complex varieties unrepresented.
6. `t_representable_functor_trick` — Yoneda on sheaves of sections, schemes-as-functors, moduli stacks is missing everywhere in cluster 12.
7. `t_category_theoretic_colimits_and_adjoints` — `(ind,res)`, `(Σ,Ω)`, `(free,forgetful)` lenses never imposed on existing states.
8. `t_furstenberg_correspondence_principle` — zero top-level invocations; applying it yields density strengthenings of any combinatorial theorem.

---

## §5 — Cross-cluster analogy candidates (technique T from Ci → state S from Cj)

From the 170 top-20-technique × canonical-cluster gap pairs, the most promising analogy candidates are:

| # | Technique | Target state (cluster) | Potential theorem sketch |
|---|-----------|------------------------|--------------------------|
| 1 | `t_compactness_argument` (C6) | `s_cyclic_quadrilateral` (C02 alg.) | Compactness on the moduli of cyclic quadrilaterals; limit cyclic quadrilateral as "most regular" — Poncelet-type closure theorem. |
| 2 | `t_compactness_argument` (C6) | `s_heat_equation_PDE` (C08 iter.) | Classical — long-time heat flow compactness; missing explicit wiring in the graph. Gives asymptotic shape theorem. |
| 3 | `t_frequency_decomposition` (C04) | `s_self_referential_godel_sentence_G` (C07 self-ref.) | Fourier/Walsh decomposition of Gödel-numbered recursive predicates → density of provable sentences. |
| 4 | `t_conserved_quantity` (C03) | `s_self_referential_godel_sentence_G` (C07 self-ref.) | Invariant of self-reference: a conserved-quantity argument that Gödel numbering fails to preserve. Candidate: a Noether-style "syntactic current". |
| 5 | `t_conserved_quantity` (C03) | `s_heat_equation_PDE` (C08 iter.) | Energy conservation for heat equation → long-time behavior. Explicit wiring missing. |
| 6 | `t_obstruction_class` (C06) | `s_invariant_subspace_decomposition` (C03 symm.) | Cohomological obstruction to the invariant-subspace problem; treat invariant subspaces as sections of a bundle. |
| 7 | `t_infinite_descent` (C08) | `s_gauss_curvature_K` (C09 cross-field) | Descent on curvature quantization; yields a combinatorial Gauss-Bonnet variant. |
| 8 | `t_structural_isomorphism` (C05) | `s_inscribed_circumscribed_96_gons` (C04 approx.) | Iso between inscribed/circumscribed n-gon lattices and dyadic filtrations → structural theorem in measure theory. |
| 9 | `t_character_decomposition_count` (C03) | `s_elliptic_curves_over_Q`-like states (C09 cross-field) | Trace-of-Frobenius character sums → bounds on rank. |
| 10 | `t_pigeonhole_collision` (C11) | `s_set_of_p_subgroups_with_G_action` (C03 symm.) | Pigeonhole on conjugates produces a Sylow-lite theorem with explicit density. |
| 11 | `t_axiomatize_from_instances` (C05) | `s_aps_in_pseudorandom_dense_subset` (C09 cross-field) | Lift Green-Tao's "transference" to an axiomatic relative-density principle. |
| 12 | `t_duality` (C03) | `s_component_type_and_characteristic_p_type_cases` (C10 comp.) | Duality between component-type / char-p analyses in the CFSG case-split → simpler classification reorganization. |

Each pair is literally absent from the graph's edge list and thus represents a theorem-generation candidate.

---

## §6 — Recursion seeds (top 5): terminal theorem T + unused technique P → candidate T′

**Seed 1. `s_noether_theorem` + `t_frequency_decomposition`**
Terminal theorem: Noether's theorem — "continuous symmetry ⇒ conservation law". Unused technique: Fourier-mode / frequency decomposition (C04), which has never been applied to the Noether intermediate `s_infinitesimal_action_variation`.
Candidate T′: For a Lagrangian system with a 1-parameter symmetry group acting via character χ on each Fourier mode, the conserved current **decomposes into independent conservation laws indexed by the spectrum of χ**, with mode-wise coercivity bounds. Equivalently, Noether's theorem lifts to a family of conservation laws on the frequency-indexed slice, giving a quantitative spectral Noether theorem that interpolates between the classical current and the quantum matrix-element statement.

**Seed 2. `s_fundamental_theorem_of_galois_theory` + `t_category_theoretic_colimits_and_adjoints`**
Terminal theorem: the Galois correspondence as a lattice anti-isomorphism. Unused technique: categorical colimits/adjoints (C12), never applied to `s_galois_correspondence`.
Candidate T′: The Galois correspondence is the restriction of an **adjunction** between `Fields/k` and `Profinite`ᵒᵖ, whose unit/counit are the Artin map and fixed-field functor. This adjunction extends to algebraic stacks: the correspondence on a scheme X with étale fundamental group π₁(X) is a colimit over affine covers. The candidate statement is a Galois correspondence for *ind-schemes* or an arithmetic-topological Grothendieck-Galois theorem where the anti-iso is replaced by a Quillen-adjunction between homotopy categories.

**Seed 3. `s_mordell_faltings` + `t_frequency_decomposition` / `t_polynomial_method`**
Terminal theorem: Mordell-Faltings — finiteness of rational points on high-genus curves. Unused technique: polynomial method (C11, 0 applications in graph), never touched `s_curve_inside_abelian_variety`.
Candidate T′: If C ↪ J_C is an Abel-Jacobi embedding, applying the polynomial method to the image of C(ℚ) in J_C modulo a prime ℓ produces an **explicit degree bound** for the number of rational points as a function of the genus, height, and a single auxiliary polynomial of controlled degree. This would be an effective Mordell bound — still open in full generality and known only in cases (Chabauty-Coleman, Katz-Rabinoff). The polynomial-method phrasing makes the bound algorithmically checkable.

**Seed 4. `s_central_limit_theorem` + `t_circle_method`**
Terminal theorem: CLT — sum of iid tends to normal. Unused technique: `t_circle_method` has not been applied to `s_limit_characteristic_function_equals_gaussian` or `s_characteristic_function_of_sum`.
Candidate T′: On each minor arc α = a/q + β with q>Q, the characteristic function φ_{S_n/√n}(t) admits a Vinogradov-style oscillation bound — yielding a **local CLT on arithmetic progressions** with effective error terms matching the circle-method major/minor decomposition. The resulting statement is a concrete quantitative CLT for sums constrained to residue classes mod q, uniform in q up to q ≤ n^{1/2-ε}.

**Seed 5. `s_stone_representation_theorem` + `t_representable_functor_trick` / `t_force_independence`**
Terminal theorem: Stone representation — every Boolean algebra is a field of sets via `B ↦ Spec B`, with Spec landing in `s_compact_totally_disconnected_stone_space`. Unused techniques: `t_representable_functor_trick` (C12), and `t_force_independence` (C07) has never been applied to `s_ultrafilter_spectrum_Spec_B`.
Candidate T′: The Stone spectrum functor is **representable** on the category of compact Hausdorff spaces by a specific universal object Ω (essentially 2 with ultrafilter topology); equivalently, Stone duality is the Yoneda-style (co)representation `Spec(-) ≅ Hom(-, Ω)`. Combined with forcing, this produces a family of Stone-style dualities **parameterized by ZFC-extensions**: for each forcing notion P, one obtains a representation-theorem of Boolean algebras enriched by P-generic information, bridging cluster 05 (abstraction) and cluster 07 (self-reference) that the graph currently keeps separate. A concrete corollary: independence of CH lifts to a non-trivial automorphism of the Stone-Čech remainder ω* ∖ ω under CH but trivialises under PFA — a candidate "duality-theoretic fingerprint" of the continuum hypothesis.

---

## Summary metrics

- **Edge state nodes**: 5 strict + 167 near-edge = 172 forward-boundary targets.
- **Master-key techniques missing from cluster 12**: 10 of top-10 — the single biggest systematic gap.
- **Under-used top-level techniques**: 15, of which 10 have a full compound subgraph yet are invoked ≤1 time.
- **Cross-cluster analogy gap pairs** (top-20 technique × 12 canonical clusters): 170 zero-interaction pairs.
- **Recursion seeds**: 5 concrete T → P → T′ statements with node IDs.

Richest single regions: (a) cluster-12 techniques × every moduli/obstruction state; (b) compound techniques with full subgraphs but single uses (`t_deformation_cohomology`, `t_selberg_sieve_method`, `t_ricci_flow_with_surgery`, `t_wiles_modularity`, `t_major_minor_arc_decomposition`); (c) edge-state targets `s_galois_group_S5`, `s_curve_inside_abelian_variety`, `s_infinitesimal_action_variation`, `s_galois_correspondence`, `s_ramification_stratification_of_elliptic_curves`.
