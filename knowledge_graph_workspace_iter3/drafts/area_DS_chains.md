# Area Dynamical Systems & Ergodic Theory Derivation Chains (iter-3)

**Source pages:**
- https://en.wikipedia.org/wiki/Category:Theorems_in_dynamical_systems
- https://en.wikipedia.org/wiki/Category:Theorems_in_ergodic_theory
- https://en.wikipedia.org/wiki/List_of_dynamical_systems_and_differential_equations_topics
- https://en.wikipedia.org/wiki/Category:Ergodic_theory
- https://en.wikipedia.org/wiki/Hyperbolic_dynamics

**Target:** 70 chains. **Drafted:** 70. **Skipped (already in graph):** 2 — `s_birkhoff_ergodic_theorem` (Birkhoff ergodic theorem), `s_szemeredi_theorem_terminal` (Szemerédi).

**Flagged (`⚠ needs new technique`):** 0.

**Note:** Some overlap is acknowledged with the PDE agent (e.g., KAM, Floquet, Aubry–Mather) and the NT agent (Selberg trace formula, Margulis arithmeticity). Where I draft a chain that overlaps, I tag it (overlap: …) and let integration dedupe. I reuse existing axiom ids where possible (`s_measure_preserving_transformation`, `s_lie_group`, `s_furstenberg_system_with_positive_measure_A`, `s_compact_smooth_manifold`, `s_riemannian_metric`).

---

## I. Recurrence and ergodic theorems

### Poincaré recurrence theorem (cite: https://en.wikipedia.org/wiki/Poincar%C3%A9_recurrence_theorem)

**Axioms:** `s_measure_preserving_transformation`, `s_finite_measure_space`
**Terminal:** `s_poincare_recurrence` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_preserving_transformation, s_finite_measure_space⟩` --[t_auxiliary_construction {object: "set of points never returning to A"}]--> output: `s_wandering_subset_of_A`
2. input: `s_wandering_subset_of_A` --[t_pigeonhole_collision {pigeons: "iterates T^n(A)", holes: "finite measure"}]--> output: `s_two_iterates_overlap`
3. input: `s_two_iterates_overlap` --[t_reductio_ad_absurdum {assumption: "no recurrence"}]--> output: `s_poincare_recurrence`

**Techniques used:** t_auxiliary_construction, t_pigeonhole_collision, t_reductio_ad_absurdum

---

### Khinchin recurrence theorem (cite: https://en.wikipedia.org/wiki/Poincar%C3%A9_recurrence_theorem#Khinchin's_theorem)

**Axioms:** `s_measure_preserving_transformation`, `s_set_of_positive_measure_A`
**Terminal:** `s_khinchin_recurrence` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_preserving_transformation, s_set_of_positive_measure_A⟩` --[t_auxiliary_construction {object: "indicator 1_A averaged along orbit"}]--> output: `s_ergodic_average_of_indicator`
2. input: `s_ergodic_average_of_indicator` --[t_projection_to_subspace {target: "T-invariant L^2 functions"}]--> output: `s_orthogonal_projection_onto_invariants`
3. input: `s_orthogonal_projection_onto_invariants` --[t_pigeonhole_collision {pigeons: "n with μ(A∩T^{-n}A) small", holes: "L^2 mass"}]--> output: `s_density_lower_bound_on_return_times`
4. input: `s_density_lower_bound_on_return_times` --[t_exhaustion_squeeze {direction: "syndetic set of returns"}]--> output: `s_khinchin_recurrence`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_pigeonhole_collision, t_exhaustion_squeeze

---

### Furstenberg multiple recurrence theorem (cite: https://en.wikipedia.org/wiki/Furstenberg%27s_multiple_recurrence_theorem)

**Axioms:** `s_furstenberg_system_with_positive_measure_A`
**Terminal:** `s_furstenberg_multiple_recurrence` (kind: theorem)

**Steps:**
1. input: `s_furstenberg_system_with_positive_measure_A` --[t_structural_isomorphism {decomposition: "compact / weak-mixing tower"}]--> output: `s_furstenberg_structure_tower`
2. input: `s_furstenberg_structure_tower` --[t_projection_to_subspace {target: "Kronecker / nilpotent factor"}]--> output: `s_distal_factor_with_AP_returns`
3. input: `s_distal_factor_with_AP_returns` --[t_exhaustion_squeeze {limit: "joint return on all k shifts"}]--> output: `s_multiple_recurrence_for_A`
4. input: `s_multiple_recurrence_for_A` --[t_compose_with_identity {wrap: "any k ≥ 1 admits return"}]--> output: `s_furstenberg_multiple_recurrence`

**Techniques used:** t_structural_isomorphism, t_projection_to_subspace, t_exhaustion_squeeze, t_compose_with_identity

---

### von Neumann mean ergodic theorem (cite: https://en.wikipedia.org/wiki/Mean_ergodic_theorem)

**Axioms:** `s_unitary_operator_on_hilbert_space`
**Terminal:** `s_von_neumann_mean_ergodic` (kind: theorem)

**Steps:**
1. input: `s_unitary_operator_on_hilbert_space` --[t_svd_and_spectral_decomposition {tool: "spectral theorem for unitaries"}]--> output: `s_spectral_measure_on_unit_circle`
2. input: `s_spectral_measure_on_unit_circle` --[t_projection_to_subspace {target: "fixed subspace ker(U−I)"}]--> output: `s_orthogonal_decomposition_fixed_plus_coboundary`
3. input: `s_orthogonal_decomposition_fixed_plus_coboundary` --[t_exhaustion_squeeze {limit: "Cesàro sums converge in L^2"}]--> output: `s_von_neumann_mean_ergodic`

**Techniques used:** t_svd_and_spectral_decomposition, t_projection_to_subspace, t_exhaustion_squeeze

---

### Wiener ergodic theorem (L¹) (cite: https://en.wikipedia.org/wiki/Wiener%27s_ergodic_theorem)

