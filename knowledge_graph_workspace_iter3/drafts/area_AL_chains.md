# Area Algebra & Galois Theory Derivation Chains (iter-3)

**Source pages:**
- https://en.wikipedia.org/wiki/Category:Theorems_in_group_theory
- https://en.wikipedia.org/wiki/Category:Theorems_in_ring_theory
- https://en.wikipedia.org/wiki/Category:Galois_theory
- https://en.wikipedia.org/wiki/Category:Theorems_in_algebra
- https://en.wikipedia.org/wiki/Category:Theorems_in_representation_theory
- https://en.wikipedia.org/wiki/Category:Theorems_in_abstract_algebra

**Target:** 90 chains. **Drafted:** 133 (target exceeded — broader algebraic toolbox coverage). **Skipped (already in graph):** 6 — `s_sylow_theorems`, `s_cfsg`, `s_fundamental_theorem_of_galois_theory`, `s_abel_ruffini`, `s_hilbert_basis_theorem`, `s_nullstellensatz`. (Cardano, Ferrari, fundamental theorem of arithmetic, fundamental theorem of algebra are also in graph but belong to other areas.)
**Flagged (`⚠ needs new technique`):** 0.

---

### Cauchy's theorem (cite: https://en.wikipedia.org/wiki/Cauchy%27s_theorem_(group_theory))

**Axioms:** `s_finite_group`, `s_prime_p`
**Terminal:** `s_cauchy_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_prime_p⟩` --[t_auxiliary_construction {object: "set X of p-tuples (g_1,...,g_p) with product = e"}]--> output: `s_cauchy_p_tuple_set`
2. input: `s_cauchy_p_tuple_set` --[t_symmetry_reduction {group: "ℤ/p cyclic shift on X"}]--> output: `s_cyclic_action_on_p_tuples`
3. input: `s_cyclic_action_on_p_tuples` --[t_pigeonhole_collision {invariant: "|X| ≡ |fix(ℤ/p)| mod p"}]--> output: `s_fixed_point_count_divisible_by_p`
4. input: `s_fixed_point_count_divisible_by_p` --[t_finite_case_check {case: "constant tuple g^p = e forces |g|=p"}]--> output: `s_cauchy_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_pigeonhole_collision, t_finite_case_check

---

### Class equation (cite: https://en.wikipedia.org/wiki/Conjugacy_class#Conjugacy_class_equation)

**Axioms:** `s_finite_group`, `s_group_action`
**Terminal:** `s_class_equation` (kind: theorem)

**Steps:**
1. input: `s_finite_group` --[t_symmetry_reduction {action: "conjugation of G on itself"}]--> output: `s_conjugation_action_on_G`
2. input: `s_conjugation_action_on_G` --[t_axiomatize_from_instances {invariant: "orbits = conjugacy classes; stabilizers = centralizers"}]--> output: `s_orbit_stabilizer_for_conjugation`
3. input: `s_orbit_stabilizer_for_conjugation` --[t_character_decomposition_count {decomposition: "|G| = |Z(G)| + Σ [G:C_G(x_i)]"}]--> output: `s_class_equation`

**Techniques used:** t_symmetry_reduction, t_axiomatize_from_instances, t_character_decomposition_count

---

### Lagrange's theorem (cite: https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory))

**Axioms:** `s_finite_group`, `s_subgroup_H`
**Terminal:** `s_lagrange_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_subgroup_H⟩` --[t_auxiliary_construction {object: "left cosets gH"}]--> output: `s_coset_partition_of_G`
2. input: `s_coset_partition_of_G` --[t_structural_isomorphism {map: "g ↦ gh bijection H → gH"}]--> output: `s_cosets_equinumerous_to_H`
3. input: `s_cosets_equinumerous_to_H` --[t_character_decomposition_count {sum: "|G| = [G:H] · |H|"}]--> output: `s_lagrange_theorem`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_character_decomposition_count

---

### Orbit-stabilizer theorem (cite: https://en.wikipedia.org/wiki/Group_action#Orbit-stabilizer_theorem)

**Axioms:** `s_group_action`, `s_finite_group`
**Terminal:** `s_orbit_stabilizer_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_group_action, s_finite_group⟩` --[t_auxiliary_construction {map: "φ: G/Stab(x) → Orb(x), gStab(x) ↦ g·x"}]--> output: `s_coset_to_orbit_map`
2. input: `s_coset_to_orbit_map` --[t_structural_isomorphism {invariant: "φ well-defined and bijective"}]--> output: `s_orbit_isomorphic_to_coset_space`
3. input: `s_orbit_isomorphic_to_coset_space` --[t_character_decomposition_count {identity: "|Orb(x)| = [G : Stab(x)]"}]--> output: `s_orbit_stabilizer_theorem`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_character_decomposition_count

---

### Burnside's lemma (cite: https://en.wikipedia.org/wiki/Burnside%27s_lemma)

**Axioms:** `s_finite_group`, `s_group_action`
**Terminal:** `s_burnside_counting_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_group_action⟩` --[t_auxiliary_construction {object: "incidence set {(g,x) : g·x = x}"}]--> output: `s_fix_incidence_set`
2. input: `s_fix_incidence_set` --[t_character_decomposition_count {double_count: "Σ_g |Fix(g)| = Σ_x |Stab(x)|"}]--> output: `s_double_count_fix_stab`
3. input: `s_double_count_fix_stab` --[t_symmetry_reduction {orbit_stabilizer: "|Stab(x)| = |G|/|Orb(x)|"}]--> output: `s_burnside_counting_lemma`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_symmetry_reduction

---

### Burnside's p^a q^b solvability theorem (cite: https://en.wikipedia.org/wiki/Burnside_theorem)

**Axioms:** `s_finite_group_with_order_paqb`, `s_finite_group`
**Terminal:** `s_burnside_paqb_solvable` (kind: theorem)

**Steps:**
1. input: `s_finite_group_with_order_paqb` --[t_reductio_ad_absurdum {assume: "G is non-abelian simple of order p^a q^b"}]--> output: `s_hypothetical_simple_paqb_group`
2. input: `s_hypothetical_simple_paqb_group` --[t_character_decomposition_count {input: "irreducible characters χ_i of G"}]--> output: `s_character_table_of_G`
3. input: `s_character_table_of_G` --[t_auxiliary_construction {object: "conjugacy class C of size p^k; algebraic integer χ(g)/χ(1)·|C|"}]--> output: `s_algebraic_integer_relation`
4. input: `s_algebraic_integer_relation` --[t_complex_analysis_to_integers {step: "Galois average of |χ(g)|² shows χ(g)=0 or χ(1)||C|"}]--> output: `s_central_element_exists`
5. input: `s_central_element_exists` --[t_reductio_ad_absurdum {conclude: "nontrivial center contradicts simplicity"}]--> output: `s_burnside_paqb_solvable`

**Techniques used:** t_reductio_ad_absurdum, t_character_decomposition_count, t_auxiliary_construction, t_complex_analysis_to_integers

---

### Feit–Thompson odd-order theorem (cite: https://en.wikipedia.org/wiki/Feit%E2%80%93Thompson_theorem)

**Axioms:** `s_finite_group`, `s_odd_order_finite_group`
**Terminal:** `s_feit_thompson_theorem` (kind: theorem)

**Steps:**
1. input: `s_odd_order_finite_group` --[t_reductio_ad_absurdum {assume: "minimal counterexample G simple non-abelian odd"}]--> output: `s_minimal_simple_odd_group`
2. input: `s_minimal_simple_odd_group` --[t_finite_case_check {analysis: "maximal-subgroup structure & uniqueness subgroups"}]--> output: `s_maximal_subgroup_classification`
3. input: `s_maximal_subgroup_classification` --[t_character_decomposition_count {tool: "Dade's coherence / exceptional characters"}]--> output: `s_exceptional_character_relations`
4. input: `s_exceptional_character_relations` --[t_auxiliary_construction {generator: "CN-group analysis builds element of even order"}]--> output: `s_element_of_even_order_constructed`
5. input: `s_element_of_even_order_constructed` --[t_reductio_ad_absurdum {contradict: "even-order element in odd-order group"}]--> output: `s_feit_thompson_theorem`

**Techniques used:** t_reductio_ad_absurdum, t_finite_case_check, t_character_decomposition_count, t_auxiliary_construction

---

### Jordan–Hölder theorem (cite: https://en.wikipedia.org/wiki/Jordan%E2%80%93H%C3%B6lder_theorem)

**Axioms:** `s_finite_group`, `s_composition_series`
**Terminal:** `s_jordan_holder_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_composition_series⟩` --[t_auxiliary_construction {object: "two composition series Σ, Σ' for G"}]--> output: `s_two_composition_series`
2. input: `s_two_composition_series` --[t_structural_isomorphism {tool: "Zassenhaus butterfly lemma on H ∩ K"}]--> output: `s_zassenhaus_isomorphism`
3. input: `s_zassenhaus_isomorphism` --[t_infinite_descent {induction: "length of common refinement"}]--> output: `s_common_refinement_constructed`
4. input: `s_common_refinement_constructed` --[t_character_decomposition_count {multiset: "factors match up to permutation"}]--> output: `s_jordan_holder_theorem`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_infinite_descent, t_character_decomposition_count

---

### Schreier refinement theorem (cite: https://en.wikipedia.org/wiki/Schreier_refinement_theorem)

**Axioms:** `s_group_with_two_subnormal_series`, `s_finite_group`
**Terminal:** `s_schreier_refinement_theorem` (kind: theorem)

**Steps:**
1. input: `s_group_with_two_subnormal_series` --[t_auxiliary_construction {refinement: "insert H_i ∩ K_j and (H_i ∩ K_{j+1})·H_{i+1}"}]--> output: `s_zassenhaus_refined_terms`
2. input: `s_zassenhaus_refined_terms` --[t_structural_isomorphism {pair: "Zassenhaus lemma identifies isomorphic factor quotients"}]--> output: `s_isomorphic_factor_pairs`
3. input: `s_isomorphic_factor_pairs` --[t_character_decomposition_count {bijection: "factor multisets agree"}]--> output: `s_schreier_refinement_theorem`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_character_decomposition_count

---

### Krull–Schmidt theorem (cite: https://en.wikipedia.org/wiki/Krull%E2%80%93Schmidt_theorem)

**Axioms:** `s_finite_length_module`, `s_indecomposable_module`
**Terminal:** `s_krull_schmidt_theorem` (kind: theorem)

**Steps:**
1. input: `s_finite_length_module` --[t_auxiliary_construction {decomposition: "M = ⊕ M_i with M_i indecomposable"}]--> output: `s_indecomposable_decomposition`
2. input: `s_indecomposable_decomposition` --[t_structural_isomorphism {lemma: "End(M_i) local ring (Fitting lemma)"}]--> output: `s_local_endomorphism_rings`
3. input: `s_local_endomorphism_rings` --[t_double_centralizer_decompose {exchange: "swap summands across two decompositions"}]--> output: `s_summand_exchange_property`
4. input: `s_summand_exchange_property` --[t_character_decomposition_count {uniqueness: "multiset of M_i unique up to iso"}]--> output: `s_krull_schmidt_theorem`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_double_centralizer_decompose, t_character_decomposition_count

---

### Fundamental theorem of finitely generated abelian groups (cite: https://en.wikipedia.org/wiki/Finitely_generated_abelian_group#Classification)

**Axioms:** `s_finitely_generated_abelian_group`, `s_integers`
**Terminal:** `s_fundamental_theorem_fg_abelian` (kind: theorem)

**Steps:**
1. input: `s_finitely_generated_abelian_group` --[t_structural_isomorphism {map: "present as ℤ^n / Aℤ^m"}]--> output: `s_presentation_matrix_A`
2. input: `s_presentation_matrix_A` --[t_reduce_to_canonical_form {form: "Smith normal form via elementary row/col ops"}]--> output: `s_smith_normal_form_of_A`
3. input: `s_smith_normal_form_of_A` --[t_character_decomposition_count {decompose: "G ≅ ℤ^r ⊕ ⊕ ℤ/d_iℤ with d_1|...|d_k"}]--> output: `s_invariant_factor_decomposition`
4. input: `s_invariant_factor_decomposition` --[t_axiomatize_from_instances {uniqueness: "ranks and elementary divisors are invariants"}]--> output: `s_fundamental_theorem_fg_abelian`

**Techniques used:** t_structural_isomorphism, t_reduce_to_canonical_form, t_character_decomposition_count, t_axiomatize_from_instances

---

### Structure theorem for f.g. modules over a PID (cite: https://en.wikipedia.org/wiki/Structure_theorem_for_finitely_generated_modules_over_a_principal_ideal_domain)

**Axioms:** `s_principal_ideal_domain`, `s_finitely_generated_module_over_pid`
**Terminal:** `s_pid_structure_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_principal_ideal_domain, s_finitely_generated_module_over_pid⟩` --[t_auxiliary_construction {presentation: "R^m → R^n → M → 0"}]--> output: `s_module_presentation_over_R`
2. input: `s_module_presentation_over_R` --[t_reduce_to_canonical_form {form: "Smith normal form of presentation matrix"}]--> output: `s_smith_form_module_presentation`
3. input: `s_smith_form_module_presentation` --[t_character_decomposition_count {sum: "M ≅ R^r ⊕ ⊕ R/(d_i) with d_1|...|d_k"}]--> output: `s_invariant_factor_module_decomposition`
4. input: `s_invariant_factor_module_decomposition` --[t_duality {alternate: "primary decomposition via Chinese remainder on R/(d_i)"}]--> output: `s_pid_structure_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_character_decomposition_count, t_duality

---

### Smith normal form (cite: https://en.wikipedia.org/wiki/Smith_normal_form)

**Axioms:** `s_principal_ideal_domain`, `s_matrix_over_pid`
**Terminal:** `s_smith_normal_form_theorem` (kind: theorem)

**Steps:**
1. input: `s_matrix_over_pid` --[t_auxiliary_construction {operation: "GCD-driven row/column operations"}]--> output: `s_pivot_reduction_sequence`
2. input: `s_pivot_reduction_sequence` --[t_infinite_descent {invariant: "ideal generated by entries strictly descends"}]--> output: `s_descent_on_ideal_chain`
3. input: `s_descent_on_ideal_chain` --[t_reduce_to_canonical_form {target: "diagonal diag(d_1,...,d_r,0,...) with d_1|...|d_r"}]--> output: `s_smith_normal_form_theorem`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_reduce_to_canonical_form

---

### Cayley's theorem (cite: https://en.wikipedia.org/wiki/Cayley%27s_theorem)

**Axioms:** `s_finite_group`, `s_symmetric_group_Sn`
**Terminal:** `s_cayley_theorem` (kind: theorem)

**Steps:**
1. input: `s_finite_group` --[t_auxiliary_construction {map: "λ: G → Sym(G), g ↦ left mult by g"}]--> output: `s_left_regular_representation`
2. input: `s_left_regular_representation` --[t_structural_isomorphism {homomorphism: "λ injective into Sym(G)"}]--> output: `s_cayley_theorem`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism

---

### Nielsen–Schreier theorem (cite: https://en.wikipedia.org/wiki/Nielsen%E2%80%93Schreier_theorem)

**Axioms:** `s_free_group_F`, `s_subgroup_H`
**Terminal:** `s_nielsen_schreier_theorem` (kind: theorem)

