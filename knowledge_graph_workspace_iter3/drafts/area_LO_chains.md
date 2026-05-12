# Area Logic & Foundations Derivation Chains (iter-3)

**Source pages:**
- https://en.wikipedia.org/wiki/List_of_mathematical_logic_topics
- https://en.wikipedia.org/wiki/Category:Theorems_in_mathematical_logic
- https://en.wikipedia.org/wiki/Category:Theorems_in_set_theory
- https://en.wikipedia.org/wiki/Category:Theorems_in_model_theory
- https://en.wikipedia.org/wiki/Category:Theorems_in_computability_theory
- https://en.wikipedia.org/wiki/Category:Theorems_in_proof_theory

**Target:** 70 chains. **Drafted:** 85. **Skipped (already in graph):** 5 — `s_godel_incompleteness`, `s_ch_independent_of_zfc`, `s_con_zfc_gch`, `s_undecidability_of_halting`, `s_uncountability_of_reals`. Additionally assumed already-in-graph from iter-2 chapter 07 work (Compactness, Löwenheim–Skolem, Church–Rosser, Łoś, Craig interpolation, Lindström, Morley categoricity, Borel determinacy, Cohen forcing, MRDP, Paris–Harrington, Gentzen consistency, AC equivalents, Schröder–Bernstein) — not re-derived here.

**Flagged (`⚠ needs new technique`):** 0.

---

### Tennenbaum's theorem (cite: https://en.wikipedia.org/wiki/Tennenbaum%27s_theorem)

**Axioms:** `s_first_order_peano_arithmetic`, `s_turing_machine_model`
**Terminal:** `s_tennenbaum_theorem` (kind: theorem) — no countable non-standard model of PA has computable +, ·.

**Steps:**
1. input: `s_first_order_peano_arithmetic` --[t_auxiliary_construction {object: countable_nonstandard_model_M}]--> output: `s_countable_nonstandard_model_of_PA`
2. input: `s_countable_nonstandard_model_of_PA` --[t_arithmetize_syntax {target: separable_disjoint_re_sets_A_B}]--> output: `s_re_inseparable_pair_coded_in_M`
3. input: `⟨s_re_inseparable_pair_coded_in_M, s_turing_machine_model⟩` --[t_reductio_ad_absurdum {assume: plus_times_computable_on_M}]--> output: `s_recursive_separation_contradiction`
4. input: `s_recursive_separation_contradiction` --[t_diagonalize {against: alleged_recursive_addition_table}]--> output: `s_tennenbaum_theorem`

**Techniques used:** t_auxiliary_construction, t_arithmetize_syntax, t_reductio_ad_absurdum, t_diagonalize

---

### Goodstein's theorem (cite: https://en.wikipedia.org/wiki/Goodstein%27s_theorem)

**Axioms:** `s_zfc_axioms`, `s_ordinal_arithmetic_below_epsilon_0`
**Terminal:** `s_goodstein_theorem` (kind: theorem) — every Goodstein sequence terminates at 0.

**Steps:**
1. input: `s_natural_number_n` --[t_reduce_to_canonical_form {form: hereditary_base_b_representation}]--> output: `s_goodstein_sequence_definition`
2. input: `s_goodstein_sequence_definition` --[t_structural_isomorphism {map: parallel_ordinal_in_cantor_normal_form}]--> output: `s_ordinal_majorant_sequence_below_epsilon_0`
3. input: `s_ordinal_majorant_sequence_below_epsilon_0` --[t_infinite_descent {wellorder: epsilon_0}]--> output: `s_ordinal_sequence_must_hit_zero`
4. input: `s_ordinal_sequence_must_hit_zero` --[t_exhaustion_squeeze {bound: goodstein_below_ordinal_majorant}]--> output: `s_goodstein_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_structural_isomorphism, t_infinite_descent, t_exhaustion_squeeze

---

### Goodstein independence from PA (Kirby–Paris) (cite: https://en.wikipedia.org/wiki/Goodstein%27s_theorem#Proof_of_Goodstein.27s_theorem)

**Axioms:** `s_first_order_peano_arithmetic`, `s_goodstein_theorem`
**Terminal:** `s_kirby_paris_independence` (kind: theorem) — Goodstein's theorem is unprovable in PA.

**Steps:**
1. input: `⟨s_first_order_peano_arithmetic, s_goodstein_theorem⟩` --[t_arithmetize_syntax {encode: total_function_Goodstein_terminates}]--> output: `s_total_function_growth_of_Goodstein`
2. input: `s_total_function_growth_of_Goodstein` --[t_reduce_to_canonical_form {to: hardy_hierarchy_at_epsilon_0}]--> output: `s_hardy_hierarchy_majorant_at_epsilon_0`
3. input: `s_hardy_hierarchy_majorant_at_epsilon_0` --[t_force_independence {against: provably_recursive_functions_of_PA}]--> output: `s_kirby_paris_independence`

**Techniques used:** t_arithmetize_syntax, t_reduce_to_canonical_form, t_force_independence

---

### Kirby–Paris hydra theorem (cite: https://en.wikipedia.org/wiki/Hydra_game)

**Axioms:** `s_finite_rooted_tree`, `s_ordinal_arithmetic_below_epsilon_0`
**Terminal:** `s_hydra_theorem` (kind: theorem) — every hydra strategy terminates; PA cannot prove this.

**Steps:**
1. input: `s_finite_rooted_tree` --[t_reduce_to_canonical_form {form: hydra_with_labelled_heads}]--> output: `s_hydra_game_state`
2. input: `s_hydra_game_state` --[t_structural_isomorphism {invariant: ordinal_rank_below_epsilon_0}]--> output: `s_hydra_ordinal_invariant`
3. input: `s_hydra_ordinal_invariant` --[t_infinite_descent {wellorder: epsilon_0}]--> output: `s_hydra_terminates`
4. input: `s_hydra_terminates` --[t_force_independence {target: PA}]--> output: `s_hydra_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_structural_isomorphism, t_infinite_descent, t_force_independence

---

### Kanamori–McAloon theorem (cite: https://en.wikipedia.org/wiki/Kanamori%E2%80%93McAloon_theorem)

**Axioms:** `s_first_order_peano_arithmetic`, `s_ramsey_theorem_infinite`
**Terminal:** `s_kanamori_mcaloon_theorem` (kind: theorem) — a regressive-coloring Ramsey statement true but unprovable in PA.

**Steps:**
1. input: `s_ramsey_theorem_infinite` --[t_conjecture_refinement {to: regressive_finite_Ramsey}]--> output: `s_regressive_finite_ramsey_statement`
2. input: `s_regressive_finite_ramsey_statement` --[t_arithmetize_syntax {witness: indicator_function_for_PA}]--> output: `s_indicator_for_PA_models`
3. input: `s_indicator_for_PA_models` --[t_force_independence {target: PA}]--> output: `s_kanamori_mcaloon_theorem`

**Techniques used:** t_conjecture_refinement, t_arithmetize_syntax, t_force_independence

---

### Kreisel's basis theorem (cite: https://en.wikipedia.org/wiki/Basis_theorem_(computability))

**Axioms:** `s_pi_0_1_class_of_reals`, `s_turing_machine_model`
**Terminal:** `s_kreisel_basis_theorem` (kind: theorem) — every nonempty Π⁰₁ class has a member of low Turing degree (i.e., recursive in 0′).

