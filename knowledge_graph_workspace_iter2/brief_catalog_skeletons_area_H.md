# Brief Catalog Skeletons — Area H (applied/misc)

Phase B bulk skeleton expansion. 40 theorems across 7 sections. One-step skeletons only, reusing existing toolbox technique ids.

---

## Probability (11)

### Kolmogorov's 0–1 law
**Terminal:** `s_kolmogorov_zero_one_law`
**Axioms:** `s_probability_axioms`
**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_frequency_decomposition]--> output: `s_kolmogorov_zero_one_law`

### Kolmogorov's extension theorem
**Terminal:** `s_kolmogorov_extension_theorem`
**Axioms:** `s_probability_axioms`
**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_compactness_argument]--> output: `s_kolmogorov_extension_theorem`

### Borel–Cantelli lemma
**Terminal:** `s_borel_cantelli_lemma`
**Axioms:** `s_probability_axioms`
**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_frequency_decomposition]--> output: `s_borel_cantelli_lemma`

### Doob's martingale convergence theorem
**Terminal:** `s_doob_martingale_convergence`
**Axioms:** `s_probability_axioms`
**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_compactness_argument]--> output: `s_doob_martingale_convergence`

### Doob's optional stopping theorem
**Terminal:** `s_doob_optional_stopping`
**Axioms:** `s_probability_axioms`
**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_conserved_quantity]--> output: `s_doob_optional_stopping`

### Itô's lemma
**Terminal:** `s_ito_lemma`
**Axioms:** `s_probability_axioms`
**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_interpolate_and_continue]--> output: `s_ito_lemma`

### Feynman–Kac formula
**Terminal:** `s_feynman_kac_formula`
**Axioms:** `s_probability_axioms`
**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_physics_to_pde]--> output: `s_feynman_kac_formula`

### Girsanov's theorem
**Terminal:** `s_girsanov_theorem`
**Axioms:** `s_probability_axioms`
**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_structural_isomorphism]--> output: `s_girsanov_theorem`

### Glivenko–Cantelli theorem
**Terminal:** `s_glivenko_cantelli`
**Axioms:** `s_iid_sequence_finite_variance`
**Steps:**
1. input: `⟨s_iid_sequence_finite_variance⟩` --[t_compactness_argument]--> output: `s_glivenko_cantelli`

### Donsker's theorem
**Terminal:** `s_donsker_theorem`
**Axioms:** `s_iid_sequence_finite_variance`
**Steps:**
1. input: `⟨s_iid_sequence_finite_variance⟩` --[t_compactness_argument]--> output: `s_donsker_theorem`

### Lindeberg–Feller central limit theorem
**Terminal:** `s_lindeberg_feller_clt`
**Axioms:** `s_probability_axioms`
**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_frequency_decomposition]--> output: `s_lindeberg_feller_clt`

---

## Dynamical Systems (Extra) (3)

### Sharkovskii's theorem
**Terminal:** `s_sharkovskii_theorem`
**Axioms:** `s_continuous_self_map`, `s_real_line_or_circle`
**Steps:**
1. input: `⟨s_continuous_self_map, s_real_line_or_circle⟩` --[t_obstruction_class]--> output: `s_sharkovskii_theorem`

### Birkhoff ergodic theorem (extra entry)
**Terminal:** `s_birkhoff_ergodic_theorem`
**Axioms:** `s_measure_preserving_transformation`
**Steps:**
1. input: `⟨s_measure_preserving_transformation⟩` --[t_conserved_quantity]--> output: `s_birkhoff_ergodic_theorem`

### Oseledets multiplicative ergodic theorem
**Terminal:** `s_oseledets_multiplicative_ergodic`
**Axioms:** `s_measure_preserving_transformation`
**Steps:**
1. input: `⟨s_measure_preserving_transformation⟩` --[t_svd_and_spectral_decomposition]--> output: `s_oseledets_multiplicative_ergodic`

---

## Category Theory (2)

### Yoneda lemma
**Terminal:** `s_yoneda_lemma`
**Axioms:** `s_diagram_in_C`
**Steps:**
1. input: `⟨s_diagram_in_C⟩` --[t_representable_functor_trick]--> output: `s_yoneda_lemma`

### Adjoint functor theorem
**Terminal:** `s_adjoint_functor_theorem`
**Axioms:** `s_diagram_in_C`
**Steps:**
1. input: `⟨s_diagram_in_C⟩` --[t_category_theoretic_colimits_and_adjoints]--> output: `s_adjoint_functor_theorem`

---

## Computer Science / Computability and Complexity (9)

### Rice's theorem
**Terminal:** `s_rice_theorem`
**Axioms:** `s_turing_machine_model`
**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_reductio_ad_absurdum]--> output: `s_rice_theorem`

### Cook–Levin theorem
**Terminal:** `s_cook_levin_theorem`
**Axioms:** `s_turing_machine_model`
**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_arithmetize_syntax]--> output: `s_cook_levin_theorem`

### Time hierarchy theorem
**Terminal:** `s_time_hierarchy_theorem`
**Axioms:** `s_turing_machine_model`
**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_diagonalize]--> output: `s_time_hierarchy_theorem`