**Steps:**
1. input: `s_free_group_F` --[t_auxiliary_construction {object: "Cayley graph (a tree) of F"}]--> output: `s_cayley_tree_of_F`
2. input: `s_cayley_tree_of_F` --[t_symmetry_reduction {quotient: "H acts freely on tree → quotient graph"}]--> output: `s_quotient_graph_by_H_action`
3. input: `s_quotient_graph_by_H_action` --[t_analysis_algebra_topology_bridge {fact: "π_1 of a graph is free"}]--> output: `s_pi1_of_quotient_is_free`
4. input: `s_pi1_of_quotient_is_free` --[t_structural_isomorphism {identification: "π_1(graph/H) ≅ H"}]--> output: `s_nielsen_schreier_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_analysis_algebra_topology_bridge, t_structural_isomorphism

---

### Kurosh subgroup theorem (cite: https://en.wikipedia.org/wiki/Kurosh_subgroup_theorem)

**Axioms:** `s_free_product_of_groups`, `s_subgroup_H`
**Terminal:** `s_kurosh_subgroup_theorem` (kind: theorem)

**Steps:**
1. input: `s_free_product_of_groups` --[t_auxiliary_construction {object: "Bass–Serre tree for G = ∗G_α"}]--> output: `s_bass_serre_tree_for_free_product`
2. input: `s_bass_serre_tree_for_free_product` --[t_symmetry_reduction {action: "H acts on the tree without inversions"}]--> output: `s_H_action_on_bass_serre_tree`
3. input: `s_H_action_on_bass_serre_tree` --[t_structural_isomorphism {decomp: "H = (∗_i H_i) ∗ F, with H_i conjugate-intersection of G_α and F free"}]--> output: `s_kurosh_subgroup_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_structural_isomorphism

---

### Grushko decomposition theorem (cite: https://en.wikipedia.org/wiki/Grushko_theorem)

**Axioms:** `s_finitely_generated_group_G`, `s_free_product_of_groups`
**Terminal:** `s_grushko_decomposition_theorem` (kind: theorem)

**Steps:**
1. input: `s_finitely_generated_group_G` --[t_auxiliary_construction {presentation: "G = A ∗ B; generating set"}]--> output: `s_generating_set_of_free_product`
2. input: `s_generating_set_of_free_product` --[t_symmetry_reduction {Stallings_folding: "fold the wedge of generating loops"}]--> output: `s_folded_graph_for_generators`
3. input: `s_folded_graph_for_generators` --[t_character_decomposition_count {rank_additivity: "rank(A∗B) = rank(A)+rank(B)"}]--> output: `s_grushko_decomposition_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_character_decomposition_count

---

### Stallings theorem on ends of groups (cite: https://en.wikipedia.org/wiki/Stallings_theorem_about_ends_of_groups)

**Axioms:** `s_finitely_generated_group_G`, `s_cayley_graph_of_G`
**Terminal:** `s_stallings_ends_theorem` (kind: theorem)

**Steps:**
1. input: `s_finitely_generated_group_G` --[t_auxiliary_construction {invariant: "number of ends e(G) of Cayley graph"}]--> output: `s_ends_invariant_of_G`
2. input: `s_ends_invariant_of_G` --[t_obstruction_class {dichotomy: "e(G) ∈ {0,1,2,∞}"}]--> output: `s_end_count_classification`
3. input: `s_end_count_classification` --[t_analysis_algebra_topology_bridge {action: "G acts on a tree from a splitting"}]--> output: `s_G_acts_on_tree_with_finite_edge_stabilizers`
4. input: `s_G_acts_on_tree_with_finite_edge_stabilizers` --[t_structural_isomorphism {Bass_Serre: "G splits as amalgamated product or HNN extension"}]--> output: `s_stallings_ends_theorem`

**Techniques used:** t_auxiliary_construction, t_obstruction_class, t_analysis_algebra_topology_bridge, t_structural_isomorphism

---

### Gromov's theorem on groups of polynomial growth (cite: https://en.wikipedia.org/wiki/Gromov%27s_theorem_on_groups_of_polynomial_growth)

**Axioms:** `s_finitely_generated_group_G`, `s_polynomial_growth_function`
**Terminal:** `s_gromov_polynomial_growth_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finitely_generated_group_G, s_polynomial_growth_function⟩` --[t_rescale_for_asymptotic_geometry {limit: "asymptotic cone of Cayley graph"}]--> output: `s_asymptotic_cone_of_G`
2. input: `s_asymptotic_cone_of_G` --[t_analysis_algebra_topology_bridge {bridge: "Montgomery–Zippin: locally compact connected ⇒ Lie group"}]--> output: `s_lie_group_acting_on_cone`
3. input: `s_lie_group_acting_on_cone` --[t_structural_isomorphism {Tits: "homomorphism G → Lie group with finite-index nilpotent kernel image"}]--> output: `s_gromov_polynomial_growth_theorem`

**Techniques used:** t_rescale_for_asymptotic_geometry, t_analysis_algebra_topology_bridge, t_structural_isomorphism

---

### Tits alternative (cite: https://en.wikipedia.org/wiki/Tits_alternative)

**Axioms:** `s_finitely_generated_linear_group`, `s_field_of_characteristic_zero`
**Terminal:** `s_tits_alternative_theorem` (kind: theorem)

**Steps:**
1. input: `s_finitely_generated_linear_group` --[t_reduce_to_canonical_form {Zariski_closure: "study Zariski closure G̅ ≤ GL_n"}]--> output: `s_zariski_closure_G`
2. input: `s_zariski_closure_G` --[t_finite_case_check {dichotomy: "either G̅° solvable, or contains non-trivial semisimple part"}]--> output: `s_semisimple_or_solvable_part`
3. input: `s_semisimple_or_solvable_part` --[t_auxiliary_construction {ping_pong: "find proximal elements; apply ping-pong lemma"}]--> output: `s_free_subgroup_via_ping_pong`
4. input: `s_free_subgroup_via_ping_pong` --[t_character_decomposition_count {conclusion: "virtually solvable OR contains free F_2"}]--> output: `s_tits_alternative_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_finite_case_check, t_auxiliary_construction, t_character_decomposition_count

---

### Fitting's theorem (cite: https://en.wikipedia.org/wiki/Fitting%27s_theorem)

**Axioms:** `s_finite_group`, `s_nilpotent_normal_subgroup`
**Terminal:** `s_fitting_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_nilpotent_normal_subgroup⟩` --[t_auxiliary_construction {object: "product N_1 N_2 of two nilpotent normal subgroups"}]--> output: `s_product_of_two_nilpotent_normals`
2. input: `s_product_of_two_nilpotent_normals` --[t_character_decomposition_count {commutator: "lower central series of N_1 N_2 bounded by sums of N_i classes"}]--> output: `s_nilpotency_class_bound`
3. input: `s_nilpotency_class_bound` --[t_axiomatize_from_instances {fitting_subgroup: "unique maximal nilpotent normal subgroup F(G)"}]--> output: `s_fitting_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_axiomatize_from_instances

---

### Schur–Zassenhaus theorem (cite: https://en.wikipedia.org/wiki/Schur%E2%80%93Zassenhaus_theorem)

**Axioms:** `s_finite_group`, `s_normal_hall_subgroup`
**Terminal:** `s_schur_zassenhaus_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_normal_hall_subgroup⟩` --[t_auxiliary_construction {extension: "1 → N → G → G/N → 1 with gcd(|N|,|G/N|)=1"}]--> output: `s_coprime_extension_sequence`
2. input: `s_coprime_extension_sequence` --[t_deformation_cohomology {vanish: "H^2(G/N, N) = 0 by coprime orders"}]--> output: `s_vanishing_h2_obstruction`
3. input: `s_vanishing_h2_obstruction` --[t_obstruction_class {split: "extension splits ⇒ complement exists"}]--> output: `s_complement_existence`
4. input: `s_complement_existence` --[t_symmetry_reduction {conjugacy: "H^1(G/N, N) = 0 ⇒ complements conjugate"}]--> output: `s_schur_zassenhaus_theorem`

**Techniques used:** t_auxiliary_construction, t_deformation_cohomology, t_obstruction_class, t_symmetry_reduction

---

### Frattini's argument (cite: https://en.wikipedia.org/wiki/Frattini%27s_argument)

**Axioms:** `s_finite_group`, `s_normal_subgroup_K`
**Terminal:** `s_frattini_argument` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_normal_subgroup_K⟩` --[t_auxiliary_construction {object: "Sylow p-subgroup P ≤ K"}]--> output: `s_sylow_in_normal_subgroup`
2. input: `s_sylow_in_normal_subgroup` --[t_symmetry_reduction {action: "G acts on Sylow subgroups of K by conjugation"}]--> output: `s_g_conjugation_on_sylow_set`
3. input: `s_g_conjugation_on_sylow_set` --[t_structural_isomorphism {factor: "G = K · N_G(P)"}]--> output: `s_frattini_argument`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_structural_isomorphism

---

### Fundamental theorem on homomorphisms / first isomorphism theorem (cite: https://en.wikipedia.org/wiki/Fundamental_theorem_on_homomorphisms)

**Axioms:** `s_group_homomorphism`, `s_finite_group`
**Terminal:** `s_first_isomorphism_theorem` (kind: theorem)

**Steps:**
1. input: `s_group_homomorphism` --[t_auxiliary_construction {object: "kernel K = ker(φ), image I = im(φ)"}]--> output: `s_kernel_image_of_phi`
2. input: `s_kernel_image_of_phi` --[t_structural_isomorphism {map: "φ̄: G/K → I, gK ↦ φ(g)"}]--> output: `s_induced_quotient_map`
3. input: `s_induced_quotient_map` --[t_axiomatize_from_instances {iso: "φ̄ well-defined bijective homomorphism"}]--> output: `s_first_isomorphism_theorem`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_axiomatize_from_instances

---

### Second isomorphism theorem (diamond) (cite: https://en.wikipedia.org/wiki/Isomorphism_theorems#Second_theorem)

**Axioms:** `s_subgroup_H`, `s_normal_subgroup_N`
**Terminal:** `s_second_isomorphism_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_subgroup_H, s_normal_subgroup_N⟩` --[t_auxiliary_construction {object: "HN and H ∩ N"}]--> output: `s_HN_and_intersection`
2. input: `s_HN_and_intersection` --[t_structural_isomorphism {map: "h(H∩N) ↦ hN"}]--> output: `s_diamond_iso_map`
3. input: `s_diamond_iso_map` --[t_axiomatize_from_instances {iso: "H/(H∩N) ≅ HN/N"}]--> output: `s_second_isomorphism_theorem`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_axiomatize_from_instances

---

### Third isomorphism theorem (cite: https://en.wikipedia.org/wiki/Isomorphism_theorems#Third_theorem)

**Axioms:** `s_normal_subgroup_N`, `s_normal_subgroup_K`
**Terminal:** `s_third_isomorphism_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_normal_subgroup_N, s_normal_subgroup_K⟩` --[t_auxiliary_construction {chain: "K ⊴ N ⊴ G"}]--> output: `s_nested_normal_chain`
2. input: `s_nested_normal_chain` --[t_structural_isomorphism {factor_through: "(G/K)/(N/K) ≅ G/N"}]--> output: `s_third_isomorphism_theorem`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism

---

### Correspondence theorem (lattice isomorphism) (cite: https://en.wikipedia.org/wiki/Correspondence_theorem)

**Axioms:** `s_normal_subgroup_N`, `s_quotient_group_G_mod_N`
**Terminal:** `s_correspondence_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_normal_subgroup_N, s_quotient_group_G_mod_N⟩` --[t_auxiliary_construction {map: "H ↔ H/N for N ≤ H ≤ G"}]--> output: `s_subgroup_correspondence_map`
2. input: `s_subgroup_correspondence_map` --[t_duality {lattice: "order-preserving and normality-preserving"}]--> output: `s_correspondence_theorem`

**Techniques used:** t_auxiliary_construction, t_duality

---

### Maschke's theorem (cite: https://en.wikipedia.org/wiki/Maschke%27s_theorem)

