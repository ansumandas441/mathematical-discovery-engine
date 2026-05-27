# Brief Catalog Skeletons — Area E (Algebra)

Mathematician E, Phase B. 69 theorems across 7 sections. Skeletons only (1 technique per theorem).

## Number Theory (21)

### Fermat's two-square theorem
**Terminal:** `s_fermat_two_square_theorem`
**Axioms:** `s_prime_p_equiv_1_mod_4`, `s_integers`
**Steps:**
1. input: `⟨s_prime_p_equiv_1_mod_4, s_integers⟩` --[t_pigeonhole_collision {lattice: Gaussian}]--> output: `s_fermat_two_square_theorem`

### Lagrange's four-square theorem
**Terminal:** `s_lagrange_four_square_theorem`
**Axioms:** `s_integers`, `s_euler_four_square_identity`
**Steps:**
1. input: `⟨s_integers, s_euler_four_square_identity⟩` --[t_infinite_descent {step: auxiliary_mp_reduce}]--> output: `s_lagrange_four_square_theorem`

### Legendre's three-square theorem
**Terminal:** `s_legendre_three_square_theorem`
**Axioms:** `s_integers`, `s_quadratic_reciprocity`
**Steps:**
1. input: `⟨s_integers, s_quadratic_reciprocity⟩` --[t_reduce_to_canonical_form {form: genus_of_quadratic_form}]--> output: `s_legendre_three_square_theorem`

### Bertrand's postulate
**Terminal:** `s_bertrand_postulate`
**Axioms:** `s_integers`, `s_primes_in_naturals`
**Steps:**
1. input: `⟨s_integers, s_primes_in_naturals⟩` --[t_sieve_by_optimized_quadratic {kernel: binomial_central}]--> output: `s_bertrand_postulate`

### Dirichlet's theorem on primes in arithmetic progressions
**Terminal:** `s_dirichlet_primes_in_ap`
**Axioms:** `s_integers`, `s_primes_in_naturals`
**Steps:**
1. input: `⟨s_integers, s_primes_in_naturals⟩` --[t_character_decomposition_count {characters: Dirichlet}]--> output: `s_dirichlet_primes_in_ap`

### Dirichlet's unit theorem
**Terminal:** `s_dirichlet_unit_theorem`
**Axioms:** `s_integers`, `s_field_extension_L_over_K`
**Steps:**
1. input: `⟨s_integers, s_field_extension_L_over_K⟩` --[t_reduce_to_canonical_form {form: logarithmic_lattice_embedding}]--> output: `s_dirichlet_unit_theorem`

### Minkowski's theorem on convex bodies
**Terminal:** `s_minkowski_convex_body_theorem`
**Axioms:** `s_integers`, `s_real_vector_space`
**Steps:**
1. input: `⟨s_integers, s_real_vector_space⟩` --[t_pigeonhole_collision {covering: translated_half_body}]--> output: `s_minkowski_convex_body_theorem`

### Hilbert–Waring theorem
**Terminal:** `s_hilbert_waring_theorem`
**Axioms:** `s_integers`, `s_naturals_with_multiplication`
**Steps:**
1. input: `⟨s_integers, s_naturals_with_multiplication⟩` --[t_circle_method {decomposition: major_minor_arcs}]--> output: `s_hilbert_waring_theorem`

### Thue's theorem
**Terminal:** `s_thue_theorem`
**Axioms:** `s_integers`, `s_polynomial_ring_over_Q`
**Steps:**
1. input: `⟨s_integers, s_polynomial_ring_over_Q⟩` --[t_pigeonhole_collision {approximation: auxiliary_polynomial}]--> output: `s_thue_theorem`

### Roth's theorem
**Terminal:** `s_roth_approximation_theorem`
**Axioms:** `s_integers`, `s_polynomial_ring_over_Q`
**Steps:**
1. input: `⟨s_integers, s_polynomial_ring_over_Q⟩` --[t_pigeonhole_collision {dim: multidim_auxiliary}]--> output: `s_roth_approximation_theorem`

### Siegel's theorem on integral points
**Terminal:** `s_siegel_integral_points_theorem`
**Axioms:** `s_smooth_projective_curve_over_Q`, `s_integers`
**Steps:**
1. input: `⟨s_smooth_projective_curve_over_Q, s_integers⟩` --[t_heights_and_galois_rep_bridge {input: Thue_bound_on_Jacobian}]--> output: `s_siegel_integral_points_theorem`

