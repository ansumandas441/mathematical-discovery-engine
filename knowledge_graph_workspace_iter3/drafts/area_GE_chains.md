# Area Geometry Derivation Chains (iter-3)

**Source pages:**
- https://en.wikipedia.org/wiki/Category:Theorems_in_differential_geometry
- https://en.wikipedia.org/wiki/Category:Theorems_in_Riemannian_geometry
- https://en.wikipedia.org/wiki/Category:Theorems_in_algebraic_geometry
- https://en.wikipedia.org/wiki/Category:Theorems_in_complex_geometry
- https://en.wikipedia.org/wiki/Category:Symplectic_geometry

**Target:** 100 chains. **Drafted:** 109. **Skipped (already in graph):** 7 — `s_gauss_bonnet_theorem`, `s_theorema_egregium`, `s_atiyah_singer_index_theorem`, `s_riemann_roch_theorem`, `s_mordell_faltings`, `s_hilbert_basis_theorem`, `s_nullstellensatz`.
**Flagged (`⚠ needs new technique`):** 0.

---

### Fundamental theorem of Riemannian geometry (Levi-Civita) (cite: https://en.wikipedia.org/wiki/Fundamental_theorem_of_Riemannian_geometry)

**Axioms:** `s_riemannian_metric`, `s_smooth_manifold`
**Terminal:** `s_levi_civita_connection` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_smooth_manifold⟩` --[t_axiomatize_from_instances {properties: ["metric_compatible", "torsion_free"]}]--> output: `s_connection_axioms_metric_torsion_free`
2. input: `s_connection_axioms_metric_torsion_free` --[t_reduce_to_canonical_form {form: "Koszul_formula"}]--> output: `s_koszul_formula_for_connection`
3. input: `s_koszul_formula_for_connection` --[t_structural_isomorphism {target: "unique_solution"}]--> output: `s_levi_civita_connection`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form, t_structural_isomorphism

---

### Hopf–Rinow theorem (cite: https://en.wikipedia.org/wiki/Hopf%E2%80%93Rinow_theorem)

**Axioms:** `s_riemannian_metric`, `s_smooth_manifold`
**Terminal:** `s_hopf_rinow_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_smooth_manifold⟩` --[t_axiomatize_from_instances {properties: ["geodesic_completeness", "metric_completeness"]}]--> output: `s_completeness_notions_for_riemannian_manifold`
2. input: `s_completeness_notions_for_riemannian_manifold` --[t_compactness_argument {use: "Heine_Borel_for_closed_balls"}]--> output: `s_closed_bounded_sets_compact`
3. input: `s_closed_bounded_sets_compact` --[t_exhaustion_squeeze {family: "expanding_geodesic_balls"}]--> output: `s_minimizing_geodesic_between_any_two_points`
4. input: `s_minimizing_geodesic_between_any_two_points` --[t_structural_isomorphism {target: "equivalence_of_completeness"}]--> output: `s_hopf_rinow_theorem`

**Techniques used:** t_axiomatize_from_instances, t_compactness_argument, t_exhaustion_squeeze, t_structural_isomorphism

---

### Cartan–Hadamard theorem (cite: https://en.wikipedia.org/wiki/Cartan%E2%80%93Hadamard_theorem)

**Axioms:** `s_riemannian_metric`, `s_smooth_manifold`
**Terminal:** `s_cartan_hadamard_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_smooth_manifold⟩` --[t_axiomatize_from_instances {properties: ["complete", "nonpositive_sectional_curvature"]}]--> output: `s_complete_nonpositively_curved_manifold`
2. input: `s_complete_nonpositively_curved_manifold` --[t_conserved_quantity {invariant: "Jacobi_field_growth"}]--> output: `s_no_conjugate_points`
3. input: `s_no_conjugate_points` --[t_structural_isomorphism {map: "exp_p"}]--> output: `s_exp_map_is_covering`
4. input: `s_exp_map_is_covering` --[t_analysis_algebra_topology_bridge {target: "universal_cover_diffeomorphic_to_Rn"}]--> output: `s_cartan_hadamard_theorem`

**Techniques used:** t_axiomatize_from_instances, t_conserved_quantity, t_structural_isomorphism, t_analysis_algebra_topology_bridge

---

### Bonnet–Myers theorem (cite: https://en.wikipedia.org/wiki/Myers%27s_theorem)

**Axioms:** `s_riemannian_metric`, `s_smooth_manifold`
**Terminal:** `s_bonnet_myers_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_smooth_manifold⟩` --[t_axiomatize_from_instances {properties: ["Ricci_geq_(n-1)k", "complete"]}]--> output: `s_complete_manifold_with_ricci_lower_bound`
2. input: `s_complete_manifold_with_ricci_lower_bound` --[t_auxiliary_construction {object: "second_variation_of_arc_length_along_geodesic"}]--> output: `s_second_variation_index_form`
3. input: `s_second_variation_index_form` --[t_reductio_ad_absurdum {assume: "geodesic_longer_than_pi/sqrt(k)"}]--> output: `s_diameter_bound_pi_over_sqrt_k`
4. input: `s_diameter_bound_pi_over_sqrt_k` --[t_compactness_argument {conclusion: "compact_finite_pi1"}]--> output: `s_bonnet_myers_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_reductio_ad_absurdum, t_compactness_argument

---

### Synge's theorem (cite: https://en.wikipedia.org/wiki/Synge%27s_theorem)

**Axioms:** `s_riemannian_metric`, `s_compact_smooth_manifold`
**Terminal:** `s_synge_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_compact_smooth_manifold⟩` --[t_axiomatize_from_instances {properties: ["positive_sectional_curvature", "even_dim", "orientable"]}]--> output: `s_compact_even_dim_orientable_positively_curved`
2. input: `s_compact_even_dim_orientable_positively_curved` --[t_auxiliary_construction {object: "shortest_closed_geodesic_in_free_homotopy_class"}]--> output: `s_closed_geodesic_minimizer`
3. input: `s_closed_geodesic_minimizer` --[t_symmetry_reduction {use: "parallel_transport_holonomy_on_geodesic"}]--> output: `s_parallel_vector_field_along_geodesic`
4. input: `s_parallel_vector_field_along_geodesic` --[t_reductio_ad_absurdum {derive: "second_variation_negative"}]--> output: `s_synge_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_symmetry_reduction, t_reductio_ad_absurdum

---

### Cheng's diameter rigidity theorem (cite: https://en.wikipedia.org/wiki/Cheng%27s_eigenvalue_comparison_theorem)

**Axioms:** `s_riemannian_metric`, `s_compact_smooth_manifold`
**Terminal:** `s_cheng_diameter_rigidity` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_compact_smooth_manifold⟩` --[t_axiomatize_from_instances {properties: ["Ricci_geq_(n-1)", "diameter_equals_pi"]}]--> output: `s_extremal_diameter_case_of_bonnet_myers`
2. input: `s_extremal_diameter_case_of_bonnet_myers` --[t_conserved_quantity {invariant: "equality_in_Bishop_volume_comparison"}]--> output: `s_volume_equality_with_round_sphere`
3. input: `s_volume_equality_with_round_sphere` --[t_structural_isomorphism {target: "isometric_to_unit_sphere"}]--> output: `s_cheng_diameter_rigidity`

**Techniques used:** t_axiomatize_from_instances, t_conserved_quantity, t_structural_isomorphism

---

### Cheeger–Gromoll splitting theorem (cite: https://en.wikipedia.org/wiki/Splitting_theorem)

**Axioms:** `s_riemannian_metric`, `s_smooth_manifold`
**Terminal:** `s_cheeger_gromoll_splitting` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_smooth_manifold⟩` --[t_axiomatize_from_instances {properties: ["complete", "Ricci_geq_0", "contains_line"]}]--> output: `s_complete_nonneg_ricci_with_line`
2. input: `s_complete_nonneg_ricci_with_line` --[t_auxiliary_construction {object: "Busemann_functions_along_line"}]--> output: `s_pair_of_busemann_functions`
3. input: `s_pair_of_busemann_functions` --[t_conserved_quantity {invariant: "harmonicity_via_Laplacian_comparison"}]--> output: `s_harmonic_busemann_function_pair`
4. input: `s_harmonic_busemann_function_pair` --[t_structural_isomorphism {target: "isometric_splitting_R_times_N"}]--> output: `s_cheeger_gromoll_splitting`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_conserved_quantity, t_structural_isomorphism

---

### Soul theorem (cite: https://en.wikipedia.org/wiki/Soul_theorem)

**Axioms:** `s_riemannian_metric`, `s_smooth_manifold`
**Terminal:** `s_soul_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_smooth_manifold⟩` --[t_axiomatize_from_instances {properties: ["complete", "noncompact", "nonneg_sectional"]}]--> output: `s_open_nonneg_curved_manifold`
2. input: `s_open_nonneg_curved_manifold` --[t_exhaustion_squeeze {family: "convex_sublevel_sets_of_Busemann"}]--> output: `s_nested_totally_convex_sets`
3. input: `s_nested_totally_convex_sets` --[t_projection_to_subspace {target: "minimal_totally_geodesic_submanifold"}]--> output: `s_soul_submanifold`
4. input: `s_soul_submanifold` --[t_structural_isomorphism {target: "M_diffeo_to_normal_bundle_of_soul"}]--> output: `s_soul_theorem`

**Techniques used:** t_axiomatize_from_instances, t_exhaustion_squeeze, t_projection_to_subspace, t_structural_isomorphism

---

### Rauch comparison theorem (cite: https://en.wikipedia.org/wiki/Rauch_comparison_theorem)

**Axioms:** `s_riemannian_metric`, `s_smooth_manifold`
**Terminal:** `s_rauch_comparison_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_smooth_manifold⟩` --[t_auxiliary_construction {object: "Jacobi_field_along_geodesic"}]--> output: `s_jacobi_equation_along_geodesic`
2. input: `s_jacobi_equation_along_geodesic` --[t_exhaustion_squeeze {bound: "sectional_curvature_K_leq_K0"}]--> output: `s_sturm_comparison_for_jacobi_norm`
3. input: `s_sturm_comparison_for_jacobi_norm` --[t_structural_isomorphism {target: "infinitesimal_distance_comparison"}]--> output: `s_rauch_comparison_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_structural_isomorphism

---

### Toponogov comparison theorem (cite: https://en.wikipedia.org/wiki/Toponogov%27s_theorem)

**Axioms:** `s_riemannian_metric`, `s_smooth_manifold`
**Terminal:** `s_toponogov_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_smooth_manifold⟩` --[t_axiomatize_from_instances {property: "sectional_curvature_geq_k"}]--> output: `s_lower_curvature_bounded_manifold`
2. input: `s_lower_curvature_bounded_manifold` --[t_auxiliary_construction {object: "geodesic_triangle_in_M_vs_model_space"}]--> output: `s_geodesic_triangle_pair_M_and_Mk`
3. input: `s_geodesic_triangle_pair_M_and_Mk` --[t_exhaustion_squeeze {use: "Rauch_comparison_for_angles"}]--> output: `s_angle_inequality_M_geq_Mk`
4. input: `s_angle_inequality_M_geq_Mk` --[t_structural_isomorphism {target: "global_triangle_comparison"}]--> output: `s_toponogov_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_exhaustion_squeeze, t_structural_isomorphism

---

### Bishop–Gromov volume comparison (cite: https://en.wikipedia.org/wiki/Bishop%E2%80%93Gromov_inequality)

**Axioms:** `s_riemannian_metric`, `s_smooth_manifold`
**Terminal:** `s_bishop_gromov_comparison` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_smooth_manifold⟩` --[t_axiomatize_from_instances {property: "Ricci_geq_(n-1)k"}]--> output: `s_ricci_lower_bounded_manifold`
2. input: `s_ricci_lower_bounded_manifold` --[t_auxiliary_construction {object: "volume_element_in_polar_coords"}]--> output: `s_jacobian_of_exp_map_in_polar`
3. input: `s_jacobian_of_exp_map_in_polar` --[t_exhaustion_squeeze {bound: "Riccati_comparison"}]--> output: `s_pointwise_jacobian_bound`
4. input: `s_pointwise_jacobian_bound` --[t_structural_isomorphism {target: "monotonicity_of_volume_ratio"}]--> output: `s_bishop_gromov_comparison`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_exhaustion_squeeze, t_structural_isomorphism

---

### Gromov compactness for Riemannian manifolds (cite: https://en.wikipedia.org/wiki/Gromov%27s_compactness_theorem_(geometry))

**Axioms:** `s_riemannian_metric`, `s_smooth_manifold`
**Terminal:** `s_gromov_compactness_riemannian` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_smooth_manifold⟩` --[t_axiomatize_from_instances {properties: ["Ricci_geq_const", "diameter_bound"]}]--> output: `s_class_of_manifolds_with_uniform_geometry`
2. input: `s_class_of_manifolds_with_uniform_geometry` --[t_rescale_for_asymptotic_geometry {target: "Gromov_Hausdorff_topology"}]--> output: `s_gromov_hausdorff_distance_on_class`
3. input: `s_gromov_hausdorff_distance_on_class` --[t_compactness_argument {use: "uniform_epsilon_net_via_Bishop_Gromov"}]--> output: `s_total_boundedness_of_class`
4. input: `s_total_boundedness_of_class` --[t_structural_isomorphism {target: "precompactness_in_GH_topology"}]--> output: `s_gromov_compactness_riemannian`

**Techniques used:** t_axiomatize_from_instances, t_rescale_for_asymptotic_geometry, t_compactness_argument, t_structural_isomorphism

---

### Cheeger finiteness theorem (cite: https://en.wikipedia.org/wiki/Cheeger%27s_finiteness_theorem)

**Axioms:** `s_riemannian_metric`, `s_compact_smooth_manifold`
**Terminal:** `s_cheeger_finiteness` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_compact_smooth_manifold⟩` --[t_axiomatize_from_instances {bounds: ["|K|_leq_K0", "vol_geq_v", "diam_leq_D"]}]--> output: `s_uniformly_bounded_geometry_class`
2. input: `s_uniformly_bounded_geometry_class` --[t_rescale_for_asymptotic_geometry {target: "harmonic_radius_lower_bound"}]--> output: `s_uniform_injectivity_radius`
3. input: `s_uniform_injectivity_radius` --[t_compactness_argument {use: "compactness_in_C^{1,alpha}_topology"}]--> output: `s_finite_diffeomorphism_types`
4. input: `s_finite_diffeomorphism_types` --[t_structural_isomorphism {target: "finiteness_statement"}]--> output: `s_cheeger_finiteness`