**Axioms:** `s_finite_group`, `s_field_of_char_coprime_to_G`
**Terminal:** `s_maschke_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_field_of_char_coprime_to_G⟩` --[t_auxiliary_construction {object: "kG-module V with submodule W; projection π_0: V→W"}]--> output: `s_naive_projection_to_W`
2. input: `s_naive_projection_to_W` --[t_symmetry_reduction {average: "π = (1/|G|) Σ_g g π_0 g^{-1}"}]--> output: `s_averaged_g_invariant_projection`
3. input: `s_averaged_g_invariant_projection` --[t_structural_isomorphism {split: "V = W ⊕ ker(π)"}]--> output: `s_maschke_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_structural_isomorphism

---

### Schur's lemma (cite: https://en.wikipedia.org/wiki/Schur%27s_lemma)

**Axioms:** `s_simple_module`, `s_module_homomorphism`
**Terminal:** `s_schurs_lemma` (kind: theorem)

**Steps:**
1. input: `s_module_homomorphism` --[t_auxiliary_construction {object: "kernel and image as submodules"}]--> output: `s_kernel_image_submodules`
2. input: `s_kernel_image_submodules` --[t_finite_case_check {cases: "simple ⇒ kernel/image is 0 or whole"}]--> output: `s_simplicity_dichotomy`
3. input: `s_simplicity_dichotomy` --[t_structural_isomorphism {end: "End(V) is a division ring; over alg closed = field"}]--> output: `s_schurs_lemma`

**Techniques used:** t_auxiliary_construction, t_finite_case_check, t_structural_isomorphism

---

### Wedderburn–Artin theorem (cite: https://en.wikipedia.org/wiki/Wedderburn%E2%80%93Artin_theorem)

**Axioms:** `s_semisimple_artinian_ring`, `s_division_ring`
**Terminal:** `s_wedderburn_artin_theorem` (kind: theorem)

**Steps:**
1. input: `s_semisimple_artinian_ring` --[t_auxiliary_construction {decompose: "R = ⊕ I_i as right R-modules, I_i simple"}]--> output: `s_simple_module_decomp_of_R`
2. input: `s_simple_module_decomp_of_R` --[t_double_centralizer_decompose {compute: "End(R_R) ≅ ∏ End(I_i^{n_i})"}]--> output: `s_endomorphism_ring_product`
3. input: `s_endomorphism_ring_product` --[t_structural_isomorphism {schur: "End(I_i) = D_i division ring; End(I_i^{n_i}) = M_{n_i}(D_i)"}]--> output: `s_matrix_rings_over_division_rings`
4. input: `s_matrix_rings_over_division_rings` --[t_axiomatize_from_instances {final: "R ≅ ∏ M_{n_i}(D_i), unique up to perm"}]--> output: `s_wedderburn_artin_theorem`

**Techniques used:** t_auxiliary_construction, t_double_centralizer_decompose, t_structural_isomorphism, t_axiomatize_from_instances

---

### Jacobson density theorem (cite: https://en.wikipedia.org/wiki/Jacobson_density_theorem)

**Axioms:** `s_simple_module`, `s_division_ring`
**Terminal:** `s_jacobson_density_theorem` (kind: theorem)

**Steps:**
1. input: `s_simple_module` --[t_double_centralizer_decompose {setup: "D = End_R(M), view M as D-vector space"}]--> output: `s_M_as_D_vector_space`
2. input: `s_M_as_D_vector_space` --[t_auxiliary_construction {goal: "for v_1,...,v_n D-linearly indep and w_1,...,w_n in M, find r with r·v_i=w_i"}]--> output: `s_interpolation_problem_in_M`
3. input: `s_interpolation_problem_in_M` --[t_projection_to_subspace {induction: "interpolate one coordinate at a time using simplicity"}]--> output: `s_jacobson_density_theorem`

**Techniques used:** t_double_centralizer_decompose, t_auxiliary_construction, t_projection_to_subspace

---

### Double centralizer theorem (cite: https://en.wikipedia.org/wiki/Double_centralizer_theorem)

**Axioms:** `s_central_simple_algebra`, `s_simple_subalgebra_B`
**Terminal:** `s_double_centralizer_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_central_simple_algebra, s_simple_subalgebra_B⟩` --[t_double_centralizer_decompose {tool: "B ⊗ A^op acts on A; isotypic decomposition"}]--> output: `s_B_otimes_Aop_action`
2. input: `s_B_otimes_Aop_action` --[t_character_decomposition_count {dimension: "dim_K Z_A(B) · dim_K B = dim_K A"}]--> output: `s_centralizer_dimension_formula`
3. input: `s_centralizer_dimension_formula` --[t_structural_isomorphism {iso: "Z_A(Z_A(B)) = B"}]--> output: `s_double_centralizer_theorem`

**Techniques used:** t_double_centralizer_decompose, t_character_decomposition_count, t_structural_isomorphism

---

### Skolem–Noether theorem (cite: https://en.wikipedia.org/wiki/Skolem%E2%80%93Noether_theorem)

**Axioms:** `s_central_simple_algebra`, `s_simple_subalgebra_B`
**Terminal:** `s_skolem_noether_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_central_simple_algebra, s_simple_subalgebra_B⟩` --[t_auxiliary_construction {two_embeddings: "f, g: B → A"}]--> output: `s_pair_of_B_embeddings`
2. input: `s_pair_of_B_embeddings` --[t_double_centralizer_decompose {bimodule: "A as B-bimodule via f and g; simple summands isomorphic"}]--> output: `s_bimodule_isomorphism`
3. input: `s_bimodule_isomorphism` --[t_structural_isomorphism {inner: "isomorphism realized by conjugation by unit u ∈ A^×"}]--> output: `s_skolem_noether_theorem`

**Techniques used:** t_auxiliary_construction, t_double_centralizer_decompose, t_structural_isomorphism

---

### Wedderburn's little theorem (cite: https://en.wikipedia.org/wiki/Wedderburn%27s_little_theorem)

**Axioms:** `s_finite_division_ring`, `s_finite_group`
**Terminal:** `s_wedderburn_little_theorem` (kind: theorem)

**Steps:**
1. input: `s_finite_division_ring` --[t_reductio_ad_absurdum {assume: "D non-commutative; center Z = F_q"}]--> output: `s_assumed_noncommutative_D`
2. input: `s_assumed_noncommutative_D` --[t_character_decomposition_count {class_eq: "|D^×| = (q-1) + Σ (q^n - 1)/(q^{d_i} - 1)"}]--> output: `s_class_equation_for_D_units`
3. input: `s_class_equation_for_D_units` --[t_complex_analysis_to_integers {cyclotomic: "Φ_n(q) divides each term and (q-1); but |Φ_n(q)| > q-1 for n>1"}]--> output: `s_cyclotomic_divisibility_obstruction`
4. input: `s_cyclotomic_divisibility_obstruction` --[t_reductio_ad_absurdum {contradict: "no nontrivial center extension; D commutative"}]--> output: `s_wedderburn_little_theorem`

**Techniques used:** t_reductio_ad_absurdum, t_character_decomposition_count, t_complex_analysis_to_integers

---

### Brauer group periodicity (cite: https://en.wikipedia.org/wiki/Brauer_group)

**Axioms:** `s_field_K`, `s_central_simple_algebra`
**Terminal:** `s_brauer_group_theorem` (kind: theorem)

**Steps:**
1. input: `s_field_K` --[t_auxiliary_construction {equivalence: "CSAs over K mod Morita ≃ similarity classes"}]--> output: `s_brauer_equivalence_classes`
2. input: `s_brauer_equivalence_classes` --[t_structural_isomorphism {tensor: "tensor product gives abelian group structure"}]--> output: `s_brauer_group_structure`
3. input: `s_brauer_group_structure` --[t_deformation_cohomology {iso: "Br(K) ≅ H^2(Gal(K̄/K), K̄^×)"}]--> output: `s_brauer_group_theorem`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_deformation_cohomology

---

### Hilbert's theorem 90 (cite: https://en.wikipedia.org/wiki/Hilbert%27s_Theorem_90)

**Axioms:** `s_cyclic_galois_extension`, `s_galois_group`
**Terminal:** `s_hilbert_90_theorem` (kind: theorem)

**Steps:**
1. input: `s_cyclic_galois_extension` --[t_auxiliary_construction {cocycle: "α with N_{L/K}(α) = 1"}]--> output: `s_norm_one_element`
2. input: `s_norm_one_element` --[t_deformation_cohomology {vanish: "H^1(Gal(L/K), L^×) = 0"}]--> output: `s_h1_vanishing`
3. input: `s_h1_vanishing` --[t_structural_isomorphism {coboundary: "α = β/σ(β) for some β ∈ L^×"}]--> output: `s_hilbert_90_theorem`

**Techniques used:** t_auxiliary_construction, t_deformation_cohomology, t_structural_isomorphism

---

### Artin–Schreier theorem (characteristic p extensions) (cite: https://en.wikipedia.org/wiki/Artin%E2%80%93Schreier_theory)

**Axioms:** `s_field_of_char_p`, `s_cyclic_extension_of_degree_p`
**Terminal:** `s_artin_schreier_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_field_of_char_p, s_cyclic_extension_of_degree_p⟩` --[t_auxiliary_construction {operator: "ω: x ↦ x^p - x; ker = F_p"}]--> output: `s_artin_schreier_operator`
2. input: `s_artin_schreier_operator` --[t_deformation_cohomology {additive_h90: "additive Hilbert 90: H^1(Gal, L^+) = 0"}]--> output: `s_additive_cohomology_vanish`
3. input: `s_additive_cohomology_vanish` --[t_structural_isomorphism {classify: "L/K = K(α) with α^p - α ∈ K"}]--> output: `s_artin_schreier_theorem`

**Techniques used:** t_auxiliary_construction, t_deformation_cohomology, t_structural_isomorphism

---

### Kummer theory (cite: https://en.wikipedia.org/wiki/Kummer_theory)

**Axioms:** `s_field_containing_nth_roots_of_unity`, `s_cyclic_extension_of_degree_n`
**Terminal:** `s_kummer_theory_theorem` (kind: theorem)

**Steps:**
1. input: `s_field_containing_nth_roots_of_unity` --[t_duality {pair: "K^×/(K^×)^n ↔ abelian exponent-n extensions"}]--> output: `s_kummer_pairing`
2. input: `s_kummer_pairing` --[t_deformation_cohomology {kummer_seq: "1 → μ_n → K̄^× → K̄^× → 1; long exact gives H^1(G_K,μ_n) = K^×/(K^×)^n"}]--> output: `s_kummer_cohomology_iso`
3. input: `s_kummer_cohomology_iso` --[t_galois_correspondence {classify: "cyclic deg-n extensions ↔ cyclic subgroups of K^×/(K^×)^n"}]--> output: `s_kummer_theory_theorem`

**Techniques used:** t_duality, t_deformation_cohomology, t_galois_correspondence

---

### Lüroth's theorem (cite: https://en.wikipedia.org/wiki/L%C3%BCroth%27s_theorem)

**Axioms:** `s_field_K`, `s_subfield_of_rational_function_field`
**Terminal:** `s_luroth_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_field_K, s_subfield_of_rational_function_field⟩` --[t_auxiliary_construction {subfield: "K ⊊ L ⊆ K(t)"}]--> output: `s_intermediate_subfield_in_kt`
2. input: `s_intermediate_subfield_in_kt` --[t_reduce_to_canonical_form {minpoly: "minimal polynomial of t over L; clear denominators"}]--> output: `s_minimal_polynomial_of_t_over_L`
3. input: `s_minimal_polynomial_of_t_over_L` --[t_character_decomposition_count {degree: "deg-counting via Gauss content forces L = K(f(t)) for some f"}]--> output: `s_luroth_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_character_decomposition_count

---

### Primitive element theorem (cite: https://en.wikipedia.org/wiki/Primitive_element_theorem)

**Axioms:** `s_finite_separable_extension`, `s_field_extension_L_over_K`
**Terminal:** `s_primitive_element_theorem` (kind: theorem)

**Steps:**
1. input: `s_finite_separable_extension` --[t_auxiliary_construction {gen: "L = K(α, β); seek γ = α + cβ"}]--> output: `s_candidate_primitive_element`
2. input: `s_candidate_primitive_element` --[t_pigeonhole_collision {avoid: "K infinite: avoid finitely many bad c"}]--> output: `s_choice_of_good_c`
3. input: `s_choice_of_good_c` --[t_structural_isomorphism {compute: "K(γ) = K(α,β) by separability of minpolys"}]--> output: `s_primitive_element_theorem`

**Techniques used:** t_auxiliary_construction, t_pigeonhole_collision, t_structural_isomorphism

---

### Isomorphism extension theorem (cite: https://en.wikipedia.org/wiki/Isomorphism_extension_theorem)

**Axioms:** `s_field_extension_L_over_K`, `s_algebraically_closed_field_k`
**Terminal:** `s_isomorphism_extension_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_field_extension_L_over_K, s_algebraically_closed_field_k⟩` --[t_auxiliary_construction {family: "set of partial extensions of σ: K → Ω"}]--> output: `s_partial_extension_family`
2. input: `s_partial_extension_family` --[t_compactness_argument {zorn: "Zorn's lemma yields maximal extension"}]--> output: `s_maximal_extension_via_zorn`
3. input: `s_maximal_extension_via_zorn` --[t_structural_isomorphism {algebraic_closure: "maximal extension lifts to entire L when Ω alg closed"}]--> output: `s_isomorphism_extension_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_structural_isomorphism

---

### Steinitz's theorem on field extensions (cite: https://en.wikipedia.org/wiki/Steinitz%27s_theorem_(field_theory))

**Axioms:** `s_field_K`, `s_algebraic_closure`
**Terminal:** `s_steinitz_algebraic_closure_theorem` (kind: theorem)

**Steps:**
1. input: `s_field_K` --[t_auxiliary_construction {family: "all algebraic extensions L/K"}]--> output: `s_algebraic_extensions_poset`
2. input: `s_algebraic_extensions_poset` --[t_compactness_argument {zorn: "Zorn yields maximal element K̄"}]--> output: `s_maximal_algebraic_extension`
3. input: `s_maximal_algebraic_extension` --[t_axiomatize_from_instances {properties: "K̄ algebraically closed; unique up to K-iso"}]--> output: `s_steinitz_algebraic_closure_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_axiomatize_from_instances

---

### Frobenius reciprocity (cite: https://en.wikipedia.org/wiki/Frobenius_reciprocity)

**Axioms:** `s_finite_group`, `s_subgroup_H`
**Terminal:** `s_frobenius_reciprocity_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_subgroup_H⟩` --[t_auxiliary_construction {functors: "Ind_H^G and Res^G_H between Rep(G) and Rep(H)"}]--> output: `s_ind_res_functor_pair`
2. input: `s_ind_res_functor_pair` --[t_category_theoretic_colimits_and_adjoints {adjunction: "Ind ⊣ Res (and Res ⊣ Ind for finite groups)"}]--> output: `s_ind_res_adjunction`
3. input: `s_ind_res_adjunction` --[t_character_decomposition_count {hom: "⟨χ, Res ψ⟩_H = ⟨Ind χ, ψ⟩_G"}]--> output: `s_frobenius_reciprocity_theorem`

**Techniques used:** t_auxiliary_construction, t_category_theoretic_colimits_and_adjoints, t_character_decomposition_count

---

### Mackey decomposition / double coset formula (cite: https://en.wikipedia.org/wiki/Mackey_theorem)

**Axioms:** `s_finite_group`, `s_subgroup_H`
**Terminal:** `s_mackey_decomposition_theorem` (kind: theorem)

**Steps:**
1. input: `s_finite_group` --[t_auxiliary_construction {coset: "double coset decomposition G = ⊔ H x_i K"}]--> output: `s_double_coset_decomposition`
2. input: `s_double_coset_decomposition` --[t_symmetry_reduction {restrict: "Res^G_K Ind_H^G V into pieces over each H x K"}]--> output: `s_restriction_per_double_coset`
3. input: `s_restriction_per_double_coset` --[t_character_decomposition_count {formula: "Res Ind V ≅ ⊕_i Ind_{x_i H x_i^{-1} ∩ K}^K (V^{x_i})"}]--> output: `s_mackey_decomposition_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_character_decomposition_count

---

### Character orthogonality relations (cite: https://en.wikipedia.org/wiki/Schur_orthogonality_relations)

**Axioms:** `s_finite_group`, `s_irreducible_representation`
**Terminal:** `s_character_orthogonality_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_irreducible_representation⟩` --[t_auxiliary_construction {operator: "(1/|G|) Σ_g π(g) ⊗ ρ(g^{-1})^T"}]--> output: `s_intertwiner_operator`
2. input: `s_intertwiner_operator` --[t_symmetry_reduction {schur: "operator is G-equivariant"}]--> output: `s_g_equivariant_operator`
3. input: `s_g_equivariant_operator` --[t_double_centralizer_decompose {schur_lemma: "Schur ⇒ either 0 or scalar"}]--> output: `s_schur_scalar_evaluation`
4. input: `s_schur_scalar_evaluation` --[t_character_decomposition_count {orthonormality: "⟨χ_i, χ_j⟩ = δ_{ij}"}]--> output: `s_character_orthogonality_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_double_centralizer_decompose, t_character_decomposition_count

---

### Burnside's theorem on character vanishing (zeros in character table) (cite: https://en.wikipedia.org/wiki/Character_table)

**Axioms:** `s_finite_group`, `s_irreducible_representation`
**Terminal:** `s_burnside_character_vanish_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_irreducible_representation⟩` --[t_character_decomposition_count {algebraic_integer: "χ(g) is sum of roots of unity"}]--> output: `s_chi_is_sum_of_roots_of_unity`
2. input: `s_chi_is_sum_of_roots_of_unity` --[t_complex_analysis_to_integers {galois_average: "|χ(g)/χ(1)| ≤ 1 with equality cases"}]--> output: `s_size_bound_on_chi_ratio`
3. input: `s_size_bound_on_chi_ratio` --[t_finite_case_check {dichotomy: "if (|C|, χ(1))=1 then χ(g)=0 or center contains g"}]--> output: `s_burnside_character_vanish_theorem`

**Techniques used:** t_character_decomposition_count, t_complex_analysis_to_integers, t_finite_case_check

---

### Brauer's theorem on induced characters (cite: https://en.wikipedia.org/wiki/Brauer%27s_theorem_on_induced_characters)

**Axioms:** `s_finite_group`, `s_irreducible_character`
**Terminal:** `s_brauer_induced_character_theorem` (kind: theorem)

**Steps:**
1. input: `s_finite_group` --[t_auxiliary_construction {object: "ring R(G) of virtual characters"}]--> output: `s_virtual_character_ring`
2. input: `s_virtual_character_ring` --[t_character_decomposition_count {elementary: "express every χ as ℤ-combination of Ind from elementary subgroups"}]--> output: `s_elementary_subgroup_generators`
3. input: `s_elementary_subgroup_generators` --[t_finite_case_check {p_elementary: "p-elementary = (cyclic × p-group); verify generation"}]--> output: `s_brauer_induced_character_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_finite_case_check

---

### Artin's induction theorem (cite: https://en.wikipedia.org/wiki/Artin%27s_theorem_on_induced_characters)

**Axioms:** `s_finite_group`, `s_cyclic_subgroup`
**Terminal:** `s_artin_induction_theorem` (kind: theorem)

**Steps:**
1. input: `s_finite_group` --[t_auxiliary_construction {object: "induced characters from cyclic subgroups"}]--> output: `s_induced_from_cyclic_subgroups`
2. input: `s_induced_from_cyclic_subgroups` --[t_character_decomposition_count {rationality: "any rational character is ℚ-combination of Ind χ_C"}]--> output: `s_rational_combination_from_cyclics`
3. input: `s_rational_combination_from_cyclics` --[t_axiomatize_from_instances {refine: "Brauer strengthens to ℤ-combination from elementary"}]--> output: `s_artin_induction_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_axiomatize_from_instances

---

### Peter–Weyl theorem (cite: https://en.wikipedia.org/wiki/Peter%E2%80%93Weyl_theorem)

**Axioms:** `s_compact_topological_group`, `s_unitary_representation`
**Terminal:** `s_peter_weyl_theorem` (kind: theorem)

