# Area Mathematical Physics Derivation Chains (iter-3)

**Source pages:**
- https://en.wikipedia.org/wiki/Category:Theorems_in_mathematical_physics
- https://en.wikipedia.org/wiki/Category:Theorems_in_quantum_mechanics
- https://en.wikipedia.org/wiki/Category:Theorems_in_general_relativity
- https://en.wikipedia.org/wiki/Category:Theorems_in_statistical_mechanics
- https://en.wikipedia.org/wiki/Category:Mathematical_principles_of_physics

**Target:** 60 chains. **Drafted:** 70 (A=10, B=8, C=10, D=10, E=12, F=10, G=10). **Skipped (already in graph):** 4 — `s_noether_theorem` (Noether's theorem), `s_kepler_three_laws` (Kepler's three laws), `s_fourier_theorem_heat` (Fourier heat theorem), `s_birkhoff_ergodic_theorem` (Birkhoff ergodic — distinct from Birkhoff GR).

**Flagged (`⚠ needs new technique`):** 0.

Notes:
- "Discovery chains" — high-level moves and technique tags, not proofs.
- Schoen–Yau positive mass and KAM are listed in user brief as "already at PD" but do not appear in the canonical_node_index.md, so they are drafted here; merge later if duplicates appear.
- `t_physics_to_pde` is heavily reused — it is the canonical bridge from physical postulate to PDE/operator formulation and is justified by the brief's "compound umbrella" guidance.
- Where a chain uses an umbrella technique (`t_atiyah_singer_index_machinery`, `t_fourier_transform`, `t_svd_and_spectral_decomposition`, `t_galois_correspondence`) it is treated atomically per brief style guide.

---

## A. Classical mechanics & integrable systems (10)

### Liouville's theorem on phase-space volume (cite: https://en.wikipedia.org/wiki/Liouville%27s_theorem_(Hamiltonian))

**Axioms:** `s_hamiltonian_phase_space`, `s_hamilton_canonical_equations`
**Terminal:** `s_liouville_phase_volume_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_hamiltonian_phase_space, s_hamilton_canonical_equations⟩` --[t_physics_to_pde {target: continuity_equation_for_phase_density}]--> output: `s_liouville_equation`
2. input: `s_liouville_equation` --[t_symmetry_reduction {symmetry: canonical_flow}]--> output: `s_divergence_free_hamiltonian_flow`
3. input: `s_divergence_free_hamiltonian_flow` --[t_conserved_quantity {quantity: symplectic_volume_form}]--> output: `s_liouville_phase_volume_theorem`

**Techniques used:** t_physics_to_pde, t_symmetry_reduction, t_conserved_quantity

---

### Hamilton–Jacobi theorem (cite: https://en.wikipedia.org/wiki/Hamilton%E2%80%93Jacobi_equation)

**Axioms:** `s_hamiltonian_phase_space`, `s_lagrangian_action_integral`
**Terminal:** `s_hamilton_jacobi_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_lagrangian_action_integral⟩` --[t_physics_to_pde {target: first_order_pde_for_action}]--> output: `s_hamilton_jacobi_pde`
2. input: `⟨s_hamilton_jacobi_pde, s_hamiltonian_phase_space⟩` --[t_duality {pairing: characteristics_vs_pde}]--> output: `s_characteristics_match_hamilton_equations`
3. input: `s_characteristics_match_hamilton_equations` --[t_reduce_to_canonical_form {form: separated_variables}]--> output: `s_complete_integral_generating_canonical_transformation`
4. input: `s_complete_integral_generating_canonical_transformation` --[t_compose_with_identity]--> output: `s_hamilton_jacobi_theorem`

**Techniques used:** t_physics_to_pde, t_duality, t_reduce_to_canonical_form, t_compose_with_identity

---

### Arnold–Liouville theorem (commuting integrals ⇒ integrability) (cite: https://en.wikipedia.org/wiki/Liouville%E2%80%93Arnold_theorem)

**Axioms:** `s_hamiltonian_phase_space`, `s_n_commuting_independent_first_integrals`
**Terminal:** `s_arnold_liouville_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_n_commuting_independent_first_integrals⟩` --[t_symmetry_reduction {symmetry: torus_action_from_Poisson_commuting_flows}]--> output: `s_invariant_lagrangian_submanifold`
2. input: `s_invariant_lagrangian_submanifold` --[t_compactness_argument {target: compact_connected_level_set}]--> output: `s_level_set_is_n_torus`
3. input: `s_level_set_is_n_torus` --[t_reduce_to_canonical_form {form: action_angle_coordinates}]--> output: `s_action_angle_coordinates_exist`
4. input: `s_action_angle_coordinates_exist` --[t_conserved_quantity {quantity: actions_I_k}]--> output: `s_arnold_liouville_theorem`

**Techniques used:** t_symmetry_reduction, t_compactness_argument, t_reduce_to_canonical_form, t_conserved_quantity

---

### KAM (Kolmogorov–Arnold–Moser) theorem (cite: https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Arnold%E2%80%93Moser_theorem)

**Axioms:** `s_hamiltonian_phase_space`, `s_nearly_integrable_hamiltonian_perturbation`, `s_diophantine_frequency_condition`
**Terminal:** `s_kam_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_nearly_integrable_hamiltonian_perturbation⟩` --[t_reduce_to_canonical_form {form: action_angle_plus_small_term}]--> output: `s_perturbed_action_angle_form`
2. input: `⟨s_perturbed_action_angle_form, s_diophantine_frequency_condition⟩` --[t_frequency_decomposition {basis: angle_Fourier_modes}]--> output: `s_small_divisor_estimates_under_diophantine_bound`
3. input: `s_small_divisor_estimates_under_diophantine_bound` --[t_contraction_fixed_point {scheme: newton_kolmogorov_iteration}]--> output: `s_kam_quadratic_convergence`
4. input: `s_kam_quadratic_convergence` --[t_obstruction_class {class: measure_of_persistent_tori}]--> output: `s_kam_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_frequency_decomposition, t_contraction_fixed_point, t_obstruction_class

---

### Bertrand's theorem (only 1/r and r² have closed orbits) (cite: https://en.wikipedia.org/wiki/Bertrand%27s_theorem)

**Axioms:** `s_newtonian_inverse_square_force`, `s_central_force_problem`
**Terminal:** `s_bertrand_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_central_force_problem⟩` --[t_symmetry_reduction {symmetry: SO(3)_rotation_to_radial_problem}]--> output: `s_effective_radial_potential`
2. input: `s_effective_radial_potential` --[t_reduce_to_canonical_form {form: small_oscillation_around_circular_orbit}]--> output: `s_apsidal_angle_perturbation`
3. input: `s_apsidal_angle_perturbation` --[t_verify_on_special_cases {potentials: [-k/r, k_r_squared]}]--> output: `s_only_inverse_square_and_harmonic_close_at_first_order`
4. input: `s_only_inverse_square_and_harmonic_close_at_first_order` --[t_obstruction_class {class: higher_order_apsidal_condition}]--> output: `s_bertrand_theorem`

**Techniques used:** t_symmetry_reduction, t_reduce_to_canonical_form, t_verify_on_special_cases, t_obstruction_class

---

### Poincaré recurrence theorem (cite: https://en.wikipedia.org/wiki/Poincar%C3%A9_recurrence_theorem)

**Axioms:** `s_measure_preserving_transformation`, `s_finite_measure_space`
**Terminal:** `s_poincare_recurrence_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_preserving_transformation, s_finite_measure_space⟩` --[t_pigeonhole_collision {boxes: forward_iterates_of_set}]--> output: `s_some_iterates_must_overlap_in_measure`
2. input: `s_some_iterates_must_overlap_in_measure` --[t_conserved_quantity {quantity: invariant_measure}]--> output: `s_almost_every_point_returns`
3. input: `s_almost_every_point_returns` --[t_compose_with_identity]--> output: `s_poincare_recurrence_theorem`

**Techniques used:** t_pigeonhole_collision, t_conserved_quantity, t_compose_with_identity

---

### Noether's second theorem (gauge identities) (cite: https://en.wikipedia.org/wiki/Noether%27s_second_theorem)

**Axioms:** `s_lagrangian_action_integral`, `s_local_gauge_symmetry_group`
**Terminal:** `s_noether_second_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_lagrangian_action_integral, s_local_gauge_symmetry_group⟩` --[t_symmetry_reduction {symmetry: infinite_dim_local_gauge}]--> output: `s_parameter_dependent_variations`
2. input: `s_parameter_dependent_variations` --[t_duality {pairing: variation_vs_Euler_Lagrange}]--> output: `s_off_shell_identities_among_eom`
3. input: `s_off_shell_identities_among_eom` --[t_obstruction_class {class: differential_relations_constraining_eom}]--> output: `s_noether_second_theorem`

**Techniques used:** t_symmetry_reduction, t_duality, t_obstruction_class

---

### Symplectic non-squeezing (Gromov) (cite: https://en.wikipedia.org/wiki/Non-squeezing_theorem)

**Axioms:** `s_symplectic_manifold`, `s_symplectic_embedding`
**Terminal:** `s_gromov_nonsqueezing_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_symplectic_manifold⟩` --[t_auxiliary_construction {object: J_holomorphic_curves}]--> output: `s_pseudoholomorphic_disks_in_target`
2. input: `s_pseudoholomorphic_disks_in_target` --[t_compactness_argument {target: gromov_compactness_of_moduli}]--> output: `s_existence_of_area_bounded_disk_through_image`
3. input: `s_existence_of_area_bounded_disk_through_image` --[t_obstruction_class {class: symplectic_capacity}]--> output: `s_gromov_nonsqueezing_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_obstruction_class

