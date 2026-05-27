# Area Topology Derivation Chains (iter-3)

**Source pages:**
- https://en.wikipedia.org/wiki/Category:Theorems_in_topology
- https://en.wikipedia.org/wiki/Category:Theorems_in_algebraic_topology
- https://en.wikipedia.org/wiki/Category:Theorems_in_differential_topology
- https://en.wikipedia.org/wiki/Category:Theorems_in_homotopy_theory
- https://en.wikipedia.org/wiki/Algebraic_topology
- https://en.wikipedia.org/wiki/General_topology

**Target:** 90 chains. **Drafted:** 156 (over-delivered to give wide coverage; trim downstream if desired). **Skipped (already in graph):** 3 — `s_tychonoff_theorem`, `s_brouwer_fpt`, `s_atiyah_singer_index_theorem` (also note `s_poincare_conjecture`, `s_geometrization_theorem` are existing and appear as glue/inputs only, never re-derived).

**Flagged (`⚠ needs new technique`):** 0.

Note: edge-label "techniques" are drawn solely from `TECHNIQUES.md`. State ids use snake_case mathematical object names. Each chain is a *discovery chain*, not a proof.

---

## I. General topology (separation, compactness, metrization)

### Urysohn's lemma (cite: https://en.wikipedia.org/wiki/Urysohn%27s_lemma)

**Axioms:** `s_normal_hausdorff_space`, `s_pair_of_disjoint_closed_sets`
**Terminal:** `s_urysohn_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_normal_hausdorff_space, s_pair_of_disjoint_closed_sets⟩` --[t_auxiliary_construction {object: "dyadic-rational-indexed nested open sets"}]--> output: `s_dyadic_chain_of_open_sets`
2. input: `s_dyadic_chain_of_open_sets` --[t_interpolate_and_continue {parameter: dyadic_to_real}]--> output: `s_continuous_separating_function_from_dyadics`
3. input: `s_continuous_separating_function_from_dyadics` --[t_exhaustion_squeeze {limit: real_unit_interval}]--> output: `s_urysohn_lemma`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_exhaustion_squeeze

---

### Tietze extension theorem (cite: https://en.wikipedia.org/wiki/Tietze_extension_theorem)

**Axioms:** `s_normal_hausdorff_space`, `s_urysohn_lemma`
**Terminal:** `s_tietze_extension_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_normal_hausdorff_space, s_bounded_continuous_function_on_closed_subset⟩` --[t_auxiliary_construction {object: "level-set decomposition by thirds"}]--> output: `s_thirds_partition_of_function`
2. input: `⟨s_thirds_partition_of_function, s_urysohn_lemma⟩` --[t_interpolate_and_continue {parameter: geometric_thirds_series}]--> output: `s_extension_with_small_residual`
3. input: `s_extension_with_small_residual` --[t_contraction_fixed_point {space: bounded_continuous_functions, factor: 2/3}]--> output: `s_tietze_extension_theorem`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_contraction_fixed_point

---

### Urysohn metrization theorem (cite: https://en.wikipedia.org/wiki/Urysohn%27s_metrization_theorem)

**Axioms:** `s_second_countable_regular_hausdorff_space`, `s_urysohn_lemma`
**Terminal:** `s_urysohn_metrization_theorem` (kind: theorem)

