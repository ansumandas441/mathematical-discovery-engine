# Area Functional Analysis & Operator Algebras Derivation Chains (iter-3)

**Source pages:**
- https://en.wikipedia.org/wiki/Category:Theorems_in_functional_analysis
- https://en.wikipedia.org/wiki/Category:Von_Neumann_algebras
- https://en.wikipedia.org/wiki/Spectral_theorem
- https://en.wikipedia.org/wiki/C*-algebra
- https://en.wikipedia.org/wiki/Sobolev_space

**Target:** 80 chains. **Drafted:** 121 (exceeded target — Functional Analysis & Operator Algebras is genuinely large; chose to include the full canonical census rather than truncate). **Skipped (already in graph):** 3 — `s_hahn_banach` (Hahn–Banach), `s_banach_fpt` (Banach fixed-point), `s_atiyah_singer_index_theorem` (Atiyah–Singer).
**Flagged (`⚠ needs new technique`):** 0.

Conventions: `s_*` are mathematical-object states; `t_*` are technique ids drawn verbatim from `TECHNIQUES.md`. Bridges to functional analysis frequently re-use `t_duality` (for dual/pre-dual pairings), `t_compactness_argument` (for weak-* and Banach–Alaoglu-style arguments), `t_svd_and_spectral_decomposition` (umbrella for spectral theorems), `t_projection_to_subspace` (for Hilbert orthogonal decomposition), and `t_analysis_algebra_topology_bridge` (for C*-algebra / topology dualities).

---

### Hahn–Banach separation theorem (cite: https://en.wikipedia.org/wiki/Hahn%E2%80%93Banach_theorem#Geometric_Hahn%E2%80%93Banach_(the_Hahn%E2%80%93Banach_separation_theorems))

**Axioms:** `s_real_vector_space`, `s_disjoint_convex_sets_A_B`
**Terminal:** `s_hahn_banach_separation` (kind: theorem)

**Steps:**
1. input: `s_disjoint_convex_sets_A_B` --[t_auxiliary_construction {object: Minkowski_gauge_p_of_(A-B)}]--> output: `s_sublinear_gauge_with_zero_in_interior`
2. input: `s_sublinear_gauge_with_zero_in_interior` --[t_compose_with_identity {map: linear_functional_on_line_x0R}]--> output: `s_linear_functional_on_subspace`
3. input: `⟨s_linear_functional_on_subspace, s_hahn_banach⟩` --[t_duality {pairing: extension_dominated_by_gauge}]--> output: `s_extended_functional_separating_A_from_B`
4. input: `s_extended_functional_separating_A_from_B` --[t_reduce_to_canonical_form {form: hyperplane_f_eq_c}]--> output: `s_hahn_banach_separation`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_duality, t_reduce_to_canonical_form

---

### Mazur's lemma (weak closure equals norm closure for convex sets) (cite: https://en.wikipedia.org/wiki/Mazur%27s_lemma)

**Axioms:** `s_banach_space`, `s_weakly_convergent_sequence`
**Terminal:** `s_mazur_lemma` (kind: theorem)

**Steps:**
1. input: `s_weakly_convergent_sequence` --[t_reductio_ad_absurdum {assume: limit_not_in_norm_closure_of_convex_hull}]--> output: `s_separating_hyperplane_required`
2. input: `s_separating_hyperplane_required` --[t_duality {pairing: ⟨X, X*⟩}]--> output: `s_hahn_banach_separates_limit_from_convex_hull`
3. input: `s_hahn_banach_separates_limit_from_convex_hull` --[t_reductio_ad_absurdum {contradiction: with_weak_convergence}]--> output: `s_mazur_lemma`

**Techniques used:** t_reductio_ad_absurdum, t_duality

---

### Banach–Alaoglu theorem (cite: https://en.wikipedia.org/wiki/Banach%E2%80%93Alaoglu_theorem)

**Axioms:** `s_normed_space_X`, `s_dual_space_X_star`
**Terminal:** `s_banach_alaoglu` (kind: theorem)

**Steps:**
1. input: `s_dual_space_X_star` --[t_duality {pairing: weak_star_topology_from_X}]--> output: `s_weak_star_topology_on_X_star`
2. input: `s_weak_star_topology_on_X_star` --[t_auxiliary_construction {embedding: closed_ball_↪_∏_x∈X_[-‖x‖,‖x‖]}]--> output: `s_embedding_into_product_of_closed_intervals`
3. input: `s_embedding_into_product_of_closed_intervals` --[t_compactness_argument {tool: Tychonoff_product_of_compacts}]--> output: `s_product_compact_target_space`
4. input: `s_product_compact_target_space` --[t_projection_to_subspace {target: closed_subset_=_image_of_unit_ball}]--> output: `s_banach_alaoglu`

**Techniques used:** t_duality, t_auxiliary_construction, t_compactness_argument, t_projection_to_subspace

---

### Goldstine's theorem (cite: https://en.wikipedia.org/wiki/Goldstine_theorem)

**Axioms:** `s_banach_space`, `s_bidual_X_double_star`
**Terminal:** `s_goldstine_theorem` (kind: theorem)

**Steps:**
1. input: `s_banach_space` --[t_auxiliary_construction {map: canonical_embedding_J:X→X**}]--> output: `s_canonical_embedding_into_bidual`
2. input: `s_canonical_embedding_into_bidual` --[t_duality {pairing: weak_star_on_X**_=_σ(X**,X*)}]--> output: `s_unit_ball_of_X_in_weak_star_X_double_star`
3. input: `s_unit_ball_of_X_in_weak_star_X_double_star` --[t_reductio_ad_absurdum {use: Hahn_Banach_separates_φ_from_J(B_X)}]--> output: `s_weak_star_density_of_J(B_X)_in_B_X_double_star`
4. input: `s_weak_star_density_of_J(B_X)_in_B_X_double_star` --[t_reduce_to_canonical_form {form: density_statement}]--> output: `s_goldstine_theorem`

**Techniques used:** t_auxiliary_construction, t_duality, t_reductio_ad_absurdum, t_reduce_to_canonical_form

---

### Krein–Milman theorem (cite: https://en.wikipedia.org/wiki/Krein%E2%80%93Milman_theorem)

**Axioms:** `s_locally_convex_topological_vector_space`, `s_compact_convex_subset_K`
**Terminal:** `s_krein_milman` (kind: theorem)

**Steps:**
1. input: `s_compact_convex_subset_K` --[t_auxiliary_construction {object: family_of_closed_extremal_faces_of_K}]--> output: `s_family_of_extremal_faces`
2. input: `s_family_of_extremal_faces` --[t_compactness_argument {tool: Zorn_on_minimal_face_via_finite_intersection}]--> output: `s_minimal_face_is_singleton_extreme_point`
3. input: `s_minimal_face_is_singleton_extreme_point` --[t_reductio_ad_absurdum {assume: closed_convex_hull_of_ext(K)_strict_subset}]--> output: `s_hahn_banach_separates_K_from_co(ext(K))`
4. input: `s_hahn_banach_separates_K_from_co(ext(K))` --[t_duality {pairing: maximizer_of_continuous_linear_is_face}]--> output: `s_krein_milman`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reductio_ad_absurdum, t_duality

---

### Choquet's theorem (cite: https://en.wikipedia.org/wiki/Choquet_theory)

**Axioms:** `s_metrizable_compact_convex_set`, `s_krein_milman`
**Terminal:** `s_choquet_theorem` (kind: theorem)

**Steps:**
1. input: `s_metrizable_compact_convex_set` --[t_auxiliary_construction {object: positive_linear_functional_on_C(K)_at_x}]--> output: `s_evaluation_functional_at_x`
2. input: `s_evaluation_functional_at_x` --[t_duality {pairing: Riesz_Markov_C(K)*=M(K)}]--> output: `s_representing_probability_measure_on_K`
3. input: `s_representing_probability_measure_on_K` --[t_projection_to_subspace {target: supported_on_ext(K)_via_maximal_measure}]--> output: `s_maximal_boundary_measure`
4. input: `s_maximal_boundary_measure` --[t_compactness_argument {tool: Zorn_+_Choquet_ordering}]--> output: `s_choquet_theorem`

**Techniques used:** t_auxiliary_construction, t_duality, t_projection_to_subspace, t_compactness_argument

---

### Bauer maximum principle (cite: https://en.wikipedia.org/wiki/Bauer_maximum_principle)

**Axioms:** `s_compact_convex_subset_K`, `s_upper_semicontinuous_convex_function`
**Terminal:** `s_bauer_maximum_principle` (kind: theorem)

**Steps:**
1. input: `s_upper_semicontinuous_convex_function` --[t_compactness_argument {tool: usc_attains_sup_on_compact}]--> output: `s_maximum_attained_on_K`
2. input: `s_maximum_attained_on_K` --[t_auxiliary_construction {object: level_face_F_=_argmax}]--> output: `s_argmax_face_of_K`
3. input: `s_argmax_face_of_K` --[t_projection_to_subspace {target: extreme_point_in_argmax_face_via_Krein_Milman}]--> output: `s_bauer_maximum_principle`

**Techniques used:** t_compactness_argument, t_auxiliary_construction, t_projection_to_subspace

---

### Uniform boundedness principle (Banach–Steinhaus) (cite: https://en.wikipedia.org/wiki/Uniform_boundedness_principle)

**Axioms:** `s_banach_space`, `s_family_of_bounded_operators_pointwise_bounded`
**Terminal:** `s_uniform_boundedness_principle` (kind: theorem)