**Techniques used:** t_axiomatize_from_instances, t_rescale_for_asymptotic_geometry, t_compactness_argument, t_structural_isomorphism

---

### Sphere theorem (1/4-pinched) (cite: https://en.wikipedia.org/wiki/Sphere_theorem)

**Axioms:** `s_riemannian_metric`, `s_compact_smooth_manifold`
**Terminal:** `s_sphere_theorem_quarter_pinched` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_compact_smooth_manifold⟩` --[t_axiomatize_from_instances {property: "1/4_lt_K_leq_1"}]--> output: `s_strictly_quarter_pinched_manifold`
2. input: `s_strictly_quarter_pinched_manifold` --[t_auxiliary_construction {object: "diameter_via_Klingenberg_injectivity"}]--> output: `s_lower_injectivity_radius_pi`
3. input: `s_lower_injectivity_radius_pi` --[t_exhaustion_squeeze {use: "Toponogov_for_geodesic_triangles"}]--> output: `s_two_exponential_charts_cover_M`
4. input: `s_two_exponential_charts_cover_M` --[t_structural_isomorphism {target: "homeomorphism_to_S^n"}]--> output: `s_sphere_theorem_quarter_pinched`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_exhaustion_squeeze, t_structural_isomorphism

---

### Killing–Hopf theorem (cite: https://en.wikipedia.org/wiki/Killing%E2%80%93Hopf_theorem)

**Axioms:** `s_riemannian_metric`, `s_smooth_manifold`
**Terminal:** `s_killing_hopf_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_smooth_manifold⟩` --[t_axiomatize_from_instances {property: "constant_sectional_curvature_k"}]--> output: `s_space_form_class`
2. input: `s_space_form_class` --[t_symmetry_reduction {use: "transitive_action_of_isometry_group"}]--> output: `s_universal_cover_is_model_space`
3. input: `s_universal_cover_is_model_space` --[t_structural_isomorphism {target: "quotient_by_discrete_isometry_group"}]--> output: `s_killing_hopf_theorem`

**Techniques used:** t_axiomatize_from_instances, t_symmetry_reduction, t_structural_isomorphism

---

### Myers–Steenrod theorem (cite: https://en.wikipedia.org/wiki/Myers%E2%80%93Steenrod_theorem)

**Axioms:** `s_riemannian_metric`, `s_smooth_manifold`
**Terminal:** `s_myers_steenrod_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_smooth_manifold⟩` --[t_auxiliary_construction {object: "isometry_group_with_compact_open_topology"}]--> output: `s_isometry_group_topological`
2. input: `s_isometry_group_topological` --[t_compactness_argument {use: "Arzela_Ascoli_on_distance_preserving_maps"}]--> output: `s_isometry_group_locally_compact`
3. input: `s_isometry_group_locally_compact` --[t_analysis_algebra_topology_bridge {target: "Lie_group_structure_via_Bochner"}]--> output: `s_myers_steenrod_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_analysis_algebra_topology_bridge

---

### Nash embedding theorem (cite: https://en.wikipedia.org/wiki/Nash_embedding_theorems)

**Axioms:** `s_riemannian_metric`, `s_smooth_manifold`
**Terminal:** `s_nash_embedding_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_smooth_manifold⟩` --[t_auxiliary_construction {object: "free_embedding_into_high_dim_Euclidean"}]--> output: `s_free_embedding_existence`
2. input: `s_free_embedding_existence` --[t_contraction_fixed_point {scheme: "Nash_Moser_iteration_with_smoothing"}]--> output: `s_perturbative_isometric_embedding`
3. input: `s_perturbative_isometric_embedding` --[t_interpolate_and_continue {target: "global_isometric_embedding"}]--> output: `s_nash_embedding_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_interpolate_and_continue

---

### Preissmann's theorem (cite: https://en.wikipedia.org/wiki/Preissmann%27s_theorem)

**Axioms:** `s_riemannian_metric`, `s_compact_smooth_manifold`
**Terminal:** `s_preissmann_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_compact_smooth_manifold⟩` --[t_axiomatize_from_instances {property: "negative_sectional_curvature"}]--> output: `s_compact_negatively_curved_manifold`
2. input: `s_compact_negatively_curved_manifold` --[t_auxiliary_construction {object: "fundamental_group_action_on_universal_cover"}]--> output: `s_pi1_action_on_Cartan_Hadamard_space`
3. input: `s_pi1_action_on_Cartan_Hadamard_space` --[t_reductio_ad_absurdum {assume: "abelian_subgroup_of_rank_2"}]--> output: `s_flat_strip_contradiction`
4. input: `s_flat_strip_contradiction` --[t_structural_isomorphism {target: "every_abelian_subgroup_cyclic"}]--> output: `s_preissmann_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_reductio_ad_absurdum, t_structural_isomorphism

---

### Mostow rigidity theorem (cite: https://en.wikipedia.org/wiki/Mostow_rigidity_theorem)

**Axioms:** `s_riemannian_metric`, `s_compact_smooth_manifold`
**Terminal:** `s_mostow_rigidity_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_compact_smooth_manifold⟩` --[t_axiomatize_from_instances {property: "finite_volume_hyperbolic_dim_geq_3"}]--> output: `s_finite_volume_hyperbolic_manifold`
2. input: `s_finite_volume_hyperbolic_manifold` --[t_auxiliary_construction {object: "boundary_extension_of_quasi_isometry"}]--> output: `s_quasiconformal_boundary_map`
3. input: `s_quasiconformal_boundary_map` --[t_ergodic_correspondence {use: "ergodicity_of_geodesic_flow"}]--> output: `s_boundary_map_is_conformal`
4. input: `s_boundary_map_is_conformal` --[t_structural_isomorphism {target: "isometry_of_hyperbolic_manifolds"}]--> output: `s_mostow_rigidity_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_ergodic_correspondence, t_structural_isomorphism

---

### Chern–Gauss–Bonnet theorem (cite: https://en.wikipedia.org/wiki/Chern%E2%80%93Gauss%E2%80%93Bonnet_theorem)

**Axioms:** `s_riemannian_metric`, `s_compact_smooth_manifold`
**Terminal:** `s_chern_gauss_bonnet` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_compact_smooth_manifold⟩` --[t_auxiliary_construction {object: "Pfaffian_of_curvature_2_form"}]--> output: `s_pfaffian_form_on_M`
2. input: `s_pfaffian_form_on_M` --[t_obstruction_class {target: "Euler_class_of_tangent_bundle"}]--> output: `s_euler_class_representative`
3. input: `s_euler_class_representative` --[t_analysis_algebra_topology_bridge {bridge: "Chern_Weil_homomorphism"}]--> output: `s_integral_equals_topological_euler_char`
4. input: `s_integral_equals_topological_euler_char` --[t_structural_isomorphism {target: "Chern_Gauss_Bonnet_identity"}]--> output: `s_chern_gauss_bonnet`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_analysis_algebra_topology_bridge, t_structural_isomorphism

---

### Hodge decomposition theorem (cite: https://en.wikipedia.org/wiki/Hodge_theory)

**Axioms:** `s_riemannian_metric`, `s_compact_smooth_manifold`
**Terminal:** `s_hodge_decomposition` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_compact_smooth_manifold⟩` --[t_auxiliary_construction {object: "Laplace_Beltrami_on_p_forms"}]--> output: `s_hodge_laplacian`
2. input: `s_hodge_laplacian` --[t_svd_and_spectral_decomposition {operator: "self_adjoint_elliptic_Laplacian"}]--> output: `s_eigenform_orthogonal_decomp`
3. input: `s_eigenform_orthogonal_decomp` --[t_projection_to_subspace {target: "harmonic_kernel"}]--> output: `s_orthogonal_decomp_im_d_im_dstar_harmonic`
4. input: `s_orthogonal_decomp_im_d_im_dstar_harmonic` --[t_structural_isomorphism {target: "harmonic_forms_iso_de_Rham_cohomology"}]--> output: `s_hodge_decomposition`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_projection_to_subspace, t_structural_isomorphism

---

### De Rham theorem (cite: https://en.wikipedia.org/wiki/De_Rham%27s_theorem)

**Axioms:** `s_smooth_manifold`, `s_differential_form`
**Terminal:** `s_de_rham_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold, s_differential_form⟩` --[t_auxiliary_construction {object: "de_Rham_complex_and_singular_cochain_complex"}]--> output: `s_two_cochain_complexes`
2. input: `s_two_cochain_complexes` --[t_sheafify_on_grothendieck_topology {target: "good_cover_Cech_resolution"}]--> output: `s_cech_de_rham_double_complex`
3. input: `s_cech_de_rham_double_complex` --[t_analysis_algebra_topology_bridge {bridge: "integration_pairing_via_Stokes"}]--> output: `s_de_rham_isomorphism`
4. input: `s_de_rham_isomorphism` --[t_structural_isomorphism {target: "ring_iso_with_singular_cohomology"}]--> output: `s_de_rham_theorem`

**Techniques used:** t_auxiliary_construction, t_sheafify_on_grothendieck_topology, t_analysis_algebra_topology_bridge, t_structural_isomorphism

---

### Frobenius theorem (integrable distributions) (cite: https://en.wikipedia.org/wiki/Frobenius_theorem_(differential_topology))

**Axioms:** `s_smooth_manifold`, `s_smooth_function`
**Terminal:** `s_frobenius_integrability` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold, s_smooth_function⟩` --[t_auxiliary_construction {object: "smooth_distribution_D_subset_TM"}]--> output: `s_smooth_distribution`
2. input: `s_smooth_distribution` --[t_axiomatize_from_instances {property: "involutivity_[X,Y]_in_D"}]--> output: `s_involutive_distribution`
3. input: `s_involutive_distribution` --[t_contraction_fixed_point {scheme: "flow_box_simultaneous_rectification"}]--> output: `s_local_foliation_chart`
4. input: `s_local_foliation_chart` --[t_structural_isomorphism {target: "global_foliation_through_each_point"}]--> output: `s_frobenius_integrability`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_contraction_fixed_point, t_structural_isomorphism

---

### Sard's theorem (cite: https://en.wikipedia.org/wiki/Sard%27s_theorem)

**Axioms:** `s_smooth_manifold`, `s_smooth_function`
**Terminal:** `s_sard_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold, s_smooth_function⟩` --[t_auxiliary_construction {object: "critical_set_of_smooth_map"}]--> output: `s_critical_set_C_of_f`
2. input: `s_critical_set_C_of_f` --[t_exhaustion_squeeze {use: "Taylor_expansion_cube_cover"}]--> output: `s_measure_bound_on_f_C`
3. input: `s_critical_set_C_of_f` --[t_compactness_argument {use: "stratify_by_order_of_vanishing"}]--> output: `s_stratified_critical_set`
4. input: `⟨s_measure_bound_on_f_C, s_stratified_critical_set⟩` --[t_structural_isomorphism {target: "image_of_critical_points_has_measure_zero"}]--> output: `s_sard_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_compactness_argument, t_structural_isomorphism

---

### Generalized Stokes theorem (cite: https://en.wikipedia.org/wiki/Generalized_Stokes_theorem)

**Axioms:** `s_smooth_manifold_with_boundary`, `s_differential_form`
**Terminal:** `s_generalized_stokes_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold_with_boundary, s_differential_form⟩` --[t_verify_on_special_cases {cases: ["interval", "rectangle"]}]--> output: `s_FTC_and_Greens_theorem_special_cases`
2. input: `s_FTC_and_Greens_theorem_special_cases` --[t_axiomatize_from_instances {object: "exterior_derivative_d"}]--> output: `s_d_omega_in_local_coords`
3. input: `s_d_omega_in_local_coords` --[t_exhaustion_squeeze {use: "partition_of_unity_assembly"}]--> output: `s_local_to_global_integration_identity`
4. input: `s_local_to_global_integration_identity` --[t_structural_isomorphism {target: "integral_of_d_omega_equals_boundary_integral"}]--> output: `s_generalized_stokes_theorem`

**Techniques used:** t_verify_on_special_cases, t_axiomatize_from_instances, t_exhaustion_squeeze, t_structural_isomorphism

---

### Cartan formula for Lie derivative (cite: https://en.wikipedia.org/wiki/Cartan_formula)

**Axioms:** `s_smooth_manifold`, `s_differential_form`
**Terminal:** `s_cartan_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold, s_differential_form⟩` --[t_auxiliary_construction {operators: ["L_X", "d", "iota_X"]}]--> output: `s_three_derivations_on_omega_star`
2. input: `s_three_derivations_on_omega_star` --[t_verify_on_special_cases {forms: ["0_forms", "1_forms"]}]--> output: `s_cartan_identity_on_low_degree`
3. input: `s_cartan_identity_on_low_degree` --[t_interpolate_and_continue {target: "extend_by_derivation_property"}]--> output: `s_cartan_formula`

**Techniques used:** t_auxiliary_construction, t_verify_on_special_cases, t_interpolate_and_continue

---

### Uniformization theorem (cite: https://en.wikipedia.org/wiki/Uniformization_theorem)

**Axioms:** `s_compact_riemann_surface`, `s_riemannian_metric`
**Terminal:** `s_uniformization_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_riemann_surface, s_riemannian_metric⟩` --[t_auxiliary_construction {object: "universal_cover_with_pulled_back_complex_structure"}]--> output: `s_simply_connected_riemann_surface`
2. input: `s_simply_connected_riemann_surface` --[t_physics_to_pde {pde: "uniformization_via_Liouville_PDE"}]--> output: `s_constant_curvature_metric_existence`
3. input: `s_constant_curvature_metric_existence` --[t_structural_isomorphism {target: "conformal_to_S2_C_or_disk"}]--> output: `s_uniformization_theorem`

**Techniques used:** t_auxiliary_construction, t_physics_to_pde, t_structural_isomorphism

---

### Fundamental theorem of curves (cite: https://en.wikipedia.org/wiki/Fundamental_theorem_of_curves)

**Axioms:** `s_smooth_function`, `s_euclidean_3_space`
**Terminal:** `s_fundamental_theorem_of_curves` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_function, s_euclidean_3_space⟩` --[t_auxiliary_construction {object: "Frenet_frame_along_curve"}]--> output: `s_frenet_frame_ODE`
2. input: `s_frenet_frame_ODE` --[t_contraction_fixed_point {scheme: "ODE_existence_uniqueness_Picard"}]--> output: `s_curve_recovered_from_kappa_tau`
3. input: `s_curve_recovered_from_kappa_tau` --[t_structural_isomorphism {target: "rigid_motion_uniqueness"}]--> output: `s_fundamental_theorem_of_curves`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_structural_isomorphism