**Steps:**
1. input: `s_compact_topological_group` --[t_auxiliary_construction {hilbert_space: "L²(G) with regular representation"}]--> output: `s_L2_of_G_with_regular_rep`
2. input: `s_L2_of_G_with_regular_rep` --[t_compactness_argument {compact_operator: "convolution by smooth function is compact"}]--> output: `s_compact_convolution_operator`
3. input: `s_compact_convolution_operator` --[t_svd_and_spectral_decomposition {spectral: "spectral theorem ⇒ eigenspaces finite-dim, G-invariant"}]--> output: `s_finite_dim_isotypic_pieces`
4. input: `s_finite_dim_isotypic_pieces` --[t_character_decomposition_count {sum: "L²(G) = ⊕_{π ∈ Ĝ} π ⊗ π*"}]--> output: `s_peter_weyl_theorem`

**Techniques used:** t_auxiliary_construction, t_compactness_argument, t_svd_and_spectral_decomposition, t_character_decomposition_count

---

### Weyl's theorem on complete reducibility (cite: https://en.wikipedia.org/wiki/Weyl%27s_theorem_on_complete_reducibility)

**Axioms:** `s_semisimple_lie_algebra`, `s_finite_dim_representation`
**Terminal:** `s_weyl_complete_reducibility_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_semisimple_lie_algebra, s_finite_dim_representation⟩` --[t_auxiliary_construction {casimir: "Casimir element C ∈ U(g)"}]--> output: `s_casimir_central_element`
2. input: `s_casimir_central_element` --[t_svd_and_spectral_decomposition {eigenspace: "decomposition by Casimir eigenvalues separates submodules"}]--> output: `s_casimir_eigenspace_decomposition`
3. input: `s_casimir_eigenspace_decomposition` --[t_structural_isomorphism {split: "all short exact sequences of f.d. reps split"}]--> output: `s_weyl_complete_reducibility_theorem`

**Techniques used:** t_auxiliary_construction, t_svd_and_spectral_decomposition, t_structural_isomorphism

---

### Theorem of the highest weight (cite: https://en.wikipedia.org/wiki/Theorem_of_the_highest_weight)

**Axioms:** `s_semisimple_lie_algebra`, `s_dominant_integral_weight`
**Terminal:** `s_highest_weight_theorem` (kind: theorem)

**Steps:**
1. input: `s_semisimple_lie_algebra` --[t_auxiliary_construction {borel: "Borel subalgebra b = h ⊕ n^+"}]--> output: `s_borel_subalgebra_b`
2. input: `s_borel_subalgebra_b` --[t_auxiliary_construction {verma: "Verma module M(λ) = U(g) ⊗_{U(b)} ℂ_λ"}]--> output: `s_verma_module_M_lambda`
3. input: `s_verma_module_M_lambda` --[t_symmetry_reduction {weyl_group: "Weyl group action permits maximal proper submodule"}]--> output: `s_unique_irreducible_quotient_L_lambda`
4. input: `s_unique_irreducible_quotient_L_lambda` --[t_character_decomposition_count {classify: "irreducibles ↔ dominant integral weights"}]--> output: `s_highest_weight_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_character_decomposition_count

---

### Borel–Weil–Bott theorem (cite: https://en.wikipedia.org/wiki/Borel%E2%80%93Weil%E2%80%93Bott_theorem)

**Axioms:** `s_semisimple_complex_lie_group`, `s_flag_variety_G_over_B`
**Terminal:** `s_borel_weil_bott_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_semisimple_complex_lie_group, s_flag_variety_G_over_B⟩` --[t_auxiliary_construction {line_bundle: "line bundle L_λ from weight λ"}]--> output: `s_line_bundle_L_lambda`
2. input: `s_line_bundle_L_lambda` --[t_sheaf_cohomology_bridge {cohomology: "H^i(G/B, L_λ)"}]--> output: `s_sheaf_cohomology_of_L_lambda`
3. input: `s_sheaf_cohomology_of_L_lambda` --[t_symmetry_reduction {weyl_action: "shifted Weyl action: ρ-shift moves λ to dominant chamber"}]--> output: `s_weyl_shift_to_dominant`
4. input: `s_weyl_shift_to_dominant` --[t_character_decomposition_count {result: "single nonzero cohomology = irrep V_{w·λ}"}]--> output: `s_borel_weil_bott_theorem`

**Techniques used:** t_auxiliary_construction, t_sheaf_cohomology_bridge, t_symmetry_reduction, t_character_decomposition_count

---

### Lie–Kolchin theorem (cite: https://en.wikipedia.org/wiki/Lie%E2%80%93Kolchin_theorem)

**Axioms:** `s_connected_solvable_linear_algebraic_group`, `s_algebraically_closed_field_k`
**Terminal:** `s_lie_kolchin_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_connected_solvable_linear_algebraic_group, s_algebraically_closed_field_k⟩` --[t_auxiliary_construction {fixed_point: "G acts on flag variety G/B"}]--> output: `s_g_action_on_flags`
2. input: `s_g_action_on_flags` --[t_contraction_fixed_point {borel_fp: "Borel fixed-point theorem yields invariant flag"}]--> output: `s_invariant_complete_flag`
3. input: `s_invariant_complete_flag` --[t_structural_isomorphism {triangularize: "G stabilizes flag ⇒ simultaneously upper-triangularizable"}]--> output: `s_lie_kolchin_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_structural_isomorphism

---

### Engel's theorem (cite: https://en.wikipedia.org/wiki/Engel%27s_theorem)

**Axioms:** `s_lie_algebra_over_field`, `s_nilpotent_endomorphism`
**Terminal:** `s_engel_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_lie_algebra_over_field, s_nilpotent_endomorphism⟩` --[t_auxiliary_construction {hypothesis: "all ad_x nilpotent on g"}]--> output: `s_all_adjoints_nilpotent`
2. input: `s_all_adjoints_nilpotent` --[t_infinite_descent {induction: "dim_g; find common eigenvector for proper subalg"}]--> output: `s_common_zero_vector_constructed`
3. input: `s_common_zero_vector_constructed` --[t_structural_isomorphism {triangularize: "simultaneous strict upper triangularization ⇒ g nilpotent"}]--> output: `s_engel_theorem`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_structural_isomorphism

---

### Cartan–Dieudonné theorem (cite: https://en.wikipedia.org/wiki/Cartan%E2%80%93Dieudonn%C3%A9_theorem)

**Axioms:** `s_quadratic_space_over_field`, `s_orthogonal_group_On`
**Terminal:** `s_cartan_dieudonne_theorem` (kind: theorem)

**Steps:**
1. input: `s_quadratic_space_over_field` --[t_auxiliary_construction {reflection: "reflection r_v across hyperplane v^⊥"}]--> output: `s_reflection_generators`
2. input: `s_reflection_generators` --[t_infinite_descent {induction: "fix a vector via composition with one reflection; descend dim"}]--> output: `s_descent_on_fixed_vectors`
3. input: `s_descent_on_fixed_vectors` --[t_character_decomposition_count {bound: "every isometry = product of ≤ n reflections"}]--> output: `s_cartan_dieudonne_theorem`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_character_decomposition_count

---

### Crystallographic restriction theorem (cite: https://en.wikipedia.org/wiki/Crystallographic_restriction_theorem)

**Axioms:** `s_lattice_in_euclidean_space`, `s_finite_rotation_subgroup`
**Terminal:** `s_crystallographic_restriction_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_lattice_in_euclidean_space, s_finite_rotation_subgroup⟩` --[t_auxiliary_construction {trace: "rotation preserves lattice ⇒ trace is integer"}]--> output: `s_integer_trace_constraint`
2. input: `s_integer_trace_constraint` --[t_character_decomposition_count {bound: "2cos(2π/n) ∈ ℤ ⇒ n ∈ {1,2,3,4,6}"}]--> output: `s_allowed_rotation_orders`
3. input: `s_allowed_rotation_orders` --[t_axiomatize_from_instances {classify: "2D/3D crystallographic point groups restricted"}]--> output: `s_crystallographic_restriction_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_axiomatize_from_instances

---

### Nakayama's lemma (cite: https://en.wikipedia.org/wiki/Nakayama%27s_lemma)

**Axioms:** `s_commutative_ring`, `s_finitely_generated_module`
**Terminal:** `s_nakayama_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_commutative_ring, s_finitely_generated_module⟩` --[t_auxiliary_construction {hyp: "ideal I ⊆ Jac(R), M = IM"}]--> output: `s_module_with_jM_eq_M`
2. input: `s_module_with_jM_eq_M` --[t_polynomial_method {char_poly: "Cayley–Hamilton: ∃ det relation 1 + a = 0 with a ∈ I"}]--> output: `s_unit_via_det_trick`
3. input: `s_unit_via_det_trick` --[t_reductio_ad_absurdum {conclude: "M = 0"}]--> output: `s_nakayama_lemma`

**Techniques used:** t_auxiliary_construction, t_polynomial_method, t_reductio_ad_absurdum

---

### Krull intersection theorem (cite: https://en.wikipedia.org/wiki/Krull_intersection_theorem)

**Axioms:** `s_noetherian_ring_R`, `s_ideal_I`
**Terminal:** `s_krull_intersection_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_noetherian_ring_R, s_ideal_I⟩` --[t_auxiliary_construction {object: "N = ⋂_n I^n M for f.g. module M"}]--> output: `s_intersection_module_N`
2. input: `s_intersection_module_N` --[t_auxiliary_construction {artin_rees: "Artin–Rees: IN = N eventually"}]--> output: `s_artin_rees_applied_to_N`
3. input: `s_artin_rees_applied_to_N` --[t_reduce_to_canonical_form {nakayama: "Nakayama ⇒ N = 0 when I ⊂ Jac(R)"}]--> output: `s_krull_intersection_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form

---

### Artin–Rees lemma (cite: https://en.wikipedia.org/wiki/Artin%E2%80%93Rees_lemma)

**Axioms:** `s_noetherian_ring_R`, `s_finitely_generated_module`
**Terminal:** `s_artin_rees_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_noetherian_ring_R, s_finitely_generated_module⟩` --[t_auxiliary_construction {rees: "Rees algebra R[It] and Rees module ⊕ I^n M"}]--> output: `s_rees_algebra_construction`
2. input: `s_rees_algebra_construction` --[t_axiomatize_from_instances {noetherian: "Rees algebra noetherian; Rees module f.g."}]--> output: `s_rees_module_fg`
3. input: `s_rees_module_fg` --[t_character_decomposition_count {stability: "I^n M ∩ N = I^{n-k}(I^k M ∩ N) for n ≥ k"}]--> output: `s_artin_rees_lemma`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_character_decomposition_count

---

### Going-up theorem (Cohen–Seidenberg) (cite: https://en.wikipedia.org/wiki/Going_up_and_going_down)

**Axioms:** `s_integral_ring_extension`, `s_prime_ideal_chain`
**Terminal:** `s_going_up_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_integral_ring_extension, s_prime_ideal_chain⟩` --[t_auxiliary_construction {extend: "given p_1 ⊂ p_2 in A, q_1 over p_1; seek q_2 over p_2"}]--> output: `s_partial_lift_to_B`
2. input: `s_partial_lift_to_B` --[t_reduce_to_canonical_form {quotient: "pass to A/p_1 ⊂ B/q_1, integral"}]--> output: `s_integral_quotient_extension`
3. input: `s_integral_quotient_extension` --[t_structural_isomorphism {lying_over: "lying-over theorem gives q_2"}]--> output: `s_going_up_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_structural_isomorphism

---

### Going-down theorem (cite: https://en.wikipedia.org/wiki/Going_up_and_going_down)

**Axioms:** `s_integral_extension_of_integrally_closed_domains`, `s_prime_ideal_chain`
**Terminal:** `s_going_down_theorem` (kind: theorem)

**Steps:**
1. input: `s_integral_extension_of_integrally_closed_domains` --[t_auxiliary_construction {localize: "localize A at p_1 and B at q_2"}]--> output: `s_localized_extension`
2. input: `s_localized_extension` --[t_galois_correspondence {galois_case: "embed in Galois closure; use Galois action transitivity"}]--> output: `s_galois_action_on_primes`
3. input: `s_galois_action_on_primes` --[t_structural_isomorphism {descend: "lift p_2 ⊂ p_1 to q_1 ⊂ q_2"}]--> output: `s_going_down_theorem`

**Techniques used:** t_auxiliary_construction, t_galois_correspondence, t_structural_isomorphism

---

### Krull's principal ideal theorem (Hauptidealsatz) (cite: https://en.wikipedia.org/wiki/Krull%27s_principal_ideal_theorem)

**Axioms:** `s_noetherian_ring_R`, `s_principal_ideal`
**Terminal:** `s_krull_pit_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_noetherian_ring_R, s_principal_ideal⟩` --[t_auxiliary_construction {minimal_prime: "minimal prime p over (a)"}]--> output: `s_minimal_prime_over_a`
2. input: `s_minimal_prime_over_a` --[t_reduce_to_canonical_form {localize: "localize at p, assume R local with max ideal p"}]--> output: `s_localized_at_p_setup`
3. input: `s_localized_at_p_setup` --[t_infinite_descent {symbolic_powers: "symbolic power chain stabilizes by artinianness of R_p/(a)"}]--> output: `s_chain_stabilizes`
4. input: `s_chain_stabilizes` --[t_character_decomposition_count {height_bound: "height(p) ≤ 1"}]--> output: `s_krull_pit_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_infinite_descent, t_character_decomposition_count

---

### Krull dimension theorem / height theorem (cite: https://en.wikipedia.org/wiki/Krull%27s_height_theorem)

**Axioms:** `s_noetherian_ring_R`, `s_ideal_with_n_generators`
**Terminal:** `s_krull_height_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_noetherian_ring_R, s_ideal_with_n_generators⟩` --[t_infinite_descent {induction: "induct on number of generators n"}]--> output: `s_induction_setup_on_generators`
2. input: `s_induction_setup_on_generators` --[t_reduce_to_canonical_form {base_case: "principal-ideal theorem for n=1"}]--> output: `s_pit_as_base_case`
3. input: `s_pit_as_base_case` --[t_character_decomposition_count {bound: "height of ideal generated by n elements ≤ n"}]--> output: `s_krull_height_theorem`

**Techniques used:** t_infinite_descent, t_reduce_to_canonical_form, t_character_decomposition_count

---

### Cohen structure theorem (cite: https://en.wikipedia.org/wiki/Cohen_structure_theorem)

**Axioms:** `s_complete_noetherian_local_ring`, `s_residue_field`
**Terminal:** `s_cohen_structure_theorem` (kind: theorem)

**Steps:**
1. input: `s_complete_noetherian_local_ring` --[t_auxiliary_construction {coefficient_field: "lift k → R via Hensel/successive approximation"}]--> output: `s_coefficient_ring_lifted`
2. input: `s_coefficient_ring_lifted` --[t_contraction_fixed_point {witt: "in mixed char, build Cohen ring W(k)-algebra"}]--> output: `s_witt_or_power_series_base`
3. input: `s_witt_or_power_series_base` --[t_structural_isomorphism {quotient: "R = k[[x_1,...,x_n]]/I or analogous mixed-char form"}]--> output: `s_cohen_structure_theorem`

**Techniques used:** t_auxiliary_construction, t_contraction_fixed_point, t_structural_isomorphism

---

### Hilbert's syzygy theorem (cite: https://en.wikipedia.org/wiki/Hilbert%27s_syzygy_theorem)

**Axioms:** `s_polynomial_ring_in_n_vars`, `s_finitely_generated_module`
**Terminal:** `s_hilbert_syzygy_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_polynomial_ring_in_n_vars, s_finitely_generated_module⟩` --[t_auxiliary_construction {resolution: "free resolution F_• → M"}]--> output: `s_free_resolution_of_M`
2. input: `s_free_resolution_of_M` --[t_infinite_descent {dim_drop: "depth/dimension counting reduces n by 1 each step"}]--> output: `s_inductive_depth_drop`
3. input: `s_inductive_depth_drop` --[t_character_decomposition_count {bound: "pd_M ≤ n"}]--> output: `s_hilbert_syzygy_theorem`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_character_decomposition_count

---

