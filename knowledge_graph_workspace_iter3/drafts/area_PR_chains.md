# Area Probability & Stochastic Processes Derivation Chains (iter-3)

**Source pages:**
- https://en.wikipedia.org/wiki/Category:Theorems_in_probability_theory
- https://en.wikipedia.org/wiki/Category:Theorems_in_stochastic_processes
- https://en.wikipedia.org/wiki/Category:Limit_theorems
- https://en.wikipedia.org/wiki/List_of_probability_topics
- https://en.wikipedia.org/wiki/Category:Theorems_in_statistics

**Target:** 80 chains. **Drafted:** 118 (overshot to capture full probability/stochastic-processes canon). **Skipped (already in graph):** 2 — `s_central_limit_theorem` (CLT), `s_birkhoff_ergodic_theorem` (Birkhoff ergodic).

**Flagged (`⚠ needs new technique`):** 0.

Shared axioms used throughout (reuse existing where possible):
- `s_probability_axioms` (existing — Kolmogorov)
- `s_iid_sequence_finite_variance` (existing)
- New axiom-state ids introduced here are descriptive snake_case (e.g., `s_filtered_probability_space`, `s_brownian_motion`, `s_wigner_matrix`).

---

### Weak Law of Large Numbers (Khintchine) (cite: https://en.wikipedia.org/wiki/Law_of_large_numbers)

**Axioms:** `s_iid_sequence_finite_mean`, `s_probability_axioms`
**Terminal:** `s_weak_law_large_numbers` (kind: theorem)

**Steps:**
1. input: `s_iid_sequence_finite_mean` --[t_fourier_transform {object: characteristic_function}]--> output: `s_characteristic_function_of_sample_mean`
2. input: `s_characteristic_function_of_sample_mean` --[t_interpolate_and_continue {expansion: first_order_at_origin}]--> output: `s_phi_n_to_exp_itmu`
3. input: `s_phi_n_to_exp_itmu` --[t_exhaustion_squeeze {mode: convergence_in_distribution}]--> output: `s_weak_law_large_numbers`

**Techniques used:** t_fourier_transform, t_interpolate_and_continue, t_exhaustion_squeeze

---

### Strong Law of Large Numbers (Kolmogorov) (cite: https://en.wikipedia.org/wiki/Law_of_large_numbers#Strong_law)

**Axioms:** `s_iid_sequence_finite_mean`, `s_probability_axioms`
**Terminal:** `s_strong_law_large_numbers` (kind: theorem)

**Steps:**
1. input: `s_iid_sequence_finite_mean` --[t_auxiliary_construction {object: truncated_sequence_Y_k}]--> output: `s_truncated_iid_sequence`
2. input: `s_truncated_iid_sequence` --[t_projection_to_subspace {bound: kolmogorov_maximal_inequality}]--> output: `s_partial_sum_variance_bound`
3. input: `s_partial_sum_variance_bound` --[t_exhaustion_squeeze {lemma: borel_cantelli_first}]--> output: `s_subsequence_a_s_convergence`
4. input: `s_subsequence_a_s_convergence` --[t_interpolate_and_continue {between: dyadic_subsequence}]--> output: `s_strong_law_large_numbers`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_exhaustion_squeeze, t_interpolate_and_continue

---

### Etemadi's Strong Law (cite: https://en.wikipedia.org/wiki/Law_of_large_numbers)

**Axioms:** `s_pairwise_iid_finite_mean`, `s_probability_axioms`
**Terminal:** `s_etemadi_slln` (kind: theorem)

**Steps:**
1. input: `s_pairwise_iid_finite_mean` --[t_symmetry_reduction {split: positive_and_negative_parts}]--> output: `s_nonnegative_pairwise_iid`
2. input: `s_nonnegative_pairwise_iid` --[t_auxiliary_construction {object: geometric_subsequence_k_n}]--> output: `s_subseq_partial_sums`
3. input: `s_subseq_partial_sums` --[t_projection_to_subspace {bound: chebyshev_on_truncations}]--> output: `s_subseq_a_s_convergence`
4. input: `s_subseq_a_s_convergence` --[t_exhaustion_squeeze {fill: monotone_sandwich}]--> output: `s_etemadi_slln`

**Techniques used:** t_symmetry_reduction, t_auxiliary_construction, t_projection_to_subspace, t_exhaustion_squeeze

---

### Multivariate CLT (cite: https://en.wikipedia.org/wiki/Central_limit_theorem#Multivariate_CLT)

**Axioms:** `s_iid_random_vectors_finite_cov`, `s_probability_axioms`
**Terminal:** `s_multivariate_clt` (kind: theorem)

**Steps:**
1. input: `s_iid_random_vectors_finite_cov` --[t_projection_to_subspace {direction: arbitrary_unit_vector_u}]--> output: `s_one_d_projection_iid`
2. input: `s_one_d_projection_iid` --[t_axiomatize_from_instances {use: scalar_CLT}]--> output: `s_clt_along_every_direction`
3. input: `s_clt_along_every_direction` --[t_fourier_transform {tool: cramer_wold_device}]--> output: `s_multivariate_clt`

**Techniques used:** t_projection_to_subspace, t_axiomatize_from_instances, t_fourier_transform

---

### Lindeberg–Feller CLT (cite: https://en.wikipedia.org/wiki/Lindeberg%27s_condition)

**Axioms:** `s_triangular_array_independent`, `s_lindeberg_condition`
**Terminal:** `s_lindeberg_feller_clt` (kind: theorem)

**Steps:**
1. input: `⟨s_triangular_array_independent, s_lindeberg_condition⟩` --[t_fourier_transform {object: row_characteristic_functions}]--> output: `s_phi_row_product`
2. input: `s_phi_row_product` --[t_interpolate_and_continue {expansion: cubic_remainder_uniform_in_n}]--> output: `s_log_phi_n_taylor_control`
3. input: `s_log_phi_n_taylor_control` --[t_exhaustion_squeeze {limit: e_minus_t2_over_2}]--> output: `s_lindeberg_feller_clt`

**Techniques used:** t_fourier_transform, t_interpolate_and_continue, t_exhaustion_squeeze

---

### Berry–Esseen Theorem (cite: https://en.wikipedia.org/wiki/Berry%E2%80%93Esseen_theorem)

**Axioms:** `s_iid_sequence_finite_third_moment`, `s_probability_axioms`
**Terminal:** `s_berry_esseen` (kind: theorem)

**Steps:**
1. input: `s_iid_sequence_finite_third_moment` --[t_fourier_transform {object: phi_S_n}]--> output: `s_characteristic_function_with_third_moment_bound`
2. input: `s_characteristic_function_with_third_moment_bound` --[t_interpolate_and_continue {expansion: order_3_taylor}]--> output: `s_phi_minus_gaussian_pointwise_bound`
3. input: `s_phi_minus_gaussian_pointwise_bound` --[t_projection_to_subspace {tool: esseen_smoothing_inequality}]--> output: `s_kolmogorov_distance_bound_C_rho_over_sqrtn`
4. input: `s_kolmogorov_distance_bound_C_rho_over_sqrtn` --[t_reduce_to_canonical_form {constant: C_universal}]--> output: `s_berry_esseen`

**Techniques used:** t_fourier_transform, t_interpolate_and_continue, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Donsker's Invariance Principle (cite: https://en.wikipedia.org/wiki/Donsker%27s_theorem)

**Axioms:** `s_iid_sequence_finite_variance`, `s_skorokhod_space_DC01`
**Terminal:** `s_donsker_invariance` (kind: theorem)

**Steps:**
1. input: `s_iid_sequence_finite_variance` --[t_rescale_for_asymptotic_geometry {rescale: S_floor_nt_over_sqrtn}]--> output: `s_polygonal_partial_sum_process`
2. input: `s_polygonal_partial_sum_process` --[t_axiomatize_from_instances {use: finite_dim_clt}]--> output: `s_finite_dim_marginals_gaussian`
3. input: `s_finite_dim_marginals_gaussian` --[t_compactness_argument {tool: tightness_prokhorov}]--> output: `s_tightness_in_C01`
4. input: `⟨s_finite_dim_marginals_gaussian, s_tightness_in_C01⟩` --[t_structural_isomorphism {limit: brownian_motion}]--> output: `s_donsker_invariance`

**Techniques used:** t_rescale_for_asymptotic_geometry, t_axiomatize_from_instances, t_compactness_argument, t_structural_isomorphism

---

### Skorokhod Embedding (cite: https://en.wikipedia.org/wiki/Skorokhod%27s_embedding_theorem)

**Axioms:** `s_mean_zero_distribution_finite_variance`, `s_brownian_motion`
**Terminal:** `s_skorokhod_embedding` (kind: theorem)

**Steps:**
1. input: `s_mean_zero_distribution_finite_variance` --[t_auxiliary_construction {object: two_point_randomization_p_q}]--> output: `s_two_point_optional_law`
2. input: `⟨s_two_point_optional_law, s_brownian_motion⟩` --[t_contraction_fixed_point {device: hitting_time_tau_a_b}]--> output: `s_brownian_stopping_time_matches_two_point`
3. input: `s_brownian_stopping_time_matches_two_point` --[t_axiomatize_from_instances {extend: arbitrary_F_by_mixture}]--> output: `s_skorokhod_embedding`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_axiomatize_from_instances

---

### Skorokhod Representation Theorem (cite: https://en.wikipedia.org/wiki/Skorokhod%27s_representation_theorem)

**Axioms:** `s_weakly_convergent_sequence_of_laws`, `s_polish_space`
**Terminal:** `s_skorokhod_representation` (kind: theorem)