**Steps:**
1. input: `s_pi_0_1_class_of_reals` --[t_reduce_to_canonical_form {form: infinite_binary_tree_with_recursive_branching}]--> output: `s_recursive_binary_tree_T`
2. input: `s_recursive_binary_tree_T` --[t_compactness_argument {space: cantor_space}]--> output: `s_existence_of_infinite_branch`
3. input: `s_existence_of_infinite_branch` --[t_auxiliary_construction {use: leftmost_path_definable_from_0_prime}]--> output: `s_leftmost_branch_recursive_in_0_prime`
4. input: `s_leftmost_branch_recursive_in_0_prime` --[t_projection_to_subspace {project: to_low_degree}]--> output: `s_kreisel_basis_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_compactness_argument, t_auxiliary_construction, t_projection_to_subspace

---

### Hyperarithmetic hierarchy theorem (cite: https://en.wikipedia.org/wiki/Hyperarithmetical_theory)

**Axioms:** `s_turing_jump_operator`, `s_recursive_ordinal`
**Terminal:** `s_hyperarithmetic_hierarchy` (kind: theorem) — the hyperarithmetic sets coincide with Δ¹₁ and are stratified by recursive ordinals.

**Steps:**
1. input: `s_turing_jump_operator` --[t_interpolate_and_continue {along: recursive_ordinals}]--> output: `s_transfinite_jump_hierarchy_H_a`
2. input: `s_transfinite_jump_hierarchy_H_a` --[t_structural_isomorphism {to: delta_1_1_sets}]--> output: `s_delta_1_1_equals_hyperarithmetic`
3. input: `s_delta_1_1_equals_hyperarithmetic` --[t_diagonalize {against: each_level}]--> output: `s_strict_hyperarithmetic_hierarchy`
4. input: `s_strict_hyperarithmetic_hierarchy` --[t_reduce_to_canonical_form {to: kleene_O_indexing}]--> output: `s_hyperarithmetic_hierarchy`

**Techniques used:** t_interpolate_and_continue, t_structural_isomorphism, t_diagonalize, t_reduce_to_canonical_form

---

### Friedman's finite gap (Kruskal-style) theorem (cite: https://en.wikipedia.org/wiki/Kruskal%27s_tree_theorem)

**Axioms:** `s_finite_labelled_trees`, `s_wqo_axioms`
**Terminal:** `s_friedman_finite_form_kruskal` (kind: theorem) — a finitary form of Kruskal's tree theorem is unprovable in ATR₀.

**Steps:**
1. input: `s_finite_labelled_trees` --[t_axiomatize_from_instances {to: wqo_property_under_embedding}]--> output: `s_kruskal_wqo_statement`
2. input: `s_kruskal_wqo_statement` --[t_conjecture_refinement {to: finitary_TREE_n_growth}]--> output: `s_finitary_TREE_function_statement`
3. input: `s_finitary_TREE_function_statement` --[t_force_independence {target: ATR_0}]--> output: `s_friedman_finite_form_kruskal`

**Techniques used:** t_axiomatize_from_instances, t_conjecture_refinement, t_force_independence

---

### Mostowski collapse lemma (cite: https://en.wikipedia.org/wiki/Mostowski_collapse_lemma)

**Axioms:** `s_zfc_axioms`, `s_wellfounded_extensional_relation`
**Terminal:** `s_mostowski_collapse` (kind: theorem) — every well-founded extensional relation is isomorphic to a unique transitive set with ∈.

**Steps:**
1. input: `s_wellfounded_extensional_relation` --[t_auxiliary_construction {define: pi(x) = { pi(y) : y R x }}]--> output: `s_collapse_function_pi`
2. input: `s_collapse_function_pi` --[t_infinite_descent {wellfounded: R}]--> output: `s_pi_total_and_injective`
3. input: `s_pi_total_and_injective` --[t_structural_isomorphism {to: transitive_epsilon_set}]--> output: `s_mostowski_collapse`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_structural_isomorphism

---

### Mostowski absoluteness (cite: https://en.wikipedia.org/wiki/Absoluteness)

**Axioms:** `s_zfc_axioms`, `s_transitive_model_of_ZF`
**Terminal:** `s_mostowski_absoluteness` (kind: theorem) — Σ¹₁ formulas are absolute between transitive models containing all countable ordinals.

**Steps:**
1. input: `s_transitive_model_of_ZF` --[t_reduce_to_canonical_form {form: sigma_1_1_via_wellfounded_trees}]--> output: `s_sigma_1_1_as_wellfoundedness`
2. input: `s_sigma_1_1_as_wellfoundedness` --[t_conserved_quantity {invariant: wellfoundedness_across_transitive_models}]--> output: `s_wellfoundedness_absolute_for_transitive_models`
3. input: `s_wellfoundedness_absolute_for_transitive_models` --[t_projection_to_subspace {to: sigma_1_1_statements}]--> output: `s_mostowski_absoluteness`

**Techniques used:** t_reduce_to_canonical_form, t_conserved_quantity, t_projection_to_subspace

---

### Shoenfield absoluteness theorem (cite: https://en.wikipedia.org/wiki/Absoluteness#Shoenfield's_absoluteness_theorem)

**Axioms:** `s_zfc_axioms`, `s_godel_L_model`
**Terminal:** `s_shoenfield_absoluteness` (kind: theorem) — Σ¹₂ statements are absolute between V and L (assuming DC).

**Steps:**
1. input: `s_sigma_1_2_formula` --[t_reduce_to_canonical_form {form: exists_real_forall_real_arith}]--> output: `s_sigma_1_2_normal_form`
2. input: `s_sigma_1_2_normal_form` --[t_auxiliary_construction {tree: shoenfield_tree_on_omega_x_omega_1}]--> output: `s_shoenfield_tree_with_absolute_wellfoundedness`
3. input: `s_shoenfield_tree_with_absolute_wellfoundedness` --[t_conserved_quantity {invariant: wellfoundedness_omega_1_absolute_to_L}]--> output: `s_absoluteness_to_L`
4. input: `s_absoluteness_to_L` --[t_projection_to_subspace {to: sigma_1_2_truth}]--> output: `s_shoenfield_absoluteness`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_conserved_quantity, t_projection_to_subspace

---

### Levy reflection principle (cite: https://en.wikipedia.org/wiki/Reflection_principle)

**Axioms:** `s_zfc_axioms`, `s_cumulative_hierarchy_V_alpha`
**Terminal:** `s_levy_reflection` (kind: theorem) — for every formula φ, ZFC proves there exist arbitrarily large V_α reflecting φ.

**Steps:**
1. input: `s_cumulative_hierarchy_V_alpha` --[t_axiomatize_from_instances {schema: reflection_for_finite_formula_lists}]--> output: `s_reflection_schema_for_finite_subtheory`
2. input: `s_reflection_schema_for_finite_subtheory` --[t_compactness_argument {use: levy_montague_closure}]--> output: `s_closure_under_skolem_functions`
3. input: `s_closure_under_skolem_functions` --[t_interpolate_and_continue {along: ordinals}]--> output: `s_levy_reflection`

**Techniques used:** t_axiomatize_from_instances, t_compactness_argument, t_interpolate_and_continue

---

### Constructible universe L (Gödel) (cite: https://en.wikipedia.org/wiki/Constructible_universe)

**Axioms:** `s_zfc_axioms`, `s_definable_powerset_operator`
**Terminal:** `s_constructible_universe_L` (kind: theorem) — L is a transitive class model of ZFC, with V=L expressible and provable in L.

**Steps:**
1. input: `s_definable_powerset_operator` --[t_interpolate_and_continue {along: ordinals_with_Def_iteration}]--> output: `s_L_hierarchy_L_alpha`
2. input: `s_L_hierarchy_L_alpha` --[t_axiomatize_from_instances {verify: ZF_axioms_relativized_to_L}]--> output: `s_L_models_ZF`
3. input: `s_L_models_ZF` --[t_auxiliary_construction {wellorder: canonical_definable_<_L}]--> output: `s_canonical_wellorder_of_L`
4. input: `s_canonical_wellorder_of_L` --[t_structural_isomorphism {to: AC_validation}]--> output: `s_constructible_universe_L`

**Techniques used:** t_interpolate_and_continue, t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism

---

### V=L implies GCH in L (cite: https://en.wikipedia.org/wiki/Constructible_universe#The_generalized_continuum_hypothesis)

**Axioms:** `s_constructible_universe_L`, `s_condensation_lemma`
**Terminal:** `s_GCH_in_L` (kind: theorem) — L satisfies GCH.

**Steps:**
1. input: `s_constructible_universe_L` --[t_auxiliary_construction {use: skolem_hull_X_in_L_kappa_plus}]--> output: `s_countable_elementary_substructure`
2. input: `s_countable_elementary_substructure` --[t_structural_isomorphism {via: mostowski_collapse}]--> output: `s_collapsed_substructure_is_L_alpha`
3. input: `s_collapsed_substructure_is_L_alpha` --[t_exhaustion_squeeze {bound: |P(kappa) cap L| <= kappa_plus}]--> output: `s_GCH_in_L`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_exhaustion_squeeze

---

### Condensation lemma (Jensen) (cite: https://en.wikipedia.org/wiki/Jensen_hierarchy)

**Axioms:** `s_constructible_universe_L`, `s_definability_in_L_alpha`
**Terminal:** `s_condensation_lemma` (kind: theorem) — an elementary substructure of L_α isomorphic to a transitive set is itself an L_β.

**Steps:**
1. input: `s_definability_in_L_alpha` --[t_auxiliary_construction {elementary_substructure: M}]--> output: `s_elementary_substructure_of_L_alpha`
2. input: `s_elementary_substructure_of_L_alpha` --[t_structural_isomorphism {via: mostowski_collapse}]--> output: `s_transitive_isomorph_M_bar`
3. input: `s_transitive_isomorph_M_bar` --[t_conserved_quantity {preserved: definability_predicate_Def}]--> output: `s_M_bar_equals_L_beta`
4. input: `s_M_bar_equals_L_beta` --[t_compose_with_identity {recover: isomorphism_with_L_beta}]--> output: `s_condensation_lemma`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_conserved_quantity, t_compose_with_identity

---

### Jensen's covering lemma (cite: https://en.wikipedia.org/wiki/Jensen%27s_covering_theorem)

**Axioms:** `s_constructible_universe_L`, `s_zero_sharp_does_not_exist`
**Terminal:** `s_jensen_covering` (kind: theorem) — if 0# does not exist, every uncountable set of ordinals is covered by an L-set of the same cardinality.

**Steps:**
1. input: `s_zero_sharp_does_not_exist` --[t_reductio_ad_absurdum {assume: uncovered_set_X}]--> output: `s_uncovered_set_hypothesis`
2. input: `s_uncovered_set_hypothesis` --[t_auxiliary_construction {use: fine_structure_of_L}]--> output: `s_fine_structure_witness_in_L`
3. input: `s_fine_structure_witness_in_L` --[t_diagonalize {extract: zero_sharp_indiscernibles}]--> output: `s_construction_of_zero_sharp`
4. input: `s_construction_of_zero_sharp` --[t_reductio_ad_absurdum {close: contradiction_with_hypothesis}]--> output: `s_jensen_covering`

**Techniques used:** t_reductio_ad_absurdum, t_auxiliary_construction, t_diagonalize

---

### Zero sharp (0#) existence (cite: https://en.wikipedia.org/wiki/Zero_sharp)

**Axioms:** `s_measurable_cardinal_axiom`, `s_constructible_universe_L`
**Terminal:** `s_zero_sharp_existence` (kind: theorem) — a measurable cardinal implies 0# exists, equivalently L admits a proper class of Silver indiscernibles.

**Steps:**
1. input: `s_measurable_cardinal_axiom` --[t_auxiliary_construction {use: ultrapower_of_V_by_normal_measure}]--> output: `s_ultrapower_embedding_j`
2. input: `s_ultrapower_embedding_j` --[t_ultraproduct_transfer {restrict: to_L}]--> output: `s_nontrivial_elementary_j_restricted_to_L`
3. input: `s_nontrivial_elementary_j_restricted_to_L` --[t_auxiliary_construction {extract: critical_points_silver_indiscernibles}]--> output: `s_silver_indiscernibles_in_L`
4. input: `s_silver_indiscernibles_in_L` --[t_arithmetize_syntax {encode: theory_of_indiscernibles_as_set}]--> output: `s_zero_sharp_existence`

**Techniques used:** t_auxiliary_construction, t_ultraproduct_transfer, t_arithmetize_syntax

---

### Silver indiscernibles theorem (cite: https://en.wikipedia.org/wiki/Silver_indiscernibles)

**Axioms:** `s_zero_sharp_existence`, `s_constructible_universe_L`
**Terminal:** `s_silver_indiscernibles_theorem` (kind: theorem) — if 0# exists, the uncountable cardinals form a class of indiscernibles for L.

**Steps:**
1. input: `s_zero_sharp_existence` --[t_axiomatize_from_instances {to: ehrenfeucht_mostowski_template}]--> output: `s_EM_blueprint_for_L`
2. input: `s_EM_blueprint_for_L` --[t_symmetry_reduction {invariant: under_order_preserving_perms_of_uncountable_cardinals}]--> output: `s_indiscernibility_of_uncountable_cardinals`
3. input: `s_indiscernibility_of_uncountable_cardinals` --[t_structural_isomorphism {to: silver_indiscernibles_class}]--> output: `s_silver_indiscernibles_theorem`

**Techniques used:** t_axiomatize_from_instances, t_symmetry_reduction, t_structural_isomorphism

---

### Solovay's model (every set Lebesgue-measurable) (cite: https://en.wikipedia.org/wiki/Solovay_model)

**Axioms:** `s_inaccessible_cardinal_axiom`, `s_zfc_axioms`
**Terminal:** `s_solovay_model` (kind: theorem) — Con(ZFC+inaccessible) ⇒ Con(ZF+DC+every set of reals is Lebesgue measurable, has BP, perfect-set property).

**Steps:**
1. input: `s_inaccessible_cardinal_axiom` --[t_auxiliary_construction {force: collapse_kappa_to_omega_1}]--> output: `s_levy_collapse_model`
2. input: `s_levy_collapse_model` --[t_projection_to_subspace {restrict: to_HOD_of_reals_and_ordinals}]--> output: `s_HOD_R_ordinals_inner_model`
3. input: `s_HOD_R_ordinals_inner_model` --[t_force_independence {add: random_real_genericity_for_every_set}]--> output: `s_every_set_definable_from_real`
4. input: `s_every_set_definable_from_real` --[t_structural_isomorphism {to: lebesgue_measurable_via_random_reals}]--> output: `s_solovay_model`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_force_independence, t_structural_isomorphism

---

### Solovay random real forcing (cite: https://en.wikipedia.org/wiki/Random_real)

**Axioms:** `s_zfc_axioms`, `s_borel_measure_algebra`
**Terminal:** `s_random_real_forcing` (kind: theorem) — forcing with the Borel measure algebra adds a real avoiding every ground-model null set.

**Steps:**
1. input: `s_borel_measure_algebra` --[t_reduce_to_canonical_form {form: complete_boolean_algebra_B}]--> output: `s_complete_BA_for_random_forcing`
2. input: `s_complete_BA_for_random_forcing` --[t_force_independence {add: B_generic_filter}]--> output: `s_generic_random_real`
3. input: `s_generic_random_real` --[t_compactness_argument {use: countably_many_null_sets_avoided}]--> output: `s_random_real_avoids_null_sets`
4. input: `s_random_real_avoids_null_sets` --[t_conserved_quantity {invariant: measure_zero_definability}]--> output: `s_random_real_forcing`

**Techniques used:** t_reduce_to_canonical_form, t_force_independence, t_compactness_argument, t_conserved_quantity

---

### Mansfield–Solovay theorem (cite: https://en.wikipedia.org/wiki/Mansfield%E2%80%93Solovay_theorem)

**Axioms:** `s_zfc_axioms`, `s_sigma_1_2_set_of_reals`
**Terminal:** `s_mansfield_solovay` (kind: theorem) — every Σ¹₂ set of reals either is contained in L or contains a perfect set.

**Steps:**
1. input: `s_sigma_1_2_set_of_reals` --[t_reduce_to_canonical_form {form: shoenfield_tree_projection}]--> output: `s_sigma_1_2_as_tree_projection`
2. input: `s_sigma_1_2_as_tree_projection` --[t_auxiliary_construction {case: tree_has_perfect_subtree}]--> output: `s_perfect_subtree_case`
3. input: `s_perfect_subtree_case` --[t_auxiliary_construction {alt: every_branch_in_L}]--> output: `s_dichotomy_perfect_or_inside_L`
4. input: `s_dichotomy_perfect_or_inside_L` --[t_compose_with_identity {package: dichotomy}]--> output: `s_mansfield_solovay`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_compose_with_identity

---

### Vaught's two-cardinal theorem (cite: https://en.wikipedia.org/wiki/Two-cardinal_theorem)

**Axioms:** `s_first_order_theory_T`, `s_elementary_substructure_property`
**Terminal:** `s_vaught_two_cardinal` (kind: theorem) — if T has a (κ,λ)-model and κ>λ≥ℵ₀, then T has (ℵ₁,ℵ₀)-models.

**Steps:**
1. input: `s_first_order_theory_T` --[t_auxiliary_construction {object: (kappa_lambda)_model_M_with_definable_subset_X}]--> output: `s_two_cardinal_model_M`
2. input: `s_two_cardinal_model_M` --[t_compactness_argument {add: elementary_chain_axioms}]--> output: `s_elementary_chain_template`
3. input: `s_elementary_chain_template` --[t_interpolate_and_continue {along: omega_1_chain}]--> output: `s_vaught_two_cardinal`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_interpolate_and_continue

---

### Vaught's conjecture (status / never-22) (cite: https://en.wikipedia.org/wiki/Vaught_conjecture)

**Axioms:** `s_complete_countable_first_order_theory`, `s_morley_analysis_of_countable_models`
**Terminal:** `s_vaught_never_22_status` (kind: theorem) — a complete countable first-order theory has ≤ℵ₀ or 2^ℵ₀ countable models; intermediate count between ℵ₁ and 2^ℵ₀ excluded under various hypotheses (Morley); full conjecture still open.

**Steps:**
1. input: `s_complete_countable_first_order_theory` --[t_axiomatize_from_instances {to: counting_function_I(T,omega)}]--> output: `s_isomorphism_class_count_I_T`
2. input: `s_isomorphism_class_count_I_T` --[t_auxiliary_construction {use: morley_tree_of_countable_models}]--> output: `s_morley_tree_analysis`
3. input: `s_morley_tree_analysis` --[t_exhaustion_squeeze {to: aleph_1_or_continuum_dichotomy}]--> output: `s_morley_dichotomy_via_scott_analysis`
4. input: `s_morley_dichotomy_via_scott_analysis` --[t_conjecture_refinement {state: vaught_never_22}]--> output: `s_vaught_never_22_status`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_exhaustion_squeeze, t_conjecture_refinement

---

### Shelah's main gap theorem (cite: https://en.wikipedia.org/wiki/Stability_spectrum)

**Axioms:** `s_complete_first_order_theory`, `s_classification_invariants_dop_otop`
**Terminal:** `s_shelah_main_gap` (kind: theorem) — for countable T, either I(T,ℵ_α) = 2^ℵ_α for all α≥1, or I(T,ℵ_α) is bounded by a slow ℶ-function (depends on dimensional invariants).

**Steps:**
1. input: `s_complete_first_order_theory` --[t_axiomatize_from_instances {classify: stability_simplicity_dop_otop}]--> output: `s_classification_dichotomy_invariants`
2. input: `s_classification_dichotomy_invariants` --[t_auxiliary_construction {build: tree_of_models_with_independent_types}]--> output: `s_tree_of_models_decomposition`
3. input: `s_tree_of_models_decomposition` --[t_structural_isomorphism {if: classifiable_case}]--> output: `s_dimensional_decomposition_in_classifiable_case`
4. input: `s_dimensional_decomposition_in_classifiable_case` --[t_exhaustion_squeeze {dichotomy: maximal_or_few}]--> output: `s_shelah_main_gap`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism, t_exhaustion_squeeze

---

### Shelah stability spectrum (cite: https://en.wikipedia.org/wiki/Stable_theory)

**Axioms:** `s_first_order_theory_T`, `s_type_space_S_n_T`
**Terminal:** `s_stability_spectrum_theorem` (kind: theorem) — the cardinals κ with |S(M)| ≤ κ for some |M|=κ form a definable spectrum (ω-stable, superstable, stable).

**Steps:**
1. input: `s_type_space_S_n_T` --[t_axiomatize_from_instances {invariant: order_property_independence}]--> output: `s_order_property_dichotomy`
2. input: `s_order_property_dichotomy` --[t_exhaustion_squeeze {count: types_per_cardinal}]--> output: `s_stability_classification`
3. input: `s_stability_classification` --[t_reduce_to_canonical_form {spectrum: omega_stable_superstable_stable}]--> output: `s_stability_spectrum_theorem`

**Techniques used:** t_axiomatize_from_instances, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Morley's theorem on ω-stable theories (omitted-types) (cite: https://en.wikipedia.org/wiki/Omitting_types_theorem)

**Axioms:** `s_first_order_theory_T`, `s_countable_language`
**Terminal:** `s_omitting_types_theorem` (kind: theorem) — every nonprincipal type can be omitted in some countable model of T.

**Steps:**
1. input: `s_countable_language` --[t_auxiliary_construction {henkin_constants_plus_omitting_clauses}]--> output: `s_henkin_construction_with_omitting`
2. input: `s_henkin_construction_with_omitting` --[t_pigeonhole_collision {nonprincipal_type: avoidable_at_each_stage}]--> output: `s_at_each_step_omit_type`
3. input: `s_at_each_step_omit_type` --[t_compactness_argument {assemble: complete_theory}]--> output: `s_omitting_types_theorem`

**Techniques used:** t_auxiliary_construction, t_pigeonhole_collision, t_compactness_argument

---

### Pillay–Steinhorn o-minimality theorem (cite: https://en.wikipedia.org/wiki/O-minimal_theory)

**Axioms:** `s_ordered_field_structure`, `s_o_minimal_definability`
**Terminal:** `s_pillay_steinhorn_o_minimal_cell_decomposition` (kind: theorem) — every definable set in an o-minimal structure admits a finite cell decomposition; definable functions are piecewise C^k.

**Steps:**
1. input: `s_ordered_field_structure` --[t_axiomatize_from_instances {to: o_minimality_axiom}]--> output: `s_o_minimal_definability`
2. input: `s_o_minimal_definability` --[t_auxiliary_construction {use: monotonicity_lemma_on_definable_1var}]--> output: `s_monotonicity_lemma`
3. input: `s_monotonicity_lemma` --[t_interpolate_and_continue {induct_on_n: dimension}]--> output: `s_cell_decomposition_in_R_n`
4. input: `s_cell_decomposition_in_R_n` --[t_structural_isomorphism {to: tame_topology}]--> output: `s_pillay_steinhorn_o_minimal_cell_decomposition`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_interpolate_and_continue, t_structural_isomorphism

---

### Hrushovski's predimension construction (cite: https://en.wikipedia.org/wiki/Hrushovski_construction)

**Axioms:** `s_class_of_finite_structures_K`, `s_predimension_function_delta`
**Terminal:** `s_hrushovski_construction` (kind: theorem) — Fraïssé-style amalgamation with a submodular predimension yields new strongly minimal/ω-stable theories refuting Zilber's trichotomy.

**Steps:**
1. input: `s_class_of_finite_structures_K` --[t_auxiliary_construction {add: submodular_delta_function}]--> output: `s_predimension_paired_class`
2. input: `s_predimension_paired_class` --[t_axiomatize_from_instances {amalgamation: delta_closed_class}]--> output: `s_fraisse_amalgamation_with_predimension`
3. input: `s_fraisse_amalgamation_with_predimension` --[t_compactness_argument {limit: generic_structure}]--> output: `s_hrushovski_generic_structure`
4. input: `s_hrushovski_generic_structure` --[t_force_independence {against: zilber_trichotomy}]--> output: `s_hrushovski_construction`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_compactness_argument, t_force_independence

---

### Tarski's quantifier elimination for RCF (cite: https://en.wikipedia.org/wiki/Tarski%27s_theorem_(real-closed_field))

**Axioms:** `s_real_closed_field`, `s_polynomial_ring_over_RCF`
**Terminal:** `s_tarski_RCF_quantifier_elimination` (kind: theorem) — the theory of real closed fields admits quantifier elimination; hence it is decidable and complete.

**Steps:**
1. input: `s_real_closed_field` --[t_reduce_to_canonical_form {form: sturm_sign_data_on_polynomial_pieces}]--> output: `s_sturm_sign_change_count`
2. input: `s_sturm_sign_change_count` --[t_auxiliary_construction {procedure: eliminate_one_quantifier}]--> output: `s_one_step_quantifier_elimination`
3. input: `s_one_step_quantifier_elimination` --[t_interpolate_and_continue {induct: across_quantifier_block}]--> output: `s_quantifier_free_equivalent`
4. input: `s_quantifier_free_equivalent` --[t_formal_verify {effective: decision_procedure}]--> output: `s_tarski_RCF_quantifier_elimination`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_interpolate_and_continue, t_formal_verify

---

### Tarski's quantifier elimination for ACF (cite: https://en.wikipedia.org/wiki/Algebraically_closed_field#Model_theory)

**Axioms:** `s_algebraically_closed_field_k`, `s_polynomial_ring_in_n_vars`
**Terminal:** `s_ACF_quantifier_elimination` (kind: theorem) — the theory of algebraically closed fields (in each characteristic) admits quantifier elimination.

**Steps:**
1. input: `s_algebraically_closed_field_k` --[t_reduce_to_canonical_form {form: polynomial_system_solvability}]--> output: `s_polynomial_solvability_predicate`
2. input: `s_polynomial_solvability_predicate` --[t_auxiliary_construction {use: resultant_to_eliminate_existential}]--> output: `s_resultant_eliminates_existential_quantifier`
3. input: `s_resultant_eliminates_existential_quantifier` --[t_interpolate_and_continue {across: all_quantifiers}]--> output: `s_ACF_quantifier_elimination`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_interpolate_and_continue

---

### Ax–Grothendieck theorem (cite: https://en.wikipedia.org/wiki/Ax%E2%80%93Grothendieck_theorem)

**Axioms:** `s_complex_numbers`, `s_ACF_quantifier_elimination`
**Terminal:** `s_ax_grothendieck_theorem` (kind: theorem) — an injective polynomial map ℂⁿ → ℂⁿ is surjective.

**Steps:**
1. input: `s_complex_numbers` --[t_reduce_to_canonical_form {to: first_order_sentence_phi_n_d_in_ACF_0}]--> output: `s_first_order_sentence_phi_n_d`
2. input: `s_first_order_sentence_phi_n_d` --[t_verify_on_special_cases {fields: F_p_bar_finite_check}]--> output: `s_phi_holds_in_all_alg_closures_of_F_p`
3. input: `s_phi_holds_in_all_alg_closures_of_F_p` --[t_ultraproduct_transfer {from: char_p_to_char_0}]--> output: `s_phi_holds_in_ACF_0`
4. input: `s_phi_holds_in_ACF_0` --[t_structural_isomorphism {to: complex_polynomial_injective_surjective}]--> output: `s_ax_grothendieck_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_verify_on_special_cases, t_ultraproduct_transfer, t_structural_isomorphism