### Mordell–Weil theorem
**Terminal:** `s_mordell_weil_theorem`
**Axioms:** `s_elliptic_curve_over_Q`, `s_integers`
**Steps:**
1. input: `⟨s_elliptic_curve_over_Q, s_integers⟩` --[t_infinite_descent {height: canonical}]--> output: `s_mordell_weil_theorem`

### Hasse–Minkowski theorem
**Terminal:** `s_hasse_minkowski_theorem`
**Axioms:** `s_integers`, `s_field_extension_L_over_K`
**Steps:**
1. input: `⟨s_integers, s_field_extension_L_over_K⟩` --[t_transference_bridge {bridge: local_to_global}]--> output: `s_hasse_minkowski_theorem`

### Hasse's theorem on elliptic curves
**Terminal:** `s_hasse_elliptic_bound`
**Axioms:** `s_elliptic_curve_over_Q`, `s_field_extension_L_over_K`
**Steps:**
1. input: `⟨s_elliptic_curve_over_Q, s_field_extension_L_over_K⟩` --[t_complex_analysis_to_integers {tool: Frobenius_eigenvalues}]--> output: `s_hasse_elliptic_bound`

### Weil conjectures (Deligne's theorem)
**Terminal:** `s_weil_conjectures_deligne`
**Axioms:** `s_field_extension_L_over_K`, `s_sheaf_O_D_on_curve`
**Steps:**
1. input: `⟨s_field_extension_L_over_K, s_sheaf_O_D_on_curve⟩` --[t_sheaf_cohomology_bridge {cohomology: etale}]--> output: `s_weil_conjectures_deligne`

### Chebotarev density theorem
**Terminal:** `s_chebotarev_density_theorem`
**Axioms:** `s_galois_group`, `s_field_extension_L_over_K`
**Steps:**
1. input: `⟨s_galois_group, s_field_extension_L_over_K⟩` --[t_character_decomposition_count {L_functions: Artin}]--> output: `s_chebotarev_density_theorem`

### Main theorem of class field theory
**Terminal:** `s_class_field_theory_main`
**Axioms:** `s_galois_group`, `s_field_extension_L_over_K`
**Steps:**
1. input: `⟨s_galois_group, s_field_extension_L_over_K⟩` --[t_structural_isomorphism {map: Artin_reciprocity_map}]--> output: `s_class_field_theory_main`

### Artin reciprocity law
**Terminal:** `s_artin_reciprocity_law`
**Axioms:** `s_galois_group`, `s_field_extension_L_over_K`
**Steps:**
1. input: `⟨s_galois_group, s_field_extension_L_over_K⟩` --[t_character_decomposition_count {map: Artin_symbol}]--> output: `s_artin_reciprocity_law`

### Erdős–Ginzburg–Ziv theorem
**Terminal:** `s_erdos_ginzburg_ziv_theorem`
**Axioms:** `s_integers`, `s_finite_group`
**Steps:**
1. input: `⟨s_integers, s_finite_group⟩` --[t_pigeonhole_collision {target: sum_mod_n_classes}]--> output: `s_erdos_ginzburg_ziv_theorem`

### Chen's theorem
**Terminal:** `s_chen_theorem`
**Axioms:** `s_integers`, `s_primes_in_naturals`
**Steps:**
1. input: `⟨s_integers, s_primes_in_naturals⟩` --[t_selberg_sieve_method {weighted: Chen_weights}]--> output: `s_chen_theorem`

### Vinogradov's theorem
**Terminal:** `s_vinogradov_three_primes_theorem`
**Axioms:** `s_integers`, `s_primes_in_naturals`
**Steps:**
1. input: `⟨s_integers, s_primes_in_naturals⟩` --[t_circle_method {decomposition: major_minor_arcs}]--> output: `s_vinogradov_three_primes_theorem`

## Field Theory & Polynomials (6)

### Eisenstein's criterion
**Terminal:** `s_eisenstein_criterion`
**Axioms:** `s_polynomial_ring`, `s_prime_p`
**Steps:**
1. input: `⟨s_polynomial_ring, s_prime_p⟩` --[t_reduce_to_canonical_form {reduce: mod_p_factorization}]--> output: `s_eisenstein_criterion`

### Gauss's lemma (polynomials)
**Terminal:** `s_gauss_lemma_polynomials`
**Axioms:** `s_polynomial_ring`, `s_integers`
**Steps:**
1. input: `⟨s_polynomial_ring, s_integers⟩` --[t_reduce_to_canonical_form {content: primitive_decomposition}]--> output: `s_gauss_lemma_polynomials`

