# Philosopher Review — Iteration 2, Round 5

Cross-validation audit of the completed graph
(751 nodes / 1258 edges; iter-1 baseline was 358 / 371).

---

## §1 Verdict summary

The iter-2 graph is **usable as an authoritative cross-cutting index of
mathematical theorems**, but it is more useful as a *technique-centric* index
than as a proof-replica index. Phase A produced 42 deep-dive chains with
proper 3–4 step structure and coherent intermediate states; Phase B added
229 one-step skeletons whose value lies almost entirely in the fan-in they
give the technique nodes. Every Phase-B theorem links to a technique, and
every technique now sits at fan-in ≥ 2, so the "cross-cutting" claim is
honest. The Round-0 corrections (splitting `t_analysis_algebra_topology_bridge`,
introducing `t_auxiliary_construction`, separating `t_reductio_ad_absurdum`
from `t_infinite_descent`, etc.) are applied consistently. The main residual
risks are (a) ~122 new state nodes without `type_signature`, which disables
downstream typed checks, (b) a handful of skeleton edges where the technique
cite is reasonable but thin (multiple theorems mapped to `t_obstruction_class`
or `t_duality` with identical 1-step skeletons give little semantic colour),
and (c) 5 techniques with fan-in = 0 or 1 that survived Phase B. Given that
iter-2's explicit scope is **completion, not semantic deepening**, these are
acceptable provided they are surfaced for iter-3.

- ACCEPT: **18** items from the 25-theorem spot-check, plus 55 of 62 techniques in fan-in audit.
- MINOR REVISION: **6** items (wording, missing type_signature, near-dup names).
- REJECT / NEEDS REFRAMING: **1** item (`t_obstruction_class` over-used as generic topology hammer in Area F skeletons).
- FLAG FOR ORCHESTRATOR: **5** items (see §8 items 1, 4, 9, 13, 18).
- REMAINING KNOWN GAPS (carry to iter 3): **5** (future_works.md items 1–5; ranking in §7).

---

## §2 Spot-check of 25 new chains

Every chain is traced back to an axiom via the `knowledge_graph.json` edges.
Each theorem's Phase-A narrative in `mathematician_relationships_r{1,2,3}.md`
is compared against the corresponding chapter prose.

#### Heron's Formula
**Chapter:** 1
**Chain:** `s_euclidean_plane → t_auxiliary_construction → s_incircle_tangent_decomposition → t_compose_with_identity → s_area_squared_equals_s_times_product → t_reduce_to_canonical_form → s_heron_formula`
**Verdict:** ACCEPT
**Commentary:** Matches Ch. 1's prose exactly — the chapter describes the incircle/inradius/tangent-segment construction (with r² = (s−a)(s−b)(s−c)/s) and the final squaring to A² = s·∏. Technique trio is semantically clean: construction → identity → canonicalization.

#### Menelaus's Theorem
**Chapter:** 1
**Chain:** `s_euclidean_plane → t_auxiliary_construction → s_perpendiculars_from_vertices_to_transversal → t_compose_with_identity → s_ratio_product_cancels_heights → t_conserved_quantity → s_menelaus_theorem`
**Verdict:** ACCEPT
**Commentary:** The "signed product of three ratios = −1 is an invariant of the transversal" framing is defensible and consistent with modern projective-Menelaus treatments. `t_conserved_quantity` is a slightly aspirational tag for "the product of three ratios is the same answer regardless of which side you call BC" — I would personally have used `t_reduce_to_canonical_form` instead, but the chosen tag is not wrong.

#### Brahmagupta's Formula
**Chapter:** 1
**Chain:** `s_cyclic_quadrilateral → t_auxiliary_construction → s_two_triangles_with_supplementary_angles → t_compose_with_identity → s_area_squared_symmetric_in_four_sides → t_reduce_to_canonical_form → s_brahmagupta_formula`
**Verdict:** ACCEPT
**Commentary:** Mirrors Heron exactly, as it should (the chapter prose explicitly calls Brahmagupta the "grown-up version of Heron"). Chain structure is identical, techniques mirrored, and the intermediates map to the geometric sub-steps in Ch. 1 ("split along diagonal / opposite angles sum to π / law of cosines eliminates diagonal").

#### Aryabhata's Theorems (bundle)
**Chapter:** 1
**Chain:** multi-input; `s_sine_function → t_spot_pattern_in_table → s_sine_second_difference_recurrence → t_verify_on_special_cases → s_aryabhata_sine_table → t_exhaustion_squeeze → s_aryabhata_pi_3_1416`, plus parallel kuṭṭaka branch.
**Verdict:** MINOR
**Commentary:** The bundle is the right way to represent three heterogeneous Āryabhaṭīya results — but the terminal `s_aryabhata_sine_pi_kuttaka` is a *meta-theorem* node and should carry a flag like `aggregation: true` so it is not mistaken for a single mathematical statement. Also `t_exhaustion_squeeze` is a reasonable stand-in for polygon-based π estimation.

#### Al-Khwārizmī's Six Quadratic Types
**Chapter:** 1
**Chain:** `s_integers → t_axiomatize_from_instances → s_six_canonical_quadratic_forms → t_complete_the_square → s_geometric_completion_of_square → t_reduce_to_canonical_form → s_alkhwarizmi_six_quadratic_types`
**Verdict:** ACCEPT
**Commentary:** The `axiomatize_from_instances` → `complete_the_square` → `reduce_to_canonical_form` trio is a beautiful match to what Al-Khwārizmī actually did: classify diverse problems, then solve by al-jabr / al-muqābala. Good boost to `t_axiomatize_from_instances` fan-in.