---

### Ax–Kochen theorem (cite: https://en.wikipedia.org/wiki/Ax%E2%80%93Kochen_theorem)

**Axioms:** `s_henselian_valued_field`, `s_residue_field_and_value_group`
**Terminal:** `s_ax_kochen_theorem` (kind: theorem) — ℚ_p and 𝔽_p((t)) are elementarily equivalent on first-order sentences that are true for all but finitely many primes p; hence Artin's conjecture on p-adic forms holds for almost all p.

**Steps:**
1. input: `s_henselian_valued_field` --[t_axiomatize_from_instances {axiom: ax_kochen_ershov_principle}]--> output: `s_ax_kochen_ershov_axioms`
2. input: `s_ax_kochen_ershov_axioms` --[t_ultraproduct_transfer {compare: Q_p_versus_F_p_t}]--> output: `s_elementary_equivalence_of_ultraproducts`
3. input: `s_elementary_equivalence_of_ultraproducts` --[t_compactness_argument {transfer: residue_to_henselian}]--> output: `s_ax_kochen_transfer`
4. input: `s_ax_kochen_transfer` --[t_projection_to_subspace {to: artin_p_adic_forms}]--> output: `s_ax_kochen_theorem`

**Techniques used:** t_axiomatize_from_instances, t_ultraproduct_transfer, t_compactness_argument, t_projection_to_subspace