---

### Four vertex theorem (cite: https://en.wikipedia.org/wiki/Four-vertex_theorem)

**Axioms:** `s_smooth_function`, `s_euclidean_plane`
**Terminal:** `s_four_vertex_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_function, s_euclidean_plane⟩` --[t_auxiliary_construction {object: "convex_simple_closed_curve_with_curvature_kappa"}]--> output: `s_smooth_convex_closed_curve`
2. input: `s_smooth_convex_closed_curve` --[t_reductio_ad_absurdum {assume: "fewer_than_four_critical_points_of_kappa"}]--> output: `s_kappa_prime_sign_change_contradiction`
3. input: `s_kappa_prime_sign_change_contradiction` --[t_conserved_quantity {invariant: "integral_of_kappa_prime_against_linear_functions"}]--> output: `s_four_vertex_theorem`

**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum, t_conserved_quantity

---

### Fenchel's theorem (cite: https://en.wikipedia.org/wiki/Fenchel%27s_theorem)

**Axioms:** `s_smooth_function`, `s_euclidean_3_space`
**Terminal:** `s_fenchel_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_function, s_euclidean_3_space⟩` --[t_auxiliary_construction {object: "tantrix_curve_on_unit_sphere"}]--> output: `s_tantrix_spherical_curve`
2. input: `s_tantrix_spherical_curve` --[t_conserved_quantity {invariant: "total_curvature_equals_length_of_tantrix"}]--> output: `s_total_curvature_equals_tantrix_length`
3. input: `s_total_curvature_equals_tantrix_length` --[t_exhaustion_squeeze {bound: "tantrix_not_in_hemisphere_implies_length_geq_2pi"}]--> output: `s_fenchel_theorem`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_exhaustion_squeeze

---

### Hilbert's theorem on hyperbolic plane (cite: https://en.wikipedia.org/wiki/Hilbert%27s_theorem_(differential_geometry))

**Axioms:** `s_smooth_surface_in_R3`, `s_gauss_curvature_K`
**Terminal:** `s_hilbert_no_isometric_immersion_hyperbolic_plane` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_surface_in_R3, s_gauss_curvature_K⟩` --[t_axiomatize_from_instances {property: "complete_constant_negative_curvature"}]--> output: `s_hyperbolic_plane_as_abstract_surface`
2. input: `s_hyperbolic_plane_as_abstract_surface` --[t_auxiliary_construction {object: "asymptotic_Tchebyshev_net"}]--> output: `s_chebyshev_net_with_angle_omega`
3. input: `s_chebyshev_net_with_angle_omega` --[t_physics_to_pde {pde: "sine_Gordon_omega_uv_equals_sin_omega"}]--> output: `s_sine_gordon_equation`
4. input: `s_sine_gordon_equation` --[t_reductio_ad_absurdum {derive: "area_bound_contradicts_completeness"}]--> output: `s_hilbert_no_isometric_immersion_hyperbolic_plane`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_physics_to_pde, t_reductio_ad_absurdum

---

### Bertrand–Diguet–Puiseux theorem (cite: https://en.wikipedia.org/wiki/Bertrand%E2%80%93Diguet%E2%80%93Puiseux_theorem)

**Axioms:** `s_smooth_surface_in_R3`, `s_gauss_curvature_K`
**Terminal:** `s_bertrand_diguet_puiseux` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_surface_in_R3, s_gauss_curvature_K⟩` --[t_auxiliary_construction {object: "geodesic_disk_of_radius_r_around_p"}]--> output: `s_geodesic_disk_circumference_C_r`
2. input: `s_geodesic_disk_circumference_C_r` --[t_interpolate_and_continue {target: "Taylor_expand_C_r_in_r"}]--> output: `s_taylor_expansion_of_circumference`
3. input: `s_taylor_expansion_of_circumference` --[t_structural_isomorphism {target: "curvature_as_local_metric_invariant"}]--> output: `s_bertrand_diguet_puiseux`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_structural_isomorphism

---

### Tennis ball theorem (cite: https://en.wikipedia.org/wiki/Tennis_ball_theorem)

**Axioms:** `s_smooth_surface_in_R3`, `s_topological_sphere_S2`
**Terminal:** `s_tennis_ball_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_surface_in_R3, s_topological_sphere_S2⟩` --[t_auxiliary_construction {object: "smooth_simple_closed_curve_bisecting_area"}]--> output: `s_area_bisecting_curve_on_sphere`
2. input: `s_area_bisecting_curve_on_sphere` --[t_conserved_quantity {invariant: "total_geodesic_curvature_zero"}]--> output: `s_zero_signed_geodesic_curvature_integral`
3. input: `s_zero_signed_geodesic_curvature_integral` --[t_pigeonhole_collision {target: "sign_change_count_geq_4"}]--> output: `s_tennis_ball_theorem`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_pigeonhole_collision

---

### Theorem of the three geodesics (cite: https://en.wikipedia.org/wiki/Theorem_of_the_three_geodesics)

**Axioms:** `s_riemannian_metric`, `s_topological_sphere_S2`
**Terminal:** `s_three_geodesics_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_topological_sphere_S2⟩` --[t_auxiliary_construction {object: "energy_functional_on_free_loop_space"}]--> output: `s_loop_space_energy_functional`
2. input: `s_loop_space_energy_functional` --[t_compactness_argument {use: "Lyusternik_Schnirelmann_min_max"}]--> output: `s_min_max_critical_values`
3. input: `s_min_max_critical_values` --[t_obstruction_class {target: "category_LS_of_loop_space_of_S2"}]--> output: `s_three_distinct_simple_closed_geodesics`
4. input: `s_three_distinct_simple_closed_geodesics` --[t_structural_isomorphism {target: "three_geodesics_existence"}]--> output: `s_three_geodesics_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_obstruction_class, t_structural_isomorphism

---

### Lyusternik–Fet theorem (cite: https://en.wikipedia.org/wiki/Lyusternik%E2%80%93Fet_theorem)

**Axioms:** `s_riemannian_metric`, `s_compact_smooth_manifold`
**Terminal:** `s_lyusternik_fet_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_compact_smooth_manifold⟩` --[t_auxiliary_construction {object: "energy_on_free_loop_space"}]--> output: `s_free_loop_space_energy`
2. input: `s_free_loop_space_energy` --[t_obstruction_class {target: "nontrivial_homotopy_of_loop_space"}]--> output: `s_nontrivial_loop_homotopy_class`
3. input: `s_nontrivial_loop_homotopy_class` --[t_compactness_argument {use: "Palais_Smale_minimax"}]--> output: `s_lyusternik_fet_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_compactness_argument

---

### Gage–Hamilton–Grayson theorem (cite: https://en.wikipedia.org/wiki/Curve-shortening_flow)

**Axioms:** `s_smooth_function`, `s_euclidean_plane`
**Terminal:** `s_gage_hamilton_grayson` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_function, s_euclidean_plane⟩` --[t_physics_to_pde {pde: "curve_shortening_flow_dgamma_dt_equals_kappa_N"}]--> output: `s_curve_shortening_flow_eqn`
2. input: `s_curve_shortening_flow_eqn` --[t_flow_with_surgery {control: "isoperimetric_pinching_estimate"}]--> output: `s_convexification_of_embedded_curve`
3. input: `s_convexification_of_embedded_curve` --[t_rescale_for_asymptotic_geometry {target: "blow_up_at_extinction_time"}]--> output: `s_round_point_limit`
4. input: `s_round_point_limit` --[t_structural_isomorphism {target: "shrinking_to_round_point"}]--> output: `s_gage_hamilton_grayson`

**Techniques used:** t_physics_to_pde, t_flow_with_surgery, t_rescale_for_asymptotic_geometry, t_structural_isomorphism

---

### Willmore conjecture (Marques–Neves) (cite: https://en.wikipedia.org/wiki/Willmore_conjecture)

**Axioms:** `s_smooth_surface_in_R3`, `s_riemannian_metric`
**Terminal:** `s_willmore_conjecture` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_surface_in_R3, s_riemannian_metric⟩` --[t_auxiliary_construction {object: "Willmore_energy_int_H2"}]--> output: `s_willmore_energy_functional`
2. input: `s_willmore_energy_functional` --[t_symmetry_reduction {use: "conformal_invariance_under_Mobius"}]--> output: `s_conformally_invariant_energy`
3. input: `s_conformally_invariant_energy` --[t_compactness_argument {use: "min_max_over_5_parameter_family"}]--> output: `s_min_max_widths_of_torus_class`
4. input: `s_min_max_widths_of_torus_class` --[t_structural_isomorphism {target: "Clifford_torus_minimizes_among_genus_1"}]--> output: `s_willmore_conjecture`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_compactness_argument, t_structural_isomorphism

---

### Bernstein's problem (cite: https://en.wikipedia.org/wiki/Bernstein%27s_problem)

**Axioms:** `s_smooth_function`, `s_euclidean_3_space`
**Terminal:** `s_bernstein_problem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_function, s_euclidean_3_space⟩` --[t_physics_to_pde {pde: "minimal_surface_eqn_div_grad_u_over_sqrt"}]--> output: `s_minimal_surface_equation`
2. input: `s_minimal_surface_equation` --[t_axiomatize_from_instances {property: "entire_solution_in_dim_n"}]--> output: `s_entire_minimal_graph_in_dim_n`
3. input: `s_entire_minimal_graph_in_dim_n` --[t_rescale_for_asymptotic_geometry {target: "tangent_cone_at_infinity"}]--> output: `s_tangent_cone_minimal_cone`
4. input: `s_tangent_cone_minimal_cone` --[t_finite_case_check {cases: "n_leq_7_only_planes; n_geq_8_Simons_cone"}]--> output: `s_bernstein_problem`

**Techniques used:** t_physics_to_pde, t_axiomatize_from_instances, t_rescale_for_asymptotic_geometry, t_finite_case_check

---

### Darboux's theorem (symplectic) (cite: https://en.wikipedia.org/wiki/Darboux%27s_theorem)

**Axioms:** `s_smooth_manifold`, `s_differential_form`
**Terminal:** `s_darboux_theorem_symplectic` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold, s_differential_form⟩` --[t_axiomatize_from_instances {property: "closed_nondegenerate_2_form_omega"}]--> output: `s_symplectic_form_omega`
2. input: `s_symplectic_form_omega` --[t_auxiliary_construction {object: "linear_normal_form_via_Gram_Schmidt"}]--> output: `s_linear_symplectic_basis_at_p`
3. input: `s_linear_symplectic_basis_at_p` --[t_contraction_fixed_point {scheme: "Moser_isotopy_trick"}]--> output: `s_local_diffeomorphism_to_standard_omega`
4. input: `s_local_diffeomorphism_to_standard_omega` --[t_structural_isomorphism {target: "local_normal_form_sum_dpi_dqi"}]--> output: `s_darboux_theorem_symplectic`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_contraction_fixed_point, t_structural_isomorphism

---

### Moser's trick (cite: https://en.wikipedia.org/wiki/Moser%27s_trick)

**Axioms:** `s_smooth_manifold`, `s_differential_form`
**Terminal:** `s_moser_trick_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold, s_differential_form⟩` --[t_auxiliary_construction {object: "path_of_volume_forms_omega_t"}]--> output: `s_homotopy_of_forms_omega_t`
2. input: `s_homotopy_of_forms_omega_t` --[t_physics_to_pde {pde: "time_dependent_vector_field_X_t_with_iota_X_omega_t_equals_alpha"}]--> output: `s_moser_vector_field_ODE`
3. input: `s_moser_vector_field_ODE` --[t_contraction_fixed_point {scheme: "integrate_flow_phi_t"}]--> output: `s_isotopy_phi_t`
4. input: `s_isotopy_phi_t` --[t_structural_isomorphism {target: "phi_1_pulls_back_omega_1_to_omega_0"}]--> output: `s_moser_trick_theorem`

**Techniques used:** t_auxiliary_construction, t_physics_to_pde, t_contraction_fixed_point, t_structural_isomorphism

---

### Weinstein neighbourhood theorem (cite: https://en.wikipedia.org/wiki/Weinstein_conjecture)

**Axioms:** `s_smooth_manifold`, `s_differential_form`
**Terminal:** `s_weinstein_neighbourhood` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold, s_differential_form⟩` --[t_auxiliary_construction {object: "Lagrangian_submanifold_L_in_M"}]--> output: `s_lagrangian_submanifold`
2. input: `s_lagrangian_submanifold` --[t_structural_isomorphism {target: "normal_bundle_iso_to_T*L"}]--> output: `s_normal_bundle_identification`
3. input: `s_normal_bundle_identification` --[t_contraction_fixed_point {scheme: "Moser_isotopy_on_neighbourhood"}]--> output: `s_local_symplectomorphism_to_T*L`
4. input: `s_local_symplectomorphism_to_T*L` --[t_structural_isomorphism {target: "tubular_neighbourhood_modeled_on_canonical"}]--> output: `s_weinstein_neighbourhood`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_contraction_fixed_point

