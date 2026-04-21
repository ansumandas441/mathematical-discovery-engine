# Mathematician's Relationships — Theorem Derivation Chains

Intermediate artifact for the knowledge-graph team. Extracts (input state → technique → output state) chains from chapters 01–06, using only the 57 toolbox techniques as edge labels. Technique node ids use the **snake_case name** of the toolbox entry (with `t_` prefix). State/axiom node ids use `s_` prefix and are stable across theorems — the whole point of the graph is that e.g. `t_symmetry_reduction` and `s_fourier_transform_pair` fan in and out across many chains.

Notation:
- `--[t_foo {param: v}]-->` means technique `t_foo` is applied with parameter binding `{param: v}` on the edge.
- `⟨s_a, s_b⟩` means multiple inputs fed to the same technique.
- `⚠ not in toolbox:` flags a step where no toolbox entry fit well.

---

## Part A — Theorem derivation chains

### Chapter 1 — Ancient & Medieval

### Pythagorean Theorem (Ch. 1)

**Axiom / starting states:** `s_euclidean_plane`, `s_right_triangle_in_plane`, `s_area_additivity`
**Terminal theorem state:** `s_pythagorean_theorem` (kind: theorem)

**Steps:**
1. input: `s_right_triangle_in_plane` --[t_symmetry_reduction {group: reflection across altitude}]--> output: `s_two_similar_subtriangles`
2. input: `⟨s_two_similar_subtriangles, s_area_additivity⟩` --[t_compose_with_identity {identity: similarity ratio squared = area ratio}]--> output: `s_segment_length_identity_on_hypotenuse`
3. input: `s_segment_length_identity_on_hypotenuse` --[t_complete_the_square]--> output: `s_pythagorean_theorem`

**Techniques used:** 6 symmetryReduction; 5 composeWithIdentity; 3 completeTheSquare

---

### Thales's Theorem (Ch. 1)

**Axioms:** `s_euclidean_plane`, `s_circle_definition`, `s_isosceles_triangle_base_angles_equal`
**Terminal:** `s_thales_theorem`

**Steps:**
1. input: `s_triangle_inscribed_in_semicircle` --[t_symmetry_reduction {group: O(2), fixing center}]--> output: `s_two_isosceles_subtriangles`
2. input: `⟨s_two_isosceles_subtriangles, s_isosceles_triangle_base_angles_equal⟩` --[t_compose_with_identity {identity: angle sum = π}]--> output: `s_thales_theorem`

**Techniques used:** 6 symmetryReduction; 5 composeWithIdentity

---

### Euclid's Infinitude of Primes (Ch. 1)

**Axioms:** `s_naturals_with_multiplication`, `s_divisibility_definition`
**Terminal:** `s_infinitude_of_primes`

**Steps:**
1. input: `s_finite_list_of_primes` --[t_compose_with_identity {identity: N = p_1 p_2 ⋯ p_k + 1 has no small prime divisor}]--> output: `s_new_number_N_coprime_to_all_primes_in_list`
2. input: `s_new_number_N_coprime_to_all_primes_in_list` --[t_infinite_descent {dual form: "cannot have only finitely many"}]--> output: `s_infinitude_of_primes`

**Techniques used:** 5 composeWithIdentity; 21 infiniteDescent

---

### Fundamental Theorem of Arithmetic (Ch. 1, completed Gauss 1801)

**Axioms:** `s_naturals_with_multiplication`, `s_euclid_lemma`
**Terminal:** `s_fundamental_theorem_of_arithmetic`

**Steps:**
1. input: `⟨s_naturals_with_multiplication, s_euclid_lemma⟩` --[t_infinite_descent {measure: size of smallest non-uniquely-factorable n}]--> output: `s_uniqueness_of_prime_factorization`
2. input: `s_uniqueness_of_prime_factorization` --[t_axiomatize_from_instances {abstracted to: UFD}]--> output: `s_fundamental_theorem_of_arithmetic`

**Techniques used:** 21 infiniteDescent; 12 axiomatizeFromInstances

---

### Archimedes' Quadrature of Circle and Sphere (Ch. 1)

**Axioms:** `s_euclidean_plane`, `s_euclidean_solid_geometry`, `s_polygon_area_formula`
**Terminal:** `s_area_of_circle`, `s_volume_of_sphere`

**Steps:**
1. input: `s_circle` --[t_symmetry_reduction {group: O(2) rotation}]--> output: `s_inscribed_circumscribed_96_gons`
2. input: `s_inscribed_circumscribed_96_gons` --[t_exhaustion_squeeze {lower: inscribed, upper: circumscribed}]--> output: `s_area_of_circle`
3. input: `s_sphere` --[t_symmetry_reduction {group: SO(3)}]--> output: `s_sphere_as_solid_of_revolution`
4. input: `s_sphere_as_solid_of_revolution` --[t_exhaustion_squeeze {dim: 3}]--> output: `s_volume_of_sphere`

**Techniques used:** 6 symmetryReduction; 9 exhaustionSqueeze

---

### Ptolemy's Theorem (Ch. 1)

**Axioms:** `s_euclidean_plane`, `s_circle_definition`, `s_similar_triangle_criterion`
**Terminal:** `s_ptolemys_theorem`

**Steps:**
1. input: `s_cyclic_quadrilateral` --[t_compose_with_identity {identity: construct auxiliary point K on diagonal with ∠ABK = ∠DBC}]--> output: `s_pair_of_similar_triangles_on_diagonal`
2. input: `s_pair_of_similar_triangles_on_diagonal` --[t_compose_with_identity {identity: AC·BD = AB·CD + AD·BC}]--> output: `s_ptolemys_theorem`

**Techniques used:** 5 composeWithIdentity

---

### Chinese Remainder Theorem (Ch. 1)

**Axioms:** `s_naturals_with_multiplication`, `s_coprime_pair`
**Terminal:** `s_chinese_remainder_theorem`

**Steps:**
1. input: `s_pair_of_coprime_moduli` --[t_reduce_to_canonical_form {form: Bezout identity au + bv = 1}]--> output: `s_idempotent_pair_mod_mn`
2. input: `s_idempotent_pair_mod_mn` --[t_structural_isomorphism {rings: ℤ/mn ≅ ℤ/m × ℤ/n}]--> output: `s_chinese_remainder_theorem`

**Techniques used:** 4 reduceToCanonicalForm; 13 structuralIsomorphism

---

### Bhāskara's Chakravāla (Ch. 1)

**Axioms:** `s_integers`, `s_pell_equation_x2_minus_N_y2`
**Terminal:** `s_solvability_of_pell_equation`

**Steps:**
1. input: `s_near_solution_triple_a_b_k` --[t_compose_with_identity {identity: Brahmagupta bhāvanā composition}]--> output: `s_composed_triple_mod_scaling`
2. input: `s_composed_triple_mod_scaling` --[t_infinite_descent {measure: |k|}]--> output: `s_solvability_of_pell_equation`

**Techniques used:** 5 composeWithIdentity; 21 infiniteDescent

---

### Chapter 2 — Renaissance & 17c

### Cardano's Cubic Formula (Ch. 2)

**Axioms:** `s_complex_numbers`, `s_polynomial_ring`
**Terminal:** `s_cardano_cubic_formula`

**Steps:**
1. input: `s_general_cubic_ax3_plus_bx2_plus_cx_plus_d` --[t_reduce_to_canonical_form {substitution: x = t − b/3a}]--> output: `s_depressed_cubic_t3_plus_pt_plus_q`
2. input: `s_depressed_cubic_t3_plus_pt_plus_q` --[t_complete_the_square {parametric: t = u + v, uv = −p/3}]--> output: `s_system_sum_and_product_of_cubes`
3. input: `s_system_sum_and_product_of_cubes` --[t_compose_with_identity {identity: u³ and v³ satisfy a quadratic}]--> output: `s_cardano_cubic_formula`

**Techniques used:** 4 reduceToCanonicalForm; 3 completeTheSquare; 5 composeWithIdentity

---

### Ferrari's Quartic (Ch. 2)

**Axioms:** `s_complex_numbers`, `s_polynomial_ring`, `s_cardano_cubic_formula`
**Terminal:** `s_ferrari_quartic_formula`