### Primitive element theorem
**Terminal:** `s_primitive_element_theorem`
**Axioms:** `s_field_extension_L_over_K`, `s_finite_normal_separable_extension_L_over_K`
**Steps:**
1. input: `⟨s_field_extension_L_over_K, s_finite_normal_separable_extension_L_over_K⟩` --[t_structural_isomorphism {witness: generic_linear_combination}]--> output: `s_primitive_element_theorem`

### Artin–Schreier theorem
**Terminal:** `s_artin_schreier_theorem`
**Axioms:** `s_field_extension_L_over_K`, `s_galois_group`
**Steps:**
1. input: `⟨s_field_extension_L_over_K, s_galois_group⟩` --[t_axiomatize_from_instances {instance: real_closure}]--> output: `s_artin_schreier_theorem`

### Hilbert's theorem 90
**Terminal:** `s_hilbert_theorem_90`
**Axioms:** `s_field_extension_L_over_K`, `s_galois_group`
**Steps:**
1. input: `⟨s_field_extension_L_over_K, s_galois_group⟩` --[t_structural_isomorphism {vanish: H1_of_multiplicative_group}]--> output: `s_hilbert_theorem_90`

### Lüroth's theorem
**Terminal:** `s_luroth_theorem`
**Axioms:** `s_polynomial_ring`, `s_field_extension_L_over_K`
**Steps:**
1. input: `⟨s_polynomial_ring, s_field_extension_L_over_K⟩` --[t_reduce_to_canonical_form {form: generator_of_rational_subfield}]--> output: `s_luroth_theorem`

## Commutative Algebra (8)

### Nakayama's lemma
**Terminal:** `s_nakayama_lemma`
**Axioms:** `s_noetherian_ring_R`, `s_ideal_I`
**Steps:**
1. input: `⟨s_noetherian_ring_R, s_ideal_I⟩` --[t_contraction_fixed_point {fixed_point: M=JM}]--> output: `s_nakayama_lemma`

### Krull's principal ideal theorem (Hauptidealsatz)
**Terminal:** `s_krull_hauptidealsatz`
**Axioms:** `s_noetherian_ring_R`, `s_ideal_I`
**Steps:**
1. input: `⟨s_noetherian_ring_R, s_ideal_I⟩` --[t_obstruction_class {obstruction: prime_chain_height}]--> output: `s_krull_hauptidealsatz`

### Krull intersection theorem
**Terminal:** `s_krull_intersection_theorem`
**Axioms:** `s_noetherian_ring_R`, `s_ideal_I`
**Steps:**
1. input: `⟨s_noetherian_ring_R, s_ideal_I⟩` --[t_contraction_fixed_point {apply: Nakayama_on_intersection}]--> output: `s_krull_intersection_theorem`

### Krull–Akizuki theorem
**Terminal:** `s_krull_akizuki_theorem`
**Axioms:** `s_noetherian_ring_R`, `s_field_extension_L_over_K`
**Steps:**
1. input: `⟨s_noetherian_ring_R, s_field_extension_L_over_K⟩` --[t_axiomatize_from_instances {condition: integral_closure_in_finite_extension}]--> output: `s_krull_akizuki_theorem`

### Cohen structure theorem
**Terminal:** `s_cohen_structure_theorem`
**Axioms:** `s_noetherian_ring_R`, `s_polynomial_ring_in_n_vars`
**Steps:**
1. input: `⟨s_noetherian_ring_R, s_polynomial_ring_in_n_vars⟩` --[t_structural_isomorphism {map: quotient_of_power_series_ring}]--> output: `s_cohen_structure_theorem`

### Hilbert's syzygy theorem
**Terminal:** `s_hilbert_syzygy_theorem`
**Axioms:** `s_polynomial_ring_in_n_vars`, `s_ideal_I`
**Steps:**
1. input: `⟨s_polynomial_ring_in_n_vars, s_ideal_I⟩` --[t_obstruction_class {resolution: finite_free}]--> output: `s_hilbert_syzygy_theorem`

### Auslander–Buchsbaum formula
**Terminal:** `s_auslander_buchsbaum_formula`
**Axioms:** `s_noetherian_ring_R`, `s_ideal_I`
**Steps:**
1. input: `⟨s_noetherian_ring_R, s_ideal_I⟩` --[t_conserved_quantity {invariant: pdim_plus_depth}]--> output: `s_auslander_buchsbaum_formula`