---

### Gromov non-squeezing theorem (cite: https://en.wikipedia.org/wiki/Non-squeezing_theorem)

**Axioms:** `s_smooth_manifold`, `s_differential_form`
**Terminal:** `s_gromov_non_squeezing` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold, s_differential_form⟩` --[t_axiomatize_from_instances {property: "symplectic_embedding_ball_into_cylinder"}]--> output: `s_alleged_squeezing_phi_B_to_Z`
2. input: `s_alleged_squeezing_phi_B_to_Z` --[t_auxiliary_construction {object: "J_holomorphic_disk_through_phi_0"}]--> output: `s_j_holomorphic_disk_existence`
3. input: `s_j_holomorphic_disk_existence` --[t_conserved_quantity {invariant: "symplectic_area_lower_bound_pi_r2"}]--> output: `s_area_bound_pi_r2_leq_pi_R2`
4. input: `s_area_bound_pi_r2_leq_pi_R2` --[t_reductio_ad_absurdum {target: "r_leq_R"}]--> output: `s_gromov_non_squeezing`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_conserved_quantity, t_reductio_ad_absurdum

---

### Gromov compactness for J-holomorphic curves (cite: https://en.wikipedia.org/wiki/Pseudoholomorphic_curve)

**Axioms:** `s_smooth_manifold`, `s_differential_form`
**Terminal:** `s_gromov_compactness_j_holomorphic` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold, s_differential_form⟩` --[t_auxiliary_construction {object: "moduli_of_J_holomorphic_curves_bounded_energy"}]--> output: `s_moduli_bounded_energy_curves`
2. input: `s_moduli_bounded_energy_curves` --[t_rescale_for_asymptotic_geometry {target: "bubble_off_at_concentration_points"}]--> output: `s_bubble_tree_at_singular_points`
3. input: `s_bubble_tree_at_singular_points` --[t_compactness_argument {use: "elliptic_regularity_plus_removal_of_singularities"}]--> output: `s_compactified_moduli_of_stable_maps`
4. input: `s_compactified_moduli_of_stable_maps` --[t_structural_isomorphism {target: "Gromov_compactness_statement"}]--> output: `s_gromov_compactness_j_holomorphic`

**Techniques used:** t_auxiliary_construction, t_rescale_for_asymptotic_geometry, t_compactness_argument, t_structural_isomorphism

---

### Arnold conjecture (Floer) (cite: https://en.wikipedia.org/wiki/Arnold_conjecture)

**Axioms:** `s_compact_smooth_manifold`, `s_differential_form`
**Terminal:** `s_arnold_conjecture` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_differential_form⟩` --[t_auxiliary_construction {object: "Hamiltonian_isotopy_phi_H_with_fixed_points"}]--> output: `s_hamiltonian_diffeomorphism_phi_H`
2. input: `s_hamiltonian_diffeomorphism_phi_H` --[t_physics_to_pde {pde: "Floer_equation_du_ds_plus_J_du_dt_grad_H"}]--> output: `s_floer_pde_for_chords`
3. input: `s_floer_pde_for_chords` --[t_obstruction_class {target: "Floer_chain_complex_HF_star"}]--> output: `s_floer_homology_HF_M`
4. input: `s_floer_homology_HF_M` --[t_structural_isomorphism {target: "HF_iso_singular_cohomology"}]--> output: `s_fixed_point_count_geq_Betti_sum`
5. input: `s_fixed_point_count_geq_Betti_sum` --[t_compactness_argument {target: "Arnold_inequality"}]--> output: `s_arnold_conjecture`

**Techniques used:** t_auxiliary_construction, t_physics_to_pde, t_obstruction_class, t_structural_isomorphism, t_compactness_argument

---

### Delzant's theorem (cite: https://en.wikipedia.org/wiki/Delzant%27s_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_differential_form`
**Terminal:** `s_delzant_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_differential_form⟩` --[t_axiomatize_from_instances {property: "toric_symplectic_manifold_with_moment_map"}]--> output: `s_toric_symplectic_manifold`
2. input: `s_toric_symplectic_manifold` --[t_auxiliary_construction {object: "Delzant_polytope_image_of_moment_map"}]--> output: `s_delzant_polytope`
3. input: `s_delzant_polytope` --[t_structural_isomorphism {target: "symplectic_reduction_recovers_M_from_polytope"}]--> output: `s_delzant_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism

---

### Duistermaat–Heckman formula (cite: https://en.wikipedia.org/wiki/Duistermaat%E2%80%93Heckman_formula)

**Axioms:** `s_compact_smooth_manifold`, `s_differential_form`
**Terminal:** `s_duistermaat_heckman` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_differential_form⟩` --[t_axiomatize_from_instances {property: "Hamiltonian_S1_action_with_moment_H"}]--> output: `s_hamiltonian_circle_action`
2. input: `s_hamiltonian_circle_action` --[t_symmetry_reduction {use: "equivariant_cohomology_localization"}]--> output: `s_atiyah_bott_localization_formula`
3. input: `s_atiyah_bott_localization_formula` --[t_structural_isomorphism {target: "stationary_phase_exact_DH_formula"}]--> output: `s_duistermaat_heckman`

**Techniques used:** t_axiomatize_from_instances, t_symmetry_reduction, t_structural_isomorphism

---

### Eliashberg classification of contact 3-manifolds (cite: https://en.wikipedia.org/wiki/Contact_geometry)

**Axioms:** `s_closed_3_manifold`, `s_differential_form`
**Terminal:** `s_eliashberg_contact_3_classification` (kind: theorem)

**Steps:**
1. input: `⟨s_closed_3_manifold, s_differential_form⟩` --[t_axiomatize_from_instances {property: "tight_vs_overtwisted_contact_structure"}]--> output: `s_tight_overtwisted_dichotomy`
2. input: `s_tight_overtwisted_dichotomy` --[t_auxiliary_construction {object: "overtwisted_disk_obstruction"}]--> output: `s_overtwisted_disk_class`
3. input: `s_overtwisted_disk_class` --[t_obstruction_class {target: "homotopy_class_of_plane_field_invariant"}]--> output: `s_h_principle_classification_of_overtwisted`
4. input: `s_h_principle_classification_of_overtwisted` --[t_structural_isomorphism {target: "overtwisted_iso_homotopy_classes_of_plane_fields"}]--> output: `s_eliashberg_contact_3_classification`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_obstruction_class, t_structural_isomorphism

---

### Weinstein conjecture (3-dim, Taubes) (cite: https://en.wikipedia.org/wiki/Weinstein_conjecture)

**Axioms:** `s_closed_3_manifold`, `s_differential_form`
**Terminal:** `s_weinstein_conjecture_3d` (kind: theorem)

**Steps:**
1. input: `⟨s_closed_3_manifold, s_differential_form⟩` --[t_auxiliary_construction {object: "Reeb_vector_field_R_alpha"}]--> output: `s_reeb_vector_field`
2. input: `s_reeb_vector_field` --[t_analysis_algebra_topology_bridge {bridge: "Seiberg_Witten_solutions_imply_closed_Reeb_orbit"}]--> output: `s_sw_to_closed_reeb_orbit`
3. input: `s_sw_to_closed_reeb_orbit` --[t_obstruction_class {target: "nonvanishing_SW_for_contact_3_manifold"}]--> output: `s_existence_of_closed_reeb_orbit`
4. input: `s_existence_of_closed_reeb_orbit` --[t_structural_isomorphism {target: "Weinstein_conjecture_statement"}]--> output: `s_weinstein_conjecture_3d`

**Techniques used:** t_auxiliary_construction, t_analysis_algebra_topology_bridge, t_obstruction_class, t_structural_isomorphism

---

### Conley conjecture (cite: https://en.wikipedia.org/wiki/Conley_conjecture)

**Axioms:** `s_compact_smooth_manifold`, `s_differential_form`
**Terminal:** `s_conley_conjecture` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_differential_form⟩` --[t_axiomatize_from_instances {property: "symplectically_aspherical_M"}]--> output: `s_aspherical_symplectic_manifold`
2. input: `s_aspherical_symplectic_manifold` --[t_auxiliary_construction {object: "Hamiltonian_phi_with_finitely_many_periodic_orbits"}]--> output: `s_hypothetical_finite_periodic_phi`
3. input: `s_hypothetical_finite_periodic_phi` --[t_obstruction_class {target: "filtered_Floer_homology_with_local_invariants"}]--> output: `s_local_floer_homology_obstruction`
4. input: `s_local_floer_homology_obstruction` --[t_reductio_ad_absurdum {target: "infinitely_many_periodic_orbits"}]--> output: `s_conley_conjecture`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_obstruction_class, t_reductio_ad_absurdum

---

### Lagrangian intersection theorem (Floer) (cite: https://en.wikipedia.org/wiki/Floer_homology)

**Axioms:** `s_compact_smooth_manifold`, `s_differential_form`
**Terminal:** `s_lagrangian_intersection_floer` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_differential_form⟩` --[t_auxiliary_construction {object: "pair_of_Hamiltonian_isotopic_Lagrangians_L0_L1"}]--> output: `s_lagrangian_pair_L0_L1`
2. input: `s_lagrangian_pair_L0_L1` --[t_physics_to_pde {pde: "Floer_strip_equation"}]--> output: `s_floer_strips_between_L0_L1`
3. input: `s_floer_strips_between_L0_L1` --[t_obstruction_class {target: "Lagrangian_Floer_homology_HF_L0_L1"}]--> output: `s_lagrangian_floer_homology`
4. input: `s_lagrangian_floer_homology` --[t_structural_isomorphism {target: "rank_HF_iso_H_star_L_yields_intersection_bound"}]--> output: `s_lagrangian_intersection_floer`

**Techniques used:** t_auxiliary_construction, t_physics_to_pde, t_obstruction_class, t_structural_isomorphism

---

### Carathéodory–Jacobi–Lie theorem (cite: https://en.wikipedia.org/wiki/Carath%C3%A9odory%E2%80%93Jacobi%E2%80%93Lie_theorem)

**Axioms:** `s_smooth_manifold`, `s_differential_form`
**Terminal:** `s_caratheodory_jacobi_lie` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold, s_differential_form⟩` --[t_axiomatize_from_instances {property: "functions_with_pairwise_vanishing_Poisson_brackets"}]--> output: `s_involutive_function_system`
2. input: `s_involutive_function_system` --[t_auxiliary_construction {object: "Hamiltonian_flows_X_fi"}]--> output: `s_commuting_hamiltonian_flows`
3. input: `s_commuting_hamiltonian_flows` --[t_structural_isomorphism {target: "complete_to_local_Darboux_coordinates"}]--> output: `s_caratheodory_jacobi_lie`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism

---

### Liouville–Arnold integrability theorem (cite: https://en.wikipedia.org/wiki/Liouville%E2%80%93Arnold_theorem)

**Axioms:** `s_smooth_manifold`, `s_differential_form`
**Terminal:** `s_liouville_arnold` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold, s_differential_form⟩` --[t_axiomatize_from_instances {property: "n_independent_Poisson_commuting_integrals"}]--> output: `s_completely_integrable_hamiltonian_system`
2. input: `s_completely_integrable_hamiltonian_system` --[t_conserved_quantity {invariant: "level_set_F_inverse_c"}]--> output: `s_compact_connected_level_set`
3. input: `s_compact_connected_level_set` --[t_structural_isomorphism {target: "level_set_diffeomorphic_to_torus_T^n"}]--> output: `s_lagrangian_torus_fibration`
4. input: `s_lagrangian_torus_fibration` --[t_reduce_to_canonical_form {form: "action_angle_variables"}]--> output: `s_liouville_arnold`

**Techniques used:** t_axiomatize_from_instances, t_conserved_quantity, t_structural_isomorphism, t_reduce_to_canonical_form

---

### Marsden–Weinstein symplectic reduction (cite: https://en.wikipedia.org/wiki/Symplectic_reduction)

**Axioms:** `s_smooth_manifold`, `s_differential_form`
**Terminal:** `s_marsden_weinstein_reduction` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold, s_differential_form⟩` --[t_axiomatize_from_instances {property: "Hamiltonian_G_action_with_moment_map_mu"}]--> output: `s_hamiltonian_G_action_with_mu`
2. input: `s_hamiltonian_G_action_with_mu` --[t_projection_to_subspace {target: "level_set_mu_inverse_0"}]--> output: `s_zero_level_set_mu`
3. input: `s_zero_level_set_mu` --[t_symmetry_reduction {target: "quotient_by_G"}]--> output: `s_reduced_space_M_sslash_G`
4. input: `s_reduced_space_M_sslash_G` --[t_structural_isomorphism {target: "induced_symplectic_form_on_quotient"}]--> output: `s_marsden_weinstein_reduction`

**Techniques used:** t_axiomatize_from_instances, t_projection_to_subspace, t_symmetry_reduction, t_structural_isomorphism

---

### Atiyah–Guillemin–Sternberg convexity theorem (cite: https://en.wikipedia.org/wiki/Convexity_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_differential_form`
**Terminal:** `s_atiyah_guillemin_sternberg` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_differential_form⟩` --[t_axiomatize_from_instances {property: "Hamiltonian_T^k_action_with_moment_mu"}]--> output: `s_compact_torus_hamiltonian_action`
2. input: `s_compact_torus_hamiltonian_action` --[t_conserved_quantity {invariant: "fibers_of_mu_connected"}]--> output: `s_connected_fibers_of_moment_map`
3. input: `s_connected_fibers_of_moment_map` --[t_structural_isomorphism {target: "image_is_convex_polytope_=_convex_hull_of_fixed_points"}]--> output: `s_atiyah_guillemin_sternberg`

**Techniques used:** t_axiomatize_from_instances, t_conserved_quantity, t_structural_isomorphism

---

### Newlander–Nirenberg theorem (cite: https://en.wikipedia.org/wiki/Newlander%E2%80%93Nirenberg_theorem)

**Axioms:** `s_smooth_manifold`, `s_smooth_function`
**Terminal:** `s_newlander_nirenberg` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold, s_smooth_function⟩` --[t_axiomatize_from_instances {property: "almost_complex_structure_J_with_J2_minus_I"}]--> output: `s_almost_complex_structure`
2. input: `s_almost_complex_structure` --[t_auxiliary_construction {object: "Nijenhuis_tensor_N_J"}]--> output: `s_nijenhuis_obstruction`
3. input: `s_nijenhuis_obstruction` --[t_physics_to_pde {pde: "dbar_J_system_of_PDEs"}]--> output: `s_dbar_system_solvability`
4. input: `s_dbar_system_solvability` --[t_structural_isomorphism {target: "integrable_iff_holomorphic_chart_exists"}]--> output: `s_newlander_nirenberg`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_physics_to_pde, t_structural_isomorphism