---

### Marsden–Weinstein symplectic reduction (cite: https://en.wikipedia.org/wiki/Symplectic_reduction)

**Axioms:** `s_symplectic_manifold`, `s_hamiltonian_lie_group_action_with_moment_map`
**Terminal:** `s_marsden_weinstein_reduction_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_hamiltonian_lie_group_action_with_moment_map⟩` --[t_conserved_quantity {quantity: moment_map_level_set}]--> output: `s_moment_map_fiber_mu_inverse_zero`
2. input: `s_moment_map_fiber_mu_inverse_zero` --[t_symmetry_reduction {quotient: by_G_action}]--> output: `s_quotient_manifold_M_red`
3. input: `s_quotient_manifold_M_red` --[t_structural_isomorphism {target: induced_symplectic_form}]--> output: `s_marsden_weinstein_reduction_theorem`

**Techniques used:** t_conserved_quantity, t_symmetry_reduction, t_structural_isomorphism

---

### Darboux theorem (local symplectic uniqueness) (cite: https://en.wikipedia.org/wiki/Darboux%27s_theorem)

**Axioms:** `s_symplectic_manifold`, `s_closed_nondegenerate_2_form`
**Terminal:** `s_darboux_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_closed_nondegenerate_2_form⟩` --[t_auxiliary_construction {object: moser_path_omega_t}]--> output: `s_moser_homotopy_of_symplectic_forms`
2. input: `s_moser_homotopy_of_symplectic_forms` --[t_contraction_fixed_point {scheme: solve_for_time_dependent_vector_field}]--> output: `s_diffeomorphism_pulling_back_to_standard_form`
3. input: `s_diffeomorphism_pulling_back_to_standard_form` --[t_reduce_to_canonical_form {form: sum_dq_i_wedge_dp_i}]--> output: `s_darboux_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_reduce_to_canonical_form

---

## B. Quantum mechanics foundations (8)

### Stone–von Neumann uniqueness theorem (cite: https://en.wikipedia.org/wiki/Stone%E2%80%93von_Neumann_theorem)

**Axioms:** `s_canonical_commutation_relations_weyl_form`, `s_irreducible_unitary_representation`
**Terminal:** `s_stone_von_neumann_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_canonical_commutation_relations_weyl_form⟩` --[t_axiomatize_from_instances {axioms: weyl_unitary_form_of_CCR}]--> output: `s_weyl_unitary_ccr_algebra`
2. input: `s_weyl_unitary_ccr_algebra` --[t_fourier_transform {target: schrodinger_representation_via_plancherel}]--> output: `s_schrodinger_representation`
3. input: `⟨s_schrodinger_representation, s_irreducible_unitary_representation⟩` --[t_structural_isomorphism {target: unique_irrep_up_to_unitary_equivalence}]--> output: `s_stone_von_neumann_theorem`

**Techniques used:** t_axiomatize_from_instances, t_fourier_transform, t_structural_isomorphism

---

### Wigner's theorem (symmetries of quantum states) (cite: https://en.wikipedia.org/wiki/Wigner%27s_theorem)

**Axioms:** `s_projective_hilbert_space`, `s_ray_preserving_transition_probability`
**Terminal:** `s_wigner_symmetry_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_ray_preserving_transition_probability⟩` --[t_symmetry_reduction {symmetry: preserves_|<phi|psi>|}]--> output: `s_inner_product_preserved_up_to_phase`
2. input: `s_inner_product_preserved_up_to_phase` --[t_structural_isomorphism {target: lift_to_unitary_or_antiunitary}]--> output: `s_unique_lift_to_U_or_anti_U`
3. input: `s_unique_lift_to_U_or_anti_U` --[t_compose_with_identity]--> output: `s_wigner_symmetry_theorem`

**Techniques used:** t_symmetry_reduction, t_structural_isomorphism, t_compose_with_identity

---

### Gleason's theorem (cite: https://en.wikipedia.org/wiki/Gleason%27s_theorem)

**Axioms:** `s_hilbert_space_dim_geq_3`, `s_frame_function_on_projections`
**Terminal:** `s_gleason_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_frame_function_on_projections⟩` --[t_symmetry_reduction {symmetry: continuity_under_unitary_rotations}]--> output: `s_continuous_frame_function`
2. input: `⟨s_continuous_frame_function, s_hilbert_space_dim_geq_3⟩` --[t_svd_and_spectral_decomposition {target: bilinear_form_on_projections}]--> output: `s_positive_trace_class_operator_rho`
3. input: `s_positive_trace_class_operator_rho` --[t_structural_isomorphism {target: measure_equals_tr_rho_P}]--> output: `s_gleason_theorem`

**Techniques used:** t_symmetry_reduction, t_svd_and_spectral_decomposition, t_structural_isomorphism

---

### Kochen–Specker theorem (cite: https://en.wikipedia.org/wiki/Kochen%E2%80%93Specker_theorem)

**Axioms:** `s_hilbert_space_dim_geq_3`, `s_noncontextual_hidden_variable_hypothesis`
**Terminal:** `s_kochen_specker_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_noncontextual_hidden_variable_hypothesis⟩` --[t_axiomatize_from_instances {axioms: 0_1_assignment_on_orthogonal_triads}]--> output: `s_KS_coloring_requirement`
2. input: `s_KS_coloring_requirement` --[t_finite_case_check {dataset: specific_finite_vector_configurations}]--> output: `s_no_consistent_KS_coloring_for_configuration`
3. input: `s_no_consistent_KS_coloring_for_configuration` --[t_reductio_ad_absurdum]--> output: `s_kochen_specker_theorem`

**Techniques used:** t_axiomatize_from_instances, t_finite_case_check, t_reductio_ad_absurdum

---

### Bell's theorem (cite: https://en.wikipedia.org/wiki/Bell%27s_theorem)

**Axioms:** `s_local_hidden_variable_hypothesis`, `s_quantum_correlations_in_singlet_state`
**Terminal:** `s_bell_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_local_hidden_variable_hypothesis⟩` --[t_axiomatize_from_instances {axioms: locality_plus_realism}]--> output: `s_chsh_inequality_for_correlations`
2. input: `⟨s_chsh_inequality_for_correlations, s_quantum_correlations_in_singlet_state⟩` --[t_verify_on_special_cases {state: spin_singlet_22_5_67_5_angles}]--> output: `s_QM_violates_CHSH_bound`
3. input: `s_QM_violates_CHSH_bound` --[t_reductio_ad_absurdum]--> output: `s_bell_theorem`

**Techniques used:** t_axiomatize_from_instances, t_verify_on_special_cases, t_reductio_ad_absurdum

---

### Heisenberg uncertainty (Robertson–Schrödinger inequality) (cite: https://en.wikipedia.org/wiki/Uncertainty_principle)

**Axioms:** `s_canonical_commutation_relations_weyl_form`, `s_hilbert_space_with_self_adjoint_operators`
**Terminal:** `s_robertson_schrodinger_uncertainty` (kind: theorem)

**Steps:**
1. input: `⟨s_hilbert_space_with_self_adjoint_operators⟩` --[t_auxiliary_construction {object: shifted_operators_A_minus_<A>}]--> output: `s_centered_observables`
2. input: `⟨s_centered_observables, s_canonical_commutation_relations_weyl_form⟩` --[t_duality {pairing: cauchy_schwarz_on_<A psi, B psi>}]--> output: `s_cauchy_schwarz_variance_bound`
3. input: `s_cauchy_schwarz_variance_bound` --[t_reduce_to_canonical_form {form: variance_product_geq_half_commutator}]--> output: `s_robertson_schrodinger_uncertainty`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Ehrenfest theorem (cite: https://en.wikipedia.org/wiki/Ehrenfest_theorem)

**Axioms:** `s_schrodinger_equation`, `s_hilbert_space_with_self_adjoint_operators`
**Terminal:** `s_ehrenfest_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_schrodinger_equation⟩` --[t_physics_to_pde {target: heisenberg_picture_evolution}]--> output: `s_heisenberg_equation_of_motion`
2. input: `s_heisenberg_equation_of_motion` --[t_duality {pairing: classical_Poisson_vs_quantum_commutator}]--> output: `s_d_dt_expectation_equals_i_hbar_commutator`
3. input: `s_d_dt_expectation_equals_i_hbar_commutator` --[t_compose_with_identity]--> output: `s_ehrenfest_theorem`

**Techniques used:** t_physics_to_pde, t_duality, t_compose_with_identity

---

### RAGE theorem (spectral decomposition of dynamics) (cite: https://en.wikipedia.org/wiki/RAGE_theorem)

**Axioms:** `s_self_adjoint_hamiltonian_H`, `s_unitary_schrodinger_flow`
**Terminal:** `s_rage_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_self_adjoint_hamiltonian_H⟩` --[t_svd_and_spectral_decomposition {target: pure_point_plus_continuous_spectrum}]--> output: `s_lebesgue_spectral_decomposition_of_H`
2. input: `⟨s_lebesgue_spectral_decomposition_of_H, s_unitary_schrodinger_flow⟩` --[t_frequency_decomposition {basis: spectral_projectors}]--> output: `s_decay_of_continuous_part_in_compact_set`
3. input: `s_decay_of_continuous_part_in_compact_set` --[t_structural_isomorphism {target: bound_vs_scattering_dichotomy}]--> output: `s_rage_theorem`

**Techniques used:** t_svd_and_spectral_decomposition, t_frequency_decomposition, t_structural_isomorphism

---

## C. Axiomatic / algebraic QFT (10)

### Wightman reconstruction theorem (cite: https://en.wikipedia.org/wiki/Wightman_axioms)

**Axioms:** `s_wightman_axioms`, `s_tempered_distribution_n_point_functions`
**Terminal:** `s_wightman_reconstruction_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_tempered_distribution_n_point_functions⟩` --[t_axiomatize_from_instances {axioms: positivity_poincare_locality_spectrum}]--> output: `s_wightman_functional_satisfies_GNS_positivity`
2. input: `s_wightman_functional_satisfies_GNS_positivity` --[t_auxiliary_construction {object: GNS_Hilbert_space_and_vacuum}]--> output: `s_borchers_algebra_GNS_representation`
3. input: `s_borchers_algebra_GNS_representation` --[t_structural_isomorphism {target: reconstructed_field_operators_on_H}]--> output: `s_wightman_reconstruction_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism

---

### Osterwalder–Schrader reconstruction (cite: https://en.wikipedia.org/wiki/Osterwalder%E2%80%93Schrader_theorem)

**Axioms:** `s_euclidean_schwinger_functions`, `s_OS_axioms_reflection_positivity`
**Terminal:** `s_osterwalder_schrader_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_OS_axioms_reflection_positivity⟩` --[t_axiomatize_from_instances {axioms: euclidean_invariance_symmetry_RP_regularity}]--> output: `s_euclidean_schwinger_data`
2. input: `s_euclidean_schwinger_data` --[t_duality {pairing: reflection_positivity_yields_physical_inner_product}]--> output: `s_physical_hilbert_space_from_RP`
3. input: `s_physical_hilbert_space_from_RP` --[t_interpolate_and_continue {direction: euclidean_to_minkowski_analytic_continuation}]--> output: `s_wightman_functions_recovered`
4. input: `s_wightman_functions_recovered` --[t_structural_isomorphism {target: euclidean_minkowski_equivalence}]--> output: `s_osterwalder_schrader_theorem`

**Techniques used:** t_axiomatize_from_instances, t_duality, t_interpolate_and_continue, t_structural_isomorphism

---

### Reeh–Schlieder theorem (cite: https://en.wikipedia.org/wiki/Reeh%E2%80%93Schlieder_theorem)

**Axioms:** `s_wightman_axioms`, `s_local_algebra_on_open_region_O`
**Terminal:** `s_reeh_schlieder_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_wightman_axioms⟩` --[t_axiomatize_from_instances {axioms: spectrum_condition_positive_energy}]--> output: `s_analyticity_of_vacuum_expectation_in_imaginary_time`
2. input: `s_analyticity_of_vacuum_expectation_in_imaginary_time` --[t_interpolate_and_continue {method: edge_of_the_wedge}]--> output: `s_edge_of_wedge_extension_of_n_point_functions`
3. input: `⟨s_edge_of_wedge_extension_of_n_point_functions, s_local_algebra_on_open_region_O⟩` --[t_structural_isomorphism {target: cyclic_and_separating_vacuum}]--> output: `s_reeh_schlieder_theorem`

**Techniques used:** t_axiomatize_from_instances, t_interpolate_and_continue, t_structural_isomorphism

---

### Bisognano–Wichmann theorem (cite: https://en.wikipedia.org/wiki/Bisognano%E2%80%93Wichmann_theorem)