### Going-up and going-down theorems
**Terminal:** `s_going_up_going_down_theorem`
**Axioms:** `s_noetherian_ring_R`, `s_ideal_I`
**Steps:**
1. input: `⟨s_noetherian_ring_R, s_ideal_I⟩` --[t_axiomatize_from_instances {condition: integral_extension}]--> output: `s_going_up_going_down_theorem`

## Algebraic Geometry (8)

### Bézout's theorem
**Terminal:** `s_bezout_theorem`
**Axioms:** `s_projective_plane`, `s_polynomial_ring_in_n_vars`
**Steps:**
1. input: `⟨s_projective_plane, s_polynomial_ring_in_n_vars⟩` --[t_raise_dimension {compactify: projective_closure}]--> output: `s_bezout_theorem`

### Chow's theorem
**Terminal:** `s_chow_theorem`
**Axioms:** `s_projective_plane`, `s_holomorphic_function_on_domain`
**Steps:**
1. input: `⟨s_projective_plane, s_holomorphic_function_on_domain⟩` --[t_analysis_algebra_topology_bridge {bridge: GAGA}]--> output: `s_chow_theorem`

### Hironaka's resolution of singularities
**Terminal:** `s_hironaka_resolution`
**Axioms:** `s_vanishing_variety_V_I`, `s_algebraically_closed_field_k`
**Steps:**
1. input: `⟨s_vanishing_variety_V_I, s_algebraically_closed_field_k⟩` --[t_flow_with_surgery {surgery: iterated_blowup}]--> output: `s_hironaka_resolution`

### Serre duality
**Terminal:** `s_serre_duality`
**Axioms:** `s_sheaf_O_D_on_curve`, `s_compact_riemann_surface`
**Steps:**
1. input: `⟨s_sheaf_O_D_on_curve, s_compact_riemann_surface⟩` --[t_duality {pairing: cup_product_to_canonical}]--> output: `s_serre_duality`

### Grothendieck–Riemann–Roch
**Terminal:** `s_grothendieck_riemann_roch`
**Axioms:** `s_sheaf_O_D_on_curve`, `s_euler_characteristic_chi_O_D`
**Steps:**
1. input: `⟨s_sheaf_O_D_on_curve, s_euler_characteristic_chi_O_D⟩` --[t_k_theoretic_index_bridge {transfer: Chern_character_naturality}]--> output: `s_grothendieck_riemann_roch`

### Zariski's main theorem
**Terminal:** `s_zariski_main_theorem`
**Axioms:** `s_vanishing_variety_V_I`, `s_noetherian_ring_R`
**Steps:**
1. input: `⟨s_vanishing_variety_V_I, s_noetherian_ring_R⟩` --[t_structural_isomorphism {map: quasi_finite_into_normal_is_open_immersion}]--> output: `s_zariski_main_theorem`

### Kodaira vanishing theorem
**Terminal:** `s_kodaira_vanishing_theorem`
**Axioms:** `s_sheaf_O_D_on_curve`, `s_compact_riemann_surface`
**Steps:**
1. input: `⟨s_sheaf_O_D_on_curve, s_compact_riemann_surface⟩` --[t_sheaf_cohomology_bridge {vanish: positivity_via_Hodge}]--> output: `s_kodaira_vanishing_theorem`

### Lefschetz hyperplane theorem
**Terminal:** `s_lefschetz_hyperplane_theorem`
**Axioms:** `s_projective_plane`, `s_vanishing_variety_V_I`
**Steps:**
1. input: `⟨s_projective_plane, s_vanishing_variety_V_I⟩` --[t_sheaf_cohomology_bridge {restriction: hyperplane_section}]--> output: `s_lefschetz_hyperplane_theorem`

## Linear and Multilinear Algebra (10)

### Rank–nullity theorem
**Terminal:** `s_rank_nullity_theorem`
**Axioms:** `s_real_vector_space`, `s_linear_functional_on_subspace`
**Steps:**
1. input: `⟨s_real_vector_space, s_linear_functional_on_subspace⟩` --[t_reduce_to_canonical_form {form: basis_extension}]--> output: `s_rank_nullity_theorem`

### Spectral theorem (finite dim)
**Terminal:** `s_spectral_theorem_finite_dim`
**Axioms:** `s_real_vector_space`, `s_complex_numbers`
**Steps:**
1. input: `⟨s_real_vector_space, s_complex_numbers⟩` --[t_svd_and_spectral_decomposition {class: normal_operator}]--> output: `s_spectral_theorem_finite_dim`