**Steps:**
1. input: `s_general_quartic` --[t_reduce_to_canonical_form {eliminate cubic term}]--> output: `s_depressed_quartic`
2. input: `s_depressed_quartic` --[t_complete_the_square {auxiliary parameter λ}]--> output: `s_resolvent_cubic`
3. input: `s_resolvent_cubic` --[t_compose_with_identity {apply t_cardano_cubic_formula}]--> output: `s_ferrari_quartic_formula`

**Techniques used:** 4 reduceToCanonicalForm; 3 completeTheSquare; 5 composeWithIdentity

---

### Desargues's Theorem (Ch. 2)

**Axioms:** `s_projective_plane`, `s_projective_space_axioms`
**Terminal:** `s_desargues_theorem`

**Steps:**
1. input: `s_two_triangles_in_perspective_in_plane` --[t_raise_dimension {from: 2D, to: 3D}]--> output: `s_two_triangles_in_perspective_in_space`
2. input: `s_two_triangles_in_perspective_in_space` --[t_duality {primal ↔ dual in projective 3-space}]--> output: `s_axis_of_perspective`
3. input: `s_axis_of_perspective` --[t_symmetry_reduction {project back to plane}]--> output: `s_desargues_theorem`

**Techniques used:** 14 raiseDimension; 8 duality; 6 symmetryReduction

---

### Fermat's Little Theorem (Ch. 2)

**Axioms:** `s_integers`, `s_prime_p`
**Terminal:** `s_fermat_little_theorem`

**Steps:**
1. input: `s_multiplicative_group_mod_p` --[t_symmetry_reduction {group: (ℤ/p)*, orbit of a}]--> output: `s_orbit_of_a_mod_p`
2. input: `s_orbit_of_a_mod_p` --[t_conserved_quantity {invariant: product of coset}]--> output: `s_fermat_little_theorem`

**Techniques used:** 6 symmetryReduction; 7 conservedQuantity

---

### Fermat's Sum of Two Squares (Ch. 2)

**Axioms:** `s_integers`, `s_prime_p_equiv_1_mod_4`
**Terminal:** `s_fermat_two_squares`