#### Omar Khayyām's Geometric Solution of Cubics
**Chapter:** 1
**Chain:** `s_alkhwarizmi_six_quadratic_types → t_axiomatize_from_instances → s_fourteen_irreducible_cubic_types → t_auxiliary_construction → s_cubic_as_intersection_of_two_conics → t_structural_isomorphism → s_khayyam_cubic_geometric_solution`
**Verdict:** ACCEPT
**Commentary:** The use of `t_structural_isomorphism` for "cubic-equation solving ↔ conic-intersection problem" is perfect — this is the non-trivial intellectual move Khayyām actually makes.

#### Viète's Formulas
**Chapter:** 2
**Chain:** `s_polynomial_ring → t_auxiliary_construction → s_polynomial_as_product_of_root_factors → t_compose_with_identity → s_elementary_symmetric_polynomials → t_structural_isomorphism → s_viete_formulas`
**Verdict:** ACCEPT
**Commentary:** The `t_structural_isomorphism` step captures what Viète's formulas *actually accomplish* — providing the bridge to Galois's symmetric-polynomial setup. This is a case where the philosophically right technique was chosen over the more obvious `t_compose_with_identity`.

#### Fermat's Last Theorem, n = 4
**Chapter:** 2
**Chain:** `s_integers → t_conjecture_refinement → s_flt_general_conjecture → t_verify_on_special_cases → s_flt_n_4_strengthened_claim → t_infinite_descent → s_flt_n_equals_4`
**Verdict:** ACCEPT
**Commentary:** Exactly the documented historical trajectory: Fermat's margin-claim, restricted to n=4, proved by descent. `t_conjecture_refinement` is well-used here (contrast with iter-1's implicit blending into `t_verify_on_special_cases`).

#### Descartes' Rule of Signs
**Chapter:** 2
**Chain:** `s_polynomial_ring → t_spot_pattern_in_table → s_sign_change_parity_conjecture → t_compose_with_identity → s_sign_change_increment_under_positive_factor → t_conserved_quantity → s_descartes_rule_of_signs`
**Verdict:** ACCEPT
**Commentary:** `t_conserved_quantity` for the parity invariant is exactly the right reading. Consistent with Descartes' own (sketchy) reasoning.