### Schur decomposition
**Terminal:** `s_schur_decomposition`
**Axioms:** `s_real_vector_space`, `s_complex_numbers`
**Steps:**
1. input: `⟨s_real_vector_space, s_complex_numbers⟩` --[t_svd_and_spectral_decomposition {form: unitary_upper_triangular}]--> output: `s_schur_decomposition`

### Jordan normal form
**Terminal:** `s_jordan_normal_form`
**Axioms:** `s_real_vector_space`, `s_algebraically_closed_field_k`
**Steps:**
1. input: `⟨s_real_vector_space, s_algebraically_closed_field_k⟩` --[t_reduce_to_canonical_form {form: generalized_eigenspace_block}]--> output: `s_jordan_normal_form`

### Singular value decomposition
**Terminal:** `s_singular_value_decomposition`
**Axioms:** `s_real_vector_space`, `s_complex_numbers`
**Steps:**
1. input: `⟨s_real_vector_space, s_complex_numbers⟩` --[t_svd_and_spectral_decomposition {factor: U_Sigma_Vstar}]--> output: `s_singular_value_decomposition`

### Perron–Frobenius theorem
**Terminal:** `s_perron_frobenius_theorem`
**Axioms:** `s_real_vector_space`, `s_real_numbers`
**Steps:**
1. input: `⟨s_real_vector_space, s_real_numbers⟩` --[t_contraction_fixed_point {cone: positive_orthant}]--> output: `s_perron_frobenius_theorem`

### Gershgorin circle theorem
**Terminal:** `s_gershgorin_circle_theorem`
**Axioms:** `s_real_vector_space`, `s_complex_numbers`
**Steps:**
1. input: `⟨s_real_vector_space, s_complex_numbers⟩` --[t_reduce_to_canonical_form {form: diagonal_dominance_disks}]--> output: `s_gershgorin_circle_theorem`

### Sylvester's law of inertia
**Terminal:** `s_sylvester_law_of_inertia`
**Axioms:** `s_real_vector_space`, `s_real_numbers`
**Steps:**
1. input: `⟨s_real_vector_space, s_real_numbers⟩` --[t_conserved_quantity {invariant: signature_p_n_z}]--> output: `s_sylvester_law_of_inertia`

### Gram–Schmidt process
**Terminal:** `s_gram_schmidt_process`
**Axioms:** `s_real_vector_space`, `s_linear_functional_on_subspace`
**Steps:**
1. input: `⟨s_real_vector_space, s_linear_functional_on_subspace⟩` --[t_projection_to_subspace {orthogonalize: iterative}]--> output: `s_gram_schmidt_process`

### Cramer's rule
**Terminal:** `s_cramer_rule`
**Axioms:** `s_real_vector_space`, `s_polynomial_ring`
**Steps:**
1. input: `⟨s_real_vector_space, s_polynomial_ring⟩` --[t_reduce_to_canonical_form {form: determinantal_ratio}]--> output: `s_cramer_rule`

## Group Theory (10)

### Cauchy's theorem (group theory)
**Terminal:** `s_cauchy_group_theorem`
**Axioms:** `s_finite_group`, `s_prime_p`
**Steps:**
1. input: `⟨s_finite_group, s_prime_p⟩` --[t_symmetry_reduction {action: cyclic_on_p_tuples}]--> output: `s_cauchy_group_theorem`

### Jordan–Hölder theorem
**Terminal:** `s_jordan_holder_theorem`
**Axioms:** `s_finite_group`, `s_finite_simple_group`
**Steps:**
1. input: `⟨s_finite_group, s_finite_simple_group⟩` --[t_conserved_quantity {invariant: multiset_of_composition_factors}]--> output: `s_jordan_holder_theorem`

### Krull–Schmidt theorem
**Terminal:** `s_krull_schmidt_theorem`
**Axioms:** `s_finite_group`, `s_noetherian_ring_R`
**Steps:**
1. input: `⟨s_finite_group, s_noetherian_ring_R⟩` --[t_conserved_quantity {invariant: indecomposable_summand_multiset}]--> output: `s_krull_schmidt_theorem`

### Feit–Thompson theorem
**Terminal:** `s_feit_thompson_theorem`
**Axioms:** `s_finite_group`, `s_finite_simple_group`
**Steps:**
1. input: `⟨s_finite_group, s_finite_simple_group⟩` --[t_character_decomposition_count {tool: character_exceptional_analysis}]--> output: `s_feit_thompson_theorem`

