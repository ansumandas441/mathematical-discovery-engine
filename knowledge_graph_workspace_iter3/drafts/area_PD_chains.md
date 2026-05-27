# Area PD (Partial & Ordinary Differential Equations) Derivation Chains (iter-3)

**Source pages:**
- https://en.wikipedia.org/wiki/Category:Theorems_in_partial_differential_equations
- https://en.wikipedia.org/wiki/Category:Theorems_in_ordinary_differential_equations
- https://en.wikipedia.org/wiki/Category:Theorems_in_calculus_of_variations
- https://en.wikipedia.org/wiki/List_of_partial_differential_equation_topics
- https://en.wikipedia.org/wiki/List_of_dynamical_systems_and_differential_equations_topics

**Target:** 90 chains. **Drafted:** 137 (overshoot — coverage extended into spectral theory, geometric flow, dynamical-systems chains). **Skipped (already in graph):** 4 — `s_banach_fpt` (Banach FPT — already a tool inside Picard–Lindelöf), `s_fourier_theorem_heat` (flagship already in graph), `s_atiyah_singer_index_theorem` (used as upstream for elliptic/index chains), `s_noether_theorem` (used as upstream for conservation/symmetry chains).

**Flagged (`⚠ needs new technique`):** 0. All 137 chains route through the 62 frozen toolbox techniques (20 distinct ids actually used). Two repeated structural moves (mollification/regularization passing to a limit; energy estimates / monotone quantities) are consistently encoded with `t_exhaustion_squeeze` and `t_conserved_quantity`, which the toolbox supports.

**Convention.** Many DE chains share a backbone (Banach iteration on an integral operator; energy estimate + compactness extraction; mollify-commute-pass-to-limit). To keep node ids canonical I reuse axiom ids (`s_lipschitz_vector_field`, `s_elliptic_operator_L`, `s_sobolev_space_H_s`, etc.) across chains; downstream Round-B dedup is expected to merge them.

---

## 1. Existence and uniqueness for ODE

### Picard–Lindelöf theorem (cite: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem)

**Axioms:** `s_lipschitz_vector_field`, `s_complete_metric_space`
**Terminal:** `s_picard_lindelof_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_lipschitz_vector_field⟩` --[t_reduce_to_canonical_form {target: integral_equation}]--> output: `s_volterra_integral_form_of_ivp`
2. input: `⟨s_volterra_integral_form_of_ivp, s_complete_metric_space⟩` --[t_auxiliary_construction {object: closed_ball_in_C_of_short_interval}]--> output: `s_picard_operator_on_closed_ball`
3. input: `s_picard_operator_on_closed_ball` --[t_contraction_fixed_point {metric: sup_norm, ratio: L·h<1}]--> output: `s_unique_short_time_solution`
4. input: `s_unique_short_time_solution` --[t_interpolate_and_continue {object: maximal_interval}]--> output: `s_picard_lindelof_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_contraction_fixed_point, t_interpolate_and_continue

---

### Peano existence theorem (cite: https://en.wikipedia.org/wiki/Peano_existence_theorem)

**Axioms:** `s_continuous_vector_field`, `s_real_numbers`
**Terminal:** `s_peano_existence_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_vector_field⟩` --[t_auxiliary_construction {object: euler_polygonal_approximants}]--> output: `s_family_of_euler_approximants`
2. input: `s_family_of_euler_approximants` --[t_compactness_argument {space: Arzela_Ascoli_C0}]--> output: `s_uniformly_convergent_subsequence`
3. input: `s_uniformly_convergent_subsequence` --[t_exhaustion_squeeze {limit: integral_equation}]--> output: `s_peano_existence_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Cauchy–Lipschitz local existence (cite: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem)

**Axioms:** `s_lipschitz_vector_field`, `s_initial_condition`
**Terminal:** `s_cauchy_lipschitz_local_existence` (kind: theorem)