### Space hierarchy theorem
**Terminal:** `s_space_hierarchy_theorem`
**Axioms:** `s_turing_machine_model`
**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_diagonalize]--> output: `s_space_hierarchy_theorem`

### Ladner's theorem
**Terminal:** `s_ladner_theorem`
**Axioms:** `s_turing_machine_model`
**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_diagonalize]--> output: `s_ladner_theorem`

### Immerman–Szelepcsényi theorem
**Terminal:** `s_immerman_szelepcsenyi`
**Axioms:** `s_turing_machine_model`
**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_finite_case_check]--> output: `s_immerman_szelepcsenyi`

### PCP theorem
**Terminal:** `s_pcp_theorem`
**Axioms:** `s_turing_machine_model`
**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_probabilistic_existence]--> output: `s_pcp_theorem`

### Gödel speed-up theorem
**Terminal:** `s_godel_speed_up_theorem`
**Axioms:** `s_first_order_peano_arithmetic`
**Steps:**
1. input: `⟨s_first_order_peano_arithmetic⟩` --[t_arithmetize_syntax]--> output: `s_godel_speed_up_theorem`

### Savitch's theorem
**Terminal:** `s_savitch_theorem`
**Axioms:** `s_turing_machine_model`
**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_finite_case_check]--> output: `s_savitch_theorem`

---

## Information Theory (4)

### Shannon's source coding theorem
**Terminal:** `s_shannon_source_coding`
**Axioms:** `s_probability_axioms`
**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_frequency_decomposition]--> output: `s_shannon_source_coding`

### Shannon's noisy-channel coding theorem
**Terminal:** `s_shannon_noisy_channel`
**Axioms:** `s_probability_axioms`
**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_probabilistic_existence]--> output: `s_shannon_noisy_channel`

### Shannon–Hartley theorem
**Terminal:** `s_shannon_hartley_theorem`
**Axioms:** `s_probability_axioms`
**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_frequency_decomposition]--> output: `s_shannon_hartley_theorem`

### Kraft's inequality
**Terminal:** `s_kraft_inequality`
**Axioms:** `s_probability_axioms`
**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_axiomatize_from_instances]--> output: `s_kraft_inequality`

---

## Mathematical Physics (7)

### CPT theorem
**Terminal:** `s_cpt_theorem`
**Axioms:** `s_lagrangian_action_integral`
**Steps:**
1. input: `⟨s_lagrangian_action_integral⟩` --[t_symmetry_reduction]--> output: `s_cpt_theorem`

### Spin-statistics theorem
**Terminal:** `s_spin_statistics_theorem`
**Axioms:** `s_lagrangian_action_integral`
**Steps:**
1. input: `⟨s_lagrangian_action_integral⟩` --[t_symmetry_reduction]--> output: `s_spin_statistics_theorem`

### Haag's theorem
**Terminal:** `s_haag_theorem`
**Axioms:** `s_lagrangian_action_integral`
**Steps:**
1. input: `⟨s_lagrangian_action_integral⟩` --[t_reductio_ad_absurdum]--> output: `s_haag_theorem`

### Noether's second theorem
**Terminal:** `s_noether_second_theorem`
**Axioms:** `s_lagrangian_action_integral`
**Steps:**
1. input: `⟨s_lagrangian_action_integral⟩` --[t_conserved_quantity]--> output: `s_noether_second_theorem`

### Reeh–Schlieder theorem
**Terminal:** `s_reeh_schlieder_theorem`
**Axioms:** `s_lagrangian_action_integral`
**Steps:**
1. input: `⟨s_lagrangian_action_integral⟩` --[t_structural_isomorphism]--> output: `s_reeh_schlieder_theorem`

### Bell's theorem
**Terminal:** `s_bell_theorem`
**Axioms:** `s_probability_axioms`
**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_reductio_ad_absurdum]--> output: `s_bell_theorem`

### Kochen–Specker theorem
**Terminal:** `s_kochen_specker_theorem`
**Axioms:** `s_probability_axioms`
**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_obstruction_class]--> output: `s_kochen_specker_theorem`

---

## Game Theory / Economics (mathematical) (4)

### Von Neumann's minimax theorem
**Terminal:** `s_von_neumann_minimax`
**Axioms:** `s_real_vector_space`
**Steps:**
1. input: `⟨s_real_vector_space⟩` --[t_compactness_argument]--> output: `s_von_neumann_minimax`

### Nash's existence theorem
**Terminal:** `s_nash_existence_theorem`
**Axioms:** `s_real_vector_space`
**Steps:**
1. input: `⟨s_real_vector_space⟩` --[t_contraction_fixed_point]--> output: `s_nash_existence_theorem`

### Arrow's impossibility theorem
**Terminal:** `s_arrow_impossibility`
**Axioms:** `s_real_vector_space`
**Steps:**
1. input: `⟨s_real_vector_space⟩` --[t_obstruction_class]--> output: `s_arrow_impossibility`

### Gibbard–Satterthwaite theorem
**Terminal:** `s_gibbard_satterthwaite`
**Axioms:** `s_real_vector_space`
**Steps:**
1. input: `⟨s_real_vector_space⟩` --[t_obstruction_class]--> output: `s_gibbard_satterthwaite`