### Schur–Zassenhaus theorem
**Terminal:** `s_schur_zassenhaus_theorem`
**Axioms:** `s_finite_group`, `s_prime_p`
**Steps:**
1. input: `⟨s_finite_group, s_prime_p⟩` --[t_obstruction_class {cohomology: H2_vanishes_coprime_order}]--> output: `s_schur_zassenhaus_theorem`

### Structure theorem for finitely generated abelian groups
**Terminal:** `s_fg_abelian_structure_theorem`
**Axioms:** `s_integers`, `s_finite_group`
**Steps:**
1. input: `⟨s_integers, s_finite_group⟩` --[t_reduce_to_canonical_form {form: Smith_normal_form}]--> output: `s_fg_abelian_structure_theorem`

### Frattini's argument
**Terminal:** `s_frattini_argument`
**Axioms:** `s_finite_group`, `s_set_of_p_subgroups_with_G_action`
**Steps:**
1. input: `⟨s_finite_group, s_set_of_p_subgroups_with_G_action⟩` --[t_symmetry_reduction {action: conjugation_on_Sylow}]--> output: `s_frattini_argument`

### Jordan's theorem on finite linear groups
**Terminal:** `s_jordan_finite_linear_theorem`
**Axioms:** `s_finite_group`, `s_real_vector_space`
**Steps:**
1. input: `⟨s_finite_group, s_real_vector_space⟩` --[t_symmetry_reduction {bound: abelian_normal_of_bounded_index}]--> output: `s_jordan_finite_linear_theorem`

### Burnside's p^a q^b theorem
**Terminal:** `s_burnside_paqb_theorem`
**Axioms:** `s_finite_group`, `s_prime_p`
**Steps:**
1. input: `⟨s_finite_group, s_prime_p⟩` --[t_character_decomposition_count {ring: cyclotomic_integers}]--> output: `s_burnside_paqb_theorem`

### Higman–Neumann–Neumann theorem
**Terminal:** `s_hnn_theorem`
**Axioms:** `s_finite_group`, `s_infinite_set`
**Steps:**
1. input: `⟨s_finite_group, s_infinite_set⟩` --[t_structural_isomorphism {embed: HNN_extension}]--> output: `s_hnn_theorem`

## Representation Theory (6)

### Maschke's theorem
**Terminal:** `s_maschke_theorem`
**Axioms:** `s_finite_group`, `s_field_extension_L_over_K`
**Steps:**
1. input: `⟨s_finite_group, s_field_extension_L_over_K⟩` --[t_symmetry_reduction {averaging: 1_over_G_idempotent}]--> output: `s_maschke_theorem`

### Schur's lemma
**Terminal:** `s_schur_lemma`
**Axioms:** `s_finite_group`, `s_invariant_subspace_decomposition`
**Steps:**
1. input: `⟨s_finite_group, s_invariant_subspace_decomposition⟩` --[t_symmetry_reduction {intertwiner: kernel_and_image_are_invariant}]--> output: `s_schur_lemma`

### Wedderburn's theorem (finite division rings)
**Terminal:** `s_wedderburn_finite_division_ring`
**Axioms:** `s_finite_group`, `s_field_extension_L_over_K`
**Steps:**
1. input: `⟨s_finite_group, s_field_extension_L_over_K⟩` --[t_character_decomposition_count {tool: class_equation_with_cyclotomic}]--> output: `s_wedderburn_finite_division_ring`

### Artin–Wedderburn theorem
**Terminal:** `s_artin_wedderburn_theorem`
**Axioms:** `s_finite_group`, `s_invariant_subspace_decomposition`
**Steps:**
1. input: `⟨s_finite_group, s_invariant_subspace_decomposition⟩` --[t_double_centralizer_decompose {decompose: semisimple_to_matrix_blocks}]--> output: `s_artin_wedderburn_theorem`

### Peter–Weyl theorem
**Terminal:** `s_peter_weyl_theorem`
**Axioms:** `s_L2_function_space`, `s_lie_group`
**Steps:**
1. input: `⟨s_L2_function_space, s_lie_group⟩` --[t_frequency_decomposition {basis: matrix_coefficients_of_irreps}]--> output: `s_peter_weyl_theorem`

### Frobenius reciprocity
**Terminal:** `s_frobenius_reciprocity`
**Axioms:** `s_finite_group`, `s_invariant_subspace_decomposition`
**Steps:**
1. input: `⟨s_finite_group, s_invariant_subspace_decomposition⟩` --[t_duality {adjunction: induction_restriction}]--> output: `s_frobenius_reciprocity`