**Axioms:** `s_wightman_axioms`, `s_wedge_local_algebra_R_W`
**Terminal:** `s_bisognano_wichmann_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_wedge_local_algebra_R_W⟩` --[t_auxiliary_construction {object: tomita_modular_operator_Delta_W}]--> output: `s_modular_operator_for_wedge`
2. input: `⟨s_modular_operator_for_wedge, s_wightman_axioms⟩` --[t_symmetry_reduction {symmetry: lorentz_boost_stabilizing_wedge}]--> output: `s_modular_flow_equals_boost`
3. input: `s_modular_flow_equals_boost` --[t_structural_isomorphism {target: KMS_at_unruh_temperature}]--> output: `s_bisognano_wichmann_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_structural_isomorphism

---

### Spin–statistics theorem (cite: https://en.wikipedia.org/wiki/Spin%E2%80%93statistics_theorem)

**Axioms:** `s_wightman_axioms`, `s_lorentz_covariant_local_field`
**Terminal:** `s_spin_statistics_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_lorentz_covariant_local_field⟩` --[t_symmetry_reduction {symmetry: SL(2,C)_spinor_representation}]--> output: `s_field_carries_half_integer_or_integer_spin`
2. input: `⟨s_field_carries_half_integer_or_integer_spin, s_wightman_axioms⟩` --[t_interpolate_and_continue {method: analytic_continuation_of_two_point_function}]--> output: `s_wightman_two_point_function_at_spacelike_infinity`
3. input: `s_wightman_two_point_function_at_spacelike_infinity` --[t_reductio_ad_absurdum {hypothesis: wrong_statistics}]--> output: `s_spin_statistics_theorem`

**Techniques used:** t_symmetry_reduction, t_interpolate_and_continue, t_reductio_ad_absurdum

---

### CPT theorem (cite: https://en.wikipedia.org/wiki/CPT_symmetry)

**Axioms:** `s_wightman_axioms`, `s_lorentz_invariance_locality_positive_energy`
**Terminal:** `s_cpt_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_lorentz_invariance_locality_positive_energy⟩` --[t_symmetry_reduction {symmetry: complexified_lorentz_group}]--> output: `s_complex_lorentz_invariance_of_wightman_functions`
2. input: `s_complex_lorentz_invariance_of_wightman_functions` --[t_interpolate_and_continue {method: analytic_continuation_into_jost_points}]--> output: `s_jost_point_analyticity`
3. input: `s_jost_point_analyticity` --[t_duality {pairing: PT_to_C_via_wightman_symmetry}]--> output: `s_cpt_theorem`

**Techniques used:** t_symmetry_reduction, t_interpolate_and_continue, t_duality

---

### Coleman–Mandula theorem (cite: https://en.wikipedia.org/wiki/Coleman%E2%80%93Mandula_theorem)

**Axioms:** `s_relativistic_s_matrix_axioms`, `s_internal_symmetry_lie_algebra_G`
**Terminal:** `s_coleman_mandula_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_relativistic_s_matrix_axioms, s_internal_symmetry_lie_algebra_G⟩` --[t_axiomatize_from_instances {axioms: nontrivial_S_matrix_analyticity_finite_particles}]--> output: `s_bosonic_charge_algebra_constraints`
2. input: `s_bosonic_charge_algebra_constraints` --[t_symmetry_reduction {symmetry: poincare_invariance_of_charges}]--> output: `s_charges_commute_with_translation_generators`
3. input: `s_charges_commute_with_translation_generators` --[t_obstruction_class {class: vanishing_of_nontrivial_lorentz_tensor_charges}]--> output: `s_coleman_mandula_theorem`

**Techniques used:** t_axiomatize_from_instances, t_symmetry_reduction, t_obstruction_class

---

### Haag–Łopuszański–Sohnius theorem (cite: https://en.wikipedia.org/wiki/Haag%E2%80%93%C5%81opusza%C5%84ski%E2%80%93Sohnius_theorem)

**Axioms:** `s_relativistic_s_matrix_axioms`, `s_graded_lie_algebra_extension`
**Terminal:** `s_HLS_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graded_lie_algebra_extension⟩` --[t_axiomatize_from_instances {axioms: Z2_grading_with_fermionic_generators}]--> output: `s_super_charge_anticommutator_structure`
2. input: `⟨s_super_charge_anticommutator_structure, s_relativistic_s_matrix_axioms⟩` --[t_symmetry_reduction {symmetry: super_poincare}]--> output: `s_unique_super_poincare_extension`
3. input: `s_unique_super_poincare_extension` --[t_obstruction_class {class: no_further_bosonic_generators}]--> output: `s_HLS_theorem`

**Techniques used:** t_axiomatize_from_instances, t_symmetry_reduction, t_obstruction_class

---

### Haag's theorem (interaction-picture nonexistence) (cite: https://en.wikipedia.org/wiki/Haag%27s_theorem)

**Axioms:** `s_wightman_axioms`, `s_interaction_picture_assumption`
**Terminal:** `s_haag_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_interaction_picture_assumption⟩` --[t_axiomatize_from_instances {axioms: unitary_equivalence_to_free_field_at_fixed_time}]--> output: `s_putative_unitary_intertwiner_V_t`
2. input: `s_putative_unitary_intertwiner_V_t` --[t_structural_isomorphism {target: equality_of_vacuum_states}]--> output: `s_vacua_must_coincide`
3. input: `s_vacua_must_coincide` --[t_reductio_ad_absurdum {observation: non_trivial_interacting_vacuum_differs}]--> output: `s_haag_theorem`

**Techniques used:** t_axiomatize_from_instances, t_structural_isomorphism, t_reductio_ad_absurdum

---

### Glimm–Jaffe construction of φ⁴ in 2 and 3 dimensions (cite: https://en.wikipedia.org/wiki/Constructive_quantum_field_theory)

**Axioms:** `s_phi_4_lagrangian_lattice_regularization`, `s_OS_axioms_reflection_positivity`
**Terminal:** `s_glimm_jaffe_phi4_construction` (kind: theorem)

**Steps:**
1. input: `⟨s_phi_4_lagrangian_lattice_regularization⟩` --[t_physics_to_pde {target: euclidean_field_theory_measure}]--> output: `s_lattice_phi_4_probability_measure`
2. input: `s_lattice_phi_4_probability_measure` --[t_rescale_for_asymptotic_geometry {direction: lattice_spacing_to_zero}]--> output: `s_renormalization_group_flow_to_continuum`
3. input: `s_renormalization_group_flow_to_continuum` --[t_compactness_argument {target: tight_family_of_measures}]--> output: `s_limit_measure_exists_in_d2_d3`
4. input: `s_limit_measure_exists_in_d2_d3` --[t_structural_isomorphism {target: verifies_OS_axioms}]--> output: `s_glimm_jaffe_phi4_construction`

**Techniques used:** t_physics_to_pde, t_rescale_for_asymptotic_geometry, t_compactness_argument, t_structural_isomorphism

---

## D. Statistical mechanics (10)

### Mermin–Wagner theorem (cite: https://en.wikipedia.org/wiki/Mermin%E2%80%93Wagner_theorem)

**Axioms:** `s_lattice_spin_model_continuous_symmetry`, `s_short_range_interaction_in_d_le_2`
**Terminal:** `s_mermin_wagner_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_lattice_spin_model_continuous_symmetry⟩` --[t_symmetry_reduction {symmetry: assume_spontaneous_magnetization}]--> output: `s_putative_order_parameter`
2. input: `⟨s_putative_order_parameter, s_short_range_interaction_in_d_le_2⟩` --[t_frequency_decomposition {basis: spin_wave_modes}]--> output: `s_bogoliubov_inequality_for_correlations`
3. input: `s_bogoliubov_inequality_for_correlations` --[t_obstruction_class {class: IR_divergence_in_d_le_2}]--> output: `s_order_parameter_must_vanish`
4. input: `s_order_parameter_must_vanish` --[t_reductio_ad_absurdum]--> output: `s_mermin_wagner_theorem`

**Techniques used:** t_symmetry_reduction, t_frequency_decomposition, t_obstruction_class, t_reductio_ad_absurdum

---

### Lee–Yang circle theorem (cite: https://en.wikipedia.org/wiki/Lee%E2%80%93Yang_theorem)

**Axioms:** `s_ferromagnetic_ising_partition_function`, `s_polynomial_in_fugacity_z`
**Terminal:** `s_lee_yang_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_ferromagnetic_ising_partition_function⟩` --[t_reduce_to_canonical_form {form: polynomial_in_z}]--> output: `s_partition_function_polynomial_P_z`
2. input: `s_partition_function_polynomial_P_z` --[t_auxiliary_construction {object: induction_on_lattice_size}]--> output: `s_inductive_zero_locus_constraint`
3. input: `s_inductive_zero_locus_constraint` --[t_obstruction_class {class: zeros_lie_on_unit_circle_|z|=1}]--> output: `s_lee_yang_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_obstruction_class

---

### Onsager exact solution of 2D Ising (cite: https://en.wikipedia.org/wiki/Square-lattice_Ising_model)

**Axioms:** `s_2d_ising_lattice_square`, `s_nearest_neighbor_coupling`
**Terminal:** `s_onsager_2d_ising_solution` (kind: theorem)

**Steps:**
1. input: `⟨s_2d_ising_lattice_square⟩` --[t_auxiliary_construction {object: transfer_matrix_V}]--> output: `s_transfer_matrix_formulation`
2. input: `s_transfer_matrix_formulation` --[t_structural_isomorphism {target: clifford_algebra_of_fermion_operators}]--> output: `s_jordan_wigner_fermionization`
3. input: `s_jordan_wigner_fermionization` --[t_svd_and_spectral_decomposition {target: diagonalize_via_bogoliubov}]--> output: `s_eigenvalues_in_closed_form`
4. input: `s_eigenvalues_in_closed_form` --[t_reduce_to_canonical_form {form: elliptic_integral_free_energy}]--> output: `s_onsager_2d_ising_solution`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_svd_and_spectral_decomposition, t_reduce_to_canonical_form

---

### Peierls argument for spontaneous magnetization (cite: https://en.wikipedia.org/wiki/Peierls_argument)

**Axioms:** `s_2d_ising_lattice_square`, `s_low_temperature_regime`
**Terminal:** `s_peierls_phase_transition` (kind: theorem)

**Steps:**
1. input: `⟨s_2d_ising_lattice_square, s_low_temperature_regime⟩` --[t_auxiliary_construction {object: contour_around_minus_droplets}]--> output: `s_peierls_contour_ensemble`
2. input: `s_peierls_contour_ensemble` --[t_sieve_by_optimized_quadratic {weighting: exp_minus_2_beta_L_per_contour}]--> output: `s_summable_contour_weight_bound`
3. input: `s_summable_contour_weight_bound` --[t_obstruction_class {class: positive_magnetization_at_low_T}]--> output: `s_peierls_phase_transition`

**Techniques used:** t_auxiliary_construction, t_sieve_by_optimized_quadratic, t_obstruction_class

---

### Lieb–Robinson bound (cite: https://en.wikipedia.org/wiki/Lieb%E2%80%93Robinson_bounds)

**Axioms:** `s_lattice_local_hamiltonian`, `s_bounded_local_interaction_norm`
**Terminal:** `s_lieb_robinson_bound` (kind: theorem)

**Steps:**
1. input: `⟨s_lattice_local_hamiltonian⟩` --[t_physics_to_pde {target: heisenberg_evolution_of_local_observable}]--> output: `s_heisenberg_evolution_operator`
2. input: `⟨s_heisenberg_evolution_operator, s_bounded_local_interaction_norm⟩` --[t_contraction_fixed_point {scheme: dyson_series_term_by_term_estimate}]--> output: `s_commutator_norm_grows_at_most_exponentially_in_distance_minus_v_t`
3. input: `s_commutator_norm_grows_at_most_exponentially_in_distance_minus_v_t` --[t_obstruction_class {class: emergent_lightcone_speed_v_LR}]--> output: `s_lieb_robinson_bound`

**Techniques used:** t_physics_to_pde, t_contraction_fixed_point, t_obstruction_class

---

### Lieb–Thirring inequalities (cite: https://en.wikipedia.org/wiki/Lieb%E2%80%93Thirring_inequality)

**Axioms:** `s_schrodinger_operator_minus_laplacian_plus_V`, `s_lp_potential_V`
**Terminal:** `s_lieb_thirring_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_schrodinger_operator_minus_laplacian_plus_V⟩` --[t_svd_and_spectral_decomposition {target: negative_eigenvalues_lambda_j}]--> output: `s_sum_over_negative_spectrum`
2. input: `s_sum_over_negative_spectrum` --[t_duality {pairing: birman_schwinger_principle}]--> output: `s_birman_schwinger_kernel_bound`
3. input: `s_birman_schwinger_kernel_bound` --[t_interpolate_and_continue {direction: trace_ideals_interpolation}]--> output: `s_lieb_thirring_inequality`

**Techniques used:** t_svd_and_spectral_decomposition, t_duality, t_interpolate_and_continue

---

### Lieb's stability of matter (cite: https://en.wikipedia.org/wiki/Stability_of_matter)