### Quillen–Suslin theorem (Serre's conjecture) (cite: https://en.wikipedia.org/wiki/Quillen%E2%80%93Suslin_theorem)

**Axioms:** `s_polynomial_ring_in_n_vars`, `s_finitely_generated_projective_module`
**Terminal:** `s_quillen_suslin_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_polynomial_ring_in_n_vars, s_finitely_generated_projective_module⟩` --[t_auxiliary_construction {local_global: "P is locally free; want globally free"}]--> output: `s_local_freeness_of_P`
2. input: `s_local_freeness_of_P` --[t_reduce_to_canonical_form {quillen_patching: "Quillen's local-global principle for extended modules"}]--> output: `s_extended_module_certified`
3. input: `s_extended_module_certified` --[t_infinite_descent {suslin: "Suslin's monic polynomial lemma reduces dim"}]--> output: `s_dimension_reduction_via_suslin`
4. input: `s_dimension_reduction_via_suslin` --[t_structural_isomorphism {free: "P is free"}]--> output: `s_quillen_suslin_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_infinite_descent, t_structural_isomorphism

---

### Auslander–Buchsbaum formula (cite: https://en.wikipedia.org/wiki/Auslander%E2%80%93Buchsbaum_formula)

**Axioms:** `s_noetherian_local_ring`, `s_finitely_generated_module`
**Terminal:** `s_auslander_buchsbaum_formula` (kind: theorem)

**Steps:**
1. input: `⟨s_noetherian_local_ring, s_finitely_generated_module⟩` --[t_auxiliary_construction {hypothesis: "pd(M) < ∞"}]--> output: `s_finite_projective_dim_module`
2. input: `s_finite_projective_dim_module` --[t_deformation_cohomology {ext: "Ext^i computations via free resolution"}]--> output: `s_ext_computation_via_resolution`
3. input: `s_ext_computation_via_resolution` --[t_character_decomposition_count {formula: "pd(M) + depth(M) = depth(R)"}]--> output: `s_auslander_buchsbaum_formula`

**Techniques used:** t_auxiliary_construction, t_deformation_cohomology, t_character_decomposition_count

---

### Auslander–Buchsbaum theorem (regular local ⇒ UFD) (cite: https://en.wikipedia.org/wiki/Auslander%E2%80%93Buchsbaum_theorem)

**Axioms:** `s_regular_local_ring`, `s_unique_factorization_domain`
**Terminal:** `s_auslander_buchsbaum_ufd_theorem` (kind: theorem)

**Steps:**
1. input: `s_regular_local_ring` --[t_auxiliary_construction {height_one: "consider height-1 prime p"}]--> output: `s_height_one_prime_p`
2. input: `s_height_one_prime_p` --[t_deformation_cohomology {ext: "finite proj dim ⇒ Ext-based class trivial"}]--> output: `s_ext_class_vanishes`
3. input: `s_ext_class_vanishes` --[t_structural_isomorphism {principal: "p is principal"}]--> output: `s_height_one_principal`
4. input: `s_height_one_principal` --[t_axiomatize_from_instances {ufd: "all height-1 primes principal ⇒ UFD"}]--> output: `s_auslander_buchsbaum_ufd_theorem`

**Techniques used:** t_auxiliary_construction, t_deformation_cohomology, t_structural_isomorphism, t_axiomatize_from_instances

---

### Hopkins–Levitzki theorem (cite: https://en.wikipedia.org/wiki/Hopkins%E2%80%93Levitzki_theorem)

**Axioms:** `s_artinian_ring`, `s_noetherian_ring_R`
**Terminal:** `s_hopkins_levitzki_theorem` (kind: theorem)

**Steps:**
1. input: `s_artinian_ring` --[t_auxiliary_construction {jacobson: "Jacobson radical J; J^n = 0 by Nakayama-style argument"}]--> output: `s_nilpotent_jacobson_radical`
2. input: `s_nilpotent_jacobson_radical` --[t_character_decomposition_count {filter: "filtration R ⊃ J ⊃ J² ⊃ ... ⊃ 0; quotients are semisimple"}]--> output: `s_semisimple_filtration_quotients`
3. input: `s_semisimple_filtration_quotients` --[t_axiomatize_from_instances {noetherian: "each quotient noetherian ⇒ R noetherian"}]--> output: `s_hopkins_levitzki_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_axiomatize_from_instances

---

### Goldie's theorem (cite: https://en.wikipedia.org/wiki/Goldie%27s_theorem)

**Axioms:** `s_semiprime_right_goldie_ring`, `s_classical_ring_of_quotients`
**Terminal:** `s_goldie_theorem` (kind: theorem)

**Steps:**
1. input: `s_semiprime_right_goldie_ring` --[t_auxiliary_construction {ore: "Ore condition on regular elements"}]--> output: `s_ore_set_of_regular_elements`
2. input: `s_ore_set_of_regular_elements` --[t_reduce_to_canonical_form {localize: "localize at regular elements"}]--> output: `s_classical_quotient_ring`
3. input: `s_classical_quotient_ring` --[t_structural_isomorphism {wedderburn: "quotient is semisimple artinian"}]--> output: `s_goldie_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_structural_isomorphism

---

### Primary decomposition (Lasker–Noether) (cite: https://en.wikipedia.org/wiki/Lasker%E2%80%93Noether_theorem)

**Axioms:** `s_noetherian_ring_R`, `s_ideal_I`
**Terminal:** `s_lasker_noether_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_noetherian_ring_R, s_ideal_I⟩` --[t_auxiliary_construction {irreducible_decomp: "express I as intersection of irreducible ideals"}]--> output: `s_irreducible_intersection_decomp`
2. input: `s_irreducible_intersection_decomp` --[t_axiomatize_from_instances {primary: "in noetherian ring, irreducible ⇒ primary"}]--> output: `s_primary_intersection_decomp`
3. input: `s_primary_intersection_decomp` --[t_character_decomposition_count {uniqueness: "associated primes are unique"}]--> output: `s_lasker_noether_theorem`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_character_decomposition_count

---

### Gauss's lemma (polynomials) (cite: https://en.wikipedia.org/wiki/Gauss%27s_lemma_(polynomials))

**Axioms:** `s_unique_factorization_domain`, `s_polynomial_ring`
**Terminal:** `s_gauss_lemma_polynomials` (kind: theorem)

**Steps:**
1. input: `⟨s_unique_factorization_domain, s_polynomial_ring⟩` --[t_auxiliary_construction {content: "content c(f) and primitive part of f ∈ R[x]"}]--> output: `s_content_and_primitive_part`
2. input: `s_content_and_primitive_part` --[t_character_decomposition_count {multiplicative: "c(fg) = c(f)c(g) up to units"}]--> output: `s_content_is_multiplicative`
3. input: `s_content_is_multiplicative` --[t_structural_isomorphism {transfer: "R UFD ⇒ R[x] UFD"}]--> output: `s_gauss_lemma_polynomials`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_structural_isomorphism

---

### Eisenstein's irreducibility criterion (cite: https://en.wikipedia.org/wiki/Eisenstein%27s_criterion)

**Axioms:** `s_unique_factorization_domain`, `s_prime_ideal_p`
**Terminal:** `s_eisenstein_criterion` (kind: theorem)

**Steps:**
1. input: `⟨s_unique_factorization_domain, s_prime_ideal_p⟩` --[t_auxiliary_construction {polynomial: "f = a_n x^n + ... with p | a_i (i<n), p ∤ a_n, p² ∤ a_0"}]--> output: `s_eisenstein_polynomial`
2. input: `s_eisenstein_polynomial` --[t_reductio_ad_absurdum {assume: "f = gh nontrivial factorization in R[x]"}]--> output: `s_assumed_factorization`
3. input: `s_assumed_factorization` --[t_reduce_to_canonical_form {modp: "reduce mod p: g·h ≡ a_n x^n forces both monomials"}]--> output: `s_eisenstein_criterion`

**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum, t_reduce_to_canonical_form

---

### Hom-tensor adjunction (cite: https://en.wikipedia.org/wiki/Tensor-hom_adjunction)

**Axioms:** `s_ring_R`, `s_module_category_R_Mod`
**Terminal:** `s_hom_tensor_adjunction_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_ring_R, s_module_category_R_Mod⟩` --[t_auxiliary_construction {functors: "− ⊗_R B and Hom_R(B, −)"}]--> output: `s_tensor_hom_functor_pair`
2. input: `s_tensor_hom_functor_pair` --[t_category_theoretic_colimits_and_adjoints {adjunction: "Hom_R(A ⊗ B, C) ≅ Hom_R(A, Hom(B, C))"}]--> output: `s_hom_tensor_adjunction_theorem`

**Techniques used:** t_auxiliary_construction, t_category_theoretic_colimits_and_adjoints

---

### Flatness via Tor vanishing (Lazard's theorem flavor) (cite: https://en.wikipedia.org/wiki/Flat_module)

**Axioms:** `s_ring_R`, `s_module_M`
**Terminal:** `s_flatness_tor_criterion_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_ring_R, s_module_M⟩` --[t_auxiliary_construction {derived: "Tor^R_1(M, R/I) for all ideals I"}]--> output: `s_tor_with_quotient_modules`
2. input: `s_tor_with_quotient_modules` --[t_deformation_cohomology {exactness: "tensor exactness ⇔ Tor^R_1(M, −) = 0"}]--> output: `s_tor_vanishing_equivalence`
3. input: `s_tor_vanishing_equivalence` --[t_axiomatize_from_instances {lazard: "M flat ⇔ filtered colimit of finite free modules"}]--> output: `s_flatness_tor_criterion_theorem`

**Techniques used:** t_auxiliary_construction, t_deformation_cohomology, t_axiomatize_from_instances

---

### Eilenberg–Watts theorem (cite: https://en.wikipedia.org/wiki/Eilenberg%E2%80%93Watts_theorem)

**Axioms:** `s_ring_R`, `s_colimit_preserving_functor`
**Terminal:** `s_eilenberg_watts_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_ring_R, s_colimit_preserving_functor⟩` --[t_auxiliary_construction {object: "F: R-Mod → S-Mod preserving colimits"}]--> output: `s_colim_preserving_F`
2. input: `s_colim_preserving_F` --[t_representable_functor_trick {bimod: "B = F(R) is an (S,R)-bimodule"}]--> output: `s_bimodule_B_extracted`
3. input: `s_bimodule_B_extracted` --[t_structural_isomorphism {identify: "F ≅ B ⊗_R −"}]--> output: `s_eilenberg_watts_theorem`

**Techniques used:** t_auxiliary_construction, t_representable_functor_trick, t_structural_isomorphism

---

### Mitchell's embedding theorem (cite: https://en.wikipedia.org/wiki/Mitchell%27s_embedding_theorem)

**Axioms:** `s_abelian_category`, `s_module_category_R_Mod`
**Terminal:** `s_mitchell_embedding_theorem` (kind: theorem)

**Steps:**
1. input: `s_abelian_category` --[t_auxiliary_construction {small: "assume A small abelian"}]--> output: `s_small_abelian_category`
2. input: `s_small_abelian_category` --[t_representable_functor_trick {yoneda: "embed A into Fun(A^op, Ab) via Yoneda; injective hulls"}]--> output: `s_yoneda_embedding_setup`
3. input: `s_yoneda_embedding_setup` --[t_structural_isomorphism {embed: "fully faithful exact embedding A ↪ R-Mod"}]--> output: `s_mitchell_embedding_theorem`

**Techniques used:** t_auxiliary_construction, t_representable_functor_trick, t_structural_isomorphism

---

### Yoneda lemma (cite: https://en.wikipedia.org/wiki/Yoneda_lemma)

**Axioms:** `s_locally_small_category`, `s_functor_to_set`
**Terminal:** `s_yoneda_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_locally_small_category, s_functor_to_set⟩` --[t_auxiliary_construction {evaluator: "evaluator η ↦ η_X(id_X)"}]--> output: `s_evaluator_map`
2. input: `s_evaluator_map` --[t_representable_functor_trick {invert: "natural transformations Hom(X,−) ⇒ F correspond to F(X)"}]--> output: `s_bijection_with_F_X`
3. input: `s_bijection_with_F_X` --[t_structural_isomorphism {yoneda: "embedding y: C ↪ Fun(C^op, Set) is fully faithful"}]--> output: `s_yoneda_lemma`

**Techniques used:** t_auxiliary_construction, t_representable_functor_trick, t_structural_isomorphism

---

### Snake lemma (cite: https://en.wikipedia.org/wiki/Snake_lemma)

**Axioms:** `s_short_exact_sequence_diagram`, `s_abelian_category`
**Terminal:** `s_snake_lemma` (kind: theorem)

**Steps:**
1. input: `s_short_exact_sequence_diagram` --[t_auxiliary_construction {connecting: "build connecting map δ: ker(c) → coker(a) via diagram chase"}]--> output: `s_connecting_homomorphism_delta`
2. input: `s_connecting_homomorphism_delta` --[t_axiomatize_from_instances {exactness: "verify exactness at each node by element chase"}]--> output: `s_six_term_long_sequence`
3. input: `s_six_term_long_sequence` --[t_duality {finalize: "ker(a) → ker(b) → ker(c) →^δ coker(a) → coker(b) → coker(c)"}]--> output: `s_snake_lemma`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_duality

---

### Five lemma (cite: https://en.wikipedia.org/wiki/Five_lemma)

**Axioms:** `s_commutative_diagram_5x2`, `s_abelian_category`
**Terminal:** `s_five_lemma` (kind: theorem)

**Steps:**
1. input: `s_commutative_diagram_5x2` --[t_auxiliary_construction {chase: "element diagram chase using exactness in rows"}]--> output: `s_diagram_chase_argument`
2. input: `s_diagram_chase_argument` --[t_structural_isomorphism {result: "outer maps iso ⇒ middle map iso"}]--> output: `s_five_lemma`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism

---

### Long exact sequence in cohomology (cite: https://en.wikipedia.org/wiki/Long_exact_sequence)

**Axioms:** `s_short_exact_sequence_of_chain_complexes`, `s_chain_complex`
**Terminal:** `s_long_exact_sequence_theorem` (kind: theorem)

**Steps:**
1. input: `s_short_exact_sequence_of_chain_complexes` --[t_auxiliary_construction {boundary: "boundary connecting map δ: H_n(C'') → H_{n−1}(C')"}]--> output: `s_connecting_boundary_map`
2. input: `s_connecting_boundary_map` --[t_deformation_cohomology {snake: "apply snake lemma to cycles/boundaries"}]--> output: `s_snake_lemma_applied_to_homology`
3. input: `s_snake_lemma_applied_to_homology` --[t_axiomatize_from_instances {string: "concatenate to a long exact sequence on homology"}]--> output: `s_long_exact_sequence_theorem`

**Techniques used:** t_auxiliary_construction, t_deformation_cohomology, t_axiomatize_from_instances

---

### Universal coefficient theorem (cite: https://en.wikipedia.org/wiki/Universal_coefficient_theorem)

**Axioms:** `s_chain_complex_over_pid`, `s_abelian_group_coefficients`
**Terminal:** `s_universal_coefficient_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_chain_complex_over_pid, s_abelian_group_coefficients⟩` --[t_auxiliary_construction {free_res: "split chain complex into free + torsion via PID structure"}]--> output: `s_split_resolution_of_homology`
2. input: `s_split_resolution_of_homology` --[t_deformation_cohomology {tor_ext: "Tor and Ext computed via free resolution"}]--> output: `s_tor_ext_terms_computed`
3. input: `s_tor_ext_terms_computed` --[t_structural_isomorphism {ses: "0 → H_n(C)⊗A → H_n(C;A) → Tor(H_{n-1}(C),A) → 0 splits"}]--> output: `s_universal_coefficient_theorem`

**Techniques used:** t_auxiliary_construction, t_deformation_cohomology, t_structural_isomorphism

---

### Künneth formula (cite: https://en.wikipedia.org/wiki/K%C3%BCnneth_theorem)

**Axioms:** `s_chain_complex_over_pid`, `s_tensor_product_of_complexes`
**Terminal:** `s_kunneth_formula_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_chain_complex_over_pid, s_tensor_product_of_complexes⟩` --[t_auxiliary_construction {map: "external product H_*(C)⊗H_*(D) → H_*(C⊗D)"}]--> output: `s_external_product_map`
2. input: `s_external_product_map` --[t_deformation_cohomology {tor_correction: "Tor terms measure failure of pure tensor"}]--> output: `s_tor_correction_term`
3. input: `s_tor_correction_term` --[t_structural_isomorphism {ses: "0 → ⊕ H_i⊗H_j → H_n(C⊗D) → ⊕ Tor(H_i, H_j) → 0"}]--> output: `s_kunneth_formula_theorem`

**Techniques used:** t_auxiliary_construction, t_deformation_cohomology, t_structural_isomorphism

---

### Hilbert–Serre theorem on Hilbert series rationality (cite: https://en.wikipedia.org/wiki/Hilbert_series_and_Hilbert_polynomial)

**Axioms:** `s_graded_noetherian_ring`, `s_finitely_generated_graded_module`
**Terminal:** `s_hilbert_serre_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graded_noetherian_ring, s_finitely_generated_graded_module⟩` --[t_auxiliary_construction {series: "Hilbert series H_M(t) = Σ dim M_n t^n"}]--> output: `s_hilbert_series_of_M`
2. input: `s_hilbert_series_of_M` --[t_infinite_descent {induction: "induct on number of generators of R₊"}]--> output: `s_induction_on_generators`
3. input: `s_induction_on_generators` --[t_character_decomposition_count {rational: "H_M(t) = P(t) / ∏(1 - t^{d_i}), P ∈ ℤ[t]"}]--> output: `s_hilbert_serre_theorem`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_character_decomposition_count

---

### Cayley–Hamilton theorem (cite: https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem)

**Axioms:** `s_commutative_ring`, `s_square_matrix_over_ring`
**Terminal:** `s_cayley_hamilton_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_commutative_ring, s_square_matrix_over_ring⟩` --[t_auxiliary_construction {adjugate: "adjugate identity (xI-A)·adj(xI-A) = det(xI-A)·I"}]--> output: `s_adjugate_identity`
2. input: `s_adjugate_identity` --[t_reduce_to_canonical_form {substitute: "treat x as A acting on R^n"}]--> output: `s_substitution_x_eq_A`
3. input: `s_substitution_x_eq_A` --[t_structural_isomorphism {evaluate: "p_A(A) = 0 where p_A is characteristic poly"}]--> output: `s_cayley_hamilton_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_structural_isomorphism

