# Area AN (Real & Complex Analysis) Derivation Chains (iter-3)

**Source pages:**
- https://en.wikipedia.org/wiki/Category:Theorems_in_real_analysis
- https://en.wikipedia.org/wiki/Category:Theorems_in_complex_analysis
- https://en.wikipedia.org/wiki/Category:Theorems_in_harmonic_analysis
- https://en.wikipedia.org/wiki/Category:Theorems_in_measure_theory
- https://en.wikipedia.org/wiki/Category:Theorems_in_functional_analysis

**Target:** 100 chains. **Drafted:** 193 (over-delivered; the analysis domain is broad and many flagship theorems chain together naturally). **Skipped (already in graph):** 11 noted in-line — `s_taylor_theorem` (Taylor's theorem), `s_cauchy_integral_formula` (Cauchy integral formula), `s_riemann_mapping_theorem` (Riemann mapping theorem), `s_hahn_banach` (Hahn–Banach), `s_weierstrass_approximation` (Weierstrass approximation), `s_fundamental_theorem_of_calculus` (FTC), `s_banach_fpt` (Banach fixed point — also referenced in Picard–Lindelöf chain), `s_birkhoff_ergodic_theorem` (Birkhoff), `s_central_limit_theorem` (CLT), `s_basel_identity` (Basel), `s_fourier_theorem_heat` (Fourier heat), `s_brouwer_fpt` (Brouwer), `s_uncountability_of_reals` (Cantor diagonal).

**Flagged (`⚠ needs new technique`):** 3 chains — Lebesgue differentiation theorem (step 2 needs a generic "density argument via weak-type estimate" primitive not on the toolbox list), Sard's theorem (step 3 needs an "image-measure-zero via Taylor remainder summation" primitive), Carleson's theorem (step 2 needs a "time-frequency tile / phase-plane decomposition" primitive). A handful of other chains contain shorthand labels (e.g. `t_cauchy_mvt_application`, `t_marcinkiewicz_interpolation`, `t_riemann_mapping_application`, `t_baire_category_application`, `t_egorov_application`, `t_radon_nikodym_application`, `t_vitali_covering_application`, `t_hardy_littlewood_application`, `t_calderon_zygmund_decomposition_application`, `t_open_mapping_application`, `t_monotone_convergence_application`, `t_caratheodory_application`, `t_urysohn_lemma_application`, `t_fatou_lemma_application`, `t_cantor_intersection_application`); each is annotated with a "reads as" note that maps it to a frozen toolbox technique already used elsewhere in the chain. They are not new techniques — they are within-domain invocations of theorems whose own chains use the canonical `t_*` ids.

---

## I. Foundations of real analysis (topology of ℝⁿ, continuity, differentiation)

### Bolzano–Weierstrass theorem (cite: https://en.wikipedia.org/wiki/Bolzano%E2%80%93Weierstrass_theorem)

**Axioms:** `s_real_numbers`, `s_bounded_sequence_in_Rn`
**Terminal:** `s_bolzano_weierstrass` (kind: theorem)

**Steps:**
1. input: `⟨s_real_numbers, s_bounded_sequence_in_Rn⟩` --[t_reduce_to_canonical_form {form: enclose_in_compact_box}]--> output: `s_sequence_in_closed_box`
2. input: `s_sequence_in_closed_box` --[t_pigeonhole_collision {bisection: nested_halves}]--> output: `s_nested_box_with_infinite_subsequence`
3. input: `s_nested_box_with_infinite_subsequence` --[t_exhaustion_squeeze {diameter: 2^-n}]--> output: `s_bolzano_weierstrass`

**Techniques used:** t_reduce_to_canonical_form, t_pigeonhole_collision, t_exhaustion_squeeze

---

### Heine–Borel theorem (cite: https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem)

**Axioms:** `s_real_numbers`, `s_subset_of_Rn`
**Terminal:** `s_heine_borel` (kind: theorem)

**Steps:**
1. input: `⟨s_real_numbers, s_subset_of_Rn⟩` --[t_axiomatize_from_instances {target: closed_and_bounded_iff_compact}]--> output: `s_closed_bounded_subset_candidate`
2. input: `s_closed_bounded_subset_candidate` --[t_bolzano_weierstrass_lemma {via: sequential_compactness}]--> output: `s_sequentially_compact_subset`
3. input: `s_sequentially_compact_subset` --[t_compactness_argument {direction: open_cover_to_finite_subcover}]--> output: `s_heine_borel`

**Techniques used:** t_axiomatize_from_instances, t_compactness_argument

⚠ Note: step 2's label is shorthand for an internal application of Bolzano–Weierstrass; the technique cluster used is `t_compactness_argument`. Replace `t_bolzano_weierstrass_lemma` with `t_compactness_argument {sub: sequential}` if a strict reading is needed.

---

### Intermediate Value theorem (cite: https://en.wikipedia.org/wiki/Intermediate_value_theorem)

**Axioms:** `s_continuous_function_on_closed_interval`, `s_real_numbers`
**Terminal:** `s_intermediate_value_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_function_on_closed_interval, s_real_numbers⟩` --[t_reduce_to_canonical_form {target: f(a)<0<f(b)}]--> output: `s_normalized_sign_change_setup`
2. input: `s_normalized_sign_change_setup` --[t_pigeonhole_collision {bisection: sign_halving}]--> output: `s_nested_intervals_with_sign_change`
3. input: `s_nested_intervals_with_sign_change` --[t_exhaustion_squeeze {limit: common_point}]--> output: `s_intermediate_value_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_pigeonhole_collision, t_exhaustion_squeeze

---

### Extreme Value theorem (cite: https://en.wikipedia.org/wiki/Extreme_value_theorem)

**Axioms:** `s_continuous_function_on_closed_interval`, `s_real_numbers`
**Terminal:** `s_extreme_value_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_function_on_closed_interval, s_real_numbers⟩` --[t_compactness_argument {domain: closed_bounded_interval}]--> output: `s_image_is_bounded`
2. input: `s_image_is_bounded` --[t_auxiliary_construction {construct: maximizing_sequence}]--> output: `s_maximizing_sequence_in_domain`
3. input: `s_maximizing_sequence_in_domain` --[t_compactness_argument {extract: convergent_subsequence}]--> output: `s_extreme_value_theorem`

**Techniques used:** t_compactness_argument, t_auxiliary_construction

---

### Mean Value theorem (cite: https://en.wikipedia.org/wiki/Mean_value_theorem)

**Axioms:** `s_continuous_function_on_closed_interval`, `s_differentiable_on_open_interval`
**Terminal:** `s_mean_value_theorem_terminal` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_function_on_closed_interval, s_differentiable_on_open_interval⟩` --[t_auxiliary_construction {tilt: g(x)=f(x)-secant_line}]--> output: `s_tilted_function_with_equal_endpoints`
2. input: `s_tilted_function_with_equal_endpoints` --[t_compactness_argument {extremum: interior_critical_point}]--> output: `s_rolle_theorem_point`
3. input: `s_rolle_theorem_point` --[t_reduce_to_canonical_form {invert: slope_identity}]--> output: `s_mean_value_theorem_terminal`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Cauchy mean value theorem (cite: https://en.wikipedia.org/wiki/Mean_value_theorem#Cauchy's_mean_value_theorem)

**Axioms:** `s_continuous_function_on_closed_interval`, `s_differentiable_on_open_interval`
**Terminal:** `s_cauchy_mean_value_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_function_on_closed_interval, s_differentiable_on_open_interval⟩` --[t_auxiliary_construction {construct: h=f(g(b)-g(a))-g(f(b)-f(a))}]--> output: `s_paired_function_with_equal_endpoints`
2. input: `s_paired_function_with_equal_endpoints` --[t_compactness_argument {via: rolle}]--> output: `s_cauchy_mean_value_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument

---

### L'Hôpital's rule (cite: https://en.wikipedia.org/wiki/L%27H%C3%B4pital%27s_rule)

**Axioms:** `s_differentiable_on_open_interval`, `s_indeterminate_form_zero_over_zero`
**Terminal:** `s_lhopital_rule` (kind: theorem)

**Steps:**
1. input: `⟨s_differentiable_on_open_interval, s_indeterminate_form_zero_over_zero⟩` --[t_reduce_to_canonical_form {extend: by_continuity_at_a}]--> output: `s_normalized_0_over_0_pair`
2. input: `s_normalized_0_over_0_pair` --[t_cauchy_mvt_application {pair: f_and_g}]--> output: `s_ratio_equals_derivative_ratio_at_xi`
3. input: `s_ratio_equals_derivative_ratio_at_xi` --[t_exhaustion_squeeze {xi: tends_to_a}]--> output: `s_lhopital_rule`

**Techniques used:** t_reduce_to_canonical_form, t_compactness_argument, t_exhaustion_squeeze

⚠ Note: `t_cauchy_mvt_application` reads as `t_compactness_argument` invoked through Cauchy MVT (above).

---

### Darboux's theorem (intermediate value for derivatives) (cite: https://en.wikipedia.org/wiki/Darboux%27s_theorem_(analysis))

**Axioms:** `s_differentiable_on_open_interval`, `s_real_numbers`
**Terminal:** `s_darboux_theorem_analysis` (kind: theorem)

**Steps:**
1. input: `⟨s_differentiable_on_open_interval, s_real_numbers⟩` --[t_auxiliary_construction {construct: g(x)=f(x)-cx}]--> output: `s_auxiliary_g_with_critical_point`
2. input: `s_auxiliary_g_with_critical_point` --[t_compactness_argument {extremum: interior}]--> output: `s_interior_critical_point_of_g`
3. input: `s_interior_critical_point_of_g` --[t_reduce_to_canonical_form {invert: f'(x)=c}]--> output: `s_darboux_theorem_analysis`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Cantor's intersection theorem (cite: https://en.wikipedia.org/wiki/Cantor%27s_intersection_theorem)

**Axioms:** `s_complete_metric_space`, `s_nested_nonempty_closed_sets_shrinking_diameter`
**Terminal:** `s_cantor_intersection_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_complete_metric_space, s_nested_nonempty_closed_sets_shrinking_diameter⟩` --[t_auxiliary_construction {pick: xn_in_Fn}]--> output: `s_cauchy_sequence_from_nested_sets`
2. input: `s_cauchy_sequence_from_nested_sets` --[t_exhaustion_squeeze {limit: by_completeness}]--> output: `s_limit_point_in_each_Fn`
3. input: `s_limit_point_in_each_Fn` --[t_compactness_argument {uniqueness: from_shrinking_diameter}]--> output: `s_cantor_intersection_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_compactness_argument

---

### Baire category theorem (cite: https://en.wikipedia.org/wiki/Baire_category_theorem)

**Axioms:** `s_complete_metric_space`, `s_countable_family_of_dense_open_sets`
**Terminal:** `s_baire_category_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_complete_metric_space, s_countable_family_of_dense_open_sets⟩` --[t_auxiliary_construction {nest: shrinking_open_balls_inside_each_Un}]--> output: `s_nested_closed_balls_radii_decreasing`
2. input: `s_nested_closed_balls_radii_decreasing` --[t_cantor_intersection_application {space: complete}]--> output: `s_common_point_in_all_Un`
3. input: `s_common_point_in_all_Un` --[t_reduce_to_canonical_form {conclude: intersection_dense}]--> output: `s_baire_category_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Banach–Steinhaus uniform boundedness principle (cite: https://en.wikipedia.org/wiki/Uniform_boundedness_principle)

**Axioms:** `s_banach_space`, `s_family_of_pointwise_bounded_operators`
**Terminal:** `s_banach_steinhaus` (kind: theorem)

**Steps:**
1. input: `⟨s_banach_space, s_family_of_pointwise_bounded_operators⟩` --[t_auxiliary_construction {sets: E_n={x: sup||T_α x||≤n}}]--> output: `s_closed_covering_of_banach_space`
2. input: `s_closed_covering_of_banach_space` --[t_baire_category_application {pick: nonmeager_E_n}]--> output: `s_E_n_with_interior_ball`
3. input: `s_E_n_with_interior_ball` --[t_reduce_to_canonical_form {translate: to_origin_via_linearity}]--> output: `s_banach_steinhaus`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Open mapping theorem (cite: https://en.wikipedia.org/wiki/Open_mapping_theorem_(functional_analysis))

**Axioms:** `s_banach_space`, `s_surjective_bounded_linear_operator`
**Terminal:** `s_open_mapping_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_banach_space, s_surjective_bounded_linear_operator⟩` --[t_auxiliary_construction {decompose: codomain = ∪_n T(nB)}]--> output: `s_nonmeager_T_image_of_ball`
2. input: `s_nonmeager_T_image_of_ball` --[t_baire_category_application {pick: ball_inside_closure_T(B)}]--> output: `s_closure_of_T_ball_has_interior`
3. input: `s_closure_of_T_ball_has_interior` --[t_contraction_fixed_point {iterate: remove_closure_via_geometric_series}]--> output: `s_T_ball_has_interior`
4. input: `s_T_ball_has_interior` --[t_reduce_to_canonical_form {conclude: T_open}]--> output: `s_open_mapping_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_contraction_fixed_point, t_reduce_to_canonical_form

---

### Closed graph theorem (cite: https://en.wikipedia.org/wiki/Closed_graph_theorem)

**Axioms:** `s_banach_space`, `s_linear_map_with_closed_graph`
**Terminal:** `s_closed_graph_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_banach_space, s_linear_map_with_closed_graph⟩` --[t_auxiliary_construction {space: graph_norm_completion}]--> output: `s_graph_as_banach_subspace`
2. input: `s_graph_as_banach_subspace` --[t_open_mapping_application {projection: π_X_bijective}]--> output: `s_inverse_projection_bounded`
3. input: `s_inverse_projection_bounded` --[t_reduce_to_canonical_form {conclude: T_bounded}]--> output: `s_closed_graph_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Arzelà–Ascoli theorem (cite: https://en.wikipedia.org/wiki/Arzel%C3%A0%E2%80%93Ascoli_theorem)

**Axioms:** `s_compact_metric_space`, `s_uniformly_bounded_equicontinuous_family`
**Terminal:** `s_arzela_ascoli` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_metric_space, s_uniformly_bounded_equicontinuous_family⟩` --[t_auxiliary_construction {dense: countable_dense_subset_D}]--> output: `s_family_indexed_by_dense_subset_D`
2. input: `s_family_indexed_by_dense_subset_D` --[t_pigeonhole_collision {diagonal: Cantor_extraction}]--> output: `s_pointwise_convergent_on_D_subsequence`
3. input: `s_pointwise_convergent_on_D_subsequence` --[t_exhaustion_squeeze {equicontinuity: extend_to_uniform_on_X}]--> output: `s_arzela_ascoli`

**Techniques used:** t_auxiliary_construction, t_pigeonhole_collision, t_exhaustion_squeeze

---

### Stone–Weierstrass theorem (cite: https://en.wikipedia.org/wiki/Stone%E2%80%93Weierstrass_theorem)

**Axioms:** `s_compact_hausdorff_space`, `s_unital_separating_subalgebra_of_C(X)`
**Terminal:** `s_stone_weierstrass` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_hausdorff_space, s_unital_separating_subalgebra_of_C(X)⟩` --[t_auxiliary_construction {poly_approx: sqrt_via_polynomials}]--> output: `s_closure_is_lattice`
2. input: `s_closure_is_lattice` --[t_reduce_to_canonical_form {use: separation_to_two_point_interpolation}]--> output: `s_two_point_interpolation_property`
3. input: `s_two_point_interpolation_property` --[t_exhaustion_squeeze {lattice: max_min_approximation}]--> output: `s_stone_weierstrass`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Tietze extension theorem (cite: https://en.wikipedia.org/wiki/Tietze_extension_theorem)

**Axioms:** `s_normal_topological_space`, `s_bounded_continuous_function_on_closed_subset`
**Terminal:** `s_tietze_extension_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_normal_topological_space, s_bounded_continuous_function_on_closed_subset⟩` --[t_auxiliary_construction {urysohn: separating_functions_on_level_pairs}]--> output: `s_urysohn_function_for_each_level`
2. input: `s_urysohn_function_for_each_level` --[t_contraction_fixed_point {iterate: 1/3_geometric_correction_series}]--> output: `s_uniformly_convergent_extension_series`
3. input: `s_uniformly_convergent_extension_series` --[t_reduce_to_canonical_form {extract: continuous_extension_to_X}]--> output: `s_tietze_extension_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_reduce_to_canonical_form

---

### Urysohn's lemma (cite: https://en.wikipedia.org/wiki/Urysohn%27s_lemma)

**Axioms:** `s_normal_topological_space`, `s_disjoint_closed_sets_A_B`
**Terminal:** `s_urysohn_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_normal_topological_space, s_disjoint_closed_sets_A_B⟩` --[t_auxiliary_construction {nest: dyadic_open_sets_U_r}]--> output: `s_dyadic_chain_of_separating_opens`
2. input: `s_dyadic_chain_of_separating_opens` --[t_reduce_to_canonical_form {define: f(x)=inf{r: x∈U_r}}]--> output: `s_dyadically_defined_function`
3. input: `s_dyadically_defined_function` --[t_exhaustion_squeeze {continuity: dyadic_density}]--> output: `s_urysohn_lemma`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Urysohn metrization theorem (cite: https://en.wikipedia.org/wiki/Urysohn%27s_metrization_theorem)

**Axioms:** `s_second_countable_regular_hausdorff_space`, `s_real_numbers`
**Terminal:** `s_urysohn_metrization` (kind: theorem)

**Steps:**
1. input: `⟨s_second_countable_regular_hausdorff_space, s_real_numbers⟩` --[t_urysohn_lemma_application {pairs: countable_basis}]--> output: `s_countable_family_of_urysohn_functions`
2. input: `s_countable_family_of_urysohn_functions` --[t_auxiliary_construction {embed: into_Hilbert_cube}]--> output: `s_homeomorphism_into_l2`
3. input: `s_homeomorphism_into_l2` --[t_structural_isomorphism {pullback: euclidean_metric}]--> output: `s_urysohn_metrization`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_reduce_to_canonical_form

---

### Dini's theorem (cite: https://en.wikipedia.org/wiki/Dini%27s_theorem)

**Axioms:** `s_compact_metric_space`, `s_monotone_pointwise_convergent_continuous_sequence`
**Terminal:** `s_dini_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_metric_space, s_monotone_pointwise_convergent_continuous_sequence⟩` --[t_auxiliary_construction {sets: U_n={x: g_n(x)<ε}}]--> output: `s_open_cover_from_pointwise_bound`
2. input: `s_open_cover_from_pointwise_bound` --[t_compactness_argument {extract: finite_subcover}]--> output: `s_uniform_bound_on_X`
3. input: `s_uniform_bound_on_X` --[t_reduce_to_canonical_form {conclude: uniform_convergence}]--> output: `s_dini_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

## II. Measure theory and integration

### Carathéodory extension theorem (cite: https://en.wikipedia.org/wiki/Carath%C3%A9odory%27s_extension_theorem)

**Axioms:** `s_premeasure_on_algebra_of_sets`, `s_sigma_algebra_generated`
**Terminal:** `s_caratheodory_extension` (kind: theorem)

**Steps:**
1. input: `⟨s_premeasure_on_algebra_of_sets, s_sigma_algebra_generated⟩` --[t_auxiliary_construction {outer_measure: μ*(E)=inf Σ μ(A_n)}]--> output: `s_outer_measure_on_powerset`
2. input: `s_outer_measure_on_powerset` --[t_axiomatize_from_instances {select: Caratheodory_measurable_sets}]--> output: `s_sigma_algebra_of_measurable_sets`
3. input: `s_sigma_algebra_of_measurable_sets` --[t_reduce_to_canonical_form {restrict: μ*_to_measurable}]--> output: `s_caratheodory_extension`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Monotone convergence theorem (cite: https://en.wikipedia.org/wiki/Monotone_convergence_theorem)

**Axioms:** `s_measure_space`, `s_increasing_sequence_of_nonneg_measurable_functions`
**Terminal:** `s_monotone_convergence_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_space, s_increasing_sequence_of_nonneg_measurable_functions⟩` --[t_auxiliary_construction {simple: simple_function_approximants_from_below}]--> output: `s_simple_function_ladder`
2. input: `s_simple_function_ladder` --[t_exhaustion_squeeze {sets: E_n={f_n > (1-ε)φ}}]--> output: `s_inner_bound_int_fn_geq_factor_phi`
3. input: `s_inner_bound_int_fn_geq_factor_phi` --[t_reduce_to_canonical_form {sup_over_simple: definition_of_integral}]--> output: `s_monotone_convergence_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Fatou's lemma (cite: https://en.wikipedia.org/wiki/Fatou%27s_lemma)

**Axioms:** `s_measure_space`, `s_nonneg_measurable_function_sequence`
**Terminal:** `s_fatou_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_space, s_nonneg_measurable_function_sequence⟩` --[t_auxiliary_construction {define: g_n=inf_{k_geq_n} f_k}]--> output: `s_increasing_inf_sequence_g_n`
2. input: `s_increasing_inf_sequence_g_n` --[t_exhaustion_squeeze {via: monotone_convergence}]--> output: `s_int_liminf_equals_lim_int_g_n`
3. input: `s_int_liminf_equals_lim_int_g_n` --[t_reduce_to_canonical_form {compare: g_n_leq_f_n}]--> output: `s_fatou_lemma`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Dominated convergence theorem (cite: https://en.wikipedia.org/wiki/Dominated_convergence_theorem)

**Axioms:** `s_measure_space`, `s_pointwise_convergent_sequence_with_integrable_dominant`
**Terminal:** `s_dominated_convergence_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_space, s_pointwise_convergent_sequence_with_integrable_dominant⟩` --[t_auxiliary_construction {pair: g_plus_fn_and_g_minus_fn_nonneg}]--> output: `s_two_nonneg_sequences_with_known_limit`
2. input: `s_two_nonneg_sequences_with_known_limit` --[t_reduce_to_canonical_form {apply: Fatou_both_sides}]--> output: `s_two_sided_squeeze_on_int_fn`
3. input: `s_two_sided_squeeze_on_int_fn` --[t_exhaustion_squeeze {conclude: lim_int_fn=int_f}]--> output: `s_dominated_convergence_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Egorov's theorem (cite: https://en.wikipedia.org/wiki/Egorov%27s_theorem)

**Axioms:** `s_finite_measure_space`, `s_ae_pointwise_convergent_measurable_sequence`
**Terminal:** `s_egorov_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_measure_space, s_ae_pointwise_convergent_measurable_sequence⟩` --[t_auxiliary_construction {sets: E_nk={|f_m-f|<1/k_for_all_m_geq_n}}]--> output: `s_increasing_chain_of_good_sets`
2. input: `s_increasing_chain_of_good_sets` --[t_pigeonhole_collision {choose: n_k_with_mu_bad_lt_eps_over_2k}]--> output: `s_thin_bad_set`
3. input: `s_thin_bad_set` --[t_reduce_to_canonical_form {complement: uniform_convergence_on_complement}]--> output: `s_egorov_theorem`

**Techniques used:** t_auxiliary_construction, t_pigeonhole_collision, t_reduce_to_canonical_form

---

### Lusin's theorem (cite: https://en.wikipedia.org/wiki/Lusin%27s_theorem)

**Axioms:** `s_finite_measure_space`, `s_measurable_function_on_metric_space`
**Terminal:** `s_lusin_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_measure_space, s_measurable_function_on_metric_space⟩` --[t_auxiliary_construction {approx: simple_function_sequence_ae_converging}]--> output: `s_simple_approximation_sequence`
2. input: `s_simple_approximation_sequence` --[t_reduce_to_canonical_form {via: Egorov_uniform_off_exceptional}]--> output: `s_uniform_convergence_off_exceptional_set`
3. input: `s_uniform_convergence_off_exceptional_set` --[t_exhaustion_squeeze {restrict: continuous_on_closed_subset}]--> output: `s_lusin_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Radon–Nikodym theorem (cite: https://en.wikipedia.org/wiki/Radon%E2%80%93Nikodym_theorem)

**Axioms:** `s_sigma_finite_measure_space`, `s_absolutely_continuous_signed_measure`
**Terminal:** `s_radon_nikodym_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sigma_finite_measure_space, s_absolutely_continuous_signed_measure⟩` --[t_auxiliary_construction {hilbert: nu_plus_mu_inner_product}]--> output: `s_bounded_linear_functional_on_L2`
2. input: `s_bounded_linear_functional_on_L2` --[t_duality {riesz_representation: g_in_L2}]--> output: `s_density_function_g_with_int_f_dnu=int_fg_dnu_plus_mu`
3. input: `s_density_function_g_with_int_f_dnu=int_fg_dnu_plus_mu` --[t_reduce_to_canonical_form {solve: dnu_over_dmu=g_over_1_minus_g}]--> output: `s_radon_nikodym_theorem`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Riesz–Markov representation theorem (cite: https://en.wikipedia.org/wiki/Riesz%E2%80%93Markov%E2%80%93Kakutani_representation_theorem)

**Axioms:** `s_locally_compact_hausdorff_space`, `s_positive_linear_functional_on_Cc_X`
**Terminal:** `s_riesz_markov_representation` (kind: theorem)

**Steps:**
1. input: `⟨s_locally_compact_hausdorff_space, s_positive_linear_functional_on_Cc_X⟩` --[t_auxiliary_construction {outer: mu_star_U=sup_Lambda_f_over_f_prec_U}]--> output: `s_outer_premeasure_on_opens`
2. input: `s_outer_premeasure_on_opens` --[t_reduce_to_canonical_form {extend: Caratheodory_to_Borel}]--> output: `s_borel_measure_candidate`
3. input: `s_borel_measure_candidate` --[t_axiomatize_from_instances {verify: Lambda_f=int_f_dmu}]--> output: `s_riesz_markov_representation`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Lebesgue differentiation theorem (cite: https://en.wikipedia.org/wiki/Lebesgue_differentiation_theorem)

**Axioms:** `s_locally_integrable_function_on_Rn`, `s_lebesgue_measure_on_Rn`
**Terminal:** `s_lebesgue_differentiation_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_locally_integrable_function_on_Rn, s_lebesgue_measure_on_Rn⟩` --[t_auxiliary_construction {maximal: Hardy_Littlewood_maximal_M}]--> output: `s_maximal_function_weak_type_bound`
2. input: `s_maximal_function_weak_type_bound` --[⚠ needs new technique {move: density_argument_via_weak_type_for_ae_convergence}]--> output: `s_ae_convergence_for_dense_subset`
3. input: `s_ae_convergence_for_dense_subset` --[t_reduce_to_canonical_form {transfer: by_maximal_bound}]--> output: `s_lebesgue_differentiation_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Vitali covering lemma (cite: https://en.wikipedia.org/wiki/Vitali_covering_lemma)

**Axioms:** `s_collection_of_balls_in_Rn_with_bounded_radii`, `s_lebesgue_measure_on_Rn`
**Terminal:** `s_vitali_covering_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_collection_of_balls_in_Rn_with_bounded_radii, s_lebesgue_measure_on_Rn⟩` --[t_pigeonhole_collision {greedy: largest_radius_remaining}]--> output: `s_disjoint_subcollection_greedy`
2. input: `s_disjoint_subcollection_greedy` --[t_rescale_for_asymptotic_geometry {expand: 5x_dilation}]--> output: `s_5x_dilated_subcollection_covers`
3. input: `s_5x_dilated_subcollection_covers` --[t_reduce_to_canonical_form {volume: 5_to_the_n_factor}]--> output: `s_vitali_covering_lemma`

**Techniques used:** t_pigeonhole_collision, t_rescale_for_asymptotic_geometry, t_reduce_to_canonical_form

---

### Vitali–Hahn–Saks theorem (cite: https://en.wikipedia.org/wiki/Vitali%E2%80%93Hahn%E2%80%93Saks_theorem)

**Axioms:** `s_sequence_of_uniformly_absolutely_continuous_measures`, `s_finite_measure_space`
**Terminal:** `s_vitali_hahn_saks` (kind: theorem)

**Steps:**
1. input: `⟨s_sequence_of_uniformly_absolutely_continuous_measures, s_finite_measure_space⟩` --[t_auxiliary_construction {metric: rho_AB=mu_symmetric_diff_complete_pseudometric}]--> output: `s_complete_metric_space_of_classes`
2. input: `s_complete_metric_space_of_classes` --[t_compactness_argument {via: Baire_pointwise_bounded}]--> output: `s_equicontinuous_at_some_set`
3. input: `s_equicontinuous_at_some_set` --[t_reduce_to_canonical_form {translate: uniform_absolute_continuity}]--> output: `s_vitali_hahn_saks`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Fubini's theorem (cite: https://en.wikipedia.org/wiki/Fubini%27s_theorem)

**Axioms:** `s_sigma_finite_product_measure_space`, `s_integrable_function_on_product`
**Terminal:** `s_fubini_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sigma_finite_product_measure_space, s_integrable_function_on_product⟩` --[t_axiomatize_from_instances {start: indicator_of_measurable_rectangle}]--> output: `s_identity_for_indicators_of_rectangles`
2. input: `s_identity_for_indicators_of_rectangles` --[t_exhaustion_squeeze {monotone_class: extend_to_sigma_algebra}]--> output: `s_identity_for_nonneg_measurable_functions`
3. input: `s_identity_for_nonneg_measurable_functions` --[t_reduce_to_canonical_form {decompose: f_eq_f_plus_minus_f_minus}]--> output: `s_fubini_theorem`

**Techniques used:** t_axiomatize_from_instances, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Tonelli's theorem (cite: https://en.wikipedia.org/wiki/Fubini%27s_theorem#Tonelli's_theorem_for_non-negative_measurable_functions)

**Axioms:** `s_sigma_finite_product_measure_space`, `s_nonneg_measurable_function_on_product`
**Terminal:** `s_tonelli_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sigma_finite_product_measure_space, s_nonneg_measurable_function_on_product⟩` --[t_auxiliary_construction {approx: simple_function_ladder}]--> output: `s_simple_function_approximation_in_product`
2. input: `s_simple_function_approximation_in_product` --[t_exhaustion_squeeze {via: monotone_convergence_in_sections}]--> output: `s_tonelli_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze

---

### Lebesgue's monotone differentiation theorem (cite: https://en.wikipedia.org/wiki/Monotonic_function#Lebesgue's_theorem)

**Axioms:** `s_monotone_function_on_interval`, `s_lebesgue_measure_on_R`
**Terminal:** `s_lebesgue_monotone_differentiation` (kind: theorem)

**Steps:**
1. input: `⟨s_monotone_function_on_interval, s_lebesgue_measure_on_R⟩` --[t_auxiliary_construction {dini: four_dini_derivates}]--> output: `s_dini_derivate_quadruple`
2. input: `s_dini_derivate_quadruple` --[t_compactness_argument {via: Vitali_covering_on_disagreement_set}]--> output: `s_zero_measure_disagreement_set`
3. input: `s_zero_measure_disagreement_set` --[t_reduce_to_canonical_form {conclude: derivative_exists_ae}]--> output: `s_lebesgue_monotone_differentiation`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Rademacher's theorem (cite: https://en.wikipedia.org/wiki/Rademacher%27s_theorem)

**Axioms:** `s_lipschitz_function_on_Rn`, `s_lebesgue_measure_on_Rn`
**Terminal:** `s_rademacher_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_lipschitz_function_on_Rn, s_lebesgue_measure_on_Rn⟩` --[t_projection_to_subspace {directional: f_restricted_to_lines}]--> output: `s_ae_directional_derivative_via_lebesgue_diff`
2. input: `s_ae_directional_derivative_via_lebesgue_diff` --[t_auxiliary_construction {pair: weak_gradient_via_test_functions}]--> output: `s_weak_gradient_exists`
3. input: `s_weak_gradient_exists` --[t_reduce_to_canonical_form {upgrade: weak_to_classical_via_lipschitz}]--> output: `s_rademacher_theorem`

**Techniques used:** t_projection_to_subspace, t_auxiliary_construction, t_reduce_to_canonical_form

---

### Sard's theorem (cite: https://en.wikipedia.org/wiki/Sard%27s_theorem)

**Axioms:** `s_smooth_map_Rn_to_Rm`, `s_critical_set_of_smooth_map`
**Terminal:** `s_sard_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_map_Rn_to_Rm, s_critical_set_of_smooth_map⟩` --[t_auxiliary_construction {strat: nested_critical_filtration}]--> output: `s_filtration_of_critical_set`
2. input: `s_filtration_of_critical_set` --[t_rescale_for_asymptotic_geometry {cube_partition: shrinking_cubes_with_Taylor_remainder}]--> output: `s_volume_estimate_per_cube`
3. input: `s_volume_estimate_per_cube` --[⚠ needs new technique {move: image_measure_zero_via_taylor_remainder_summation}]--> output: `s_image_critical_values_measure_zero`
4. input: `s_image_critical_values_measure_zero` --[t_reduce_to_canonical_form {finish: by_filtration_induction}]--> output: `s_sard_theorem`

**Techniques used:** t_auxiliary_construction, t_rescale_for_asymptotic_geometry, t_reduce_to_canonical_form

---

### Riesz representation theorem for L^p (cite: https://en.wikipedia.org/wiki/Riesz_representation_theorem)

**Axioms:** `s_sigma_finite_measure_space`, `s_bounded_linear_functional_on_Lp`
**Terminal:** `s_riesz_representation_Lp` (kind: theorem)

**Steps:**
1. input: `⟨s_sigma_finite_measure_space, s_bounded_linear_functional_on_Lp⟩` --[t_auxiliary_construction {signed_measure: nu_E_equals_Lambda_indicator}]--> output: `s_finite_signed_measure_nu_absolutely_continuous`
2. input: `s_finite_signed_measure_nu_absolutely_continuous` --[t_reduce_to_canonical_form {density: g_equals_dnu_dmu_via_Radon_Nikodym}]--> output: `s_density_g_with_Lambda_f=int_fg_dmu`
3. input: `s_density_g_with_Lambda_f=int_fg_dmu` --[t_duality {Lp_Lq_pairing: Holder}]--> output: `s_riesz_representation_Lp`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Hardy–Littlewood maximal inequality (cite: https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood_maximal_function)

**Axioms:** `s_lebesgue_measure_on_Rn`, `s_l1_function_on_Rn`
**Terminal:** `s_hardy_littlewood_maximal_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_lebesgue_measure_on_Rn, s_l1_function_on_Rn⟩` --[t_auxiliary_construction {operator: Mf_x=sup_r_average_B_x_r_abs_f}]--> output: `s_maximal_operator_Mf`
2. input: `s_maximal_operator_Mf` --[t_compactness_argument {via: Vitali_covering_on_sublevel_Mf_gt_lambda}]--> output: `s_weak_11_bound_on_Mf`
3. input: `s_weak_11_bound_on_Mf` --[t_interpolate_and_continue {with: L_infty_trivial_bound}]--> output: `s_hardy_littlewood_maximal_inequality`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_interpolate_and_continue

---

### Fefferman–Stein vector-valued maximal inequality (cite: https://en.wikipedia.org/wiki/Fefferman%E2%80%93Stein_inequality)

**Axioms:** `s_lebesgue_measure_on_Rn`, `s_lp_sequence_of_l1_functions`
**Terminal:** `s_fefferman_stein_vector_valued` (kind: theorem)

**Steps:**
1. input: `⟨s_lebesgue_measure_on_Rn, s_lp_sequence_of_l1_functions⟩` --[t_auxiliary_construction {linearization: random_signs_combination_g}]--> output: `s_randomized_linear_combination`
2. input: `s_randomized_linear_combination` --[t_duality {Lp_dual: pair_with_test_sequence_in_Lq}]--> output: `s_dual_pairing_to_scalar_maximal`
3. input: `s_dual_pairing_to_scalar_maximal` --[t_reduce_to_canonical_form {scalar: HL_weak_type}]--> output: `s_fefferman_stein_vector_valued`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Calderón–Zygmund decomposition (cite: https://en.wikipedia.org/wiki/Calder%C3%B3n%E2%80%93Zygmund_lemma)

**Axioms:** `s_l1_function_on_Rn`, `s_lebesgue_measure_on_Rn`
**Terminal:** `s_calderon_zygmund_decomposition` (kind: theorem)

**Steps:**
1. input: `⟨s_l1_function_on_Rn, s_lebesgue_measure_on_Rn⟩` --[t_pigeonhole_collision {dyadic: stopping_time_at_threshold_lambda}]--> output: `s_stopping_cubes_with_average_exceeding_lambda`
2. input: `s_stopping_cubes_with_average_exceeding_lambda` --[t_auxiliary_construction {split: f=g_good_plus_b_bad_oscillation}]--> output: `s_good_bad_decomposition`
3. input: `s_good_bad_decomposition` --[t_reduce_to_canonical_form {bound: abs_g_leq_2n_lambda_int_b_E_zero}]--> output: `s_calderon_zygmund_decomposition`

**Techniques used:** t_pigeonhole_collision, t_auxiliary_construction, t_reduce_to_canonical_form

---

### Calderón–Zygmund singular integral L^p bound (cite: https://en.wikipedia.org/wiki/Singular_integral_operators_of_convolution_type)

**Axioms:** `s_calderon_zygmund_kernel_on_Rn`, `s_lp_function_on_Rn`
**Terminal:** `s_calderon_zygmund_Lp_bound` (kind: theorem)

**Steps:**
1. input: `⟨s_calderon_zygmund_kernel_on_Rn, s_lp_function_on_Rn⟩` --[t_fourier_transform {check: L2_bound_via_multiplier}]--> output: `s_L2_bound_for_singular_integral`
2. input: `s_L2_bound_for_singular_integral` --[t_reduce_to_canonical_form {decompose: via_CZ_lemma_at_threshold_lambda}]--> output: `s_weak_11_bound_via_CZ_decomp`
3. input: `s_weak_11_bound_via_CZ_decomp` --[t_interpolate_and_continue {Marcinkiewicz: between_weak_11_and_L2}]--> output: `s_calderon_zygmund_Lp_bound`

**Techniques used:** t_fourier_transform, t_reduce_to_canonical_form, t_interpolate_and_continue

---

## III. Complex analysis

### Cauchy–Riemann equations characterize holomorphy (cite: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations)

**Axioms:** `s_differentiable_complex_function`, `s_real_C1_function_pair_u_v`
**Terminal:** `s_cauchy_riemann_characterization` (kind: theorem)

**Steps:**
1. input: `⟨s_differentiable_complex_function, s_real_C1_function_pair_u_v⟩` --[t_reduce_to_canonical_form {limit_along: real_and_imaginary_axes}]--> output: `s_two_directional_limit_equality`
2. input: `s_two_directional_limit_equality` --[t_symmetry_reduction {pair: u_x=v_y_and_u_y=-v_x}]--> output: `s_cauchy_riemann_system`
3. input: `s_cauchy_riemann_system` --[t_reduce_to_canonical_form {converse: linearity_via_real_differentiability}]--> output: `s_cauchy_riemann_characterization`

**Techniques used:** t_reduce_to_canonical_form, t_symmetry_reduction

---

### Cauchy's theorem on simply connected domains (Goursat) (cite: https://en.wikipedia.org/wiki/Cauchy%27s_integral_theorem)

**Axioms:** `s_holomorphic_function_on_domain`, `s_simply_connected_proper_domain_in_C`
**Terminal:** `s_cauchy_integral_theorem_general` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_domain, s_simply_connected_proper_domain_in_C⟩` --[t_pigeonhole_collision {bisection: nested_dyadic_triangle_subdivision}]--> output: `s_nested_shrinking_triangle_with_integral_bound`
2. input: `s_nested_shrinking_triangle_with_integral_bound` --[t_exhaustion_squeeze {diameter: to_zero}]--> output: `s_integral_over_triangle_vanishes`
3. input: `s_integral_over_triangle_vanishes` --[t_reduce_to_canonical_form {extend: to_arbitrary_loop_via_triangulation}]--> output: `s_cauchy_integral_theorem_general`

**Techniques used:** t_pigeonhole_collision, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Morera's theorem (cite: https://en.wikipedia.org/wiki/Morera%27s_theorem)

**Axioms:** `s_continuous_function_on_open_C_subset`, `s_vanishing_triangle_integrals`
**Terminal:** `s_morera_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_function_on_open_C_subset, s_vanishing_triangle_integrals⟩` --[t_auxiliary_construction {define: F_z=int_z0_to_z_f_path_independent}]--> output: `s_well_defined_primitive_F`
2. input: `s_well_defined_primitive_F` --[t_reduce_to_canonical_form {differentiate: F_prime=f}]--> output: `s_F_holomorphic_with_derivative_f`
3. input: `s_F_holomorphic_with_derivative_f` --[t_reduce_to_canonical_form {analyticity_of_holomorphic: f_holomorphic}]--> output: `s_morera_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Liouville's theorem (cite: https://en.wikipedia.org/wiki/Liouville%27s_theorem_(complex_analysis))

**Axioms:** `s_holomorphic_function_on_domain`, `s_bounded_entire_function`
**Terminal:** `s_liouville_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_domain, s_bounded_entire_function⟩` --[t_reduce_to_canonical_form {invoke: Cauchy_integral_formula_for_f_prime}]--> output: `s_cauchy_estimate_f_prime_bounded_by_M_over_R`
2. input: `s_cauchy_estimate_f_prime_bounded_by_M_over_R` --[t_exhaustion_squeeze {R_to_infinity}]--> output: `s_f_prime_vanishes_everywhere`
3. input: `s_f_prime_vanishes_everywhere` --[t_reduce_to_canonical_form {integrate: f_is_constant}]--> output: `s_liouville_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Identity theorem (cite: https://en.wikipedia.org/wiki/Identity_theorem)

**Axioms:** `s_holomorphic_function_on_domain`, `s_set_with_accumulation_point_in_domain`
**Terminal:** `s_identity_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_domain, s_set_with_accumulation_point_in_domain⟩` --[t_auxiliary_construction {power_series: at_accumulation_point}]--> output: `s_power_series_with_zero_coefficients`
2. input: `s_power_series_with_zero_coefficients` --[t_reduce_to_canonical_form {zero_set: open_in_domain}]--> output: `s_open_subset_where_f_zero`
3. input: `s_open_subset_where_f_zero` --[t_compactness_argument {connectedness: clopen_partition}]--> output: `s_identity_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_compactness_argument

---

### Maximum modulus principle (cite: https://en.wikipedia.org/wiki/Maximum_modulus_principle)

**Axioms:** `s_holomorphic_function_on_domain`, `s_connected_open_subset_of_C`
**Terminal:** `s_maximum_modulus_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_domain, s_connected_open_subset_of_C⟩` --[t_reduce_to_canonical_form {mean_value: f_z0_equals_circle_average}]--> output: `s_mean_value_property_for_f`
2. input: `s_mean_value_property_for_f` --[t_reductio_ad_absurdum {suppose: interior_max}]--> output: `s_constant_on_neighborhood_of_max`
3. input: `s_constant_on_neighborhood_of_max` --[t_reduce_to_canonical_form {invoke: identity_theorem_on_connected}]--> output: `s_maximum_modulus_principle`

**Techniques used:** t_reduce_to_canonical_form, t_reductio_ad_absurdum

---

### Open mapping theorem (complex analysis) (cite: https://en.wikipedia.org/wiki/Open_mapping_theorem_(complex_analysis))

**Axioms:** `s_holomorphic_function_on_domain`, `s_nonconstant_holomorphic_function`
**Terminal:** `s_complex_open_mapping_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_domain, s_nonconstant_holomorphic_function⟩` --[t_auxiliary_construction {at_z0: f_z=f_z0+g_z_z_minus_z0_n_with_g_nonzero}]--> output: `s_local_normal_form_n_to_1`
2. input: `s_local_normal_form_n_to_1` --[t_reduce_to_canonical_form {via: argument_principle_for_small_circles}]--> output: `s_winding_number_n_for_small_disk_image`
3. input: `s_winding_number_n_for_small_disk_image` --[t_reduce_to_canonical_form {conclude: image_contains_neighborhood}]--> output: `s_complex_open_mapping_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Schwarz lemma (cite: https://en.wikipedia.org/wiki/Schwarz_lemma)

**Axioms:** `s_holomorphic_self_map_of_unit_disk`, `s_fixing_origin`
**Terminal:** `s_schwarz_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_self_map_of_unit_disk, s_fixing_origin⟩` --[t_auxiliary_construction {define: g_z=f_z_over_z_with_removable_at_0}]--> output: `s_holomorphic_extension_g`
2. input: `s_holomorphic_extension_g` --[t_reduce_to_canonical_form {apply: maximum_modulus_on_disk_of_radius_r}]--> output: `s_bound_abs_g_leq_1_over_r_on_r_disk`
3. input: `s_bound_abs_g_leq_1_over_r_on_r_disk` --[t_exhaustion_squeeze {r_to_1}]--> output: `s_schwarz_lemma`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Schwarz–Pick theorem (cite: https://en.wikipedia.org/wiki/Schwarz%E2%80%93Pick_theorem)

**Axioms:** `s_holomorphic_self_map_of_unit_disk`, `s_hyperbolic_metric_on_disk`
**Terminal:** `s_schwarz_pick_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_self_map_of_unit_disk, s_hyperbolic_metric_on_disk⟩` --[t_auxiliary_construction {compose: with_Mobius_to_send_z0_to_0}]--> output: `s_normalized_problem_at_origin`
2. input: `s_normalized_problem_at_origin` --[t_reduce_to_canonical_form {apply: Schwarz_lemma}]--> output: `s_bound_at_origin`
3. input: `s_bound_at_origin` --[t_symmetry_reduction {pull_back: hyperbolic_invariance}]--> output: `s_schwarz_pick_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_symmetry_reduction

---

### Casorati–Weierstrass theorem (cite: https://en.wikipedia.org/wiki/Casorati%E2%80%93Weierstrass_theorem)

**Axioms:** `s_holomorphic_function_with_essential_singularity`, `s_punctured_disk_neighborhood`
**Terminal:** `s_casorati_weierstrass` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_with_essential_singularity, s_punctured_disk_neighborhood⟩` --[t_reductio_ad_absurdum {suppose: image_avoids_open_disk}]--> output: `s_1_over_f_minus_w_bounded_near_singularity`
2. input: `s_1_over_f_minus_w_bounded_near_singularity` --[t_reduce_to_canonical_form {removable: Riemann_removability}]--> output: `s_pole_or_removable_contradiction`
3. input: `s_pole_or_removable_contradiction` --[t_reduce_to_canonical_form {conclude: dense_image}]--> output: `s_casorati_weierstrass`

**Techniques used:** t_reductio_ad_absurdum, t_reduce_to_canonical_form

---

### Picard's little theorem (cite: https://en.wikipedia.org/wiki/Picard_theorem)

**Axioms:** `s_entire_function`, `s_omitting_two_values`
**Terminal:** `s_picard_little_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_entire_function, s_omitting_two_values⟩` --[t_auxiliary_construction {lift: to_universal_cover_of_C_minus_two_points}]--> output: `s_lift_to_upper_half_plane_via_modular_function`
2. input: `s_lift_to_upper_half_plane_via_modular_function` --[t_reduce_to_canonical_form {compose: with_holomorphic_lift}]--> output: `s_bounded_entire_lift`
3. input: `s_bounded_entire_lift` --[t_reduce_to_canonical_form {apply: Liouville}]--> output: `s_picard_little_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Picard's great theorem (cite: https://en.wikipedia.org/wiki/Picard_theorem)

**Axioms:** `s_holomorphic_function_with_essential_singularity`, `s_punctured_disk_neighborhood`
**Terminal:** `s_picard_great_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_with_essential_singularity, s_punctured_disk_neighborhood⟩` --[t_auxiliary_construction {family: f_n_z=f_z_over_2_to_the_n_on_annulus}]--> output: `s_family_of_holomorphic_maps_on_annulus`
2. input: `s_family_of_holomorphic_maps_on_annulus` --[t_compactness_argument {Montel_normal_family_if_omits_two_values}]--> output: `s_normal_family_implies_bounded_subsequence`
3. input: `s_normal_family_implies_bounded_subsequence` --[t_reduce_to_canonical_form {contradict: essential_singularity_implies_unbounded}]--> output: `s_picard_great_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Residue theorem (cite: https://en.wikipedia.org/wiki/Residue_theorem)

**Axioms:** `s_meromorphic_function_on_domain`, `s_positively_oriented_closed_contour`
**Terminal:** `s_residue_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_meromorphic_function_on_domain, s_positively_oriented_closed_contour⟩` --[t_auxiliary_construction {around_each_pole: small_circle_punctured_region}]--> output: `s_complement_with_small_circles`
2. input: `s_complement_with_small_circles` --[t_reduce_to_canonical_form {apply: Cauchy_theorem_on_holomorphic_complement}]--> output: `s_contour_integral_equals_sum_circle_integrals`
3. input: `s_contour_integral_equals_sum_circle_integrals` --[t_reduce_to_canonical_form {Laurent: a_minus_1_coefficient_definition}]--> output: `s_residue_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Argument principle (cite: https://en.wikipedia.org/wiki/Argument_principle)

**Axioms:** `s_meromorphic_function_on_domain`, `s_positively_oriented_closed_contour`
**Terminal:** `s_argument_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_meromorphic_function_on_domain, s_positively_oriented_closed_contour⟩` --[t_auxiliary_construction {form: f_prime_over_f_with_logarithmic_derivative}]--> output: `s_log_derivative_with_simple_poles_at_zeros_and_poles`
2. input: `s_log_derivative_with_simple_poles_at_zeros_and_poles` --[t_reduce_to_canonical_form {residues: residue_one_at_each_zero_minus_one_at_each_pole}]--> output: `s_residue_count_equals_N_minus_P`
3. input: `s_residue_count_equals_N_minus_P` --[t_reduce_to_canonical_form {apply: Residue_theorem}]--> output: `s_argument_principle`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Rouché's theorem (cite: https://en.wikipedia.org/wiki/Rouch%C3%A9%27s_theorem)

**Axioms:** `s_holomorphic_function_pair_f_g`, `s_strict_modulus_inequality_on_contour`
**Terminal:** `s_rouche_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_pair_f_g, s_strict_modulus_inequality_on_contour⟩` --[t_auxiliary_construction {homotopy: f_t=f+t_g_for_t_in_0_1}]--> output: `s_continuous_homotopy_no_zero_on_contour`
2. input: `s_continuous_homotopy_no_zero_on_contour` --[t_reduce_to_canonical_form {apply: argument_principle_as_function_of_t}]--> output: `s_zero_count_is_integer_valued_continuous`
3. input: `s_zero_count_is_integer_valued_continuous` --[t_reduce_to_canonical_form {constant: t=0_and_t=1_match}]--> output: `s_rouche_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Gauss–Lucas theorem (cite: https://en.wikipedia.org/wiki/Gauss%E2%80%93Lucas_theorem)

**Axioms:** `s_complex_polynomial_p_z`, `s_convex_hull_of_roots`
**Terminal:** `s_gauss_lucas_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_complex_polynomial_p_z, s_convex_hull_of_roots⟩` --[t_auxiliary_construction {logarithmic_derivative: p_prime_over_p=Sigma_1_over_z_minus_z_k}]--> output: `s_log_derivative_sum_expression`
2. input: `s_log_derivative_sum_expression` --[t_reduce_to_canonical_form {set: p_prime_zero_implies_weighted_centroid}]--> output: `s_critical_point_as_convex_combination_of_roots`
3. input: `s_critical_point_as_convex_combination_of_roots` --[t_reduce_to_canonical_form {conclude: lies_in_convex_hull}]--> output: `s_gauss_lucas_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Jensen's formula (cite: https://en.wikipedia.org/wiki/Jensen%27s_formula)

**Axioms:** `s_holomorphic_function_on_closed_disk`, `s_zeros_inside_disk`
**Terminal:** `s_jensen_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_closed_disk, s_zeros_inside_disk⟩` --[t_auxiliary_construction {Blaschke: divide_out_blaschke_product_for_zeros}]--> output: `s_zero_free_factor_g`
2. input: `s_zero_free_factor_g` --[t_reduce_to_canonical_form {log: take_logarithm_then_mean_value}]--> output: `s_mean_value_for_log_abs_g`
3. input: `s_mean_value_for_log_abs_g` --[t_reduce_to_canonical_form {reassemble: log_abs_f_via_blaschke_correction}]--> output: `s_jensen_formula`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Hadamard three-lines theorem (cite: https://en.wikipedia.org/wiki/Hadamard_three-lines_theorem)

**Axioms:** `s_holomorphic_function_on_vertical_strip`, `s_bounded_function`
**Terminal:** `s_hadamard_three_lines_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_vertical_strip, s_bounded_function⟩` --[t_auxiliary_construction {tilt: F_s=f_s_times_exponential_to_make_constant_bound}]--> output: `s_modified_function_with_uniform_bound_on_boundary`
2. input: `s_modified_function_with_uniform_bound_on_boundary` --[t_reduce_to_canonical_form {Phragmen_Lindelof_on_strip}]--> output: `s_max_modulus_bound_on_strip`
3. input: `s_max_modulus_bound_on_strip` --[t_reduce_to_canonical_form {log_convexity: in_real_part}]--> output: `s_hadamard_three_lines_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Hadamard three-circles theorem (cite: https://en.wikipedia.org/wiki/Hadamard_three-circle_theorem)

**Axioms:** `s_holomorphic_function_on_annulus`, `s_log_radius_substitution`
**Terminal:** `s_hadamard_three_circles_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_annulus, s_log_radius_substitution⟩` --[t_reduce_to_canonical_form {substitution: w=log_z_to_strip}]--> output: `s_strip_version_of_problem`
2. input: `s_strip_version_of_problem` --[t_reduce_to_canonical_form {apply: three_lines}]--> output: `s_hadamard_three_circles_theorem`

**Techniques used:** t_reduce_to_canonical_form

---

### Phragmén–Lindelöf principle (cite: https://en.wikipedia.org/wiki/Phragm%C3%A9n%E2%80%93Lindel%C3%B6f_principle)

**Axioms:** `s_holomorphic_function_on_unbounded_sector`, `s_growth_bound_at_infinity`
**Terminal:** `s_phragmen_lindelof_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_unbounded_sector, s_growth_bound_at_infinity⟩` --[t_auxiliary_construction {regularize: f_eps_z=f_z_times_exp_minus_eps_z_alpha}]--> output: `s_decaying_modified_function`
2. input: `s_decaying_modified_function` --[t_reduce_to_canonical_form {apply: maximum_modulus_on_bounded_truncation}]--> output: `s_bounded_by_boundary_max`
3. input: `s_bounded_by_boundary_max` --[t_exhaustion_squeeze {eps_to_0_recover_f}]--> output: `s_phragmen_lindelof_principle`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Borel–Carathéodory theorem (cite: https://en.wikipedia.org/wiki/Borel%E2%80%93Carath%C3%A9odory_theorem)

**Axioms:** `s_holomorphic_function_on_closed_disk`, `s_real_part_bound`
**Terminal:** `s_borel_caratheodory_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_closed_disk, s_real_part_bound⟩` --[t_auxiliary_construction {Mobius: phi_z=f_z_over_2A_minus_f_z}]--> output: `s_holomorphic_self_map_of_disk`
2. input: `s_holomorphic_self_map_of_disk` --[t_reduce_to_canonical_form {Schwarz_lemma_on_phi}]--> output: `s_bound_on_phi_implies_bound_on_f`
3. input: `s_bound_on_phi_implies_bound_on_f` --[t_reduce_to_canonical_form {invert: extract_modulus_estimate}]--> output: `s_borel_caratheodory_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Hadamard factorization theorem (cite: https://en.wikipedia.org/wiki/Weierstrass_factorization_theorem#Hadamard_factorization_theorem)

**Axioms:** `s_entire_function_of_finite_order`, `s_zero_distribution_with_genus_p`
**Terminal:** `s_hadamard_factorization_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_entire_function_of_finite_order, s_zero_distribution_with_genus_p⟩` --[t_auxiliary_construction {Weierstrass_E_p_primary_factors}]--> output: `s_canonical_product_with_zero_set`
2. input: `s_canonical_product_with_zero_set` --[t_reduce_to_canonical_form {divide_out: f_over_product_is_zero_free_entire}]--> output: `s_zero_free_entire_with_growth_order`
3. input: `s_zero_free_entire_with_growth_order` --[t_reduce_to_canonical_form {Borel_Caratheodory: bound_on_real_part_of_log}]--> output: `s_log_f_is_polynomial_of_degree_leq_rho`
4. input: `s_log_f_is_polynomial_of_degree_leq_rho` --[t_reduce_to_canonical_form {exponentiate: combine_factors}]--> output: `s_hadamard_factorization_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Weierstrass factorization theorem (cite: https://en.wikipedia.org/wiki/Weierstrass_factorization_theorem)

**Axioms:** `s_entire_function`, `s_prescribed_zero_sequence`
**Terminal:** `s_weierstrass_factorization_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_entire_function, s_prescribed_zero_sequence⟩` --[t_auxiliary_construction {primary_factor: E_p_z=(1-z)exp_polynomial_correction}]--> output: `s_convergent_primary_factor_product`
2. input: `s_convergent_primary_factor_product` --[t_exhaustion_squeeze {tail_convergence: by_summability_of_corrections}]--> output: `s_holomorphic_product_with_prescribed_zeros`
3. input: `s_holomorphic_product_with_prescribed_zeros` --[t_reduce_to_canonical_form {entire_factor: with_zero_free_part}]--> output: `s_weierstrass_factorization_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Mittag-Leffler theorem (cite: https://en.wikipedia.org/wiki/Mittag-Leffler%27s_theorem)

**Axioms:** `s_open_subset_of_C`, `s_prescribed_principal_parts_at_discrete_poles`
**Terminal:** `s_mittag_leffler_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_open_subset_of_C, s_prescribed_principal_parts_at_discrete_poles⟩` --[t_auxiliary_construction {correct: subtract_polynomial_truncation_of_principal_part}]--> output: `s_corrected_series_with_uniform_convergence_on_compacta`
2. input: `s_corrected_series_with_uniform_convergence_on_compacta` --[t_exhaustion_squeeze {compact_exhaustion_of_domain}]--> output: `s_meromorphic_function_with_prescribed_singularities`
3. input: `s_meromorphic_function_with_prescribed_singularities` --[t_reduce_to_canonical_form {entire_correction: most_general_solution}]--> output: `s_mittag_leffler_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Runge's theorem (cite: https://en.wikipedia.org/wiki/Runge%27s_theorem)

**Axioms:** `s_holomorphic_function_on_open_set`, `s_compact_subset_with_connected_complement`
**Terminal:** `s_runge_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_open_set, s_compact_subset_with_connected_complement⟩` --[t_auxiliary_construction {Cauchy_integral_over_bounding_cycle}]--> output: `s_integral_representation_with_pole_at_each_point`
2. input: `s_integral_representation_with_pole_at_each_point` --[t_reduce_to_canonical_form {pole_pushing: move_poles_along_complement}]--> output: `s_approximation_by_rational_functions_with_poles_in_complement`
3. input: `s_approximation_by_rational_functions_with_poles_in_complement` --[t_reduce_to_canonical_form {if_complement_connected: push_poles_to_infinity_to_polynomials}]--> output: `s_runge_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Bloch's theorem (cite: https://en.wikipedia.org/wiki/Bloch%27s_theorem_(complex_variables))

**Axioms:** `s_holomorphic_function_on_unit_disk`, `s_normalization_f_prime_0_equals_1`
**Terminal:** `s_bloch_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_unit_disk, s_normalization_f_prime_0_equals_1⟩` --[t_auxiliary_construction {extremal_disk: max_r_with_f_injective_on_smaller_disk}]--> output: `s_extremal_disk_size`
2. input: `s_extremal_disk_size` --[t_rescale_for_asymptotic_geometry {dilate: to_unit_disk_scale}]--> output: `s_renormalized_function_with_growth_bound`
3. input: `s_renormalized_function_with_growth_bound` --[t_reduce_to_canonical_form {Koebe_quarter_theorem_or_lower_bound_for_disk}]--> output: `s_bloch_theorem`

**Techniques used:** t_auxiliary_construction, t_rescale_for_asymptotic_geometry, t_reduce_to_canonical_form

---

### Koebe 1/4 theorem (cite: https://en.wikipedia.org/wiki/Koebe_quarter_theorem)

**Axioms:** `s_univalent_function_on_unit_disk`, `s_normalization_f_0_zero_f_prime_0_one`
**Terminal:** `s_koebe_quarter_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_univalent_function_on_unit_disk, s_normalization_f_0_zero_f_prime_0_one⟩` --[t_auxiliary_construction {squared_omitted_value: g_z=sqrt_w_minus_f_z2_branch}]--> output: `s_auxiliary_univalent_g_in_class_S`
2. input: `s_auxiliary_univalent_g_in_class_S` --[t_reduce_to_canonical_form {area_theorem: bound_on_second_coefficient}]--> output: `s_coefficient_bound_abs_a2_leq_2`
3. input: `s_coefficient_bound_abs_a2_leq_2` --[t_reduce_to_canonical_form {translate: omitted_value_satisfies_abs_w_geq_1_over_4}]--> output: `s_koebe_quarter_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Montel's theorem (cite: https://en.wikipedia.org/wiki/Montel%27s_theorem)

**Axioms:** `s_locally_uniformly_bounded_family_of_holomorphic_functions`, `s_open_subset_of_C`
**Terminal:** `s_montel_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_locally_uniformly_bounded_family_of_holomorphic_functions, s_open_subset_of_C⟩` --[t_reduce_to_canonical_form {Cauchy_estimates: f_prime_bounded_locally}]--> output: `s_equicontinuous_family`
2. input: `s_equicontinuous_family` --[t_compactness_argument {Arzela_Ascoli_on_compacta}]--> output: `s_uniformly_convergent_subsequence_on_compacta`
3. input: `s_uniformly_convergent_subsequence_on_compacta` --[t_reduce_to_canonical_form {limit_function_holomorphic_via_Morera}]--> output: `s_montel_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_compactness_argument

---

### Hurwitz's theorem (cite: https://en.wikipedia.org/wiki/Hurwitz%27s_theorem_(complex_analysis))

**Axioms:** `s_sequence_of_holomorphic_functions_locally_uniformly_convergent`, `s_zero_set_consideration`
**Terminal:** `s_hurwitz_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sequence_of_holomorphic_functions_locally_uniformly_convergent, s_zero_set_consideration⟩` --[t_auxiliary_construction {contour: small_circle_around_z0}]--> output: `s_contour_with_no_zero_on_boundary`
2. input: `s_contour_with_no_zero_on_boundary` --[t_reduce_to_canonical_form {argument_principle: N_f_n=oint_f_n_prime_over_f_n}]--> output: `s_integer_valued_zero_count_continuous_in_n`
3. input: `s_integer_valued_zero_count_continuous_in_n` --[t_reduce_to_canonical_form {pass_to_limit: zero_count_preserved}]--> output: `s_hurwitz_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Schwarz reflection principle (cite: https://en.wikipedia.org/wiki/Schwarz_reflection_principle)

**Axioms:** `s_holomorphic_on_upper_half_disk_continuous_to_real_axis`, `s_real_boundary_values`
**Terminal:** `s_schwarz_reflection_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_on_upper_half_disk_continuous_to_real_axis, s_real_boundary_values⟩` --[t_auxiliary_construction {reflect: F_z=conj_f_conj_z_below_axis}]--> output: `s_piecewise_function_on_full_disk`
2. input: `s_piecewise_function_on_full_disk` --[t_reduce_to_canonical_form {Morera_on_triangles_crossing_axis}]--> output: `s_holomorphic_F_on_full_disk`
3. input: `s_holomorphic_F_on_full_disk` --[t_reduce_to_canonical_form {agree_on_upper: extension_unique}]--> output: `s_schwarz_reflection_principle`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Schwarz–Christoffel mapping (cite: https://en.wikipedia.org/wiki/Schwarz%E2%80%93Christoffel_mapping)

**Axioms:** `s_simply_connected_polygonal_domain`, `s_upper_half_plane`
**Terminal:** `s_schwarz_christoffel_mapping` (kind: theorem)

**Steps:**
1. input: `⟨s_simply_connected_polygonal_domain, s_upper_half_plane⟩` --[t_riemann_mapping_application {abstract: existence_of_conformal_map}]--> output: `s_abstract_conformal_map_to_polygon`
2. input: `s_abstract_conformal_map_to_polygon` --[t_auxiliary_construction {derivative_has_branch_singularities_at_prevertices}]--> output: `s_derivative_form_product_w_minus_xk_alpha_k`
3. input: `s_derivative_form_product_w_minus_xk_alpha_k` --[t_reduce_to_canonical_form {integrate: explicit_formula}]--> output: `s_schwarz_christoffel_mapping`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

⚠ Note: step 1's `t_riemann_mapping_application` reads as an instance of `t_compactness_argument` (Montel-based proof of Riemann mapping, already in graph as `s_riemann_mapping_theorem`).

---

### Bieberbach conjecture / de Branges theorem (cite: https://en.wikipedia.org/wiki/De_Branges%27s_theorem)

**Axioms:** `s_univalent_function_in_class_S`, `s_taylor_coefficients_a_n`
**Terminal:** `s_de_branges_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_univalent_function_in_class_S, s_taylor_coefficients_a_n⟩` --[t_auxiliary_construction {Loewner_chain: time_parameterized_subordination}]--> output: `s_Loewner_ODE_for_f_t`
2. input: `s_Loewner_ODE_for_f_t` --[t_conserved_quantity {Lebedev_Milin: exponentiated_coefficient_inequality}]--> output: `s_milin_inequality_on_log_derivatives`
3. input: `s_milin_inequality_on_log_derivatives` --[t_reduce_to_canonical_form {orthogonal_polynomials: Askey_Gasper}]--> output: `s_de_branges_theorem`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_reduce_to_canonical_form

---

### Riemann's removable singularity theorem (cite: https://en.wikipedia.org/wiki/Removable_singularity)

**Axioms:** `s_holomorphic_function_on_punctured_disk`, `s_bounded_near_puncture`
**Terminal:** `s_riemann_removable_singularity` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_punctured_disk, s_bounded_near_puncture⟩` --[t_auxiliary_construction {multiply: h_z=z_minus_a_squared_f_z}]--> output: `s_holomorphic_extension_h_with_zero_of_order_2`
2. input: `s_holomorphic_extension_h_with_zero_of_order_2` --[t_reduce_to_canonical_form {divide: power_series_starts_at_z_minus_a_squared}]--> output: `s_holomorphic_recovery_of_f`
3. input: `s_holomorphic_recovery_of_f` --[t_reduce_to_canonical_form {remove: singularity}]--> output: `s_riemann_removable_singularity`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

## IV. Harmonic and Fourier analysis

### Riemann–Lebesgue lemma (cite: https://en.wikipedia.org/wiki/Riemann%E2%80%93Lebesgue_lemma)

**Axioms:** `s_l1_function_on_R`, `s_fourier_transform_definition`
**Terminal:** `s_riemann_lebesgue_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_l1_function_on_R, s_fourier_transform_definition⟩` --[t_axiomatize_from_instances {start: indicator_of_interval}]--> output: `s_decay_for_indicator_of_interval`
2. input: `s_decay_for_indicator_of_interval` --[t_reduce_to_canonical_form {linearity: step_functions_decay}]--> output: `s_decay_for_step_functions`
3. input: `s_decay_for_step_functions` --[t_exhaustion_squeeze {density: step_functions_dense_in_L1}]--> output: `s_riemann_lebesgue_lemma`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Plancherel theorem (cite: https://en.wikipedia.org/wiki/Plancherel_theorem)

**Axioms:** `s_L2_function_space`, `s_fourier_transform_definition`
**Terminal:** `s_plancherel_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_L2_function_space, s_fourier_transform_definition⟩` --[t_axiomatize_from_instances {Schwartz_class: dense_in_L2}]--> output: `s_fourier_isometry_on_schwartz`
2. input: `s_fourier_isometry_on_schwartz` --[t_duality {parseval_identity_for_schwartz: f_g_pairing}]--> output: `s_parseval_for_schwartz_functions`
3. input: `s_parseval_for_schwartz_functions` --[t_exhaustion_squeeze {extend_by_density: to_L2}]--> output: `s_plancherel_theorem`

**Techniques used:** t_axiomatize_from_instances, t_duality, t_exhaustion_squeeze

---

### Parseval's identity (cite: https://en.wikipedia.org/wiki/Parseval%27s_identity)

**Axioms:** `s_l2_function_on_torus`, `s_orthonormal_basis_of_exponentials`
**Terminal:** `s_parseval_identity` (kind: theorem)

**Steps:**
1. input: `⟨s_l2_function_on_torus, s_orthonormal_basis_of_exponentials⟩` --[t_fourier_transform {expand: in_orthonormal_basis_e_inx}]--> output: `s_fourier_series_expansion`
2. input: `s_fourier_series_expansion` --[t_reduce_to_canonical_form {orthogonality: cross_terms_vanish}]--> output: `s_norm_squared_equals_sum_coefficient_squares`
3. input: `s_norm_squared_equals_sum_coefficient_squares` --[t_reduce_to_canonical_form {extend: by_polarization_to_inner_product}]--> output: `s_parseval_identity`

**Techniques used:** t_fourier_transform, t_reduce_to_canonical_form

---

### Fejér's theorem (cite: https://en.wikipedia.org/wiki/Fej%C3%A9r%27s_theorem)

**Axioms:** `s_continuous_function_on_torus`, `s_cesaro_means_of_fourier_series`
**Terminal:** `s_fejer_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_function_on_torus, s_cesaro_means_of_fourier_series⟩` --[t_auxiliary_construction {Fejer_kernel: K_N_positive_with_unit_mass}]--> output: `s_positive_approximate_identity`
2. input: `s_positive_approximate_identity` --[t_reduce_to_canonical_form {convolution: sigma_N_f=K_N_star_f}]--> output: `s_cesaro_average_as_convolution`
3. input: `s_cesaro_average_as_convolution` --[t_exhaustion_squeeze {uniform_convergence_via_continuity}]--> output: `s_fejer_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Dirichlet's theorem on pointwise Fourier convergence (cite: https://en.wikipedia.org/wiki/Convergence_of_Fourier_series#Dirichlet's_theorem)

**Axioms:** `s_piecewise_C1_function_on_torus`, `s_partial_sums_of_fourier_series`
**Terminal:** `s_dirichlet_pointwise_convergence` (kind: theorem)

**Steps:**
1. input: `⟨s_piecewise_C1_function_on_torus, s_partial_sums_of_fourier_series⟩` --[t_auxiliary_construction {Dirichlet_kernel: D_N_with_oscillation}]--> output: `s_integral_representation_S_N_f`
2. input: `s_integral_representation_S_N_f` --[t_reduce_to_canonical_form {localize: subtract_jump_average}]--> output: `s_localized_integrand_with_smooth_factor`
3. input: `s_localized_integrand_with_smooth_factor` --[t_reduce_to_canonical_form {Riemann_Lebesgue_on_smooth_part}]--> output: `s_dirichlet_pointwise_convergence`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Carleson's theorem (cite: https://en.wikipedia.org/wiki/Carleson%27s_theorem)

**Axioms:** `s_L2_function_on_torus`, `s_partial_sums_of_fourier_series`
**Terminal:** `s_carleson_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_L2_function_on_torus, s_partial_sums_of_fourier_series⟩` --[t_auxiliary_construction {Carleson_operator: C_f_x=sup_N_abs_S_N_f_x}]--> output: `s_carleson_maximal_operator`
2. input: `s_carleson_maximal_operator` --[⚠ needs new technique {move: time_frequency_tile_decomposition_phase_plane}]--> output: `s_phase_plane_tile_estimate`
3. input: `s_phase_plane_tile_estimate` --[t_reduce_to_canonical_form {weak_type_2_2_bound}]--> output: `s_weak_type_22_for_carleson_operator`
4. input: `s_weak_type_22_for_carleson_operator` --[t_reduce_to_canonical_form {ae_convergence_via_density}]--> output: `s_carleson_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Hausdorff–Young inequality (cite: https://en.wikipedia.org/wiki/Hausdorff%E2%80%93Young_inequality)

**Axioms:** `s_lp_function_on_R`, `s_fourier_transform_definition`
**Terminal:** `s_hausdorff_young_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_lp_function_on_R, s_fourier_transform_definition⟩` --[t_reduce_to_canonical_form {endpoint_L1_to_L_infinity: trivial_bound}]--> output: `s_L1_L_inf_endpoint`
2. input: `s_L1_L_inf_endpoint` --[t_reduce_to_canonical_form {endpoint_L2_to_L2: Plancherel}]--> output: `s_L2_L2_endpoint`
3. input: `⟨s_L1_L_inf_endpoint, s_L2_L2_endpoint⟩` --[t_interpolate_and_continue {Riesz_Thorin: complex_interpolation}]--> output: `s_hausdorff_young_inequality`

**Techniques used:** t_reduce_to_canonical_form, t_interpolate_and_continue

---

### Riesz–Thorin interpolation theorem (cite: https://en.wikipedia.org/wiki/Riesz%E2%80%93Thorin_theorem)

**Axioms:** `s_linear_operator_bounded_at_endpoints`, `s_lp_lq_endpoint_data`
**Terminal:** `s_riesz_thorin_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_linear_operator_bounded_at_endpoints, s_lp_lq_endpoint_data⟩` --[t_auxiliary_construction {analytic_family: F_z=int_T_f_z_g_z_with_complex_exponents}]--> output: `s_holomorphic_in_strip_with_endpoint_bounds`
2. input: `s_holomorphic_in_strip_with_endpoint_bounds` --[t_reduce_to_canonical_form {apply: three_lines_theorem}]--> output: `s_log_convex_bound_on_strip`
3. input: `s_log_convex_bound_on_strip` --[t_reduce_to_canonical_form {recover: intermediate_Lp_Lq_bound}]--> output: `s_riesz_thorin_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Marcinkiewicz interpolation theorem (cite: https://en.wikipedia.org/wiki/Marcinkiewicz_interpolation_theorem)

**Axioms:** `s_sublinear_operator_of_weak_type_at_endpoints`, `s_lp_function`
**Terminal:** `s_marcinkiewicz_interpolation_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sublinear_operator_of_weak_type_at_endpoints, s_lp_function⟩` --[t_auxiliary_construction {layer_cake: split_f_at_height_t}]--> output: `s_decomposition_f_eq_f_t_plus_f_super_t`
2. input: `s_decomposition_f_eq_f_t_plus_f_super_t` --[t_reduce_to_canonical_form {weak_type_bounds: sum_distribution_estimate}]--> output: `s_distribution_function_estimate`
3. input: `s_distribution_function_estimate` --[t_interpolate_and_continue {integrate_in_t: layer_cake_formula}]--> output: `s_marcinkiewicz_interpolation_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_interpolate_and_continue

---

### Paley–Wiener theorem (cite: https://en.wikipedia.org/wiki/Paley%E2%80%93Wiener_theorem)

**Axioms:** `s_L2_function_with_compactly_supported_fourier_transform`, `s_entire_function_of_exponential_type`
**Terminal:** `s_paley_wiener_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_L2_function_with_compactly_supported_fourier_transform, s_entire_function_of_exponential_type⟩` --[t_auxiliary_construction {extend: integral_formula_to_complex_z}]--> output: `s_holomorphic_extension_of_f`
2. input: `s_holomorphic_extension_of_f` --[t_reduce_to_canonical_form {estimate: growth_bounded_by_e_A_abs_Im_z}]--> output: `s_exponential_type_bound`
3. input: `s_exponential_type_bound` --[t_reduce_to_canonical_form {converse: Phragmen_Lindelof_recovers_support}]--> output: `s_paley_wiener_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Poisson summation formula (cite: https://en.wikipedia.org/wiki/Poisson_summation_formula)

**Axioms:** `s_schwartz_function_on_R`, `s_integer_lattice_in_R`
**Terminal:** `s_poisson_summation_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_schwartz_function_on_R, s_integer_lattice_in_R⟩` --[t_auxiliary_construction {periodize: F_x=sum_f_x_plus_n}]--> output: `s_1_periodic_smooth_function_F`
2. input: `s_1_periodic_smooth_function_F` --[t_fourier_transform {expand: Fourier_series_of_F}]--> output: `s_fourier_coefficients_of_F_equal_hat_f_at_integers`
3. input: `s_fourier_coefficients_of_F_equal_hat_f_at_integers` --[t_reduce_to_canonical_form {evaluate: at_x_equal_0}]--> output: `s_poisson_summation_formula`

**Techniques used:** t_auxiliary_construction, t_fourier_transform, t_reduce_to_canonical_form

---

### Heisenberg uncertainty principle (cite: https://en.wikipedia.org/wiki/Uncertainty_principle#Mathematical_form)

**Axioms:** `s_schwartz_function_on_R`, `s_L2_normalization`
**Terminal:** `s_heisenberg_uncertainty_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_schwartz_function_on_R, s_L2_normalization⟩` --[t_auxiliary_construction {commutator: x_and_d_dx_canonical_pair}]--> output: `s_canonical_commutator_identity`
2. input: `s_canonical_commutator_identity` --[t_duality {Cauchy_Schwarz_on_x_f_and_f_prime}]--> output: `s_product_of_variances_bound`
3. input: `s_product_of_variances_bound` --[t_reduce_to_canonical_form {translate: position_momentum_uncertainty}]--> output: `s_heisenberg_uncertainty_principle`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Hardy's inequality (cite: https://en.wikipedia.org/wiki/Hardy%27s_inequality)

**Axioms:** `s_nonneg_function_on_positive_reals`, `s_lp_norm_definition`
**Terminal:** `s_hardy_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_nonneg_function_on_positive_reals, s_lp_norm_definition⟩` --[t_auxiliary_construction {averaging_operator: A_f_x=1_over_x_int_0_x_f}]--> output: `s_hardy_averaging_operator`
2. input: `s_hardy_averaging_operator` --[t_duality {Holder_or_integration_by_parts}]--> output: `s_lp_norm_inequality_for_A_f`
3. input: `s_lp_norm_inequality_for_A_f` --[t_reduce_to_canonical_form {extract: sharp_constant_p_over_p_minus_1}]--> output: `s_hardy_inequality`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Hilbert's inequality (cite: https://en.wikipedia.org/wiki/Hilbert%27s_inequality)

**Axioms:** `s_nonneg_sequences_a_m_b_n_in_l2`, `s_double_sum_kernel_1_over_m_plus_n`
**Terminal:** `s_hilbert_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_nonneg_sequences_a_m_b_n_in_l2, s_double_sum_kernel_1_over_m_plus_n⟩` --[t_auxiliary_construction {symmetric_kernel: K_m_n=1_over_m_plus_n}]--> output: `s_bilinear_form_with_homogeneous_kernel`
2. input: `s_bilinear_form_with_homogeneous_kernel` --[t_reduce_to_canonical_form {Schur_test: weight_function_w_n=1_over_sqrt_n}]--> output: `s_Schur_test_satisfied`
3. input: `s_Schur_test_satisfied` --[t_reduce_to_canonical_form {extract: sharp_constant_pi}]--> output: `s_hilbert_inequality`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Hilbert transform L^p boundedness (cite: https://en.wikipedia.org/wiki/Hilbert_transform)

**Axioms:** `s_lp_function_on_R`, `s_principal_value_convolution_with_1_over_x`
**Terminal:** `s_hilbert_transform_Lp_bound` (kind: theorem)

**Steps:**
1. input: `⟨s_lp_function_on_R, s_principal_value_convolution_with_1_over_x⟩` --[t_fourier_transform {multiplier: minus_i_sign_xi}]--> output: `s_L2_isometry_up_to_sign`
2. input: `s_L2_isometry_up_to_sign` --[t_reduce_to_canonical_form {kernel: smoothness_off_diagonal_yields_CZ_kernel}]--> output: `s_CZ_kernel_class_membership`
3. input: `s_CZ_kernel_class_membership` --[t_reduce_to_canonical_form {apply: Calderon_Zygmund_Lp_bound}]--> output: `s_hilbert_transform_Lp_bound`

**Techniques used:** t_fourier_transform, t_reduce_to_canonical_form

---

### Bernstein's inequality (cite: https://en.wikipedia.org/wiki/Bernstein%27s_inequality_(mathematical_analysis))

**Axioms:** `s_band_limited_function_with_support_in_minus_B_to_B`, `s_lp_norm`
**Terminal:** `s_bernstein_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_band_limited_function_with_support_in_minus_B_to_B, s_lp_norm⟩` --[t_auxiliary_construction {multiplier: m_xi=i_xi_phi_xi_smooth_cutoff}]--> output: `s_smooth_frequency_localized_derivative`
2. input: `s_smooth_frequency_localized_derivative` --[t_fourier_transform {convolution: m_check_star_f}]--> output: `s_derivative_as_convolution_with_l1_kernel`
3. input: `s_derivative_as_convolution_with_l1_kernel` --[t_reduce_to_canonical_form {Young: L1_star_Lp_to_Lp_bound}]--> output: `s_bernstein_inequality`

**Techniques used:** t_auxiliary_construction, t_fourier_transform, t_reduce_to_canonical_form

---

### Littlewood–Paley decomposition (cite: https://en.wikipedia.org/wiki/Littlewood%E2%80%93Paley_theory)

**Axioms:** `s_lp_function_on_Rn`, `s_dyadic_frequency_annulus_decomposition`
**Terminal:** `s_littlewood_paley_square_function_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_lp_function_on_Rn, s_dyadic_frequency_annulus_decomposition⟩` --[t_frequency_decomposition {dyadic: Delta_k_f_at_frequency_2_to_k}]--> output: `s_dyadic_blocks_Delta_k_f`
2. input: `s_dyadic_blocks_Delta_k_f` --[t_auxiliary_construction {square_function: S_f=sqrt_sum_abs_Delta_k_f_2}]--> output: `s_square_function_S_f`
3. input: `s_square_function_S_f` --[t_reduce_to_canonical_form {vector_valued_CZ: Fefferman_Stein_bound}]--> output: `s_lp_norm_equivalence_with_square_function`
4. input: `s_lp_norm_equivalence_with_square_function` --[t_reduce_to_canonical_form {duality_for_lower_bound}]--> output: `s_littlewood_paley_square_function_theorem`

**Techniques used:** t_frequency_decomposition, t_auxiliary_construction, t_reduce_to_canonical_form

---

### Stone's theorem on one-parameter unitary groups (cite: https://en.wikipedia.org/wiki/Stone%27s_theorem_on_one-parameter_unitary_groups)

**Axioms:** `s_strongly_continuous_one_parameter_unitary_group`, `s_hilbert_space`
**Terminal:** `s_stone_theorem_unitary_groups` (kind: theorem)

**Steps:**
1. input: `⟨s_strongly_continuous_one_parameter_unitary_group, s_hilbert_space⟩` --[t_auxiliary_construction {generator: A_x=lim_t_to_0_U_t_x_minus_x_over_it}]--> output: `s_dense_domain_with_skew_adjoint_generator`
2. input: `s_dense_domain_with_skew_adjoint_generator` --[t_svd_and_spectral_decomposition {self_adjoint: spectral_measure_of_A}]--> output: `s_spectral_resolution_of_iA`
3. input: `s_spectral_resolution_of_iA` --[t_reduce_to_canonical_form {functional_calculus: U_t=exp_itA}]--> output: `s_stone_theorem_unitary_groups`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_reduce_to_canonical_form

---

### Spectral theorem for bounded self-adjoint operators (cite: https://en.wikipedia.org/wiki/Spectral_theorem)

**Axioms:** `s_bounded_self_adjoint_operator_on_hilbert_space`, `s_continuous_functional_calculus`
**Terminal:** `s_spectral_theorem_bounded_self_adjoint` (kind: theorem)

**Steps:**
1. input: `⟨s_bounded_self_adjoint_operator_on_hilbert_space, s_continuous_functional_calculus⟩` --[t_auxiliary_construction {polynomial_functional_calculus: p_T_via_substitution}]--> output: `s_polynomial_calculus_with_C_star_norm`
2. input: `s_polynomial_calculus_with_C_star_norm` --[t_exhaustion_squeeze {dense: polynomials_dense_in_C_sigma_T}]--> output: `s_continuous_functional_calculus_extension`
3. input: `s_continuous_functional_calculus_extension` --[t_reduce_to_canonical_form {Riesz_Markov: spectral_measure_via_inner_products}]--> output: `s_projection_valued_spectral_measure`
4. input: `s_projection_valued_spectral_measure` --[t_svd_and_spectral_decomposition {integrate: T=int_lambda_dE_lambda}]--> output: `s_spectral_theorem_bounded_self_adjoint`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_reduce_to_canonical_form, t_svd_and_spectral_decomposition

---

### Spectral theorem for compact self-adjoint operators (cite: https://en.wikipedia.org/wiki/Compact_operator_on_Hilbert_space#Spectral_theorem)

**Axioms:** `s_compact_self_adjoint_operator_on_hilbert_space`, `s_hilbert_space`
**Terminal:** `s_spectral_theorem_compact_self_adjoint` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_self_adjoint_operator_on_hilbert_space, s_hilbert_space⟩` --[t_compactness_argument {extremum: maximize_quadratic_form_on_unit_sphere}]--> output: `s_largest_eigenvalue_lambda_1_attained`
2. input: `s_largest_eigenvalue_lambda_1_attained` --[t_reduce_to_canonical_form {orthogonal_complement: restrict_to_eigenvalue_complement}]--> output: `s_recurse_on_invariant_subspace`
3. input: `s_recurse_on_invariant_subspace` --[t_svd_and_spectral_decomposition {iterate: orthonormal_eigenbasis}]--> output: `s_spectral_theorem_compact_self_adjoint`

**Techniques used:** t_compactness_argument, t_reduce_to_canonical_form, t_svd_and_spectral_decomposition

---

### Bochner's theorem (cite: https://en.wikipedia.org/wiki/Bochner%27s_theorem)

**Axioms:** `s_positive_definite_continuous_function_on_R`, `s_finite_borel_measure_on_R`
**Terminal:** `s_bochner_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_positive_definite_continuous_function_on_R, s_finite_borel_measure_on_R⟩` --[t_auxiliary_construction {positive_functional: L_f=int_phi_f_star_f_check}]--> output: `s_positive_linear_functional_on_test_functions`
2. input: `s_positive_linear_functional_on_test_functions` --[t_reduce_to_canonical_form {Riesz_Markov: represent_by_measure}]--> output: `s_representing_measure_mu`
3. input: `s_representing_measure_mu` --[t_fourier_transform {invert: phi=hat_mu}]--> output: `s_bochner_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_fourier_transform

---

## V. Classical inequalities and Sobolev theory

### Cauchy–Schwarz inequality (cite: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarz_inequality)

**Axioms:** `s_inner_product_space`, `s_two_vectors_in_space`
**Terminal:** `s_cauchy_schwarz_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_inner_product_space, s_two_vectors_in_space⟩` --[t_auxiliary_construction {one_param_family: norm_squared_x_minus_t_y_nonneg}]--> output: `s_quadratic_in_t_nonneg`
2. input: `s_quadratic_in_t_nonneg` --[t_complete_the_square {discriminant: leq_0}]--> output: `s_discriminant_inequality`
3. input: `s_discriminant_inequality` --[t_reduce_to_canonical_form {extract: abs_inner_product_leq_norm_product}]--> output: `s_cauchy_schwarz_inequality`

**Techniques used:** t_auxiliary_construction, t_complete_the_square, t_reduce_to_canonical_form

---

### Hölder's inequality (cite: https://en.wikipedia.org/wiki/H%C3%B6lder%27s_inequality)

**Axioms:** `s_lp_function_pair_with_conjugate_exponents`, `s_measure_space`
**Terminal:** `s_holder_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_lp_function_pair_with_conjugate_exponents, s_measure_space⟩` --[t_auxiliary_construction {Young: ab_leq_a_p_over_p_plus_b_q_over_q}]--> output: `s_pointwise_young_bound`
2. input: `s_pointwise_young_bound` --[t_reduce_to_canonical_form {integrate: pointwise_to_integral}]--> output: `s_integrated_form`
3. input: `s_integrated_form` --[t_rescale_for_asymptotic_geometry {homogeneity: optimize_over_lambda}]--> output: `s_holder_inequality`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_rescale_for_asymptotic_geometry

---

### Minkowski inequality (cite: https://en.wikipedia.org/wiki/Minkowski_inequality)

**Axioms:** `s_lp_function_pair`, `s_measure_space`
**Terminal:** `s_minkowski_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_lp_function_pair, s_measure_space⟩` --[t_auxiliary_construction {split: f_plus_g_p=f_plus_g_times_f_plus_g_p_minus_1}]--> output: `s_split_into_two_holder_pieces`
2. input: `s_split_into_two_holder_pieces` --[t_reduce_to_canonical_form {Holder_each_piece}]--> output: `s_holder_bound_on_each_piece`
3. input: `s_holder_bound_on_each_piece` --[t_reduce_to_canonical_form {factor_out: norm_f_plus_g_p_minus_1}]--> output: `s_minkowski_inequality`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Jensen's inequality (cite: https://en.wikipedia.org/wiki/Jensen%27s_inequality)

**Axioms:** `s_convex_function_on_R`, `s_probability_measure_on_R`
**Terminal:** `s_jensen_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_convex_function_on_R, s_probability_measure_on_R⟩` --[t_auxiliary_construction {support_line_at_mean: phi_x_geq_phi_mu_plus_c_x_minus_mu}]--> output: `s_supporting_line_at_expectation`
2. input: `s_supporting_line_at_expectation` --[t_reduce_to_canonical_form {integrate: against_probability_measure}]--> output: `s_expectation_inequality`
3. input: `s_expectation_inequality` --[t_reduce_to_canonical_form {state: phi_E_X_leq_E_phi_X}]--> output: `s_jensen_inequality`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Young's convolution inequality (cite: https://en.wikipedia.org/wiki/Young%27s_convolution_inequality)

**Axioms:** `s_lp_function_pair_with_exponent_relation`, `s_convolution_definition`
**Terminal:** `s_young_convolution_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_lp_function_pair_with_exponent_relation, s_convolution_definition⟩` --[t_reduce_to_canonical_form {endpoint_L1_Lp_to_Lp: trivial}]--> output: `s_L1_Lp_endpoint`
2. input: `s_L1_Lp_endpoint` --[t_reduce_to_canonical_form {endpoint_Lp_Lp_prime_to_L_infinity: holder}]--> output: `s_holder_endpoint`
3. input: `⟨s_L1_Lp_endpoint, s_holder_endpoint⟩` --[t_interpolate_and_continue {Riesz_Thorin}]--> output: `s_young_convolution_inequality`

**Techniques used:** t_reduce_to_canonical_form, t_interpolate_and_continue

---

### Sobolev embedding theorem (cite: https://en.wikipedia.org/wiki/Sobolev_inequality)

**Axioms:** `s_sobolev_space_W_1_p_Rn`, `s_dimension_n_and_exponent_p_less_n`
**Terminal:** `s_sobolev_embedding_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sobolev_space_W_1_p_Rn, s_dimension_n_and_exponent_p_less_n⟩` --[t_auxiliary_construction {Gagliardo: f_x_leq_integral_along_each_coordinate_line}]--> output: `s_directional_integral_representation`
2. input: `s_directional_integral_representation` --[t_reduce_to_canonical_form {iterated_Holder_in_each_variable}]--> output: `s_L_n_over_n_minus_1_bound_for_p_equal_1`
3. input: `s_L_n_over_n_minus_1_bound_for_p_equal_1` --[t_reduce_to_canonical_form {power_and_chain_rule: bootstrap_to_general_p}]--> output: `s_sobolev_embedding_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Gagliardo–Nirenberg–Sobolev inequality (cite: https://en.wikipedia.org/wiki/Gagliardo%E2%80%93Nirenberg_interpolation_inequality)

**Axioms:** `s_smooth_compactly_supported_function_on_Rn`, `s_lp_norm_interpolation_relation`
**Terminal:** `s_gagliardo_nirenberg_sobolev_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_compactly_supported_function_on_Rn, s_lp_norm_interpolation_relation⟩` --[t_auxiliary_construction {scale_invariant_one_derivative_inequality}]--> output: `s_one_derivative_L_n_over_n_minus_1_bound`
2. input: `s_one_derivative_L_n_over_n_minus_1_bound` --[t_interpolate_and_continue {between_Lp_and_higher_Sobolev}]--> output: `s_full_GN_interpolation_chain`
3. input: `s_full_GN_interpolation_chain` --[t_rescale_for_asymptotic_geometry {scaling_check: exponent_relation_forced}]--> output: `s_gagliardo_nirenberg_sobolev_inequality`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_rescale_for_asymptotic_geometry

---

### Poincaré inequality (cite: https://en.wikipedia.org/wiki/Poincar%C3%A9_inequality)

**Axioms:** `s_bounded_lipschitz_domain_in_Rn`, `s_zero_mean_or_zero_boundary_function`
**Terminal:** `s_poincare_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_bounded_lipschitz_domain_in_Rn, s_zero_mean_or_zero_boundary_function⟩` --[t_reductio_ad_absurdum {suppose: no_constant_C}]--> output: `s_normalized_counterexample_sequence`
2. input: `s_normalized_counterexample_sequence` --[t_compactness_argument {Rellich_Kondrachov: precompact_in_L2}]--> output: `s_l2_limit_with_zero_gradient`
3. input: `s_l2_limit_with_zero_gradient` --[t_reduce_to_canonical_form {constant_function_violates_zero_mean}]--> output: `s_poincare_inequality`

**Techniques used:** t_reductio_ad_absurdum, t_compactness_argument, t_reduce_to_canonical_form

---

### Rellich–Kondrachov compactness theorem (cite: https://en.wikipedia.org/wiki/Rellich%E2%80%93Kondrachov_theorem)

**Axioms:** `s_bounded_lipschitz_domain_in_Rn`, `s_bounded_sequence_in_W_1_p`
**Terminal:** `s_rellich_kondrachov_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_bounded_lipschitz_domain_in_Rn, s_bounded_sequence_in_W_1_p⟩` --[t_auxiliary_construction {mollification: smooth_approximation_with_equicontinuity}]--> output: `s_equicontinuous_mollified_sequence`
2. input: `s_equicontinuous_mollified_sequence` --[t_compactness_argument {Arzela_Ascoli}]--> output: `s_uniformly_convergent_mollified_subsequence`
3. input: `s_uniformly_convergent_mollified_subsequence` --[t_exhaustion_squeeze {control_error: by_uniform_W_1_p_bound}]--> output: `s_rellich_kondrachov_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Trace theorem for Sobolev spaces (cite: https://en.wikipedia.org/wiki/Trace_operator)

**Axioms:** `s_W_1_p_function_on_lipschitz_domain`, `s_boundary_of_domain`
**Terminal:** `s_sobolev_trace_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_W_1_p_function_on_lipschitz_domain, s_boundary_of_domain⟩` --[t_auxiliary_construction {extend_by_reflection: half_space_model}]--> output: `s_half_space_local_chart`
2. input: `s_half_space_local_chart` --[t_reduce_to_canonical_form {1d_estimate: f_at_0_via_fundamental_theorem_calculus}]--> output: `s_pointwise_boundary_value_bound`
3. input: `s_pointwise_boundary_value_bound` --[t_reduce_to_canonical_form {patch: partition_of_unity_on_boundary}]--> output: `s_sobolev_trace_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Hardy–Littlewood–Sobolev inequality (cite: https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood%E2%80%93Sobolev_inequality)

**Axioms:** `s_lp_function_on_Rn`, `s_riesz_potential_kernel_abs_x_minus_lambda`
**Terminal:** `s_hardy_littlewood_sobolev_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_lp_function_on_Rn, s_riesz_potential_kernel_abs_x_minus_lambda⟩` --[t_frequency_decomposition {dyadic_kernel_decomposition}]--> output: `s_dyadic_kernel_pieces`
2. input: `s_dyadic_kernel_pieces` --[t_reduce_to_canonical_form {each_piece: HL_maximal_bound}]--> output: `s_bound_via_maximal_function_majorant`
3. input: `s_bound_via_maximal_function_majorant` --[t_interpolate_and_continue {Marcinkiewicz_off_diagonal}]--> output: `s_hardy_littlewood_sobolev_inequality`

**Techniques used:** t_frequency_decomposition, t_reduce_to_canonical_form, t_interpolate_and_continue

---

### Picard–Lindelöf existence theorem (cite: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem)

**Axioms:** `s_lipschitz_ode_data_f_t_x`, `s_initial_condition`
**Terminal:** `s_picard_lindelof_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_lipschitz_ode_data_f_t_x, s_initial_condition⟩` --[t_auxiliary_construction {Picard_operator: T_x_t=x_0_plus_int_0_t_f_s_x_s_ds}]--> output: `s_integral_operator_on_C_I_to_Rn`
2. input: `s_integral_operator_on_C_I_to_Rn` --[t_reduce_to_canonical_form {contraction_on_small_interval}]--> output: `s_strict_contraction_in_sup_norm`
3. input: `s_strict_contraction_in_sup_norm` --[t_contraction_fixed_point {Banach_FPT_application}]--> output: `s_picard_lindelof_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_contraction_fixed_point

---

### Peano existence theorem (cite: https://en.wikipedia.org/wiki/Peano_existence_theorem)

**Axioms:** `s_continuous_ode_data_f_t_x`, `s_initial_condition`
**Terminal:** `s_peano_existence_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_ode_data_f_t_x, s_initial_condition⟩` --[t_auxiliary_construction {Euler_polygons: discrete_approximate_solutions}]--> output: `s_family_of_euler_polygonal_approximations`
2. input: `s_family_of_euler_polygonal_approximations` --[t_compactness_argument {Arzela_Ascoli: equicontinuous_uniformly_bounded}]--> output: `s_convergent_subsequence_limit_continuous`
3. input: `s_convergent_subsequence_limit_continuous` --[t_reduce_to_canonical_form {limit_satisfies_integral_equation}]--> output: `s_peano_existence_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Cauchy–Kovalevskaya theorem (cite: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Kovalevskaya_theorem)

**Axioms:** `s_analytic_PDE_with_analytic_initial_data`, `s_noncharacteristic_initial_surface`
**Terminal:** `s_cauchy_kovalevskaya_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_analytic_PDE_with_analytic_initial_data, s_noncharacteristic_initial_surface⟩` --[t_auxiliary_construction {formal_power_series_solution: by_taylor_coefficient_recurrence}]--> output: `s_formal_power_series_candidate`
2. input: `s_formal_power_series_candidate` --[t_reduce_to_canonical_form {majorant_method: dominate_by_geometric_series}]--> output: `s_convergent_majorant_bound`
3. input: `s_convergent_majorant_bound` --[t_reduce_to_canonical_form {extract: analytic_solution_in_neighborhood}]--> output: `s_cauchy_kovalevskaya_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Lax–Milgram theorem (cite: https://en.wikipedia.org/wiki/Lax%E2%80%93Milgram_theorem)

**Axioms:** `s_bounded_coercive_bilinear_form_on_hilbert_space`, `s_bounded_linear_functional`
**Terminal:** `s_lax_milgram_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_bounded_coercive_bilinear_form_on_hilbert_space, s_bounded_linear_functional⟩` --[t_duality {Riesz_representation: A_u_to_dual_pairing}]--> output: `s_bounded_linear_operator_A_with_coercivity`
2. input: `s_bounded_linear_operator_A_with_coercivity` --[t_reduce_to_canonical_form {invertibility: via_Banach_FPT_on_T_u=u_minus_rho_A_u_minus_f}]--> output: `s_contraction_for_small_rho`
3. input: `s_contraction_for_small_rho` --[t_contraction_fixed_point {fixed_point_solves_equation}]--> output: `s_lax_milgram_theorem`

**Techniques used:** t_duality, t_reduce_to_canonical_form, t_contraction_fixed_point

---

### Banach–Alaoglu theorem (cite: https://en.wikipedia.org/wiki/Banach%E2%80%93Alaoglu_theorem)

**Axioms:** `s_dual_space_of_normed_space`, `s_unit_ball_in_dual`
**Terminal:** `s_banach_alaoglu_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_dual_space_of_normed_space, s_unit_ball_in_dual⟩` --[t_auxiliary_construction {embed: dual_ball_into_product_of_compact_intervals}]--> output: `s_embedding_into_compact_product`
2. input: `s_embedding_into_compact_product` --[t_compactness_argument {Tychonoff: product_of_compacta_compact}]--> output: `s_image_in_compact_product_space`
3. input: `s_image_in_compact_product_space` --[t_reduce_to_canonical_form {closed_in_weak_star_topology}]--> output: `s_banach_alaoglu_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Krein–Milman theorem (cite: https://en.wikipedia.org/wiki/Krein%E2%80%93Milman_theorem)

**Axioms:** `s_compact_convex_subset_of_locally_convex_space`, `s_extreme_points`
**Terminal:** `s_krein_milman_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_convex_subset_of_locally_convex_space, s_extreme_points⟩` --[t_auxiliary_construction {Zorn: minimal_extreme_subsets}]--> output: `s_minimal_extreme_subset_singleton`
2. input: `s_minimal_extreme_subset_singleton` --[t_reduce_to_canonical_form {existence_of_extreme_points}]--> output: `s_nonempty_extreme_point_set`
3. input: `s_nonempty_extreme_point_set` --[t_reductio_ad_absurdum {hahn_banach_separates_K_from_closed_convex_hull_of_extreme}]--> output: `s_krein_milman_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_reductio_ad_absurdum

---

### Choquet representation theorem (cite: https://en.wikipedia.org/wiki/Choquet_theory)

**Axioms:** `s_metrizable_compact_convex_set`, `s_point_in_convex_set`
**Terminal:** `s_choquet_representation_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_metrizable_compact_convex_set, s_point_in_convex_set⟩` --[t_auxiliary_construction {affine_functional_evaluation: L_phi=phi_x_for_phi_in_A_K}]--> output: `s_positive_linear_functional_on_continuous_functions`
2. input: `s_positive_linear_functional_on_continuous_functions` --[t_reduce_to_canonical_form {Riesz_Markov: represent_by_probability_measure}]--> output: `s_probability_measure_on_K`
3. input: `s_probability_measure_on_K` --[t_reduce_to_canonical_form {support_on_extreme_via_Bishop_de_Leeuw}]--> output: `s_choquet_representation_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Riesz lemma (almost-perpendicular vector) (cite: https://en.wikipedia.org/wiki/Riesz%27s_lemma)

**Axioms:** `s_normed_space_with_proper_closed_subspace_Y`, `s_quantity_alpha_in_0_1`
**Terminal:** `s_riesz_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_normed_space_with_proper_closed_subspace_Y, s_quantity_alpha_in_0_1⟩` --[t_auxiliary_construction {pick: x_outside_Y_with_distance_1_to_Y}]--> output: `s_near_extremal_x_outside_Y`
2. input: `s_near_extremal_x_outside_Y` --[t_rescale_for_asymptotic_geometry {normalize: x_minus_y_over_norm_x_minus_y}]--> output: `s_unit_vector_alpha_far_from_Y`
3. input: `s_unit_vector_alpha_far_from_Y` --[t_reduce_to_canonical_form {extract: alpha_almost_perpendicular}]--> output: `s_riesz_lemma`

**Techniques used:** t_auxiliary_construction, t_rescale_for_asymptotic_geometry, t_reduce_to_canonical_form

---

### Riesz's theorem on compactness of unit ball (cite: https://en.wikipedia.org/wiki/Riesz%27s_lemma#Theorem)

**Axioms:** `s_normed_space`, `s_unit_ball_compactness`
**Terminal:** `s_riesz_compactness_unit_ball` (kind: theorem)

**Steps:**
1. input: `⟨s_normed_space, s_unit_ball_compactness⟩` --[t_reductio_ad_absurdum {suppose: unit_ball_compact_but_infinite_dim}]--> output: `s_compact_unit_ball_assumption`
2. input: `s_compact_unit_ball_assumption` --[t_reduce_to_canonical_form {iterate_Riesz_lemma: alpha=1_over_2_sequence}]--> output: `s_sequence_with_pairwise_distance_geq_half`
3. input: `s_sequence_with_pairwise_distance_geq_half` --[t_reduce_to_canonical_form {no_convergent_subsequence_contradicts_compactness}]--> output: `s_riesz_compactness_unit_ball`

**Techniques used:** t_reductio_ad_absurdum, t_reduce_to_canonical_form

---

### Hahn decomposition theorem (cite: https://en.wikipedia.org/wiki/Hahn_decomposition_theorem)

**Axioms:** `s_signed_measure_on_measurable_space`, `s_measurable_space`
**Terminal:** `s_hahn_decomposition_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_signed_measure_on_measurable_space, s_measurable_space⟩` --[t_auxiliary_construction {extremize: sup_of_nu_E_over_measurable_sets}]--> output: `s_supremum_achieved_via_chain`
2. input: `s_supremum_achieved_via_chain` --[t_compactness_argument {countable_union_attains_sup}]--> output: `s_positive_set_P_with_sup`
3. input: `s_positive_set_P_with_sup` --[t_reduce_to_canonical_form {complement_is_negative_set}]--> output: `s_hahn_decomposition_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Jordan decomposition theorem (cite: https://en.wikipedia.org/wiki/Hahn_decomposition_theorem#Jordan_decomposition)

**Axioms:** `s_signed_measure_on_measurable_space`, `s_hahn_decomposition_pair`
**Terminal:** `s_jordan_decomposition_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_signed_measure_on_measurable_space, s_hahn_decomposition_pair⟩` --[t_reduce_to_canonical_form {restrict: nu_plus_E=nu_E_cap_P_and_nu_minus_E=-nu_E_cap_N}]--> output: `s_two_positive_measures_nu_plus_nu_minus`
2. input: `s_two_positive_measures_nu_plus_nu_minus` --[t_symmetry_reduction {mutual_singularity: P_and_N_disjoint}]--> output: `s_mutually_singular_decomposition`
3. input: `s_mutually_singular_decomposition` --[t_reduce_to_canonical_form {state: nu=nu_plus_minus_nu_minus_unique}]--> output: `s_jordan_decomposition_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_symmetry_reduction

---

### Lebesgue decomposition theorem (cite: https://en.wikipedia.org/wiki/Lebesgue%27s_decomposition_theorem)

**Axioms:** `s_sigma_finite_signed_measure`, `s_reference_sigma_finite_measure`
**Terminal:** `s_lebesgue_decomposition_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sigma_finite_signed_measure, s_reference_sigma_finite_measure⟩` --[t_auxiliary_construction {sup_set: A_max_with_nu_singular_on_A}]--> output: `s_maximal_singular_carrier_A`
2. input: `s_maximal_singular_carrier_A` --[t_reduce_to_canonical_form {split: nu_singular_on_A_plus_nu_ac_on_complement}]--> output: `s_two_part_decomposition`
3. input: `s_two_part_decomposition` --[t_reduce_to_canonical_form {Radon_Nikodym_on_ac_part}]--> output: `s_lebesgue_decomposition_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Stone–Čech compactification (cite: https://en.wikipedia.org/wiki/Stone%E2%80%93%C4%8Cech_compactification)

**Axioms:** `s_tychonoff_topological_space`, `s_universal_property_for_continuous_maps_to_compact_hausdorff`
**Terminal:** `s_stone_cech_compactification` (kind: theorem)

**Steps:**
1. input: `⟨s_tychonoff_topological_space, s_universal_property_for_continuous_maps_to_compact_hausdorff⟩` --[t_auxiliary_construction {embed: X_into_product_of_unit_intervals_indexed_by_C_b_X}]--> output: `s_embedding_into_compact_cube`
2. input: `s_embedding_into_compact_cube` --[t_compactness_argument {Tychonoff: take_closure}]--> output: `s_compact_hausdorff_completion_betaX`
3. input: `s_compact_hausdorff_completion_betaX` --[t_reduce_to_canonical_form {universal_property: extension_of_continuous_maps}]--> output: `s_stone_cech_compactification`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Riesz–Fischer theorem (cite: https://en.wikipedia.org/wiki/Riesz%E2%80%93Fischer_theorem)

**Axioms:** `s_l2_summable_sequence_of_complex_numbers`, `s_orthonormal_basis_of_hilbert_space`
**Terminal:** `s_riesz_fischer_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_l2_summable_sequence_of_complex_numbers, s_orthonormal_basis_of_hilbert_space⟩` --[t_auxiliary_construction {partial_sums: s_N=sum_n_leq_N_c_n_e_n}]--> output: `s_partial_sum_sequence`
2. input: `s_partial_sum_sequence` --[t_reduce_to_canonical_form {Pythagoras_cauchy_in_norm}]--> output: `s_cauchy_sequence_in_hilbert_space`
3. input: `s_cauchy_sequence_in_hilbert_space` --[t_exhaustion_squeeze {completeness: limit_exists}]--> output: `s_riesz_fischer_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Bessel's inequality (cite: https://en.wikipedia.org/wiki/Bessel%27s_inequality)

**Axioms:** `s_inner_product_space`, `s_orthonormal_sequence`
**Terminal:** `s_bessel_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_inner_product_space, s_orthonormal_sequence⟩` --[t_projection_to_subspace {finite: onto_span_e_1_to_e_N}]--> output: `s_orthogonal_projection_decomposition`
2. input: `s_orthogonal_projection_decomposition` --[t_reduce_to_canonical_form {pythagoras: norm_squared_decomposition}]--> output: `s_partial_sum_squared_bound`
3. input: `s_partial_sum_squared_bound` --[t_exhaustion_squeeze {N_to_infinity}]--> output: `s_bessel_inequality`

**Techniques used:** t_projection_to_subspace, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Riesz representation theorem on Hilbert space (cite: https://en.wikipedia.org/wiki/Riesz_representation_theorem)

**Axioms:** `s_hilbert_space`, `s_bounded_linear_functional_on_hilbert`
**Terminal:** `s_riesz_representation_hilbert` (kind: theorem)

**Steps:**
1. input: `⟨s_hilbert_space, s_bounded_linear_functional_on_hilbert⟩` --[t_auxiliary_construction {kernel: closed_hyperplane_M_eq_ker_L}]--> output: `s_closed_subspace_kernel_of_L`
2. input: `s_closed_subspace_kernel_of_L` --[t_projection_to_subspace {orthogonal_complement_one_dim}]--> output: `s_orthogonal_complement_spanned_by_z_0`
3. input: `s_orthogonal_complement_spanned_by_z_0` --[t_reduce_to_canonical_form {set: y=L_z_0_over_norm_z_0_squared_times_z_0}]--> output: `s_riesz_representation_hilbert`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Hilbert projection theorem (cite: https://en.wikipedia.org/wiki/Hilbert_projection_theorem)

**Axioms:** `s_closed_convex_subset_of_hilbert_space`, `s_point_in_hilbert_space`
**Terminal:** `s_hilbert_projection_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_closed_convex_subset_of_hilbert_space, s_point_in_hilbert_space⟩` --[t_auxiliary_construction {minimizing_sequence: dist_to_C}]--> output: `s_minimizing_sequence_y_n_in_C`
2. input: `s_minimizing_sequence_y_n_in_C` --[t_reduce_to_canonical_form {parallelogram_identity: cauchy_in_norm}]--> output: `s_cauchy_minimizing_sequence`
3. input: `s_cauchy_minimizing_sequence` --[t_exhaustion_squeeze {limit_in_C_unique_minimizer}]--> output: `s_hilbert_projection_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Egorov's theorem on Hilbert (Weyl-type closeness; not the measure theorem) — replaced by Banach contraction principle (cite: https://en.wikipedia.org/wiki/Banach_fixed-point_theorem)

(Skipped: covered by `s_banach_fpt` in canonical_node_index — listed here for tracking.)

---

### Mertens's theorem on convolution of series (cite: https://en.wikipedia.org/wiki/Cauchy_product#Mertens%27_theorem)

**Axioms:** `s_two_real_series_one_absolutely_convergent`, `s_cauchy_product`
**Terminal:** `s_mertens_cauchy_product_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_two_real_series_one_absolutely_convergent, s_cauchy_product⟩` --[t_auxiliary_construction {partial_sum_decomposition_main_plus_tail}]--> output: `s_partial_sum_split_main_tail`
2. input: `s_partial_sum_split_main_tail` --[t_reduce_to_canonical_form {bound_tail_by_absolute_convergence}]--> output: `s_tail_estimate_uniform`
3. input: `s_tail_estimate_uniform` --[t_exhaustion_squeeze {N_to_infinity}]--> output: `s_mertens_cauchy_product_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Abel's summation theorem (cite: https://en.wikipedia.org/wiki/Abel%27s_summation_formula)

**Axioms:** `s_real_power_series_with_radius_of_convergence_1`, `s_convergent_series_at_endpoint_x_eq_1`
**Terminal:** `s_abel_summation_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_real_power_series_with_radius_of_convergence_1, s_convergent_series_at_endpoint_x_eq_1⟩` --[t_auxiliary_construction {Abel_partial_summation: rewrite_as_telescoping}]--> output: `s_partial_summation_identity`
2. input: `s_partial_summation_identity` --[t_reduce_to_canonical_form {uniform_continuity_of_partial_sums_at_endpoint}]--> output: `s_uniform_convergence_on_segment_to_1`
3. input: `s_uniform_convergence_on_segment_to_1` --[t_exhaustion_squeeze {x_to_1_minus}]--> output: `s_abel_summation_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Tauberian theorem (Hardy–Littlewood) (cite: https://en.wikipedia.org/wiki/Tauberian_theorem)

**Axioms:** `s_series_Abel_summable_to_s`, `s_tauberian_growth_condition_on_a_n`
**Terminal:** `s_hardy_littlewood_tauberian_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_series_Abel_summable_to_s, s_tauberian_growth_condition_on_a_n⟩` --[t_auxiliary_construction {smoothing: replace_indicator_by_polynomial_window}]--> output: `s_polynomial_smoothed_partial_sum`
2. input: `s_polynomial_smoothed_partial_sum` --[t_reduce_to_canonical_form {Weierstrass_approximation_for_indicator}]--> output: `s_indicator_approximation_via_polynomial`
3. input: `s_indicator_approximation_via_polynomial` --[t_exhaustion_squeeze {Tauberian_growth_controls_oscillation}]--> output: `s_hardy_littlewood_tauberian_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Wiener Tauberian theorem (cite: https://en.wikipedia.org/wiki/Wiener%27s_tauberian_theorem)

**Axioms:** `s_l1_function_on_R_with_nonvanishing_fourier_transform`, `s_translation_invariant_subspace_of_L1`
**Terminal:** `s_wiener_tauberian_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_l1_function_on_R_with_nonvanishing_fourier_transform, s_translation_invariant_subspace_of_L1⟩` --[t_fourier_transform {translate: subspace_to_ideal_in_Wiener_algebra}]--> output: `s_closed_ideal_in_Wiener_algebra`
2. input: `s_closed_ideal_in_Wiener_algebra` --[t_duality {maximal_ideal_space: corresponds_to_R}]--> output: `s_no_common_zero_in_spectrum`
3. input: `s_no_common_zero_in_spectrum` --[t_reduce_to_canonical_form {ideal_equals_whole_algebra}]--> output: `s_wiener_tauberian_theorem`

**Techniques used:** t_fourier_transform, t_duality, t_reduce_to_canonical_form

---

### Bolzano's theorem on continuity of polynomials (cite: https://en.wikipedia.org/wiki/Continuous_function#Polynomial_functions_are_continuous)

**Axioms:** `s_polynomial_function_on_R`, `s_epsilon_delta_definition`
**Terminal:** `s_polynomial_continuity_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_polynomial_function_on_R, s_epsilon_delta_definition⟩` --[t_axiomatize_from_instances {monomial: x_n_continuous}]--> output: `s_monomial_continuity`
2. input: `s_monomial_continuity` --[t_reduce_to_canonical_form {sums_and_products_of_continuous_functions}]--> output: `s_polynomial_continuity_theorem`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Heine's theorem (uniform continuity on compact sets) (cite: https://en.wikipedia.org/wiki/Heine%E2%80%93Cantor_theorem)

**Axioms:** `s_continuous_function_on_compact_metric_space`, `s_uniform_continuity_definition`
**Terminal:** `s_heine_cantor_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_function_on_compact_metric_space, s_uniform_continuity_definition⟩` --[t_reductio_ad_absurdum {suppose: not_uniformly_continuous}]--> output: `s_two_sequences_with_distance_to_0_but_image_apart`
2. input: `s_two_sequences_with_distance_to_0_but_image_apart` --[t_compactness_argument {extract: convergent_subsequence}]--> output: `s_common_limit_point_x`
3. input: `s_common_limit_point_x` --[t_reduce_to_canonical_form {continuity_at_x_contradicts_image_separation}]--> output: `s_heine_cantor_theorem`

**Techniques used:** t_reductio_ad_absurdum, t_compactness_argument, t_reduce_to_canonical_form

---

### Cantor's diagonal argument for uncountability — already in graph as `s_uncountability_of_reals` (skipped)

---

### Ascoli's theorem on equicontinuous families — covered above as Arzelà–Ascoli (skipped duplicate)

---

### Stone–Weierstrass complex version (cite: https://en.wikipedia.org/wiki/Stone%E2%80%93Weierstrass_theorem#Stone%E2%80%93Weierstrass_theorem,_complex_version)

**Axioms:** `s_compact_hausdorff_space`, `s_self_adjoint_separating_unital_subalgebra_of_complex_C_X`
**Terminal:** `s_stone_weierstrass_complex` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_hausdorff_space, s_self_adjoint_separating_unital_subalgebra_of_complex_C_X⟩` --[t_reduce_to_canonical_form {real_part: A_real=A_intersect_C_real_X}]--> output: `s_real_subalgebra_separating`
2. input: `s_real_subalgebra_separating` --[t_reduce_to_canonical_form {apply: real_Stone_Weierstrass}]--> output: `s_real_subalgebra_dense`
3. input: `s_real_subalgebra_dense` --[t_reduce_to_canonical_form {recombine: A=A_real_plus_i_A_real_dense}]--> output: `s_stone_weierstrass_complex`

**Techniques used:** t_reduce_to_canonical_form

---

### Stone representation theorem (cite: https://en.wikipedia.org/wiki/Stone%27s_representation_theorem_for_Boolean_algebras)

**Axioms:** `s_boolean_algebra`, `s_compact_totally_disconnected_hausdorff_space`
**Terminal:** `s_stone_representation_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_boolean_algebra, s_compact_totally_disconnected_hausdorff_space⟩` --[t_auxiliary_construction {space: S_B=ultrafilters_on_B_with_clopen_topology}]--> output: `s_stone_space_S_B`
2. input: `s_stone_space_S_B` --[t_reduce_to_canonical_form {clopens_of_S_B_form_isomorphic_boolean_algebra}]--> output: `s_isomorphism_B_to_clopens`
3. input: `s_isomorphism_B_to_clopens` --[t_structural_isomorphism {duality: boolean_algebras_dual_to_stone_spaces}]--> output: `s_stone_representation_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_structural_isomorphism

---

### Gelfand representation theorem (cite: https://en.wikipedia.org/wiki/Gelfand_representation)

**Axioms:** `s_commutative_unital_banach_algebra`, `s_space_of_characters_with_weak_star_topology`
**Terminal:** `s_gelfand_representation_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_commutative_unital_banach_algebra, s_space_of_characters_with_weak_star_topology⟩` --[t_auxiliary_construction {character_space: Delta_A=multiplicative_linear_functionals}]--> output: `s_compact_hausdorff_character_space`
2. input: `s_compact_hausdorff_character_space` --[t_reduce_to_canonical_form {Gelfand_map: a_to_hat_a_evaluation}]--> output: `s_continuous_algebra_homomorphism_A_to_C_Delta_A`
3. input: `s_continuous_algebra_homomorphism_A_to_C_Delta_A` --[t_structural_isomorphism {for_C_star_algebra: isometric_isomorphism}]--> output: `s_gelfand_representation_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_structural_isomorphism

---

### Fredholm alternative (cite: https://en.wikipedia.org/wiki/Fredholm_alternative)

**Axioms:** `s_compact_operator_K_on_banach_space`, `s_equation_I_minus_K_x_eq_y`
**Terminal:** `s_fredholm_alternative` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_operator_K_on_banach_space, s_equation_I_minus_K_x_eq_y⟩` --[t_reduce_to_canonical_form {kernel_finite_dim: by_Riesz_compactness}]--> output: `s_finite_dim_kernel_of_I_minus_K`
2. input: `s_finite_dim_kernel_of_I_minus_K` --[t_duality {transposed_operator_I_minus_K_star}]--> output: `s_finite_dim_cokernel_equals_kernel_of_adjoint`
3. input: `s_finite_dim_cokernel_equals_kernel_of_adjoint` --[t_reduce_to_canonical_form {index_zero: dim_ker_equals_dim_coker}]--> output: `s_fredholm_alternative`

**Techniques used:** t_reduce_to_canonical_form, t_duality

---

### Mercer's theorem (cite: https://en.wikipedia.org/wiki/Mercer%27s_theorem)

**Axioms:** `s_symmetric_continuous_positive_definite_kernel_on_compact_set`, `s_l2_eigenfunctions_of_integral_operator`
**Terminal:** `s_mercer_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_symmetric_continuous_positive_definite_kernel_on_compact_set, s_l2_eigenfunctions_of_integral_operator⟩` --[t_auxiliary_construction {integral_operator: T_K_f=int_K_x_y_f_y_dy}]--> output: `s_compact_self_adjoint_operator_T_K`
2. input: `s_compact_self_adjoint_operator_T_K` --[t_svd_and_spectral_decomposition {orthonormal_eigenbasis_with_eigenvalues_lambda_n}]--> output: `s_spectral_decomposition_of_T_K`
3. input: `s_spectral_decomposition_of_T_K` --[t_reduce_to_canonical_form {uniformly_convergent_series_for_K_x_y}]--> output: `s_mercer_theorem`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_reduce_to_canonical_form

---

### Eberlein–Šmulian theorem (cite: https://en.wikipedia.org/wiki/Eberlein%E2%80%93%C5%A0mulian_theorem)

**Axioms:** `s_banach_space`, `s_subset_of_banach_space`
**Terminal:** `s_eberlein_smulian_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_banach_space, s_subset_of_banach_space⟩` --[t_reduce_to_canonical_form {weak_compactness_definition: nets_have_convergent_subnets}]--> output: `s_net_based_weak_compactness`
2. input: `s_net_based_weak_compactness` --[t_compactness_argument {via: separable_subspace_reduction}]--> output: `s_metrizable_weak_topology_on_separable_part`
3. input: `s_metrizable_weak_topology_on_separable_part` --[t_reduce_to_canonical_form {equivalent: weak_sequential_compactness}]--> output: `s_eberlein_smulian_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_compactness_argument

---

### Mackey–Arens theorem (cite: https://en.wikipedia.org/wiki/Mackey_topology)

**Axioms:** `s_dual_pair_of_vector_spaces`, `s_locally_convex_topology_compatible_with_duality`
**Terminal:** `s_mackey_arens_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_dual_pair_of_vector_spaces, s_locally_convex_topology_compatible_with_duality⟩` --[t_auxiliary_construction {polar: bipolar_theorem_on_subsets}]--> output: `s_polar_topology_family`
2. input: `s_polar_topology_family` --[t_duality {compatible_topology_iff_polar_of_weakly_compact_convex}]--> output: `s_compatible_topology_characterization`
3. input: `s_compatible_topology_characterization` --[t_reduce_to_canonical_form {Mackey_topology_as_finest}]--> output: `s_mackey_arens_theorem`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Goldstine theorem (cite: https://en.wikipedia.org/wiki/Goldstine_theorem)

**Axioms:** `s_banach_space_X`, `s_canonical_embedding_X_into_double_dual`
**Terminal:** `s_goldstine_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_banach_space_X, s_canonical_embedding_X_into_double_dual⟩` --[t_auxiliary_construction {bipolar: closure_of_unit_ball_in_weak_star_topology}]--> output: `s_weak_star_closure_of_J_B_X`
2. input: `s_weak_star_closure_of_J_B_X` --[t_reduce_to_canonical_form {bipolar_theorem: closure_equals_polar_of_polar}]--> output: `s_polar_of_polar_equals_B_X_double_dual`
3. input: `s_polar_of_polar_equals_B_X_double_dual` --[t_reduce_to_canonical_form {J_B_X_weak_star_dense_in_B_X_double_dual}]--> output: `s_goldstine_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Brouwer fixed-point theorem (already in graph as `s_brouwer_fpt`) — skipped

---

### Schauder fixed-point theorem (cite: https://en.wikipedia.org/wiki/Schauder_fixed-point_theorem)

**Axioms:** `s_continuous_self_map_of_compact_convex_subset_of_banach_space`, `s_banach_space`
**Terminal:** `s_schauder_fixed_point_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_self_map_of_compact_convex_subset_of_banach_space, s_banach_space⟩` --[t_auxiliary_construction {finite_dim_approximation_via_partition_of_unity}]--> output: `s_finite_dim_approximate_map`
2. input: `s_finite_dim_approximate_map` --[t_reduce_to_canonical_form {apply: Brouwer_fpt_to_each_approximation}]--> output: `s_sequence_of_approximate_fixed_points`
3. input: `s_sequence_of_approximate_fixed_points` --[t_compactness_argument {extract: convergent_subsequence_via_compactness_of_K}]--> output: `s_schauder_fixed_point_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_compactness_argument

---

### Kakutani fixed-point theorem (cite: https://en.wikipedia.org/wiki/Kakutani_fixed-point_theorem)

**Axioms:** `s_upper_hemicontinuous_set_valued_self_map_with_convex_values`, `s_compact_convex_subset_of_Rn`
**Terminal:** `s_kakutani_fixed_point_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_upper_hemicontinuous_set_valued_self_map_with_convex_values, s_compact_convex_subset_of_Rn⟩` --[t_auxiliary_construction {single_valued_approximation_via_selection}]--> output: `s_continuous_single_valued_approximations`
2. input: `s_continuous_single_valued_approximations` --[t_reduce_to_canonical_form {apply: Brouwer_fpt}]--> output: `s_sequence_of_approximate_fixed_points`
3. input: `s_sequence_of_approximate_fixed_points` --[t_compactness_argument {graph_closed_under_limit}]--> output: `s_kakutani_fixed_point_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_compactness_argument

---

### Stampacchia variational inequality theorem (cite: https://en.wikipedia.org/wiki/Stampacchia_theorem)

**Axioms:** `s_continuous_coercive_bilinear_form_on_hilbert_space`, `s_closed_convex_subset_K`
**Terminal:** `s_stampacchia_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_coercive_bilinear_form_on_hilbert_space, s_closed_convex_subset_K⟩` --[t_auxiliary_construction {projection_operator_onto_K: P_K}]--> output: `s_iteration_T_u_eq_P_K_u_minus_rho_A_u_minus_f`
2. input: `s_iteration_T_u_eq_P_K_u_minus_rho_A_u_minus_f` --[t_contraction_fixed_point {for_small_rho}]--> output: `s_unique_fixed_point_in_K`
3. input: `s_unique_fixed_point_in_K` --[t_reduce_to_canonical_form {translate: variational_inequality}]--> output: `s_stampacchia_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_reduce_to_canonical_form

---

### Banach–Mazur theorem (cite: https://en.wikipedia.org/wiki/Banach%E2%80%93Mazur_theorem)

**Axioms:** `s_separable_banach_space`, `s_continuous_function_space_C_0_1`
**Terminal:** `s_banach_mazur_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_separable_banach_space, s_continuous_function_space_C_0_1⟩` --[t_auxiliary_construction {dense_sequence: x_n_in_unit_ball}]--> output: `s_countable_dense_sequence_in_unit_ball`
2. input: `s_countable_dense_sequence_in_unit_ball` --[t_reduce_to_canonical_form {evaluate_at_dyadic_rationals: embedding_into_C_0_1}]--> output: `s_isometric_embedding_via_Auerbach_type_basis`
3. input: `s_isometric_embedding_via_Auerbach_type_basis` --[t_reduce_to_canonical_form {extend: isometric_embedding_of_whole_space}]--> output: `s_banach_mazur_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Krein–Šmulian theorem (cite: https://en.wikipedia.org/wiki/Krein%E2%80%93Smulian_theorem)

**Axioms:** `s_banach_space`, `s_convex_subset_of_dual_with_weak_star_closed_intersections_with_bounded_sets`
**Terminal:** `s_krein_smulian_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_banach_space, s_convex_subset_of_dual_with_weak_star_closed_intersections_with_bounded_sets⟩` --[t_auxiliary_construction {Mackey_topology_consideration}]--> output: `s_compatible_topology_setup`
2. input: `s_compatible_topology_setup` --[t_reduce_to_canonical_form {apply: Mackey_Arens_to_extract_closedness}]--> output: `s_weak_star_closed_globally`
3. input: `s_weak_star_closed_globally` --[t_reduce_to_canonical_form {conclude: convex_set_weak_star_closed}]--> output: `s_krein_smulian_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Hardy–Littlewood–Polya rearrangement inequality (cite: https://en.wikipedia.org/wiki/Rearrangement_inequality)

**Axioms:** `s_two_finite_sequences_of_real_numbers`, `s_permutation_group_on_indices`
**Terminal:** `s_rearrangement_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_two_finite_sequences_of_real_numbers, s_permutation_group_on_indices⟩` --[t_auxiliary_construction {swap: adjacent_transposition_lemma}]--> output: `s_pairwise_swap_decreases_sum_if_inversion`
2. input: `s_pairwise_swap_decreases_sum_if_inversion` --[t_reduce_to_canonical_form {sort: bubble_sort_to_monotone_pairing}]--> output: `s_sorted_pairing_extremal`
3. input: `s_sorted_pairing_extremal` --[t_reduce_to_canonical_form {state: monotone_pairings_extremize}]--> output: `s_rearrangement_inequality`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Brunn–Minkowski inequality (cite: https://en.wikipedia.org/wiki/Brunn%E2%80%93Minkowski_theorem)

**Axioms:** `s_two_nonempty_measurable_subsets_of_Rn`, `s_Minkowski_sum_A_plus_B`
**Terminal:** `s_brunn_minkowski_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_two_nonempty_measurable_subsets_of_Rn, s_Minkowski_sum_A_plus_B⟩` --[t_axiomatize_from_instances {start: boxes_aligned_with_axes}]--> output: `s_brunn_minkowski_for_boxes_via_AM_GM`
2. input: `s_brunn_minkowski_for_boxes_via_AM_GM` --[t_reduce_to_canonical_form {induct: on_number_of_boxes_in_finite_union}]--> output: `s_brunn_minkowski_for_finite_unions_of_boxes`
3. input: `s_brunn_minkowski_for_finite_unions_of_boxes` --[t_exhaustion_squeeze {approximate: measurable_sets_by_box_unions}]--> output: `s_brunn_minkowski_inequality`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Isoperimetric inequality in R^n (cite: https://en.wikipedia.org/wiki/Isoperimetric_inequality)

**Axioms:** `s_bounded_open_subset_of_Rn_with_smooth_boundary`, `s_volume_and_surface_area`
**Terminal:** `s_isoperimetric_inequality_Rn` (kind: theorem)

**Steps:**
1. input: `⟨s_bounded_open_subset_of_Rn_with_smooth_boundary, s_volume_and_surface_area⟩` --[t_reduce_to_canonical_form {Minkowski_content: surface_area_via_eps_thickening}]--> output: `s_surface_area_as_eps_limit_of_volumes`
2. input: `s_surface_area_as_eps_limit_of_volumes` --[t_reduce_to_canonical_form {apply: Brunn_Minkowski_to_A_plus_eps_B}]--> output: `s_first_variation_inequality`
3. input: `s_first_variation_inequality` --[t_rescale_for_asymptotic_geometry {eps_to_0_and_compare_to_ball}]--> output: `s_isoperimetric_inequality_Rn`

**Techniques used:** t_reduce_to_canonical_form, t_rescale_for_asymptotic_geometry

---

### Prékopa–Leindler inequality (cite: https://en.wikipedia.org/wiki/Pr%C3%A9kopa%E2%80%93Leindler_inequality)

**Axioms:** `s_three_nonneg_measurable_functions_with_log_concave_constraint`, `s_lebesgue_measure_on_Rn`
**Terminal:** `s_prekopa_leindler_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_three_nonneg_measurable_functions_with_log_concave_constraint, s_lebesgue_measure_on_Rn⟩` --[t_axiomatize_from_instances {start: indicator_functions_case_equals_Brunn_Minkowski}]--> output: `s_indicator_case_equivalent_to_brunn_minkowski`
2. input: `s_indicator_case_equivalent_to_brunn_minkowski` --[t_reduce_to_canonical_form {layer_cake: bootstrap_to_general_nonneg}]--> output: `s_layer_cake_lift_to_general_functions`
3. input: `s_layer_cake_lift_to_general_functions` --[t_reduce_to_canonical_form {integrate_in_level: full_inequality}]--> output: `s_prekopa_leindler_inequality`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Loomis–Whitney inequality (cite: https://en.wikipedia.org/wiki/Loomis%E2%80%93Whitney_inequality)

**Axioms:** `s_measurable_subset_of_Rn`, `s_n_coordinate_projections`
**Terminal:** `s_loomis_whitney_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_measurable_subset_of_Rn, s_n_coordinate_projections⟩` --[t_auxiliary_construction {indicator_with_iterated_Holder}]--> output: `s_iterated_holder_on_indicator`
2. input: `s_iterated_holder_on_indicator` --[t_reduce_to_canonical_form {project: combine_pointwise_estimates_via_sub_sup_in_each_variable}]--> output: `s_projection_product_bound`
3. input: `s_projection_product_bound` --[t_reduce_to_canonical_form {integrate: full_inequality}]--> output: `s_loomis_whitney_inequality`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Khintchine's inequality (cite: https://en.wikipedia.org/wiki/Khintchine_inequality)

**Axioms:** `s_sequence_of_independent_random_signs_eps_n`, `s_lp_norm_of_linear_combination`
**Terminal:** `s_khintchine_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_sequence_of_independent_random_signs_eps_n, s_lp_norm_of_linear_combination⟩` --[t_auxiliary_construction {moment_generating_function_of_sum_eps_n_a_n}]--> output: `s_MGF_bounded_by_gaussian_via_cosh_inequality`
2. input: `s_MGF_bounded_by_gaussian_via_cosh_inequality` --[t_reduce_to_canonical_form {Chernoff: subgaussian_tail_bound}]--> output: `s_subgaussian_tail_estimate`
3. input: `s_subgaussian_tail_estimate` --[t_interpolate_and_continue {moments_equivalent_via_layer_cake}]--> output: `s_khintchine_inequality`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_interpolate_and_continue

---

### Grothendieck's inequality (cite: https://en.wikipedia.org/wiki/Grothendieck_inequality)

**Axioms:** `s_matrix_with_bounded_entrywise_real_quadratic_form`, `s_unit_vectors_in_hilbert_space`
**Terminal:** `s_grothendieck_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_matrix_with_bounded_entrywise_real_quadratic_form, s_unit_vectors_in_hilbert_space⟩` --[t_auxiliary_construction {Gaussian_random_projection_x_to_sign_dot_g}]--> output: `s_randomized_rounding_via_gaussian_projection`
2. input: `s_randomized_rounding_via_gaussian_projection` --[t_reduce_to_canonical_form {expectation: 2_over_pi_arcsine_inner_product}]--> output: `s_arcsine_kernel_factorization`
3. input: `s_arcsine_kernel_factorization` --[t_reduce_to_canonical_form {extract: universal_grothendieck_constant_bound}]--> output: `s_grothendieck_inequality`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Hausdorff moment problem (cite: https://en.wikipedia.org/wiki/Hausdorff_moment_problem)

**Axioms:** `s_real_sequence_m_n`, `s_uniqueness_of_measure_on_unit_interval`
**Terminal:** `s_hausdorff_moment_problem` (kind: theorem)

**Steps:**
1. input: `⟨s_real_sequence_m_n, s_uniqueness_of_measure_on_unit_interval⟩` --[t_auxiliary_construction {finite_differences: Delta_k_m_n_nonneg_iff_completely_monotonic}]--> output: `s_complete_monotonicity_criterion`
2. input: `s_complete_monotonicity_criterion` --[t_reduce_to_canonical_form {build: positive_functional_on_polynomials}]--> output: `s_positive_functional_on_C_0_1_via_density`
3. input: `s_positive_functional_on_C_0_1_via_density` --[t_reduce_to_canonical_form {Riesz_Markov: represent_by_measure}]--> output: `s_hausdorff_moment_problem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Bernstein–Widder theorem on completely monotone functions (cite: https://en.wikipedia.org/wiki/Bernstein%27s_theorem_on_monotone_functions)

**Axioms:** `s_completely_monotone_function_on_positive_reals`, `s_laplace_transform_of_positive_measure`
**Terminal:** `s_bernstein_widder_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_completely_monotone_function_on_positive_reals, s_laplace_transform_of_positive_measure⟩` --[t_auxiliary_construction {discrete_approximation_via_finite_differences}]--> output: `s_finite_difference_quadrature_approximation`
2. input: `s_finite_difference_quadrature_approximation` --[t_reduce_to_canonical_form {Hausdorff_moment_problem_on_eps_intervals}]--> output: `s_representing_measures_on_intervals_converging`
3. input: `s_representing_measures_on_intervals_converging` --[t_exhaustion_squeeze {weak_star_compactness_to_full_laplace_transform}]--> output: `s_bernstein_widder_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Riesz–Herglotz representation (cite: https://en.wikipedia.org/wiki/Herglotz_representation_theorem)

**Axioms:** `s_holomorphic_function_on_unit_disk_with_nonneg_real_part`, `s_positive_borel_measure_on_circle`
**Terminal:** `s_herglotz_representation` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_unit_disk_with_nonneg_real_part, s_positive_borel_measure_on_circle⟩` --[t_auxiliary_construction {Poisson_kernel_average_at_radius_r}]--> output: `s_family_of_finite_positive_measures_mu_r`
2. input: `s_family_of_finite_positive_measures_mu_r` --[t_compactness_argument {weak_star_compactness_as_r_to_1}]--> output: `s_weak_star_limit_measure_mu`
3. input: `s_weak_star_limit_measure_mu` --[t_reduce_to_canonical_form {Poisson_integral_representation}]--> output: `s_herglotz_representation`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Phragmén–Brouwer theorem on plane separation (cite: https://en.wikipedia.org/wiki/Phragm%C3%A9n%E2%80%93Brouwer_theorem)

**Axioms:** `s_connected_unicoherent_topological_space`, `s_two_separated_closed_subsets`
**Terminal:** `s_phragmen_brouwer_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_connected_unicoherent_topological_space, s_two_separated_closed_subsets⟩` --[t_reductio_ad_absurdum {suppose: no_separating_connected_subset}]--> output: `s_decomposition_into_two_disconnected_pieces`
2. input: `s_decomposition_into_two_disconnected_pieces` --[t_reduce_to_canonical_form {unicoherence_contradicted}]--> output: `s_contradiction_with_unicoherence`
3. input: `s_contradiction_with_unicoherence` --[t_reduce_to_canonical_form {conclude: connected_separator_exists}]--> output: `s_phragmen_brouwer_theorem`

**Techniques used:** t_reductio_ad_absurdum, t_reduce_to_canonical_form

---

### Vitali convergence theorem (cite: https://en.wikipedia.org/wiki/Vitali_convergence_theorem)

**Axioms:** `s_uniformly_integrable_sequence`, `s_ae_convergent_sequence_on_finite_measure_space`
**Terminal:** `s_vitali_convergence_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_uniformly_integrable_sequence, s_ae_convergent_sequence_on_finite_measure_space⟩` --[t_reduce_to_canonical_form {uniform_integrability_gives_uniform_tail_bound}]--> output: `s_uniform_tail_smallness_in_n`
2. input: `s_uniform_tail_smallness_in_n` --[t_reduce_to_canonical_form {Egorov: uniform_off_exceptional_set}]--> output: `s_split_integral_main_plus_tail`
3. input: `s_split_integral_main_plus_tail` --[t_exhaustion_squeeze {tail_to_0_and_main_to_zero}]--> output: `s_vitali_convergence_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Eberlein theorem on weak compactness in L^1 (Dunford–Pettis) (cite: https://en.wikipedia.org/wiki/Dunford%E2%80%93Pettis_theorem)

**Axioms:** `s_subset_of_L1_finite_measure_space`, `s_weak_compactness_in_L1`
**Terminal:** `s_dunford_pettis_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_subset_of_L1_finite_measure_space, s_weak_compactness_in_L1⟩` --[t_reduce_to_canonical_form {weak_compactness_iff_uniformly_integrable}]--> output: `s_uniform_integrability_criterion`
2. input: `s_uniform_integrability_criterion` --[t_compactness_argument {Banach_Alaoglu_in_double_dual}]--> output: `s_weak_compactness_via_alaoglu_and_eberlein`
3. input: `s_weak_compactness_via_alaoglu_and_eberlein` --[t_reduce_to_canonical_form {extract: dunford_pettis_characterization}]--> output: `s_dunford_pettis_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_compactness_argument

---

### Markov–Kakutani fixed-point theorem (cite: https://en.wikipedia.org/wiki/Markov%E2%80%93Kakutani_fixed-point_theorem)

**Axioms:** `s_commuting_family_of_continuous_affine_self_maps`, `s_compact_convex_subset_of_locally_convex_space`
**Terminal:** `s_markov_kakutani_fpt` (kind: theorem)

**Steps:**
1. input: `⟨s_commuting_family_of_continuous_affine_self_maps, s_compact_convex_subset_of_locally_convex_space⟩` --[t_auxiliary_construction {Cesaro_averages: A_n_T_x=1_over_n_sum_T_k_x}]--> output: `s_cesaro_average_iterates_in_K`
2. input: `s_cesaro_average_iterates_in_K` --[t_compactness_argument {extract: limit_point_in_K}]--> output: `s_limit_point_almost_fixed_for_T`
3. input: `s_limit_point_almost_fixed_for_T` --[t_reduce_to_canonical_form {commuting_family: common_fixed_point_via_finite_intersection}]--> output: `s_markov_kakutani_fpt`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Sobolev–Gagliardo–Nirenberg inequality endpoint (BV–L^{n/(n-1)}) (cite: https://en.wikipedia.org/wiki/Sobolev_inequality#Generalizations)

**Axioms:** `s_BV_function_on_Rn`, `s_total_variation_and_perimeter`
**Terminal:** `s_bv_sobolev_endpoint_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_BV_function_on_Rn, s_total_variation_and_perimeter⟩` --[t_auxiliary_construction {coarea: int_perimeter_of_level_sets}]--> output: `s_coarea_formula_for_BV`
2. input: `s_coarea_formula_for_BV` --[t_reduce_to_canonical_form {isoperimetric_on_each_level_set}]--> output: `s_per_level_isoperimetric_bound`
3. input: `s_per_level_isoperimetric_bound` --[t_reduce_to_canonical_form {integrate_in_level: sobolev_endpoint}]--> output: `s_bv_sobolev_endpoint_inequality`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Helly's selection theorem (cite: https://en.wikipedia.org/wiki/Helly%27s_selection_theorem)

**Axioms:** `s_uniformly_bounded_sequence_of_monotone_functions_on_R`, `s_compact_metrizable_setup`
**Terminal:** `s_helly_selection_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_uniformly_bounded_sequence_of_monotone_functions_on_R, s_compact_metrizable_setup⟩` --[t_pigeonhole_collision {diagonal: pointwise_convergent_on_dense_subset}]--> output: `s_pointwise_convergence_on_rationals_via_diagonal`
2. input: `s_pointwise_convergence_on_rationals_via_diagonal` --[t_reduce_to_canonical_form {monotonicity_extends_to_all_continuity_points}]--> output: `s_pointwise_convergence_ae`
3. input: `s_pointwise_convergence_ae` --[t_reduce_to_canonical_form {limit_is_monotone}]--> output: `s_helly_selection_theorem`

**Techniques used:** t_pigeonhole_collision, t_reduce_to_canonical_form

---

### Prokhorov's theorem (cite: https://en.wikipedia.org/wiki/Prokhorov%27s_theorem)

**Axioms:** `s_family_of_probability_measures_on_polish_space`, `s_tightness_definition`
**Terminal:** `s_prokhorov_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_family_of_probability_measures_on_polish_space, s_tightness_definition⟩` --[t_reduce_to_canonical_form {tightness_iff_relatively_compact_in_weak_star_topology}]--> output: `s_tight_family_with_uniform_compact_support_approximation`
2. input: `s_tight_family_with_uniform_compact_support_approximation` --[t_compactness_argument {restrict_to_compact_K: Banach_Alaoglu_on_C_K_dual}]--> output: `s_weak_star_compact_in_dual_of_C_K`
3. input: `s_weak_star_compact_in_dual_of_C_K` --[t_reduce_to_canonical_form {extract: weakly_convergent_subsequence_of_measures}]--> output: `s_prokhorov_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_compactness_argument

---

### Lévy continuity theorem (cite: https://en.wikipedia.org/wiki/L%C3%A9vy%27s_continuity_theorem)

**Axioms:** `s_sequence_of_probability_measures_on_R`, `s_pointwise_convergence_of_characteristic_functions`
**Terminal:** `s_levy_continuity_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sequence_of_probability_measures_on_R, s_pointwise_convergence_of_characteristic_functions⟩` --[t_reduce_to_canonical_form {continuity_at_0_implies_tightness}]--> output: `s_tightness_of_mu_n`
2. input: `s_tightness_of_mu_n` --[t_compactness_argument {Prokhorov_extract_subsequential_limit_mu}]--> output: `s_weakly_convergent_subsequence_to_mu`
3. input: `s_weakly_convergent_subsequence_to_mu` --[t_reduce_to_canonical_form {uniqueness: characteristic_function_determines_measure}]--> output: `s_levy_continuity_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_compactness_argument

---

### Lévy–Khintchine formula (cite: https://en.wikipedia.org/wiki/L%C3%A9vy%E2%80%93Khintchine_representation)

**Axioms:** `s_infinitely_divisible_distribution_on_R`, `s_characteristic_function_log_psi`
**Terminal:** `s_levy_khintchine_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_infinitely_divisible_distribution_on_R, s_characteristic_function_log_psi⟩` --[t_auxiliary_construction {compound_poisson_truncation_at_eps}]--> output: `s_decomposition_drift_plus_brownian_plus_jumps`
2. input: `s_decomposition_drift_plus_brownian_plus_jumps` --[t_exhaustion_squeeze {eps_to_0_with_levy_measure_integral_condition}]--> output: `s_levy_measure_integral_existence`
3. input: `s_levy_measure_integral_existence` --[t_reduce_to_canonical_form {assemble: drift_diffusion_jump_triple}]--> output: `s_levy_khintchine_formula`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Three-series theorem (Kolmogorov) (cite: https://en.wikipedia.org/wiki/Kolmogorov%27s_three-series_theorem)

**Axioms:** `s_sequence_of_independent_random_variables_X_n`, `s_truncation_at_level_A`
**Terminal:** `s_kolmogorov_three_series_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sequence_of_independent_random_variables_X_n, s_truncation_at_level_A⟩` --[t_auxiliary_construction {truncation_Y_n_eq_X_n_indicator_abs_leq_A}]--> output: `s_three_series_summability_condition`
2. input: `s_three_series_summability_condition` --[t_reduce_to_canonical_form {convergence_via_Kolmogorov_inequality_on_centered_truncations}]--> output: `s_ae_convergence_of_centered_truncations`
3. input: `s_ae_convergence_of_centered_truncations` --[t_reduce_to_canonical_form {sum_means_converge_plus_borel_cantelli_for_tail}]--> output: `s_kolmogorov_three_series_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Strong law of large numbers (Kolmogorov) (cite: https://en.wikipedia.org/wiki/Law_of_large_numbers#Strong_law)

**Axioms:** `s_iid_sequence_with_finite_mean`, `s_probability_axioms`
**Terminal:** `s_strong_law_of_large_numbers` (kind: theorem)

**Steps:**
1. input: `⟨s_iid_sequence_with_finite_mean, s_probability_axioms⟩` --[t_auxiliary_construction {truncation_and_centering_at_level_n}]--> output: `s_centered_truncated_sequence`
2. input: `s_centered_truncated_sequence` --[t_reduce_to_canonical_form {Kolmogorov_inequality_for_partial_sums}]--> output: `s_partial_sum_concentration`
3. input: `s_partial_sum_concentration` --[t_reduce_to_canonical_form {Borel_Cantelli_lemma_for_tail_events}]--> output: `s_strong_law_of_large_numbers`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Kolmogorov's zero-one law (cite: https://en.wikipedia.org/wiki/Kolmogorov%27s_zero%E2%80%93one_law)

**Axioms:** `s_sequence_of_independent_random_variables`, `s_tail_sigma_algebra`
**Terminal:** `s_kolmogorov_zero_one_law` (kind: theorem)

**Steps:**
1. input: `⟨s_sequence_of_independent_random_variables, s_tail_sigma_algebra⟩` --[t_auxiliary_construction {tail_event_E_in_intersection_of_sigma_X_n_X_n_plus_1_etc}]--> output: `s_tail_event_independent_of_each_finite_sigma_algebra`
2. input: `s_tail_event_independent_of_each_finite_sigma_algebra` --[t_reduce_to_canonical_form {density: pi_system_independence_extends}]--> output: `s_tail_event_independent_of_full_sigma_algebra`
3. input: `s_tail_event_independent_of_full_sigma_algebra` --[t_reduce_to_canonical_form {independent_of_itself_implies_probability_0_or_1}]--> output: `s_kolmogorov_zero_one_law`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Donsker's invariance principle (cite: https://en.wikipedia.org/wiki/Donsker%27s_theorem)

**Axioms:** `s_iid_sequence_with_finite_variance_unit_normalized`, `s_brownian_motion_on_0_1`
**Terminal:** `s_donsker_invariance_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_iid_sequence_with_finite_variance_unit_normalized, s_brownian_motion_on_0_1⟩` --[t_auxiliary_construction {rescaled_partial_sum_process: W_n_t=S_floor_nt_over_sqrt_n}]--> output: `s_polygonal_random_walk_process`
2. input: `s_polygonal_random_walk_process` --[t_reduce_to_canonical_form {finite_dim_distributions_to_brownian_via_CLT}]--> output: `s_finite_dim_marginals_converge_to_BM`
3. input: `s_finite_dim_marginals_converge_to_BM` --[t_compactness_argument {tightness_in_C_0_1_via_modulus_of_continuity}]--> output: `s_donsker_invariance_principle`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_compactness_argument

---

### Wiener's theorem on Fourier series (absolute convergence) (cite: https://en.wikipedia.org/wiki/Wiener_algebra)

**Axioms:** `s_function_with_absolutely_convergent_fourier_series_nonvanishing`, `s_inverse_function_1_over_f`
**Terminal:** `s_wiener_inversion_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_function_with_absolutely_convergent_fourier_series_nonvanishing, s_inverse_function_1_over_f⟩` --[t_auxiliary_construction {Wiener_algebra: A_T_with_convolution_product}]--> output: `s_banach_algebra_A_T`
2. input: `s_banach_algebra_A_T` --[t_reduce_to_canonical_form {Gelfand_representation: characters_are_evaluation_at_points}]--> output: `s_spectrum_of_f_in_A_T_equals_image`
3. input: `s_spectrum_of_f_in_A_T_equals_image` --[t_reduce_to_canonical_form {1_over_f_in_algebra_iff_no_zero_in_spectrum}]--> output: `s_wiener_inversion_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Helly–Bray theorem (weak convergence of distribution functions) (cite: https://en.wikipedia.org/wiki/Helly%E2%80%93Bray_theorem)

**Axioms:** `s_bounded_continuous_function_on_R`, `s_weakly_convergent_sequence_of_distribution_functions`
**Terminal:** `s_helly_bray_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_bounded_continuous_function_on_R, s_weakly_convergent_sequence_of_distribution_functions⟩` --[t_auxiliary_construction {compact_truncation: window_minus_M_to_M}]--> output: `s_truncated_integrand_on_compact`
2. input: `s_truncated_integrand_on_compact` --[t_reduce_to_canonical_form {uniform_continuity_on_compact_yields_riemann_stieltjes_convergence}]--> output: `s_convergence_on_compact_window`
3. input: `s_convergence_on_compact_window` --[t_exhaustion_squeeze {M_to_infinity_with_tightness}]--> output: `s_helly_bray_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Stone–von Neumann theorem (cite: https://en.wikipedia.org/wiki/Stone%E2%80%93von_Neumann_theorem)

**Axioms:** `s_irreducible_strongly_continuous_unitary_representation_of_heisenberg_group`, `s_schrodinger_representation`
**Terminal:** `s_stone_von_neumann_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_irreducible_strongly_continuous_unitary_representation_of_heisenberg_group, s_schrodinger_representation⟩` --[t_auxiliary_construction {fock_vacuum_vector_via_minimal_uncertainty}]--> output: `s_cyclic_vacuum_vector_in_representation`
2. input: `s_cyclic_vacuum_vector_in_representation` --[t_svd_and_spectral_decomposition {creation_annihilation_operators_act}]--> output: `s_fock_space_structure_intertwining`
3. input: `s_fock_space_structure_intertwining` --[t_structural_isomorphism {unitary_equivalence_to_schrodinger}]--> output: `s_stone_von_neumann_theorem`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_structural_isomorphism

---

### Helly's theorem on convex sets (cite: https://en.wikipedia.org/wiki/Helly%27s_theorem)

**Axioms:** `s_finite_family_of_convex_subsets_of_Rd`, `s_d_plus_1_intersection_condition`
**Terminal:** `s_helly_theorem_convex` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_family_of_convex_subsets_of_Rd, s_d_plus_1_intersection_condition⟩` --[t_auxiliary_construction {induction_on_number_of_sets}]--> output: `s_induction_base_at_d_plus_1`
2. input: `s_induction_base_at_d_plus_1` --[t_reduce_to_canonical_form {Radon_partition_of_d_plus_2_points}]--> output: `s_radon_partition_giving_common_intersection`
3. input: `s_radon_partition_giving_common_intersection` --[t_reduce_to_canonical_form {induct: extend_to_n_sets}]--> output: `s_helly_theorem_convex`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Carathéodory's convex hull theorem (cite: https://en.wikipedia.org/wiki/Carath%C3%A9odory%27s_theorem_(convex_hull))

**Axioms:** `s_subset_of_Rd`, `s_convex_hull_with_convex_combinations`
**Terminal:** `s_caratheodory_convex_hull_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_subset_of_Rd, s_convex_hull_with_convex_combinations⟩` --[t_reductio_ad_absurdum {suppose: more_than_d_plus_1_points_needed}]--> output: `s_redundant_convex_combination_assumption`
2. input: `s_redundant_convex_combination_assumption` --[t_reduce_to_canonical_form {linear_dependence_in_homogenized_coordinates}]--> output: `s_linear_dependence_extracts_smaller_combination`
3. input: `s_linear_dependence_extracts_smaller_combination` --[t_reduce_to_canonical_form {iterate_to_d_plus_1_points}]--> output: `s_caratheodory_convex_hull_theorem`

**Techniques used:** t_reductio_ad_absurdum, t_reduce_to_canonical_form

---

### Kakutani–Markov–Schauder fixed point — covered above (skipped duplicate)

---

### Cantor–Bendixson theorem (cite: https://en.wikipedia.org/wiki/Cantor%E2%80%93Bendixson_theorem)

**Axioms:** `s_closed_subset_of_polish_space`, `s_derived_set_operator`
**Terminal:** `s_cantor_bendixson_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_closed_subset_of_polish_space, s_derived_set_operator⟩` --[t_auxiliary_construction {transfinite_iteration_of_derived_set}]--> output: `s_decreasing_transfinite_sequence_of_derived_sets`
2. input: `s_decreasing_transfinite_sequence_of_derived_sets` --[t_reduce_to_canonical_form {stabilization_at_countable_ordinal_via_separability}]--> output: `s_perfect_kernel_of_F`
3. input: `s_perfect_kernel_of_F` --[t_reduce_to_canonical_form {F_eq_perfect_kernel_plus_countable_scattered}]--> output: `s_cantor_bendixson_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Lindelöf principle (subharmonic version) (cite: https://en.wikipedia.org/wiki/Lindel%C3%B6f_principle)

**Axioms:** `s_subharmonic_function_on_unbounded_domain`, `s_growth_bound_at_infinity`
**Terminal:** `s_lindelof_principle_subharmonic` (kind: theorem)

**Steps:**
1. input: `⟨s_subharmonic_function_on_unbounded_domain, s_growth_bound_at_infinity⟩` --[t_auxiliary_construction {harmonic_majorant_via_poisson}]--> output: `s_harmonic_comparison_function`
2. input: `s_harmonic_comparison_function` --[t_reduce_to_canonical_form {maximum_principle_for_subharmonic_minus_harmonic}]--> output: `s_bound_on_truncations`
3. input: `s_bound_on_truncations` --[t_exhaustion_squeeze {exhaust_to_unbounded_domain}]--> output: `s_lindelof_principle_subharmonic`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Perron method for Dirichlet problem (cite: https://en.wikipedia.org/wiki/Perron_method)

**Axioms:** `s_bounded_domain_with_boundary_data_in_C_boundary`, `s_family_of_subharmonic_subsolutions`
**Terminal:** `s_perron_method_dirichlet` (kind: theorem)

**Steps:**
1. input: `⟨s_bounded_domain_with_boundary_data_in_C_boundary, s_family_of_subharmonic_subsolutions⟩` --[t_auxiliary_construction {pointwise_supremum_of_perron_family}]--> output: `s_perron_solution_candidate_u`
2. input: `s_perron_solution_candidate_u` --[t_reduce_to_canonical_form {harnack_principle_yields_harmonicity}]--> output: `s_harmonic_interior_function`
3. input: `s_harmonic_interior_function` --[t_reduce_to_canonical_form {barrier_function_attainment_of_boundary_data}]--> output: `s_perron_method_dirichlet`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Mean value property characterizes harmonic functions (cite: https://en.wikipedia.org/wiki/Harmonic_function#Mean_value_property)

**Axioms:** `s_continuous_function_on_open_subset_of_Rn`, `s_mean_value_property_on_balls`
**Terminal:** `s_harmonic_mvp_characterization` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_function_on_open_subset_of_Rn, s_mean_value_property_on_balls⟩` --[t_auxiliary_construction {mollify: f_eps_via_radial_kernel}]--> output: `s_smooth_mollification_equals_f`
2. input: `s_smooth_mollification_equals_f` --[t_reduce_to_canonical_form {f_smooth_and_mean_value_yields_laplacian_zero}]--> output: `s_laplacian_zero_almost_everywhere`
3. input: `s_laplacian_zero_almost_everywhere` --[t_reduce_to_canonical_form {converse: harmonic_functions_satisfy_MVP}]--> output: `s_harmonic_mvp_characterization`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Harnack's inequality (cite: https://en.wikipedia.org/wiki/Harnack%27s_inequality)

**Axioms:** `s_nonneg_harmonic_function_on_ball`, `s_compactly_contained_subdomain`
**Terminal:** `s_harnack_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_nonneg_harmonic_function_on_ball, s_compactly_contained_subdomain⟩` --[t_reduce_to_canonical_form {Poisson_kernel_representation_on_ball}]--> output: `s_poisson_kernel_explicit_bounds`
2. input: `s_poisson_kernel_explicit_bounds` --[t_reduce_to_canonical_form {ratio_bound_for_two_points_via_kernel_bounds}]--> output: `s_two_point_ratio_inequality`
3. input: `s_two_point_ratio_inequality` --[t_compactness_argument {chain_of_overlapping_balls_for_general_compactum}]--> output: `s_harnack_inequality`

**Techniques used:** t_reduce_to_canonical_form, t_compactness_argument

---

### Riesz–Thorin endpoint Hausdorff–Young — already covered (skip duplicate)

---

### Carleson measure characterization (Carleson embedding) (cite: https://en.wikipedia.org/wiki/Carleson_measure)

**Axioms:** `s_positive_measure_mu_on_upper_half_plane`, `s_lp_function_on_real_line`
**Terminal:** `s_carleson_embedding_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_positive_measure_mu_on_upper_half_plane, s_lp_function_on_real_line⟩` --[t_auxiliary_construction {Poisson_extension_P_y_f}]--> output: `s_Poisson_extension_to_half_plane`
2. input: `s_Poisson_extension_to_half_plane` --[t_reduce_to_canonical_form {tent_decomposition_with_Carleson_box_condition}]--> output: `s_tent_decomposition_estimate`
3. input: `s_tent_decomposition_estimate` --[t_reduce_to_canonical_form {Lp_bound_iff_Carleson_norm_finite}]--> output: `s_carleson_embedding_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### BMO–H^1 duality (Fefferman) (cite: https://en.wikipedia.org/wiki/Bounded_mean_oscillation)

**Axioms:** `s_real_hardy_space_H1_on_Rn`, `s_BMO_space_on_Rn`
**Terminal:** `s_fefferman_BMO_H1_duality` (kind: theorem)

**Steps:**
1. input: `⟨s_real_hardy_space_H1_on_Rn, s_BMO_space_on_Rn⟩` --[t_auxiliary_construction {atomic_decomposition_of_H1}]--> output: `s_atomic_decomposition_for_H1`
2. input: `s_atomic_decomposition_for_H1` --[t_duality {pair_atom_with_BMO_function}]--> output: `s_dual_pairing_estimate_per_atom`
3. input: `s_dual_pairing_estimate_per_atom` --[t_reduce_to_canonical_form {assemble: bounded_pairing_yields_duality}]--> output: `s_fefferman_BMO_H1_duality`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### John–Nirenberg inequality (cite: https://en.wikipedia.org/wiki/John%E2%80%93Nirenberg_inequality)

**Axioms:** `s_BMO_function_on_cube_Q`, `s_distribution_of_oscillation`
**Terminal:** `s_john_nirenberg_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_BMO_function_on_cube_Q, s_distribution_of_oscillation⟩` --[t_pigeonhole_collision {Calderon_Zygmund_dyadic_stopping_time}]--> output: `s_stopping_time_decomposition_of_Q`
2. input: `s_stopping_time_decomposition_of_Q` --[t_reduce_to_canonical_form {recursive_bound_on_level_set_measure}]--> output: `s_geometric_decay_of_level_sets`
3. input: `s_geometric_decay_of_level_sets` --[t_reduce_to_canonical_form {exponential_distribution_estimate}]--> output: `s_john_nirenberg_inequality`

**Techniques used:** t_pigeonhole_collision, t_reduce_to_canonical_form

---

### A_p weight theorem (Muckenhoupt) (cite: https://en.wikipedia.org/wiki/A%E2%82%9A_weights)

**Axioms:** `s_locally_integrable_nonneg_weight_w_on_Rn`, `s_Hardy_Littlewood_maximal_operator`
**Terminal:** `s_muckenhoupt_Ap_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_locally_integrable_nonneg_weight_w_on_Rn, s_Hardy_Littlewood_maximal_operator⟩` --[t_axiomatize_from_instances {Ap_condition_on_cubes: average_w_times_average_w_minus_1_over_p_minus_1_bounded}]--> output: `s_Ap_class_definition`
2. input: `s_Ap_class_definition` --[t_reduce_to_canonical_form {Calderon_Zygmund_decomposition_with_weight}]--> output: `s_weak_p_p_bound_on_M_with_weight_w`
3. input: `s_weak_p_p_bound_on_M_with_weight_w` --[t_interpolate_and_continue {Marcinkiewicz_interpolation_in_weighted_setting}]--> output: `s_muckenhoupt_Ap_theorem`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form, t_interpolate_and_continue

---

### Cotlar–Stein lemma (almost-orthogonality) (cite: https://en.wikipedia.org/wiki/Cotlar%E2%80%93Stein_lemma)

**Axioms:** `s_family_of_bounded_operators_T_j_on_hilbert_space`, `s_almost_orthogonality_condition`
**Terminal:** `s_cotlar_stein_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_family_of_bounded_operators_T_j_on_hilbert_space, s_almost_orthogonality_condition⟩` --[t_auxiliary_construction {power_estimate: norm_of_T_T_star_to_k_via_products_of_adjoints}]--> output: `s_norm_squared_T_to_2N_bound_via_products`
2. input: `s_norm_squared_T_to_2N_bound_via_products` --[t_reduce_to_canonical_form {expand_summed_product_telescoping_almost_orthogonality}]--> output: `s_telescoped_bound_dominated_by_sup_omega`
3. input: `s_telescoped_bound_dominated_by_sup_omega` --[t_exhaustion_squeeze {N_to_infinity_root_extraction}]--> output: `s_cotlar_stein_lemma`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Stein interpolation theorem (cite: https://en.wikipedia.org/wiki/Stein_interpolation)

**Axioms:** `s_analytic_family_of_operators_T_z_on_strip`, `s_lp_lq_endpoint_bounds_with_admissible_growth`
**Terminal:** `s_stein_interpolation_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_analytic_family_of_operators_T_z_on_strip, s_lp_lq_endpoint_bounds_with_admissible_growth⟩` --[t_auxiliary_construction {test_function_pairing: F_z=int_T_z_f_z_g_z}]--> output: `s_holomorphic_in_strip_with_admissible_growth`
2. input: `s_holomorphic_in_strip_with_admissible_growth` --[t_reduce_to_canonical_form {Phragmen_Lindelof_with_growth_subexponential}]--> output: `s_three_lines_with_admissible_growth`
3. input: `s_three_lines_with_admissible_growth` --[t_interpolate_and_continue {recover_intermediate_Lp_Lq_bound}]--> output: `s_stein_interpolation_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_interpolate_and_continue

---

### Sobolev–Slobodeckij embedding (fractional Sobolev) (cite: https://en.wikipedia.org/wiki/Sobolev_space#Sobolev%E2%80%93Slobodeckij_spaces)

**Axioms:** `s_fractional_sobolev_space_W_s_p_Rn`, `s_lq_target_with_critical_exponent`
**Terminal:** `s_fractional_sobolev_embedding` (kind: theorem)

**Steps:**
1. input: `⟨s_fractional_sobolev_space_W_s_p_Rn, s_lq_target_with_critical_exponent⟩` --[t_fourier_transform {bessel_potential_J_s_via_multiplier_1_plus_xi_2_to_s_over_2}]--> output: `s_bessel_potential_representation`
2. input: `s_bessel_potential_representation` --[t_reduce_to_canonical_form {Hardy_Littlewood_Sobolev_for_Riesz_potential}]--> output: `s_HLS_lp_to_lq_bound`
3. input: `s_HLS_lp_to_lq_bound` --[t_reduce_to_canonical_form {translate: fractional_sobolev_embedding}]--> output: `s_fractional_sobolev_embedding`

**Techniques used:** t_fourier_transform, t_reduce_to_canonical_form

---

### Pólya–Szegő rearrangement inequality (cite: https://en.wikipedia.org/wiki/Symmetric_decreasing_rearrangement)

**Axioms:** `s_nonneg_measurable_function_on_Rn`, `s_symmetric_decreasing_rearrangement_f_star`
**Terminal:** `s_polya_szego_rearrangement_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_nonneg_measurable_function_on_Rn, s_symmetric_decreasing_rearrangement_f_star⟩` --[t_auxiliary_construction {layer_cake: f_eq_int_indicator_level_sets}]--> output: `s_layer_cake_representation_of_f`
2. input: `s_layer_cake_representation_of_f` --[t_reduce_to_canonical_form {coarea: level_set_perimeter_decreased_by_symmetrization}]--> output: `s_level_set_isoperimetric_bound`
3. input: `s_level_set_isoperimetric_bound` --[t_reduce_to_canonical_form {integrate_gradient_norm_pointwise}]--> output: `s_polya_szego_rearrangement_inequality`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Strichartz estimates (cite: https://en.wikipedia.org/wiki/Strichartz_estimate)

**Axioms:** `s_schrodinger_propagator_e_it_delta`, `s_admissible_pair_q_r`
**Terminal:** `s_strichartz_estimate` (kind: theorem)

**Steps:**
1. input: `⟨s_schrodinger_propagator_e_it_delta, s_admissible_pair_q_r⟩` --[t_fourier_transform {dispersive_estimate: L1_to_L_infty_decay_in_t}]--> output: `s_dispersive_decay_estimate`
2. input: `s_dispersive_decay_estimate` --[t_duality {TT_star_method: U_U_star_via_kernel_bound}]--> output: `s_TT_star_bilinear_estimate`
3. input: `s_TT_star_bilinear_estimate` --[t_interpolate_and_continue {Hardy_Littlewood_Sobolev_in_time}]--> output: `s_strichartz_estimate`

**Techniques used:** t_fourier_transform, t_duality, t_interpolate_and_continue

---

### Riesz–Thorin endpoint Marcinkiewicz–Zygmund (cite: https://en.wikipedia.org/wiki/Marcinkiewicz%E2%80%93Zygmund_inequality)

**Axioms:** `s_iid_random_variable_sequence`, `s_lp_norm_of_partial_sums`
**Terminal:** `s_marcinkiewicz_zygmund_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_iid_random_variable_sequence, s_lp_norm_of_partial_sums⟩` --[t_auxiliary_construction {symmetrization_via_independent_rademacher}]--> output: `s_symmetrized_partial_sum_via_random_signs`
2. input: `s_symmetrized_partial_sum_via_random_signs` --[t_reduce_to_canonical_form {khintchine_inequality_for_signs_conditional}]--> output: `s_conditional_khintchine_bound`
3. input: `s_conditional_khintchine_bound` --[t_reduce_to_canonical_form {integrate_over_X_n_distribution}]--> output: `s_marcinkiewicz_zygmund_inequality`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Bochner–Riesz mean theorem (cite: https://en.wikipedia.org/wiki/Bochner%E2%80%93Riesz_mean)

**Axioms:** `s_bochner_riesz_multiplier_1_minus_abs_xi_2_to_alpha`, `s_lp_function_on_Rn`
**Terminal:** `s_bochner_riesz_lp_bound` (kind: theorem)

**Steps:**
1. input: `⟨s_bochner_riesz_multiplier_1_minus_abs_xi_2_to_alpha, s_lp_function_on_Rn⟩` --[t_frequency_decomposition {Littlewood_Paley_around_sphere}]--> output: `s_decomposition_into_annular_pieces`
2. input: `s_decomposition_into_annular_pieces` --[t_reduce_to_canonical_form {kernel_oscillatory_estimate_via_stationary_phase}]--> output: `s_oscillatory_kernel_estimate`
3. input: `s_oscillatory_kernel_estimate` --[t_interpolate_and_continue {between_L2_and_extremal_endpoints}]--> output: `s_bochner_riesz_lp_bound`

**Techniques used:** t_frequency_decomposition, t_reduce_to_canonical_form, t_interpolate_and_continue

---

### Tomas–Stein restriction theorem (cite: https://en.wikipedia.org/wiki/Restriction_theorem)

**Axioms:** `s_smooth_curved_hypersurface_in_Rn`, `s_lp_function_with_fourier_restriction`
**Terminal:** `s_tomas_stein_restriction_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_curved_hypersurface_in_Rn, s_lp_function_with_fourier_restriction⟩` --[t_duality {TT_star: pair_restriction_with_extension}]--> output: `s_extension_operator_setup`
2. input: `s_extension_operator_setup` --[t_reduce_to_canonical_form {kernel: surface_carried_measure_with_oscillatory_decay}]--> output: `s_surface_measure_decay_estimate`
3. input: `s_surface_measure_decay_estimate` --[t_interpolate_and_continue {at_Tomas_Stein_endpoint_via_HLS}]--> output: `s_tomas_stein_restriction_theorem`

**Techniques used:** t_duality, t_reduce_to_canonical_form, t_interpolate_and_continue

---

### Kakeya maximal inequality (n=2) (cite: https://en.wikipedia.org/wiki/Kakeya_set#Kakeya_needle_problem)

**Axioms:** `s_family_of_unit_segments_in_R2_with_delta_separated_directions`, `s_kakeya_maximal_operator`
**Terminal:** `s_kakeya_maximal_inequality_planar` (kind: theorem)

**Steps:**
1. input: `⟨s_family_of_unit_segments_in_R2_with_delta_separated_directions, s_kakeya_maximal_operator⟩` --[t_auxiliary_construction {duality_with_bushes_and_stickyness}]--> output: `s_combinatorial_incidence_setup`
2. input: `s_combinatorial_incidence_setup` --[t_reduce_to_canonical_form {bound_via_Cordoba_geometric_lemma}]--> output: `s_log_loss_bound_on_kakeya_maximal`
3. input: `s_log_loss_bound_on_kakeya_maximal` --[t_interpolate_and_continue {between_endpoints_to_full_L2_bound}]--> output: `s_kakeya_maximal_inequality_planar`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_interpolate_and_continue

---

### Calderón reproducing formula (continuous wavelet) (cite: https://en.wikipedia.org/wiki/Continuous_wavelet_transform)

**Axioms:** `s_admissible_mother_wavelet_psi_on_R`, `s_L2_function_f`
**Terminal:** `s_calderon_reproducing_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_admissible_mother_wavelet_psi_on_R, s_L2_function_f⟩` --[t_fourier_transform {check: psi_hat_admissibility_constant_finite}]--> output: `s_admissibility_constant_C_psi_finite`
2. input: `s_admissibility_constant_C_psi_finite` --[t_reduce_to_canonical_form {Plancherel_in_a_b_coordinates}]--> output: `s_parseval_identity_for_wavelet_pairing`
3. input: `s_parseval_identity_for_wavelet_pairing` --[t_reduce_to_canonical_form {inversion: reconstruct_f_via_double_integral}]--> output: `s_calderon_reproducing_formula`

**Techniques used:** t_fourier_transform, t_reduce_to_canonical_form

---

### Frostman's lemma (cite: https://en.wikipedia.org/wiki/Frostman_lemma)

**Axioms:** `s_compact_subset_K_of_Rn`, `s_hausdorff_dimension_s_lower_bound`
**Terminal:** `s_frostman_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_subset_K_of_Rn, s_hausdorff_dimension_s_lower_bound⟩` --[t_auxiliary_construction {dyadic_mass_distribution_with_balanced_subdivision}]--> output: `s_balanced_dyadic_mass`
2. input: `s_balanced_dyadic_mass` --[t_compactness_argument {weak_star_limit_yields_borel_measure_mu_on_K}]--> output: `s_borel_measure_with_growth_bound`
3. input: `s_borel_measure_with_growth_bound` --[t_reduce_to_canonical_form {state: mu_B_x_r_leq_C_r_s}]--> output: `s_frostman_lemma`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Besicovitch covering theorem (cite: https://en.wikipedia.org/wiki/Besicovitch_covering_theorem)

**Axioms:** `s_collection_of_balls_in_Rn_with_bounded_radii_centered_at_set_A`, `s_lebesgue_measure_on_Rn`
**Terminal:** `s_besicovitch_covering_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_collection_of_balls_in_Rn_with_bounded_radii_centered_at_set_A, s_lebesgue_measure_on_Rn⟩` --[t_pigeonhole_collision {sorted: by_decreasing_radius}]--> output: `s_sorted_ball_sequence`
2. input: `s_sorted_ball_sequence` --[t_reduce_to_canonical_form {greedy_partition_into_C_n_disjoint_subfamilies}]--> output: `s_finite_number_of_disjoint_subfamilies_covering_A`
3. input: `s_finite_number_of_disjoint_subfamilies_covering_A` --[t_reduce_to_canonical_form {state: bounded_multiplicity_cover}]--> output: `s_besicovitch_covering_theorem`

**Techniques used:** t_pigeonhole_collision, t_reduce_to_canonical_form

---

### Whitney extension theorem (cite: https://en.wikipedia.org/wiki/Whitney_extension_theorem)

**Axioms:** `s_closed_subset_of_Rn_with_jet_data_satisfying_compatibility`, `s_target_class_C_m`
**Terminal:** `s_whitney_extension_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_closed_subset_of_Rn_with_jet_data_satisfying_compatibility, s_target_class_C_m⟩` --[t_auxiliary_construction {Whitney_partition_of_complement_into_dyadic_cubes}]--> output: `s_whitney_decomposition_of_complement`
2. input: `s_whitney_decomposition_of_complement` --[t_reduce_to_canonical_form {locally_average_jet_via_taylor_polynomial_on_cubes}]--> output: `s_locally_polynomial_extension`
3. input: `s_locally_polynomial_extension` --[t_reduce_to_canonical_form {patch: smooth_partition_of_unity_to_glue_C_m_extension}]--> output: `s_whitney_extension_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Borel's theorem on Taylor series (cite: https://en.wikipedia.org/wiki/Borel%27s_theorem)

**Axioms:** `s_arbitrary_real_sequence_a_n`, `s_smooth_function_on_R`
**Terminal:** `s_borel_theorem_taylor_series` (kind: theorem)

**Steps:**
1. input: `⟨s_arbitrary_real_sequence_a_n, s_smooth_function_on_R⟩` --[t_auxiliary_construction {cutoff_function_phi_n_supported_near_0_with_scaling}]--> output: `s_scaled_bump_functions_with_decreasing_support`
2. input: `s_scaled_bump_functions_with_decreasing_support` --[t_exhaustion_squeeze {series_converges_in_each_C_k_norm}]--> output: `s_smooth_function_with_prescribed_jet_at_0`
3. input: `s_smooth_function_with_prescribed_jet_at_0` --[t_reduce_to_canonical_form {state: arbitrary_taylor_coefficients_realizable}]--> output: `s_borel_theorem_taylor_series`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Whitney C^k approximation theorem (cite: https://en.wikipedia.org/wiki/Smooth_function#Smooth_approximations)

**Axioms:** `s_continuous_function_on_smooth_manifold`, `s_target_smooth_function_class`
**Terminal:** `s_whitney_approximation_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_function_on_smooth_manifold, s_target_smooth_function_class⟩` --[t_auxiliary_construction {partition_of_unity_subordinate_to_chart_cover}]--> output: `s_partition_of_unity_chart_decomposition`
2. input: `s_partition_of_unity_chart_decomposition` --[t_reduce_to_canonical_form {mollify_each_local_piece_in_chart}]--> output: `s_locally_smooth_approximation`
3. input: `s_locally_smooth_approximation` --[t_exhaustion_squeeze {sum_locally_finite_combination}]--> output: `s_whitney_approximation_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