**Axioms:** `s_many_body_coulomb_hamiltonian`, `s_fermionic_antisymmetry`
**Terminal:** `s_stability_of_matter_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_many_body_coulomb_hamiltonian⟩` --[t_auxiliary_construction {object: thomas_fermi_functional}]--> output: `s_thomas_fermi_lower_bound`
2. input: `⟨s_thomas_fermi_lower_bound, s_fermionic_antisymmetry⟩` --[t_svd_and_spectral_decomposition {target: lieb_thirring_kinetic_bound}]--> output: `s_extensive_kinetic_energy_bound`
3. input: `s_extensive_kinetic_energy_bound` --[t_obstruction_class {class: ground_state_energy_geq_minus_const_N}]--> output: `s_stability_of_matter_theorem`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_obstruction_class

---

### Dobrushin–Lanford–Ruelle (DLR) characterization of Gibbs states (cite: https://en.wikipedia.org/wiki/Dobrushin%E2%80%93Lanford%E2%80%93Ruelle_equations)

**Axioms:** `s_lattice_local_hamiltonian`, `s_specifications_family_of_conditional_distributions`
**Terminal:** `s_dlr_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_specifications_family_of_conditional_distributions⟩` --[t_axiomatize_from_instances {axioms: consistency_under_volume_changes}]--> output: `s_consistent_specification`
2. input: `s_consistent_specification` --[t_compactness_argument {target: tight_set_of_finite_volume_measures}]--> output: `s_set_of_DLR_solutions_nonempty_compact_convex`
3. input: `s_set_of_DLR_solutions_nonempty_compact_convex` --[t_structural_isomorphism {target: pure_phases_equal_extreme_points}]--> output: `s_dlr_theorem`

**Techniques used:** t_axiomatize_from_instances, t_compactness_argument, t_structural_isomorphism

---

### Kramers–Wannier duality (cite: https://en.wikipedia.org/wiki/Kramers%E2%80%93Wannier_duality)

**Axioms:** `s_2d_ising_lattice_square`, `s_low_temperature_high_temperature_expansions`
**Terminal:** `s_kramers_wannier_duality_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_low_temperature_high_temperature_expansions⟩` --[t_duality {pairing: high_T_low_T_graph_expansion_correspondence}]--> output: `s_partition_function_duality_relation`
2. input: `s_partition_function_duality_relation` --[t_reduce_to_canonical_form {form: tanh_beta_dual_equals_exp_minus_2_beta}]--> output: `s_self_dual_temperature_equation`
3. input: `s_self_dual_temperature_equation` --[t_structural_isomorphism {target: critical_temperature_at_fixed_point}]--> output: `s_kramers_wannier_duality_theorem`

**Techniques used:** t_duality, t_reduce_to_canonical_form, t_structural_isomorphism

---

### Gibbs variational principle (cite: https://en.wikipedia.org/wiki/Variational_principle#Statistical_mechanics)

**Axioms:** `s_lattice_local_hamiltonian`, `s_relative_entropy_functional`
**Terminal:** `s_gibbs_variational_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_relative_entropy_functional⟩` --[t_duality {pairing: entropy_minus_beta_energy_legendre}]--> output: `s_free_energy_legendre_dual`
2. input: `s_free_energy_legendre_dual` --[t_conserved_quantity {quantity: pressure_per_site}]--> output: `s_pressure_attains_supremum_at_gibbs_state`
3. input: `s_pressure_attains_supremum_at_gibbs_state` --[t_structural_isomorphism {target: equilibrium_states_equal_DLR_states}]--> output: `s_gibbs_variational_principle`

**Techniques used:** t_duality, t_conserved_quantity, t_structural_isomorphism

---

## E. General relativity (12)

### Birkhoff's theorem (GR) (cite: https://en.wikipedia.org/wiki/Birkhoff%27s_theorem_(relativity))

**Axioms:** `s_einstein_field_equations_vacuum`, `s_spherical_symmetry_ansatz`
**Terminal:** `s_birkhoff_gr_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_spherical_symmetry_ansatz⟩` --[t_symmetry_reduction {symmetry: SO(3)_isometry}]--> output: `s_spherically_symmetric_metric_ansatz`
2. input: `⟨s_spherically_symmetric_metric_ansatz, s_einstein_field_equations_vacuum⟩` --[t_physics_to_pde {target: vacuum_ricci_zero_in_radial_coords}]--> output: `s_radial_einstein_equations`
3. input: `s_radial_einstein_equations` --[t_conserved_quantity {quantity: t_independence_forced}]--> output: `s_staticity_emerges`
4. input: `s_staticity_emerges` --[t_reduce_to_canonical_form {form: schwarzschild_metric}]--> output: `s_birkhoff_gr_theorem`

**Techniques used:** t_symmetry_reduction, t_physics_to_pde, t_conserved_quantity, t_reduce_to_canonical_form

---

### Penrose singularity theorem (cite: https://en.wikipedia.org/wiki/Penrose%E2%80%93Hawking_singularity_theorems)

**Axioms:** `s_einstein_field_equations`, `s_null_energy_condition`, `s_trapped_surface_exists`
**Terminal:** `s_penrose_singularity_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_einstein_field_equations, s_null_energy_condition⟩` --[t_physics_to_pde {target: raychaudhuri_equation_for_null_congruences}]--> output: `s_raychaudhuri_focusing_inequality`
2. input: `⟨s_raychaudhuri_focusing_inequality, s_trapped_surface_exists⟩` --[t_obstruction_class {class: caustics_form_along_null_geodesics}]--> output: `s_null_geodesic_incompleteness_obstruction`
3. input: `s_null_geodesic_incompleteness_obstruction` --[t_compactness_argument {target: cauchy_horizon_topology}]--> output: `s_penrose_singularity_theorem`

**Techniques used:** t_physics_to_pde, t_obstruction_class, t_compactness_argument

---

### Hawking singularity theorem (cite: https://en.wikipedia.org/wiki/Penrose%E2%80%93Hawking_singularity_theorems)

**Axioms:** `s_einstein_field_equations`, `s_strong_energy_condition`, `s_globally_hyperbolic_spacetime`
**Terminal:** `s_hawking_singularity_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_einstein_field_equations, s_strong_energy_condition⟩` --[t_physics_to_pde {target: raychaudhuri_for_timelike_congruences}]--> output: `s_timelike_focusing_inequality`
2. input: `⟨s_timelike_focusing_inequality, s_globally_hyperbolic_spacetime⟩` --[t_obstruction_class {class: conjugate_points_along_geodesics}]--> output: `s_finite_proper_time_to_focal_point`
3. input: `s_finite_proper_time_to_focal_point` --[t_reductio_ad_absurdum {hypothesis: geodesic_completeness}]--> output: `s_hawking_singularity_theorem`

**Techniques used:** t_physics_to_pde, t_obstruction_class, t_reductio_ad_absurdum

---

### Hawking's area theorem (cite: https://en.wikipedia.org/wiki/Black_hole_thermodynamics#Area_theorem)

**Axioms:** `s_einstein_field_equations`, `s_null_energy_condition`, `s_cosmic_censorship`
**Terminal:** `s_hawking_area_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_einstein_field_equations, s_null_energy_condition⟩` --[t_physics_to_pde {target: raychaudhuri_for_event_horizon_generators}]--> output: `s_horizon_generator_focusing`
2. input: `s_horizon_generator_focusing` --[t_obstruction_class {class: no_endpoints_on_future_horizon}]--> output: `s_nonnegative_expansion_on_horizon`
3. input: `s_nonnegative_expansion_on_horizon` --[t_conserved_quantity {quantity: horizon_cross_section_area_nondecreasing}]--> output: `s_hawking_area_theorem`

**Techniques used:** t_physics_to_pde, t_obstruction_class, t_conserved_quantity

---

### Schoen–Yau positive mass theorem (cite: https://en.wikipedia.org/wiki/Positive_energy_theorem)

**Axioms:** `s_asymptotically_flat_initial_data_set`, `s_dominant_energy_condition`
**Terminal:** `s_schoen_yau_positive_mass_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_asymptotically_flat_initial_data_set⟩` --[t_rescale_for_asymptotic_geometry {direction: blowdown_to_minkowski}]--> output: `s_adm_mass_definition`
2. input: `⟨s_adm_mass_definition, s_dominant_energy_condition⟩` --[t_auxiliary_construction {object: jang_equation_and_minimal_surface}]--> output: `s_minimal_surface_reduction`
3. input: `s_minimal_surface_reduction` --[t_obstruction_class {class: scalar_curvature_positivity_forces_no_stable_minimal_surface}]--> output: `s_no_zero_mass_initial_data_unless_minkowski`
4. input: `s_no_zero_mass_initial_data_unless_minkowski` --[t_reductio_ad_absurdum {hypothesis: negative_mass}]--> output: `s_schoen_yau_positive_mass_theorem`

**Techniques used:** t_rescale_for_asymptotic_geometry, t_auxiliary_construction, t_obstruction_class, t_reductio_ad_absurdum

---

### Bekenstein–Hawking entropy formula (cite: https://en.wikipedia.org/wiki/Bekenstein%E2%80%93Hawking_formula)