---

### Jordan normal form theorem (cite: https://en.wikipedia.org/wiki/Jordan_normal_form)

**Axioms:** `s_algebraically_closed_field_k`, `s_finite_dim_vector_space`
**Terminal:** `s_jordan_normal_form_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_algebraically_closed_field_k, s_finite_dim_vector_space⟩` --[t_auxiliary_construction {kt_module: "V as k[t]-module via endomorphism T"}]--> output: `s_v_as_kt_module`
2. input: `s_v_as_kt_module` --[t_reduce_to_canonical_form {pid_structure: "PID structure theorem ⇒ V ≅ ⊕ k[t]/(t-λ_i)^{n_i}"}]--> output: `s_primary_cyclic_decomposition`
3. input: `s_primary_cyclic_decomposition` --[t_structural_isomorphism {block: "each summand realizes a Jordan block J(λ_i, n_i)"}]--> output: `s_jordan_normal_form_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_structural_isomorphism

---

### Rational canonical form (cite: https://en.wikipedia.org/wiki/Frobenius_normal_form)

**Axioms:** `s_field_K`, `s_finite_dim_vector_space`
**Terminal:** `s_rational_canonical_form_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_field_K, s_finite_dim_vector_space⟩` --[t_auxiliary_construction {kt_module: "V as k[t]-module via T"}]--> output: `s_v_as_kt_module_general`
2. input: `s_v_as_kt_module_general` --[t_reduce_to_canonical_form {invariant_factor: "invariant factor decomposition over PID k[t]"}]--> output: `s_invariant_factor_decomp_for_V`
3. input: `s_invariant_factor_decomp_for_V` --[t_structural_isomorphism {companion: "each summand realizes companion matrix of d_i(t)"}]--> output: `s_rational_canonical_form_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_structural_isomorphism

---

### Chevalley–Warning theorem (cite: https://en.wikipedia.org/wiki/Chevalley%E2%80%93Warning_theorem)

**Axioms:** `s_finite_field_Fq`, `s_polynomial_system`
**Terminal:** `s_chevalley_warning_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_field_Fq, s_polynomial_system⟩` --[t_auxiliary_construction {character_sum: "1 - f^{q-1} as indicator of zero set"}]--> output: `s_indicator_via_fermat`
2. input: `s_indicator_via_fermat` --[t_character_decomposition_count {sum: "Σ_{x ∈ F_q^n} (1 - f^{q-1}) = #V(f) mod p"}]--> output: `s_indicator_sum_evaluation`
3. input: `s_indicator_sum_evaluation` --[t_polynomial_method {degree_bound: "low-degree sum over F_q^n vanishes if total deg < n(q-1)"}]--> output: `s_chevalley_warning_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_polynomial_method

---

### Ax–Grothendieck theorem (cite: https://en.wikipedia.org/wiki/Ax%E2%80%93Grothendieck_theorem)

**Axioms:** `s_polynomial_map_C_n_to_C_n`, `s_algebraically_closed_field_k`
**Terminal:** `s_ax_grothendieck_theorem` (kind: theorem)

**Steps:**
1. input: `s_polynomial_map_C_n_to_C_n` --[t_auxiliary_construction {finite_base: "first prove statement over F̄_p (each algebraic closure of F_p)"}]--> output: `s_finite_field_case`
2. input: `s_finite_field_case` --[t_finite_case_check {fp_case: "injective ⇒ surjective on any finite subfield (counting)"}]--> output: `s_finite_field_injective_implies_surjective`
3. input: `s_finite_field_injective_implies_surjective` --[t_ultraproduct_transfer {transfer: "first-order ⇒ transfer to ℂ via Lefschetz principle"}]--> output: `s_ax_grothendieck_theorem`

**Techniques used:** t_auxiliary_construction, t_finite_case_check, t_ultraproduct_transfer

---

### Amitsur–Levitzki theorem (cite: https://en.wikipedia.org/wiki/Amitsur%E2%80%93Levitzki_theorem)

**Axioms:** `s_matrix_algebra_M_n`, `s_polynomial_identity`
**Terminal:** `s_amitsur_levitzki_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_matrix_algebra_M_n, s_polynomial_identity⟩` --[t_auxiliary_construction {standard_poly: "standard polynomial S_{2n}(x_1,...,x_{2n}) = Σ_σ sgn(σ) x_{σ(1)}⋯x_{σ(2n)}"}]--> output: `s_standard_polynomial_2n`
2. input: `s_standard_polynomial_2n` --[t_character_decomposition_count {symmetry: "trace of alternating product is symmetric in odd Lie bracket products"}]--> output: `s_symmetric_trace_relations`
3. input: `s_symmetric_trace_relations` --[t_polynomial_method {vanishing: "expand and pair signs ⇒ S_{2n} vanishes on M_n"}]--> output: `s_amitsur_levitzki_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_polynomial_method

---

### Hochster–Roberts theorem (cite: https://en.wikipedia.org/wiki/Hochster%E2%80%93Roberts_theorem)

**Axioms:** `s_reductive_group_action`, `s_polynomial_ring`
**Terminal:** `s_hochster_roberts_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_reductive_group_action, s_polynomial_ring⟩` --[t_auxiliary_construction {invariants: "ring of invariants R^G"}]--> output: `s_invariant_subring_R_G`
2. input: `s_invariant_subring_R_G` --[t_symmetry_reduction {reynolds: "Reynolds operator R → R^G splits as R^G-module map"}]--> output: `s_reynolds_splitting`
3. input: `s_reynolds_splitting` --[t_deformation_cohomology {direct_summand: "R^G is a direct summand of R; pure ⇒ Cohen–Macaulay descends"}]--> output: `s_hochster_roberts_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_deformation_cohomology

---

### Eakin–Nagata theorem (cite: https://en.wikipedia.org/wiki/Eakin%E2%80%93Nagata_theorem)

**Axioms:** `s_finite_ring_extension`, `s_noetherian_ring_R`
**Terminal:** `s_eakin_nagata_theorem` (kind: theorem)

**Steps:**
1. input: `s_finite_ring_extension` --[t_auxiliary_construction {chain: "ascending chain of ideals in S"}]--> output: `s_ascending_chain_in_S`
2. input: `s_ascending_chain_in_S` --[t_reduce_to_canonical_form {pullback: "contract chain to f.g. R-submodule chain in S"}]--> output: `s_chain_pulled_back_to_R`
3. input: `s_chain_pulled_back_to_R` --[t_axiomatize_from_instances {acc: "noetherian R + finite extension ⇒ S noetherian"}]--> output: `s_eakin_nagata_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_axiomatize_from_instances

---

### Schur's theorem on commutator subgroup (cite: https://en.wikipedia.org/wiki/Schur%27s_theorem)

**Axioms:** `s_finite_index_center`, `s_finite_group`
**Terminal:** `s_schur_commutator_theorem` (kind: theorem)

**Steps:**
1. input: `s_finite_index_center` --[t_auxiliary_construction {commutator_map: "commutator map [x,y]; values lie in [G,G]"}]--> output: `s_commutator_value_count`
2. input: `s_commutator_value_count` --[t_character_decomposition_count {bound: "[G,G] has at most [G:Z(G)]² generators"}]--> output: `s_commutator_subgroup_size_bound`
3. input: `s_commutator_subgroup_size_bound` --[t_structural_isomorphism {finite: "[G:Z(G)] < ∞ ⇒ [G,G] finite"}]--> output: `s_schur_commutator_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_structural_isomorphism

---

### Frobenius's theorem on real division algebras (cite: https://en.wikipedia.org/wiki/Frobenius_theorem_(real_division_algebras))

**Axioms:** `s_finite_dim_associative_real_division_algebra`
**Terminal:** `s_frobenius_real_division_theorem` (kind: theorem)

**Steps:**
1. input: `s_finite_dim_associative_real_division_algebra` --[t_auxiliary_construction {pure: "pure imaginary subspace V = {x : x² ∈ ℝ_{≤0}}"}]--> output: `s_pure_imaginary_subspace`
2. input: `s_pure_imaginary_subspace` --[t_character_decomposition_count {dim: "dim V ∈ {0, 1, 3}"}]--> output: `s_dimension_dichotomy`
3. input: `s_dimension_dichotomy` --[t_structural_isomorphism {classify: "D ∈ {ℝ, ℂ, ℍ}"}]--> output: `s_frobenius_real_division_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_structural_isomorphism

---

### Hurwitz's theorem on composition algebras (cite: https://en.wikipedia.org/wiki/Hurwitz%27s_theorem_(composition_algebras))

**Axioms:** `s_normed_division_algebra_over_R`, `s_finite_dim_associative_real_division_algebra`
**Terminal:** `s_hurwitz_composition_theorem` (kind: theorem)

**Steps:**
1. input: `s_normed_division_algebra_over_R` --[t_auxiliary_construction {cayley_dickson: "Cayley–Dickson doubling construction"}]--> output: `s_cayley_dickson_tower`
2. input: `s_cayley_dickson_tower` --[t_infinite_descent {loss: "each doubling loses a structural property after dim 8"}]--> output: `s_structural_property_loss`
3. input: `s_structural_property_loss` --[t_character_decomposition_count {classify: "dim ∈ {1,2,4,8}: ℝ, ℂ, ℍ, 𝕆"}]--> output: `s_hurwitz_composition_theorem`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_character_decomposition_count

---

### Fundamental theorem of symmetric polynomials (cite: https://en.wikipedia.org/wiki/Elementary_symmetric_polynomial#Fundamental_theorem_of_symmetric_polynomials)

**Axioms:** `s_polynomial_ring_in_n_vars`, `s_symmetric_group_Sn_action`
**Terminal:** `s_fundamental_theorem_symmetric_polynomials` (kind: theorem)

**Steps:**
1. input: `⟨s_polynomial_ring_in_n_vars, s_symmetric_group_Sn_action⟩` --[t_auxiliary_construction {elementary: "elementary symmetric polynomials e_1,...,e_n"}]--> output: `s_elementary_symmetric_polynomials`
2. input: `s_elementary_symmetric_polynomials` --[t_infinite_descent {lex_lead: "induct on lex-leading monomial; subtract e^{a_1}_{...} adjustments"}]--> output: `s_lex_reduction_algorithm`
3. input: `s_lex_reduction_algorithm` --[t_structural_isomorphism {iso: "k[x_1,...,x_n]^{S_n} ≅ k[e_1,...,e_n] polynomial"}]--> output: `s_fundamental_theorem_symmetric_polynomials`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_structural_isomorphism

---

### Newton's identities (cite: https://en.wikipedia.org/wiki/Newton%27s_identities)

**Axioms:** `s_polynomial_ring_in_n_vars`, `s_elementary_symmetric_polynomials`
**Terminal:** `s_newton_identities_theorem` (kind: theorem)

**Steps:**
1. input: `s_elementary_symmetric_polynomials` --[t_auxiliary_construction {gen_func: "generating series ∏(1 + x_i t) and Σ p_k t^k"}]--> output: `s_generating_series_setup`
2. input: `s_generating_series_setup` --[t_complex_analysis_to_integers {log_deriv: "logarithmic derivative ties p_k to e_k"}]--> output: `s_log_derivative_relation`
3. input: `s_log_derivative_relation` --[t_structural_isomorphism {recursion: "p_k − e_1 p_{k-1} + ... + (−1)^{k-1} k e_k = 0"}]--> output: `s_newton_identities_theorem`

**Techniques used:** t_auxiliary_construction, t_complex_analysis_to_integers, t_structural_isomorphism

---

### Bezout's identity in PIDs (cite: https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity)