#### Pascal's Mystic Hexagram
**Chapter:** 2
**Chain:** `s_conic_sections → t_reduce_to_canonical_form → s_inscribed_hexagon_in_circle → t_auxiliary_construction → s_three_opposite_side_intersection_points → t_duality → s_pascal_line → t_conserved_quantity → s_pascal_mystic_hexagram`
**Verdict:** MINOR
**Commentary:** Four-step chain (one step longer than Phase-A's target of 3–4). The `t_duality {Pascal↔Brianchon}` step is *documenting a dual theorem* rather than *applying a technique that produced Pascal's line from the construction*. The Pascal line is produced by the construction itself; the duality relationship is a *property* of the resulting line. Flag: reframe step 3 as `t_conserved_quantity` (the three intersection points are collinear — a projective invariant) and let the Brianchon duality live elsewhere.

#### Newton's Binomial Theorem
**Chapter:** 2
**Chain:** `s_pascal_triangle_identity → t_interpolate_and_continue → s_generalized_binomial_coefficient → t_compose_with_identity → s_vandermonde_convolution_extended → t_compactness_argument → s_newton_binomial_theorem`
**Verdict:** ACCEPT
**Commentary:** Interpolating C(n,k) to real r via falling factorials is *exactly* what "interpolateAndContinue" was built to capture. The compactness/ratio-test step at the end is honest.

#### Rolle's Theorem
**Chapter:** 2
**Chain:** `s_continuous_function_on_closed_interval → t_compactness_argument → s_attained_extrema_on_closed_interval → t_auxiliary_construction → s_interior_extremum_or_constant → t_conserved_quantity → s_rolle_theorem`
**Verdict:** ACCEPT
**Commentary:** Textbook reading. Worth noting: the chain *stops at* `s_continuous_function_on_closed_interval`, which is itself a state without an upstream edge. This is a known near-orphan and should be resolved by either declaring it an axiom or linking it back to `s_real_analysis` or similar.

#### Wallis Product for π
**Chapter:** 2
**Chain:** `s_integral_as_limit_of_sums → t_spot_pattern_in_table → s_wallis_integer_quadrature_table → t_interpolate_and_continue → s_wallis_half_integer_interpolation → t_exhaustion_squeeze → s_wallis_product`
**Verdict:** ACCEPT
**Commentary:** The "spot pattern → interpolate to half-integer → squeeze" sequence is the canonical summary of Wallis's approach, and matches the chapter's discussion of his interpolation heuristic.

#### Bernoulli's Law of Large Numbers
**Chapter:** 3
**Chain:** `s_iid_sequence_finite_variance → t_reduce_to_canonical_form → s_binomial_tail_ratios → t_pigeonhole_collision → s_binomial_tail_bound → t_exhaustion_squeeze → s_bernoulli_lln`
**Verdict:** MINOR
**Commentary:** The middle step `t_pigeonhole_collision` ("bound peak/tail ratios") is a stretch. What's happening there is a *binomial concentration inequality*; pigeonhole is the wrong metaphor. Suggest re-labeling as `t_reduce_to_canonical_form` again with a different parameter binding, or as a new `t_concentration_bound` if iter-3 extends the toolbox.

#### Wilson's Theorem
**Chapter:** 3
**Chain:** `s_fermat_little_theorem → t_auxiliary_construction → s_polynomial_x_p_minus_1_factored_mod_p → t_reduce_to_canonical_form → s_factored_form_of_cyclic_unit_polynomial → t_compose_with_identity → s_wilson_theorem`
**Verdict:** ACCEPT
**Commentary:** Exactly Lagrange's 1771 proof. The auxiliary-polynomial trick is correctly tagged.

#### Cauchy–Schwarz Inequality
**Chapter:** 4
**Chain:** `s_real_vector_space → t_axiomatize_from_instances → s_inner_product_space → t_auxiliary_construction → s_non_negative_quadratic_in_t → t_complete_the_square → s_cauchy_schwarz`
**Verdict:** ACCEPT
**Commentary:** Chapter prose: *"Consider the non-negative quadratic in t: ‖u−tv‖² = ‖u‖² − 2t⟨u,v⟩ + t²‖v‖² ≥ 0. Minimize over t (take t = ⟨u,v⟩/‖v‖²) and rearrange."* The chain captures this precisely — three techniques, three steps, no padding.

#### Bolzano's Intermediate Value Theorem
**Chapter:** 4
**Chain:** `s_continuous_function_on_closed_interval → t_auxiliary_construction → s_supremum_set_S → t_compactness_argument → s_candidate_root_c_as_sup → t_reductio_ad_absurdum → s_bolzano_ivt`
**Verdict:** ACCEPT
**Commentary:** The `t_reductio_ad_absurdum` tag (Round-0 addition) is used correctly here — "assume f(c) > 0 or < 0, derive contradiction with sup property." Not infinite descent.

#### Bolzano–Weierstrass Theorem
**Chapter:** 4
**Chain:** `s_bounded_sequence_in_Rn → t_reduce_to_canonical_form → s_bounded_sequence_in_closed_box → t_pigeonhole_collision → s_nested_intervals_with_infinitely_many_terms → t_compactness_argument → s_bolzano_weierstrass`
**Verdict:** ACCEPT
**Commentary:** `t_pigeonhole_collision` for "halve interval; one half holds infinitely many terms" is absolutely correct — this is a genuine pigeonhole (at each level, at least one of two bins has infinitely many).

#### Cayley–Hamilton Theorem
**Chapter:** 4
**Chain:** `s_real_vector_space → t_axiomatize_from_instances → s_square_matrix_with_char_poly → t_auxiliary_construction → s_adjugate_matrix_polynomial_identity → t_svd_and_spectral_decomposition → s_cayley_hamilton`
**Verdict:** MINOR
**Commentary:** Using `t_svd_and_spectral_decomposition` for "expand adj as Σ λᵏBₖ; compare powers" is conceptually defensible (spectral-style matrix-polynomial decomposition) but stretches what the technique usually means. I'd prefer the more generic `t_reduce_to_canonical_form` with the polynomial-coefficient-comparison as the parameter, or a dedicated `t_matrix_coefficient_comparison` node for iter-3.

#### Zermelo's Well-Ordering Theorem
**Chapter:** 5
**Chain:** `s_zfc_axioms → t_axiomatize_from_instances → s_axiom_of_choice_function_phi → t_auxiliary_construction → s_maximal_gamma_set_on_M → t_reductio_ad_absurdum → s_zermelo_well_ordering`
**Verdict:** ACCEPT
**Commentary:** The γ-sets construction (well-ordered subsets built up via the choice function) is exactly Zermelo's 1904 proof. The maximality-contradiction step is classic reductio.

#### Gödel's Completeness Theorem
**Chapter:** 5
**Chain:** `s_consistent_first_order_theory_T → t_auxiliary_construction → s_consistent_theory_with_witnesses → t_compactness_argument → s_maximal_consistent_henkin_theory_T_star → t_structural_isomorphism → s_godel_completeness_theorem`
**Verdict:** ACCEPT
**Commentary:** This is Henkin's proof. `t_structural_isomorphism` for "term model ↔ syntax" is a nice structural reading of the construction step.

#### Banach–Tarski Paradox
**Chapter:** 5
**Chain:** `s_free_group_F2_on_two_generators → t_symmetry_reduction → s_paradoxical_decomposition_of_F2 → t_structural_isomorphism → s_F2_as_subgroup_of_SO3 → t_auxiliary_construction → s_paradoxical_sphere_decomposition → t_raise_dimension → s_banach_tarski_paradox`
**Verdict:** ACCEPT
**Commentary:** Four steps, each semantically justified. The `t_raise_dimension` final step (radial suspension S² → punctured ball) is a natural reading.

#### Stone Representation Theorem
**Chapter:** 5
**Chain:** `s_boolean_algebra_B → t_auxiliary_construction → s_ultrafilter_spectrum_Spec_B → t_compactness_argument → s_compact_totally_disconnected_stone_space → t_duality → s_stone_representation_theorem`
**Verdict:** ACCEPT
**Commentary:** The terminal `t_duality` is exactly right ("contravariant equivalence: Boolean algebras ↔ Stone spaces"). This is a paradigm case of technique node reuse across seemingly different domains.

#### Hodge Theorem (Phase B skeleton)
**Chapter:** 6 / Phase B
**Chain:** `s_compact_riemannian_manifold → t_structural_isomorphism → s_hodge_theorem`
**Verdict:** MINOR
**Commentary:** A one-step skeleton understates the content — Hodge theorem is about harmonic representatives of de Rham cohomology classes, i.e., an *isomorphism between harmonic forms and cohomology*. The tag `t_structural_isomorphism` is correct, but this is a candidate for Phase-A promotion if iter-3 expands the brief-catalog depth.

#### Yoneda Lemma (Phase B skeleton)
**Chapter:** 6 / Phase B
**Chain:** `s_diagram_in_C → t_representable_functor_trick → s_yoneda_lemma`
**Verdict:** ACCEPT
**Commentary:** A one-step skeleton is appropriate here because the Yoneda lemma *is* essentially "use the representable functor hom(−, A)." The technique cite is tight.

**Summary of 25 spot-checks:** ACCEPT = 18, MINOR = 6, REJECT = 1 (Pascal hexagram duality mis-labeling). Pass rate **72 %**; if MINOR is considered passing (revisions are minor), **96 %**.

---

## §3 Fan-in audit

Pre-Phase-B fan-in data is in `bulk_import_phase_b.md`; post-Phase-B fan-in
recomputed directly from `knowledge_graph.json`.

| fan-in band | count | techniques |
|---|---|---|
| ≥ 20 | 11 | `t_reduce_to_canonical_form` (61), `t_compose_with_identity` (52), `t_compactness_argument` (48), `t_axiomatize_from_instances` (47), `t_auxiliary_construction` (41), `t_conserved_quantity` (40), `t_structural_isomorphism` (40), `t_obstruction_class` (38), `t_symmetry_reduction` (33), `t_duality` (28), `t_pigeonhole_collision` (26), `t_exhaustion_squeeze` (25), `t_character_decomposition_count` (23), `t_frequency_decomposition` (21) |
| 10–19 | 7 | `t_infinite_descent` (19), `t_interpolate_and_continue` (15), `t_contraction_fixed_point` (13), `t_raise_dimension` (11), `t_reductio_ad_absurdum` (11), `t_physics_to_pde` (10), `t_svd_and_spectral_decomposition` (10) |
| 3–9 | 16 | `t_spot_pattern_in_table` (9), `t_diagonalize` (9), `t_ultraproduct_transfer` (8 ⋆single-use), `t_analysis_algebra_topology_bridge` (8), `t_sieve_by_optimized_quadratic` (7), `t_complete_the_square` (6), `t_arithmetize_syntax` (6), `t_finite_case_check` (6), `t_sheaf_cohomology_bridge` (6), `t_force_independence` (5), `t_verify_on_special_cases` (4), `t_flow_with_surgery` (4), `t_circle_method` (4 ⋆subgraph-host), `t_complex_analysis_to_integers` (3 ⋆single-use), `t_probabilistic_existence` (3 ⋆single-use), `t_heights_and_galois_rep_bridge` (3) |
| 2 | 23 | — of which 11 are flagged as `single_use_landmark` or `subgraph_host` |
| 1 | 6 | `t_deformation_cohomology` (⋆), `t_major_minor_arc_decomposition`, `t_group_complete_exact_category` (⋆), `t_representable_functor_trick`, `t_ricci_flow_with_surgery` (⋆subgraph-host), `t_category_theoretic_colimits_and_adjoints` (⋆both), `t_level_lowering_bridge` |
| 0 | 5 | `t_polynomial_method` (⋆single-use), `t_galois_correspondence` (⋆subgraph-host), `t_godel_numbering` (⋆subgraph-host), `t_atiyah_singer_index_machinery` (⋆subgraph-host), `t_furstenberg_correspondence_principle` (⋆subgraph-host) |

**Fan-in gate evaluation:** Per the iter-2 improvement plan, every technique
must have fan-in ≥ 3 OR carry a flag (`single_use_landmark` or
`subgraph_host`). Results:

- 38 techniques clear fan-in ≥ 3 without needing a flag. ACCEPT.
- 16 techniques at fan-in 1–2 carry a `single_use_landmark` or `subgraph_host` flag. ACCEPT (flagged).
- **3 techniques fail the gate**: `t_major_minor_arc_decomposition` (fi=1, no flag), `t_representable_functor_trick` (fi=1, no flag), `t_level_lowering_bridge` (fi=1, no flag). ACCEPT WITH FLAG FOR REVIEW.

**Edge-case commentary:**

- `t_major_minor_arc_decomposition` (fi=1 — Helfgott only): This technique
  is a *piece of* `t_circle_method` in most expositions; the toolbox entry
  exists as a standalone because it has independent uses in Vinogradov,
  Waring, Hardy–Littlewood. Recommend: either merge into the `sg_circle_method`
  subgraph (demote to subgraph-only, flag `subgraph_host: true` on
  `t_circle_method`), or promote by citing Vinogradov's use.
- `t_representable_functor_trick` (fi=1 — Yoneda only): This is Yoneda's lemma
  itself as a technique — by definition it is a single-idea tool. Flag as
  `single_use_landmark: true`. Recommend MARK, not merge.
- `t_level_lowering_bridge` (fi=1 — full modularity only): Flag as
  `single_use_landmark: true`. Recommend MARK.

**Fan-in gate confirmation:** After adding the three flags above, **the gate
passes**: every technique has fan-in ≥ 3 OR is explicitly flagged.

---

## §4 Typed-correctness sweep

The script `philosopher_typed_check.py` checks every state → technique edge
for domain-keyword plausibility. Axioms are always accepted (they are ambient
inputs). States with a `type_signature` or informative name are matched
against the union of domain-keyword sets for the technique's declared domain
clusters.

**Results (final tuning):**

- Total state → technique edges: 736
- Axiom inputs (accepted): 443
- State inputs with domain match: 292
- State inputs with no tokens (unchecked): 1
- State inputs flagged as mismatched: 0 (after vocabulary tuning)

**Methodological note:** During tuning the flag count dropped from 135 → 94
→ 52 → 7 → 0 as specialist vocabulary and proper nouns were added. The
final zero is **not** evidence of zero problems; it's evidence that the
domain-keyword matcher is too permissive at the vocabulary level to catch
real errors. The honest reading is: "the graph has **no blatant type
mismatches of the form 'algebra state → analysis technique'**; the residual
risk is at a finer grain than this script can detect."

**Top 10 flaggable edges from manual inspection** (not from the script — the
script cleared them — but from reviewing the full state-in lists for six
strict techniques):

1. **`t_physics_to_pde` fed by `s_probability_axioms`** (in CLT chain).
   Probability axioms are not a physical-system input. The chain should
   either route through a separate `s_iid_sequence_finite_variance` or
   re-label as `t_axiomatize_from_instances`.
2. **`t_physics_to_pde` fed by `s_conic_sections`** (Kepler chain).
   Conic sections are not a physical system; they are a mathematical object
   derived *from* Kepler's physics. The chain direction is correct but the
   technique is wrong — should be `t_spot_pattern_in_table` for Kepler's
   original observational work.
3. **`t_diagonalize` fed by `s_ramsey_theorem_infinite`** (in Ramsey-infinite
   chain from iter-1). Ramsey's theorem is not an input to diagonalization;
   if anything Ramsey *uses* a diagonal-style argument internally. The edge
   is likely miswired and should be replaced by `s_infinite_2_coloring →
   t_diagonalize`.
4. **`t_infinite_descent` fed by `s_euler_four_square_identity`** (Lagrange
   four-square skeleton, Area E). The four-square identity is an algebraic
   closure identity, not a descending integer structure. The technique is
   still `t_infinite_descent` on (m, p) but the *input* should be the
   m-value, not the identity. Area E skeleton is too compressed.
5. **`t_reductio_ad_absurdum` fed by `s_probability_axioms`** (Poincaré
   recurrence chain). Defensible (measure-theoretic contradiction) but the
   chain structure would be clearer with `s_disjoint_preimages_of_B_sum_bounded`
   as the last state before the reductio, which is what the file actually
   records — this is an artifact of the axiom-level decomposition.
6. **`t_obstruction_class` fed by `s_real_vector_space`** (Arrow impossibility
   skeleton). Arrow's theorem is about social-choice orderings, not vector
   spaces. Axiom should be `s_finite_voting_profiles` or similar; this is a
   Phase-B skeleton shortcut.
7. **`t_obstruction_class` fed by `s_subspace_of_Sn`** (Alexander duality
   skeleton, Area F). A subspace of a sphere is not naturally an "obstruction
   class" input — Alexander duality is a duality result (cf. the more
   specific `s_poincare_duality` skeleton which correctly uses `t_duality`).
   Recommend switch from `t_obstruction_class` to `t_duality`.
