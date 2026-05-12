# Area AN2 (Real & Complex Analysis) Derivation Chains — Supplement (iter-3)

**Source pages:**
- https://en.wikipedia.org/wiki/Category:Theorems_in_real_analysis
- https://en.wikipedia.org/wiki/Category:Theorems_in_complex_analysis
- https://en.wikipedia.org/wiki/Category:Theorems_in_harmonic_analysis
- https://en.wikipedia.org/wiki/Category:Theorems_in_measure_theory
- https://en.wikipedia.org/wiki/Category:Theorems_in_functional_analysis

**Target:** ~60 supplementary chains (to bring AN coverage past 100 with `area_AN_chains.md`'s 40 already drafted). **Drafted:** 63.
**Already in `area_AN_chains.md` (do NOT re-derive here):** Bolzano–Weierstrass, Heine–Borel, IVT, EVT, MVT, Cauchy MVT, L'Hôpital, Darboux, Cantor intersection, Baire, Banach–Steinhaus, Open mapping (FA), Closed graph, Arzelà–Ascoli, Stone–Weierstrass, Tietze, Urysohn lemma, Urysohn metrization, Dini, Carathéodory ext, MCT, Fatou, DCT, Egorov, Lusin, Radon–Nikodym, Riesz–Markov, Lebesgue differentiation, Vitali covering, Vitali–Hahn–Saks, Fubini, Tonelli, Lebesgue monotone differentiation, Rademacher, Sard, Riesz rep L^p, Hardy–Littlewood maximal, Fefferman–Stein vector-valued, Calderón–Zygmund decomposition, Calderón–Zygmund Lp.
**Skipped (already in canonical graph):** `s_taylor_theorem`, `s_cauchy_integral_formula`, `s_riemann_mapping_theorem`, `s_hahn_banach`, `s_weierstrass_approximation`, `s_fundamental_theorem_of_calculus`, `s_banach_fpt`, `s_birkhoff_ergodic_theorem`, `s_central_limit_theorem`, `s_basel_identity`, `s_fourier_theorem_heat`.
**Flagged (`⚠ needs new technique`):** 4 — Carleson a.e. convergence (time-frequency tile decomposition), Lebesgue density theorem (maximal-function ae conv. primitive), Hadamard factorization (canonical product machinery), Mergelyan's theorem (rational-approximation Vitushkin machinery).

---

## III. Inequalities and L^p geometry

### Hölder's inequality (cite: https://en.wikipedia.org/wiki/H%C3%B6lder%27s_inequality)

**Axioms:** `s_measure_space`, `s_conjugate_exponents_p_q`
**Terminal:** `s_holder_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_space, s_conjugate_exponents_p_q⟩` --[t_auxiliary_construction {pointwise: Young_ab_leq_ap_over_p_plus_bq_over_q}]--> output: `s_pointwise_young_inequality`
2. input: `s_pointwise_young_inequality` --[t_reduce_to_canonical_form {normalize: by_norms_||f||_p_and_||g||_q}]--> output: `s_normalized_pointwise_bound`
3. input: `s_normalized_pointwise_bound` --[t_exhaustion_squeeze {integrate: sum_to_one}]--> output: `s_holder_inequality`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Minkowski's inequality (cite: https://en.wikipedia.org/wiki/Minkowski_inequality)

**Axioms:** `s_measure_space`, `s_lp_function_pair`
**Terminal:** `s_minkowski_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_space, s_lp_function_pair⟩` --[t_auxiliary_construction {expand: |f+g|^p_leq_|f+g|^{p-1}(|f|+|g|)}]--> output: `s_pointwise_split_of_pth_power`
2. input: `s_pointwise_split_of_pth_power` --[t_duality {apply: Holder_with_conjugate_q=p/(p-1)}]--> output: `s_two_holder_bounds_on_each_term`
3. input: `s_two_holder_bounds_on_each_term` --[t_reduce_to_canonical_form {divide: by_||f+g||_p^{p-1}}]--> output: `s_minkowski_inequality`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Jensen's inequality (cite: https://en.wikipedia.org/wiki/Jensen%27s_inequality)

**Axioms:** `s_probability_axioms`, `s_convex_function_phi`
**Terminal:** `s_jensen_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms, s_convex_function_phi⟩` --[t_auxiliary_construction {tangent: affine_supporting_line_at_E[X]}]--> output: `s_supporting_affine_minorant_of_phi`
2. input: `s_supporting_affine_minorant_of_phi` --[t_reduce_to_canonical_form {integrate: against_probability_measure}]--> output: `s_jensen_inequality`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Young's convolution inequality (cite: https://en.wikipedia.org/wiki/Young%27s_convolution_inequality)

**Axioms:** `s_lebesgue_measure_on_Rn`, `s_lp_lq_pair_with_1+1/r=1/p+1/q`
**Terminal:** `s_young_convolution_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_lebesgue_measure_on_Rn, s_lp_lq_pair_with_1+1/r=1/p+1/q⟩` --[t_auxiliary_construction {split: triple_holder_in_three_factors}]--> output: `s_three_factor_decomposition_of_kernel`
2. input: `s_three_factor_decomposition_of_kernel` --[t_duality {apply: generalized_Holder_three_factors}]--> output: `s_pointwise_bound_for_convolution`
3. input: `s_pointwise_bound_for_convolution` --[t_reduce_to_canonical_form {integrate: in_x_via_Fubini}]--> output: `s_young_convolution_inequality`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Hardy's inequality (continuous) (cite: https://en.wikipedia.org/wiki/Hardy%27s_inequality)

**Axioms:** `s_lebesgue_measure_on_R_plus`, `s_lp_function_on_R_plus`
**Terminal:** `s_hardy_inequality_continuous` (kind: theorem)

**Steps:**
1. input: `⟨s_lebesgue_measure_on_R_plus, s_lp_function_on_R_plus⟩` --[t_auxiliary_construction {operator: (Hf)(x)=x^{-1}int_0^x_f}]--> output: `s_hardy_averaging_operator`
2. input: `s_hardy_averaging_operator` --[t_rescale_for_asymptotic_geometry {scale: x_to_lambda_x_invariance}]--> output: `s_scale_invariant_kernel`
3. input: `s_scale_invariant_kernel` --[t_duality {via: Schur_test_with_weight_x^{-1/p}}]--> output: `s_hardy_inequality_continuous`

**Techniques used:** t_auxiliary_construction, t_rescale_for_asymptotic_geometry, t_duality

---

### Hardy's inequality (discrete) (cite: https://en.wikipedia.org/wiki/Hardy%27s_inequality)

**Axioms:** `s_lp_sequence`, `s_natural_numbers`
**Terminal:** `s_hardy_inequality_discrete` (kind: theorem)

**Steps:**
1. input: `⟨s_lp_sequence, s_natural_numbers⟩` --[t_auxiliary_construction {average: A_n=1/n_sum_a_k}]--> output: `s_discrete_averaging_sequence`
2. input: `s_discrete_averaging_sequence` --[t_duality {summation_by_parts: pair_with_test_sequence}]--> output: `s_dual_pairing_with_test_sequence`
3. input: `s_dual_pairing_with_test_sequence` --[t_reduce_to_canonical_form {bound: factor_p/(p-1)}]--> output: `s_hardy_inequality_discrete`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Hilbert's inequality (cite: https://en.wikipedia.org/wiki/Hilbert%27s_inequality)

**Axioms:** `s_lp_sequence`, `s_kernel_1_over_m_plus_n`
**Terminal:** `s_hilbert_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_lp_sequence, s_kernel_1_over_m_plus_n⟩` --[t_auxiliary_construction {bilinear: B(a,b)=sum_a_m_b_n/(m+n)}]--> output: `s_bilinear_form_kernel_diagonal`
2. input: `s_bilinear_form_kernel_diagonal` --[t_rescale_for_asymptotic_geometry {homogeneous: degree_minus_1_kernel}]--> output: `s_homogeneous_degree_minus_one`
3. input: `s_homogeneous_degree_minus_one` --[t_duality {Schur_test: weight_m^{-1/p}}]--> output: `s_hilbert_inequality`

**Techniques used:** t_auxiliary_construction, t_rescale_for_asymptotic_geometry, t_duality

---

### Carleman's inequality (cite: https://en.wikipedia.org/wiki/Carleman%27s_inequality)

**Axioms:** `s_l1_positive_sequence`, `s_natural_numbers`
**Terminal:** `s_carleman_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_l1_positive_sequence, s_natural_numbers⟩` --[t_auxiliary_construction {weight: b_k=k_a_k_times_(k+1)^k/k!}]--> output: `s_weighted_substitution_for_GM`
2. input: `s_weighted_substitution_for_GM` --[t_reduce_to_canonical_form {AM_GM_pointwise: per_term}]--> output: `s_term_by_term_AM_GM_bound`
3. input: `s_term_by_term_AM_GM_bound` --[t_exhaustion_squeeze {telescoping: limit_(1+1/k)^k_to_e}]--> output: `s_carleman_inequality`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Riesz–Fischer theorem (cite: https://en.wikipedia.org/wiki/Riesz%E2%80%93Fischer_theorem)

**Axioms:** `s_L2_function_space`, `s_orthonormal_basis_in_L2`
**Terminal:** `s_riesz_fischer_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_L2_function_space, s_orthonormal_basis_in_L2⟩` --[t_auxiliary_construction {partial_sums: S_N=sum_n_leq_N_c_n_phi_n}]--> output: `s_partial_sum_sequence_in_L2`
2. input: `s_partial_sum_sequence_in_L2` --[t_compactness_argument {via: Cauchy_in_L2_from_l2_convergence_of_coefficients}]--> output: `s_cauchy_sequence_in_L2`
3. input: `s_cauchy_sequence_in_L2` --[t_reduce_to_canonical_form {complete: L2_completeness}]--> output: `s_riesz_fischer_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Marcinkiewicz interpolation theorem (cite: https://en.wikipedia.org/wiki/Marcinkiewicz_interpolation_theorem)

**Axioms:** `s_sublinear_operator_T_weak_type_at_endpoints`, `s_lp_lq_pair_endpoints`
**Terminal:** `s_marcinkiewicz_interpolation` (kind: theorem)

**Steps:**
1. input: `⟨s_sublinear_operator_T_weak_type_at_endpoints, s_lp_lq_pair_endpoints⟩` --[t_auxiliary_construction {split: f=f_chi_{|f|>lambda}+f_chi_{|f|<=lambda}}]--> output: `s_layer_cake_decomposition_of_f`
2. input: `s_layer_cake_decomposition_of_f` --[t_interpolate_and_continue {weak_type_at_both_endpoints: integrate_in_lambda}]--> output: `s_strong_type_bound_at_intermediate_p`
3. input: `s_strong_type_bound_at_intermediate_p` --[t_reduce_to_canonical_form {finish: optimize_lambda}]--> output: `s_marcinkiewicz_interpolation`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_reduce_to_canonical_form

---

### Riesz–Thorin interpolation theorem (cite: https://en.wikipedia.org/wiki/Riesz%E2%80%93Thorin_theorem)

**Axioms:** `s_linear_operator_T_bounded_at_endpoints`, `s_complex_strip_0_leq_Re_z_leq_1`
**Terminal:** `s_riesz_thorin_interpolation` (kind: theorem)

**Steps:**
1. input: `⟨s_linear_operator_T_bounded_at_endpoints, s_complex_strip_0_leq_Re_z_leq_1⟩` --[t_auxiliary_construction {analytic_family: F(z)=int(Tf_z)g_z}]--> output: `s_analytic_function_on_complex_strip`
2. input: `s_analytic_function_on_complex_strip` --[t_complex_analysis_to_integers {three_lines: Hadamard_three_lines_lemma}]--> output: `s_log_norm_convex_in_z`
3. input: `s_log_norm_convex_in_z` --[t_interpolate_and_continue {evaluate: at_intermediate_theta}]--> output: `s_riesz_thorin_interpolation`

**Techniques used:** t_auxiliary_construction, t_complex_analysis_to_integers, t_interpolate_and_continue

---

### Stein interpolation theorem (cite: https://en.wikipedia.org/wiki/Stein_interpolation_theorem)

**Axioms:** `s_analytic_family_of_operators_T_z`, `s_lp_lq_pair_endpoints`
**Terminal:** `s_stein_interpolation` (kind: theorem)

**Steps:**
1. input: `⟨s_analytic_family_of_operators_T_z, s_lp_lq_pair_endpoints⟩` --[t_auxiliary_construction {dual_pair: F(z)=<T_z_f_z,g_z>}]--> output: `s_analytic_F_with_growth_control`
2. input: `s_analytic_F_with_growth_control` --[t_complex_analysis_to_integers {Phragmen_Lindelof_for_strip}]--> output: `s_log_convex_bound_on_strip`
3. input: `s_log_convex_bound_on_strip` --[t_interpolate_and_continue {endpoint_norms: at_Re_z=0_and_1}]--> output: `s_stein_interpolation`

**Techniques used:** t_auxiliary_construction, t_complex_analysis_to_integers, t_interpolate_and_continue

---

## IV. Measure decompositions and integration tools

### Hahn decomposition theorem (cite: https://en.wikipedia.org/wiki/Hahn_decomposition_theorem)

**Axioms:** `s_signed_measure_on_measurable_space`, `s_measurable_space`
**Terminal:** `s_hahn_decomposition` (kind: theorem)

**Steps:**
1. input: `⟨s_signed_measure_on_measurable_space, s_measurable_space⟩` --[t_auxiliary_construction {max: P_supremum_of_nu_over_positive_sets}]--> output: `s_supremum_of_positive_set_values`
2. input: `s_supremum_of_positive_set_values` --[t_exhaustion_squeeze {extract: maximizing_sequence_of_positive_sets}]--> output: `s_limit_positive_set_P_star`
3. input: `s_limit_positive_set_P_star` --[t_reduce_to_canonical_form {complement: N=X\\P_negative}]--> output: `s_hahn_decomposition`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Jordan decomposition of a measure (cite: https://en.wikipedia.org/wiki/Jordan_decomposition_theorem)

**Axioms:** `s_signed_measure_on_measurable_space`, `s_hahn_decomposition`
**Terminal:** `s_jordan_decomposition_measure` (kind: theorem)

**Steps:**
1. input: `⟨s_signed_measure_on_measurable_space, s_hahn_decomposition⟩` --[t_reduce_to_canonical_form {split: nu_plus=nu|_P_and_nu_minus=-nu|_N}]--> output: `s_two_positive_measures_mutually_singular`
2. input: `s_two_positive_measures_mutually_singular` --[t_axiomatize_from_instances {uniqueness: minimality_of_decomposition}]--> output: `s_jordan_decomposition_measure`

**Techniques used:** t_reduce_to_canonical_form, t_axiomatize_from_instances

---

### Lebesgue decomposition theorem (cite: https://en.wikipedia.org/wiki/Lebesgue%27s_decomposition_theorem)

**Axioms:** `s_sigma_finite_measure_space`, `s_pair_of_sigma_finite_measures_mu_nu`
**Terminal:** `s_lebesgue_decomposition` (kind: theorem)

**Steps:**
1. input: `⟨s_sigma_finite_measure_space, s_pair_of_sigma_finite_measures_mu_nu⟩` --[t_auxiliary_construction {radon_nikodym: derivative_of_nu_wrt_mu_plus_nu}]--> output: `s_radon_nikodym_density_against_sum`
2. input: `s_radon_nikodym_density_against_sum` --[t_reduce_to_canonical_form {split: f=0_set_and_complement}]--> output: `s_singular_plus_absolutely_continuous_split`
3. input: `s_singular_plus_absolutely_continuous_split` --[t_axiomatize_from_instances {uniqueness: characterization_by_absolute_continuity_and_singularity}]--> output: `s_lebesgue_decomposition`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_axiomatize_from_instances

---

### Riesz representation theorem for C(K) (cite: https://en.wikipedia.org/wiki/Riesz_representation_theorem#The_representation_theorem_for_the_dual_of_C0(X))

**Axioms:** `s_compact_hausdorff_space`, `s_bounded_linear_functional_on_C_K`
**Terminal:** `s_riesz_representation_C_K` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_hausdorff_space, s_bounded_linear_functional_on_C_K⟩` --[t_auxiliary_construction {decompose: Jordan_into_positive_minus_negative}]--> output: `s_pair_of_positive_functionals`
2. input: `s_pair_of_positive_functionals` --[t_duality {Riesz_Markov: each_positive_part_is_a_measure}]--> output: `s_pair_of_radon_measures`
3. input: `s_pair_of_radon_measures` --[t_reduce_to_canonical_form {combine: signed_radon_measure}]--> output: `s_riesz_representation_C_K`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Lebesgue–Stieltjes integral existence (cite: https://en.wikipedia.org/wiki/Lebesgue%E2%80%93Stieltjes_integration)

**Axioms:** `s_right_continuous_nondecreasing_function_on_R`, `s_borel_sigma_algebra_on_R`
**Terminal:** `s_lebesgue_stieltjes_existence` (kind: theorem)

**Steps:**
1. input: `⟨s_right_continuous_nondecreasing_function_on_R, s_borel_sigma_algebra_on_R⟩` --[t_auxiliary_construction {premeasure: mu_F((a,b])=F(b)-F(a)}]--> output: `s_premeasure_on_half_open_intervals`
2. input: `s_premeasure_on_half_open_intervals` --[t_reduce_to_canonical_form {extend: Caratheodory_extension_theorem}]--> output: `s_lebesgue_stieltjes_existence`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Helly's selection theorem (cite: https://en.wikipedia.org/wiki/Helly%27s_selection_theorem)

**Axioms:** `s_sequence_of_uniformly_bounded_monotone_functions`, `s_real_numbers`
**Terminal:** `s_helly_selection_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sequence_of_uniformly_bounded_monotone_functions, s_real_numbers⟩` --[t_auxiliary_construction {dense: countable_dense_subset_Q}]--> output: `s_values_at_rational_points_bounded`
2. input: `s_values_at_rational_points_bounded` --[t_pigeonhole_collision {diagonal: Cantor_extraction_subsequence}]--> output: `s_subsequence_converging_on_Q`
3. input: `s_subsequence_converging_on_Q` --[t_exhaustion_squeeze {monotonicity: extend_to_R_at_continuity_points}]--> output: `s_helly_selection_theorem`

**Techniques used:** t_auxiliary_construction, t_pigeonhole_collision, t_exhaustion_squeeze

---

### Borel–Cantelli lemmas (cite: https://en.wikipedia.org/wiki/Borel%E2%80%93Cantelli_lemma)

**Axioms:** `s_probability_axioms`, `s_sequence_of_measurable_events`
**Terminal:** `s_borel_cantelli_lemmas` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms, s_sequence_of_measurable_events⟩` --[t_auxiliary_construction {limsup: lim_sup_A_n=cap_N_cup_{n>=N}_A_n}]--> output: `s_limsup_event_definition`
2. input: `s_limsup_event_definition` --[t_exhaustion_squeeze {sum: P(limsup)<=lim_N_sum_{n>=N}_P(A_n)}]--> output: `s_first_borel_cantelli`
3. input: `s_first_borel_cantelli` --[t_reduce_to_canonical_form {independence: complement_product_decomposition}]--> output: `s_borel_cantelli_lemmas`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Lebesgue density theorem (cite: https://en.wikipedia.org/wiki/Lebesgue%27s_density_theorem)

**Axioms:** `s_lebesgue_measurable_set_in_Rn`, `s_lebesgue_measure_on_Rn`
**Terminal:** `s_lebesgue_density_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_lebesgue_measurable_set_in_Rn, s_lebesgue_measure_on_Rn⟩` --[t_reduce_to_canonical_form {indicator: f=chi_E}]--> output: `s_indicator_function_of_E`
2. input: `s_indicator_function_of_E` --[⚠ needs new technique {move: Lebesgue_differentiation_applied_to_indicator}]--> output: `s_ae_average_indicator_converges_to_indicator`
3. input: `s_ae_average_indicator_converges_to_indicator` --[t_reduce_to_canonical_form {interpret: density_one_at_almost_every_point_of_E}]--> output: `s_lebesgue_density_theorem`

**Techniques used:** t_reduce_to_canonical_form

---

## V. Complex analysis core

### Cauchy–Riemann equations (cite: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations)

**Axioms:** `s_complex_differentiable_function`, `s_open_domain_in_C`
**Terminal:** `s_cauchy_riemann_equations` (kind: theorem)

**Steps:**
1. input: `⟨s_complex_differentiable_function, s_open_domain_in_C⟩` --[t_reduce_to_canonical_form {split: f=u+iv_and_z=x+iy}]--> output: `s_real_imaginary_split`
2. input: `s_real_imaginary_split` --[t_symmetry_reduction {direction: differentiate_along_real_then_imaginary_axes}]--> output: `s_two_directional_derivatives_match`
3. input: `s_two_directional_derivatives_match` --[t_reduce_to_canonical_form {equate: u_x=v_y_and_u_y=-v_x}]--> output: `s_cauchy_riemann_equations`

**Techniques used:** t_reduce_to_canonical_form, t_symmetry_reduction

---

### Looman–Menchoff theorem (cite: https://en.wikipedia.org/wiki/Looman%E2%80%93Menchoff_theorem)

**Axioms:** `s_continuous_function_satisfying_CR_ae`, `s_open_domain_in_C`
**Terminal:** `s_looman_menchoff_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_function_satisfying_CR_ae, s_open_domain_in_C⟩` --[t_auxiliary_construction {green: rectangle_integral_via_CR}]--> output: `s_vanishing_rectangle_integral`
2. input: `s_vanishing_rectangle_integral` --[t_reduce_to_canonical_form {morera: zero_integral_on_all_rectangles}]--> output: `s_morera_hypothesis_satisfied`
3. input: `s_morera_hypothesis_satisfied` --[t_compactness_argument {conclude: holomorphic_via_Morera}]--> output: `s_looman_menchoff_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_compactness_argument

---

### Cauchy's theorem (rectangle / Goursat) (cite: https://en.wikipedia.org/wiki/Cauchy%27s_integral_theorem)

**Axioms:** `s_holomorphic_function_on_domain`, `s_rectangle_in_C`
**Terminal:** `s_cauchy_goursat_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_domain, s_rectangle_in_C⟩` --[t_pigeonhole_collision {bisect: rectangle_into_four_subrectangles}]--> output: `s_nested_quartered_rectangle_with_largest_integral`
2. input: `s_nested_quartered_rectangle_with_largest_integral` --[t_exhaustion_squeeze {diameter: 2^-n_shrinkage}]--> output: `s_point_with_local_linear_approximation`
3. input: `s_point_with_local_linear_approximation` --[t_reduce_to_canonical_form {linear_part_integrates_to_zero}]--> output: `s_cauchy_goursat_theorem`

**Techniques used:** t_pigeonhole_collision, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Cauchy's theorem (homotopy version) (cite: https://en.wikipedia.org/wiki/Cauchy%27s_integral_theorem#Homotopy_form)

**Axioms:** `s_holomorphic_function_on_domain`, `s_two_homotopic_closed_curves`
**Terminal:** `s_cauchy_theorem_homotopy` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_domain, s_two_homotopic_closed_curves⟩` --[t_auxiliary_construction {homotopy: H:[0,1]^2_to_domain}]--> output: `s_homotopy_grid_partition`
2. input: `s_homotopy_grid_partition` --[t_compactness_argument {cover: finite_lebesgue_grid_of_small_rectangles}]--> output: `s_finite_grid_with_goursat_per_cell`
3. input: `s_finite_grid_with_goursat_per_cell` --[t_reduce_to_canonical_form {telescope: cancel_interior_edges}]--> output: `s_cauchy_theorem_homotopy`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Morera's theorem (cite: https://en.wikipedia.org/wiki/Morera%27s_theorem)

**Axioms:** `s_continuous_function_on_domain`, `s_vanishing_integral_on_all_triangles`
**Terminal:** `s_morera_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_function_on_domain, s_vanishing_integral_on_all_triangles⟩` --[t_auxiliary_construction {primitive: F(z)=int_z_0^z_f}]--> output: `s_well_defined_primitive_F`
2. input: `s_well_defined_primitive_F` --[t_reduce_to_canonical_form {differentiate: F'=f_holomorphic_primitive}]--> output: `s_F_holomorphic_with_derivative_f`
3. input: `s_F_holomorphic_with_derivative_f` --[t_compactness_argument {derivatives_of_holomorphic_are_holomorphic}]--> output: `s_morera_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_compactness_argument

---

### Maximum modulus principle (cite: https://en.wikipedia.org/wiki/Maximum_modulus_principle)

**Axioms:** `s_holomorphic_function_on_domain`, `s_interior_local_maximum_of_modulus`
**Terminal:** `s_maximum_modulus_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_domain, s_interior_local_maximum_of_modulus⟩` --[t_auxiliary_construction {mean_value: |f(z_0)|=average_on_circle}]--> output: `s_mean_value_property_on_circle`
2. input: `s_mean_value_property_on_circle` --[t_reductio_ad_absurdum {assume: strict_interior_maximum}]--> output: `s_contradiction_with_averaging_equality`
3. input: `s_contradiction_with_averaging_equality` --[t_reduce_to_canonical_form {conclude: f_constant_on_connected_component}]--> output: `s_maximum_modulus_principle`

**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum, t_reduce_to_canonical_form

---

### Schwarz lemma (cite: https://en.wikipedia.org/wiki/Schwarz_lemma)

**Axioms:** `s_holomorphic_self_map_of_unit_disk_fixing_zero`, `s_unit_disk_in_C`
**Terminal:** `s_schwarz_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_self_map_of_unit_disk_fixing_zero, s_unit_disk_in_C⟩` --[t_auxiliary_construction {quotient: g(z)=f(z)/z}]--> output: `s_holomorphic_quotient_g`
2. input: `s_holomorphic_quotient_g` --[t_reduce_to_canonical_form {apply: maximum_modulus_on_|z|=r<1}]--> output: `s_bound_|g|<=1_on_disk`
3. input: `s_bound_|g|<=1_on_disk` --[t_exhaustion_squeeze {let: r_to_1}]--> output: `s_schwarz_lemma`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Schwarz–Pick theorem (cite: https://en.wikipedia.org/wiki/Schwarz%E2%80%93Pick_theorem)

**Axioms:** `s_holomorphic_self_map_of_unit_disk`, `s_unit_disk_in_C`
**Terminal:** `s_schwarz_pick_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_self_map_of_unit_disk, s_unit_disk_in_C⟩` --[t_auxiliary_construction {compose: Mobius_translation_to_fix_zero}]--> output: `s_normalized_self_map_fixing_zero`
2. input: `s_normalized_self_map_fixing_zero` --[t_reduce_to_canonical_form {apply: Schwarz_lemma}]--> output: `s_bound_at_origin`
3. input: `s_bound_at_origin` --[t_symmetry_reduction {automorphism_group: SU(1,1)_invariance}]--> output: `s_schwarz_pick_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_symmetry_reduction

---

### Liouville's theorem (cite: https://en.wikipedia.org/wiki/Liouville%27s_theorem_(complex_analysis))

**Axioms:** `s_bounded_entire_function`, `s_complex_numbers`
**Terminal:** `s_liouville_theorem_complex` (kind: theorem)

**Steps:**
1. input: `⟨s_bounded_entire_function, s_complex_numbers⟩` --[t_auxiliary_construction {Cauchy_estimate: |f'(z)|<=M/R}]--> output: `s_cauchy_estimate_for_derivative`
2. input: `s_cauchy_estimate_for_derivative` --[t_exhaustion_squeeze {let: R_to_infinity}]--> output: `s_f_prime_identically_zero`
3. input: `s_f_prime_identically_zero` --[t_reduce_to_canonical_form {integrate: f_constant}]--> output: `s_liouville_theorem_complex`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Argument principle (cite: https://en.wikipedia.org/wiki/Argument_principle)

**Axioms:** `s_meromorphic_function_on_domain`, `s_simple_closed_curve_in_domain`
**Terminal:** `s_argument_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_meromorphic_function_on_domain, s_simple_closed_curve_in_domain⟩` --[t_auxiliary_construction {logarithmic_derivative: f'(z)/f(z)}]--> output: `s_logarithmic_derivative_with_poles_at_zeros_and_poles`
2. input: `s_logarithmic_derivative_with_poles_at_zeros_and_poles` --[t_reduce_to_canonical_form {residue: residue_at_each_zero_and_pole}]--> output: `s_residue_sum_equals_Z_minus_P`
3. input: `s_residue_sum_equals_Z_minus_P` --[t_compactness_argument {via: residue_theorem_inside_curve}]--> output: `s_argument_principle`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_compactness_argument

---

### Rouché's theorem (cite: https://en.wikipedia.org/wiki/Rouch%C3%A9%27s_theorem)

**Axioms:** `s_holomorphic_pair_f_g_with_|g|<|f|_on_boundary`, `s_simple_closed_curve_in_domain`
**Terminal:** `s_rouche_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_pair_f_g_with_|g|<|f|_on_boundary, s_simple_closed_curve_in_domain⟩` --[t_auxiliary_construction {homotopy: f_t=f+t_g_for_t_in_[0,1]}]--> output: `s_continuous_homotopy_avoiding_zero_on_curve`
2. input: `s_continuous_homotopy_avoiding_zero_on_curve` --[t_obstruction_class {winding_number_integer_valued_continuous}]--> output: `s_winding_number_constant_along_homotopy`
3. input: `s_winding_number_constant_along_homotopy` --[t_reduce_to_canonical_form {via: argument_principle_at_t=0_and_1}]--> output: `s_rouche_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_reduce_to_canonical_form

---

### Open mapping theorem (complex) (cite: https://en.wikipedia.org/wiki/Open_mapping_theorem_(complex_analysis))

**Axioms:** `s_nonconstant_holomorphic_function`, `s_open_domain_in_C`
**Terminal:** `s_open_mapping_theorem_complex` (kind: theorem)

**Steps:**
1. input: `⟨s_nonconstant_holomorphic_function, s_open_domain_in_C⟩` --[t_auxiliary_construction {shift: g(z)=f(z)-w_0}]--> output: `s_shifted_function_with_zero_at_z_0`
2. input: `s_shifted_function_with_zero_at_z_0` --[t_reduce_to_canonical_form {via: argument_principle_count_zeros}]--> output: `s_neighborhood_of_w_0_in_image`
3. input: `s_neighborhood_of_w_0_in_image` --[t_compactness_argument {extract: open_neighborhood_in_image}]--> output: `s_open_mapping_theorem_complex`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_compactness_argument

---

### Casorati–Weierstrass theorem (cite: https://en.wikipedia.org/wiki/Casorati%E2%80%93Weierstrass_theorem)

**Axioms:** `s_holomorphic_function_with_essential_singularity`, `s_punctured_disk_around_singularity`
**Terminal:** `s_casorati_weierstrass` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_with_essential_singularity, s_punctured_disk_around_singularity⟩` --[t_reductio_ad_absurdum {assume: image_misses_neighborhood_of_w}]--> output: `s_inverted_function_1_over_f_minus_w_bounded`
2. input: `s_inverted_function_1_over_f_minus_w_bounded` --[t_reduce_to_canonical_form {via: removable_singularity_for_bounded}]--> output: `s_contradiction_with_essential_singularity`
3. input: `s_contradiction_with_essential_singularity` --[t_compactness_argument {conclude: image_dense_in_C}]--> output: `s_casorati_weierstrass`

**Techniques used:** t_reductio_ad_absurdum, t_reduce_to_canonical_form, t_compactness_argument

---

### Picard's little theorem (cite: https://en.wikipedia.org/wiki/Picard_theorem)

**Axioms:** `s_nonconstant_entire_function`, `s_complex_numbers`
**Terminal:** `s_picard_little_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_nonconstant_entire_function, s_complex_numbers⟩` --[t_reductio_ad_absurdum {assume: omits_two_values}]--> output: `s_entire_function_missing_two_values`
2. input: `s_entire_function_missing_two_values` --[t_auxiliary_construction {modular_lambda: lift_via_universal_cover_to_disk}]--> output: `s_holomorphic_lift_to_unit_disk`
3. input: `s_holomorphic_lift_to_unit_disk` --[t_reduce_to_canonical_form {Liouville: bounded_entire_constant}]--> output: `s_picard_little_theorem`

**Techniques used:** t_reductio_ad_absurdum, t_auxiliary_construction, t_reduce_to_canonical_form

---

### Picard's great theorem (cite: https://en.wikipedia.org/wiki/Picard_theorem#Great_Picard's_theorem)

**Axioms:** `s_holomorphic_function_with_essential_singularity`, `s_punctured_disk_around_singularity`
**Terminal:** `s_picard_great_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_with_essential_singularity, s_punctured_disk_around_singularity⟩` --[t_reductio_ad_absurdum {assume: image_omits_two_values_in_punctured_disk}]--> output: `s_function_missing_two_values_near_singularity`
2. input: `s_function_missing_two_values_near_singularity` --[t_auxiliary_construction {Montel_normal_family_via_modular_function}]--> output: `s_normal_family_of_dilates`
3. input: `s_normal_family_of_dilates` --[t_compactness_argument {extract: bounded_subsequence_contradicting_essential_singularity}]--> output: `s_picard_great_theorem`

**Techniques used:** t_reductio_ad_absurdum, t_auxiliary_construction, t_compactness_argument

---

### Phragmén–Lindelöf principle (cite: https://en.wikipedia.org/wiki/Phragm%C3%A9n%E2%80%93Lindel%C3%B6f_principle)

**Axioms:** `s_holomorphic_function_on_sector_with_growth_bound`, `s_unbounded_sector_in_C`
**Terminal:** `s_phragmen_lindelof` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_sector_with_growth_bound, s_unbounded_sector_in_C⟩` --[t_auxiliary_construction {auxiliary: g(z)=f(z)*exp(-eps_z^alpha)}]--> output: `s_auxiliary_decaying_function_g`
2. input: `s_auxiliary_decaying_function_g` --[t_reduce_to_canonical_form {bounded: on_finite_arc_by_continuity}]--> output: `s_g_bounded_on_bounded_part`
3. input: `s_g_bounded_on_bounded_part` --[t_compactness_argument {max_modulus_on_truncated_sector_then_eps_to_zero}]--> output: `s_phragmen_lindelof`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_compactness_argument

---

### Hadamard three-lines theorem (cite: https://en.wikipedia.org/wiki/Hadamard_three-lines_theorem)

**Axioms:** `s_holomorphic_bounded_function_on_strip`, `s_vertical_strip_0_leq_Re_z_leq_1`
**Terminal:** `s_hadamard_three_lines` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_bounded_function_on_strip, s_vertical_strip_0_leq_Re_z_leq_1⟩` --[t_auxiliary_construction {auxiliary: g(z)=f(z)*M_0^{z-1}*M_1^{-z}}]--> output: `s_normalized_function_with_boundary_modulus_one`
2. input: `s_normalized_function_with_boundary_modulus_one` --[t_reduce_to_canonical_form {phragmen_lindelof: bounded_on_strip}]--> output: `s_modulus_g_leq_1_in_strip`
3. input: `s_modulus_g_leq_1_in_strip` --[t_interpolate_and_continue {log_M_convex_in_Re_z}]--> output: `s_hadamard_three_lines`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_interpolate_and_continue

---

### Hadamard three-circles theorem (cite: https://en.wikipedia.org/wiki/Hadamard_three-circle_theorem)

**Axioms:** `s_holomorphic_function_on_annulus`, `s_annulus_r1_leq_|z|_leq_r3`
**Terminal:** `s_hadamard_three_circles` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_annulus, s_annulus_r1_leq_|z|_leq_r3⟩` --[t_reduce_to_canonical_form {substitute: w=log_z_maps_annulus_to_strip}]--> output: `s_pullback_to_vertical_strip`
2. input: `s_pullback_to_vertical_strip` --[t_reduce_to_canonical_form {apply: three_lines_theorem}]--> output: `s_log_max_convex_in_log_r`
3. input: `s_log_max_convex_in_log_r` --[t_interpolate_and_continue {log_M_r_convex_in_log_r}]--> output: `s_hadamard_three_circles`

**Techniques used:** t_reduce_to_canonical_form, t_interpolate_and_continue

---

### Hadamard factorization theorem (cite: https://en.wikipedia.org/wiki/Hadamard_factorization_theorem)

**Axioms:** `s_entire_function_of_finite_order`, `s_complex_numbers`
**Terminal:** `s_hadamard_factorization` (kind: theorem)

**Steps:**
1. input: `⟨s_entire_function_of_finite_order, s_complex_numbers⟩` --[t_auxiliary_construction {zeros: list_zeros_with_multiplicities}]--> output: `s_zero_sequence_with_density_bound`
2. input: `s_zero_sequence_with_density_bound` --[⚠ needs new technique {move: canonical_product_with_genus_p_factors}]--> output: `s_canonical_weierstrass_product`
3. input: `s_canonical_weierstrass_product` --[t_reduce_to_canonical_form {quotient_with_polynomial_exponent: by_order_bound}]--> output: `s_hadamard_factorization`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Weierstrass factorization theorem (cite: https://en.wikipedia.org/wiki/Weierstrass_factorization_theorem)

**Axioms:** `s_complex_numbers`, `s_sequence_a_n_to_infinity_with_multiplicities`
**Terminal:** `s_weierstrass_factorization` (kind: theorem)

**Steps:**
1. input: `⟨s_complex_numbers, s_sequence_a_n_to_infinity_with_multiplicities⟩` --[t_auxiliary_construction {elementary_factors: E_p(z)=(1-z)exp(z+z^2/2+...+z^p/p)}]--> output: `s_elementary_factors_with_convergence_exponents`
2. input: `s_elementary_factors_with_convergence_exponents` --[t_exhaustion_squeeze {choose_p_n: uniform_convergence_on_compacta}]--> output: `s_convergent_infinite_product`
3. input: `s_convergent_infinite_product` --[t_reduce_to_canonical_form {entire_function_with_prescribed_zeros}]--> output: `s_weierstrass_factorization`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Mittag-Leffler theorem (cite: https://en.wikipedia.org/wiki/Mittag-Leffler%27s_theorem)

**Axioms:** `s_open_subset_of_C`, `s_discrete_set_of_poles_with_principal_parts`
**Terminal:** `s_mittag_leffler_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_open_subset_of_C, s_discrete_set_of_poles_with_principal_parts⟩` --[t_auxiliary_construction {polynomial_correctors: subtract_taylor_polynomials_for_uniform_convergence}]--> output: `s_corrected_principal_parts_summable`
2. input: `s_corrected_principal_parts_summable` --[t_exhaustion_squeeze {sum: convergent_on_compacta}]--> output: `s_meromorphic_sum_function`
3. input: `s_meromorphic_sum_function` --[t_reduce_to_canonical_form {check: prescribed_principal_parts_recovered}]--> output: `s_mittag_leffler_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Bloch's theorem (cite: https://en.wikipedia.org/wiki/Bloch%27s_theorem_(complex_variables))

**Axioms:** `s_holomorphic_function_on_unit_disk_with_f_prime_zero_one`, `s_unit_disk_in_C`
**Terminal:** `s_bloch_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_unit_disk_with_f_prime_zero_one, s_unit_disk_in_C⟩` --[t_auxiliary_construction {extremal: maximize_r(1-|z|)|f'(z)|_over_z_in_disk}]--> output: `s_optimal_point_z_star_and_radius`
2. input: `s_optimal_point_z_star_and_radius` --[t_rescale_for_asymptotic_geometry {rescale: f_into_unit_disk_image}]--> output: `s_normalized_function_with_uniform_derivative`
3. input: `s_normalized_function_with_uniform_derivative` --[t_reduce_to_canonical_form {schwarz_type_bound: image_contains_universal_disk}]--> output: `s_bloch_theorem`

**Techniques used:** t_auxiliary_construction, t_rescale_for_asymptotic_geometry, t_reduce_to_canonical_form

---

### Montel's theorem (cite: https://en.wikipedia.org/wiki/Montel%27s_theorem)

**Axioms:** `s_locally_uniformly_bounded_family_of_holomorphic_functions`, `s_open_domain_in_C`
**Terminal:** `s_montel_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_locally_uniformly_bounded_family_of_holomorphic_functions, s_open_domain_in_C⟩` --[t_auxiliary_construction {derivative_bound: Cauchy_estimate_for_f_prime_on_compacta}]--> output: `s_equicontinuous_family_on_compacta`
2. input: `s_equicontinuous_family_on_compacta` --[t_compactness_argument {Arzela_Ascoli: extract_uniformly_convergent_subsequence}]--> output: `s_subsequence_converging_uniformly_on_compacta`
3. input: `s_subsequence_converging_uniformly_on_compacta` --[t_reduce_to_canonical_form {limit_holomorphic: by_Morera}]--> output: `s_montel_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Vitali's convergence theorem (complex) (cite: https://en.wikipedia.org/wiki/Vitali_convergence_theorem)

**Axioms:** `s_locally_uniformly_bounded_holomorphic_sequence`, `s_open_connected_domain_in_C`
**Terminal:** `s_vitali_convergence_complex` (kind: theorem)

**Steps:**
1. input: `⟨s_locally_uniformly_bounded_holomorphic_sequence, s_open_connected_domain_in_C⟩` --[t_compactness_argument {Montel: any_subsequence_has_convergent_sub_subsequence}]--> output: `s_normal_family_with_subsequence_limit`
2. input: `s_normal_family_with_subsequence_limit` --[t_auxiliary_construction {identity_principle: limit_unique_on_set_with_accumulation_point}]--> output: `s_limit_function_determined_by_pointwise_set`
3. input: `s_normal_family_with_subsequence_limit` --[t_reduce_to_canonical_form {conclude: whole_sequence_converges_locally_uniformly}]--> output: `s_vitali_convergence_complex`

**Techniques used:** t_compactness_argument, t_auxiliary_construction, t_reduce_to_canonical_form

---

### Runge's theorem (cite: https://en.wikipedia.org/wiki/Runge%27s_theorem)

**Axioms:** `s_holomorphic_function_on_open_neighborhood_of_compact_K`, `s_compact_subset_K_of_C`
**Terminal:** `s_runge_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_holomorphic_function_on_open_neighborhood_of_compact_K, s_compact_subset_K_of_C⟩` --[t_auxiliary_construction {Cauchy_kernel_partition: pole_pushing_via_geometric_series}]--> output: `s_rational_approximation_with_poles_in_C_minus_K`
2. input: `s_rational_approximation_with_poles_in_C_minus_K` --[t_compactness_argument {pole_pushing: shift_poles_into_each_complement_component}]--> output: `s_approximation_with_poles_in_prescribed_set`
3. input: `s_approximation_with_poles_in_prescribed_set` --[t_reduce_to_canonical_form {polynomial_case: when_complement_connected_at_infinity}]--> output: `s_runge_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Mergelyan's theorem (cite: https://en.wikipedia.org/wiki/Mergelyan%27s_theorem)

**Axioms:** `s_continuous_function_on_compact_K_holomorphic_in_interior`, `s_compact_subset_K_of_C_with_connected_complement`
**Terminal:** `s_mergelyan_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_function_on_compact_K_holomorphic_in_interior, s_compact_subset_K_of_C_with_connected_complement⟩` --[t_auxiliary_construction {smoothing: convolve_with_compactly_supported_mollifier}]--> output: `s_smooth_approximant_of_f`
2. input: `s_smooth_approximant_of_f` --[⚠ needs new technique {move: Vitushkin_localization_with_uniform_Cauchy_transform_estimates}]--> output: `s_rational_approximation_uniform_on_K`
3. input: `s_rational_approximation_uniform_on_K` --[t_reduce_to_canonical_form {via: Runge_with_connected_complement}]--> output: `s_mergelyan_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Carleman approximation theorem (cite: https://en.wikipedia.org/wiki/Carleman%27s_theorem)

**Axioms:** `s_continuous_function_on_real_line`, `s_positive_continuous_error_function_eps`
**Terminal:** `s_carleman_approximation` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_function_on_real_line, s_positive_continuous_error_function_eps⟩` --[t_auxiliary_construction {entire_partial_approximants_on_growing_intervals}]--> output: `s_sequence_of_entire_partial_approximants`
2. input: `s_sequence_of_entire_partial_approximants` --[t_reduce_to_canonical_form {via: Runge_on_compact_horizontal_strips}]--> output: `s_uniform_approximation_with_error_eps_on_R`
3. input: `s_uniform_approximation_with_error_eps_on_R` --[t_exhaustion_squeeze {patch: telescoping_correction_series}]--> output: `s_carleman_approximation`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Schwarz–Christoffel mapping (cite: https://en.wikipedia.org/wiki/Schwarz%E2%80%93Christoffel_mapping)

**Axioms:** `s_polygon_in_C`, `s_upper_half_plane`
**Terminal:** `s_schwarz_christoffel_mapping` (kind: theorem)

**Steps:**
1. input: `⟨s_polygon_in_C, s_upper_half_plane⟩` --[t_riemann_mapping_application {existence: hol_bijection_to_polygon}]--> output: `s_hol_bijection_to_polygon_interior`
2. input: `s_hol_bijection_to_polygon_interior` --[t_auxiliary_construction {reflection: across_each_polygon_side}]--> output: `s_log_derivative_with_branch_points_at_prevertices`
3. input: `s_log_derivative_with_branch_points_at_prevertices` --[t_reduce_to_canonical_form {integrate: f'(z)=C*prod(z-x_k)^{alpha_k-1}}]--> output: `s_schwarz_christoffel_mapping`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

## VI. Fourier analysis & harmonic analysis

### Riemann–Lebesgue lemma (cite: https://en.wikipedia.org/wiki/Riemann%E2%80%93Lebesgue_lemma)

**Axioms:** `s_l1_function_on_Rn`, `s_lebesgue_measure_on_Rn`
**Terminal:** `s_riemann_lebesgue_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_l1_function_on_Rn, s_lebesgue_measure_on_Rn⟩` --[t_auxiliary_construction {approx: indicator_of_rectangle_dense_in_L1}]--> output: `s_approximation_by_rectangle_indicators`
2. input: `s_approximation_by_rectangle_indicators` --[t_verify_on_special_cases {direct: Fourier_of_rectangle_indicator_decays}]--> output: `s_decay_for_step_functions`
3. input: `s_decay_for_step_functions` --[t_exhaustion_squeeze {density_argument: extend_by_L1_density}]--> output: `s_riemann_lebesgue_lemma`

**Techniques used:** t_auxiliary_construction, t_verify_on_special_cases, t_exhaustion_squeeze

---

### Plancherel theorem (cite: https://en.wikipedia.org/wiki/Plancherel_theorem)

**Axioms:** `s_L2_function_space`, `s_schwartz_class_dense_in_L2`
**Terminal:** `s_plancherel_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_L2_function_space, s_schwartz_class_dense_in_L2⟩` --[t_fourier_transform {schwartz: Fourier_isometry_on_S}]--> output: `s_isometry_on_dense_Schwartz_subspace`
2. input: `s_isometry_on_dense_Schwartz_subspace` --[t_compactness_argument {extend: bounded_linear_to_L2_via_density}]--> output: `s_unitary_extension_to_L2`
3. input: `s_unitary_extension_to_L2` --[t_reduce_to_canonical_form {parseval: ||f||_2=||hat_f||_2}]--> output: `s_plancherel_theorem`

**Techniques used:** t_fourier_transform, t_compactness_argument, t_reduce_to_canonical_form

---

### Paley–Wiener theorem (cite: https://en.wikipedia.org/wiki/Paley%E2%80%93Wiener_theorem)

**Axioms:** `s_L2_function_compactly_supported`, `s_complex_numbers`
**Terminal:** `s_paley_wiener_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_L2_function_compactly_supported, s_complex_numbers⟩` --[t_fourier_transform {extend: Fourier_to_complex_argument}]--> output: `s_entire_extension_of_Fourier_transform`
2. input: `s_entire_extension_of_Fourier_transform` --[t_reduce_to_canonical_form {growth: exponential_type_bound_from_support}]--> output: `s_exponential_type_function`
3. input: `s_exponential_type_function` --[t_duality {converse: exponential_type_plus_L2_on_R_implies_compact_support}]--> output: `s_paley_wiener_theorem`

**Techniques used:** t_fourier_transform, t_reduce_to_canonical_form, t_duality

---

### Poisson summation formula (cite: https://en.wikipedia.org/wiki/Poisson_summation_formula)

**Axioms:** `s_schwartz_class_function_on_R`, `s_integers`
**Terminal:** `s_poisson_summation_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_schwartz_class_function_on_R, s_integers⟩` --[t_auxiliary_construction {periodize: F(x)=sum_n_f(x+n)}]--> output: `s_periodic_function_F_with_period_one`
2. input: `s_periodic_function_F_with_period_one` --[t_fourier_transform {expand: Fourier_series_of_F}]--> output: `s_fourier_series_with_coefficients_hat_f(k)`
3. input: `s_fourier_series_with_coefficients_hat_f(k)` --[t_reduce_to_canonical_form {evaluate: at_x=0}]--> output: `s_poisson_summation_formula`

**Techniques used:** t_auxiliary_construction, t_fourier_transform, t_reduce_to_canonical_form

---

### Bochner's theorem (cite: https://en.wikipedia.org/wiki/Bochner%27s_theorem)

**Axioms:** `s_continuous_positive_definite_function_on_Rn`, `s_locally_compact_abelian_group_R`
**Terminal:** `s_bochner_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_positive_definite_function_on_Rn, s_locally_compact_abelian_group_R⟩` --[t_auxiliary_construction {positive_functional: Lambda(f)=int_phi_f}]--> output: `s_positive_linear_functional_on_test_functions`
2. input: `s_positive_linear_functional_on_test_functions` --[t_duality {Riesz_Markov: represent_as_finite_Borel_measure}]--> output: `s_finite_borel_measure_on_dual_group`
3. input: `s_finite_borel_measure_on_dual_group` --[t_fourier_transform {Fourier_inversion: phi_equals_Fourier_of_measure}]--> output: `s_bochner_theorem`

**Techniques used:** t_auxiliary_construction, t_duality, t_fourier_transform

---

### Bernstein's theorem on absolutely monotonic functions (cite: https://en.wikipedia.org/wiki/Bernstein%27s_theorem_on_monotone_functions)

**Axioms:** `s_completely_monotonic_function_on_R_plus`, `s_positive_real_line`
**Terminal:** `s_bernstein_theorem_monotonic` (kind: theorem)

**Steps:**
1. input: `⟨s_completely_monotonic_function_on_R_plus, s_positive_real_line⟩` --[t_auxiliary_construction {finite_differences: backward_n_th_difference_nonneg}]--> output: `s_nonneg_finite_differences_at_grid`
2. input: `s_nonneg_finite_differences_at_grid` --[t_compactness_argument {Helly_selection: limit_distribution_function}]--> output: `s_limit_measure_dmu_on_R_plus`
3. input: `s_limit_measure_dmu_on_R_plus` --[t_reduce_to_canonical_form {Laplace: f(x)=int_e^{-xt}_dmu(t)}]--> output: `s_bernstein_theorem_monotonic`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Carleson's theorem on a.e. convergence of Fourier series (cite: https://en.wikipedia.org/wiki/Carleson%27s_theorem)

**Axioms:** `s_l2_function_on_circle`, `s_fourier_series_partial_sums`
**Terminal:** `s_carleson_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_l2_function_on_circle, s_fourier_series_partial_sums⟩` --[t_auxiliary_construction {Carleson_operator: C_f(x)=sup_N_|S_N_f(x)|}]--> output: `s_carleson_maximal_operator`
2. input: `s_carleson_maximal_operator` --[⚠ needs new technique {move: time_frequency_tile_decomposition_with_BMO_bounds}]--> output: `s_weak_type_(2,2)_bound_for_Carleson_op`
3. input: `s_weak_type_(2,2)_bound_for_Carleson_op` --[t_reduce_to_canonical_form {ae_convergence: from_maximal_inequality_density}]--> output: `s_carleson_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Kahane–Katznelson–de Leeuw theorem (cite: https://en.wikipedia.org/wiki/Kahane%E2%80%93Katznelson%E2%80%93de_Leeuw_theorem)

**Axioms:** `s_continuous_function_on_circle`, `s_l2_fourier_coefficient_sequence`
**Terminal:** `s_kahane_katznelson_de_leeuw` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_function_on_circle, s_l2_fourier_coefficient_sequence⟩` --[t_auxiliary_construction {randomize: signs_via_independent_pm1_choices}]--> output: `s_random_sign_modification_of_coefficients`
2. input: `s_random_sign_modification_of_coefficients` --[t_probabilistic_existence {Khintchine: bound_expected_sup_norm}]--> output: `s_existence_of_realization_with_bounded_sup_norm`
3. input: `s_existence_of_realization_with_bounded_sup_norm` --[t_reduce_to_canonical_form {majorize: with_continuous_function_having_same_modulus_coefficients}]--> output: `s_kahane_katznelson_de_leeuw`

**Techniques used:** t_auxiliary_construction, t_probabilistic_existence, t_reduce_to_canonical_form

---

### Hörmander–Mikhlin multiplier theorem (cite: https://en.wikipedia.org/wiki/H%C3%B6rmander%E2%80%93Mikhlin_multiplier_theorem)

**Axioms:** `s_symbol_m_smooth_with_homogeneous_derivative_bounds`, `s_lp_function_on_Rn`
**Terminal:** `s_hormander_mikhlin_multiplier` (kind: theorem)

**Steps:**
1. input: `⟨s_symbol_m_smooth_with_homogeneous_derivative_bounds, s_lp_function_on_Rn⟩` --[t_frequency_decomposition {Littlewood_Paley: dyadic_annular_pieces}]--> output: `s_dyadic_decomposition_of_symbol`
2. input: `s_dyadic_decomposition_of_symbol` --[t_reduce_to_canonical_form {kernel_estimate: Calderon_Zygmund_pointwise_bounds}]--> output: `s_kernel_satisfies_CZ_conditions`
3. input: `s_kernel_satisfies_CZ_conditions` --[t_interpolate_and_continue {CZ_Lp_theory: weak_11_plus_L2_yields_Lp}]--> output: `s_hormander_mikhlin_multiplier`

**Techniques used:** t_frequency_decomposition, t_reduce_to_canonical_form, t_interpolate_and_continue

---

### Cotlar–Stein lemma (cite: https://en.wikipedia.org/wiki/Cotlar%E2%80%93Stein_lemma)

**Axioms:** `s_family_of_bounded_operators_T_j_on_Hilbert_space`, `s_almost_orthogonality_estimates`
**Terminal:** `s_cotlar_stein_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_family_of_bounded_operators_T_j_on_Hilbert_space, s_almost_orthogonality_estimates⟩` --[t_auxiliary_construction {sum: S=sum_T_j_T_j_star_and_T_j_star_T_j}]--> output: `s_pair_of_positive_operator_sums`
2. input: `s_pair_of_positive_operator_sums` --[t_reduce_to_canonical_form {schur_test: square_root_of_orthogonality_bound}]--> output: `s_norm_bound_on_sum_via_schur`
3. input: `s_norm_bound_on_sum_via_schur` --[t_compactness_argument {finite_truncation_then_limit}]--> output: `s_cotlar_stein_lemma`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_compactness_argument

---

### T(1) theorem (David–Journé) (cite: https://en.wikipedia.org/wiki/T(1)_theorem)

**Axioms:** `s_singular_integral_operator_with_CZ_kernel`, `s_BMO_function_T_one_and_T_star_one`
**Terminal:** `s_T_one_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_singular_integral_operator_with_CZ_kernel, s_BMO_function_T_one_and_T_star_one⟩` --[t_auxiliary_construction {paraproduct: subtract_T_one_paraproduct_and_T_star_one_adjoint}]--> output: `s_modified_operator_with_T_one_zero`
2. input: `s_modified_operator_with_T_one_zero` --[t_reduce_to_canonical_form {weak_boundedness_property: testing_on_bumps}]--> output: `s_L2_bounded_modified_operator`
3. input: `s_L2_bounded_modified_operator` --[t_compactness_argument {Cotlar_Stein_on_dyadic_decomposition}]--> output: `s_T_one_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_compactness_argument

---

### Sobolev embedding theorem (cite: https://en.wikipedia.org/wiki/Sobolev_inequality)

**Axioms:** `s_sobolev_space_W_kp_on_Rn`, `s_lebesgue_measure_on_Rn`
**Terminal:** `s_sobolev_embedding_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sobolev_space_W_kp_on_Rn, s_lebesgue_measure_on_Rn⟩` --[t_auxiliary_construction {representation: f=Riesz_potential_of_gradient}]--> output: `s_fractional_integral_representation`
2. input: `s_fractional_integral_representation` --[t_rescale_for_asymptotic_geometry {scaling: critical_exponent_p_star_n_minus_kp}]--> output: `s_scale_critical_target_exponent`
3. input: `s_scale_critical_target_exponent` --[t_reduce_to_canonical_form {via: Hardy_Littlewood_Sobolev_inequality}]--> output: `s_sobolev_embedding_theorem`

**Techniques used:** t_auxiliary_construction, t_rescale_for_asymptotic_geometry, t_reduce_to_canonical_form

---

### Rellich–Kondrachov compactness theorem (cite: https://en.wikipedia.org/wiki/Rellich%E2%80%93Kondrachov_theorem)

**Axioms:** `s_bounded_lipschitz_domain_in_Rn`, `s_sobolev_space_W_kp_on_domain`
**Terminal:** `s_rellich_kondrachov_compactness` (kind: theorem)

**Steps:**
1. input: `⟨s_bounded_lipschitz_domain_in_Rn, s_sobolev_space_W_kp_on_domain⟩` --[t_auxiliary_construction {mollify: convolve_with_smooth_approximate_identity}]--> output: `s_mollification_with_uniform_Lp_control`
2. input: `s_mollification_with_uniform_Lp_control` --[t_compactness_argument {Arzela_Ascoli: equicontinuous_pointwise_bounded}]--> output: `s_relatively_compact_in_Lp_after_mollification`
3. input: `s_relatively_compact_in_Lp_after_mollification` --[t_exhaustion_squeeze {pass_eps_to_zero}]--> output: `s_rellich_kondrachov_compactness`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Poincaré inequality (cite: https://en.wikipedia.org/wiki/Poincar%C3%A9_inequality)

**Axioms:** `s_bounded_connected_lipschitz_domain`, `s_sobolev_space_W_1p_on_domain`
**Terminal:** `s_poincare_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_bounded_connected_lipschitz_domain, s_sobolev_space_W_1p_on_domain⟩` --[t_reductio_ad_absurdum {assume: sequence_violating_with_||f_n||_=1_and_||grad_f_n||_to_zero}]--> output: `s_normalized_sequence_with_vanishing_gradient`
2. input: `s_normalized_sequence_with_vanishing_gradient` --[t_compactness_argument {Rellich: subsequence_converging_in_Lp}]--> output: `s_Lp_limit_with_zero_gradient_so_constant`
3. input: `s_Lp_limit_with_zero_gradient_so_constant` --[t_reduce_to_canonical_form {mean_zero_constraint_implies_zero_limit_contradiction}]--> output: `s_poincare_inequality`

**Techniques used:** t_reductio_ad_absurdum, t_compactness_argument, t_reduce_to_canonical_form

---

### Hardy–Littlewood–Sobolev inequality (cite: https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood%E2%80%93Sobolev_inequality)

**Axioms:** `s_lp_function_on_Rn`, `s_Riesz_potential_kernel_|x|^{-alpha}`
**Terminal:** `s_hardy_littlewood_sobolev_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_lp_function_on_Rn, s_Riesz_potential_kernel_|x|^{-alpha}⟩` --[t_auxiliary_construction {layer_cake: rearrangement_to_radially_decreasing}]--> output: `s_symmetrized_radial_problem`
2. input: `s_symmetrized_radial_problem` --[t_rescale_for_asymptotic_geometry {scale_invariance: critical_exponents}]--> output: `s_scale_critical_setup`
3. input: `s_scale_critical_setup` --[t_interpolate_and_continue {via: Marcinkiewicz_between_endpoints}]--> output: `s_hardy_littlewood_sobolev_inequality`

**Techniques used:** t_auxiliary_construction, t_rescale_for_asymptotic_geometry, t_interpolate_and_continue

---

### Gagliardo–Nirenberg interpolation inequality (cite: https://en.wikipedia.org/wiki/Gagliardo%E2%80%93Nirenberg_interpolation_inequality)

**Axioms:** `s_smooth_compactly_supported_function_on_Rn`, `s_sobolev_norms_with_mixed_orders`
**Terminal:** `s_gagliardo_nirenberg_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_compactly_supported_function_on_Rn, s_sobolev_norms_with_mixed_orders⟩` --[t_frequency_decomposition {Littlewood_Paley: dyadic_pieces_f_j}]--> output: `s_dyadic_pieces_with_localized_frequency`
2. input: `s_dyadic_pieces_with_localized_frequency` --[t_interpolate_and_continue {pointwise_geometric_mean_of_two_norms}]--> output: `s_pointwise_interpolation_inequality`
3. input: `s_pointwise_interpolation_inequality` --[t_reduce_to_canonical_form {sum: dyadic_Lp_summation_via_Holder}]--> output: `s_gagliardo_nirenberg_inequality`

**Techniques used:** t_frequency_decomposition, t_interpolate_and_continue, t_reduce_to_canonical_form

---

### John–Nirenberg inequality (cite: https://en.wikipedia.org/wiki/John%E2%80%93Nirenberg_inequality)

**Axioms:** `s_bmo_function_on_Rn`, `s_cube_in_Rn`
**Terminal:** `s_john_nirenberg_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_bmo_function_on_Rn, s_cube_in_Rn⟩` --[t_auxiliary_construction {Calderon_Zygmund_stopping_at_threshold_lambda_||f||_BMO}]--> output: `s_stopping_cubes_at_threshold_lambda`
2. input: `s_stopping_cubes_at_threshold_lambda` --[t_contraction_fixed_point {iterate: cubes_have_2^n_lambda_geometric_decay}]--> output: `s_exponential_decay_of_distribution`
3. input: `s_exponential_decay_of_distribution` --[t_reduce_to_canonical_form {extract: exponential_decay_bound_for_oscillation}]--> output: `s_john_nirenberg_inequality`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_reduce_to_canonical_form

---

### Fefferman duality H¹–BMO (cite: https://en.wikipedia.org/wiki/Hardy_space#Duality)

**Axioms:** `s_hardy_space_H1_on_Rn`, `s_bmo_space_on_Rn`
**Terminal:** `s_fefferman_duality_H1_BMO` (kind: theorem)

**Steps:**
1. input: `⟨s_hardy_space_H1_on_Rn, s_bmo_space_on_Rn⟩` --[t_auxiliary_construction {atomic_decomposition: H1_atoms_with_cancellation}]--> output: `s_atomic_decomposition_of_H1`
2. input: `s_atomic_decomposition_of_H1` --[t_duality {pair_atom_with_BMO_via_Carleson_embedding}]--> output: `s_bounded_bilinear_pairing_BMO_times_H1`
3. input: `s_bounded_bilinear_pairing_BMO_times_H1` --[t_reduce_to_canonical_form {identify: every_H1_dual_functional_BMO}]--> output: `s_fefferman_duality_H1_BMO`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

