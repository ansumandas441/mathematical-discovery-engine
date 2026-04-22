# Round 0 Cleanup — Execution Log

Baseline: 352 nodes, 343 edges.

## Step 1 — New technique nodes
Added 9:
  - `t_auxiliary_construction`
  - `t_conjecture_refinement`
  - `t_reductio_ad_absurdum`
  - `t_projection_to_subspace`
  - `t_sheaf_cohomology_bridge`
  - `t_k_theoretic_index_bridge`
  - `t_heights_and_galois_rep_bridge`
  - `t_level_lowering_bridge`
  - `t_transference_bridge`

## Step 2 — Metadata corrections
(13 updates)
  - t_distributed_collaboration -> meta_technique: true
  - t_complex_analysis_to_integers -> single_use_landmark: true
  - t_sheafify_on_grothendieck_topology -> single_use_landmark: true
  - t_group_complete_exact_category -> single_use_landmark: true
  - t_rescale_for_asymptotic_geometry -> single_use_landmark: true
  - t_ultraproduct_transfer -> single_use_landmark: true
  - t_probabilistic_existence -> single_use_landmark: true
  - t_category_theoretic_colimits_and_adjoints -> single_use_landmark: true
  - t_polynomial_method -> single_use_landmark: true
  - t_deformation_cohomology -> single_use_landmark: true
  - t_svd_and_spectral_decomposition -> no longer provisional
  - s_galois_group is_specialization_of s_finite_group
  - s_compact_oriented_surface_without_boundary is_specialization_of s_compact_smooth_manifold

## Step 3 — Deduplication (3 merges)
  - Dedup: merged s_prime_numbers -> s_primes_in_naturals (0 edges remapped total)
  - Dedup: merged s_euclidean_solid_geometry -> s_euclidean_3_space (0 edges remapped total)
  - Dedup: merged s_real_line -> s_real_numbers (0 edges remapped total)

## Step 4 — Orphan audit
Orphans before fix: 76

Applied 28 Type-A fixes (axiom → technique → theorem wire-ups):
  - wired s_polygon_area_formula -> t_exhaustion_squeeze -> (s_area_of_circle)
  - wired s_similar_triangle_criterion -> t_compose_with_identity -> (s_ptolemys_theorem)
  - wired s_circle_definition -> t_symmetry_reduction -> (s_area_of_circle)
  - wired s_prime_pair_p_q -> t_character_decomposition_count -> (s_quadratic_reciprocity)
  - wired s_unit_circle_in_C -> t_frequency_decomposition -> (s_de_moivre_formula)
  - wired s_topological_sphere_S2 -> t_conserved_quantity -> (s_euler_polyhedron_formula)
  - wired s_first_fundamental_form -> t_physics_to_pde -> (s_theorema_egregium)
  - wired s_projective_plane -> t_raise_dimension -> (s_desargues_theorem)
  - wired s_projective_space_axioms -> t_raise_dimension -> (s_desargues_theorem)
  - wired s_simply_connected_proper_domain_in_C -> t_interpolate_and_continue -> (s_riemann_mapping_theorem)
  - wired s_coprime_pair -> t_reduce_to_canonical_form -> (s_chinese_remainder_theorem)
  - wired s_pell_equation_x2_minus_N_y2 -> t_infinite_descent -> (s_solvability_of_pell_equation)
  - wired s_graph_definition -> t_axiomatize_from_instances -> (s_eulerian_path_criterion)
  - wired s_prime_p -> t_symmetry_reduction -> (s_fermat_little_theorem)
  - wired s_probability_axioms -> t_frequency_decomposition -> (s_central_limit_theorem)
  - wired s_conic_sections -> t_physics_to_pde -> (s_kepler_three_laws)
  - wired s_product_topology -> t_ultraproduct_transfer -> (s_tychonoff_theorem)
  - wired s_differential_form -> t_duality -> (s_stokes_theorem)
  - wired s_real_analysis -> t_frequency_decomposition -> (s_basel_identity)
  - wired s_prime_power_divisor_p_n -> t_symmetry_reduction -> (s_sylow_theorems)
  - (+ 8 more)

Applied 10 Type-B umbrella flags:
  - t_selberg_sieve_method -> subgraph_host: true
  - t_category_theoretic_colimits_and_adjoints -> subgraph_host: true
  - t_atiyah_singer_index_machinery -> subgraph_host: true
  - t_furstenberg_correspondence_principle -> subgraph_host: true
  - t_circle_method -> subgraph_host: true
  - t_ricci_flow_with_surgery -> subgraph_host: true
  - t_galois_correspondence -> subgraph_host: true
  - t_wiles_modularity -> subgraph_host: true
  - t_godel_numbering -> subgraph_host: true
  - t_fourier_transform -> subgraph_host: true

Orphans after fix: 52
Remaining (not Type-A/B autofixable): ['s_euclidean_plane', 's_euclidean_3_space', 's_real_numbers', 's_real_line_or_circle', 's_complex_numbers', 's_integers', 's_turing_machine_model', 's_divisor_on_curve', 's_primes_in_naturals', 's_riemann_zeta_function', 's_finite_group', 's_closed_ball_D_n', 's_continuous_self_map', 's_real_vector_space', 's_polynomial_ring']

## Step 5 — Canonical index emitted
62 techniques, 231 axiom+state, 65 theorem ids written to `canonical_node_index.md`

## Step 6 — Integrity checks

Theorems without incoming edge: 0
Unresolved duplicate type_signatures: 20
Orphans total: 52 (10 flagged as subgraph_host, 42 unflagged)
  → unflagged sample: ['s_euclidean_plane', 's_euclidean_3_space', 's_real_numbers', 's_real_line_or_circle', 's_complex_numbers', 's_integers', 's_turing_machine_model', 's_divisor_on_curve', 's_primes_in_naturals', 's_riemann_zeta_function']

## Final
Nodes: 358 (was 352). Edges: 371 (was 343).

Round 0 gate: RETRY (unflagged orphans = 42).