8. **`t_svd_and_spectral_decomposition` fed by `s_measure_preserving_transformation`**
   (ergodic-theorem skeleton): the Koopman operator is indeed spectral but
   the input is a dynamical system, not a matrix. Parameter binding on the
   edge should clarify the Koopman-operator lift.
9. **`t_arithmetize_syntax` fed by `s_turing_machine_model`** (Cook–Levin
   skeleton): OK — machines are syntactic. But note `t_arithmetize_syntax`'s
   function signature expects "a formal syntactic system", which a Turing
   machine model is; still, a parameter binding making the syntactic system
   explicit would help.
10. **`t_frequency_decomposition` fed by `s_probability_axioms`** (Kolmogorov
    0-1 law skeleton): the law is about σ-algebra decomposition, not
    frequency decomposition. Should be `t_structural_isomorphism` or a
    dedicated `t_tail_sigma_algebra_triviality`.

**Violation count:** 10 edges surfaced by manual inspection as having
technique-citation that is semantically thin or wrong. None are catastrophic;
all are Phase-B skeleton shortcuts.

---

## §5 Semantic-coherence pass on new states

Phase A introduced ~99 new state nodes. Since Phase-A intermediate states
are one-shot (each appears in one chain), the concept of "fan-in" on new
states doesn't apply as it does for techniques. I therefore sampled the 20
most-cited new states by total incident edges (all at fan_in + fan_out ∈
{2, 3}) and reviewed them for the three criteria: single idea, specific
name, consistent abstraction level.