**Axioms:** `s_black_hole_thermodynamics_axioms`, `s_hawking_area_theorem`
**Terminal:** `s_bekenstein_hawking_entropy` (kind: theorem)

**Steps:**
1. input: `⟨s_hawking_area_theorem⟩` --[t_duality {pairing: area_as_second_law_quantity}]--> output: `s_area_acts_as_entropy_proxy`
2. input: `⟨s_area_acts_as_entropy_proxy, s_black_hole_thermodynamics_axioms⟩` --[t_physics_to_pde {target: hawking_radiation_temperature_T_H}]--> output: `s_hawking_temperature_kappa_over_2pi`
3. input: `s_hawking_temperature_kappa_over_2pi` --[t_reduce_to_canonical_form {form: S_BH_equals_A_over_4_G_hbar}]--> output: `s_bekenstein_hawking_entropy`

**Techniques used:** t_duality, t_physics_to_pde, t_reduce_to_canonical_form

---

### Cosmic no-hair theorem (de Sitter attractor) (cite: https://en.wikipedia.org/wiki/No-hair_theorem)

**Axioms:** `s_einstein_field_equations_with_positive_lambda`, `s_initially_inhomogeneous_data`
**Terminal:** `s_cosmic_no_hair_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_einstein_field_equations_with_positive_lambda⟩` --[t_physics_to_pde {target: friedmann_constraints_with_lambda}]--> output: `s_constraint_equations_with_cosmological_constant`
2. input: `s_constraint_equations_with_cosmological_constant` --[t_contraction_fixed_point {scheme: exponential_expansion_damps_anisotropy}]--> output: `s_anisotropy_decays_like_e_minus_Ht`
3. input: `s_anisotropy_decays_like_e_minus_Ht` --[t_obstruction_class {class: late_time_de_sitter_attractor}]--> output: `s_cosmic_no_hair_theorem`

**Techniques used:** t_physics_to_pde, t_contraction_fixed_point, t_obstruction_class

---

### Geroch's no-go for global spinor structure (cite: https://en.wikipedia.org/wiki/Spin_structure)

**Axioms:** `s_orientable_lorentzian_manifold`, `s_spin_lift_existence_question`
**Terminal:** `s_geroch_spinor_obstruction_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_orientable_lorentzian_manifold⟩` --[t_obstruction_class {class: second_stiefel_whitney_class_w2}]--> output: `s_w2_vanishing_required`
2. input: `s_w2_vanishing_required` --[t_analysis_algebra_topology_bridge {bridge: tangent_bundle_cohomology}]--> output: `s_spin_lift_exists_iff_w2_zero`
3. input: `s_spin_lift_exists_iff_w2_zero` --[t_structural_isomorphism {target: parallelizable_4_manifolds_have_spin}]--> output: `s_geroch_spinor_obstruction_theorem`

**Techniques used:** t_obstruction_class, t_analysis_algebra_topology_bridge, t_structural_isomorphism

---

### Israel uniqueness of Schwarzschild (cite: https://en.wikipedia.org/wiki/No-hair_theorem)

**Axioms:** `s_einstein_field_equations_vacuum`, `s_static_asymptotically_flat_black_hole`
**Terminal:** `s_israel_uniqueness_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_static_asymptotically_flat_black_hole⟩` --[t_symmetry_reduction {symmetry: timelike_killing_vector}]--> output: `s_static_metric_ansatz`
2. input: `⟨s_static_metric_ansatz, s_einstein_field_equations_vacuum⟩` --[t_physics_to_pde {target: elliptic_pde_on_t_const_slice}]--> output: `s_elliptic_system_on_riemannian_slice`
3. input: `s_elliptic_system_on_riemannian_slice` --[t_obstruction_class {class: divergence_identity_yields_sphere_topology}]--> output: `s_israel_uniqueness_theorem`

**Techniques used:** t_symmetry_reduction, t_physics_to_pde, t_obstruction_class

---

### Newman–Janis algorithm (cite: https://en.wikipedia.org/wiki/Newman%E2%80%93Janis_algorithm)

**Axioms:** `s_schwarzschild_metric_in_null_coordinates`, `s_complex_coordinate_shift_recipe`
**Terminal:** `s_newman_janis_algorithm_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_schwarzschild_metric_in_null_coordinates⟩` --[t_interpolate_and_continue {direction: complexify_radial_coordinate}]--> output: `s_complexified_null_tetrad`
2. input: `⟨s_complexified_null_tetrad, s_complex_coordinate_shift_recipe⟩` --[t_compose_with_identity {operation: r_to_r_plus_i_a_cos_theta}]--> output: `s_shifted_metric_in_real_form`
3. input: `s_shifted_metric_in_real_form` --[t_structural_isomorphism {target: kerr_metric_recovered}]--> output: `s_newman_janis_algorithm_theorem`

**Techniques used:** t_interpolate_and_continue, t_compose_with_identity, t_structural_isomorphism

---

### Choquet–Bruhat well-posedness of Einstein vacuum (cite: https://en.wikipedia.org/wiki/Initial_value_formulation_(general_relativity))

**Axioms:** `s_einstein_field_equations_vacuum`, `s_initial_data_satisfying_constraints`
**Terminal:** `s_choquet_bruhat_well_posedness` (kind: theorem)

**Steps:**
1. input: `⟨s_einstein_field_equations_vacuum⟩` --[t_symmetry_reduction {gauge: harmonic_coordinates}]--> output: `s_harmonic_gauge_reduces_to_quasilinear_wave`
2. input: `⟨s_harmonic_gauge_reduces_to_quasilinear_wave, s_initial_data_satisfying_constraints⟩` --[t_physics_to_pde {target: quasilinear_hyperbolic_system}]--> output: `s_hyperbolic_cauchy_problem`
3. input: `s_hyperbolic_cauchy_problem` --[t_contraction_fixed_point {scheme: energy_estimate_iteration}]--> output: `s_local_existence_and_uniqueness`
4. input: `s_local_existence_and_uniqueness` --[t_structural_isomorphism {target: maximal_globally_hyperbolic_development}]--> output: `s_choquet_bruhat_well_posedness`

**Techniques used:** t_symmetry_reduction, t_physics_to_pde, t_contraction_fixed_point, t_structural_isomorphism

---

### Raychaudhuri equation (cite: https://en.wikipedia.org/wiki/Raychaudhuri_equation)

**Axioms:** `s_lorentzian_manifold`, `s_geodesic_congruence`
**Terminal:** `s_raychaudhuri_equation_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_geodesic_congruence⟩` --[t_auxiliary_construction {object: expansion_shear_twist_decomposition}]--> output: `s_kinematic_decomposition_of_congruence`
2. input: `⟨s_kinematic_decomposition_of_congruence, s_lorentzian_manifold⟩` --[t_physics_to_pde {target: ODE_for_expansion_theta}]--> output: `s_dtheta_ds_equation`
3. input: `s_dtheta_ds_equation` --[t_reduce_to_canonical_form {form: dtheta_ds_plus_theta_sq_over_n_plus_shear_sq_minus_twist_sq_plus_Ricci}]--> output: `s_raychaudhuri_equation_theorem`

**Techniques used:** t_auxiliary_construction, t_physics_to_pde, t_reduce_to_canonical_form

---

## F. Gauge theory / topology in physics (10)

### Faddeev–Popov gauge-fixing procedure (cite: https://en.wikipedia.org/wiki/Faddeev%E2%80%93Popov_ghost)

**Axioms:** `s_yang_mills_action`, `s_path_integral_with_gauge_redundancy`
**Terminal:** `s_faddeev_popov_partition_function_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_path_integral_with_gauge_redundancy⟩` --[t_symmetry_reduction {gauge: choose_gauge_slice}]--> output: `s_gauge_slice_with_jacobian`
2. input: `s_gauge_slice_with_jacobian` --[t_auxiliary_construction {object: grassmann_ghost_fields}]--> output: `s_grassmann_representation_of_FP_determinant`
3. input: `s_grassmann_representation_of_FP_determinant` --[t_reduce_to_canonical_form {form: extended_local_BRST_action}]--> output: `s_faddeev_popov_partition_function_theorem`

**Techniques used:** t_symmetry_reduction, t_auxiliary_construction, t_reduce_to_canonical_form

---

### BPS bound and BPS saturation (cite: https://en.wikipedia.org/wiki/BPS_state)

**Axioms:** `s_supersymmetry_algebra_with_central_charge`, `s_massive_state_in_rep_of_algebra`
**Terminal:** `s_bps_bound_and_saturation_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_supersymmetry_algebra_with_central_charge⟩` --[t_duality {pairing: anticommutator_positivity_on_states}]--> output: `s_positivity_of_Q_dagger_Q`
2. input: `s_positivity_of_Q_dagger_Q` --[t_reduce_to_canonical_form {form: M_geq_|Z|}]--> output: `s_bps_mass_inequality`
3. input: `s_bps_mass_inequality` --[t_obstruction_class {class: shortened_multiplet_when_saturated}]--> output: `s_bps_bound_and_saturation_theorem`