---

### Decidability of Presburger arithmetic (cite: https://en.wikipedia.org/wiki/Presburger_arithmetic)

**Axioms:** `s_naturals_with_addition`, `s_first_order_logic_with_equality`
**Terminal:** `s_presburger_decidability` (kind: theorem) — the first-order theory of (ℕ,+,0,1,<) admits quantifier elimination (with congruence predicates) and is decidable.

**Steps:**
1. input: `s_naturals_with_addition` --[t_reduce_to_canonical_form {add: congruence_predicates_mod_k}]--> output: `s_presburger_with_congruences`
2. input: `s_presburger_with_congruences` --[t_auxiliary_construction {procedure: eliminate_existential_via_lcm_trick}]--> output: `s_qe_procedure_for_presburger`
3. input: `s_qe_procedure_for_presburger` --[t_interpolate_and_continue {induct: on_quantifier_depth}]--> output: `s_quantifier_free_form`
4. input: `s_quantifier_free_form` --[t_formal_verify {algorithm: decide_QF_truth}]--> output: `s_presburger_decidability`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_interpolate_and_continue, t_formal_verify

---

### Rice's theorem (cite: https://en.wikipedia.org/wiki/Rice%27s_theorem)

**Axioms:** `s_turing_machine_model`, `s_undecidability_of_halting`
**Terminal:** `s_rice_theorem` (kind: theorem) — every nontrivial semantic property of programs is undecidable.

**Steps:**
1. input: `s_turing_machine_model` --[t_reduce_to_canonical_form {target: index_set_A_for_property_P}]--> output: `s_index_set_A_for_property`
2. input: `s_undecidability_of_halting` --[t_auxiliary_construction {reduction: halting_into_A}]--> output: `s_many_one_reduction_HP_to_A`
3. input: `s_many_one_reduction_HP_to_A` --[t_reductio_ad_absurdum {assume: A_recursive}]--> output: `s_rice_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_reductio_ad_absurdum

---

### Rice–Shapiro theorem (cite: https://en.wikipedia.org/wiki/Rice%E2%80%93Shapiro_theorem)

**Axioms:** `s_turing_machine_model`, `s_re_set_of_partial_recursive_functions`
**Terminal:** `s_rice_shapiro_theorem` (kind: theorem) — an r.e. index set A is r.e. iff its underlying class is closed under finite restriction/extension limits (compactly determined by finite subfunctions).

**Steps:**
1. input: `s_re_set_of_partial_recursive_functions` --[t_axiomatize_from_instances {to: index_set_A_re}]--> output: `s_re_index_set_property`
2. input: `s_re_index_set_property` --[t_compactness_argument {use: finite_subfunction_witnesses}]--> output: `s_finite_witness_property`
3. input: `s_finite_witness_property` --[t_reductio_ad_absurdum {assume: no_finite_witness}]--> output: `s_rice_shapiro_theorem`

**Techniques used:** t_axiomatize_from_instances, t_compactness_argument, t_reductio_ad_absurdum

---

### Kleene's second recursion theorem (cite: https://en.wikipedia.org/wiki/Kleene%27s_recursion_theorem)

**Axioms:** `s_turing_machine_model`, `s_s_m_n_theorem`
**Terminal:** `s_kleene_second_recursion_theorem` (kind: theorem) — for every total computable f there is e with φ_e = φ_{f(e)}.

**Steps:**
1. input: `s_s_m_n_theorem` --[t_auxiliary_construction {build: d(x) using s_1_1}]--> output: `s_diagonal_program_d_x`
2. input: `s_diagonal_program_d_x` --[t_diagonalize {apply: d(d_index)}]--> output: `s_fixed_point_index_e`
3. input: `s_fixed_point_index_e` --[t_compose_with_identity {package: fixed_point_property}]--> output: `s_kleene_second_recursion_theorem`

**Techniques used:** t_auxiliary_construction, t_diagonalize, t_compose_with_identity

---

### s-m-n theorem (cite: https://en.wikipedia.org/wiki/Smn_theorem)

**Axioms:** `s_turing_machine_model`, `s_universal_turing_machine`
**Terminal:** `s_s_m_n_theorem` (kind: theorem) — there is a primitive recursive function s such that φ_{s(e,x)}(y) = φ_e(x,y).

**Steps:**
1. input: `s_universal_turing_machine` --[t_auxiliary_construction {build: program_that_hardcodes_x}]--> output: `s_program_with_hardcoded_input`
2. input: `s_program_with_hardcoded_input` --[t_arithmetize_syntax {extract: index_as_primrec_function}]--> output: `s_index_function_s_e_x`
3. input: `s_index_function_s_e_x` --[t_compose_with_identity {assert: phi_s_e_x_y_equals_phi_e_x_y}]--> output: `s_s_m_n_theorem`

**Techniques used:** t_auxiliary_construction, t_arithmetize_syntax, t_compose_with_identity

---

### Friedberg–Muchnik theorem (cite: https://en.wikipedia.org/wiki/Friedberg%E2%80%93Muchnik_theorem)

**Axioms:** `s_re_sets`, `s_turing_reducibility`
**Terminal:** `s_friedberg_muchnik_theorem` (kind: theorem) — there exist Turing-incomparable r.e. sets A, B; in particular Post's problem has a positive solution.

**Steps:**
1. input: `s_re_sets` --[t_axiomatize_from_instances {requirements: R_e_S_e_for_each_index}]--> output: `s_priority_requirement_list`
2. input: `s_priority_requirement_list` --[t_auxiliary_construction {priority_method: finite_injury}]--> output: `s_finite_injury_construction`
3. input: `s_finite_injury_construction` --[t_pigeonhole_collision {control: only_finite_injury_per_requirement}]--> output: `s_each_requirement_satisfied`
4. input: `s_each_requirement_satisfied` --[t_diagonalize {against: alleged_reduction}]--> output: `s_friedberg_muchnik_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_pigeonhole_collision, t_diagonalize

---

### Sacks density theorem (cite: https://en.wikipedia.org/wiki/Sacks_density_theorem)

**Axioms:** `s_re_turing_degrees`, `s_priority_method`
**Terminal:** `s_sacks_density_theorem` (kind: theorem) — between any two r.e. degrees a < b lies a third r.e. degree c with a < c < b.

**Steps:**
1. input: `s_re_turing_degrees` --[t_auxiliary_construction {targets: requirements_below_b_above_a}]--> output: `s_intermediate_degree_requirements`
2. input: `s_intermediate_degree_requirements` --[t_auxiliary_construction {priority: infinite_injury_with_guessing}]--> output: `s_infinite_injury_construction`
3. input: `s_infinite_injury_construction` --[t_pigeonhole_collision {bound: injuries_along_true_path}]--> output: `s_true_path_argument_succeeds`
4. input: `s_true_path_argument_succeeds` --[t_compose_with_identity {package: density}]--> output: `s_sacks_density_theorem`

**Techniques used:** t_auxiliary_construction, t_pigeonhole_collision, t_compose_with_identity

---

### Sacks splitting theorem (cite: https://en.wikipedia.org/wiki/Sacks_splitting_theorem)

**Axioms:** `s_re_set_A_nonrecursive`, `s_priority_method`
**Terminal:** `s_sacks_splitting_theorem` (kind: theorem) — every nonrecursive r.e. set A splits into two r.e. sets A_0 ∪ A_1 of strictly lower Turing degree.

**Steps:**
1. input: `s_re_set_A_nonrecursive` --[t_auxiliary_construction {split_requirements: each_part_low_against_A}]--> output: `s_splitting_requirement_list`
2. input: `s_splitting_requirement_list` --[t_auxiliary_construction {priority: finite_injury_splitting}]--> output: `s_splitting_construction`
3. input: `s_splitting_construction` --[t_diagonalize {against: each_potential_reduction_of_A_from_A_i}]--> output: `s_sacks_splitting_theorem`

**Techniques used:** t_auxiliary_construction, t_diagonalize

---

### Sacks jump inversion theorem (cite: https://en.wikipedia.org/wiki/Sacks%27_jump_theorem)

**Axioms:** `s_turing_jump_operator`, `s_re_degree_zero_prime`
**Terminal:** `s_sacks_jump_inversion` (kind: theorem) — for every degree c ≥ 0′ that is r.e. in 0′, there is an r.e. degree a with a′ = c.

**Steps:**
1. input: `s_re_degree_zero_prime` --[t_auxiliary_construction {target: pre_image_under_jump}]--> output: `s_jump_inversion_requirements`
2. input: `s_jump_inversion_requirements` --[t_auxiliary_construction {priority: infinite_injury}]--> output: `s_jump_inversion_construction`
3. input: `s_jump_inversion_construction` --[t_interpolate_and_continue {iterate: omega_levels}]--> output: `s_jump_target_achieved`
4. input: `s_jump_target_achieved` --[t_compose_with_identity {assemble: a_with_a_prime_equals_c}]--> output: `s_sacks_jump_inversion`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_compose_with_identity

---