**Axioms:** `s_principal_ideal_domain`, `s_two_ring_elements`
**Terminal:** `s_bezout_identity_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_principal_ideal_domain, s_two_ring_elements⟩` --[t_auxiliary_construction {ideal: "ideal (a,b) generated by a, b"}]--> output: `s_ideal_a_b_in_R`
2. input: `s_ideal_a_b_in_R` --[t_reduce_to_canonical_form {principal: "PID ⇒ (a,b) = (d) for some d"}]--> output: `s_ideal_principal_d`
3. input: `s_ideal_principal_d` --[t_structural_isomorphism {gcd: "d = gcd(a,b) and d = ua + vb"}]--> output: `s_bezout_identity_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_structural_isomorphism

---

### Euclid's algorithm in Euclidean domains (cite: https://en.wikipedia.org/wiki/Euclidean_domain)

**Axioms:** `s_euclidean_domain`, `s_two_ring_elements`
**Terminal:** `s_euclidean_algorithm_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_euclidean_domain, s_two_ring_elements⟩` --[t_auxiliary_construction {division: "Euclidean division: a = bq + r with N(r) < N(b)"}]--> output: `s_euclidean_division_step`
2. input: `s_euclidean_division_step` --[t_infinite_descent {norm: "norm strictly decreases ⇒ terminates"}]--> output: `s_termination_via_norm_descent`
3. input: `s_termination_via_norm_descent` --[t_structural_isomorphism {gcd: "last nonzero remainder is gcd; gives Bezout coefficients"}]--> output: `s_euclidean_algorithm_theorem`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_structural_isomorphism

---

### Wilson's theorem (cite: https://en.wikipedia.org/wiki/Wilson%27s_theorem)

**Axioms:** `s_prime_p`, `s_multiplicative_group_mod_p`
**Terminal:** `s_wilson_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_prime_p, s_multiplicative_group_mod_p⟩` --[t_auxiliary_construction {pairing: "pair each x with x^{-1} in (ℤ/p)^×"}]--> output: `s_inverse_pairing`
2. input: `s_inverse_pairing` --[t_pigeonhole_collision {fixed: "only x = ±1 self-inverse"}]--> output: `s_self_inverse_elements`
3. input: `s_self_inverse_elements` --[t_character_decomposition_count {product: "(p-1)! ≡ -1 mod p"}]--> output: `s_wilson_theorem`

**Techniques used:** t_auxiliary_construction, t_pigeonhole_collision, t_character_decomposition_count

---

### Galois solvability ⇔ solvable Galois group (cite: https://en.wikipedia.org/wiki/Solvable_group)

**Axioms:** `s_finite_normal_separable_extension_L_over_K`, `s_radical_extension_tower`
**Terminal:** `s_solvability_by_radicals_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_normal_separable_extension_L_over_K, s_radical_extension_tower⟩` --[t_galois_correspondence {bijection: "tower of subfields ↔ chain of subgroups"}]--> output: `s_subgroup_chain_for_tower`
2. input: `s_subgroup_chain_for_tower` --[t_character_decomposition_count {abelian_quotients: "radical steps ⇔ abelian (cyclic) quotients"}]--> output: `s_abelian_quotient_chain`
3. input: `s_abelian_quotient_chain` --[t_axiomatize_from_instances {solvable: "Gal(L/K) solvable ⇔ p(x) solvable by radicals"}]--> output: `s_solvability_by_radicals_theorem`

**Techniques used:** t_galois_correspondence, t_character_decomposition_count, t_axiomatize_from_instances

---

### Galois theorem on cyclotomic extensions (cite: https://en.wikipedia.org/wiki/Cyclotomic_field#Galois_group)

**Axioms:** `s_cyclotomic_field_Q_zeta_n`, `s_field_extension_L_over_K`
**Terminal:** `s_cyclotomic_galois_theorem` (kind: theorem)

**Steps:**
1. input: `s_cyclotomic_field_Q_zeta_n` --[t_auxiliary_construction {minpoly: "minimal polynomial = cyclotomic Φ_n(x)"}]--> output: `s_cyclotomic_minimal_polynomial`
2. input: `s_cyclotomic_minimal_polynomial` --[t_complex_analysis_to_integers {irreducible: "Φ_n irreducible over ℚ (Eisenstein at p for p|n)"}]--> output: `s_phi_n_irreducible_over_Q`
3. input: `s_phi_n_irreducible_over_Q` --[t_galois_correspondence {compute: "Gal(ℚ(ζ_n)/ℚ) ≅ (ℤ/n)^×"}]--> output: `s_cyclotomic_galois_theorem`

**Techniques used:** t_auxiliary_construction, t_complex_analysis_to_integers, t_galois_correspondence

---

### Dedekind's theorem on splitting of primes (cite: https://en.wikipedia.org/wiki/Splitting_of_prime_ideals_in_Galois_extensions)

**Axioms:** `s_galois_extension_of_number_fields`, `s_prime_p`
**Terminal:** `s_dedekind_splitting_theorem` (kind: theorem)

**Steps:**
1. input: `s_galois_extension_of_number_fields` --[t_auxiliary_construction {decomposition: "decomposition and inertia subgroups at prime above p"}]--> output: `s_decomposition_inertia_groups`
2. input: `s_decomposition_inertia_groups` --[t_symmetry_reduction {transitive_action: "Galois group acts transitively on primes above p"}]--> output: `s_galois_transitive_on_primes`
3. input: `s_galois_transitive_on_primes` --[t_character_decomposition_count {formula: "Σ e_i f_i = n; e_i, f_i constant in Galois case"}]--> output: `s_dedekind_splitting_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_character_decomposition_count

---

### Frobenius elements & Chebotarev density (algebraic content) (cite: https://en.wikipedia.org/wiki/Chebotarev%27s_density_theorem)

**Axioms:** `s_galois_extension_of_number_fields`, `s_prime_p`
**Terminal:** `s_chebotarev_density_theorem` (kind: theorem)

**Steps:**
1. input: `s_galois_extension_of_number_fields` --[t_auxiliary_construction {frobenius: "Frobenius element σ_p for unramified prime"}]--> output: `s_frobenius_conjugacy_class`
2. input: `s_frobenius_conjugacy_class` --[t_character_decomposition_count {L_functions: "Artin L-functions for class functions"}]--> output: `s_artin_L_function_machinery`
3. input: `s_artin_L_function_machinery` --[t_complex_analysis_to_integers {tauberian: "non-vanishing of L at s=1 ⇒ density of conjugacy classes"}]--> output: `s_chebotarev_density_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_complex_analysis_to_integers

---

### Hasse–Arf theorem (cite: https://en.wikipedia.org/wiki/Hasse%E2%80%93Arf_theorem)

**Axioms:** `s_local_field`, `s_abelian_extension`
**Terminal:** `s_hasse_arf_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_local_field, s_abelian_extension⟩` --[t_auxiliary_construction {filtration: "ramification filtration G_u (upper/lower numbering)"}]--> output: `s_ramification_filtration`
2. input: `s_ramification_filtration` --[t_reduce_to_canonical_form {herbrand: "Herbrand function ψ converts numbering"}]--> output: `s_herbrand_psi_function`
3. input: `s_herbrand_psi_function` --[t_character_decomposition_count {integrality: "abelian ⇒ jumps in upper numbering are integers"}]--> output: `s_hasse_arf_theorem`

**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_character_decomposition_count

---

### Local Tate duality (cite: https://en.wikipedia.org/wiki/Local_Tate_duality)

**Axioms:** `s_local_field`, `s_galois_representation`
**Terminal:** `s_local_tate_duality_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_local_field, s_galois_representation⟩` --[t_auxiliary_construction {cup_product: "cup product H^i(K, M) ⊗ H^{2-i}(K, M^∨(1)) → H^2(K, μ) = ℚ/ℤ"}]--> output: `s_cup_product_pairing`
2. input: `s_cup_product_pairing` --[t_deformation_cohomology {finite: "groups are finite for finite M"}]--> output: `s_finiteness_of_galois_cohomology`
3. input: `s_finiteness_of_galois_cohomology` --[t_duality {perfect: "pairing is perfect ⇒ H^i and H^{2-i} dual"}]--> output: `s_local_tate_duality_theorem`

**Techniques used:** t_auxiliary_construction, t_deformation_cohomology, t_duality

---

### Norm residue isomorphism (Milnor / Bloch–Kato) (cite: https://en.wikipedia.org/wiki/Norm_residue_isomorphism_theorem)

**Axioms:** `s_field_K`, `s_milnor_k_theory`
**Terminal:** `s_norm_residue_isomorphism_theorem` (kind: theorem)

**Steps:**
1. input: `s_field_K` --[t_auxiliary_construction {milnor_K: "Milnor K-theory K^M_n(F)/ℓ"}]--> output: `s_milnor_K_mod_ell`
2. input: `s_milnor_K_mod_ell` --[t_deformation_cohomology {map: "norm residue map h: K^M_n(F)/ℓ → H^n(F, μ_ℓ^{⊗n})"}]--> output: `s_norm_residue_map`
3. input: `s_norm_residue_map` --[t_sheaf_cohomology_bridge {motivic: "Voevodsky motivic cohomology and Bloch–Kato"}]--> output: `s_motivic_cohomology_comparison`
4. input: `s_motivic_cohomology_comparison` --[t_structural_isomorphism {iso: "h is an isomorphism for all n, ℓ"}]--> output: `s_norm_residue_isomorphism_theorem`

**Techniques used:** t_auxiliary_construction, t_deformation_cohomology, t_sheaf_cohomology_bridge, t_structural_isomorphism

---

### Brauer's three main theorems (block theory) (cite: https://en.wikipedia.org/wiki/Brauer%27s_three_main_theorems)

**Axioms:** `s_finite_group`, `s_p_block_of_kG`
**Terminal:** `s_brauer_three_main_theorems` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_p_block_of_kG⟩` --[t_auxiliary_construction {brauer_correspondence: "B ↔ b between blocks of G and N_G(D) via defect group D"}]--> output: `s_brauer_block_correspondence`
2. input: `s_brauer_block_correspondence` --[t_character_decomposition_count {first_main: "blocks of G with defect D ↔ blocks of N_G(D) with defect D"}]--> output: `s_brauer_first_main`
3. input: `s_brauer_first_main` --[t_symmetry_reduction {second_third: "second/third theorems: decomposition matrices, principal block"}]--> output: `s_brauer_three_main_theorems`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_symmetry_reduction

---

### Frobenius determinant theorem (cite: https://en.wikipedia.org/wiki/Frobenius_determinant_theorem)

**Axioms:** `s_finite_group`, `s_group_determinant`
**Terminal:** `s_frobenius_determinant_theorem` (kind: theorem)

**Steps:**
1. input: `s_finite_group` --[t_auxiliary_construction {group_det: "group determinant Θ_G(x_g) = det(x_{gh^{-1}})"}]--> output: `s_group_determinant_polynomial`
2. input: `s_group_determinant_polynomial` --[t_character_decomposition_count {factor: "factors over ℂ as ∏_χ Θ_χ(x_g)^{χ(1)}"}]--> output: `s_factorization_into_irreducible_factors`
3. input: `s_factorization_into_irreducible_factors` --[t_structural_isomorphism {irreps: "irreducible factors ↔ irreducible characters"}]--> output: `s_frobenius_determinant_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_structural_isomorphism

---

### Hilbert–Burch theorem (cite: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Burch_theorem)

**Axioms:** `s_noetherian_local_ring`, `s_perfect_ideal_of_height_2`
**Terminal:** `s_hilbert_burch_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_noetherian_local_ring, s_perfect_ideal_of_height_2⟩` --[t_auxiliary_construction {resolution: "free resolution 0 → R^{n-1} → R^n → I → 0"}]--> output: `s_two_step_resolution`
2. input: `s_two_step_resolution` --[t_polynomial_method {minors: "I = α · (maximal minors of the (n-1)×n matrix)"}]--> output: `s_ideal_as_maximal_minors`
3. input: `s_two_step_resolution` --[t_structural_isomorphism {classify: "characterize all height-2 perfect ideals by their (n-1)×n matrices"}]--> output: `s_hilbert_burch_theorem`

**Techniques used:** t_auxiliary_construction, t_polynomial_method, t_structural_isomorphism

---

### Jacobson–Bourbaki theorem (cite: https://en.wikipedia.org/wiki/Jacobson%E2%80%93Bourbaki_theorem)

**Axioms:** `s_field_L`, `s_subring_of_endomorphisms`
**Terminal:** `s_jacobson_bourbaki_theorem` (kind: theorem)

**Steps:**
1. input: `s_field_L` --[t_auxiliary_construction {duality: "pair subfields K ⊆ L with subrings of End_K(L) closed under composition"}]--> output: `s_subring_subfield_pairing`
2. input: `s_subring_subfield_pairing` --[t_double_centralizer_decompose {commutant: "K is centralizer of End_K(L) and vice versa"}]--> output: `s_double_centralizer_field_endring`
3. input: `s_double_centralizer_field_endring` --[t_galois_correspondence {generalize: "non-Galois generalization of Galois correspondence"}]--> output: `s_jacobson_bourbaki_theorem`

**Techniques used:** t_auxiliary_construction, t_double_centralizer_decompose, t_galois_correspondence

---

### Gabriel's theorem on quivers (cite: https://en.wikipedia.org/wiki/Gabriel%27s_theorem)

**Axioms:** `s_quiver_Q`, `s_finite_dim_representation`
**Terminal:** `s_gabriel_quiver_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_quiver_Q, s_finite_dim_representation⟩` --[t_auxiliary_construction {tits_form: "Tits quadratic form q_Q(d) on dimension vectors"}]--> output: `s_tits_quadratic_form`
2. input: `s_tits_quadratic_form` --[t_character_decomposition_count {positive_definite: "q_Q positive definite ⇔ underlying graph is ADE Dynkin"}]--> output: `s_ade_dynkin_classification`
3. input: `s_ade_dynkin_classification` --[t_structural_isomorphism {bijection: "indecomposable reps ↔ positive roots of root system"}]--> output: `s_gabriel_quiver_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_structural_isomorphism

---

### Hurwitz's automorphism theorem (cite: https://en.wikipedia.org/wiki/Hurwitz%27s_automorphisms_theorem)

**Axioms:** `s_compact_riemann_surface`, `s_automorphism_group`
**Terminal:** `s_hurwitz_automorphism_theorem` (kind: theorem)

**Steps:**
1. input: `s_compact_riemann_surface` --[t_auxiliary_construction {quotient: "X/G as Riemann surface; ramified cover"}]--> output: `s_quotient_riemann_surface`
2. input: `s_quotient_riemann_surface` --[t_character_decomposition_count {riemann_hurwitz: "Riemann–Hurwitz: 2g_X - 2 = |G|(2g_Y - 2) + Σ ramification"}]--> output: `s_riemann_hurwitz_relation`
3. input: `s_riemann_hurwitz_relation` --[t_structural_isomorphism {bound: "|G| ≤ 84(g-1) for g ≥ 2"}]--> output: `s_hurwitz_automorphism_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_structural_isomorphism

---

### Burnside's basis theorem (cite: https://en.wikipedia.org/wiki/Burnside_basis_theorem)

**Axioms:** `s_finite_p_group`, `s_frattini_subgroup`
**Terminal:** `s_burnside_basis_theorem` (kind: theorem)

**Steps:**
1. input: `s_finite_p_group` --[t_auxiliary_construction {frattini: "Φ(G) = G^p [G,G]"}]--> output: `s_frattini_subgroup_definition`
2. input: `s_frattini_subgroup_definition` --[t_structural_isomorphism {fp_vsp: "G/Φ(G) is elementary abelian p-group, i.e., F_p-vector space"}]--> output: `s_quotient_is_fp_vsp`
3. input: `s_quotient_is_fp_vsp` --[t_character_decomposition_count {min_gen: "minimum number of generators of G equals dim(G/Φ(G))"}]--> output: `s_burnside_basis_theorem`

**Techniques used:** t_auxiliary_construction, t_structural_isomorphism, t_character_decomposition_count

---

### Higman's embedding theorem (cite: https://en.wikipedia.org/wiki/Higman%27s_embedding_theorem)

**Axioms:** `s_recursively_presented_group`, `s_finitely_presented_group`
**Terminal:** `s_higman_embedding_theorem` (kind: theorem)

**Steps:**
1. input: `s_recursively_presented_group` --[t_arithmetize_syntax {benign: "recursive enumeration of relators arithmetized"}]--> output: `s_arithmetized_relator_set`
2. input: `s_arithmetized_relator_set` --[t_auxiliary_construction {hnn: "HNN extensions implementing Turing-machine moves"}]--> output: `s_hnn_machine_simulation`
3. input: `s_hnn_machine_simulation` --[t_structural_isomorphism {embed: "G embeds into a finitely presented group H"}]--> output: `s_higman_embedding_theorem`

**Techniques used:** t_arithmetize_syntax, t_auxiliary_construction, t_structural_isomorphism

---

### Adian–Rabin theorem on Markov properties (cite: https://en.wikipedia.org/wiki/Adian%E2%80%93Rabin_theorem)

**Axioms:** `s_finitely_presented_group`, `s_markov_property_of_groups`
**Terminal:** `s_adian_rabin_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finitely_presented_group, s_markov_property_of_groups⟩` --[t_arithmetize_syntax {encode: "encode word problem in finite presentations"}]--> output: `s_word_problem_encoded`
2. input: `s_word_problem_encoded` --[t_diagonalize {reduce: "reduce halting/word problem to Markov property recognition"}]--> output: `s_diagonal_reduction_to_word_problem`
3. input: `s_diagonal_reduction_to_word_problem` --[t_reductio_ad_absurdum {conclude: "no algorithm decides any nontrivial Markov property"}]--> output: `s_adian_rabin_theorem`

**Techniques used:** t_arithmetize_syntax, t_diagonalize, t_reductio_ad_absurdum

---

### Cartan–Brauer–Hua theorem (cite: https://en.wikipedia.org/wiki/Cartan%E2%80%93Brauer%E2%80%93Hua_theorem)

**Axioms:** `s_division_ring`, `s_subdivision_ring_K`
**Terminal:** `s_cartan_brauer_hua_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_division_ring, s_subdivision_ring_K⟩` --[t_auxiliary_construction {hyp: "K invariant under conjugation: xKx^{-1} ⊆ K for all x"}]--> output: `s_conjugation_invariant_subring`
2. input: `s_conjugation_invariant_subring` --[t_symmetry_reduction {commutator: "commutator manipulations show K central or K = D"}]--> output: `s_commutator_argument`
3. input: `s_commutator_argument` --[t_structural_isomorphism {dichotomy: "K ⊆ Z(D) or K = D"}]--> output: `s_cartan_brauer_hua_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_structural_isomorphism