**Techniques used:** t_duality, t_reduce_to_canonical_form, t_obstruction_class

---

### Witten index (cite: https://en.wikipedia.org/wiki/Witten_index)

**Axioms:** `s_supersymmetric_quantum_mechanics`, `s_supercharge_Q_with_Q_squared_equals_H`
**Terminal:** `s_witten_index_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_supercharge_Q_with_Q_squared_equals_H⟩` --[t_auxiliary_construction {object: graded_trace_tr_minus1_F_e_minus_beta_H}]--> output: `s_graded_trace_definition`
2. input: `s_graded_trace_definition` --[t_obstruction_class {class: nonzero_modes_pair_up_and_cancel}]--> output: `s_only_zero_modes_contribute`
3. input: `s_only_zero_modes_contribute` --[t_structural_isomorphism {target: beta_independent_topological_invariant}]--> output: `s_witten_index_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_structural_isomorphism

---

### Wess–Zumino consistency / descent equations (cite: https://en.wikipedia.org/wiki/Wess%E2%80%93Zumino_consistency_condition)

**Axioms:** `s_gauge_symmetry_with_anomaly_functional`, `s_brst_cohomology`
**Terminal:** `s_wess_zumino_descent_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_gauge_symmetry_with_anomaly_functional⟩` --[t_axiomatize_from_instances {axioms: WZ_consistency_on_double_gauge_variation}]--> output: `s_anomaly_satisfies_cocycle_condition`
2. input: `⟨s_anomaly_satisfies_cocycle_condition, s_brst_cohomology⟩` --[t_deformation_cohomology {target: H_1_BRST_local_functionals}]--> output: `s_anomaly_class_in_local_BRST_cohomology`
3. input: `s_anomaly_class_in_local_BRST_cohomology` --[t_analysis_algebra_topology_bridge {bridge: chern_simons_descent}]--> output: `s_wess_zumino_descent_theorem`

**Techniques used:** t_axiomatize_from_instances, t_deformation_cohomology, t_analysis_algebra_topology_bridge

---

### Atiyah–Bott Lefschetz fixed point (equivariant) (cite: https://en.wikipedia.org/wiki/Atiyah%E2%80%93Bott_fixed-point_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_elliptic_operator_D_on_manifold`, `s_smooth_self_map_with_isolated_fixed_points`
**Terminal:** `s_atiyah_bott_fixed_point_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_self_map_with_isolated_fixed_points⟩` --[t_atiyah_singer_index_machinery {input: equivariant_index_class}]--> output: `s_equivariant_index_localized_to_fixed_points`
2. input: `s_equivariant_index_localized_to_fixed_points` --[t_k_theoretic_index_bridge {bridge: K_G_localization}]--> output: `s_localization_to_sum_over_fixed_points`
3. input: `s_localization_to_sum_over_fixed_points` --[t_reduce_to_canonical_form {form: weighted_sum_over_fixed_points_supertrace_over_det_1_minus_df}]--> output: `s_atiyah_bott_fixed_point_theorem`

**Techniques used:** t_atiyah_singer_index_machinery, t_k_theoretic_index_bridge, t_reduce_to_canonical_form

---

### Atiyah–Singer applied to anomalies (Stora–Zumino) (cite: https://en.wikipedia.org/wiki/Anomaly_(physics))

**Axioms:** `s_chiral_dirac_operator`, `s_gauge_bundle_with_connection`
**Terminal:** `s_chiral_anomaly_from_index_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_chiral_dirac_operator⟩` --[t_atiyah_singer_index_machinery {bundle: spin_times_E}]--> output: `s_index_of_chiral_dirac_equals_A_roof_ch_E`
2. input: `s_index_of_chiral_dirac_equals_A_roof_ch_E` --[t_duality {pairing: index_equals_anomaly_coefficient}]--> output: `s_perturbative_anomaly_coefficient`
3. input: `s_perturbative_anomaly_coefficient` --[t_structural_isomorphism {target: ABJ_anomaly_equation}]--> output: `s_chiral_anomaly_from_index_theorem`

**Techniques used:** t_atiyah_singer_index_machinery, t_duality, t_structural_isomorphism

---

### Donaldson's theorem on smooth 4-manifolds (cite: https://en.wikipedia.org/wiki/Donaldson%27s_theorem)

**Axioms:** `s_smooth_simply_connected_4_manifold`, `s_definite_intersection_form`
**Terminal:** `s_donaldson_intersection_form_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_simply_connected_4_manifold⟩` --[t_auxiliary_construction {object: SU(2)_anti_self_dual_connections_moduli}]--> output: `s_ASD_moduli_space`
2. input: `s_ASD_moduli_space` --[t_atiyah_singer_index_machinery {operator: ASD_deformation_complex}]--> output: `s_dimension_of_moduli_via_index`
3. input: `s_dimension_of_moduli_via_index` --[t_obstruction_class {class: singularities_force_intersection_form_diagonalizable}]--> output: `s_donaldson_intersection_form_theorem`

**Techniques used:** t_auxiliary_construction, t_atiyah_singer_index_machinery, t_obstruction_class

---

### Seiberg–Witten invariants existence (cite: https://en.wikipedia.org/wiki/Seiberg%E2%80%93Witten_invariants)

**Axioms:** `s_smooth_4_manifold_with_spin_c_structure`, `s_seiberg_witten_equations`
**Terminal:** `s_seiberg_witten_invariants_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_seiberg_witten_equations⟩` --[t_physics_to_pde {target: monopole_PDEs_for_pair_A_phi}]--> output: `s_monopole_moduli_space`
2. input: `s_monopole_moduli_space` --[t_compactness_argument {target: weitzenbock_a_priori_bound}]--> output: `s_compact_smooth_moduli_under_generic_metric`
3. input: `s_compact_smooth_moduli_under_generic_metric` --[t_atiyah_singer_index_machinery {operator: spin_c_dirac_plus_d_plus}]--> output: `s_dimension_of_SW_moduli_via_index`
4. input: `s_dimension_of_SW_moduli_via_index` --[t_obstruction_class {class: signed_count_invariant_of_metric}]--> output: `s_seiberg_witten_invariants_theorem`

**Techniques used:** t_physics_to_pde, t_compactness_argument, t_atiyah_singer_index_machinery, t_obstruction_class

---

### Verlinde formula for SU(N) WZW (cite: https://en.wikipedia.org/wiki/Verlinde_formula)

**Axioms:** `s_WZW_model_at_level_k_for_SU_N`, `s_modular_S_matrix_on_characters`
**Terminal:** `s_verlinde_formula_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_WZW_model_at_level_k_for_SU_N⟩` --[t_character_decomposition_count {basis: integrable_affine_characters_at_level_k}]--> output: `s_fusion_rules_as_tensor_product_decomposition`
2. input: `⟨s_fusion_rules_as_tensor_product_decomposition, s_modular_S_matrix_on_characters⟩` --[t_duality {pairing: modular_S_diagonalizes_fusion}]--> output: `s_S_matrix_diagonalizes_fusion`
3. input: `s_S_matrix_diagonalizes_fusion` --[t_reduce_to_canonical_form {form: N_ij_k_equals_sum_S_S_S_over_S_0}]--> output: `s_verlinde_formula_theorem`

**Techniques used:** t_character_decomposition_count, t_duality, t_reduce_to_canonical_form

---

### Modular invariance of CFT partition function (S, T action) (cite: https://en.wikipedia.org/wiki/Conformal_field_theory#Modular_invariance)

**Axioms:** `s_2d_cft_on_torus`, `s_partition_function_Z_tau`
**Terminal:** `s_cft_modular_invariance_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_2d_cft_on_torus⟩` --[t_symmetry_reduction {symmetry: torus_modulus_tau_under_SL2Z}]--> output: `s_partition_function_depends_only_on_modulus`
2. input: `s_partition_function_depends_only_on_modulus` --[t_character_decomposition_count {basis: virasoro_characters_chi_h}]--> output: `s_Z_as_quadratic_form_in_characters`
3. input: `s_Z_as_quadratic_form_in_characters` --[t_obstruction_class {class: invariance_under_S_and_T_generators}]--> output: `s_cft_modular_invariance_theorem`

**Techniques used:** t_symmetry_reduction, t_character_decomposition_count, t_obstruction_class

---

## G. Integrable systems & exact solvability (10)

### Lax pair representation yields conserved quantities (cite: https://en.wikipedia.org/wiki/Lax_pair)