---

### Hodge decomposition for compact Kähler manifolds (cite: https://en.wikipedia.org/wiki/K%C3%A4hler_manifold)

**Axioms:** `s_compact_smooth_manifold`, `s_riemannian_metric`
**Terminal:** `s_kahler_hodge_decomposition` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_riemannian_metric⟩` --[t_axiomatize_from_instances {property: "Kahler_metric_g_compatible_with_J_omega"}]--> output: `s_kahler_manifold`
2. input: `s_kahler_manifold` --[t_auxiliary_construction {object: "Kahler_identities_relating_Laplacians"}]--> output: `s_kahler_identities`
3. input: `s_kahler_identities` --[t_svd_and_spectral_decomposition {operator: "Hodge_Laplacian_equals_2_Laplacian_dbar"}]--> output: `s_p_q_decomposition_of_harmonic_forms`
4. input: `s_p_q_decomposition_of_harmonic_forms` --[t_structural_isomorphism {target: "H^k_iso_oplus_H^p_q_with_complex_conjugation_symmetry"}]--> output: `s_kahler_hodge_decomposition`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_svd_and_spectral_decomposition, t_structural_isomorphism

---

### Kodaira embedding theorem (cite: https://en.wikipedia.org/wiki/Kodaira_embedding_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_riemannian_metric`
**Terminal:** `s_kodaira_embedding` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_riemannian_metric⟩` --[t_axiomatize_from_instances {property: "compact_Kahler_with_positive_line_bundle_L"}]--> output: `s_hodge_manifold`
2. input: `s_hodge_manifold` --[t_auxiliary_construction {object: "sections_of_L^k_for_large_k"}]--> output: `s_sections_of_high_tensor_power`
3. input: `s_sections_of_high_tensor_power` --[t_sheaf_cohomology_bridge {target: "Kodaira_vanishing_to_get_enough_sections"}]--> output: `s_base_point_free_separating_jets`
4. input: `s_base_point_free_separating_jets` --[t_structural_isomorphism {target: "embedding_into_PN_via_sections"}]--> output: `s_kodaira_embedding`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_sheaf_cohomology_bridge, t_structural_isomorphism

---

### Kodaira vanishing theorem (cite: https://en.wikipedia.org/wiki/Kodaira_vanishing_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_riemannian_metric`
**Terminal:** `s_kodaira_vanishing` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_riemannian_metric⟩` --[t_axiomatize_from_instances {property: "positive_holomorphic_line_bundle_L_on_Kahler_X"}]--> output: `s_positive_line_bundle_L`
2. input: `s_positive_line_bundle_L` --[t_auxiliary_construction {object: "Bochner_Kodaira_Nakano_identity"}]--> output: `s_bochner_kodaira_identity`
3. input: `s_bochner_kodaira_identity` --[t_conserved_quantity {invariant: "positive_curvature_term_in_Weitzenbock"}]--> output: `s_pointwise_positivity_of_curvature_operator`
4. input: `s_pointwise_positivity_of_curvature_operator` --[t_structural_isomorphism {target: "Hp_q_K_X_otimes_L_vanish_for_p_plus_q_gt_n"}]--> output: `s_kodaira_vanishing`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_conserved_quantity, t_structural_isomorphism

---

### Akizuki–Nakano vanishing theorem (cite: https://en.wikipedia.org/wiki/Kodaira_vanishing_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_riemannian_metric`
**Terminal:** `s_akizuki_nakano` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_riemannian_metric⟩` --[t_auxiliary_construction {object: "Bochner_Kodaira_Nakano_extended_to_Omega^p"}]--> output: `s_bochner_kodaira_nakano_identity_extended`
2. input: `s_bochner_kodaira_nakano_identity_extended` --[t_conserved_quantity {invariant: "curvature_pairing_positivity"}]--> output: `s_positive_curvature_pairing_on_p_q_forms`
3. input: `s_positive_curvature_pairing_on_p_q_forms` --[t_structural_isomorphism {target: "H_q_X_Omega_p_otimes_L_vanish_for_p_plus_q_gt_n"}]--> output: `s_akizuki_nakano`

**Techniques used:** t_auxiliary_construction, t_conserved_quantity, t_structural_isomorphism

---

### Calabi conjecture (Yau's theorem) (cite: https://en.wikipedia.org/wiki/Calabi_conjecture)

**Axioms:** `s_compact_smooth_manifold`, `s_riemannian_metric`
**Terminal:** `s_yau_calabi` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_riemannian_metric⟩` --[t_axiomatize_from_instances {property: "compact_Kahler_X_with_prescribed_volume_form"}]--> output: `s_kahler_class_with_target_Ricci`
2. input: `s_kahler_class_with_target_Ricci` --[t_physics_to_pde {pde: "complex_Monge_Ampere_log_det_g_plus_phi_equals_f"}]--> output: `s_complex_monge_ampere_pde`
3. input: `s_complex_monge_ampere_pde` --[t_contraction_fixed_point {scheme: "continuity_method_with_C2_estimates"}]--> output: `s_unique_smooth_solution_phi`
4. input: `s_unique_smooth_solution_phi` --[t_structural_isomorphism {target: "Ricci_form_prescribed_arbitrarily_in_c1"}]--> output: `s_yau_calabi`

**Techniques used:** t_axiomatize_from_instances, t_physics_to_pde, t_contraction_fixed_point, t_structural_isomorphism

---

### Aubin–Yau theorem (negative curvature Kähler–Einstein) (cite: https://en.wikipedia.org/wiki/K%C3%A4hler%E2%80%93Einstein_metric)

**Axioms:** `s_compact_smooth_manifold`, `s_riemannian_metric`
**Terminal:** `s_aubin_yau_KE` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_riemannian_metric⟩` --[t_axiomatize_from_instances {property: "compact_Kahler_with_c1_X_negative"}]--> output: `s_kahler_manifold_with_negative_c1`
2. input: `s_kahler_manifold_with_negative_c1` --[t_physics_to_pde {pde: "Monge_Ampere_with_minus_phi_term"}]--> output: `s_monge_ampere_negative_c1`
3. input: `s_monge_ampere_negative_c1` --[t_contraction_fixed_point {scheme: "maximum_principle_yields_C0_bound"}]--> output: `s_a_priori_estimates_for_KE_metric`
4. input: `s_a_priori_estimates_for_KE_metric` --[t_structural_isomorphism {target: "unique_Kahler_Einstein_metric_in_class"}]--> output: `s_aubin_yau_KE`

**Techniques used:** t_axiomatize_from_instances, t_physics_to_pde, t_contraction_fixed_point, t_structural_isomorphism

---

### Donaldson–Uhlenbeck–Yau theorem (cite: https://en.wikipedia.org/wiki/Donaldson%E2%80%93Uhlenbeck%E2%80%93Yau_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_riemannian_metric`
**Terminal:** `s_donaldson_uhlenbeck_yau` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_riemannian_metric⟩` --[t_axiomatize_from_instances {property: "stable_holomorphic_vector_bundle_E"}]--> output: `s_stable_holomorphic_bundle`
2. input: `s_stable_holomorphic_bundle` --[t_physics_to_pde {pde: "Hermitian_Yang_Mills_equation"}]--> output: `s_hermitian_yang_mills_eqn`
3. input: `s_hermitian_yang_mills_eqn` --[t_contraction_fixed_point {scheme: "heat_flow_on_metrics_with_Donaldson_functional"}]--> output: `s_long_time_existence_of_metric_flow`
4. input: `s_long_time_existence_of_metric_flow` --[t_structural_isomorphism {target: "stability_iff_HYM_metric_exists"}]--> output: `s_donaldson_uhlenbeck_yau`

**Techniques used:** t_axiomatize_from_instances, t_physics_to_pde, t_contraction_fixed_point, t_structural_isomorphism

---

### Donaldson's diagonalizability theorem (cite: https://en.wikipedia.org/wiki/Donaldson%27s_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_differential_form`
**Terminal:** `s_donaldson_diagonalizability` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_differential_form⟩` --[t_axiomatize_from_instances {property: "simply_connected_smooth_4_manifold_definite_form"}]--> output: `s_simply_connected_4_manifold_definite_intersection`
2. input: `s_simply_connected_4_manifold_definite_intersection` --[t_auxiliary_construction {object: "moduli_space_of_ASD_SU2_instantons"}]--> output: `s_asd_moduli_space`
3. input: `s_asd_moduli_space` --[t_obstruction_class {target: "cobordism_M_to_disjoint_CP2"}]--> output: `s_cobordism_via_moduli_endpoints`
4. input: `s_cobordism_via_moduli_endpoints` --[t_structural_isomorphism {target: "intersection_form_diagonal_over_Z"}]--> output: `s_donaldson_diagonalizability`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_obstruction_class, t_structural_isomorphism

---

### Seiberg–Witten invariants (cite: https://en.wikipedia.org/wiki/Seiberg%E2%80%93Witten_invariants)

**Axioms:** `s_compact_smooth_manifold`, `s_differential_form`
**Terminal:** `s_seiberg_witten_invariants` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_differential_form⟩` --[t_axiomatize_from_instances {property: "4_manifold_with_spin_c_structure"}]--> output: `s_spin_c_4_manifold`
2. input: `s_spin_c_4_manifold` --[t_physics_to_pde {pde: "Seiberg_Witten_monopole_equations"}]--> output: `s_sw_equations`
3. input: `s_sw_equations` --[t_compactness_argument {use: "moduli_compact_via_a_priori_C0_bound"}]--> output: `s_compact_sw_moduli_space`
4. input: `s_compact_sw_moduli_space` --[t_obstruction_class {target: "signed_count_yielding_SW_invariant"}]--> output: `s_seiberg_witten_invariants`

**Techniques used:** t_axiomatize_from_instances, t_physics_to_pde, t_compactness_argument, t_obstruction_class

---

### Hironaka resolution of singularities (cite: https://en.wikipedia.org/wiki/Resolution_of_singularities)

**Axioms:** `s_algebraically_closed_field_k`, `s_polynomial_ring_in_n_vars`
**Terminal:** `s_hironaka_resolution` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_polynomial_ring_in_n_vars⟩` --[t_axiomatize_from_instances {property: "variety_X_over_field_of_char_0"}]--> output: `s_variety_in_char_zero`
2. input: `s_variety_in_char_zero` --[t_auxiliary_construction {object: "blow_up_along_smooth_center_of_max_singularity"}]--> output: `s_blow_up_X_along_Z`
3. input: `s_blow_up_X_along_Z` --[t_infinite_descent {invariant: "Hironaka_order_function_drops"}]--> output: `s_terminating_blow_up_sequence`
4. input: `s_terminating_blow_up_sequence` --[t_structural_isomorphism {target: "smooth_variety_X_tilde_birational_to_X"}]--> output: `s_hironaka_resolution`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_infinite_descent, t_structural_isomorphism

---

### Bertini's theorem on smoothness (cite: https://en.wikipedia.org/wiki/Bertini%27s_theorem)

**Axioms:** `s_algebraically_closed_field_k`, `s_polynomial_ring_in_n_vars`
**Terminal:** `s_bertini_smoothness` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_polynomial_ring_in_n_vars⟩` --[t_axiomatize_from_instances {property: "smooth_quasi_projective_X_in_PN"}]--> output: `s_smooth_subvariety_in_PN`
2. input: `s_smooth_subvariety_in_PN` --[t_auxiliary_construction {object: "linear_system_of_hyperplanes_parametrized_by_dual_PN"}]--> output: `s_hyperplane_family_in_dual_PN`
3. input: `s_hyperplane_family_in_dual_PN` --[t_probabilistic_existence {target: "generic_hyperplane_avoids_singularities"}]--> output: `s_generic_H_meets_X_transversely`
4. input: `s_generic_H_meets_X_transversely` --[t_structural_isomorphism {target: "general_hyperplane_section_smooth"}]--> output: `s_bertini_smoothness`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_probabilistic_existence, t_structural_isomorphism

---

### Bertini irreducibility theorem (cite: https://en.wikipedia.org/wiki/Bertini%27s_theorem)

**Axioms:** `s_algebraically_closed_field_k`, `s_polynomial_ring_in_n_vars`
**Terminal:** `s_bertini_irreducibility` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_polynomial_ring_in_n_vars⟩` --[t_axiomatize_from_instances {property: "irreducible_X_dim_geq_2_in_PN"}]--> output: `s_irreducible_variety_dim_ge_2`
2. input: `s_irreducible_variety_dim_ge_2` --[t_auxiliary_construction {object: "incidence_variety_X_cap_H"}]--> output: `s_incidence_variety_construction`
3. input: `s_incidence_variety_construction` --[t_compactness_argument {use: "Zariski_connectedness_of_generic_fiber"}]--> output: `s_generic_section_connected`
4. input: `s_generic_section_connected` --[t_structural_isomorphism {target: "generic_hyperplane_section_irreducible"}]--> output: `s_bertini_irreducibility`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_compactness_argument, t_structural_isomorphism

---

### Bezout's theorem (cite: https://en.wikipedia.org/wiki/B%C3%A9zout%27s_theorem)

**Axioms:** `s_algebraically_closed_field_k`, `s_polynomial_ring_in_n_vars`
**Terminal:** `s_bezout_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_polynomial_ring_in_n_vars⟩` --[t_axiomatize_from_instances {property: "two_curves_in_PP2_degrees_m_n"}]--> output: `s_two_projective_curves_with_degrees`
2. input: `s_two_projective_curves_with_degrees` --[t_auxiliary_construction {object: "intersection_with_multiplicity_via_local_ring"}]--> output: `s_intersection_multiplicity_sum`
3. input: `s_intersection_multiplicity_sum` --[t_conserved_quantity {invariant: "degree_in_Chow_ring_of_PP2"}]--> output: `s_degree_count_equals_mn`
4. input: `s_degree_count_equals_mn` --[t_structural_isomorphism {target: "Bezout_count_mn_intersections"}]--> output: `s_bezout_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_conserved_quantity, t_structural_isomorphism