**Axioms:** `s_measure_preserving_transformation`, `s_L1_function`
**Terminal:** `s_wiener_ergodic_l1` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_preserving_transformation, s_L1_function⟩` --[t_auxiliary_construction {object: "maximal function M_T f"}]--> output: `s_hardy_littlewood_maximal_for_T`
2. input: `s_hardy_littlewood_maximal_for_T` --[t_exhaustion_squeeze {tool: "weak (1,1) bound"}]--> output: `s_weak_type_inequality_for_averages`
3. input: `s_weak_type_inequality_for_averages` --[t_interpolate_and_continue {density: "dense subset of L^1"}]--> output: `s_wiener_ergodic_l1`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_interpolate_and_continue

---

### Kingman subadditive ergodic theorem (cite: https://en.wikipedia.org/wiki/Subadditive_ergodic_theorem)

**Axioms:** `s_measure_preserving_transformation`, `s_subadditive_cocycle`
**Terminal:** `s_kingman_subadditive_ergodic` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_preserving_transformation, s_subadditive_cocycle⟩` --[t_auxiliary_construction {object: "limsup f_n/n and liminf f_n/n"}]--> output: `s_invariant_limsup_liminf_pair`
2. input: `s_invariant_limsup_liminf_pair` --[t_compactness_argument {tool: "selecting block decomposition"}]--> output: `s_block_decomposition_with_controlled_error`
3. input: `s_block_decomposition_with_controlled_error` --[t_exhaustion_squeeze {direction: "limsup ≤ liminf"}]--> output: `s_kingman_subadditive_ergodic`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Oseledec multiplicative ergodic theorem (cite: https://en.wikipedia.org/wiki/Oseledets_theorem)

**Axioms:** `s_measure_preserving_transformation`, `s_matrix_cocycle_over_T`
**Terminal:** `s_oseledec_multiplicative_ergodic` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_preserving_transformation, s_matrix_cocycle_over_T⟩` --[t_auxiliary_construction {object: "Lyapunov norm ‖A_n(x)v‖^{1/n}"}]--> output: `s_lyapunov_growth_function`
2. input: `s_lyapunov_growth_function` --[t_svd_and_spectral_decomposition {tool: "polar decomposition of A_n"}]--> output: `s_singular_value_filtration`
3. input: `s_singular_value_filtration` --[t_exhaustion_squeeze {limit: "n → ∞ along ergodic average"}]--> output: `s_lyapunov_spectrum_a_e`
4. input: `s_lyapunov_spectrum_a_e` --[t_projection_to_subspace {target: "Oseledec filtration / splitting"}]--> output: `s_oseledec_multiplicative_ergodic`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_exhaustion_squeeze, t_projection_to_subspace

---

### Pesin entropy formula (cite: https://en.wikipedia.org/wiki/Pesin_entropy_formula)

**Axioms:** `s_smooth_volume_preserving_diffeomorphism`
**Terminal:** `s_pesin_entropy_formula` (kind: theorem)

**Steps:**
1. input: `s_smooth_volume_preserving_diffeomorphism` --[t_auxiliary_construction {object: "Oseledec splitting with Lyapunov exponents"}]--> output: `s_oseledec_splitting_for_f`
2. input: `s_oseledec_splitting_for_f` --[t_auxiliary_construction {object: "local unstable manifolds W^u_loc"}]--> output: `s_local_unstable_manifold_family`
3. input: `s_local_unstable_manifold_family` --[t_projection_to_subspace {target: "partition subordinate to W^u"}]--> output: `s_conditional_entropy_along_unstable`
4. input: `s_conditional_entropy_along_unstable` --[t_exhaustion_squeeze {identity: "h_μ = ∑ χ_i^+ a.e."}]--> output: `s_pesin_entropy_formula`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_exhaustion_squeeze

---

### Margulis–Ruelle inequality (cite: https://en.wikipedia.org/wiki/Ruelle_inequality)

**Axioms:** `s_C1_diffeomorphism_of_compact_manifold`, `s_invariant_borel_probability`
**Terminal:** `s_margulis_ruelle_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_C1_diffeomorphism_of_compact_manifold, s_invariant_borel_probability⟩` --[t_auxiliary_construction {object: "Lyapunov spectrum χ_i"}]--> output: `s_lyapunov_exponents_ae`
2. input: `s_lyapunov_exponents_ae` --[t_projection_to_subspace {target: "expanding subbundle"}]--> output: `s_partition_subordinate_to_expanding`
3. input: `s_partition_subordinate_to_expanding` --[t_exhaustion_squeeze {bound: "h_μ ≤ ∑ χ_i^+"}]--> output: `s_margulis_ruelle_inequality`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_exhaustion_squeeze

---

### Variational principle for topological entropy (cite: https://en.wikipedia.org/wiki/Topological_entropy#Variational_principle)

**Axioms:** `s_continuous_self_map_of_compact_space`
**Terminal:** `s_variational_principle_entropy` (kind: theorem)

**Steps:**
1. input: `s_continuous_self_map_of_compact_space` --[t_auxiliary_construction {object: "(n,ε)-separated set N(n,ε)"}]--> output: `s_topological_entropy_h_top`
2. input: `s_topological_entropy_h_top` --[t_duality {pair: "measures ↔ separated sets via Misiurewicz partition"}]--> output: `s_measure_entropy_bounded_by_h_top`
3. input: `s_measure_entropy_bounded_by_h_top` --[t_compactness_argument {space: "M_inv(X) weak-* compact"}]--> output: `s_supremum_attained_by_invariant_measure`
4. input: `s_supremum_attained_by_invariant_measure` --[t_exhaustion_squeeze {equality: "sup h_μ = h_top"}]--> output: `s_variational_principle_entropy`

**Techniques used:** t_auxiliary_construction, t_duality, t_compactness_argument, t_exhaustion_squeeze

---

### Krylov–Bogolyubov existence of invariant measures (cite: https://en.wikipedia.org/wiki/Krylov%E2%80%93Bogolyubov_theorem)

**Axioms:** `s_continuous_self_map_of_compact_space`
**Terminal:** `s_krylov_bogolyubov_invariant_measure` (kind: theorem)

**Steps:**
1. input: `s_continuous_self_map_of_compact_space` --[t_auxiliary_construction {object: "Cesàro averages μ_n = (1/n) ∑ δ_{T^k x}"}]--> output: `s_cesaro_average_of_dirac_orbits`
2. input: `s_cesaro_average_of_dirac_orbits` --[t_compactness_argument {space: "Prob(X) weak-* compact"}]--> output: `s_weak_star_limit_point_of_averages`
3. input: `s_weak_star_limit_point_of_averages` --[t_exhaustion_squeeze {check: "T-invariance under integration"}]--> output: `s_krylov_bogolyubov_invariant_measure`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Hopf decomposition theorem (cite: https://en.wikipedia.org/wiki/Hopf_decomposition)

**Axioms:** `s_measure_preserving_transformation`, `s_sigma_finite_measure_space`
**Terminal:** `s_hopf_decomposition` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_preserving_transformation, s_sigma_finite_measure_space⟩` --[t_auxiliary_construction {object: "conservative vs dissipative parts"}]--> output: `s_conservative_dissipative_split`
2. input: `s_conservative_dissipative_split` --[t_projection_to_subspace {target: "T-invariant sigma-algebra"}]--> output: `s_invariant_partition_C_D`
3. input: `s_invariant_partition_C_D` --[t_exhaustion_squeeze {uniqueness: "Hopf decomposition"}]--> output: `s_hopf_decomposition`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_exhaustion_squeeze

---

### Ergodic decomposition theorem (cite: https://en.wikipedia.org/wiki/Ergodic_decomposition_theorem)

**Axioms:** `s_measure_preserving_transformation`, `s_invariant_probability_measure`
**Terminal:** `s_ergodic_decomposition_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_preserving_transformation, s_invariant_probability_measure⟩` --[t_projection_to_subspace {target: "T-invariant sigma-algebra"}]--> output: `s_conditional_measure_family`
2. input: `s_conditional_measure_family` --[t_auxiliary_construction {object: "ergodic component μ_x"}]--> output: `s_ergodic_components_disintegration`
3. input: `s_ergodic_components_disintegration` --[t_exhaustion_squeeze {identity: "μ = ∫ μ_x dμ"}]--> output: `s_ergodic_decomposition_theorem`

**Techniques used:** t_projection_to_subspace, t_auxiliary_construction, t_exhaustion_squeeze

---

## II. Symbolic dynamics, entropy, and structural theorems

### Bowen's specification property implies unique equilibrium (cite: https://en.wikipedia.org/wiki/Specification_property)

**Axioms:** `s_expansive_homeomorphism_with_specification`, `s_holder_potential_phi`
**Terminal:** `s_bowen_specification_unique_equilibrium` (kind: theorem)

**Steps:**
1. input: `⟨s_expansive_homeomorphism_with_specification, s_holder_potential_phi⟩` --[t_auxiliary_construction {object: "Bowen ball B_n(x,ε) partition function"}]--> output: `s_bowen_partition_function_Z_n`
2. input: `s_bowen_partition_function_Z_n` --[t_compactness_argument {limit: "subadditive limit P(φ)"}]--> output: `s_topological_pressure_P_phi`
3. input: `s_topological_pressure_P_phi` --[t_contraction_fixed_point {operator: "transfer operator L_φ"}]--> output: `s_eigenmeasure_for_L_phi`
4. input: `s_eigenmeasure_for_L_phi` --[t_exhaustion_squeeze {uniqueness: "Gibbs / equilibrium state"}]--> output: `s_bowen_specification_unique_equilibrium`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Bowen formula for Hausdorff dimension of repellers (cite: https://en.wikipedia.org/wiki/Bowen%27s_formula)

**Axioms:** `s_conformal_expanding_repeller_J`
**Terminal:** `s_bowen_dimension_formula` (kind: theorem)

**Steps:**
1. input: `s_conformal_expanding_repeller_J` --[t_auxiliary_construction {object: "geometric potential φ_s = -s log |f'|"}]--> output: `s_geometric_pressure_function_P_s`
2. input: `s_geometric_pressure_function_P_s` --[t_contraction_fixed_point {root: "P(φ_s) = 0"}]--> output: `s_bowen_root_s_star`
3. input: `s_bowen_root_s_star` --[t_exhaustion_squeeze {identity: "dim_H(J) = s*"}]--> output: `s_bowen_dimension_formula`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Curtis–Hedlund–Lyndon theorem (cite: https://en.wikipedia.org/wiki/Curtis%E2%80%93Hedlund%E2%80%93Lyndon_theorem)

**Axioms:** `s_shift_space_A_Z`, `s_continuous_shift_commuting_map`
**Terminal:** `s_curtis_hedlund_lyndon` (kind: theorem)

**Steps:**
1. input: `⟨s_shift_space_A_Z, s_continuous_shift_commuting_map⟩` --[t_compactness_argument {space: "Cantor / A^ℤ"}]--> output: `s_uniform_continuity_via_compactness`
2. input: `s_uniform_continuity_via_compactness` --[t_auxiliary_construction {object: "finite radius r local rule"}]--> output: `s_local_rule_of_radius_r`
3. input: `s_local_rule_of_radius_r` --[t_structural_isomorphism {identification: "cellular automaton ↔ shift-commuting cts map"}]--> output: `s_curtis_hedlund_lyndon`

**Techniques used:** t_compactness_argument, t_auxiliary_construction, t_structural_isomorphism

---

### Williams classification of SFTs up to shift equivalence (cite: https://en.wikipedia.org/wiki/Subshift_of_finite_type#Conjugacy)

**Axioms:** `s_subshift_of_finite_type`
**Terminal:** `s_williams_shift_equivalence` (kind: theorem)

**Steps:**
1. input: `s_subshift_of_finite_type` --[t_structural_isomorphism {target: "edge shift on transition matrix A"}]--> output: `s_transition_matrix_presentation_A`
2. input: `s_transition_matrix_presentation_A` --[t_auxiliary_construction {object: "strong shift equivalence via elementary R,S decomposition"}]--> output: `s_strong_shift_equivalence_chain`
3. input: `s_strong_shift_equivalence_chain` --[t_exhaustion_squeeze {invariant: "shift equivalence ⇒ conjugacy"}]--> output: `s_williams_shift_equivalence`

**Techniques used:** t_structural_isomorphism, t_auxiliary_construction, t_exhaustion_squeeze

---

### Perron–Frobenius for primitive nonnegative matrices (cite: https://en.wikipedia.org/wiki/Perron%E2%80%93Frobenius_theorem)

**Axioms:** `s_primitive_nonnegative_matrix_A`
**Terminal:** `s_perron_frobenius_theorem` (kind: theorem)

**Steps:**
1. input: `s_primitive_nonnegative_matrix_A` --[t_auxiliary_construction {object: "Hilbert projective metric on positive cone"}]--> output: `s_hilbert_metric_on_cone`
2. input: `s_hilbert_metric_on_cone` --[t_contraction_fixed_point {operator: "A acts as contraction on cone"}]--> output: `s_unique_positive_eigenvector`
3. input: `s_unique_positive_eigenvector` --[t_svd_and_spectral_decomposition {invariant: "spectral gap of A"}]--> output: `s_perron_frobenius_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_svd_and_spectral_decomposition

---

### Sharkovskii's theorem (period 3 implies all periods) (cite: https://en.wikipedia.org/wiki/Sharkovskii%27s_theorem)

**Axioms:** `s_continuous_function_on_interval`
**Terminal:** `s_sharkovskii_theorem` (kind: theorem)

**Steps:**
1. input: `s_continuous_function_on_interval` --[t_auxiliary_construction {object: "Markov graph of intervals covering each other"}]--> output: `s_markov_graph_of_covers`
2. input: `s_markov_graph_of_covers` --[t_compactness_argument {tool: "intermediate value theorem on covers"}]--> output: `s_period_implication_from_covers`
3. input: `s_period_implication_from_covers` --[t_finite_case_check {ordering: "3 ▷ 5 ▷ 7 ▷ … ▷ 2^k"}]--> output: `s_sharkovskii_ordering_on_periods`
4. input: `s_sharkovskii_ordering_on_periods` --[t_exhaustion_squeeze {direction: "period m ⇒ period n for n ◁ m"}]--> output: `s_sharkovskii_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_finite_case_check, t_exhaustion_squeeze

---

### Singer's theorem (negative Schwarzian implies bounded attractors) (cite: https://en.wikipedia.org/wiki/Schwarzian_derivative#Singer's_theorem)

**Axioms:** `s_interval_map_with_negative_schwarzian`
**Terminal:** `s_singer_theorem` (kind: theorem)

**Steps:**
1. input: `s_interval_map_with_negative_schwarzian` --[t_conserved_quantity {invariant: "Schwarzian Sf < 0 stable under composition"}]--> output: `s_negative_schwarzian_preserved_under_iteration`
2. input: `s_negative_schwarzian_preserved_under_iteration` --[t_auxiliary_construction {object: "immediate basin of periodic attractor"}]--> output: `s_basin_with_no_interior_critical_point_or_boundary`
3. input: `s_basin_with_no_interior_critical_point_or_boundary` --[t_exhaustion_squeeze {bound: "attractor basin meets critical orbit or ∂I"}]--> output: `s_singer_theorem`

**Techniques used:** t_conserved_quantity, t_auxiliary_construction, t_exhaustion_squeeze

---

### Misiurewicz–Thurston rigidity for postcritically finite maps (cite: https://en.wikipedia.org/wiki/Thurston%27s_theorem_for_postcritically_finite_maps)

**Axioms:** `s_postcritically_finite_branched_cover_of_S2`
**Terminal:** `s_thurston_pcf_rigidity` (kind: theorem)

**Steps:**
1. input: `s_postcritically_finite_branched_cover_of_S2` --[t_auxiliary_construction {object: "Teichmüller space of marked sphere"}]--> output: `s_teichmuller_pullback_map_sigma_f`
2. input: `s_teichmuller_pullback_map_sigma_f` --[t_contraction_fixed_point {operator: "σ_f on Teich(S^2, P_f)"}]--> output: `s_fixed_point_or_obstruction_dichotomy`
3. input: `s_fixed_point_or_obstruction_dichotomy` --[t_obstruction_class {class: "Thurston obstruction = invariant multicurve"}]--> output: `s_thurston_pcf_rigidity`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_obstruction_class

---

## III. Hyperbolic dynamics

### Hadamard–Perron stable/unstable manifold theorem (cite: https://en.wikipedia.org/wiki/Stable_manifold_theorem)

**Axioms:** `s_hyperbolic_fixed_point_of_diffeomorphism`
**Terminal:** `s_hadamard_perron_stable_manifold` (kind: theorem)

**Steps:**
1. input: `s_hyperbolic_fixed_point_of_diffeomorphism` --[t_auxiliary_construction {object: "graph transform on space of Lipschitz sections"}]--> output: `s_graph_transform_operator`
2. input: `s_graph_transform_operator` --[t_contraction_fixed_point {space: "Banach space of Lipschitz graphs"}]--> output: `s_invariant_lipschitz_graph_W_s`
3. input: `s_invariant_lipschitz_graph_W_s` --[t_exhaustion_squeeze {regularity: "bootstrap to C^k smoothness"}]--> output: `s_hadamard_perron_stable_manifold`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Hartman–Grobman theorem (cite: https://en.wikipedia.org/wiki/Hartman%E2%80%93Grobman_theorem)

**Axioms:** `s_hyperbolic_fixed_point_of_diffeomorphism`
**Terminal:** `s_hartman_grobman_theorem` (kind: theorem)

**Steps:**
1. input: `s_hyperbolic_fixed_point_of_diffeomorphism` --[t_auxiliary_construction {object: "conjugacy equation h ∘ f = Df(0) ∘ h"}]--> output: `s_conjugacy_functional_equation`
2. input: `s_conjugacy_functional_equation` --[t_contraction_fixed_point {space: "C^0 bounded perturbations"}]--> output: `s_topological_conjugacy_h`
3. input: `s_topological_conjugacy_h` --[t_exhaustion_squeeze {neighborhood: "local linearization"}]--> output: `s_hartman_grobman_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Anosov closing lemma (cite: https://en.wikipedia.org/wiki/Anosov_diffeomorphism#Closing_lemma)

**Axioms:** `s_anosov_diffeomorphism`, `s_epsilon_pseudo_periodic_orbit`
**Terminal:** `s_anosov_closing_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_anosov_diffeomorphism, s_epsilon_pseudo_periodic_orbit⟩` --[t_auxiliary_construction {object: "local product structure rectangle"}]--> output: `s_local_product_box`
2. input: `s_local_product_box` --[t_contraction_fixed_point {operator: "intersection of stable+unstable"}]--> output: `s_unique_periodic_orbit_near_pseudo`
3. input: `s_unique_periodic_orbit_near_pseudo` --[t_exhaustion_squeeze {bound: "shadowing distance ≤ Cε"}]--> output: `s_anosov_closing_lemma`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Anosov shadowing lemma (cite: https://en.wikipedia.org/wiki/Shadowing_lemma)

**Axioms:** `s_anosov_diffeomorphism`, `s_delta_pseudo_orbit`
**Terminal:** `s_anosov_shadowing_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_anosov_diffeomorphism, s_delta_pseudo_orbit⟩` --[t_auxiliary_construction {object: "infinite-product space of correction terms"}]--> output: `s_correction_sequence_space`
2. input: `s_correction_sequence_space` --[t_contraction_fixed_point {operator: "shadowing map on E^s ⊕ E^u sequences"}]--> output: `s_unique_shadowing_orbit`
3. input: `s_unique_shadowing_orbit` --[t_exhaustion_squeeze {error: "ε(δ) → 0 as δ → 0"}]--> output: `s_anosov_shadowing_lemma`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Smale horseshoe (cite: https://en.wikipedia.org/wiki/Horseshoe_map)

**Axioms:** `s_diffeomorphism_with_transverse_homoclinic_point`
**Terminal:** `s_smale_horseshoe` (kind: theorem)

**Steps:**
1. input: `s_diffeomorphism_with_transverse_homoclinic_point` --[t_auxiliary_construction {object: "rectangle R with horizontal/vertical strips"}]--> output: `s_markov_rectangle_R`
2. input: `s_markov_rectangle_R` --[t_structural_isomorphism {target: "full 2-shift Σ_2"}]--> output: `s_invariant_cantor_set_Λ`
3. input: `s_invariant_cantor_set_Λ` --[t_exhaustion_squeeze {dynamics: "topological conjugacy to (Σ_2, σ)"}]--> output: `s_smale_horseshoe`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_exhaustion_squeeze

---

### Smale–Birkhoff homoclinic theorem (cite: https://en.wikipedia.org/wiki/Homoclinic_orbit#Smale%E2%80%93Birkhoff_theorem)

**Axioms:** `s_diffeomorphism_with_transverse_homoclinic_point`
**Terminal:** `s_smale_birkhoff_homoclinic` (kind: theorem)

**Steps:**
1. input: `s_diffeomorphism_with_transverse_homoclinic_point` --[t_auxiliary_construction {object: "iterated rectangle near homoclinic intersection"}]--> output: `s_iterated_neighborhood_of_homoclinic`
2. input: `s_iterated_neighborhood_of_homoclinic` --[t_structural_isomorphism {target: "horseshoe in iterate f^N"}]--> output: `s_horseshoe_in_f_N`
3. input: `s_horseshoe_in_f_N` --[t_exhaustion_squeeze {inclusion: "shift Σ_2 embeds in dynamics"}]--> output: `s_smale_birkhoff_homoclinic`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_exhaustion_squeeze

---

### Smale spectral decomposition theorem (cite: https://en.wikipedia.org/wiki/Axiom_A)

**Axioms:** `s_axiom_A_diffeomorphism`
**Terminal:** `s_smale_spectral_decomposition` (kind: theorem)

**Steps:**
1. input: `s_axiom_A_diffeomorphism` --[t_auxiliary_construction {object: "non-wandering set Ω(f)"}]--> output: `s_non_wandering_set_Omega`
2. input: `s_non_wandering_set_Omega` --[t_projection_to_subspace {target: "basic sets via local product structure"}]--> output: `s_basic_set_partition`
3. input: `s_basic_set_partition` --[t_exhaustion_squeeze {finite_disjoint: "Ω = Ω_1 ⊔ … ⊔ Ω_k"}]--> output: `s_smale_spectral_decomposition`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_exhaustion_squeeze

---

### Sinai–Ruelle–Bowen (SRB) measure existence for Axiom A (cite: https://en.wikipedia.org/wiki/SRB_measure)

**Axioms:** `s_axiom_A_attractor`
**Terminal:** `s_srb_measure_existence` (kind: theorem)

**Steps:**
1. input: `s_axiom_A_attractor` --[t_auxiliary_construction {object: "Markov partition of attractor"}]--> output: `s_markov_partition_of_attractor`
2. input: `s_markov_partition_of_attractor` --[t_structural_isomorphism {target: "two-sided subshift of finite type"}]--> output: `s_sft_conjugate_to_attractor`
3. input: `s_sft_conjugate_to_attractor` --[t_contraction_fixed_point {operator: "Ruelle transfer operator for log |Df|_E^u|"}]--> output: `s_gibbs_state_for_unstable_potential`
4. input: `s_gibbs_state_for_unstable_potential` --[t_exhaustion_squeeze {projection: "push down to manifold"}]--> output: `s_srb_measure_existence`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Manning's theorem (volume entropy = topological entropy) (cite: https://en.wikipedia.org/wiki/Topological_entropy#Manning's_theorem)

**Axioms:** `s_compact_negatively_curved_riemannian_manifold`
**Terminal:** `s_manning_volume_entropy` (kind: theorem)

**Steps:**
1. input: `s_compact_negatively_curved_riemannian_manifold` --[t_auxiliary_construction {object: "volume of ball B(x,R) in universal cover"}]--> output: `s_volume_growth_function`
2. input: `s_volume_growth_function` --[t_rescale_for_asymptotic_geometry {limit: "exponential growth rate h_vol"}]--> output: `s_volume_entropy_h_vol`
3. input: `s_volume_entropy_h_vol` --[t_duality {pair: "geodesic flow ↔ universal cover growth"}]--> output: `s_topological_entropy_of_geodesic_flow`
4. input: `s_topological_entropy_of_geodesic_flow` --[t_exhaustion_squeeze {equality: "h_top = h_vol"}]--> output: `s_manning_volume_entropy`

**Techniques used:** t_auxiliary_construction, t_rescale_for_asymptotic_geometry, t_duality, t_exhaustion_squeeze

---

### Pesin set / Pesin block existence (cite: https://en.wikipedia.org/wiki/Pesin_theory)

**Axioms:** `s_smooth_diffeomorphism_with_nonzero_lyapunov_spectrum`
**Terminal:** `s_pesin_set_theorem` (kind: theorem)

**Steps:**
1. input: `s_smooth_diffeomorphism_with_nonzero_lyapunov_spectrum` --[t_auxiliary_construction {object: "Lyapunov chart with anisotropic norm"}]--> output: `s_lyapunov_charts`
2. input: `s_lyapunov_charts` --[t_compactness_argument {space: "regular set, level ℓ"}]--> output: `s_pesin_block_Lambda_ell`
3. input: `s_pesin_block_Lambda_ell` --[t_exhaustion_squeeze {union: "full measure ⋃_ℓ Λ_ℓ"}]--> output: `s_pesin_set_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Mañé–Bowen formula for repellers (cite: https://en.wikipedia.org/wiki/Bowen%27s_formula)

**Axioms:** `s_conformal_repeller_with_holder_jacobian`
**Terminal:** `s_mane_bowen_formula` (kind: theorem)

**Steps:**
1. input: `s_conformal_repeller_with_holder_jacobian` --[t_auxiliary_construction {object: "pressure P(-s log |f'|)"}]--> output: `s_pressure_function_of_s`
2. input: `s_pressure_function_of_s` --[t_contraction_fixed_point {root: "unique s with P=0"}]--> output: `s_bowen_root_for_repeller`
3. input: `s_bowen_root_for_repeller` --[t_exhaustion_squeeze {identity: "dim_H = s_*"}]--> output: `s_mane_bowen_formula`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Bowen's equidistribution of periodic orbits (cite: https://en.wikipedia.org/wiki/Bowen%27s_formula)

**Axioms:** `s_axiom_A_basic_set`, `s_holder_potential_phi`
**Terminal:** `s_bowen_periodic_equidistribution` (kind: theorem)

**Steps:**
1. input: `⟨s_axiom_A_basic_set, s_holder_potential_phi⟩` --[t_auxiliary_construction {object: "weighted periodic measure (1/Z_n)∑ e^{S_n φ(p)} δ_p"}]--> output: `s_weighted_periodic_orbit_measure`
2. input: `s_weighted_periodic_orbit_measure` --[t_contraction_fixed_point {operator: "Ruelle transfer L_φ"}]--> output: `s_convergence_to_equilibrium_state`
3. input: `s_convergence_to_equilibrium_state` --[t_exhaustion_squeeze {limit: "n → ∞"}]--> output: `s_bowen_periodic_equidistribution`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

## IV. Complex dynamics

### Julia–Fatou dichotomy (cite: https://en.wikipedia.org/wiki/Julia_set)

**Axioms:** `s_rational_map_on_riemann_sphere`
**Terminal:** `s_julia_fatou_dichotomy` (kind: theorem)

**Steps:**
1. input: `s_rational_map_on_riemann_sphere` --[t_auxiliary_construction {object: "normal family of iterates {f^n}"}]--> output: `s_normality_locus_F_f`
2. input: `s_normality_locus_F_f` --[t_compactness_argument {tool: "Montel's theorem"}]--> output: `s_montel_normal_family_criterion`
3. input: `s_montel_normal_family_criterion` --[t_duality {pair: "Fatou (normal) vs Julia (chaotic)"}]--> output: `s_julia_fatou_dichotomy`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_duality

---

### Sullivan no-wandering-domains theorem (cite: https://en.wikipedia.org/wiki/No-wandering-domain_theorem)

**Axioms:** `s_rational_map_on_riemann_sphere`
**Terminal:** `s_sullivan_no_wandering` (kind: theorem)

**Steps:**
1. input: `s_rational_map_on_riemann_sphere` --[t_auxiliary_construction {object: "Teichmüller space of Riemann surface lamination"}]--> output: `s_teichmuller_space_of_lamination`
2. input: `s_teichmuller_space_of_lamination` --[t_compactness_argument {space: "finite-dimensional moduli"}]--> output: `s_finite_dimensional_deformation_space`
3. input: `s_finite_dimensional_deformation_space` --[t_reductio_ad_absurdum {assumption: "wandering domain ⇒ infinite-dim QC deformations"}]--> output: `s_sullivan_no_wandering`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_reductio_ad_absurdum

---

### Mañé–Sad–Sullivan structural stability (cite: https://en.wikipedia.org/wiki/Holomorphic_motion)

**Axioms:** `s_family_of_rational_maps_with_parameter_λ`
**Terminal:** `s_mane_sad_sullivan_stability` (kind: theorem)

**Steps:**
1. input: `s_family_of_rational_maps_with_parameter_λ` --[t_auxiliary_construction {object: "holomorphic motion of Julia set"}]--> output: `s_holomorphic_motion_of_J_λ`
2. input: `s_holomorphic_motion_of_J_λ` --[t_compactness_argument {extension: "λ-lemma extends to closure"}]--> output: `s_lambda_lemma_extension`
3. input: `s_lambda_lemma_extension` --[t_exhaustion_squeeze {open_density: "J-stability is open and dense"}]--> output: `s_mane_sad_sullivan_stability`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Douady–Hubbard straightening theorem (cite: https://en.wikipedia.org/wiki/Polynomial-like_map)

**Axioms:** `s_polynomial_like_map_of_degree_d`
**Terminal:** `s_douady_hubbard_straightening` (kind: theorem)

**Steps:**
1. input: `s_polynomial_like_map_of_degree_d` --[t_auxiliary_construction {object: "Beltrami coefficient extending dynamics"}]--> output: `s_invariant_beltrami_coefficient`
2. input: `s_invariant_beltrami_coefficient` --[t_contraction_fixed_point {operator: "measurable Riemann mapping theorem"}]--> output: `s_quasiconformal_conjugacy_to_polynomial`
3. input: `s_quasiconformal_conjugacy_to_polynomial` --[t_structural_isomorphism {target: "honest polynomial of degree d"}]--> output: `s_douady_hubbard_straightening`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_structural_isomorphism

---

### Yoccoz's theorem on local connectivity of Mandelbrot at finitely renormalizable points (cite: https://en.wikipedia.org/wiki/Mandelbrot_set#Local_connectivity)

**Axioms:** `s_finitely_renormalizable_quadratic`
**Terminal:** `s_yoccoz_local_connectivity` (kind: theorem)

**Steps:**
1. input: `s_finitely_renormalizable_quadratic` --[t_auxiliary_construction {object: "Yoccoz puzzle pieces at level n"}]--> output: `s_yoccoz_puzzle_at_level_n`
2. input: `s_yoccoz_puzzle_at_level_n` --[t_rescale_for_asymptotic_geometry {bound: "moduli grow / a-priori bounds"}]--> output: `s_a_priori_moduli_bound`
3. input: `s_a_priori_moduli_bound` --[t_exhaustion_squeeze {limit: "diameter of nested pieces → 0"}]--> output: `s_yoccoz_local_connectivity`

**Techniques used:** t_auxiliary_construction, t_rescale_for_asymptotic_geometry, t_exhaustion_squeeze

---

### Misiurewicz–Mañé theorem on hyperbolicity from non-recurrent critical orbits (cite: https://en.wikipedia.org/wiki/Hyperbolic_set)

**Axioms:** `s_rational_map_with_nonrecurrent_critical_orbits`
**Terminal:** `s_mane_hyperbolicity_theorem` (kind: theorem)

**Steps:**
1. input: `s_rational_map_with_nonrecurrent_critical_orbits` --[t_auxiliary_construction {object: "expansion estimate away from postcritical set"}]--> output: `s_local_expansion_estimate`
2. input: `s_local_expansion_estimate` --[t_compactness_argument {set: "Julia set minus periodic attractors"}]--> output: `s_uniform_expansion_on_J`
3. input: `s_uniform_expansion_on_J` --[t_exhaustion_squeeze {conclusion: "Julia set is hyperbolic"}]--> output: `s_mane_hyperbolicity_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Brolin–Lyubich measure of maximal entropy for rational maps (cite: https://en.wikipedia.org/wiki/Equidistribution_theorem)

**Axioms:** `s_rational_map_of_degree_d_at_least_2`
**Terminal:** `s_brolin_lyubich_measure` (kind: theorem)

**Steps:**
1. input: `s_rational_map_of_degree_d_at_least_2` --[t_auxiliary_construction {object: "pullback (1/d^n) (f^n)* δ_a of point measure"}]--> output: `s_pullback_point_measure_sequence`
2. input: `s_pullback_point_measure_sequence` --[t_compactness_argument {tool: "potential-theoretic equidistribution"}]--> output: `s_potential_theoretic_limit`
3. input: `s_potential_theoretic_limit` --[t_exhaustion_squeeze {invariance_check: "limit is unique, f-invariant, mixing"}]--> output: `s_brolin_lyubich_measure`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

## V. Homogeneous and unipotent dynamics

### Ratner measure rigidity theorem (cite: https://en.wikipedia.org/wiki/Ratner%27s_theorems)

**Axioms:** `s_lie_group`, `s_unipotent_one_parameter_subgroup_u_t`, `s_lattice_subgroup_Gamma`
**Terminal:** `s_ratner_measure_rigidity` (kind: theorem)

**Steps:**
1. input: `⟨s_lie_group, s_unipotent_one_parameter_subgroup_u_t, s_lattice_subgroup_Gamma⟩` --[t_auxiliary_construction {object: "Q-shift invariant under u_t"}]--> output: `s_unipotent_q_shift_invariance`
2. input: `s_unipotent_q_shift_invariance` --[t_symmetry_reduction {group: "centralizer / extra translation invariance"}]--> output: `s_extra_invariance_under_subgroup_H`
3. input: `s_extra_invariance_under_subgroup_H` --[t_structural_isomorphism {target: "homogeneous H-orbit"}]--> output: `s_invariant_measure_is_homogeneous`
4. input: `s_invariant_measure_is_homogeneous` --[t_exhaustion_squeeze {classification: "all u_t-invariant ergodic measures are algebraic"}]--> output: `s_ratner_measure_rigidity`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_structural_isomorphism, t_exhaustion_squeeze

---

### Ratner orbit closure theorem (cite: https://en.wikipedia.org/wiki/Ratner%27s_theorems)

**Axioms:** `s_lie_group`, `s_unipotent_one_parameter_subgroup_u_t`, `s_lattice_subgroup_Gamma`
**Terminal:** `s_ratner_orbit_closure` (kind: theorem)

**Steps:**
1. input: `⟨s_lie_group, s_unipotent_one_parameter_subgroup_u_t, s_lattice_subgroup_Gamma⟩` --[t_auxiliary_construction {object: "closure of orbit u_t·x in G/Γ"}]--> output: `s_orbit_closure_candidate`
2. input: `s_orbit_closure_candidate` --[t_structural_isomorphism {input: "Ratner measure rigidity ⇒ orbit closure is homogeneous"}]--> output: `s_homogeneous_subset_closure`
3. input: `s_homogeneous_subset_closure` --[t_exhaustion_squeeze {classification: "all closures are H·x for closed H ≤ G"}]--> output: `s_ratner_orbit_closure`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_exhaustion_squeeze

---

### Ratner equidistribution theorem (cite: https://en.wikipedia.org/wiki/Ratner%27s_theorems)

**Axioms:** `s_lie_group`, `s_unipotent_one_parameter_subgroup_u_t`, `s_lattice_subgroup_Gamma`
**Terminal:** `s_ratner_equidistribution` (kind: theorem)

**Steps:**
1. input: `⟨s_lie_group, s_unipotent_one_parameter_subgroup_u_t, s_lattice_subgroup_Gamma⟩` --[t_auxiliary_construction {object: "time-average along unipotent orbit"}]--> output: `s_unipotent_time_average`
2. input: `s_unipotent_time_average` --[t_compactness_argument {space: "Prob(G/Γ) weak-* compact, Ratner classification"}]--> output: `s_unique_limit_is_homogeneous_haar`
3. input: `s_unique_limit_is_homogeneous_haar` --[t_exhaustion_squeeze {equidistribution: "time average = space average on H·x"}]--> output: `s_ratner_equidistribution`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Margulis arithmeticity theorem (cite: https://en.wikipedia.org/wiki/Margulis_arithmeticity_theorem)

**Axioms:** `s_semisimple_lie_group_of_higher_rank`, `s_irreducible_lattice_subgroup`
**Terminal:** `s_margulis_arithmeticity` (kind: theorem)

**Steps:**
1. input: `⟨s_semisimple_lie_group_of_higher_rank, s_irreducible_lattice_subgroup⟩` --[t_auxiliary_construction {object: "non-trivial linear representation of Γ"}]--> output: `s_finite_dim_linear_rep_of_lattice`
2. input: `s_finite_dim_linear_rep_of_lattice` --[t_structural_isomorphism {input: "Margulis super-rigidity extends rep to G"}]--> output: `s_extension_to_algebraic_rep_of_G`
3. input: `s_extension_to_algebraic_rep_of_G` --[t_heights_and_galois_rep_bridge {target: "Q-structure on G"}]--> output: `s_q_structure_yielding_arithmetic_lattice`
4. input: `s_q_structure_yielding_arithmetic_lattice` --[t_exhaustion_squeeze {conclusion: "Γ commensurable to G(ℤ)"}]--> output: `s_margulis_arithmeticity`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_heights_and_galois_rep_bridge, t_exhaustion_squeeze

---

### Margulis super-rigidity (cite: https://en.wikipedia.org/wiki/Superrigidity)

**Axioms:** `s_semisimple_lie_group_of_higher_rank`, `s_irreducible_lattice_subgroup`
**Terminal:** `s_margulis_super_rigidity` (kind: theorem)

**Steps:**
1. input: `⟨s_semisimple_lie_group_of_higher_rank, s_irreducible_lattice_subgroup⟩` --[t_auxiliary_construction {object: "ρ: Γ → H linear representation"}]--> output: `s_lattice_representation_rho`
2. input: `s_lattice_representation_rho` --[t_ergodic_correspondence {device: "Furstenberg boundary, harmonic maps from G/P"}]--> output: `s_boundary_map_phi`
3. input: `s_boundary_map_phi` --[t_symmetry_reduction {tool: "Mautner phenomenon / ergodicity on G/P"}]--> output: `s_equivariant_boundary_value`
4. input: `s_equivariant_boundary_value` --[t_exhaustion_squeeze {extension: "ρ extends from Γ to G as algebraic morphism"}]--> output: `s_margulis_super_rigidity`

**Techniques used:** t_auxiliary_construction, t_ergodic_correspondence, t_symmetry_reduction, t_exhaustion_squeeze

---

### Margulis normal subgroup theorem (cite: https://en.wikipedia.org/wiki/Margulis%27s_normal_subgroup_theorem)

**Axioms:** `s_semisimple_lie_group_of_higher_rank`, `s_irreducible_lattice_subgroup`
**Terminal:** `s_margulis_normal_subgroup` (kind: theorem)

**Steps:**
1. input: `⟨s_semisimple_lie_group_of_higher_rank, s_irreducible_lattice_subgroup⟩` --[t_auxiliary_construction {object: "normal subgroup N ⊴ Γ"}]--> output: `s_normal_subgroup_N`
2. input: `s_normal_subgroup_N` --[t_ergodic_correspondence {device: "Γ/N action on G/P amenable+kazhdan dichotomy"}]--> output: `s_amenable_property_T_clash`
3. input: `s_amenable_property_T_clash` --[t_reductio_ad_absurdum {dichotomy: "N finite or Γ/N finite"}]--> output: `s_margulis_normal_subgroup`

**Techniques used:** t_auxiliary_construction, t_ergodic_correspondence, t_reductio_ad_absurdum

---

### Mostow rigidity theorem (cite: https://en.wikipedia.org/wiki/Mostow_rigidity_theorem)

**Axioms:** `s_closed_hyperbolic_manifold_of_dim_at_least_3`
**Terminal:** `s_mostow_rigidity` (kind: theorem)

**Steps:**
1. input: `s_closed_hyperbolic_manifold_of_dim_at_least_3` --[t_auxiliary_construction {object: "boundary map between sphere at infinity"}]--> output: `s_quasiconformal_boundary_map`
2. input: `s_quasiconformal_boundary_map` --[t_rescale_for_asymptotic_geometry {tool: "ergodicity of geodesic flow on boundary"}]--> output: `s_conformal_boundary_extension`
3. input: `s_conformal_boundary_extension` --[t_structural_isomorphism {target: "isometry of universal covers"}]--> output: `s_mostow_rigidity`

**Techniques used:** t_auxiliary_construction, t_rescale_for_asymptotic_geometry, t_structural_isomorphism

---

### Furstenberg ×2 ×3 ergodic measure rigidity (Rudolph) (cite: https://en.wikipedia.org/wiki/Furstenberg%27s_conjecture_on_2-3-invariant_measures)

**Axioms:** `s_circle_R_mod_Z`, `s_jointly_invariant_ergodic_measure_for_x2_x3`
**Terminal:** `s_rudolph_measure_rigidity` (kind: theorem)

**Steps:**
1. input: `⟨s_circle_R_mod_Z, s_jointly_invariant_ergodic_measure_for_x2_x3⟩` --[t_auxiliary_construction {object: "conditional entropy h(×2 | ×3-invariant σ-alg)"}]--> output: `s_conditional_entropy_for_x2_given_x3`
2. input: `s_conditional_entropy_for_x2_given_x3` --[t_projection_to_subspace {target: "T-invariant factor / Pinsker algebra"}]--> output: `s_positive_entropy_implies_full_support_lebesgue`
3. input: `s_positive_entropy_implies_full_support_lebesgue` --[t_exhaustion_squeeze {dichotomy: "either Lebesgue or zero entropy"}]--> output: `s_rudolph_measure_rigidity`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_exhaustion_squeeze

---

### Host's theorem on normal numbers in base 2 and 3 (cite: https://en.wikipedia.org/wiki/Normal_number)

**Axioms:** `s_x2_invariant_ergodic_measure`
**Terminal:** `s_host_normal_numbers` (kind: theorem)

**Steps:**
1. input: `s_x2_invariant_ergodic_measure` --[t_auxiliary_construction {object: "Fourier-analytic correlation along ×3 orbit"}]--> output: `s_x3_orbit_fourier_correlation`
2. input: `s_x3_orbit_fourier_correlation` --[t_fourier_transform {space: "ℓ²(T) characters"}]--> output: `s_decay_of_dual_iterates`
3. input: `s_decay_of_dual_iterates` --[t_exhaustion_squeeze {pointwise: "×3 orbits equidistribute μ-a.e."}]--> output: `s_host_normal_numbers`

**Techniques used:** t_auxiliary_construction, t_fourier_transform, t_exhaustion_squeeze

---

### Mahler compactness criterion (cite: https://en.wikipedia.org/wiki/Mahler%27s_compactness_theorem)

**Axioms:** `s_space_of_unimodular_lattices_SL_n_R_over_SL_n_Z`
**Terminal:** `s_mahler_compactness_criterion` (kind: theorem)

**Steps:**
1. input: `s_space_of_unimodular_lattices_SL_n_R_over_SL_n_Z` --[t_auxiliary_construction {object: "shortest vector function λ_1(Λ)"}]--> output: `s_shortest_vector_function`
2. input: `s_shortest_vector_function` --[t_compactness_argument {bound: "λ_1 ≥ ε defines compact set"}]--> output: `s_compact_subset_via_lambda1_bound`
3. input: `s_compact_subset_via_lambda1_bound` --[t_duality {pair: "geometry of numbers ↔ homogeneous space"}]--> output: `s_mahler_compactness_criterion`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_duality

---

### Dani correspondence for Diophantine approximation (cite: https://en.wikipedia.org/wiki/Diophantine_approximation#Dani_correspondence)

**Axioms:** `s_irrational_vector_alpha_in_R_n`
**Terminal:** `s_dani_correspondence` (kind: theorem)

**Steps:**
1. input: `s_irrational_vector_alpha_in_R_n` --[t_auxiliary_construction {object: "unimodular lattice u_α ℤ^{n+1}"}]--> output: `s_lattice_associated_to_alpha`
2. input: `s_lattice_associated_to_alpha` --[t_structural_isomorphism {target: "diagonal flow a_t on SL_{n+1}/SL_{n+1}(ℤ)"}]--> output: `s_diagonal_flow_orbit`
3. input: `s_diagonal_flow_orbit` --[t_ergodic_correspondence {device: "well-approximability ↔ orbit excursions"}]--> output: `s_dani_correspondence`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_ergodic_correspondence

---

### Oppenheim conjecture (Margulis) (cite: https://en.wikipedia.org/wiki/Oppenheim_conjecture)

**Axioms:** `s_indefinite_irrational_quadratic_form_Q_in_n_at_least_3`
**Terminal:** `s_oppenheim_conjecture` (kind: theorem)

**Steps:**
1. input: `s_indefinite_irrational_quadratic_form_Q_in_n_at_least_3` --[t_auxiliary_construction {object: "stabilizer H = SO(Q) acting on SL_n(ℝ)/SL_n(ℤ)"}]--> output: `s_SO_Q_orbit_in_homogeneous_space`
2. input: `s_SO_Q_orbit_in_homogeneous_space` --[t_structural_isomorphism {input: "Ratner orbit closure ⇒ dense or closed"}]--> output: `s_orbit_dense_in_full_space`
3. input: `s_orbit_dense_in_full_space` --[t_exhaustion_squeeze {density: "Q(ℤ^n) dense in ℝ"}]--> output: `s_oppenheim_conjecture`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_exhaustion_squeeze

---

### Linnik's equidistribution of integer points on spheres (cite: https://en.wikipedia.org/wiki/Linnik%27s_theorem)

**Axioms:** `s_integer_points_on_sphere_x2_plus_y2_plus_z2_equals_N`
**Terminal:** `s_linnik_equidistribution_spheres` (kind: theorem)

**Steps:**
1. input: `s_integer_points_on_sphere_x2_plus_y2_plus_z2_equals_N` --[t_auxiliary_construction {object: "Hecke orbit on adelic SO(3)-quotient"}]--> output: `s_hecke_orbit_on_homogeneous_space`
2. input: `s_hecke_orbit_on_homogeneous_space` --[t_ergodic_correspondence {device: "torus action on SL_2(ℝ)-bundle"}]--> output: `s_torus_orbit_equidistribution`
3. input: `s_torus_orbit_equidistribution` --[t_exhaustion_squeeze {limit: "N → ∞ along admissible class"}]--> output: `s_linnik_equidistribution_spheres`

**Techniques used:** t_auxiliary_construction, t_ergodic_correspondence, t_exhaustion_squeeze

---

### Selberg trace formula (cite: https://en.wikipedia.org/wiki/Selberg_trace_formula)

**Axioms:** `s_compact_hyperbolic_surface_Gamma_minus_H2`
**Terminal:** `s_selberg_trace_formula` (kind: theorem)

(overlap: number theory)

**Steps:**
1. input: `s_compact_hyperbolic_surface_Gamma_minus_H2` --[t_auxiliary_construction {object: "convolution operator T_h on L^2(Γ\ℍ)"}]--> output: `s_convolution_kernel_operator`
2. input: `s_convolution_kernel_operator` --[t_svd_and_spectral_decomposition {decomposition: "spectral side ∑ h(t_n)"}]--> output: `s_spectral_side_of_trace`
3. input: `s_convolution_kernel_operator` --[t_character_decomposition_count {decomposition: "geometric side, sum over conjugacy classes"}]--> output: `s_geometric_side_of_trace`
4. input: `⟨s_spectral_side_of_trace, s_geometric_side_of_trace⟩` --[t_duality {pair: "spectral ↔ geometric"}]--> output: `s_selberg_trace_formula`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_character_decomposition_count, t_duality

---

### Lindenstrauss arithmetic quantum unique ergodicity (cite: https://en.wikipedia.org/wiki/Quantum_ergodicity)

**Axioms:** `s_hecke_eigenfunctions_on_arithmetic_surface`
**Terminal:** `s_lindenstrauss_quantum_unique_ergodicity` (kind: theorem)

**Steps:**
1. input: `s_hecke_eigenfunctions_on_arithmetic_surface` --[t_auxiliary_construction {object: "microlocal lift to T^1(Γ\ℍ)"}]--> output: `s_microlocal_lift_measure_mu_inf`
2. input: `s_microlocal_lift_measure_mu_inf` --[t_symmetry_reduction {invariance: "A-invariance + Hecke recurrence"}]--> output: `s_diagonal_plus_hecke_invariant_measure`
3. input: `s_diagonal_plus_hecke_invariant_measure` --[t_structural_isomorphism {input: "measure-rigidity à la Einsiedler–Katok–Lindenstrauss"}]--> output: `s_only_invariant_measure_is_haar`
4. input: `s_only_invariant_measure_is_haar` --[t_exhaustion_squeeze {limit: "eigenfunctions equidistribute"}]--> output: `s_lindenstrauss_quantum_unique_ergodicity`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_structural_isomorphism, t_exhaustion_squeeze

---

### Einsiedler–Katok–Lindenstrauss theorem on Littlewood (partial) (cite: https://en.wikipedia.org/wiki/Littlewood_conjecture)

**Axioms:** `s_diagonal_action_on_SL_3_R_over_SL_3_Z`
**Terminal:** `s_ekl_littlewood_partial` (kind: theorem)

**Steps:**
1. input: `s_diagonal_action_on_SL_3_R_over_SL_3_Z` --[t_auxiliary_construction {object: "invariant ergodic measure under full diagonal A"}]--> output: `s_A_invariant_ergodic_measure`
2. input: `s_A_invariant_ergodic_measure` --[t_projection_to_subspace {entropy: "positive entropy condition"}]--> output: `s_positive_entropy_under_some_one_parameter_flow`
3. input: `s_positive_entropy_under_some_one_parameter_flow` --[t_structural_isomorphism {target: "Haar measure"}]--> output: `s_measure_classification`
4. input: `s_measure_classification` --[t_exhaustion_squeeze {set: "Hausdorff-zero counterexample set to Littlewood"}]--> output: `s_ekl_littlewood_partial`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_structural_isomorphism, t_exhaustion_squeeze

---

## VI. Linear ODE / linearization theorems

### Lyapunov–Poincaré linearization theorem (cite: https://en.wikipedia.org/wiki/Linearization)

**Axioms:** `s_analytic_vector_field_with_hyperbolic_singular_point`
**Terminal:** `s_poincare_linearization_theorem` (kind: theorem)

**Steps:**
1. input: `s_analytic_vector_field_with_hyperbolic_singular_point` --[t_auxiliary_construction {object: "formal power-series conjugacy series"}]--> output: `s_formal_conjugacy_series_h_z`
2. input: `s_formal_conjugacy_series_h_z` --[t_reduce_to_canonical_form {target: "Jordan / spectral non-resonance"}]--> output: `s_non_resonance_condition_on_eigenvalues`
3. input: `s_non_resonance_condition_on_eigenvalues` --[t_contraction_fixed_point {space: "Banach space of analytic germs"}]--> output: `s_poincare_linearization_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_contraction_fixed_point

---

### Siegel linearization theorem for irrational rotation numbers (cite: https://en.wikipedia.org/wiki/Siegel_disc)

**Axioms:** `s_holomorphic_germ_with_diophantine_rotation_number`
**Terminal:** `s_siegel_linearization` (kind: theorem)

**Steps:**
1. input: `s_holomorphic_germ_with_diophantine_rotation_number` --[t_auxiliary_construction {object: "Newton-scheme conjugacy h_n"}]--> output: `s_newton_iteration_of_conjugacies`
2. input: `s_newton_iteration_of_conjugacies` --[t_reduce_to_canonical_form {tool: "Diophantine small-divisor estimate"}]--> output: `s_small_divisor_bound`
3. input: `s_small_divisor_bound` --[t_contraction_fixed_point {space: "shrinking annular domains"}]--> output: `s_siegel_linearization`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_contraction_fixed_point

---

### Floquet theorem for periodic linear ODE (cite: https://en.wikipedia.org/wiki/Floquet_theory)

**Axioms:** `s_linear_ode_with_t_periodic_coefficient_A_t`
**Terminal:** `s_floquet_theorem` (kind: theorem)

**Steps:**
1. input: `s_linear_ode_with_t_periodic_coefficient_A_t` --[t_auxiliary_construction {object: "monodromy matrix M = Φ(T)"}]--> output: `s_monodromy_matrix_M`
2. input: `s_monodromy_matrix_M` --[t_svd_and_spectral_decomposition {tool: "complex matrix logarithm log M = TB"}]--> output: `s_floquet_exponent_matrix_B`
3. input: `s_floquet_exponent_matrix_B` --[t_structural_isomorphism {factorization: "Φ(t) = P(t)e^{tB}, P periodic"}]--> output: `s_floquet_theorem`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_structural_isomorphism

---

### Lyapunov stability theorem (cite: https://en.wikipedia.org/wiki/Lyapunov_stability)

**Axioms:** `s_ode_with_equilibrium_x_star`, `s_lyapunov_function_V`
**Terminal:** `s_lyapunov_stability_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_ode_with_equilibrium_x_star, s_lyapunov_function_V⟩` --[t_conserved_quantity {quantity: "V positive-definite, dV/dt ≤ 0"}]--> output: `s_lyapunov_function_decreasing`
2. input: `s_lyapunov_function_decreasing` --[t_compactness_argument {space: "level sets {V ≤ c} compact"}]--> output: `s_trapped_in_level_set`
3. input: `s_trapped_in_level_set` --[t_exhaustion_squeeze {conclusion: "x(t) → x* (if dV/dt < 0)"}]--> output: `s_lyapunov_stability_theorem`

**Techniques used:** t_conserved_quantity, t_compactness_argument, t_exhaustion_squeeze

---

### Hartman's theorem on smoothness of conjugacies (cite: https://en.wikipedia.org/wiki/Sternberg%27s_theorem)

**Axioms:** `s_smooth_vector_field_with_nonresonant_hyperbolic_point`
**Terminal:** `s_sternberg_linearization` (kind: theorem)

**Steps:**
1. input: `s_smooth_vector_field_with_nonresonant_hyperbolic_point` --[t_auxiliary_construction {object: "k-jet conjugacy at the singular point"}]--> output: `s_normal_form_at_jet_k`
2. input: `s_normal_form_at_jet_k` --[t_reduce_to_canonical_form {tool: "iterated Sternberg normal-form moves"}]--> output: `s_sternberg_normal_form`
3. input: `s_sternberg_normal_form` --[t_contraction_fixed_point {space: "C^k bounded perturbations"}]--> output: `s_sternberg_linearization`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_contraction_fixed_point

---

### Center manifold theorem (cite: https://en.wikipedia.org/wiki/Center_manifold)

**Axioms:** `s_smooth_vector_field_with_partially_hyperbolic_fixed_point`
**Terminal:** `s_center_manifold_theorem` (kind: theorem)

**Steps:**
1. input: `s_smooth_vector_field_with_partially_hyperbolic_fixed_point` --[t_auxiliary_construction {object: "graph transform on center subspace sections"}]--> output: `s_graph_transform_on_center`
2. input: `s_graph_transform_on_center` --[t_contraction_fixed_point {space: "C^r bounded Lipschitz graphs"}]--> output: `s_invariant_center_graph`
3. input: `s_invariant_center_graph` --[t_exhaustion_squeeze {regularity: "C^r smoothness, possibly non-unique"}]--> output: `s_center_manifold_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Poincaré–Bendixson theorem (cite: https://en.wikipedia.org/wiki/Poincar%C3%A9%E2%80%93Bendixson_theorem)

**Axioms:** `s_smooth_planar_vector_field`, `s_positively_invariant_compact_region`
**Terminal:** `s_poincare_bendixson_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_smooth_planar_vector_field, s_positively_invariant_compact_region⟩` --[t_auxiliary_construction {object: "ω-limit set ω(x)"}]--> output: `s_omega_limit_set_in_plane`
2. input: `s_omega_limit_set_in_plane` --[t_compactness_argument {tool: "Jordan curve / transverse section"}]--> output: `s_monotone_intersection_with_section`
3. input: `s_monotone_intersection_with_section` --[t_exhaustion_squeeze {dichotomy: "equilibrium or closed orbit or graphic"}]--> output: `s_poincare_bendixson_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Peixoto's theorem on structural stability in dimension 2 (cite: https://en.wikipedia.org/wiki/Peixoto%27s_theorem)

**Axioms:** `s_smooth_vector_field_on_compact_2_manifold`
**Terminal:** `s_peixoto_structural_stability` (kind: theorem)

**Steps:**
1. input: `s_smooth_vector_field_on_compact_2_manifold` --[t_auxiliary_construction {object: "Morse–Smale condition: finite hyperbolic singularities + closed orbits, transverse intersections"}]--> output: `s_morse_smale_condition`
2. input: `s_morse_smale_condition` --[t_compactness_argument {space: "C^1 vector fields on M"}]--> output: `s_structural_stability_for_morse_smale`
3. input: `s_structural_stability_for_morse_smale` --[t_exhaustion_squeeze {density: "Morse–Smale is open & dense"}]--> output: `s_peixoto_structural_stability`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

## VII. KAM, Aubry–Mather, twist maps

### Kolmogorov–Arnold–Moser (KAM) theorem (cite: https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Arnold%E2%80%93Moser_theorem)

**Axioms:** `s_integrable_hamiltonian_with_diophantine_frequency`, `s_small_smooth_perturbation`
**Terminal:** `s_kam_theorem` (kind: theorem)

(overlap: PDE / classical mechanics)

**Steps:**
1. input: `⟨s_integrable_hamiltonian_with_diophantine_frequency, s_small_smooth_perturbation⟩` --[t_auxiliary_construction {object: "Newton-iteration sequence of canonical changes of variables"}]--> output: `s_newton_iteration_of_canonical_transforms`
2. input: `s_newton_iteration_of_canonical_transforms` --[t_reduce_to_canonical_form {bound: "Diophantine small-divisor estimate"}]--> output: `s_diophantine_small_divisor_control`
3. input: `s_diophantine_small_divisor_control` --[t_contraction_fixed_point {space: "analytic shrinking domains"}]--> output: `s_persistent_invariant_torus`
4. input: `s_persistent_invariant_torus` --[t_exhaustion_squeeze {measure: "positive-measure set of preserved tori"}]--> output: `s_kam_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Aubry–Mather theory (cite: https://en.wikipedia.org/wiki/Aubry%E2%80%93Mather_theory)

**Axioms:** `s_monotone_twist_map_of_annulus`
**Terminal:** `s_aubry_mather_theorem` (kind: theorem)

**Steps:**
1. input: `s_monotone_twist_map_of_annulus` --[t_auxiliary_construction {object: "action functional on configurations of rotation number ω"}]--> output: `s_action_minimizing_configurations`
2. input: `s_action_minimizing_configurations` --[t_compactness_argument {space: "minimizers along ω"}]--> output: `s_minimizing_set_M_omega`
3. input: `s_minimizing_set_M_omega` --[t_exhaustion_squeeze {classification: "M_ω = invariant circle or Cantorus"}]--> output: `s_aubry_mather_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Mather's variational principle for connecting orbits (cite: https://en.wikipedia.org/wiki/Aubry%E2%80%93Mather_theory)

**Axioms:** `s_tonelli_lagrangian_on_T_M`
**Terminal:** `s_mather_connecting_orbits` (kind: theorem)

**Steps:**
1. input: `s_tonelli_lagrangian_on_T_M` --[t_auxiliary_construction {object: "Mather alpha and beta functions"}]--> output: `s_alpha_beta_function_pair`
2. input: `s_alpha_beta_function_pair` --[t_duality {pair: "Legendre / Fenchel duality"}]--> output: `s_dual_pair_alpha_beta`
3. input: `s_dual_pair_alpha_beta` --[t_exhaustion_squeeze {existence: "minimizers in given cohomology class"}]--> output: `s_mather_connecting_orbits`

**Techniques used:** t_auxiliary_construction, t_duality, t_exhaustion_squeeze

---

### Denjoy's theorem on circle diffeomorphisms (cite: https://en.wikipedia.org/wiki/Denjoy%27s_theorem_on_the_circle)

**Axioms:** `s_C2_circle_diffeomorphism_with_irrational_rotation_number`
**Terminal:** `s_denjoy_theorem` (kind: theorem)

**Steps:**
1. input: `s_C2_circle_diffeomorphism_with_irrational_rotation_number` --[t_auxiliary_construction {object: "Denjoy distortion control via bounded variation of log f'"}]--> output: `s_distortion_control_via_BV_log_derivative`
2. input: `s_distortion_control_via_BV_log_derivative` --[t_compactness_argument {space: "Schwarzian intervals"}]--> output: `s_no_wandering_intervals`
3. input: `s_no_wandering_intervals` --[t_structural_isomorphism {target: "topological conjugacy to rotation by ω"}]--> output: `s_denjoy_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_structural_isomorphism

---

### Herman's theorem on smooth conjugacy of circle diffeomorphisms (cite: https://en.wikipedia.org/wiki/Michel_Herman)

**Axioms:** `s_smooth_circle_diffeomorphism_with_diophantine_rotation_number`
**Terminal:** `s_herman_smooth_conjugacy` (kind: theorem)

**Steps:**
1. input: `s_smooth_circle_diffeomorphism_with_diophantine_rotation_number` --[t_auxiliary_construction {object: "renormalization scheme on the circle"}]--> output: `s_herman_renormalization_scheme`
2. input: `s_herman_renormalization_scheme` --[t_reduce_to_canonical_form {tool: "Diophantine small-divisor control"}]--> output: `s_small_divisor_estimate_circle_case`
3. input: `s_small_divisor_estimate_circle_case` --[t_contraction_fixed_point {space: "smooth conjugacy iteration"}]--> output: `s_herman_smooth_conjugacy`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_contraction_fixed_point

---

## VIII. Billiards and continuous-time chaos

### Sinai dispersing billiards ergodicity (cite: https://en.wikipedia.org/wiki/Dynamical_billiards#Sinai_billiards)

**Axioms:** `s_sinai_billiard_table_with_dispersing_walls`
**Terminal:** `s_sinai_billiard_ergodicity` (kind: theorem)

**Steps:**
1. input: `s_sinai_billiard_table_with_dispersing_walls` --[t_auxiliary_construction {object: "stable/unstable cone fields"}]--> output: `s_invariant_cone_fields_for_billiard_map`
2. input: `s_invariant_cone_fields_for_billiard_map` --[t_structural_isomorphism {target: "non-uniformly hyperbolic system with singularities"}]--> output: `s_pesin_theory_for_billiards`
3. input: `s_pesin_theory_for_billiards` --[t_exhaustion_squeeze {conclusion: "ergodicity, K-property"}]--> output: `s_sinai_billiard_ergodicity`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_exhaustion_squeeze

---

### Bunimovich stadium ergodicity (cite: https://en.wikipedia.org/wiki/Bunimovich_stadium)

**Axioms:** `s_bunimovich_stadium_table`
**Terminal:** `s_bunimovich_stadium_ergodicity` (kind: theorem)

**Steps:**
1. input: `s_bunimovich_stadium_table` --[t_auxiliary_construction {object: "defocusing mechanism on focusing arcs"}]--> output: `s_defocusing_property_on_arcs`
2. input: `s_defocusing_property_on_arcs` --[t_structural_isomorphism {target: "cone-field hyperbolicity even with focusing walls"}]--> output: `s_hyperbolicity_for_stadium`
3. input: `s_hyperbolicity_for_stadium` --[t_exhaustion_squeeze {conclusion: "ergodicity & K-mixing"}]--> output: `s_bunimovich_stadium_ergodicity`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_exhaustion_squeeze

---

### Bunimovich–Spohn–Boldrighini Boltzmann-Grad limit (cite: https://en.wikipedia.org/wiki/Boltzmann_equation)

**Axioms:** `s_finitely_many_hard_disks_in_box`
**Terminal:** `s_boltzmann_grad_limit_chaos` (kind: theorem)

**Steps:**
1. input: `s_finitely_many_hard_disks_in_box` --[t_auxiliary_construction {object: "BBGKY hierarchy of marginals"}]--> output: `s_bbgky_hierarchy`
2. input: `s_bbgky_hierarchy` --[t_rescale_for_asymptotic_geometry {limit: "Boltzmann–Grad scaling Nd² → 1"}]--> output: `s_boltzmann_grad_scaling_limit`
3. input: `s_boltzmann_grad_scaling_limit` --[t_exhaustion_squeeze {propagation: "molecular chaos preserved"}]--> output: `s_boltzmann_grad_limit_chaos`

**Techniques used:** t_auxiliary_construction, t_rescale_for_asymptotic_geometry, t_exhaustion_squeeze

---

### Veech dichotomy for translation surfaces (cite: https://en.wikipedia.org/wiki/Veech_surface)

**Axioms:** `s_veech_translation_surface`
**Terminal:** `s_veech_dichotomy` (kind: theorem)

**Steps:**
1. input: `s_veech_translation_surface` --[t_auxiliary_construction {object: "Teichmüller orbit of the surface"}]--> output: `s_teichmuller_geodesic`
2. input: `s_teichmuller_geodesic` --[t_compactness_argument {set: "closed SL_2(ℝ) orbit"}]--> output: `s_closed_sl2_orbit_in_strata`
3. input: `s_closed_sl2_orbit_in_strata` --[t_exhaustion_squeeze {dichotomy: "direction is uniquely ergodic OR completely periodic"}]--> output: `s_veech_dichotomy`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Masur–Veech ergodicity of Teichmüller flow on moduli of abelian differentials (cite: https://en.wikipedia.org/wiki/Teichm%C3%BCller_space#Teichm%C3%BCller_flow)

**Axioms:** `s_stratum_of_abelian_differentials`
**Terminal:** `s_masur_veech_ergodicity` (kind: theorem)

**Steps:**
1. input: `s_stratum_of_abelian_differentials` --[t_auxiliary_construction {object: "Masur–Veech smooth measure on stratum"}]--> output: `s_masur_veech_measure`
2. input: `s_masur_veech_measure` --[t_compactness_argument {tool: "finite total mass after period normalization"}]--> output: `s_finite_volume_normalization`
3. input: `s_finite_volume_normalization` --[t_exhaustion_squeeze {conclusion: "Teichmüller flow ergodic, mixing"}]--> output: `s_masur_veech_ergodicity`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

## IX. Bifurcations, Morse–Conley, and Avila/Damanik

### Morse–Conley index theorem (cite: https://en.wikipedia.org/wiki/Conley_index_theory)

**Axioms:** `s_continuous_dynamical_system_on_locally_compact_space`, `s_isolated_invariant_set_S`
**Terminal:** `s_conley_index_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_dynamical_system_on_locally_compact_space, s_isolated_invariant_set_S⟩` --[t_auxiliary_construction {object: "index pair (N, L) for S"}]--> output: `s_conley_index_pair`
2. input: `s_conley_index_pair` --[t_obstruction_class {invariant: "homotopy type [N/L]"}]--> output: `s_conley_index_class_h_S`
3. input: `s_conley_index_class_h_S` --[t_exhaustion_squeeze {invariance: "homotopy invariance under continuation"}]--> output: `s_conley_index_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_exhaustion_squeeze

---

### Morse inequalities (Smale gradient version) (cite: https://en.wikipedia.org/wiki/Morse_theory)

**Axioms:** `s_morse_smale_gradient_flow_on_compact_manifold`
**Terminal:** `s_morse_inequalities` (kind: theorem)

**Steps:**
1. input: `s_morse_smale_gradient_flow_on_compact_manifold` --[t_auxiliary_construction {object: "Morse–Smale chain complex over critical points"}]--> output: `s_morse_chain_complex`
2. input: `s_morse_chain_complex` --[t_obstruction_class {invariant: "Morse homology = singular homology"}]--> output: `s_morse_homology_equals_h_star`
3. input: `s_morse_homology_equals_h_star` --[t_exhaustion_squeeze {inequality: "# critical points of index k ≥ b_k"}]--> output: `s_morse_inequalities`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_exhaustion_squeeze

---

### Andronov–Hopf bifurcation theorem (cite: https://en.wikipedia.org/wiki/Hopf_bifurcation)

**Axioms:** `s_one_parameter_family_of_vector_fields_with_pair_of_eigenvalues_crossing_imaginary_axis`
**Terminal:** `s_hopf_bifurcation_theorem` (kind: theorem)

**Steps:**
1. input: `s_one_parameter_family_of_vector_fields_with_pair_of_eigenvalues_crossing_imaginary_axis` --[t_reduce_to_canonical_form {target: "Poincaré normal form, polar coords"}]--> output: `s_normal_form_for_hopf`
2. input: `s_normal_form_for_hopf` --[t_auxiliary_construction {object: "Lyapunov coefficient l_1"}]--> output: `s_first_lyapunov_coefficient`
3. input: `s_first_lyapunov_coefficient` --[t_exhaustion_squeeze {bifurcation: "limit cycle of radius ∝ √μ"}]--> output: `s_hopf_bifurcation_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_exhaustion_squeeze

---

### Saddle-node (fold) bifurcation theorem (cite: https://en.wikipedia.org/wiki/Saddle-node_bifurcation)

**Axioms:** `s_one_parameter_family_with_zero_eigenvalue_at_mu_zero`
**Terminal:** `s_saddle_node_bifurcation` (kind: theorem)

**Steps:**
1. input: `s_one_parameter_family_with_zero_eigenvalue_at_mu_zero` --[t_reduce_to_canonical_form {target: "normal form x' = μ - x²"}]--> output: `s_saddle_node_normal_form`
2. input: `s_saddle_node_normal_form` --[t_auxiliary_construction {object: "implicit function for equilibrium curve"}]--> output: `s_equilibrium_curve_in_mu_x_plane`
3. input: `s_equilibrium_curve_in_mu_x_plane` --[t_exhaustion_squeeze {birth: "two equilibria collide and disappear"}]--> output: `s_saddle_node_bifurcation`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_exhaustion_squeeze

---

### Period-doubling cascade (Feigenbaum universality) (cite: https://en.wikipedia.org/wiki/Feigenbaum_constants)

**Axioms:** `s_unimodal_family_of_interval_maps`
**Terminal:** `s_feigenbaum_universality` (kind: theorem)

**Steps:**
1. input: `s_unimodal_family_of_interval_maps` --[t_auxiliary_construction {object: "renormalization operator R on space of unimodal maps"}]--> output: `s_renormalization_operator_R`
2. input: `s_renormalization_operator_R` --[t_contraction_fixed_point {fixed_point: "Feigenbaum fixed point g*"}]--> output: `s_feigenbaum_fixed_point_g_star`
3. input: `s_feigenbaum_fixed_point_g_star` --[t_svd_and_spectral_decomposition {spectrum: "expansion eigenvalue δ"}]--> output: `s_feigenbaum_constant_delta`
4. input: `s_feigenbaum_constant_delta` --[t_exhaustion_squeeze {universality: "limit ratios are δ for all C^k unimodal"}]--> output: `s_feigenbaum_universality`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_svd_and_spectral_decomposition, t_exhaustion_squeeze

---

### Avila's reducibility theorem for quasi-periodic cocycles (cite: https://en.wikipedia.org/wiki/Quasiperiodic_motion)

**Axioms:** `s_quasi_periodic_SL_2_R_cocycle_with_diophantine_frequency`
**Terminal:** `s_avila_reducibility` (kind: theorem)

**Steps:**
1. input: `s_quasi_periodic_SL_2_R_cocycle_with_diophantine_frequency` --[t_auxiliary_construction {object: "renormalization of cocycle"}]--> output: `s_cocycle_renormalization_orbit`
2. input: `s_cocycle_renormalization_orbit` --[t_reduce_to_canonical_form {target: "KAM-type small-divisor scheme"}]--> output: `s_small_divisor_estimate_for_cocycle`
3. input: `s_small_divisor_estimate_for_cocycle` --[t_contraction_fixed_point {space: "analytic cocycle perturbations"}]--> output: `s_avila_reducibility`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_contraction_fixed_point

---

### Avila–Damanik almost Mathieu spectrum (Ten Martini Problem) (cite: https://en.wikipedia.org/wiki/Almost_Mathieu_operator)

**Axioms:** `s_almost_mathieu_operator_with_irrational_frequency`
**Terminal:** `s_ten_martini_theorem` (kind: theorem)

**Steps:**
1. input: `s_almost_mathieu_operator_with_irrational_frequency` --[t_auxiliary_construction {object: "Lyapunov exponent L(E) of transfer cocycle"}]--> output: `s_lyapunov_exponent_along_E`
2. input: `s_lyapunov_exponent_along_E` --[t_fourier_transform {operator: "Aubry duality H_λ ↔ H_{1/λ}"}]--> output: `s_aubry_dual_operator`
3. input: `s_aubry_dual_operator` --[t_exhaustion_squeeze {regime: "subcritical / critical / supercritical"}]--> output: `s_global_phase_picture_of_amo`
4. input: `s_global_phase_picture_of_amo` --[t_structural_isomorphism {conclusion: "spectrum is a Cantor set"}]--> output: `s_ten_martini_theorem`

**Techniques used:** t_auxiliary_construction, t_fourier_transform, t_exhaustion_squeeze, t_structural_isomorphism

---

### Avila–Krikorian renormalization theorem (cite: https://en.wikipedia.org/wiki/Schr%C3%B6dinger_operator)

**Axioms:** `s_schrodinger_cocycle_with_irrational_frequency`
**Terminal:** `s_avila_krikorian_theorem` (kind: theorem)

**Steps:**
1. input: `s_schrodinger_cocycle_with_irrational_frequency` --[t_auxiliary_construction {object: "renormalization fixed point analysis"}]--> output: `s_renormalization_fixed_point_for_cocycle`
2. input: `s_renormalization_fixed_point_for_cocycle` --[t_compactness_argument {set: "positive measure of energies"}]--> output: `s_positive_measure_of_regular_energies`
3. input: `s_positive_measure_of_regular_energies` --[t_exhaustion_squeeze {conclusion: "non-uniform hyperbolicity on positive-measure set"}]--> output: `s_avila_krikorian_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Avila global theory of one-frequency Schrödinger operators (cite: https://en.wikipedia.org/wiki/Schr%C3%B6dinger_operator)

**Axioms:** `s_one_frequency_quasi_periodic_schrodinger_operator`
**Terminal:** `s_avila_global_theory` (kind: theorem)

**Steps:**
1. input: `s_one_frequency_quasi_periodic_schrodinger_operator` --[t_auxiliary_construction {object: "complexified Lyapunov exponent ω(ε)"}]--> output: `s_complexified_lyapunov_function`
2. input: `s_complexified_lyapunov_function` --[t_fourier_transform {tool: "complex strip analyticity"}]--> output: `s_piecewise_linear_lyapunov_in_strip`
3. input: `s_piecewise_linear_lyapunov_in_strip` --[t_exhaustion_squeeze {classification: "subcritical / critical / supercritical phases"}]--> output: `s_avila_global_theory`

**Techniques used:** t_auxiliary_construction, t_fourier_transform, t_exhaustion_squeeze

---

## X. Miscellaneous classical and modern

### Birkhoff's theorem on transitive points (recurrence) (cite: https://en.wikipedia.org/wiki/Topological_dynamics)

**Axioms:** `s_continuous_self_map_of_compact_space`, `s_minimal_subsystem`
**Terminal:** `s_birkhoff_minimal_recurrence` (kind: theorem)

**Steps:**
1. input: `⟨s_continuous_self_map_of_compact_space, s_minimal_subsystem⟩` --[t_auxiliary_construction {object: "Zorn / minimal closed invariant subset"}]--> output: `s_minimal_invariant_subset_M`
2. input: `s_minimal_invariant_subset_M` --[t_compactness_argument {tool: "every point in M is uniformly recurrent"}]--> output: `s_uniform_recurrence_in_M`
3. input: `s_uniform_recurrence_in_M` --[t_exhaustion_squeeze {conclusion: "M contains uniformly recurrent points"}]--> output: `s_birkhoff_minimal_recurrence`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Weyl equidistribution theorem (cite: https://en.wikipedia.org/wiki/Equidistribution_theorem)

**Axioms:** `s_irrational_real_alpha`
**Terminal:** `s_weyl_equidistribution` (kind: theorem)

**Steps:**
1. input: `s_irrational_real_alpha` --[t_auxiliary_construction {object: "exponential sum (1/N)∑ e^{2πikn α}"}]--> output: `s_weyl_exponential_sum`
2. input: `s_weyl_exponential_sum` --[t_fourier_transform {test: "trigonometric polynomials are dense"}]--> output: `s_decay_of_exponential_sum`
3. input: `s_decay_of_exponential_sum` --[t_exhaustion_squeeze {density: "Riemann-integrable test functions"}]--> output: `s_weyl_equidistribution`

**Techniques used:** t_auxiliary_construction, t_fourier_transform, t_exhaustion_squeeze

---

### Furstenberg–Kesten theorem (Lyapunov exponents from cocycles) (cite: https://en.wikipedia.org/wiki/Lyapunov_exponent)

**Axioms:** `s_measure_preserving_transformation`, `s_log_integrable_matrix_cocycle`
**Terminal:** `s_furstenberg_kesten_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_preserving_transformation, s_log_integrable_matrix_cocycle⟩` --[t_auxiliary_construction {object: "subadditive sequence log ‖A_n(x)‖"}]--> output: `s_subadditive_log_norm`
2. input: `s_subadditive_log_norm` --[t_exhaustion_squeeze {tool: "Kingman subadditive ergodic"}]--> output: `s_pointwise_limit_lambda_top`
3. input: `s_pointwise_limit_lambda_top` --[t_compose_with_identity {wrap: "top Lyapunov exponent exists a.e."}]--> output: `s_furstenberg_kesten_theorem`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_compose_with_identity

---

### Glasner–Weiss strong proximality / structure theorem (cite: https://en.wikipedia.org/wiki/Topological_dynamics)

**Axioms:** `s_compact_metric_dynamical_system_with_group_action`
**Terminal:** `s_glasner_weiss_structure` (kind: theorem)

**Steps:**
1. input: `s_compact_metric_dynamical_system_with_group_action` --[t_auxiliary_construction {object: "proximal relation P(X,T)"}]--> output: `s_proximal_equivalence_relation`
2. input: `s_proximal_equivalence_relation` --[t_projection_to_subspace {target: "maximal equicontinuous factor"}]--> output: `s_maximal_equicontinuous_factor`
3. input: `s_maximal_equicontinuous_factor` --[t_exhaustion_squeeze {decomposition: "equicontinuous ⊕ weakly mixing pieces"}]--> output: `s_glasner_weiss_structure`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_exhaustion_squeeze

---

### Hindman's finite-sums theorem (cite: https://en.wikipedia.org/wiki/Hindman%27s_theorem)

**Axioms:** `s_finite_coloring_of_naturals`
**Terminal:** `s_hindman_finite_sums` (kind: theorem)

**Steps:**
1. input: `s_finite_coloring_of_naturals` --[t_auxiliary_construction {object: "Stone–Čech compactification βℕ with semigroup ops"}]--> output: `s_beta_n_compactification`
2. input: `s_beta_n_compactification` --[t_compactness_argument {tool: "minimal idempotent ultrafilter exists"}]--> output: `s_minimal_idempotent_p`
3. input: `s_minimal_idempotent_p` --[t_exhaustion_squeeze {extraction: "IP-set in one color class"}]--> output: `s_hindman_finite_sums`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Furstenberg's structure theorem for distal systems (cite: https://en.wikipedia.org/wiki/Distal_system)

**Axioms:** `s_minimal_distal_topological_dynamical_system`
**Terminal:** `s_furstenberg_distal_structure` (kind: theorem)

**Steps:**
1. input: `s_minimal_distal_topological_dynamical_system` --[t_auxiliary_construction {object: "tower of equicontinuous extensions"}]--> output: `s_equicontinuous_tower`
2. input: `s_equicontinuous_tower` --[t_projection_to_subspace {target: "transfinite tower of isometric extensions"}]--> output: `s_transfinite_isometric_tower`
3. input: `s_transfinite_isometric_tower` --[t_exhaustion_squeeze {limit: "exhausts X"}]--> output: `s_furstenberg_distal_structure`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_exhaustion_squeeze

---

### Bernoulli isomorphism theorem (Ornstein) (cite: https://en.wikipedia.org/wiki/Ornstein_isomorphism_theorem)

**Axioms:** `s_two_bernoulli_shifts_of_equal_entropy`
**Terminal:** `s_ornstein_isomorphism` (kind: theorem)

**Steps:**
1. input: `s_two_bernoulli_shifts_of_equal_entropy` --[t_auxiliary_construction {object: "very-weak-Bernoulli (VWB) tower decomposition"}]--> output: `s_vwb_tower_decomposition`
2. input: `s_vwb_tower_decomposition` --[t_structural_isomorphism {tool: "finitely determined property"}]--> output: `s_finitely_determined_invariant`
3. input: `s_finitely_determined_invariant` --[t_exhaustion_squeeze {conclusion: "measure-preserving isomorphism"}]--> output: `s_ornstein_isomorphism`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_exhaustion_squeeze

---

### Hopf ergodicity of geodesic flow on negative-curvature surfaces (cite: https://en.wikipedia.org/wiki/Anosov_flow)

**Axioms:** `s_compact_hyperbolic_surface_Gamma_minus_H2`
**Terminal:** `s_hopf_geodesic_flow_ergodicity` (kind: theorem)

**Steps:**
1. input: `s_compact_hyperbolic_surface_Gamma_minus_H2` --[t_auxiliary_construction {object: "stable/unstable horocycle foliations"}]--> output: `s_horocycle_foliations`
2. input: `s_horocycle_foliations` --[t_symmetry_reduction {tool: "Hopf argument along absolutely continuous foliations"}]--> output: `s_invariant_function_is_constant`
3. input: `s_invariant_function_is_constant` --[t_exhaustion_squeeze {conclusion: "geodesic flow is ergodic"}]--> output: `s_hopf_geodesic_flow_ergodicity`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_exhaustion_squeeze

---

### Smale's stable manifold theorem for non-uniformly hyperbolic systems (Pesin) (cite: https://en.wikipedia.org/wiki/Pesin_theory)

**Axioms:** `s_smooth_measure_preserving_diffeomorphism_with_nonzero_lyapunov_exponents`
**Terminal:** `s_pesin_stable_manifold_theorem` (kind: theorem)

**Steps:**
1. input: `s_smooth_measure_preserving_diffeomorphism_with_nonzero_lyapunov_exponents` --[t_auxiliary_construction {object: "Lyapunov chart, anisotropic norm"}]--> output: `s_anisotropic_lyapunov_chart`
2. input: `s_anisotropic_lyapunov_chart` --[t_contraction_fixed_point {space: "graph transform in adapted norm"}]--> output: `s_pesin_local_stable_graph`
3. input: `s_pesin_local_stable_graph` --[t_exhaustion_squeeze {global: "absolute continuity of stable foliation"}]--> output: `s_pesin_stable_manifold_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Hopf ratio ergodic theorem (cite: https://en.wikipedia.org/wiki/Ratio_ergodic_theorem)

**Axioms:** `s_measure_preserving_transformation`, `s_sigma_finite_measure_space`, `s_two_L1_functions_f_g`
**Terminal:** `s_hopf_ratio_ergodic` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_preserving_transformation, s_sigma_finite_measure_space, s_two_L1_functions_f_g⟩` --[t_auxiliary_construction {object: "ratio S_n f / S_n g"}]--> output: `s_birkhoff_ratio_sequence`
2. input: `s_birkhoff_ratio_sequence` --[t_compactness_argument {tool: "maximal inequality for ratios"}]--> output: `s_hopf_maximal_inequality`
3. input: `s_hopf_maximal_inequality` --[t_exhaustion_squeeze {limit: "almost-everywhere convergence"}]--> output: `s_hopf_ratio_ergodic`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Furstenberg–Zimmer structure theorem (cite: https://en.wikipedia.org/wiki/Furstenberg%E2%80%93Zimmer_structure_theorem)

**Axioms:** `s_ergodic_measure_preserving_system`
**Terminal:** `s_furstenberg_zimmer_structure` (kind: theorem)

**Steps:**
1. input: `s_ergodic_measure_preserving_system` --[t_auxiliary_construction {object: "characteristic factor / Hilbert module decomposition"}]--> output: `s_hilbert_module_decomposition`
2. input: `s_hilbert_module_decomposition` --[t_projection_to_subspace {target: "maximal compact-extensions tower"}]--> output: `s_tower_of_compact_extensions`
3. input: `s_tower_of_compact_extensions` --[t_exhaustion_squeeze {limit: "weak-mixing relative to base"}]--> output: `s_furstenberg_zimmer_structure`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_exhaustion_squeeze

---

### Host–Kra structure theorem (nilfactors) (cite: https://en.wikipedia.org/wiki/Nilsequence)

**Axioms:** `s_ergodic_measure_preserving_system`
**Terminal:** `s_host_kra_nilfactor_structure` (kind: theorem)

**Steps:**
1. input: `s_ergodic_measure_preserving_system` --[t_auxiliary_construction {object: "Gowers–Host–Kra seminorms ‖f‖_{U^k}"}]--> output: `s_uniformity_seminorms_U_k`
2. input: `s_uniformity_seminorms_U_k` --[t_projection_to_subspace {target: "characteristic factor Z_k"}]--> output: `s_nilfactor_Z_k`
3. input: `s_nilfactor_Z_k` --[t_structural_isomorphism {target: "k-step nilsystem"}]--> output: `s_host_kra_nilfactor_structure`

**Techniques used:** t_auxiliary_construction, t_projection_to_subspace, t_structural_isomorphism

---

### Tao–Ziegler equidistribution of nilsequences (cite: https://en.wikipedia.org/wiki/Nilsequence)

**Axioms:** `s_polynomial_nilorbit_in_nilmanifold_G_over_Gamma`
**Terminal:** `s_tao_ziegler_nilequidistribution` (kind: theorem)

**Steps:**
1. input: `s_polynomial_nilorbit_in_nilmanifold_G_over_Gamma` --[t_auxiliary_construction {object: "factorization theorem: smooth + equidistributed + rational"}]--> output: `s_green_tao_factorization`
2. input: `s_green_tao_factorization` --[t_compactness_argument {tool: "iterate descent into subnilmanifold"}]--> output: `s_subnilmanifold_descent_step`
3. input: `s_subnilmanifold_descent_step` --[t_exhaustion_squeeze {limit: "equidistribution on the subnil"}]--> output: `s_tao_ziegler_nilequidistribution`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Stable ergodicity of partially hyperbolic systems (Pugh–Shub) (cite: https://en.wikipedia.org/wiki/Partially_hyperbolic_diffeomorphism)

**Axioms:** `s_partially_hyperbolic_diffeomorphism_with_accessible_center`
**Terminal:** `s_pugh_shub_stable_ergodicity` (kind: theorem)

**Steps:**
1. input: `s_partially_hyperbolic_diffeomorphism_with_accessible_center` --[t_auxiliary_construction {object: "accessibility classes via su-paths"}]--> output: `s_accessibility_class_decomposition`
2. input: `s_accessibility_class_decomposition` --[t_symmetry_reduction {tool: "Hopf-type argument on accessibility"}]--> output: `s_invariant_functions_constant_on_classes`
3. input: `s_invariant_functions_constant_on_classes` --[t_exhaustion_squeeze {robustness: "C^r-open property"}]--> output: `s_pugh_shub_stable_ergodicity`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_exhaustion_squeeze

---

### Brin–Katok local entropy formula (cite: https://en.wikipedia.org/wiki/Topological_entropy#Brin%E2%80%93Katok)

**Axioms:** `s_measure_preserving_homeomorphism_of_compact_metric_space`
**Terminal:** `s_brin_katok_local_entropy` (kind: theorem)

**Steps:**
1. input: `s_measure_preserving_homeomorphism_of_compact_metric_space` --[t_auxiliary_construction {object: "Bowen ball B_n(x,ε)"}]--> output: `s_bowen_ball_measure_decay`
2. input: `s_bowen_ball_measure_decay` --[t_exhaustion_squeeze {limit: "h(x,ε) := -lim (1/n) log μ(B_n(x,ε))"}]--> output: `s_pointwise_entropy_function`
3. input: `s_pointwise_entropy_function` --[t_projection_to_subspace {target: "ergodic decomposition"}]--> output: `s_brin_katok_local_entropy`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_projection_to_subspace

---

### Bowen 1979 dimension formula (Hausdorff dim of limit sets of Kleinian groups) (cite: https://en.wikipedia.org/wiki/Limit_set#Bowen's_formula)

**Axioms:** `s_convex_cocompact_kleinian_group_Gamma`
**Terminal:** `s_bowen_limit_set_dimension` (kind: theorem)

**Steps:**
1. input: `s_convex_cocompact_kleinian_group_Gamma` --[t_auxiliary_construction {object: "Poincaré series ∑ e^{-s d(0, γ 0)}"}]--> output: `s_poincare_series_critical_exponent_delta`
2. input: `s_poincare_series_critical_exponent_delta` --[t_contraction_fixed_point {fixed_point: "transfer-operator eigenvalue at s = δ"}]--> output: `s_transfer_operator_fixed_point`
3. input: `s_transfer_operator_fixed_point` --[t_exhaustion_squeeze {identity: "dim_H(Λ_Γ) = δ"}]--> output: `s_bowen_limit_set_dimension`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Sarnak's Möbius randomness in horocycle flows (cite: https://en.wikipedia.org/wiki/M%C3%B6bius_function#Sarnak's_conjecture)

**Axioms:** `s_unipotent_horocycle_flow_on_modular_surface`
**Terminal:** `s_sarnak_mobius_horocycle` (kind: theorem)

**Steps:**
1. input: `s_unipotent_horocycle_flow_on_modular_surface` --[t_auxiliary_construction {object: "Möbius-weighted Birkhoff average ∑ μ(n) F(h_n x)"}]--> output: `s_mobius_weighted_average`
2. input: `s_mobius_weighted_average` --[t_ergodic_correspondence {device: "disjointness from Möbius / Sarnak conjecture instance"}]--> output: `s_disjointness_with_mobius`
3. input: `s_disjointness_with_mobius` --[t_exhaustion_squeeze {limit: "average → 0"}]--> output: `s_sarnak_mobius_horocycle`

**Techniques used:** t_auxiliary_construction, t_ergodic_correspondence, t_exhaustion_squeeze

---

### Buzzi–Pollicott–Sarig classification of measures for surface diffeomorphisms (cite: https://en.wikipedia.org/wiki/Sarig)

**Axioms:** `s_C_inf_surface_diffeomorphism_with_positive_topological_entropy`
**Terminal:** `s_sarig_symbolic_extension` (kind: theorem)

**Steps:**
1. input: `s_C_inf_surface_diffeomorphism_with_positive_topological_entropy` --[t_auxiliary_construction {object: "countable Markov partition"}]--> output: `s_countable_markov_partition`
2. input: `s_countable_markov_partition` --[t_structural_isomorphism {target: "countable-state SFT extension"}]--> output: `s_countable_sft_extension`
3. input: `s_countable_sft_extension` --[t_exhaustion_squeeze {classification: "ergodic measures of maximal entropy, finite in number"}]--> output: `s_sarig_symbolic_extension`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_exhaustion_squeeze

---

### Eskin–Mirzakhani–Mohammadi rigidity for SL(2,ℝ) action on moduli space (cite: https://en.wikipedia.org/wiki/Maryam_Mirzakhani)

**Axioms:** `s_stratum_of_translation_surfaces_with_SL2R_action`
**Terminal:** `s_eskin_mirzakhani_mohammadi` (kind: theorem)

**Steps:**
1. input: `s_stratum_of_translation_surfaces_with_SL2R_action` --[t_auxiliary_construction {object: "P-invariant ergodic measure (P = upper triangular)"}]--> output: `s_P_invariant_ergodic_measure`
2. input: `s_P_invariant_ergodic_measure` --[t_symmetry_reduction {tool: "extra invariance along expanding horocycle"}]--> output: `s_full_SL2R_invariance`
3. input: `s_full_SL2R_invariance` --[t_structural_isomorphism {target: "affine invariant submanifold"}]--> output: `s_affine_invariant_submanifold_closure`
4. input: `s_affine_invariant_submanifold_closure` --[t_exhaustion_squeeze {classification: "all orbit closures are affine"}]--> output: `s_eskin_mirzakhani_mohammadi`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_structural_isomorphism, t_exhaustion_squeeze

---

### McMullen's renormalization theorem for complex dynamics (cite: https://en.wikipedia.org/wiki/Renormalization)

**Axioms:** `s_infinitely_renormalizable_quadratic_with_bounded_combinatorics`
**Terminal:** `s_mcmullen_renormalization` (kind: theorem)

**Steps:**
1. input: `s_infinitely_renormalizable_quadratic_with_bounded_combinatorics` --[t_auxiliary_construction {object: "renormalization operator R on polynomial-like germs"}]--> output: `s_renormalization_operator_on_germs`
2. input: `s_renormalization_operator_on_germs` --[t_contraction_fixed_point {space: "Banach space of holomorphic germs"}]--> output: `s_renormalization_fixed_point_or_attractor`
3. input: `s_renormalization_fixed_point_or_attractor` --[t_exhaustion_squeeze {bound: "a-priori bounds + exponential contraction"}]--> output: `s_mcmullen_renormalization`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Sullivan's classification of conformal expanding repellers (cite: https://en.wikipedia.org/wiki/Hyperbolic_set)

**Axioms:** `s_conformal_expanding_repeller_in_complex_plane`
**Terminal:** `s_sullivan_conformal_expanding_classification` (kind: theorem)

**Steps:**
1. input: `s_conformal_expanding_repeller_in_complex_plane` --[t_auxiliary_construction {object: "Sullivan's conformal measure of dimension δ"}]--> output: `s_sullivan_conformal_measure`
2. input: `s_sullivan_conformal_measure` --[t_contraction_fixed_point {operator: "transfer operator at δ"}]--> output: `s_unique_eigenmeasure_for_T_delta`
3. input: `s_unique_eigenmeasure_for_T_delta` --[t_exhaustion_squeeze {classification: "Hausdorff = packing = box dimension = δ"}]--> output: `s_sullivan_conformal_expanding_classification`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_exhaustion_squeeze

---

### Pesin–Sinai SRB physical-measure existence (cite: https://en.wikipedia.org/wiki/SRB_measure)

**Axioms:** `s_dissipative_attractor_with_one_positive_lyapunov_exponent`
**Terminal:** `s_pesin_sinai_srb_existence` (kind: theorem)

**Steps:**
1. input: `s_dissipative_attractor_with_one_positive_lyapunov_exponent` --[t_auxiliary_construction {object: "unstable absolutely continuous conditional measure"}]--> output: `s_ac_conditional_on_unstable_manifold`
2. input: `s_ac_conditional_on_unstable_manifold` --[t_compactness_argument {space: "Cesàro averages of Lebesgue along unstable"}]--> output: `s_cesaro_limit_along_unstable`
3. input: `s_cesaro_limit_along_unstable` --[t_exhaustion_squeeze {physicality: "basin of attraction has positive Lebesgue measure"}]--> output: `s_pesin_sinai_srb_existence`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Newhouse phenomenon (persistence of homoclinic tangencies) (cite: https://en.wikipedia.org/wiki/Newhouse_phenomenon)

**Axioms:** `s_C2_diffeomorphism_with_homoclinic_tangency`
**Terminal:** `s_newhouse_phenomenon` (kind: theorem)

**Steps:**
1. input: `s_C2_diffeomorphism_with_homoclinic_tangency` --[t_auxiliary_construction {object: "thick horseshoes Λ with Cantor-set stable/unstable cross-section"}]--> output: `s_thick_horseshoe_Lambda`
2. input: `s_thick_horseshoe_Lambda` --[t_compactness_argument {tool: "thickness + Newhouse gap lemma"}]--> output: `s_residual_intersection_of_cantor_sets`
3. input: `s_residual_intersection_of_cantor_sets` --[t_exhaustion_squeeze {density: "tangencies are C^2-generic in tangency region"}]--> output: `s_newhouse_phenomenon`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Palis–Takens density of hyperbolicity for one-dim endomorphisms (cite: https://en.wikipedia.org/wiki/Hyperbolic_dynamical_system)

**Axioms:** `s_C2_family_of_unimodal_interval_maps`
**Terminal:** `s_palis_takens_density` (kind: theorem)

**Steps:**
1. input: `s_C2_family_of_unimodal_interval_maps` --[t_auxiliary_construction {object: "set of parameters with stochastic / hyperbolic behavior"}]--> output: `s_hyperbolic_or_stochastic_parameter_set`
2. input: `s_hyperbolic_or_stochastic_parameter_set` --[t_compactness_argument {density: "full Lebesgue measure"}]--> output: `s_full_measure_parameters`
3. input: `s_full_measure_parameters` --[t_exhaustion_squeeze {dichotomy: "regular or stochastic"}]--> output: `s_palis_takens_density`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_exhaustion_squeeze

---

### Krieger's generator theorem (cite: https://en.wikipedia.org/wiki/Krieger%27s_theorem)

**Axioms:** `s_ergodic_measure_preserving_transformation_with_finite_entropy`
**Terminal:** `s_krieger_generator_theorem` (kind: theorem)

**Steps:**
1. input: `s_ergodic_measure_preserving_transformation_with_finite_entropy` --[t_auxiliary_construction {object: "candidate finite generating partition"}]--> output: `s_candidate_generating_partition`
2. input: `s_candidate_generating_partition` --[t_pigeonhole_collision {bound: "|P| ≤ 2^{h(T)} + 1"}]--> output: `s_partition_size_upper_bound`
3. input: `s_partition_size_upper_bound` --[t_exhaustion_squeeze {construction: "Rohlin tower argument generates σ-algebra"}]--> output: `s_krieger_generator_theorem`

**Techniques used:** t_auxiliary_construction, t_pigeonhole_collision, t_exhaustion_squeeze

---

### Rohlin lemma (Rokhlin tower) (cite: https://en.wikipedia.org/wiki/Rokhlin%27s_lemma)

**Axioms:** `s_aperiodic_measure_preserving_transformation`
**Terminal:** `s_rohlin_lemma` (kind: theorem)

**Steps:**
1. input: `s_aperiodic_measure_preserving_transformation` --[t_auxiliary_construction {object: "candidate base set B with iterated translates disjoint"}]--> output: `s_candidate_tower_base_B`
2. input: `s_candidate_tower_base_B` --[t_pigeonhole_collision {bound: "exhaust by union over T^k B"}]--> output: `s_exhaustion_of_X_by_tower`
3. input: `s_exhaustion_of_X_by_tower` --[t_exhaustion_squeeze {ε_approximation: "measure (T^k B)_{k=0..n-1} ≥ 1-ε"}]--> output: `s_rohlin_lemma`

**Techniques used:** t_auxiliary_construction, t_pigeonhole_collision, t_exhaustion_squeeze

---

### Kolmogorov–Sinai entropy invariant theorem (cite: https://en.wikipedia.org/wiki/Measure-preserving_dynamical_system#Kolmogorov%E2%80%93Sinai_entropy)

**Axioms:** `s_measure_preserving_transformation`
**Terminal:** `s_ks_entropy_invariance` (kind: theorem)

**Steps:**
1. input: `s_measure_preserving_transformation` --[t_auxiliary_construction {object: "h(T,P) over finite partitions P"}]--> output: `s_partition_entropy_function`
2. input: `s_partition_entropy_function` --[t_exhaustion_squeeze {sup: "h(T) := sup_P h(T,P)"}]--> output: `s_ks_entropy_h_T`
3. input: `s_ks_entropy_h_T` --[t_structural_isomorphism {invariance: "h(T) preserved under measure-theoretic isomorphism"}]--> output: `s_ks_entropy_invariance`

**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_structural_isomorphism

---

### Mautner phenomenon (cite: https://en.wikipedia.org/wiki/Mautner_phenomenon)

**Axioms:** `s_unitary_representation_of_simple_lie_group_G`
**Terminal:** `s_mautner_phenomenon` (kind: theorem)

**Steps:**
1. input: `s_unitary_representation_of_simple_lie_group_G` --[t_auxiliary_construction {object: "horospherical element a contracting unipotent u"}]--> output: `s_contracting_decomposition_in_G`
2. input: `s_contracting_decomposition_in_G` --[t_symmetry_reduction {invariance: "a-invariant vector is u-invariant"}]--> output: `s_extra_invariance_propagation`
3. input: `s_extra_invariance_propagation` --[t_exhaustion_squeeze {conclusion: "invariance under full G"}]--> output: `s_mautner_phenomenon`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_exhaustion_squeeze

---

### Howe–Moore mixing for semisimple groups (cite: https://en.wikipedia.org/wiki/Howe%E2%80%93Moore_theorem)

**Axioms:** `s_unitary_representation_of_semisimple_lie_group_no_invariant_vectors`
**Terminal:** `s_howe_moore_mixing` (kind: theorem)

**Steps:**
1. input: `s_unitary_representation_of_semisimple_lie_group_no_invariant_vectors` --[t_auxiliary_construction {object: "matrix coefficient ⟨π(g)v, w⟩"}]--> output: `s_matrix_coefficient_function`
2. input: `s_matrix_coefficient_function` --[t_svd_and_spectral_decomposition {tool: "KAK decomposition + bounded representation theory"}]--> output: `s_decay_estimate_on_K_a_K_decomposition`
3. input: `s_decay_estimate_on_K_a_K_decomposition` --[t_exhaustion_squeeze {limit: "matrix coefficients → 0 at infinity"}]--> output: `s_howe_moore_mixing`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_exhaustion_squeeze

---

## Summary

- **Drafted:** 70 chains.
- **Skipped (already in graph):** `s_birkhoff_ergodic_theorem`, `s_szemeredi_theorem_terminal`.
- **Flagged `⚠ needs new technique`:** 0.
- **Overlap notes:**
  - KAM, Floquet, Lyapunov stability, Poincaré–Bendixson — overlap with PDE / classical mechanics agent.
  - Selberg trace formula, Linnik equidistribution, Sarnak Möbius — overlap with number theory agent.
  - Furstenberg correspondence already in graph as composite technique — referenced but not re-derived.
  - Mostow rigidity overlaps with geometry/topology agent.

Frequency of techniques used (sanity check):
- `t_auxiliary_construction`: used in nearly every chain (canonical move).
- `t_exhaustion_squeeze`: heavily used (final-step convergence).
- `t_contraction_fixed_point`: used for all renormalization / fixed-point / linearization theorems.
- `t_structural_isomorphism`: used for symbolic conjugacies, Ratner-type rigidity.
- `t_compactness_argument`: used for weak-* limits, Mahler-type criteria.
- `t_symmetry_reduction`, `t_projection_to_subspace`: used for ergodic structure / Furstenberg-tower style.
- Composites used: `t_ergodic_correspondence`, `t_heights_and_galois_rep_bridge`, `t_fourier_transform`.
- All 70 chains use only frozen techniques from `TECHNIQUES.md`.
