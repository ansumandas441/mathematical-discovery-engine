# Area Combinatorics & Graph Theory Derivation Chains (iter-3)

**Source pages:**
- https://en.wikipedia.org/wiki/Category:Theorems_in_combinatorics
- https://en.wikipedia.org/wiki/Category:Theorems_in_graph_theory
- https://en.wikipedia.org/wiki/Category:Extremal_combinatorics
- https://en.wikipedia.org/wiki/List_of_combinatorial_identities
- https://en.wikipedia.org/wiki/Glossary_of_graph_theory

**Target:** 80 chains. **Drafted:** 80. **Skipped (already in graph):** 5
- `s_szemeredi_theorem_terminal` (Szemerédi's theorem)
- `s_green_tao` (Green–Tao theorem)
- `s_ramsey_theorem_infinite` (Infinite Ramsey theorem)
- `s_four_color_theorem` (4-color theorem)
- `s_graph_minor_theorem` (Robertson–Seymour graph minor theorem)
- `s_eulerian_path_criterion` (Eulerian path criterion — Euler's bridges)

**Flagged (`⚠ needs new technique`):** 0.

Conventions: a chain uses only `t_*` ids from `TECHNIQUES.md`. Axioms are minimal supporting states; `s_*` ids are stable snake_case mathematical objects. Compound techniques (e.g., `t_fourier_transform`, `t_furstenberg_correspondence_principle`) are used as single atomic arrows.

---

## I. RAMSEY-TYPE & PARTITION REGULARITY (1–10)

### Ramsey's theorem (finite version) (cite: https://en.wikipedia.org/wiki/Ramsey%27s_theorem)

**Axioms:** `s_k_coloring_of_pairs`, `s_graph_definition`
**Terminal:** `s_ramsey_theorem_finite` (kind: theorem)

**Steps:**
1. input: `⟨s_k_coloring_of_pairs, s_graph_definition⟩` --[t_axiomatize_from_instances {pattern: "K_n always contains monochromatic K_r"}]--> output: `s_finite_ramsey_conjecture`
2. input: `s_finite_ramsey_conjecture` --[t_pigeonhole_collision {pigeons: "neighbours of a vertex", holes: "colour classes"}]--> output: `s_recursive_majority_color_neighbourhood`
3. input: `s_recursive_majority_color_neighbourhood` --[t_infinite_descent {direction: "induction on r+s"}]--> output: `s_ramsey_number_recurrence_R_r_s`
4. input: `s_ramsey_number_recurrence_R_r_s` --[t_finite_case_check {base: "R(2,s)=s"}]--> output: `s_ramsey_theorem_finite`

**Techniques used:** t_axiomatize_from_instances, t_pigeonhole_collision, t_infinite_descent, t_finite_case_check

---

### Schur's theorem (cite: https://en.wikipedia.org/wiki/Schur%27s_theorem)

**Axioms:** `s_integers`, `s_k_coloring_of_pairs`
**Terminal:** `s_schur_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_integers, s_k_coloring_of_pairs⟩` --[t_auxiliary_construction {object: "complete graph on {1..N} with edges coloured by c(|i-j|)"}]--> output: `s_edge_colored_complete_graph_from_schur_coloring`
2. input: `s_edge_colored_complete_graph_from_schur_coloring` --[t_structural_isomorphism {target: "monochromatic triangle"}]--> output: `s_monochromatic_triangle_to_schur_triple`
3. input: `s_monochromatic_triangle_to_schur_triple` --[t_pigeonhole_collision {hypothesis: "N ≥ R(3,3,…,3)"}]--> output: `s_schur_theorem`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_pigeonhole_collision

---

### Van der Waerden's theorem (cite: https://en.wikipedia.org/wiki/Van_der_Waerden%27s_theorem)

**Axioms:** `s_integers`, `s_k_coloring_of_pairs`
**Terminal:** `s_van_der_waerden_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_integers, s_k_coloring_of_pairs⟩` --[t_conjecture_refinement {claim: "monochromatic AP of length k exists in any r-colouring of long enough interval"}]--> output: `s_vdw_conjecture_W_r_k`
2. input: `s_vdw_conjecture_W_r_k` --[t_pigeonhole_collision {blocks: "consecutive m-blocks of colours"}]--> output: `s_color_focused_progressions`
3. input: `s_color_focused_progressions` --[t_infinite_descent {induction: "double induction on (k, r)"}]--> output: `s_vdw_finite_intersection_lemma`
4. input: `s_vdw_finite_intersection_lemma` --[t_compactness_argument {space: "Stone–Čech βℕ or product of colour spaces"}]--> output: `s_van_der_waerden_theorem`

**Techniques used:** t_conjecture_refinement, t_pigeonhole_collision, t_infinite_descent, t_compactness_argument

---

### Hales–Jewett theorem (cite: https://en.wikipedia.org/wiki/Hales%E2%80%93Jewett_theorem)

**Axioms:** `s_k_coloring_of_pairs`, `s_finite_combinatorial_cube_word_space`
**Terminal:** `s_hales_jewett_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_k_coloring_of_pairs, s_finite_combinatorial_cube_word_space⟩` --[t_axiomatize_from_instances {observation: "VdW = HJ over alphabet [k] projected to ℤ"}]--> output: `s_combinatorial_line_target`
2. input: `s_combinatorial_line_target` --[t_infinite_descent {induction: "induction on alphabet size t"}]--> output: `s_shelah_cube_lemma`
3. input: `s_shelah_cube_lemma` --[t_pigeonhole_collision {object: "first-difference layers in Shelah cube"}]--> output: `s_hales_jewett_theorem`

**Techniques used:** t_axiomatize_from_instances, t_infinite_descent, t_pigeonhole_collision

---

### Hindman's finite sums theorem (cite: https://en.wikipedia.org/wiki/Hindman%27s_theorem)

**Axioms:** `s_naturals_with_multiplication`, `s_k_coloring_of_pairs`
**Terminal:** `s_hindman_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_naturals_with_multiplication, s_k_coloring_of_pairs⟩` --[t_auxiliary_construction {object: "Stone–Čech compactification βℕ with extended +"}]--> output: `s_compact_right_topological_semigroup_beta_N`
2. input: `s_compact_right_topological_semigroup_beta_N` --[t_contraction_fixed_point {ellis: "Ellis–Numakura lemma → idempotent ultrafilter"}]--> output: `s_idempotent_ultrafilter_p`
3. input: `s_idempotent_ultrafilter_p` --[t_ultraproduct_transfer {transfer: "membership in p propagates to finite-sum sets"}]--> output: `s_hindman_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_ultraproduct_transfer

---

### Graham–Rothschild theorem (cite: https://en.wikipedia.org/wiki/Graham%E2%80%93Rothschild_theorem)

**Axioms:** `s_finite_combinatorial_cube_word_space`, `s_k_coloring_of_pairs`
**Terminal:** `s_graham_rothschild_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_combinatorial_cube_word_space, s_k_coloring_of_pairs⟩` --[t_axiomatize_from_instances {pattern: "HJ generalised to k-parameter subcubes"}]--> output: `s_parameter_word_partition_setup`
2. input: `s_parameter_word_partition_setup` --[t_infinite_descent {induction: "iterate Hales–Jewett on parameter sets"}]--> output: `s_iterated_hj_combinatorial_subspace`
3. input: `s_iterated_hj_combinatorial_subspace` --[t_pigeonhole_collision {layer: "monochromatic parameter subcube"}]--> output: `s_graham_rothschild_theorem`

**Techniques used:** t_axiomatize_from_instances, t_infinite_descent, t_pigeonhole_collision

---

### Folkman's theorem (cite: https://en.wikipedia.org/wiki/Folkman%27s_theorem)

**Axioms:** `s_naturals_with_multiplication`, `s_k_coloring_of_pairs`
**Terminal:** `s_folkman_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_naturals_with_multiplication, s_k_coloring_of_pairs⟩` --[t_conjecture_refinement {claim: "finite analogue of Hindman: monochromatic sums of any size-m subset"}]--> output: `s_folkman_finite_target`
2. input: `s_folkman_finite_target` --[t_auxiliary_construction {tool: "Hales–Jewett over alphabet [n]"}]--> output: `s_folkman_via_hj_reduction`
3. input: `s_folkman_via_hj_reduction` --[t_pigeonhole_collision {monochromatic: "combinatorial line ↦ sumset"}]--> output: `s_folkman_theorem`

**Techniques used:** t_conjecture_refinement, t_auxiliary_construction, t_pigeonhole_collision

---

### Gallai's theorem (multidimensional VdW) (cite: https://en.wikipedia.org/wiki/Gallai%27s_theorem)

**Axioms:** `s_integers`, `s_k_coloring_of_pairs`
**Terminal:** `s_gallai_theorem_multidim_vdw` (kind: theorem)

**Steps:**
1. input: `⟨s_integers, s_k_coloring_of_pairs⟩` --[t_axiomatize_from_instances {pattern: "any finite configuration in ℤ^d has monochromatic homothetic copy"}]--> output: `s_homothetic_copy_target`
2. input: `s_homothetic_copy_target` --[t_structural_isomorphism {reduction: "embed configuration as Hales–Jewett line"}]--> output: `s_gallai_via_hj_reduction`
3. input: `s_gallai_via_hj_reduction` --[t_pigeonhole_collision]--> output: `s_gallai_theorem_multidim_vdw`

**Techniques used:** t_axiomatize_from_instances, t_structural_isomorphism, t_pigeonhole_collision

---

### Erdős–Rado theorem (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Rado_theorem)

**Axioms:** `s_infinite_set`, `s_k_coloring_of_pairs`
**Terminal:** `s_erdos_rado_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_infinite_set, s_k_coloring_of_pairs⟩` --[t_axiomatize_from_instances {claim: "infinite Ramsey for uncountable cardinals: (2^κ)+ → (κ+)²_κ"}]--> output: `s_uncountable_partition_target`
2. input: `s_uncountable_partition_target` --[t_auxiliary_construction {object: "transfinite canonical sequence"}]--> output: `s_transfinite_color_canonization`
3. input: `s_transfinite_color_canonization` --[t_infinite_descent {induction: "transfinite induction on κ"}]--> output: `s_erdos_rado_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_infinite_descent

---

### Carlson–Simpson theorem (cite: https://en.wikipedia.org/wiki/Carlson%E2%80%93Simpson_theorem)

**Axioms:** `s_finite_combinatorial_cube_word_space`, `s_k_coloring_of_pairs`
**Terminal:** `s_carlson_simpson_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_combinatorial_cube_word_space, s_k_coloring_of_pairs⟩` --[t_conjecture_refinement {strengthening: "infinitary Hales–Jewett with variable words"}]--> output: `s_infinitary_hj_target`
2. input: `s_infinitary_hj_target` --[t_compactness_argument {space: "ultrafilter on space of variable words"}]--> output: `s_ultrafilter_on_variable_words`
3. input: `s_ultrafilter_on_variable_words` --[t_pigeonhole_collision {extract: "monochromatic infinite-dim combinatorial subspace"}]--> output: `s_carlson_simpson_theorem`

**Techniques used:** t_conjecture_refinement, t_compactness_argument, t_pigeonhole_collision

---

## II. EXTREMAL SET THEORY (11–18)

### Erdős–Ko–Rado theorem (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Ko%E2%80%93Rado_theorem)

**Axioms:** `s_finite_set_family`, `s_intersecting_family_property`
**Terminal:** `s_erdos_ko_rado_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_set_family, s_intersecting_family_property⟩` --[t_axiomatize_from_instances {target: "max |F| for intersecting k-uniform family on [n], n ≥ 2k"}]--> output: `s_max_intersecting_k_uniform_problem`
2. input: `s_max_intersecting_k_uniform_problem` --[t_auxiliary_construction {object: "Katona cyclic permutation argument"}]--> output: `s_cyclic_arc_counting_bound`
3. input: `s_cyclic_arc_counting_bound` --[t_double_centralizer_decompose {action: "S_n cyclic shifts"}]--> output: `s_double_counting_arc_intersection`
4. input: `s_double_counting_arc_intersection` --[t_exhaustion_squeeze {squeeze: "tight when family = star {A : x∈A}"}]--> output: `s_erdos_ko_rado_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_double_centralizer_decompose, t_exhaustion_squeeze

---

### Kruskal–Katona theorem (cite: https://en.wikipedia.org/wiki/Kruskal%E2%80%93Katona_theorem)

**Axioms:** `s_finite_set_family`, `s_shadow_operator_on_set_family`
**Terminal:** `s_kruskal_katona_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_set_family, s_shadow_operator_on_set_family⟩` --[t_axiomatize_from_instances {target: "minimise |∂F| over k-uniform F of size m"}]--> output: `s_shadow_minimisation_problem`
2. input: `s_shadow_minimisation_problem` --[t_reduce_to_canonical_form {form: "colex-initial family"}]--> output: `s_colex_initial_family_extremum`
3. input: `s_colex_initial_family_extremum` --[t_auxiliary_construction {tool: "compression / shifting operator"}]--> output: `s_compression_preserves_size_reduces_shadow`
4. input: `s_compression_preserves_size_reduces_shadow` --[t_exhaustion_squeeze]--> output: `s_kruskal_katona_theorem`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form, t_auxiliary_construction, t_exhaustion_squeeze

---

### LYM inequality (cite: https://en.wikipedia.org/wiki/Lubell%E2%80%93Yamamoto%E2%80%93Meshalkin_inequality)

**Axioms:** `s_finite_set_family`, `s_antichain_in_boolean_lattice`
**Terminal:** `s_lym_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_set_family, s_antichain_in_boolean_lattice⟩` --[t_auxiliary_construction {tool: "uniform random maximal chain in 2^[n]"}]--> output: `s_random_maximal_chain_on_boolean_lattice`
2. input: `s_random_maximal_chain_on_boolean_lattice` --[t_probabilistic_existence {expectation: "E[|chain ∩ antichain|] ≤ 1"}]--> output: `s_chain_meets_antichain_at_most_once`
3. input: `s_chain_meets_antichain_at_most_once` --[t_exhaustion_squeeze]--> output: `s_lym_inequality`

**Techniques used:** t_auxiliary_construction, t_probabilistic_existence, t_exhaustion_squeeze

---

### Sperner's theorem (cite: https://en.wikipedia.org/wiki/Sperner%27s_theorem)

**Axioms:** `s_antichain_in_boolean_lattice`, `s_lym_inequality`
**Terminal:** `s_sperner_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_antichain_in_boolean_lattice, s_lym_inequality⟩` --[t_exhaustion_squeeze {bound: "Σ 1/C(n,|A|) ≤ 1 maximised at |A|=⌊n/2⌋"}]--> output: `s_middle_layer_bound_for_antichain`
2. input: `s_middle_layer_bound_for_antichain` --[t_verify_on_special_cases {witness: "middle layer achieves bound"}]--> output: `s_sperner_theorem`

**Techniques used:** t_exhaustion_squeeze, t_verify_on_special_cases

---

### Bollobás set-pair inequality (cite: https://en.wikipedia.org/wiki/Bollob%C3%A1s%27_inequality)

**Axioms:** `s_finite_set_family`, `s_cross_intersecting_pair_system`
**Terminal:** `s_bollobas_set_pair_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_set_family, s_cross_intersecting_pair_system⟩` --[t_auxiliary_construction {tool: "uniform random linear order on ground set"}]--> output: `s_random_linear_order_on_ground_set`
2. input: `s_random_linear_order_on_ground_set` --[t_probabilistic_existence {event: "all of A_i precedes all of B_i"}]--> output: `s_probability_event_disjoint_pairs`
3. input: `s_probability_event_disjoint_pairs` --[t_exhaustion_squeeze]--> output: `s_bollobas_set_pair_inequality`

**Techniques used:** t_auxiliary_construction, t_probabilistic_existence, t_exhaustion_squeeze

---

### Sauer–Shelah lemma (VC dimension) (cite: https://en.wikipedia.org/wiki/Sauer%E2%80%93Shelah_lemma)

**Axioms:** `s_finite_set_family`, `s_vc_dimension_definition`
**Terminal:** `s_sauer_shelah_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_set_family, s_vc_dimension_definition⟩` --[t_axiomatize_from_instances {target: "bound |F| in terms of VC(F)=d"}]--> output: `s_vc_count_bound_target`
2. input: `s_vc_count_bound_target` --[t_auxiliary_construction {tool: "shift / down-compression to hereditary family"}]--> output: `s_down_compressed_shattering_preserved`
3. input: `s_down_compressed_shattering_preserved` --[t_infinite_descent {induction: "induction on |X|"}]--> output: `s_shattering_bound_sum_binomials`
4. input: `s_shattering_bound_sum_binomials` --[t_exhaustion_squeeze]--> output: `s_sauer_shelah_lemma`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_infinite_descent, t_exhaustion_squeeze

---

### Frankl–Wilson theorem (cite: https://en.wikipedia.org/wiki/Frankl%E2%80%93Wilson_theorem)

**Axioms:** `s_finite_set_family`, `s_prime_p`
**Terminal:** `s_frankl_wilson_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_set_family, s_prime_p⟩` --[t_axiomatize_from_instances {target: "|F| bound when |A∩B| ∈ L (mod p) avoided"}]--> output: `s_mod_p_intersection_pattern_target`
2. input: `s_mod_p_intersection_pattern_target` --[t_polynomial_method {tool: "associate to each A its incidence polynomial in 𝔽_p"}]--> output: `s_incidence_polynomial_basis_in_F_p`
3. input: `s_incidence_polynomial_basis_in_F_p` --[t_projection_to_subspace {target: "linearly independent in degree-≤s space"}]--> output: `s_frankl_wilson_theorem`

**Techniques used:** t_axiomatize_from_instances, t_polynomial_method, t_projection_to_subspace

---

### Ahlswede–Khachatrian theorem (cite: https://en.wikipedia.org/wiki/Ahlswede%E2%80%93Khachatrian_theorem)

**Axioms:** `s_finite_set_family`, `s_t_intersecting_family_property`
**Terminal:** `s_ahlswede_khachatrian_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_set_family, s_t_intersecting_family_property⟩` --[t_conjecture_refinement {refine: "complete intersection conjecture, t-intersecting families on [n,k]"}]--> output: `s_complete_intersection_problem`
2. input: `s_complete_intersection_problem` --[t_auxiliary_construction {family: "F_r = {A : |A ∩ [t+2r]| ≥ t+r}"}]--> output: `s_frankl_family_F_r_candidate`
3. input: `s_frankl_family_F_r_candidate` --[t_double_centralizer_decompose {eigenspace: "Johnson scheme spectral analysis"}]--> output: `s_johnson_scheme_eigenvalue_optimum`
4. input: `s_johnson_scheme_eigenvalue_optimum` --[t_exhaustion_squeeze]--> output: `s_ahlswede_khachatrian_theorem`

**Techniques used:** t_conjecture_refinement, t_auxiliary_construction, t_double_centralizer_decompose, t_exhaustion_squeeze

---

## III. ORDER, MATCHING, DUALITY (19–28)

### Hall's marriage theorem (cite: https://en.wikipedia.org/wiki/Hall%27s_marriage_theorem)

**Axioms:** `s_bipartite_graph`, `s_perfect_matching_definition`
**Terminal:** `s_hall_marriage_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_bipartite_graph, s_perfect_matching_definition⟩` --[t_conjecture_refinement {hall_condition: "|N(S)| ≥ |S| for every S ⊆ A"}]--> output: `s_hall_condition_statement`
2. input: `s_hall_condition_statement` --[t_reductio_ad_absurdum {assume: "no perfect matching exists"}]--> output: `s_minimum_vertex_cover_smaller_than_A`
3. input: `s_minimum_vertex_cover_smaller_than_A` --[t_auxiliary_construction {augmenting_path: "alternating path from unmatched a"}]--> output: `s_augmenting_path_yields_violator_S`
4. input: `s_augmenting_path_yields_violator_S` --[t_exhaustion_squeeze]--> output: `s_hall_marriage_theorem`

**Techniques used:** t_conjecture_refinement, t_reductio_ad_absurdum, t_auxiliary_construction, t_exhaustion_squeeze

---

### König's theorem (cite: https://en.wikipedia.org/wiki/K%C5%91nig%27s_theorem_(graph_theory))

**Axioms:** `s_bipartite_graph`, `s_min_vertex_cover_definition`
**Terminal:** `s_konig_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_bipartite_graph, s_min_vertex_cover_definition⟩` --[t_duality {pairing: "max matching ↔ min vertex cover"}]--> output: `s_lp_relaxation_matching_vs_cover`
2. input: `s_lp_relaxation_matching_vs_cover` --[t_auxiliary_construction {object: "alternating BFS tree from unmatched vertices"}]--> output: `s_konig_cover_constructed_from_max_matching`
3. input: `s_konig_cover_constructed_from_max_matching` --[t_exhaustion_squeeze]--> output: `s_konig_theorem`

**Techniques used:** t_duality, t_auxiliary_construction, t_exhaustion_squeeze

---

### Dilworth's theorem (cite: https://en.wikipedia.org/wiki/Dilworth%27s_theorem)

**Axioms:** `s_finite_poset`, `s_antichain_chain_decomposition_problem`
**Terminal:** `s_dilworth_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_poset, s_antichain_chain_decomposition_problem⟩` --[t_duality {dual: "max antichain ↔ min chain cover"}]--> output: `s_lp_dual_for_chain_cover`
2. input: `s_lp_dual_for_chain_cover` --[t_structural_isomorphism {reduce: "incidence bipartite graph on comparable pairs"}]--> output: `s_dilworth_reduced_to_konig_on_comparability_bipartite`
3. input: `s_dilworth_reduced_to_konig_on_comparability_bipartite` --[t_compose_with_identity {apply: "König's theorem"}]--> output: `s_dilworth_theorem`

**Techniques used:** t_duality, t_structural_isomorphism, t_compose_with_identity

---

### Mirsky's theorem (cite: https://en.wikipedia.org/wiki/Mirsky%27s_theorem)

**Axioms:** `s_finite_poset`, `s_antichain_chain_decomposition_problem`
**Terminal:** `s_mirsky_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_poset, s_antichain_chain_decomposition_problem⟩` --[t_duality {dual_of_dilworth: "max chain ↔ min antichain cover"}]--> output: `s_dual_chain_cover_problem`
2. input: `s_dual_chain_cover_problem` --[t_auxiliary_construction {height_function: "f(x) = length of longest chain ending at x"}]--> output: `s_height_function_level_sets`
3. input: `s_height_function_level_sets` --[t_exhaustion_squeeze]--> output: `s_mirsky_theorem`

**Techniques used:** t_duality, t_auxiliary_construction, t_exhaustion_squeeze

---

### Menger's theorem (cite: https://en.wikipedia.org/wiki/Menger%27s_theorem)

**Axioms:** `s_graph_definition`, `s_connectivity_definition`
**Terminal:** `s_menger_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_connectivity_definition⟩` --[t_axiomatize_from_instances {claim: "max number of disjoint s–t paths = min s–t cut"}]--> output: `s_menger_target`
2. input: `s_menger_target` --[t_duality {flow_cut_duality: "integral version"}]--> output: `s_integral_flow_equals_integral_cut`
3. input: `s_integral_flow_equals_integral_cut` --[t_auxiliary_construction {tool: "augmenting path in residual graph"}]--> output: `s_menger_theorem`

**Techniques used:** t_axiomatize_from_instances, t_duality, t_auxiliary_construction

---

### Max-flow min-cut theorem (cite: https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem)

**Axioms:** `s_directed_graph_with_capacities`, `s_flow_conservation_axiom`
**Terminal:** `s_max_flow_min_cut_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_directed_graph_with_capacities, s_flow_conservation_axiom⟩` --[t_duality {lp_dual: "primal max-flow LP ↔ dual min-cut LP"}]--> output: `s_max_flow_lp_dual`
2. input: `s_max_flow_lp_dual` --[t_auxiliary_construction {object: "augmenting path until none exists"}]--> output: `s_residual_graph_no_augmenting_path_yields_cut`
3. input: `s_residual_graph_no_augmenting_path_yields_cut` --[t_exhaustion_squeeze]--> output: `s_max_flow_min_cut_theorem`

**Techniques used:** t_duality, t_auxiliary_construction, t_exhaustion_squeeze

---

### Berge's theorem (augmenting path) (cite: https://en.wikipedia.org/wiki/Berge%27s_theorem)

**Axioms:** `s_graph_definition`, `s_matching_in_graph`
**Terminal:** `s_berge_augmenting_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_matching_in_graph⟩` --[t_axiomatize_from_instances {claim: "M maximum ⇔ no M-augmenting path"}]--> output: `s_berge_target`
2. input: `s_berge_target` --[t_reductio_ad_absurdum {assume: "M not maximum yet no augmenting path"}]--> output: `s_symmetric_difference_M_Mprime_decomposes_into_paths`
3. input: `s_symmetric_difference_M_Mprime_decomposes_into_paths` --[t_exhaustion_squeeze]--> output: `s_berge_augmenting_theorem`

**Techniques used:** t_axiomatize_from_instances, t_reductio_ad_absurdum, t_exhaustion_squeeze

---

### Petersen's theorem (3-regular bridgeless) (cite: https://en.wikipedia.org/wiki/Petersen%27s_theorem)

**Axioms:** `s_graph_definition`, `s_three_regular_bridgeless_graph`
**Terminal:** `s_petersen_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_three_regular_bridgeless_graph⟩` --[t_conjecture_refinement {claim: "every cubic bridgeless graph has perfect matching"}]--> output: `s_petersen_target`
2. input: `s_petersen_target` --[t_auxiliary_construction {odd_components: "Tutte: count odd components after deleting S"}]--> output: `s_tutte_odd_component_count_under_3regular_bridgeless`
3. input: `s_tutte_odd_component_count_under_3regular_bridgeless` --[t_compose_with_identity {apply: "Tutte's theorem"}]--> output: `s_petersen_theorem`

**Techniques used:** t_conjecture_refinement, t_auxiliary_construction, t_compose_with_identity

---

### Tutte's theorem (perfect matching) (cite: https://en.wikipedia.org/wiki/Tutte_theorem)

**Axioms:** `s_graph_definition`, `s_perfect_matching_definition`
**Terminal:** `s_tutte_perfect_matching_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_perfect_matching_definition⟩` --[t_axiomatize_from_instances {tutte_condition: "o(G-S) ≤ |S| for all S"}]--> output: `s_tutte_condition_target`
2. input: `s_tutte_condition_target` --[t_reductio_ad_absurdum {assume: "no perfect matching but Tutte condition holds"}]--> output: `s_maximal_counterexample_extremal_S`
3. input: `s_maximal_counterexample_extremal_S` --[t_auxiliary_construction {alternating_structure: "block-cut tree of G-S"}]--> output: `s_block_structure_contradicts_tutte_count`
4. input: `s_block_structure_contradicts_tutte_count` --[t_exhaustion_squeeze]--> output: `s_tutte_perfect_matching_theorem`

**Techniques used:** t_axiomatize_from_instances, t_reductio_ad_absurdum, t_auxiliary_construction, t_exhaustion_squeeze

---

### Gale–Ryser theorem (degree sequence) (cite: https://en.wikipedia.org/wiki/Gale%E2%80%93Ryser_theorem)

**Axioms:** `s_bipartite_graph`, `s_degree_sequence`
**Terminal:** `s_gale_ryser_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_bipartite_graph, s_degree_sequence⟩` --[t_axiomatize_from_instances {target: "characterise bipartite-realizable pairs (d, e)"}]--> output: `s_gale_ryser_target`
2. input: `s_gale_ryser_target` --[t_duality {flow_model: "transportation polytope = integral hull"}]--> output: `s_transportation_polytope_integrality_certificate`
3. input: `s_transportation_polytope_integrality_certificate` --[t_compose_with_identity {apply: "max-flow min-cut"}]--> output: `s_gale_ryser_theorem`

**Techniques used:** t_axiomatize_from_instances, t_duality, t_compose_with_identity

---

### Erdős–Gallai theorem (graphic sequence) (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gallai_theorem)

**Axioms:** `s_graph_definition`, `s_degree_sequence`
**Terminal:** `s_erdos_gallai_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_degree_sequence⟩` --[t_axiomatize_from_instances {target: "characterise graphic sequences"}]--> output: `s_graphic_sequence_target`
2. input: `s_graphic_sequence_target` --[t_reduce_to_canonical_form {form: "sort d_1 ≥ … ≥ d_n, inequality on Σ_{i ≤ k} d_i"}]--> output: `s_sorted_degree_partial_sums_inequality`
3. input: `s_sorted_degree_partial_sums_inequality` --[t_auxiliary_construction {hh_algorithm: "Havel–Hakimi successive reduction"}]--> output: `s_erdos_gallai_theorem`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form, t_auxiliary_construction

---

## IV. EXTREMAL GRAPH THEORY (29–38)

### Turán's theorem (cite: https://en.wikipedia.org/wiki/Tur%C3%A1n%27s_theorem)

**Axioms:** `s_graph_definition`, `s_forbidden_subgraph_K_r_plus_1`
**Terminal:** `s_turan_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_forbidden_subgraph_K_r_plus_1⟩` --[t_axiomatize_from_instances {target: "max edges in K_{r+1}-free graph on n vertices"}]--> output: `s_extremal_count_target`
2. input: `s_extremal_count_target` --[t_auxiliary_construction {tool: "Zykov symmetrisation / weight shifting"}]--> output: `s_zykov_symmetric_extremal_graph`
3. input: `s_zykov_symmetric_extremal_graph` --[t_reduce_to_canonical_form {form: "complete r-partite Turán graph T(n,r)"}]--> output: `s_turan_graph_T_n_r`
4. input: `s_turan_graph_T_n_r` --[t_exhaustion_squeeze]--> output: `s_turan_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Erdős–Stone theorem (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Stone_theorem)

**Axioms:** `s_graph_definition`, `s_chromatic_number_definition`
**Terminal:** `s_erdos_stone_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_chromatic_number_definition⟩` --[t_axiomatize_from_instances {target: "ex(n,H) ~ (1 - 1/(χ(H)-1)) C(n,2)"}]--> output: `s_erdos_stone_target`
2. input: `s_erdos_stone_target` --[t_auxiliary_construction {find: "dense K_{r,r,…,r} via repeated DFS branching"}]--> output: `s_blow_up_complete_multipartite_found`
3. input: `s_blow_up_complete_multipartite_found` --[t_compose_with_identity {apply: "Turán bound on (r+1)-partite reduction"}]--> output: `s_erdos_stone_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_compose_with_identity

---

### Kővári–Sós–Turán theorem (cite: https://en.wikipedia.org/wiki/K%C5%91v%C3%A1ri%E2%80%93S%C3%B3s%E2%80%93Tur%C3%A1n_theorem)

**Axioms:** `s_bipartite_graph`, `s_forbidden_subgraph_K_s_t`
**Terminal:** `s_kovari_sos_turan_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_bipartite_graph, s_forbidden_subgraph_K_s_t⟩` --[t_axiomatize_from_instances {target: "bound edges in K_{s,t}-free graph"}]--> output: `s_kst_extremal_target`
2. input: `s_kst_extremal_target` --[t_auxiliary_construction {tool: "double-count copies of K_{s,1} via convex deg-sum"}]--> output: `s_jensen_lower_bound_on_K_s_copies`
3. input: `s_jensen_lower_bound_on_K_s_copies` --[t_exhaustion_squeeze]--> output: `s_kovari_sos_turan_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_exhaustion_squeeze

---

### Bondy–Simonovits theorem (even cycles) (cite: https://en.wikipedia.org/wiki/Even_circuit_theorem)

**Axioms:** `s_graph_definition`, `s_forbidden_even_cycle_C_2k`
**Terminal:** `s_bondy_simonovits_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_forbidden_even_cycle_C_2k⟩` --[t_axiomatize_from_instances {target: "ex(n,C_{2k}) = O(n^{1+1/k})"}]--> output: `s_even_cycle_extremal_target`
2. input: `s_even_cycle_extremal_target` --[t_auxiliary_construction {tool: "BFS layering and path-counting argument"}]--> output: `s_bfs_layer_count_doubling`
3. input: `s_bfs_layer_count_doubling` --[t_pigeonhole_collision {two_paths_same_endpoints: "yields C_{2k}"}]--> output: `s_bondy_simonovits_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_pigeonhole_collision

---

### Szemerédi regularity lemma (cite: https://en.wikipedia.org/wiki/Szemer%C3%A9di_regularity_lemma)

**Axioms:** `s_graph_definition`, `s_density_between_vertex_sets`
**Terminal:** `s_szemeredi_regularity_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_density_between_vertex_sets⟩` --[t_axiomatize_from_instances {claim: "every graph admits ε-regular equipartition"}]--> output: `s_regularity_target`
2. input: `s_regularity_target` --[t_auxiliary_construction {potential: "index q(P) = Σ |V_i||V_j| d(V_i,V_j)²"}]--> output: `s_mean_square_density_index_q`
3. input: `s_mean_square_density_index_q` --[t_infinite_descent {iterate: "refine until no irregular pair, q bounded ≤ 1"}]--> output: `s_szemeredi_regularity_lemma`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_infinite_descent

---

### Graph removal lemma (cite: https://en.wikipedia.org/wiki/Graph_removal_lemma)

**Axioms:** `s_graph_definition`, `s_szemeredi_regularity_lemma`
**Terminal:** `s_graph_removal_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_szemeredi_regularity_lemma⟩` --[t_compose_with_identity {apply: "regularity → cleaned reduced graph"}]--> output: `s_cleaned_reduced_graph_H_free_or_dense`
2. input: `s_cleaned_reduced_graph_H_free_or_dense` --[t_auxiliary_construction {counting_lemma: "ε-regular triple ⇒ Ω(ε^{|V(H)|}) copies"}]--> output: `s_counting_lemma_dense_H_implication`
3. input: `s_counting_lemma_dense_H_implication` --[t_reductio_ad_absurdum]--> output: `s_graph_removal_lemma`

**Techniques used:** t_compose_with_identity, t_auxiliary_construction, t_reductio_ad_absurdum

---

### Corners theorem (Ajtai–Szemerédi) (cite: https://en.wikipedia.org/wiki/Corners_theorem)

**Axioms:** `s_positive_density_subset`, `s_two_dimensional_lattice`
**Terminal:** `s_corners_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_positive_density_subset, s_two_dimensional_lattice⟩` --[t_axiomatize_from_instances {target: "positive density A ⊆ [N]² contains corner (x,y),(x+d,y),(x,y+d)"}]--> output: `s_corner_target`
2. input: `s_corner_target` --[t_compose_with_identity {apply: "triangle removal lemma to auxiliary tripartite graph"}]--> output: `s_triangle_removal_yields_corner`
3. input: `s_triangle_removal_yields_corner` --[t_exhaustion_squeeze]--> output: `s_corners_theorem`

**Techniques used:** t_axiomatize_from_instances, t_compose_with_identity, t_exhaustion_squeeze

---

### Szemerédi–Trotter theorem (incidence) (cite: https://en.wikipedia.org/wiki/Szemer%C3%A9di%E2%80%93Trotter_theorem)

**Axioms:** `s_finite_point_set_in_plane`, `s_finite_line_set_in_plane`
**Terminal:** `s_szemeredi_trotter_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_point_set_in_plane, s_finite_line_set_in_plane⟩` --[t_axiomatize_from_instances {target: "I(P,L) = O((|P||L|)^{2/3} + |P| + |L|)"}]--> output: `s_szemeredi_trotter_target`
2. input: `s_szemeredi_trotter_target` --[t_auxiliary_construction {tool: "cell decomposition by random sample of lines"}]--> output: `s_cutting_into_cells_count_incidences_per_cell`
3. input: `s_cutting_into_cells_count_incidences_per_cell` --[t_exhaustion_squeeze]--> output: `s_szemeredi_trotter_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_exhaustion_squeeze

---

### Erdős–Pósa theorem (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93P%C3%B3sa_theorem)

**Axioms:** `s_graph_definition`, `s_disjoint_cycle_packing_vs_cover`
**Terminal:** `s_erdos_posa_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_disjoint_cycle_packing_vs_cover⟩` --[t_duality {pack_cover: "k disjoint cycles or O(k log k) vertices covering all cycles"}]--> output: `s_erdos_posa_dual_target`
2. input: `s_erdos_posa_dual_target` --[t_auxiliary_construction {tool: "DFS tree + back edges decomposition"}]--> output: `s_dfs_back_edges_yield_disjoint_cycles_or_small_FVS`
3. input: `s_dfs_back_edges_yield_disjoint_cycles_or_small_FVS` --[t_exhaustion_squeeze]--> output: `s_erdos_posa_theorem`

**Techniques used:** t_duality, t_auxiliary_construction, t_exhaustion_squeeze

---

### Erdős–Ko–Rado for vector spaces (q-analog) (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Ko%E2%80%93Rado_theorem#q-analogs)

**Axioms:** `s_finite_dim_vector_space_over_F_q`, `s_intersecting_family_property`
**Terminal:** `s_q_analog_ekr_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_dim_vector_space_over_F_q, s_intersecting_family_property⟩` --[t_axiomatize_from_instances {target: "max intersecting family of k-subspaces"}]--> output: `s_q_ekr_target`
2. input: `s_q_ekr_target` --[t_double_centralizer_decompose {scheme: "Grassmann association scheme eigenvalues"}]--> output: `s_grassmann_scheme_eigen_optimum`
3. input: `s_grassmann_scheme_eigen_optimum` --[t_exhaustion_squeeze]--> output: `s_q_analog_ekr_theorem`

**Techniques used:** t_axiomatize_from_instances, t_double_centralizer_decompose, t_exhaustion_squeeze

---

## V. ENUMERATIVE COMBINATORICS (39–48)

### Cayley's formula (n^{n-2} trees) (cite: https://en.wikipedia.org/wiki/Cayley%27s_formula)

**Axioms:** `s_labeled_tree_definition`, `s_naturals_with_multiplication`
**Terminal:** `s_cayley_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_labeled_tree_definition, s_naturals_with_multiplication⟩` --[t_spot_pattern_in_table {data: "n=1,2,3,4 ↦ 1,1,3,16,125"}]--> output: `s_cayley_conjecture_n_n_minus_2`
2. input: `s_cayley_conjecture_n_n_minus_2` --[t_structural_isomorphism {bijection: "Prüfer sequence: tree ↔ word in [n]^{n-2}"}]--> output: `s_prufer_bijection`
3. input: `s_prufer_bijection` --[t_exhaustion_squeeze]--> output: `s_cayley_formula`

**Techniques used:** t_spot_pattern_in_table, t_structural_isomorphism, t_exhaustion_squeeze

---

### Kirchhoff's matrix-tree theorem (cite: https://en.wikipedia.org/wiki/Kirchhoff%27s_theorem)

**Axioms:** `s_graph_definition`, `s_laplacian_matrix_of_graph`
**Terminal:** `s_matrix_tree_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_laplacian_matrix_of_graph⟩` --[t_auxiliary_construction {object: "signed incidence matrix B"}]--> output: `s_incidence_matrix_factorisation_L_eq_B_B_T`
2. input: `s_incidence_matrix_factorisation_L_eq_B_B_T` --[t_svd_and_spectral_decomposition {cauchy_binet: "expand det of minor as sum over k-subsets"}]--> output: `s_cauchy_binet_expansion_of_principal_minor`
3. input: `s_cauchy_binet_expansion_of_principal_minor` --[t_structural_isomorphism {nonzero_terms: "each = ±1 ↔ spanning tree"}]--> output: `s_matrix_tree_theorem`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_structural_isomorphism

---

### Lindström–Gessel–Viennot lemma (cite: https://en.wikipedia.org/wiki/Lindstr%C3%B6m%E2%80%93Gessel%E2%80%93Viennot_lemma)

**Axioms:** `s_acyclic_directed_graph_with_weights`, `s_non_intersecting_lattice_paths_problem`
**Terminal:** `s_lgv_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_acyclic_directed_graph_with_weights, s_non_intersecting_lattice_paths_problem⟩` --[t_auxiliary_construction {object: "path matrix M_{ij} = weighted sum of paths a_i → b_j"}]--> output: `s_path_matrix_M_setup`
2. input: `s_path_matrix_M_setup` --[t_symmetry_reduction {involution: "swap-tails at first crossing pairs"}]--> output: `s_sign_reversing_involution_on_crossing_path_systems`
3. input: `s_sign_reversing_involution_on_crossing_path_systems` --[t_exhaustion_squeeze {det_M_eq_sum_non_intersecting: "fixed points = non-intersecting systems"}]--> output: `s_lgv_lemma`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_exhaustion_squeeze

---

### RSK correspondence (cite: https://en.wikipedia.org/wiki/Robinson%E2%80%93Schensted%E2%80%93Knuth_correspondence)

**Axioms:** `s_finite_matrix_nonneg_integer_entries`, `s_pair_of_young_tableaux`
**Terminal:** `s_rsk_correspondence` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_matrix_nonneg_integer_entries, s_pair_of_young_tableaux⟩` --[t_axiomatize_from_instances {claim: "bijection ℕ-matrices ↔ pairs (P,Q) of same-shape SSYT"}]--> output: `s_rsk_target`
2. input: `s_rsk_target` --[t_auxiliary_construction {insertion: "row-insertion algorithm"}]--> output: `s_row_insertion_algorithm_well_defined`
3. input: `s_row_insertion_algorithm_well_defined` --[t_structural_isomorphism {invertibility: "uninsertion algorithm"}]--> output: `s_rsk_correspondence`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism

---

### Hook-length formula (cite: https://en.wikipedia.org/wiki/Hook_length_formula)

**Axioms:** `s_partition_lambda`, `s_standard_young_tableau`
**Terminal:** `s_hook_length_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_partition_lambda, s_standard_young_tableau⟩` --[t_spot_pattern_in_table {small_partitions: "λ=(2,1) gives 2 SYT"}]--> output: `s_hook_formula_conjecture`
2. input: `s_hook_formula_conjecture` --[t_auxiliary_construction {nps_proof: "Novelli–Pak–Stoyanovskii hook walk algorithm"}]--> output: `s_hook_walk_bijection_setup`
3. input: `s_hook_walk_bijection_setup` --[t_probabilistic_existence {expected_value: "uniform random cell argument"}]--> output: `s_uniform_random_tableau_distribution_argument`
4. input: `s_uniform_random_tableau_distribution_argument` --[t_exhaustion_squeeze]--> output: `s_hook_length_formula`

**Techniques used:** t_spot_pattern_in_table, t_auxiliary_construction, t_probabilistic_existence, t_exhaustion_squeeze

---

### Pólya enumeration theorem (cite: https://en.wikipedia.org/wiki/P%C3%B3lya_enumeration_theorem)

**Axioms:** `s_finite_group`, `s_group_action_on_set_of_colorings`
**Terminal:** `s_polya_enumeration_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_group_action_on_set_of_colorings⟩` --[t_character_decomposition_count {tool: "Burnside lemma: |orbits| = (1/|G|) Σ |Fix(g)|"}]--> output: `s_burnside_lemma`
2. input: `s_burnside_lemma` --[t_auxiliary_construction {cycle_index: "Z_G(x_1,…,x_n) = (1/|G|) Σ_g Π x_{c_k}^{j_k(g)}"}]--> output: `s_cycle_index_polynomial`
3. input: `s_cycle_index_polynomial` --[t_compose_with_identity {substitute: "x_k ↦ Σ_c w(c)^k"}]--> output: `s_polya_enumeration_theorem`

**Techniques used:** t_character_decomposition_count, t_auxiliary_construction, t_compose_with_identity

---

### Burnside's lemma (orbit counting) (cite: https://en.wikipedia.org/wiki/Burnside%27s_lemma)

**Axioms:** `s_finite_group`, `s_group_action`
**Terminal:** `s_burnside_orbit_counting` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_group_action⟩` --[t_auxiliary_construction {object: "incidence relation R = {(g,x) : g·x = x}"}]--> output: `s_incidence_relation_R`
2. input: `s_incidence_relation_R` --[t_character_decomposition_count {double_count: "|R| = Σ_g |Fix(g)| = Σ_x |G_x|"}]--> output: `s_double_count_fix_stabilizer_identity`
3. input: `s_double_count_fix_stabilizer_identity` --[t_compose_with_identity {orbit_stabilizer: "|G|/|G_x| = |orbit(x)|"}]--> output: `s_burnside_orbit_counting`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_compose_with_identity

---

### Lagrange inversion theorem (cite: https://en.wikipedia.org/wiki/Lagrange_inversion_theorem)

**Axioms:** `s_formal_power_series_ring`, `s_compositional_inverse_problem`
**Terminal:** `s_lagrange_inversion_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_formal_power_series_ring, s_compositional_inverse_problem⟩` --[t_axiomatize_from_instances {target: "[z^n] f^{-1}(z) = (1/n)[w^{n-1}] (w/φ(w))^n"}]--> output: `s_lagrange_inversion_target`
2. input: `s_lagrange_inversion_target` --[t_complex_analysis_to_integers {contour: "residue at z=0 via Cauchy"}]--> output: `s_residue_calculation_of_coefficient`
3. input: `s_residue_calculation_of_coefficient` --[t_exhaustion_squeeze]--> output: `s_lagrange_inversion_theorem`

**Techniques used:** t_axiomatize_from_instances, t_complex_analysis_to_integers, t_exhaustion_squeeze

---

### MacMahon's master theorem (cite: https://en.wikipedia.org/wiki/MacMahon_master_theorem)

**Axioms:** `s_formal_power_series_ring`, `s_finite_matrix_nonneg_integer_entries`
**Terminal:** `s_macmahon_master_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_formal_power_series_ring, s_finite_matrix_nonneg_integer_entries⟩` --[t_axiomatize_from_instances {target: "Σ diagonal coefficient (Ax)^m = 1/det(I - X·A)"}]--> output: `s_macmahon_target`
2. input: `s_macmahon_target` --[t_complex_analysis_to_integers {tool: "multivariate residue / Foata's proof"}]--> output: `s_residue_extraction_diagonal_coefficient`
3. input: `s_residue_extraction_diagonal_coefficient` --[t_exhaustion_squeeze]--> output: `s_macmahon_master_theorem`

**Techniques used:** t_axiomatize_from_instances, t_complex_analysis_to_integers, t_exhaustion_squeeze

---

### Stanley's reciprocity theorem (cite: https://en.wikipedia.org/wiki/Stanley%27s_reciprocity_theorem)

**Axioms:** `s_rational_cone_in_R_n`, `s_lattice_point_enumerator`
**Terminal:** `s_stanley_reciprocity_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_rational_cone_in_R_n, s_lattice_point_enumerator⟩` --[t_axiomatize_from_instances {target: "σ_K(1/z) = (-1)^d σ_{K°}(z)"}]--> output: `s_reciprocity_target`
2. input: `s_reciprocity_target` --[t_duality {polar_dual: "interior cone K° ↔ closed cone K"}]--> output: `s_polar_duality_on_cones`
3. input: `s_polar_duality_on_cones` --[t_complex_analysis_to_integers {brion: "Brion's decomposition + residue"}]--> output: `s_stanley_reciprocity_theorem`

**Techniques used:** t_axiomatize_from_instances, t_duality, t_complex_analysis_to_integers

---

## VI. GRAPH COLORING & STRUCTURE (49–58)

### Five color theorem (cite: https://en.wikipedia.org/wiki/Five_color_theorem)

**Axioms:** `s_planar_graph`, `s_proper_vertex_coloring`
**Terminal:** `s_five_color_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_planar_graph, s_proper_vertex_coloring⟩` --[t_axiomatize_from_instances {target: "every planar graph 5-colorable"}]--> output: `s_5_color_target`
2. input: `s_5_color_target` --[t_compose_with_identity {euler: "δ(G) ≤ 5 for planar G via Euler's formula"}]--> output: `s_min_degree_at_most_five_lemma`
3. input: `s_min_degree_at_most_five_lemma` --[t_infinite_descent {induction: "delete deg-≤5 vertex, recolor by Kempe chain"}]--> output: `s_kempe_chain_recoloring_argument`
4. input: `s_kempe_chain_recoloring_argument` --[t_exhaustion_squeeze]--> output: `s_five_color_theorem`

**Techniques used:** t_axiomatize_from_instances, t_compose_with_identity, t_infinite_descent, t_exhaustion_squeeze

---

### Brooks' theorem (cite: https://en.wikipedia.org/wiki/Brooks%27_theorem)

**Axioms:** `s_graph_definition`, `s_proper_vertex_coloring`
**Terminal:** `s_brooks_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_proper_vertex_coloring⟩` --[t_axiomatize_from_instances {target: "χ(G) ≤ Δ(G) unless G is K_{Δ+1} or odd cycle"}]--> output: `s_brooks_target`
2. input: `s_brooks_target` --[t_auxiliary_construction {ordering: "good DFS / nonseparating ear ordering"}]--> output: `s_good_vertex_ordering_with_two_nonadjacent_priors`
3. input: `s_good_vertex_ordering_with_two_nonadjacent_priors` --[t_exhaustion_squeeze]--> output: `s_brooks_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_exhaustion_squeeze

---

### Vizing's theorem (cite: https://en.wikipedia.org/wiki/Vizing%27s_theorem)

**Axioms:** `s_graph_definition`, `s_edge_chromatic_number`
**Terminal:** `s_vizing_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_edge_chromatic_number⟩` --[t_axiomatize_from_instances {target: "χ'(G) ∈ {Δ(G), Δ(G)+1}"}]--> output: `s_vizing_target`
2. input: `s_vizing_target` --[t_auxiliary_construction {fan: "Vizing fan / multifan around an edge"}]--> output: `s_vizing_fan_recoloring_setup`
3. input: `s_vizing_fan_recoloring_setup` --[t_infinite_descent {iterate: "flip colour along fan + Kempe chain"}]--> output: `s_vizing_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_infinite_descent

---

### Grötzsch's theorem (cite: https://en.wikipedia.org/wiki/Gr%C3%B6tzsch%27s_theorem)

**Axioms:** `s_planar_graph`, `s_triangle_free_graph_property`
**Terminal:** `s_grotzsch_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_planar_graph, s_triangle_free_graph_property⟩` --[t_axiomatize_from_instances {target: "triangle-free planar G is 3-colorable"}]--> output: `s_grotzsch_target`
2. input: `s_grotzsch_target` --[t_auxiliary_construction {discharge: "discharging argument + reducible configurations"}]--> output: `s_reducible_configurations_for_3_coloring`
3. input: `s_reducible_configurations_for_3_coloring` --[t_finite_case_check {check: "unavoidable + reducible set"}]--> output: `s_grotzsch_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_finite_case_check

---

### Kuratowski's theorem (planarity) (cite: https://en.wikipedia.org/wiki/Kuratowski%27s_theorem)

**Axioms:** `s_graph_definition`, `s_planar_embedding_definition`
**Terminal:** `s_kuratowski_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_planar_embedding_definition⟩` --[t_axiomatize_from_instances {target: "G planar ⇔ no K_5 or K_{3,3} subdivision"}]--> output: `s_kuratowski_target`
2. input: `s_kuratowski_target` --[t_obstruction_class {non_planar_obstruction: "K_5 and K_{3,3} as minimal forbidden minors"}]--> output: `s_minimal_non_planar_obstructions_K5_K33`
3. input: `s_minimal_non_planar_obstructions_K5_K33` --[t_reductio_ad_absurdum {block_decomp: "reduce to 3-connected case, case analysis"}]--> output: `s_kuratowski_theorem`

**Techniques used:** t_axiomatize_from_instances, t_obstruction_class, t_reductio_ad_absurdum

---

### Wagner's theorem (cite: https://en.wikipedia.org/wiki/Wagner%27s_theorem)

**Axioms:** `s_graph_definition`, `s_minor_ordering`
**Terminal:** `s_wagner_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_minor_ordering⟩` --[t_axiomatize_from_instances {target: "G planar ⇔ no K_5 or K_{3,3} minor"}]--> output: `s_wagner_target`
2. input: `s_wagner_target` --[t_structural_isomorphism {equivalence: "minor ↔ topological minor in low max-deg case"}]--> output: `s_minor_vs_topological_minor_equivalence`
3. input: `s_minor_vs_topological_minor_equivalence` --[t_compose_with_identity {apply: "Kuratowski"}]--> output: `s_wagner_theorem`

**Techniques used:** t_axiomatize_from_instances, t_structural_isomorphism, t_compose_with_identity

---

### Fáry's theorem (cite: https://en.wikipedia.org/wiki/F%C3%A1ry%27s_theorem)

**Axioms:** `s_planar_graph`, `s_straight_line_embedding_definition`
**Terminal:** `s_fary_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_planar_graph, s_straight_line_embedding_definition⟩` --[t_axiomatize_from_instances {target: "every planar graph has straight-line embedding"}]--> output: `s_fary_target`
2. input: `s_fary_target` --[t_infinite_descent {induction: "induct on |V|; convex position of outer face"}]--> output: `s_inductive_straightening_of_edges`
3. input: `s_inductive_straightening_of_edges` --[t_exhaustion_squeeze]--> output: `s_fary_theorem`

**Techniques used:** t_axiomatize_from_instances, t_infinite_descent, t_exhaustion_squeeze

---

### Steinitz's theorem (polytopes ↔ planar 3-connected) (cite: https://en.wikipedia.org/wiki/Steinitz%27s_theorem)

**Axioms:** `s_convex_polyhedron`, `s_planar_graph`
**Terminal:** `s_steinitz_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_convex_polyhedron, s_planar_graph⟩` --[t_axiomatize_from_instances {target: "G is 1-skeleton of 3-polytope ⇔ G planar 3-connected"}]--> output: `s_steinitz_target`
2. input: `s_steinitz_target` --[t_structural_isomorphism {tutte_embedding: "Tutte spring / rubber-band embedding"}]--> output: `s_tutte_rubber_band_realisation`
3. input: `s_tutte_rubber_band_realisation` --[t_raise_dimension {lift: "Maxwell–Cremona lift to ℝ³ convex"}]--> output: `s_steinitz_theorem`

**Techniques used:** t_axiomatize_from_instances, t_structural_isomorphism, t_raise_dimension

---

### Perfect graph theorem (Lovász) (cite: https://en.wikipedia.org/wiki/Perfect_graph_theorem)

**Axioms:** `s_graph_definition`, `s_perfect_graph_definition`
**Terminal:** `s_lovasz_perfect_graph_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_perfect_graph_definition⟩` --[t_axiomatize_from_instances {target: "G perfect ⇔ Ḡ perfect"}]--> output: `s_perfect_complement_target`
2. input: `s_perfect_complement_target` --[t_duality {complement: "α(G) = ω(Ḡ); chromatic ↔ clique cover"}]--> output: `s_complement_duality_on_perfection`
3. input: `s_perfect_complement_target` --[t_auxiliary_construction {replication: "replication / blow-up lemma"}]--> output: `s_replication_lemma`
4. input: `s_replication_lemma` --[t_exhaustion_squeeze]--> output: `s_lovasz_perfect_graph_theorem`

**Techniques used:** t_axiomatize_from_instances, t_duality, t_auxiliary_construction, t_exhaustion_squeeze

---

### Strong perfect graph theorem (cite: https://en.wikipedia.org/wiki/Strong_perfect_graph_theorem)

**Axioms:** `s_graph_definition`, `s_perfect_graph_definition`
**Terminal:** `s_strong_perfect_graph_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_perfect_graph_definition⟩` --[t_axiomatize_from_instances {target: "G perfect ⇔ no odd hole and no odd antihole"}]--> output: `s_spgt_target`
2. input: `s_spgt_target` --[t_obstruction_class {minimal_imperfect: "Berge graphs vs. odd-hole/odd-antihole"}]--> output: `s_berge_graph_decomposition_skeleton`
3. input: `s_berge_graph_decomposition_skeleton` --[t_finite_case_check {chudnovsky_robertson_seymour_thomas: "structure theorem case analysis"}]--> output: `s_strong_perfect_graph_theorem`

**Techniques used:** t_axiomatize_from_instances, t_obstruction_class, t_finite_case_check

---

## VII. PROBABILISTIC METHOD & RANDOM GRAPHS (59–66)

### Lovász local lemma (cite: https://en.wikipedia.org/wiki/Lov%C3%A1sz_local_lemma)

**Axioms:** `s_probability_axioms`, `s_dependency_graph_of_events`
**Terminal:** `s_lovasz_local_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms, s_dependency_graph_of_events⟩` --[t_axiomatize_from_instances {target: "avoid all bad events when 4·d·p ≤ 1"}]--> output: `s_lll_target`
2. input: `s_lll_target` --[t_auxiliary_construction {weights: "weights x_A ∈ (0,1) verifying Pr(A) ≤ x_A Π_B (1-x_B)"}]--> output: `s_weight_certificate_for_lll`
3. input: `s_weight_certificate_for_lll` --[t_infinite_descent {induction: "induct on |S| in Pr(A | ∩_{B∈S} B^c)"}]--> output: `s_lovasz_local_lemma`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_infinite_descent

---

### Erdős probabilistic lower bound on R(k,k) (cite: https://en.wikipedia.org/wiki/Ramsey%27s_theorem)

**Axioms:** `s_probability_axioms`, `s_graph_definition`
**Terminal:** `s_erdos_ramsey_lower_bound` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms, s_graph_definition⟩` --[t_auxiliary_construction {object: "uniform random 2-coloring of K_n edges"}]--> output: `s_uniform_random_two_coloring_of_K_n`
2. input: `s_uniform_random_two_coloring_of_K_n` --[t_probabilistic_existence {expected_monochromatic_K_k: "C(n,k) · 2^{1 - C(k,2)} < 1"}]--> output: `s_expected_count_less_than_one`
3. input: `s_expected_count_less_than_one` --[t_exhaustion_squeeze]--> output: `s_erdos_ramsey_lower_bound`

**Techniques used:** t_auxiliary_construction, t_probabilistic_existence, t_exhaustion_squeeze

---

### Spencer's six standard deviations (cite: https://en.wikipedia.org/wiki/Six_standard_deviations_suffice)

**Axioms:** `s_set_system_on_n_points`, `s_signed_coloring_problem`
**Terminal:** `s_spencer_six_sigma_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_set_system_on_n_points, s_signed_coloring_problem⟩` --[t_axiomatize_from_instances {target: "discrepancy ≤ 6√n for any n-set system on n points"}]--> output: `s_spencer_target`
2. input: `s_spencer_target` --[t_auxiliary_construction {partial_coloring: "entropy / pigeonhole on ±1 signings"}]--> output: `s_partial_coloring_lemma_entropy_bucket`
3. input: `s_partial_coloring_lemma_entropy_bucket` --[t_infinite_descent {iterate: "halve unfrozen, accumulate ≤ 6√n bound"}]--> output: `s_spencer_six_sigma_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_infinite_descent

---

### Beck–Fiala theorem (cite: https://en.wikipedia.org/wiki/Beck%E2%80%93Fiala_theorem)

**Axioms:** `s_set_system_on_n_points`, `s_signed_coloring_problem`
**Terminal:** `s_beck_fiala_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_set_system_on_n_points, s_signed_coloring_problem⟩` --[t_axiomatize_from_instances {target: "discrepancy ≤ 2t-1 if each point in ≤ t sets"}]--> output: `s_beck_fiala_target`
2. input: `s_beck_fiala_target` --[t_auxiliary_construction {polytope: "iterative LP: float fractional coordinates"}]--> output: `s_floating_lp_iteration`
3. input: `s_floating_lp_iteration` --[t_exhaustion_squeeze]--> output: `s_beck_fiala_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_exhaustion_squeeze

---

### Beck's three-coloring theorem (cite: https://en.wikipedia.org/wiki/Beck%27s_theorem_(geometry))

**Axioms:** `s_set_system_on_n_points`, `s_signed_coloring_problem`
**Terminal:** `s_beck_three_coloring_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_set_system_on_n_points, s_signed_coloring_problem⟩` --[t_axiomatize_from_instances {target: "any n-uniform hypergraph with ≤ 2^{n-3}n edges is 2-colorable"}]--> output: `s_beck_three_color_target`
2. input: `s_beck_three_color_target` --[t_probabilistic_existence {random: "random ±1 colouring, control bad-event prob"}]--> output: `s_random_two_coloring_and_local_correction`
3. input: `s_random_two_coloring_and_local_correction` --[t_compose_with_identity {apply: "Lovász local lemma"}]--> output: `s_beck_three_coloring_theorem`

**Techniques used:** t_axiomatize_from_instances, t_probabilistic_existence, t_compose_with_identity

---

### Erdős–Rényi threshold for connectivity (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model)

**Axioms:** `s_probability_axioms`, `s_random_graph_G_n_p_model`
**Terminal:** `s_erdos_renyi_connectivity_threshold` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms, s_random_graph_G_n_p_model⟩` --[t_axiomatize_from_instances {target: "p = (log n + c)/n is sharp threshold for connectivity"}]--> output: `s_threshold_target`
2. input: `s_threshold_target` --[t_auxiliary_construction {first_moment: "E[isolated vertices] = n(1-p)^{n-1}"}]--> output: `s_first_moment_isolated_vertices`
3. input: `s_first_moment_isolated_vertices` --[t_probabilistic_existence {second_moment: "Var control"}]--> output: `s_second_moment_estimate`
4. input: `s_second_moment_estimate` --[t_exhaustion_squeeze]--> output: `s_erdos_renyi_connectivity_threshold`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_probabilistic_existence, t_exhaustion_squeeze

---

### Erdős–Szekeres monotone subsequence theorem (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Szekeres_theorem)

**Axioms:** `s_finite_sequence_of_reals`, `s_monotone_subsequence_problem`
**Terminal:** `s_erdos_szekeres_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_sequence_of_reals, s_monotone_subsequence_problem⟩` --[t_axiomatize_from_instances {target: "every sequence of (r-1)(s-1)+1 reals has inc subseq of length r or dec of length s"}]--> output: `s_es_target`
2. input: `s_es_target` --[t_auxiliary_construction {pair_label: "(a_i, b_i) = (longest inc ending at i, longest dec ending at i)"}]--> output: `s_pair_labels_distinct`
3. input: `s_pair_labels_distinct` --[t_pigeonhole_collision]--> output: `s_erdos_szekeres_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_pigeonhole_collision

---

### Friendship theorem (Erdős–Rényi–Sós) (cite: https://en.wikipedia.org/wiki/Friendship_theorem)

**Axioms:** `s_graph_definition`, `s_friendship_condition_every_pair_unique_common_neighbor`
**Terminal:** `s_friendship_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_friendship_condition_every_pair_unique_common_neighbor⟩` --[t_axiomatize_from_instances {target: "friendship graph is windmill F_k"}]--> output: `s_friendship_target`
2. input: `s_friendship_target` --[t_svd_and_spectral_decomposition {adjacency: "A² = (k-1)I + J, eigenvalues"}]--> output: `s_adjacency_spectral_argument`
3. input: `s_adjacency_spectral_argument` --[t_reductio_ad_absurdum {regular_case: "k-regular ⇒ contradiction in trace mod"}]--> output: `s_friendship_theorem`

**Techniques used:** t_axiomatize_from_instances, t_svd_and_spectral_decomposition, t_reductio_ad_absurdum

---

## VIII. HAMILTONICITY & CLOSURE (67–72)

### Ore's theorem (cite: https://en.wikipedia.org/wiki/Ore%27s_theorem)

**Axioms:** `s_graph_definition`, `s_hamilton_cycle_problem`
**Terminal:** `s_ore_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_hamilton_cycle_problem⟩` --[t_axiomatize_from_instances {target: "deg(u)+deg(v) ≥ n for non-adjacent u,v ⇒ Hamiltonian"}]--> output: `s_ore_target`
2. input: `s_ore_target` --[t_reductio_ad_absurdum {longest_path: "extremal longest path P=v_1…v_n"}]--> output: `s_longest_path_endpoint_degree_sum_bound`
3. input: `s_longest_path_endpoint_degree_sum_bound` --[t_pigeonhole_collision {indices: "neighbors yield Hamilton cycle via cross-edges"}]--> output: `s_ore_theorem`

**Techniques used:** t_axiomatize_from_instances, t_reductio_ad_absurdum, t_pigeonhole_collision

---

### Bondy–Chvátal closure theorem (cite: https://en.wikipedia.org/wiki/Bondy%E2%80%93Chv%C3%A1tal_theorem)

**Axioms:** `s_graph_definition`, `s_hamilton_cycle_problem`
**Terminal:** `s_bondy_chvatal_closure_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_hamilton_cycle_problem⟩` --[t_axiomatize_from_instances {target: "G Hamiltonian ⇔ closure cl(G) is Hamiltonian"}]--> output: `s_closure_target`
2. input: `s_closure_target` --[t_auxiliary_construction {closure_op: "iteratively add edge uv when deg(u)+deg(v) ≥ n"}]--> output: `s_closure_operator_well_defined`
3. input: `s_closure_operator_well_defined` --[t_infinite_descent {invariance: "Hamiltonicity is closure-invariant"}]--> output: `s_bondy_chvatal_closure_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_infinite_descent

---

### Chvátal–Erdős theorem (cite: https://en.wikipedia.org/wiki/Chv%C3%A1tal%E2%80%93Erd%C5%91s_theorem)

**Axioms:** `s_graph_definition`, `s_hamilton_cycle_problem`
**Terminal:** `s_chvatal_erdos_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_hamilton_cycle_problem⟩` --[t_axiomatize_from_instances {target: "κ(G) ≥ α(G) ⇒ G Hamiltonian"}]--> output: `s_chvatal_erdos_target`
2. input: `s_chvatal_erdos_target` --[t_duality {connectivity_vs_independence: "Menger paths between independent set"}]--> output: `s_disjoint_paths_argument`
3. input: `s_disjoint_paths_argument` --[t_reductio_ad_absurdum {longest_cycle: "assume non-Hamiltonian, contradict α ≤ κ"}]--> output: `s_chvatal_erdos_theorem`

**Techniques used:** t_axiomatize_from_instances, t_duality, t_reductio_ad_absurdum

---

### Pósa's rotation-extension lemma (cite: https://en.wikipedia.org/wiki/P%C3%B3sa%27s_theorem)

**Axioms:** `s_graph_definition`, `s_hamilton_cycle_problem`
**Terminal:** `s_posa_rotation_extension_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_hamilton_cycle_problem⟩` --[t_axiomatize_from_instances {target: "expander ⇒ Hamiltonian via rotation-extension"}]--> output: `s_posa_target`
2. input: `s_posa_target` --[t_auxiliary_construction {rotation: "endpoint rotation on longest path"}]--> output: `s_endpoint_set_grows_under_rotation`
3. input: `s_posa_target` --[t_pigeonhole_collision {edge_back: "many endpoints + expansion ⇒ closing edge"}]--> output: `s_posa_rotation_extension_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_pigeonhole_collision

---

### Tutte's theorem on Hamilton cycles in 4-connected planar (cite: https://en.wikipedia.org/wiki/Tutte_theorem)

**Axioms:** `s_planar_graph`, `s_hamilton_cycle_problem`
**Terminal:** `s_tutte_hamilton_4connected_planar` (kind: theorem)

**Steps:**
1. input: `⟨s_planar_graph, s_hamilton_cycle_problem⟩` --[t_axiomatize_from_instances {target: "every 4-connected planar graph is Hamiltonian"}]--> output: `s_tutte_4conn_target`
2. input: `s_tutte_4conn_target` --[t_auxiliary_construction {tutte_path: "Tutte path with prescribed endpoints in a face"}]--> output: `s_tutte_path_construction`
3. input: `s_tutte_path_construction` --[t_infinite_descent {induction: "bridge decomposition"}]--> output: `s_tutte_hamilton_4connected_planar`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_infinite_descent

---

### Fleischner's theorem (cite: https://en.wikipedia.org/wiki/Fleischner%27s_theorem)

**Axioms:** `s_graph_definition`, `s_hamilton_cycle_problem`
**Terminal:** `s_fleischner_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition, s_hamilton_cycle_problem⟩` --[t_axiomatize_from_instances {target: "the square G² of a 2-connected graph is Hamiltonian"}]--> output: `s_fleischner_target`
2. input: `s_fleischner_target` --[t_auxiliary_construction {ear_decomposition: "open ear decomposition + DFS traversal"}]--> output: `s_dfs_ear_traversal_yields_hamilton_cycle_in_square`
3. input: `s_dfs_ear_traversal_yields_hamilton_cycle_in_square` --[t_exhaustion_squeeze]--> output: `s_fleischner_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_exhaustion_squeeze

---

## IX. ADDITIVE COMBINATORICS (73–80)

### Cauchy–Davenport theorem (cite: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Davenport_theorem)

**Axioms:** `s_prime_p`, `s_subsets_of_Z_p`
**Terminal:** `s_cauchy_davenport_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_prime_p, s_subsets_of_Z_p⟩` --[t_axiomatize_from_instances {target: "|A+B| ≥ min(p, |A|+|B|-1)"}]--> output: `s_cauchy_davenport_target`
2. input: `s_cauchy_davenport_target` --[t_polynomial_method {tool: "Combinatorial Nullstellensatz: nonzero coefficient ⇒ existence"}]--> output: `s_nullstellensatz_certificate_for_sumset`
3. input: `s_nullstellensatz_certificate_for_sumset` --[t_exhaustion_squeeze]--> output: `s_cauchy_davenport_theorem`

**Techniques used:** t_axiomatize_from_instances, t_polynomial_method, t_exhaustion_squeeze

---

### Erdős–Ginzburg–Ziv theorem (zero-sum) (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Ginzburg%E2%80%93Ziv_theorem)

**Axioms:** `s_integers`, `s_prime_p`
**Terminal:** `s_erdos_ginzburg_ziv_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_integers, s_prime_p⟩` --[t_axiomatize_from_instances {target: "among 2n-1 integers, n sum to 0 mod n"}]--> output: `s_egz_target`
2. input: `s_egz_target` --[t_reduce_to_canonical_form {n_eq_p_prime_case: "reduce general n to prime via multiplicativity"}]--> output: `s_reduction_to_prime_case`
3. input: `s_reduction_to_prime_case` --[t_polynomial_method {chevalley_warning: "Chevalley–Warning on two F_p polynomials"}]--> output: `s_erdos_ginzburg_ziv_theorem`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form, t_polynomial_method

---

### Davenport constant for abelian groups (cite: https://en.wikipedia.org/wiki/Davenport_constant)

**Axioms:** `s_finite_abelian_group`, `s_zero_sum_sequence_problem`
**Terminal:** `s_davenport_constant_theorem_for_p_groups` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_abelian_group, s_zero_sum_sequence_problem⟩` --[t_axiomatize_from_instances {target: "D(G) for elementary abelian p-group is 1+Σ(p_i - 1)"}]--> output: `s_davenport_target`
2. input: `s_davenport_target` --[t_polynomial_method {kemnitz_tool: "Chevalley–Warning on group ring"}]--> output: `s_chevalley_warning_for_abelian_p_group`
3. input: `s_chevalley_warning_for_abelian_p_group` --[t_exhaustion_squeeze]--> output: `s_davenport_constant_theorem_for_p_groups`

**Techniques used:** t_axiomatize_from_instances, t_polynomial_method, t_exhaustion_squeeze

---

### Kneser's addition theorem (cite: https://en.wikipedia.org/wiki/Kneser%27s_theorem_(combinatorics))

**Axioms:** `s_finite_abelian_group`, `s_sumset_definition`
**Terminal:** `s_kneser_addition_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_abelian_group, s_sumset_definition⟩` --[t_axiomatize_from_instances {target: "|A+B| ≥ |A| + |B| - |H| where H=stab(A+B)"}]--> output: `s_kneser_target`
2. input: `s_kneser_target` --[t_symmetry_reduction {stabilizer: "quotient by H = stab(A+B)"}]--> output: `s_quotient_by_stabilizer_gives_strict_sumset_growth`
3. input: `s_quotient_by_stabilizer_gives_strict_sumset_growth` --[t_infinite_descent {induct: "induct on |A|+|B|"}]--> output: `s_kneser_addition_theorem`

**Techniques used:** t_axiomatize_from_instances, t_symmetry_reduction, t_infinite_descent

---

### Plünnecke–Ruzsa inequality (cite: https://en.wikipedia.org/wiki/Pl%C3%BCnnecke%E2%80%93Ruzsa_inequality)

**Axioms:** `s_finite_abelian_group`, `s_sumset_definition`
**Terminal:** `s_plunnecke_ruzsa_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_abelian_group, s_sumset_definition⟩` --[t_axiomatize_from_instances {target: "|nA - mA| ≤ K^{n+m} |A| when |A+A| ≤ K|A|"}]--> output: `s_plunnecke_target`
2. input: `s_plunnecke_target` --[t_auxiliary_construction {graph_model: "addition graph with magnification ratios"}]--> output: `s_petridis_magnification_argument`
3. input: `s_petridis_magnification_argument` --[t_exhaustion_squeeze]--> output: `s_plunnecke_ruzsa_inequality`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_exhaustion_squeeze

---

### Freiman's theorem (cite: https://en.wikipedia.org/wiki/Freiman%27s_theorem)

**Axioms:** `s_integers`, `s_sumset_definition`
**Terminal:** `s_freiman_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_integers, s_sumset_definition⟩` --[t_axiomatize_from_instances {target: "|A+A| ≤ K|A| ⇒ A ⊆ generalised AP of bounded rank and size"}]--> output: `s_freiman_target`
2. input: `s_freiman_target` --[t_compose_with_identity {ruzsa_covering: "Ruzsa covering lemma + Plünnecke"}]--> output: `s_ruzsa_covering_applied`
3. input: `s_ruzsa_covering_applied` --[t_fourier_transform {bohr_sets: "Bohr-set ↔ generalised AP via Bogolyubov"}]--> output: `s_bogolyubov_bohr_set_inside_2A_minus_2A`
4. input: `s_bogolyubov_bohr_set_inside_2A_minus_2A` --[t_exhaustion_squeeze]--> output: `s_freiman_theorem`

**Techniques used:** t_axiomatize_from_instances, t_compose_with_identity, t_fourier_transform, t_exhaustion_squeeze

---

### Behrend's construction (large AP-free set) (cite: https://en.wikipedia.org/wiki/Salem%E2%80%93Spencer_set)

**Axioms:** `s_integers`, `s_three_term_AP_free_property`
**Terminal:** `s_behrend_construction_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_integers, s_three_term_AP_free_property⟩` --[t_axiomatize_from_instances {target: "exists 3-AP-free A ⊆ [N], |A| ≥ N · exp(-c√log N)"}]--> output: `s_behrend_target`
2. input: `s_behrend_target` --[t_raise_dimension {sphere_in_Z_m_d: "use lattice points on sphere of radius √r in [m]^d"}]--> output: `s_sphere_in_Z_m_d_is_AP_free`
3. input: `s_sphere_in_Z_m_d_is_AP_free` --[t_compose_with_identity {project: "base-m digit projection injects sphere ↦ [N]"}]--> output: `s_behrend_construction_theorem`

**Techniques used:** t_axiomatize_from_instances, t_raise_dimension, t_compose_with_identity

---

### Roth's theorem on 3-APs (cite: https://en.wikipedia.org/wiki/Roth%27s_theorem)

**Axioms:** `s_positive_density_subset`, `s_three_term_AP_free_property`
**Terminal:** `s_roth_theorem_3AP` (kind: theorem)

**Steps:**
1. input: `⟨s_positive_density_subset, s_three_term_AP_free_property⟩` --[t_axiomatize_from_instances {target: "positive density subset of ℤ contains 3-AP"}]--> output: `s_roth_target`
2. input: `s_roth_target` --[t_fourier_transform {l_infty_large: "1_A has large nontrivial Fourier coefficient"}]--> output: `s_large_fourier_coefficient_dichotomy`
3. input: `s_large_fourier_coefficient_dichotomy` --[t_major_minor_arc_decomposition {energy_increment: "density increment on long AP"}]--> output: `s_density_increment_iteration`
4. input: `s_density_increment_iteration` --[t_infinite_descent]--> output: `s_roth_theorem_3AP`

**Techniques used:** t_axiomatize_from_instances, t_fourier_transform, t_major_minor_arc_decomposition, t_infinite_descent

---

## X. APPENDIX — Skipped (already in canonical_node_index)

- Infinite Ramsey theorem → `s_ramsey_theorem_infinite`
- Szemerédi's theorem → `s_szemeredi_theorem_terminal`
- Green–Tao theorem → `s_green_tao`
- Four color theorem → `s_four_color_theorem`
- Graph minor theorem (Robertson–Seymour) → `s_graph_minor_theorem`
- Eulerian path criterion → `s_eulerian_path_criterion`

End of file.