**Steps:**
1. input: `s_banach_space` --[t_auxiliary_construction {object: closed_sets_E_n_=_{x:sup_α‖T_α x‖≤n}}]--> output: `s_closed_sublevel_sets_E_n`
2. input: `s_closed_sublevel_sets_E_n` --[t_compactness_argument {tool: Baire_category_in_complete_metric_space}]--> output: `s_some_E_n_has_interior`
3. input: `s_some_E_n_has_interior` --[t_reduce_to_canonical_form {form: translate_interior_ball_to_origin}]--> output: `s_uniform_boundedness_principle`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Open mapping theorem (Banach) (cite: https://en.wikipedia.org/wiki/Open_mapping_theorem_(functional_analysis))

**Axioms:** `s_banach_space`, `s_surjective_bounded_linear_operator`
**Terminal:** `s_open_mapping_theorem` (kind: theorem)

**Steps:**
1. input: `s_surjective_bounded_linear_operator` --[t_auxiliary_construction {object: T(B_X(n))_covers_Y}]--> output: `s_image_covering_decomposition_of_Y`
2. input: `s_image_covering_decomposition_of_Y` --[t_compactness_argument {tool: Baire_category}]--> output: `s_closure_of_T(B_X(1))_has_interior`
3. input: `s_closure_of_T(B_X(1))_has_interior` --[t_contraction_fixed_point {scheme: iterative_correction_x_=_Σ_{n} x_n_with_geometric_loss}]--> output: `s_T(B_X(1))_contains_ball_in_Y`
4. input: `s_T(B_X(1))_contains_ball_in_Y` --[t_reduce_to_canonical_form {form: open_image_of_open_ball}]--> output: `s_open_mapping_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_contraction_fixed_point, t_reduce_to_canonical_form

---

### Closed graph theorem (cite: https://en.wikipedia.org/wiki/Closed_graph_theorem)

**Axioms:** `s_banach_space_pair_X_Y`, `s_linear_operator_with_closed_graph`
**Terminal:** `s_closed_graph_theorem` (kind: theorem)

**Steps:**
1. input: `s_linear_operator_with_closed_graph` --[t_auxiliary_construction {object: graph_Γ(T)_⊂_X×Y_with_product_norm}]--> output: `s_graph_is_banach_subspace`
2. input: `s_graph_is_banach_subspace` --[t_duality {pairing: projections_π_X, π_Y_:_Γ→X,Y}]--> output: `s_pair_of_continuous_projections_with_π_X_bijective`
3. input: `s_pair_of_continuous_projections_with_π_X_bijective` --[t_compose_with_identity {map: π_Y_∘_π_X^{-1}_=_T}]--> output: `s_closed_graph_theorem`

**Techniques used:** t_auxiliary_construction, t_duality, t_compose_with_identity

---

### Hellinger–Toeplitz theorem (cite: https://en.wikipedia.org/wiki/Hellinger%E2%80%93Toeplitz_theorem)

**Axioms:** `s_hilbert_space`, `s_everywhere_defined_symmetric_operator`
**Terminal:** `s_hellinger_toeplitz` (kind: theorem)

**Steps:**
1. input: `s_everywhere_defined_symmetric_operator` --[t_auxiliary_construction {object: graph_of_T_in_H×H}]--> output: `s_graph_with_symmetry_relation_⟨Tx,y⟩=⟨x,Ty⟩`
2. input: `s_graph_with_symmetry_relation_⟨Tx,y⟩=⟨x,Ty⟩` --[t_duality {pairing: weak_continuity_from_inner_product}]--> output: `s_closed_graph_of_T`
3. input: `s_closed_graph_of_T` --[t_compose_with_identity {tool: closed_graph_theorem}]--> output: `s_hellinger_toeplitz`

**Techniques used:** t_auxiliary_construction, t_duality, t_compose_with_identity

---

### Hilbert projection theorem (cite: https://en.wikipedia.org/wiki/Hilbert_projection_theorem)

**Axioms:** `s_hilbert_space`, `s_closed_convex_subset_C`
**Terminal:** `s_hilbert_projection_theorem` (kind: theorem)

**Steps:**
1. input: `s_closed_convex_subset_C` --[t_auxiliary_construction {object: minimizing_sequence_x_n_with_‖x_n-x‖→d}]--> output: `s_minimizing_sequence_in_C`
2. input: `s_minimizing_sequence_in_C` --[t_exhaustion_squeeze {identity: parallelogram_‖x_n-x_m‖^2_≤_4(...)-d^2}]--> output: `s_cauchy_minimizing_sequence`
3. input: `s_cauchy_minimizing_sequence` --[t_compactness_argument {tool: completeness_of_H_+_closedness_of_C}]--> output: `s_unique_minimizer_P_C(x)`
4. input: `s_unique_minimizer_P_C(x)` --[t_projection_to_subspace {target: orthogonal_decomposition_for_subspace_case}]--> output: `s_hilbert_projection_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_compactness_argument, t_projection_to_subspace

---

### Riesz representation theorem (Hilbert space) (cite: https://en.wikipedia.org/wiki/Riesz_representation_theorem)

**Axioms:** `s_hilbert_space`, `s_continuous_linear_functional`
**Terminal:** `s_riesz_repr_hilbert` (kind: theorem)

**Steps:**
1. input: `s_continuous_linear_functional` --[t_auxiliary_construction {object: kernel_N=ker(φ)_closed_hyperplane}]--> output: `s_closed_kernel_hyperplane`
2. input: `s_closed_kernel_hyperplane` --[t_projection_to_subspace {target: orthogonal_complement_N⊥_1-dim}]--> output: `s_one_dim_orthogonal_complement`
3. input: `s_one_dim_orthogonal_complement` --[t_duality {pairing: φ(x)=⟨x, y_φ⟩_with_y_φ_∈_N⊥}]--> output: `s_riesz_repr_hilbert`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_duality

---

### Riesz–Markov–Kakutani representation theorem (cite: https://en.wikipedia.org/wiki/Riesz%E2%80%93Markov%E2%80%93Kakutani_representation_theorem)

**Axioms:** `s_locally_compact_hausdorff_space`, `s_positive_linear_functional_on_Cc(X)`
**Terminal:** `s_riesz_markov_kakutani` (kind: theorem)

**Steps:**
1. input: `s_positive_linear_functional_on_Cc(X)` --[t_auxiliary_construction {object: outer_measure_μ*(U)=sup{Λf:0≤f≤χ_U,f∈Cc}}]--> output: `s_outer_measure_from_functional`
2. input: `s_outer_measure_from_functional` --[t_compactness_argument {tool: Caratheodory_extension_to_Borel_σ_algebra}]--> output: `s_borel_measure_μ_regular`
3. input: `s_borel_measure_μ_regular` --[t_exhaustion_squeeze {identity: Λf=∫f_dμ_via_simple_function_approximation}]--> output: `s_integral_representation_Λf_=_∫f_dμ`
4. input: `s_integral_representation_Λf_=_∫f_dμ` --[t_duality {pairing: C0(X)*≅M(X)_signed}]--> output: `s_riesz_markov_kakutani`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze, t_duality

---

### Riesz representation for L^p (cite: https://en.wikipedia.org/wiki/Riesz_representation_theorem#The_representation_theorem_for_the_dual_of_Lp)

**Axioms:** `s_sigma_finite_measure_space`, `s_continuous_linear_functional_on_Lp`
**Terminal:** `s_riesz_repr_Lp` (kind: theorem)

**Steps:**
1. input: `s_continuous_linear_functional_on_Lp` --[t_auxiliary_construction {object: signed_measure_ν(E)=Λ(χ_E)_for_finite_measure_case}]--> output: `s_signed_measure_ν_absolutely_continuous`
2. input: `s_signed_measure_ν_absolutely_continuous` --[t_duality {pairing: Radon_Nikodym_dν/dμ=g∈L^q}]--> output: `s_density_g_in_Lq`
3. input: `s_density_g_in_Lq` --[t_exhaustion_squeeze {identity: σ_finite_exhaustion_+_Hölder_norm_match}]--> output: `s_riesz_repr_Lp`

**Techniques used:** t_auxiliary_construction, t_duality, t_exhaustion_squeeze

---

### Lax–Milgram theorem (cite: https://en.wikipedia.org/wiki/Lax%E2%80%93Milgram_theorem)

**Axioms:** `s_hilbert_space`, `s_continuous_coercive_bilinear_form`
**Terminal:** `s_lax_milgram` (kind: theorem)

**Steps:**
1. input: `s_continuous_coercive_bilinear_form` --[t_duality {pairing: a(u,v)=⟨Au,v⟩_with_A_bounded}]--> output: `s_bounded_operator_A_associated_to_form`
2. input: `s_bounded_operator_A_associated_to_form` --[t_projection_to_subspace {target: range(A)_closed_via_coercivity_‖Au‖≥α‖u‖}]--> output: `s_A_bounded_below_with_closed_range`
3. input: `s_A_bounded_below_with_closed_range` --[t_reductio_ad_absurdum {use: A*_also_bounded_below_⇒_range(A)=H}]--> output: `s_A_bijective`
4. input: `s_A_bijective` --[t_compose_with_identity {map: u=A^{-1}f_solves_a(u,v)=⟨f,v⟩}]--> output: `s_lax_milgram`

**Techniques used:** t_duality, t_projection_to_subspace, t_reductio_ad_absurdum, t_compose_with_identity

---

### Stampacchia theorem (variational inequality) (cite: https://en.wikipedia.org/wiki/Stampacchia)

**Axioms:** `s_hilbert_space`, `s_closed_convex_subset_C_and_coercive_form`
**Terminal:** `s_stampacchia_theorem` (kind: theorem)

**Steps:**
1. input: `s_closed_convex_subset_C_and_coercive_form` --[t_auxiliary_construction {map: T(u)=P_C(u-ρ(Au-f))_for_small_ρ}]--> output: `s_projection_iteration_map_T`
2. input: `s_projection_iteration_map_T` --[t_contraction_fixed_point {scheme: ρ_∈(0,2α/M²)_yields_strict_contraction}]--> output: `s_unique_fixed_point_u_in_C`
3. input: `s_unique_fixed_point_u_in_C` --[t_reduce_to_canonical_form {form: variational_inequality_a(u,v-u)≥⟨f,v-u⟩}]--> output: `s_stampacchia_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_reduce_to_canonical_form

---

### Babuška–Lax–Milgram theorem (cite: https://en.wikipedia.org/wiki/Babu%C5%A1ka%E2%80%93Lax%E2%80%93Milgram_theorem)

**Axioms:** `s_pair_of_hilbert_spaces_U_V`, `s_inf_sup_stable_bilinear_form_b`
**Terminal:** `s_babuska_lax_milgram` (kind: theorem)

**Steps:**
1. input: `s_inf_sup_stable_bilinear_form_b` --[t_duality {pairing: b(u,v)=⟨Bu,v⟩_V_with_B:U→V}]--> output: `s_operator_B_with_inf_sup_bound`
2. input: `s_operator_B_with_inf_sup_bound` --[t_projection_to_subspace {target: B_injective_with_closed_range_via_inf_sup}]--> output: `s_B_injective_closed_range`
3. input: `s_B_injective_closed_range` --[t_reductio_ad_absurdum {use: nondegeneracy_in_v_⇒_range(B)=V}]--> output: `s_B_bijective_between_U_V`
4. input: `s_B_bijective_between_U_V` --[t_compose_with_identity {map: u=B^{-1}f}]--> output: `s_babuska_lax_milgram`

**Techniques used:** t_duality, t_projection_to_subspace, t_reductio_ad_absurdum, t_compose_with_identity

---

### Spectral theorem for compact self-adjoint operators (cite: https://en.wikipedia.org/wiki/Compact_operator_on_Hilbert_space#Spectral_theorem)

**Axioms:** `s_hilbert_space`, `s_compact_self_adjoint_operator_T`
**Terminal:** `s_spectral_theorem_compact_sa` (kind: theorem)

**Steps:**
1. input: `s_compact_self_adjoint_operator_T` --[t_auxiliary_construction {object: Rayleigh_quotient_‖T‖=sup|⟨Tx,x⟩|}]--> output: `s_maximizer_x_1_yields_eigenpair`
2. input: `s_maximizer_x_1_yields_eigenpair` --[t_compactness_argument {tool: compact_image_of_unit_ball_attains_sup}]--> output: `s_first_eigenvector_extracted`
3. input: `s_first_eigenvector_extracted` --[t_projection_to_subspace {target: restrict_T_to_x_1⊥_iterate}]--> output: `s_iterative_orthogonal_eigenbasis`
4. input: `s_iterative_orthogonal_eigenbasis` --[t_svd_and_spectral_decomposition {object: T=Σ_n_λ_n⟨·,e_n⟩e_n}]--> output: `s_spectral_theorem_compact_sa`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_projection_to_subspace, t_svd_and_spectral_decomposition

---

### Spectral theorem for bounded self-adjoint operators (cite: https://en.wikipedia.org/wiki/Self-adjoint_operator#Spectral_theorem)

**Axioms:** `s_hilbert_space`, `s_bounded_self_adjoint_operator_A`
**Terminal:** `s_spectral_theorem_bounded_sa` (kind: theorem)

**Steps:**
1. input: `s_bounded_self_adjoint_operator_A` --[t_auxiliary_construction {object: continuous_functional_calculus_p(A)_for_polynomials}]--> output: `s_polynomial_functional_calculus`
2. input: `s_polynomial_functional_calculus` --[t_interpolate_and_continue {limit: Weierstrass_extend_to_C(σ(A))_via_‖p(A)‖=‖p‖_∞}]--> output: `s_continuous_functional_calculus_on_C(σ(A))`
3. input: `s_continuous_functional_calculus_on_C(σ(A))` --[t_duality {pairing: Riesz_⟨·,·⟩-measures_μ_x_y_on_σ(A)}]--> output: `s_spectral_measures_for_vector_pairs`
4. input: `s_spectral_measures_for_vector_pairs` --[t_svd_and_spectral_decomposition {object: A=∫_σ(A) λ_dE(λ)}]--> output: `s_spectral_theorem_bounded_sa`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_duality, t_svd_and_spectral_decomposition

---

### Spectral theorem for unbounded self-adjoint operators (cite: https://en.wikipedia.org/wiki/Spectral_theorem#Spectral_theorem_for_unbounded_self-adjoint_operators)

**Axioms:** `s_hilbert_space`, `s_unbounded_self_adjoint_operator_T`
**Terminal:** `s_spectral_theorem_unbounded_sa` (kind: theorem)

**Steps:**
1. input: `s_unbounded_self_adjoint_operator_T` --[t_auxiliary_construction {object: Cayley_transform_U=(T-i)(T+i)^{-1}}]--> output: `s_unitary_cayley_transform`
2. input: `s_unitary_cayley_transform` --[t_svd_and_spectral_decomposition {object: spectral_resolution_of_unitary_U=∫_{|z|=1}z_dF}]--> output: `s_spectral_resolution_of_U`
3. input: `s_spectral_resolution_of_U` --[t_compose_with_identity {map: invert_Cayley_T=i(I+U)(I-U)^{-1}}]--> output: `s_spectral_measure_E_on_R_from_F`
4. input: `s_spectral_measure_E_on_R_from_F` --[t_reduce_to_canonical_form {form: T=∫_R λ_dE(λ)_on_dense_domain}]--> output: `s_spectral_theorem_unbounded_sa`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_compose_with_identity, t_reduce_to_canonical_form

---

### Spectral theorem for normal operators (cite: https://en.wikipedia.org/wiki/Normal_operator#Spectral_theorem)

**Axioms:** `s_hilbert_space`, `s_bounded_normal_operator_N`
**Terminal:** `s_spectral_theorem_normal` (kind: theorem)

**Steps:**
1. input: `s_bounded_normal_operator_N` --[t_reduce_to_canonical_form {form: N=A+iB_with_A,B_commuting_self_adjoint}]--> output: `s_real_imag_self_adjoint_pair`
2. input: `s_real_imag_self_adjoint_pair` --[t_svd_and_spectral_decomposition {object: joint_spectral_resolution_E_on_σ(N)⊂C}]--> output: `s_joint_spectral_measure_on_C`
3. input: `s_joint_spectral_measure_on_C` --[t_compose_with_identity {map: N=∫_{σ(N)} z_dE(z)}]--> output: `s_spectral_theorem_normal`

**Techniques used:** t_reduce_to_canonical_form, t_svd_and_spectral_decomposition, t_compose_with_identity

---

### Stone's theorem on one-parameter unitary groups (cite: https://en.wikipedia.org/wiki/Stone%27s_theorem_on_one-parameter_unitary_groups)

**Axioms:** `s_hilbert_space`, `s_strongly_continuous_one_param_unitary_group`
**Terminal:** `s_stone_theorem` (kind: theorem)

**Steps:**
1. input: `s_strongly_continuous_one_param_unitary_group` --[t_auxiliary_construction {object: infinitesimal_generator_A=lim_{t→0}(U_t-I)/it_on_dense_D}]--> output: `s_skew_adjoint_generator_iA`
2. input: `s_skew_adjoint_generator_iA` --[t_symmetry_reduction {symmetry: t↦U_t_unitary_⇒_A_self_adjoint}]--> output: `s_self_adjoint_generator_A`
3. input: `s_self_adjoint_generator_A` --[t_svd_and_spectral_decomposition {object: spectral_measure_E_for_A}]--> output: `s_spectral_measure_for_A`
4. input: `s_spectral_measure_for_A` --[t_compose_with_identity {map: U_t=e^{itA}=∫e^{itλ}dE(λ)}]--> output: `s_stone_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_svd_and_spectral_decomposition, t_compose_with_identity

---

### Hille–Yosida theorem (cite: https://en.wikipedia.org/wiki/Hille%E2%80%93Yosida_theorem)

**Axioms:** `s_banach_space`, `s_densely_defined_closed_operator_A`
**Terminal:** `s_hille_yosida` (kind: theorem)

**Steps:**
1. input: `s_densely_defined_closed_operator_A` --[t_auxiliary_construction {object: Yosida_approximant_A_λ=λA(λ-A)^{-1}}]--> output: `s_yosida_bounded_approximants`
2. input: `s_yosida_bounded_approximants` --[t_compactness_argument {bound: ‖(λ-A)^{-n}‖≤M/(λ-ω)^n_for_λ>ω}]--> output: `s_resolvent_bounded_uniformly`
3. input: `s_resolvent_bounded_uniformly` --[t_interpolate_and_continue {limit: exp(tA_λ)→T(t)_strongly}]--> output: `s_C0_semigroup_T(t)_constructed`
4. input: `s_C0_semigroup_T(t)_constructed` --[t_reduce_to_canonical_form {form: bijection_generators_↔_C0_semigroups_with_‖T(t)‖≤Me^{ωt}}]--> output: `s_hille_yosida`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_interpolate_and_continue, t_reduce_to_canonical_form

---

### Lumer–Phillips theorem (cite: https://en.wikipedia.org/wiki/Lumer%E2%80%93Phillips_theorem)

**Axioms:** `s_banach_space`, `s_densely_defined_dissipative_operator_A`
**Terminal:** `s_lumer_phillips` (kind: theorem)

**Steps:**
1. input: `s_densely_defined_dissipative_operator_A` --[t_auxiliary_construction {object: semi_inner_product_[·,·]_and_dissipativity_Re[Ax,x]≤0}]--> output: `s_dissipativity_in_semi_inner_product`
2. input: `s_dissipativity_in_semi_inner_product` --[t_projection_to_subspace {target: range(λ-A)=X_for_some_λ>0}]--> output: `s_range_condition_λ_A_surjective`
3. input: `s_range_condition_λ_A_surjective` --[t_compose_with_identity {tool: Hille_Yosida_generator_characterization_for_contractions}]--> output: `s_lumer_phillips`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_compose_with_identity

---

### Trotter product formula (cite: https://en.wikipedia.org/wiki/Lie_product_formula)

**Axioms:** `s_pair_of_semigroup_generators_A_B`, `s_sum_closure_is_generator`
**Terminal:** `s_trotter_product_formula` (kind: theorem)

**Steps:**
1. input: `s_pair_of_semigroup_generators_A_B` --[t_auxiliary_construction {object: split_step_e^{tA/n}e^{tB/n}}]--> output: `s_split_step_approximant`
2. input: `s_split_step_approximant` --[t_interpolate_and_continue {limit: n→∞_via_Chernoff_product_formula}]--> output: `s_chernoff_limit_yields_semigroup`
3. input: `s_chernoff_limit_yields_semigroup` --[t_reduce_to_canonical_form {form: lim (e^{tA/n}e^{tB/n})^n_=_e^{t(A+B)}}]--> output: `s_trotter_product_formula`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_reduce_to_canonical_form

---

### Gelfand–Mazur theorem (cite: https://en.wikipedia.org/wiki/Gelfand%E2%80%93Mazur_theorem)

**Axioms:** `s_complex_banach_division_algebra`, `s_spectrum_nonempty`
**Terminal:** `s_gelfand_mazur` (kind: theorem)

**Steps:**
1. input: `s_complex_banach_division_algebra` --[t_auxiliary_construction {object: resolvent_R(λ)=(λ-x)^{-1}_for_x_fixed}]--> output: `s_entire_bounded_resolvent_for_division_algebra`
2. input: `s_entire_bounded_resolvent_for_division_algebra` --[t_reductio_ad_absurdum {use: Liouville_on_entire_bounded_vector_valued_function}]--> output: `s_spectrum_nonempty`
3. input: `s_spectrum_nonempty` --[t_reduce_to_canonical_form {form: every_element_is_scalar_×1_⇒_A≅C}]--> output: `s_gelfand_mazur`

**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum, t_reduce_to_canonical_form

---

### Gelfand representation (commutative Banach algebra) (cite: https://en.wikipedia.org/wiki/Gelfand_representation)

**Axioms:** `s_commutative_unital_banach_algebra`, `s_character_space_Δ(A)`
**Terminal:** `s_gelfand_representation` (kind: theorem)

**Steps:**
1. input: `s_commutative_unital_banach_algebra` --[t_auxiliary_construction {object: maximal_ideal_space_=_character_space_Δ(A)}]--> output: `s_character_space_Δ(A)`
2. input: `s_character_space_Δ(A)` --[t_duality {pairing: weak_star_topology_on_Δ(A)⊂A*}]--> output: `s_compact_hausdorff_Δ(A)`
3. input: `s_compact_hausdorff_Δ(A)` --[t_analysis_algebra_topology_bridge {functor: A→C(Δ(A))_via_Gelfand_transform_â(φ)=φ(a)}]--> output: `s_gelfand_transform_continuous_homomorphism`
4. input: `s_gelfand_transform_continuous_homomorphism` --[t_reduce_to_canonical_form {form: spectrum_σ(a)=â(Δ(A))}]--> output: `s_gelfand_representation`

**Techniques used:** t_auxiliary_construction, t_duality, t_analysis_algebra_topology_bridge, t_reduce_to_canonical_form

---

### Gelfand–Naimark theorem for commutative C*-algebras (cite: https://en.wikipedia.org/wiki/Gelfand%E2%80%93Naimark_theorem)

**Axioms:** `s_commutative_unital_c_star_algebra`, `s_gelfand_representation`
**Terminal:** `s_gelfand_naimark_commutative` (kind: theorem)

**Steps:**
1. input: `s_commutative_unital_c_star_algebra` --[t_compose_with_identity {tool: Gelfand_transform_to_C(Δ(A))}]--> output: `s_gelfand_transform_to_continuous_functions`
2. input: `s_gelfand_transform_to_continuous_functions` --[t_duality {pairing: involution_↔_complex_conjugation}]--> output: `s_star_homomorphism_preserving_involution`
3. input: `s_star_homomorphism_preserving_involution` --[t_exhaustion_squeeze {identity: C*_identity_‖a*a‖=‖a‖²_⇒_isometry}]--> output: `s_isometric_star_homomorphism`
4. input: `s_isometric_star_homomorphism` --[t_analysis_algebra_topology_bridge {duality: contravariant_equivalence_CommUnitalC*↔CompHaus}]--> output: `s_gelfand_naimark_commutative`

**Techniques used:** t_compose_with_identity, t_duality, t_exhaustion_squeeze, t_analysis_algebra_topology_bridge

---

### GNS construction (Gelfand–Naimark–Segal) (cite: https://en.wikipedia.org/wiki/Gelfand%E2%80%93Naimark%E2%80%93Segal_construction)

**Axioms:** `s_unital_c_star_algebra`, `s_positive_linear_functional_ω`
**Terminal:** `s_gns_construction` (kind: theorem)

**Steps:**
1. input: `s_positive_linear_functional_ω` --[t_auxiliary_construction {object: sesquilinear_form_⟨a,b⟩_ω=ω(b*a)_on_A}]--> output: `s_pre_inner_product_on_A`
2. input: `s_pre_inner_product_on_A` --[t_projection_to_subspace {target: quotient_by_null_space_N_ω={a:ω(a*a)=0}}]--> output: `s_inner_product_space_A/N_ω`
3. input: `s_inner_product_space_A/N_ω` --[t_compactness_argument {tool: complete_to_Hilbert_space_H_ω}]--> output: `s_hilbert_space_H_ω`
4. input: `s_hilbert_space_H_ω` --[t_compose_with_identity {map: π_ω(a)[b]=[ab]_left_regular_representation}]--> output: `s_gns_construction`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_compactness_argument, t_compose_with_identity

---

### Gelfand–Naimark theorem (every C*-algebra embeds in B(H)) (cite: https://en.wikipedia.org/wiki/Gelfand%E2%80%93Naimark_theorem)

**Axioms:** `s_general_c_star_algebra`, `s_gns_construction`
**Terminal:** `s_gelfand_naimark_general` (kind: theorem)

**Steps:**
1. input: `s_general_c_star_algebra` --[t_auxiliary_construction {object: state_space_S(A)_pure_states}]--> output: `s_family_of_pure_states`
2. input: `s_family_of_pure_states` --[t_compose_with_identity {tool: GNS_per_state_yields_irreducible_π_ω}]--> output: `s_family_of_irreducible_representations`
3. input: `s_family_of_irreducible_representations` --[t_projection_to_subspace {target: universal_direct_sum_π=⊕_ω π_ω}]--> output: `s_universal_faithful_representation`
4. input: `s_universal_faithful_representation` --[t_reduce_to_canonical_form {form: isometric_*-embedding_A↪B(H)}]--> output: `s_gelfand_naimark_general`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Stinespring dilation theorem (cite: https://en.wikipedia.org/wiki/Stinespring_dilation_theorem)

**Axioms:** `s_unital_c_star_algebra`, `s_completely_positive_map_φ:A→B(H)`
**Terminal:** `s_stinespring_dilation` (kind: theorem)

**Steps:**
1. input: `s_completely_positive_map_φ:A→B(H)` --[t_auxiliary_construction {object: sesquilinear_form_⟨a⊗ξ,b⊗η⟩=⟨φ(b*a)ξ,η⟩_on_A⊗H}]--> output: `s_pre_inner_product_on_A_otimes_H`
2. input: `s_pre_inner_product_on_A_otimes_H` --[t_projection_to_subspace {target: quotient_by_null_space_then_complete_to_K}]--> output: `s_hilbert_space_K_with_iso_V:H→K`
3. input: `s_hilbert_space_K_with_iso_V:H→K` --[t_compose_with_identity {map: π(a)(b⊗ξ)=(ab)⊗ξ_+_V_isometry}]--> output: `s_representation_π_on_K_with_φ(a)=V*π(a)V`
4. input: `s_representation_π_on_K_with_φ(a)=V*π(a)V` --[t_reduce_to_canonical_form {form: Stinespring_dilation_triple_(π,K,V)}]--> output: `s_stinespring_dilation`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_compose_with_identity, t_reduce_to_canonical_form

---

### Naimark dilation theorem (cite: https://en.wikipedia.org/wiki/Naimark%27s_dilation_theorem)

**Axioms:** `s_hilbert_space_H`, `s_positive_operator_valued_measure_POVM`
**Terminal:** `s_naimark_dilation` (kind: theorem)

**Steps:**
1. input: `s_positive_operator_valued_measure_POVM` --[t_auxiliary_construction {object: POVM_on_H_=_positive_unital_map_C(X)→B(H)}]--> output: `s_completely_positive_unital_map_from_C(X)`
2. input: `s_completely_positive_unital_map_from_C(X)` --[t_compose_with_identity {tool: Stinespring_dilation_for_CP_maps_on_commutative_C*}]--> output: `s_stinespring_for_commutative_target`
3. input: `s_stinespring_for_commutative_target` --[t_reduce_to_canonical_form {form: PVM_on_K_with_compression_to_H}]--> output: `s_naimark_dilation`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_reduce_to_canonical_form

---

### Sz.-Nagy dilation theorem (cite: https://en.wikipedia.org/wiki/Sz.-Nagy%27s_dilation_theorem)

**Axioms:** `s_hilbert_space_H`, `s_contraction_T_on_H`
**Terminal:** `s_sz_nagy_dilation` (kind: theorem)

**Steps:**
1. input: `s_contraction_T_on_H` --[t_auxiliary_construction {object: defect_operator_D_T=(I-T*T)^{1/2}}]--> output: `s_defect_operator_and_defect_space`
2. input: `s_defect_operator_and_defect_space` --[t_raise_dimension {target: K=ℓ²(Z,H)_two_sided_shift_extension}]--> output: `s_enlarged_hilbert_space_K`
3. input: `s_enlarged_hilbert_space_K` --[t_compose_with_identity {map: unitary_U_on_K_with_T^n=P_H U^n|_H}]--> output: `s_unitary_dilation_of_T`
4. input: `s_unitary_dilation_of_T` --[t_reduce_to_canonical_form {form: minimal_unitary_dilation_unique}]--> output: `s_sz_nagy_dilation`

**Techniques used:** t_auxiliary_construction, t_raise_dimension, t_compose_with_identity, t_reduce_to_canonical_form

---

### Choi's theorem on completely positive maps (cite: https://en.wikipedia.org/wiki/Choi%27s_theorem_on_completely_positive_maps)

**Axioms:** `s_matrix_algebra_M_n`, `s_linear_map_φ:M_n→M_m`
**Terminal:** `s_choi_theorem` (kind: theorem)

**Steps:**
1. input: `s_linear_map_φ:M_n→M_m` --[t_auxiliary_construction {object: Choi_matrix_C_φ=Σ_{ij} E_{ij}⊗φ(E_{ij})}]--> output: `s_choi_matrix`
2. input: `s_choi_matrix` --[t_duality {pairing: φ_CP_⇔_C_φ_positive_semidefinite}]--> output: `s_positive_choi_matrix_characterization`
3. input: `s_positive_choi_matrix_characterization` --[t_svd_and_spectral_decomposition {object: spectral_decomp_C_φ=Σ_k v_k v_k*}]--> output: `s_kraus_operators_V_k_from_eigenvectors`
4. input: `s_kraus_operators_V_k_from_eigenvectors` --[t_reduce_to_canonical_form {form: φ(X)=Σ_k V_k X V_k*}]--> output: `s_choi_theorem`

**Techniques used:** t_auxiliary_construction, t_duality, t_svd_and_spectral_decomposition, t_reduce_to_canonical_form

---

### Kadison transitivity theorem (cite: https://en.wikipedia.org/wiki/Kadison_transitivity_theorem)

**Axioms:** `s_irreducible_representation_π_of_C*_algebra`, `s_finite_set_of_target_vectors`
**Terminal:** `s_kadison_transitivity` (kind: theorem)

**Steps:**
1. input: `s_irreducible_representation_π_of_C*_algebra` --[t_auxiliary_construction {object: bicommutant_π(A)''=B(H)_by_irreducibility}]--> output: `s_bicommutant_equals_B(H)`
2. input: `s_bicommutant_equals_B(H)` --[t_compose_with_identity {tool: Kaplansky_density_in_unit_ball}]--> output: `s_strong_density_in_unit_ball`
3. input: `s_strong_density_in_unit_ball` --[t_contraction_fixed_point {scheme: successive_approximation_for_finite_vectors_with_geometric_error}]--> output: `s_exact_lift_to_a∈A`
4. input: `s_exact_lift_to_a∈A` --[t_reduce_to_canonical_form {form: π(a)ξ_i=η_i_with_‖a‖_controlled}]--> output: `s_kadison_transitivity`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_contraction_fixed_point, t_reduce_to_canonical_form

---

### Kaplansky density theorem (cite: https://en.wikipedia.org/wiki/Kaplansky_density_theorem)

**Axioms:** `s_c_star_subalgebra_A_of_B(H)`, `s_double_commutant_A_double_prime`
**Terminal:** `s_kaplansky_density` (kind: theorem)

**Steps:**
1. input: `s_c_star_subalgebra_A_of_B(H)` --[t_auxiliary_construction {object: continuous_functional_calculus_on_self_adjoint_part}]--> output: `s_sa_part_dense_via_functional_calculus`
2. input: `s_sa_part_dense_via_functional_calculus` --[t_interpolate_and_continue {limit: bounded_function_f(x)=2x/(1+x²)_truncation}]--> output: `s_unit_ball_approximation_by_truncation`
3. input: `s_unit_ball_approximation_by_truncation` --[t_reduce_to_canonical_form {form: unit_ball_of_A_strongly_dense_in_unit_ball_of_A''}]--> output: `s_kaplansky_density`

**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_reduce_to_canonical_form

---

### Von Neumann bicommutant theorem (cite: https://en.wikipedia.org/wiki/Von_Neumann_bicommutant_theorem)

**Axioms:** `s_unital_*subalgebra_M_of_B(H)`, `s_commutant_M_prime`
**Terminal:** `s_bicommutant_theorem` (kind: theorem)

**Steps:**
1. input: `s_unital_*subalgebra_M_of_B(H)` --[t_auxiliary_construction {object: cyclic_subspace_M[ξ]_for_each_ξ}]--> output: `s_cyclic_subspaces_with_projections_in_M_prime`
2. input: `s_cyclic_subspaces_with_projections_in_M_prime` --[t_projection_to_subspace {target: T∈M''_preserves_each_M[ξ]}]--> output: `s_invariance_of_cyclic_subspaces_under_M''`
3. input: `s_invariance_of_cyclic_subspaces_under_M''` --[t_compactness_argument {tool: strong_operator_approximation_on_finite_vectors}]--> output: `s_strong_approximation_of_T_by_M`
4. input: `s_strong_approximation_of_T_by_M` --[t_reduce_to_canonical_form {form: M''=closure_SOT_M_=closure_WOT_M}]--> output: `s_bicommutant_theorem`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_compactness_argument, t_reduce_to_canonical_form

---

### Murray–von Neumann classification of factors (cite: https://en.wikipedia.org/wiki/Von_Neumann_algebra#Factors)

**Axioms:** `s_factor_M_trivial_center`, `s_equivalence_of_projections_p~q`
**Terminal:** `s_mvn_factor_classification` (kind: theorem)

**Steps:**
1. input: `s_equivalence_of_projections_p~q` --[t_auxiliary_construction {object: dimension_function_d:Proj(M)→[0,∞]_via_partial_isometries}]--> output: `s_dimension_function_d`
2. input: `s_dimension_function_d` --[t_spot_pattern_in_table {features: range_d(Proj(M))_=_{0,..,n}∞|[0,1]|[0,∞]|{0,∞}}]--> output: `s_three_dimension_patterns_observed`
3. input: `s_three_dimension_patterns_observed` --[t_axiomatize_from_instances {axioms: type_I/II/III_by_dimension_range_and_minimal_projection_existence}]--> output: `s_type_axioms_I_II_III`
4. input: `s_type_axioms_I_II_III` --[t_reduce_to_canonical_form {form: M_=_type_I_n,I_∞,II_1,II_∞,III}]--> output: `s_mvn_factor_classification`

**Techniques used:** t_auxiliary_construction, t_spot_pattern_in_table, t_axiomatize_from_instances, t_reduce_to_canonical_form

---

### Tomita–Takesaki modular theory (cite: https://en.wikipedia.org/wiki/Tomita%E2%80%93Takesaki_theory)

**Axioms:** `s_von_neumann_algebra_M`, `s_cyclic_separating_vector_Ω`
**Terminal:** `s_tomita_takesaki` (kind: theorem)

**Steps:**
1. input: `s_cyclic_separating_vector_Ω` --[t_auxiliary_construction {object: closable_antilinear_S:aΩ↦a*Ω}]--> output: `s_antilinear_operator_S_closable`
2. input: `s_antilinear_operator_S_closable` --[t_svd_and_spectral_decomposition {object: polar_decomposition_S=JΔ^{1/2}}]--> output: `s_modular_conjugation_J_modular_operator_Δ`
3. input: `s_modular_conjugation_J_modular_operator_Δ` --[t_duality {pairing: JMJ=M'_and_Δ^{it}MΔ^{-it}=M}]--> output: `s_modular_automorphism_group_σ_t`
4. input: `s_modular_automorphism_group_σ_t` --[t_reduce_to_canonical_form {form: KMS_condition_at_β=-1_for_(M,Ω)}]--> output: `s_tomita_takesaki`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_duality, t_reduce_to_canonical_form

---

### Connes' classification of injective factors (cite: https://en.wikipedia.org/wiki/Hyperfinite_type_II_factor#Connes'_theorem)

**Axioms:** `s_injective_factor_M`, `s_tomita_takesaki`
**Terminal:** `s_connes_injective_classification` (kind: theorem)

**Steps:**
1. input: `s_injective_factor_M` --[t_compose_with_identity {tool: tomita_takesaki_yields_modular_flow_σ_t}]--> output: `s_modular_flow_on_M`
2. input: `s_modular_flow_on_M` --[t_auxiliary_construction {invariant: Connes_spectrum_S(M)⊂[0,∞)_and_T(M)⊂ℝ}]--> output: `s_connes_invariants_S_T`
3. input: `s_connes_invariants_S_T` --[t_spot_pattern_in_table {features: S(M)={0,1}|{0}∪{λ^n}|{0,1}|[0,∞)_⇒_type_III_λ_subtypes}]--> output: `s_type_III_λ_subclassification`
4. input: `s_type_III_λ_subclassification` --[t_ultraproduct_transfer {transfer: hyperfinite_via_central_sequence_algebra}]--> output: `s_uniqueness_of_hyperfinite_II_1_and_III_λ`
5. input: `s_uniqueness_of_hyperfinite_II_1_and_III_λ` --[t_reduce_to_canonical_form {form: complete_list_R,R_λ,R_∞,R_0,1}]--> output: `s_connes_injective_classification`

**Techniques used:** t_compose_with_identity, t_auxiliary_construction, t_spot_pattern_in_table, t_ultraproduct_transfer, t_reduce_to_canonical_form

---

### Atkinson's theorem (Fredholm operators) (cite: https://en.wikipedia.org/wiki/Atkinson%27s_theorem)

**Axioms:** `s_bounded_operator_T_on_banach_space`, `s_compact_operators_K(X)`
**Terminal:** `s_atkinson_theorem` (kind: theorem)

**Steps:**
1. input: `s_bounded_operator_T_on_banach_space` --[t_auxiliary_construction {object: Calkin_algebra_B(X)/K(X)}]--> output: `s_calkin_algebra_quotient`
2. input: `s_calkin_algebra_quotient` --[t_duality {pairing: Fredholm_⇔_invertible_in_Calkin}]--> output: `s_fredholm_iff_invertible_modulo_compacts`
3. input: `s_fredholm_iff_invertible_modulo_compacts` --[t_reduce_to_canonical_form {form: ker_T,coker_T_finite_dim_with_closed_range}]--> output: `s_atkinson_theorem`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Index of Toeplitz operators on the circle (cite: https://en.wikipedia.org/wiki/Toeplitz_operator#Index_theory)

**Axioms:** `s_continuous_symbol_φ_on_S1_nonvanishing`, `s_hardy_space_H2`
**Terminal:** `s_toeplitz_index_formula` (kind: theorem)

**Steps:**
1. input: `s_continuous_symbol_φ_on_S1_nonvanishing` --[t_auxiliary_construction {operator: T_φ=P_+_M_φ_|_H²}]--> output: `s_toeplitz_operator_T_φ`
2. input: `s_toeplitz_operator_T_φ` --[t_compose_with_identity {tool: Atkinson_via_T_φT_ψ-T_{φψ}_compact}]--> output: `s_T_φ_fredholm_iff_φ_invertible`
3. input: `s_T_φ_fredholm_iff_φ_invertible` --[t_k_theoretic_index_bridge {invariant: ind(T_φ)=-winding_number(φ)}]--> output: `s_toeplitz_index_formula`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_k_theoretic_index_bridge

---

### Calkin algebra index map (cite: https://en.wikipedia.org/wiki/Calkin_algebra)

**Axioms:** `s_calkin_algebra_quotient`, `s_atkinson_theorem`
**Terminal:** `s_calkin_index_map` (kind: theorem)

**Steps:**
1. input: `s_calkin_algebra_quotient` --[t_auxiliary_construction {sequence: 0→K(H)→B(H)→Q(H)→0_short_exact}]--> output: `s_short_exact_sequence_of_C*_algebras`
2. input: `s_short_exact_sequence_of_C*_algebras` --[t_k_theoretic_index_bridge {invariant: 6_term_exact_sequence_in_K_theory}]--> output: `s_six_term_K_theory_sequence`
3. input: `s_six_term_K_theory_sequence` --[t_reduce_to_canonical_form {form: index_map_K_1(Q(H))→K_0(K(H))=Z}]--> output: `s_calkin_index_map`

**Techniques used:** t_auxiliary_construction, t_k_theoretic_index_bridge, t_reduce_to_canonical_form

---

### Fuglede's theorem (cite: https://en.wikipedia.org/wiki/Fuglede%27s_theorem)

**Axioms:** `s_normal_operator_N`, `s_bounded_operator_B_with_BN=NB`
**Terminal:** `s_fuglede_theorem` (kind: theorem)

**Steps:**
1. input: `s_bounded_operator_B_with_BN=NB` --[t_auxiliary_construction {object: e^{i(zN+\bar z N*)}_unitary_via_normality}]--> output: `s_unitary_one_parameter_family_U(z)`
2. input: `s_unitary_one_parameter_family_U(z)` --[t_compose_with_identity {tool: f(z)=U(z)BU(-z)_entire_bounded}]--> output: `s_entire_bounded_operator_valued_function`
3. input: `s_entire_bounded_operator_valued_function` --[t_reductio_ad_absurdum {use: Liouville_⇒_f_constant_⇒_BN*=N*B}]--> output: `s_fuglede_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_reductio_ad_absurdum

---

### Putnam–Fuglede theorem (cite: https://en.wikipedia.org/wiki/Fuglede%27s_theorem#Putnam's_generalization)

**Axioms:** `s_pair_of_normal_operators_M_N`, `s_intertwiner_T_with_TM=NT`
**Terminal:** `s_putnam_fuglede` (kind: theorem)

**Steps:**
1. input: `s_intertwiner_T_with_TM=NT` --[t_auxiliary_construction {operator: block_normal_N⊕M_on_H⊕K}]--> output: `s_block_normal_operator`
2. input: `s_block_normal_operator` --[t_compose_with_identity {tool: Fuglede_applied_to_block_with_intertwiner_off_diagonal}]--> output: `s_block_intertwiner_commutes_with_adjoint`
3. input: `s_block_intertwiner_commutes_with_adjoint` --[t_reduce_to_canonical_form {form: TM*=N*T}]--> output: `s_putnam_fuglede`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_reduce_to_canonical_form

---

### Banach–Stone theorem (cite: https://en.wikipedia.org/wiki/Banach%E2%80%93Stone_theorem)

**Axioms:** `s_compact_hausdorff_pair_K_L`, `s_isometric_isomorphism_C(K)→C(L)`
**Terminal:** `s_banach_stone` (kind: theorem)

**Steps:**
1. input: `s_isometric_isomorphism_C(K)→C(L)` --[t_duality {pairing: extreme_points_of_unit_ball_of_C(K)*=±point_masses}]--> output: `s_isometry_sends_point_masses_to_point_masses`
2. input: `s_isometry_sends_point_masses_to_point_masses` --[t_auxiliary_construction {map: induced_homeomorphism_τ:L→K}]--> output: `s_induced_homeomorphism_τ`
3. input: `s_induced_homeomorphism_τ` --[t_reduce_to_canonical_form {form: (Tf)(y)=h(y)f(τ(y))_with_|h|=1}]--> output: `s_banach_stone`

**Techniques used:** t_duality, t_auxiliary_construction, t_reduce_to_canonical_form

---

### Plancherel theorem (cite: https://en.wikipedia.org/wiki/Plancherel_theorem)

**Axioms:** `s_L2_function_space`, `s_fourier_transform_on_L1_cap_L2`
**Terminal:** `s_plancherel_theorem` (kind: theorem)

**Steps:**
1. input: `s_fourier_transform_on_L1_cap_L2` --[t_fourier_transform {target: Schwartz_space_S(R^n)}]--> output: `s_fourier_on_schwartz_with_‖f̂‖_2=‖f‖_2`
2. input: `s_fourier_on_schwartz_with_‖f̂‖_2=‖f‖_2` --[t_interpolate_and_continue {limit: extend_by_density_to_L²}]--> output: `s_unitary_extension_to_L²`
3. input: `s_unitary_extension_to_L²` --[t_reduce_to_canonical_form {form: F:L²→L²_unitary}]--> output: `s_plancherel_theorem`

**Techniques used:** t_fourier_transform, t_interpolate_and_continue, t_reduce_to_canonical_form

---

### Bochner's theorem (cite: https://en.wikipedia.org/wiki/Bochner%27s_theorem)

**Axioms:** `s_continuous_positive_definite_function_on_R`, `s_fourier_inversion_program`
**Terminal:** `s_bochner_theorem` (kind: theorem)

**Steps:**
1. input: `s_continuous_positive_definite_function_on_R` --[t_auxiliary_construction {object: GNS_state_on_group_C*_algebra_C*(R)≅C_0(R)}]--> output: `s_state_on_commutative_group_C_star`
2. input: `s_state_on_commutative_group_C_star` --[t_duality {pairing: positive_states_on_C_0(R)↔positive_measures}]--> output: `s_positive_measure_μ_via_Riesz_Markov`
3. input: `s_positive_measure_μ_via_Riesz_Markov` --[t_fourier_transform {inverse: φ(t)=∫e^{itx}dμ(x)}]--> output: `s_bochner_theorem`

**Techniques used:** t_auxiliary_construction, t_duality, t_fourier_transform

---

### Peter–Weyl theorem (cite: https://en.wikipedia.org/wiki/Peter%E2%80%93Weyl_theorem)

**Axioms:** `s_compact_topological_group_G`, `s_haar_measure_on_G`
**Terminal:** `s_peter_weyl` (kind: theorem)

**Steps:**
1. input: `s_compact_topological_group_G` --[t_auxiliary_construction {object: regular_representation_on_L²(G)}]--> output: `s_left_regular_representation`
2. input: `s_left_regular_representation` --[t_svd_and_spectral_decomposition {object: convolution_with_continuous_class_function_compact_self_adjoint}]--> output: `s_compact_self_adjoint_convolution_operators`
3. input: `s_compact_self_adjoint_convolution_operators` --[t_character_decomposition_count {invariant: matrix_coefficients_of_finite_dim_irreducibles}]--> output: `s_finite_dim_irreps_dense_in_L²(G)`
4. input: `s_finite_dim_irreps_dense_in_L²(G)` --[t_reduce_to_canonical_form {form: L²(G)=⊕_π dim(π)·π_⊗_π*}]--> output: `s_peter_weyl`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_character_decomposition_count, t_reduce_to_canonical_form

---

### Stone–von Neumann theorem (cite: https://en.wikipedia.org/wiki/Stone%E2%80%93von_Neumann_theorem)

**Axioms:** `s_canonical_commutation_relations_PQ_QP=iħ`, `s_irreducibility_assumption`
**Terminal:** `s_stone_von_neumann` (kind: theorem)

**Steps:**
1. input: `s_canonical_commutation_relations_PQ_QP=iħ` --[t_auxiliary_construction {object: Weyl_unitaries_U(s)V(t)=e^{ist}V(t)U(s)}]--> output: `s_weyl_form_of_CCR`
2. input: `s_weyl_form_of_CCR` --[t_symmetry_reduction {symmetry: Heisenberg_group_representation}]--> output: `s_heisenberg_group_representation`
3. input: `s_heisenberg_group_representation` --[t_character_decomposition_count {invariant: central_character_=_e^{itħ}}]--> output: `s_fixed_central_character_irreducible`
4. input: `s_fixed_central_character_irreducible` --[t_structural_isomorphism {iso: unique_up_to_unitary_equivalence_=_Schrödinger_rep_on_L²(R)}]--> output: `s_stone_von_neumann`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_character_decomposition_count, t_structural_isomorphism

---

### Schwartz kernel theorem (cite: https://en.wikipedia.org/wiki/Schwartz_kernel_theorem)

**Axioms:** `s_continuous_bilinear_form_on_test_functions`, `s_schwartz_space_distributions_pair`
**Terminal:** `s_schwartz_kernel_theorem` (kind: theorem)

**Steps:**
1. input: `s_continuous_bilinear_form_on_test_functions` --[t_duality {pairing: D(X)⊗D(Y)→C_continuous}]--> output: `s_jointly_continuous_bilinear_form`
2. input: `s_jointly_continuous_bilinear_form` --[t_compose_with_identity {tool: nuclear_space_property_of_D(X)}]--> output: `s_factor_through_completed_tensor_product_D(X×Y)`
3. input: `s_jointly_continuous_bilinear_form` --[t_representable_functor_trick {functor: Hom(D(X)⊗D(Y),C)≅D'(X×Y)}]--> output: `s_kernel_distribution_K∈D'(X×Y)`
4. input: `s_kernel_distribution_K∈D'(X×Y)` --[t_reduce_to_canonical_form {form: B(φ,ψ)=⟨K,φ⊗ψ⟩}]--> output: `s_schwartz_kernel_theorem`

**Techniques used:** t_duality, t_compose_with_identity, t_representable_functor_trick, t_reduce_to_canonical_form

---

### Nuclear space characterization (Grothendieck) (cite: https://en.wikipedia.org/wiki/Nuclear_space)

**Axioms:** `s_locally_convex_space_X`, `s_family_of_seminorms_p_α`
**Terminal:** `s_nuclear_space_grothendieck` (kind: theorem)

**Steps:**
1. input: `s_locally_convex_space_X` --[t_auxiliary_construction {object: canonical_maps_X_α→X_β_for_seminorm_pair}]--> output: `s_canonical_maps_between_local_banach_spaces`
2. input: `s_canonical_maps_between_local_banach_spaces` --[t_compactness_argument {tool: each_canonical_map_nuclear_=_trace_class_factorization}]--> output: `s_nuclear_canonical_maps`
3. input: `s_nuclear_canonical_maps` --[t_representable_functor_trick {functor: tensor_products_π_=_ε_for_nuclear}]--> output: `s_uniqueness_of_tensor_product_topology`
4. input: `s_uniqueness_of_tensor_product_topology` --[t_reduce_to_canonical_form {form: Schwartz_space_is_nuclear_⇒_kernel_theorem}]--> output: `s_nuclear_space_grothendieck`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_representable_functor_trick, t_reduce_to_canonical_form

---

### Sobolev embedding theorem (cite: https://en.wikipedia.org/wiki/Sobolev_inequality)

**Axioms:** `s_sobolev_space_Wkp(R^n)`, `s_riesz_potential_estimate`
**Terminal:** `s_sobolev_embedding` (kind: theorem)

**Steps:**
1. input: `s_sobolev_space_Wkp(R^n)` --[t_fourier_transform {target: Bessel_potential_(1-Δ)^{-k/2}_on_L^p_via_multiplier}]--> output: `s_bessel_potential_representation`
2. input: `s_bessel_potential_representation` --[t_frequency_decomposition {tool: Littlewood_Paley_dyadic_blocks}]--> output: `s_dyadic_block_decomposition_of_u`
3. input: `s_dyadic_block_decomposition_of_u` --[t_exhaustion_squeeze {inequality: Hardy_Littlewood_Sobolev_‖I_α f‖_q≤C‖f‖_p_for_1/p-1/q=α/n}]--> output: `s_hardy_littlewood_sobolev_inequality`
4. input: `s_hardy_littlewood_sobolev_inequality` --[t_reduce_to_canonical_form {form: Wkp↪L^{p*}_for_kp<n_or_↪C^m_for_kp>n+m}]--> output: `s_sobolev_embedding`

**Techniques used:** t_fourier_transform, t_frequency_decomposition, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Rellich–Kondrachov compactness theorem (cite: https://en.wikipedia.org/wiki/Rellich%E2%80%93Kondrachov_theorem)

**Axioms:** `s_bounded_lipschitz_domain_Ω`, `s_sobolev_embedding`
**Terminal:** `s_rellich_kondrachov` (kind: theorem)

**Steps:**
1. input: `s_sobolev_embedding` --[t_auxiliary_construction {object: convolution_with_mollifier_η_ε}]--> output: `s_mollification_approximant_u_ε`
2. input: `s_mollification_approximant_u_ε` --[t_exhaustion_squeeze {bound: ‖u-u_ε‖_p≤Cε‖∇u‖_p_via_Poincaré_type}]--> output: `s_equicontinuity_in_L^p`
3. input: `s_equicontinuity_in_L^p` --[t_compactness_argument {tool: Fréchet_Kolmogorov_compactness_in_L^p}]--> output: `s_precompact_set_in_L^p`
4. input: `s_precompact_set_in_L^p` --[t_reduce_to_canonical_form {form: W^{1,p}(Ω)↪↪L^q(Ω)_for_q<p*}]--> output: `s_rellich_kondrachov`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_compactness_argument, t_reduce_to_canonical_form

---

### Fréchet–Kolmogorov compactness theorem (cite: https://en.wikipedia.org/wiki/Fr%C3%A9chet%E2%80%93Kolmogorov_theorem)

**Axioms:** `s_subset_F_of_Lp`, `s_translation_continuity_uniform`
**Terminal:** `s_frechet_kolmogorov` (kind: theorem)

**Steps:**
1. input: `s_subset_F_of_Lp` --[t_auxiliary_construction {object: mollifier_convolution_F_ε=F*η_ε}]--> output: `s_mollified_family_uniformly_close_to_F`
2. input: `s_mollified_family_uniformly_close_to_F` --[t_compactness_argument {tool: Arzelà_Ascoli_on_compactly_supported_continuous_versions}]--> output: `s_precompact_after_mollification`
3. input: `s_precompact_after_mollification` --[t_exhaustion_squeeze {limit: ε→0_uniform_approximation_⇒_total_boundedness}]--> output: `s_frechet_kolmogorov`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Trace theorem for Sobolev spaces (cite: https://en.wikipedia.org/wiki/Trace_operator)

**Axioms:** `s_lipschitz_domain_Ω_with_boundary`, `s_sobolev_space_W1p(Ω)`
**Terminal:** `s_trace_theorem` (kind: theorem)

**Steps:**
1. input: `s_sobolev_space_W1p(Ω)` --[t_auxiliary_construction {object: smooth_dense_subset_C∞(Ω̄)_with_pointwise_boundary_values}]--> output: `s_smooth_functions_dense_in_W1p`
2. input: `s_smooth_functions_dense_in_W1p` --[t_exhaustion_squeeze {bound: ‖tr(u)‖_{W^{1-1/p,p}(∂Ω)}≤C‖u‖_{W^{1,p}(Ω)}_via_partition_of_unity}]--> output: `s_boundary_trace_estimate`
3. input: `s_boundary_trace_estimate` --[t_interpolate_and_continue {limit: extend_trace_by_density_to_full_W1p}]--> output: `s_trace_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_interpolate_and_continue

---

### Calderón extension theorem (cite: https://en.wikipedia.org/wiki/Sobolev_space#Extension_by_zero)

**Axioms:** `s_lipschitz_domain_Ω`, `s_sobolev_function_on_Ω`
**Terminal:** `s_calderon_extension` (kind: theorem)

**Steps:**
1. input: `s_lipschitz_domain_Ω` --[t_auxiliary_construction {object: local_charts_flattening_boundary_+_partition_of_unity}]--> output: `s_local_half_space_reduction`
2. input: `s_local_half_space_reduction` --[t_symmetry_reduction {symmetry: reflection_across_∂R^n_+_higher_order_combinations}]--> output: `s_reflection_extension_in_each_chart`
3. input: `s_reflection_extension_in_each_chart` --[t_compose_with_identity {map: glue_via_partition_of_unity_to_E:W^{k,p}(Ω)→W^{k,p}(R^n)}]--> output: `s_calderon_extension`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_compose_with_identity

---

### Gagliardo–Nirenberg interpolation inequality (cite: https://en.wikipedia.org/wiki/Gagliardo%E2%80%93Nirenberg_interpolation_inequality)

**Axioms:** `s_smooth_compactly_supported_function`, `s_lebesgue_index_triple_p_q_r`
**Terminal:** `s_gagliardo_nirenberg` (kind: theorem)

**Steps:**
1. input: `s_smooth_compactly_supported_function` --[t_rescale_for_asymptotic_geometry {symmetry: dilation_u_λ(x)=u(λx)_forces_exponent_relation}]--> output: `s_scaling_dimensional_balance`
2. input: `s_scaling_dimensional_balance` --[t_frequency_decomposition {tool: Littlewood_Paley_dyadic_decomposition}]--> output: `s_interpolation_inequality_on_dyadic_blocks`
3. input: `s_interpolation_inequality_on_dyadic_blocks` --[t_interpolate_and_continue {limit: Hölder_+_Sobolev_on_blocks_summed}]--> output: `s_full_interpolation_estimate`
4. input: `s_full_interpolation_estimate` --[t_reduce_to_canonical_form {form: ‖u‖_p≤C‖∇^m u‖_r^θ ‖u‖_q^{1-θ}}]--> output: `s_gagliardo_nirenberg`

**Techniques used:** t_rescale_for_asymptotic_geometry, t_frequency_decomposition, t_interpolate_and_continue, t_reduce_to_canonical_form

---

### Riesz–Thorin interpolation theorem (cite: https://en.wikipedia.org/wiki/Riesz%E2%80%93Thorin_theorem)

**Axioms:** `s_linear_operator_bounded_at_two_endpoints`, `s_lebesgue_endpoint_pairs`
**Terminal:** `s_riesz_thorin` (kind: theorem)

**Steps:**
1. input: `s_linear_operator_bounded_at_two_endpoints` --[t_auxiliary_construction {object: analytic_family_F(z)=∫(Tf_z)g_z_dμ_on_strip_0≤Rez≤1}]--> output: `s_analytic_family_in_complex_strip`
2. input: `s_analytic_family_in_complex_strip` --[t_compactness_argument {tool: Hadamard_three_lines_theorem_on_strip}]--> output: `s_three_lines_bound_on_F(z)`
3. input: `s_three_lines_bound_on_F(z)` --[t_interpolate_and_continue {limit: optimize_over_simple_f,g_then_density}]--> output: `s_riesz_thorin`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_interpolate_and_continue

---

### Marcinkiewicz interpolation theorem (cite: https://en.wikipedia.org/wiki/Marcinkiewicz_interpolation_theorem)

**Axioms:** `s_sublinear_operator_weak_type_at_endpoints`, `s_lorentz_spaces_Lp_q`
**Terminal:** `s_marcinkiewicz_interpolation` (kind: theorem)

**Steps:**
1. input: `s_sublinear_operator_weak_type_at_endpoints` --[t_auxiliary_construction {object: layer_cake_split_f=f_χ_{|f|>λ}+f_χ_{|f|≤λ}}]--> output: `s_layer_cake_decomposition`
2. input: `s_layer_cake_decomposition` --[t_frequency_decomposition {tool: distribution_function_d_f(λ)_estimates}]--> output: `s_distribution_function_bounds`
3. input: `s_distribution_function_bounds` --[t_interpolate_and_continue {limit: integrate_over_λ_with_optimal_λ(f)}]--> output: `s_strong_type_estimate`
4. input: `s_strong_type_estimate` --[t_reduce_to_canonical_form {form: strong_(p,p)_for_p_between_endpoints}]--> output: `s_marcinkiewicz_interpolation`

**Techniques used:** t_auxiliary_construction, t_frequency_decomposition, t_interpolate_and_continue, t_reduce_to_canonical_form

---

### Hörmander–Mikhlin multiplier theorem (cite: https://en.wikipedia.org/wiki/Multiplier_(Fourier_analysis)#H%C3%B6rmander%E2%80%93Mikhlin_multiplier_theorem)

**Axioms:** `s_bounded_fourier_multiplier_m`, `s_mikhlin_derivative_estimates`
**Terminal:** `s_hormander_mikhlin` (kind: theorem)

**Steps:**
1. input: `s_bounded_fourier_multiplier_m` --[t_fourier_transform {target: convolution_operator_T_m_f=F^{-1}(m·f̂)}]--> output: `s_convolution_operator_with_kernel_K_m`
2. input: `s_convolution_operator_with_kernel_K_m` --[t_frequency_decomposition {tool: Littlewood_Paley_pieces_φ_j(ξ)m(ξ)}]--> output: `s_dyadic_pieces_with_bounded_derivatives`
3. input: `s_dyadic_pieces_with_bounded_derivatives` --[t_exhaustion_squeeze {bound: Calderón_Zygmund_kernel_estimate_|∇K|≤C/|x|^{n+1}}]--> output: `s_CZ_singular_integral_bounds`
4. input: `s_CZ_singular_integral_bounds` --[t_interpolate_and_continue {limit: strong_(p,p)_for_1<p<∞_via_Marcinkiewicz}]--> output: `s_hormander_mikhlin`

**Techniques used:** t_fourier_transform, t_frequency_decomposition, t_exhaustion_squeeze, t_interpolate_and_continue

---

### Calderón–Zygmund decomposition (cite: https://en.wikipedia.org/wiki/Calder%C3%B3n%E2%80%93Zygmund_lemma)

**Axioms:** `s_L1_function_on_Rn`, `s_dyadic_cube_grid`
**Terminal:** `s_calderon_zygmund_decomposition` (kind: theorem)

**Steps:**
1. input: `s_L1_function_on_Rn` --[t_auxiliary_construction {object: stopping_time_on_dyadic_grid_at_level_α}]--> output: `s_maximal_dyadic_cubes_with_average>α`
2. input: `s_maximal_dyadic_cubes_with_average>α` --[t_projection_to_subspace {target: bad_part_b=Σ_Q(f-f_Q)χ_Q,good_part_g=f-b}]--> output: `s_good_bad_decomposition_f=g+b`
3. input: `s_good_bad_decomposition_f=g+b` --[t_exhaustion_squeeze {bounds: ‖g‖_∞≤Cα,_∫b_Q=0,_|∪Q|≤‖f‖_1/α}]--> output: `s_calderon_zygmund_decomposition`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_exhaustion_squeeze

---

### Hardy–Littlewood maximal inequality (cite: https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood_maximal_function)

**Axioms:** `s_L1_function_on_Rn`, `s_centered_maximal_function_Mf`
**Terminal:** `s_hardy_littlewood_maximal_inequality` (kind: theorem)

**Steps:**
1. input: `s_L1_function_on_Rn` --[t_auxiliary_construction {object: level_set_E_α={Mf>α}}]--> output: `s_level_set_of_maximal_function`
2. input: `s_level_set_of_maximal_function` --[t_compactness_argument {tool: Vitali_covering_lemma_on_E_α}]--> output: `s_disjoint_balls_with_5_fold_cover`
3. input: `s_disjoint_balls_with_5_fold_cover` --[t_exhaustion_squeeze {bound: |E_α|≤(5^n/α)‖f‖_1}]--> output: `s_weak_type_(1,1)_estimate`
4. input: `s_weak_type_(1,1)_estimate` --[t_interpolate_and_continue {limit: Marcinkiewicz_with_trivial_(∞,∞)_bound}]--> output: `s_hardy_littlewood_maximal_inequality`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze, t_interpolate_and_continue

---

### Lebesgue differentiation theorem (cite: https://en.wikipedia.org/wiki/Lebesgue_differentiation_theorem)

**Axioms:** `s_locally_integrable_function_on_Rn`, `s_hardy_littlewood_maximal_inequality`
**Terminal:** `s_lebesgue_differentiation` (kind: theorem)

**Steps:**
1. input: `s_locally_integrable_function_on_Rn` --[t_auxiliary_construction {object: continuous_approximant_g_close_in_L¹}]--> output: `s_continuous_approximant_with_‖f-g‖_1<ε`
2. input: `s_continuous_approximant_with_‖f-g‖_1<ε` --[t_compose_with_identity {tool: Lebesgue_differentiation_for_g_continuous_is_pointwise}]--> output: `s_pointwise_a.e._convergence_for_g`
3. input: `s_pointwise_a.e._convergence_for_g` --[t_exhaustion_squeeze {tool: HL_maximal_controls_|f-g|_difference}]--> output: `s_lebesgue_differentiation`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_exhaustion_squeeze

---

### Arzelà–Ascoli theorem (cite: https://en.wikipedia.org/wiki/Arzel%C3%A0%E2%80%93Ascoli_theorem)

**Axioms:** `s_compact_metric_space_K`, `s_equicontinuous_pointwise_bounded_family`
**Terminal:** `s_arzela_ascoli` (kind: theorem)

**Steps:**
1. input: `s_equicontinuous_pointwise_bounded_family` --[t_auxiliary_construction {object: dense_countable_subset_D⊂K}]--> output: `s_dense_countable_subset`
2. input: `s_dense_countable_subset` --[t_compactness_argument {tool: Cantor_diagonal_extraction_at_D}]--> output: `s_pointwise_convergent_subsequence_on_D`
3. input: `s_pointwise_convergent_subsequence_on_D` --[t_exhaustion_squeeze {bound: equicontinuity_⇒_uniform_Cauchy_on_K}]--> output: `s_uniform_cauchy_subsequence`
4. input: `s_uniform_cauchy_subsequence` --[t_reduce_to_canonical_form {form: precompact_iff_equicontinuous_+_pointwise_bounded}]--> output: `s_arzela_ascoli`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Eberlein–Šmulian theorem (cite: https://en.wikipedia.org/wiki/Eberlein%E2%80%93%C5%A0mulian_theorem)

**Axioms:** `s_banach_space`, `s_weakly_compact_subset_K`
**Terminal:** `s_eberlein_smulian` (kind: theorem)

**Steps:**
1. input: `s_weakly_compact_subset_K` --[t_duality {pairing: K⊂X**_via_canonical_embedding_J:X→X**}]--> output: `s_K_in_double_dual_with_weak_star_compact_image`
2. input: `s_K_in_double_dual_with_weak_star_compact_image` --[t_compactness_argument {tool: Banach_Alaoglu_+_metrizability_of_separable_dual_ball}]--> output: `s_metrizable_weak_star_compact_image`
3. input: `s_metrizable_weak_star_compact_image` --[t_reduce_to_canonical_form {form: weak_compactness_⇔_weak_sequential_compactness}]--> output: `s_eberlein_smulian`

**Techniques used:** t_duality, t_compactness_argument, t_reduce_to_canonical_form

---

### James's theorem (cite: https://en.wikipedia.org/wiki/James%27s_theorem)

**Axioms:** `s_banach_space_X`, `s_every_continuous_linear_functional_attains_norm_on_B_X`
**Terminal:** `s_james_theorem` (kind: theorem)

**Steps:**
1. input: `s_every_continuous_linear_functional_attains_norm_on_B_X` --[t_reductio_ad_absurdum {assume: B_X_not_weakly_compact}]--> output: `s_non_attainment_in_some_functional_construction`
2. input: `s_non_attainment_in_some_functional_construction` --[t_auxiliary_construction {object: nested_separating_functional_sequence_via_Bishop_Phelps_type}]--> output: `s_non_norm_attaining_functional`
3. input: `s_non_norm_attaining_functional` --[t_reductio_ad_absurdum {contradiction: violates_hypothesis}]--> output: `s_james_theorem`

**Techniques used:** t_reductio_ad_absurdum, t_auxiliary_construction

---

### Milman–Pettis theorem (cite: https://en.wikipedia.org/wiki/Milman%E2%80%93Pettis_theorem)

**Axioms:** `s_uniformly_convex_banach_space`, `s_canonical_embedding_into_bidual`
**Terminal:** `s_milman_pettis` (kind: theorem)

**Steps:**
1. input: `s_uniformly_convex_banach_space` --[t_auxiliary_construction {object: modulus_of_convexity_δ(ε)>0}]--> output: `s_quantitative_strict_convexity`
2. input: `s_quantitative_strict_convexity` --[t_compose_with_identity {tool: Goldstine_density_+_uniform_convexity_⇒_J(B_X)=B_{X**}}]--> output: `s_canonical_embedding_surjective_on_unit_balls`
3. input: `s_canonical_embedding_surjective_on_unit_balls` --[t_reduce_to_canonical_form {form: X=X**_reflexive}]--> output: `s_milman_pettis`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_reduce_to_canonical_form

---

### Bishop–Phelps theorem (cite: https://en.wikipedia.org/wiki/Bishop%E2%80%93Phelps_theorem)

**Axioms:** `s_banach_space`, `s_continuous_linear_functional`
**Terminal:** `s_bishop_phelps` (kind: theorem)

**Steps:**
1. input: `s_continuous_linear_functional` --[t_auxiliary_construction {object: support_cone_K_φ,k={x:φ(x)≥k‖x‖}}]--> output: `s_support_cone_partial_order`
2. input: `s_support_cone_partial_order` --[t_compactness_argument {tool: Zorn_on_K_φ,k_chains_yields_maximal_element}]--> output: `s_maximal_element_in_cone`
3. input: `s_maximal_element_in_cone` --[t_duality {pairing: maximal_⇒_supporting_functional_ψ_norm_attaining_close_to_φ}]--> output: `s_bishop_phelps`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_duality

---

### Krein–Smulian theorem (cite: https://en.wikipedia.org/wiki/Krein%E2%80%93Smulian_theorem)

**Axioms:** `s_dual_banach_space_X_star`, `s_convex_set_C_with_C∩nB_weak_star_closed_for_all_n`
**Terminal:** `s_krein_smulian` (kind: theorem)

**Steps:**
1. input: `s_convex_set_C_with_C∩nB_weak_star_closed_for_all_n` --[t_auxiliary_construction {object: polar_C°⊂X_via_duality}]--> output: `s_polar_set_in_X`
2. input: `s_polar_set_in_X` --[t_compactness_argument {tool: Banach_Alaoglu_+_metrizability_on_each_nB}]--> output: `s_weak_star_closure_recoverable_levelwise`
3. input: `s_weak_star_closure_recoverable_levelwise` --[t_reduce_to_canonical_form {form: C_weak_star_closed_globally}]--> output: `s_krein_smulian`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Krein–Rutman theorem (cite: https://en.wikipedia.org/wiki/Krein%E2%80%93Rutman_theorem)

**Axioms:** `s_compact_positive_operator_on_cone`, `s_solid_pointed_cone_K`
**Terminal:** `s_krein_rutman` (kind: theorem)

**Steps:**
1. input: `s_compact_positive_operator_on_cone` --[t_auxiliary_construction {object: rescaled_iterate_T^n x/‖T^n x‖_on_K∩unit_sphere}]--> output: `s_rescaled_iteration_on_cone`
2. input: `s_rescaled_iteration_on_cone` --[t_compactness_argument {tool: compactness_+_Schauder_fixed_point}]--> output: `s_fixed_point_in_cone`
3. input: `s_fixed_point_in_cone` --[t_svd_and_spectral_decomposition {object: leading_eigenvalue_r(T)>0_simple_with_positive_eigenvector}]--> output: `s_krein_rutman`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_svd_and_spectral_decomposition

---

### Schauder fixed-point theorem (cite: https://en.wikipedia.org/wiki/Schauder_fixed-point_theorem)

**Axioms:** `s_compact_convex_subset_of_banach`, `s_continuous_self_map`
**Terminal:** `s_schauder_fpt` (kind: theorem)

**Steps:**
1. input: `s_compact_convex_subset_of_banach` --[t_auxiliary_construction {object: finite_ε_net_+_Schauder_projection_P_ε:K→span(net)}]--> output: `s_finite_dim_approximation_of_K`
2. input: `s_finite_dim_approximation_of_K` --[t_compose_with_identity {tool: Brouwer_fpt_for_P_ε∘f_on_finite_dim_simplex}]--> output: `s_finite_dim_fixed_point_x_ε`
3. input: `s_finite_dim_fixed_point_x_ε` --[t_compactness_argument {limit: extract_convergent_subnet_x_ε→x*}]--> output: `s_schauder_fpt`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_compactness_argument

---

### Markov–Kakutani fixed-point theorem (cite: https://en.wikipedia.org/wiki/Markov%E2%80%93Kakutani_fixed-point_theorem)

**Axioms:** `s_compact_convex_subset_in_locally_convex_space`, `s_commuting_family_of_continuous_affine_maps`
**Terminal:** `s_markov_kakutani` (kind: theorem)

**Steps:**
1. input: `s_commuting_family_of_continuous_affine_maps` --[t_auxiliary_construction {object: Cesàro_averages_A_n(T)=(I+T+...+T^{n-1})/n}]--> output: `s_cesaro_averages_of_maps`
2. input: `s_cesaro_averages_of_maps` --[t_compactness_argument {tool: nested_intersection_of_nonempty_closed_subsets_A_n(T)(K)}]--> output: `s_nonempty_intersection_per_map`
3. input: `s_nonempty_intersection_per_map` --[t_compose_with_identity {tool: commuting_family_⇒_simultaneous_intersection_nonempty}]--> output: `s_markov_kakutani`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_compose_with_identity

---

### Ryll-Nardzewski fixed-point theorem (cite: https://en.wikipedia.org/wiki/Ryll-Nardzewski_fixed-point_theorem)

**Axioms:** `s_weakly_compact_convex_set_K`, `s_noncontracting_semigroup_of_isometries`
**Terminal:** `s_ryll_nardzewski` (kind: theorem)

**Steps:**
1. input: `s_noncontracting_semigroup_of_isometries` --[t_auxiliary_construction {object: minimal_invariant_compact_convex_subset_K_0⊂K}]--> output: `s_minimal_invariant_set_K_0`
2. input: `s_minimal_invariant_set_K_0` --[t_reductio_ad_absurdum {assume: diam(K_0)>0_⇒_strict_contraction_violates_noncontracting}]--> output: `s_K_0_singleton_via_contradiction`
3. input: `s_K_0_singleton_via_contradiction` --[t_reduce_to_canonical_form {form: common_fixed_point_of_semigroup}]--> output: `s_ryll_nardzewski`

**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum, t_reduce_to_canonical_form

---

### Ekeland's variational principle (cite: https://en.wikipedia.org/wiki/Ekeland%27s_variational_principle)

**Axioms:** `s_complete_metric_space`, `s_lower_semicontinuous_bounded_below_function`
**Terminal:** `s_ekeland_variational_principle` (kind: theorem)

**Steps:**
1. input: `s_lower_semicontinuous_bounded_below_function` --[t_auxiliary_construction {object: partial_order_y≼x_iff_f(y)+εd(x,y)≤f(x)}]--> output: `s_partial_order_on_X`
2. input: `s_partial_order_on_X` --[t_compactness_argument {tool: Zorn_lemma_on_decreasing_chains_via_completeness}]--> output: `s_maximal_minimal_element_x_ε`
3. input: `s_maximal_minimal_element_x_ε` --[t_reduce_to_canonical_form {form: f(y)>f(x_ε)-εd(x_ε,y)_for_y≠x_ε}]--> output: `s_ekeland_variational_principle`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Browder–Minty theorem (monotone operators) (cite: https://en.wikipedia.org/wiki/Browder%E2%80%93Minty_theorem)

**Axioms:** `s_reflexive_banach_space`, `s_monotone_coercive_hemicontinuous_operator`
**Terminal:** `s_browder_minty` (kind: theorem)

**Steps:**
1. input: `s_monotone_coercive_hemicontinuous_operator` --[t_auxiliary_construction {object: Galerkin_finite_dim_approximation_T_n_on_X_n}]--> output: `s_finite_dim_galerkin_approximants`
2. input: `s_finite_dim_galerkin_approximants` --[t_compose_with_identity {tool: Brouwer_existence_via_topological_degree_for_T_n}]--> output: `s_finite_dim_solutions_x_n`
3. input: `s_finite_dim_solutions_x_n` --[t_compactness_argument {tool: coercivity_⇒_bounded_⇒_weak_limit}]--> output: `s_weak_limit_x_*`
4. input: `s_weak_limit_x_*` --[t_reduce_to_canonical_form {form: monotonicity_trick_(Minty)_identifies_T(x*)=f}]--> output: `s_browder_minty`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_compactness_argument, t_reduce_to_canonical_form

---

### Mercer's theorem (cite: https://en.wikipedia.org/wiki/Mercer%27s_theorem)

**Axioms:** `s_continuous_symmetric_positive_kernel`, `s_compact_domain_X`
**Terminal:** `s_mercer_theorem` (kind: theorem)

**Steps:**
1. input: `s_continuous_symmetric_positive_kernel` --[t_auxiliary_construction {operator: T_K f(x)=∫K(x,y)f(y)dy_compact_self_adjoint_on_L²(X)}]--> output: `s_integral_operator_compact_self_adjoint`
2. input: `s_integral_operator_compact_self_adjoint` --[t_svd_and_spectral_decomposition {object: eigenvalues_λ_n≥0_+_continuous_eigenfunctions_φ_n}]--> output: `s_spectral_decomposition_of_T_K`
3. input: `s_spectral_decomposition_of_T_K` --[t_interpolate_and_continue {limit: Dini_uniform_convergence_for_positive_kernel}]--> output: `s_uniformly_convergent_kernel_series`
4. input: `s_uniformly_convergent_kernel_series` --[t_reduce_to_canonical_form {form: K(x,y)=Σ λ_n φ_n(x)φ_n(y)_uniformly}]--> output: `s_mercer_theorem`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_interpolate_and_continue, t_reduce_to_canonical_form

---

### Hilbert–Schmidt theorem (cite: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Schmidt_theorem)

**Axioms:** `s_hilbert_schmidt_integral_operator`, `s_L2_function_space`
**Terminal:** `s_hilbert_schmidt_theorem` (kind: theorem)

**Steps:**
1. input: `s_hilbert_schmidt_integral_operator` --[t_auxiliary_construction {object: kernel_K∈L²(X×Y)_yields_compact_operator}]--> output: `s_compact_operator_from_L²_kernel`
2. input: `s_compact_operator_from_L²_kernel` --[t_svd_and_spectral_decomposition {object: SVD_T=Σ_n σ_n⟨·,e_n⟩f_n_with_Σσ_n²=‖K‖²_L²}]--> output: `s_hilbert_schmidt_theorem`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition

---

### Min-max theorem (Courant–Fischer–Weyl) (cite: https://en.wikipedia.org/wiki/Min-max_theorem)

**Axioms:** `s_compact_self_adjoint_operator_T`, `s_eigenvalues_ordered_decreasing`
**Terminal:** `s_min_max_theorem` (kind: theorem)

**Steps:**
1. input: `s_compact_self_adjoint_operator_T` --[t_svd_and_spectral_decomposition {object: eigenpairs_(λ_n,e_n)_with_λ_1≥λ_2≥...}]--> output: `s_eigenpair_sequence`
2. input: `s_eigenpair_sequence` --[t_auxiliary_construction {object: Rayleigh_quotient_R(x)=⟨Tx,x⟩/‖x‖²}]--> output: `s_rayleigh_quotient_with_extremal_property`
3. input: `s_rayleigh_quotient_with_extremal_property` --[t_projection_to_subspace {target: min_max_over_codim_(k-1)_subspaces}]--> output: `s_min_max_theorem`

**Techniques used:** t_svd_and_spectral_decomposition, t_auxiliary_construction, t_projection_to_subspace

---

### Weyl's theorem on essential spectrum (cite: https://en.wikipedia.org/wiki/Weyl%27s_theorem_on_unitary_equivalence)

**Axioms:** `s_self_adjoint_operator_A`, `s_compact_perturbation_K`
**Terminal:** `s_weyl_essential_spectrum` (kind: theorem)

**Steps:**
1. input: `s_compact_perturbation_K` --[t_auxiliary_construction {object: Weyl_sequence_x_n_⇀0_with_‖(A-λ)x_n‖→0}]--> output: `s_weyl_singular_sequence_at_λ`
2. input: `s_weyl_singular_sequence_at_λ` --[t_compactness_argument {tool: K_compact_⇒_Kx_n→0_strongly}]--> output: `s_weyl_sequence_preserved_under_compact_perturbation`
3. input: `s_weyl_sequence_preserved_under_compact_perturbation` --[t_reduce_to_canonical_form {form: σ_ess(A+K)=σ_ess(A)}]--> output: `s_weyl_essential_spectrum`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reduce_to_canonical_form

---

### Lomonosov's invariant subspace theorem (cite: https://en.wikipedia.org/wiki/Lomonosov%27s_invariant_subspace_theorem)

**Axioms:** `s_bounded_operator_commuting_with_nonzero_compact`, `s_banach_space_infinite_dim`
**Terminal:** `s_lomonosov_invariant_subspace` (kind: theorem)

**Steps:**
1. input: `s_bounded_operator_commuting_with_nonzero_compact` --[t_reductio_ad_absurdum {assume: no_nontrivial_closed_invariant_subspace}]--> output: `s_orbit_density_assumption`
2. input: `s_orbit_density_assumption` --[t_auxiliary_construction {object: continuous_map_x↦y_with_Tx_in_open_neighborhood_via_compactness}]--> output: `s_self_map_with_compact_image`
3. input: `s_self_map_with_compact_image` --[t_compose_with_identity {tool: Schauder_fpt_yields_fixed_x_with_compact_eigenvector}]--> output: `s_compact_eigenvector_yields_invariant_subspace`
4. input: `s_compact_eigenvector_yields_invariant_subspace` --[t_reductio_ad_absurdum {contradicts: assumed_no_invariant_subspace}]--> output: `s_lomonosov_invariant_subspace`

**Techniques used:** t_reductio_ad_absurdum, t_auxiliary_construction, t_compose_with_identity

---

### Closed range theorem (cite: https://en.wikipedia.org/wiki/Closed_range_theorem)

**Axioms:** `s_densely_defined_closed_operator_T`, `s_adjoint_T_star`
**Terminal:** `s_closed_range_theorem` (kind: theorem)

**Steps:**
1. input: `s_densely_defined_closed_operator_T` --[t_duality {pairing: range(T)⊥=ker(T*)_via_adjoint_pairing}]--> output: `s_orthogonality_relation_range_kernel`
2. input: `s_orthogonality_relation_range_kernel` --[t_projection_to_subspace {target: range(T)_closed_⇔_range(T*)_closed}]--> output: `s_equivalent_closedness_conditions`
3. input: `s_equivalent_closedness_conditions` --[t_reduce_to_canonical_form {form: range(T)=ker(T*)⊥_when_closed}]--> output: `s_closed_range_theorem`

**Techniques used:** t_duality, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Fredholm alternative (cite: https://en.wikipedia.org/wiki/Fredholm_alternative)

**Axioms:** `s_compact_operator_K_on_banach`, `s_operator_I_minus_K`
**Terminal:** `s_fredholm_alternative` (kind: theorem)

**Steps:**
1. input: `s_compact_operator_K_on_banach` --[t_auxiliary_construction {object: ker(I-K)_finite_dim_via_compactness_of_unit_ball}]--> output: `s_finite_dim_kernel`
2. input: `s_finite_dim_kernel` --[t_compose_with_identity {tool: ind(I-K)=0_invariant_under_compact_perturbation}]--> output: `s_index_zero_fredholm_operator`
3. input: `s_index_zero_fredholm_operator` --[t_duality {pairing: range(I-K)=ker(I-K*)⊥}]--> output: `s_fredholm_alternative`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_duality

---

### Analytic Fredholm theorem (cite: https://en.wikipedia.org/wiki/Analytic_Fredholm_theorem)

**Axioms:** `s_analytic_family_of_compact_operators_K(z)`, `s_connected_domain_D`
**Terminal:** `s_analytic_fredholm` (kind: theorem)

**Steps:**
1. input: `s_analytic_family_of_compact_operators_K(z)` --[t_auxiliary_construction {object: analytic_resolvent_R(z)=(I-K(z))^{-1}_where_defined}]--> output: `s_meromorphic_resolvent`
2. input: `s_meromorphic_resolvent` --[t_compose_with_identity {tool: Fredholm_alternative_pointwise}]--> output: `s_local_invertibility_or_finite_kernel`
3. input: `s_local_invertibility_or_finite_kernel` --[t_reduce_to_canonical_form {form: either_singular_everywhere_or_meromorphic_with_discrete_pole_set}]--> output: `s_analytic_fredholm`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_reduce_to_canonical_form

---

### Cotlar–Stein lemma (cite: https://en.wikipedia.org/wiki/Cotlar%E2%80%93Stein_lemma)

**Axioms:** `s_almost_orthogonal_family_of_operators_T_j`, `s_l1_summable_correlation_estimates`
**Terminal:** `s_cotlar_stein` (kind: theorem)

**Steps:**
1. input: `s_almost_orthogonal_family_of_operators_T_j` --[t_auxiliary_construction {object: high_power_(ΣT_j)^{2n}_expanded_as_sum_of_2n_fold_products}]--> output: `s_expanded_2n_th_power`
2. input: `s_expanded_2n_th_power` --[t_exhaustion_squeeze {bound: each_term_bounded_by_√(‖T_iT_j*‖·‖T_j T_k*‖)_recursively}]--> output: `s_chain_correlation_bound`
3. input: `s_chain_correlation_bound` --[t_interpolate_and_continue {limit: n→∞_extract_‖ΣT_j‖≤Σ_j √sup_k ‖T_j*T_k‖^{1/2}}]--> output: `s_cotlar_stein`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_interpolate_and_continue

---

### T(1) theorem (David–Journé) (cite: https://en.wikipedia.org/wiki/T(1)_theorem)

**Axioms:** `s_singular_integral_operator_T_with_CZ_kernel`, `s_BMO_test_T(1)_and_T*(1)`
**Terminal:** `s_t1_theorem` (kind: theorem)

**Steps:**
1. input: `s_singular_integral_operator_T_with_CZ_kernel` --[t_auxiliary_construction {object: paraproducts_π_b_subtracting_T(1)_and_T*(1)_components}]--> output: `s_paraproduct_corrected_operator_T_0`
2. input: `s_paraproduct_corrected_operator_T_0` --[t_frequency_decomposition {tool: Littlewood_Paley_decomposition_of_T_0}]--> output: `s_almost_orthogonal_pieces_T_jk`
3. input: `s_almost_orthogonal_pieces_T_jk` --[t_compose_with_identity {tool: Cotlar_Stein_on_T_jk}]--> output: `s_L²_boundedness_of_T_0`
4. input: `s_L²_boundedness_of_T_0` --[t_reduce_to_canonical_form {form: T_bounded_on_L²_iff_T(1),T*(1)∈BMO_and_weak_boundedness}]--> output: `s_t1_theorem`

**Techniques used:** t_auxiliary_construction, t_frequency_decomposition, t_compose_with_identity, t_reduce_to_canonical_form

---

### Hörmander's pseudodifferential symbol class theorem (cite: https://en.wikipedia.org/wiki/Pseudo-differential_operator)

**Axioms:** `s_symbol_a_in_S^m_rho_delta`, `s_oscillatory_integral_definition`
**Terminal:** `s_hormander_symbol_class` (kind: theorem)

**Steps:**
1. input: `s_symbol_a_in_S^m_rho_delta` --[t_auxiliary_construction {object: pseudodifferential_op_a(x,D)f=(2π)^{-n}∫e^{ix·ξ}a(x,ξ)f̂(ξ)dξ}]--> output: `s_pseudodifferential_operator_a(x,D)`
2. input: `s_pseudodifferential_operator_a(x,D)` --[t_frequency_decomposition {tool: dyadic_decomposition_in_ξ_and_oscillatory_integral_stationary_phase}]--> output: `s_dyadic_oscillatory_pieces`
3. input: `s_dyadic_oscillatory_pieces` --[t_compose_with_identity {tool: composition_law_a#b=Σ(-i)^α/α!·∂_ξ^α a·∂_x^α b}]--> output: `s_symbol_calculus_modulo_lower_order`
4. input: `s_symbol_calculus_modulo_lower_order` --[t_reduce_to_canonical_form {form: ΨDO_calculus_with_principal_symbol_and_index}]--> output: `s_hormander_symbol_class`

**Techniques used:** t_auxiliary_construction, t_frequency_decomposition, t_compose_with_identity, t_reduce_to_canonical_form

---

### Hörmander L² ∂̄ estimates (cite: https://en.wikipedia.org/wiki/H%C3%B6rmander%27s_condition)

**Axioms:** `s_pseudoconvex_domain_in_Cn`, `s_∂̄_closed_(0,1)_form_with_L²_weight`
**Terminal:** `s_hormander_l2_dbar` (kind: theorem)

**Steps:**
1. input: `s_∂̄_closed_(0,1)_form_with_L²_weight` --[t_auxiliary_construction {object: weighted_L²_space_with_plurisubharmonic_weight_φ}]--> output: `s_weighted_hilbert_space_L²(e^{-φ})`
2. input: `s_weighted_hilbert_space_L²(e^{-φ})` --[t_duality {pairing: ⟨∂̄u,v⟩_φ=⟨u,∂̄*v⟩_φ_with_Bochner_Kodaira_identity}]--> output: `s_bochner_kodaira_morrey_identity`
3. input: `s_bochner_kodaira_morrey_identity` --[t_projection_to_subspace {target: range(∂̄)_closed_via_a_priori_estimate}]--> output: `s_a_priori_estimate_‖u‖²≤(1/c)⟨∂̄*∂̄ u,u⟩`
4. input: `s_a_priori_estimate_‖u‖²≤(1/c)⟨∂̄*∂̄ u,u⟩` --[t_reduce_to_canonical_form {form: solve_∂̄u=f_with_‖u‖²_φ≤∫|f|²/c_dλ}]--> output: `s_hormander_l2_dbar`

**Techniques used:** t_auxiliary_construction, t_duality, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Garding's inequality (cite: https://en.wikipedia.org/wiki/G%C3%A5rding%27s_inequality)

**Axioms:** `s_strongly_elliptic_form_a(u,v)`, `s_sobolev_space_H^k(Ω)`
**Terminal:** `s_garding_inequality` (kind: theorem)

**Steps:**
1. input: `s_strongly_elliptic_form_a(u,v)` --[t_fourier_transform {target: principal_symbol_positive_definite_at_each_point}]--> output: `s_pointwise_positivity_of_symbol`
2. input: `s_pointwise_positivity_of_symbol` --[t_auxiliary_construction {object: partition_of_unity_localizing_to_freeze_coefficients}]--> output: `s_local_constant_coefficient_pieces`
3. input: `s_local_constant_coefficient_pieces` --[t_exhaustion_squeeze {bound: Plancherel_+_symbol_lower_bound_⇒_a(u,u)≥c‖u‖²_{H^k}-C‖u‖²_{L²}}]--> output: `s_garding_inequality`

**Techniques used:** t_fourier_transform, t_auxiliary_construction, t_exhaustion_squeeze

---

### Aubin–Lions lemma (cite: https://en.wikipedia.org/wiki/Aubin%E2%80%93Lions_lemma)

**Axioms:** `s_triple_of_banach_spaces_X⊂⊂B⊂Y`, `s_bounded_set_in_Lp(0,T;X)_with_derivative_in_Lq(0,T;Y)`
**Terminal:** `s_aubin_lions` (kind: theorem)

**Steps:**
1. input: `s_bounded_set_in_Lp(0,T;X)_with_derivative_in_Lq(0,T;Y)` --[t_auxiliary_construction {object: Ehrling_lemma_‖u‖_B≤ε‖u‖_X+C(ε)‖u‖_Y}]--> output: `s_ehrling_interpolation_inequality`
2. input: `s_ehrling_interpolation_inequality` --[t_compactness_argument {tool: time_shift_continuity_in_Y_+_compact_embedding_X↪↪B}]--> output: `s_equicontinuity_in_time_in_B`
3. input: `s_equicontinuity_in_time_in_B` --[t_compose_with_identity {tool: Frechet_Kolmogorov_in_L^p(0,T;B)}]--> output: `s_aubin_lions`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_compose_with_identity

---

### Meyers–Serrin theorem (H = W) (cite: https://en.wikipedia.org/wiki/Meyers%E2%80%93Serrin_theorem)

**Axioms:** `s_sobolev_space_W^{m,p}(Ω)`, `s_smooth_function_in_W^{m,p}`
**Terminal:** `s_meyers_serrin` (kind: theorem)

**Steps:**
1. input: `s_sobolev_space_W^{m,p}(Ω)` --[t_auxiliary_construction {object: covering_of_Ω_by_open_sets_Ω_k_with_partition_of_unity}]--> output: `s_locally_finite_cover_with_pou`
2. input: `s_locally_finite_cover_with_pou` --[t_compose_with_identity {tool: mollify_each_localized_piece_with_ε_k_sufficiently_small}]--> output: `s_local_mollification_summed`
3. input: `s_local_mollification_summed` --[t_exhaustion_squeeze {limit: ‖u-Σ φ_k(η_{ε_k}*u)‖_{W^{m,p}}<ε}]--> output: `s_meyers_serrin`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_exhaustion_squeeze

---

### Mazur–Ulam theorem (cite: https://en.wikipedia.org/wiki/Mazur%E2%80%93Ulam_theorem)

**Axioms:** `s_real_normed_spaces`, `s_surjective_isometry_f:X→Y`
**Terminal:** `s_mazur_ulam` (kind: theorem)

**Steps:**
1. input: `s_surjective_isometry_f:X→Y` --[t_auxiliary_construction {object: midpoint_set_M(x,y)={z:‖z-x‖=‖z-y‖=‖x-y‖/2}}]--> output: `s_midpoint_set_characterization`
2. input: `s_midpoint_set_characterization` --[t_symmetry_reduction {symmetry: reflection_z↦2((x+y)/2)-z_preserves_M(x,y)}]--> output: `s_midpoint_preserved_under_reflection`
3. input: `s_midpoint_preserved_under_reflection` --[t_reduce_to_canonical_form {form: f(midpoint)=midpoint(f(x),f(y))_⇒_affine_linearity}]--> output: `s_mazur_ulam`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_reduce_to_canonical_form

---

### Kirszbraun theorem (Lipschitz extension) (cite: https://en.wikipedia.org/wiki/Kirszbraun_theorem)

**Axioms:** `s_subset_S_of_hilbert_space`, `s_lipschitz_map_f:S→hilbert`
**Terminal:** `s_kirszbraun_theorem` (kind: theorem)

**Steps:**
1. input: `s_lipschitz_map_f:S→hilbert` --[t_auxiliary_construction {object: intersection_of_balls_B(f(s),L·d(x,s))_for_s∈S}]--> output: `s_intersection_of_balls_at_each_x`
2. input: `s_intersection_of_balls_at_each_x` --[t_compactness_argument {tool: Helly_in_hilbert_=_finite_intersection_property_via_finite_dim_Helly}]--> output: `s_nonempty_intersection_for_each_x`
3. input: `s_nonempty_intersection_for_each_x` --[t_compose_with_identity {tool: Zorn_+_consistent_choice_extends_to_full_domain}]--> output: `s_kirszbraun_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_compose_with_identity

---

### Michael selection theorem (cite: https://en.wikipedia.org/wiki/Michael_selection_theorem)

**Axioms:** `s_paracompact_space`, `s_lower_semicontinuous_correspondence_with_convex_values_in_banach`
**Terminal:** `s_michael_selection` (kind: theorem)

**Steps:**
1. input: `s_lower_semicontinuous_correspondence_with_convex_values_in_banach` --[t_auxiliary_construction {object: locally_finite_partition_of_unity_+_finite_dim_selections_on_simplices}]--> output: `s_ε_approximate_selection`
2. input: `s_ε_approximate_selection` --[t_compactness_argument {tool: iterate_ε_n→0_with_geometric_convergence}]--> output: `s_cauchy_sequence_of_approximate_selections`
3. input: `s_cauchy_sequence_of_approximate_selections` --[t_interpolate_and_continue {limit: completeness_+_lsc_yields_continuous_selection}]--> output: `s_michael_selection`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_interpolate_and_continue

---

### Dvoretzky's theorem (cite: https://en.wikipedia.org/wiki/Dvoretzky%27s_theorem)

**Axioms:** `s_infinite_dim_banach_space`, `s_concentration_of_measure_on_sphere`
**Terminal:** `s_dvoretzky_theorem` (kind: theorem)

**Steps:**
1. input: `s_infinite_dim_banach_space` --[t_auxiliary_construction {object: Dvoretzky_Rogers_basis_+_random_subspace_of_dim_k(ε,n)}]--> output: `s_random_high_dim_subspace_selection`
2. input: `s_random_high_dim_subspace_selection` --[t_probabilistic_existence {tool: Lévy_concentration_of_Lipschitz_function_on_S^{n-1}}]--> output: `s_concentration_of_norm_on_sphere`
3. input: `s_concentration_of_norm_on_sphere` --[t_compactness_argument {tool: ε_net_+_union_bound}]--> output: `s_almost_euclidean_section_existence`
4. input: `s_almost_euclidean_section_existence` --[t_reduce_to_canonical_form {form: ∀ε∃k=k(ε)_subspace_(1+ε)_close_to_l²_k}]--> output: `s_dvoretzky_theorem`

**Techniques used:** t_auxiliary_construction, t_probabilistic_existence, t_compactness_argument, t_reduce_to_canonical_form

---

### Grothendieck inequality (cite: https://en.wikipedia.org/wiki/Grothendieck_inequality)

**Axioms:** `s_real_matrix_A_with_|Σa_ij s_i t_j|≤1_for_signs`, `s_unit_vectors_x_i_y_j_in_hilbert`
**Terminal:** `s_grothendieck_inequality` (kind: theorem)

**Steps:**
1. input: `s_real_matrix_A_with_|Σa_ij s_i t_j|≤1_for_signs` --[t_auxiliary_construction {object: Gaussian_rounding_x↦sign(⟨g,x⟩)_for_random_g}]--> output: `s_gaussian_rounding_estimator`
2. input: `s_gaussian_rounding_estimator` --[t_probabilistic_existence {tool: E[sign(⟨g,x⟩)sign(⟨g,y⟩)]=(2/π)arcsin(⟨x,y⟩)}]--> output: `s_arcsin_kernel_relation`
3. input: `s_arcsin_kernel_relation` --[t_exhaustion_squeeze {bound: |Σa_ij⟨x_i,y_j⟩|≤K_G·sup_signs}]--> output: `s_grothendieck_inequality`

**Techniques used:** t_auxiliary_construction, t_probabilistic_existence, t_exhaustion_squeeze

---

### Connes embedding problem / theorem statement (cite: https://en.wikipedia.org/wiki/Connes_embedding_problem)

**Axioms:** `s_separable_II_1_factor_M`, `s_ultrapower_of_hyperfinite_R_omega`
**Terminal:** `s_connes_embedding_statement` (kind: theorem)

**Steps:**
1. input: `s_separable_II_1_factor_M` --[t_ultraproduct_transfer {transfer: tracial_ultrapower_R^ω_of_hyperfinite_II_1}]--> output: `s_tracial_ultrapower_target`
2. input: `s_tracial_ultrapower_target` --[t_auxiliary_construction {object: microstate_approximations_of_matrix_relations}]--> output: `s_finite_dim_matricial_microstates`
3. input: `s_finite_dim_matricial_microstates` --[t_reduce_to_canonical_form {form: M↪R^ω_iff_microstates_exist_for_all_relations}]--> output: `s_connes_embedding_statement`

**Techniques used:** t_ultraproduct_transfer, t_auxiliary_construction, t_reduce_to_canonical_form

---

### Bessel's inequality (cite: https://en.wikipedia.org/wiki/Bessel%27s_inequality)

**Axioms:** `s_hilbert_space`, `s_orthonormal_sequence_e_n`
**Terminal:** `s_bessel_inequality` (kind: theorem)

**Steps:**
1. input: `s_orthonormal_sequence_e_n` --[t_projection_to_subspace {target: P_N x=Σ_{n=1}^N ⟨x,e_n⟩e_n}]--> output: `s_partial_orthogonal_projection`
2. input: `s_partial_orthogonal_projection` --[t_exhaustion_squeeze {identity: ‖x‖²=‖P_N x‖²+‖x-P_N x‖²≥Σ_{n=1}^N |⟨x,e_n⟩|²}]--> output: `s_bessel_inequality`

**Techniques used:** t_projection_to_subspace, t_exhaustion_squeeze

---

### Parseval's identity (cite: https://en.wikipedia.org/wiki/Parseval%27s_identity)

**Axioms:** `s_hilbert_space`, `s_complete_orthonormal_basis_e_n`
**Terminal:** `s_parseval_identity` (kind: theorem)

**Steps:**
1. input: `s_complete_orthonormal_basis_e_n` --[t_compose_with_identity {tool: Bessel_inequality_extends_to_equality_when_basis_complete}]--> output: `s_bessel_becomes_equality_for_complete_basis`
2. input: `s_bessel_becomes_equality_for_complete_basis` --[t_reduce_to_canonical_form {form: ‖x‖²=Σ|⟨x,e_n⟩|²}]--> output: `s_parseval_identity`

**Techniques used:** t_compose_with_identity, t_reduce_to_canonical_form

---

### Hölder's inequality (cite: https://en.wikipedia.org/wiki/H%C3%B6lder%27s_inequality)

**Axioms:** `s_measure_space`, `s_conjugate_exponent_pair_1/p+1/q=1`
**Terminal:** `s_holder_inequality` (kind: theorem)

**Steps:**
1. input: `s_conjugate_exponent_pair_1/p+1/q=1` --[t_auxiliary_construction {object: Young_inequality_ab≤a^p/p+b^q/q_via_concavity_of_log}]--> output: `s_young_pointwise_inequality`
2. input: `s_young_pointwise_inequality` --[t_exhaustion_squeeze {integration: pointwise_normalize_|f|/‖f‖_p,|g|/‖g‖_q_and_integrate}]--> output: `s_holder_inequality`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze

---

### Propagation of singularities theorem (cite: https://en.wikipedia.org/wiki/Propagation_of_singularities_theorem)

**Axioms:** `s_pseudodifferential_operator_P_real_principal_symbol`, `s_wavefront_set_WF(u)`
**Terminal:** `s_propagation_of_singularities` (kind: theorem)

**Steps:**
1. input: `s_pseudodifferential_operator_P_real_principal_symbol` --[t_auxiliary_construction {object: bicharacteristic_flow_of_Hamiltonian_H_p_on_T*M}]--> output: `s_hamiltonian_flow_bicharacteristics`
2. input: `s_hamiltonian_flow_bicharacteristics` --[t_frequency_decomposition {tool: microlocal_cutoffs_along_bicharacteristic_strip}]--> output: `s_microlocal_propagation_estimate`
3. input: `s_microlocal_propagation_estimate` --[t_compose_with_identity {tool: positive_commutator_a(x,D)P-Pa(x,D)_lower_bound}]--> output: `s_commutator_inequality_yields_regularity_transport`
4. input: `s_commutator_inequality_yields_regularity_transport` --[t_reduce_to_canonical_form {form: WF(u)\WF(Pu)_invariant_under_bicharacteristic_flow}]--> output: `s_propagation_of_singularities`

**Techniques used:** t_auxiliary_construction, t_frequency_decomposition, t_compose_with_identity, t_reduce_to_canonical_form

---

### Open mapping theorem (Fréchet space version) (cite: https://en.wikipedia.org/wiki/Open_mapping_theorem_(functional_analysis))

**Axioms:** `s_pair_of_frechet_spaces`, `s_continuous_surjective_linear_map_T`
**Terminal:** `s_open_mapping_frechet` (kind: theorem)

**Steps:**
1. input: `s_continuous_surjective_linear_map_T` --[t_auxiliary_construction {object: countable_neighborhood_basis_of_zero_in_both_spaces}]--> output: `s_translation_invariant_metric_setup`
2. input: `s_translation_invariant_metric_setup` --[t_compactness_argument {tool: Baire_category_in_Fréchet_completeness}]--> output: `s_T(U)_dense_in_some_neighborhood`
3. input: `s_T(U)_dense_in_some_neighborhood` --[t_contraction_fixed_point {scheme: iterative_correction_with_geometric_step_in_metric}]--> output: `s_T(U)_contains_neighborhood`
4. input: `s_T(U)_contains_neighborhood` --[t_reduce_to_canonical_form {form: T_open}]--> output: `s_open_mapping_frechet`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_contraction_fixed_point, t_reduce_to_canonical_form

---

### Wold decomposition (cite: https://en.wikipedia.org/wiki/Wold%27s_decomposition)

**Axioms:** `s_hilbert_space_with_isometry_V`, `s_wandering_subspace_L=H⊖VH`
**Terminal:** `s_wold_decomposition` (kind: theorem)

**Steps:**
1. input: `s_hilbert_space_with_isometry_V` --[t_auxiliary_construction {object: decreasing_chain_V^n H_and_intersection_H_u=∩V^n H}]--> output: `s_unitary_part_H_u`
2. input: `s_unitary_part_H_u` --[t_projection_to_subspace {target: orthogonal_complement_H_s=⊕_{n≥0}V^n L}]--> output: `s_shift_part_H_s_as_orthogonal_sum`
3. input: `s_shift_part_H_s_as_orthogonal_sum` --[t_reduce_to_canonical_form {form: V=V_u⊕shift_on_l²(L)_canonical_decomposition}]--> output: `s_wold_decomposition`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Commutant lifting theorem (cite: https://en.wikipedia.org/wiki/Commutant_lifting_theorem)

**Axioms:** `s_contraction_T_with_isometric_dilation_V`, `s_intertwining_operator_X_commuting_with_T`
**Terminal:** `s_commutant_lifting` (kind: theorem)

**Steps:**
1. input: `s_intertwining_operator_X_commuting_with_T` --[t_auxiliary_construction {object: Sz_Nagy_minimal_isometric_dilation_K_⊃_H}]--> output: `s_minimal_isometric_dilation_space`
2. input: `s_minimal_isometric_dilation_space` --[t_raise_dimension {target: extension_Y:K→K_commuting_with_V_with_‖Y‖=‖X‖}]--> output: `s_norm_preserving_extension_problem`
3. input: `s_norm_preserving_extension_problem` --[t_compose_with_identity {tool: Hahn_Banach_type_extension_via_Parrott_completion}]--> output: `s_parrott_completion_yields_Y`
4. input: `s_norm_preserving_extension_problem` --[t_reduce_to_canonical_form {form: ‖Y‖=‖X‖_with_P_H Y=XP_H_on_dilation}]--> output: `s_commutant_lifting`

**Techniques used:** t_auxiliary_construction, t_raise_dimension, t_compose_with_identity, t_reduce_to_canonical_form

---

### Russo–Dye theorem (cite: https://en.wikipedia.org/wiki/Russo%E2%80%93Dye_theorem)

**Axioms:** `s_unital_c_star_algebra`, `s_convex_hull_of_unitaries`
**Terminal:** `s_russo_dye` (kind: theorem)

**Steps:**
1. input: `s_unital_c_star_algebra` --[t_auxiliary_construction {object: element_x_with_‖x‖<1_written_as_(u+v)/2_with_u,v_unitary}]--> output: `s_two_unitary_decomposition_of_strict_contraction`
2. input: `s_two_unitary_decomposition_of_strict_contraction` --[t_compose_with_identity {tool: continuous_functional_calculus_to_build_u=x+i√(1-x*x),v=x-i√(1-x*x)}]--> output: `s_explicit_unitary_pair`
3. input: `s_explicit_unitary_pair` --[t_reduce_to_canonical_form {form: closed_unit_ball_=_closed_convex_hull_of_unitaries}]--> output: `s_russo_dye`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_reduce_to_canonical_form

---

### Crossed product construction (von Neumann) (cite: https://en.wikipedia.org/wiki/Crossed_product)

**Axioms:** `s_von_neumann_algebra_M_with_group_action_α:G↷M`, `s_l2_G_with_M_valued_functions`
**Terminal:** `s_crossed_product_construction` (kind: theorem)

**Steps:**
1. input: `s_von_neumann_algebra_M_with_group_action_α:G↷M` --[t_auxiliary_construction {object: Hilbert_space_L²(G,H)_with_left_regular_representation}]--> output: `s_extended_hilbert_space_L²(G,H)`
2. input: `s_extended_hilbert_space_L²(G,H)` --[t_compose_with_identity {tool: covariant_pair_(π,λ)_with_π(α_g(a))=λ_g π(a) λ_g*}]--> output: `s_covariant_representation`
3. input: `s_covariant_representation` --[t_reduce_to_canonical_form {form: M⋊_α G_=_von_Neumann_algebra_generated_by_π(M),λ(G)}]--> output: `s_crossed_product_construction`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_reduce_to_canonical_form

---

### Continuous functional calculus (cite: https://en.wikipedia.org/wiki/Continuous_functional_calculus)

**Axioms:** `s_normal_element_a_in_c_star_algebra`, `s_compact_spectrum_σ(a)`
**Terminal:** `s_continuous_functional_calculus` (kind: theorem)

**Steps:**
1. input: `s_normal_element_a_in_c_star_algebra` --[t_auxiliary_construction {object: polynomial_calculus_p,q↦p(a,a*)}]--> output: `s_polynomial_star_calculus`
2. input: `s_polynomial_star_calculus` --[t_compose_with_identity {tool: spectral_radius_=_norm_for_normal_⇒_‖p(a,a*)‖=‖p‖_{C(σ(a))}}]--> output: `s_isometry_to_polynomials_on_spectrum`
3. input: `s_isometry_to_polynomials_on_spectrum` --[t_interpolate_and_continue {limit: Stone_Weierstrass_extends_to_C(σ(a))}]--> output: `s_continuous_functional_calculus`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_interpolate_and_continue

---

### Borel functional calculus (cite: https://en.wikipedia.org/wiki/Borel_functional_calculus)

**Axioms:** `s_normal_operator_on_hilbert`, `s_continuous_functional_calculus`
**Terminal:** `s_borel_functional_calculus` (kind: theorem)

**Steps:**
1. input: `s_continuous_functional_calculus` --[t_duality {pairing: vector_pair_(x,y)↦measure_μ_xy_via_Riesz_Markov}]--> output: `s_spectral_measure_per_vector_pair`
2. input: `s_spectral_measure_per_vector_pair` --[t_compose_with_identity {tool: extend_∫f_dμ_xy_to_bounded_Borel_f}]--> output: `s_borel_functional_calculus_per_pair`
3. input: `s_borel_functional_calculus_per_pair` --[t_reduce_to_canonical_form {form: f↦f(N)_with_f(N)_=_∫f_dE_spectral_measure}]--> output: `s_borel_functional_calculus`

**Techniques used:** t_duality, t_compose_with_identity, t_reduce_to_canonical_form

---

### Direct integral decomposition (von Neumann) (cite: https://en.wikipedia.org/wiki/Direct_integral)

**Axioms:** `s_separable_hilbert_space`, `s_abelian_von_neumann_subalgebra_A`
**Terminal:** `s_direct_integral_decomposition` (kind: theorem)

**Steps:**
1. input: `s_abelian_von_neumann_subalgebra_A` --[t_compose_with_identity {tool: spectral_theorem_⇒_A≅L^∞(X,μ)}]--> output: `s_a_acts_as_multiplication_on_measure_space_X`
2. input: `s_a_acts_as_multiplication_on_measure_space_X` --[t_auxiliary_construction {object: measurable_field_of_hilbert_spaces_x↦H_x}]--> output: `s_measurable_hilbert_field`
3. input: `s_measurable_hilbert_field` --[t_projection_to_subspace {target: H≅∫^⊕_X H_x dμ(x)_with_A_acting_pointwise}]--> output: `s_direct_integral_isomorphism`
4. input: `s_direct_integral_isomorphism` --[t_reduce_to_canonical_form {form: M=∫^⊕ M_x dμ_for_decomposable_T's}]--> output: `s_direct_integral_decomposition`

**Techniques used:** t_compose_with_identity, t_auxiliary_construction, t_projection_to_subspace, t_reduce_to_canonical_form

---

### Banach–Mazur theorem (separable Banach spaces embed in C[0,1]) (cite: https://en.wikipedia.org/wiki/Banach%E2%80%93Mazur_theorem)

**Axioms:** `s_separable_banach_space_X`, `s_unit_ball_of_X_star`
**Terminal:** `s_banach_mazur_embedding` (kind: theorem)

**Steps:**
1. input: `s_unit_ball_of_X_star` --[t_compactness_argument {tool: Banach_Alaoglu_+_weak_star_metrizability_of_separable_dual_ball}]--> output: `s_compact_metrizable_dual_unit_ball_K`
2. input: `s_compact_metrizable_dual_unit_ball_K` --[t_auxiliary_construction {object: evaluation_map_J:X→C(K),Jx(φ)=φ(x)}]--> output: `s_isometric_embedding_J_into_C(K)`
3. input: `s_isometric_embedding_J_into_C(K)` --[t_compose_with_identity {tool: K_homeomorphic_to_subset_of_[0,1]_⇒_C(K)↪C[0,1]_via_extension}]--> output: `s_banach_mazur_embedding`

**Techniques used:** t_compactness_argument, t_auxiliary_construction, t_compose_with_identity

---

### Plancherel for non-abelian compact groups (cite: https://en.wikipedia.org/wiki/Plancherel_theorem_for_spherical_functions)

**Axioms:** `s_compact_lie_group_G`, `s_peter_weyl`
**Terminal:** `s_plancherel_nonabelian` (kind: theorem)

**Steps:**
1. input: `s_compact_lie_group_G` --[t_compose_with_identity {tool: Peter_Weyl_yields_L²(G)=⊕_π dim(π)·H_π⊗H_π*}]--> output: `s_peter_weyl_decomposition`
2. input: `s_peter_weyl_decomposition` --[t_character_decomposition_count {invariant: matrix_coefficient_basis_indexed_by_(π,i,j)}]--> output: `s_matrix_coefficient_orthogonality`
3. input: `s_matrix_coefficient_orthogonality` --[t_fourier_transform {target: f↦{π↦∫_G f(g)π(g)*dg}}]--> output: `s_operator_valued_fourier_transform`
4. input: `s_operator_valued_fourier_transform` --[t_reduce_to_canonical_form {form: ‖f‖²_2=Σ_π dim(π)·‖f̂(π)‖²_HS}]--> output: `s_plancherel_nonabelian`

**Techniques used:** t_compose_with_identity, t_character_decomposition_count, t_fourier_transform, t_reduce_to_canonical_form

---

### Pontryagin duality (cite: https://en.wikipedia.org/wiki/Pontryagin_duality)

**Axioms:** `s_locally_compact_abelian_group_G`, `s_character_group_Ĝ`
**Terminal:** `s_pontryagin_duality` (kind: theorem)

**Steps:**
1. input: `s_locally_compact_abelian_group_G` --[t_auxiliary_construction {object: character_group_Ĝ=Hom_cont(G,T)_with_compact_open_topology}]--> output: `s_lca_character_group_Ĝ`
2. input: `s_lca_character_group_Ĝ` --[t_duality {pairing: canonical_eval_G→Ĝ̂}]--> output: `s_canonical_double_dual_map`
3. input: `s_canonical_double_dual_map` --[t_fourier_transform {tool: Plancherel_+_Fourier_inversion_on_LCA}]--> output: `s_fourier_isometry_L²(G)↔L²(Ĝ)`
4. input: `s_fourier_isometry_L²(G)↔L²(Ĝ)` --[t_analysis_algebra_topology_bridge {duality: contravariant_equivalence_LCAGrp↔LCAGrp_via_(̂)}]--> output: `s_pontryagin_duality`

**Techniques used:** t_auxiliary_construction, t_duality, t_fourier_transform, t_analysis_algebra_topology_bridge

---

### Aubert–Choi continuity / Choi–Effros lifting theorem (cite: https://en.wikipedia.org/wiki/Choi%E2%80%93Effros_lifting_theorem)

**Axioms:** `s_nuclear_separable_c_star_algebra`, `s_quotient_*-homomorphism_π:B→B/J`
**Terminal:** `s_choi_effros_lifting` (kind: theorem)

**Steps:**
1. input: `s_nuclear_separable_c_star_algebra` --[t_auxiliary_construction {object: completely_positive_approximations_A↦M_n↦A}]--> output: `s_cp_approximation_diagrams`
2. input: `s_cp_approximation_diagrams` --[t_compose_with_identity {tool: Arveson_extension_for_each_M_n_diagram_to_B}]--> output: `s_diagram_lifted_into_B`
3. input: `s_diagram_lifted_into_B` --[t_compactness_argument {tool: point_weak_compactness_+_diagonal_subsequence}]--> output: `s_coherent_lift_of_CP_diagrams`
4. input: `s_coherent_lift_of_CP_diagrams` --[t_reduce_to_canonical_form {form: CP_lifting_φ̃:A→B_with_π∘φ̃=id_A_section}]--> output: `s_choi_effros_lifting`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_compactness_argument, t_reduce_to_canonical_form

---

### Glimm's dichotomy / type I vs non-type-I (cite: https://en.wikipedia.org/wiki/Type_I_C*-algebra)

**Axioms:** `s_separable_c_star_algebra`, `s_irreducible_representation_class`
**Terminal:** `s_glimm_dichotomy` (kind: theorem)

**Steps:**
1. input: `s_separable_c_star_algebra` --[t_auxiliary_construction {object: dual_object_Â_=_set_of_irreducible_reps_modulo_unitary_equivalence}]--> output: `s_dual_object_Â`
2. input: `s_dual_object_Â` --[t_spot_pattern_in_table {features: Â_T_0_with_smooth_Borel_structure_⇔_type_I}]--> output: `s_pattern_T_0_dual_indicates_type_I`
3. input: `s_pattern_T_0_dual_indicates_type_I` --[t_reductio_ad_absurdum {non_type_I: produce_uncountable_family_of_inequivalent_reps_via_UHF_embedding}]--> output: `s_non_type_I_dichotomy_witness`
4. input: `s_non_type_I_dichotomy_witness` --[t_reduce_to_canonical_form {form: either_type_I_with_smooth_dual_or_contains_UHF_with_continuum_classes}]--> output: `s_glimm_dichotomy`

**Techniques used:** t_auxiliary_construction, t_spot_pattern_in_table, t_reductio_ad_absurdum, t_reduce_to_canonical_form

---

### Connes' noncommutative index formula (cite: https://en.wikipedia.org/wiki/Noncommutative_geometry#Index_theory)

**Axioms:** `s_spectral_triple_(A,H,D)`, `s_chern_connes_pairing`
**Terminal:** `s_connes_noncommutative_index` (kind: theorem)

**Steps:**
1. input: `s_spectral_triple_(A,H,D)` --[t_auxiliary_construction {object: K_homology_class_[D]∈KK(A,C)_from_Fredholm_module}]--> output: `s_k_homology_class_of_D`
2. input: `s_k_homology_class_of_D` --[t_k_theoretic_index_bridge {pairing: K_0(A)×KK(A,C)→Z_via_index}]--> output: `s_pairing_with_K_theory_of_A`
3. input: `s_pairing_with_K_theory_of_A` --[t_compose_with_identity {tool: Chern_Connes_character_to_cyclic_cohomology}]--> output: `s_chern_connes_character_in_periodic_cyclic`
4. input: `s_chern_connes_character_in_periodic_cyclic` --[t_reduce_to_canonical_form {form: index(D_e)=⟨[e],ch_*(D)⟩_local_formula}]--> output: `s_connes_noncommutative_index`

**Techniques used:** t_auxiliary_construction, t_k_theoretic_index_bridge, t_compose_with_identity, t_reduce_to_canonical_form

---

### Pettis theorem (weakly measurable = strongly measurable for separable values) (cite: https://en.wikipedia.org/wiki/Pettis%27_theorem)

**Axioms:** `s_banach_valued_function_f:Ω→X`, `s_separable_range_a.e.`
**Terminal:** `s_pettis_measurability` (kind: theorem)

**Steps:**
1. input: `s_separable_range_a.e.` --[t_auxiliary_construction {object: countable_dense_subset_+_simple_function_approximation}]--> output: `s_simple_function_approximant_pointwise`
2. input: `s_simple_function_approximant_pointwise` --[t_duality {pairing: weak_measurability_via_X*_separating_points}]--> output: `s_borel_measurability_in_weak_topology`
3. input: `s_borel_measurability_in_weak_topology` --[t_reduce_to_canonical_form {form: f_=_a.e._limit_of_simple_functions_⇒_strongly_measurable}]--> output: `s_pettis_measurability`

**Techniques used:** t_auxiliary_construction, t_duality, t_reduce_to_canonical_form

---

### Eidelheit separation theorem (cite: https://en.wikipedia.org/wiki/Hyperplane_separation_theorem)

**Axioms:** `s_convex_set_with_nonempty_interior_in_topological_vector_space`, `s_disjoint_convex_set`
**Terminal:** `s_eidelheit_separation` (kind: theorem)

**Steps:**
1. input: `s_convex_set_with_nonempty_interior_in_topological_vector_space` --[t_auxiliary_construction {object: Minkowski_functional_of_int(A)-B+x_0}]--> output: `s_minkowski_gauge_continuous`
2. input: `s_minkowski_gauge_continuous` --[t_compose_with_identity {tool: Hahn_Banach_dominated_by_continuous_gauge_⇒_continuous_extension}]--> output: `s_continuous_separating_functional`
3. input: `s_continuous_separating_functional` --[t_reduce_to_canonical_form {form: closed_hyperplane_separates_A_from_B}]--> output: `s_eidelheit_separation`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_reduce_to_canonical_form

---

### Nash–Moser implicit function theorem (cite: https://en.wikipedia.org/wiki/Nash%E2%80%93Moser_theorem)

**Axioms:** `s_tame_frechet_space_pair`, `s_smoothing_operators_S_t`
**Terminal:** `s_nash_moser` (kind: theorem)

**Steps:**
1. input: `s_tame_frechet_space_pair` --[t_auxiliary_construction {object: smoothing_operators_S_t_with_loss_estimates}]--> output: `s_smoothing_family_S_t`
2. input: `s_smoothing_family_S_t` --[t_contraction_fixed_point {scheme: Newton_iteration_x_{n+1}=x_n-DF(x_n)^{-1}F(x_n)_with_S_t_n}]--> output: `s_modified_newton_iteration`
3. input: `s_modified_newton_iteration` --[t_exhaustion_squeeze {bound: quadratic_convergence_compensates_derivative_loss_via_tame_estimates}]--> output: `s_convergent_quadratic_iteration`
4. input: `s_convergent_quadratic_iteration` --[t_reduce_to_canonical_form {form: smooth_inverse_function_in_tame_category}]--> output: `s_nash_moser`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze, t_reduce_to_canonical_form

---

### Weak formulation of elliptic BVP / Lax–Milgram applied (cite: https://en.wikipedia.org/wiki/Weak_formulation)

**Axioms:** `s_second_order_elliptic_pde_Lu=f_with_Dirichlet`, `s_sobolev_space_H1_0`
**Terminal:** `s_weak_formulation_elliptic` (kind: theorem)

**Steps:**
1. input: `s_second_order_elliptic_pde_Lu=f_with_Dirichlet` --[t_duality {pairing: multiply_by_test_v_and_integrate_by_parts}]--> output: `s_bilinear_form_a(u,v)=⟨f,v⟩`
2. input: `s_bilinear_form_a(u,v)=⟨f,v⟩` --[t_compose_with_identity {tool: Garding_+_Poincaré_⇒_coercivity}]--> output: `s_coercive_continuous_bilinear_form`
3. input: `s_coercive_continuous_bilinear_form` --[t_compose_with_identity {tool: Lax_Milgram_yields_unique_u∈H¹_0}]--> output: `s_weak_formulation_elliptic`

**Techniques used:** t_duality, t_compose_with_identity

---

### Stone–Weierstrass theorem (cite: https://en.wikipedia.org/wiki/Stone%E2%80%93Weierstrass_theorem)

**Axioms:** `s_compact_hausdorff_space`, `s_unital_subalgebra_A_of_C(K)_separating_points`
**Terminal:** `s_stone_weierstrass` (kind: theorem)

**Steps:**
1. input: `s_unital_subalgebra_A_of_C(K)_separating_points` --[t_auxiliary_construction {object: lattice_closure_of_A_via_|f|=√(f²)_uniformly_approximated_by_polynomials}]--> output: `s_a_is_lattice_under_uniform_closure`
2. input: `s_a_is_lattice_under_uniform_closure` --[t_exhaustion_squeeze {tool: Kakutani_Stone_lattice_approximation_per_pair_of_points}]--> output: `s_pairwise_approximation_per_(p,q)`
3. input: `s_pairwise_approximation_per_(p,q)` --[t_compactness_argument {tool: finite_subcover_of_K_+_minimum_pasting}]--> output: `s_stone_weierstrass`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_compactness_argument

---