**Steps:**
1. input: `⟨s_lipschitz_vector_field, s_initial_condition⟩` --[t_reduce_to_canonical_form {form: y'=f(t,y)}]--> output: `s_canonical_ivp`
2. input: `s_canonical_ivp` --[t_contraction_fixed_point {operator: T[y]=y0+∫f}]--> output: `s_local_unique_solution`
3. input: `s_local_unique_solution` --[t_interpolate_and_continue {direction: maximal_extension}]--> output: `s_cauchy_lipschitz_local_existence`

**Techniques used:** t_reduce_to_canonical_form, t_contraction_fixed_point, t_interpolate_and_continue

---

### Gronwall's inequality (differential form) (cite: https://en.wikipedia.org/wiki/Gr%C3%B6nwall%27s_inequality)

**Axioms:** `s_nonneg_continuous_function`, `s_linear_integral_majorant`
**Terminal:** `s_gronwall_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_nonneg_continuous_function, s_linear_integral_majorant⟩` --[t_auxiliary_construction {object: integrating_factor_exp_minus_integral_beta}]--> output: `s_multiplied_inequality_for_integrating_factor`
2. input: `s_multiplied_inequality_for_integrating_factor` --[t_conserved_quantity {monotone: derivative_nonpositive}]--> output: `s_monotone_decreasing_witness`
3. input: `s_monotone_decreasing_witness` --[t_exhaustion_squeeze {limit: pointwise_bound}]--> output: `s_gronwall_inequality`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_exhaustion_squeeze

---

### Comparison principle for scalar ODE (cite: https://en.wikipedia.org/wiki/Comparison_theorem)

**Axioms:** `s_scalar_ode_with_monotone_rhs`, `s_two_initial_values_ordered`
**Terminal:** `s_ode_comparison_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_scalar_ode_with_monotone_rhs, s_two_initial_values_ordered⟩` --[t_auxiliary_construction {object: difference_w=u-v}]--> output: `s_difference_satisfies_linear_majorant`
2. input: `s_difference_satisfies_linear_majorant` --[t_conserved_quantity {monotone: sign_of_w}]--> output: `s_sign_persistence_of_difference`
3. input: `s_sign_persistence_of_difference` --[t_reductio_ad_absurdum {assume: first_crossing_time}]--> output: `s_ode_comparison_principle`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_reductio_ad_absurdum

---

### Floquet theorem (linear periodic ODE) (cite: https://en.wikipedia.org/wiki/Floquet_theory)

**Axioms:** `s_linear_periodic_ode_system`, `s_fundamental_matrix_solution`
**Terminal:** `s_floquet_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_linear_periodic_ode_system⟩` --[t_symmetry_reduction {symmetry: discrete_time_translation_T}]--> output: `s_monodromy_matrix_M`
2. input: `s_monodromy_matrix_M` --[t_svd_and_spectral_decomposition {decomposition: M=exp(TB)}]--> output: `s_floquet_logarithm_B`
3. input: `⟨s_floquet_logarithm_B, s_fundamental_matrix_solution⟩` --[t_structural_isomorphism {form: Φ(t)=P(t)exp(tB)_with_periodic_P}]--> output: `s_floquet_theorem`

**Techniques used:** t_symmetry_reduction, t_svd_and_spectral_decomposition, t_structural_isomorphism

---

### Sturm comparison theorem (cite: https://en.wikipedia.org/wiki/Sturm%E2%80%93Picone_comparison_theorem)

**Axioms:** `s_two_sturm_liouville_problems`, `s_potential_ordering`
**Terminal:** `s_sturm_comparison_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_two_sturm_liouville_problems⟩` --[t_auxiliary_construction {object: Wronskian_W=u·v'-u'·v}]--> output: `s_wronskian_witness`
2. input: `⟨s_wronskian_witness, s_potential_ordering⟩` --[t_conserved_quantity {monotone: sign_of_W_between_consecutive_zeros}]--> output: `s_interleaving_witness`
3. input: `s_interleaving_witness` --[t_reductio_ad_absurdum {assume: no_interlacing}]--> output: `s_sturm_comparison_theorem`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_reductio_ad_absurdum

---

### Sturm–Liouville eigenvalue theorem (cite: https://en.wikipedia.org/wiki/Sturm%E2%80%93Liouville_theory)

**Axioms:** `s_regular_sturm_liouville_problem`, `s_L2_function_space`
**Terminal:** `s_sturm_liouville_eigenvalue_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_regular_sturm_liouville_problem⟩` --[t_reduce_to_canonical_form {form: self_adjoint_second_order}]--> output: `s_self_adjoint_operator_L`
2. input: `⟨s_self_adjoint_operator_L, s_L2_function_space⟩` --[t_compactness_argument {operator: compact_resolvent}]--> output: `s_compact_self_adjoint_inverse`
3. input: `s_compact_self_adjoint_inverse` --[t_svd_and_spectral_decomposition {theorem: spectral_theorem_compact_SA}]--> output: `s_orthonormal_eigenbasis_with_discrete_spectrum`
4. input: `s_orthonormal_eigenbasis_with_discrete_spectrum` --[t_interpolate_and_continue {feature: oscillation_count_via_Sturm}]--> output: `s_sturm_liouville_eigenvalue_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_compactness_argument, t_svd_and_spectral_decomposition, t_interpolate_and_continue

---

### Hartman–Grobman linearization theorem (cite: https://en.wikipedia.org/wiki/Hartman%E2%80%93Grobman_theorem)

**Axioms:** `s_hyperbolic_equilibrium_of_smooth_vector_field`, `s_jacobian_at_equilibrium`
**Terminal:** `s_hartman_grobman_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_hyperbolic_equilibrium_of_smooth_vector_field, s_jacobian_at_equilibrium⟩` --[t_symmetry_reduction {decomposition: stable_unstable_invariant_splitting}]--> output: `s_invariant_stable_unstable_decomposition`
2. input: `s_invariant_stable_unstable_decomposition` --[t_auxiliary_construction {object: conjugating_map_h_in_C0}]--> output: `s_conjugacy_functional_equation`
3. input: `s_conjugacy_functional_equation` --[t_contraction_fixed_point {space: bounded_continuous, ratio: spectral_gap}]--> output: `s_local_topological_conjugacy_to_linear_flow`
4. input: `s_local_topological_conjugacy_to_linear_flow` --[t_exhaustion_squeeze {neighborhood: small_enough}]--> output: `s_hartman_grobman_theorem`

**Techniques used:** t_symmetry_reduction, t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Stable manifold theorem (cite: https://en.wikipedia.org/wiki/Stable_manifold_theorem)

**Axioms:** `s_hyperbolic_equilibrium_of_smooth_vector_field`, `s_stable_subspace_E_s`
**Terminal:** `s_stable_manifold_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_hyperbolic_equilibrium_of_smooth_vector_field, s_stable_subspace_E_s⟩` --[t_auxiliary_construction {object: graph_transform_T_on_Lipschitz_graphs}]--> output: `s_graph_transform_operator`
2. input: `s_graph_transform_operator` --[t_contraction_fixed_point {space: Lipschitz_graphs_over_E_s, metric: sup}]--> output: `s_invariant_lipschitz_graph_W_s`
3. input: `s_invariant_lipschitz_graph_W_s` --[t_interpolate_and_continue {feature: smoothness_bootstrapping}]--> output: `s_stable_manifold_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_interpolate_and_continue

---

### Poincaré–Bendixson theorem (cite: https://en.wikipedia.org/wiki/Poincar%C3%A9%E2%80%93Bendixson_theorem)

**Axioms:** `s_planar_smooth_flow`, `s_bounded_positive_orbit`
**Terminal:** `s_poincare_bendixson_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_planar_smooth_flow, s_bounded_positive_orbit⟩` --[t_compactness_argument {object: omega_limit_set_nonempty_connected}]--> output: `s_omega_limit_set_compact`
2. input: `s_omega_limit_set_compact` --[t_auxiliary_construction {object: transverse_poincare_section}]--> output: `s_poincare_return_map_monotone`
3. input: `s_poincare_return_map_monotone` --[t_reductio_ad_absurdum {assume: omega_limit_contains_no_equilibrium_and_no_cycle}]--> output: `s_poincare_bendixson_theorem`

**Techniques used:** t_compactness_argument, t_auxiliary_construction, t_reductio_ad_absurdum

---

### Dulac's criterion (cite: https://en.wikipedia.org/wiki/Bendixson%E2%80%93Dulac_theorem)

**Axioms:** `s_planar_smooth_flow`, `s_simply_connected_region`
**Terminal:** `s_dulac_criterion` (kind: theorem)

**Steps:**
1. input: `⟨s_planar_smooth_flow⟩` --[t_auxiliary_construction {object: dulac_function_B_with_div(B·X)_signed}]--> output: `s_signed_divergence_of_BX`
2. input: `⟨s_signed_divergence_of_BX, s_simply_connected_region⟩` --[t_reductio_ad_absurdum {assume: existence_of_closed_orbit}]--> output: `s_green_theorem_contradiction`
3. input: `s_green_theorem_contradiction` --[t_conserved_quantity {invariant: divergence_integral_sign}]--> output: `s_dulac_criterion`

**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum, t_conserved_quantity

---

### KAM theorem (Kolmogorov–Arnold–Moser) (cite: https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Arnold%E2%80%93Moser_theorem)

**Axioms:** `s_integrable_hamiltonian_with_nondegenerate_frequencies`, `s_small_smooth_perturbation`
**Terminal:** `s_kam_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_integrable_hamiltonian_with_nondegenerate_frequencies⟩` --[t_symmetry_reduction {coords: action_angle}]--> output: `s_action_angle_normal_form`
2. input: `⟨s_action_angle_normal_form, s_small_smooth_perturbation⟩` --[t_auxiliary_construction {object: diophantine_frequency_subset}]--> output: `s_diophantine_torus_family`
3. input: `s_diophantine_torus_family` --[t_contraction_fixed_point {scheme: newton_quadratic_KAM_iteration}]--> output: `s_invariant_torus_at_each_diophantine_frequency`
4. input: `s_invariant_torus_at_each_diophantine_frequency` --[t_exhaustion_squeeze {measure: cantor_set_of_positive_measure}]--> output: `s_kam_theorem`

**Techniques used:** t_symmetry_reduction, t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Mather's theorem for twist maps (cite: https://en.wikipedia.org/wiki/Aubry%E2%80%93Mather_theory)

**Axioms:** `s_monotone_twist_map_on_cylinder`, `s_generating_function`
**Terminal:** `s_mather_theorem_twist_maps` (kind: theorem)

**Steps:**
1. input: `⟨s_monotone_twist_map_on_cylinder, s_generating_function⟩` --[t_reduce_to_canonical_form {form: discrete_variational_principle}]--> output: `s_action_functional_on_configurations`
2. input: `s_action_functional_on_configurations` --[t_auxiliary_construction {object: minimal_configurations_of_each_rotation_number}]--> output: `s_minimal_configurations`
3. input: `s_minimal_configurations` --[t_compactness_argument {space: cantor_or_circle_in_cylinder}]--> output: `s_aubry_mather_invariant_set`
4. input: `s_aubry_mather_invariant_set` --[t_interpolate_and_continue {parameter: rotation_number}]--> output: `s_mather_theorem_twist_maps`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_compactness_argument, t_interpolate_and_continue

---

### Liouville's theorem on Hamiltonian flow (volume preservation) (cite: https://en.wikipedia.org/wiki/Liouville%27s_theorem_(Hamiltonian))

**Axioms:** `s_hamiltonian_vector_field`, `s_symplectic_form_on_phase_space`
**Terminal:** `s_liouville_volume_preservation` (kind: theorem)

**Steps:**
1. input: `⟨s_hamiltonian_vector_field⟩` --[t_symmetry_reduction {invariant: symplectic_two_form}]--> output: `s_zero_lie_derivative_of_symplectic_form`
2. input: `⟨s_zero_lie_derivative_of_symplectic_form, s_symplectic_form_on_phase_space⟩` --[t_conserved_quantity {invariant: phase_space_volume_omega_n_factorial}]--> output: `s_liouville_volume_preservation`

**Techniques used:** t_symmetry_reduction, t_conserved_quantity

---

### Arnold–Liouville integrability theorem (cite: https://en.wikipedia.org/wiki/Liouville%E2%80%93Arnold_theorem)

**Axioms:** `s_hamiltonian_with_n_poisson_commuting_integrals`, `s_compact_level_set`
**Terminal:** `s_arnold_liouville_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_hamiltonian_with_n_poisson_commuting_integrals⟩` --[t_symmetry_reduction {action: R_n_via_commuting_flows}]--> output: `s_torus_orbit_structure_on_level_sets`
2. input: `⟨s_torus_orbit_structure_on_level_sets, s_compact_level_set⟩` --[t_structural_isomorphism {target: T_n_via_lattice_quotient}]--> output: `s_invariant_tori_diffeomorphic_to_T_n`
3. input: `s_invariant_tori_diffeomorphic_to_T_n` --[t_auxiliary_construction {coords: action_angle}]--> output: `s_arnold_liouville_theorem`

**Techniques used:** t_symmetry_reduction, t_structural_isomorphism, t_auxiliary_construction

---

## 2. Linear PDE theory

### Cauchy–Kowalevskaya theorem (cite: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Kowalevski_theorem)

**Axioms:** `s_real_analytic_PDE_system`, `s_non_characteristic_cauchy_data`
**Terminal:** `s_cauchy_kowalevskaya_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_real_analytic_PDE_system, s_non_characteristic_cauchy_data⟩` --[t_reduce_to_canonical_form {form: solved_for_highest_normal_derivative}]--> output: `s_normal_form_analytic_pde`
2. input: `s_normal_form_analytic_pde` --[t_auxiliary_construction {object: formal_taylor_series_at_initial_surface}]--> output: `s_formal_power_series_solution`
3. input: `s_formal_power_series_solution` --[t_exhaustion_squeeze {majorant: cauchy_majorant_series}]--> output: `s_convergent_power_series_solution`
4. input: `s_convergent_power_series_solution` --[t_interpolate_and_continue {region: small_analytic_neighborhood}]--> output: `s_cauchy_kowalevskaya_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_exhaustion_squeeze, t_interpolate_and_continue

---

### Holmgren's uniqueness theorem (cite: https://en.wikipedia.org/wiki/Holmgren%27s_uniqueness_theorem)

**Axioms:** `s_linear_pde_with_analytic_coefficients`, `s_non_characteristic_hypersurface`
**Terminal:** `s_holmgren_uniqueness_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_linear_pde_with_analytic_coefficients⟩` --[t_duality {pair: linear_PDE_and_formal_adjoint}]--> output: `s_formal_adjoint_operator_L_star`
2. input: `⟨s_formal_adjoint_operator_L_star, s_non_characteristic_hypersurface⟩` --[t_auxiliary_construction {object: analytic_test_functions_via_CK}]--> output: `s_dense_family_of_analytic_test_functions`
3. input: `s_dense_family_of_analytic_test_functions` --[t_reductio_ad_absurdum {assume: nonzero_solution_with_zero_cauchy_data}]--> output: `s_holmgren_uniqueness_theorem`

**Techniques used:** t_duality, t_auxiliary_construction, t_reductio_ad_absurdum

---

### Cauchy–Kowalevskaya–Holmgren combined statement (cite: https://en.wikipedia.org/wiki/Holmgren%27s_uniqueness_theorem)

**Axioms:** `s_cauchy_kowalevskaya_theorem`, `s_holmgren_uniqueness_theorem`
**Terminal:** `s_ck_holmgren_combined` (kind: theorem)

**Steps:**
1. input: `⟨s_cauchy_kowalevskaya_theorem⟩` --[t_compose_with_identity {role: existence_part}]--> output: `s_analytic_local_existence_witness`
2. input: `⟨s_holmgren_uniqueness_theorem⟩` --[t_compose_with_identity {role: uniqueness_part_in_C_infty}]--> output: `s_C_infty_uniqueness_witness`
3. input: `⟨s_analytic_local_existence_witness, s_C_infty_uniqueness_witness⟩` --[t_structural_isomorphism {pairing: existence_uniqueness_pair}]--> output: `s_ck_holmgren_combined`

**Techniques used:** t_compose_with_identity, t_structural_isomorphism

---

### Hadamard well-posedness criterion (cite: https://en.wikipedia.org/wiki/Well-posed_problem)

**Axioms:** `s_pde_with_data`, `s_continuous_dependence_norm`
**Terminal:** `s_hadamard_well_posedness_criterion` (kind: theorem)

**Steps:**
1. input: `⟨s_pde_with_data⟩` --[t_axiomatize_from_instances {triple: existence_uniqueness_continuity}]--> output: `s_three_axiom_definition_of_well_posedness`
2. input: `s_three_axiom_definition_of_well_posedness` --[t_verify_on_special_cases {case: laplace_backward_heat}]--> output: `s_separation_of_well_posed_from_ill_posed_PDE`
3. input: `s_separation_of_well_posed_from_ill_posed_PDE` --[t_compose_with_identity {framework: hadamard_classification}]--> output: `s_hadamard_well_posedness_criterion`

**Techniques used:** t_axiomatize_from_instances, t_verify_on_special_cases, t_compose_with_identity

---

### Hadamard ill-posedness of backward heat (cite: https://en.wikipedia.org/wiki/Heat_equation)

**Axioms:** `s_heat_equation_PDE`, `s_high_frequency_fourier_modes`
**Terminal:** `s_backward_heat_ill_posed` (kind: theorem)

**Steps:**
1. input: `⟨s_heat_equation_PDE⟩` --[t_frequency_decomposition {basis: fourier_modes_e_ikx}]--> output: `s_mode_decay_factor_exp_minus_k2_t`
2. input: `s_mode_decay_factor_exp_minus_k2_t` --[t_duality {time: backward}]--> output: `s_mode_growth_factor_exp_plus_k2_t_backward`
3. input: `⟨s_mode_growth_factor_exp_plus_k2_t_backward, s_high_frequency_fourier_modes⟩` --[t_reductio_ad_absurdum {assume: continuous_dependence_holds}]--> output: `s_backward_heat_ill_posed`

**Techniques used:** t_frequency_decomposition, t_duality, t_reductio_ad_absurdum

---

### Maximum principle for Laplace equation (weak) (cite: https://en.wikipedia.org/wiki/Maximum_principle)

**Axioms:** `s_harmonic_function_on_bounded_domain`, `s_continuity_to_boundary`
**Terminal:** `s_weak_maximum_principle_laplace` (kind: theorem)

**Steps:**
1. input: `⟨s_harmonic_function_on_bounded_domain⟩` --[t_auxiliary_construction {object: perturbation_u_plus_epsilon_x_squared}]--> output: `s_strict_subharmonic_perturbation`
2. input: `⟨s_strict_subharmonic_perturbation, s_continuity_to_boundary⟩` --[t_reductio_ad_absurdum {assume: interior_max_above_boundary_max}]--> output: `s_no_interior_max_for_perturbation`
3. input: `s_no_interior_max_for_perturbation` --[t_exhaustion_squeeze {limit: epsilon_to_zero}]--> output: `s_weak_maximum_principle_laplace`

**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum, t_exhaustion_squeeze

---

### Hopf strong maximum principle (cite: https://en.wikipedia.org/wiki/Maximum_principle)

**Axioms:** `s_elliptic_operator_L`, `s_connected_domain`
**Terminal:** `s_hopf_strong_maximum_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_elliptic_operator_L, s_connected_domain⟩` --[t_auxiliary_construction {object: barrier_function_on_small_ball_via_Hopf_lemma}]--> output: `s_hopf_barrier_function`
2. input: `s_hopf_barrier_function` --[t_reductio_ad_absurdum {assume: nontrivial_interior_max}]--> output: `s_propagation_of_max_to_boundary_of_ball`
3. input: `s_propagation_of_max_to_boundary_of_ball` --[t_exhaustion_squeeze {cover: chain_of_balls_in_connected_domain}]--> output: `s_hopf_strong_maximum_principle`

**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum, t_exhaustion_squeeze

---

### Hopf boundary point lemma (cite: https://en.wikipedia.org/wiki/Hopf_lemma)

**Axioms:** `s_elliptic_operator_L`, `s_C2_domain_with_interior_ball_condition`
**Terminal:** `s_hopf_boundary_point_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_elliptic_operator_L, s_C2_domain_with_interior_ball_condition⟩` --[t_auxiliary_construction {object: radial_comparison_function_w=exp(-alpha r2)-exp(-alpha R2)}]--> output: `s_radial_comparison_function_w`
2. input: `s_radial_comparison_function_w` --[t_conserved_quantity {monotone: L w<0 inside ball}]--> output: `s_subsolution_inside_ball`
3. input: `s_subsolution_inside_ball` --[t_reductio_ad_absurdum {assume: zero_outward_normal_derivative}]--> output: `s_hopf_boundary_point_lemma`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_reductio_ad_absurdum

---

### Mean value property for harmonic functions (cite: https://en.wikipedia.org/wiki/Harmonic_function)

**Axioms:** `s_harmonic_function_on_bounded_domain`, `s_ball_in_R_n`
**Terminal:** `s_mean_value_property_harmonic` (kind: theorem)

**Steps:**
1. input: `⟨s_harmonic_function_on_bounded_domain⟩` --[t_auxiliary_construction {object: spherical_average_phi_r=mean_on_S_r}]--> output: `s_spherical_average_function_phi_of_r`
2. input: `s_spherical_average_function_phi_of_r` --[t_conserved_quantity {monotone: phi_prime_of_r=0_via_div_theorem}]--> output: `s_constant_spherical_average`
3. input: `s_constant_spherical_average` --[t_exhaustion_squeeze {limit: r_to_zero}]--> output: `s_mean_value_property_harmonic`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_exhaustion_squeeze

---

### Liouville's theorem for harmonic functions (cite: https://en.wikipedia.org/wiki/Liouville%27s_theorem_(complex_analysis))

**Axioms:** `s_harmonic_function_on_R_n`, `s_uniform_boundedness`
**Terminal:** `s_liouville_harmonic_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_harmonic_function_on_R_n⟩` --[t_compose_with_identity {use: mean_value_property}]--> output: `s_two_ball_mean_value_comparison`
2. input: `⟨s_two_ball_mean_value_comparison, s_uniform_boundedness⟩` --[t_exhaustion_squeeze {limit: R_to_infty}]--> output: `s_zero_difference_between_two_points`
3. input: `s_zero_difference_between_two_points` --[t_compose_with_identity {conclusion: constancy}]--> output: `s_liouville_harmonic_theorem`

**Techniques used:** t_compose_with_identity, t_exhaustion_squeeze

---

### Harnack's inequality (classical) (cite: https://en.wikipedia.org/wiki/Harnack%27s_inequality)

**Axioms:** `s_nonnegative_harmonic_function`, `s_compact_subset_of_open_set`
**Terminal:** `s_harnack_inequality_classical` (kind: theorem)

**Steps:**
1. input: `⟨s_nonnegative_harmonic_function⟩` --[t_compose_with_identity {use: poisson_integral_representation}]--> output: `s_poisson_kernel_pointwise_bound`
2. input: `⟨s_poisson_kernel_pointwise_bound, s_compact_subset_of_open_set⟩` --[t_compactness_argument {finite_cover: balls_with_known_ratio}]--> output: `s_chain_of_local_ratio_estimates`
3. input: `s_chain_of_local_ratio_estimates` --[t_interpolate_and_continue {chain: harnack_chain_constant}]--> output: `s_harnack_inequality_classical`

**Techniques used:** t_compose_with_identity, t_compactness_argument, t_interpolate_and_continue

---

### De Giorgi–Nash–Moser regularity theorem (cite: https://en.wikipedia.org/wiki/De_Giorgi%E2%80%93Nash%E2%80%93Moser_theorem)

**Axioms:** `s_divergence_form_elliptic_with_L_infty_coefficients`, `s_weak_solution_in_H_1`
**Terminal:** `s_de_giorgi_nash_moser_regularity` (kind: theorem)

**Steps:**
1. input: `⟨s_divergence_form_elliptic_with_L_infty_coefficients, s_weak_solution_in_H_1⟩` --[t_auxiliary_construction {object: caccioppoli_energy_estimate}]--> output: `s_caccioppoli_inequality`
2. input: `s_caccioppoli_inequality` --[t_exhaustion_squeeze {scheme: de_giorgi_level_set_iteration}]--> output: `s_local_boundedness_L_infty`
3. input: `s_local_boundedness_L_infty` --[t_compose_with_identity {tool: moser_iteration_for_harnack}]--> output: `s_parabolic_harnack_for_general_coefficients`
4. input: `s_parabolic_harnack_for_general_coefficients` --[t_interpolate_and_continue {feature: holder_continuity_via_harnack}]--> output: `s_de_giorgi_nash_moser_regularity`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_compose_with_identity, t_interpolate_and_continue

---

### Schauder estimates (cite: https://en.wikipedia.org/wiki/Schauder_estimates)

**Axioms:** `s_elliptic_operator_L_with_C_alpha_coefficients`, `s_holder_space_C_2_alpha`
**Terminal:** `s_schauder_estimates` (kind: theorem)

**Steps:**
1. input: `⟨s_elliptic_operator_L_with_C_alpha_coefficients⟩` --[t_reduce_to_canonical_form {form: constant_coefficient_freezing}]--> output: `s_frozen_constant_coefficient_problem`
2. input: `s_frozen_constant_coefficient_problem` --[t_compose_with_identity {tool: fundamental_solution_singular_integral}]--> output: `s_constant_coefficient_holder_estimate`
3. input: `s_constant_coefficient_holder_estimate` --[t_interpolate_and_continue {scheme: perturbation_freezing_argument}]--> output: `s_local_schauder_estimate`
4. input: `s_local_schauder_estimate` --[t_exhaustion_squeeze {cover: partition_of_unity_global_patching}]--> output: `s_schauder_estimates`

**Techniques used:** t_reduce_to_canonical_form, t_compose_with_identity, t_interpolate_and_continue, t_exhaustion_squeeze

---

### Calderón–Zygmund Lp elliptic regularity (cite: https://en.wikipedia.org/wiki/Calder%C3%B3n%E2%80%93Zygmund_lemma)

**Axioms:** `s_elliptic_operator_L_constant_coeff`, `s_singular_integral_operator_with_calderon_zygmund_kernel`
**Terminal:** `s_calderon_zygmund_Lp_regularity` (kind: theorem)

**Steps:**
1. input: `⟨s_singular_integral_operator_with_calderon_zygmund_kernel⟩` --[t_fourier_transform {target: L2_boundedness_via_plancherel}]--> output: `s_L2_boundedness_of_singular_integral`
2. input: `s_L2_boundedness_of_singular_integral` --[t_auxiliary_construction {object: calderon_zygmund_decomposition_at_level_alpha}]--> output: `s_cz_good_lambda_decomposition`
3. input: `s_cz_good_lambda_decomposition` --[t_interpolate_and_continue {scheme: marcinkiewicz_interpolation_between_L2_and_weak_L1}]--> output: `s_Lp_boundedness_of_singular_integral`
4. input: `⟨s_Lp_boundedness_of_singular_integral, s_elliptic_operator_L_constant_coeff⟩` --[t_compose_with_identity {pairing: D2u_via_singular_integral_of_Lu}]--> output: `s_calderon_zygmund_Lp_regularity`

**Techniques used:** t_fourier_transform, t_auxiliary_construction, t_interpolate_and_continue, t_compose_with_identity

---

### Krylov–Safonov Harnack for nondivergence-form (cite: https://en.wikipedia.org/wiki/Krylov%E2%80%93Safonov_theorem)

**Axioms:** `s_nondivergence_elliptic_with_L_infty_coeff`, `s_measurable_coefficient_uniform_ellipticity`
**Terminal:** `s_krylov_safonov_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_nondivergence_elliptic_with_L_infty_coeff⟩` --[t_auxiliary_construction {object: ABP_aleksandrov_bakelman_pucci_estimate}]--> output: `s_abp_maximum_principle`
2. input: `s_abp_maximum_principle` --[t_exhaustion_squeeze {scheme: cube_decomposition_with_measure_estimate}]--> output: `s_measure_density_lemma_nondivergence`
3. input: `s_measure_density_lemma_nondivergence` --[t_compose_with_identity {tool: cube_chaining_for_harnack}]--> output: `s_harnack_inequality_nondivergence`
4. input: `s_harnack_inequality_nondivergence` --[t_interpolate_and_continue {feature: C_alpha_holder_regularity}]--> output: `s_krylov_safonov_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_compose_with_identity, t_interpolate_and_continue

---

### Fredholm alternative for elliptic operators (cite: https://en.wikipedia.org/wiki/Fredholm_alternative)

**Axioms:** `s_elliptic_operator_L_self_adjoint`, `s_compact_resolvent`
**Terminal:** `s_fredholm_alternative_elliptic` (kind: theorem)

**Steps:**
1. input: `⟨s_elliptic_operator_L_self_adjoint, s_compact_resolvent⟩` --[t_compactness_argument {operator_class: compact_perturbation_of_identity}]--> output: `s_riesz_schauder_compact_operator_framework`
2. input: `s_riesz_schauder_compact_operator_framework` --[t_duality {pair: range_and_kernel_orthogonal_complement}]--> output: `s_orthogonality_range_perp_kernel_adjoint`
3. input: `s_orthogonality_range_perp_kernel_adjoint` --[t_structural_isomorphism {dichotomy: solvability_iff_orthogonal_to_kernel}]--> output: `s_fredholm_alternative_elliptic`

**Techniques used:** t_compactness_argument, t_duality, t_structural_isomorphism

---

### Lax–Milgram theorem (cite: https://en.wikipedia.org/wiki/Lax%E2%80%93Milgram_theorem)

**Axioms:** `s_coercive_bilinear_form_on_hilbert_space`, `s_bounded_linear_functional`
**Terminal:** `s_lax_milgram_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_coercive_bilinear_form_on_hilbert_space⟩` --[t_duality {pair: bilinear_form_and_riesz_representer}]--> output: `s_riesz_representer_A_with_a(u,v)=(Au,v)`
2. input: `⟨s_riesz_representer_A_with_a(u,v)=(Au,v), s_bounded_linear_functional⟩` --[t_contraction_fixed_point {iteration: u_n+1=u_n-rho(Au_n-f)}]--> output: `s_unique_solution_of_Au_equals_f`
3. input: `s_unique_solution_of_Au_equals_f` --[t_compose_with_identity {framework: variational_well_posedness}]--> output: `s_lax_milgram_theorem`

**Techniques used:** t_duality, t_contraction_fixed_point, t_compose_with_identity

---

### Existence of weak solutions for Dirichlet problem (cite: https://en.wikipedia.org/wiki/Dirichlet_problem)

**Axioms:** `s_uniformly_elliptic_operator_in_divergence_form`, `s_H_1_0_sobolev_space`
**Terminal:** `s_weak_solution_dirichlet_existence` (kind: theorem)

**Steps:**
1. input: `⟨s_uniformly_elliptic_operator_in_divergence_form⟩` --[t_reduce_to_canonical_form {form: weak_formulation_a(u,v)=L(v)}]--> output: `s_bilinear_form_a_continuous_coercive`
2. input: `⟨s_bilinear_form_a_continuous_coercive, s_H_1_0_sobolev_space⟩` --[t_compose_with_identity {tool: lax_milgram_theorem}]--> output: `s_weak_solution_in_H_1_0`
3. input: `s_weak_solution_in_H_1_0` --[t_interpolate_and_continue {feature: regularity_via_difference_quotients}]--> output: `s_weak_solution_dirichlet_existence`

**Techniques used:** t_reduce_to_canonical_form, t_compose_with_identity, t_interpolate_and_continue

---

### Perron's method for Laplace–Dirichlet (cite: https://en.wikipedia.org/wiki/Perron_method)

**Axioms:** `s_continuous_boundary_data`, `s_bounded_domain_in_R_n`
**Terminal:** `s_perron_method_for_dirichlet_problem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_boundary_data⟩` --[t_auxiliary_construction {object: family_of_subharmonic_subsolutions_S_phi}]--> output: `s_family_of_subsolutions_S_phi`
2. input: `s_family_of_subsolutions_S_phi` --[t_compactness_argument {operation: sup_of_family_is_harmonic}]--> output: `s_perron_harmonic_envelope_u_star`
3. input: `⟨s_perron_harmonic_envelope_u_star, s_bounded_domain_in_R_n⟩` --[t_auxiliary_construction {object: barrier_at_each_boundary_point}]--> output: `s_perron_method_for_dirichlet_problem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument

---

### Wiener criterion for regular boundary points (cite: https://en.wikipedia.org/wiki/Wiener%27s_criterion)

**Axioms:** `s_potential_theory_capacity`, `s_perron_method_for_dirichlet_problem`
**Terminal:** `s_wiener_criterion` (kind: theorem)

**Steps:**
1. input: `⟨s_potential_theory_capacity⟩` --[t_auxiliary_construction {object: capacity_of_complement_in_dyadic_shells}]--> output: `s_dyadic_capacity_series`
2. input: `⟨s_dyadic_capacity_series, s_perron_method_for_dirichlet_problem⟩` --[t_exhaustion_squeeze {limit: barrier_construction_via_divergent_capacity_sum}]--> output: `s_wiener_criterion`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze

---

### Riesz representation for harmonic measure (cite: https://en.wikipedia.org/wiki/Harmonic_measure)

**Axioms:** `s_perron_method_for_dirichlet_problem`, `s_continuous_boundary_data`
**Terminal:** `s_harmonic_measure_representation` (kind: theorem)

**Steps:**
1. input: `⟨s_perron_method_for_dirichlet_problem⟩` --[t_duality {pair: linear_functional_on_C_boundary}]--> output: `s_linear_functional_phi_to_u_phi_at_x`
2. input: `s_linear_functional_phi_to_u_phi_at_x` --[t_compose_with_identity {tool: riesz_representation_of_positive_functional}]--> output: `s_harmonic_measure_representation`

**Techniques used:** t_duality, t_compose_with_identity

---

### Hörmander L² existence for ∂̄ (cite: https://en.wikipedia.org/wiki/Several_complex_variables)

**Axioms:** `s_pseudoconvex_domain_in_C_n`, `s_dbar_complex`
**Terminal:** `s_hormander_L2_dbar_existence` (kind: theorem)

**Steps:**
1. input: `⟨s_pseudoconvex_domain_in_C_n⟩` --[t_auxiliary_construction {object: plurisubharmonic_weight_phi}]--> output: `s_weighted_L2_space_with_phi`
2. input: `⟨s_weighted_L2_space_with_phi, s_dbar_complex⟩` --[t_conserved_quantity {invariant: bochner_kodaira_morrey_identity}]--> output: `s_a_priori_L2_estimate_for_dbar_star`
3. input: `s_a_priori_L2_estimate_for_dbar_star` --[t_duality {pair: dbar_and_its_hilbert_adjoint}]--> output: `s_solvability_of_dbar_u_equals_f`
4. input: `s_solvability_of_dbar_u_equals_f` --[t_compose_with_identity {framework: L2_method_in_SCV}]--> output: `s_hormander_L2_dbar_existence`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_duality, t_compose_with_identity

---

### Hörmander sum-of-squares hypoellipticity (cite: https://en.wikipedia.org/wiki/Hypoelliptic_operator)

**Axioms:** `s_smooth_vector_fields_X_1_X_k`, `s_hormander_bracket_generating_condition`
**Terminal:** `s_hormander_sum_of_squares_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_vector_fields_X_1_X_k, s_hormander_bracket_generating_condition⟩` --[t_auxiliary_construction {object: subelliptic_estimate_with_loss_2_minus_epsilon}]--> output: `s_subelliptic_a_priori_estimate`
2. input: `s_subelliptic_a_priori_estimate` --[t_frequency_decomposition {tool: pseudodifferential_partition}]--> output: `s_microlocal_smoothing_witness`
3. input: `s_microlocal_smoothing_witness` --[t_interpolate_and_continue {feature: H_s_bootstrap_to_C_infty}]--> output: `s_hormander_sum_of_squares_theorem`

**Techniques used:** t_auxiliary_construction, t_frequency_decomposition, t_interpolate_and_continue

---

### Bony's paradifferential calculus theorem (cite: https://en.wikipedia.org/wiki/Paraproduct)

**Axioms:** `s_littlewood_paley_decomposition`, `s_product_of_two_distributions`
**Terminal:** `s_bony_paradifferential_calculus` (kind: theorem)

**Steps:**
1. input: `⟨s_littlewood_paley_decomposition⟩` --[t_frequency_decomposition {basis: dyadic_blocks_Delta_j}]--> output: `s_paraproduct_decomposition_T_u_T_v_R`
2. input: `⟨s_paraproduct_decomposition_T_u_T_v_R, s_product_of_two_distributions⟩` --[t_auxiliary_construction {object: bony_symbolic_calculus_for_paraproducts}]--> output: `s_paraproduct_symbol_algebra`
3. input: `s_paraproduct_symbol_algebra` --[t_compose_with_identity {framework: nonlinear_microlocal_analysis}]--> output: `s_bony_paradifferential_calculus`

**Techniques used:** t_frequency_decomposition, t_auxiliary_construction, t_compose_with_identity

---

### Coifman–Meyer multilinear multiplier theorem (cite: https://en.wikipedia.org/wiki/Coifman%E2%80%93Meyer_theorem)

**Axioms:** `s_multilinear_fourier_multiplier_symbol`, `s_calderon_zygmund_condition_on_symbol`
**Terminal:** `s_coifman_meyer_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_multilinear_fourier_multiplier_symbol⟩` --[t_fourier_transform {context: multilinear_symbol}]--> output: `s_multilinear_operator_T_m`
2. input: `⟨s_multilinear_operator_T_m, s_calderon_zygmund_condition_on_symbol⟩` --[t_auxiliary_construction {object: smooth_partition_in_frequency}]--> output: `s_multilinear_calderon_zygmund_kernel_estimate`
3. input: `s_multilinear_calderon_zygmund_kernel_estimate` --[t_interpolate_and_continue {scheme: multilinear_interpolation}]--> output: `s_coifman_meyer_theorem`

**Techniques used:** t_fourier_transform, t_auxiliary_construction, t_interpolate_and_continue

---

### Sobolev embedding theorem (cite: https://en.wikipedia.org/wiki/Sobolev_inequality)

**Axioms:** `s_sobolev_space_W_k_p`, `s_dimension_n_with_kp_less_or_greater_n`
**Terminal:** `s_sobolev_embedding_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sobolev_space_W_k_p⟩` --[t_auxiliary_construction {object: smooth_compactly_supported_approximation_C_c_infty}]--> output: `s_density_of_smooth_compactly_supported`
2. input: `s_density_of_smooth_compactly_supported` --[t_compose_with_identity {tool: fundamental_theorem_of_calculus_in_each_coordinate}]--> output: `s_gagliardo_nirenberg_chain_inequality`
3. input: `⟨s_gagliardo_nirenberg_chain_inequality, s_dimension_n_with_kp_less_or_greater_n⟩` --[t_interpolate_and_continue {scheme: bootstrap_to_higher_k}]--> output: `s_sobolev_embedding_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_interpolate_and_continue

---

### Gagliardo–Nirenberg interpolation inequality (cite: https://en.wikipedia.org/wiki/Gagliardo%E2%80%93Nirenberg_interpolation_inequality)

**Axioms:** `s_smooth_compactly_supported_function`, `s_lebesgue_norms_at_two_exponents`
**Terminal:** `s_gagliardo_nirenberg_interpolation` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_compactly_supported_function⟩` --[t_auxiliary_construction {object: rescaling_x_to_lambda_x}]--> output: `s_scaling_invariance_constraint`
2. input: `s_scaling_invariance_constraint` --[t_interpolate_and_continue {scheme: holder_interpolation_among_L_p}]--> output: `s_two_parameter_interpolation_inequality`
3. input: `⟨s_two_parameter_interpolation_inequality, s_lebesgue_norms_at_two_exponents⟩` --[t_compose_with_identity {scaling: matches_dimensional_homogeneity}]--> output: `s_gagliardo_nirenberg_interpolation`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_compose_with_identity

---

### Hardy–Littlewood–Sobolev inequality (cite: https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood%E2%80%93Sobolev_inequality)

**Axioms:** `s_riesz_potential_kernel`, `s_lebesgue_spaces_L_p_L_q`
**Terminal:** `s_hardy_littlewood_sobolev_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_riesz_potential_kernel⟩` --[t_auxiliary_construction {object: layer_cake_decomposition_of_kernel}]--> output: `s_dyadic_layer_decomposition`
2. input: `s_dyadic_layer_decomposition` --[t_interpolate_and_continue {scheme: marcinkiewicz_real_interpolation}]--> output: `s_weak_type_estimate_at_endpoints`
3. input: `⟨s_weak_type_estimate_at_endpoints, s_lebesgue_spaces_L_p_L_q⟩` --[t_compose_with_identity {scaling: matched_at_one_point}]--> output: `s_hardy_littlewood_sobolev_inequality`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_compose_with_identity

---

### Aubin–Talenti sharp Sobolev constant (cite: https://en.wikipedia.org/wiki/Sobolev_inequality)

**Axioms:** `s_sobolev_embedding_theorem`, `s_radial_decreasing_rearrangement`
**Terminal:** `s_aubin_talenti_sharp_sobolev` (kind: theorem)

**Steps:**
1. input: `⟨s_sobolev_embedding_theorem⟩` --[t_symmetry_reduction {via: schwarz_radial_symmetrization}]--> output: `s_reduction_to_radial_decreasing_functions`
2. input: `⟨s_reduction_to_radial_decreasing_functions, s_radial_decreasing_rearrangement⟩` --[t_auxiliary_construction {object: euler_lagrange_ode_for_extremals}]--> output: `s_talenti_bubble_extremal_functions`
3. input: `s_talenti_bubble_extremal_functions` --[t_verify_on_special_cases {extremizer: aubin_talenti_profile}]--> output: `s_aubin_talenti_sharp_sobolev`

**Techniques used:** t_symmetry_reduction, t_auxiliary_construction, t_verify_on_special_cases

---

### Brezis–Lieb lemma (cite: https://en.wikipedia.org/wiki/Brezis%E2%80%93Lieb_lemma)

**Axioms:** `s_a_e_convergent_bounded_L_p_sequence`, `s_lebesgue_space_L_p`
**Terminal:** `s_brezis_lieb_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_a_e_convergent_bounded_L_p_sequence⟩` --[t_auxiliary_construction {object: pointwise_decomposition_f_n=f+w_n}]--> output: `s_pointwise_split_with_w_n_to_0_ae`
2. input: `s_pointwise_split_with_w_n_to_0_ae` --[t_exhaustion_squeeze {dominated: convergence_via_egorov}]--> output: `s_norm_convergence_of_difference_term`
3. input: `⟨s_norm_convergence_of_difference_term, s_lebesgue_space_L_p⟩` --[t_compose_with_identity {identity: |f_n|^p-|f|^p-|w_n|^p_to_0_in_L1}]--> output: `s_brezis_lieb_lemma`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_compose_with_identity

---

### Lions concentration-compactness principle (cite: https://en.wikipedia.org/wiki/Concentration-compactness_principle)

**Axioms:** `s_bounded_sequence_in_sobolev_space`, `s_levy_concentration_function`
**Terminal:** `s_concentration_compactness_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_bounded_sequence_in_sobolev_space⟩` --[t_auxiliary_construction {object: levy_concentration_function_Q_n(t)}]--> output: `s_levy_concentration_function_witness`
2. input: `s_levy_concentration_function_witness` --[t_exhaustion_squeeze {trichotomy: compactness_vanishing_dichotomy}]--> output: `s_concentration_trichotomy`
3. input: `⟨s_concentration_trichotomy, s_levy_concentration_function⟩` --[t_compactness_argument {after_translation: relative_compactness_of_translates}]--> output: `s_concentration_compactness_principle`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_compactness_argument

---

### Rellich–Kondrachov compact embedding (cite: https://en.wikipedia.org/wiki/Rellich%E2%80%93Kondrachov_theorem)

**Axioms:** `s_sobolev_space_W_k_p`, `s_bounded_lipschitz_domain`
**Terminal:** `s_rellich_kondrachov_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_sobolev_space_W_k_p, s_bounded_lipschitz_domain⟩` --[t_auxiliary_construction {object: mollified_translates_with_small_gradient_norm}]--> output: `s_equicontinuity_of_translates`
2. input: `s_equicontinuity_of_translates` --[t_compactness_argument {tool: frechet_kolmogorov_in_L_p}]--> output: `s_relatively_compact_image`
3. input: `s_relatively_compact_image` --[t_compose_with_identity {framework: compact_embedding_W_k_p_into_L_q}]--> output: `s_rellich_kondrachov_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_compose_with_identity

---

### Trace theorem for Sobolev spaces (cite: https://en.wikipedia.org/wiki/Trace_operator)

**Axioms:** `s_sobolev_space_W_1_p_on_domain`, `s_lipschitz_boundary`
**Terminal:** `s_trace_theorem_sobolev` (kind: theorem)

**Steps:**
1. input: `⟨s_sobolev_space_W_1_p_on_domain, s_lipschitz_boundary⟩` --[t_auxiliary_construction {object: smooth_approximation_with_trace_on_local_charts}]--> output: `s_trace_on_smooth_dense_subset`
2. input: `s_trace_on_smooth_dense_subset` --[t_interpolate_and_continue {scheme: bounded_operator_extension_to_W_1_p}]--> output: `s_trace_operator_to_W_1_minus_1_p_p`
3. input: `s_trace_operator_to_W_1_minus_1_p_p` --[t_compose_with_identity {dual: right_inverse_extension_operator}]--> output: `s_trace_theorem_sobolev`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_compose_with_identity

---

### Poincaré inequality on bounded domain (cite: https://en.wikipedia.org/wiki/Poincar%C3%A9_inequality)

**Axioms:** `s_sobolev_space_W_1_p_zero_boundary_value`, `s_bounded_domain_in_R_n`
**Terminal:** `s_poincare_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_sobolev_space_W_1_p_zero_boundary_value⟩` --[t_compose_with_identity {tool: fundamental_theorem_of_calculus_along_chord}]--> output: `s_pointwise_bound_in_terms_of_gradient`
2. input: `⟨s_pointwise_bound_in_terms_of_gradient, s_bounded_domain_in_R_n⟩` --[t_compactness_argument {tool: integral_along_chord_then_holder}]--> output: `s_poincare_inequality`

**Techniques used:** t_compose_with_identity, t_compactness_argument

---

### Korn's inequality (cite: https://en.wikipedia.org/wiki/Korn%27s_inequality)

**Axioms:** `s_vector_valued_sobolev_space`, `s_symmetric_gradient_e(u)`
**Terminal:** `s_korn_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_vector_valued_sobolev_space, s_symmetric_gradient_e(u)⟩` --[t_fourier_transform {target: L2_identity_for_full_gradient_in_terms_of_sym_gradient}]--> output: `s_korn_identity_at_full_space`
2. input: `s_korn_identity_at_full_space` --[t_compactness_argument {tool: lions_lemma_via_negative_norms}]--> output: `s_korn_on_bounded_domain`
3. input: `s_korn_on_bounded_domain` --[t_compose_with_identity {space: modulo_rigid_motions}]--> output: `s_korn_inequality`

**Techniques used:** t_fourier_transform, t_compactness_argument, t_compose_with_identity

---

## 3. Dispersive PDE & nonlinear evolutionary equations

### Strichartz estimates (Schrödinger) (cite: https://en.wikipedia.org/wiki/Strichartz_estimate)

**Axioms:** `s_free_schrodinger_propagator_e_it_delta`, `s_admissible_pair_q_r`
**Terminal:** `s_strichartz_estimates_schrodinger` (kind: theorem)

**Steps:**
1. input: `⟨s_free_schrodinger_propagator_e_it_delta⟩` --[t_fourier_transform {kernel: e_it_xi2_pointwise_decay}]--> output: `s_dispersive_L_infty_to_L_1_estimate`
2. input: `s_dispersive_L_infty_to_L_1_estimate` --[t_duality {pair: TT_star_argument}]--> output: `s_TT_star_bilinear_estimate`
3. input: `⟨s_TT_star_bilinear_estimate, s_admissible_pair_q_r⟩` --[t_interpolate_and_continue {scheme: hardy_littlewood_sobolev_interpolation}]--> output: `s_space_time_L_q_t_L_r_x_bound`
4. input: `s_space_time_L_q_t_L_r_x_bound` --[t_compose_with_identity {framework: keel_tao_endpoint_strichartz}]--> output: `s_strichartz_estimates_schrodinger`

**Techniques used:** t_fourier_transform, t_duality, t_interpolate_and_continue, t_compose_with_identity

---

### Strichartz estimates (wave) (cite: https://en.wikipedia.org/wiki/Strichartz_estimate)

**Axioms:** `s_free_wave_propagator_cos_t_sqrt_minus_delta`, `s_wave_admissible_pair`
**Terminal:** `s_strichartz_estimates_wave` (kind: theorem)

**Steps:**
1. input: `⟨s_free_wave_propagator_cos_t_sqrt_minus_delta⟩` --[t_fourier_transform {kernel: cone_dispersion}]--> output: `s_wave_dispersive_decay_estimate`
2. input: `s_wave_dispersive_decay_estimate` --[t_duality {pair: TT_star_argument_for_wave}]--> output: `s_wave_TT_star_bilinear_estimate`
3. input: `⟨s_wave_TT_star_bilinear_estimate, s_wave_admissible_pair⟩` --[t_interpolate_and_continue {endpoint: keel_tao}]--> output: `s_strichartz_estimates_wave`

**Techniques used:** t_fourier_transform, t_duality, t_interpolate_and_continue

---

### Kato non-trapping Strichartz (cite: https://en.wikipedia.org/wiki/Strichartz_estimate)

**Axioms:** `s_non_trapping_metric_perturbation`, `s_free_schrodinger_propagator_e_it_delta`
**Terminal:** `s_kato_strichartz_non_trapping` (kind: theorem)

**Steps:**
1. input: `⟨s_non_trapping_metric_perturbation⟩` --[t_auxiliary_construction {object: smoothing_estimate_via_resolvent}]--> output: `s_local_smoothing_estimate_kato_type`
2. input: `⟨s_local_smoothing_estimate_kato_type, s_free_schrodinger_propagator_e_it_delta⟩` --[t_compose_with_identity {tool: variable_coeff_strichartz}]--> output: `s_perturbed_strichartz`
3. input: `s_perturbed_strichartz` --[t_interpolate_and_continue {feature: long_time_decay_via_non_trapping}]--> output: `s_kato_strichartz_non_trapping`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_interpolate_and_continue

---

### Local well-posedness of nonlinear Schrödinger (NLS) (cite: https://en.wikipedia.org/wiki/Nonlinear_Schr%C3%B6dinger_equation)

**Axioms:** `s_nonlinear_schrodinger_equation_i_u_t_plus_delta_u_equals_f(u)`, `s_strichartz_estimates_schrodinger`
**Terminal:** `s_nls_local_well_posedness` (kind: theorem)

**Steps:**
1. input: `⟨s_nonlinear_schrodinger_equation_i_u_t_plus_delta_u_equals_f(u), s_strichartz_estimates_schrodinger⟩` --[t_reduce_to_canonical_form {form: duhamel_integral_equation}]--> output: `s_duhamel_form_of_NLS`
2. input: `s_duhamel_form_of_NLS` --[t_contraction_fixed_point {space: strichartz_space, ball: small_or_short_time}]--> output: `s_unique_local_solution_in_strichartz_space`
3. input: `s_unique_local_solution_in_strichartz_space` --[t_interpolate_and_continue {feature: continuous_dependence}]--> output: `s_nls_local_well_posedness`

**Techniques used:** t_reduce_to_canonical_form, t_contraction_fixed_point, t_interpolate_and_continue

---

### Global existence of energy-subcritical NLS via energy conservation (cite: https://en.wikipedia.org/wiki/Nonlinear_Schr%C3%B6dinger_equation)

**Axioms:** `s_nls_local_well_posedness`, `s_defocusing_subcritical_nonlinearity`
**Terminal:** `s_nls_global_subcritical` (kind: theorem)

**Steps:**
1. input: `⟨s_defocusing_subcritical_nonlinearity⟩` --[t_conserved_quantity {invariant: energy_E[u]=½|∇u|²+(1/p+1)|u|^p+1}]--> output: `s_energy_conservation_for_NLS`
2. input: `⟨s_energy_conservation_for_NLS, s_nls_local_well_posedness⟩` --[t_exhaustion_squeeze {bound: a_priori_H_1_bound}]--> output: `s_a_priori_global_H_1_bound`
3. input: `s_a_priori_global_H_1_bound` --[t_interpolate_and_continue {iteration: continuation_to_T_infty}]--> output: `s_nls_global_subcritical`

**Techniques used:** t_conserved_quantity, t_exhaustion_squeeze, t_interpolate_and_continue

---

### Lax pair / integrable structure for KdV (cite: https://en.wikipedia.org/wiki/Lax_pair)

**Axioms:** `s_kdv_equation`, `s_schrodinger_operator_L_with_potential_u`
**Terminal:** `s_lax_pair_for_KdV` (kind: theorem)

**Steps:**
1. input: `⟨s_kdv_equation, s_schrodinger_operator_L_with_potential_u⟩` --[t_auxiliary_construction {object: third_order_operator_P_with_L_t=[P,L]}]--> output: `s_lax_pair_LP`
2. input: `s_lax_pair_LP` --[t_symmetry_reduction {invariant: isospectral_evolution}]--> output: `s_isospectral_evolution_of_L`
3. input: `s_isospectral_evolution_of_L` --[t_conserved_quantity {infinite_family: spectral_invariants_of_L}]--> output: `s_lax_pair_for_KdV`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_conserved_quantity

---

### Inverse scattering transform for KdV (cite: https://en.wikipedia.org/wiki/Inverse_scattering_transform)

**Axioms:** `s_lax_pair_for_KdV`, `s_decaying_initial_data`
**Terminal:** `s_inverse_scattering_transform_KdV` (kind: theorem)

**Steps:**
1. input: `⟨s_lax_pair_for_KdV, s_decaying_initial_data⟩` --[t_fourier_transform {variant: scattering_data_via_jost_solutions}]--> output: `s_scattering_data_R(k)_kappa_n_c_n`
2. input: `s_scattering_data_R(k)_kappa_n_c_n` --[t_symmetry_reduction {evolution: linear_phase_in_time}]--> output: `s_time_evolution_of_scattering_data`
3. input: `s_time_evolution_of_scattering_data` --[t_compose_with_identity {tool: gelfand_levitan_marchenko_equation}]--> output: `s_potential_reconstruction_via_GLM`
4. input: `s_potential_reconstruction_via_GLM` --[t_structural_isomorphism {pairing: direct_inverse_scattering_pair}]--> output: `s_inverse_scattering_transform_KdV`

**Techniques used:** t_fourier_transform, t_symmetry_reduction, t_compose_with_identity, t_structural_isomorphism

---

### Local well-posedness of KdV in low regularity (Bourgain spaces) (cite: https://en.wikipedia.org/wiki/Korteweg%E2%80%93de_Vries_equation)

**Axioms:** `s_kdv_equation`, `s_bourgain_space_X_s_b`
**Terminal:** `s_kdv_local_well_posedness_bourgain` (kind: theorem)

**Steps:**
1. input: `⟨s_kdv_equation, s_bourgain_space_X_s_b⟩` --[t_frequency_decomposition {basis: bourgain_modulation_decomposition}]--> output: `s_dyadic_bilinear_estimates_in_X_s_b`
2. input: `s_dyadic_bilinear_estimates_in_X_s_b` --[t_auxiliary_construction {object: nonlinear_duhamel_in_X_s_b}]--> output: `s_duhamel_form_in_bourgain_space`
3. input: `s_duhamel_form_in_bourgain_space` --[t_contraction_fixed_point {space: X_s_b_with_small_time}]--> output: `s_kdv_local_well_posedness_bourgain`

**Techniques used:** t_frequency_decomposition, t_auxiliary_construction, t_contraction_fixed_point

---

### Beale–Kato–Majda blow-up criterion (cite: https://en.wikipedia.org/wiki/Beale%E2%80%93Kato%E2%80%93Majda_theorem)

**Axioms:** `s_local_smooth_solution_of_euler`, `s_vorticity_omega`
**Terminal:** `s_beale_kato_majda_criterion` (kind: theorem)

**Steps:**
1. input: `⟨s_local_smooth_solution_of_euler, s_vorticity_omega⟩` --[t_auxiliary_construction {object: log_sobolev_inequality_for_vorticity}]--> output: `s_log_sobolev_bound_on_velocity_gradient`
2. input: `s_log_sobolev_bound_on_velocity_gradient` --[t_conserved_quantity {gronwall_for: H_s_norm}]--> output: `s_double_exponential_growth_bound`
3. input: `s_double_exponential_growth_bound` --[t_reductio_ad_absurdum {assume: blow_up_with_finite_L1_t_L_infty_vorticity}]--> output: `s_beale_kato_majda_criterion`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_reductio_ad_absurdum

---

### Local existence for incompressible Euler in 3D (cite: https://en.wikipedia.org/wiki/Euler_equations_(fluid_dynamics))

**Axioms:** `s_incompressible_euler_equations`, `s_sobolev_space_H_s_with_s_gt_5_2`
**Terminal:** `s_local_existence_euler_3d` (kind: theorem)

**Steps:**
1. input: `⟨s_incompressible_euler_equations⟩` --[t_reduce_to_canonical_form {form: projection_onto_divergence_free_vector_fields}]--> output: `s_helmholtz_projected_euler_equation`
2. input: `⟨s_helmholtz_projected_euler_equation, s_sobolev_space_H_s_with_s_gt_5_2⟩` --[t_auxiliary_construction {object: friedrichs_mollifier_approximation}]--> output: `s_approximate_smooth_solution`
3. input: `s_approximate_smooth_solution` --[t_conserved_quantity {energy: H_s_a_priori_bound_via_commutator_estimates}]--> output: `s_uniform_H_s_bound_short_time`
4. input: `s_uniform_H_s_bound_short_time` --[t_exhaustion_squeeze {limit: pass_to_limit_of_mollifications}]--> output: `s_local_existence_euler_3d`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_conserved_quantity, t_exhaustion_squeeze

---

### Leray–Hopf weak solutions of Navier–Stokes (cite: https://en.wikipedia.org/wiki/Leray%E2%80%93Hopf_solution)

**Axioms:** `s_navier_stokes_equations`, `s_L2_initial_data`
**Terminal:** `s_leray_hopf_weak_solutions` (kind: theorem)

**Steps:**
1. input: `⟨s_navier_stokes_equations⟩` --[t_auxiliary_construction {object: galerkin_finite_dim_approximation}]--> output: `s_galerkin_ode_for_first_N_modes`
2. input: `s_galerkin_ode_for_first_N_modes` --[t_conserved_quantity {energy: L2_energy_inequality}]--> output: `s_uniform_energy_bound_on_galerkin`
3. input: `s_uniform_energy_bound_on_galerkin` --[t_compactness_argument {tool: aubin_lions_compactness}]--> output: `s_convergent_subsequence_to_weak_solution`
4. input: `s_convergent_subsequence_to_weak_solution` --[t_exhaustion_squeeze {limit: pass_to_limit_in_weak_form}]--> output: `s_leray_hopf_weak_solutions`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_compactness_argument, t_exhaustion_squeeze

---

### Caffarelli–Kohn–Nirenberg partial regularity for Navier–Stokes (cite: https://en.wikipedia.org/wiki/Caffarelli%E2%80%93Kohn%E2%80%93Nirenberg_theorem)

**Axioms:** `s_leray_hopf_weak_solutions`, `s_suitable_weak_solution`
**Terminal:** `s_ckn_partial_regularity` (kind: theorem)

**Steps:**
1. input: `⟨s_suitable_weak_solution⟩` --[t_auxiliary_construction {object: local_energy_inequality_with_pressure}]--> output: `s_local_energy_inequality`
2. input: `s_local_energy_inequality` --[t_rescale_for_asymptotic_geometry {scaling: parabolic_scaling_at_singular_point}]--> output: `s_epsilon_regularity_criterion`
3. input: `⟨s_epsilon_regularity_criterion, s_leray_hopf_weak_solutions⟩` --[t_exhaustion_squeeze {covering: parabolic_hausdorff_one_dim}]--> output: `s_ckn_partial_regularity`

**Techniques used:** t_auxiliary_construction, t_rescale_for_asymptotic_geometry, t_exhaustion_squeeze

---

### Vlasov–Poisson global existence (Pfaffelmoser) (cite: https://en.wikipedia.org/wiki/Vlasov_equation)

**Axioms:** `s_vlasov_poisson_system`, `s_compactly_supported_smooth_initial_data`
**Terminal:** `s_vlasov_poisson_global_existence` (kind: theorem)

**Steps:**
1. input: `⟨s_vlasov_poisson_system, s_compactly_supported_smooth_initial_data⟩` --[t_auxiliary_construction {object: maximal_velocity_support_function_Q(t)}]--> output: `s_velocity_support_evolution_inequality`
2. input: `s_velocity_support_evolution_inequality` --[t_conserved_quantity {invariant: density_L_infty_in_terms_of_Q}]--> output: `s_double_exponential_growth_bound_on_Q`
3. input: `s_double_exponential_growth_bound_on_Q` --[t_interpolate_and_continue {iteration: continuation_via_local_existence}]--> output: `s_vlasov_poisson_global_existence`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_interpolate_and_continue

---

### Lions–Perthame global existence for Vlasov–Poisson (cite: https://en.wikipedia.org/wiki/Vlasov_equation)

**Axioms:** `s_vlasov_poisson_system`, `s_finite_velocity_moment_initial_data`
**Terminal:** `s_lions_perthame_vlasov` (kind: theorem)

**Steps:**
1. input: `⟨s_vlasov_poisson_system⟩` --[t_auxiliary_construction {object: velocity_moments_M_k(t)}]--> output: `s_evolution_inequality_for_velocity_moments`
2. input: `⟨s_evolution_inequality_for_velocity_moments, s_finite_velocity_moment_initial_data⟩` --[t_conserved_quantity {bootstrap: propagation_of_velocity_moments}]--> output: `s_global_bound_on_velocity_moments`
3. input: `s_global_bound_on_velocity_moments` --[t_interpolate_and_continue {iteration: global_continuation}]--> output: `s_lions_perthame_vlasov`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_interpolate_and_continue

---

### Galerkin existence for parabolic PDE (cite: https://en.wikipedia.org/wiki/Galerkin_method)

**Axioms:** `s_parabolic_pde_in_divergence_form`, `s_L2_initial_data`
**Terminal:** `s_galerkin_parabolic_existence` (kind: theorem)

**Steps:**
1. input: `⟨s_parabolic_pde_in_divergence_form, s_L2_initial_data⟩` --[t_auxiliary_construction {object: galerkin_truncation_in_orthonormal_basis}]--> output: `s_finite_dim_ode_approximation`
2. input: `s_finite_dim_ode_approximation` --[t_conserved_quantity {energy: parabolic_energy_estimate}]--> output: `s_uniform_a_priori_bounds_in_L2_H_1`
3. input: `s_uniform_a_priori_bounds_in_L2_H_1` --[t_compactness_argument {tool: aubin_lions_compactness}]--> output: `s_galerkin_parabolic_existence`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_compactness_argument

---

### Lions monotone-operator existence theorem (cite: https://en.wikipedia.org/wiki/Monotone_operator)

**Axioms:** `s_reflexive_banach_space`, `s_monotone_hemicontinuous_coercive_operator`
**Terminal:** `s_lions_monotone_operator_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_reflexive_banach_space, s_monotone_hemicontinuous_coercive_operator⟩` --[t_auxiliary_construction {object: galerkin_finite_dim_approximation}]--> output: `s_finite_dim_brouwer_existence`
2. input: `s_finite_dim_brouwer_existence` --[t_compactness_argument {weak_topology: weak_limits_in_reflexive}]--> output: `s_weak_limit_in_reflexive_space`
3. input: `s_weak_limit_in_reflexive_space` --[t_duality {trick: minty_monotonicity_passage}]--> output: `s_lions_monotone_operator_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_duality

---

### Minty's lemma on monotone operators (cite: https://en.wikipedia.org/wiki/Monotone_operator)

**Axioms:** `s_monotone_operator_on_hilbert_space`, `s_hemicontinuity`
**Terminal:** `s_minty_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_monotone_operator_on_hilbert_space⟩` --[t_duality {pair: weak_limit_against_test_vector}]--> output: `s_pairing_against_test_in_monotone_form`
2. input: `⟨s_pairing_against_test_in_monotone_form, s_hemicontinuity⟩` --[t_exhaustion_squeeze {limit: t_to_zero_in_v=u+tw}]--> output: `s_minty_lemma`

**Techniques used:** t_duality, t_exhaustion_squeeze

---

## 4. Geometric flows and harmonic maps

### Hamilton short-time existence for Ricci flow (cite: https://en.wikipedia.org/wiki/Ricci_flow)

**Axioms:** `s_riemannian_metric`, `s_ricci_flow_equation`
**Terminal:** `s_hamilton_short_time_ricci_flow` (kind: theorem)

**Steps:**
1. input: `⟨s_ricci_flow_equation⟩` --[t_reduce_to_canonical_form {trick: DeTurck_gauge_fixing_to_strictly_parabolic}]--> output: `s_deturck_strictly_parabolic_system`
2. input: `⟨s_deturck_strictly_parabolic_system, s_riemannian_metric⟩` --[t_contraction_fixed_point {space: short_time_parabolic_holder_space}]--> output: `s_short_time_solution_of_deturck_system`
3. input: `s_short_time_solution_of_deturck_system` --[t_symmetry_reduction {gauge: diffeomorphism_pull_back}]--> output: `s_hamilton_short_time_ricci_flow`

**Techniques used:** t_reduce_to_canonical_form, t_contraction_fixed_point, t_symmetry_reduction

---

### DeTurck trick (cite: https://en.wikipedia.org/wiki/Ricci_flow)

**Axioms:** `s_ricci_flow_equation`, `s_diffeomorphism_gauge_field`
**Terminal:** `s_deturck_trick` (kind: theorem)

**Steps:**
1. input: `⟨s_ricci_flow_equation⟩` --[t_symmetry_reduction {symmetry: diffeomorphism_invariance}]--> output: `s_gauge_orbit_of_metrics`
2. input: `⟨s_gauge_orbit_of_metrics, s_diffeomorphism_gauge_field⟩` --[t_auxiliary_construction {object: harmonic_map_heat_flow_gauge}]--> output: `s_deturck_modified_ricci_flow`
3. input: `s_deturck_modified_ricci_flow` --[t_compose_with_identity {framework: strictly_parabolic_system}]--> output: `s_deturck_trick`

**Techniques used:** t_symmetry_reduction, t_auxiliary_construction, t_compose_with_identity

---

### Eells–Sampson harmonic map heat flow existence (cite: https://en.wikipedia.org/wiki/Harmonic_map)

**Axioms:** `s_smooth_map_between_riemannian_manifolds`, `s_target_with_nonpositive_sectional_curvature`
**Terminal:** `s_eells_sampson_harmonic_map_flow` (kind: theorem)

**Steps:**
1. input: `⟨s_target_with_nonpositive_sectional_curvature⟩` --[t_auxiliary_construction {object: energy_functional_E[u]=½∫|du|²}]--> output: `s_dirichlet_energy_for_maps`
2. input: `⟨s_dirichlet_energy_for_maps, s_smooth_map_between_riemannian_manifolds⟩` --[t_conserved_quantity {monotone: Bochner_formula_yields_subharmonic_density}]--> output: `s_bochner_subharmonicity_of_energy_density`
3. input: `s_bochner_subharmonicity_of_energy_density` --[t_exhaustion_squeeze {flow: gradient_heat_flow_for_E}]--> output: `s_long_time_existence_of_harmonic_heat_flow`
4. input: `s_long_time_existence_of_harmonic_heat_flow` --[t_interpolate_and_continue {limit: t_to_infinity_harmonic_map}]--> output: `s_eells_sampson_harmonic_map_flow`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_exhaustion_squeeze, t_interpolate_and_continue

---

### Schoen–Uhlenbeck regularity for harmonic maps (cite: https://en.wikipedia.org/wiki/Harmonic_map)

**Axioms:** `s_minimizing_harmonic_map`, `s_target_riemannian_manifold`
**Terminal:** `s_schoen_uhlenbeck_regularity` (kind: theorem)

**Steps:**
1. input: `⟨s_minimizing_harmonic_map⟩` --[t_rescale_for_asymptotic_geometry {scaling: tangent_map_at_a_point}]--> output: `s_tangent_map_homogeneous_minimizer`
2. input: `s_tangent_map_homogeneous_minimizer` --[t_auxiliary_construction {object: epsilon_regularity_for_small_energy_balls}]--> output: `s_epsilon_regularity_lemma`
3. input: `⟨s_epsilon_regularity_lemma, s_target_riemannian_manifold⟩` --[t_exhaustion_squeeze {dimension: singular_set_codim_at_least_3}]--> output: `s_schoen_uhlenbeck_regularity`

**Techniques used:** t_rescale_for_asymptotic_geometry, t_auxiliary_construction, t_exhaustion_squeeze

---

### Mean curvature flow short-time existence (cite: https://en.wikipedia.org/wiki/Mean_curvature_flow)

**Axioms:** `s_smooth_hypersurface_in_R_n_plus_1`, `s_mean_curvature_vector_H`
**Terminal:** `s_mcf_short_time_existence` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_hypersurface_in_R_n_plus_1, s_mean_curvature_vector_H⟩` --[t_reduce_to_canonical_form {graph: locally_express_surface_as_graph_over_tangent}]--> output: `s_graphical_mcf_quasilinear_parabolic_equation`
2. input: `s_graphical_mcf_quasilinear_parabolic_equation` --[t_contraction_fixed_point {space: parabolic_holder_short_time}]--> output: `s_short_time_graphical_solution`
3. input: `s_short_time_graphical_solution` --[t_exhaustion_squeeze {patching: cover_surface_by_local_graphs}]--> output: `s_mcf_short_time_existence`

**Techniques used:** t_reduce_to_canonical_form, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Huisken's monotonicity formula for MCF (cite: https://en.wikipedia.org/wiki/Mean_curvature_flow)

**Axioms:** `s_mcf_short_time_existence`, `s_backward_heat_kernel_in_R_n_plus_1`
**Terminal:** `s_huisken_monotonicity_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_backward_heat_kernel_in_R_n_plus_1⟩` --[t_auxiliary_construction {object: gaussian_density_phi_at_singular_point}]--> output: `s_gaussian_density_function_theta`
2. input: `⟨s_gaussian_density_function_theta, s_mcf_short_time_existence⟩` --[t_conserved_quantity {monotone: d/dt_theta_le_0}]--> output: `s_huisken_monotonicity_formula`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity

---

### Schoen–Yau positive mass theorem (cite: https://en.wikipedia.org/wiki/Positive_energy_theorem)

**Axioms:** `s_asymptotically_flat_3_manifold`, `s_nonnegative_scalar_curvature`
**Terminal:** `s_schoen_yau_positive_mass` (kind: theorem)

**Steps:**
1. input: `⟨s_asymptotically_flat_3_manifold, s_nonnegative_scalar_curvature⟩` --[t_auxiliary_construction {object: asymptotic_minimal_surface_capturing_ADM_mass}]--> output: `s_minimal_surface_argument`
2. input: `s_minimal_surface_argument` --[t_reductio_ad_absurdum {assume: negative_ADM_mass}]--> output: `s_contradiction_via_stable_minimal_surface`
3. input: `s_contradiction_via_stable_minimal_surface` --[t_rescale_for_asymptotic_geometry {scaling: asymptotic_to_euclidean}]--> output: `s_schoen_yau_positive_mass`

**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum, t_rescale_for_asymptotic_geometry

---

### Yang–Mills heat flow existence (cite: https://en.wikipedia.org/wiki/Yang%E2%80%93Mills_equations)

**Axioms:** `s_yang_mills_functional`, `s_principal_bundle_over_compact_4_manifold`
**Terminal:** `s_yang_mills_heat_flow_existence` (kind: theorem)

**Steps:**
1. input: `⟨s_yang_mills_functional⟩` --[t_reduce_to_canonical_form {gauge: coulomb_gauge}]--> output: `s_coulomb_gauge_yang_mills_flow`
2. input: `⟨s_coulomb_gauge_yang_mills_flow, s_principal_bundle_over_compact_4_manifold⟩` --[t_conserved_quantity {energy: yang_mills_energy_E[A]}]--> output: `s_yang_mills_energy_a_priori_bound`
3. input: `s_yang_mills_energy_a_priori_bound` --[t_exhaustion_squeeze {flow: parabolic_gradient_flow_with_bubbling}]--> output: `s_yang_mills_heat_flow_existence`

**Techniques used:** t_reduce_to_canonical_form, t_conserved_quantity, t_exhaustion_squeeze

---

### Uhlenbeck compactness for Yang–Mills (cite: https://en.wikipedia.org/wiki/Uhlenbeck%27s_theorem)

**Axioms:** `s_sequence_of_connections_with_L_2_bounded_curvature`, `s_principal_bundle_over_compact_4_manifold`
**Terminal:** `s_uhlenbeck_compactness_yang_mills` (kind: theorem)

**Steps:**
1. input: `⟨s_sequence_of_connections_with_L_2_bounded_curvature⟩` --[t_reduce_to_canonical_form {gauge: coulomb_gauge_existence_lemma}]--> output: `s_coulomb_gauge_representatives`
2. input: `⟨s_coulomb_gauge_representatives, s_principal_bundle_over_compact_4_manifold⟩` --[t_compactness_argument {tool: weak_compactness_in_W_1_2}]--> output: `s_weak_limit_of_connections_modulo_gauge`
3. input: `s_weak_limit_of_connections_modulo_gauge` --[t_exhaustion_squeeze {bubble: removable_singularity_at_concentration_points}]--> output: `s_uhlenbeck_compactness_yang_mills`

**Techniques used:** t_reduce_to_canonical_form, t_compactness_argument, t_exhaustion_squeeze

---

## 5. Maximum principles, variational and other classical results

### Lewy's example of unsolvable linear PDE (cite: https://en.wikipedia.org/wiki/Hans_Lewy)

**Axioms:** `s_lewy_operator_d_dz_minus_2i_z_bar_d_dt`, `s_smooth_inhomogeneity`
**Terminal:** `s_lewy_unsolvability` (kind: theorem)

**Steps:**
1. input: `⟨s_lewy_operator_d_dz_minus_2i_z_bar_d_dt⟩` --[t_auxiliary_construction {object: tangential_CR_operator_on_boundary}]--> output: `s_cr_operator_realization`
2. input: `⟨s_cr_operator_realization, s_smooth_inhomogeneity⟩` --[t_reductio_ad_absurdum {assume: distributional_solution_exists}]--> output: `s_contradiction_via_hartogs_extension`
3. input: `s_contradiction_via_hartogs_extension` --[t_compose_with_identity {framework: nonzero_obstruction_to_local_solvability}]--> output: `s_lewy_unsolvability`

**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum, t_compose_with_identity

---

### Malgrange–Ehrenpreis theorem (cite: https://en.wikipedia.org/wiki/Malgrange%E2%80%93Ehrenpreis_theorem)

**Axioms:** `s_constant_coefficient_linear_pde_operator`, `s_compactly_supported_distribution`
**Terminal:** `s_malgrange_ehrenpreis_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_constant_coefficient_linear_pde_operator⟩` --[t_fourier_transform {target: division_by_polynomial_symbol_P(xi)}]--> output: `s_division_in_paley_wiener_space`
2. input: `s_division_in_paley_wiener_space` --[t_auxiliary_construction {object: contour_shift_to_avoid_zero_set_of_P}]--> output: `s_fundamental_solution_E`
3. input: `⟨s_fundamental_solution_E, s_compactly_supported_distribution⟩` --[t_compose_with_identity {framework: convolution_with_fundamental_solution}]--> output: `s_malgrange_ehrenpreis_theorem`

**Techniques used:** t_fourier_transform, t_auxiliary_construction, t_compose_with_identity

---

### Poincaré–Hopf for vector fields (cite: https://en.wikipedia.org/wiki/Poincar%C3%A9%E2%80%93Hopf_theorem)

**Axioms:** `s_smooth_vector_field_with_isolated_zeros`, `s_compact_smooth_manifold`
**Terminal:** `s_poincare_hopf_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_vector_field_with_isolated_zeros⟩` --[t_auxiliary_construction {object: local_index_at_each_zero}]--> output: `s_local_index_count`
2. input: `⟨s_local_index_count, s_compact_smooth_manifold⟩` --[t_obstruction_class {invariant: euler_class_of_TM}]--> output: `s_global_index_equals_euler_characteristic`
3. input: `s_global_index_equals_euler_characteristic` --[t_compose_with_identity {framework: index_invariance_under_isotopy}]--> output: `s_poincare_hopf_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_compose_with_identity

---

### Direct method of calculus of variations (cite: https://en.wikipedia.org/wiki/Direct_method_in_the_calculus_of_variations)

**Axioms:** `s_coercive_lower_semicontinuous_functional`, `s_reflexive_banach_space`
**Terminal:** `s_direct_method_calculus_of_variations` (kind: theorem)

**Steps:**
1. input: `⟨s_coercive_lower_semicontinuous_functional⟩` --[t_auxiliary_construction {object: minimizing_sequence_in_sublevel_set}]--> output: `s_bounded_minimizing_sequence`
2. input: `⟨s_bounded_minimizing_sequence, s_reflexive_banach_space⟩` --[t_compactness_argument {tool: banach_alaoglu_weak_compactness}]--> output: `s_weak_limit_candidate_minimizer`
3. input: `s_weak_limit_candidate_minimizer` --[t_exhaustion_squeeze {lower_semicontinuity: pass_to_limit}]--> output: `s_direct_method_calculus_of_variations`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Euler–Lagrange equation derivation (cite: https://en.wikipedia.org/wiki/Euler%E2%80%93Lagrange_equation)

**Axioms:** `s_action_functional_J[u]_equals_integral_L`, `s_compactly_supported_variation`
**Terminal:** `s_euler_lagrange_equation` (kind: theorem)

**Steps:**
1. input: `⟨s_action_functional_J[u]_equals_integral_L⟩` --[t_auxiliary_construction {object: first_variation_d_d_epsilon_J[u+epsilon_h]}]--> output: `s_first_variation_formula`
2. input: `⟨s_first_variation_formula, s_compactly_supported_variation⟩` --[t_compose_with_identity {step: integration_by_parts}]--> output: `s_weak_form_with_arbitrary_test_function`
3. input: `s_weak_form_with_arbitrary_test_function` --[t_duality {trick: fundamental_lemma_of_calculus_of_variations}]--> output: `s_euler_lagrange_equation`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_duality

---

### Pohozaev identity (cite: https://en.wikipedia.org/wiki/Poho%C5%BEaev%27s_identity)

**Axioms:** `s_semilinear_elliptic_equation`, `s_starshaped_bounded_domain`
**Terminal:** `s_pohozaev_identity` (kind: theorem)

**Steps:**
1. input: `⟨s_semilinear_elliptic_equation⟩` --[t_auxiliary_construction {object: multiplier_x_dot_grad_u}]--> output: `s_multiplied_equation_by_x_dot_grad_u`
2. input: `⟨s_multiplied_equation_by_x_dot_grad_u, s_starshaped_bounded_domain⟩` --[t_compose_with_identity {step: integrate_by_parts_with_pohozaev_multiplier}]--> output: `s_boundary_volume_identity`
3. input: `s_boundary_volume_identity` --[t_reductio_ad_absurdum {assume: nontrivial_solution_for_supercritical_p}]--> output: `s_pohozaev_identity`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_reductio_ad_absurdum

---

### Mountain pass theorem (cite: https://en.wikipedia.org/wiki/Mountain_pass_theorem)

**Axioms:** `s_C_1_functional_with_palais_smale`, `s_two_separated_local_minima`
**Terminal:** `s_mountain_pass_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_two_separated_local_minima⟩` --[t_auxiliary_construction {object: family_of_paths_gamma_between_minima}]--> output: `s_minimax_value_c_equals_inf_max_J_on_gamma`
2. input: `⟨s_minimax_value_c_equals_inf_max_J_on_gamma, s_C_1_functional_with_palais_smale⟩` --[t_compactness_argument {hypothesis: palais_smale_at_level_c}]--> output: `s_palais_smale_sequence_at_level_c`
3. input: `s_palais_smale_sequence_at_level_c` --[t_exhaustion_squeeze {limit: convergent_subsequence_critical_point}]--> output: `s_mountain_pass_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Ekeland's variational principle (cite: https://en.wikipedia.org/wiki/Ekeland%27s_variational_principle)

**Axioms:** `s_complete_metric_space`, `s_lower_semicontinuous_bounded_below_function`
**Terminal:** `s_ekeland_variational_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_lower_semicontinuous_bounded_below_function⟩` --[t_auxiliary_construction {object: perturbed_function_f+epsilon_d(x,x_0)}]--> output: `s_perturbed_lsc_function`
2. input: `⟨s_perturbed_lsc_function, s_complete_metric_space⟩` --[t_contraction_fixed_point {scheme: cantor_intersection_of_descending_closed_sets}]--> output: `s_almost_minimizer_with_local_min_property`
3. input: `s_almost_minimizer_with_local_min_property` --[t_compose_with_identity {framework: epsilon_approximate_critical_point}]--> output: `s_ekeland_variational_principle`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_compose_with_identity

---

### Pohozaev nonexistence for supercritical Yamabe-type equations (cite: https://en.wikipedia.org/wiki/Yamabe_problem)

**Axioms:** `s_supercritical_semilinear_elliptic`, `s_starshaped_bounded_domain`
**Terminal:** `s_pohozaev_nonexistence_supercritical` (kind: theorem)

**Steps:**
1. input: `⟨s_supercritical_semilinear_elliptic⟩` --[t_compose_with_identity {prior: pohozaev_identity}]--> output: `s_signed_boundary_integral`
2. input: `⟨s_signed_boundary_integral, s_starshaped_bounded_domain⟩` --[t_reductio_ad_absurdum {assume: nontrivial_positive_solution}]--> output: `s_pohozaev_nonexistence_supercritical`

**Techniques used:** t_compose_with_identity, t_reductio_ad_absurdum

---

### Sobolev–Talenti–Aubin Yamabe problem solution (cite: https://en.wikipedia.org/wiki/Yamabe_problem)

**Axioms:** `s_riemannian_metric`, `s_yamabe_functional_Q[g]`
**Terminal:** `s_yamabe_problem_solution` (kind: theorem)

**Steps:**
1. input: `⟨s_yamabe_functional_Q[g]⟩` --[t_auxiliary_construction {object: subcritical_approximation_p_to_2_star}]--> output: `s_subcritical_minimizers_u_p`
2. input: `s_subcritical_minimizers_u_p` --[t_compactness_argument {tool: positive_mass_to_beat_sphere_threshold}]--> output: `s_minimizer_below_sphere_threshold_Y(S_n)`
3. input: `⟨s_minimizer_below_sphere_threshold_Y(S_n), s_riemannian_metric⟩` --[t_exhaustion_squeeze {limit: p_to_2_star_minimizer_exists}]--> output: `s_yamabe_problem_solution`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Liouville theorem for nonnegative elliptic solutions in R^n (cite: https://en.wikipedia.org/wiki/Liouville%27s_theorem_(differential_equations))

**Axioms:** `s_semilinear_elliptic_in_R_n`, `s_nonnegative_classical_solution`
**Terminal:** `s_gidas_ni_nirenberg_liouville` (kind: theorem)

**Steps:**
1. input: `⟨s_nonnegative_classical_solution⟩` --[t_symmetry_reduction {method: moving_planes}]--> output: `s_radial_symmetry_via_moving_planes`
2. input: `s_radial_symmetry_via_moving_planes` --[t_reduce_to_canonical_form {form: ODE_in_radial_variable}]--> output: `s_radial_ode_problem`
3. input: `⟨s_radial_ode_problem, s_semilinear_elliptic_in_R_n⟩` --[t_reductio_ad_absurdum {assume: nontrivial_nonnegative_radial_solution}]--> output: `s_gidas_ni_nirenberg_liouville`

**Techniques used:** t_symmetry_reduction, t_reduce_to_canonical_form, t_reductio_ad_absurdum

---

### Gidas–Ni–Nirenberg radial symmetry (cite: https://en.wikipedia.org/wiki/Gidas%E2%80%93Ni%E2%80%93Nirenberg_theorem)

**Axioms:** `s_positive_solution_in_ball`, `s_semilinear_elliptic_in_R_n`
**Terminal:** `s_gidas_ni_nirenberg_symmetry` (kind: theorem)

**Steps:**
1. input: `⟨s_positive_solution_in_ball⟩` --[t_auxiliary_construction {object: hyperplane_reflection_T_lambda}]--> output: `s_reflected_solution_u_lambda`
2. input: `s_reflected_solution_u_lambda` --[t_symmetry_reduction {method: moving_planes_via_strong_max_principle}]--> output: `s_solution_symmetric_about_critical_plane`
3. input: `⟨s_solution_symmetric_about_critical_plane, s_semilinear_elliptic_in_R_n⟩` --[t_compose_with_identity {framework: rotate_to_every_direction}]--> output: `s_gidas_ni_nirenberg_symmetry`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_compose_with_identity

---

## 6. Numerical / finite-difference and convergence theorems

### Lax equivalence theorem (cite: https://en.wikipedia.org/wiki/Lax_equivalence_theorem)

**Axioms:** `s_well_posed_linear_initial_value_problem`, `s_consistent_finite_difference_scheme`
**Terminal:** `s_lax_equivalence_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_consistent_finite_difference_scheme⟩` --[t_axiomatize_from_instances {triple: consistency_stability_convergence}]--> output: `s_three_property_axiom_definition`
2. input: `⟨s_three_property_axiom_definition, s_well_posed_linear_initial_value_problem⟩` --[t_compactness_argument {tool: banach_steinhaus_for_uniform_bound}]--> output: `s_stability_implies_uniform_boundedness`
3. input: `s_stability_implies_uniform_boundedness` --[t_structural_isomorphism {biconditional: stable_consistent_iff_convergent}]--> output: `s_lax_equivalence_theorem`

**Techniques used:** t_axiomatize_from_instances, t_compactness_argument, t_structural_isomorphism

---

### Von Neumann stability analysis (cite: https://en.wikipedia.org/wiki/Von_Neumann_stability_analysis)

**Axioms:** `s_constant_coefficient_finite_difference_scheme`, `s_periodic_grid`
**Terminal:** `s_von_neumann_stability_criterion` (kind: theorem)

**Steps:**
1. input: `⟨s_constant_coefficient_finite_difference_scheme, s_periodic_grid⟩` --[t_fourier_transform {discrete: dft_on_grid}]--> output: `s_amplification_factor_g(k)`
2. input: `s_amplification_factor_g(k)` --[t_structural_isomorphism {criterion: max_modulus_le_1_plus_O_dt}]--> output: `s_von_neumann_stability_criterion`

**Techniques used:** t_fourier_transform, t_structural_isomorphism

---

### CFL convergence criterion for hyperbolic schemes (cite: https://en.wikipedia.org/wiki/Courant%E2%80%93Friedrichs%E2%80%93Lewy_condition)

**Axioms:** `s_explicit_finite_difference_for_hyperbolic_pde`, `s_characteristic_propagation_cone`
**Terminal:** `s_cfl_criterion` (kind: theorem)

**Steps:**
1. input: `⟨s_explicit_finite_difference_for_hyperbolic_pde⟩` --[t_auxiliary_construction {object: domain_of_dependence_for_scheme}]--> output: `s_numerical_domain_of_dependence`
2. input: `⟨s_numerical_domain_of_dependence, s_characteristic_propagation_cone⟩` --[t_reductio_ad_absurdum {assume: scheme_domain_smaller_than_PDE_domain}]--> output: `s_cfl_criterion`

**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum

---

### Lax–Wendroff convergence theorem for conservation laws (cite: https://en.wikipedia.org/wiki/Lax%E2%80%93Wendroff_theorem)

**Axioms:** `s_consistent_conservative_finite_difference_scheme`, `s_a_priori_BV_bound`
**Terminal:** `s_lax_wendroff_convergence` (kind: theorem)

**Steps:**
1. input: `⟨s_consistent_conservative_finite_difference_scheme⟩` --[t_compactness_argument {space: BV_with_helly_selection}]--> output: `s_convergent_subsequence_to_function_v`
2. input: `⟨s_convergent_subsequence_to_function_v, s_a_priori_BV_bound⟩` --[t_exhaustion_squeeze {limit: weak_form_of_conservation_law}]--> output: `s_v_is_weak_entropy_solution`
3. input: `s_v_is_weak_entropy_solution` --[t_compose_with_identity {framework: weak_consistency}]--> output: `s_lax_wendroff_convergence`

**Techniques used:** t_compactness_argument, t_exhaustion_squeeze, t_compose_with_identity

---

### Kruzhkov uniqueness for scalar conservation laws (cite: https://en.wikipedia.org/wiki/Conservation_law_(physics))

**Axioms:** `s_scalar_conservation_law_u_t+f(u)_x=0`, `s_kruzhkov_entropy_pair`
**Terminal:** `s_kruzhkov_uniqueness_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_kruzhkov_entropy_pair⟩` --[t_auxiliary_construction {object: family_eta_k(u)=|u-k|}]--> output: `s_kruzhkov_doubling_variables_technique`
2. input: `⟨s_kruzhkov_doubling_variables_technique, s_scalar_conservation_law_u_t+f(u)_x=0⟩` --[t_exhaustion_squeeze {limit: entropy_inequality_after_diagonal_limit}]--> output: `s_L1_contraction_for_entropy_solutions`
3. input: `s_L1_contraction_for_entropy_solutions` --[t_compose_with_identity {framework: uniqueness_in_L1}]--> output: `s_kruzhkov_uniqueness_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_compose_with_identity

---

### Vanishing viscosity convergence (cite: https://en.wikipedia.org/wiki/Vanishing_viscosity)

**Axioms:** `s_scalar_conservation_law_u_t+f(u)_x=0`, `s_viscous_approximation_u_epsilon`
**Terminal:** `s_vanishing_viscosity_convergence` (kind: theorem)

**Steps:**
1. input: `⟨s_viscous_approximation_u_epsilon⟩` --[t_conserved_quantity {bound: a_priori_BV_uniform_in_epsilon}]--> output: `s_BV_uniform_bound`
2. input: `⟨s_BV_uniform_bound, s_scalar_conservation_law_u_t+f(u)_x=0⟩` --[t_compactness_argument {tool: helly_selection_in_BV}]--> output: `s_convergent_subsequence`
3. input: `s_convergent_subsequence` --[t_exhaustion_squeeze {limit: entropy_inequality_for_limit}]--> output: `s_vanishing_viscosity_convergence`

**Techniques used:** t_conserved_quantity, t_compactness_argument, t_exhaustion_squeeze

---

## 7. Spectral, scattering, and microlocal theorems

### Stone's theorem on one-parameter unitary groups (cite: https://en.wikipedia.org/wiki/Stone%27s_theorem_on_one-parameter_unitary_groups)

**Axioms:** `s_strongly_continuous_one_parameter_unitary_group`, `s_hilbert_space`
**Terminal:** `s_stone_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_strongly_continuous_one_parameter_unitary_group⟩` --[t_auxiliary_construction {object: infinitesimal_generator_iA=lim_t→0_(U(t)−1)/t}]--> output: `s_generator_iA_self_adjoint_candidate`
2. input: `⟨s_generator_iA_self_adjoint_candidate, s_hilbert_space⟩` --[t_svd_and_spectral_decomposition {tool: spectral_theorem_for_unbounded_SA}]--> output: `s_spectral_resolution_of_A`
3. input: `s_spectral_resolution_of_A` --[t_structural_isomorphism {bijection: unitary_groups_iff_self_adjoint_generators}]--> output: `s_stone_theorem`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_structural_isomorphism

---

### Hille–Yosida theorem for semigroups (cite: https://en.wikipedia.org/wiki/Hille%E2%80%93Yosida_theorem)

**Axioms:** `s_densely_defined_closed_linear_operator`, `s_resolvent_bound_on_real_axis`
**Terminal:** `s_hille_yosida_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_densely_defined_closed_linear_operator, s_resolvent_bound_on_real_axis⟩` --[t_auxiliary_construction {object: yosida_approximation_A_lambda=lambda·A·(lambda-A)^-1}]--> output: `s_yosida_bounded_approximants`
2. input: `s_yosida_bounded_approximants` --[t_exhaustion_squeeze {limit: lambda_to_infinity_strong_convergence}]--> output: `s_generated_C_0_semigroup`
3. input: `s_generated_C_0_semigroup` --[t_structural_isomorphism {bijection: generators_iff_C0_semigroups}]--> output: `s_hille_yosida_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_structural_isomorphism

---

### Lumer–Phillips theorem for dissipative operators (cite: https://en.wikipedia.org/wiki/Lumer%E2%80%93Phillips_theorem)

**Axioms:** `s_dissipative_operator_on_hilbert_space`, `s_range_condition_lambda_A_surjective`
**Terminal:** `s_lumer_phillips_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_dissipative_operator_on_hilbert_space⟩` --[t_conserved_quantity {monotone: Re(Au,u)≤0}]--> output: `s_contraction_property_of_resolvent`
2. input: `⟨s_contraction_property_of_resolvent, s_range_condition_lambda_A_surjective⟩` --[t_compose_with_identity {tool: hille_yosida_for_contraction_semigroups}]--> output: `s_contraction_semigroup_generation`
3. input: `s_contraction_semigroup_generation` --[t_compose_with_identity {framework: dissipativity_iff_contraction_semigroup}]--> output: `s_lumer_phillips_theorem`

**Techniques used:** t_conserved_quantity, t_compose_with_identity, t_compose_with_identity

---

### Trotter–Kato product formula (cite: https://en.wikipedia.org/wiki/Trotter_product_formula)

**Axioms:** `s_two_semigroup_generators_A_B`, `s_sum_A_plus_B_generates_semigroup`
**Terminal:** `s_trotter_kato_product_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_two_semigroup_generators_A_B⟩` --[t_auxiliary_construction {object: trotter_splitting_(e^tA/n_e^tB/n)^n}]--> output: `s_trotter_splitting_approximant`
2. input: `⟨s_trotter_splitting_approximant, s_sum_A_plus_B_generates_semigroup⟩` --[t_exhaustion_squeeze {limit: n_to_infinity_strong_convergence}]--> output: `s_trotter_kato_product_formula`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze

---

### Kato–Rellich self-adjointness theorem (cite: https://en.wikipedia.org/wiki/Kato%E2%80%93Rellich_theorem)

**Axioms:** `s_self_adjoint_operator_A`, `s_symmetric_relatively_bounded_perturbation_B`
**Terminal:** `s_kato_rellich_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_self_adjoint_operator_A, s_symmetric_relatively_bounded_perturbation_B⟩` --[t_auxiliary_construction {object: A_plus_B_with_estimate_||Bu||≤a||Au||+b||u||_with_a<1}]--> output: `s_relatively_bounded_sum`
2. input: `s_relatively_bounded_sum` --[t_compactness_argument {operator: range_of_A+B+iλ_dense}]--> output: `s_essentially_self_adjointness_of_sum`
3. input: `s_essentially_self_adjointness_of_sum` --[t_compose_with_identity {framework: stability_of_self_adjointness_under_perturbation}]--> output: `s_kato_rellich_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_compose_with_identity

---

### Weyl's law for eigenvalue counting (cite: https://en.wikipedia.org/wiki/Weyl_law)

**Axioms:** `s_dirichlet_laplacian_on_bounded_domain`, `s_eigenvalue_counting_function_N(lambda)`
**Terminal:** `s_weyl_law` (kind: theorem)

**Steps:**
1. input: `⟨s_dirichlet_laplacian_on_bounded_domain⟩` --[t_auxiliary_construction {object: trace_of_heat_kernel_Tr_e^(tΔ)}]--> output: `s_heat_kernel_trace_asymptotic`
2. input: `s_heat_kernel_trace_asymptotic` --[t_exhaustion_squeeze {tool: tauberian_theorem}]--> output: `s_N(lambda)_asymptotic_(2π)^-n_omega_n_vol_Omega_lambda^n/2`
3. input: `⟨s_N(lambda)_asymptotic_(2π)^-n_omega_n_vol_Omega_lambda^n/2, s_eigenvalue_counting_function_N(lambda)⟩` --[t_compose_with_identity {framework: weyl_asymptotic}]--> output: `s_weyl_law`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_compose_with_identity

---

### Agmon decay of eigenfunctions (cite: https://en.wikipedia.org/wiki/Agmon%27s_theorem)

**Axioms:** `s_schrodinger_operator_minus_delta_plus_V`, `s_eigenfunction_below_essential_spectrum`
**Terminal:** `s_agmon_decay_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_eigenfunction_below_essential_spectrum⟩` --[t_auxiliary_construction {object: agmon_distance_rho(x)_via_riemannian_metric_(V-E)_+}]--> output: `s_agmon_riemannian_distance`
2. input: `⟨s_agmon_riemannian_distance, s_schrodinger_operator_minus_delta_plus_V⟩` --[t_conserved_quantity {weighted_energy: integration_by_parts_with_e^(2rho)}]--> output: `s_weighted_energy_estimate`
3. input: `s_weighted_energy_estimate` --[t_exhaustion_squeeze {limit: exponential_decay_at_rate_rho}]--> output: `s_agmon_decay_theorem`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_exhaustion_squeeze

---

### Hörmander wavefront set propagation theorem (cite: https://en.wikipedia.org/wiki/Wavefront_set)

**Axioms:** `s_pseudodifferential_operator_P_principal_type`, `s_distribution_solution_Pu=0`
**Terminal:** `s_propagation_of_singularities` (kind: theorem)

**Steps:**
1. input: `⟨s_pseudodifferential_operator_P_principal_type⟩` --[t_auxiliary_construction {object: hamiltonian_vector_field_of_principal_symbol_p}]--> output: `s_bicharacteristic_flow_of_p`
2. input: `⟨s_bicharacteristic_flow_of_p, s_distribution_solution_Pu=0⟩` --[t_frequency_decomposition {tool: pseudodifferential_microlocalization}]--> output: `s_wavefront_set_invariant_under_bicharacteristic_flow`
3. input: `s_wavefront_set_invariant_under_bicharacteristic_flow` --[t_compose_with_identity {framework: propagation_of_singularities}]--> output: `s_propagation_of_singularities`

**Techniques used:** t_auxiliary_construction, t_frequency_decomposition, t_compose_with_identity

---

### Lax–Phillips scattering theory (cite: https://en.wikipedia.org/wiki/Lax%E2%80%93Phillips_scattering)

**Axioms:** `s_unperturbed_unitary_group`, `s_perturbed_unitary_group_with_compactly_supported_obstacle`
**Terminal:** `s_lax_phillips_scattering` (kind: theorem)

**Steps:**
1. input: `⟨s_unperturbed_unitary_group, s_perturbed_unitary_group_with_compactly_supported_obstacle⟩` --[t_auxiliary_construction {object: incoming_outgoing_subspaces_D_minus_D_plus}]--> output: `s_translation_representation_via_D_minus_D_plus`
2. input: `s_translation_representation_via_D_minus_D_plus` --[t_duality {pair: wave_operators_W_pm}]--> output: `s_wave_operators_intertwining`
3. input: `s_wave_operators_intertwining` --[t_compose_with_identity {object: scattering_operator_S=W_+^*_W_-}]--> output: `s_lax_phillips_scattering`

**Techniques used:** t_auxiliary_construction, t_duality, t_compose_with_identity

---

### Birman–Schwinger principle (cite: https://en.wikipedia.org/wiki/Birman%E2%80%93Schwinger_principle)

**Axioms:** `s_schrodinger_operator_minus_delta_plus_V`, `s_negative_eigenvalue_minus_E`
**Terminal:** `s_birman_schwinger_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_schrodinger_operator_minus_delta_plus_V, s_negative_eigenvalue_minus_E⟩` --[t_auxiliary_construction {object: birman_schwinger_operator_K_E=|V|^1/2_(-Δ+E)^-1_|V|^1/2}]--> output: `s_birman_schwinger_operator_K_E`
2. input: `s_birman_schwinger_operator_K_E` --[t_structural_isomorphism {bijection: eigenvalues_of_H_below_zero_iff_K_E_has_eigenvalue_1}]--> output: `s_birman_schwinger_principle`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism

---

### Cwikel–Lieb–Rozenblum bound on bound states (cite: https://en.wikipedia.org/wiki/Cwikel%E2%80%93Lieb%E2%80%93Rozenblum_inequality)

**Axioms:** `s_schrodinger_operator_minus_delta_plus_V`, `s_negative_part_V_minus_in_L_n_2`
**Terminal:** `s_clr_bound` (kind: theorem)

**Steps:**
1. input: `⟨s_negative_part_V_minus_in_L_n_2⟩` --[t_compose_with_identity {tool: birman_schwinger_principle}]--> output: `s_negative_eigenvalues_via_birman_schwinger`
2. input: `s_negative_eigenvalues_via_birman_schwinger` --[t_auxiliary_construction {tool: trace_class_estimate_for_K_0}]--> output: `s_trace_norm_bound_on_K_0`
3. input: `⟨s_trace_norm_bound_on_K_0, s_schrodinger_operator_minus_delta_plus_V⟩` --[t_exhaustion_squeeze {bound: N(V)_le_C_n_||V_minus||_L_n/2^n/2}]--> output: `s_clr_bound`

**Techniques used:** t_compose_with_identity, t_auxiliary_construction, t_exhaustion_squeeze

---

### Lieb–Thirring inequality (cite: https://en.wikipedia.org/wiki/Lieb%E2%80%93Thirring_inequality)

**Axioms:** `s_schrodinger_operator_minus_delta_plus_V`, `s_negative_eigenvalue_moments_gamma_geq_1`
**Terminal:** `s_lieb_thirring_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_negative_eigenvalue_moments_gamma_geq_1⟩` --[t_compose_with_identity {tool: birman_schwinger_principle}]--> output: `s_eigenvalue_moments_via_trace_of_K_E`
2. input: `s_eigenvalue_moments_via_trace_of_K_E` --[t_interpolate_and_continue {scheme: integration_against_E_gamma_minus_1}]--> output: `s_phase_space_trace_estimate`
3. input: `⟨s_phase_space_trace_estimate, s_schrodinger_operator_minus_delta_plus_V⟩` --[t_compose_with_identity {bound: sum_E_n^gamma_le_L_gamma_n_int_V_minus^(gamma+n/2)}]--> output: `s_lieb_thirring_inequality`

**Techniques used:** t_compose_with_identity, t_interpolate_and_continue, t_compose_with_identity

---

## 8. Auxiliary classical evolution / parabolic theorems

### Aronson Gaussian bounds for fundamental solution (cite: https://en.wikipedia.org/wiki/Heat_kernel)

**Axioms:** `s_divergence_form_parabolic_with_L_infty_coeff`, `s_fundamental_solution_p(t,x,y)`
**Terminal:** `s_aronson_gaussian_bounds` (kind: theorem)

**Steps:**
1. input: `⟨s_divergence_form_parabolic_with_L_infty_coeff⟩` --[t_compose_with_identity {tool: de_giorgi_nash_moser_regularity}]--> output: `s_holder_regularity_of_fundamental_solution`
2. input: `s_holder_regularity_of_fundamental_solution` --[t_auxiliary_construction {object: nash_entropy_method_or_davies_perturbation}]--> output: `s_two_sided_gaussian_estimate`
3. input: `⟨s_two_sided_gaussian_estimate, s_fundamental_solution_p(t,x,y)⟩` --[t_compose_with_identity {framework: aronson_estimates}]--> output: `s_aronson_gaussian_bounds`

**Techniques used:** t_compose_with_identity, t_auxiliary_construction, t_compose_with_identity

---

### Li–Yau differential Harnack inequality (cite: https://en.wikipedia.org/wiki/Harnack%27s_inequality)

**Axioms:** `s_positive_solution_of_heat_equation_on_riemannian_manifold`, `s_nonneg_ricci_curvature`
**Terminal:** `s_li_yau_differential_harnack` (kind: theorem)

**Steps:**
1. input: `⟨s_positive_solution_of_heat_equation_on_riemannian_manifold⟩` --[t_auxiliary_construction {object: gradient_quantity_F=|∇log_u|^2−alpha·∂t_log_u}]--> output: `s_li_yau_gradient_quantity_F`
2. input: `⟨s_li_yau_gradient_quantity_F, s_nonneg_ricci_curvature⟩` --[t_conserved_quantity {bochner: F_satisfies_max_principle_inequality}]--> output: `s_max_principle_bound_on_F`
3. input: `s_max_principle_bound_on_F` --[t_exhaustion_squeeze {integrate: along_geodesic}]--> output: `s_li_yau_differential_harnack`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_exhaustion_squeeze

---

### Bakry–Émery curvature-dimension criterion (cite: https://en.wikipedia.org/wiki/Bakry%E2%80%93%C3%89mery_curvature)

**Axioms:** `s_diffusion_generator_L_with_carre_du_champ`, `s_curvature_dimension_CD(K,N)_condition`
**Terminal:** `s_bakry_emery_criterion` (kind: theorem)

**Steps:**
1. input: `⟨s_diffusion_generator_L_with_carre_du_champ⟩` --[t_auxiliary_construction {object: iterated_carre_du_champ_Γ_2}]--> output: `s_gamma_2_operator`
2. input: `⟨s_gamma_2_operator, s_curvature_dimension_CD(K,N)_condition⟩` --[t_conserved_quantity {bound: Γ_2_geq_K_Γ_plus_(Lf)^2/N}]--> output: `s_CD_K_N_inequality`
3. input: `s_CD_K_N_inequality` --[t_compose_with_identity {framework: equivalent_to_functional_inequalities_log_sobolev_etc}]--> output: `s_bakry_emery_criterion`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_compose_with_identity

---

### Otto's gradient flow interpretation of heat equation (cite: https://en.wikipedia.org/wiki/Gradient_flow)

**Axioms:** `s_wasserstein_2_metric_on_probability_measures`, `s_relative_entropy_functional_H(mu|rho)`
**Terminal:** `s_otto_gradient_flow_heat` (kind: theorem)

**Steps:**
1. input: `⟨s_wasserstein_2_metric_on_probability_measures, s_relative_entropy_functional_H(mu|rho)⟩` --[t_auxiliary_construction {object: jko_minimizing_movement_scheme}]--> output: `s_jko_time_discretization`
2. input: `s_jko_time_discretization` --[t_exhaustion_squeeze {limit: time_step_to_zero}]--> output: `s_continuous_time_gradient_flow`
3. input: `s_continuous_time_gradient_flow` --[t_structural_isomorphism {identification: gradient_flow_solves_heat_equation_with_drift}]--> output: `s_otto_gradient_flow_heat`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_structural_isomorphism

---

### Crandall–Lions viscosity solutions of Hamilton–Jacobi (cite: https://en.wikipedia.org/wiki/Viscosity_solution)

**Axioms:** `s_hamilton_jacobi_equation_u_t+H(Du,x)=0`, `s_continuous_hamiltonian_H`
**Terminal:** `s_viscosity_solutions_theory` (kind: theorem)

**Steps:**
1. input: `⟨s_hamilton_jacobi_equation_u_t+H(Du,x)=0⟩` --[t_axiomatize_from_instances {definition: viscosity_sub_supersolution_via_smooth_test_functions}]--> output: `s_definition_of_viscosity_sub_super_solution`
2. input: `⟨s_definition_of_viscosity_sub_super_solution, s_continuous_hamiltonian_H⟩` --[t_auxiliary_construction {object: doubling_variables_method}]--> output: `s_doubling_variables_comparison`
3. input: `s_doubling_variables_comparison` --[t_compose_with_identity {framework: comparison_implies_uniqueness}]--> output: `s_viscosity_solutions_theory`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_compose_with_identity

---

### Evans–Krylov C^{2,α} regularity for fully nonlinear PDE (cite: https://en.wikipedia.org/wiki/Fully_nonlinear)

**Axioms:** `s_concave_fully_nonlinear_uniformly_elliptic_pde`, `s_continuous_viscosity_solution`
**Terminal:** `s_evans_krylov_regularity` (kind: theorem)

**Steps:**
1. input: `⟨s_concave_fully_nonlinear_uniformly_elliptic_pde⟩` --[t_auxiliary_construction {object: second_difference_quotients_D_e_e_u}]--> output: `s_second_difference_subsolution_property`
2. input: `s_second_difference_subsolution_property` --[t_compose_with_identity {tool: krylov_safonov_harnack_on_difference_quotients}]--> output: `s_holder_continuity_of_D_2_u`
3. input: `⟨s_holder_continuity_of_D_2_u, s_continuous_viscosity_solution⟩` --[t_compose_with_identity {framework: C^2_alpha_estimate}]--> output: `s_evans_krylov_regularity`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_compose_with_identity

---

### Caffarelli C^{2,α} regularity for Monge–Ampère (cite: https://en.wikipedia.org/wiki/Monge%E2%80%93Amp%C3%A8re_equation)

**Axioms:** `s_strictly_convex_alexandrov_solution`, `s_C_alpha_right_hand_side_f`
**Terminal:** `s_caffarelli_monge_ampere_regularity` (kind: theorem)

**Steps:**
1. input: `⟨s_strictly_convex_alexandrov_solution⟩` --[t_rescale_for_asymptotic_geometry {scaling: john_ellipsoid_normalization}]--> output: `s_normalized_section_of_solution`
2. input: `s_normalized_section_of_solution` --[t_auxiliary_construction {object: pogorelov_estimate_for_pure_second_derivatives}]--> output: `s_C2_alpha_estimate_on_sections`
3. input: `⟨s_C2_alpha_estimate_on_sections, s_C_alpha_right_hand_side_f⟩` --[t_compose_with_identity {framework: classical_solvability}]--> output: `s_caffarelli_monge_ampere_regularity`

**Techniques used:** t_rescale_for_asymptotic_geometry, t_auxiliary_construction, t_compose_with_identity

---

### Allard regularity theorem for varifolds (cite: https://en.wikipedia.org/wiki/Geometric_measure_theory)

**Axioms:** `s_integral_varifold_with_bounded_mean_curvature`, `s_small_density_excess_at_point`
**Terminal:** `s_allard_regularity_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_integral_varifold_with_bounded_mean_curvature, s_small_density_excess_at_point⟩` --[t_rescale_for_asymptotic_geometry {scaling: tangent_cone_at_a_point}]--> output: `s_flat_tangent_cone`
2. input: `s_flat_tangent_cone` --[t_auxiliary_construction {object: lipschitz_graphical_approximation}]--> output: `s_lipschitz_graph_approximation`
3. input: `s_lipschitz_graph_approximation` --[t_interpolate_and_continue {feature: C_1_alpha_regularity_via_harmonic_approximation}]--> output: `s_allard_regularity_theorem`

**Techniques used:** t_rescale_for_asymptotic_geometry, t_auxiliary_construction, t_interpolate_and_continue

---

### Rauch comparison theorem (geometric ODE) (cite: https://en.wikipedia.org/wiki/Rauch_comparison_theorem)

**Axioms:** `s_jacobi_field_along_geodesic`, `s_sectional_curvature_bound`
**Terminal:** `s_rauch_comparison_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_jacobi_field_along_geodesic⟩` --[t_reduce_to_canonical_form {form: jacobi_ode_along_geodesic}]--> output: `s_jacobi_ode_J''+RJ=0`
2. input: `⟨s_jacobi_ode_J''+RJ=0, s_sectional_curvature_bound⟩` --[t_compose_with_identity {tool: sturm_comparison_for_ODE}]--> output: `s_growth_of_jacobi_field_bounded_by_model_space`
3. input: `s_growth_of_jacobi_field_bounded_by_model_space` --[t_compose_with_identity {framework: comparison_of_distances_volumes}]--> output: `s_rauch_comparison_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_compose_with_identity, t_compose_with_identity

---

### Toponogov triangle comparison (cite: https://en.wikipedia.org/wiki/Toponogov%27s_theorem)

**Axioms:** `s_complete_riemannian_manifold_with_lower_sectional_curvature_bound`, `s_geodesic_triangle`
**Terminal:** `s_toponogov_comparison_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_complete_riemannian_manifold_with_lower_sectional_curvature_bound⟩` --[t_compose_with_identity {tool: rauch_comparison_theorem}]--> output: `s_geodesic_length_comparison`
2. input: `⟨s_geodesic_length_comparison, s_geodesic_triangle⟩` --[t_compose_with_identity {framework: model_space_triangle_comparison}]--> output: `s_toponogov_comparison_theorem`

**Techniques used:** t_compose_with_identity, t_compose_with_identity

---

### Cheeger isoperimetric–spectral gap inequality (cite: https://en.wikipedia.org/wiki/Cheeger_constant)

**Axioms:** `s_compact_riemannian_manifold`, `s_cheeger_isoperimetric_constant_h(M)`
**Terminal:** `s_cheeger_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_cheeger_isoperimetric_constant_h(M)⟩` --[t_auxiliary_construction {object: coarea_formula_for_test_functions}]--> output: `s_coarea_inequality`
2. input: `⟨s_coarea_inequality, s_compact_riemannian_manifold⟩` --[t_duality {pair: rayleigh_quotient_and_isoperimetric}]--> output: `s_lambda_1_geq_h_squared_over_4`
3. input: `s_lambda_1_geq_h_squared_over_4` --[t_compose_with_identity {framework: cheeger_inequality}]--> output: `s_cheeger_inequality`

**Techniques used:** t_auxiliary_construction, t_duality, t_compose_with_identity

---

### Bishop–Gromov volume comparison (cite: https://en.wikipedia.org/wiki/Bishop%E2%80%93Gromov_inequality)

**Axioms:** `s_complete_riemannian_manifold`, `s_ricci_curvature_lower_bound`
**Terminal:** `s_bishop_gromov_comparison` (kind: theorem)

**Steps:**
1. input: `⟨s_ricci_curvature_lower_bound⟩` --[t_auxiliary_construction {object: jacobian_of_exponential_map_J(r,theta)}]--> output: `s_volume_density_J`
2. input: `s_volume_density_J` --[t_conserved_quantity {monotone: ratio_J/J_model_decreasing_in_r}]--> output: `s_volume_density_ratio_monotone`
3. input: `⟨s_volume_density_ratio_monotone, s_complete_riemannian_manifold⟩` --[t_exhaustion_squeeze {integrate: in_r}]--> output: `s_bishop_gromov_comparison`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_exhaustion_squeeze

---

### Cheeger–Gromov compactness theorem (cite: https://en.wikipedia.org/wiki/Cheeger%E2%80%93Gromov_convergence)

**Axioms:** `s_sequence_of_riemannian_manifolds_with_curvature_volume_bounds`, `s_pointed_riemannian_manifolds`
**Terminal:** `s_cheeger_gromov_compactness` (kind: theorem)

**Steps:**
1. input: `⟨s_sequence_of_riemannian_manifolds_with_curvature_volume_bounds⟩` --[t_compactness_argument {tool: harmonic_coordinates_with_uniform_radius}]--> output: `s_uniform_harmonic_atlas`
2. input: `⟨s_uniform_harmonic_atlas, s_pointed_riemannian_manifolds⟩` --[t_compactness_argument {tool: arzela_ascoli_in_C_1_alpha}]--> output: `s_subsequential_C_1_alpha_convergence`
3. input: `s_subsequential_C_1_alpha_convergence` --[t_compose_with_identity {framework: cheeger_gromov_topology}]--> output: `s_cheeger_gromov_compactness`

**Techniques used:** t_compactness_argument, t_compactness_argument, t_compose_with_identity

---

### Hamilton's compactness theorem for Ricci flows (cite: https://en.wikipedia.org/wiki/Ricci_flow)

**Axioms:** `s_sequence_of_pointed_ricci_flows_with_uniform_curvature_bound`, `s_injectivity_radius_lower_bound`
**Terminal:** `s_hamilton_ricci_flow_compactness` (kind: theorem)

**Steps:**
1. input: `⟨s_sequence_of_pointed_ricci_flows_with_uniform_curvature_bound⟩` --[t_compose_with_identity {tool: cheeger_gromov_compactness}]--> output: `s_C_infty_subsequential_metric_limit`
2. input: `⟨s_C_infty_subsequential_metric_limit, s_injectivity_radius_lower_bound⟩` --[t_interpolate_and_continue {feature: parabolic_smoothing_for_curvature_derivatives}]--> output: `s_C_infty_smooth_limit_flow`
3. input: `s_C_infty_smooth_limit_flow` --[t_compose_with_identity {framework: limit_is_ricci_flow}]--> output: `s_hamilton_ricci_flow_compactness`

**Techniques used:** t_compose_with_identity, t_interpolate_and_continue, t_compose_with_identity

---

### Perelman entropy monotonicity (W-functional) (cite: https://en.wikipedia.org/wiki/Ricci_flow)

**Axioms:** `s_ricci_flow_equation`, `s_perelman_W_functional`
**Terminal:** `s_perelman_W_monotonicity` (kind: theorem)

**Steps:**
1. input: `⟨s_perelman_W_functional⟩` --[t_auxiliary_construction {object: coupled_evolution_g_phi_tau}]--> output: `s_coupled_flow_with_conjugate_heat`
2. input: `⟨s_coupled_flow_with_conjugate_heat, s_ricci_flow_equation⟩` --[t_conserved_quantity {monotone: dW/dt_geq_0_along_coupled_flow}]--> output: `s_perelman_W_monotonicity`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity

---

### Perelman no-local-collapsing theorem (cite: https://en.wikipedia.org/wiki/Ricci_flow)

**Axioms:** `s_ricci_flow_equation`, `s_perelman_W_monotonicity`
**Terminal:** `s_perelman_no_local_collapsing` (kind: theorem)

**Steps:**
1. input: `⟨s_perelman_W_monotonicity⟩` --[t_auxiliary_construction {object: reduced_volume_or_W_test_at_small_scale}]--> output: `s_W_lower_bound_in_terms_of_initial_data`
2. input: `⟨s_W_lower_bound_in_terms_of_initial_data, s_ricci_flow_equation⟩` --[t_reductio_ad_absurdum {assume: local_collapse_with_bounded_curvature}]--> output: `s_perelman_no_local_collapsing`

**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum

---

### Hamilton tensor maximum principle (cite: https://en.wikipedia.org/wiki/Ricci_flow)

**Axioms:** `s_symmetric_tensor_satisfying_parabolic_inequality`, `s_compact_riemannian_manifold`
**Terminal:** `s_hamilton_tensor_max_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_symmetric_tensor_satisfying_parabolic_inequality⟩` --[t_auxiliary_construction {object: convex_invariant_subset_K_of_symmetric_2_tensors}]--> output: `s_convex_invariant_K`
2. input: `⟨s_convex_invariant_K, s_compact_riemannian_manifold⟩` --[t_conserved_quantity {monotone: tensor_remains_in_K_under_flow}]--> output: `s_hamilton_tensor_max_principle`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity

---

### Brakke mean-curvature flow weak existence (cite: https://en.wikipedia.org/wiki/Mean_curvature_flow)

**Axioms:** `s_initial_integral_varifold`, `s_brakke_inequality_for_varifolds`
**Terminal:** `s_brakke_flow_existence` (kind: theorem)

**Steps:**
1. input: `⟨s_initial_integral_varifold⟩` --[t_auxiliary_construction {object: elliptic_regularization_with_small_epsilon}]--> output: `s_elliptic_regularization_approximation`
2. input: `⟨s_elliptic_regularization_approximation, s_brakke_inequality_for_varifolds⟩` --[t_compactness_argument {tool: varifold_compactness}]--> output: `s_subsequential_varifold_limit`
3. input: `s_subsequential_varifold_limit` --[t_exhaustion_squeeze {limit: pass_to_brakke_inequality}]--> output: `s_brakke_flow_existence`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Sard's theorem (cite: https://en.wikipedia.org/wiki/Sard%27s_theorem)

**Axioms:** `s_smooth_map_between_manifolds`, `s_critical_set_of_smooth_map`
**Terminal:** `s_sard_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_map_between_manifolds, s_critical_set_of_smooth_map⟩` --[t_auxiliary_construction {object: cube_decomposition_via_taylor_expansion}]--> output: `s_taylor_remainder_estimate_on_critical_cubes`
2. input: `s_taylor_remainder_estimate_on_critical_cubes` --[t_exhaustion_squeeze {covering: image_covered_by_small_balls}]--> output: `s_lebesgue_measure_zero_image_of_critical_set`
3. input: `s_lebesgue_measure_zero_image_of_critical_set` --[t_compose_with_identity {framework: sard_theorem}]--> output: `s_sard_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_compose_with_identity

---

### Implicit function theorem (Banach version) (cite: https://en.wikipedia.org/wiki/Implicit_function_theorem)

**Axioms:** `s_C1_map_between_banach_spaces`, `s_invertible_partial_derivative_at_a_point`
**Terminal:** `s_implicit_function_theorem_banach` (kind: theorem)

**Steps:**
1. input: `⟨s_C1_map_between_banach_spaces, s_invertible_partial_derivative_at_a_point⟩` --[t_reduce_to_canonical_form {form: fixed_point_equation_y=y-(D_yF)^-1F(x,y)}]--> output: `s_fixed_point_equation_for_y`
2. input: `s_fixed_point_equation_for_y` --[t_contraction_fixed_point {space: small_ball_around_y_0}]--> output: `s_unique_local_solution_y(x)`
3. input: `s_unique_local_solution_y(x)` --[t_interpolate_and_continue {feature: C^1_dependence_on_x}]--> output: `s_implicit_function_theorem_banach`

**Techniques used:** t_reduce_to_canonical_form, t_contraction_fixed_point, t_interpolate_and_continue

---

### Nash–Moser inverse function theorem (cite: https://en.wikipedia.org/wiki/Nash%E2%80%93Moser_theorem)

**Axioms:** `s_tame_frechet_space_map`, `s_tame_estimate_for_inverse_of_linearization`
**Terminal:** `s_nash_moser_inverse_function_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_tame_frechet_space_map, s_tame_estimate_for_inverse_of_linearization⟩` --[t_auxiliary_construction {object: smoothing_operators_S_t}]--> output: `s_smoothing_operator_family`
2. input: `s_smoothing_operator_family` --[t_contraction_fixed_point {scheme: newton_iteration_with_smoothing}]--> output: `s_quadratically_convergent_iteration`
3. input: `s_quadratically_convergent_iteration` --[t_exhaustion_squeeze {limit: convergence_in_C_infty_topology}]--> output: `s_nash_moser_inverse_function_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Krasovskii–LaSalle invariance principle (cite: https://en.wikipedia.org/wiki/LaSalle%27s_invariance_principle)

**Axioms:** `s_smooth_dynamical_system`, `s_lyapunov_function_V_with_V_dot_le_0`
**Terminal:** `s_lasalle_invariance_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_lyapunov_function_V_with_V_dot_le_0⟩` --[t_conserved_quantity {monotone: V_decreasing_along_trajectories}]--> output: `s_V_monotonically_nonincreasing`
2. input: `⟨s_V_monotonically_nonincreasing, s_smooth_dynamical_system⟩` --[t_compactness_argument {object: omega_limit_set}]--> output: `s_omega_limit_inside_set_V_dot_equal_0`
3. input: `s_omega_limit_inside_set_V_dot_equal_0` --[t_compose_with_identity {framework: largest_invariant_subset_E}]--> output: `s_lasalle_invariance_principle`

**Techniques used:** t_conserved_quantity, t_compactness_argument, t_compose_with_identity

---

### Lyapunov second method (stability theorem) (cite: https://en.wikipedia.org/wiki/Lyapunov_stability)

**Axioms:** `s_smooth_dynamical_system`, `s_lyapunov_function_V_positive_definite_with_V_dot_negative_semidefinite`
**Terminal:** `s_lyapunov_stability_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_lyapunov_function_V_positive_definite_with_V_dot_negative_semidefinite⟩` --[t_conserved_quantity {monotone: V_along_orbits}]--> output: `s_V_bounded_along_orbits`
2. input: `⟨s_V_bounded_along_orbits, s_smooth_dynamical_system⟩` --[t_exhaustion_squeeze {nested: sublevel_sets_invariant}]--> output: `s_invariant_neighborhoods_of_equilibrium`
3. input: `s_invariant_neighborhoods_of_equilibrium` --[t_compose_with_identity {framework: stability_in_sense_of_lyapunov}]--> output: `s_lyapunov_stability_theorem`

**Techniques used:** t_conserved_quantity, t_exhaustion_squeeze, t_compose_with_identity

---

### Massera converse Lyapunov theorem (cite: https://en.wikipedia.org/wiki/Lyapunov_stability)

**Axioms:** `s_uniformly_asymptotically_stable_equilibrium`, `s_smooth_dynamical_system`
**Terminal:** `s_massera_converse_lyapunov` (kind: theorem)

**Steps:**
1. input: `⟨s_uniformly_asymptotically_stable_equilibrium⟩` --[t_auxiliary_construction {object: V(x)=integral_0_infty_||phi(t,x)||^p_dt}]--> output: `s_integral_lyapunov_function_candidate`
2. input: `⟨s_integral_lyapunov_function_candidate, s_smooth_dynamical_system⟩` --[t_compose_with_identity {step: verify_positive_definite_smooth_decreasing_along_flow}]--> output: `s_massera_converse_lyapunov`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Center manifold theorem (cite: https://en.wikipedia.org/wiki/Center_manifold)

**Axioms:** `s_equilibrium_with_center_subspace_E_c`, `s_smooth_vector_field`
**Terminal:** `s_center_manifold_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_equilibrium_with_center_subspace_E_c, s_smooth_vector_field⟩` --[t_symmetry_reduction {splitting: stable_center_unstable}]--> output: `s_decomposition_of_linearization`
2. input: `s_decomposition_of_linearization` --[t_auxiliary_construction {object: graph_transform_over_E_c}]--> output: `s_graph_transform_for_center_manifold`
3. input: `s_graph_transform_for_center_manifold` --[t_contraction_fixed_point {space: Lipschitz_graphs_over_E_c}]--> output: `s_center_manifold_theorem`

**Techniques used:** t_symmetry_reduction, t_auxiliary_construction, t_contraction_fixed_point

---

### Hopf bifurcation theorem (cite: https://en.wikipedia.org/wiki/Hopf_bifurcation)

**Axioms:** `s_one_parameter_family_smooth_vector_fields`, `s_eigenvalue_pair_crossing_imaginary_axis_transversally`
**Terminal:** `s_hopf_bifurcation_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_eigenvalue_pair_crossing_imaginary_axis_transversally⟩` --[t_compose_with_identity {tool: center_manifold_reduction}]--> output: `s_two_dim_center_manifold_dynamics`
2. input: `s_two_dim_center_manifold_dynamics` --[t_reduce_to_canonical_form {form: poincare_normal_form_in_polar}]--> output: `s_hopf_normal_form_r_dot_eq_alpha_r_a_r_3`
3. input: `⟨s_hopf_normal_form_r_dot_eq_alpha_r_a_r_3, s_one_parameter_family_smooth_vector_fields⟩` --[t_verify_on_special_cases {bifurcation: super_or_subcritical}]--> output: `s_hopf_bifurcation_theorem`

**Techniques used:** t_compose_with_identity, t_reduce_to_canonical_form, t_verify_on_special_cases

---

### Smale horseshoe / chaos theorem (cite: https://en.wikipedia.org/wiki/Horseshoe_map)

**Axioms:** `s_transverse_homoclinic_orbit`, `s_smooth_diffeomorphism`
**Terminal:** `s_smale_horseshoe_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_transverse_homoclinic_orbit, s_smooth_diffeomorphism⟩` --[t_auxiliary_construction {object: horseshoe_invariant_set_Λ}]--> output: `s_horseshoe_invariant_set`
2. input: `s_horseshoe_invariant_set` --[t_structural_isomorphism {bijection: lambda_homeomorphic_to_shift_space_2_Z}]--> output: `s_topological_conjugacy_to_bernoulli_shift`
3. input: `s_topological_conjugacy_to_bernoulli_shift` --[t_compose_with_identity {framework: symbolic_dynamics_implies_chaos}]--> output: `s_smale_horseshoe_theorem`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_compose_with_identity

---

### Sharkovskii's theorem (cite: https://en.wikipedia.org/wiki/Sharkovskii%27s_theorem)

**Axioms:** `s_continuous_self_map_of_interval`, `s_sharkovskii_ordering_on_naturals`
**Terminal:** `s_sharkovskii_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_self_map_of_interval⟩` --[t_auxiliary_construction {object: periodic_orbit_combinatorial_pattern}]--> output: `s_periodic_orbit_pattern`
2. input: `⟨s_periodic_orbit_pattern, s_sharkovskii_ordering_on_naturals⟩` --[t_pigeonhole_collision {forcing: interval_covering_relations}]--> output: `s_pattern_forces_lower_periods`
3. input: `s_pattern_forces_lower_periods` --[t_compose_with_identity {framework: sharkovskii_order_periodicity}]--> output: `s_sharkovskii_theorem`

**Techniques used:** t_auxiliary_construction, t_pigeonhole_collision, t_compose_with_identity

---

### Denjoy theorem for circle diffeomorphisms (cite: https://en.wikipedia.org/wiki/Denjoy%27s_theorem_on_the_circle)

**Axioms:** `s_C2_diffeomorphism_of_circle`, `s_irrational_rotation_number`
**Terminal:** `s_denjoy_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_C2_diffeomorphism_of_circle, s_irrational_rotation_number⟩` --[t_auxiliary_construction {object: schwarzian_or_bounded_variation_of_log_derivative}]--> output: `s_bounded_variation_estimate`
2. input: `s_bounded_variation_estimate` --[t_reductio_ad_absurdum {assume: wandering_interval_exists}]--> output: `s_no_wandering_intervals`
3. input: `s_no_wandering_intervals` --[t_structural_isomorphism {conjugacy: to_irrational_rotation}]--> output: `s_denjoy_theorem`

**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum, t_structural_isomorphism

---

### Arnold tongues / mode-locking theorem (cite: https://en.wikipedia.org/wiki/Arnold_tongue)

**Axioms:** `s_one_parameter_family_of_circle_maps`, `s_resonant_rotation_number`
**Terminal:** `s_arnold_tongues_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_one_parameter_family_of_circle_maps⟩` --[t_auxiliary_construction {object: parameter_set_with_given_rational_rotation_number}]--> output: `s_resonance_tongue_in_parameter_space`
2. input: `⟨s_resonance_tongue_in_parameter_space, s_resonant_rotation_number⟩` --[t_verify_on_special_cases {regime: weak_coupling_diophantine_vs_resonant}]--> output: `s_tongue_structure_with_devils_staircase`
3. input: `s_tongue_structure_with_devils_staircase` --[t_compose_with_identity {framework: arnold_tongue_phenomenon}]--> output: `s_arnold_tongues_theorem`

**Techniques used:** t_auxiliary_construction, t_verify_on_special_cases, t_compose_with_identity

---

## End of file