---

### Riemann–Roch theorem for surfaces (cite: https://en.wikipedia.org/wiki/Riemann%E2%80%93Roch_theorem_for_surfaces)

**Axioms:** `s_algebraically_closed_field_k`, `s_compact_riemann_surface`
**Terminal:** `s_riemann_roch_surfaces` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_compact_riemann_surface⟩` --[t_axiomatize_from_instances {property: "smooth_projective_surface_S_with_divisor_D"}]--> output: `s_smooth_projective_surface_with_divisor`
2. input: `s_smooth_projective_surface_with_divisor` --[t_auxiliary_construction {object: "Euler_characteristic_chi_O_D"}]--> output: `s_euler_characteristic_of_O_D`
3. input: `s_euler_characteristic_of_O_D` --[t_sheaf_cohomology_bridge {target: "intersection_pairing_with_K_S"}]--> output: `s_intersection_with_canonical_class`
4. input: `s_intersection_with_canonical_class` --[t_structural_isomorphism {target: "chi_O_D_equals_D(D-K)/2_plus_chi_O_S"}]--> output: `s_riemann_roch_surfaces`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_sheaf_cohomology_bridge, t_structural_isomorphism

---

### Hirzebruch–Riemann–Roch theorem (cite: https://en.wikipedia.org/wiki/Hirzebruch%E2%80%93Riemann%E2%80%93Roch_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_compact_riemann_surface`
**Terminal:** `s_hirzebruch_riemann_roch` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_compact_riemann_surface⟩` --[t_axiomatize_from_instances {property: "holomorphic_vector_bundle_E_on_compact_complex_X"}]--> output: `s_holomorphic_bundle_on_X`
2. input: `s_holomorphic_bundle_on_X` --[t_auxiliary_construction {object: "Chern_character_ch_E_and_Todd_class_td_X"}]--> output: `s_ch_and_todd_classes`
3. input: `s_ch_and_todd_classes` --[t_k_theoretic_index_bridge {target: "index_of_dbar_E_via_Atiyah_Singer"}]--> output: `s_index_of_dbar_operator`
4. input: `s_index_of_dbar_operator` --[t_structural_isomorphism {target: "chi_E_equals_integral_ch_E_td_X"}]--> output: `s_hirzebruch_riemann_roch`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_k_theoretic_index_bridge, t_structural_isomorphism

---

### Grothendieck–Riemann–Roch theorem (cite: https://en.wikipedia.org/wiki/Grothendieck%E2%80%93Riemann%E2%80%93Roch_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_algebraically_closed_field_k`
**Terminal:** `s_grothendieck_riemann_roch` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "proper_morphism_f_X_to_Y_of_smooth_varieties"}]--> output: `s_proper_morphism_f`
2. input: `s_proper_morphism_f` --[t_auxiliary_construction {object: "push_forward_in_K_theory_and_in_Chow"}]--> output: `s_two_push_forwards`
3. input: `s_two_push_forwards` --[t_k_theoretic_index_bridge {target: "compare_via_ch_and_Todd"}]--> output: `s_grr_relation_in_chow_groups`
4. input: `s_grr_relation_in_chow_groups` --[t_structural_isomorphism {target: "ch(f_!E)td(Y)=f_*(ch(E)td(X))"}]--> output: `s_grothendieck_riemann_roch`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_k_theoretic_index_bridge, t_structural_isomorphism

---

### Lefschetz hyperplane theorem (cite: https://en.wikipedia.org/wiki/Lefschetz_hyperplane_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_algebraically_closed_field_k`
**Terminal:** `s_lefschetz_hyperplane` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "smooth_projective_X_in_PN_with_hyperplane_section_Y"}]--> output: `s_smooth_projective_with_hyperplane_section`
2. input: `s_smooth_projective_with_hyperplane_section` --[t_auxiliary_construction {object: "Morse_function_via_distance_to_hyperplane"}]--> output: `s_morse_function_with_indices_geq_n`
3. input: `s_morse_function_with_indices_geq_n` --[t_obstruction_class {target: "cell_attachment_in_high_dimension_only"}]--> output: `s_Y_obtained_from_X_by_cells_of_dim_geq_n`
4. input: `s_Y_obtained_from_X_by_cells_of_dim_geq_n` --[t_structural_isomorphism {target: "H_k_Y_iso_H_k_X_for_k_lt_n-1"}]--> output: `s_lefschetz_hyperplane`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_obstruction_class, t_structural_isomorphism

---

### Hard Lefschetz theorem (cite: https://en.wikipedia.org/wiki/Lefschetz_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_differential_form`
**Terminal:** `s_hard_lefschetz` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_differential_form⟩` --[t_axiomatize_from_instances {property: "compact_Kahler_X_of_dim_n_with_Kahler_class_omega"}]--> output: `s_compact_kahler_with_class`
2. input: `s_compact_kahler_with_class` --[t_auxiliary_construction {object: "sl2_triple_L_Lambda_H_on_cohomology"}]--> output: `s_sl2_action_on_H_star_X`
3. input: `s_sl2_action_on_H_star_X` --[t_svd_and_spectral_decomposition {target: "Lefschetz_decomposition_into_primitive_parts"}]--> output: `s_primitive_decomposition`
4. input: `s_primitive_decomposition` --[t_structural_isomorphism {target: "L^k_iso_H^n-k_to_H^n+k"}]--> output: `s_hard_lefschetz`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_svd_and_spectral_decomposition, t_structural_isomorphism

---

### Lefschetz (1,1)-classes theorem (cite: https://en.wikipedia.org/wiki/Lefschetz_theorem_on_(1,1)-classes)

**Axioms:** `s_compact_smooth_manifold`, `s_differential_form`
**Terminal:** `s_lefschetz_1_1_classes` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_differential_form⟩` --[t_axiomatize_from_instances {property: "compact_Kahler_X_with_integral_(1,1)_class"}]--> output: `s_integral_1_1_class_on_kahler`
2. input: `s_integral_1_1_class_on_kahler` --[t_auxiliary_construction {object: "exponential_sequence_0_to_Z_to_O_to_O_star"}]--> output: `s_exponential_exact_sequence_pic`
3. input: `s_exponential_exact_sequence_pic` --[t_sheaf_cohomology_bridge {target: "long_exact_sequence_to_Pic_X"}]--> output: `s_pic_to_NS_via_chern_class`
4. input: `s_pic_to_NS_via_chern_class` --[t_structural_isomorphism {target: "integral_(1,1)_class_iso_c1_of_line_bundle"}]--> output: `s_lefschetz_1_1_classes`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_sheaf_cohomology_bridge, t_structural_isomorphism

---

### Hodge index theorem (cite: https://en.wikipedia.org/wiki/Hodge_index_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_differential_form`
**Terminal:** `s_hodge_index_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_differential_form⟩` --[t_axiomatize_from_instances {property: "smooth_projective_surface_S_with_NS_S"}]--> output: `s_neron_severi_lattice`
2. input: `s_neron_severi_lattice` --[t_auxiliary_construction {object: "intersection_pairing_restricted_to_NS_R"}]--> output: `s_intersection_form_on_NS_R`
3. input: `s_intersection_form_on_NS_R` --[t_svd_and_spectral_decomposition {target: "signature_via_Lefschetz_decomposition_on_H^1_1"}]--> output: `s_signature_(1,rho-1)`
4. input: `s_signature_(1,rho-1)` --[t_structural_isomorphism {target: "Hodge_index_signature_statement"}]--> output: `s_hodge_index_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_svd_and_spectral_decomposition, t_structural_isomorphism

---

### Torelli theorem for curves (cite: https://en.wikipedia.org/wiki/Torelli_theorem)

**Axioms:** `s_compact_riemann_surface`, `s_algebraically_closed_field_k`
**Terminal:** `s_torelli_curves` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_riemann_surface, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "smooth_projective_curve_C_genus_geq_2"}]--> output: `s_smooth_curve_C`
2. input: `s_smooth_curve_C` --[t_auxiliary_construction {object: "Jacobian_J_C_with_principal_polarization_theta"}]--> output: `s_polarized_jacobian`
3. input: `s_polarized_jacobian` --[t_duality {use: "theta_divisor_recovers_C_via_Riemann_singularity"}]--> output: `s_theta_divisor_singularities_recover_C`
4. input: `s_theta_divisor_singularities_recover_C` --[t_structural_isomorphism {target: "isomorphism_of_polarized_Jacobians_iff_isomorphism_of_curves"}]--> output: `s_torelli_curves`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_duality, t_structural_isomorphism

---

### Torelli theorem for K3 surfaces (cite: https://en.wikipedia.org/wiki/Torelli_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_algebraically_closed_field_k`
**Terminal:** `s_torelli_K3` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "K3_surface_with_Hodge_structure_on_H2"}]--> output: `s_K3_surface_with_hodge_structure`
2. input: `s_K3_surface_with_hodge_structure` --[t_auxiliary_construction {object: "period_point_in_period_domain_D"}]--> output: `s_period_map_for_K3`
3. input: `s_period_map_for_K3` --[t_structural_isomorphism {target: "Hodge_isometry_lifts_to_K3_isomorphism"}]--> output: `s_torelli_K3`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism

---

### Fourier–Mukai transform (cite: https://en.wikipedia.org/wiki/Fourier%E2%80%93Mukai_transform)

**Axioms:** `s_compact_smooth_manifold`, `s_algebraically_closed_field_k`
**Terminal:** `s_fourier_mukai_transform` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "abelian_variety_A_with_dual_A_hat"}]--> output: `s_abelian_variety_with_dual`
2. input: `s_abelian_variety_with_dual` --[t_auxiliary_construction {object: "Poincare_line_bundle_P_on_A_times_A_hat"}]--> output: `s_poincare_bundle`
3. input: `s_poincare_bundle` --[t_duality {use: "integral_transform_with_Poincare_kernel"}]--> output: `s_integral_transform_on_derived_category`
4. input: `s_integral_transform_on_derived_category` --[t_structural_isomorphism {target: "derived_equivalence_D(A)_iso_D(A_hat)"}]--> output: `s_fourier_mukai_transform`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_duality, t_structural_isomorphism

---

### Serre duality (cite: https://en.wikipedia.org/wiki/Serre_duality)

**Axioms:** `s_compact_smooth_manifold`, `s_algebraically_closed_field_k`
**Terminal:** `s_serre_duality` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "smooth_proper_X_dim_n_with_coherent_sheaf_F"}]--> output: `s_smooth_proper_X_with_F`
2. input: `s_smooth_proper_X_with_F` --[t_auxiliary_construction {object: "dualizing_sheaf_omega_X_via_canonical_bundle"}]--> output: `s_dualizing_sheaf_omega_X`
3. input: `s_dualizing_sheaf_omega_X` --[t_duality {use: "Yoneda_pairing_with_trace_map"}]--> output: `s_perfect_pairing_H_i_H_n-i`
4. input: `s_perfect_pairing_H_i_H_n-i` --[t_structural_isomorphism {target: "H_i_F_dual_to_H_n-i_F_dual_otimes_omega"}]--> output: `s_serre_duality`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_duality, t_structural_isomorphism

---

### Castelnuovo–Mumford regularity (cite: https://en.wikipedia.org/wiki/Castelnuovo%E2%80%93Mumford_regularity)

**Axioms:** `s_algebraically_closed_field_k`, `s_polynomial_ring_in_n_vars`
**Terminal:** `s_castelnuovo_mumford_regularity` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_polynomial_ring_in_n_vars⟩` --[t_axiomatize_from_instances {property: "coherent_sheaf_F_on_PN"}]--> output: `s_coherent_sheaf_F_on_PN`
2. input: `s_coherent_sheaf_F_on_PN` --[t_auxiliary_construction {object: "regularity_m_via_H_i_F(m-i)=0"}]--> output: `s_regularity_definition`
3. input: `s_regularity_definition` --[t_sheaf_cohomology_bridge {target: "twist_by_O(1)_propagates_vanishing"}]--> output: `s_vanishing_propagation`
4. input: `s_vanishing_propagation` --[t_structural_isomorphism {target: "F(m)_generated_by_global_sections_for_m_geq_reg"}]--> output: `s_castelnuovo_mumford_regularity`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_sheaf_cohomology_bridge, t_structural_isomorphism

---

### Castelnuovo's contractibility criterion (cite: https://en.wikipedia.org/wiki/Castelnuovo%27s_contraction_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_algebraically_closed_field_k`
**Terminal:** `s_castelnuovo_contractibility` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "smooth_projective_surface_with_(-1)-curve_E"}]--> output: `s_minus_one_curve_on_surface`
2. input: `s_minus_one_curve_on_surface` --[t_auxiliary_construction {object: "embedding_via_nK+H_for_ample_H"}]--> output: `s_morphism_contracting_E`
3. input: `s_morphism_contracting_E` --[t_structural_isomorphism {target: "image_smooth_with_inverse_a_blow_up"}]--> output: `s_castelnuovo_contractibility`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism

---