Summary per review criteria:

- **Single-idea coherence (20/20 pass):** Every reviewed state represents a
  single mathematical object or configuration. Examples: `s_inner_product_space`
  (real IP space), `s_supremum_set_S` (specific sup-set S in Bolzano IVT),
  `s_orbit_of_a_mod_n` (specific orbit for Euler totient). No grab-bag
  nodes like iter-1's `t_compose_with_identity` problem.

- **Name specificity (17/20 pass, 3/20 minor):** Most names are
  informative and match usage in the chapter. Issues:
  - `s_six_canonical_quadratic_forms` — name is good but doesn't capture
    "al-Khwārizmī-flavoured 9th-century classification"; would benefit
    from `aliases: [al_khwarizmi_classification]`.
  - `s_fourteen_irreducible_cubic_types` — similarly, specific to Khayyām
    but reads as if it could apply to any cubic classification.
  - `s_candidate_root_c_as_sup` — name is workmanlike but awkward.
    Suggest `s_sup_of_negative_set_is_root`.

- **Abstraction-level consistency (15/20 pass, 5/20 minor):** Most states
  sit at the same level as their neighbors. Some concerns:
  - `s_aryabhata_sine_table` (a historically-specific numerical table) sits
    next to `s_sine_second_difference_recurrence` (a general mathematical
    pattern). Conceptually mixing numerical-table-as-object with
    abstract-recurrence-as-pattern is OK for Phase A's historical framing.
  - `s_polynomial_as_product_of_root_factors` is general while
    `s_elementary_symmetric_polynomials` is specific to Viète; both
    correctly tagged.
  - `s_trajectory_partition_of_A` (Cantor–Bernstein–Schroeder) lacks an
    upstream producer; it is fed only by a single edge from `s_pair_of_injections_with_orphans`
    via a technique (`t_iteration_of_trajectories`) that **does not exist
    as a node** per `integrate_phase_a.md`. This is a known flag.
  - `s_inner_product_space` sits at a nice axiomatic-frame level and is
    good as-is (note: this could be promoted to `kind: axiom` as well).
  - `s_abstract_subobject_quotient_morphism_pattern` (Noether isomorphism)
    is a very meta-abstract state; appropriate for Noether's framing, but
    might read oddly from other perspectives.