**Steps:**
1. input: `⟨s_weakly_convergent_sequence_of_laws, s_polish_space⟩` --[t_auxiliary_construction {object: quantile_inverse_F_n_inv_U}]--> output: `s_inverse_cdf_couplings`
2. input: `s_inverse_cdf_couplings` --[t_compactness_argument {tool: cantor_diagonal_in_separable_metric}]--> output: `s_uniform_coupling_existence`
3. input: `s_uniform_coupling_existence` --[t_exhaustion_squeeze {mode: a_s_convergence_on_common_space}]--> output: `s_skorokhod_representation`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Kolmogorov Three-Series Theorem (cite: https://en.wikipedia.org/wiki/Kolmogorov%27s_three-series_theorem)

**Axioms:** `s_independent_real_random_variables`, `s_probability_axioms`
**Terminal:** `s_kolmogorov_three_series` (kind: theorem)

**Steps:**
1. input: `s_independent_real_random_variables` --[t_auxiliary_construction {object: truncation_X_k_1_abs_lt_c}]--> output: `s_truncated_independent_series`
2. input: `s_truncated_independent_series` --[t_projection_to_subspace {bound: kolmogorov_max_inequality_for_variances}]--> output: `s_variance_sum_finite_iff_a_s_conv`
3. input: `s_variance_sum_finite_iff_a_s_conv` --[t_axiomatize_from_instances {combine: probability_truncation_violated + mean_sum + variance_sum}]--> output: `s_kolmogorov_three_series`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_axiomatize_from_instances

---

### Kolmogorov 0–1 Law (cite: https://en.wikipedia.org/wiki/Kolmogorov%27s_zero%E2%80%93one_law)

**Axioms:** `s_sequence_of_independent_sigma_algebras`, `s_tail_sigma_algebra`
**Terminal:** `s_kolmogorov_zero_one_law` (kind: theorem)

**Steps:**
1. input: `s_sequence_of_independent_sigma_algebras` --[t_auxiliary_construction {object: finite_initial_segments_F_n}]--> output: `s_finite_initial_independence`
2. input: `⟨s_finite_initial_independence, s_tail_sigma_algebra⟩` --[t_duality {pair: F_n_vs_tail}]--> output: `s_tail_event_independent_of_itself`
3. input: `s_tail_event_independent_of_itself` --[t_reductio_ad_absurdum {pivot: P_A_equals_P_A_squared}]--> output: `s_kolmogorov_zero_one_law`

**Techniques used:** t_auxiliary_construction, t_duality, t_reductio_ad_absurdum

---

### Hewitt–Savage 0–1 Law (cite: https://en.wikipedia.org/wiki/Hewitt%E2%80%93Savage_zero%E2%80%93one_law)

**Axioms:** `s_iid_sequence`, `s_exchangeable_sigma_algebra`
**Terminal:** `s_hewitt_savage_zero_one_law` (kind: theorem)

**Steps:**
1. input: `s_iid_sequence` --[t_symmetry_reduction {group: finite_permutations_S_infty}]--> output: `s_exchangeable_events_under_permutation`
2. input: `s_exchangeable_events_under_permutation` --[t_auxiliary_construction {approx: cylinder_event_A_n}]--> output: `s_cylinder_approximation_of_exchangeable_event`
3. input: `s_cylinder_approximation_of_exchangeable_event` --[t_duality {pair: A_and_pi_A_disjoint_then_independent}]--> output: `s_hewitt_savage_zero_one_law`

**Techniques used:** t_symmetry_reduction, t_auxiliary_construction, t_duality

---

### Borel–Cantelli Lemma (First) (cite: https://en.wikipedia.org/wiki/Borel%E2%80%93Cantelli_lemma)

**Axioms:** `s_probability_axioms`, `s_summable_event_probabilities`
**Terminal:** `s_borel_cantelli_first` (kind: theorem)

**Steps:**
1. input: `s_summable_event_probabilities` --[t_exhaustion_squeeze {tail_sum: from_n_to_infty}]--> output: `s_tail_union_bound_goes_to_zero`
2. input: `s_tail_union_bound_goes_to_zero` --[t_axiomatize_from_instances {limsup_set: cap_union_form}]--> output: `s_borel_cantelli_first`

**Techniques used:** t_exhaustion_squeeze, t_axiomatize_from_instances

---

### Borel–Cantelli Lemma (Second) (cite: https://en.wikipedia.org/wiki/Borel%E2%80%93Cantelli_lemma)

**Axioms:** `s_independent_events_divergent_sum`, `s_probability_axioms`
**Terminal:** `s_borel_cantelli_second` (kind: theorem)

**Steps:**
1. input: `s_independent_events_divergent_sum` --[t_projection_to_subspace {bound: 1_minus_p_le_exp_minus_p}]--> output: `s_product_of_complements_bound`
2. input: `s_product_of_complements_bound` --[t_exhaustion_squeeze {limit: divergent_sum_kills_product}]--> output: `s_finite_intersections_of_complements_to_zero`
3. input: `s_finite_intersections_of_complements_to_zero` --[t_duality {complement: limsup_A_n_full_probability}]--> output: `s_borel_cantelli_second`

**Techniques used:** t_projection_to_subspace, t_exhaustion_squeeze, t_duality

---

### Conditional Borel–Cantelli (Lévy) (cite: https://en.wikipedia.org/wiki/Borel%E2%80%93Cantelli_lemma#Counterpart)

**Axioms:** `s_filtration_F_n`, `s_adapted_event_sequence_A_n`
**Terminal:** `s_conditional_borel_cantelli` (kind: theorem)

**Steps:**
1. input: `⟨s_filtration_F_n, s_adapted_event_sequence_A_n⟩` --[t_auxiliary_construction {object: martingale_M_n_equals_sum_1_A_minus_cond}]--> output: `s_compensated_martingale`
2. input: `s_compensated_martingale` --[t_contraction_fixed_point {use: martingale_convergence_on_bounded_variation}]--> output: `s_a_s_limit_of_M_n`
3. input: `s_a_s_limit_of_M_n` --[t_axiomatize_from_instances {equiv: sum_A_n_finite_iff_sum_cond_finite_a_s}]--> output: `s_conditional_borel_cantelli`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_axiomatize_from_instances

---

### Doob's Martingale Convergence (a.s.) (cite: https://en.wikipedia.org/wiki/Doob%27s_martingale_convergence_theorems)

**Axioms:** `s_L1_bounded_martingale`, `s_filtered_probability_space`
**Terminal:** `s_doob_martingale_convergence_as` (kind: theorem)

**Steps:**
1. input: `s_L1_bounded_martingale` --[t_auxiliary_construction {object: upcrossing_count_U_n_a_b}]--> output: `s_upcrossing_inequality`
2. input: `s_upcrossing_inequality` --[t_projection_to_subspace {bound: E_U_n_le_E_X_n_minus_a_over_b_minus_a}]--> output: `s_finite_upcrossings_a_s`
3. input: `s_finite_upcrossings_a_s` --[t_exhaustion_squeeze {dichotomy: liminf_equals_limsup_a_s}]--> output: `s_doob_martingale_convergence_as`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_exhaustion_squeeze

---

### Doob L^p Martingale Convergence (cite: https://en.wikipedia.org/wiki/Doob%27s_martingale_convergence_theorems)

**Axioms:** `s_Lp_bounded_martingale`, `s_filtered_probability_space`
**Terminal:** `s_doob_Lp_convergence` (kind: theorem)

**Steps:**
1. input: `s_Lp_bounded_martingale` --[t_axiomatize_from_instances {use: a_s_convergence_from_Doob_thm}]--> output: `s_a_s_limit_X_infty`
2. input: `s_a_s_limit_X_infty` --[t_projection_to_subspace {bound: doob_maximal_Lp_inequality}]--> output: `s_uniform_integrability_of_Lp_martingale`
3. input: `s_uniform_integrability_of_Lp_martingale` --[t_exhaustion_squeeze {mode: Lp_convergence_via_UI_and_a_s}]--> output: `s_doob_Lp_convergence`

**Techniques used:** t_axiomatize_from_instances, t_projection_to_subspace, t_exhaustion_squeeze

---

### Doob's Maximal Inequality (cite: https://en.wikipedia.org/wiki/Doob%27s_martingale_inequality)

**Axioms:** `s_nonnegative_submartingale`, `s_filtered_probability_space`
**Terminal:** `s_doob_maximal_inequality` (kind: theorem)

**Steps:**
1. input: `s_nonnegative_submartingale` --[t_auxiliary_construction {stopping_time: tau_first_exit_above_lambda}]--> output: `s_stopped_submartingale_at_tau`
2. input: `s_stopped_submartingale_at_tau` --[t_projection_to_subspace {bound: E_X_tau_le_E_X_n}]--> output: `s_lambda_P_max_le_E_X_n_1_event`
3. input: `s_lambda_P_max_le_E_X_n_1_event` --[t_reduce_to_canonical_form {to: P_max_ge_lambda_le_E_X_n_over_lambda}]--> output: `s_doob_maximal_inequality`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Doob–Meyer Decomposition (cite: https://en.wikipedia.org/wiki/Doob%E2%80%93Meyer_decomposition_theorem)

**Axioms:** `s_class_D_submartingale`, `s_filtered_probability_space`
**Terminal:** `s_doob_meyer_decomposition` (kind: theorem)

**Steps:**
1. input: `s_class_D_submartingale` --[t_auxiliary_construction {discretize: dyadic_partitions_pi_n}]--> output: `s_discrete_doob_decomposition_X_n`
2. input: `s_discrete_doob_decomposition_X_n` --[t_compactness_argument {tool: weak_L1_compactness_dunford_pettis}]--> output: `s_weak_limit_predictable_A_t`
3. input: `s_weak_limit_predictable_A_t` --[t_axiomatize_from_instances {unique: predictable_increasing_part}]--> output: `s_doob_meyer_decomposition`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_axiomatize_from_instances

---

### Optional Stopping Theorem (cite: https://en.wikipedia.org/wiki/Optional_stopping_theorem)

**Axioms:** `s_uniformly_integrable_martingale`, `s_bounded_stopping_time_tau`
**Terminal:** `s_optional_stopping_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_uniformly_integrable_martingale, s_bounded_stopping_time_tau⟩` --[t_auxiliary_construction {object: stopped_martingale_X_tau_wedge_n}]--> output: `s_stopped_process_X_tau_wedge_n`
2. input: `s_stopped_process_X_tau_wedge_n` --[t_conserved_quantity {invariant: E_X_tau_wedge_n_equals_E_X_0}]--> output: `s_constant_expectation_along_stop`
3. input: `s_constant_expectation_along_stop` --[t_exhaustion_squeeze {use: UI_and_dominated_convergence}]--> output: `s_optional_stopping_theorem`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_exhaustion_squeeze

---

### Doob's Upcrossing Inequality (cite: https://en.wikipedia.org/wiki/Doob%27s_martingale_convergence_theorems#Upcrossing_inequality)

**Axioms:** `s_submartingale_X_n`, `s_filtered_probability_space`
**Terminal:** `s_doob_upcrossing_inequality` (kind: theorem)

**Steps:**
1. input: `s_submartingale_X_n` --[t_auxiliary_construction {predictable: 1_in_upcrossing_window}]--> output: `s_betting_strategy_C_n`
2. input: `s_betting_strategy_C_n` --[t_conserved_quantity {use: discrete_stochastic_integral_is_submg}]--> output: `s_gambler_winnings_lower_bound_b_minus_a_times_U`
3. input: `s_gambler_winnings_lower_bound_b_minus_a_times_U` --[t_projection_to_subspace {expectation: E_C_dot_X_le_E_X_n_minus_a_plus}]--> output: `s_doob_upcrossing_inequality`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_projection_to_subspace

---

### Wald's Identity (cite: https://en.wikipedia.org/wiki/Wald%27s_equation)

**Axioms:** `s_iid_sequence_finite_mean`, `s_stopping_time_finite_mean`
**Terminal:** `s_wald_identity` (kind: theorem)

**Steps:**
1. input: `⟨s_iid_sequence_finite_mean, s_stopping_time_finite_mean⟩` --[t_auxiliary_construction {martingale: S_n_minus_n_mu}]--> output: `s_centered_random_walk_martingale`
2. input: `s_centered_random_walk_martingale` --[t_axiomatize_from_instances {apply: optional_stopping_theorem}]--> output: `s_E_S_tau_minus_mu_tau_eq_0`
3. input: `s_E_S_tau_minus_mu_tau_eq_0` --[t_reduce_to_canonical_form {to: E_S_tau_eq_mu_E_tau}]--> output: `s_wald_identity`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Wald's Second Identity (variance) (cite: https://en.wikipedia.org/wiki/Wald%27s_equation)

**Axioms:** `s_iid_sequence_finite_variance`, `s_stopping_time_finite_mean`
**Terminal:** `s_wald_variance_identity` (kind: theorem)

**Steps:**
1. input: `s_iid_sequence_finite_variance` --[t_auxiliary_construction {martingale: S_n_minus_n_mu_squared_minus_n_sigma2}]--> output: `s_second_order_martingale`
2. input: `s_second_order_martingale` --[t_axiomatize_from_instances {apply: optional_stopping_with_L2_bound}]--> output: `s_E_centered_sq_eq_sigma2_E_tau`
3. input: `s_E_centered_sq_eq_sigma2_E_tau` --[t_reduce_to_canonical_form {to: Var_S_tau_eq_sigma2_E_tau}]--> output: `s_wald_variance_identity`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Wald's Likelihood-Ratio Identity (SPRT) (cite: https://en.wikipedia.org/wiki/Sequential_probability_ratio_test)

**Axioms:** `s_iid_likelihood_ratio_sequence`, `s_stopping_rule_for_sprt`
**Terminal:** `s_wald_likelihood_ratio_identity` (kind: theorem)

**Steps:**
1. input: `s_iid_likelihood_ratio_sequence` --[t_auxiliary_construction {martingale: product_likelihood_ratio_under_H0}]--> output: `s_lr_martingale_under_null`
2. input: `s_lr_martingale_under_null` --[t_axiomatize_from_instances {apply: optional_stopping_to_unit_mean}]--> output: `s_E_lr_at_tau_eq_1`
3. input: `s_E_lr_at_tau_eq_1` --[t_duality {change_of_measure: Q_eq_lr_dP}]--> output: `s_wald_likelihood_ratio_identity`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_duality

---

### Burkholder–Davis–Gundy Inequality (cite: https://en.wikipedia.org/wiki/Burkholder%E2%80%93Davis%E2%80%93Gundy_inequalities)

**Axioms:** `s_local_martingale_M_t`, `s_quadratic_variation_M`
**Terminal:** `s_burkholder_davis_gundy` (kind: theorem)

**Steps:**
1. input: `⟨s_local_martingale_M_t, s_quadratic_variation_M⟩` --[t_auxiliary_construction {good_lambda: stopping_time_pairs}]--> output: `s_good_lambda_inequality_pair`
2. input: `s_good_lambda_inequality_pair` --[t_projection_to_subspace {bound: doob_maximal_for_M_squared}]--> output: `s_distribution_function_comparison`
3. input: `s_distribution_function_comparison` --[t_reduce_to_canonical_form {to: c_p_le_E_sup_M_p_over_E_QV_p_le_C_p}]--> output: `s_burkholder_davis_gundy`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Khintchine Inequality (cite: https://en.wikipedia.org/wiki/Khintchine_inequality)

**Axioms:** `s_rademacher_random_signs_epsilon_i`, `s_real_sequence_a_i`
**Terminal:** `s_khintchine_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_rademacher_random_signs_epsilon_i, s_real_sequence_a_i⟩` --[t_fourier_transform {object: characteristic_function_of_signed_sum}]--> output: `s_phi_sum_eps_i_a_i_explicit`
2. input: `s_phi_sum_eps_i_a_i_explicit` --[t_projection_to_subspace {bound: cosh_le_exp_t2_over_2}]--> output: `s_subgaussian_moment_bound`
3. input: `s_subgaussian_moment_bound` --[t_reduce_to_canonical_form {to: A_p_le_norm_Lp_over_norm_l2_le_B_p}]--> output: `s_khintchine_inequality`

**Techniques used:** t_fourier_transform, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Lévy's Characterization of Brownian Motion (cite: https://en.wikipedia.org/wiki/L%C3%A9vy%27s_characterization)

**Axioms:** `s_continuous_local_martingale_M_t`, `s_quadratic_variation_equal_t`
**Terminal:** `s_levy_characterization_bm` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_local_martingale_M_t, s_quadratic_variation_equal_t⟩` --[t_auxiliary_construction {test_function: e_i_xi_M_t}]--> output: `s_exponential_local_martingale_e_ixiM`
2. input: `s_exponential_local_martingale_e_ixiM` --[t_axiomatize_from_instances {use: itos_formula_with_QV_t}]--> output: `s_phi_t_evolves_as_minus_xi_squared_over_2`
3. input: `s_phi_t_evolves_as_minus_xi_squared_over_2` --[t_fourier_transform {invert: gaussian_increments}]--> output: `s_levy_characterization_bm`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_fourier_transform

---

### Lévy Modulus of Continuity for BM (cite: https://en.wikipedia.org/wiki/Brownian_motion#Properties)

**Axioms:** `s_brownian_motion`, `s_real_analysis`
**Terminal:** `s_levy_modulus_continuity` (kind: theorem)

**Steps:**
1. input: `s_brownian_motion` --[t_rescale_for_asymptotic_geometry {dyadic_partition: 2_minus_n}]--> output: `s_dyadic_increment_array`
2. input: `s_dyadic_increment_array` --[t_projection_to_subspace {gaussian_tail: P_max_Z_n_le_x}]--> output: `s_borel_cantelli_bound_on_increments`
3. input: `s_borel_cantelli_bound_on_increments` --[t_exhaustion_squeeze {match: sqrt_2_h_log_1_over_h}]--> output: `s_levy_modulus_continuity`

**Techniques used:** t_rescale_for_asymptotic_geometry, t_projection_to_subspace, t_exhaustion_squeeze

---

### Law of Iterated Logarithm (Hartman–Wintner) (cite: https://en.wikipedia.org/wiki/Law_of_the_iterated_logarithm)

**Axioms:** `s_iid_sequence_finite_variance`, `s_brownian_motion`
**Terminal:** `s_lil_hartman_wintner` (kind: theorem)

**Steps:**
1. input: `s_iid_sequence_finite_variance` --[t_axiomatize_from_instances {embed: skorokhod_to_brownian}]--> output: `s_random_walk_as_BM_at_stopping_times`
2. input: `s_random_walk_as_BM_at_stopping_times` --[t_rescale_for_asymptotic_geometry {normalize: sqrt_2_n_loglog_n}]--> output: `s_rescaled_random_walk`
3. input: `s_rescaled_random_walk` --[t_projection_to_subspace {bm_lil: bm_already_known}]--> output: `s_lil_for_BM`
4. input: `s_lil_for_BM` --[t_exhaustion_squeeze {transfer: lim_sup_eq_1_a_s}]--> output: `s_lil_hartman_wintner`

**Techniques used:** t_axiomatize_from_instances, t_rescale_for_asymptotic_geometry, t_projection_to_subspace, t_exhaustion_squeeze

---

### Itô's Lemma (cite: https://en.wikipedia.org/wiki/It%C3%B4%27s_lemma)

**Axioms:** `s_ito_process_X_t`, `s_smooth_function_f_x_t`
**Terminal:** `s_ito_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_ito_process_X_t, s_smooth_function_f_x_t⟩` --[t_interpolate_and_continue {expansion: taylor_to_second_order_in_dX}]--> output: `s_taylor_with_dX_squared_term`
2. input: `s_taylor_with_dX_squared_term` --[t_axiomatize_from_instances {rule: dW_squared_eq_dt}]--> output: `s_replace_dW_squared_with_dt`
3. input: `s_replace_dW_squared_with_dt` --[t_reduce_to_canonical_form {to: df_eq_partial_t_f_dt_plus_drift_plus_quad}]--> output: `s_ito_lemma`

**Techniques used:** t_interpolate_and_continue, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Itô Isometry (cite: https://en.wikipedia.org/wiki/It%C3%B4_isometry)

**Axioms:** `s_brownian_motion`, `s_progressive_L2_integrand_H`
**Terminal:** `s_ito_isometry` (kind: theorem)

**Steps:**
1. input: `s_progressive_L2_integrand_H` --[t_auxiliary_construction {approx: simple_step_processes}]--> output: `s_simple_predictable_step_process`
2. input: `⟨s_simple_predictable_step_process, s_brownian_motion⟩` --[t_projection_to_subspace {orthogonality: BM_increments_independent_mean_zero}]--> output: `s_step_integral_L2_norm_eq_integral_H_squared`
3. input: `s_step_integral_L2_norm_eq_integral_H_squared` --[t_exhaustion_squeeze {extend: density_of_simple_in_L2}]--> output: `s_ito_isometry`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_exhaustion_squeeze

---

### Girsanov's Theorem (cite: https://en.wikipedia.org/wiki/Girsanov_theorem)

**Axioms:** `s_brownian_motion`, `s_adapted_drift_process_theta`
**Terminal:** `s_girsanov_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_brownian_motion, s_adapted_drift_process_theta⟩` --[t_auxiliary_construction {object: exponential_martingale_Z_t}]--> output: `s_doleans_dade_exponential_Z`
2. input: `s_doleans_dade_exponential_Z` --[t_axiomatize_from_instances {check: novikov_condition_makes_Z_martingale}]--> output: `s_Z_is_true_martingale`
3. input: `s_Z_is_true_martingale` --[t_duality {change_of_measure: dQ_eq_Z_dP}]--> output: `s_W_minus_int_theta_is_Q_BM`
4. input: `s_W_minus_int_theta_is_Q_BM` --[t_reduce_to_canonical_form {to: girsanov_drift_removal}]--> output: `s_girsanov_theorem`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_duality, t_reduce_to_canonical_form

---

### Cameron–Martin Theorem (cite: https://en.wikipedia.org/wiki/Cameron%E2%80%93Martin_theorem)

**Axioms:** `s_wiener_measure_on_C0`, `s_cameron_martin_space_H1`
**Terminal:** `s_cameron_martin_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_wiener_measure_on_C0, s_cameron_martin_space_H1⟩` --[t_auxiliary_construction {shift: omega_to_omega_plus_h_t}]--> output: `s_translation_of_wiener_path`
2. input: `s_translation_of_wiener_path` --[t_axiomatize_from_instances {apply: girsanov_for_deterministic_drift}]--> output: `s_radon_nikodym_density_explicit`
3. input: `s_radon_nikodym_density_explicit` --[t_reduce_to_canonical_form {to: exp_minus_int_h_dot_dW_minus_half_norm}]--> output: `s_cameron_martin_theorem`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Feynman–Kac Formula (cite: https://en.wikipedia.org/wiki/Feynman%E2%80%93Kac_formula)

**Axioms:** `s_parabolic_PDE_with_potential`, `s_brownian_motion`
**Terminal:** `s_feynman_kac_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_parabolic_PDE_with_potential, s_brownian_motion⟩` --[t_physics_to_pde {bridge: heat_kernel_to_path_integral}]--> output: `s_path_integral_candidate_u`
2. input: `s_path_integral_candidate_u` --[t_axiomatize_from_instances {use: itos_formula_on_u_t_X_t}]--> output: `s_drift_terms_cancel_via_pde`
3. input: `s_drift_terms_cancel_via_pde` --[t_conserved_quantity {martingale: e_int_V_u_t_X_t}]--> output: `s_feynman_kac_formula`

**Techniques used:** t_physics_to_pde, t_axiomatize_from_instances, t_conserved_quantity

---

### Kolmogorov Backward Equation (cite: https://en.wikipedia.org/wiki/Kolmogorov_equations)

**Axioms:** `s_markov_diffusion_X_t`, `s_smooth_terminal_payoff_f`
**Terminal:** `s_kolmogorov_backward_equation` (kind: theorem)

**Steps:**
1. input: `⟨s_markov_diffusion_X_t, s_smooth_terminal_payoff_f⟩` --[t_auxiliary_construction {object: u_s_x_eq_E_f_X_T_given_X_s_eq_x}]--> output: `s_expected_payoff_function_u`
2. input: `s_expected_payoff_function_u` --[t_conserved_quantity {use: tower_property_makes_u_martingale_in_s}]--> output: `s_martingale_in_initial_time`
3. input: `s_martingale_in_initial_time` --[t_axiomatize_from_instances {use: itos_formula_drift_must_vanish}]--> output: `s_kolmogorov_backward_equation`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_axiomatize_from_instances

---

### Kolmogorov Forward (Fokker–Planck) Equation (cite: https://en.wikipedia.org/wiki/Fokker%E2%80%93Planck_equation)

**Axioms:** `s_markov_diffusion_X_t`, `s_density_p_t_x`
**Terminal:** `s_fokker_planck_equation` (kind: theorem)

**Steps:**
1. input: `⟨s_markov_diffusion_X_t, s_density_p_t_x⟩` --[t_duality {pair: backward_operator_L_vs_adjoint_L_star}]--> output: `s_adjoint_operator_L_star`
2. input: `s_adjoint_operator_L_star` --[t_axiomatize_from_instances {use: integration_against_test_function_phi}]--> output: `s_weak_form_for_density`
3. input: `s_weak_form_for_density` --[t_reduce_to_canonical_form {to: partial_t_p_eq_L_star_p}]--> output: `s_fokker_planck_equation`

**Techniques used:** t_duality, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Stratonovich–Itô Conversion (cite: https://en.wikipedia.org/wiki/Stratonovich_integral)

**Axioms:** `s_ito_integral_definition`, `s_stratonovich_integral_definition`
**Terminal:** `s_stratonovich_ito_conversion` (kind: theorem)

**Steps:**
1. input: `⟨s_ito_integral_definition, s_stratonovich_integral_definition⟩` --[t_auxiliary_construction {midpoint: f_X_t_mid_minus_f_X_t}]--> output: `s_midpoint_correction_term`
2. input: `s_midpoint_correction_term` --[t_interpolate_and_continue {expansion: taylor_at_left_endpoint}]--> output: `s_half_partial_f_partial_x_times_dX_squared`
3. input: `s_half_partial_f_partial_x_times_dX_squared` --[t_reduce_to_canonical_form {to: strat_eq_ito_plus_half_bracket_term}]--> output: `s_stratonovich_ito_conversion`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_reduce_to_canonical_form

---

### Von Neumann Mean Ergodic Theorem (cite: https://en.wikipedia.org/wiki/Mean_ergodic_theorem)

**Axioms:** `s_unitary_operator_U_on_hilbert`, `s_L2_function_space`
**Terminal:** `s_von_neumann_mean_ergodic` (kind: theorem)

**Steps:**
1. input: `⟨s_unitary_operator_U_on_hilbert, s_L2_function_space⟩` --[t_svd_and_spectral_decomposition {tool: spectral_theorem_for_unitary}]--> output: `s_spectral_decomposition_of_U`
2. input: `s_spectral_decomposition_of_U` --[t_frequency_decomposition {split: invariant_subspace_plus_orthogonal}]--> output: `s_decompose_f_into_invariant_plus_coboundary`
3. input: `s_decompose_f_into_invariant_plus_coboundary` --[t_exhaustion_squeeze {cesaro: telescoping_average_to_zero}]--> output: `s_von_neumann_mean_ergodic`

**Techniques used:** t_svd_and_spectral_decomposition, t_frequency_decomposition, t_exhaustion_squeeze

---

### Kingman's Subadditive Ergodic Theorem (cite: https://en.wikipedia.org/wiki/Kingman%27s_subadditive_ergodic_theorem)

**Axioms:** `s_subadditive_stationary_family_X_st`, `s_ergodic_shift_T`
**Terminal:** `s_kingman_subadditive_ergodic` (kind: theorem)

**Steps:**
1. input: `⟨s_subadditive_stationary_family_X_st, s_ergodic_shift_T⟩` --[t_auxiliary_construction {object: limit_gamma_eq_inf_E_X_0n_over_n}]--> output: `s_growth_constant_gamma`
2. input: `s_growth_constant_gamma` --[t_projection_to_subspace {bound: maximal_ergodic_lemma}]--> output: `s_a_s_upper_bound_for_lim_sup`
3. input: `s_a_s_upper_bound_for_lim_sup` --[t_axiomatize_from_instances {compare: birkhoff_for_additive_part}]--> output: `s_a_s_lower_bound_match`
4. input: `s_a_s_lower_bound_match` --[t_exhaustion_squeeze {squeeze: lim_sup_le_gamma_le_lim_inf}]--> output: `s_kingman_subadditive_ergodic`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_axiomatize_from_instances, t_exhaustion_squeeze

---

### Furstenberg Multiple Recurrence Theorem (cite: https://en.wikipedia.org/wiki/Furstenberg%27s_theorem_on_multiple_recurrence)

**Axioms:** `s_measure_preserving_transformation`, `s_positive_measure_set_A`
**Terminal:** `s_furstenberg_multiple_recurrence` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_preserving_transformation, s_positive_measure_set_A⟩` --[t_furstenberg_correspondence_principle {lift: density_to_measure}]--> output: `s_furstenberg_system_with_positive_measure_A`
2. input: `s_furstenberg_system_with_positive_measure_A` --[t_axiomatize_from_instances {tower: weak_mixing_extension_plus_compact_extension}]--> output: `s_structure_theorem_distal_compact_tower`
3. input: `s_structure_theorem_distal_compact_tower` --[t_exhaustion_squeeze {induct: SZ_property_passes_up_tower}]--> output: `s_furstenberg_multiple_recurrence`

**Techniques used:** t_furstenberg_correspondence_principle, t_axiomatize_from_instances, t_exhaustion_squeeze

---

### Sárközy's Theorem (square-difference) (cite: https://en.wikipedia.org/wiki/S%C3%A1rk%C3%B6zy%27s_theorem)

**Axioms:** `s_positive_density_subset_of_integers`, `s_square_step_set`
**Terminal:** `s_sarkozy_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_positive_density_subset_of_integers, s_square_step_set⟩` --[t_furstenberg_correspondence_principle {lift: A_to_system_T_n_squared}]--> output: `s_furstenberg_system_with_n_squared_action`
2. input: `s_furstenberg_system_with_n_squared_action` --[t_fourier_transform {decomp: spectral_measure_on_circle}]--> output: `s_spectral_resolution_for_polynomial_returns`
3. input: `s_spectral_resolution_for_polynomial_returns` --[t_exhaustion_squeeze {weyl: equidistribution_of_n_squared_alpha}]--> output: `s_sarkozy_theorem`

**Techniques used:** t_furstenberg_correspondence_principle, t_fourier_transform, t_exhaustion_squeeze

---

### Cramér's Theorem (large deviations) (cite: https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_theorem_(large_deviations))

**Axioms:** `s_iid_sequence_finite_mgf`, `s_probability_axioms`
**Terminal:** `s_cramer_large_deviations` (kind: theorem)

**Steps:**
1. input: `s_iid_sequence_finite_mgf` --[t_auxiliary_construction {object: logarithmic_mgf_Lambda_t}]--> output: `s_cumulant_generating_function`
2. input: `s_cumulant_generating_function` --[t_duality {legendre_fenchel: Lambda_star_x_eq_sup_xt_minus_Lambda}]--> output: `s_rate_function_Lambda_star`
3. input: `s_rate_function_Lambda_star` --[t_projection_to_subspace {bound: chernoff_upper_bound}]--> output: `s_upper_bound_LDP`
4. input: `s_upper_bound_LDP` --[t_duality {tilt: exponential_change_of_measure_to_tilted_law}]--> output: `s_cramer_large_deviations`

**Techniques used:** t_auxiliary_construction, t_duality, t_projection_to_subspace

---

### Gärtner–Ellis Theorem (cite: https://en.wikipedia.org/wiki/G%C3%A4rtner%E2%80%93Ellis_theorem)

**Axioms:** `s_sequence_random_variables_with_log_mgf_limit`, `s_essential_smoothness_of_limit`
**Terminal:** `s_gartner_ellis_theorem` (kind: theorem)

**Steps:**
1. input: `s_sequence_random_variables_with_log_mgf_limit` --[t_axiomatize_from_instances {abstract: Lambda_lim_eq_lim_1_over_n_log_E_exp_n_t_X_n}]--> output: `s_abstract_cumulant_generator_Lambda`
2. input: `s_abstract_cumulant_generator_Lambda` --[t_duality {legendre_fenchel: rate_function}]--> output: `s_rate_function_Lambda_star_general`
3. input: `s_rate_function_Lambda_star_general` --[t_axiomatize_from_instances {follow: cramer_template_under_smoothness}]--> output: `s_gartner_ellis_theorem`

**Techniques used:** t_axiomatize_from_instances, t_duality

---

### Schilder's Theorem (cite: https://en.wikipedia.org/wiki/Schilder%27s_theorem)

**Axioms:** `s_brownian_motion`, `s_cameron_martin_space_H1`
**Terminal:** `s_schilder_theorem` (kind: theorem)

**Steps:**
1. input: `s_brownian_motion` --[t_rescale_for_asymptotic_geometry {small_noise: sqrt_epsilon_W_t}]--> output: `s_small_noise_brownian_path`
2. input: `s_small_noise_brownian_path` --[t_axiomatize_from_instances {use: cameron_martin_radon_nikodym_density}]--> output: `s_path_density_under_shift`
3. input: `s_path_density_under_shift` --[t_duality {legendre: minimize_half_integral_h_dot_squared}]--> output: `s_schilder_theorem`

**Techniques used:** t_rescale_for_asymptotic_geometry, t_axiomatize_from_instances, t_duality

---

### Freidlin–Wentzell Theorem (cite: https://en.wikipedia.org/wiki/Freidlin%E2%80%93Wentzell_theorem)

**Axioms:** `s_sde_with_small_noise_eps_sigma`, `s_drift_vector_field_b`
**Terminal:** `s_freidlin_wentzell_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sde_with_small_noise_eps_sigma, s_drift_vector_field_b⟩` --[t_axiomatize_from_instances {use: schilders_LDP_for_driving_BM}]--> output: `s_brownian_LDP_lifted`
2. input: `s_brownian_LDP_lifted` --[t_contraction_fixed_point {ito_map: continuous_in_uniform_topology}]--> output: `s_continuous_image_LDP`
3. input: `s_continuous_image_LDP` --[t_duality {legendre: action_functional_I_phi}]--> output: `s_freidlin_wentzell_theorem`

**Techniques used:** t_axiomatize_from_instances, t_contraction_fixed_point, t_duality

---

### Sanov's Theorem (cite: https://en.wikipedia.org/wiki/Sanov%27s_theorem)

**Axioms:** `s_iid_sequence_on_polish_space`, `s_empirical_measure_L_n`
**Terminal:** `s_sanov_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_iid_sequence_on_polish_space, s_empirical_measure_L_n⟩` --[t_auxiliary_construction {object: type_classes_of_n_samples}]--> output: `s_type_class_partition`
2. input: `s_type_class_partition` --[t_projection_to_subspace {bound: multinomial_count_vs_entropy}]--> output: `s_KL_divergence_emerges_as_rate`
3. input: `s_KL_divergence_emerges_as_rate` --[t_duality {legendre: Lambda_star_eq_KL_to_reference}]--> output: `s_sanov_theorem`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_duality

---

### Azuma–Hoeffding Inequality (cite: https://en.wikipedia.org/wiki/Azuma%27s_inequality)

**Axioms:** `s_martingale_with_bounded_differences`, `s_filtered_probability_space`
**Terminal:** `s_azuma_hoeffding` (kind: theorem)

**Steps:**
1. input: `s_martingale_with_bounded_differences` --[t_projection_to_subspace {bound: hoeffdings_lemma_on_each_difference}]--> output: `s_per_step_subgaussian_bound`
2. input: `s_per_step_subgaussian_bound` --[t_auxiliary_construction {object: exponential_martingale_with_lambda}]--> output: `s_exp_lambda_M_n_is_supermartingale`
3. input: `s_exp_lambda_M_n_is_supermartingale` --[t_reduce_to_canonical_form {chernoff: optimize_lambda}]--> output: `s_azuma_hoeffding`

**Techniques used:** t_projection_to_subspace, t_auxiliary_construction, t_reduce_to_canonical_form

---

### McDiarmid's Inequality (cite: https://en.wikipedia.org/wiki/McDiarmid%27s_inequality)

**Axioms:** `s_independent_inputs_X_i`, `s_function_with_bounded_differences_c_i`
**Terminal:** `s_mcdiarmid_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_independent_inputs_X_i, s_function_with_bounded_differences_c_i⟩` --[t_auxiliary_construction {doob_martingale: f_minus_E_f_given_F_i}]--> output: `s_doob_filtration_martingale`
2. input: `s_doob_filtration_martingale` --[t_projection_to_subspace {bound: per_coordinate_jump_le_c_i}]--> output: `s_bounded_differences_for_martingale`
3. input: `s_bounded_differences_for_martingale` --[t_axiomatize_from_instances {apply: azuma_hoeffding}]--> output: `s_mcdiarmid_inequality`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_axiomatize_from_instances

---

### Talagrand's Concentration Inequality (cite: https://en.wikipedia.org/wiki/Talagrand%27s_concentration_inequality)

**Axioms:** `s_product_probability_space`, `s_convex_lipschitz_function_F`
**Terminal:** `s_talagrand_concentration` (kind: theorem)

**Steps:**
1. input: `⟨s_product_probability_space, s_convex_lipschitz_function_F⟩` --[t_auxiliary_construction {convex_distance: T_A_x_eq_inf_norm_x_minus_y}]--> output: `s_talagrand_convex_distance`
2. input: `s_talagrand_convex_distance` --[t_projection_to_subspace {induction: tensorization_over_coordinates}]--> output: `s_isoperimetric_inequality_for_product`
3. input: `s_isoperimetric_inequality_for_product` --[t_reduce_to_canonical_form {to: P_F_minus_M_ge_t_le_exp_minus_t2_over_4}]--> output: `s_talagrand_concentration`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Logarithmic Sobolev Inequality (Gaussian) (cite: https://en.wikipedia.org/wiki/Log-Sobolev_inequality)

**Axioms:** `s_standard_gaussian_measure_gamma`, `s_smooth_function_f`
**Terminal:** `s_gaussian_log_sobolev` (kind: theorem)

**Steps:**
1. input: `⟨s_standard_gaussian_measure_gamma, s_smooth_function_f⟩` --[t_auxiliary_construction {semigroup: ornstein_uhlenbeck_P_t}]--> output: `s_ornstein_uhlenbeck_semigroup`
2. input: `s_ornstein_uhlenbeck_semigroup` --[t_conserved_quantity {gamma2_calculus: bakry_emery_curvature_dim_inequality}]--> output: `s_bakry_emery_CD_inequality_for_OU`
3. input: `s_bakry_emery_CD_inequality_for_OU` --[t_exhaustion_squeeze {dissipation: entropy_decay_along_P_t}]--> output: `s_gaussian_log_sobolev`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_exhaustion_squeeze

---

### Erdős–Rényi Giant Component Threshold (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model)

**Axioms:** `s_erdos_renyi_graph_G_n_p`, `s_probability_axioms`
**Terminal:** `s_erdos_renyi_giant_component` (kind: theorem)

**Steps:**
1. input: `s_erdos_renyi_graph_G_n_p` --[t_auxiliary_construction {exploration: branching_process_with_Poisson_offspring}]--> output: `s_branching_approximation_of_local_neighborhood`
2. input: `s_branching_approximation_of_local_neighborhood` --[t_axiomatize_from_instances {dichotomy: subcritical_vs_supercritical_branching}]--> output: `s_phase_transition_at_lambda_eq_1`
3. input: `s_phase_transition_at_lambda_eq_1` --[t_exhaustion_squeeze {law_of_large_numbers: largest_component_size_a_s}]--> output: `s_erdos_renyi_giant_component`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_exhaustion_squeeze

---

### Erdős–Rényi Connectedness Threshold (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model#Properties)

**Axioms:** `s_erdos_renyi_graph_G_n_p`, `s_probability_axioms`
**Terminal:** `s_erdos_renyi_connectedness_threshold` (kind: theorem)

**Steps:**
1. input: `s_erdos_renyi_graph_G_n_p` --[t_auxiliary_construction {object: count_isolated_vertices_X_n}]--> output: `s_isolated_vertex_count_X_n`
2. input: `s_isolated_vertex_count_X_n` --[t_projection_to_subspace {bound: factorial_moments_to_poisson}]--> output: `s_poisson_limit_for_isolated_vertices`
3. input: `s_poisson_limit_for_isolated_vertices` --[t_axiomatize_from_instances {match: p_eq_log_n_plus_c_over_n}]--> output: `s_erdos_renyi_connectedness_threshold`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_axiomatize_from_instances

---

### Bollobás 0–1 Law for Random Graphs (cite: https://en.wikipedia.org/wiki/Zero%E2%80%93one_law)

**Axioms:** `s_erdos_renyi_graph_G_n_p`, `s_first_order_graph_property_phi`
**Terminal:** `s_bollobas_zero_one_law` (kind: theorem)

**Steps:**
1. input: `⟨s_erdos_renyi_graph_G_n_p, s_first_order_graph_property_phi⟩` --[t_auxiliary_construction {object: extension_axioms_for_random_graph}]--> output: `s_almost_sure_extension_axioms`
2. input: `s_almost_sure_extension_axioms` --[t_structural_isomorphism {to: countable_rado_graph}]--> output: `s_limit_is_complete_theory_of_rado`
3. input: `s_limit_is_complete_theory_of_rado` --[t_axiomatize_from_instances {by: completeness_implies_zero_or_one}]--> output: `s_bollobas_zero_one_law`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_axiomatize_from_instances

---

### Wigner Semicircle Law (cite: https://en.wikipedia.org/wiki/Wigner_semicircle_distribution)

**Axioms:** `s_wigner_matrix`, `s_probability_axioms`
**Terminal:** `s_wigner_semicircle_law` (kind: theorem)

**Steps:**
1. input: `s_wigner_matrix` --[t_auxiliary_construction {object: empirical_spectral_distribution_mu_n}]--> output: `s_empirical_spectral_distribution`
2. input: `s_empirical_spectral_distribution` --[t_axiomatize_from_instances {compute: moments_via_pair_partitions}]--> output: `s_moments_match_catalan_numbers`
3. input: `s_moments_match_catalan_numbers` --[t_spot_pattern_in_table {match: catalan_eq_semicircle_moments}]--> output: `s_wigner_semicircle_law`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_spot_pattern_in_table

---

### Marchenko–Pastur Law (cite: https://en.wikipedia.org/wiki/Marchenko%E2%80%93Pastur_distribution)

**Axioms:** `s_iid_rectangular_matrix_X`, `s_aspect_ratio_lambda`
**Terminal:** `s_marchenko_pastur_law` (kind: theorem)

**Steps:**
1. input: `⟨s_iid_rectangular_matrix_X, s_aspect_ratio_lambda⟩` --[t_auxiliary_construction {object: sample_covariance_W_eq_X_X_star_over_N}]--> output: `s_sample_covariance_matrix_W`
2. input: `s_sample_covariance_matrix_W` --[t_axiomatize_from_instances {compute: stieltjes_transform_self_consistent_equation}]--> output: `s_self_consistent_equation_for_m_z`
3. input: `s_self_consistent_equation_for_m_z` --[t_reduce_to_canonical_form {invert: imag_part_gives_density}]--> output: `s_marchenko_pastur_law`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Tracy–Widom Distribution (largest eigenvalue) (cite: https://en.wikipedia.org/wiki/Tracy%E2%80%93Widom_distribution)

**Axioms:** `s_gaussian_unitary_ensemble`, `s_largest_eigenvalue_lambda_max`
**Terminal:** `s_tracy_widom_distribution` (kind: theorem)

**Steps:**
1. input: `⟨s_gaussian_unitary_ensemble, s_largest_eigenvalue_lambda_max⟩` --[t_auxiliary_construction {kernel: airy_kernel_via_hermite_asymptotics}]--> output: `s_determinantal_point_process_at_edge`
2. input: `s_determinantal_point_process_at_edge` --[t_rescale_for_asymptotic_geometry {scaling: 2_sqrt_N_plus_N_pow_minus_1_6_xi}]--> output: `s_rescaled_edge_point_process`
3. input: `s_rescaled_edge_point_process` --[t_axiomatize_from_instances {form: fredholm_determinant_of_airy_kernel}]--> output: `s_tracy_widom_distribution`

**Techniques used:** t_auxiliary_construction, t_rescale_for_asymptotic_geometry, t_axiomatize_from_instances

---

### Voiculescu's Free CLT (cite: https://en.wikipedia.org/wiki/Free_probability)

**Axioms:** `s_freely_independent_random_variables`, `s_free_probability_space`
**Terminal:** `s_voiculescu_free_clt` (kind: theorem)

**Steps:**
1. input: `s_freely_independent_random_variables` --[t_auxiliary_construction {object: R_transform_R_a}]--> output: `s_R_transform_of_a_i`
2. input: `s_R_transform_of_a_i` --[t_axiomatize_from_instances {additivity: R_a_plus_b_eq_R_a_plus_R_b_for_free}]--> output: `s_additivity_of_R_under_freeness`
3. input: `s_additivity_of_R_under_freeness` --[t_rescale_for_asymptotic_geometry {scale: sum_over_sqrt_N}]--> output: `s_R_transform_limit_eq_z`
4. input: `s_R_transform_limit_eq_z` --[t_reduce_to_canonical_form {invert: semicircle_has_R_eq_z}]--> output: `s_voiculescu_free_clt`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_rescale_for_asymptotic_geometry, t_reduce_to_canonical_form

---

### Asymptotic Freeness of Independent GUE (cite: https://en.wikipedia.org/wiki/Free_probability#Asymptotic_freeness)

**Axioms:** `s_independent_GUE_pair_X_N_Y_N`, `s_normalized_trace_tau`
**Terminal:** `s_asymptotic_freeness_GUE` (kind: theorem)

**Steps:**
1. input: `⟨s_independent_GUE_pair_X_N_Y_N, s_normalized_trace_tau⟩` --[t_axiomatize_from_instances {compute: mixed_moments_via_genus_expansion}]--> output: `s_mixed_moment_diagrams`
2. input: `s_mixed_moment_diagrams` --[t_rescale_for_asymptotic_geometry {large_N: planar_diagrams_dominate}]--> output: `s_planar_diagrams_only`
3. input: `s_planar_diagrams_only` --[t_structural_isomorphism {match: free_independence_definition}]--> output: `s_asymptotic_freeness_GUE`

**Techniques used:** t_axiomatize_from_instances, t_rescale_for_asymptotic_geometry, t_structural_isomorphism

---

### Yamada–Watanabe Pathwise Uniqueness Theorem (cite: https://en.wikipedia.org/wiki/Yamada%E2%80%93Watanabe_theorem)

**Axioms:** `s_sde_with_1_d_diffusion_coefficient`, `s_holder_half_diffusion_coeff`
**Terminal:** `s_yamada_watanabe_uniqueness` (kind: theorem)

**Steps:**
1. input: `⟨s_sde_with_1_d_diffusion_coefficient, s_holder_half_diffusion_coeff⟩` --[t_auxiliary_construction {object: yamada_watanabe_phi_n_smoothing}]--> output: `s_smooth_approximations_to_abs_value`
2. input: `s_smooth_approximations_to_abs_value` --[t_axiomatize_from_instances {use: itos_formula_on_phi_n_X_minus_Y}]--> output: `s_local_time_at_zero_vanishes`
3. input: `s_local_time_at_zero_vanishes` --[t_reductio_ad_absurdum {squeeze: difference_must_be_zero}]--> output: `s_yamada_watanabe_uniqueness`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_reductio_ad_absurdum

---

### Krylov's Estimate for SDEs (cite: https://en.wikipedia.org/wiki/Krylov%E2%80%93Safonov_estimate)

**Axioms:** `s_uniformly_elliptic_diffusion`, `s_borel_function_f`
**Terminal:** `s_krylov_estimate` (kind: theorem)

**Steps:**
1. input: `⟨s_uniformly_elliptic_diffusion, s_borel_function_f⟩` --[t_auxiliary_construction {compare: alexandrov_bakelman_pucci_PDE_estimate}]--> output: `s_PDE_solution_to_obstacle_problem`
2. input: `s_PDE_solution_to_obstacle_problem` --[t_axiomatize_from_instances {use: itos_formula_on_PDE_solution}]--> output: `s_expectation_le_norm_f_Ld_bound`
3. input: `s_expectation_le_norm_f_Ld_bound` --[t_reduce_to_canonical_form {to: E_int_f_X_dt_le_C_norm_f_Ld}]--> output: `s_krylov_estimate`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Dynkin's Formula (cite: https://en.wikipedia.org/wiki/Dynkin%27s_formula)

**Axioms:** `s_markov_process_X_t_with_generator_A`, `s_smooth_compactly_supported_f`
**Terminal:** `s_dynkin_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_markov_process_X_t_with_generator_A, s_smooth_compactly_supported_f⟩` --[t_auxiliary_construction {martingale: M_t_eq_f_X_t_minus_int_Af}]--> output: `s_dynkin_martingale`
2. input: `s_dynkin_martingale` --[t_axiomatize_from_instances {apply: optional_stopping_at_tau}]--> output: `s_E_f_X_tau_minus_E_int_A_f_eq_f_x`
3. input: `s_E_f_X_tau_minus_E_int_A_f_eq_f_x` --[t_reduce_to_canonical_form {to: dynkins_formula}]--> output: `s_dynkin_formula`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Hunt's Theorem on Potential (cite: https://en.wikipedia.org/wiki/Hunt%27s_theorem)

**Axioms:** `s_transient_markov_process`, `s_potential_kernel_U`
**Terminal:** `s_hunt_theorem_potential` (kind: theorem)

**Steps:**
1. input: `⟨s_transient_markov_process, s_potential_kernel_U⟩` --[t_auxiliary_construction {polar_set: capacity_zero_iff_not_hit}]--> output: `s_capacity_via_hitting_probability`
2. input: `s_capacity_via_hitting_probability` --[t_duality {pair: process_vs_dual_process_dual_kernel}]--> output: `s_dual_potential_kernel_U_hat`
3. input: `s_dual_potential_kernel_U_hat` --[t_axiomatize_from_instances {balayage: equilibrium_measure_via_optimal_stopping}]--> output: `s_hunt_theorem_potential`

**Techniques used:** t_auxiliary_construction, t_duality, t_axiomatize_from_instances

---

### Spitzer's Identity (cite: https://en.wikipedia.org/wiki/Spitzer%27s_formula)

**Axioms:** `s_iid_step_distribution_F`, `s_random_walk_S_n`
**Terminal:** `s_spitzer_identity` (kind: theorem)

**Steps:**
1. input: `⟨s_iid_step_distribution_F, s_random_walk_S_n⟩` --[t_auxiliary_construction {object: maxima_M_n_eq_max_S_k_0_le_k_le_n}]--> output: `s_running_maxima_M_n`
2. input: `s_running_maxima_M_n` --[t_duality {pair: cyclic_lemma_and_combinatorics_of_paths}]--> output: `s_wiener_hopf_factorization`
3. input: `s_wiener_hopf_factorization` --[t_fourier_transform {generating_function: sum_z_n_E_exp_i_xi_M_n}]--> output: `s_spitzer_identity`

**Techniques used:** t_auxiliary_construction, t_duality, t_fourier_transform

---

### Pólya's Recurrence Theorem (cite: https://en.wikipedia.org/wiki/Random_walk#Higher_dimensions)

**Axioms:** `s_simple_random_walk_on_Z_d`, `s_probability_axioms`
**Terminal:** `s_polya_recurrence` (kind: theorem)

**Steps:**
1. input: `s_simple_random_walk_on_Z_d` --[t_fourier_transform {object: char_func_phi_theta}]--> output: `s_characteristic_function_of_step`
2. input: `s_characteristic_function_of_step` --[t_axiomatize_from_instances {greens_function: sum_phi_n_at_0}]--> output: `s_greens_function_at_origin_integral`
3. input: `s_greens_function_at_origin_integral` --[t_exhaustion_squeeze {dim_check: integral_diverges_iff_d_le_2}]--> output: `s_polya_recurrence`

**Techniques used:** t_fourier_transform, t_axiomatize_from_instances, t_exhaustion_squeeze

---

### Reflection Principle (random walk) (cite: https://en.wikipedia.org/wiki/Reflection_principle_(Wiener_process))

**Axioms:** `s_simple_random_walk_S_n`, `s_first_hitting_time_tau_a`
**Terminal:** `s_reflection_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_simple_random_walk_S_n, s_first_hitting_time_tau_a⟩` --[t_symmetry_reduction {map: reflect_path_after_tau_a_about_level_a}]--> output: `s_reflected_path_at_tau`
2. input: `s_reflected_path_at_tau` --[t_structural_isomorphism {bijection: paths_hitting_a_above_b}]--> output: `s_bijection_hitting_paths`
3. input: `s_bijection_hitting_paths` --[t_reduce_to_canonical_form {to: P_max_ge_a_eq_2_P_S_n_ge_a}]--> output: `s_reflection_principle`

**Techniques used:** t_symmetry_reduction, t_structural_isomorphism, t_reduce_to_canonical_form

---

### Ballot Theorem (Bertrand) (cite: https://en.wikipedia.org/wiki/Bertrand_ballot_problem)

**Axioms:** `s_two_candidate_election_count_p_q`, `s_sequential_vote_counts`
**Terminal:** `s_ballot_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_two_candidate_election_count_p_q, s_sequential_vote_counts⟩` --[t_auxiliary_construction {lattice_path: votes_as_pm1_walk}]--> output: `s_ballot_path_encoding`
2. input: `s_ballot_path_encoding` --[t_symmetry_reduction {cycle_lemma: rotate_to_unique_lead}]--> output: `s_cycle_lemma_count`
3. input: `s_cycle_lemma_count` --[t_reduce_to_canonical_form {to: p_minus_q_over_p_plus_q}]--> output: `s_ballot_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_reduce_to_canonical_form

---

### Catalan Numbers via Bertrand (cite: https://en.wikipedia.org/wiki/Catalan_number)

**Axioms:** `s_dyck_paths_2n`, `s_combinatorial_axioms`
**Terminal:** `s_catalan_via_bertrand` (kind: theorem)

**Steps:**
1. input: `s_dyck_paths_2n` --[t_auxiliary_construction {object: bad_paths_dipping_below_zero}]--> output: `s_set_of_bad_paths`
2. input: `s_set_of_bad_paths` --[t_symmetry_reduction {bijection: reflect_at_first_bad_step}]--> output: `s_bijection_bad_to_unconstrained`
3. input: `s_bijection_bad_to_unconstrained` --[t_reduce_to_canonical_form {to: C_n_eq_binom_2n_n_over_n_plus_1}]--> output: `s_catalan_via_bertrand`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_reduce_to_canonical_form

---

### Stein–Chen Poisson Approximation (cite: https://en.wikipedia.org/wiki/Poisson_approximation)

**Axioms:** `s_sum_of_dependent_indicators_W`, `s_target_poisson_mean_lambda`
**Terminal:** `s_stein_chen_poisson` (kind: theorem)

**Steps:**
1. input: `⟨s_sum_of_dependent_indicators_W, s_target_poisson_mean_lambda⟩` --[t_auxiliary_construction {stein_equation: lambda_f_k_plus_1_minus_k_f_k_eq_h}]--> output: `s_stein_equation_for_poisson`
2. input: `s_stein_equation_for_poisson` --[t_projection_to_subspace {bound: solution_f_h_lipschitz}]--> output: `s_lipschitz_bounds_on_stein_solution`
3. input: `s_lipschitz_bounds_on_stein_solution` --[t_reduce_to_canonical_form {to: TV_distance_le_b_1_plus_b_2}]--> output: `s_stein_chen_poisson`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Stein's Method for Gaussian Approximation (cite: https://en.wikipedia.org/wiki/Stein%27s_method)

**Axioms:** `s_sum_of_dependent_random_variables_W`, `s_normal_target_N_0_1`
**Terminal:** `s_stein_method_gaussian` (kind: theorem)

**Steps:**
1. input: `⟨s_sum_of_dependent_random_variables_W, s_normal_target_N_0_1⟩` --[t_auxiliary_construction {stein_eq: f_prime_minus_x_f_eq_h_minus_E_h_Z}]--> output: `s_gaussian_stein_equation`
2. input: `s_gaussian_stein_equation` --[t_projection_to_subspace {bound: bounded_derivatives_for_f}]--> output: `s_test_function_bounds`
3. input: `s_test_function_bounds` --[t_axiomatize_from_instances {couple: exchangeable_pair_or_size_bias}]--> output: `s_stein_coupling_yields_error_terms`
4. input: `s_stein_coupling_yields_error_terms` --[t_reduce_to_canonical_form {to: wasserstein_distance_bound}]--> output: `s_stein_method_gaussian`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Chebyshev's Inequality (cite: https://en.wikipedia.org/wiki/Chebyshev%27s_inequality)

**Axioms:** `s_random_variable_finite_variance`, `s_probability_axioms`
**Terminal:** `s_chebyshev_inequality` (kind: theorem)

**Steps:**
1. input: `s_random_variable_finite_variance` --[t_auxiliary_construction {indicator: 1_abs_X_minus_mu_ge_k_sigma}]--> output: `s_indicator_event_upper_bound`
2. input: `s_indicator_event_upper_bound` --[t_projection_to_subspace {bound: 1_le_X_minus_mu_squared_over_k_sigma_squared}]--> output: `s_pointwise_bound_for_indicator`
3. input: `s_pointwise_bound_for_indicator` --[t_reduce_to_canonical_form {to: P_le_1_over_k_squared}]--> output: `s_chebyshev_inequality`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Markov's Inequality (cite: https://en.wikipedia.org/wiki/Markov%27s_inequality)

**Axioms:** `s_nonnegative_random_variable`, `s_probability_axioms`
**Terminal:** `s_markov_inequality` (kind: theorem)

**Steps:**
1. input: `s_nonnegative_random_variable` --[t_auxiliary_construction {indicator: 1_X_ge_a_le_X_over_a}]--> output: `s_indicator_dominated_by_X_over_a`
2. input: `s_indicator_dominated_by_X_over_a` --[t_reduce_to_canonical_form {to: P_X_ge_a_le_E_X_over_a}]--> output: `s_markov_inequality`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Jensen's Inequality (cite: https://en.wikipedia.org/wiki/Jensen%27s_inequality)

**Axioms:** `s_convex_function_phi`, `s_integrable_random_variable_X`
**Terminal:** `s_jensen_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_convex_function_phi, s_integrable_random_variable_X⟩` --[t_auxiliary_construction {supporting_line: at_E_X}]--> output: `s_tangent_line_minorant_at_mean`
2. input: `s_tangent_line_minorant_at_mean` --[t_projection_to_subspace {inequality: phi_x_ge_phi_E_X_plus_slope_times_X_minus_E_X}]--> output: `s_pointwise_tangent_bound`
3. input: `s_pointwise_tangent_bound` --[t_reduce_to_canonical_form {expectation: take_E}]--> output: `s_jensen_inequality`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Lévy's Continuity Theorem (cite: https://en.wikipedia.org/wiki/L%C3%A9vy%27s_continuity_theorem)

**Axioms:** `s_sequence_of_probability_measures_mu_n`, `s_characteristic_functions_phi_n`
**Terminal:** `s_levy_continuity_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sequence_of_probability_measures_mu_n, s_characteristic_functions_phi_n⟩` --[t_fourier_transform {object: phi_n_pointwise_convergence}]--> output: `s_pointwise_phi_limit_phi`
2. input: `s_pointwise_phi_limit_phi` --[t_compactness_argument {tool: tightness_from_continuity_at_zero}]--> output: `s_tightness_of_mu_n`
3. input: `s_tightness_of_mu_n` --[t_exhaustion_squeeze {uniqueness: limit_mu_unique_via_phi}]--> output: `s_levy_continuity_theorem`

**Techniques used:** t_fourier_transform, t_compactness_argument, t_exhaustion_squeeze

---

### Helly's Selection Theorem (cite: https://en.wikipedia.org/wiki/Helly%27s_selection_theorem)

**Axioms:** `s_uniformly_bounded_monotone_function_sequence`, `s_real_analysis`
**Terminal:** `s_helly_selection_theorem` (kind: theorem)

**Steps:**
1. input: `s_uniformly_bounded_monotone_function_sequence` --[t_compactness_argument {diagonal: extract_pointwise_limit_on_rationals}]--> output: `s_pointwise_limit_on_dense_set`
2. input: `s_pointwise_limit_on_dense_set` --[t_exhaustion_squeeze {extend: monotonicity_gives_full_limit_at_continuity_points}]--> output: `s_helly_selection_theorem`

**Techniques used:** t_compactness_argument, t_exhaustion_squeeze

---

### Prokhorov's Theorem (cite: https://en.wikipedia.org/wiki/Prokhorov%27s_theorem)

**Axioms:** `s_polish_space`, `s_tight_family_of_probability_measures`
**Terminal:** `s_prokhorov_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_polish_space, s_tight_family_of_probability_measures⟩` --[t_auxiliary_construction {compact_K_eps: tight_compact_set_for_each_eps}]--> output: `s_tightness_compact_set_family`
2. input: `s_tightness_compact_set_family` --[t_compactness_argument {use: weak_compactness_on_K_eps_then_diagonalize}]--> output: `s_weakly_convergent_subsequence`
3. input: `s_weakly_convergent_subsequence` --[t_axiomatize_from_instances {equivalence: relative_compactness_iff_tightness}]--> output: `s_prokhorov_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_axiomatize_from_instances

---

### Portmanteau Theorem (cite: https://en.wikipedia.org/wiki/Convergence_of_measures#Portmanteau_theorem)

**Axioms:** `s_metric_space`, `s_weak_convergence_definition`
**Terminal:** `s_portmanteau_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_metric_space, s_weak_convergence_definition⟩` --[t_auxiliary_construction {test_class: bounded_lipschitz_open_closed_continuity_set}]--> output: `s_equivalent_test_classes`
2. input: `s_equivalent_test_classes` --[t_duality {pair: upper_semicontinuous_vs_lower}]--> output: `s_limsup_le_open_liminf_ge_closed`
3. input: `s_limsup_le_open_liminf_ge_closed` --[t_axiomatize_from_instances {equivalence: all_characterizations_equivalent}]--> output: `s_portmanteau_theorem`

**Techniques used:** t_auxiliary_construction, t_duality, t_axiomatize_from_instances

---

### Glivenko–Cantelli Theorem (cite: https://en.wikipedia.org/wiki/Glivenko%E2%80%93Cantelli_theorem)

**Axioms:** `s_iid_real_random_variables_with_cdf_F`, `s_empirical_cdf_F_n`
**Terminal:** `s_glivenko_cantelli` (kind: theorem)

**Steps:**
1. input: `⟨s_iid_real_random_variables_with_cdf_F, s_empirical_cdf_F_n⟩` --[t_axiomatize_from_instances {use: SLLN_pointwise_at_each_x}]--> output: `s_pointwise_a_s_convergence_at_each_x`
2. input: `s_pointwise_a_s_convergence_at_each_x` --[t_compactness_argument {partition: finite_grid_at_quantiles}]--> output: `s_uniform_via_finite_grid_plus_monotonicity`
3. input: `s_uniform_via_finite_grid_plus_monotonicity` --[t_exhaustion_squeeze {sup_to_zero: sandwich}]--> output: `s_glivenko_cantelli`

**Techniques used:** t_axiomatize_from_instances, t_compactness_argument, t_exhaustion_squeeze

---

### Dvoretzky–Kiefer–Wolfowitz Inequality (cite: https://en.wikipedia.org/wiki/Dvoretzky%E2%80%93Kiefer%E2%80%93Wolfowitz_inequality)

**Axioms:** `s_iid_real_random_variables_with_cdf_F`, `s_empirical_cdf_F_n`
**Terminal:** `s_dkw_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_iid_real_random_variables_with_cdf_F, s_empirical_cdf_F_n⟩` --[t_auxiliary_construction {object: brownian_bridge_approximation}]--> output: `s_kmt_strong_approximation`
2. input: `s_kmt_strong_approximation` --[t_projection_to_subspace {bound: maximal_inequality_for_brownian_bridge}]--> output: `s_subgaussian_tail_for_KS_statistic`
3. input: `s_subgaussian_tail_for_KS_statistic` --[t_reduce_to_canonical_form {to: P_sup_le_2_exp_minus_2_n_eps2}]--> output: `s_dkw_inequality`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Kolmogorov–Smirnov Test Statistic Law (cite: https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test)

**Axioms:** `s_iid_real_random_variables_with_cdf_F`, `s_empirical_cdf_F_n`
**Terminal:** `s_kolmogorov_smirnov_law` (kind: theorem)

**Steps:**
1. input: `⟨s_iid_real_random_variables_with_cdf_F, s_empirical_cdf_F_n⟩` --[t_auxiliary_construction {object: sqrt_n_F_n_minus_F_process}]--> output: `s_empirical_process`
2. input: `s_empirical_process` --[t_axiomatize_from_instances {limit: brownian_bridge}]--> output: `s_brownian_bridge_limit`
3. input: `s_brownian_bridge_limit` --[t_fourier_transform {compute: distribution_of_sup_brownian_bridge}]--> output: `s_kolmogorov_smirnov_law`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_fourier_transform

---

### Cochran's Theorem (cite: https://en.wikipedia.org/wiki/Cochran%27s_theorem)

**Axioms:** `s_iid_gaussian_vector_n`, `s_orthogonal_decomposition_of_quadratic_forms`
**Terminal:** `s_cochran_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_iid_gaussian_vector_n, s_orthogonal_decomposition_of_quadratic_forms⟩` --[t_svd_and_spectral_decomposition {decompose: identity_into_idempotent_projections}]--> output: `s_orthogonal_idempotents_summing_to_I`
2. input: `s_orthogonal_idempotents_summing_to_I` --[t_axiomatize_from_instances {fact: P_i_Z_squared_chi_squared_rank_P_i}]--> output: `s_each_quadratic_form_is_chi_squared`
3. input: `s_each_quadratic_form_is_chi_squared` --[t_reduce_to_canonical_form {independence: from_orthogonality}]--> output: `s_cochran_theorem`

**Techniques used:** t_svd_and_spectral_decomposition, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Slutsky's Theorem (cite: https://en.wikipedia.org/wiki/Slutsky%27s_theorem)

**Axioms:** `s_X_n_weak_to_X`, `s_Y_n_to_constant_c`
**Terminal:** `s_slutsky_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_X_n_weak_to_X, s_Y_n_to_constant_c⟩` --[t_axiomatize_from_instances {use: joint_tightness}]--> output: `s_joint_convergence_pair`
2. input: `s_joint_convergence_pair` --[t_compose_with_identity {map: continuous_g_x_y}]--> output: `s_apply_continuous_mapping_theorem`
3. input: `s_apply_continuous_mapping_theorem` --[t_reduce_to_canonical_form {to: products_and_sums_combine_correctly}]--> output: `s_slutsky_theorem`

**Techniques used:** t_axiomatize_from_instances, t_compose_with_identity, t_reduce_to_canonical_form

---

### Continuous Mapping Theorem (cite: https://en.wikipedia.org/wiki/Continuous_mapping_theorem)

**Axioms:** `s_X_n_to_X_in_some_mode`, `s_g_continuous_on_support_of_X`
**Terminal:** `s_continuous_mapping_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_X_n_to_X_in_some_mode, s_g_continuous_on_support_of_X⟩` --[t_auxiliary_construction {object: portmanteau_via_bounded_continuous}]--> output: `s_portmanteau_test_function_class`
2. input: `s_portmanteau_test_function_class` --[t_compose_with_identity {composition: h_circ_g}]--> output: `s_h_circ_g_bounded_continuous`
3. input: `s_h_circ_g_bounded_continuous` --[t_reduce_to_canonical_form {transfer: weak_convergence_pushes_forward}]--> output: `s_continuous_mapping_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_reduce_to_canonical_form

---

### Radon–Nikodym Theorem (cite: https://en.wikipedia.org/wiki/Radon%E2%80%93Nikodym_theorem)

**Axioms:** `s_sigma_finite_measure_mu`, `s_absolutely_continuous_measure_nu`
**Terminal:** `s_radon_nikodym_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sigma_finite_measure_mu, s_absolutely_continuous_measure_nu⟩` --[t_auxiliary_construction {hilbert_space: L2_mu_plus_nu}]--> output: `s_hilbert_space_dominating_measure`
2. input: `s_hilbert_space_dominating_measure` --[t_duality {riesz_representation_of_int_f_d_nu}]--> output: `s_bounded_linear_functional_representation`
3. input: `s_bounded_linear_functional_representation` --[t_reduce_to_canonical_form {to: nu_eq_int_f_d_mu_unique_a_e}]--> output: `s_radon_nikodym_theorem`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Kolmogorov Extension (Consistency) Theorem (cite: https://en.wikipedia.org/wiki/Kolmogorov_extension_theorem)

**Axioms:** `s_consistent_family_of_finite_dim_marginals`, `s_polish_state_space`
**Terminal:** `s_kolmogorov_extension_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_consistent_family_of_finite_dim_marginals, s_polish_state_space⟩` --[t_auxiliary_construction {object: cylinder_set_premeasure}]--> output: `s_premeasure_on_cylinder_algebra`
2. input: `s_premeasure_on_cylinder_algebra` --[t_compactness_argument {regularity: inner_regular_by_compacts_via_polish}]--> output: `s_sigma_additivity_via_compactness`
3. input: `s_sigma_additivity_via_compactness` --[t_axiomatize_from_instances {extend: caratheodory}]--> output: `s_kolmogorov_extension_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_axiomatize_from_instances

---

### Daniell–Kolmogorov Construction of Brownian Motion (cite: https://en.wikipedia.org/wiki/Wiener_process#Construction)

**Axioms:** `s_gaussian_finite_dim_marginals_with_BM_covariance`, `s_continuity_modulus_estimates`
**Terminal:** `s_wiener_existence` (kind: theorem)

**Steps:**
1. input: `s_gaussian_finite_dim_marginals_with_BM_covariance` --[t_axiomatize_from_instances {apply: kolmogorov_extension_to_get_law_on_R_0_infty}]--> output: `s_law_on_path_space_without_continuity`
2. input: `s_law_on_path_space_without_continuity` --[t_projection_to_subspace {bound: kolmogorov_continuity_criterion}]--> output: `s_holder_continuous_version`
3. input: `s_holder_continuous_version` --[t_reduce_to_canonical_form {to: brownian_motion_on_C0}]--> output: `s_wiener_existence`

**Techniques used:** t_axiomatize_from_instances, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Markov Chain Ergodic Theorem (cite: https://en.wikipedia.org/wiki/Markov_chain#Ergodic_theorem)

**Axioms:** `s_irreducible_aperiodic_positive_recurrent_markov_chain`, `s_invariant_distribution_pi`
**Terminal:** `s_markov_chain_ergodic_theorem` (kind: theorem)

**Steps:**
1. input: `s_irreducible_aperiodic_positive_recurrent_markov_chain` --[t_auxiliary_construction {regeneration: split_chain_at_atom}]--> output: `s_regeneration_at_atom_via_nummelin_splitting`
2. input: `s_regeneration_at_atom_via_nummelin_splitting` --[t_axiomatize_from_instances {apply: SLLN_to_iid_excursions}]--> output: `s_iid_excursions_yield_LLN`
3. input: `s_iid_excursions_yield_LLN` --[t_reduce_to_canonical_form {to: time_average_to_pi_average}]--> output: `s_markov_chain_ergodic_theorem`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Perron–Frobenius for Stochastic Matrices (cite: https://en.wikipedia.org/wiki/Perron%E2%80%93Frobenius_theorem)

**Axioms:** `s_finite_irreducible_stochastic_matrix_P`, `s_probability_simplex`
**Terminal:** `s_perron_frobenius_stochastic` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_irreducible_stochastic_matrix_P, s_probability_simplex⟩` --[t_contraction_fixed_point {map: P_acting_on_simplex_via_Brouwer}]--> output: `s_invariant_distribution_existence`
2. input: `s_invariant_distribution_existence` --[t_svd_and_spectral_decomposition {use: spectral_gap_below_1}]--> output: `s_largest_eigenvalue_one_simple`
3. input: `s_largest_eigenvalue_one_simple` --[t_exhaustion_squeeze {convergence: P_n_to_pi_in_total_variation}]--> output: `s_perron_frobenius_stochastic`

**Techniques used:** t_contraction_fixed_point, t_svd_and_spectral_decomposition, t_exhaustion_squeeze

---

### De Finetti's Exchangeability Theorem (cite: https://en.wikipedia.org/wiki/De_Finetti%27s_theorem)

**Axioms:** `s_infinite_exchangeable_sequence`, `s_polish_state_space`
**Terminal:** `s_de_finetti_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_infinite_exchangeable_sequence, s_polish_state_space⟩` --[t_symmetry_reduction {group: finite_permutation_group}]--> output: `s_symmetric_law_under_permutations`
2. input: `s_symmetric_law_under_permutations` --[t_auxiliary_construction {tail_field: limit_empirical_measure_M_n}]--> output: `s_random_empirical_limit_M`
3. input: `s_random_empirical_limit_M` --[t_axiomatize_from_instances {conditional_iid: given_M_sequence_is_iid}]--> output: `s_de_finetti_theorem`

**Techniques used:** t_symmetry_reduction, t_auxiliary_construction, t_axiomatize_from_instances

---

### Poisson Process Existence and Characterization (cite: https://en.wikipedia.org/wiki/Poisson_point_process)

**Axioms:** `s_rate_measure_lambda_on_sigma_finite_space`, `s_independence_and_poisson_count_axioms`
**Terminal:** `s_poisson_process_characterization` (kind: theorem)

**Steps:**
1. input: `⟨s_rate_measure_lambda_on_sigma_finite_space, s_independence_and_poisson_count_axioms⟩` --[t_auxiliary_construction {iid_atoms_on_disjoint_cells_then_take_limit}]--> output: `s_atomic_partition_construction`
2. input: `s_atomic_partition_construction` --[t_axiomatize_from_instances {check: independent_increments_and_marginal_poisson}]--> output: `s_finite_dim_distributions_match`
3. input: `s_finite_dim_distributions_match` --[t_reduce_to_canonical_form {kolmogorov_extension: glue_to_full_process}]--> output: `s_poisson_process_characterization`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Lévy–Khintchine Representation (cite: https://en.wikipedia.org/wiki/L%C3%A9vy_process)

**Axioms:** `s_levy_process_X_t`, `s_characteristic_function_phi_t`
**Terminal:** `s_levy_khintchine_representation` (kind: theorem)

**Steps:**
1. input: `⟨s_levy_process_X_t, s_characteristic_function_phi_t⟩` --[t_axiomatize_from_instances {observe: phi_t_eq_phi_1_to_t}]--> output: `s_infinitely_divisible_law`
2. input: `s_infinitely_divisible_law` --[t_auxiliary_construction {decompose: jumps_via_jump_measure_nu}]--> output: `s_jump_compensated_decomposition`
3. input: `s_jump_compensated_decomposition` --[t_fourier_transform {compute: log_phi_in_drift_gaussian_jump_form}]--> output: `s_levy_khintchine_representation`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_fourier_transform

---

### Itô Representation Theorem (martingale representation) (cite: https://en.wikipedia.org/wiki/Martingale_representation_theorem)

**Axioms:** `s_brownian_filtration_F_t`, `s_L2_F_T_random_variable`
**Terminal:** `s_ito_representation_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_brownian_filtration_F_t, s_L2_F_T_random_variable⟩` --[t_auxiliary_construction {dense_class: exponential_functionals_of_BM}]--> output: `s_dense_set_of_explicit_stochastic_integrals`
2. input: `s_dense_set_of_explicit_stochastic_integrals` --[t_projection_to_subspace {use: ito_isometry_to_extend}]--> output: `s_density_in_L2_F_T`
3. input: `s_density_in_L2_F_T` --[t_reduce_to_canonical_form {to: F_eq_E_F_plus_int_0_T_H_dW}]--> output: `s_ito_representation_theorem`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Clark–Ocone Formula (cite: https://en.wikipedia.org/wiki/Clark%E2%80%93Ocone_theorem)

**Axioms:** `s_brownian_filtration_F_t`, `s_malliavin_differentiable_random_variable_F`
**Terminal:** `s_clark_ocone_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_brownian_filtration_F_t, s_malliavin_differentiable_random_variable_F⟩` --[t_auxiliary_construction {object: malliavin_derivative_D_t_F}]--> output: `s_malliavin_derivative_D_F`
2. input: `s_malliavin_derivative_D_F` --[t_axiomatize_from_instances {apply: ito_representation_with_predictable_projection}]--> output: `s_predictable_projection_of_D_F`
3. input: `s_predictable_projection_of_D_F` --[t_reduce_to_canonical_form {to: F_eq_E_F_plus_int_predictable_DF_dW}]--> output: `s_clark_ocone_formula`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Hoeffding's Inequality (cite: https://en.wikipedia.org/wiki/Hoeffding%27s_inequality)

**Axioms:** `s_independent_bounded_random_variables`, `s_probability_axioms`
**Terminal:** `s_hoeffding_inequality` (kind: theorem)

**Steps:**
1. input: `s_independent_bounded_random_variables` --[t_projection_to_subspace {bound: hoeffdings_lemma_E_exp_lambda_X_le_exp_lambda2_b_minus_a_2_over_8}]--> output: `s_per_variable_subgaussian_mgf_bound`
2. input: `s_per_variable_subgaussian_mgf_bound` --[t_auxiliary_construction {product: mgf_of_sum_via_independence}]--> output: `s_mgf_of_sum_bound`
3. input: `s_mgf_of_sum_bound` --[t_reduce_to_canonical_form {chernoff_optimize: lambda_eq_t_over_sum_b_minus_a_squared}]--> output: `s_hoeffding_inequality`

**Techniques used:** t_projection_to_subspace, t_auxiliary_construction, t_reduce_to_canonical_form

---

### Bernstein's Inequality (cite: https://en.wikipedia.org/wiki/Bernstein_inequalities_(probability_theory))

**Axioms:** `s_independent_bounded_random_variables`, `s_finite_variance_sum_sigma2`
**Terminal:** `s_bernstein_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_independent_bounded_random_variables, s_finite_variance_sum_sigma2⟩` --[t_projection_to_subspace {bound: mgf_via_taylor_with_variance_term}]--> output: `s_per_variable_bernstein_mgf_bound`
2. input: `s_per_variable_bernstein_mgf_bound` --[t_auxiliary_construction {sum: log_mgf_le_sigma2_g_lambda}]--> output: `s_sum_log_mgf_bound`
3. input: `s_sum_log_mgf_bound` --[t_reduce_to_canonical_form {chernoff: P_ge_t_le_exp_minus_t2_over_2_sigma2_plus_M_t}]--> output: `s_bernstein_inequality`

**Techniques used:** t_projection_to_subspace, t_auxiliary_construction, t_reduce_to_canonical_form

---

### Chernoff Bound (cite: https://en.wikipedia.org/wiki/Chernoff_bound)

**Axioms:** `s_random_variable_with_mgf`, `s_probability_axioms`
**Terminal:** `s_chernoff_bound` (kind: theorem)

**Steps:**
1. input: `s_random_variable_with_mgf` --[t_auxiliary_construction {indicator: 1_X_ge_a_le_exp_lambda_X_minus_a}]--> output: `s_exponential_markov_bound`
2. input: `s_exponential_markov_bound` --[t_reduce_to_canonical_form {optimize: inf_lambda_E_exp_lambda_X_minus_a}]--> output: `s_chernoff_bound`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Doob's L^p Maximal Inequality (cite: https://en.wikipedia.org/wiki/Doob%27s_martingale_inequality)

**Axioms:** `s_nonnegative_submartingale`, `s_p_strictly_greater_than_1`
**Terminal:** `s_doob_Lp_maximal_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_nonnegative_submartingale, s_p_strictly_greater_than_1⟩` --[t_axiomatize_from_instances {use: weak_type_doob_max}]--> output: `s_weak_type_1_1_for_maximum`
2. input: `s_weak_type_1_1_for_maximum` --[t_projection_to_subspace {bound: layer_cake_integration}]--> output: `s_layer_cake_to_Lp_norm`
3. input: `s_layer_cake_to_Lp_norm` --[t_reduce_to_canonical_form {to: norm_max_le_p_over_p_minus_1_norm_X_n}]--> output: `s_doob_Lp_maximal_inequality`

**Techniques used:** t_axiomatize_from_instances, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Lindvall's Coupling Inequality (cite: https://en.wikipedia.org/wiki/Coupling_(probability))

**Axioms:** `s_two_random_variables_on_common_space`, `s_coupling_distribution`
**Terminal:** `s_coupling_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_two_random_variables_on_common_space, s_coupling_distribution⟩` --[t_auxiliary_construction {tau: coupling_time_inf_n_X_eq_Y}]--> output: `s_coupling_time_tau`
2. input: `s_coupling_time_tau` --[t_projection_to_subspace {bound: TV_le_P_X_neq_Y}]--> output: `s_tv_bound_via_coupling_time`
3. input: `s_tv_bound_via_coupling_time` --[t_reduce_to_canonical_form {to: norm_TV_mu_n_minus_pi_le_P_tau_gt_n}]--> output: `s_coupling_inequality`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Kingman's Coalescent Existence (cite: https://en.wikipedia.org/wiki/Kingman%27s_coalescent)

**Axioms:** `s_genealogy_under_neutral_evolution`, `s_haploid_population_model_N_haploids`
**Terminal:** `s_kingman_coalescent` (kind: theorem)

**Steps:**
1. input: `⟨s_genealogy_under_neutral_evolution, s_haploid_population_model_N_haploids⟩` --[t_rescale_for_asymptotic_geometry {time: t_eq_n_over_N}]--> output: `s_rescaled_coalescence_time`
2. input: `s_rescaled_coalescence_time` --[t_axiomatize_from_instances {limit: pairwise_coalescence_rate_binom_n_2}]--> output: `s_pairwise_rate_in_limit`
3. input: `s_pairwise_rate_in_limit` --[t_reduce_to_canonical_form {to: kingmans_coalescent_process}]--> output: `s_kingman_coalescent`

**Techniques used:** t_rescale_for_asymptotic_geometry, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Mixing Time and Spectral Gap (cite: https://en.wikipedia.org/wiki/Markov_chain_mixing_time)

**Axioms:** `s_reversible_finite_markov_chain_P`, `s_spectral_gap_gamma`
**Terminal:** `s_mixing_time_spectral_gap` (kind: theorem)

**Steps:**
1. input: `⟨s_reversible_finite_markov_chain_P, s_spectral_gap_gamma⟩` --[t_svd_and_spectral_decomposition {self_adjoint: P_in_L2_pi}]--> output: `s_spectral_decomposition_of_P_in_L2_pi`
2. input: `s_spectral_decomposition_of_P_in_L2_pi` --[t_projection_to_subspace {bound: P_n_minus_pi_in_L2_le_1_minus_gamma_n}]--> output: `s_L2_decay_bound`
3. input: `s_L2_decay_bound` --[t_reduce_to_canonical_form {to: t_mix_eps_le_log_1_over_eps_pi_min_over_gamma}]--> output: `s_mixing_time_spectral_gap`

**Techniques used:** t_svd_and_spectral_decomposition, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Aldous–Hoover Theorem (exchangeable arrays) (cite: https://en.wikipedia.org/wiki/Exchangeable_random_variables)

**Axioms:** `s_jointly_exchangeable_random_array`, `s_polish_state_space`
**Terminal:** `s_aldous_hoover_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_jointly_exchangeable_random_array, s_polish_state_space⟩` --[t_symmetry_reduction {group: product_of_finite_symmetric_groups}]--> output: `s_double_index_exchangeability`
2. input: `s_double_index_exchangeability` --[t_auxiliary_construction {latent: row_factor_xi_i_column_factor_xi_j_pair_factor}]--> output: `s_latent_variable_representation`
3. input: `s_latent_variable_representation` --[t_axiomatize_from_instances {extend: de_finetti_in_two_indices}]--> output: `s_aldous_hoover_theorem`

**Techniques used:** t_symmetry_reduction, t_auxiliary_construction, t_axiomatize_from_instances

---

### Strassen's Theorem (coupling characterization) (cite: https://en.wikipedia.org/wiki/Strassen%27s_theorem)

**Axioms:** `s_two_probability_measures_mu_nu`, `s_metric_or_closed_relation`
**Terminal:** `s_strassen_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_two_probability_measures_mu_nu, s_metric_or_closed_relation⟩` --[t_duality {pair: linear_programming_primal_dual_for_couplings}]--> output: `s_lp_duality_for_optimal_transport_form`
2. input: `s_lp_duality_for_optimal_transport_form` --[t_compactness_argument {tool: weak_compactness_of_coupling_set}]--> output: `s_optimal_coupling_exists`
3. input: `s_optimal_coupling_exists` --[t_reduce_to_canonical_form {to: coupling_exists_iff_marginal_inequality_holds}]--> output: `s_strassen_theorem`

**Techniques used:** t_duality, t_compactness_argument, t_reduce_to_canonical_form

---

### Kantorovich–Rubinstein Duality (cite: https://en.wikipedia.org/wiki/Wasserstein_metric#Dual_representation_of_W_1)

**Axioms:** `s_two_probability_measures_with_finite_first_moment`, `s_polish_metric_space`
**Terminal:** `s_kantorovich_rubinstein_duality` (kind: theorem)

**Steps:**
1. input: `⟨s_two_probability_measures_with_finite_first_moment, s_polish_metric_space⟩` --[t_auxiliary_construction {primal: optimal_transport_with_metric_cost}]--> output: `s_W1_as_primal_optimal_transport`
2. input: `s_W1_as_primal_optimal_transport` --[t_duality {pair: LP_duality_with_1_lipschitz_functions}]--> output: `s_dual_problem_over_1_lipschitz`
3. input: `s_dual_problem_over_1_lipschitz` --[t_reduce_to_canonical_form {to: W_1_eq_sup_int_f_d_mu_minus_d_nu}]--> output: `s_kantorovich_rubinstein_duality`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Brunn–Minkowski for Gaussian (Ehrhard inequality) (cite: https://en.wikipedia.org/wiki/Ehrhard_inequality)

**Axioms:** `s_standard_gaussian_measure_in_R_n`, `s_two_borel_sets_A_B`
**Terminal:** `s_ehrhard_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_standard_gaussian_measure_in_R_n, s_two_borel_sets_A_B⟩` --[t_auxiliary_construction {object: gaussian_isoperimetric_function_Phi_inv_mu}]--> output: `s_gaussian_isoperimetric_profile`
2. input: `s_gaussian_isoperimetric_profile` --[t_projection_to_subspace {bound: ehrhard_via_one_dim_reduction}]--> output: `s_one_dim_ehrhard_reduction`
3. input: `s_one_dim_ehrhard_reduction` --[t_reduce_to_canonical_form {to: Phi_inv_mu_lambda_A_plus_1_minus_lambda_B_ge_lambda_Phi_inv_mu_A_plus_1_minus_lambda_Phi_inv_mu_B}]--> output: `s_ehrhard_inequality`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Stochastic Loewner Evolution Existence (SLE) (cite: https://en.wikipedia.org/wiki/Schramm%E2%80%93Loewner_evolution)

**Axioms:** `s_brownian_motion`, `s_loewner_chordal_ODE`
**Terminal:** `s_sle_existence` (kind: theorem)

**Steps:**
1. input: `⟨s_brownian_motion, s_loewner_chordal_ODE⟩` --[t_auxiliary_construction {driver: sqrt_kappa_B_t}]--> output: `s_sle_kappa_driver`
2. input: `s_sle_kappa_driver` --[t_contraction_fixed_point {ode: g_t_z_via_loewner_pde}]--> output: `s_conformal_maps_g_t`
3. input: `s_conformal_maps_g_t` --[t_axiomatize_from_instances {trace_existence: rohde_schramm_continuity}]--> output: `s_sle_existence`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_axiomatize_from_instances

---

### Two-Series Theorem (Kolmogorov) (cite: https://en.wikipedia.org/wiki/Kolmogorov%27s_three-series_theorem)

**Axioms:** `s_independent_centered_random_variables`, `s_finite_variance_sum_sigma2`
**Terminal:** `s_kolmogorov_two_series_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_independent_centered_random_variables, s_finite_variance_sum_sigma2⟩` --[t_projection_to_subspace {bound: kolmogorov_max_inequality_for_partial_sums}]--> output: `s_uniform_partial_sum_bound`
2. input: `s_uniform_partial_sum_bound` --[t_axiomatize_from_instances {cauchy_in_probability: yields_a_s_convergence}]--> output: `s_a_s_convergence_via_levy_equivalence`
3. input: `s_a_s_convergence_via_levy_equivalence` --[t_reduce_to_canonical_form {to: finite_variance_sum_implies_a_s_convergent_series}]--> output: `s_kolmogorov_two_series_theorem`

**Techniques used:** t_projection_to_subspace, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Lévy's Equivalence Theorem (cite: https://en.wikipedia.org/wiki/L%C3%A9vy%27s_theorem)

**Axioms:** `s_sum_of_independent_random_variables`, `s_probability_axioms`
**Terminal:** `s_levy_equivalence_theorem` (kind: theorem)

**Steps:**
1. input: `s_sum_of_independent_random_variables` --[t_symmetry_reduction {symmetrization: X_minus_X_prime}]--> output: `s_symmetrized_independent_sum`
2. input: `s_symmetrized_independent_sum` --[t_projection_to_subspace {bound: levy_maximal_inequality}]--> output: `s_max_partial_sum_concentration`
3. input: `s_max_partial_sum_concentration` --[t_axiomatize_from_instances {equivalence: a_s_conv_iff_prob_conv_iff_dist_conv}]--> output: `s_levy_equivalence_theorem`

**Techniques used:** t_symmetry_reduction, t_projection_to_subspace, t_axiomatize_from_instances

---

### Stein's Lemma (Gaussian integration by parts) (cite: https://en.wikipedia.org/wiki/Stein%27s_lemma)

**Axioms:** `s_standard_gaussian_Z`, `s_absolutely_continuous_function_g`
**Terminal:** `s_stein_lemma_gaussian` (kind: theorem)

**Steps:**
1. input: `⟨s_standard_gaussian_Z, s_absolutely_continuous_function_g⟩` --[t_auxiliary_construction {density: phi_z_with_phi_prime_eq_minus_z_phi}]--> output: `s_gaussian_density_ODE_identity`
2. input: `s_gaussian_density_ODE_identity` --[t_duality {integration_by_parts: shift_derivative_from_phi_to_g}]--> output: `s_IBP_with_gaussian_density`
3. input: `s_IBP_with_gaussian_density` --[t_reduce_to_canonical_form {to: E_Z_g_Z_eq_E_g_prime_Z}]--> output: `s_stein_lemma_gaussian`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Slepian's Inequality (Gaussian comparison) (cite: https://en.wikipedia.org/wiki/Slepian%27s_lemma)

**Axioms:** `s_two_centered_gaussian_vectors_X_Y`, `s_pairwise_covariance_inequality`
**Terminal:** `s_slepian_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_two_centered_gaussian_vectors_X_Y, s_pairwise_covariance_inequality⟩` --[t_auxiliary_construction {interpolation: gaussian_path_t_X_plus_sqrt_1_minus_t_Y}]--> output: `s_gaussian_interpolation_path`
2. input: `s_gaussian_interpolation_path` --[t_projection_to_subspace {bound: derivative_of_E_F_interp_via_stein}]--> output: `s_derivative_sign_via_covariance_difference`
3. input: `s_derivative_sign_via_covariance_difference` --[t_reduce_to_canonical_form {to: P_max_X_le_t_le_P_max_Y_le_t}]--> output: `s_slepian_inequality`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Borell–TIS Inequality (Gaussian concentration of maxima) (cite: https://en.wikipedia.org/wiki/Borell%E2%80%93TIS_inequality)

**Axioms:** `s_centered_gaussian_process_X_t_separable`, `s_almost_sure_finite_sup`
**Terminal:** `s_borell_tis_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_centered_gaussian_process_X_t_separable, s_almost_sure_finite_sup⟩` --[t_auxiliary_construction {object: sup_X_t_as_lipschitz_in_underlying_gaussian}]--> output: `s_sup_as_lipschitz_function_of_iid_gaussians`
2. input: `s_sup_as_lipschitz_function_of_iid_gaussians` --[t_axiomatize_from_instances {use: gaussian_concentration_for_lipschitz}]--> output: `s_lipschitz_gaussian_concentration_bound`
3. input: `s_lipschitz_gaussian_concentration_bound` --[t_reduce_to_canonical_form {to: P_sup_minus_med_ge_t_le_exp_minus_t2_over_2_sigma2}]--> output: `s_borell_tis_inequality`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Dudley's Entropy Bound (cite: https://en.wikipedia.org/wiki/Dudley%27s_theorem)

**Axioms:** `s_subgaussian_process_on_metric_space_T`, `s_metric_entropy_log_N_eps`
**Terminal:** `s_dudley_entropy_bound` (kind: theorem)

**Steps:**
1. input: `⟨s_subgaussian_process_on_metric_space_T, s_metric_entropy_log_N_eps⟩` --[t_auxiliary_construction {chain: dyadic_nets_T_k_for_eps_k_eq_2_minus_k}]--> output: `s_dyadic_chaining_nets`
2. input: `s_dyadic_chaining_nets` --[t_projection_to_subspace {bound: max_subgaussian_le_C_sqrt_log_N}]--> output: `s_chaining_subgaussian_bound`
3. input: `s_chaining_subgaussian_bound` --[t_reduce_to_canonical_form {to: E_sup_le_C_int_sqrt_log_N_eps_d_eps}]--> output: `s_dudley_entropy_bound`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Donsker–Varadhan Variational Formula (cite: https://en.wikipedia.org/wiki/Donsker%E2%80%93Varadhan_theorem)

**Axioms:** `s_ergodic_markov_process`, `s_empirical_occupation_measure`
**Terminal:** `s_donsker_varadhan_LDP` (kind: theorem)

**Steps:**
1. input: `⟨s_ergodic_markov_process, s_empirical_occupation_measure⟩` --[t_auxiliary_construction {variational: I_mu_eq_sup_int_minus_Lu_over_u_d_mu}]--> output: `s_variational_rate_function`
2. input: `s_variational_rate_function` --[t_duality {legendre: variational_to_KL_divergence}]--> output: `s_DV_rate_function_eq_dirichlet_form`
3. input: `s_DV_rate_function_eq_dirichlet_form` --[t_reduce_to_canonical_form {LDP: large_deviation_principle_for_occupation_measure}]--> output: `s_donsker_varadhan_LDP`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Varadhan's Lemma (cite: https://en.wikipedia.org/wiki/Varadhan%27s_lemma)

**Axioms:** `s_family_satisfying_LDP_with_rate_I`, `s_continuous_bounded_function_F`
**Terminal:** `s_varadhan_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_family_satisfying_LDP_with_rate_I, s_continuous_bounded_function_F⟩` --[t_projection_to_subspace {upper_bound: laplace_method_compactness}]--> output: `s_laplace_upper_bound`
2. input: `s_laplace_upper_bound` --[t_projection_to_subspace {lower_bound: localize_near_optimizer_of_F_minus_I}]--> output: `s_laplace_lower_bound`
3. input: `⟨s_laplace_upper_bound, s_laplace_lower_bound⟩` --[t_reduce_to_canonical_form {to: lim_1_over_n_log_E_exp_n_F_eq_sup_F_minus_I}]--> output: `s_varadhan_lemma`

**Techniques used:** t_projection_to_subspace, t_reduce_to_canonical_form

---

### Contraction Principle (large deviations) (cite: https://en.wikipedia.org/wiki/Contraction_principle_(large_deviations_theory))

**Axioms:** `s_family_satisfying_LDP_with_rate_I_on_X`, `s_continuous_map_F_X_to_Y`
**Terminal:** `s_contraction_principle_LDP` (kind: theorem)

**Steps:**
1. input: `⟨s_family_satisfying_LDP_with_rate_I_on_X, s_continuous_map_F_X_to_Y⟩` --[t_auxiliary_construction {push_forward: F_image_family_on_Y}]--> output: `s_push_forward_family_on_Y`
2. input: `s_push_forward_family_on_Y` --[t_compactness_argument {use: F_inverse_of_open_open}]--> output: `s_LDP_with_inverse_image_rate`
3. input: `s_LDP_with_inverse_image_rate` --[t_reduce_to_canonical_form {to: J_y_eq_inf_I_x_F_x_eq_y}]--> output: `s_contraction_principle_LDP`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Renewal Theorem (Blackwell) (cite: https://en.wikipedia.org/wiki/Renewal_theory#Renewal_theorems)

**Axioms:** `s_iid_positive_inter_arrival_times`, `s_renewal_function_U_t`
**Terminal:** `s_blackwell_renewal_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_iid_positive_inter_arrival_times, s_renewal_function_U_t⟩` --[t_auxiliary_construction {coupling: stationary_renewal_process}]--> output: `s_stationary_renewal_coupling`
2. input: `s_stationary_renewal_coupling` --[t_axiomatize_from_instances {use: coupling_inequality_to_TV_zero}]--> output: `s_TV_distance_to_stationary_renewal_zero`
3. input: `s_TV_distance_to_stationary_renewal_zero` --[t_reduce_to_canonical_form {to: U_t_plus_h_minus_U_t_to_h_over_mu}]--> output: `s_blackwell_renewal_theorem`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Kesten–Stigum Theorem (Branching processes) (cite: https://en.wikipedia.org/wiki/Galton%E2%80%93Watson_process)

**Axioms:** `s_supercritical_galton_watson_process`, `s_x_log_x_moment_condition`
**Terminal:** `s_kesten_stigum_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_supercritical_galton_watson_process, s_x_log_x_moment_condition⟩` --[t_auxiliary_construction {martingale: W_n_eq_Z_n_over_m_n}]--> output: `s_normalized_population_martingale_W_n`
2. input: `s_normalized_population_martingale_W_n` --[t_axiomatize_from_instances {apply: doob_L1_convergence_under_x_log_x}]--> output: `s_W_infty_nondegenerate`
3. input: `s_W_infty_nondegenerate` --[t_reduce_to_canonical_form {to: P_W_infty_gt_0_eq_survival_probability}]--> output: `s_kesten_stigum_theorem`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Stochastic Approximation (Robbins–Monro) Convergence (cite: https://en.wikipedia.org/wiki/Stochastic_approximation)

**Axioms:** `s_root_finding_problem_h_x_eq_0`, `s_step_size_sequence_alpha_n_with_robbins_monro_conditions`
**Terminal:** `s_robbins_monro_convergence` (kind: theorem)

**Steps:**
1. input: `⟨s_root_finding_problem_h_x_eq_0, s_step_size_sequence_alpha_n_with_robbins_monro_conditions⟩` --[t_auxiliary_construction {lyapunov_function: V_x_eq_x_minus_x_star_squared}]--> output: `s_lyapunov_for_robbins_monro`
2. input: `s_lyapunov_for_robbins_monro` --[t_axiomatize_from_instances {apply: robbins_siegmund_supermartingale_lemma}]--> output: `s_supermartingale_convergence_for_V_n`
3. input: `s_supermartingale_convergence_for_V_n` --[t_exhaustion_squeeze {gradient_lyapunov: sum_alpha_n_h_at_X_n_finite_implies_X_n_to_x_star}]--> output: `s_robbins_monro_convergence`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_exhaustion_squeeze

---

### Functional Law of the Iterated Logarithm (Strassen) (cite: https://en.wikipedia.org/wiki/Law_of_the_iterated_logarithm)

**Axioms:** `s_iid_sequence_finite_variance`, `s_brownian_motion`
**Terminal:** `s_strassen_functional_lil` (kind: theorem)

**Steps:**
1. input: `s_iid_sequence_finite_variance` --[t_axiomatize_from_instances {use: skorokhod_embed_to_brownian}]--> output: `s_brownian_embedding_of_random_walk`
2. input: `s_brownian_embedding_of_random_walk` --[t_rescale_for_asymptotic_geometry {scaling: W_n_t_over_sqrt_2_n_loglog_n}]--> output: `s_rescaled_brownian_paths`
3. input: `s_rescaled_brownian_paths` --[t_compactness_argument {schilders_ldp_compact_clustering_set}]--> output: `s_cluster_set_is_strassen_ball`
4. input: `s_cluster_set_is_strassen_ball` --[t_reduce_to_canonical_form {to: strassens_functional_lil}]--> output: `s_strassen_functional_lil`

**Techniques used:** t_axiomatize_from_instances, t_rescale_for_asymptotic_geometry, t_compactness_argument, t_reduce_to_canonical_form

---

### Karhunen–Loève Expansion (cite: https://en.wikipedia.org/wiki/Karhunen%E2%80%93Lo%C3%A8ve_theorem)

**Axioms:** `s_L2_centered_stochastic_process_with_continuous_covariance`, `s_hilbert_schmidt_kernel`
**Terminal:** `s_karhunen_loeve_expansion` (kind: theorem)

**Steps:**
1. input: `⟨s_L2_centered_stochastic_process_with_continuous_covariance, s_hilbert_schmidt_kernel⟩` --[t_svd_and_spectral_decomposition {tool: mercer_expansion_of_covariance_kernel}]--> output: `s_eigenfunction_eigenvalue_decomposition`
2. input: `s_eigenfunction_eigenvalue_decomposition` --[t_auxiliary_construction {object: coefficient_random_variables_Z_n_eq_int_X_phi_n}]--> output: `s_uncorrelated_coefficient_sequence`
3. input: `s_uncorrelated_coefficient_sequence` --[t_reduce_to_canonical_form {to: X_t_eq_sum_sqrt_lambda_n_Z_n_phi_n_t}]--> output: `s_karhunen_loeve_expansion`

**Techniques used:** t_svd_and_spectral_decomposition, t_auxiliary_construction, t_reduce_to_canonical_form

---