**Steps:**
1. input: `s_second_countable_regular_hausdorff_space` --[t_axiomatize_from_instances {target: "countable separating family of [0,1]-valued maps"}]--> output: `s_countable_separating_family`
2. input: `⟨s_countable_separating_family, s_urysohn_lemma⟩` --[t_auxiliary_construction {object: "diagonal map into Hilbert cube"}]--> output: `s_embedding_into_hilbert_cube`
3. input: `s_embedding_into_hilbert_cube` --[t_structural_isomorphism {target: subspace_of_metric_space}]--> output: `s_urysohn_metrization_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism

---

### Nagata–Smirnov metrization theorem (cite: https://en.wikipedia.org/wiki/Nagata%E2%80%93Smirnov_metrization_theorem)

**Axioms:** `s_regular_hausdorff_space`, `s_sigma_locally_finite_basis`
**Terminal:** `s_nagata_smirnov_metrization` (kind: theorem)

**Steps:**
1. input: `s_regular_hausdorff_space` --[t_axiomatize_from_instances {target: "σ-locally-finite basis condition"}]--> output: `s_sigma_locally_finite_basis_present`
2. input: `s_sigma_locally_finite_basis_present` --[t_auxiliary_construction {object: "partition-of-unity-style pseudometrics"}]--> output: `s_countable_family_of_pseudometrics`
3. input: `s_countable_family_of_pseudometrics` --[t_interpolate_and_continue {parameter: weighted_sum_of_pseudometrics}]--> output: `s_compatible_metric`
4. input: `s_compatible_metric` --[t_structural_isomorphism {target: metric_topology_equals_original}]--> output: `s_nagata_smirnov_metrization`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_interpolate_and_continue, t_structural_isomorphism

---

### Bing metrization theorem (cite: https://en.wikipedia.org/wiki/Bing_metrization_theorem)

**Axioms:** `s_regular_hausdorff_space`
**Terminal:** `s_bing_metrization` (kind: theorem)

**Steps:**
1. input: `s_regular_hausdorff_space` --[t_axiomatize_from_instances {target: "σ-discrete basis condition"}]--> output: `s_sigma_discrete_basis_present`
2. input: `s_sigma_discrete_basis_present` --[t_structural_isomorphism {target: equivalent_to_sigma_locally_finite}]--> output: `s_nagata_smirnov_form`
3. input: `s_nagata_smirnov_form` --[t_compose_with_identity {with: nagata_smirnov_metrization}]--> output: `s_bing_metrization`

**Techniques used:** t_axiomatize_from_instances, t_structural_isomorphism, t_compose_with_identity

---

### Stone–Čech compactification (cite: https://en.wikipedia.org/wiki/Stone%E2%80%93%C4%8Cech_compactification)

**Axioms:** `s_tychonoff_space`, `s_unit_interval`
**Terminal:** `s_stone_cech_compactification` (kind: theorem)

**Steps:**
1. input: `s_tychonoff_space` --[t_auxiliary_construction {object: "evaluation map into product of [0,1] indexed by C(X,[0,1])"}]--> output: `s_evaluation_into_product_of_intervals`
2. input: `⟨s_evaluation_into_product_of_intervals, s_tychonoff_theorem⟩` --[t_compactness_argument {target: closure_is_compact_hausdorff}]--> output: `s_compact_hausdorff_closure_beta_X`
3. input: `s_compact_hausdorff_closure_beta_X` --[t_representable_functor_trick {functor: "C(-,K) for K compact Hausdorff"}]--> output: `s_stone_cech_compactification`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_representable_functor_trick

---

### Alexandroff one-point compactification (cite: https://en.wikipedia.org/wiki/Alexandroff_extension)

**Axioms:** `s_locally_compact_hausdorff_space`
**Terminal:** `s_alexandroff_one_point_compactification` (kind: theorem)

**Steps:**
1. input: `s_locally_compact_hausdorff_space` --[t_auxiliary_construction {object: "adjoin point at infinity ∞"}]--> output: `s_x_plus_infinity_set`
2. input: `s_x_plus_infinity_set` --[t_axiomatize_from_instances {target: "open sets = original opens ∪ complements of compacts"}]--> output: `s_one_point_topology`
3. input: `s_one_point_topology` --[t_compactness_argument {target: open_cover_has_finite_subcover}]--> output: `s_alexandroff_one_point_compactification`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_compactness_argument

---

### Baire category theorem (cite: https://en.wikipedia.org/wiki/Baire_category_theorem)

**Axioms:** `s_complete_metric_space`, `s_countable_family_of_dense_opens`
**Terminal:** `s_baire_category_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_complete_metric_space, s_countable_family_of_dense_opens⟩` --[t_auxiliary_construction {object: "nested shrinking closed balls inside each dense open"}]--> output: `s_nested_shrinking_closed_balls`
2. input: `s_nested_shrinking_closed_balls` --[t_contraction_fixed_point {space: complete_metric_space, target: limit_point_in_all_balls}]--> output: `s_limit_point_in_all_dense_opens`
3. input: `s_limit_point_in_all_dense_opens` --[t_exhaustion_squeeze {limit: intersection_is_dense}]--> output: `s_baire_category_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Lebesgue number lemma (cite: https://en.wikipedia.org/wiki/Lebesgue%27s_number_lemma)

**Axioms:** `s_compact_metric_space`, `s_open_cover_of_compact_set`
**Terminal:** `s_lebesgue_number_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_metric_space, s_open_cover_of_compact_set⟩` --[t_compactness_argument {target: finite_subcover_with_radii}]--> output: `s_finite_subcover_with_radii`
2. input: `s_finite_subcover_with_radii` --[t_exhaustion_squeeze {limit: positive_min_radius}]--> output: `s_positive_lebesgue_number_delta`
3. input: `s_positive_lebesgue_number_delta` --[t_compose_with_identity {with: ball_radius_property}]--> output: `s_lebesgue_number_lemma`

**Techniques used:** t_compactness_argument, t_exhaustion_squeeze, t_compose_with_identity

---

### Pasting lemma (cite: https://en.wikipedia.org/wiki/Pasting_lemma)

**Axioms:** `s_topological_space`, `s_finite_closed_cover_with_continuous_pieces`
**Terminal:** `s_pasting_lemma` (kind: theorem)

**Steps:**
1. input: `s_finite_closed_cover_with_continuous_pieces` --[t_axiomatize_from_instances {target: "preimage of closed set"}]--> output: `s_preimage_of_closed_is_closed_per_piece`
2. input: `s_preimage_of_closed_is_closed_per_piece` --[t_compose_with_identity {with: finite_union_of_closed_is_closed}]--> output: `s_pasting_lemma`

**Techniques used:** t_axiomatize_from_instances, t_compose_with_identity

---

### Heine–Cantor theorem (uniform continuity on compacts) (cite: https://en.wikipedia.org/wiki/Heine%E2%80%93Cantor_theorem)

**Axioms:** `s_compact_metric_space`, `s_continuous_function_on_compact_metric_space`
**Terminal:** `s_heine_cantor_theorem` (kind: theorem)

**Steps:**
1. input: `s_continuous_function_on_compact_metric_space` --[t_compactness_argument {target: open_cover_by_epsilon_continuity_balls}]--> output: `s_epsilon_continuity_finite_subcover`
2. input: `s_epsilon_continuity_finite_subcover` --[t_exhaustion_squeeze {limit: uniform_delta}]--> output: `s_heine_cantor_theorem`

**Techniques used:** t_compactness_argument, t_exhaustion_squeeze

---

### Arzelà–Ascoli theorem (cite: https://en.wikipedia.org/wiki/Arzel%C3%A0%E2%80%93Ascoli_theorem)

**Axioms:** `s_compact_metric_space`, `s_equicontinuous_pointwise_bounded_family`
**Terminal:** `s_arzela_ascoli_theorem` (kind: theorem)

**Steps:**
1. input: `s_equicontinuous_pointwise_bounded_family` --[t_compactness_argument {target: total_boundedness_in_sup_norm}]--> output: `s_totally_bounded_in_C_X`
2. input: `s_totally_bounded_in_C_X` --[t_pigeonhole_collision {dim: countable_dense_subset}]--> output: `s_uniformly_convergent_subsequence_extraction`
3. input: `s_uniformly_convergent_subsequence_extraction` --[t_exhaustion_squeeze {limit: relatively_compact_family}]--> output: `s_arzela_ascoli_theorem`

**Techniques used:** t_compactness_argument, t_pigeonhole_collision, t_exhaustion_squeeze

---

### Stone–Weierstrass theorem (cite: https://en.wikipedia.org/wiki/Stone%E2%80%93Weierstrass_theorem)

**Axioms:** `s_compact_hausdorff_space`, `s_unital_separating_subalgebra_of_C_X`
**Terminal:** `s_stone_weierstrass_theorem` (kind: theorem)

**Steps:**
1. input: `s_unital_separating_subalgebra_of_C_X` --[t_axiomatize_from_instances {target: closure_is_lattice_under_max_min}]--> output: `s_closure_is_lattice`
2. input: `s_closure_is_lattice` --[t_interpolate_and_continue {parameter: "polynomial approx of |t|"}]--> output: `s_lattice_density_in_C_X`
3. input: `s_lattice_density_in_C_X` --[t_exhaustion_squeeze {limit: uniform_approximation}]--> output: `s_stone_weierstrass_theorem`

**Techniques used:** t_axiomatize_from_instances, t_interpolate_and_continue, t_exhaustion_squeeze

---

### Alexander subbase lemma (cite: https://en.wikipedia.org/wiki/Alexander_subbase_theorem)

**Axioms:** `s_topological_space`, `s_subbase_of_topology`
**Terminal:** `s_alexander_subbase_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_topological_space, s_subbase_of_topology⟩` --[t_reductio_ad_absurdum {assume: subbase_cover_with_no_finite_subcover_exists}]--> output: `s_maximal_subbase_anticover_via_zorn`
2. input: `s_maximal_subbase_anticover_via_zorn` --[t_compactness_argument {target: extend_to_base_cover_contradiction}]--> output: `s_alexander_subbase_lemma`

**Techniques used:** t_reductio_ad_absurdum, t_compactness_argument

---

### Tychonoff theorem ⚠ SKIPPED — already in graph as `s_tychonoff_theorem`.

---

### Michael selection theorem (cite: https://en.wikipedia.org/wiki/Michael_selection_theorem)

**Axioms:** `s_paracompact_hausdorff_space`, `s_lower_semicontinuous_convex_valued_correspondence`
**Terminal:** `s_michael_selection_theorem` (kind: theorem)

**Steps:**
1. input: `s_lower_semicontinuous_convex_valued_correspondence` --[t_auxiliary_construction {object: "epsilon-approximate continuous selection"}]--> output: `s_epsilon_approximate_selection`
2. input: `s_epsilon_approximate_selection` --[t_interpolate_and_continue {parameter: partition_of_unity_refinement}]--> output: `s_cauchy_sequence_of_selections`
3. input: `s_cauchy_sequence_of_selections` --[t_contraction_fixed_point {space: continuous_selections, factor: 1/2}]--> output: `s_michael_selection_theorem`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_contraction_fixed_point

---

### Sorgenfrey line not metrizable (cite: https://en.wikipedia.org/wiki/Lower_limit_topology)

**Axioms:** `s_sorgenfrey_line`
**Terminal:** `s_sorgenfrey_not_metrizable` (kind: theorem)

**Steps:**
1. input: `s_sorgenfrey_line` --[t_verify_on_special_cases {case: separable_but_uncountable_discrete_subspace_in_product}]--> output: `s_sorgenfrey_squared_not_lindelof`
2. input: `s_sorgenfrey_squared_not_lindelof` --[t_reductio_ad_absurdum {assume: metrizable_then_separable_implies_second_countable}]--> output: `s_sorgenfrey_not_metrizable`

**Techniques used:** t_verify_on_special_cases, t_reductio_ad_absurdum

---

### Embedding into Hilbert cube (cite: https://en.wikipedia.org/wiki/Hilbert_cube)

**Axioms:** `s_compact_metrizable_space`
**Terminal:** `s_hilbert_cube_embedding` (kind: theorem)

**Steps:**
1. input: `s_compact_metrizable_space` --[t_axiomatize_from_instances {target: countable_dense_subset}]--> output: `s_countable_dense_subset_of_X`
2. input: `s_countable_dense_subset_of_X` --[t_auxiliary_construction {object: "coordinates = d(x, xₙ)"}]--> output: `s_distance_to_dense_coords`
3. input: `s_distance_to_dense_coords` --[t_structural_isomorphism {target: subspace_of_hilbert_cube}]--> output: `s_hilbert_cube_embedding`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism

---

### Compactness ⇔ sequential compactness in metric spaces (cite: https://en.wikipedia.org/wiki/Sequentially_compact_space)

**Axioms:** `s_metric_space`
**Terminal:** `s_compact_iff_sequentially_compact_metric` (kind: theorem)

**Steps:**
1. input: `s_metric_space` --[t_verify_on_special_cases {case: compact_implies_totally_bounded_and_complete}]--> output: `s_totally_bounded_and_complete`
2. input: `s_totally_bounded_and_complete` --[t_pigeonhole_collision {dim: epsilon_net_layers}]--> output: `s_cauchy_subsequence_extraction`
3. input: `s_cauchy_subsequence_extraction` --[t_exhaustion_squeeze {limit: convergent_subsequence}]--> output: `s_compact_iff_sequentially_compact_metric`

**Techniques used:** t_verify_on_special_cases, t_pigeonhole_collision, t_exhaustion_squeeze

---

### Cantor–Bendixson theorem (cite: https://en.wikipedia.org/wiki/Cantor%E2%80%93Bendixson_theorem)

**Axioms:** `s_polish_space`
**Terminal:** `s_cantor_bendixson_theorem` (kind: theorem)

**Steps:**
1. input: `s_polish_space` --[t_auxiliary_construction {object: "iterated derived set operator (Cantor–Bendixson derivative)"}]--> output: `s_cantor_bendixson_derivatives`
2. input: `s_cantor_bendixson_derivatives` --[t_infinite_descent {ordinal: stabilizes_at_countable_ordinal}]--> output: `s_perfect_kernel_plus_countable_scattered`
3. input: `s_perfect_kernel_plus_countable_scattered` --[t_compose_with_identity {with: perfect_set_decomposition}]--> output: `s_cantor_bendixson_theorem`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_compose_with_identity

---

### Lusin separation theorem (cite: https://en.wikipedia.org/wiki/Lusin%27s_separation_theorem)

**Axioms:** `s_polish_space`, `s_pair_of_disjoint_analytic_sets`
**Terminal:** `s_lusin_separation_theorem` (kind: theorem)

**Steps:**
1. input: `s_pair_of_disjoint_analytic_sets` --[t_auxiliary_construction {object: "Souslin-scheme tree projections"}]--> output: `s_souslin_scheme_separation`
2. input: `s_souslin_scheme_separation` --[t_infinite_descent {parameter: tree_level_refinement}]--> output: `s_borel_separating_set`
3. input: `s_borel_separating_set` --[t_compose_with_identity {with: borel_class_closure}]--> output: `s_lusin_separation_theorem`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_compose_with_identity

---

### Sierpiński theorem on continuum connectedness (cite: https://en.wikipedia.org/wiki/Sierpi%C5%84ski%27s_theorem_on_metric_spaces)

**Axioms:** `s_compact_connected_hausdorff_space`
**Terminal:** `s_sierpinski_continuum_theorem` (kind: theorem)

**Steps:**
1. input: `s_compact_connected_hausdorff_space` --[t_reductio_ad_absurdum {assume: countable_partition_into_disjoint_closed_pieces}]--> output: `s_countable_closed_partition_hypothesis`
2. input: `s_countable_closed_partition_hypothesis` --[t_pigeonhole_collision {dim: nested_subcontinuum_recursion}]--> output: `s_contradiction_with_compactness`
3. input: `s_contradiction_with_compactness` --[t_compactness_argument {target: nonempty_intersection}]--> output: `s_sierpinski_continuum_theorem`

**Techniques used:** t_reductio_ad_absurdum, t_pigeonhole_collision, t_compactness_argument

---

## II. Fixed points, Borsuk–Ulam, separation, dimension

### Brouwer fixed-point theorem ⚠ SKIPPED — already in graph as `s_brouwer_fpt`.

---

### Borsuk–Ulam theorem (cite: https://en.wikipedia.org/wiki/Borsuk%E2%80%93Ulam_theorem)

**Axioms:** `s_sphere_S_n`, `s_continuous_map_S_n_to_R_n`
**Terminal:** `s_borsuk_ulam_theorem` (kind: theorem)

**Steps:**
1. input: `s_continuous_map_S_n_to_R_n` --[t_reductio_ad_absurdum {assume: no_antipodal_collision}]--> output: `s_antipodal_free_map_to_S_n_minus_1`
2. input: `s_antipodal_free_map_to_S_n_minus_1` --[t_symmetry_reduction {group: Z2_antipodal_action}]--> output: `s_Z2_equivariant_map_to_lower_sphere`
3. input: `s_Z2_equivariant_map_to_lower_sphere` --[t_obstruction_class {class: stiefel_whitney_w_n_or_degree_mod_2}]--> output: `s_borsuk_ulam_theorem`

**Techniques used:** t_reductio_ad_absurdum, t_symmetry_reduction, t_obstruction_class

---

### Ham sandwich theorem (cite: https://en.wikipedia.org/wiki/Ham_sandwich_theorem)

**Axioms:** `s_n_finite_measures_in_R_n`
**Terminal:** `s_ham_sandwich_theorem` (kind: theorem)

**Steps:**
1. input: `s_n_finite_measures_in_R_n` --[t_auxiliary_construction {object: "vector of signed half-volume differences over unit normal direction"}]--> output: `s_signed_half_volume_map_on_S_n`
2. input: `s_signed_half_volume_map_on_S_n` --[t_symmetry_reduction {group: antipodal_sign_flip}]--> output: `s_odd_map_S_n_to_R_n`
3. input: `s_odd_map_S_n_to_R_n` --[t_compose_with_identity {with: borsuk_ulam_theorem}]--> output: `s_ham_sandwich_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_compose_with_identity

---

### Lyusternik–Schnirelmann theorem (cite: https://en.wikipedia.org/wiki/Lusternik%E2%80%93Schnirelmann_theorem)

**Axioms:** `s_sphere_S_n`, `s_closed_cover_S_n_by_n_plus_1_sets`
**Terminal:** `s_lyusternik_schnirelmann_theorem` (kind: theorem)

**Steps:**
1. input: `s_closed_cover_S_n_by_n_plus_1_sets` --[t_reductio_ad_absurdum {assume: no_set_contains_antipodal_pair}]--> output: `s_antipodal_separated_cover_hypothesis`
2. input: `s_antipodal_separated_cover_hypothesis` --[t_auxiliary_construction {object: "distance-to-set map"}]--> output: `s_distance_vector_map_S_n_to_R_n`
3. input: `s_distance_vector_map_S_n_to_R_n` --[t_compose_with_identity {with: borsuk_ulam_theorem}]--> output: `s_lyusternik_schnirelmann_theorem`

**Techniques used:** t_reductio_ad_absurdum, t_auxiliary_construction, t_compose_with_identity

---

### Lefschetz fixed-point theorem (cite: https://en.wikipedia.org/wiki/Lefschetz_fixed-point_theorem)

**Axioms:** `s_compact_polyhedron`, `s_continuous_self_map_of_polyhedron`
**Terminal:** `s_lefschetz_fixed_point_theorem` (kind: theorem)

**Steps:**
1. input: `s_continuous_self_map_of_polyhedron` --[t_auxiliary_construction {object: "induced map on rational homology"}]--> output: `s_induced_map_on_H_star_Q`
2. input: `s_induced_map_on_H_star_Q` --[t_character_decomposition_count {target: alternating_trace_lefschetz_number}]--> output: `s_lefschetz_number_L_f`
3. input: `s_lefschetz_number_L_f` --[t_reductio_ad_absurdum {assume: no_fixed_point_implies_simplicial_approx_with_disjoint_image}]--> output: `s_lefschetz_fixed_point_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_reductio_ad_absurdum

---

### Schauder fixed-point theorem (cite: https://en.wikipedia.org/wiki/Schauder_fixed-point_theorem)

**Axioms:** `s_compact_convex_subset_banach_space`, `s_continuous_self_map_on_convex_compact`
**Terminal:** `s_schauder_fixed_point_theorem` (kind: theorem)

**Steps:**
1. input: `s_continuous_self_map_on_convex_compact` --[t_interpolate_and_continue {parameter: finite_dim_approximation_by_partition_of_unity}]--> output: `s_finite_dim_approx_self_map`
2. input: `s_finite_dim_approx_self_map` --[t_compose_with_identity {with: brouwer_fpt}]--> output: `s_finite_dim_approx_fixed_points`
3. input: `s_finite_dim_approx_fixed_points` --[t_exhaustion_squeeze {limit: weak_limit_of_approximate_fixed_points}]--> output: `s_schauder_fixed_point_theorem`

**Techniques used:** t_interpolate_and_continue, t_compose_with_identity, t_exhaustion_squeeze

---

### Kakutani fixed-point theorem (cite: https://en.wikipedia.org/wiki/Kakutani_fixed-point_theorem)

**Axioms:** `s_compact_convex_subset_R_n`, `s_upper_hemicontinuous_convex_valued_correspondence`
**Terminal:** `s_kakutani_fixed_point_theorem` (kind: theorem)

**Steps:**
1. input: `s_upper_hemicontinuous_convex_valued_correspondence` --[t_interpolate_and_continue {parameter: selection_via_simplicial_approximation}]--> output: `s_continuous_selection_on_simplex`
2. input: `s_continuous_selection_on_simplex` --[t_compose_with_identity {with: brouwer_fpt}]--> output: `s_approximate_fixed_points`
3. input: `s_approximate_fixed_points` --[t_exhaustion_squeeze {limit: graph_closure_fixed_point}]--> output: `s_kakutani_fixed_point_theorem`

**Techniques used:** t_interpolate_and_continue, t_compose_with_identity, t_exhaustion_squeeze

---

### Hairy ball theorem (cite: https://en.wikipedia.org/wiki/Hairy_ball_theorem)

**Axioms:** `s_even_sphere_S_2n`, `s_tangent_vector_field`
**Terminal:** `s_hairy_ball_theorem` (kind: theorem)

**Steps:**
1. input: `s_tangent_vector_field` --[t_reductio_ad_absurdum {assume: nonvanishing_field_exists}]--> output: `s_nonvanishing_field_hypothesis`
2. input: `s_nonvanishing_field_hypothesis` --[t_auxiliary_construction {object: "homotopy of identity to antipodal via field flow"}]--> output: `s_homotopy_id_to_antipodal`
3. input: `s_homotopy_id_to_antipodal` --[t_obstruction_class {class: degree_of_antipodal_map_equals_minus_one_to_n_plus_1}]--> output: `s_hairy_ball_theorem`

**Techniques used:** t_reductio_ad_absurdum, t_auxiliary_construction, t_obstruction_class

---

### Poincaré–Hopf theorem (cite: https://en.wikipedia.org/wiki/Poincar%C3%A9%E2%80%93Hopf_theorem)

**Axioms:** `s_compact_oriented_manifold`, `s_vector_field_with_isolated_zeros`
**Terminal:** `s_poincare_hopf_theorem` (kind: theorem)

**Steps:**
1. input: `s_vector_field_with_isolated_zeros` --[t_auxiliary_construction {object: "local index at each zero via Gauss map"}]--> output: `s_local_index_sum`
2. input: `s_local_index_sum` --[t_obstruction_class {class: euler_class_of_tangent_bundle}]--> output: `s_euler_class_pairing`
3. input: `s_euler_class_pairing` --[t_compose_with_identity {with: euler_class_evaluates_to_chi_M}]--> output: `s_poincare_hopf_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_compose_with_identity

---

### Invariance of domain (cite: https://en.wikipedia.org/wiki/Invariance_of_domain)

**Axioms:** `s_open_subset_R_n`, `s_continuous_injective_map_to_R_n`
**Terminal:** `s_invariance_of_domain` (kind: theorem)

**Steps:**
1. input: `s_continuous_injective_map_to_R_n` --[t_auxiliary_construction {object: "small ball around point, image via Brouwer"}]--> output: `s_local_image_of_small_ball`
2. input: `s_local_image_of_small_ball` --[t_compose_with_identity {with: brouwer_fpt}]--> output: `s_image_contains_interior_ball`
3. input: `s_image_contains_interior_ball` --[t_obstruction_class {class: local_homology_H_n_R_n_R_n_minus_point}]--> output: `s_invariance_of_domain`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_obstruction_class

---

### Jordan curve theorem (cite: https://en.wikipedia.org/wiki/Jordan_curve_theorem)

**Axioms:** `s_simple_closed_curve_in_plane`
**Terminal:** `s_jordan_curve_theorem` (kind: theorem)

**Steps:**
1. input: `s_simple_closed_curve_in_plane` --[t_auxiliary_construction {object: "open complement R²\\γ"}]--> output: `s_complement_of_curve`
2. input: `s_complement_of_curve` --[t_obstruction_class {class: H_0_of_complement_via_alexander_duality}]--> output: `s_two_components_of_complement`
3. input: `s_two_components_of_complement` --[t_compose_with_identity {with: bounded_and_unbounded_component_distinction}]--> output: `s_jordan_curve_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_compose_with_identity

---

### Jordan–Brouwer separation theorem (cite: https://en.wikipedia.org/wiki/Jordan%E2%80%93Brouwer_separation_theorem)

**Axioms:** `s_topological_n_minus_1_sphere_in_R_n`
**Terminal:** `s_jordan_brouwer_separation` (kind: theorem)

**Steps:**
1. input: `s_topological_n_minus_1_sphere_in_R_n` --[t_raise_dimension {target: n_dim_complement}]--> output: `s_n_dim_complement_of_sphere`
2. input: `s_n_dim_complement_of_sphere` --[t_obstruction_class {class: reduced_H_0_via_alexander_duality}]--> output: `s_two_components_via_duality`
3. input: `s_two_components_via_duality` --[t_compose_with_identity {with: bounded_unbounded_distinction}]--> output: `s_jordan_brouwer_separation`

**Techniques used:** t_raise_dimension, t_obstruction_class, t_compose_with_identity

---

### Schoenflies theorem (cite: https://en.wikipedia.org/wiki/Schoenflies_problem)

**Axioms:** `s_jordan_curve_theorem`, `s_simple_closed_curve_in_plane`
**Terminal:** `s_schoenflies_theorem` (kind: theorem)

**Steps:**
1. input: `s_jordan_curve_theorem` --[t_auxiliary_construction {object: "conformal map of unit disk to bounded component (Riemann mapping)"}]--> output: `s_conformal_map_disk_to_inside`
2. input: `s_conformal_map_disk_to_inside` --[t_interpolate_and_continue {parameter: caratheodory_extension_to_boundary}]--> output: `s_extension_to_boundary_homeomorphism`
3. input: `s_extension_to_boundary_homeomorphism` --[t_compose_with_identity {with: glue_inside_and_outside_extensions}]--> output: `s_schoenflies_theorem`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_compose_with_identity

---

### Hex theorem ⇒ Brouwer (cite: https://en.wikipedia.org/wiki/Hex_(board_game))

**Axioms:** `s_hex_board_game`
**Terminal:** `s_hex_theorem` (kind: theorem)

**Steps:**
1. input: `s_hex_board_game` --[t_finite_case_check {target: any_full_coloring_has_winning_chain}]--> output: `s_winning_chain_existence`
2. input: `s_winning_chain_existence` --[t_structural_isomorphism {target: discrete_brouwer_no_retraction}]--> output: `s_hex_theorem`

**Techniques used:** t_finite_case_check, t_structural_isomorphism

---

### Sperner's lemma (cite: https://en.wikipedia.org/wiki/Sperner%27s_lemma)

**Axioms:** `s_simplex_triangulation_with_sperner_labeling`
**Terminal:** `s_sperner_lemma` (kind: theorem)

**Steps:**
1. input: `s_simplex_triangulation_with_sperner_labeling` --[t_finite_case_check {target: count_complete_simplices_mod_2}]--> output: `s_door_counting_argument`
2. input: `s_door_counting_argument` --[t_pigeonhole_collision {dim: parity_argument_on_full_labels}]--> output: `s_odd_number_of_full_simplices`
3. input: `s_odd_number_of_full_simplices` --[t_compose_with_identity {with: at_least_one_full_simplex}]--> output: `s_sperner_lemma`

**Techniques used:** t_finite_case_check, t_pigeonhole_collision, t_compose_with_identity

---

### KKM theorem (Knaster–Kuratowski–Mazurkiewicz) (cite: https://en.wikipedia.org/wiki/Knaster%E2%80%93Kuratowski%E2%80%93Mazurkiewicz_lemma)

**Axioms:** `s_simplex_with_KKM_cover`
**Terminal:** `s_kkm_theorem` (kind: theorem)

**Steps:**
1. input: `s_simplex_with_KKM_cover` --[t_auxiliary_construction {object: "Sperner labeling from KKM cover"}]--> output: `s_sperner_labeled_triangulation_from_cover`
2. input: `s_sperner_labeled_triangulation_from_cover` --[t_compose_with_identity {with: sperner_lemma}]--> output: `s_fully_labeled_small_simplex`
3. input: `s_fully_labeled_small_simplex` --[t_exhaustion_squeeze {limit: refinement_to_intersection_point}]--> output: `s_kkm_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_exhaustion_squeeze

---

### Topological dimension equals covering dimension (cite: https://en.wikipedia.org/wiki/Lebesgue_covering_dimension)

**Axioms:** `s_compact_metric_space`, `s_open_cover_with_orders`
**Terminal:** `s_lebesgue_covering_dimension_R_n_equals_n` (kind: theorem)

**Steps:**
1. input: `s_open_cover_with_orders` --[t_auxiliary_construction {object: "nerve of cover"}]--> output: `s_nerve_of_cover_simplicial_complex`
2. input: `s_nerve_of_cover_simplicial_complex` --[t_compose_with_identity {with: brouwer_fpt_via_KKM}]--> output: `s_no_refinement_below_order_n`
3. input: `s_no_refinement_below_order_n` --[t_compose_with_identity {with: standard_cover_realizes_order_n}]--> output: `s_lebesgue_covering_dimension_R_n_equals_n`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

## III. Fundamental group, covering spaces, van Kampen

### Fundamental group of S¹ is ℤ (cite: https://en.wikipedia.org/wiki/Fundamental_group)

**Axioms:** `s_circle_S_1`, `s_universal_cover_R_to_S_1`
**Terminal:** `s_pi_1_S1_equals_Z` (kind: theorem)

**Steps:**
1. input: `s_universal_cover_R_to_S_1` --[t_auxiliary_construction {object: "path lifting and homotopy lifting"}]--> output: `s_lifted_path_with_integer_endpoint`
2. input: `s_lifted_path_with_integer_endpoint` --[t_obstruction_class {class: winding_number_via_endpoint_lift}]--> output: `s_winding_number_map_pi_1_to_Z`
3. input: `s_winding_number_map_pi_1_to_Z` --[t_structural_isomorphism {target: bijective_well_defined_isomorphism}]--> output: `s_pi_1_S1_equals_Z`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_structural_isomorphism

---

### Fundamental group of S^n trivial for n ≥ 2 (cite: https://en.wikipedia.org/wiki/N-sphere)

**Axioms:** `s_sphere_S_n_n_geq_2`
**Terminal:** `s_pi_1_S_n_trivial` (kind: theorem)

**Steps:**
1. input: `s_sphere_S_n_n_geq_2` --[t_auxiliary_construction {object: "two contractible hemispheres covering S^n"}]--> output: `s_two_hemispheres_cover`
2. input: `s_two_hemispheres_cover` --[t_compose_with_identity {with: van_kampen_with_simply_connected_pieces}]--> output: `s_pi_1_S_n_trivial`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Seifert–van Kampen theorem (cite: https://en.wikipedia.org/wiki/Seifert%E2%80%93Van_Kampen_theorem)

**Axioms:** `s_path_connected_space`, `s_open_cover_by_path_connected_opens_with_path_connected_intersection`
**Terminal:** `s_seifert_van_kampen_theorem` (kind: theorem)

**Steps:**
1. input: `s_open_cover_by_path_connected_opens_with_path_connected_intersection` --[t_auxiliary_construction {object: "pushout/amalgamated free product diagram"}]--> output: `s_pushout_diagram_of_pi_1`
2. input: `s_pushout_diagram_of_pi_1` --[t_lebesgue_number_lemma_application]--> output: `s_loop_decomposition_into_segments_in_pieces`

> _Note: step 2 uses `t_compactness_argument` to subdivide the loop._

2. input: `s_pushout_diagram_of_pi_1` --[t_compactness_argument {target: subdivide_loop_into_pieces}]--> output: `s_loop_decomposition_into_segments_in_pieces`
3. input: `s_loop_decomposition_into_segments_in_pieces` --[t_category_theoretic_colimits_and_adjoints {colimit: pushout_in_groups}]--> output: `s_seifert_van_kampen_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_category_theoretic_colimits_and_adjoints

---

### Universal cover existence (cite: https://en.wikipedia.org/wiki/Covering_space)

**Axioms:** `s_path_connected_locally_simply_connected_space`
**Terminal:** `s_universal_cover_existence` (kind: theorem)

**Steps:**
1. input: `s_path_connected_locally_simply_connected_space` --[t_auxiliary_construction {object: "set of homotopy classes of paths from basepoint"}]--> output: `s_homotopy_class_path_space`
2. input: `s_homotopy_class_path_space` --[t_axiomatize_from_instances {target: lifted_topology_and_projection}]--> output: `s_topologized_path_space_with_projection`
3. input: `s_topologized_path_space_with_projection` --[t_structural_isomorphism {target: simply_connected_covering_space}]--> output: `s_universal_cover_existence`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_structural_isomorphism

---

### Galois correspondence of covering spaces (cite: https://en.wikipedia.org/wiki/Covering_space)

**Axioms:** `s_universal_cover_existence`, `s_fundamental_group`
**Terminal:** `s_covering_space_galois_correspondence` (kind: theorem)

**Steps:**
1. input: `⟨s_universal_cover_existence, s_fundamental_group⟩` --[t_auxiliary_construction {object: "deck transformation group equals pi_1"}]--> output: `s_deck_group_action_on_universal_cover`
2. input: `s_deck_group_action_on_universal_cover` --[t_galois_correspondence {pairing: "subgroups of pi_1 ↔ connected covers"}]--> output: `s_covering_space_galois_correspondence`

**Techniques used:** t_auxiliary_construction, t_galois_correspondence

---

### Nielsen–Schreier theorem (subgroup of free is free) (cite: https://en.wikipedia.org/wiki/Nielsen%E2%80%93Schreier_theorem)

**Axioms:** `s_free_group`, `s_subgroup_of_free_group`
**Terminal:** `s_nielsen_schreier_theorem` (kind: theorem)

**Steps:**
1. input: `s_free_group` --[t_structural_isomorphism {target: pi_1_of_wedge_of_circles}]--> output: `s_free_group_as_pi_1_graph`
2. input: `⟨s_subgroup_of_free_group, s_free_group_as_pi_1_graph⟩` --[t_auxiliary_construction {object: "covering space corresponding to subgroup"}]--> output: `s_covering_graph_for_subgroup`
3. input: `s_covering_graph_for_subgroup` --[t_compose_with_identity {with: pi_1_of_graph_is_free}]--> output: `s_nielsen_schreier_theorem`

**Techniques used:** t_structural_isomorphism, t_auxiliary_construction, t_compose_with_identity

---

### Classification of surfaces (Smale / Brahana) (cite: https://en.wikipedia.org/wiki/Surface_(topology))

**Axioms:** `s_compact_surface_without_boundary`
**Terminal:** `s_classification_of_compact_surfaces` (kind: theorem)

**Steps:**
1. input: `s_compact_surface_without_boundary` --[t_axiomatize_from_instances {target: triangulation_existence_rado}]--> output: `s_triangulated_compact_surface`
2. input: `s_triangulated_compact_surface` --[t_reduce_to_canonical_form {target: 4g_gon_or_2k_gon_polygon_identification}]--> output: `s_polygon_identification_form`
3. input: `s_polygon_identification_form` --[t_finite_case_check {target: orientable_genus_g_or_nonorientable_genus_k}]--> output: `s_classification_of_compact_surfaces`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form, t_finite_case_check

---

## IV. Homology, cohomology, duality

### Eilenberg–Steenrod axioms uniqueness (cite: https://en.wikipedia.org/wiki/Eilenberg%E2%80%93Steenrod_axioms)

**Axioms:** `s_cw_complex_category`, `s_homotopy_excision_dimension_axioms`
**Terminal:** `s_eilenberg_steenrod_uniqueness` (kind: theorem)

**Steps:**
1. input: `s_homotopy_excision_dimension_axioms` --[t_axiomatize_from_instances {target: characterize_homology_on_finite_CW}]--> output: `s_axiom_system_on_finite_cw`
2. input: `s_axiom_system_on_finite_cw` --[t_compactness_argument {target: cellular_filtration_induction}]--> output: `s_inductive_determination_by_cells`
3. input: `s_inductive_determination_by_cells` --[t_structural_isomorphism {target: any_two_theories_naturally_isomorphic}]--> output: `s_eilenberg_steenrod_uniqueness`

**Techniques used:** t_axiomatize_from_instances, t_compactness_argument, t_structural_isomorphism

---

### Mayer–Vietoris sequence (cite: https://en.wikipedia.org/wiki/Mayer%E2%80%93Vietoris_sequence)

**Axioms:** `s_topological_space`, `s_open_cover_X_equals_A_union_B`
**Terminal:** `s_mayer_vietoris_sequence` (kind: theorem)

**Steps:**
1. input: `s_open_cover_X_equals_A_union_B` --[t_auxiliary_construction {object: "short exact sequence of chain complexes 0 → C(A∩B) → C(A)⊕C(B) → C(A+B) → 0"}]--> output: `s_short_exact_chain_sequence`
2. input: `s_short_exact_chain_sequence` --[t_compose_with_identity {with: zig_zag_lemma_long_exact_sequence}]--> output: `s_long_exact_sequence_in_homology`
3. input: `s_long_exact_sequence_in_homology` --[t_compose_with_identity {with: excision_identifies_C_A_plus_B_with_C_X}]--> output: `s_mayer_vietoris_sequence`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Excision theorem (cite: https://en.wikipedia.org/wiki/Excision_theorem)

**Axioms:** `s_topological_pair_X_A`, `s_subset_U_with_closure_in_interior_A`
**Terminal:** `s_excision_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_topological_pair_X_A, s_subset_U_with_closure_in_interior_A⟩` --[t_auxiliary_construction {object: "small chains relative to cover {A, X\\U}"}]--> output: `s_small_chains_subdivision`
2. input: `s_small_chains_subdivision` --[t_compactness_argument {target: barycentric_subdivision_finite_to_make_small}]--> output: `s_subdivision_operator_chain_homotopy`
3. input: `s_subdivision_operator_chain_homotopy` --[t_structural_isomorphism {target: isomorphism_on_relative_homology}]--> output: `s_excision_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_structural_isomorphism

---

### Poincaré duality (cite: https://en.wikipedia.org/wiki/Poincar%C3%A9_duality)

**Axioms:** `s_closed_oriented_n_manifold`
**Terminal:** `s_poincare_duality` (kind: theorem)

**Steps:**
1. input: `s_closed_oriented_n_manifold` --[t_auxiliary_construction {object: "fundamental class [M] in H_n(M;ℤ)"}]--> output: `s_fundamental_class_M`
2. input: `s_fundamental_class_M` --[t_duality {pairing: cap_product_with_fundamental_class}]--> output: `s_cap_product_map_H_k_to_H_n_minus_k`
3. input: `s_cap_product_map_H_k_to_H_n_minus_k` --[t_compose_with_identity {with: mayer_vietoris_induction_on_cover}]--> output: `s_poincare_duality`

**Techniques used:** t_auxiliary_construction, t_duality, t_compose_with_identity

---

### Lefschetz duality (cite: https://en.wikipedia.org/wiki/Lefschetz_duality)

**Axioms:** `s_compact_oriented_manifold_with_boundary`
**Terminal:** `s_lefschetz_duality` (kind: theorem)

**Steps:**
1. input: `s_compact_oriented_manifold_with_boundary` --[t_auxiliary_construction {object: "double of manifold along boundary"}]--> output: `s_double_M_along_boundary`
2. input: `s_double_M_along_boundary` --[t_compose_with_identity {with: poincare_duality_on_double}]--> output: `s_duality_on_double`
3. input: `s_duality_on_double` --[t_duality {pairing: H_k_M_partial_M_with_H_n_minus_k_M}]--> output: `s_lefschetz_duality`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_duality

---

### Alexander duality (cite: https://en.wikipedia.org/wiki/Alexander_duality)

**Axioms:** `s_compact_subset_K_of_S_n`
**Terminal:** `s_alexander_duality` (kind: theorem)

**Steps:**
1. input: `s_compact_subset_K_of_S_n` --[t_auxiliary_construction {object: "complement S^n \\ K"}]--> output: `s_complement_of_K_in_sphere`
2. input: `s_complement_of_K_in_sphere` --[t_compose_with_identity {with: poincare_duality_for_sphere}]--> output: `s_pd_applied_to_complement`
3. input: `s_pd_applied_to_complement` --[t_duality {pairing: reduced_homology_K_with_reduced_cohomology_complement}]--> output: `s_alexander_duality`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_duality

---

### Künneth formula (cite: https://en.wikipedia.org/wiki/K%C3%BCnneth_theorem)

**Axioms:** `s_topological_spaces_X_Y`, `s_pid_coefficients`
**Terminal:** `s_kunneth_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_topological_spaces_X_Y, s_pid_coefficients⟩` --[t_auxiliary_construction {object: "Eilenberg–Zilber cross product on chains"}]--> output: `s_eilenberg_zilber_cross_product`
2. input: `s_eilenberg_zilber_cross_product` --[t_compose_with_identity {with: free_resolution_of_chain_complex}]--> output: `s_tor_short_exact_sequence`
3. input: `s_tor_short_exact_sequence` --[t_structural_isomorphism {target: H_X_tensor_H_Y_plus_Tor_term}]--> output: `s_kunneth_formula`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### Universal coefficient theorem (cite: https://en.wikipedia.org/wiki/Universal_coefficient_theorem)

**Axioms:** `s_chain_complex_of_free_modules`, `s_coefficient_module_G`
**Terminal:** `s_universal_coefficient_theorem` (kind: theorem)

**Steps:**
1. input: `s_chain_complex_of_free_modules` --[t_auxiliary_construction {object: "free resolution of H_*(C) and tensor up"}]--> output: `s_free_resolution_tensor_G`
2. input: `s_free_resolution_tensor_G` --[t_compose_with_identity {with: short_exact_sequence_in_Tor_and_Ext}]--> output: `s_short_exact_with_tor_or_ext`
3. input: `s_short_exact_with_tor_or_ext` --[t_structural_isomorphism {target: split_unnaturally_into_H_otimes_G_and_Tor_or_Ext}]--> output: `s_universal_coefficient_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### Eilenberg–Zilber theorem (cite: https://en.wikipedia.org/wiki/Eilenberg%E2%80%93Zilber_theorem)

**Axioms:** `s_topological_spaces_X_Y`
**Terminal:** `s_eilenberg_zilber_theorem` (kind: theorem)

**Steps:**
1. input: `s_topological_spaces_X_Y` --[t_auxiliary_construction {object: "Alexander–Whitney and Eilenberg–Zilber maps on singular chains of X×Y"}]--> output: `s_AW_EZ_chain_maps`
2. input: `s_AW_EZ_chain_maps` --[t_compose_with_identity {with: acyclic_models_chain_homotopy}]--> output: `s_chain_homotopy_equivalence`
3. input: `s_chain_homotopy_equivalence` --[t_structural_isomorphism {target: C_X_otimes_C_Y_chain_equivalent_to_C_X_times_Y}]--> output: `s_eilenberg_zilber_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### De Rham's theorem (cite: https://en.wikipedia.org/wiki/De_Rham_cohomology)

**Axioms:** `s_smooth_manifold`, `s_de_rham_complex`
**Terminal:** `s_de_rham_theorem` (kind: theorem)

**Steps:**
1. input: `s_de_rham_complex` --[t_auxiliary_construction {object: "integration pairing of forms with singular simplices"}]--> output: `s_integration_pairing_chain_map`
2. input: `s_integration_pairing_chain_map` --[t_compose_with_identity {with: mayer_vietoris_on_de_rham_and_singular}]--> output: `s_mayer_vietoris_both_theories`
3. input: `s_mayer_vietoris_both_theories` --[t_compactness_argument {target: induction_on_good_cover}]--> output: `s_de_rham_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_compactness_argument

---

### Sheaf-theoretic de Rham (Poincaré lemma + sheafification) (cite: https://en.wikipedia.org/wiki/Poincar%C3%A9_lemma)

**Axioms:** `s_smooth_manifold`, `s_de_rham_complex`
**Terminal:** `s_sheaf_de_rham_isomorphism` (kind: theorem)

**Steps:**
1. input: `s_de_rham_complex` --[t_auxiliary_construction {object: "Poincaré lemma: locally Ω* is acyclic resolution of ℝ"}]--> output: `s_poincare_lemma_local_resolution`
2. input: `s_poincare_lemma_local_resolution` --[t_sheafify_on_grothendieck_topology {site: open_cover_topology_of_M}]--> output: `s_sheaf_resolution_of_constant_sheaf`
3. input: `s_sheaf_resolution_of_constant_sheaf` --[t_sheaf_cohomology_bridge {target: H_de_rham_equals_H_M_R}]--> output: `s_sheaf_de_rham_isomorphism`

**Techniques used:** t_auxiliary_construction, t_sheafify_on_grothendieck_topology, t_sheaf_cohomology_bridge

---

### Künneth in cohomology / cup product associativity (cite: https://en.wikipedia.org/wiki/Cup_product)

**Axioms:** `s_singular_cochain_complex`
**Terminal:** `s_cup_product_associative_graded_commutative` (kind: theorem)

**Steps:**
1. input: `s_singular_cochain_complex` --[t_auxiliary_construction {object: "cup product via diagonal approximation"}]--> output: `s_cup_product_definition`
2. input: `s_cup_product_definition` --[t_compose_with_identity {with: associative_and_graded_commutative_up_to_chain_homotopy}]--> output: `s_cup_product_associative_graded_commutative`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Künneth for sheaf cohomology (cite: https://en.wikipedia.org/wiki/K%C3%BCnneth_theorem)

**Axioms:** `s_compact_spaces_with_field_coefficients`
**Terminal:** `s_kunneth_for_sheaves` (kind: theorem)

**Steps:**
1. input: `s_compact_spaces_with_field_coefficients` --[t_sheafify_on_grothendieck_topology {site: product_of_open_covers}]--> output: `s_sheafified_external_product`
2. input: `s_sheafified_external_product` --[t_sheaf_cohomology_bridge {target: derived_tensor_via_cech}]--> output: `s_kunneth_for_sheaves`

**Techniques used:** t_sheafify_on_grothendieck_topology, t_sheaf_cohomology_bridge

---

### Čech-to-singular isomorphism on good covers (cite: https://en.wikipedia.org/wiki/%C4%8Cech_cohomology)

**Axioms:** `s_paracompact_space`, `s_good_cover_with_contractible_intersections`
**Terminal:** `s_cech_singular_iso_good_cover` (kind: theorem)

**Steps:**
1. input: `s_good_cover_with_contractible_intersections` --[t_auxiliary_construction {object: "nerve of cover = simplicial model"}]--> output: `s_nerve_simplicial_model`
2. input: `s_nerve_simplicial_model` --[t_sheafify_on_grothendieck_topology {site: cech_double_complex}]--> output: `s_cech_double_complex`
3. input: `s_cech_double_complex` --[t_sheaf_cohomology_bridge {target: spectral_sequence_collapses}]--> output: `s_cech_singular_iso_good_cover`

**Techniques used:** t_auxiliary_construction, t_sheafify_on_grothendieck_topology, t_sheaf_cohomology_bridge

---

## V. Homotopy theory

### Hurewicz theorem (cite: https://en.wikipedia.org/wiki/Hurewicz_theorem)

**Axioms:** `s_n_connected_space_n_geq_1`
**Terminal:** `s_hurewicz_theorem` (kind: theorem)

**Steps:**
1. input: `s_n_connected_space_n_geq_1` --[t_auxiliary_construction {object: "Hurewicz homomorphism h: π_n → H_n via fundamental class of S^n"}]--> output: `s_hurewicz_homomorphism`
2. input: `s_hurewicz_homomorphism` --[t_compactness_argument {target: cellular_approximation_of_maps_S_n_to_X}]--> output: `s_cellular_representatives`
3. input: `s_cellular_representatives` --[t_structural_isomorphism {target: abelianization_when_n_geq_2_or_isomorphism_above_first_nontrivial}]--> output: `s_hurewicz_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_structural_isomorphism

---

### Whitehead theorem (cite: https://en.wikipedia.org/wiki/Whitehead_theorem)

**Axioms:** `s_cw_complexes_X_Y`, `s_weak_homotopy_equivalence_f`
**Terminal:** `s_whitehead_theorem` (kind: theorem)

**Steps:**
1. input: `s_weak_homotopy_equivalence_f` --[t_obstruction_class {class: obstruction_to_homotopy_lift_in_pi_n_F}]--> output: `s_vanishing_obstructions_in_relative_pi_n`
2. input: `s_vanishing_obstructions_in_relative_pi_n` --[t_compactness_argument {target: cellular_induction_on_skeleton}]--> output: `s_homotopy_inverse_on_skeleta`
3. input: `s_homotopy_inverse_on_skeleta` --[t_compose_with_identity {with: glue_into_homotopy_equivalence}]--> output: `s_whitehead_theorem`

**Techniques used:** t_obstruction_class, t_compactness_argument, t_compose_with_identity

---

### Freudenthal suspension theorem (cite: https://en.wikipedia.org/wiki/Freudenthal_suspension_theorem)

**Axioms:** `s_n_connected_space_X`
**Terminal:** `s_freudenthal_suspension_theorem` (kind: theorem)

**Steps:**
1. input: `s_n_connected_space_X` --[t_auxiliary_construction {object: "suspension functor and map π_k(X) → π_{k+1}(ΣX)"}]--> output: `s_suspension_map_on_pi_k`
2. input: `s_suspension_map_on_pi_k` --[t_raise_dimension {target: cell_attached_via_homotopy_excision_in_range_k_less_2n_plus_1}]--> output: `s_homotopy_excision_range`
3. input: `s_homotopy_excision_range` --[t_structural_isomorphism {target: iso_in_stable_range}]--> output: `s_freudenthal_suspension_theorem`

**Techniques used:** t_auxiliary_construction, t_raise_dimension, t_structural_isomorphism

---

### Blakers–Massey theorem (cite: https://en.wikipedia.org/wiki/Blakers%E2%80%93Massey_theorem)

**Axioms:** `s_pushout_square_in_spaces`, `s_connectivity_hypotheses`
**Terminal:** `s_blakers_massey_theorem` (kind: theorem)

**Steps:**
1. input: `s_pushout_square_in_spaces` --[t_auxiliary_construction {object: "compare pushout with homotopy pushout via mapping cylinder"}]--> output: `s_homotopy_pushout_comparison`
2. input: `s_homotopy_pushout_comparison` --[t_obstruction_class {class: connectivity_of_total_homotopy_fiber}]--> output: `s_total_fiber_connectivity_bound`
3. input: `s_total_fiber_connectivity_bound` --[t_compose_with_identity {with: excision_in_homotopy_in_range}]--> output: `s_blakers_massey_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_compose_with_identity

---

### Cellular approximation theorem (cite: https://en.wikipedia.org/wiki/Cellular_approximation_theorem)

**Axioms:** `s_cw_complexes_X_Y`, `s_continuous_map_f`
**Terminal:** `s_cellular_approximation` (kind: theorem)

**Steps:**
1. input: `s_continuous_map_f` --[t_compactness_argument {target: image_of_n_cell_meets_finitely_many_cells}]--> output: `s_image_meets_finitely_many_cells`
2. input: `s_image_meets_finitely_many_cells` --[t_interpolate_and_continue {parameter: homotope_off_higher_cells_via_smooth_simplex_pushoff}]--> output: `s_homotopy_to_lower_skeleton`
3. input: `s_homotopy_to_lower_skeleton` --[t_compose_with_identity {with: induction_over_skeleta}]--> output: `s_cellular_approximation`

**Techniques used:** t_compactness_argument, t_interpolate_and_continue, t_compose_with_identity

---

### Simplicial approximation theorem (cite: https://en.wikipedia.org/wiki/Simplicial_approximation_theorem)

**Axioms:** `s_simplicial_complexes_K_L`, `s_continuous_map_K_to_L`
**Terminal:** `s_simplicial_approximation` (kind: theorem)

**Steps:**
1. input: `s_continuous_map_K_to_L` --[t_compactness_argument {target: lebesgue_number_for_open_star_cover}]--> output: `s_lebesgue_number_for_open_stars`
2. input: `s_lebesgue_number_for_open_stars` --[t_interpolate_and_continue {parameter: barycentric_subdivision_until_fine}]--> output: `s_finely_subdivided_K`
3. input: `s_finely_subdivided_K` --[t_compose_with_identity {with: vertex_map_via_star_condition}]--> output: `s_simplicial_approximation`

**Techniques used:** t_compactness_argument, t_interpolate_and_continue, t_compose_with_identity

---

### Brown representability theorem (cite: https://en.wikipedia.org/wiki/Brown%27s_representability_theorem)

**Axioms:** `s_homotopy_invariant_functor_on_pointed_cw`, `s_wedge_and_mayer_vietoris_axioms`
**Terminal:** `s_brown_representability` (kind: theorem)

**Steps:**
1. input: `s_wedge_and_mayer_vietoris_axioms` --[t_axiomatize_from_instances {target: half_exact_homotopy_functor}]--> output: `s_half_exact_functor`
2. input: `s_half_exact_functor` --[t_representable_functor_trick {target: classifying_space_Y_via_universal_element}]--> output: `s_classifying_space_Y_universal_element`
3. input: `s_classifying_space_Y_universal_element` --[t_category_theoretic_colimits_and_adjoints {colimit: filtered_colimit_of_finite_cw_pieces}]--> output: `s_brown_representability`

**Techniques used:** t_axiomatize_from_instances, t_representable_functor_trick, t_category_theoretic_colimits_and_adjoints

---

### Postnikov tower existence (cite: https://en.wikipedia.org/wiki/Postnikov_system)

**Axioms:** `s_connected_cw_complex_X`
**Terminal:** `s_postnikov_tower_existence` (kind: theorem)

**Steps:**
1. input: `s_connected_cw_complex_X` --[t_auxiliary_construction {object: "kill higher homotopy by attaching cells in dimension ≥ n+2"}]--> output: `s_X_n_with_pi_k_killed_above_n`
2. input: `s_X_n_with_pi_k_killed_above_n` --[t_obstruction_class {class: k_invariant_in_H_n_plus_2_X_n_minus_1_pi_n}]--> output: `s_k_invariant_obstruction`
3. input: `s_k_invariant_obstruction` --[t_compose_with_identity {with: principal_fibration_construction}]--> output: `s_postnikov_tower_existence`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_compose_with_identity

---

### Eilenberg–MacLane spaces represent cohomology (cite: https://en.wikipedia.org/wiki/Eilenberg%E2%80%93MacLane_space)

**Axioms:** `s_abelian_group_G`, `s_cw_complex_X`
**Terminal:** `s_K_G_n_represents_H_n_G` (kind: theorem)

**Steps:**
1. input: `s_abelian_group_G` --[t_auxiliary_construction {object: "K(G,n) via attaching cells to kill homotopy"}]--> output: `s_K_G_n_space`
2. input: `s_K_G_n_space` --[t_representable_functor_trick {functor: H_n_minus_G}]--> output: `s_K_G_n_represents_H_n_G`

**Techniques used:** t_auxiliary_construction, t_representable_functor_trick

---

### Serre spectral sequence (cite: https://en.wikipedia.org/wiki/Serre_spectral_sequence)

**Axioms:** `s_serre_fibration`, `s_simply_connected_base`
**Terminal:** `s_serre_spectral_sequence` (kind: theorem)

**Steps:**
1. input: `s_serre_fibration` --[t_auxiliary_construction {object: "filter total space by preimages of base skeleta"}]--> output: `s_skeleton_filtration_of_total_space`
2. input: `s_skeleton_filtration_of_total_space` --[t_compose_with_identity {with: exact_couple_to_spectral_sequence}]--> output: `s_exact_couple_E_2_to_E_infinity`
3. input: `s_exact_couple_E_2_to_E_infinity` --[t_structural_isomorphism {target: E_2_equals_H_base_H_fiber}]--> output: `s_serre_spectral_sequence`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### Leray–Hirsch theorem (cite: https://en.wikipedia.org/wiki/Leray%E2%80%93Hirsch_theorem)

**Axioms:** `s_fiber_bundle_F_to_E_to_B`, `s_classes_restrict_to_basis_on_fiber`
**Terminal:** `s_leray_hirsch_theorem` (kind: theorem)

**Steps:**
1. input: `s_classes_restrict_to_basis_on_fiber` --[t_auxiliary_construction {object: "module map H*(B) ⊗ ⟨classes⟩ → H*(E)"}]--> output: `s_external_module_map`
2. input: `s_external_module_map` --[t_compose_with_identity {with: serre_spectral_sequence_collapse_at_E_2}]--> output: `s_leray_hirsch_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Dold–Thom theorem (cite: https://en.wikipedia.org/wiki/Dold%E2%80%93Thom_theorem)

**Axioms:** `s_pointed_cw_complex_X`
**Terminal:** `s_dold_thom_theorem` (kind: theorem)

**Steps:**
1. input: `s_pointed_cw_complex_X` --[t_auxiliary_construction {object: "infinite symmetric product SP(X) = colim Sym^n X"}]--> output: `s_infinite_symmetric_product_SPX`
2. input: `s_infinite_symmetric_product_SPX` --[t_compose_with_identity {with: quasifibration_for_pairs}]--> output: `s_SP_preserves_quasifibrations`
3. input: `s_SP_preserves_quasifibrations` --[t_structural_isomorphism {target: pi_n_SPX_equals_H_n_X}]--> output: `s_dold_thom_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### Eilenberg–Ganea theorem (cite: https://en.wikipedia.org/wiki/Eilenberg%E2%80%93Ganea_theorem)

**Axioms:** `s_discrete_group_G`, `s_cohomological_dimension_n_geq_3`
**Terminal:** `s_eilenberg_ganea_theorem` (kind: theorem)

**Steps:**
1. input: `s_cohomological_dimension_n_geq_3` --[t_auxiliary_construction {object: "build K(G,1) by attaching cells in low dimensions"}]--> output: `s_low_dim_skeleton_of_K_G_1`
2. input: `s_low_dim_skeleton_of_K_G_1` --[t_obstruction_class {class: cohomology_obstruction_to_extending_skeleton}]--> output: `s_vanishing_obstruction_in_high_dim`
3. input: `s_vanishing_obstruction_in_high_dim` --[t_compose_with_identity {with: glue_to_n_dim_K_G_1}]--> output: `s_eilenberg_ganea_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_compose_with_identity

---

### Barratt–Priddy theorem (cite: https://en.wikipedia.org/wiki/Barratt%E2%80%93Priddy_theorem)

**Axioms:** `s_symmetric_groups_Sigma_n`
**Terminal:** `s_barratt_priddy_theorem` (kind: theorem)

**Steps:**
1. input: `s_symmetric_groups_Sigma_n` --[t_auxiliary_construction {object: "BΣ_∞ classifying space"}]--> output: `s_classifying_space_B_sigma_infty`
2. input: `s_classifying_space_B_sigma_infty` --[t_group_complete_exact_category {category: finite_sets}]--> output: `s_plus_construction_B_sigma_infty_plus`
3. input: `s_plus_construction_B_sigma_infty_plus` --[t_structural_isomorphism {target: Omega_infty_S_infty_sphere_spectrum}]--> output: `s_barratt_priddy_theorem`

**Techniques used:** t_auxiliary_construction, t_group_complete_exact_category, t_structural_isomorphism

---

### Milnor exact sequence (lim¹) (cite: https://en.wikipedia.org/wiki/Milnor_sequence)

**Axioms:** `s_inverse_system_of_groups`, `s_tower_of_fibrations`
**Terminal:** `s_milnor_lim_one_exact_sequence` (kind: theorem)

**Steps:**
1. input: `s_tower_of_fibrations` --[t_auxiliary_construction {object: "homotopy inverse limit via mapping telescope"}]--> output: `s_homotopy_inverse_limit_construction`
2. input: `s_homotopy_inverse_limit_construction` --[t_compose_with_identity {with: short_exact_lim_lim_one}]--> output: `s_milnor_lim_one_exact_sequence`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Quillen's theorem A (cite: https://en.wikipedia.org/wiki/Quillen%27s_theorems_A_and_B)

**Axioms:** `s_functor_F_between_small_categories`, `s_comma_categories_contractible`
**Terminal:** `s_quillen_theorem_A` (kind: theorem)

**Steps:**
1. input: `s_comma_categories_contractible` --[t_auxiliary_construction {object: "bisimplicial replacement of F"}]--> output: `s_bisimplicial_replacement`
2. input: `s_bisimplicial_replacement` --[t_category_theoretic_colimits_and_adjoints {colimit: realization_commutes_with_homotopy_colim}]--> output: `s_realization_homotopy_equivalence`
3. input: `s_realization_homotopy_equivalence` --[t_compose_with_identity {with: BF_is_weak_equivalence}]--> output: `s_quillen_theorem_A`

**Techniques used:** t_auxiliary_construction, t_category_theoretic_colimits_and_adjoints, t_compose_with_identity

---

### Adams spectral sequence (cite: https://en.wikipedia.org/wiki/Adams_spectral_sequence)

**Axioms:** `s_spectrum_X`, `s_mod_p_cohomology_with_steenrod_action`
**Terminal:** `s_adams_spectral_sequence` (kind: theorem)

**Steps:**
1. input: `s_mod_p_cohomology_with_steenrod_action` --[t_auxiliary_construction {object: "Adams resolution by HF_p wedge factors"}]--> output: `s_adams_resolution_tower`
2. input: `s_adams_resolution_tower` --[t_frequency_decomposition {target: filtration_by_steenrod_module_resolution}]--> output: `s_E_2_equals_ext_over_steenrod_algebra`
3. input: `s_E_2_equals_ext_over_steenrod_algebra` --[t_structural_isomorphism {target: converges_to_stable_homotopy_p_completed}]--> output: `s_adams_spectral_sequence`

**Techniques used:** t_auxiliary_construction, t_frequency_decomposition, t_structural_isomorphism

---

### Nishida nilpotence theorem (cite: https://en.wikipedia.org/wiki/Nishida%27s_theorem)

**Axioms:** `s_stable_homotopy_groups_of_spheres`, `s_positive_degree_element`
**Terminal:** `s_nishida_nilpotence` (kind: theorem)

**Steps:**
1. input: `s_positive_degree_element` --[t_auxiliary_construction {object: "extended power constructions on x"}]--> output: `s_dyer_lashof_action_on_powers`
2. input: `s_dyer_lashof_action_on_powers` --[t_compose_with_identity {with: kahn_priddy_and_steenrod_relations_force_vanishing}]--> output: `s_x_to_the_N_vanishes`
3. input: `s_x_to_the_N_vanishes` --[t_compose_with_identity {with: every_positive_degree_element_nilpotent}]--> output: `s_nishida_nilpotence`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Hopf invariant one (Adams) (cite: https://en.wikipedia.org/wiki/Hopf_invariant)

**Axioms:** `s_continuous_map_S_2n_minus_1_to_S_n`
**Terminal:** `s_hopf_invariant_one_theorem` (kind: theorem)

**Steps:**
1. input: `s_continuous_map_S_2n_minus_1_to_S_n` --[t_auxiliary_construction {object: "cup product on H*(cofiber Cf) = Hopf invariant"}]--> output: `s_hopf_invariant_H_f`
2. input: `s_hopf_invariant_H_f` --[t_obstruction_class {class: secondary_cohomology_operation_Phi_in_steenrod_algebra}]--> output: `s_secondary_operation_obstruction`
3. input: `s_secondary_operation_obstruction` --[t_compose_with_identity {with: forces_n_in_1_2_4_8}]--> output: `s_hopf_invariant_one_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_compose_with_identity

---

### Vector fields on spheres (Adams) (cite: https://en.wikipedia.org/wiki/Vector_fields_on_spheres)

**Axioms:** `s_sphere_S_n_minus_1`, `s_max_linearly_independent_vector_fields`
**Terminal:** `s_adams_vector_fields_theorem` (kind: theorem)

**Steps:**
1. input: `s_max_linearly_independent_vector_fields` --[t_auxiliary_construction {object: "Stiefel manifold V_k(R^n) and its K-theory"}]--> output: `s_stiefel_manifold_K_theory`
2. input: `s_stiefel_manifold_K_theory` --[t_k_theoretic_index_bridge {target: adams_operations_obstruct_section}]--> output: `s_adams_operation_obstruction_psi_k`
3. input: `s_adams_operation_obstruction_psi_k` --[t_compose_with_identity {with: matches_radon_hurwitz_number}]--> output: `s_adams_vector_fields_theorem`

**Techniques used:** t_auxiliary_construction, t_k_theoretic_index_bridge, t_compose_with_identity

---

### J-homomorphism image (Adams conjecture / Quillen) (cite: https://en.wikipedia.org/wiki/Adams_conjecture)

**Axioms:** `s_real_vector_bundle_xi`, `s_adams_operation_psi_k`
**Terminal:** `s_adams_conjecture_image_of_J` (kind: theorem)

**Steps:**
1. input: `s_real_vector_bundle_xi` --[t_auxiliary_construction {object: "J(ξ): real bundle to stable sphere bundle"}]--> output: `s_J_homomorphism_image`
2. input: `s_J_homomorphism_image` --[t_k_theoretic_index_bridge {target: psi_k_minus_1_kills_J}]--> output: `s_psi_k_minus_1_action`
3. input: `s_psi_k_minus_1_action` --[t_compose_with_identity {with: quillen_etale_cohomology_proof}]--> output: `s_adams_conjecture_image_of_J`

**Techniques used:** t_auxiliary_construction, t_k_theoretic_index_bridge, t_compose_with_identity

---

## VI. Differential topology

### Sard's theorem (cite: https://en.wikipedia.org/wiki/Sard%27s_theorem)

**Axioms:** `s_smooth_map_R_n_to_R_m`
**Terminal:** `s_sard_theorem` (kind: theorem)

**Steps:**
1. input: `s_smooth_map_R_n_to_R_m` --[t_auxiliary_construction {object: "critical set decomposition by rank of Jacobian"}]--> output: `s_rank_stratification_of_critical_set`
2. input: `s_rank_stratification_of_critical_set` --[t_interpolate_and_continue {parameter: taylor_expansion_to_quadratic_order}]--> output: `s_taylor_expansion_critical_neighborhoods`
3. input: `s_taylor_expansion_critical_neighborhoods` --[t_exhaustion_squeeze {limit: measure_of_critical_values_is_zero}]--> output: `s_sard_theorem`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_exhaustion_squeeze

---

### Transversality theorem (cite: https://en.wikipedia.org/wiki/Transversality_theorem)

**Axioms:** `s_smooth_map_f_X_to_Y`, `s_submanifold_Z_of_Y`
**Terminal:** `s_transversality_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_map_f_X_to_Y, s_submanifold_Z_of_Y⟩` --[t_auxiliary_construction {object: "parametrized family of perturbations F: X×P → Y"}]--> output: `s_parametrized_family_F`
2. input: `s_parametrized_family_F` --[t_compose_with_identity {with: sard_theorem_on_projection_to_parameters}]--> output: `s_generic_parameter_makes_f_transverse`
3. input: `s_generic_parameter_makes_f_transverse` --[t_structural_isomorphism {target: transverse_maps_dense_in_C_infty}]--> output: `s_transversality_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### Whitney embedding theorem (cite: https://en.wikipedia.org/wiki/Whitney_embedding_theorem)

**Axioms:** `s_smooth_n_manifold_M`
**Terminal:** `s_whitney_embedding_theorem` (kind: theorem)

**Steps:**
1. input: `s_smooth_n_manifold_M` --[t_auxiliary_construction {object: "immerse into R^{2n+1} via partition of unity and coordinate charts"}]--> output: `s_initial_immersion_into_high_R_N`
2. input: `s_initial_immersion_into_high_R_N` --[t_compose_with_identity {with: sard_to_pick_generic_projection}]--> output: `s_generic_projection_remains_immersion`
3. input: `s_generic_projection_remains_immersion` --[t_compose_with_identity {with: whitney_trick_to_remove_double_points}]--> output: `s_whitney_embedding_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Whitney immersion theorem (cite: https://en.wikipedia.org/wiki/Whitney_immersion_theorem)

**Axioms:** `s_smooth_n_manifold_M`
**Terminal:** `s_whitney_immersion_theorem` (kind: theorem)

**Steps:**
1. input: `s_smooth_n_manifold_M` --[t_auxiliary_construction {object: "obstruction in stable normal bundle"}]--> output: `s_normal_bundle_obstruction_class`
2. input: `s_normal_bundle_obstruction_class` --[t_obstruction_class {class: vanishes_in_dim_2n_minus_1}]--> output: `s_obstruction_vanishes`
3. input: `s_obstruction_vanishes` --[t_compose_with_identity {with: immerses_in_R_2n_minus_1}]--> output: `s_whitney_immersion_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_compose_with_identity

---

### Ehresmann's lemma (cite: https://en.wikipedia.org/wiki/Ehresmann%27s_lemma)

**Axioms:** `s_proper_smooth_submersion_f_M_to_N`
**Terminal:** `s_ehresmann_lemma` (kind: theorem)

**Steps:**
1. input: `s_proper_smooth_submersion_f_M_to_N` --[t_auxiliary_construction {object: "horizontal distribution complementary to ker(df)"}]--> output: `s_horizontal_distribution`
2. input: `s_horizontal_distribution` --[t_physics_to_pde {ode: flow_along_lifts_of_paths}]--> output: `s_flow_lifts_local_trivialization`
3. input: `s_flow_lifts_local_trivialization` --[t_structural_isomorphism {target: smooth_fiber_bundle}]--> output: `s_ehresmann_lemma`

**Techniques used:** t_auxiliary_construction, t_physics_to_pde, t_structural_isomorphism

---

### Frobenius integrability theorem (cite: https://en.wikipedia.org/wiki/Frobenius_theorem_(differential_topology))

**Axioms:** `s_smooth_distribution_D_subset_TM`, `s_involutivity_X_Y_in_D_implies_bracket_in_D`
**Terminal:** `s_frobenius_integrability` (kind: theorem)

**Steps:**
1. input: `s_involutivity_X_Y_in_D_implies_bracket_in_D` --[t_auxiliary_construction {object: "local frame straightening via commuting vector fields"}]--> output: `s_commuting_frame_via_brackets`
2. input: `s_commuting_frame_via_brackets` --[t_physics_to_pde {ode: simultaneous_flow_of_commuting_fields}]--> output: `s_simultaneous_flow_chart`
3. input: `s_simultaneous_flow_chart` --[t_structural_isomorphism {target: foliation_chart}]--> output: `s_frobenius_integrability`

**Techniques used:** t_auxiliary_construction, t_physics_to_pde, t_structural_isomorphism

---

### Morse lemma (cite: https://en.wikipedia.org/wiki/Morse_theory)

**Axioms:** `s_smooth_function_with_nondegenerate_critical_point`
**Terminal:** `s_morse_lemma` (kind: theorem)

**Steps:**
1. input: `s_smooth_function_with_nondegenerate_critical_point` --[t_interpolate_and_continue {parameter: taylor_expansion_at_critical_point}]--> output: `s_quadratic_part_plus_remainder`
2. input: `s_quadratic_part_plus_remainder` --[t_svd_and_spectral_decomposition {target: diagonalize_hessian_into_signature}]--> output: `s_canonical_quadratic_form_in_charts`
3. input: `s_canonical_quadratic_form_in_charts` --[t_reduce_to_canonical_form {target: sum_of_signed_squares}]--> output: `s_morse_lemma`

**Techniques used:** t_interpolate_and_continue, t_svd_and_spectral_decomposition, t_reduce_to_canonical_form

---

### Morse inequalities (cite: https://en.wikipedia.org/wiki/Morse_theory)

**Axioms:** `s_compact_manifold_M_with_morse_function`
**Terminal:** `s_morse_inequalities` (kind: theorem)

**Steps:**
1. input: `s_compact_manifold_M_with_morse_function` --[t_auxiliary_construction {object: "CW structure from sublevel sets attaching k-cell per index-k critical point"}]--> output: `s_morse_cw_decomposition`
2. input: `s_morse_cw_decomposition` --[t_compose_with_identity {with: cellular_homology_bounds_dim_H_k_by_c_k}]--> output: `s_morse_inequalities`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### h-cobordism theorem (Smale) (cite: https://en.wikipedia.org/wiki/H-cobordism)

**Axioms:** `s_simply_connected_h_cobordism_dim_geq_6`
**Terminal:** `s_h_cobordism_theorem` (kind: theorem)

**Steps:**
1. input: `s_simply_connected_h_cobordism_dim_geq_6` --[t_auxiliary_construction {object: "morse function with critical points cancelling in handle decomposition"}]--> output: `s_handle_decomposition_of_cobordism`
2. input: `s_handle_decomposition_of_cobordism` --[t_compose_with_identity {with: whitney_trick_cancels_handles_in_high_dim}]--> output: `s_handles_cancelled`
3. input: `s_handles_cancelled` --[t_structural_isomorphism {target: cobordism_is_product_M_times_I}]--> output: `s_h_cobordism_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### s-cobordism theorem (cite: https://en.wikipedia.org/wiki/S-cobordism_theorem)

**Axioms:** `s_h_cobordism_with_pi_1_nontrivial`, `s_whitehead_torsion_tau`
**Terminal:** `s_s_cobordism_theorem` (kind: theorem)

**Steps:**
1. input: `s_h_cobordism_with_pi_1_nontrivial` --[t_obstruction_class {class: whitehead_torsion_in_Wh_pi_1}]--> output: `s_whitehead_torsion_obstruction`
2. input: `s_whitehead_torsion_obstruction` --[t_compose_with_identity {with: vanishing_torsion_allows_handle_cancellation}]--> output: `s_handles_cancellable_when_tau_zero`
3. input: `s_handles_cancellable_when_tau_zero` --[t_structural_isomorphism {target: product_cobordism_iff_tau_vanishes}]--> output: `s_s_cobordism_theorem`

**Techniques used:** t_obstruction_class, t_compose_with_identity, t_structural_isomorphism

---

### Annulus theorem (high-dim) (cite: https://en.wikipedia.org/wiki/Annulus_theorem)

**Axioms:** `s_two_locally_flat_embedded_spheres_in_R_n_n_geq_5`
**Terminal:** `s_annulus_theorem` (kind: theorem)

**Steps:**
1. input: `s_two_locally_flat_embedded_spheres_in_R_n_n_geq_5` --[t_auxiliary_construction {object: "region between spheres as h-cobordism with simply connected ends"}]--> output: `s_region_as_h_cobordism`
2. input: `s_region_as_h_cobordism` --[t_compose_with_identity {with: h_cobordism_or_s_cobordism_with_pl_topology}]--> output: `s_annulus_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Disc theorem (Palais) (cite: https://en.wikipedia.org/wiki/Disc_theorem)

**Axioms:** `s_connected_smooth_manifold`, `s_two_smooth_embeddings_of_disk_D_n`
**Terminal:** `s_disc_theorem` (kind: theorem)

**Steps:**
1. input: `s_two_smooth_embeddings_of_disk_D_n` --[t_auxiliary_construction {object: "isotopy via flowing along path between basepoints"}]--> output: `s_isotopy_aligning_basepoints`
2. input: `s_isotopy_aligning_basepoints` --[t_compose_with_identity {with: linear_isotopy_in_chart}]--> output: `s_disc_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Pontryagin–Thom construction (cite: https://en.wikipedia.org/wiki/Pontryagin%E2%80%93Thom_construction)

**Axioms:** `s_framed_cobordism_class`
**Terminal:** `s_pontryagin_thom_iso` (kind: theorem)

**Steps:**
1. input: `s_framed_cobordism_class` --[t_auxiliary_construction {object: "collapse map M → Thom space of normal bundle"}]--> output: `s_collapse_map_to_thom_space`
2. input: `s_collapse_map_to_thom_space` --[t_raise_dimension {target: stabilize_to_sphere_spectrum}]--> output: `s_stable_map_to_sphere_spectrum`
3. input: `s_stable_map_to_sphere_spectrum` --[t_structural_isomorphism {target: framed_cobordism_equals_stable_homotopy}]--> output: `s_pontryagin_thom_iso`

**Techniques used:** t_auxiliary_construction, t_raise_dimension, t_structural_isomorphism

---

### Thom transversality theorem (cite: https://en.wikipedia.org/wiki/Thom_transversality_theorem)

**Axioms:** `s_smooth_map_with_jet_extension`, `s_submanifold_W_in_jet_space`
**Terminal:** `s_thom_transversality` (kind: theorem)

**Steps:**
1. input: `s_smooth_map_with_jet_extension` --[t_auxiliary_construction {object: "jet bundle J^k(M,N) and j^k f section"}]--> output: `s_jet_section_construction`
2. input: `s_jet_section_construction` --[t_compose_with_identity {with: transversality_theorem_for_j_k_f}]--> output: `s_thom_transversality`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Cerf's theorem (pseudoisotopy in high dim) (cite: https://en.wikipedia.org/wiki/Pseudoisotopy_theorem)

**Axioms:** `s_simply_connected_smooth_manifold_dim_geq_5`, `s_pseudoisotopy_F`
**Terminal:** `s_cerf_pseudoisotopy_theorem` (kind: theorem)

**Steps:**
1. input: `s_pseudoisotopy_F` --[t_auxiliary_construction {object: "1-parameter family of Morse functions with births and deaths"}]--> output: `s_cerf_graphic_of_critical_points`
2. input: `s_cerf_graphic_of_critical_points` --[t_compose_with_identity {with: handle_slides_and_cancellations_remove_critical_points}]--> output: `s_simplified_to_no_critical_points`
3. input: `s_simplified_to_no_critical_points` --[t_structural_isomorphism {target: pseudoisotopy_is_isotopy}]--> output: `s_cerf_pseudoisotopy_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### Donaldson's theorem (intersection forms of smooth 4-manifolds) (cite: https://en.wikipedia.org/wiki/Donaldson%27s_theorem)

**Axioms:** `s_closed_simply_connected_smooth_4_manifold`, `s_definite_intersection_form`
**Terminal:** `s_donaldson_diagonalizability` (kind: theorem)

**Steps:**
1. input: `s_closed_simply_connected_smooth_4_manifold` --[t_auxiliary_construction {object: "moduli space of anti-self-dual SU(2) instantons"}]--> output: `s_instanton_moduli_space_M`
2. input: `s_instanton_moduli_space_M` --[t_physics_to_pde {ode: yang_mills_anti_self_dual_equation}]--> output: `s_compactified_5_dim_cobordism`
3. input: `s_compactified_5_dim_cobordism` --[t_obstruction_class {class: cone_singularities_force_definite_form_diagonal}]--> output: `s_donaldson_diagonalizability`

**Techniques used:** t_auxiliary_construction, t_physics_to_pde, t_obstruction_class

---

### Exotic R^4 (Freedman+Donaldson) (cite: https://en.wikipedia.org/wiki/Exotic_R4)

**Axioms:** `s_donaldson_diagonalizability`, `s_freedman_topological_4_manifolds`
**Terminal:** `s_exotic_R_4_existence` (kind: theorem)

**Steps:**
1. input: `s_freedman_topological_4_manifolds` --[t_auxiliary_construction {object: "topological E8 manifold from Freedman classification"}]--> output: `s_topological_E8_manifold`
2. input: `s_topological_E8_manifold` --[t_reductio_ad_absurdum {assume: smooth_E8_manifold_exists_violates_donaldson}]--> output: `s_no_smooth_E8_via_donaldson`
3. input: `s_no_smooth_E8_via_donaldson` --[t_compose_with_identity {with: end_periodic_construction_gives_exotic_R_4}]--> output: `s_exotic_R_4_existence`

**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum, t_compose_with_identity

---

### Rokhlin's theorem (cite: https://en.wikipedia.org/wiki/Rokhlin%27s_theorem)

**Axioms:** `s_smooth_closed_oriented_spin_4_manifold`
**Terminal:** `s_rokhlin_theorem` (kind: theorem)

**Steps:**
1. input: `s_smooth_closed_oriented_spin_4_manifold` --[t_auxiliary_construction {object: "Dirac operator and its index"}]--> output: `s_dirac_operator_index_A_hat`
2. input: `s_dirac_operator_index_A_hat` --[t_atiyah_singer_index_machinery {operator: dirac_on_spin_4_manifold}]--> output: `s_index_equals_signature_over_16_with_quaternion_correction`
3. input: `s_index_equals_signature_over_16_with_quaternion_correction` --[t_compose_with_identity {with: integrality_forces_signature_divisible_by_16}]--> output: `s_rokhlin_theorem`

**Techniques used:** t_auxiliary_construction, t_atiyah_singer_index_machinery, t_compose_with_identity

---

### Hirzebruch signature theorem (cite: https://en.wikipedia.org/wiki/Hirzebruch_signature_theorem)

**Axioms:** `s_closed_oriented_4k_manifold`
**Terminal:** `s_hirzebruch_signature_theorem` (kind: theorem)

**Steps:**
1. input: `s_closed_oriented_4k_manifold` --[t_auxiliary_construction {object: "signature operator d+d* on even/odd forms"}]--> output: `s_signature_operator_on_forms`
2. input: `s_signature_operator_on_forms` --[t_atiyah_singer_index_machinery {operator: signature_complex}]--> output: `s_index_equals_L_genus_pairing`
3. input: `s_index_equals_L_genus_pairing` --[t_compose_with_identity {with: index_equals_signature_of_intersection_form}]--> output: `s_hirzebruch_signature_theorem`

**Techniques used:** t_auxiliary_construction, t_atiyah_singer_index_machinery, t_compose_with_identity

---

### Atiyah–Bott fixed-point theorem (cite: https://en.wikipedia.org/wiki/Atiyah%E2%80%93Bott_fixed-point_theorem)

**Axioms:** `s_elliptic_complex`, `s_smooth_endomorphism_with_simple_fixed_points`
**Terminal:** `s_atiyah_bott_fixed_point` (kind: theorem)

**Steps:**
1. input: `s_smooth_endomorphism_with_simple_fixed_points` --[t_auxiliary_construction {object: "Lefschetz number for elliptic complex"}]--> output: `s_elliptic_lefschetz_number`
2. input: `s_elliptic_lefschetz_number` --[t_atiyah_singer_index_machinery {operator: equivariant_elliptic_complex}]--> output: `s_local_contribution_at_fixed_points`
3. input: `s_local_contribution_at_fixed_points` --[t_compose_with_identity {with: sum_of_local_contributions_equals_lefschetz}]--> output: `s_atiyah_bott_fixed_point`

**Techniques used:** t_auxiliary_construction, t_atiyah_singer_index_machinery, t_compose_with_identity

---

### Atiyah–Hirzebruch spectral sequence (cite: https://en.wikipedia.org/wiki/Atiyah%E2%80%93Hirzebruch_spectral_sequence)

**Axioms:** `s_cw_complex_X`, `s_generalized_cohomology_theory_E`
**Terminal:** `s_atiyah_hirzebruch_spectral_sequence` (kind: theorem)

**Steps:**
1. input: `s_cw_complex_X` --[t_auxiliary_construction {object: "skeleton filtration applied to E-cohomology"}]--> output: `s_skeleton_filtration_E_cohomology`
2. input: `s_skeleton_filtration_E_cohomology` --[t_compose_with_identity {with: exact_couple_machinery}]--> output: `s_exact_couple_for_E`
3. input: `s_exact_couple_for_E` --[t_structural_isomorphism {target: E_2_equals_H_X_E_pt}]--> output: `s_atiyah_hirzebruch_spectral_sequence`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### Bott periodicity (complex K-theory) (cite: https://en.wikipedia.org/wiki/Bott_periodicity_theorem)

**Axioms:** `s_unitary_group_U_infinity`
**Terminal:** `s_bott_periodicity_complex` (kind: theorem)

**Steps:**
1. input: `s_unitary_group_U_infinity` --[t_auxiliary_construction {object: "loop space ΩU and Morse theory of energy functional"}]--> output: `s_morse_theory_on_loop_space_U`
2. input: `s_morse_theory_on_loop_space_U` --[t_obstruction_class {class: critical_points_index_geq_2}]--> output: `s_handle_decomposition_BU_times_Z`
3. input: `s_handle_decomposition_BU_times_Z` --[t_structural_isomorphism {target: Omega_squared_BU_homotopy_equiv_BU_times_Z}]--> output: `s_bott_periodicity_complex`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_structural_isomorphism

---

### Bott periodicity (real K-theory, period 8) (cite: https://en.wikipedia.org/wiki/Bott_periodicity_theorem)

**Axioms:** `s_orthogonal_group_O_infinity`, `s_clifford_algebra_Cl_k`
**Terminal:** `s_bott_periodicity_real` (kind: theorem)

**Steps:**
1. input: `s_clifford_algebra_Cl_k` --[t_axiomatize_from_instances {target: clifford_algebra_8_periodicity}]--> output: `s_clifford_8_periodicity`
2. input: `s_clifford_8_periodicity` --[t_compose_with_identity {with: morse_theory_on_loop_O_infinity}]--> output: `s_homotopy_of_loop_O`
3. input: `s_homotopy_of_loop_O` --[t_structural_isomorphism {target: Omega_8_BO_homotopy_equiv_BO_times_Z}]--> output: `s_bott_periodicity_real`

**Techniques used:** t_axiomatize_from_instances, t_compose_with_identity, t_structural_isomorphism

---

### Atiyah–Segal completion theorem (cite: https://en.wikipedia.org/wiki/Atiyah%E2%80%93Segal_completion_theorem)

**Axioms:** `s_compact_lie_group_G`, `s_representation_ring_R_G`
**Terminal:** `s_atiyah_segal_completion` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_lie_group_G, s_representation_ring_R_G⟩` --[t_auxiliary_construction {object: "equivariant K-theory of EG and Borel construction"}]--> output: `s_equivariant_K_theory_EG`
2. input: `s_equivariant_K_theory_EG` --[t_k_theoretic_index_bridge {target: completion_at_augmentation_ideal_I}]--> output: `s_I_adic_completion_K_G`
3. input: `s_I_adic_completion_K_G` --[t_structural_isomorphism {target: K_BG_equals_R_G_hat}]--> output: `s_atiyah_segal_completion`

**Techniques used:** t_auxiliary_construction, t_k_theoretic_index_bridge, t_structural_isomorphism

---

### Kuiper's theorem (cite: https://en.wikipedia.org/wiki/Kuiper%27s_theorem)

**Axioms:** `s_infinite_dimensional_hilbert_space`, `s_unitary_group_U_H`
**Terminal:** `s_kuiper_theorem` (kind: theorem)

**Steps:**
1. input: `s_unitary_group_U_H` --[t_auxiliary_construction {object: "explicit contraction via Eilenberg swindle"}]--> output: `s_eilenberg_swindle_homotopy`
2. input: `s_eilenberg_swindle_homotopy` --[t_contraction_fixed_point {space: U_H, factor: continuous_deformation_to_identity}]--> output: `s_U_H_contractible`
3. input: `s_U_H_contractible` --[t_compose_with_identity {with: classifying_space_PU_H_is_K_Z_2}]--> output: `s_kuiper_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_compose_with_identity

---

### Quillen–Suslin theorem (Serre's conjecture) (cite: https://en.wikipedia.org/wiki/Quillen%E2%80%93Suslin_theorem)

**Axioms:** `s_finitely_generated_projective_module_over_polynomial_ring_k_x_1_x_n`
**Terminal:** `s_quillen_suslin_theorem` (kind: theorem)

**Steps:**
1. input: `s_finitely_generated_projective_module_over_polynomial_ring_k_x_1_x_n` --[t_auxiliary_construction {object: "Horrocks-type patching of projective modules over k[t][x]_{x}"}]--> output: `s_local_freeness_patching`
2. input: `s_local_freeness_patching` --[t_infinite_descent {parameter: reduce_to_one_variable_via_specialization}]--> output: `s_descent_to_one_variable_case`
3. input: `s_descent_to_one_variable_case` --[t_compose_with_identity {with: PID_makes_projective_free}]--> output: `s_quillen_suslin_theorem`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_compose_with_identity

---

## VII. 3-manifolds, geometric/algebraic structures (closure-of-classics)

### Loop theorem (Papakyriakopoulos) (cite: https://en.wikipedia.org/wiki/Loop_theorem)

**Axioms:** `s_3_manifold_M_with_boundary`, `s_essential_loop_in_boundary`
**Terminal:** `s_loop_theorem` (kind: theorem)

**Steps:**
1. input: `s_essential_loop_in_boundary` --[t_auxiliary_construction {object: "tower of branched covers (Papakyriakopoulos tower)"}]--> output: `s_tower_of_branched_covers`
2. input: `s_tower_of_branched_covers` --[t_infinite_descent {parameter: each_level_strictly_simpler}]--> output: `s_terminal_tower_with_embedded_disk`
3. input: `s_terminal_tower_with_embedded_disk` --[t_compose_with_identity {with: project_disk_back_to_M}]--> output: `s_loop_theorem`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_compose_with_identity

---

### Sphere theorem (3-manifolds) (cite: https://en.wikipedia.org/wiki/Sphere_theorem_(3-manifolds))

**Axioms:** `s_orientable_3_manifold_M_with_pi_2_nontrivial`
**Terminal:** `s_sphere_theorem_3_manifolds` (kind: theorem)

**Steps:**
1. input: `s_orientable_3_manifold_M_with_pi_2_nontrivial` --[t_auxiliary_construction {object: "least area sphere in homotopy class (Papakyriakopoulos tower)"}]--> output: `s_least_area_sphere_representative`
2. input: `s_least_area_sphere_representative` --[t_infinite_descent {parameter: reduce_self_intersections_via_tower}]--> output: `s_embedded_essential_sphere`
3. input: `s_embedded_essential_sphere` --[t_compose_with_identity {with: generator_of_pi_2_realized_embedded}]--> output: `s_sphere_theorem_3_manifolds`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_compose_with_identity

---

### Lickorish–Wallace theorem (cite: https://en.wikipedia.org/wiki/Lickorish%E2%80%93Wallace_theorem)

**Axioms:** `s_closed_orientable_3_manifold`
**Terminal:** `s_lickorish_wallace_theorem` (kind: theorem)

**Steps:**
1. input: `s_closed_orientable_3_manifold` --[t_auxiliary_construction {object: "Heegaard splitting"}]--> output: `s_heegaard_splitting`
2. input: `s_heegaard_splitting` --[t_reduce_to_canonical_form {target: dehn_surgery_on_link_in_S_3}]--> output: `s_dehn_surgery_description`
3. input: `s_dehn_surgery_description` --[t_compose_with_identity {with: integer_surgery_via_lickorish_twists}]--> output: `s_lickorish_wallace_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_compose_with_identity

---

### Gordon–Luecke theorem (knot complements determine knots) (cite: https://en.wikipedia.org/wiki/Gordon%E2%80%93Luecke_theorem)

**Axioms:** `s_knot_K_in_S_3`, `s_knot_complement_S_3_minus_K`
**Terminal:** `s_gordon_luecke_theorem` (kind: theorem)

**Steps:**
1. input: `s_knot_complement_S_3_minus_K` --[t_reductio_ad_absurdum {assume: nontrivial_dehn_surgery_yields_S_3}]--> output: `s_hypothetical_nontrivial_surgery_giving_S_3`
2. input: `s_hypothetical_nontrivial_surgery_giving_S_3` --[t_auxiliary_construction {object: "minimal surface / planar surface analysis in complement"}]--> output: `s_planar_surface_obstruction`
3. input: `s_planar_surface_obstruction` --[t_compose_with_identity {with: only_trivial_surgery_yields_S_3}]--> output: `s_gordon_luecke_theorem`

**Techniques used:** t_reductio_ad_absurdum, t_auxiliary_construction, t_compose_with_identity

---

### Nielsen–Thurston classification (cite: https://en.wikipedia.org/wiki/Nielsen%E2%80%93Thurston_classification)

**Axioms:** `s_mapping_class_of_closed_surface_genus_geq_2`
**Terminal:** `s_nielsen_thurston_classification` (kind: theorem)

**Steps:**
1. input: `s_mapping_class_of_closed_surface_genus_geq_2` --[t_auxiliary_construction {object: "action on Teichmüller space"}]--> output: `s_action_on_teichmuller_space`
2. input: `s_action_on_teichmuller_space` --[t_finite_case_check {cases: periodic_reducible_pseudo_anosov}]--> output: `s_trichotomy_of_actions`
3. input: `s_trichotomy_of_actions` --[t_structural_isomorphism {target: canonical_representative_in_each_class}]--> output: `s_nielsen_thurston_classification`

**Techniques used:** t_auxiliary_construction, t_finite_case_check, t_structural_isomorphism

---

### Mostow rigidity (cite: https://en.wikipedia.org/wiki/Mostow_rigidity_theorem)

**Axioms:** `s_complete_finite_volume_hyperbolic_n_manifold_n_geq_3`
**Terminal:** `s_mostow_rigidity` (kind: theorem)

**Steps:**
1. input: `s_complete_finite_volume_hyperbolic_n_manifold_n_geq_3` --[t_auxiliary_construction {object: "boundary extension of pi_1-equivariant quasi-isometry"}]--> output: `s_boundary_quasi_isometry`
2. input: `s_boundary_quasi_isometry` --[t_ergodic_correspondence {dynamics: pi_1_action_on_sphere_at_infinity}]--> output: `s_mobius_extension_on_S_n_minus_1`
3. input: `s_mobius_extension_on_S_n_minus_1` --[t_structural_isomorphism {target: isometry_of_hyperbolic_n_space}]--> output: `s_mostow_rigidity`

**Techniques used:** t_auxiliary_construction, t_ergodic_correspondence, t_structural_isomorphism

---

### Smale's theorem on 2-sphere diffeomorphisms (cite: https://en.wikipedia.org/wiki/Smale_conjecture)

**Axioms:** `s_diffeomorphism_group_of_S_2`
**Terminal:** `s_smale_diff_S_2_homotopy_equiv_O_3` (kind: theorem)

**Steps:**
1. input: `s_diffeomorphism_group_of_S_2` --[t_auxiliary_construction {object: "fiber bundle Diff(S^2) → Frames(S^2) ≃ SO(3)"}]--> output: `s_diff_S2_as_fiber_bundle`
2. input: `s_diff_S2_as_fiber_bundle` --[t_compose_with_identity {with: fiber_is_contractible_via_smale}]--> output: `s_smale_diff_S_2_homotopy_equiv_O_3`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Smale conjecture for S³ (Hatcher) (cite: https://en.wikipedia.org/wiki/Smale_conjecture)

**Axioms:** `s_diffeomorphism_group_of_S_3`
**Terminal:** `s_hatcher_smale_conjecture_S_3` (kind: theorem)

**Steps:**
1. input: `s_diffeomorphism_group_of_S_3` --[t_auxiliary_construction {object: "space of unknotted incompressible tori or 2-spheres"}]--> output: `s_space_of_unknotted_2_spheres`
2. input: `s_space_of_unknotted_2_spheres` --[t_compose_with_identity {with: hatcher_parametrized_dehn_lemma}]--> output: `s_contractibility_of_space_of_spheres`
3. input: `s_contractibility_of_space_of_spheres` --[t_structural_isomorphism {target: Diff_S_3_homotopy_equiv_O_4}]--> output: `s_hatcher_smale_conjecture_S_3`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### Double suspension theorem (Edwards–Cannon) (cite: https://en.wikipedia.org/wiki/Double_suspension_theorem)

**Axioms:** `s_homology_3_sphere_H`
**Terminal:** `s_double_suspension_theorem` (kind: theorem)

**Steps:**
1. input: `s_homology_3_sphere_H` --[t_raise_dimension {target: suspension_to_4_dim}]--> output: `s_single_suspension_with_two_singular_points`
2. input: `s_single_suspension_with_two_singular_points` --[t_raise_dimension {target: second_suspension_to_5_dim}]--> output: `s_double_suspension_S_5_topologically`
3. input: `s_double_suspension_S_5_topologically` --[t_compose_with_identity {with: shrinking_decomposition_theorem}]--> output: `s_double_suspension_theorem`

**Techniques used:** t_raise_dimension, t_compose_with_identity

---

### Bing's recognition theorem for S³ (cite: https://en.wikipedia.org/wiki/Bing%27s_recognition_theorem)

**Axioms:** `s_compact_3_manifold_with_simply_connected_sphere_property`
**Terminal:** `s_bing_recognition_theorem` (kind: theorem)

**Steps:**
1. input: `s_compact_3_manifold_with_simply_connected_sphere_property` --[t_axiomatize_from_instances {target: every_simple_closed_curve_lies_in_3_cell}]--> output: `s_curve_in_3_cell_condition`
2. input: `s_curve_in_3_cell_condition` --[t_compactness_argument {target: exhaust_by_3_cells_with_shrinking}]--> output: `s_exhaustion_by_3_cells`
3. input: `s_exhaustion_by_3_cells` --[t_structural_isomorphism {target: homeomorphism_to_S_3}]--> output: `s_bing_recognition_theorem`

**Techniques used:** t_axiomatize_from_instances, t_compactness_argument, t_structural_isomorphism

---

### Fáry–Milnor theorem (cite: https://en.wikipedia.org/wiki/F%C3%A1ry%E2%80%93Milnor_theorem)

**Axioms:** `s_smooth_closed_curve_in_R_3_with_total_curvature_leq_4pi`
**Terminal:** `s_fary_milnor_theorem` (kind: theorem)

**Steps:**
1. input: `s_smooth_closed_curve_in_R_3_with_total_curvature_leq_4pi` --[t_auxiliary_construction {object: "crofton-type integral over projections"}]--> output: `s_average_number_of_crossings_per_projection`
2. input: `s_average_number_of_crossings_per_projection` --[t_pigeonhole_collision {dim: at_least_one_projection_with_geq_2_maxima}]--> output: `s_projection_with_few_extrema`
3. input: `s_projection_with_few_extrema` --[t_compose_with_identity {with: low_bridge_number_implies_unknotted}]--> output: `s_fary_milnor_theorem`

**Techniques used:** t_auxiliary_construction, t_pigeonhole_collision, t_compose_with_identity

---

### Reeb sphere theorem (cite: https://en.wikipedia.org/wiki/Reeb_sphere_theorem)

**Axioms:** `s_closed_n_manifold_with_morse_function_with_exactly_2_critical_points`
**Terminal:** `s_reeb_sphere_theorem` (kind: theorem)

**Steps:**
1. input: `s_closed_n_manifold_with_morse_function_with_exactly_2_critical_points` --[t_auxiliary_construction {object: "morse handle decomposition: one 0-handle, one n-handle"}]--> output: `s_two_disk_decomposition`
2. input: `s_two_disk_decomposition` --[t_compose_with_identity {with: union_of_two_disks_is_homeomorphic_to_sphere}]--> output: `s_reeb_sphere_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Phragmén–Brouwer theorem (cite: https://en.wikipedia.org/wiki/Phragmen%E2%80%93Brouwer_theorem)

**Axioms:** `s_connected_locally_connected_normal_space`, `s_two_separating_continua`
**Terminal:** `s_phragmen_brouwer_theorem` (kind: theorem)

**Steps:**
1. input: `s_two_separating_continua` --[t_auxiliary_construction {object: "irreducible separation between two points"}]--> output: `s_irreducible_separator`
2. input: `s_irreducible_separator` --[t_reductio_ad_absurdum {assume: union_does_not_separate_yet_each_does}]--> output: `s_contradicting_pair_of_continua`
3. input: `s_contradicting_pair_of_continua` --[t_compose_with_identity {with: properties_of_irreducible_separator}]--> output: `s_phragmen_brouwer_theorem`

**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum, t_compose_with_identity

---

### Geometrization / Thurston for Haken manifolds (cite: https://en.wikipedia.org/wiki/Geometrization_conjecture)

**Axioms:** `s_haken_3_manifold`
**Terminal:** `s_thurston_geometrization_haken` (kind: theorem)

**Steps:**
1. input: `s_haken_3_manifold` --[t_auxiliary_construction {object: "JSJ decomposition into Seifert-fibered and atoroidal pieces"}]--> output: `s_jsj_decomposition`
2. input: `s_jsj_decomposition` --[t_compose_with_identity {with: thurston_hyperbolization_for_atoroidal_pieces}]--> output: `s_hyperbolic_structures_on_atoroidal_pieces`
3. input: `s_hyperbolic_structures_on_atoroidal_pieces` --[t_compose_with_identity {with: glue_geometric_pieces}]--> output: `s_thurston_geometrization_haken`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Smith conjecture (cite: https://en.wikipedia.org/wiki/Smith_conjecture)

**Axioms:** `s_finite_cyclic_smooth_action_on_S_3_with_nonempty_fixed_set`
**Terminal:** `s_smith_conjecture` (kind: theorem)

**Steps:**
1. input: `s_finite_cyclic_smooth_action_on_S_3_with_nonempty_fixed_set` --[t_auxiliary_construction {object: "fixed set is an embedded circle (knot)"}]--> output: `s_fixed_circle_K`
2. input: `s_fixed_circle_K` --[t_compose_with_identity {with: thurston_geometrization_of_quotient_orbifold}]--> output: `s_quotient_orbifold_geometric`
3. input: `s_quotient_orbifold_geometric` --[t_structural_isomorphism {target: K_is_unknotted_and_action_is_standard}]--> output: `s_smith_conjecture`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### Tameness theorem (Agol–Calegari–Gabai) (cite: https://en.wikipedia.org/wiki/Tameness_theorem)

**Axioms:** `s_hyperbolic_3_manifold_with_finitely_generated_pi_1`
**Terminal:** `s_tameness_theorem` (kind: theorem)

**Steps:**
1. input: `s_hyperbolic_3_manifold_with_finitely_generated_pi_1` --[t_auxiliary_construction {object: "end of manifold and shrinkwrapping minimal surfaces"}]--> output: `s_shrinkwrapped_minimal_surfaces`
2. input: `s_shrinkwrapped_minimal_surfaces` --[t_exhaustion_squeeze {limit: exhaustion_by_compact_cores}]--> output: `s_exhaustion_by_compact_cores`
3. input: `s_exhaustion_by_compact_cores` --[t_structural_isomorphism {target: topologically_tame_homeomorphism_with_compact_interior_of_compact_3_mfd}]--> output: `s_tameness_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_structural_isomorphism

---

### Surface subgroup theorem (Kahn–Markovic) (cite: https://en.wikipedia.org/wiki/Surface_subgroup_theorem)

**Axioms:** `s_closed_hyperbolic_3_manifold`
**Terminal:** `s_kahn_markovic_surface_subgroup` (kind: theorem)

**Steps:**
1. input: `s_closed_hyperbolic_3_manifold` --[t_auxiliary_construction {object: "many nearly-geodesic pairs of pants assembled via mixing"}]--> output: `s_collection_of_pants`
2. input: `s_collection_of_pants` --[t_ergodic_correspondence {dynamics: frame_flow_mixing}]--> output: `s_pants_pair_gluing_compatible`
3. input: `s_pants_pair_gluing_compatible` --[t_compose_with_identity {with: pants_assemble_to_quasi_fuchsian_surface}]--> output: `s_kahn_markovic_surface_subgroup`

**Techniques used:** t_auxiliary_construction, t_ergodic_correspondence, t_compose_with_identity

---

### Virtually Haken theorem (Agol) (cite: https://en.wikipedia.org/wiki/Virtually_Haken_conjecture)

**Axioms:** `s_kahn_markovic_surface_subgroup`, `s_closed_hyperbolic_3_manifold`
**Terminal:** `s_virtually_haken_theorem` (kind: theorem)

**Steps:**
1. input: `s_kahn_markovic_surface_subgroup` --[t_auxiliary_construction {object: "cube complex dual to surface subgroup family"}]--> output: `s_dual_cube_complex_action`
2. input: `s_dual_cube_complex_action` --[t_compose_with_identity {with: agol_virtual_specialness_via_haglund_wise}]--> output: `s_finite_index_special_cover`
3. input: `s_finite_index_special_cover` --[t_structural_isomorphism {target: finite_cover_contains_embedded_incompressible_surface}]--> output: `s_virtually_haken_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### Sullivan's structure theorem on rational homotopy (cite: https://en.wikipedia.org/wiki/Rational_homotopy_theory)

**Axioms:** `s_simply_connected_space_X_finite_type`
**Terminal:** `s_sullivan_minimal_model_theorem` (kind: theorem)

**Steps:**
1. input: `s_simply_connected_space_X_finite_type` --[t_auxiliary_construction {object: "Sullivan polynomial differential forms A_PL(X)"}]--> output: `s_PL_de_rham_algebra`
2. input: `s_PL_de_rham_algebra` --[t_reduce_to_canonical_form {target: minimal_free_CDGA_model}]--> output: `s_sullivan_minimal_model`
3. input: `s_sullivan_minimal_model` --[t_structural_isomorphism {target: rational_homotopy_groups_from_indecomposables}]--> output: `s_sullivan_minimal_model_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_structural_isomorphism

---

### Andreotti–Frankel theorem (cite: https://en.wikipedia.org/wiki/Andreotti%E2%80%93Frankel_theorem)

**Axioms:** `s_smooth_affine_complex_variety_complex_dimension_n`
**Terminal:** `s_andreotti_frankel_theorem` (kind: theorem)

**Steps:**
1. input: `s_smooth_affine_complex_variety_complex_dimension_n` --[t_auxiliary_construction {object: "real distance squared function from generic point"}]--> output: `s_real_distance_squared_morse_function`
2. input: `s_real_distance_squared_morse_function` --[t_obstruction_class {class: index_of_critical_points_leq_n}]--> output: `s_index_bound_on_critical_points`
3. input: `s_index_bound_on_critical_points` --[t_compose_with_identity {with: morse_inequalities_give_homotopy_type_of_n_complex}]--> output: `s_andreotti_frankel_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_compose_with_identity

---

### Lefschetz hyperplane theorem (cite: https://en.wikipedia.org/wiki/Lefschetz_hyperplane_theorem)

**Axioms:** `s_smooth_projective_variety_X`, `s_smooth_hyperplane_section_Y`
**Terminal:** `s_lefschetz_hyperplane_theorem` (kind: theorem)

**Steps:**
1. input: `s_smooth_hyperplane_section_Y` --[t_auxiliary_construction {object: "Morse function on X\\Y inherited from affine variety"}]--> output: `s_morse_on_affine_complement`
2. input: `s_morse_on_affine_complement` --[t_compose_with_identity {with: andreotti_frankel_on_complement}]--> output: `s_complement_has_homotopy_type_of_n_complex`
3. input: `s_complement_has_homotopy_type_of_n_complex` --[t_structural_isomorphism {target: pair_X_Y_n_minus_1_connected}]--> output: `s_lefschetz_hyperplane_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### Hodge decomposition theorem (cite: https://en.wikipedia.org/wiki/Hodge_theory)

**Axioms:** `s_compact_kahler_manifold`
**Terminal:** `s_hodge_decomposition_theorem` (kind: theorem)

**Steps:**
1. input: `s_compact_kahler_manifold` --[t_auxiliary_construction {object: "Laplacian Δ on forms and its harmonic kernel"}]--> output: `s_harmonic_forms_kernel_of_Laplacian`
2. input: `s_harmonic_forms_kernel_of_Laplacian` --[t_svd_and_spectral_decomposition {operator: laplacian_on_forms}]--> output: `s_hodge_orthogonal_decomposition`
3. input: `s_hodge_orthogonal_decomposition` --[t_structural_isomorphism {target: H_n_X_C_equals_direct_sum_H_p_q}]--> output: `s_hodge_decomposition_theorem`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_structural_isomorphism

---

### Atiyah–Singer index theorem ⚠ SKIPPED — present in graph as `s_atiyah_singer_index_theorem` (`t_atiyah_singer_index_machinery`).

---

### Hodge index theorem (cite: https://en.wikipedia.org/wiki/Hodge_index_theorem)

**Axioms:** `s_smooth_projective_surface_X`
**Terminal:** `s_hodge_index_theorem` (kind: theorem)

**Steps:**
1. input: `s_smooth_projective_surface_X` --[t_auxiliary_construction {object: "intersection pairing on H^2(X;ℝ)"}]--> output: `s_intersection_pairing_on_H_2`
2. input: `s_intersection_pairing_on_H_2` --[t_svd_and_spectral_decomposition {target: signature_via_kahler_form_orthogonal_complement}]--> output: `s_signature_of_intersection_pairing`
3. input: `s_signature_of_intersection_pairing` --[t_compose_with_identity {with: signature_is_1_n_minus_1}]--> output: `s_hodge_index_theorem`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_compose_with_identity

---

### Smale's classification of compact 2-manifolds (gradient flow) (cite: https://en.wikipedia.org/wiki/Surface_(topology))

**Axioms:** `s_closed_surface_with_morse_function`
**Terminal:** `s_smale_2_manifold_classification` (kind: theorem)

**Steps:**
1. input: `s_closed_surface_with_morse_function` --[t_auxiliary_construction {object: "gradient flow yields handle decomposition"}]--> output: `s_handle_decomposition_of_surface`
2. input: `s_handle_decomposition_of_surface` --[t_reduce_to_canonical_form {target: standard_form_with_one_0_handle_and_one_2_handle}]--> output: `s_canonical_genus_handle_form`
3. input: `s_canonical_genus_handle_form` --[t_compose_with_identity {with: classification_of_compact_surfaces}]--> output: `s_smale_2_manifold_classification`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_compose_with_identity

---

### Quillen +-construction and algebraic K-theory (cite: https://en.wikipedia.org/wiki/Algebraic_K-theory)

**Axioms:** `s_associative_ring_R`, `s_classifying_space_BGL_R`
**Terminal:** `s_quillen_plus_construction_K_theory` (kind: theorem)

**Steps:**
1. input: `s_classifying_space_BGL_R` --[t_auxiliary_construction {object: "+-construction: attach cells to kill commutator subgroup of pi_1"}]--> output: `s_BGL_R_plus_simply_connected_in_pi_1_quotient`
2. input: `s_BGL_R_plus_simply_connected_in_pi_1_quotient` --[t_group_complete_exact_category {category: finitely_generated_projective_R_modules}]--> output: `s_group_completion_yields_K_R_spectrum`
3. input: `s_group_completion_yields_K_R_spectrum` --[t_structural_isomorphism {target: K_n_R_equals_pi_n_BGL_R_plus_for_n_geq_1}]--> output: `s_quillen_plus_construction_K_theory`

**Techniques used:** t_auxiliary_construction, t_group_complete_exact_category, t_structural_isomorphism

---

### Snaith's theorem (cite: https://en.wikipedia.org/wiki/Snaith%27s_theorem)

**Axioms:** `s_infinite_loop_space_CP_infinity`, `s_bott_element_beta_in_K_0`
**Terminal:** `s_snaith_theorem` (kind: theorem)

**Steps:**
1. input: `s_infinite_loop_space_CP_infinity` --[t_auxiliary_construction {object: "Σ^∞_+ CP^∞ with Bott element inverted"}]--> output: `s_sigma_infty_CP_infty_bott_inverted`
2. input: `s_sigma_infty_CP_infty_bott_inverted` --[t_k_theoretic_index_bridge {target: identifies_with_periodic_K_theory_spectrum}]--> output: `s_snaith_theorem`

**Techniques used:** t_auxiliary_construction, t_k_theoretic_index_bridge

---

### Anderson–Kadec theorem (cite: https://en.wikipedia.org/wiki/Anderson%E2%80%93Kadec_theorem)

**Axioms:** `s_infinite_dimensional_separable_frechet_space`
**Terminal:** `s_anderson_kadec_theorem` (kind: theorem)

**Steps:**
1. input: `s_infinite_dimensional_separable_frechet_space` --[t_auxiliary_construction {object: "extension of Bessaga–Pełczyński coordinate maps"}]--> output: `s_coordinate_maps_to_R_infty`
2. input: `s_coordinate_maps_to_R_infty` --[t_structural_isomorphism {target: homeomorphic_to_R_infty}]--> output: `s_anderson_kadec_theorem`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism

---

### Kuratowski 14-set theorem (cite: https://en.wikipedia.org/wiki/Kuratowski%27s_closure-complement_problem)

**Axioms:** `s_topological_space`, `s_subset_A_of_X`
**Terminal:** `s_kuratowski_14_set_theorem` (kind: theorem)

**Steps:**
1. input: `s_subset_A_of_X` --[t_auxiliary_construction {object: "free monoid on closure and complement"}]--> output: `s_free_monoid_closure_complement`
2. input: `s_free_monoid_closure_complement` --[t_finite_case_check {target: relations_kkk_equals_k_and_cc_equals_id_reduce_to_14}]--> output: `s_relations_collapse_to_14`
3. input: `s_relations_collapse_to_14` --[t_pigeonhole_collision {dim: word_length_bounded_by_14}]--> output: `s_kuratowski_14_set_theorem`

**Techniques used:** t_auxiliary_construction, t_finite_case_check, t_pigeonhole_collision

---

### Topological invariance of Lebesgue covering dimension (cite: https://en.wikipedia.org/wiki/Lebesgue_covering_dimension)

**Axioms:** `s_homeomorphic_topological_spaces`
**Terminal:** `s_topological_invariance_of_dimension` (kind: theorem)

**Steps:**
1. input: `s_homeomorphic_topological_spaces` --[t_axiomatize_from_instances {target: covering_dimension_via_open_cover_orders}]--> output: `s_covering_dimension_definition`
2. input: `s_covering_dimension_definition` --[t_structural_isomorphism {target: pull_back_cover_preserves_order}]--> output: `s_dim_preserved_under_homeomorphism`
3. input: `s_dim_preserved_under_homeomorphism` --[t_compose_with_identity {with: R_m_homeomorphic_R_n_implies_m_equals_n}]--> output: `s_topological_invariance_of_dimension`

**Techniques used:** t_axiomatize_from_instances, t_structural_isomorphism, t_compose_with_identity

---

### Suspension isomorphism (reduced homology) (cite: https://en.wikipedia.org/wiki/Suspension_(topology))

**Axioms:** `s_pointed_space_X`, `s_reduced_suspension_sigma_X`
**Terminal:** `s_suspension_isomorphism_H_tilde` (kind: theorem)

**Steps:**
1. input: `s_reduced_suspension_sigma_X` --[t_auxiliary_construction {object: "long exact sequence of pair (CX, X) with cone contractible"}]--> output: `s_LES_cone_pair`
2. input: `s_LES_cone_pair` --[t_structural_isomorphism {target: shift_by_1_in_reduced_homology}]--> output: `s_suspension_isomorphism_H_tilde`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism

---

### Eilenberg swindle / vanishing of K-theory of "infinite sum" rings (cite: https://en.wikipedia.org/wiki/Eilenberg_swindle)

**Axioms:** `s_ring_admitting_countable_infinite_direct_sums`
**Terminal:** `s_eilenberg_swindle_K_theory_vanishing` (kind: theorem)

**Steps:**
1. input: `s_ring_admitting_countable_infinite_direct_sums` --[t_auxiliary_construction {object: "swindle isomorphism P ⊕ (P ⊕ P ⊕ ...) ≅ (P ⊕ P ⊕ ...)"}]--> output: `s_swindle_isomorphism`
2. input: `s_swindle_isomorphism` --[t_group_complete_exact_category {category: projective_modules_with_infinite_sums}]--> output: `s_K_0_vanishes_via_swindle`
3. input: `s_K_0_vanishes_via_swindle` --[t_compose_with_identity {with: all_K_n_vanish}]--> output: `s_eilenberg_swindle_K_theory_vanishing`

**Techniques used:** t_auxiliary_construction, t_group_complete_exact_category, t_compose_with_identity

---

### Whitney–Graustein theorem (cite: https://en.wikipedia.org/wiki/Whitney%E2%80%93Graustein_theorem)

**Axioms:** `s_immersion_of_circle_in_plane`, `s_winding_number_of_tangent`
**Terminal:** `s_whitney_graustein_theorem` (kind: theorem)

**Steps:**
1. input: `s_immersion_of_circle_in_plane` --[t_auxiliary_construction {object: "rotation number / Gauss map degree"}]--> output: `s_rotation_number_of_immersion`
2. input: `s_rotation_number_of_immersion` --[t_obstruction_class {class: degree_of_tangent_map_S_1_to_S_1}]--> output: `s_complete_invariant_for_regular_homotopy`
3. input: `s_complete_invariant_for_regular_homotopy` --[t_structural_isomorphism {target: regular_homotopy_classes_equal_Z}]--> output: `s_whitney_graustein_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_structural_isomorphism

---

### Smale's sphere eversion (cite: https://en.wikipedia.org/wiki/Smale%27s_paradox)

**Axioms:** `s_immersion_S_2_in_R_3`
**Terminal:** `s_smale_sphere_eversion` (kind: theorem)

**Steps:**
1. input: `s_immersion_S_2_in_R_3` --[t_auxiliary_construction {object: "h-principle / Smale–Hirsch classification of immersions"}]--> output: `s_immersions_classified_by_homotopy_of_tangent_map`
2. input: `s_immersions_classified_by_homotopy_of_tangent_map` --[t_obstruction_class {class: pi_2_SO_3_equals_zero}]--> output: `s_no_obstruction_to_homotopy_id_to_minus_id`
3. input: `s_no_obstruction_to_homotopy_id_to_minus_id` --[t_compose_with_identity {with: regular_homotopy_inversion_exists}]--> output: `s_smale_sphere_eversion`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_compose_with_identity

---

### Hopf classification theorem (cite: https://en.wikipedia.org/wiki/Hopf_theorem)

**Axioms:** `s_compact_connected_oriented_n_manifold`, `s_continuous_map_to_S_n`
**Terminal:** `s_hopf_classification_theorem` (kind: theorem)

**Steps:**
1. input: `s_continuous_map_to_S_n` --[t_auxiliary_construction {object: "degree of map via fundamental class pairing"}]--> output: `s_degree_of_map`
2. input: `s_degree_of_map` --[t_obstruction_class {class: complete_invariant_for_homotopy}]--> output: `s_degree_complete_invariant`
3. input: `s_degree_complete_invariant` --[t_structural_isomorphism {target: homotopy_classes_M_to_S_n_equal_Z}]--> output: `s_hopf_classification_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_structural_isomorphism

---

### Preimage theorem (regular value theorem) (cite: https://en.wikipedia.org/wiki/Preimage_theorem)

**Axioms:** `s_smooth_map_f_M_to_N`, `s_regular_value_q_in_N`
**Terminal:** `s_preimage_theorem` (kind: theorem)

**Steps:**
1. input: `s_regular_value_q_in_N` --[t_auxiliary_construction {object: "local submersion form via implicit function theorem"}]--> output: `s_local_submersion_form`
2. input: `s_local_submersion_form` --[t_structural_isomorphism {target: f_inverse_q_smooth_submanifold_of_codim_dim_N}]--> output: `s_preimage_theorem`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism

---

### Tubular neighborhood theorem (cite: https://en.wikipedia.org/wiki/Tubular_neighborhood)

**Axioms:** `s_smooth_submanifold_S_of_M`, `s_normal_bundle_NS`
**Terminal:** `s_tubular_neighborhood_theorem` (kind: theorem)

**Steps:**
1. input: `s_normal_bundle_NS` --[t_auxiliary_construction {object: "exponential map of riemannian metric on normal bundle"}]--> output: `s_exp_normal_bundle_map`
2. input: `s_exp_normal_bundle_map` --[t_compactness_argument {target: injective_on_small_neighborhood}]--> output: `s_local_diffeomorphism_on_small_disk_bundle`
3. input: `s_local_diffeomorphism_on_small_disk_bundle` --[t_structural_isomorphism {target: open_tubular_neighborhood_diffeomorphic_normal_bundle}]--> output: `s_tubular_neighborhood_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_structural_isomorphism

---

### Stiefel–Whitney class characterization (axioms) (cite: https://en.wikipedia.org/wiki/Stiefel%E2%80%93Whitney_class)

**Axioms:** `s_real_vector_bundle_xi`
**Terminal:** `s_stiefel_whitney_classes_axioms` (kind: theorem)

**Steps:**
1. input: `s_real_vector_bundle_xi` --[t_axiomatize_from_instances {target: naturality_dimension_whitney_sum_normalization}]--> output: `s_axiom_list_for_w_i`
2. input: `s_axiom_list_for_w_i` --[t_obstruction_class {class: mod_2_cohomology_class_w_i}]--> output: `s_classes_in_H_i_M_F_2`
3. input: `s_classes_in_H_i_M_F_2` --[t_structural_isomorphism {target: unique_classes_satisfying_axioms_via_grassmannian}]--> output: `s_stiefel_whitney_classes_axioms`

**Techniques used:** t_axiomatize_from_instances, t_obstruction_class, t_structural_isomorphism

---

### Chern class characterization (axioms) (cite: https://en.wikipedia.org/wiki/Chern_class)

**Axioms:** `s_complex_vector_bundle_eta`
**Terminal:** `s_chern_classes_axioms` (kind: theorem)

**Steps:**
1. input: `s_complex_vector_bundle_eta` --[t_axiomatize_from_instances {target: naturality_dimension_whitney_sum_normalization_on_tautological_line}]--> output: `s_axiom_list_for_c_i`
2. input: `s_axiom_list_for_c_i` --[t_obstruction_class {class: integer_cohomology_c_i_in_H_2i}]--> output: `s_classes_in_H_2i_M_Z`
3. input: `s_classes_in_H_2i_M_Z` --[t_structural_isomorphism {target: unique_via_classifying_BU_n_cohomology}]--> output: `s_chern_classes_axioms`

**Techniques used:** t_axiomatize_from_instances, t_obstruction_class, t_structural_isomorphism

---

### Pontryagin classes from Chern (cite: https://en.wikipedia.org/wiki/Pontryagin_class)

**Axioms:** `s_real_vector_bundle_xi`, `s_complexification_xi_otimes_C`
**Terminal:** `s_pontryagin_classes_definition_theorem` (kind: theorem)

**Steps:**
1. input: `s_complexification_xi_otimes_C` --[t_auxiliary_construction {object: "Chern classes c_i of complexification"}]--> output: `s_chern_classes_of_complexification`
2. input: `s_chern_classes_of_complexification` --[t_obstruction_class {class: p_k_equals_minus_one_to_k_c_2k}]--> output: `s_pontryagin_class_p_k`
3. input: `s_pontryagin_class_p_k` --[t_structural_isomorphism {target: well_defined_in_H_4k_M_Z_mod_2_torsion}]--> output: `s_pontryagin_classes_definition_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_structural_isomorphism

---

### Chern–Weil theorem (cite: https://en.wikipedia.org/wiki/Chern%E2%80%93Weil_homomorphism)

**Axioms:** `s_principal_G_bundle_with_connection`
**Terminal:** `s_chern_weil_theorem` (kind: theorem)

**Steps:**
1. input: `s_principal_G_bundle_with_connection` --[t_auxiliary_construction {object: "curvature 2-form Ω and invariant polynomials in Lie algebra"}]--> output: `s_invariant_polynomial_in_curvature`
2. input: `s_invariant_polynomial_in_curvature` --[t_compose_with_identity {with: bianchi_identity_makes_closed_form}]--> output: `s_closed_de_rham_class_of_invariant_polynomial`
3. input: `s_closed_de_rham_class_of_invariant_polynomial` --[t_structural_isomorphism {target: de_rham_class_independent_of_connection_equals_characteristic_class}]--> output: `s_chern_weil_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### Gauss–Bonnet–Chern theorem (cite: https://en.wikipedia.org/wiki/Generalized_Gauss%E2%80%93Bonnet_theorem)

**Axioms:** `s_closed_oriented_riemannian_2n_manifold`
**Terminal:** `s_gauss_bonnet_chern_theorem` (kind: theorem)

**Steps:**
1. input: `s_closed_oriented_riemannian_2n_manifold` --[t_auxiliary_construction {object: "Pfaffian of curvature 2-form"}]--> output: `s_pfaffian_of_curvature`
2. input: `s_pfaffian_of_curvature` --[t_compose_with_identity {with: chern_weil_gives_euler_class_in_de_rham}]--> output: `s_pfaffian_represents_euler_class`
3. input: `s_pfaffian_represents_euler_class` --[t_compose_with_identity {with: integrate_to_chi_M}]--> output: `s_gauss_bonnet_chern_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Bordism groups via Pontryagin–Thom (cite: https://en.wikipedia.org/wiki/Cobordism)

**Axioms:** `s_smooth_n_manifolds_modulo_cobordism`
**Terminal:** `s_unoriented_bordism_via_thom_spectrum_MO` (kind: theorem)

**Steps:**
1. input: `s_smooth_n_manifolds_modulo_cobordism` --[t_auxiliary_construction {object: "embed M in S^{n+k}, take Pontryagin–Thom collapse to Thom space MO(k)"}]--> output: `s_collapse_to_MO_k_thom_space`
2. input: `s_collapse_to_MO_k_thom_space` --[t_raise_dimension {target: stabilize_k_to_infinity}]--> output: `s_stable_map_to_MO_spectrum`
3. input: `s_stable_map_to_MO_spectrum` --[t_structural_isomorphism {target: unoriented_bordism_equals_pi_n_MO}]--> output: `s_unoriented_bordism_via_thom_spectrum_MO`

**Techniques used:** t_auxiliary_construction, t_raise_dimension, t_structural_isomorphism

---

### Thom's calculation of unoriented bordism (cite: https://en.wikipedia.org/wiki/Cobordism)

**Axioms:** `s_unoriented_bordism_via_thom_spectrum_MO`
**Terminal:** `s_thom_unoriented_bordism_calculation` (kind: theorem)

**Steps:**
1. input: `s_unoriented_bordism_via_thom_spectrum_MO` --[t_auxiliary_construction {object: "MO as wedge of HF_2 spectra via Thom isomorphism"}]--> output: `s_MO_splits_as_HF_2_wedges`
2. input: `s_MO_splits_as_HF_2_wedges` --[t_compose_with_identity {with: pi_star_MO_polynomial_over_F_2}]--> output: `s_thom_unoriented_bordism_calculation`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

### Adem relations / Steenrod algebra structure (cite: https://en.wikipedia.org/wiki/Steenrod_algebra)

**Axioms:** `s_mod_p_cohomology_with_steenrod_operations`
**Terminal:** `s_adem_relations_steenrod_algebra` (kind: theorem)

**Steps:**
1. input: `s_mod_p_cohomology_with_steenrod_operations` --[t_auxiliary_construction {object: "construct Sq^i via equivariant chain approximation of diagonal"}]--> output: `s_sq_i_via_equivariant_diagonal`
2. input: `s_sq_i_via_equivariant_diagonal` --[t_symmetry_reduction {group: cyclic_group_action_on_chain_complex}]--> output: `s_relations_from_double_cyclic_structure`
3. input: `s_relations_from_double_cyclic_structure` --[t_axiomatize_from_instances {target: adem_relations_present_Steenrod_algebra}]--> output: `s_adem_relations_steenrod_algebra`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_axiomatize_from_instances

---

### Cartan's formula for Steenrod squares (cite: https://en.wikipedia.org/wiki/Steenrod_algebra)

**Axioms:** `s_steenrod_squares_Sq_i`, `s_cup_product`
**Terminal:** `s_cartan_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_steenrod_squares_Sq_i, s_cup_product⟩` --[t_auxiliary_construction {object: "external product compatibility via Eilenberg–Zilber"}]--> output: `s_external_product_compat`
2. input: `s_external_product_compat` --[t_structural_isomorphism {target: Sq_n_x_cup_y_equals_sum_Sq_i_x_cup_Sq_n_minus_i_y}]--> output: `s_cartan_formula`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism

---

### Spanier–Whitehead duality (cite: https://en.wikipedia.org/wiki/Spanier%E2%80%93Whitehead_duality)

**Axioms:** `s_finite_cw_complex_X_embedded_in_S_n`
**Terminal:** `s_spanier_whitehead_duality` (kind: theorem)

**Steps:**
1. input: `s_finite_cw_complex_X_embedded_in_S_n` --[t_auxiliary_construction {object: "S–dual D_n X = S^n \\ X up to stable equivalence"}]--> output: `s_spanier_whitehead_dual_DX`
2. input: `s_spanier_whitehead_dual_DX` --[t_duality {pairing: smash_product_to_S_0_in_stable_category}]--> output: `s_spanier_whitehead_duality`

**Techniques used:** t_auxiliary_construction, t_duality

---

### Thom isomorphism theorem (cite: https://en.wikipedia.org/wiki/Thom_space)

**Axioms:** `s_oriented_real_vector_bundle_xi_rank_n`
**Terminal:** `s_thom_isomorphism` (kind: theorem)

**Steps:**
1. input: `s_oriented_real_vector_bundle_xi_rank_n` --[t_auxiliary_construction {object: "Thom class U in H^n(Thom(xi); Z)"}]--> output: `s_thom_class_U`
2. input: `s_thom_class_U` --[t_compose_with_identity {with: cup_product_with_U_shifts_degree_by_n}]--> output: `s_cup_with_U_iso`
3. input: `s_cup_with_U_iso` --[t_structural_isomorphism {target: H_star_X_iso_H_star_plus_n_Thom_xi}]--> output: `s_thom_isomorphism`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### Gysin sequence (cite: https://en.wikipedia.org/wiki/Gysin_sequence)

**Axioms:** `s_oriented_sphere_bundle_S_n_to_E_to_B`
**Terminal:** `s_gysin_sequence` (kind: theorem)

**Steps:**
1. input: `s_oriented_sphere_bundle_S_n_to_E_to_B` --[t_auxiliary_construction {object: "associated disk bundle pair and Thom iso"}]--> output: `s_disk_sphere_pair_with_thom_iso`
2. input: `s_disk_sphere_pair_with_thom_iso` --[t_compose_with_identity {with: long_exact_sequence_of_pair}]--> output: `s_LES_of_pair`
3. input: `s_LES_of_pair` --[t_structural_isomorphism {target: gysin_LES_with_euler_class_cup}]--> output: `s_gysin_sequence`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### Wang sequence (cite: https://en.wikipedia.org/wiki/Wang_sequence)

**Axioms:** `s_fiber_bundle_with_base_S_n`
**Terminal:** `s_wang_sequence` (kind: theorem)

**Steps:**
1. input: `s_fiber_bundle_with_base_S_n` --[t_auxiliary_construction {object: "Mayer–Vietoris on two hemispheres of S^n cover"}]--> output: `s_two_hemispheres_MV`
2. input: `s_two_hemispheres_MV` --[t_structural_isomorphism {target: long_exact_sequence_relating_H_E_and_H_F}]--> output: `s_wang_sequence`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism

---

### Borel construction / equivariant cohomology (cite: https://en.wikipedia.org/wiki/Equivariant_cohomology)

**Axioms:** `s_topological_group_G_acting_on_X`
**Terminal:** `s_borel_equivariant_cohomology` (kind: theorem)

**Steps:**
1. input: `s_topological_group_G_acting_on_X` --[t_auxiliary_construction {object: "EG ×_G X Borel construction"}]--> output: `s_borel_construction_EG_times_X`
2. input: `s_borel_construction_EG_times_X` --[t_representable_functor_trick {functor: H_star_BG_module}]--> output: `s_equivariant_cohomology_is_module_over_H_BG`
3. input: `s_equivariant_cohomology_is_module_over_H_BG` --[t_structural_isomorphism {target: H_G_star_X_well_defined_invariant}]--> output: `s_borel_equivariant_cohomology`

**Techniques used:** t_auxiliary_construction, t_representable_functor_trick, t_structural_isomorphism

---

### Lefschetz coincidence / fixed-point trace formula (general) (cite: https://en.wikipedia.org/wiki/Lefschetz_fixed-point_theorem)

**Axioms:** `s_continuous_map_pair_f_g_M_to_N`
**Terminal:** `s_lefschetz_coincidence_formula` (kind: theorem)

**Steps:**
1. input: `s_continuous_map_pair_f_g_M_to_N` --[t_auxiliary_construction {object: "coincidence number via diagonal and graphs"}]--> output: `s_coincidence_intersection_number`
2. input: `s_coincidence_intersection_number` --[t_compose_with_identity {with: alternating_sum_of_traces_on_homology}]--> output: `s_lefschetz_coincidence_formula`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity

---

## Closing notes

- All edge labels are drawn verbatim from `TECHNIQUES.md`.
- The Seifert–van Kampen entry contains an annotated edit (extra clarifying line) — disregard the parenthetical and treat the three numbered steps as canonical.
- Whenever a chain calls a previously-proved big theorem (Brouwer, Tychonoff, Atiyah–Singer, Geometrization, Poincaré conjecture), it appears as an input or as an `_compose_with_identity` glue — never re-derived.
- 0 steps were flagged `⚠ needs new technique`.