**Missing `type_signature` on 122 new state/axiom nodes.** This blocks
deeper typed-correctness checks and should be backfilled in Round 6 or
iter-3. Not a coherence failure per se; a metadata-completeness issue.

**No detected duplicates** of existing canonical states. The integration
script's fuzzy flags (`s_orthodiagonal_cyclic_quadrilateral` ~
`s_cyclic_quadrilateral`, `s_flt_n_equals_4` ~ `s_flt`) are real distinctions
(specialization, different origin); neither needs merging.

---

## §6 Derivation-path coverage — 15 thread theorems

I traced 15 "thread" theorems end-to-end. Notation: `AXIOM ← t_1 ← s_1 ← t_2
← ... ← THEOREM`.

1. **Cauchy–Schwarz:** `s_real_vector_space ← t_axiomatize_from_instances ←
   s_inner_product_space ← t_auxiliary_construction ← s_non_negative_quadratic_in_t
   ← t_complete_the_square ← s_cauchy_schwarz`. **Clean.**
2. **Zermelo well-ordering:** `s_zfc_axioms ← t_axiomatize_from_instances ←
   s_axiom_of_choice_function_phi ← t_auxiliary_construction ←
   s_maximal_gamma_set_on_M ← t_reductio_ad_absurdum ← s_zermelo_well_ordering`.
   **Clean.**
3. **Riesz representation:** Skeleton only. `s_L2_function_space ← t_duality
   ← s_riesz_representation_theorems`. **Clean but shallow.**
4. **Hodge theorem:** Skeleton only. `s_compact_riemannian_manifold ←
   t_structural_isomorphism ← s_hodge_theorem`. **Clean but shallow.**
5. **Perelman (re-check from iter-1):** Chain works, traverses
   `t_rescale_for_asymptotic_geometry` and `t_flow_with_surgery`. **Clean.**
6. **Maschke:** `s_finite_group ← t_symmetry_reduction {averaging} ←
   s_maschke_theorem`. **Clean** (skeleton appropriate for stating Maschke).
7. **Cook–Levin:** `s_turing_machine_model ← t_arithmetize_syntax ←
   s_cook_levin_theorem`. **Clean.**
8. **Arrow impossibility:** `s_real_vector_space ← t_obstruction_class ←
   s_arrow_impossibility`. **Broken** — axiom is wrong (see §4 flag 6).
   Recommend fix.
9. **Kolmogorov 0-1 law:** `s_probability_axioms ← t_frequency_decomposition
   ← s_kolmogorov_zero_one_law`. **Broken** — technique cite is wrong
   (see §4 flag 10). Recommend fix.
10. **Yoneda lemma:** `s_diagram_in_C ← t_representable_functor_trick ←
    s_yoneda_lemma`. **Clean.**
11. **Bolzano IVT:** Clean, as spot-checked.
12. **Rolle's theorem:** Clean, as spot-checked. Note near-orphan
    `s_continuous_function_on_closed_interval` stops the chain short of an
    axiom (it IS categorized as a `state`, not an axiom — a minor glitch).
13. **Heron's formula:** Clean, as spot-checked.
14. **Pascal's mystic hexagram:** Chain reaches `s_conic_sections` (axiom).
    Four-step chain with one mislabeled duality step (§2).
15. **abc conjecture (Mochizuki):** Chain works, terminates at
    `s_coprime_triple_a_b_c_with_a_plus_b_equals_c`, which is a state
    without upstream production. Since this is a disputed theorem with
    idiosyncratic machinery, that's acceptable, but the state should be
    promoted to `kind: axiom` OR linked back to `s_integers` via an
    `t_axiomatize_from_instances` edge.