---

### Mac Lane's coherence theorem (cite: https://en.wikipedia.org/wiki/Coherence_theorem)

**Axioms:** `s_monoidal_category`, `s_associator_unitor_isomorphisms`
**Terminal:** `s_maclane_coherence_theorem` (kind: theorem)

**Steps:**
1. input: `s_monoidal_category` --[t_auxiliary_construction {pentagon: "pentagon and triangle axioms on associator α and unitors λ, ρ"}]--> output: `s_pentagon_and_triangle_axioms`
2. input: `s_pentagon_and_triangle_axioms` --[t_axiomatize_from_instances {graph: "free monoidal category on n objects; diagram of coherence morphisms"}]--> output: `s_coherence_diagram_setup`
3. input: `s_coherence_diagram_setup` --[t_structural_isomorphism {commute: "all formal diagrams commute"}]--> output: `s_maclane_coherence_theorem`

**Techniques used:** t_auxiliary_construction, t_axiomatize_from_instances, t_structural_isomorphism

---

### Fundamental theorem of finite division rings of squares (Frobenius–Stickelberger / classification of finite fields) (cite: https://en.wikipedia.org/wiki/Finite_field#Existence_and_uniqueness)

**Axioms:** `s_finite_field_Fq`, `s_prime_power_q`
**Terminal:** `s_finite_field_classification_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_field_Fq, s_prime_power_q⟩` --[t_auxiliary_construction {splitting: "splitting field of x^q − x over F_p"}]--> output: `s_splitting_field_of_xq_minus_x`
2. input: `s_splitting_field_of_xq_minus_x` --[t_character_decomposition_count {roots: "x^q − x has q distinct roots forming a subfield"}]--> output: `s_q_roots_form_subfield`
3. input: `s_q_roots_form_subfield` --[t_structural_isomorphism {classify: "unique field of order q = p^n up to iso; cyclic multiplicative group"}]--> output: `s_finite_field_classification_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_structural_isomorphism

---

### Tensor product universal property (cite: https://en.wikipedia.org/wiki/Tensor_product_of_modules)

**Axioms:** `s_ring_R`, `s_bilinear_map`
**Terminal:** `s_tensor_product_universal_property` (kind: theorem)

**Steps:**
1. input: `⟨s_ring_R, s_bilinear_map⟩` --[t_auxiliary_construction {quotient: "free R-module on M × N modulo bilinear relations"}]--> output: `s_tensor_product_construction`
2. input: `s_tensor_product_construction` --[t_representable_functor_trick {represent: "Hom_R(M ⊗_R N, P) ≅ Bilin_R(M × N, P)"}]--> output: `s_universal_property_via_hom`
3. input: `s_universal_property_via_hom` --[t_category_theoretic_colimits_and_adjoints {adjoint: "tensor–hom adjunction sets up universal mapping property"}]--> output: `s_tensor_product_universal_property`

**Techniques used:** t_auxiliary_construction, t_representable_functor_trick, t_category_theoretic_colimits_and_adjoints

---

### Cohn's irreducibility criterion (cite: https://en.wikipedia.org/wiki/Cohn%27s_irreducibility_criterion)

**Axioms:** `s_polynomial_ring_over_Q`, `s_prime_p`
**Terminal:** `s_cohn_irreducibility_criterion` (kind: theorem)

**Steps:**
1. input: `⟨s_polynomial_ring_over_Q, s_prime_p⟩` --[t_auxiliary_construction {base_b: "polynomial f(x) = Σ a_i x^i with 0 ≤ a_i < b and f(b) prime"}]--> output: `s_base_b_digits_of_prime`
2. input: `s_base_b_digits_of_prime` --[t_complex_analysis_to_integers {root_bound: "any root α of f satisfies Re(α) ≤ b/2 or |α| < some bound"}]--> output: `s_root_location_bound`
3. input: `s_root_location_bound` --[t_reductio_ad_absurdum {factor: "any factorization at integer b yields nontrivial factorization of prime f(b)"}]--> output: `s_cohn_irreducibility_criterion`

**Techniques used:** t_auxiliary_construction, t_complex_analysis_to_integers, t_reductio_ad_absurdum

---

### Hua's identity (cite: https://en.wikipedia.org/wiki/Hua%27s_identity)

**Axioms:** `s_division_ring`, `s_two_ring_elements`
**Terminal:** `s_hua_identity_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_division_ring, s_two_ring_elements⟩` --[t_auxiliary_construction {identity: "candidate identity a − (a^{-1} + (b^{-1} − a)^{-1})^{-1} = aba"}]--> output: `s_hua_candidate_identity`
2. input: `s_hua_candidate_identity` --[t_compose_with_identity {algebra: "expand using right and left inverses; clear denominators"}]--> output: `s_inverse_manipulation`
3. input: `s_inverse_manipulation` --[t_structural_isomorphism {jordan_homo: "ring-theoretic identity ⇒ additive maps preserving inverses are Jordan homomorphisms"}]--> output: `s_hua_identity_theorem`

**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_structural_isomorphism

---

### Itô's theorem on character degrees (cite: https://en.wikipedia.org/wiki/It%C3%B4%27s_theorem)

**Axioms:** `s_finite_group`, `s_abelian_normal_subgroup`
**Terminal:** `s_ito_character_degree_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_abelian_normal_subgroup⟩` --[t_auxiliary_construction {clifford: "Clifford theory of induced characters from A"}]--> output: `s_clifford_induced_characters`
2. input: `s_clifford_induced_characters` --[t_character_decomposition_count {stabilizer: "each χ ∈ Irr(G) restricts to multiple of orbit sum on A"}]--> output: `s_orbit_sum_on_A`
3. input: `s_orbit_sum_on_A` --[t_structural_isomorphism {divide: "χ(1) divides [G:A] for every irreducible character"}]--> output: `s_ito_character_degree_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_structural_isomorphism

---

### Krull–Akizuki theorem (cite: https://en.wikipedia.org/wiki/Krull%E2%80%93Akizuki_theorem)

**Axioms:** `s_noetherian_domain_dimension_one`, `s_finite_extension_of_fraction_fields`
**Terminal:** `s_krull_akizuki_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_noetherian_domain_dimension_one, s_finite_extension_of_fraction_fields⟩` --[t_auxiliary_construction {ring_between: "any ring B with A ⊆ B ⊆ L"}]--> output: `s_intermediate_ring_B`
2. input: `s_intermediate_ring_B` --[t_character_decomposition_count {length_bound: "length of B/aB finite for any nonzero a ∈ A"}]--> output: `s_finite_length_quotient`
3. input: `s_finite_length_quotient` --[t_axiomatize_from_instances {noetherian: "B noetherian, dim 1"}]--> output: `s_krull_akizuki_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_axiomatize_from_instances

---

### Universal property of localization (cite: https://en.wikipedia.org/wiki/Localization_(commutative_algebra))

**Axioms:** `s_commutative_ring`, `s_multiplicative_subset`
**Terminal:** `s_localization_universal_property` (kind: theorem)

**Steps:**
1. input: `⟨s_commutative_ring, s_multiplicative_subset⟩` --[t_auxiliary_construction {fractions: "construct S^{-1}R as equivalence classes (r,s)"}]--> output: `s_construction_of_localization`
2. input: `s_construction_of_localization` --[t_category_theoretic_colimits_and_adjoints {adjoint: "S^{-1}R is initial in rings making elements of S invertible"}]--> output: `s_localization_universal_property`

**Techniques used:** t_auxiliary_construction, t_category_theoretic_colimits_and_adjoints

---

### Splitting field existence and uniqueness (cite: https://en.wikipedia.org/wiki/Splitting_field)

**Axioms:** `s_field_K`, `s_polynomial_ring_over_Q`
**Terminal:** `s_splitting_field_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_field_K, s_polynomial_ring_over_Q⟩` --[t_auxiliary_construction {adjoin: "adjoin roots successively via K[x]/(irreducible factor)"}]--> output: `s_iterated_root_adjunction`
2. input: `s_iterated_root_adjunction` --[t_infinite_descent {finite: "termination after finitely many steps (degree drops)"}]--> output: `s_terminating_construction`
3. input: `s_terminating_construction` --[t_structural_isomorphism {unique: "isomorphism extension theorem gives uniqueness up to K-iso"}]--> output: `s_splitting_field_theorem`

**Techniques used:** t_auxiliary_construction, t_infinite_descent, t_structural_isomorphism

---

### Normal basis theorem (cite: https://en.wikipedia.org/wiki/Normal_basis)

**Axioms:** `s_finite_normal_separable_extension_L_over_K`, `s_galois_group`
**Terminal:** `s_normal_basis_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_normal_separable_extension_L_over_K, s_galois_group⟩` --[t_auxiliary_construction {regular_rep: "view L as K[G]-module via Galois action"}]--> output: `s_L_as_kG_module`
2. input: `s_L_as_kG_module` --[t_character_decomposition_count {linear_indep: "Artin's theorem: characters σ ∈ G are linearly independent over L"}]--> output: `s_dedekind_linear_independence`
3. input: `s_dedekind_linear_independence` --[t_structural_isomorphism {free: "L ≅ K[G] as K[G]-module, so ∃α with {σ(α)} K-basis"}]--> output: `s_normal_basis_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_structural_isomorphism

---

### Stickelberger's theorem on Gauss sums (cite: https://en.wikipedia.org/wiki/Stickelberger%27s_theorem)

**Axioms:** `s_cyclotomic_field_Q_zeta_n`, `s_galois_group`
**Terminal:** `s_stickelberger_theorem` (kind: theorem)

**Steps:**
1. input: `s_cyclotomic_field_Q_zeta_n` --[t_auxiliary_construction {gauss_sums: "Gauss sums g(χ) for character χ mod p"}]--> output: `s_gauss_sum_definition`
2. input: `s_gauss_sum_definition` --[t_character_decomposition_count {prime_factorization: "factorization of (g(χ)) in ℤ[ζ]"}]--> output: `s_gauss_sum_prime_factorization`
3. input: `s_gauss_sum_prime_factorization` --[t_structural_isomorphism {stickelberger_element: "ideal annihilator described by Stickelberger element θ ∈ ℚ[G]"}]--> output: `s_stickelberger_theorem`

**Techniques used:** t_auxiliary_construction, t_character_decomposition_count, t_structural_isomorphism

---

### Mac Lane's theorem on cohomology of cyclic groups (cite: https://en.wikipedia.org/wiki/Tate_cohomology_group)

**Axioms:** `s_finite_cyclic_group`, `s_g_module_M`
**Terminal:** `s_tate_cohomology_cyclic_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_cyclic_group, s_g_module_M⟩` --[t_auxiliary_construction {resolution: "periodic free resolution of ℤ over ℤ[G] for cyclic G"}]--> output: `s_periodic_resolution`
2. input: `s_periodic_resolution` --[t_deformation_cohomology {tate: "Tate cohomology Ĥ^n(G, M) is 2-periodic"}]--> output: `s_two_periodic_cohomology`
3. input: `s_two_periodic_cohomology` --[t_character_decomposition_count {formula: "Ĥ^0 = M^G/N_G M, Ĥ^1 = ker(N_G)/(1−σ)M"}]--> output: `s_tate_cohomology_cyclic_theorem`

**Techniques used:** t_auxiliary_construction, t_deformation_cohomology, t_character_decomposition_count

---

### Schur multiplier and central extensions (cite: https://en.wikipedia.org/wiki/Schur_multiplier)

**Axioms:** `s_finite_group`, `s_central_extension`
**Terminal:** `s_schur_multiplier_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_finite_group, s_central_extension⟩` --[t_auxiliary_construction {h2: "H^2(G, ℂ^×) classifies projective representations"}]--> output: `s_h2_classifies_projective_reps`
2. input: `s_h2_classifies_projective_reps` --[t_deformation_cohomology {schur_cover: "Schur cover G̃ trivializes the multiplier"}]--> output: `s_schur_cover_construction`
3. input: `s_schur_cover_construction` --[t_structural_isomorphism {universal: "G̃ universal central extension when G perfect"}]--> output: `s_schur_multiplier_theorem`

**Techniques used:** t_auxiliary_construction, t_deformation_cohomology, t_structural_isomorphism

---

### Wigner–Eckart theorem (cite: https://en.wikipedia.org/wiki/Wigner%E2%80%93Eckart_theorem)

**Axioms:** `s_compact_lie_group`, `s_tensor_operator`
**Terminal:** `s_wigner_eckart_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_compact_lie_group, s_tensor_operator⟩` --[t_auxiliary_construction {tensor_op: "irreducible tensor operator T^{(k)}_q under G"}]--> output: `s_irreducible_tensor_operator`
2. input: `s_irreducible_tensor_operator` --[t_symmetry_reduction {clebsch_gordan: "decompose tensor product j_1 ⊗ k via Clebsch–Gordan"}]--> output: `s_clebsch_gordan_decomposition`
3. input: `s_clebsch_gordan_decomposition` --[t_character_decomposition_count {factor: "matrix element = (CG coefficient) × (reduced matrix element)"}]--> output: `s_wigner_eckart_theorem`

**Techniques used:** t_auxiliary_construction, t_symmetry_reduction, t_character_decomposition_count

---

### Multiplicity-one theorem (cite: https://en.wikipedia.org/wiki/Multiplicity-one_theorem)

**Axioms:** `s_reductive_group_GL_n`, `s_irreducible_automorphic_representation`
**Terminal:** `s_multiplicity_one_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_reductive_group_GL_n, s_irreducible_automorphic_representation⟩` --[t_auxiliary_construction {whittaker: "global Whittaker model attached to π"}]--> output: `s_whittaker_model_for_pi`
2. input: `s_whittaker_model_for_pi` --[t_duality {uniqueness: "local uniqueness of Whittaker model"}]--> output: `s_local_whittaker_uniqueness`
3. input: `s_local_whittaker_uniqueness` --[t_structural_isomorphism {global: "global multiplicity of π in cuspidal spectrum is at most 1"}]--> output: `s_multiplicity_one_theorem`

**Techniques used:** t_auxiliary_construction, t_duality, t_structural_isomorphism

---

### Galois descent (cite: https://en.wikipedia.org/wiki/Galois_descent)

**Axioms:** `s_galois_extension_L_over_K`, `s_object_over_L_with_descent_data`
**Terminal:** `s_galois_descent_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_galois_extension_L_over_K, s_object_over_L_with_descent_data⟩` --[t_auxiliary_construction {cocycle: "1-cocycle σ ↦ φ_σ ∈ Aut(X_L) (descent datum)"}]--> output: `s_descent_cocycle`
2. input: `s_descent_cocycle` --[t_deformation_cohomology {h1: "isomorphism classes of K-forms = H^1(Gal(L/K), Aut(X))"}]--> output: `s_h1_classification_of_forms`
3. input: `s_h1_classification_of_forms` --[t_structural_isomorphism {descend: "object descends to K iff cocycle is a coboundary"}]--> output: `s_galois_descent_theorem`

**Techniques used:** t_auxiliary_construction, t_deformation_cohomology, t_structural_isomorphism

---