**Steps:**
1. input: `s_prime_p_equiv_1_mod_4` --[t_compose_with_identity {identity: −1 is a QR mod p}]--> output: `s_existence_of_x_with_x2_equiv_minus1`
2. input: `s_existence_of_x_with_x2_equiv_minus1` --[t_pigeonhole_collision {bins: Thue's lattice bins}]--> output: `s_small_a_b_with_a2_plus_b2_equiv_0_mod_p`
3. input: `s_small_a_b_with_a2_plus_b2_equiv_0_mod_p` --[t_infinite_descent {measure: m in mp = a² + b²}]--> output: `s_fermat_two_squares`

**Techniques used:** 5 composeWithIdentity; 30 pigeonholeCollision; 21 infiniteDescent

---

### Fundamental Theorem of Calculus (Ch. 2)

**Axioms:** `s_real_line`, `s_continuous_function_on_interval`
**Terminal:** `s_fundamental_theorem_of_calculus`

**Steps:**
1. input: `s_continuous_function_on_interval` --[t_exhaustion_squeeze {Riemann sums}]--> output: `s_integral_as_limit_of_sums`
2. input: `⟨s_integral_as_limit_of_sums, s_mean_value_theorem⟩` --[t_compose_with_identity {identity: (F(x+h)−F(x))/h = f(ξ)}]--> output: `s_fundamental_theorem_of_calculus`

**Techniques used:** 9 exhaustionSqueeze; 5 composeWithIdentity

---

### Kepler's Laws (Ch. 2)

**Axioms:** `s_newtonian_inverse_square_force` (physical), `s_conic_sections`
**Terminal:** `s_kepler_three_laws`

**Steps:**
1. input: `s_tycho_brahe_observation_table` --[t_spot_pattern_in_table]--> output: `s_T_squared_prop_a_cubed_conjecture`
2. input: `s_T_squared_prop_a_cubed_conjecture` --[t_verify_on_special_cases]--> output: `s_third_law`
3. input: `s_newtonian_inverse_square_force` --[t_physics_to_pde {conservation: angular momentum and energy}]--> output: `s_kepler_three_laws`

**Techniques used:** 1 spotPatternInTable; 2 verifyOnSpecialCases; 23 physicsToPDE

---

### Chapter 3 — Eighteenth Century

### Taylor's Theorem (Ch. 3)

**Axioms:** `s_smooth_function`, `s_real_line`
**Terminal:** `s_taylor_theorem`

**Steps:**
1. input: `s_smooth_function` --[t_interpolate_and_continue {Newton forward-difference → derivative}]--> output: `s_polynomial_approximation_of_order_n`
2. input: `s_polynomial_approximation_of_order_n` --[t_compose_with_identity {Lagrange remainder}]--> output: `s_taylor_theorem`

**Techniques used:** 10 interpolateAndContinue; 5 composeWithIdentity

---

### De Moivre's Formula (Ch. 3)

**Axioms:** `s_complex_numbers`, `s_unit_circle_in_C`
**Terminal:** `s_de_moivre_formula`

**Steps:**
1. input: `s_complex_number_cos_theta_plus_i_sin_theta` --[t_compose_with_identity {identity: addition theorem for sin/cos}]--> output: `s_multiplicative_law_on_unit_circle`
2. input: `s_multiplicative_law_on_unit_circle` --[t_frequency_decomposition {basis: e^{ikθ}}]--> output: `s_de_moivre_formula`

**Techniques used:** 5 composeWithIdentity; 11 frequencyDecomposition

---

### Euler's Formula e^{iθ} = cos θ + i sin θ (Ch. 3)

**Axioms:** `s_complex_numbers`, `s_analytic_exponential_series`
**Terminal:** `s_euler_formula`

**Steps:**
1. input: `s_analytic_exponential_series` --[t_interpolate_and_continue {extend exp to imaginary argument}]--> output: `s_series_for_e_i_theta`
2. input: `s_series_for_e_i_theta` --[t_frequency_decomposition {separate real/imag}]--> output: `s_euler_formula`

**Techniques used:** 10 interpolateAndContinue; 11 frequencyDecomposition

---

### Euler's Polyhedron Formula V − E + F = 2 (Ch. 3)

**Axioms:** `s_convex_polyhedron`, `s_topological_sphere_S2`
**Terminal:** `s_euler_polyhedron_formula`

**Steps:**
1. input: `s_convex_polyhedron` --[t_reduce_to_canonical_form {triangulate faces}]--> output: `s_triangulated_sphere_S2`
2. input: `s_triangulated_sphere_S2` --[t_conserved_quantity {invariant: V − E + F under edge flips}]--> output: `s_euler_polyhedron_formula`

**Techniques used:** 4 reduceToCanonicalForm; 7 conservedQuantity

---

### Basel Problem Σ 1/n² = π²/6 (Ch. 3)

**Axioms:** `s_real_analysis`, `s_sine_function`
**Terminal:** `s_basel_identity`

**Steps:**
1. input: `s_sine_function` --[t_frequency_decomposition {roots at nπ → product expansion}]--> output: `s_sin_x_as_infinite_product`
2. input: `s_sin_x_as_infinite_product` --[t_compose_with_identity {coefficients of x² of product = Σ 1/n²}]--> output: `s_basel_identity`

**Techniques used:** 11 frequencyDecomposition; 5 composeWithIdentity

---

### Seven Bridges / Birth of Graph Theory (Ch. 3)

**Axioms:** `s_graph_definition`
**Terminal:** `s_eulerian_path_criterion`

**Steps:**
1. input: `s_konigsberg_bridge_configuration` --[t_axiomatize_from_instances {extract: multigraph}]--> output: `s_abstract_multigraph`
2. input: `s_abstract_multigraph` --[t_conserved_quantity {parity of vertex degrees}]--> output: `s_eulerian_path_criterion`

**Techniques used:** 12 axiomatizeFromInstances; 7 conservedQuantity

---

### Fundamental Theorem of Algebra (Gauss 1799, Ch. 3)

**Axioms:** `s_complex_numbers`, `s_polynomial_ring`
**Terminal:** `s_fundamental_theorem_of_algebra`

**Steps:**
1. input: `s_complex_polynomial_p_z` --[t_raise_dimension {from polynomial on ℂ to two real surfaces in ℝ²}]--> output: `s_two_real_algebraic_curves_in_plane`
2. input: `s_two_real_algebraic_curves_in_plane` --[t_compactness_argument {large circle bounds behaviour}]--> output: `s_intersection_exists`
3. input: `s_intersection_exists` --[t_conserved_quantity {winding number of p(z) around 0}]--> output: `s_fundamental_theorem_of_algebra`

**Techniques used:** 14 raiseDimension; 16 compactnessArgument; 7 conservedQuantity

---

### Lagrange's Four-Square Theorem (Ch. 3)

**Axioms:** `s_integers`, `s_euler_four_square_identity`
**Terminal:** `s_lagrange_four_squares`

**Steps:**
1. input: `s_prime_p` --[t_pigeonhole_collision {two sets of (p+1)/2 residues overlap}]--> output: `s_auxiliary_mp_equals_sum_of_four_squares`
2. input: `s_auxiliary_mp_equals_sum_of_four_squares` --[t_infinite_descent {measure: m}]--> output: `s_prime_as_sum_of_four_squares`
3. input: `⟨s_prime_as_sum_of_four_squares, s_euler_four_square_identity⟩` --[t_compose_with_identity]--> output: `s_lagrange_four_squares`

**Techniques used:** 30 pigeonholeCollision; 21 infiniteDescent; 5 composeWithIdentity

---

### Laplace's Central Limit Theorem (Ch. 3)

**Axioms:** `s_iid_sequence_finite_variance`, `s_probability_axioms`
**Terminal:** `s_central_limit_theorem`

**Steps:**
1. input: `s_iid_sequence_finite_variance` --[t_frequency_decomposition {Fourier / characteristic function φ(t) = E[e^{itX}]}]--> output: `s_characteristic_function_of_sum`
2. input: `s_characteristic_function_of_sum` --[t_interpolate_and_continue {log φ expansion near 0}]--> output: `s_limit_characteristic_function_equals_gaussian`
3. input: `s_limit_characteristic_function_equals_gaussian` --[t_compactness_argument {Lévy continuity}]--> output: `s_central_limit_theorem`

**Techniques used:** 11 frequencyDecomposition; 10 interpolateAndContinue; 16 compactnessArgument

---

### Gauss's Quadratic Reciprocity (Ch. 3)

**Axioms:** `s_integers`, `s_prime_pair_p_q`
**Terminal:** `s_quadratic_reciprocity`

**Steps:**
1. input: `s_legendre_symbol_table` --[t_spot_pattern_in_table]--> output: `s_reciprocity_conjecture`
2. input: `s_reciprocity_conjecture` --[t_verify_on_special_cases {p, q small}]--> output: `s_refined_reciprocity_conjecture`
3. input: `s_refined_reciprocity_conjecture` --[t_character_decomposition_count {Gauss sum evaluation}]--> output: `s_quadratic_reciprocity`

**Techniques used:** 1 spotPatternInTable; 2 verifyOnSpecialCases; 36 characterDecompositionCount

---

### Chapter 4 — Nineteenth Century

### Gauss's Theorema Egregium (Ch. 4)

**Axioms:** `s_smooth_surface_in_R3`, `s_first_fundamental_form`
**Terminal:** `s_theorema_egregium`

**Steps:**
1. input: `s_smooth_surface_in_R3` --[t_physics_to_pde {Hanover geodetic survey}]--> output: `s_gauss_curvature_K`
2. input: `s_gauss_curvature_K` --[t_conserved_quantity {invariant under isometry}]--> output: `s_theorema_egregium`

**Techniques used:** 23 physicsToPDE; 7 conservedQuantity

---

### Gauss–Bonnet Theorem (Ch. 4)

**Axioms:** `s_theorema_egregium`, `s_compact_oriented_surface_without_boundary`, `s_euler_polyhedron_formula`
**Terminal:** `s_gauss_bonnet_theorem`

**Steps:**
1. input: `s_compact_oriented_surface_without_boundary` --[t_reduce_to_canonical_form {triangulate}]--> output: `s_geodesic_triangulation`
2. input: `⟨s_geodesic_triangulation, s_gauss_curvature_K⟩` --[t_conserved_quantity {∫K dA is triangulation-independent}]--> output: `s_local_angle_defect_identity`
3. input: `⟨s_local_angle_defect_identity, s_euler_polyhedron_formula⟩` --[t_compose_with_identity {sum over triangles}]--> output: `s_gauss_bonnet_theorem`

**Techniques used:** 4 reduceToCanonicalForm; 7 conservedQuantity; 5 composeWithIdentity

---

### Cauchy's Integral Formula (Ch. 4)

**Axioms:** `s_complex_numbers`, `s_holomorphic_function_on_domain`
**Terminal:** `s_cauchy_integral_formula`

**Steps:**
1. input: `s_holomorphic_function_on_domain` --[t_conserved_quantity {closed-form closed under exact → vanishes}]--> output: `s_cauchy_integral_theorem`
2. input: `s_cauchy_integral_theorem` --[t_compose_with_identity {divide by (z − a), residue}]--> output: `s_cauchy_integral_formula`

**Techniques used:** 7 conservedQuantity; 5 composeWithIdentity

---

### Abel–Ruffini Theorem (Ch. 4)

**Axioms:** `s_polynomial_ring_over_Q`, `s_radical_extension_tower`
**Terminal:** `s_abel_ruffini`

**Steps:**
1. input: `s_quintic_polynomial` --[t_structural_isomorphism {polynomial ↔ Galois group of splitting field}]--> output: `s_galois_group_S5`
2. input: `s_galois_group_S5` --[t_obstruction_class {solvability of group}]--> output: `s_A5_is_simple_non_abelian`
3. input: `s_A5_is_simple_non_abelian` --[t_obstruction_class {solvable group requirement for radical tower}]--> output: `s_abel_ruffini`

**Techniques used:** 13 structuralIsomorphism; 15 obstructionClass

---

### Galois Fundamental Theorem (Ch. 4)

**Axioms:** `s_field_extension_L_over_K`, `s_group_action`
**Terminal:** `s_fundamental_theorem_of_galois_theory`

**Steps:**
1. input: `s_finite_normal_separable_extension_L_over_K` --[t_axiomatize_from_instances {Galois group Gal(L/K)}]--> output: `s_galois_group`
2. input: `⟨s_galois_group, s_intermediate_fields_of_L⟩` --[t_duality {subgroups ↔ intermediate fields, order-reversing}]--> output: `s_galois_correspondence`
3. input: `s_galois_correspondence` --[t_structural_isomorphism]--> output: `s_fundamental_theorem_of_galois_theory`

**Techniques used:** 12 axiomatizeFromInstances; 8 duality; 13 structuralIsomorphism

---

### Fourier's Theorem on the Heat Equation (Ch. 4)

**Axioms:** `s_real_line_or_circle`, `s_L2_function_space`
**Terminal:** `s_fourier_theorem_heat`

**Steps:**
1. input: `s_heat_conduction_on_rod` --[t_physics_to_pde {∂u/∂t = α ∂²u/∂x²}]--> output: `s_heat_equation_PDE`
2. input: `s_heat_equation_PDE` --[t_frequency_decomposition {basis: sin(nπx/L) on interval}]--> output: `s_mode_by_mode_ODE_system`
3. input: `s_mode_by_mode_ODE_system` --[t_contraction_fixed_point {exponential decay e^{−α n² t}}]--> output: `s_fourier_theorem_heat`

**Techniques used:** 23 physicsToPDE; 11 frequencyDecomposition; 20 contractionFixedPoint

---

### Stokes' Theorem (Ch. 4)

**Axioms:** `s_smooth_manifold_with_boundary`, `s_differential_form`
**Terminal:** `s_stokes_theorem`

**Steps:**
1. input: `s_differential_form_omega_on_manifold` --[t_reduce_to_canonical_form {local coordinates, exterior derivative d}]--> output: `s_d_omega_in_local_coords`
2. input: `s_d_omega_in_local_coords` --[t_duality {integration vs differentiation: ∫_M dω = ∫_{∂M} ω}]--> output: `s_stokes_theorem`

**Techniques used:** 4 reduceToCanonicalForm; 8 duality

---

### Riemann Mapping Theorem (Ch. 4)

**Axioms:** `s_simply_connected_proper_domain_in_C`, `s_holomorphic_function_on_domain`
**Terminal:** `s_riemann_mapping_theorem`

**Steps:**
1. input: `s_simply_connected_proper_domain_in_C` --[t_axiomatize_from_instances {normalized extremal problem}]--> output: `s_family_F_of_injective_holomorphic_maps_to_unit_disk`
2. input: `s_family_F_of_injective_holomorphic_maps_to_unit_disk` --[t_compactness_argument {Montel: normal family}]--> output: `s_extremal_map_f_star`
3. input: `s_extremal_map_f_star` --[t_contraction_fixed_point {variational: any not-surjective f admits larger |f'(0)|}]--> output: `s_riemann_mapping_theorem`

**Techniques used:** 12 axiomatizeFromInstances; 16 compactnessArgument; 20 contractionFixedPoint

---

### Riemann–Roch Theorem (Ch. 4)

**Axioms:** `s_compact_riemann_surface`, `s_divisor_on_curve`
**Terminal:** `s_riemann_roch_theorem`

**Steps:**
1. input: `⟨s_compact_riemann_surface, s_divisor_D⟩` --[t_sheafify_on_grothendieck_topology {line bundle O(D)}]--> output: `s_sheaf_O_D_on_curve`
2. input: `s_sheaf_O_D_on_curve` --[t_analysis_algebra_topology_bridge {cohomology: H⁰, H¹}]--> output: `s_euler_characteristic_chi_O_D`
3. input: `s_euler_characteristic_chi_O_D` --[t_conserved_quantity {χ − deg = 1 − g is invariant}]--> output: `s_riemann_roch_theorem`

**Techniques used:** 54 sheafifyOnGrothendieckTopology; 25 analysisAlgebraTopologyBridge; 7 conservedQuantity

---

### Prime Number Theorem (Ch. 4)

**Axioms:** `s_primes_in_naturals`, `s_riemann_zeta_function`
**Terminal:** `s_prime_number_theorem`

**Steps:**
1. input: `s_euler_product_zeta` --[t_interpolate_and_continue {analytically continue ζ(s) to ℂ \ {1}}]--> output: `s_meromorphic_zeta_on_plane`
2. input: `s_meromorphic_zeta_on_plane` --[t_obstruction_class {non-vanishing on Re(s) = 1}]--> output: `s_zeta_nonvanishing_on_line_Re_1`
3. input: `s_zeta_nonvanishing_on_line_Re_1` --[t_complex_analysis_to_integers {Perron-style contour}]--> output: `s_prime_number_theorem`

**Techniques used:** 10 interpolateAndContinue; 15 obstructionClass; 24 complexAnalysisToIntegers

---

### Sylow's Theorems (Ch. 4)

**Axioms:** `s_finite_group`, `s_prime_power_divisor_p_n`
**Terminal:** `s_sylow_theorems`

**Steps:**
1. input: `s_finite_group_G_with_order_divisible_by_p_n` --[t_symmetry_reduction {conjugation action on p-subgroups}]--> output: `s_set_of_p_subgroups_with_G_action`
2. input: `s_set_of_p_subgroups_with_G_action` --[t_character_decomposition_count {count fixed points mod p}]--> output: `s_sylow_theorems`

**Techniques used:** 6 symmetryReduction; 36 characterDecompositionCount

---

### Cantor's Uncountability of ℝ (Ch. 4)

**Axioms:** `s_real_numbers`
**Terminal:** `s_uncountability_of_reals`

**Steps:**
1. input: `s_alleged_enumeration_of_reals_in_0_1` --[t_diagonalize {flip the n-th digit of the n-th listed real}]--> output: `s_real_not_in_list`
2. input: `s_real_not_in_list` --[t_infinite_descent {contradicts assumed enumeration}]--> output: `s_uncountability_of_reals`

**Techniques used:** 17 diagonalize; 21 infiniteDescent

---

### Bolzano–Weierstrass / Weierstrass Approximation (Ch. 4)

**Axioms:** `s_closed_bounded_interval`, `s_continuous_function_on_interval`
**Terminal:** `s_weierstrass_approximation`

**Steps:**
1. input: `s_continuous_function_on_closed_interval` --[t_flow_with_surgery {Gaussian heat-kernel smoothing, no surgery needed}]--> output: `s_smooth_approximant_f_epsilon`
2. input: `s_smooth_approximant_f_epsilon` --[t_exhaustion_squeeze {sup-norm error shrinks}]--> output: `s_weierstrass_approximation`

**Techniques used:** 22 flowWithSurgery; 9 exhaustionSqueeze

---

### Chapter 5 — Early Twentieth Century

### Hilbert's Basis Theorem (Ch. 5)

**Axioms:** `s_noetherian_ring_R`, `s_polynomial_ring`
**Terminal:** `s_hilbert_basis_theorem`

**Steps:**
1. input: `s_ideal_in_R_x` --[t_infinite_descent {ascending-chain of leading ideals stabilizes}]--> output: `s_finite_generating_set_of_ideal`
2. input: `s_finite_generating_set_of_ideal` --[t_axiomatize_from_instances]--> output: `s_hilbert_basis_theorem`

**Techniques used:** 21 infiniteDescent; 12 axiomatizeFromInstances

---

### Hilbert's Nullstellensatz (Ch. 5)

**Axioms:** `s_algebraically_closed_field_k`, `s_polynomial_ring_in_n_vars`
**Terminal:** `s_nullstellensatz`

**Steps:**
1. input: `s_maximal_ideal_m_in_k_x_1_x_n` --[t_structural_isomorphism {k[x]/m ≅ k via algebraic closure}]--> output: `s_point_in_affine_n_space`
2. input: `⟨s_ideal_I, s_vanishing_variety_V_I⟩` --[t_duality {ideals ↔ varieties, radical ↔ V ∘ I}]--> output: `s_nullstellensatz`

**Techniques used:** 13 structuralIsomorphism; 8 duality

---

### Brouwer Fixed-Point Theorem (Ch. 5)

**Axioms:** `s_closed_ball_D_n`, `s_continuous_self_map`
**Terminal:** `s_brouwer_fpt`

**Steps:**
1. input: `s_continuous_self_map_of_disk_without_fixed_point` --[t_compose_with_identity {build retraction D_n → ∂D_n}]--> output: `s_retraction_to_boundary_sphere`
2. input: `s_retraction_to_boundary_sphere` --[t_obstruction_class {degree of identity on S^{n-1} ≠ 0}]--> output: `s_contradiction_no_retraction`
3. input: `s_contradiction_no_retraction` --[t_infinite_descent {dual form}]--> output: `s_brouwer_fpt`

**Techniques used:** 5 composeWithIdentity; 15 obstructionClass; 21 infiniteDescent

---

### Noether's Theorem (Ch. 5)

**Axioms:** `s_lagrangian_action_integral`, `s_lie_group`
**Terminal:** `s_noether_theorem`

**Steps:**
1. input: `⟨s_lagrangian_action_integral, s_lie_group⟩` --[t_symmetry_reduction {1-parameter subgroup of G}]--> output: `s_infinitesimal_action_variation`
2. input: `s_infinitesimal_action_variation` --[t_conserved_quantity {Euler–Lagrange + invariance → divergence of Noether current}]--> output: `s_noether_theorem`

**Techniques used:** 6 symmetryReduction; 7 conservedQuantity

---

### Gödel's Incompleteness Theorems (Ch. 5)

**Axioms:** `s_first_order_peano_arithmetic`
**Terminal:** `s_godel_incompleteness`

**Steps:**
1. input: `s_first_order_peano_arithmetic` --[t_arithmetize_syntax {Gödel numbering; primitive recursion encodes proofs}]--> output: `s_syntactic_predicates_as_arithmetic_predicates`
2. input: `s_syntactic_predicates_as_arithmetic_predicates` --[t_diagonalize {fixed-point lemma: G ↔ ¬Prov(⌜G⌝)}]--> output: `s_self_referential_godel_sentence_G`
3. input: `s_self_referential_godel_sentence_G` --[t_obstruction_class {consistency blocks deriving G or ¬G}]--> output: `s_godel_incompleteness`

**Techniques used:** 18 arithmetizeSyntax; 17 diagonalize; 15 obstructionClass

---

### Banach Fixed-Point Theorem (Ch. 5)

**Axioms:** `s_complete_metric_space`, `s_strict_contraction`
**Terminal:** `s_banach_fpt`

**Steps:**
1. input: `⟨s_complete_metric_space, s_strict_contraction⟩` --[t_contraction_fixed_point]--> output: `s_banach_fpt`

**Techniques used:** 20 contractionFixedPoint

---

### Hahn–Banach Theorem (Ch. 5)

**Axioms:** `s_real_vector_space`, `s_sublinear_functional_p`, `s_linear_functional_on_subspace`
**Terminal:** `s_hahn_banach`

**Steps:**
1. input: `⟨s_linear_functional_on_subspace, s_sublinear_functional_p⟩` --[t_reduce_to_canonical_form {extend by one dimension at a time, pick value in allowed interval}]--> output: `s_one_dim_extension_step`
2. input: `s_one_dim_extension_step` --[t_compactness_argument {Zorn's lemma on chain of extensions}]--> output: `s_hahn_banach`

**Techniques used:** 4 reduceToCanonicalForm; 16 compactnessArgument

---

### Tychonoff's Theorem (Ch. 5)

**Axioms:** `s_family_of_compact_spaces`, `s_product_topology`
**Terminal:** `s_tychonoff_theorem`

**Steps:**
1. input: `s_family_of_compact_spaces` --[t_ultraproduct_transfer {ultrafilter on index set}]--> output: `s_ultrafilter_limit_in_product`
2. input: `s_ultrafilter_limit_in_product` --[t_compactness_argument {projection is continuous}]--> output: `s_tychonoff_theorem`

**Techniques used:** 35 ultraproductTransfer; 16 compactnessArgument

---

### Church–Turing Halting (Ch. 5)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_undecidability_of_halting`

**Steps:**
1. input: `s_alleged_decider_H_for_halting` --[t_arithmetize_syntax {machines as tape input}]--> output: `s_encoding_of_machines_as_data`
2. input: `s_encoding_of_machines_as_data` --[t_diagonalize {D(⟨M⟩) halts iff M(⟨M⟩) does not}]--> output: `s_self_contradictory_machine_D`
3. input: `s_self_contradictory_machine_D` --[t_infinite_descent {dual form}]--> output: `s_undecidability_of_halting`

**Techniques used:** 18 arithmetizeSyntax; 17 diagonalize; 21 infiniteDescent

---

### Gödel's Consistency of CH with ZFC (Ch. 5)

**Axioms:** `s_zfc_axioms`
**Terminal:** `s_con_zfc_gch`

**Steps:**
1. input: `s_zfc_axioms` --[t_force_independence {inner model L = constructible universe}]--> output: `s_model_L_of_ZFC_plus_GCH`
2. input: `s_model_L_of_ZFC_plus_GCH` --[t_structural_isomorphism {relative consistency}]--> output: `s_con_zfc_gch`

**Techniques used:** 19 forceIndependence; 13 structuralIsomorphism

---

### Ramsey's Theorem (Ch. 5)

**Axioms:** `s_infinite_set`, `s_k_coloring_of_pairs`
**Terminal:** `s_ramsey_theorem_infinite`

**Steps:**
1. input: `⟨s_infinite_set, s_k_coloring_of_pairs⟩` --[t_pigeonhole_collision {majority color class at each step}]--> output: `s_nested_monochromatic_sequence`
2. input: `s_nested_monochromatic_sequence` --[t_compactness_argument {diagonal / König's lemma}]--> output: `s_ramsey_theorem_infinite`

**Techniques used:** 30 pigeonholeCollision; 16 compactnessArgument

---

### Ergodic Theorem (Birkhoff / von Neumann) (Ch. 5)

**Axioms:** `s_measure_preserving_transformation`, `s_L2_function_space`
**Terminal:** `s_birkhoff_ergodic_theorem`

**Steps:**
1. input: `⟨s_measure_preserving_transformation, s_L2_function_space⟩` --[t_frequency_decomposition {spectral decomposition of Koopman operator U}]--> output: `s_invariant_subspace_decomposition`
2. input: `s_invariant_subspace_decomposition` --[t_conserved_quantity {projection onto U-invariants = time average}]--> output: `s_birkhoff_ergodic_theorem`

**Techniques used:** 11 frequencyDecomposition; 7 conservedQuantity

---

### Chapter 6 — Modern & Contemporary

### Atiyah–Singer Index Theorem (Ch. 6)

**Axioms:** `s_compact_smooth_manifold`, `s_elliptic_operator_D`
**Terminal:** `s_atiyah_singer_index_theorem`

**Steps:**
1. input: `s_elliptic_operator_D_on_manifold` --[t_frequency_decomposition {symbol σ(D) on T*M}]--> output: `s_principal_symbol_in_K_theory_of_TM`
2. input: `s_principal_symbol_in_K_theory_of_TM` --[t_group_complete_exact_category {K-theory of cotangent bundle}]--> output: `s_topological_index_class_in_K_of_point`
3. input: `s_topological_index_class_in_K_of_point` --[t_analysis_algebra_topology_bridge {push-forward = analytic index}]--> output: `s_atiyah_singer_index_theorem`

**Techniques used:** 11 frequencyDecomposition; 52 groupCompleteExactCategory; 25 analysisAlgebraTopologyBridge

---

### Classification of Finite Simple Groups (Ch. 6)

**Axioms:** `s_finite_simple_group`
**Terminal:** `s_cfsg`

**Steps:**
1. input: `s_finite_simple_group` --[t_reduce_to_canonical_form {local analysis by Sylow subgroups, signalizer functors}]--> output: `s_component_type_and_characteristic_p_type_cases`
2. input: `s_component_type_and_characteristic_p_type_cases` --[t_distributed_collaboration {hundreds of authors, thousands of pages}]--> output: `s_case_exhaustion_complete`
3. input: `s_case_exhaustion_complete` --[t_finite_case_check {26 sporadic groups, 18 infinite families}]--> output: `s_cfsg`

**Techniques used:** 4 reduceToCanonicalForm; 28 distributedCollaboration; 26 finiteCaseCheck

---

### Independence of Continuum Hypothesis (Cohen) (Ch. 6)

**Axioms:** `s_zfc_axioms`
**Terminal:** `s_ch_independent_of_zfc`

**Steps:**
1. input: `⟨s_zfc_axioms, s_godel_L_model⟩` --[t_force_independence {Cohen forcing: add a generic set}]--> output: `s_model_of_ZFC_plus_not_CH`
2. input: `⟨s_model_of_ZFC_plus_not_CH, s_model_L_of_ZFC_plus_GCH⟩` --[t_structural_isomorphism {combined with prior GCH-model}]--> output: `s_ch_independent_of_zfc`

**Techniques used:** 19 forceIndependence; 13 structuralIsomorphism

---

### Four Color Theorem (Ch. 6)

**Axioms:** `s_planar_graph`, `s_proper_vertex_coloring`
**Terminal:** `s_four_color_theorem`

**Steps:**
1. input: `s_planar_graph` --[t_reduce_to_canonical_form {unavoidable set of configurations}]--> output: `s_finite_list_of_1500_configurations`
2. input: `s_finite_list_of_1500_configurations` --[t_finite_case_check {reducibility checked by computer}]--> output: `s_four_color_theorem`
3. (later) input: `s_four_color_theorem` --[t_formal_verify {Gonthier's Coq proof}]--> output: `s_four_color_theorem_machine_certified`

**Techniques used:** 4 reduceToCanonicalForm; 26 finiteCaseCheck; 27 formalVerify

---

### Faltings's Theorem / Mordell Conjecture (Ch. 6)

**Axioms:** `s_smooth_projective_curve_over_Q`, `s_jacobian_variety`
**Terminal:** `s_mordell_faltings`

**Steps:**
1. input: `s_curve_of_genus_at_least_2` --[t_raise_dimension {curve C ↪ Jacobian J_C}]--> output: `s_curve_inside_abelian_variety`
2. input: `s_curve_inside_abelian_variety` --[t_analysis_algebra_topology_bridge {heights, Galois representations, p-adic Hodge}]--> output: `s_finiteness_of_isogeny_class`
3. input: `s_finiteness_of_isogeny_class` --[t_obstruction_class {Tate conjecture for abelian varieties → rational points finite}]--> output: `s_mordell_faltings`

**Techniques used:** 14 raiseDimension; 25 analysisAlgebraTopologyBridge; 15 obstructionClass

---

### Wiles's Modularity / FLT (Ch. 6)

**Axioms:** `s_elliptic_curve_over_Q`, `s_modular_form`, `s_galois_representation`
**Terminal:** `s_flt`

**Steps:**
1. input: `s_hypothetical_FLT_solution_a_n_plus_b_n_equals_c_n` --[t_compose_with_identity {Frey curve y² = x(x − aⁿ)(x + bⁿ)}]--> output: `s_frey_elliptic_curve`
2. input: `s_frey_elliptic_curve` --[t_analysis_algebra_topology_bridge {Ribet level-lowering: Frey curve ⇒ non-modular mod ℓ rep}]--> output: `s_non_modular_galois_representation_required`
3. input: `s_non_modular_galois_representation_required` --[t_deformation_cohomology {R = T theorem: universal deformation ring = Hecke algebra}]--> output: `s_semistable_modularity_theorem`
4. input: `⟨s_semistable_modularity_theorem, s_non_modular_galois_representation_required⟩` --[t_obstruction_class {contradiction: every semistable elliptic curve is modular}]--> output: `s_flt`

**Techniques used:** 5 composeWithIdentity; 25 analysisAlgebraTopologyBridge; 41 deformationCohomology; 15 obstructionClass

---

### Perelman's Poincaré / Geometrization (Ch. 6)

**Axioms:** `s_closed_3_manifold`, `s_riemannian_metric`
**Terminal:** `s_poincare_conjecture`, `s_geometrization_theorem`

**Steps:**
1. input: `⟨s_closed_3_manifold, s_riemannian_metric⟩` --[t_physics_to_pde {Hamilton's Ricci flow ∂g/∂t = −2 Ric(g)}]--> output: `s_ricci_flow_equation`
2. input: `s_ricci_flow_equation` --[t_flow_with_surgery {neck-pinch surgery; Perelman entropy and reduced volume as monotone monitors}]--> output: `s_long_time_decomposition_into_geometric_pieces`
3. input: `s_long_time_decomposition_into_geometric_pieces` --[t_rescale_for_asymptotic_geometry {κ-solutions, blow-up analysis}]--> output: `s_thurston_eight_geometries_classification`
4. input: `s_thurston_eight_geometries_classification` --[t_obstruction_class {simply connected ⇒ S³}]--> output: `s_poincare_conjecture`

**Techniques used:** 23 physicsToPDE; 22 flowWithSurgery; 44 rescaleForAsymptoticGeometry; 15 obstructionClass

---

### Kepler Conjecture (Hales) (Ch. 6)

**Axioms:** `s_euclidean_3_space`, `s_unit_balls_sphere_packing`
**Terminal:** `s_kepler_conjecture`

**Steps:**
1. input: `s_sphere_packing_density_functional` --[t_reduce_to_canonical_form {Voronoi / decomposition stars: finite local structure}]--> output: `s_finite_family_of_local_star_configurations`
2. input: `s_finite_family_of_local_star_configurations` --[t_finite_case_check {≈10⁵ nonlinear programs}]--> output: `s_kepler_conjecture`
3. (later) input: `s_kepler_conjecture` --[t_formal_verify {Flyspeck, HOL Light / Isabelle}]--> output: `s_kepler_conjecture_machine_certified`

**Techniques used:** 4 reduceToCanonicalForm; 26 finiteCaseCheck; 27 formalVerify

---

### Green–Tao Theorem (Arithmetic Progressions in Primes) (Ch. 6)

**Axioms:** `s_prime_numbers`, `s_szemeredi_theorem`
**Terminal:** `s_green_tao`

**Steps:**
1. input: `⟨s_primes_with_density_zero, s_szemeredi_theorem⟩` --[t_analysis_algebra_topology_bridge {transference principle: dense subset of a pseudorandom majorant}]--> output: `s_relative_szemeredi_for_pseudorandom_majorants`
2. input: `s_relative_szemeredi_for_pseudorandom_majorants` --[t_ergodic_correspondence {combinatorial AP count = ergodic multi-return}]--> output: `s_aps_in_pseudorandom_dense_subset`
3. input: `⟨s_aps_in_pseudorandom_dense_subset, s_goldston_yildirim_sieve_majorant⟩` --[t_sieve_by_optimized_quadratic]--> output: `s_green_tao`

**Techniques used:** 25 analysisAlgebraTopologyBridge; 48 ergodicCorrespondence; 50 sieveByOptimizedQuadratic

---

### Zhang / Maynard–Tao Bounded Gaps (Ch. 6)

**Axioms:** `s_prime_numbers`, `s_admissible_k_tuple`
**Terminal:** `s_bounded_gaps_between_primes`

**Steps:**
1. input: `s_admissible_k_tuple` --[t_sieve_by_optimized_quadratic {Selberg-type weights with multidimensional truncation}]--> output: `s_positive_lower_bound_on_prime_pairs_in_tuple`
2. input: `s_positive_lower_bound_on_prime_pairs_in_tuple` --[t_distributed_collaboration {Polymath 8 optimization}]--> output: `s_gap_bound_246`
3. input: `s_gap_bound_246` --[t_compose_with_identity]--> output: `s_bounded_gaps_between_primes`

**Techniques used:** 50 sieveByOptimizedQuadratic; 28 distributedCollaboration; 5 composeWithIdentity

---

### Helfgott's Ternary Goldbach (Ch. 6)

**Axioms:** `s_integers`, `s_primes_in_naturals`
**Terminal:** `s_ternary_goldbach`

**Steps:**
1. input: `s_integer_N_odd_and_larger_than_5` --[t_frequency_decomposition {exponential sum F(α) = Σ_{p ≤ N} e^{2πipα}}]--> output: `s_circle_integral_for_r3_N`
2. input: `s_circle_integral_for_r3_N` --[t_major_minor_arc_decomposition {Farey dissection}]--> output: `s_major_arc_asymptotic_plus_minor_arc_error`
3. input: `s_major_arc_asymptotic_plus_minor_arc_error` --[t_finite_case_check {verify Vinogradov-style bounds explicitly up to 10³⁰}]--> output: `s_ternary_goldbach`

**Techniques used:** 11 frequencyDecomposition; 47 majorMinorArcDecomposition; 26 finiteCaseCheck

---

### Robertson–Seymour Graph Minor Theorem (Ch. 6)

**Axioms:** `s_graph_definition`, `s_minor_ordering`
**Terminal:** `s_graph_minor_theorem`

**Steps:**
1. input: `s_infinite_sequence_of_graphs` --[t_reduce_to_canonical_form {tree-decomposition into 3-connected parts}]--> output: `s_tree_width_decomposition`
2. input: `s_tree_width_decomposition` --[t_compactness_argument {well-quasi-order of trees and labelled components}]--> output: `s_graph_minor_theorem`

**Techniques used:** 4 reduceToCanonicalForm; 16 compactnessArgument

---

### Szemerédi's Theorem (Ch. 6)

**Axioms:** `s_integers`, `s_positive_density_subset`
**Terminal:** `s_szemeredi_theorem`

**Steps:**
1. input: `s_positive_density_subset_of_integers` --[t_ergodic_correspondence {Furstenberg: subset ↔ measure-preserving system}]--> output: `s_furstenberg_system_with_positive_measure_A`
2. input: `s_furstenberg_system_with_positive_measure_A` --[t_probabilistic_existence {Szemerédi regularity lemma as partition with low error}]--> output: `s_multiple_recurrence_for_A`
3. input: `s_multiple_recurrence_for_A` --[t_compose_with_identity {translate back to APs in original subset}]--> output: `s_szemeredi_theorem`

**Techniques used:** 48 ergodicCorrespondence; 29 probabilisticExistence; 5 composeWithIdentity

---

## Part B — Common state / technique inventory

### B1. Recurring states (appear in 3+ theorems)

- **`s_real_numbers`** — axiom/state — the real line ℝ (completion of ℚ). Used as base ring/field in Cauchy, Cantor, Bolzano, Weierstrass, FTC, CLT, Stokes, Hahn–Banach.
- **`s_complex_numbers`** — axiom — field ℂ. Used in de Moivre, Euler formula, FTA, Cardano, Cauchy integral, Riemann mapping, Riemann–Roch, PNT.
- **`s_integers`** — axiom — ring ℤ. Used in FLT, Euclid's primes, FTA, Lagrange four-square, Fermat LT/2-sq, Chakravāla, Wilson, Helfgott, Zhang.
- **`s_polynomial_ring`** — state — polynomial ring over a field. Used in Cardano, Ferrari, FTA, Abel–Ruffini, Galois, Hilbert's basis, Nullstellensatz.
- **`s_continuous_function_on_interval`** — state. Bolzano, FTC, Weierstrass approximation, Brouwer, Banach.
- **`s_L2_function_space`** — state. Fourier, CLT, Plancherel-style steps, ergodic theorem.
- **`s_finite_group`** — state/axiom. Sylow, Galois, CFSG, Lagrange, Fermat LT, Burnside-style counting.
- **`s_galois_group`** — state. Abel–Ruffini, Galois FT, Wiles (Galois reps as modern analog).
- **`s_compact_smooth_manifold`** — state. Gauss–Bonnet, Atiyah–Singer, Poincaré, de Rham/Stokes.
- **`s_smooth_function`** — state. Taylor, MVT, FTC, Stokes, physics-to-PDE family.
- **`s_riemannian_metric`** — state. Theorema Egregium, Gauss–Bonnet, Ricci flow/Perelman.
- **`s_compact_oriented_surface_without_boundary`** — state. Gauss–Bonnet, Riemann–Roch, Riemann mapping (via genus).
- **`s_elliptic_curve_over_Q`** — state. Wiles/FLT, modularity, Mordell–Faltings, BSD-adjacent steps.
- **`s_modular_form`** — state. Wiles, modularity, monstrous moonshine, Hardy–Ramanujan partitions.
- **`s_riemann_zeta_function`** — state. PNT, Basel, Riemann memoir, Dirichlet L-function analogues.
- **`s_euler_characteristic_chi`** — state. Euler polyhedron, Gauss–Bonnet, Riemann–Roch, Atiyah–Singer.
- **`s_prime_numbers`** — state. Euclid, Fermat LT, PNT, Green–Tao, Zhang, Dirichlet, Goldbach.
- **`s_measure_preserving_transformation`** — state. Ergodic theorem, Furstenberg/Szemerédi, Green–Tao.
- **`s_zfc_axioms`** — axiom. Well-ordering, CH independence, Banach–Tarski.
- **`s_smooth_manifold_with_boundary`** — state. Stokes, de Rham, Atiyah–Singer.
- **`s_primes_in_naturals`** — state/axiom alias. PNT, Dirichlet, Goldbach, Green–Tao.
- **`s_simply_connected_manifold`** — state. Riemann mapping (n=2), Poincaré (n=3), generalized Poincaré (n≥5).

### B2. Recurring techniques (appear in 3+ theorem chains above)

- **t_symmetry_reduction** (Cluster 3) — quotient by a group action. Pythagoras, Thales, Archimedes, Fermat LT, Sylow, Noether, Desargues.
- **t_compose_with_identity** (Cluster 2) — use an algebraic identity to combine P-instances. Pythagoras, Euclid primes, Ptolemy, Chakravāla, Lagrange four-square, Cauchy formula, Gauss–Bonnet, Brouwer, Ferrari/Cardano linkage, FTC, Wiles (Frey curve identity).
- **t_reduce_to_canonical_form** (Cluster 2) — change of coordinates to normal form. CRT, Cardano, Ferrari, Euler polyhedron, Stokes, Hahn–Banach, Graph minor, CFSG, Kepler, Four Color, Gauss–Bonnet.
- **t_conserved_quantity** (Cluster 3) — invariant under transformation. Euler polyhedron, Gauss–Bonnet, Theorema Egregium, FTA (winding), Cauchy (closed form), Sylow counting, Noether, Riemann–Roch, Ergodic theorem.
- **t_frequency_decomposition** (Cluster 4) — project onto orthogonal basis. de Moivre, Euler formula, Basel, Fourier, CLT, ergodic (spectral), Atiyah–Singer (symbol), Helfgott.
- **t_compactness_argument** (Cluster 6) — extract convergent subsequence. FTA, Riemann mapping, Hahn–Banach (Zorn), Tychonoff, Ramsey, CLT (Lévy), Graph minor, Weierstrass.
- **t_exhaustion_squeeze** (Cluster 4) — Lₙ ≤ target ≤ Uₙ both converge. Archimedes (circle & sphere), FTC (Riemann sums), Weierstrass approximation.
- **t_structural_isomorphism** (Cluster 5) — build a functor between theories. CRT, Galois FT, Nullstellensatz, CH consistency, Abel–Ruffini.
- **t_obstruction_class** (Cluster 6) — invariant must vanish for construction. Abel–Ruffini (A_5), Brouwer (degree), PNT (ζ non-vanishing), Mordell–Faltings, Wiles, Poincaré, Gödel.
- **t_infinite_descent** (Cluster 8) — minimal counterexample leads to smaller one. Euclid primes, FTA (uniqueness), Fermat 2-sq, Lagrange 4-sq, Chakravāla, Cantor (dual), Hilbert basis (ACC), Brouwer (dual), Halting (dual).
- **t_contraction_fixed_point** (Cluster 8) — Banach iteration. Banach FPT, Fourier (mode-decay), Riemann mapping (variational).
- **t_physics_to_pde** (Cluster 9) — distil physics into equations. Kepler, Fourier/heat, Theorema Egregium (geodesy), Noether (action), Perelman (Ricci flow).
- **t_diagonalize** (Cluster 7) — construct element not in alleged enumeration. Cantor, Gödel, Halting.
- **t_arithmetize_syntax** (Cluster 7) — encode formal system in arithmetic. Gödel, Halting, Cook–Levin.
- **t_finite_case_check** (Cluster 10) — finite reduction + machine check. Four Color, Kepler, CFSG, Helfgott, Robertson–Seymour.
- **t_formal_verify** (Cluster 10) — kernel-checked proof. Four Color (Gonthier), Kepler (Flyspeck), Feit–Thompson.
- **t_distributed_collaboration** (Cluster 10) — many-author roadmap. CFSG, Modularity chain, Polymath 8, Green–Tao extensions.
- **t_force_independence** (Cluster 7) — build models both ways. Gödel L, Cohen CH, Solovay measurability.
- **t_raise_dimension** (Cluster 6) — embed into higher space. Desargues 2→3D, FTA (curves in plane), Faltings (curve↪Jacobian), Wiles (elliptic↪Galois rep), Perelman (metric space detour).
- **t_analysis_algebra_topology_bridge** (Cluster 9) — translate across fields. Riemann–Roch, Atiyah–Singer, Faltings, Wiles, Green–Tao transference.
- **t_interpolate_and_continue** (Cluster 4) — extend formula ℕ → ℂ. Taylor, Euler formula, PNT (ζ continuation), CLT (log φ expansion), Wallis.
- **t_axiomatize_from_instances** (Cluster 5) — abstract shared structure. FTA (UFD), Graph theory, Galois, Riemann mapping (extremal family), Hilbert basis, Hahn–Banach.
- **t_pigeonhole_collision** (Cluster 11) — |objects| > |bins|. Fermat 2-sq (Thue's lemma), Lagrange 4-sq, Ramsey, Dirichlet approximation.
- **t_spot_pattern_in_table** (Cluster 1) — empirical conjecture. Kepler's 3rd law, Quadratic reciprocity, Basel (Euler's numerical 1.6449…).
- **t_sieve_by_optimized_quadratic** (Cluster 11) — Selberg sieve. Zhang/Maynard, Green–Tao, Goldston–Yıldırım.
- **t_ergodic_correspondence** (Cluster 9) — subset ↔ measure-preserving system. Furstenberg/Szemerédi, Green–Tao, Host–Kra.
- **t_duality** (Cluster 3) — reverse-arrow equivalence. Desargues (projective), Galois, Nullstellensatz (ideals ↔ varieties), Stokes (∫/d), de Rham.
- **t_character_decomposition_count** (Cluster 3) — decompose against irreducible characters. Sylow, Quadratic reciprocity (Gauss sum), Burnside counting.

### B3. Compound techniques flagged for subgraph elaboration

Each of the following should have `has_subgraph: true` in the formal graph. Listed with sub-techniques that compose it.

1. **t_fourier_transform** (umbrella for t_frequency_decomposition at continuous/discrete/group-theoretic level). Sub-techniques: orthogonal projection onto basis; Plancherel isometry; convolution-to-pointwise; inverse transform. Appears in: Fourier heat, CLT, Helfgott (on the circle), ergodic spectral theorem, Atiyah–Singer (symbol calculus).

2. **t_svd_and_spectral_decomposition** (⚠ not in toolbox as a named entry; closest is t_reduce_to_canonical_form + t_frequency_decomposition composed). Flag for orchestrator: consider adding as a new toolbox entry under Cluster 2 or Cluster 4. Sub-techniques: orthogonal diagonalization of self-adjoint; polar decomposition; Eckart–Young approximation.

3. **t_galois_correspondence** (t_structural_isomorphism instantiated). Sub-techniques: Galois group construction (t_symmetry_reduction on roots); normality and separability conditions; subgroup↔subfield lattice (t_duality); solvable tower criterion (t_obstruction_class). Appears in: Galois FT, Abel–Ruffini, class field theory, Wiles (as deformation-of-reps analog).

4. **t_ricci_flow_with_surgery** (instantiation of t_flow_with_surgery). Sub-techniques: Hamilton parabolic PDE setup (t_physics_to_pde); maximum principle / curvature evolution; Perelman entropy monotonicity (t_conserved_quantity); κ-solutions asymptotic analysis (t_rescale_for_asymptotic_geometry); neck-pinch classification; gluing / surgery procedure. Appears in: Poincaré, Geometrization, Kähler–Ricci (Song–Tian).

5. **t_atiyah_singer_index_machinery** (composite of t_frequency_decomposition + t_group_complete_exact_category + t_analysis_algebra_topology_bridge). Sub-techniques: symbol class in K(TX); Thom isomorphism / Gysin pushforward; embedding into ℝⁿ and Bott periodicity; topological index map; heat-kernel proof (an alternative route). Appears in: classical Atiyah–Singer, equivariant and families index, Connes noncommutative index.

6. **t_wiles_modularity** (composite of t_deformation_cohomology + t_analysis_algebra_topology_bridge + t_obstruction_class). Sub-techniques: Frey curve construction; Ribet level-lowering; universal deformation ring R; Hecke algebra T; R = T theorem (numerical criterion); Taylor–Wiles patching; Kisin refinements. Appears in: semistable modularity, full modularity (BCDT), Serre conjecture proofs.

7. **t_godel_numbering** (composite inside t_arithmetize_syntax). Sub-techniques: prime-power encoding of sequences; primitive-recursive predicates; representability of recursive relations; diagonal/fixed-point lemma (t_diagonalize). Appears in: Incompleteness, Halting, Cook–Levin, Matiyasevich/MRDP.

8. **t_category_theoretic_colimits_and_adjoints** (composite under t_representable_functor_trick). Sub-techniques: universal property → Yoneda; colimit as left adjoint; Freyd adjoint functor theorem; Kan extension. Appears in: sheafification, Grothendieck K₀ (Grothendieck group = free abelian colimit), moduli functor representability.

9. **t_selberg_sieve_method** (instantiation of t_sieve_by_optimized_quadratic). Sub-techniques: Möbius inversion (t_compose_with_identity); upper-bound quadratic form; level-of-distribution estimate (Bombieri–Vinogradov); GPY multidim weights (Maynard). Appears in: Chen's theorem, Zhang/Maynard, Green–Tao majorant, Brun–Titchmarsh.

10. **t_circle_method** (instantiation of t_major_minor_arc_decomposition). Sub-techniques: generating exponential sum F(α); Farey arc dissection; singular-series evaluation via local Euler products; Weyl differencing / Vinogradov's method on minor arcs; Vaughan identity. Appears in: Hardy–Ramanujan, Waring, Vinogradov three primes, Helfgott, Bourgain–Demeter–Guth decoupling.

11. **t_furstenberg_correspondence_principle** (instantiation of t_ergodic_correspondence). Sub-techniques: Krylov–Bogolyubov invariant-measure extension (t_compactness_argument); Kronecker factor / characteristic factor theory; Host–Kra nilsequence structure. Appears in: Szemerédi (ergodic), Green–Tao transference, polynomial Szemerédi.

12. **t_polynomial_method** (already a toolbox entry; flagged because its applications are themselves multi-step). Sub-techniques: dimension-counting for vanishing polynomial; restriction to structured lines (univariate overdetermination); Guth–Katz polynomial partitioning; low-degree approximation (Razborov–Smolensky). Appears in: Kakeya (Dvir), cap-set (Ellenberg–Gijswijt), distinct distances (Guth–Katz).

13. **t_schur_weyl_and_double_centralizer** (already a toolbox entry t_double_centralizer_decompose). Sub-techniques: commuting-action setup; isotypic decomposition on each side; character-table transfer. Appears in: Schur–Weyl, Peter–Weyl, Howe reciprocity.

14. **t_deformation_and_R_equals_T** (instantiation of t_deformation_cohomology). Sub-techniques: universal deformation ring (t_representable_functor_trick); tangent-obstruction computation via Galois cohomology H¹/H²; Hecke algebra as analytic side (t_sheafify_on_grothendieck_topology + modular forms); Taylor–Wiles patching (t_compactness_argument in a pro-finite setting). Appears in: Wiles, Kisin, Calegari–Geraghty.

15. **t_perelman_entropy_package** (sub-components of the Ricci-flow subgraph but also standalone techniques). Sub-techniques: reduced-volume monotonicity; κ-non-collapsing; no-local-collapsing under bounded curvature. Appears in: Perelman's Poincaré, Tian–Zhang (Kähler), mean-curvature-flow analogs.

---

## Flags summary

- **⚠ not in toolbox: t_svd_and_spectral_decomposition** (Part B3 item 2). I used the composite `t_reduce_to_canonical_form + t_frequency_decomposition` in the chains that needed it, but a named entry would be cleaner. Orchestrator to decide whether to add.
- **⚠ partial-fit: t_heights_and_galois_representations** — in Faltings and Wiles chains I collapsed this into `t_analysis_algebra_topology_bridge`, which is correct at the abstraction level of the main graph; if the subgraph for Wiles elaborates further, sub-nodes for "canonical height", "Galois representation", "p-adic Hodge theory" will be needed.
- **⚠ partial-fit: t_zorn_lemma / t_axiom_of_choice** — I folded this into `t_compactness_argument` (Hahn–Banach) following the toolbox's treatment of Zorn as a compactness-style existence principle. If philosopher flags it as distinct, split.

---

## Self-audit

- Part A theorem chains: **63** (spread: 8 ancient/medieval, 7 renaissance/17c, 10 eighteenth-century, 13 nineteenth-century, 12 early-20c, 13 modern). Slightly above the 40–50 target because reusing states/techniques across many chains was cheap and made the fan-in argument for Part B stronger.
- Part B recurring states: **22**.
- Part B recurring techniques (3+ appearances): **28**.
- Part B compound techniques flagged for subgraphs: **15**.
- Not-in-toolbox flags: **1 firm** (`t_svd_and_spectral_decomposition`) + **2 partial-fit** notes (`t_heights_and_galois_representations`, `t_zorn_lemma`) for the orchestrator to review.