### Mori cone theorem (cite: https://en.wikipedia.org/wiki/Cone_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_algebraically_closed_field_k`
**Terminal:** `s_mori_cone_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "smooth_projective_X_with_canonical_K_X"}]--> output: `s_smooth_X_with_canonical`
2. input: `s_smooth_X_with_canonical` --[t_auxiliary_construction {object: "cone_of_curves_NE_X_with_K_X_negative_part"}]--> output: `s_cone_NE_decomposition`
3. input: `s_cone_NE_decomposition` --[t_compactness_argument {use: "bend_and_break_produces_rational_curves"}]--> output: `s_extremal_rays_spanned_by_rational_curves`
4. input: `s_extremal_rays_spanned_by_rational_curves` --[t_structural_isomorphism {target: "K_X_negative_part_locally_polyhedral"}]--> output: `s_mori_cone_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_compactness_argument, t_structural_isomorphism

---

### Mori extremal contraction (cite: https://en.wikipedia.org/wiki/Minimal_model_program)

**Axioms:** `s_compact_smooth_manifold`, `s_algebraically_closed_field_k`
**Terminal:** `s_mori_extremal_contraction` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "K_X_negative_extremal_ray_R"}]--> output: `s_extremal_ray_R`
2. input: `s_extremal_ray_R` --[t_auxiliary_construction {object: "supporting_nef_divisor_D_with_D.R=0"}]--> output: `s_supporting_nef_divisor`
3. input: `s_supporting_nef_divisor` --[t_sheaf_cohomology_bridge {target: "base_point_free_theorem_makes_D_semi_ample"}]--> output: `s_semi_ample_supporting_divisor`
4. input: `s_semi_ample_supporting_divisor` --[t_structural_isomorphism {target: "contraction_morphism_cont_R"}]--> output: `s_mori_extremal_contraction`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_sheaf_cohomology_bridge, t_structural_isomorphism

---

### Kawamata–Shokurov base-point-free theorem (cite: https://en.wikipedia.org/wiki/Base_point_free_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_algebraically_closed_field_k`
**Terminal:** `s_base_point_free_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "klt_pair_(X,Delta)_with_nef_aD-K_big"}]--> output: `s_nef_big_divisor_setup`
2. input: `s_nef_big_divisor_setup` --[t_auxiliary_construction {object: "Kawamata_Viehweg_vanishing_on_a_log_resolution"}]--> output: `s_KV_vanishing_application`
3. input: `s_KV_vanishing_application` --[t_sheaf_cohomology_bridge {target: "inductive_lift_of_sections_from_base_locus"}]--> output: `s_inductive_section_lifting`
4. input: `s_inductive_section_lifting` --[t_structural_isomorphism {target: "mD_is_globally_generated_for_m_large"}]--> output: `s_base_point_free_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_sheaf_cohomology_bridge, t_structural_isomorphism

---

### Kawamata–Viehweg vanishing theorem (cite: https://en.wikipedia.org/wiki/Kawamata%E2%80%93Viehweg_vanishing_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_algebraically_closed_field_k`
**Terminal:** `s_kawamata_viehweg_vanishing` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "big_and_nef_Q_divisor_D_on_smooth_X"}]--> output: `s_big_nef_q_divisor`
2. input: `s_big_nef_q_divisor` --[t_auxiliary_construction {object: "cyclic_cover_resolving_fractional_part"}]--> output: `s_cyclic_cover_construction`
3. input: `s_cyclic_cover_construction` --[t_sheaf_cohomology_bridge {target: "apply_Kodaira_vanishing_on_cover_and_descend"}]--> output: `s_descended_vanishing_statement`
4. input: `s_descended_vanishing_statement` --[t_structural_isomorphism {target: "H_i_X_K_X_plus_ceil_D_vanish_for_i_gt_0"}]--> output: `s_kawamata_viehweg_vanishing`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_sheaf_cohomology_bridge, t_structural_isomorphism

---

### Cartan's theorems A and B (cite: https://en.wikipedia.org/wiki/Cartan%27s_theorems_A_and_B)

**Axioms:** `s_compact_smooth_manifold`, `s_smooth_function`
**Terminal:** `s_cartan_A_B` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_smooth_function⟩` --[t_axiomatize_from_instances {property: "Stein_manifold_X_with_coherent_analytic_sheaf_F"}]--> output: `s_stein_manifold_with_coherent_F`
2. input: `s_stein_manifold_with_coherent_F` --[t_auxiliary_construction {object: "plurisubharmonic_exhaustion_function"}]--> output: `s_psh_exhaustion_of_X`
3. input: `s_psh_exhaustion_of_X` --[t_sheaf_cohomology_bridge {target: "Cousin_problem_solvable_via_d_bar_estimates"}]--> output: `s_H_i_X_F_vanish_for_i_geq_1`
4. input: `s_H_i_X_F_vanish_for_i_geq_1` --[t_structural_isomorphism {target: "global_sections_generate_stalks_(Theorem_A)_and_higher_vanish_(Theorem_B)"}]--> output: `s_cartan_A_B`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_sheaf_cohomology_bridge, t_structural_isomorphism

---

### Hurwitz's automorphisms theorem (cite: https://en.wikipedia.org/wiki/Hurwitz%27s_automorphisms_theorem)

**Axioms:** `s_compact_riemann_surface`, `s_algebraically_closed_field_k`
**Terminal:** `s_hurwitz_automorphisms` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_riemann_surface, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "compact_curve_C_genus_g_geq_2_with_automorphism_group_G"}]--> output: `s_curve_with_automorphism_group`
2. input: `s_curve_with_automorphism_group` --[t_symmetry_reduction {use: "Riemann_Hurwitz_for_quotient_map_C_to_C/G"}]--> output: `s_riemann_hurwitz_relation`
3. input: `s_riemann_hurwitz_relation` --[t_exhaustion_squeeze {bound: "minimize_2g-2_geq_|G|/42"}]--> output: `s_size_bound_|G|_leq_84(g-1)`
4. input: `s_size_bound_|G|_leq_84(g-1)` --[t_structural_isomorphism {target: "Hurwitz_84(g-1)_bound"}]--> output: `s_hurwitz_automorphisms`

**Techniques used:** t_axiomatize_from_instances, t_symmetry_reduction, t_exhaustion_squeeze, t_structural_isomorphism

---

### Belyi's theorem (cite: https://en.wikipedia.org/wiki/Belyi%27s_theorem)

**Axioms:** `s_compact_riemann_surface`, `s_algebraically_closed_field_k`
**Terminal:** `s_belyi_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_riemann_surface, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "smooth_projective_curve_C_defined_over_Q_bar"}]--> output: `s_curve_over_algebraic_closure_of_Q`
2. input: `s_curve_over_algebraic_closure_of_Q` --[t_auxiliary_construction {object: "rational_function_f_C_to_P1_ramified_over_few_points"}]--> output: `s_belyi_map_construction`
3. input: `s_belyi_map_construction` --[t_infinite_descent {invariant: "reduce_ramification_locus_via_Shabat_polynomials"}]--> output: `s_ramification_over_3_points_only`
4. input: `s_ramification_over_3_points_only` --[t_structural_isomorphism {target: "iff_C_defined_over_Q_bar"}]--> output: `s_belyi_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_infinite_descent, t_structural_isomorphism

---

### Chow's theorem (analytic = algebraic) (cite: https://en.wikipedia.org/wiki/Chow%27s_theorem)

**Axioms:** `s_compact_smooth_manifold`, `s_algebraically_closed_field_k`
**Terminal:** `s_chow_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "closed_analytic_subset_of_complex_projective_space"}]--> output: `s_analytic_subset_of_CPN`
2. input: `s_analytic_subset_of_CPN` --[t_auxiliary_construction {object: "Remmert_proper_mapping_theorem"}]--> output: `s_proper_image_analytic`
3. input: `s_proper_image_analytic` --[t_compactness_argument {use: "compactness_yields_finitely_many_irreducible_components"}]--> output: `s_finite_decomposition_into_components`
4. input: `s_finite_decomposition_into_components` --[t_structural_isomorphism {target: "every_analytic_subvariety_of_CPN_algebraic"}]--> output: `s_chow_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_compactness_argument, t_structural_isomorphism

---

### GAGA principle (Serre) (cite: https://en.wikipedia.org/wiki/Algebraic_geometry_and_analytic_geometry)

**Axioms:** `s_compact_smooth_manifold`, `s_algebraically_closed_field_k`
**Terminal:** `s_gaga_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "proper_algebraic_X_over_C_with_coherent_sheaf"}]--> output: `s_proper_X_with_coherent_sheaf`
2. input: `s_proper_X_with_coherent_sheaf` --[t_auxiliary_construction {object: "analytification_functor_F_to_F_an"}]--> output: `s_analytification_functor`
3. input: `s_analytification_functor` --[t_sheaf_cohomology_bridge {target: "H_i_F_iso_H_i_F_an_via_finiteness"}]--> output: `s_cohomology_isomorphism`
4. input: `s_cohomology_isomorphism` --[t_structural_isomorphism {target: "equivalence_of_coherent_categories"}]--> output: `s_gaga_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_sheaf_cohomology_bridge, t_structural_isomorphism

---

### Zariski's main theorem (cite: https://en.wikipedia.org/wiki/Zariski%27s_main_theorem)

**Axioms:** `s_algebraically_closed_field_k`, `s_noetherian_ring_R`
**Terminal:** `s_zariski_main_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_noetherian_ring_R⟩` --[t_axiomatize_from_instances {property: "quasi_finite_morphism_f_X_to_Y_of_noetherian_schemes"}]--> output: `s_quasi_finite_morphism`
2. input: `s_quasi_finite_morphism` --[t_auxiliary_construction {object: "Stein_factorization_f_equals_g_circ_h"}]--> output: `s_stein_factorization`
3. input: `s_stein_factorization` --[t_structural_isomorphism {target: "factor_into_open_immersion_followed_by_finite"}]--> output: `s_zariski_main_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism

---

### Zariski's connectedness theorem (cite: https://en.wikipedia.org/wiki/Zariski%27s_connectedness_theorem)

**Axioms:** `s_algebraically_closed_field_k`, `s_noetherian_ring_R`
**Terminal:** `s_zariski_connectedness` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_noetherian_ring_R⟩` --[t_axiomatize_from_instances {property: "proper_birational_morphism_to_normal_variety"}]--> output: `s_proper_birational_to_normal`
2. input: `s_proper_birational_to_normal` --[t_sheaf_cohomology_bridge {target: "f_star_O_X_equals_O_Y_by_normality"}]--> output: `s_pushforward_of_structure_sheaf_iso`
3. input: `s_pushforward_of_structure_sheaf_iso` --[t_structural_isomorphism {target: "fibers_connected_geometrically"}]--> output: `s_zariski_connectedness`

**Techniques used:** t_axiomatize_from_instances, t_sheaf_cohomology_bridge, t_structural_isomorphism

---

### Tarski–Seidenberg theorem (cite: https://en.wikipedia.org/wiki/Tarski%E2%80%93Seidenberg_theorem)

**Axioms:** `s_algebraically_closed_field_k`, `s_real_numbers`
**Terminal:** `s_tarski_seidenberg` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_real_numbers⟩` --[t_axiomatize_from_instances {property: "semialgebraic_set_S_in_R^n"}]--> output: `s_semialgebraic_set`
2. input: `s_semialgebraic_set` --[t_auxiliary_construction {object: "cylindrical_algebraic_decomposition_CAD"}]--> output: `s_CAD_of_S`
3. input: `s_CAD_of_S` --[t_projection_to_subspace {target: "image_under_linear_projection_remains_semialgebraic"}]--> output: `s_projection_is_semialgebraic`
4. input: `s_projection_is_semialgebraic` --[t_structural_isomorphism {target: "quantifier_elimination_for_real_closed_fields"}]--> output: `s_tarski_seidenberg`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_projection_to_subspace, t_structural_isomorphism

---

### Chevalley constructibility theorem (cite: https://en.wikipedia.org/wiki/Constructible_set)

**Axioms:** `s_algebraically_closed_field_k`, `s_noetherian_ring_R`
**Terminal:** `s_chevalley_constructibility` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_noetherian_ring_R⟩` --[t_axiomatize_from_instances {property: "finite_type_morphism_f_X_to_Y_of_noetherian_schemes"}]--> output: `s_finite_type_morphism`
2. input: `s_finite_type_morphism` --[t_auxiliary_construction {object: "Noetherian_induction_on_image_dimension"}]--> output: `s_noetherian_induction_setup`
3. input: `s_noetherian_induction_setup` --[t_projection_to_subspace {target: "image_of_constructible_constructible"}]--> output: `s_chevalley_constructibility`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_projection_to_subspace

---

### Borel fixed-point theorem (cite: https://en.wikipedia.org/wiki/Borel_fixed-point_theorem)

**Axioms:** `s_algebraically_closed_field_k`, `s_lie_group`
**Terminal:** `s_borel_fixed_point` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_lie_group⟩` --[t_axiomatize_from_instances {property: "connected_solvable_algebraic_group_G_acting_on_proper_variety"}]--> output: `s_solvable_action_on_proper`
2. input: `s_solvable_action_on_proper` --[t_auxiliary_construction {object: "minimal_orbit_closure"}]--> output: `s_minimal_orbit_closure`
3. input: `s_minimal_orbit_closure` --[t_compactness_argument {use: "complete_homogeneous_variety_under_solvable_group_is_a_point"}]--> output: `s_fixed_point_exists`
4. input: `s_fixed_point_exists` --[t_structural_isomorphism {target: "Borel_fixed_point_statement"}]--> output: `s_borel_fixed_point`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_compactness_argument, t_structural_isomorphism

---

### Chow's lemma (cite: https://en.wikipedia.org/wiki/Chow%27s_lemma)

**Axioms:** `s_algebraically_closed_field_k`, `s_noetherian_ring_R`
**Terminal:** `s_chow_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_noetherian_ring_R⟩` --[t_axiomatize_from_instances {property: "proper_morphism_X_to_S_of_finite_type"}]--> output: `s_proper_morphism_finite_type`
2. input: `s_proper_morphism_finite_type` --[t_auxiliary_construction {object: "open_cover_by_quasi_projective_pieces_then_blow_up"}]--> output: `s_blow_up_yielding_projective_birational_X_tilde`
3. input: `s_blow_up_yielding_projective_birational_X_tilde` --[t_structural_isomorphism {target: "projective_birational_to_X"}]--> output: `s_chow_lemma`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism

---

### Nagata compactification theorem (cite: https://en.wikipedia.org/wiki/Nagata%27s_compactification_theorem)

**Axioms:** `s_algebraically_closed_field_k`, `s_noetherian_ring_R`
**Terminal:** `s_nagata_compactification` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_noetherian_ring_R⟩` --[t_axiomatize_from_instances {property: "separated_finite_type_morphism_X_to_S"}]--> output: `s_separated_finite_type`
2. input: `s_separated_finite_type` --[t_auxiliary_construction {object: "patch_local_compactifications_using_blow_ups"}]--> output: `s_local_compactifications`
3. input: `s_local_compactifications` --[t_compactness_argument {use: "Zariski_Riemann_space_glues_to_proper_overscheme"}]--> output: `s_glued_proper_overscheme_X_bar`
4. input: `s_glued_proper_overscheme_X_bar` --[t_structural_isomorphism {target: "open_immersion_X_to_X_bar_proper_over_S"}]--> output: `s_nagata_compactification`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_compactness_argument, t_structural_isomorphism

---

### Modularity theorem (Taylor–Wiles–Breuil–Conrad–Diamond) (cite: https://en.wikipedia.org/wiki/Modularity_theorem)

**Axioms:** `s_elliptic_curve_over_Q`, `s_modular_form`
**Terminal:** `s_modularity_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_elliptic_curve_over_Q, s_modular_form⟩` --[t_axiomatize_from_instances {property: "elliptic_curve_E_over_Q_with_Galois_rep_rho_E"}]--> output: `s_galois_rep_of_elliptic_curve`
2. input: `s_galois_rep_of_elliptic_curve` --[t_heights_and_galois_rep_bridge {target: "deformation_theory_of_Galois_representations"}]--> output: `s_deformation_ring_R_to_T_map`
3. input: `s_deformation_ring_R_to_T_map` --[t_wiles_modularity {step: "R_equals_T_theorem"}]--> output: `s_R_equals_T_for_E`
4. input: `s_R_equals_T_for_E` --[t_structural_isomorphism {target: "E_modular_via_attached_newform"}]--> output: `s_modularity_theorem`

**Techniques used:** t_axiomatize_from_instances, t_heights_and_galois_rep_bridge, t_wiles_modularity, t_structural_isomorphism

---

### Tate isogeny theorem (cite: https://en.wikipedia.org/wiki/Tate%27s_isogeny_theorem)

**Axioms:** `s_algebraically_closed_field_k`, `s_elliptic_curve_over_Q`
**Terminal:** `s_tate_isogeny` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_elliptic_curve_over_Q⟩` --[t_axiomatize_from_instances {property: "abelian_variety_A_over_finite_field_F_q"}]--> output: `s_abelian_variety_over_Fq`
2. input: `s_abelian_variety_over_Fq` --[t_auxiliary_construction {object: "Tate_module_T_ell_A_with_Frobenius_action"}]--> output: `s_tate_module_with_frobenius`
3. input: `s_tate_module_with_frobenius` --[t_heights_and_galois_rep_bridge {target: "Hom_galois_T_ell_A_T_ell_B_iso_Hom_A_B_otimes_Z_ell"}]--> output: `s_hom_iso_via_galois_action`
4. input: `s_hom_iso_via_galois_action` --[t_structural_isomorphism {target: "isogeny_classification_via_characteristic_polynomial"}]--> output: `s_tate_isogeny`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_heights_and_galois_rep_bridge, t_structural_isomorphism

---

### Chow–Rashevskii theorem (cite: https://en.wikipedia.org/wiki/Chow%E2%80%93Rashevskii_theorem)

**Axioms:** `s_smooth_manifold`, `s_smooth_function`
**Terminal:** `s_chow_rashevskii` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold, s_smooth_function⟩` --[t_axiomatize_from_instances {property: "bracket_generating_distribution_D_on_M"}]--> output: `s_bracket_generating_distribution`
2. input: `s_bracket_generating_distribution` --[t_auxiliary_construction {object: "iterated_Lie_brackets_filling_tangent_space"}]--> output: `s_lie_bracket_filtration`
3. input: `s_lie_bracket_filtration` --[t_contraction_fixed_point {scheme: "concatenate_short_horizontal_paths_along_bracket_directions"}]--> output: `s_horizontal_path_reaches_neighborhood`
4. input: `s_horizontal_path_reaches_neighborhood` --[t_structural_isomorphism {target: "any_two_points_connected_by_horizontal_curve"}]--> output: `s_chow_rashevskii`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_contraction_fixed_point, t_structural_isomorphism

---

### Pansu differentiation theorem (cite: https://en.wikipedia.org/wiki/Pansu_derivative)

**Axioms:** `s_smooth_manifold`, `s_smooth_function`
**Terminal:** `s_pansu_differentiation` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_manifold, s_smooth_function⟩` --[t_axiomatize_from_instances {property: "Carnot_group_G_with_dilation_delta_t"}]--> output: `s_carnot_group_setting`
2. input: `s_carnot_group_setting` --[t_rescale_for_asymptotic_geometry {target: "limit_of_delta_t_pullback_of_Lipschitz_map"}]--> output: `s_blowup_limit_of_lipschitz`
3. input: `s_blowup_limit_of_lipschitz` --[t_structural_isomorphism {target: "Pansu_derivative_is_group_homomorphism_a.e."}]--> output: `s_pansu_differentiation`

**Techniques used:** t_axiomatize_from_instances, t_rescale_for_asymptotic_geometry, t_structural_isomorphism

---

### Cartan–Dieudonné theorem (cite: https://en.wikipedia.org/wiki/Cartan%E2%80%93Dieudonn%C3%A9_theorem)

**Axioms:** `s_real_vector_space`, `s_lie_group`
**Terminal:** `s_cartan_dieudonne` (kind: theorem)

**Steps:**
1. input: `⟨s_real_vector_space, s_lie_group⟩` --[t_axiomatize_from_instances {property: "orthogonal_transformation_T_of_nondegenerate_quadratic_space"}]--> output: `s_orthogonal_transformation`
2. input: `s_orthogonal_transformation` --[t_auxiliary_construction {object: "reflection_in_hyperplane_through_v-Tv"}]--> output: `s_canonical_reflection`
3. input: `s_canonical_reflection` --[t_infinite_descent {invariant: "fix_space_grows_with_each_reflection"}]--> output: `s_reduction_to_identity_after_n_reflections`
4. input: `s_reduction_to_identity_after_n_reflections` --[t_structural_isomorphism {target: "O(n)_generated_by_at_most_n_reflections"}]--> output: `s_cartan_dieudonne`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_infinite_descent, t_structural_isomorphism

---

### Beltrami theorem (cite: https://en.wikipedia.org/wiki/Beltrami%27s_theorem)

**Axioms:** `s_riemannian_metric`, `s_smooth_manifold`
**Terminal:** `s_beltrami_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_smooth_manifold⟩` --[t_axiomatize_from_instances {property: "geodesics_map_to_straight_lines_in_chart"}]--> output: `s_projectively_flat_metric`
2. input: `s_projectively_flat_metric` --[t_conserved_quantity {invariant: "constant_sectional_curvature_implied"}]--> output: `s_constant_sectional_curvature`
3. input: `s_constant_sectional_curvature` --[t_structural_isomorphism {target: "iff_metric_has_constant_curvature"}]--> output: `s_beltrami_theorem`

**Techniques used:** t_axiomatize_from_instances, t_conserved_quantity, t_structural_isomorphism

---

### Schur's theorem (Riemannian, isotropic implies constant curvature) (cite: https://en.wikipedia.org/wiki/Schur%27s_theorem)

**Axioms:** `s_riemannian_metric`, `s_smooth_manifold`
**Terminal:** `s_schur_riemannian` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_smooth_manifold⟩` --[t_axiomatize_from_instances {property: "isotropic_curvature_at_each_point_dim_geq_3"}]--> output: `s_isotropic_pointwise_curvature`
2. input: `s_isotropic_pointwise_curvature` --[t_conserved_quantity {invariant: "second_Bianchi_identity_for_curvature"}]--> output: `s_bianchi_identity_constraint`
3. input: `s_bianchi_identity_constraint` --[t_structural_isomorphism {target: "K_globally_constant"}]--> output: `s_schur_riemannian`

**Techniques used:** t_axiomatize_from_instances, t_conserved_quantity, t_structural_isomorphism

---

### Schwarz–Ahlfors–Pick theorem (cite: https://en.wikipedia.org/wiki/Schwarz%E2%80%93Ahlfors%E2%80%93Pick_theorem)

**Axioms:** `s_riemannian_metric`, `s_holomorphic_function_on_domain`
**Terminal:** `s_schwarz_ahlfors_pick` (kind: theorem)

**Steps:**
1. input: `⟨s_riemannian_metric, s_holomorphic_function_on_domain⟩` --[t_axiomatize_from_instances {property: "holomorphic_map_between_hyperbolic_Riemann_surfaces"}]--> output: `s_holomorphic_map_of_hyperbolic_surfaces`
2. input: `s_holomorphic_map_of_hyperbolic_surfaces` --[t_auxiliary_construction {object: "Ahlfors_Poincare_metric_on_each"}]--> output: `s_poincare_metric_pair`
3. input: `s_poincare_metric_pair` --[t_exhaustion_squeeze {bound: "pullback_metric_dominated_by_target"}]--> output: `s_distance_decreasing_property`
4. input: `s_distance_decreasing_property` --[t_structural_isomorphism {target: "Schwarz_Pick_inequality_with_equality_for_isometries"}]--> output: `s_schwarz_ahlfors_pick`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_exhaustion_squeeze, t_structural_isomorphism

---

### Williamson normal form theorem (cite: https://en.wikipedia.org/wiki/Williamson_theorem)

**Axioms:** `s_real_vector_space`, `s_differential_form`
**Terminal:** `s_williamson_normal_form` (kind: theorem)

**Steps:**
1. input: `⟨s_real_vector_space, s_differential_form⟩` --[t_axiomatize_from_instances {property: "symmetric_positive_definite_M_on_symplectic_R^2n"}]--> output: `s_positive_quadratic_form_on_symplectic_space`
2. input: `s_positive_quadratic_form_on_symplectic_space` --[t_svd_and_spectral_decomposition {operator: "symplectic_eigenvalues_of_Omega_inv_M"}]--> output: `s_symplectic_spectrum`
3. input: `s_symplectic_spectrum` --[t_reduce_to_canonical_form {form: "diag(d_i) Hamiltonian normal form"}]--> output: `s_williamson_normal_form`

**Techniques used:** t_axiomatize_from_instances, t_svd_and_spectral_decomposition, t_reduce_to_canonical_form

---

### Birkhoff–Grothendieck theorem (cite: https://en.wikipedia.org/wiki/Birkhoff%E2%80%93Grothendieck_theorem)

**Axioms:** `s_algebraically_closed_field_k`, `s_compact_riemann_surface`
**Terminal:** `s_birkhoff_grothendieck` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_compact_riemann_surface⟩` --[t_axiomatize_from_instances {property: "holomorphic_vector_bundle_E_on_P1"}]--> output: `s_holomorphic_bundle_on_P1`
2. input: `s_holomorphic_bundle_on_P1` --[t_auxiliary_construction {object: "maximal_degree_line_subbundle_O(a_1)"}]--> output: `s_maximal_subbundle`
3. input: `s_maximal_subbundle` --[t_infinite_descent {invariant: "rank_decreases_after_splitting_off_line_bundle"}]--> output: `s_inductive_splitting_into_line_bundles`
4. input: `s_inductive_splitting_into_line_bundles` --[t_structural_isomorphism {target: "E_iso_oplus_O(a_i)_with_a_1_geq..."}]--> output: `s_birkhoff_grothendieck`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_infinite_descent, t_structural_isomorphism

---

### Lüroth's theorem (cite: https://en.wikipedia.org/wiki/L%C3%BCroth%27s_theorem)

**Axioms:** `s_algebraically_closed_field_k`, `s_compact_riemann_surface`
**Terminal:** `s_luroth_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_compact_riemann_surface⟩` --[t_axiomatize_from_instances {property: "subfield_K_of_k(t)_containing_k"}]--> output: `s_intermediate_field_in_k(t)`
2. input: `s_intermediate_field_in_k(t)` --[t_auxiliary_construction {object: "minimal_polynomial_of_t_over_K"}]--> output: `s_minimal_polynomial_of_t`
3. input: `s_minimal_polynomial_of_t` --[t_structural_isomorphism {target: "K_iso_k(u)_for_one_generator_u"}]--> output: `s_luroth_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism

---

### Clifford's theorem on special divisors (cite: https://en.wikipedia.org/wiki/Clifford%27s_theorem_on_special_divisors)

**Axioms:** `s_compact_riemann_surface`, `s_algebraically_closed_field_k`
**Terminal:** `s_clifford_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_riemann_surface, s_algebraically_closed_field_k⟩` --[t_axiomatize_from_instances {property: "special_divisor_D_with_h0_D_geq_1_and_h1_D_geq_1"}]--> output: `s_special_divisor_setup`
2. input: `s_special_divisor_setup` --[t_auxiliary_construction {object: "linear_systems_|D|_and_|K-D|_multiplication_map"}]--> output: `s_multiplication_map_of_linear_systems`
3. input: `s_multiplication_map_of_linear_systems` --[t_exhaustion_squeeze {bound: "2 h0(D) - 2 leq deg(D)"}]--> output: `s_clifford_inequality`
4. input: `s_clifford_inequality` --[t_structural_isomorphism {target: "equality_iff_D=0_K_or_hyperelliptic_g2k"}]--> output: `s_clifford_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_exhaustion_squeeze, t_structural_isomorphism

---