### Wadge's lemma (cite: https://en.wikipedia.org/wiki/Wadge_hierarchy)

**Axioms:** `s_borel_sets_in_baire_space`, `s_axiom_of_determinacy_for_borel_games`
**Terminal:** `s_wadge_lemma` (kind: theorem) — for any two Borel sets A, B in Baire space, either A ≤_W B or ¬B ≤_W A.

**Steps:**
1. input: `s_borel_sets_in_baire_space` --[t_auxiliary_construction {game: wadge_game_G(A,B)}]--> output: `s_wadge_game`
2. input: `s_wadge_game` --[t_axiomatize_from_instances {apply: borel_determinacy_to_G}]--> output: `s_wadge_game_determined`
3. input: `s_wadge_game_determined` --[t_duality {convert: winning_strategies_to_reductions}]--> output: `s_wadge_lemma`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_duality

---

### Wadge hierarchy / antichain structure (cite: https://en.wikipedia.org/wiki/Wadge_hierarchy)

**Axioms:** `s_wadge_lemma`, `s_borel_sets_in_baire_space`
**Terminal:** `s_wadge_hierarchy_theorem` (kind: theorem) — Wadge order on Borel sets is a well-quasi-order with no antichains of size ≥3 and length ω₁.

**Steps:**
1. input: `s_wadge_lemma` --[t_reduce_to_canonical_form {to: order_on_borel_classes}]--> output: `s_wadge_ordering`
2. input: `s_wadge_ordering` --[t_infinite_descent {wellfoundedness: martin_borel_wf_argument}]--> output: `s_wadge_wellfounded`
3. input: `s_wadge_wellfounded` --[t_exhaustion_squeeze {length: omega_1}]--> output: `s_wadge_hierarchy_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_infinite_descent, t_exhaustion_squeeze

---

### Martin's theorem: Σ¹₁-determinacy from measurable (cite: https://en.wikipedia.org/wiki/Determinacy#Determinacy_from_large_cardinals)

**Axioms:** `s_measurable_cardinal_axiom`, `s_analytic_set_in_baire_space`
**Terminal:** `s_martin_analytic_determinacy` (kind: theorem) — a measurable cardinal implies all analytic (Σ¹₁) games are determined.

**Steps:**
1. input: `s_analytic_set_in_baire_space` --[t_reduce_to_canonical_form {form: tree_T_with_analytic_projection}]--> output: `s_tree_representation_of_analytic_set`
2. input: `s_measurable_cardinal_axiom` --[t_auxiliary_construction {use: homogeneous_tree_with_measures}]--> output: `s_homogeneous_tree_for_T`
3. input: `s_homogeneous_tree_for_T` --[t_ultraproduct_transfer {combine: tower_of_measures}]--> output: `s_tower_argument_winning_strategy`
4. input: `s_tower_argument_winning_strategy` --[t_compose_with_identity {package: analytic_determinacy}]--> output: `s_martin_analytic_determinacy`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_ultraproduct_transfer, t_compose_with_identity

---

### AD in L(ℝ) from large cardinals (Woodin) (cite: https://en.wikipedia.org/wiki/Axiom_of_determinacy)

**Axioms:** `s_infinitely_many_woodin_cardinals`, `s_constructible_closure_L_R`
**Terminal:** `s_AD_in_L_R` (kind: theorem) — infinitely many Woodin cardinals plus a measurable above imply L(ℝ) ⊨ AD.

**Steps:**
1. input: `s_infinitely_many_woodin_cardinals` --[t_auxiliary_construction {use: iteration_trees}]--> output: `s_iteration_trees_on_V`
2. input: `s_iteration_trees_on_V` --[t_auxiliary_construction {use: homogeneously_suslin_representations}]--> output: `s_universally_baire_pointclass`
3. input: `s_universally_baire_pointclass` --[t_interpolate_and_continue {induct: across_projective_levels}]--> output: `s_projective_determinacy`
4. input: `s_projective_determinacy` --[t_ultraproduct_transfer {ascend: to_L(R)}]--> output: `s_AD_in_L_R`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_ultraproduct_transfer

---

### Souslin's theorem (Σ¹₁ ∩ Π¹₁ = Borel) (cite: https://en.wikipedia.org/wiki/Suslin%27s_theorem)

**Axioms:** `s_polish_space`, `s_analytic_set_in_baire_space`
**Terminal:** `s_souslin_theorem` (kind: theorem) — a set in a Polish space is Borel iff it is both analytic and coanalytic.

**Steps:**
1. input: `s_analytic_set_in_baire_space` --[t_auxiliary_construction {separation: lusin_separation_lemma}]--> output: `s_lusin_separation_for_disjoint_analytics`
2. input: `s_lusin_separation_for_disjoint_analytics` --[t_duality {apply_to: A_and_complement}]--> output: `s_separating_borel_set_for_A_and_comp_A`
3. input: `s_separating_borel_set_for_A_and_comp_A` --[t_compose_with_identity {conclude: A_is_Borel}]--> output: `s_souslin_theorem`

**Techniques used:** t_auxiliary_construction, t_duality, t_compose_with_identity

---

### Kondô's uniformization theorem (cite: https://en.wikipedia.org/wiki/Uniformization_(set_theory))

**Axioms:** `s_pi_1_1_set_in_product_space`, `s_constructible_universe_L`
**Terminal:** `s_kondo_uniformization` (kind: theorem) — every Π¹₁ subset of X × Y can be uniformized by a Π¹₁ function.

**Steps:**
1. input: `s_pi_1_1_set_in_product_space` --[t_reduce_to_canonical_form {form: tree_T_x_with_wellfounded_sections}]--> output: `s_wellfounded_tree_T_x`
2. input: `s_wellfounded_tree_T_x` --[t_auxiliary_construction {choose: leftmost_rank_minimizer}]--> output: `s_canonical_section_selector`
3. input: `s_canonical_section_selector` --[t_projection_to_subspace {project: to_pi_1_1_graph}]--> output: `s_kondo_uniformization`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_projection_to_subspace

---

### Transfinite recursion theorem (cite: https://en.wikipedia.org/wiki/Transfinite_recursion)

**Axioms:** `s_zfc_axioms`, `s_wellordered_class_ON`
**Terminal:** `s_transfinite_recursion_theorem` (kind: theorem) — for any class function G on V, there is a unique class function F on Ordinals with F(α)=G(F↾α).

**Steps:**
1. input: `s_wellordered_class_ON` --[t_auxiliary_construction {form: set_of_attempts_alpha_indexed}]--> output: `s_set_of_attempts`
2. input: `s_set_of_attempts` --[t_infinite_descent {wellfoundedness: ON}]--> output: `s_uniqueness_of_attempts`
3. input: `s_uniqueness_of_attempts` --[t_compose_with_identity {assemble: union_into_class_function_F}]--> output: `s_transfinite_recursion_theorem`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_compose_with_identity

---

### Erdős–Tarski theorem on weakly compact cardinals (cite: https://en.wikipedia.org/wiki/Weakly_compact_cardinal)

**Axioms:** `s_inaccessible_cardinal_axiom`, `s_partition_relation_kappa_to_kappa_2_2`
**Terminal:** `s_erdos_tarski_theorem` (kind: theorem) — for an uncountable κ, κ → (κ)²₂ iff κ is weakly compact iff κ is Π¹₁-indescribable.

**Steps:**
1. input: `s_partition_relation_kappa_to_kappa_2_2` --[t_axiomatize_from_instances {to: tree_property_on_kappa}]--> output: `s_tree_property_for_kappa`
2. input: `s_tree_property_for_kappa` --[t_structural_isomorphism {equiv: pi_1_1_indescribability}]--> output: `s_pi_1_1_indescribability`
3. input: `s_pi_1_1_indescribability` --[t_compactness_argument {filter: closed_unbounded}]--> output: `s_weak_compactness_characterization`
4. input: `s_weak_compactness_characterization` --[t_compose_with_identity {package: equivalences}]--> output: `s_erdos_tarski_theorem`

**Techniques used:** t_axiomatize_from_instances, t_structural_isomorphism, t_compactness_argument, t_compose_with_identity

---

### Scott's theorem (no measurable cardinal in L) (cite: https://en.wikipedia.org/wiki/Measurable_cardinal)

**Axioms:** `s_measurable_cardinal_axiom`, `s_constructible_universe_L`
**Terminal:** `s_scott_theorem_V_not_L` (kind: theorem) — the existence of a measurable cardinal implies V ≠ L.

**Steps:**
1. input: `s_measurable_cardinal_axiom` --[t_auxiliary_construction {use: normal_measure_ultrapower_j}]--> output: `s_ultrapower_embedding_j`
2. input: `s_ultrapower_embedding_j` --[t_ultraproduct_transfer {restrict: j_restricted_to_L_is_definable_if_V_equals_L}]--> output: `s_kunen_inconsistency_in_L`
3. input: `s_kunen_inconsistency_in_L` --[t_reductio_ad_absurdum {assume: V_equals_L}]--> output: `s_scott_theorem_V_not_L`

**Techniques used:** t_auxiliary_construction, t_ultraproduct_transfer, t_reductio_ad_absurdum

---

### Kunen inconsistency theorem (cite: https://en.wikipedia.org/wiki/Kunen%27s_inconsistency_theorem)

**Axioms:** `s_zfc_axioms`, `s_elementary_embedding_j_V_to_V`
**Terminal:** `s_kunen_inconsistency` (kind: theorem) — there is no nontrivial elementary embedding j : V → V in ZFC.

**Steps:**
1. input: `s_elementary_embedding_j_V_to_V` --[t_auxiliary_construction {choose: critical_point_kappa_and_omega_th_iterate}]--> output: `s_iterated_critical_points`
2. input: `s_iterated_critical_points` --[t_auxiliary_construction {use: erdos_kunen_subset_function}]--> output: `s_problematic_definable_subset`
3. input: `s_problematic_definable_subset` --[t_diagonalize {against: alleged_j_image_property}]--> output: `s_kunen_inconsistency`

**Techniques used:** t_auxiliary_construction, t_diagonalize

---

### Reflection theorem in L (cite: https://en.wikipedia.org/wiki/Reflection_principle#In_constructible_universe)

**Axioms:** `s_constructible_universe_L`, `s_definability_in_L_alpha`
**Terminal:** `s_reflection_in_L` (kind: theorem) — every formula true in L is reflected to club-many L_α.

**Steps:**
1. input: `s_constructible_universe_L` --[t_axiomatize_from_instances {form: reflection_schema_for_phi}]--> output: `s_phi_reflection_schema_in_L`
2. input: `s_phi_reflection_schema_in_L` --[t_compactness_argument {use: levy_reflection_relativized_to_L}]--> output: `s_levy_reflection_in_L`
3. input: `s_levy_reflection_in_L` --[t_interpolate_and_continue {along: club_class_of_ordinals}]--> output: `s_reflection_in_L`

**Techniques used:** t_axiomatize_from_instances, t_compactness_argument, t_interpolate_and_continue

---

### Mostowski rank theorem (cite: https://en.wikipedia.org/wiki/Well-founded_relation#Rank_function)

**Axioms:** `s_zfc_axioms`, `s_wellfounded_relation_R`
**Terminal:** `s_mostowski_rank_function` (kind: theorem) — every set-like well-founded relation admits a unique ordinal-valued rank function.

**Steps:**
1. input: `s_wellfounded_relation_R` --[t_auxiliary_construction {define: rank(x) = sup_{yRx}(rank(y)+1)}]--> output: `s_rank_recursive_definition`
2. input: `s_rank_recursive_definition` --[t_infinite_descent {wellfoundedness: R}]--> output: `s_rank_total_and_uniquely_defined`
3. input: `s_rank_total_and_uniquely_defined` --[t_compose_with_identity {package: rank_function}]--> output: `s_mostowski_rank_function`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_compose_with_identity

---

### Friedman's harmonious functor theorem (cite: https://en.wikipedia.org/wiki/Reverse_mathematics)

**Axioms:** `s_subsystem_RCA_0`, `s_class_of_borel_functors`
**Terminal:** `s_friedman_borel_diagonalization` (kind: theorem) — Friedman's Borel diagonalization theorem (BDT) is independent of ATR₀ but provable in Π¹₁-CA₀.

**Steps:**
1. input: `s_class_of_borel_functors` --[t_axiomatize_from_instances {to: borel_diagonalization_statement}]--> output: `s_BDT_statement`
2. input: `s_BDT_statement` --[t_force_independence {target: ATR_0}]--> output: `s_BDT_not_in_ATR_0`
3. input: `s_BDT_statement` --[t_diagonalize {use: Pi_1_1_comprehension}]--> output: `s_BDT_provable_in_pi_1_1_CA_0`
4. input: `⟨s_BDT_not_in_ATR_0, s_BDT_provable_in_pi_1_1_CA_0⟩` --[t_compose_with_identity {package: classification}]--> output: `s_friedman_borel_diagonalization`

**Techniques used:** t_axiomatize_from_instances, t_force_independence, t_diagonalize, t_compose_with_identity

---

### Ramsey-type Paris–Harrington-style independence (general PA-unprovable) (cite: https://en.wikipedia.org/wiki/Paris%E2%80%93Harrington_theorem)

**Axioms:** `s_first_order_peano_arithmetic`, `s_ramsey_theorem_infinite`
**Terminal:** `s_strong_ramsey_independence` (kind: theorem) — the relatively-large finite Ramsey is true but unprovable in PA (a paradigmatic example; the canonical statement is in graph as Paris–Harrington).

**Steps:**
1. input: `s_ramsey_theorem_infinite` --[t_conjecture_refinement {to: large_finite_ramsey_with_min_constraint}]--> output: `s_relatively_large_ramsey_statement`
2. input: `s_relatively_large_ramsey_statement` --[t_arithmetize_syntax {realize: indicator_function_for_PA_models}]--> output: `s_indicator_for_PA_growth`
3. input: `s_indicator_for_PA_growth` --[t_force_independence {against: PA_provably_recursive_functions}]--> output: `s_strong_ramsey_independence`

**Techniques used:** t_conjecture_refinement, t_arithmetize_syntax, t_force_independence

---

### Skolem's paradox (cite: https://en.wikipedia.org/wiki/Skolem%27s_paradox)

**Axioms:** `s_zfc_axioms`, `s_downward_lowenheim_skolem`
**Terminal:** `s_skolem_paradox` (kind: theorem) — ZFC has a countable model in which "ℝ is uncountable" still holds (relativized).

**Steps:**
1. input: `s_zfc_axioms` --[t_axiomatize_from_instances {apply: downward_LS}]--> output: `s_countable_elementary_substructure_of_V`
2. input: `s_countable_elementary_substructure_of_V` --[t_structural_isomorphism {via: mostowski_collapse}]--> output: `s_countable_transitive_model`
3. input: `s_countable_transitive_model` --[t_conserved_quantity {preserved: relativized_uncountability}]--> output: `s_skolem_paradox`

**Techniques used:** t_axiomatize_from_instances, t_structural_isomorphism, t_conserved_quantity

---

### Specker–Ackermann ordinal of PA / Gentzen analysis (cite: https://en.wikipedia.org/wiki/Ordinal_analysis)

**Axioms:** `s_first_order_peano_arithmetic`, `s_ordinal_arithmetic_below_epsilon_0`
**Terminal:** `s_PA_proof_theoretic_ordinal_epsilon_0` (kind: theorem) — the proof-theoretic ordinal of PA is ε₀.

**Steps:**
1. input: `s_first_order_peano_arithmetic` --[t_arithmetize_syntax {assign: ordinal_to_each_proof}]--> output: `s_proof_ordinal_assignment`
2. input: `s_proof_ordinal_assignment` --[t_reduce_to_canonical_form {procedure: cut_elimination_decreases_ordinal}]--> output: `s_cut_elimination_bound`
3. input: `s_cut_elimination_bound` --[t_infinite_descent {wellorder: epsilon_0}]--> output: `s_consistency_via_descent`
4. input: `s_consistency_via_descent` --[t_compose_with_identity {package: ordinal_epsilon_0}]--> output: `s_PA_proof_theoretic_ordinal_epsilon_0`

**Techniques used:** t_arithmetize_syntax, t_reduce_to_canonical_form, t_infinite_descent, t_compose_with_identity

---

### Cut-elimination theorem (Gentzen Hauptsatz) (cite: https://en.wikipedia.org/wiki/Cut-elimination_theorem)

**Axioms:** `s_sequent_calculus_LK`, `s_proof_tree`
**Terminal:** `s_cut_elimination_theorem` (kind: theorem) — every proof in LK/LJ can be transformed into a cut-free proof.

**Steps:**
1. input: `s_proof_tree` --[t_auxiliary_construction {operation: reduce_one_cut_by_local_rule}]--> output: `s_local_cut_reduction_rules`
2. input: `s_local_cut_reduction_rules` --[t_interpolate_and_continue {induct: on_cut_rank_then_height}]--> output: `s_double_induction_termination`
3. input: `s_double_induction_termination` --[t_infinite_descent {wellfounded: ordinal_lex_on_(rank,height)}]--> output: `s_cut_elimination_theorem`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_infinite_descent

---

### Curry–Howard correspondence (cite: https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence)

**Axioms:** `s_simply_typed_lambda_calculus`, `s_intuitionistic_propositional_logic`
**Terminal:** `s_curry_howard_correspondence` (kind: theorem) — terms of STLC correspond to natural deduction proofs in IPL; reduction = cut-elimination.

**Steps:**
1. input: `s_simply_typed_lambda_calculus` --[t_structural_isomorphism {types_as_propositions: hom_correspondence}]--> output: `s_types_as_propositions_map`
2. input: `s_intuitionistic_propositional_logic` --[t_structural_isomorphism {proofs_as_terms: deduction_to_lambda}]--> output: `s_proofs_as_terms_map`
3. input: `⟨s_types_as_propositions_map, s_proofs_as_terms_map⟩` --[t_compose_with_identity {package: iso}]--> output: `s_iso_STLC_IPL_proofs`
4. input: `s_iso_STLC_IPL_proofs` --[t_conserved_quantity {invariant: reduction_corresponds_to_normalization}]--> output: `s_curry_howard_correspondence`

**Techniques used:** t_structural_isomorphism, t_compose_with_identity, t_conserved_quantity

---

### Strong normalization for STLC (cite: https://en.wikipedia.org/wiki/Strongly_normalizing)

**Axioms:** `s_simply_typed_lambda_calculus`, `s_type_assignment`
**Terminal:** `s_strong_normalization_STLC` (kind: theorem) — every well-typed term in STLC is strongly normalizing.

**Steps:**
1. input: `s_type_assignment` --[t_auxiliary_construction {tait_reducibility_candidates: per_type}]--> output: `s_reducibility_candidates`
2. input: `s_reducibility_candidates` --[t_structural_isomorphism {invariant: closure_under_typing_rules}]--> output: `s_candidate_closure_properties`
3. input: `s_candidate_closure_properties` --[t_infinite_descent {wellfounded: candidate_membership}]--> output: `s_strong_normalization_STLC`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_infinite_descent

---

### Löb's theorem (cite: https://en.wikipedia.org/wiki/L%C3%B6b%27s_theorem)

**Axioms:** `s_first_order_peano_arithmetic`, `s_provability_predicate_box`
**Terminal:** `s_lob_theorem` (kind: theorem) — if PA ⊢ □φ → φ, then PA ⊢ φ.

**Steps:**
1. input: `s_provability_predicate_box` --[t_axiomatize_from_instances {to: hilbert_bernays_provability_conditions}]--> output: `s_HB_provability_axioms`
2. input: `s_HB_provability_axioms` --[t_diagonalize {build: psi_with_psi_iff_box_psi_to_phi}]--> output: `s_lob_diagonal_sentence`
3. input: `s_lob_diagonal_sentence` --[t_compose_with_identity {derive: phi_provable_from_box_phi_to_phi}]--> output: `s_lob_theorem`

**Techniques used:** t_axiomatize_from_instances, t_diagonalize, t_compose_with_identity

---

### Tarski's undefinability of truth (cite: https://en.wikipedia.org/wiki/Tarski%27s_undefinability_theorem)

**Axioms:** `s_first_order_peano_arithmetic`, `s_arithmetical_definability`
**Terminal:** `s_tarski_undefinability` (kind: theorem) — the set of Gödel numbers of true sentences of arithmetic is not arithmetically definable.

**Steps:**
1. input: `s_first_order_peano_arithmetic` --[t_arithmetize_syntax {encode: sentence_godel_numbers}]--> output: `s_godel_numbering_of_arithmetic`
2. input: `s_godel_numbering_of_arithmetic` --[t_diagonalize {build: liar_sentence_via_definable_truth_predicate}]--> output: `s_liar_via_truth_predicate`
3. input: `s_liar_via_truth_predicate` --[t_reductio_ad_absurdum {assume: T_arithmetical}]--> output: `s_tarski_undefinability`

**Techniques used:** t_arithmetize_syntax, t_diagonalize, t_reductio_ad_absurdum

---

### Beth definability theorem (cite: https://en.wikipedia.org/wiki/Beth_definability)

**Axioms:** `s_first_order_theory_T`, `s_implicit_definability_predicate`
**Terminal:** `s_beth_definability` (kind: theorem) — implicit definability ⇔ explicit definability in first-order logic.

**Steps:**
1. input: `s_implicit_definability_predicate` --[t_reduce_to_canonical_form {form: T_decides_R_uniquely}]--> output: `s_T_uniqueness_of_R`
2. input: `s_T_uniqueness_of_R` --[t_axiomatize_from_instances {apply: craig_interpolation_on_separation}]--> output: `s_craig_interpolant_phi`
3. input: `s_craig_interpolant_phi` --[t_structural_isomorphism {to: explicit_first_order_definition}]--> output: `s_beth_definability`

**Techniques used:** t_reduce_to_canonical_form, t_axiomatize_from_instances, t_structural_isomorphism

---

### Gödel's completeness theorem (cite: https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem)

**Axioms:** `s_first_order_logic_with_equality`, `s_henkin_witness_construction`
**Terminal:** `s_godel_completeness_theorem` (kind: theorem) — every consistent first-order theory has a model.

**Steps:**
1. input: `s_first_order_logic_with_equality` --[t_axiomatize_from_instances {expand: with_henkin_constants}]--> output: `s_expanded_language_with_henkin_constants`
2. input: `s_expanded_language_with_henkin_constants` --[t_auxiliary_construction {build: maximal_consistent_extension}]--> output: `s_maximal_consistent_henkin_theory`
3. input: `s_maximal_consistent_henkin_theory` --[t_structural_isomorphism {to: term_model}]--> output: `s_term_model_satisfies_T`
4. input: `s_term_model_satisfies_T` --[t_compose_with_identity {package: completeness}]--> output: `s_godel_completeness_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism, t_compose_with_identity