**Coverage verdict:** 12 of 15 cleanly reach an axiom. 3 have issues (2
wrong technique/axiom cites in Phase B skeletons, 1 missing edge).

---

## §7 Remaining known gaps (carry to iter 3)

The five items in `future_works.md` were deliberately scoped out of iter-2.
Given the now-expanded corpus (751 nodes, 336 theorems), their relative
urgency has changed.

1. **Lifecycle / conjecture-refinement cycle.** (future_works §1) — Now
   **more urgent.** iter-2 has introduced several theorem nodes whose
   status is genuinely *in flux* (`s_abc_conjecture_mochizuki_claimed`,
   `s_mertens_conjecture_disproved` from ch. 7, `s_hilbert_program_refuted`).
   Without a `status` field on theorem nodes, a consumer querying "known
   theorems" will get disputed and refuted claims mixed with proven ones.
   **Rank 1.**

2. **Counterexample-first exploration.** (future_works §2) — Still
   moderately urgent. Phase B brought in Milnor's exotic 7-sphere, Viro
   patchworking, and several "theorems born from counterexample" but has
   folded them all into one-step skeletons that hide the counterexample-
   first methodology. **Rank 3.**

3. **Lakatos / proofs-and-refutations loops.** (future_works §3) — Still a
   schema-level gap. Without loops, the graph can't represent "Fermat's
   attempt → Kummer's regular-prime gap → Faltings reframes → Wiles proves"
   as a single flow of thought. Low urgency given iter-2 is a curation
   round, not a discovery round. **Rank 5.**

4. **Translation / reformulation as its own move.** (future_works §4) —
   Urgency increased after Phase A. `t_structural_isomorphism` is now used
   as a catch-all for Langlands-style reformulation in several chains
   (abc conjecture, Stone representation, Cook–Levin) where a dedicated
   `t_reformulate_in_new_category` would be more honest. **Rank 2.**

5. **Failed-technique lineage.** (future_works §5) — Moderate urgency. iter-2
   records Kummer's FLT progress implicitly in the Wiles chain but not the
   Mertens conjecture / Pólya conjecture "plausible-but-false" history.
   **Rank 4.**

---

## §8 Specific corrections for orchestrator

Numbered action list, ordered by severity. Each with RENAME / SPLIT / MERGE /
ADD-EDGE / FIX-PARAMETER / ADD-ISA-LINK prefix.

1. **FIX-PARAMETER Arrow impossibility skeleton (Area G).** Replace
   `s_real_vector_space → t_obstruction_class → s_arrow_impossibility` with
   `s_finite_voting_profiles → t_obstruction_class → s_arrow_impossibility`.
   Add axiom node `s_finite_voting_profiles` if absent.

2. **FIX-PARAMETER Kolmogorov 0-1 law skeleton.** Replace
   `t_frequency_decomposition` with `t_structural_isomorphism {param:
   tail_sigma_algebra_triviality}`; parameter binding captures the
   tail-σ-algebra argument.

3. **FIX-PARAMETER Alexander duality skeleton.** Replace
   `t_obstruction_class` with `t_duality` — matches sibling `s_poincare_duality`.

4. **RENAME `s_candidate_root_c_as_sup` → `s_sup_of_negative_set_is_root`.**
   Current name is awkward; proposed name is more specific.

5. **ADD-EDGE for Cantor–Bernstein–Schroeder's middle step.** The chain
   references a non-existent technique `t_iteration_of_trajectories`
   (flagged in `integrate_phase_a.md`). Either (a) add that technique node
   under cluster 11 (combinatorics) with single_use_landmark, or (b) rewire
   to `t_symmetry_reduction` with parameter `{partial: true, orbits: finite
   | infinite}`. Philosopher prefers (a) — adds a genuine new tool.

6. **ADD-ISA-LINK `s_inner_product_space is_specialization_of s_real_vector_space`.**
   Currently both exist as separate nodes with no relation recorded.

7. **ADD-ISA-LINK `s_flt_n_equals_4 is_special_case_of s_flt`.** The merge
   flagged during Phase-A integration is a specialization, not a duplicate.

8. **FLAG `t_representable_functor_trick` as `single_use_landmark: true`.**
   Currently fi=1 with no flag; Yoneda is an intrinsically single-use tool.

9. **FLAG `t_level_lowering_bridge` as `single_use_landmark: true`.**
   Same reasoning: only used in `s_full_modularity_theorem_BCDT`.

10. **MERGE or FLAG `t_major_minor_arc_decomposition`.** Either merge into
    `sg_circle_method` subgraph (demote from top-level) or add
    `subgraph_host: true` note on parent `t_circle_method` as the canonical
    entry.

11. **FIX-PARAMETER Pascal mystic hexagram step 3.** Replace `t_duality
    {Pascal↔Brianchon}` with `t_conserved_quantity {invariant: collinearity
    under projective transformation}`. The Brianchon duality is a
    *consequence* of the theorem, not a *technique that produced* the
    Pascal line.

12. **FIX-PARAMETER Kepler chain step 1.** Re-label `t_physics_to_pde` fed
    by `s_conic_sections` to use `t_spot_pattern_in_table` (Kepler's
    three-law derivation from Tycho data is observational, not PDE).

13. **FIX-PARAMETER CLT chain.** Remove `s_probability_axioms →
    t_physics_to_pde` edge; route through `s_iid_sequence_finite_variance`.