**Axioms:** `s_evolution_equation_with_lax_pair_L_M`
**Terminal:** `s_lax_pair_conserved_quantities_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_evolution_equation_with_lax_pair_L_M⟩` --[t_reduce_to_canonical_form {form: dL_dt_equals_commutator_M_L}]--> output: `s_isospectral_flow`
2. input: `s_isospectral_flow` --[t_svd_and_spectral_decomposition {target: spectrum_of_L_invariant}]--> output: `s_spectrum_independent_of_time`
3. input: `s_spectrum_independent_of_time` --[t_conserved_quantity {quantity: tr_L_to_the_n}]--> output: `s_lax_pair_conserved_quantities_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_svd_and_spectral_decomposition, t_conserved_quantity

---

### Inverse scattering transform for KdV (cite: https://en.wikipedia.org/wiki/Inverse_scattering_transform)

**Axioms:** `s_kdv_equation`, `s_schrodinger_scattering_operator_with_potential_u`
**Terminal:** `s_kdv_inverse_scattering_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_kdv_equation⟩` --[t_auxiliary_construction {object: lax_pair_with_schrodinger_L}]--> output: `s_lax_pair_for_kdv`
2. input: `⟨s_lax_pair_for_kdv, s_schrodinger_scattering_operator_with_potential_u⟩` --[t_duality {pairing: potential_u_versus_scattering_data}]--> output: `s_scattering_data_evolve_linearly`
3. input: `s_scattering_data_evolve_linearly` --[t_fourier_transform {target: GLM_equation_for_reconstruction}]--> output: `s_gelfand_levitan_marchenko_reconstruction`
4. input: `s_gelfand_levitan_marchenko_reconstruction` --[t_structural_isomorphism {target: nonlinear_kdv_to_linear_scattering}]--> output: `s_kdv_inverse_scattering_theorem`

**Techniques used:** t_auxiliary_construction, t_duality, t_fourier_transform, t_structural_isomorphism

---

### Yang–Baxter equation as integrability condition (cite: https://en.wikipedia.org/wiki/Yang%E2%80%93Baxter_equation)

**Axioms:** `s_two_particle_scattering_matrix_R`, `s_factorized_n_particle_S_matrix`
**Terminal:** `s_yang_baxter_integrability_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_factorized_n_particle_S_matrix⟩` --[t_axiomatize_from_instances {axioms: associativity_of_three_particle_scattering}]--> output: `s_triangle_consistency_condition`
2. input: `s_triangle_consistency_condition` --[t_reduce_to_canonical_form {form: R12_R13_R23_equals_R23_R13_R12}]--> output: `s_yang_baxter_equation`
3. input: `s_yang_baxter_equation` --[t_structural_isomorphism {target: commuting_transfer_matrix_family}]--> output: `s_yang_baxter_integrability_theorem`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form, t_structural_isomorphism

---

### Bethe ansatz solution of the Heisenberg XXX chain (cite: https://en.wikipedia.org/wiki/Bethe_ansatz)

**Axioms:** `s_heisenberg_xxx_spin_chain`, `s_plane_wave_ansatz_with_rapidities`
**Terminal:** `s_bethe_ansatz_xxx_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_heisenberg_xxx_spin_chain⟩` --[t_symmetry_reduction {symmetry: SU(2)_global}]--> output: `s_magnon_sector_decomposition`
2. input: `⟨s_magnon_sector_decomposition, s_plane_wave_ansatz_with_rapidities⟩` --[t_auxiliary_construction {object: coordinate_bethe_wavefunction}]--> output: `s_two_particle_S_matrix_phase`
3. input: `s_two_particle_S_matrix_phase` --[t_reduce_to_canonical_form {form: bethe_equations_for_rapidities}]--> output: `s_bethe_equations`
4. input: `s_bethe_equations` --[t_structural_isomorphism {target: complete_spectrum_via_solutions}]--> output: `s_bethe_ansatz_xxx_theorem`

**Techniques used:** t_symmetry_reduction, t_auxiliary_construction, t_reduce_to_canonical_form, t_structural_isomorphism

---

### Hirota bilinear form ⇒ soliton solutions (cite: https://en.wikipedia.org/wiki/Bilinear_equation)

**Axioms:** `s_integrable_pde_eg_kdv_or_KP`
**Terminal:** `s_hirota_soliton_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_integrable_pde_eg_kdv_or_KP⟩` --[t_reduce_to_canonical_form {form: substitution_u_equals_2_partial_x_sq_log_tau}]--> output: `s_tau_function_substitution`
2. input: `s_tau_function_substitution` --[t_auxiliary_construction {object: hirota_bilinear_D_operators}]--> output: `s_bilinear_pde_in_tau`
3. input: `s_bilinear_pde_in_tau` --[t_verify_on_special_cases {ansatz: exponential_sum_tau_equals_sum_exp_eta_i}]--> output: `s_hirota_soliton_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_verify_on_special_cases

---

### Riemann–Hilbert reformulation of integrable PDE (cite: https://en.wikipedia.org/wiki/Riemann%E2%80%93Hilbert_problem)

**Axioms:** `s_integrable_pde_with_lax_pair`, `s_jump_matrix_on_contour`
**Terminal:** `s_riemann_hilbert_method_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_integrable_pde_with_lax_pair⟩` --[t_duality {pairing: scattering_data_as_jump_data}]--> output: `s_jump_data_on_spectral_curve`
2. input: `⟨s_jump_data_on_spectral_curve, s_jump_matrix_on_contour⟩` --[t_reduce_to_canonical_form {form: matrix_riemann_hilbert_problem}]--> output: `s_matrix_RH_problem`
3. input: `s_matrix_RH_problem` --[t_contraction_fixed_point {scheme: deift_zhou_steepest_descent}]--> output: `s_riemann_hilbert_method_theorem`

**Techniques used:** t_duality, t_reduce_to_canonical_form, t_contraction_fixed_point

---

### Calogero–Moser integrability (cite: https://en.wikipedia.org/wiki/Calogero%E2%80%93Moser_system)

**Axioms:** `s_calogero_moser_hamiltonian_with_1_over_x_sq_pair`
**Terminal:** `s_calogero_moser_integrability_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_calogero_moser_hamiltonian_with_1_over_x_sq_pair⟩` --[t_auxiliary_construction {object: lax_pair_via_dunkl_operators}]--> output: `s_lax_pair_for_calogero_moser`
2. input: `s_lax_pair_for_calogero_moser` --[t_conserved_quantity {quantity: tr_L_to_the_k}]--> output: `s_n_commuting_first_integrals_constructed`
3. input: `s_n_commuting_first_integrals_constructed` --[t_structural_isomorphism {target: arnold_liouville_integrability}]--> output: `s_calogero_moser_integrability_theorem`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_structural_isomorphism

---

### Toda lattice integrability (cite: https://en.wikipedia.org/wiki/Toda_lattice)

**Axioms:** `s_toda_lattice_hamiltonian_exponential_potential`
**Terminal:** `s_toda_lattice_integrability_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_toda_lattice_hamiltonian_exponential_potential⟩` --[t_auxiliary_construction {object: flaschka_variables_a_b}]--> output: `s_flaschka_variable_form`
2. input: `s_flaschka_variable_form` --[t_reduce_to_canonical_form {form: jacobi_matrix_lax_pair}]--> output: `s_jacobi_matrix_isospectral_flow`
3. input: `s_jacobi_matrix_isospectral_flow` --[t_conserved_quantity {quantity: trace_invariants_of_jacobi_matrix}]--> output: `s_toda_lattice_integrability_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_conserved_quantity

---

### Sklyanin separation of variables (cite: https://en.wikipedia.org/wiki/Separation_of_variables_in_integrable_systems)

**Axioms:** `s_quantum_integrable_system_with_transfer_matrix`
**Terminal:** `s_sklyanin_sov_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_quantum_integrable_system_with_transfer_matrix⟩` --[t_duality {pairing: operator_B_zeros_as_coordinates}]--> output: `s_separation_coordinates_from_B_zeros`
2. input: `s_separation_coordinates_from_B_zeros` --[t_reduce_to_canonical_form {form: factorized_baxter_equation}]--> output: `s_baxter_TQ_relation`
3. input: `s_baxter_TQ_relation` --[t_structural_isomorphism {target: separated_wavefunction_product}]--> output: `s_sklyanin_sov_theorem`

**Techniques used:** t_duality, t_reduce_to_canonical_form, t_structural_isomorphism

---

### Painlevé property and isomonodromy (cite: https://en.wikipedia.org/wiki/Painlev%C3%A9_transcendents)

**Axioms:** `s_second_order_ode_with_movable_singularities`
**Terminal:** `s_painleve_classification_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_second_order_ode_with_movable_singularities⟩` --[t_axiomatize_from_instances {axioms: only_movable_poles_allowed}]--> output: `s_painleve_property_definition`
2. input: `s_painleve_property_definition` --[t_finite_case_check {dataset: kovalevskaya_alpha_test_on_candidates}]--> output: `s_50_canonical_ODEs_reduced_to_6_irreducible`
3. input: `s_50_canonical_ODEs_reduced_to_6_irreducible` --[t_structural_isomorphism {target: isomonodromy_deformations_of_linear_systems}]--> output: `s_painleve_classification_theorem`

**Techniques used:** t_axiomatize_from_instances, t_finite_case_check, t_structural_isomorphism

---