---

### Robinson's joint consistency theorem (cite: https://en.wikipedia.org/wiki/Robinson%27s_joint_consistency_theorem)

**Axioms:** `s_two_consistent_first_order_theories_T1_T2`, `s_common_subtheory_T_0`
**Terminal:** `s_robinson_joint_consistency` (kind: theorem) — if T_1 and T_2 are consistent, share a complete common subtheory T_0, then T_1 ∪ T_2 is consistent.

**Steps:**
1. input: `s_common_subtheory_T_0` --[t_axiomatize_from_instances {form: complete_common_substructure}]--> output: `s_common_complete_subtheory`
2. input: `s_common_complete_subtheory` --[t_auxiliary_construction {apply: craig_interpolation}]--> output: `s_no_disagreement_via_interpolant`
3. input: `s_no_disagreement_via_interpolant` --[t_compactness_argument {assemble: joint_model}]--> output: `s_robinson_joint_consistency`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_compactness_argument

---

### Keisler–Shelah ultrapower characterization of elementary equivalence (cite: https://en.wikipedia.org/wiki/Keisler%E2%80%93Shelah_isomorphism_theorem)

**Axioms:** `s_two_first_order_structures_M_N`, `s_ultrafilter_on_index_set`
**Terminal:** `s_keisler_shelah_theorem` (kind: theorem) — M ≡ N iff some ultrapowers M^I/U ≅ N^I/U are isomorphic.