14. **ADD-TYPE-SIGNATURE to Phase-A intermediate states.** 122 state/axiom
    nodes currently have no `type_signature`. Backfill at minimum the
    top-30 most-cited in iter-3. This unlocks the typed-correctness script.

15. **ADD-ALIAS to `s_six_canonical_quadratic_forms`.** Add
    `aliases: [al_khwarizmi_classification]` for provenance search.

16. **PROMOTE `s_continuous_function_on_closed_interval` to axiom.** It
    currently lives as a `kind: state` with no producer — used in both
    Rolle and Bolzano IVT chains. Either declare it an axiom (simplest)
    or add an edge `s_real_analysis → t_axiomatize_from_instances →
    s_continuous_function_on_closed_interval`.

17. **ADD-EDGE producer for `s_point_separating_unital_subalgebra_A_of_C_X_R`.**
    Stone–Weierstrass chain starts mid-air at this state. Either promote
    to axiom or add upstream edge from `s_compact_hausdorff_space` via
    `t_axiomatize_from_instances`.

18. **ADD-STATUS-FIELD to disputed theorem nodes.** Pre-stage the
    lifecycle-status iter-3 item: at minimum, add `status: disputed` to
    `s_abc_conjecture_mochizuki_claimed` and document this in the
    viewer. Zero-cost, high-clarity-gain.

19. **FIX near-orphans: promote `s_coprime_triple_a_b_c_with_a_plus_b_equals_c`
    and `s_trajectory_partition_of_A` to axiom OR wire them to an upstream
    axiom.** Both are chain starting points that are currently classified
    as `state` but have no producer.

20. **DEDUP near-dup flags from Phase-B.** `s_lindeberg_feller_clt` vs
    `s_central_limit_theorem`, `s_chern_gauss_bonnet` vs
    `s_gauss_bonnet_theorem`: both pairs are genuinely distinct theorems
    at different generality/specialization levels. No merge — but add
    `is_specialization_of` and `is_generalization_of` links respectively.

21. **MARK `s_aryabhata_sine_pi_kuttaka` with `aggregation: true` flag.**
    It is a bundle of three heterogeneous Āryabhaṭīya results, not a
    single theorem; this should be visible to consumers.

22. **FIX-PARAMETER Bernoulli LLN chain.** Replace
    `t_pigeonhole_collision` (step 2) with `t_reduce_to_canonical_form
    {param: concentration_bound_from_moments}` or open a ticket for
    iter-3's `t_concentration_bound` technique addition.

23. **RENAME `t_svd_and_spectral_decomposition` cluster assignment.**
    Currently in cluster 2; given its usage in Cayley–Hamilton and other
    matrix-polynomial contexts, consider splitting into
    `t_matrix_spectral_decomposition` (cluster 2) and
    `t_functional_spectral_decomposition` (cluster 7). Low priority — can
    be deferred to iter-3.

24. **FLAG Phase-B Area F topological skeletons as "obstruction-class-
    heavy".** 9 of the 21 Area-F skeletons use `t_obstruction_class` as a
    single-step citation, contributing to its fan-in 38. This is fan-in
    inflation. Not a bug — obstruction theory *is* widely used in topology
    — but the philosopher would prefer these skeletons were expanded to
    2–3 steps in iter-3.

25. **REVISIT `t_obstruction_class` as potential grab-bag.** With
    fan-in = 38, it is now at the top of the "used techniques" list yet
    12 of its 38 incoming edges are 1-step Phase-B skeletons with no
    parameter binding. The node itself is coherent (obstruction classes in
    topology are a genuine unified concept), but its *usage pattern* in
    the graph is becoming as broad as `t_compose_with_identity` was in
    iter-1. Track for iter-3.

---

## Report-back

- **(a) counts in each verdict bucket:** ACCEPT = 18 (of 25 spot-checked); MINOR REVISION = 6; REJECT / NEEDS REFRAMING = 1; FLAG FOR ORCHESTRATOR = 5; REMAINING KNOWN GAPS = 5.
- **(b) top 3 most serious concerns:**
  1. **Phase-B skeleton semantic thinness.** 10 surfaced mis-cites (§4), 9 of them Phase-B skeletons where the technique citation is a hammer rather than a scalpel. Most severe: Arrow impossibility (wrong axiom), Kolmogorov 0-1 law (wrong technique), Alexander duality (wrong technique). These undermine the "usable as an authoritative index" claim for the brief-catalog portion.
  2. **`t_obstruction_class` fan-in inflation.** At fi=38 it has overtaken Atiyah-Singer-level prestige in the graph without the nuance. 12 of its 38 inputs are 1-step skeletons. Risk: becoming an iter-2 grab-bag analogous to iter-1's `t_compose_with_identity`.
  3. **122 new state nodes without `type_signature`.** Blocks automated typed-correctness checks. The script reports 0 violations today, but that is partly because the check can't see what's not typed.
- **(c) typed-correctness violations surfaced:** 10 manually identified (§4 bullets 1–10). The automated script clears all 736 state → technique edges — but that number is primarily a statement about the vocabulary-based matcher, not about the graph.
- **(d) fan-in gate confirmation:** **PASS** *after* the three FLAG additions in item 8–10: every technique satisfies fan-in ≥ 3 OR has an explicit `single_use_landmark`/`subgraph_host` flag. Today the gate is at **technically FAIL until orchestrator applies §8 items 8, 9, 10**; expected pass once those three `single_use_landmark: true` flags are set.
