# 62 Frozen Toolbox Techniques (iter-3 reference)

Agents: use these `t_*` ids verbatim in chain steps. **Do not invent new techniques.**
If a theorem genuinely needs a process not on this list, flag the step `⚠ needs new technique` and continue.

| id | cluster | name |
|---|---|---|
| `t_spot_pattern_in_table` | 01_experimental_and_numerical | Spot pattern in table |
| `t_verify_on_special_cases` | 01_experimental_and_numerical | Verify on special cases |
| `t_complete_the_square` | 02_algebraic_manipulation | Complete the square |
| `t_reduce_to_canonical_form` | 02_algebraic_manipulation | Reduce to canonical form |
| `t_compose_with_identity` | 02_algebraic_manipulation | Compose with identity |
| `t_symmetry_reduction` | 03_symmetry_and_invariants | Symmetry reduction |
| `t_conserved_quantity` | 03_symmetry_and_invariants | Conserved quantity |
| `t_duality` | 03_symmetry_and_invariants | Duality |
| `t_character_decomposition_count` | 03_symmetry_and_invariants | Character decomposition count |
| `t_exhaustion_squeeze` | 04_approximation_and_limits | Exhaustion / squeeze |
| `t_interpolate_and_continue` | 04_approximation_and_limits | Interpolate and continue |
| `t_frequency_decomposition` | 04_approximation_and_limits | Frequency decomposition |
| `t_axiomatize_from_instances` | 05_abstraction_and_axiomatization | Axiomatize from instances |
| `t_structural_isomorphism` | 05_abstraction_and_axiomatization | Structural isomorphism |
| `t_ultraproduct_transfer` | 05_abstraction_and_axiomatization | Ultraproduct transfer |
| `t_raise_dimension` | 06_topology_and_obstruction | Raise dimension |
| `t_obstruction_class` | 06_topology_and_obstruction | Obstruction class |
| `t_compactness_argument` | 06_topology_and_obstruction | Compactness argument |
| `t_deformation_cohomology` | 06_topology_and_obstruction | Deformation cohomology |
| `t_rescale_for_asymptotic_geometry` | 06_topology_and_obstruction | Rescale for asymptotic geometry |
| `t_diagonalize` | 07_self_reference_and_impossibility | Diagonalize |
| `t_arithmetize_syntax` | 07_self_reference_and_impossibility | Arithmetize syntax |
| `t_force_independence` | 07_self_reference_and_impossibility | Force independence |
| `t_contraction_fixed_point` | 08_iteration_and_fixed_points | Contraction fixed point |
| `t_infinite_descent` | 08_iteration_and_fixed_points | Infinite descent |
| `t_flow_with_surgery` | 08_iteration_and_fixed_points | Flow with surgery |
| `t_physics_to_pde` | 09_cross_field_transfer | Physics to PDE |
| `t_complex_analysis_to_integers` | 09_cross_field_transfer | Complex analysis to integers |
| `t_analysis_algebra_topology_bridge` | 09_cross_field_transfer | Analysis–algebra–topology bridge |
| `t_major_minor_arc_decomposition` | 09_cross_field_transfer | Major/minor arc decomposition |
| `t_ergodic_correspondence` | 09_cross_field_transfer | Ergodic correspondence |
| `t_finite_case_check` | 10_computer_and_collaboration | Finite case check |
| `t_formal_verify` | 10_computer_and_collaboration | Formal verify |
| `t_distributed_collaboration` | 10_computer_and_collaboration | Distributed collaboration |
| `t_probabilistic_existence` | 11_probabilistic_and_counting | Probabilistic existence |
| `t_pigeonhole_collision` | 11_probabilistic_and_counting | Pigeonhole collision |
| `t_sieve_by_optimized_quadratic` | 11_probabilistic_and_counting | Sieve by optimized quadratic |
| `t_group_complete_exact_category` | 12_homological_and_categorical | Group-complete exact category (K-theory) |
| `t_sheafify_on_grothendieck_topology` | 12_homological_and_categorical | Sheafify on Grothendieck topology |
| `t_representable_functor_trick` | 12_homological_and_categorical | Representable functor trick |
| `t_polynomial_method` | 11_probabilistic_and_counting | Polynomial method |
| `t_double_centralizer_decompose` | 03_symmetry_and_invariants | Double centralizer decompose |
| `t_fourier_transform` | 04_approximation_and_limits | Fourier transform (umbrella) |
| `t_svd_and_spectral_decomposition` | 02_algebraic_manipulation_and_04_approximation_and_limits | SVD / spectral decomposition |
| `t_galois_correspondence` | 05_abstraction_and_axiomatization | Galois correspondence (composite) |
| `t_ricci_flow_with_surgery` | 08_iteration_and_fixed_points | Ricci flow with surgery (composite) |
| `t_wiles_modularity` | 06_topology_and_obstruction | Wiles modularity (composite) |
| `t_godel_numbering` | 07_self_reference_and_impossibility | Gödel numbering (composite) |
| `t_atiyah_singer_index_machinery` | 12_homological_and_categorical | Atiyah–Singer index machinery (composite) |
| `t_selberg_sieve_method` | 11_probabilistic_and_counting | Selberg sieve method (composite) |
| `t_circle_method` | 09_cross_field_transfer | Circle method (composite) |
| `t_furstenberg_correspondence_principle` | 09_cross_field_transfer | Furstenberg correspondence (composite) |
| `t_category_theoretic_colimits_and_adjoints` | 12_homological_and_categorical | Category-theoretic colimits/adjoints (composite) |
| `t_auxiliary_construction` | C2 | Auxiliary construction |
| `t_conjecture_refinement` | C1 | Conjecture refinement |
| `t_reductio_ad_absurdum` | C7 | Reductio ad absurdum |
| `t_projection_to_subspace` | C6 | Projection to subspace |
| `t_sheaf_cohomology_bridge` | C12 | Sheaf cohomology bridge |
| `t_k_theoretic_index_bridge` | C12 | K-theoretic index bridge |
| `t_heights_and_galois_rep_bridge` | C9 | Heights / Galois representation bridge |
| `t_level_lowering_bridge` | C9 | Level-lowering bridge (Ribet) |
| `t_transference_bridge` | C9 | Transference bridge |