**Steps:**
1. input: `s_two_first_order_structures_M_N` --[t_ultraproduct_transfer {form: ultrapower_M_I_over_U}]--> output: `s_ultrapowers_M_U_N_U`
2. input: `s_ultrapowers_M_U_N_U` --[t_axiomatize_from_instances {use: saturation_via_good_ultrafilter}]--> output: `s_saturated_ultrapowers`
3. input: `s_saturated_ultrapowers` --[t_structural_isomorphism {to_isomorphism_via_back_and_forth}]--> output: `s_isomorphism_of_saturated_models`
4. input: `s_isomorphism_of_saturated_models` --[t_compose_with_identity {package: characterization}]--> output: `s_keisler_shelah_theorem`

**Techniques used:** t_ultraproduct_transfer, t_axiomatize_from_instances, t_structural_isomorphism, t_compose_with_identity

---

### Existence of saturated models (cite: https://en.wikipedia.org/wiki/Saturated_model)

**Axioms:** `s_first_order_theory_T`, `s_continuum_hypothesis_or_GCH`
**Terminal:** `s_saturated_model_existence` (kind: theorem) — under GCH (or with appropriate cardinal arithmetic), every consistent theory T has a κ-saturated model in cardinality κ for κ regular ≥ |T|⁺.

**Steps:**
1. input: `s_first_order_theory_T` --[t_auxiliary_construction {elementary_chain: realize_one_type_per_step}]--> output: `s_elementary_chain_realizing_types`
2. input: `s_elementary_chain_realizing_types` --[t_pigeonhole_collision {bound: number_of_types_below_kappa}]--> output: `s_type_realization_succeeds`
3. input: `s_type_realization_succeeds` --[t_compactness_argument {limit: union_chain}]--> output: `s_saturated_model_existence`

**Techniques used:** t_auxiliary_construction, t_pigeonhole_collision, t_compactness_argument

---

### Vaught's test (cite: https://en.wikipedia.org/wiki/Vaught%27s_test)

**Axioms:** `s_first_order_theory_T_no_finite_models`, `s_kappa_categoricity`
**Terminal:** `s_vaught_test` (kind: theorem) — if T has no finite models and is κ-categorical for some κ ≥ |L(T)|, then T is complete.

**Steps:**
1. input: `s_kappa_categoricity` --[t_reductio_ad_absurdum {assume: incomplete_T}]--> output: `s_two_distinct_completions_T1_T2`
2. input: `s_two_distinct_completions_T1_T2` --[t_axiomatize_from_instances {use: downward_LS_to_kappa}]--> output: `s_two_kappa_sized_models_distinct`
3. input: `s_two_kappa_sized_models_distinct` --[t_reductio_ad_absurdum {contradict: kappa_categoricity}]--> output: `s_vaught_test`

**Techniques used:** t_reductio_ad_absurdum, t_axiomatize_from_instances

---

### Ryll-Nardzewski theorem (cite: https://en.wikipedia.org/wiki/Ryll-Nardzewski_theorem)

**Axioms:** `s_complete_countable_theory_T`, `s_type_space_S_n_T`
**Terminal:** `s_ryll_nardzewski_theorem` (kind: theorem) — T is ω-categorical iff S_n(T) is finite for every n.

**Steps:**
1. input: `s_complete_countable_theory_T` --[t_structural_isomorphism {to: stone_space_S_n_T}]--> output: `s_stone_space_of_T`
2. input: `s_stone_space_of_T` --[t_axiomatize_from_instances {pin: omega_categorical_iff_isolated_types_dense}]--> output: `s_isolated_types_dense_iff_omega_categorical`
3. input: `s_isolated_types_dense_iff_omega_categorical` --[t_compactness_argument {use: S_n_finite_implies_all_isolated}]--> output: `s_ryll_nardzewski_theorem`

**Techniques used:** t_structural_isomorphism, t_axiomatize_from_instances, t_compactness_argument

---

### Robinson's theorem on differentially closed fields (cite: https://en.wikipedia.org/wiki/Differential_algebra#Differentially_closed_fields)

**Axioms:** `s_differential_field`, `s_existential_closure`
**Terminal:** `s_DCF_0_model_complete` (kind: theorem) — DCF₀ is the model completion of differential fields of characteristic 0; it is ω-stable and admits quantifier elimination.

**Steps:**
1. input: `s_differential_field` --[t_axiomatize_from_instances {add: existential_closure_axioms}]--> output: `s_DCF_0_axioms`
2. input: `s_DCF_0_axioms` --[t_reduce_to_canonical_form {via: kolchin_seidenberg_QE}]--> output: `s_DCF_0_qe`
3. input: `s_DCF_0_qe` --[t_structural_isomorphism {to: omega_stable_theory}]--> output: `s_DCF_0_omega_stable`
4. input: `s_DCF_0_omega_stable` --[t_compose_with_identity {package}]--> output: `s_DCF_0_model_complete`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form, t_structural_isomorphism, t_compose_with_identity

---

### Hrushovski–Lascar group configuration / definable groups in stable theories (cite: https://en.wikipedia.org/wiki/Stable_group)

**Axioms:** `s_stable_theory_T`, `s_group_configuration_in_types`
**Terminal:** `s_hrushovski_lascar_group_configuration` (kind: theorem) — a generic group configuration in a stable theory gives rise to a type-definable group.

**Steps:**
1. input: `s_group_configuration_in_types` --[t_axiomatize_from_instances {extract: independence_diagram_with_associativity}]--> output: `s_associativity_diagram_of_types`
2. input: `s_associativity_diagram_of_types` --[t_auxiliary_construction {build: germ_of_definable_function}]--> output: `s_germ_of_group_multiplication`
3. input: `s_germ_of_group_multiplication` --[t_compose_with_identity {recover: type_definable_group}]--> output: `s_hrushovski_lascar_group_configuration`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_compose_with_identity

---

### Trichotomy in Zariski geometries / Hrushovski–Zilber (cite: https://en.wikipedia.org/wiki/Zilber_trichotomy)

**Axioms:** `s_strongly_minimal_set`, `s_geometry_of_algebraic_closure`
**Terminal:** `s_hrushovski_zilber_trichotomy` (kind: theorem) — every Zariski geometry is either disintegrated, locally modular nontrivial, or non-locally-modular (and then interprets an ACF).

**Steps:**
1. input: `s_strongly_minimal_set` --[t_axiomatize_from_instances {add: zariski_topology_axioms}]--> output: `s_zariski_geometry_axioms`
2. input: `s_zariski_geometry_axioms` --[t_auxiliary_construction {dichotomy: locally_modular_vs_not}]--> output: `s_local_modularity_dichotomy`
3. input: `s_local_modularity_dichotomy` --[t_structural_isomorphism {if: non_modular_recover_ACF}]--> output: `s_ACF_interpretation_in_non_modular_case`
4. input: `s_ACF_interpretation_in_non_modular_case` --[t_compose_with_identity {package: trichotomy}]--> output: `s_hrushovski_zilber_trichotomy`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism, t_compose_with_identity

---

### Lévy–Solovay theorem on indestructibility of large cardinals under small forcing (cite: https://en.wikipedia.org/wiki/L%C3%A9vy%E2%80%93Solovay_theorem)

**Axioms:** `s_measurable_cardinal_axiom`, `s_small_forcing_P_below_kappa`
**Terminal:** `s_levy_solovay_theorem` (kind: theorem) — small forcing preserves measurability (and similar large-cardinal properties).

**Steps:**
1. input: `s_measurable_cardinal_axiom` --[t_auxiliary_construction {use: normal_measure_U_in_ground_model}]--> output: `s_ground_normal_measure_U`
2. input: `s_ground_normal_measure_U` --[t_force_independence {force_with: small_P}]--> output: `s_generic_extension_V_G`
3. input: `s_generic_extension_V_G` --[t_auxiliary_construction {lift: U_to_U_star_in_V_G}]--> output: `s_lifted_measure_U_star`
4. input: `s_lifted_measure_U_star` --[t_compose_with_identity {package: measurability_preserved}]--> output: `s_levy_solovay_theorem`

**Techniques used:** t_auxiliary_construction, t_force_independence, t_compose_with_identity

---

### Easton's theorem on continuum function (cite: https://en.wikipedia.org/wiki/Easton%27s_theorem)

**Axioms:** `s_zfc_axioms`, `s_regular_cardinal_arithmetic`
**Terminal:** `s_easton_theorem` (kind: theorem) — for any class function F on regular cardinals satisfying König and monotonicity, there is a class forcing extension with 2^κ = F(κ) on regular κ.

**Steps:**
1. input: `s_regular_cardinal_arithmetic` --[t_axiomatize_from_instances {constraints: F_monotone_and_konig}]--> output: `s_easton_admissible_F`
2. input: `s_easton_admissible_F` --[t_auxiliary_construction {product: easton_class_forcing_P}]--> output: `s_easton_class_forcing`
3. input: `s_easton_class_forcing` --[t_force_independence {add: generic_at_every_regular_kappa}]--> output: `s_generic_extension_with_F`
4. input: `s_generic_extension_with_F` --[t_compose_with_identity {package: realization}]--> output: `s_easton_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_force_independence, t_compose_with_identity

---

### Silver's theorem on singular cardinals (cite: https://en.wikipedia.org/wiki/Silver%27s_theorem)

**Axioms:** `s_zfc_axioms`, `s_singular_cardinal_kappa_of_uncountable_cofinality`
**Terminal:** `s_silver_singular_cardinals_theorem` (kind: theorem) — if κ is singular of uncountable cofinality and GCH holds below κ on a stationary set, then 2^κ = κ⁺.

**Steps:**
1. input: `s_singular_cardinal_kappa_of_uncountable_cofinality` --[t_auxiliary_construction {find: stationary_set_of_GCH_points}]--> output: `s_stationary_GCH_carrier`
2. input: `s_stationary_GCH_carrier` --[t_auxiliary_construction {build: generic_ultrapower_via_NS_quotient}]--> output: `s_generic_ultrapower`
3. input: `s_generic_ultrapower` --[t_ultraproduct_transfer {push: GCH_through_quotient}]--> output: `s_2_kappa_bounded_in_quotient`
4. input: `s_2_kappa_bounded_in_quotient` --[t_compose_with_identity {extract: 2_kappa_equals_kappa_plus}]--> output: `s_silver_singular_cardinals_theorem`

**Techniques used:** t_auxiliary_construction, t_ultraproduct_transfer, t_compose_with_identity

---

### Solovay's stationary splitting theorem (cite: https://en.wikipedia.org/wiki/Stationary_set)

**Axioms:** `s_regular_uncountable_cardinal_kappa`, `s_stationary_subset_of_kappa`
**Terminal:** `s_solovay_stationary_splitting` (kind: theorem) — every stationary subset of a regular uncountable κ splits into κ many disjoint stationary subsets.

**Steps:**
1. input: `s_stationary_subset_of_kappa` --[t_auxiliary_construction {choose: regressive_function_via_Fodor}]--> output: `s_regressive_function_on_S`
2. input: `s_regressive_function_on_S` --[t_axiomatize_from_instances {apply: fodor_pressing_down}]--> output: `s_fodor_constancy_on_stationary_subset`
3. input: `s_fodor_constancy_on_stationary_subset` --[t_pigeonhole_collision {iterate: extract_kappa_disjoint_pieces}]--> output: `s_solovay_stationary_splitting`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_pigeonhole_collision

---

### Fodor's pressing-down lemma (cite: https://en.wikipedia.org/wiki/Fodor%27s_lemma)

**Axioms:** `s_regular_uncountable_cardinal_kappa`, `s_regressive_function_on_stationary_set`
**Terminal:** `s_fodor_lemma` (kind: theorem) — every regressive function on a stationary set is constant on a stationary subset.

**Steps:**
1. input: `s_regressive_function_on_stationary_set` --[t_reductio_ad_absurdum {assume: every_fibre_nonstationary}]--> output: `s_each_fibre_nonstationary`
2. input: `s_each_fibre_nonstationary` --[t_auxiliary_construction {diagonal_intersection: club_C}]--> output: `s_diagonal_intersection_club`
3. input: `s_diagonal_intersection_club` --[t_pigeonhole_collision {contradict: stationarity_of_S}]--> output: `s_fodor_lemma`

**Techniques used:** t_reductio_ad_absurdum, t_auxiliary_construction, t_pigeonhole_collision

---

### Solovay's theorem on real-valued measurable cardinals (cite: https://en.wikipedia.org/wiki/Real-valued_measurable_cardinal)

**Axioms:** `s_real_valued_measurable_cardinal`, `s_measure_extension_problem`
**Terminal:** `s_solovay_RVM_theorem` (kind: theorem) — Con(ZFC + measurable) ⇔ Con(ZFC + real-valued measurable continuum).

**Steps:**
1. input: `s_real_valued_measurable_cardinal` --[t_auxiliary_construction {build: random_forcing_extension_of_measurable_model}]--> output: `s_random_real_extension_over_measurable`
2. input: `s_random_real_extension_over_measurable` --[t_force_independence {use: random_real_forcing_at_kappa}]--> output: `s_RVM_continuum_witnessed`
3. input: `s_RVM_continuum_witnessed` --[t_duality {invert: RVM_to_measurable_via_quotient}]--> output: `s_solovay_RVM_theorem`

**Techniques used:** t_auxiliary_construction, t_force_independence, t_duality

---

### Suslin's hypothesis / ◊ implies a Suslin tree (Jensen) (cite: https://en.wikipedia.org/wiki/Suslin%27s_problem)

**Axioms:** `s_diamond_principle_on_omega_1`, `s_tree_of_height_omega_1`
**Terminal:** `s_diamond_implies_suslin_tree` (kind: theorem) — ◊ implies the existence of a Suslin tree (so ¬SH consistent with ZFC).

**Steps:**
1. input: `s_diamond_principle_on_omega_1` --[t_auxiliary_construction {use: diamond_sequence_predicts_antichains}]--> output: `s_diamond_anticipates_antichains`
2. input: `s_diamond_anticipates_antichains` --[t_interpolate_and_continue {induct: along_omega_1_levels}]--> output: `s_construct_tree_killing_each_predicted_antichain`
3. input: `s_construct_tree_killing_each_predicted_antichain` --[t_compose_with_identity {assemble: suslin_tree}]--> output: `s_diamond_implies_suslin_tree`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_compose_with_identity

---

### Martin's axiom and Suslin's hypothesis (cite: https://en.wikipedia.org/wiki/Martin%27s_axiom)

**Axioms:** `s_martins_axiom_MA_omega_1`, `s_ccc_partial_order`
**Terminal:** `s_MA_implies_SH` (kind: theorem) — MA(ω₁) implies Suslin's hypothesis (no Suslin trees).

**Steps:**
1. input: `s_martins_axiom_MA_omega_1` --[t_reductio_ad_absurdum {assume: suslin_tree_T_exists}]--> output: `s_hypothetical_suslin_tree`
2. input: `s_hypothetical_suslin_tree` --[t_axiomatize_from_instances {as: ccc_partial_order_T_inv}]--> output: `s_T_as_ccc_poset`
3. input: `s_T_as_ccc_poset` --[t_force_independence {apply: MA_to_get_branch_through_T}]--> output: `s_omega_1_branch_kills_suslin`
4. input: `s_omega_1_branch_kills_suslin` --[t_reductio_ad_absurdum {contradicts: T_being_suslin}]--> output: `s_MA_implies_SH`

**Techniques used:** t_reductio_ad_absurdum, t_axiomatize_from_instances, t_force_independence

---

### Proper Forcing Axiom consequences (Todorčević) (cite: https://en.wikipedia.org/wiki/Proper_forcing_axiom)

**Axioms:** `s_proper_forcing_axiom`, `s_countable_proper_forcing_class`
**Terminal:** `s_PFA_consequences` (kind: theorem) — PFA implies 2^ℵ₀ = ℵ₂, SH, and many structural dichotomies (e.g., open coloring axiom).

**Steps:**
1. input: `s_proper_forcing_axiom` --[t_axiomatize_from_instances {to: open_coloring_axiom_OCA}]--> output: `s_OCA_from_PFA`
2. input: `s_OCA_from_PFA` --[t_auxiliary_construction {ramsey_type_partition: into_continuous_pieces}]--> output: `s_structural_dichotomy_on_separable_metric_spaces`
3. input: `s_structural_dichotomy_on_separable_metric_spaces` --[t_compose_with_identity {derive: 2_aleph_0_equals_aleph_2_and_SH}]--> output: `s_PFA_consequences`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_compose_with_identity

---

### Halpern–Läuchli theorem (cite: https://en.wikipedia.org/wiki/Halpern%E2%80%93L%C3%A4uchli_theorem)

**Axioms:** `s_finite_product_of_finitely_branching_trees`, `s_finite_coloring`
**Terminal:** `s_halpern_lauchli_theorem` (kind: theorem) — any finite coloring of the level-product of d finitely branching infinite trees has a monochromatic strong subtree.

**Steps:**
1. input: `s_finite_product_of_finitely_branching_trees` --[t_auxiliary_construction {strong_subtree_at_each_level: combinatorial_witness}]--> output: `s_strong_subtree_template`
2. input: `s_strong_subtree_template` --[t_pigeonhole_collision {bound: finite_coloring_per_level}]--> output: `s_per_level_monochromatic_choice`
3. input: `s_per_level_monochromatic_choice` --[t_compactness_argument {assemble: monochromatic_subtree_via_dependent_choice}]--> output: `s_halpern_lauchli_theorem`

**Techniques used:** t_auxiliary_construction, t_pigeonhole_collision, t_compactness_argument

---

### Galvin–Prikry theorem (cite: https://en.wikipedia.org/wiki/Galvin%E2%80%93Prikry_theorem)

**Axioms:** `s_borel_subset_of_omega_omega`, `s_infinite_subsets_of_omega`
**Terminal:** `s_galvin_prikry_theorem` (kind: theorem) — every Borel subset of [ω]^ω is Ramsey: contains or is disjoint from [A]^ω for some infinite A.

**Steps:**
1. input: `s_borel_subset_of_omega_omega` --[t_reduce_to_canonical_form {form: open_or_closed_via_borel_hierarchy}]--> output: `s_open_case_reduction`
2. input: `s_open_case_reduction` --[t_auxiliary_construction {ramsey_game: galvin_prikry_game}]--> output: `s_galvin_prikry_game`
3. input: `s_galvin_prikry_game` --[t_axiomatize_from_instances {apply: open_determinacy_or_compactness}]--> output: `s_winning_strategy_yields_homogeneous_A`
4. input: `s_winning_strategy_yields_homogeneous_A` --[t_compose_with_identity {package: ramsey_property}]--> output: `s_galvin_prikry_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_axiomatize_from_instances, t_compose_with_identity

---

### Higman's embedding theorem (cite: https://en.wikipedia.org/wiki/Higman%27s_embedding_theorem)

**Axioms:** `s_finitely_generated_group_with_re_presentation`, `s_finitely_presented_group`
**Terminal:** `s_higman_embedding_theorem` (kind: theorem) — a finitely generated group has a recursively enumerable presentation iff it embeds in a finitely presented group.

**Steps:**
1. input: `s_finitely_generated_group_with_re_presentation` --[t_arithmetize_syntax {encode: presentation_as_machine_M}]--> output: `s_machine_encoding_of_presentation`
2. input: `s_machine_encoding_of_presentation` --[t_auxiliary_construction {use: HNN_extensions_simulating_M}]--> output: `s_HNN_simulator_for_M`
3. input: `s_HNN_simulator_for_M` --[t_compose_with_identity {package: into_fp_group}]--> output: `s_finitely_presented_supergroup`
4. input: `s_finitely_presented_supergroup` --[t_duality {direction: fp_implies_re}]--> output: `s_higman_embedding_theorem`

**Techniques used:** t_arithmetize_syntax, t_auxiliary_construction, t_compose_with_identity, t_duality

---

### Word problem for groups (Novikov–Boone) (cite: https://en.wikipedia.org/wiki/Word_problem_for_groups)

**Axioms:** `s_finitely_presented_group`, `s_undecidability_of_halting`
**Terminal:** `s_novikov_boone_theorem` (kind: theorem) — there exists a finitely presented group with unsolvable word problem.

**Steps:**
1. input: `s_undecidability_of_halting` --[t_arithmetize_syntax {encode: turing_machine_as_semigroup_presentation}]--> output: `s_semigroup_encoding_of_TM`
2. input: `s_semigroup_encoding_of_TM` --[t_auxiliary_construction {build: group_via_HNN_extensions}]--> output: `s_group_simulating_TM`
3. input: `s_group_simulating_TM` --[t_reductio_ad_absurdum {assume: word_problem_decidable}]--> output: `s_novikov_boone_theorem`

**Techniques used:** t_arithmetize_syntax, t_auxiliary_construction, t_reductio_ad_absurdum

---
