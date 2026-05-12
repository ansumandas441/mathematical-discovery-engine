# Area Theoretical Computer Science & Discrete Math Derivation Chains (iter-3)

**Source pages:**
- https://en.wikipedia.org/wiki/Category:Theorems_in_computational_complexity_theory
- https://en.wikipedia.org/wiki/Category:Theorems_in_theory_of_computation
- https://en.wikipedia.org/wiki/Category:Theorems_in_information_theory
- https://en.wikipedia.org/wiki/Category:Theorems_in_coding_theory
- https://en.wikipedia.org/wiki/Category:Theorems_in_discrete_mathematics

**Target:** 60 chains. **Drafted:** 68. **Skipped (already in graph):** 1 (`s_undecidability_of_halting` — Halting problem; we cite it as an axiom for downstream chains).

**Notes on overlap with sibling agents:**
- Rice's theorem partially overlaps Logic agent's computability slice — we keep the complexity-flavored statement (semantic properties of programs).
- Lovász local lemma partially overlaps Combinatorics agent — we keep the algorithmic/derandomization framing.
- Hall's marriage, Menger, König overlap Combinatorics — we keep the LP-duality / max-flow-min-cut bridge framing.
- Eulerian path criterion (already in graph) is the discrete-math analogue — not re-derived.

**Flagged (`⚠ needs new technique`):** 0. All 60 chains fit the 62-technique toolbox (the `t_polynomial_method`, `t_probabilistic_existence`, `t_diagonalize`, `t_pigeonhole_collision`, `t_duality`, `t_arithmetize_syntax`, `t_reduce_to_canonical_form`, `t_fourier_transform`, `t_compactness_argument` cover most of the CS canon naturally).

---

## Computability

### Rice's theorem (cite: https://en.wikipedia.org/wiki/Rice%27s_theorem)

**Axioms:** `s_turing_machine_model`, `s_encoding_of_machines_as_data`, `s_undecidability_of_halting`
**Terminal:** `s_rice_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model, s_encoding_of_machines_as_data⟩` --[t_axiomatize_from_instances {target: "non-trivial semantic property P of the language L(M)"}]--> output: `s_nontrivial_semantic_property_P`
2. input: `s_nontrivial_semantic_property_P` --[t_auxiliary_construction {target: "build reduction M_x that simulates x then runs witness machine for P"}]--> output: `s_reduction_from_halting_to_P`
3. input: `⟨s_reduction_from_halting_to_P, s_undecidability_of_halting⟩` --[t_reductio_ad_absurdum {target: "decider for P would decide halting"}]--> output: `s_rice_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_reductio_ad_absurdum

---

### Recursion theorem (Kleene's second) (cite: https://en.wikipedia.org/wiki/Kleene%27s_recursion_theorem)

**Axioms:** `s_turing_machine_model`, `s_encoding_of_machines_as_data`
**Terminal:** `s_kleene_recursion_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model, s_encoding_of_machines_as_data⟩` --[t_arithmetize_syntax {target: "computable indexing φ_e of partial recursive functions"}]--> output: `s_godel_numbering_of_programs`
2. input: `s_godel_numbering_of_programs` --[t_compose_with_identity {target: "diagonal padder d(x) := φ_x(x)"}]--> output: `s_diagonal_program_construction`
3. input: `s_diagonal_program_construction` --[t_contraction_fixed_point {target: "fixed-point index e with φ_e ≡ φ_{f(e)}"}]--> output: `s_kleene_recursion_theorem`

**Techniques used:** t_arithmetize_syntax, t_compose_with_identity, t_contraction_fixed_point

---

### Smn theorem (parameter theorem) (cite: https://en.wikipedia.org/wiki/Smn_theorem)

**Axioms:** `s_turing_machine_model`, `s_encoding_of_machines_as_data`
**Terminal:** `s_smn_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model, s_encoding_of_machines_as_data⟩` --[t_godel_numbering {target: "uniform program indexing"}]--> output: `s_uniform_program_index`
2. input: `s_uniform_program_index` --[t_auxiliary_construction {target: "compiler s^m_n that hardcodes m inputs into program text"}]--> output: `s_smn_theorem`

**Techniques used:** t_godel_numbering, t_auxiliary_construction

---

### Existence of RE but non-recursive sets (cite: https://en.wikipedia.org/wiki/Recursively_enumerable_set)

**Axioms:** `s_turing_machine_model`, `s_undecidability_of_halting`
**Terminal:** `s_re_not_recursive` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model, s_undecidability_of_halting⟩` --[t_axiomatize_from_instances {target: "halting set K = {⟨M,x⟩ : M(x)↓}"}]--> output: `s_halting_set_K`
2. input: `s_halting_set_K` --[t_verify_on_special_cases {target: "K is RE by dovetailing simulation"}]--> output: `s_K_is_re`
3. input: `⟨s_K_is_re, s_undecidability_of_halting⟩` --[t_reductio_ad_absurdum {target: "K recursive would decide halting"}]--> output: `s_re_not_recursive`

**Techniques used:** t_axiomatize_from_instances, t_verify_on_special_cases, t_reductio_ad_absurdum

---

## Complexity (Time and Space)

### Time hierarchy theorem (Hartmanis–Stearns) (cite: https://en.wikipedia.org/wiki/Time_hierarchy_theorem)

**Axioms:** `s_turing_machine_model`, `s_encoding_of_machines_as_data`
**Terminal:** `s_time_hierarchy_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model, s_encoding_of_machines_as_data⟩` --[t_axiomatize_from_instances {target: "time-constructible bound f(n) log f(n) = o(g(n))"}]--> output: `s_time_constructible_bound_pair`
2. input: `s_time_constructible_bound_pair` --[t_auxiliary_construction {target: "universal simulator with f(n)·log overhead clocked at g(n)"}]--> output: `s_clocked_universal_simulator`
3. input: `s_clocked_universal_simulator` --[t_diagonalize {target: "language flipping every f(n)-time machine on its own code"}]--> output: `s_time_hierarchy_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_diagonalize

---

### Space hierarchy theorem (cite: https://en.wikipedia.org/wiki/Space_hierarchy_theorem)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_space_hierarchy_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "space-constructible f(n) = o(g(n))"}]--> output: `s_space_constructible_bound_pair`
2. input: `s_space_constructible_bound_pair` --[t_auxiliary_construction {target: "configuration-graph simulator within g(n) tape cells"}]--> output: `s_space_clocked_simulator`
3. input: `s_space_clocked_simulator` --[t_diagonalize {target: "flip every f(n)-space machine on its own description"}]--> output: `s_space_hierarchy_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_diagonalize

---

### Savitch's theorem (NSPACE(s) ⊆ DSPACE(s²)) (cite: https://en.wikipedia.org/wiki/Savitch%27s_theorem)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_savitch_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_reduce_to_canonical_form {target: "nondeterministic acceptance ↔ reachability in configuration graph"}]--> output: `s_configuration_reachability_problem`
2. input: `s_configuration_reachability_problem` --[t_auxiliary_construction {target: "midpoint-recursion REACH(u,v,2^k) = ∃m REACH(u,m,2^{k-1}) ∧ REACH(m,v,2^{k-1})"}]--> output: `s_midpoint_recursion_for_reach`
3. input: `s_midpoint_recursion_for_reach` --[t_exhaustion_squeeze {target: "stack depth log²(2^s) = s² space; reuse"}]--> output: `s_savitch_theorem`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_exhaustion_squeeze

---

### Immerman–Szelepcsényi theorem (NL = co-NL) (cite: https://en.wikipedia.org/wiki/Immerman%E2%80%93Szelepcs%C3%A9nyi_theorem)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_immerman_szelepcsenyi` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_reduce_to_canonical_form {target: "co-NL = certify non-reachability in directed graph"}]--> output: `s_non_reachability_certificate_goal`
2. input: `s_non_reachability_certificate_goal` --[t_auxiliary_construction {target: "inductive counting: |R_{i+1}| from |R_i| using non-determinism"}]--> output: `s_inductive_counting_construction`
3. input: `s_inductive_counting_construction` --[t_pigeonhole_collision {target: "if guessed count matches, exactly enumerated reachable set; reject all others"}]--> output: `s_immerman_szelepcsenyi`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_pigeonhole_collision

---

### Cook–Levin theorem (SAT is NP-complete) (cite: https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem)

**Axioms:** `s_turing_machine_model`, `s_encoding_of_machines_as_data`
**Terminal:** `s_cook_levin_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "NP = poly-time verifier with poly certificate"}]--> output: `s_np_verifier_model`
2. input: `s_np_verifier_model` --[t_arithmetize_syntax {target: "tableau of computation as Boolean grid (cell, head, state) variables"}]--> output: `s_computation_tableau_encoding`
3. input: `s_computation_tableau_encoding` --[t_reduce_to_canonical_form {target: "local consistency clauses (start, transition, accept) yield 3-CNF"}]--> output: `s_local_consistency_cnf`
4. input: `s_local_consistency_cnf` --[t_auxiliary_construction {target: "polynomial-size SAT instance equivalent to acceptance"}]--> output: `s_cook_levin_theorem`

**Techniques used:** t_axiomatize_from_instances, t_arithmetize_syntax, t_reduce_to_canonical_form, t_auxiliary_construction

---

### Ladner's theorem (NP-intermediate exists if P ≠ NP) (cite: https://en.wikipedia.org/wiki/Ladner%27s_theorem)

**Axioms:** `s_turing_machine_model`, `s_cook_levin_theorem`
**Terminal:** `s_ladner_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_cook_levin_theorem⟩` --[t_auxiliary_construction {target: "blow holes in SAT on alternating intervals indexed by f(n)"}]--> output: `s_padded_sat_language`
2. input: `s_padded_sat_language` --[t_diagonalize {target: "f grows slowly enough to defeat every poly-time machine AND every Karp reducer from SAT"}]--> output: `s_double_diagonal_pad_schedule`
3. input: `s_double_diagonal_pad_schedule` --[t_reductio_ad_absurdum {target: "language is in NP, not in P, not NP-complete (under P≠NP)"}]--> output: `s_ladner_theorem`

**Techniques used:** t_auxiliary_construction, t_diagonalize, t_reductio_ad_absurdum

---

### Karp–Lipton theorem (NP ⊆ P/poly ⇒ PH = Σ₂) (cite: https://en.wikipedia.org/wiki/Karp%E2%80%93Lipton_theorem)

**Axioms:** `s_turing_machine_model`, `s_cook_levin_theorem`
**Terminal:** `s_karp_lipton_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_cook_levin_theorem⟩` --[t_axiomatize_from_instances {target: "hypothesize poly-size circuit family C_n decides SAT"}]--> output: `s_hypothetical_sat_circuit_family`
2. input: `s_hypothetical_sat_circuit_family` --[t_auxiliary_construction {target: "self-reducibility builds satisfying assignment by repeated circuit calls"}]--> output: `s_self_reducible_circuit_finder`
3. input: `s_self_reducible_circuit_finder` --[t_duality {target: "swap ∀ circuit guess / ∃ counterexample at level 2 of PH"}]--> output: `s_karp_lipton_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_duality

---

### Toda's theorem (PH ⊆ P^#P) (cite: https://en.wikipedia.org/wiki/Toda%27s_theorem)

**Axioms:** `s_turing_machine_model`, `s_cook_levin_theorem`
**Terminal:** `s_toda_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_cook_levin_theorem⟩` --[t_axiomatize_from_instances {target: "Valiant–Vazirani isolation = parity sees a unique witness w.h.p."}]--> output: `s_isolation_lemma_witness`
2. input: `s_isolation_lemma_witness` --[t_probabilistic_existence {target: "BPP⊕P ⊇ PH via random hash + ⊕P"}]--> output: `s_ph_inside_bpp_parity_p`
3. input: `s_ph_inside_bpp_parity_p` --[t_polynomial_method {target: "low-degree polynomials over ℤ encode ⊕P; #P captures coefficients"}]--> output: `s_parity_p_in_p_sharp_p`
4. input: `s_parity_p_in_p_sharp_p` --[t_compose_with_identity {target: "chain PH ⊆ BPP⊕P ⊆ P^#P"}]--> output: `s_toda_theorem`

**Techniques used:** t_axiomatize_from_instances, t_probabilistic_existence, t_polynomial_method, t_compose_with_identity

---

### PCP theorem (Arora–Lund–Motwani–Sudan–Szegedy) (cite: https://en.wikipedia.org/wiki/PCP_theorem)

**Axioms:** `s_turing_machine_model`, `s_cook_levin_theorem`
**Terminal:** `s_pcp_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_cook_levin_theorem⟩` --[t_axiomatize_from_instances {target: "probabilistically-checkable verifier with O(log n) randomness, O(1) queries"}]--> output: `s_pcp_verifier_model`
2. input: `s_pcp_verifier_model` --[t_polynomial_method {target: "low-degree extension + sum-check encodes NP witnesses as polynomial codewords"}]--> output: `s_low_degree_arithmetization`
3. input: `s_low_degree_arithmetization` --[t_auxiliary_construction {target: "composition of inner (constant query) and outer (log randomness) verifiers"}]--> output: `s_verifier_composition`
4. input: `s_verifier_composition` --[t_frequency_decomposition {target: "gap amplification by parallel repetition / expander walks"}]--> output: `s_pcp_theorem`

**Techniques used:** t_axiomatize_from_instances, t_polynomial_method, t_auxiliary_construction, t_frequency_decomposition

---

### Sipser–Gács–Lautemann theorem (BPP ⊆ Σ₂) (cite: https://en.wikipedia.org/wiki/Sipser%E2%80%93Lautemann_theorem)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_sipser_gacs_lautemann` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "BPP language with error 2^-n by amplification"}]--> output: `s_amplified_bpp_acceptance_set`
2. input: `s_amplified_bpp_acceptance_set` --[t_probabilistic_existence {target: "shifts {S_i} of accept set cover {0,1}^m for YES, miss for NO"}]--> output: `s_translation_cover_witness`
3. input: `s_translation_cover_witness` --[t_duality {target: "express cover by ∃ shift list ∀ string in Σ₂ form"}]--> output: `s_sipser_gacs_lautemann`

**Techniques used:** t_axiomatize_from_instances, t_probabilistic_existence, t_duality

---

## Probabilistic, Circuit, and Pseudorandomness

### Adleman's theorem (BPP ⊆ P/poly) (cite: https://en.wikipedia.org/wiki/Adleman%27s_theorem)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_adleman_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "BPP machine, amplify error to < 2^-n"}]--> output: `s_amplified_bpp_machine`
2. input: `s_amplified_bpp_machine` --[t_probabilistic_existence {target: "union bound: random r works for all 2^n inputs simultaneously w.p. > 0"}]--> output: `s_universal_advice_string`
3. input: `s_universal_advice_string` --[t_axiomatize_from_instances {target: "hardwire r_n as poly-size advice / circuit"}]--> output: `s_adleman_theorem`

**Techniques used:** t_axiomatize_from_instances, t_probabilistic_existence

---

### Yao's minimax principle (cite: https://en.wikipedia.org/wiki/Yao%27s_principle)

**Axioms:** `s_probability_axioms`, `s_turing_machine_model`
**Terminal:** `s_yao_minimax_principle` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "randomized algorithm = distribution over deterministic ones"}]--> output: `s_randomized_alg_as_mixed_strategy`
2. input: `s_randomized_alg_as_mixed_strategy` --[t_duality {target: "von Neumann minimax: min-max = max-min for zero-sum game (algorithm vs input distribution)"}]--> output: `s_yao_minimax_principle`

**Techniques used:** t_axiomatize_from_instances, t_duality

---

### Razborov–Smolensky lower bound on AC⁰[p] (cite: https://en.wikipedia.org/wiki/Razborov%E2%80%93Smolensky_theorem)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_razborov_smolensky` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "AC⁰[p] circuit with MOD-p gates, depth d, size s"}]--> output: `s_acc0_p_circuit_model`
2. input: `s_acc0_p_circuit_model` --[t_polynomial_method {target: "approximate every gate by polynomial of degree (log s)^O(d) over 𝔽_p"}]--> output: `s_low_degree_polynomial_approximation`
3. input: `s_low_degree_polynomial_approximation` --[t_pigeonhole_collision {target: "MOD-q (q≠p) has no such approximation; counting low-degree polys vs functions"}]--> output: `s_razborov_smolensky`

**Techniques used:** t_axiomatize_from_instances, t_polynomial_method, t_pigeonhole_collision

---

### Furst–Saxe–Sipser (parity ∉ AC⁰) (cite: https://en.wikipedia.org/wiki/AC0)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_parity_not_in_ac0` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "AC⁰ = constant-depth, unbounded fan-in, polynomial-size circuit"}]--> output: `s_ac0_circuit_model`
2. input: `s_ac0_circuit_model` --[t_probabilistic_existence {target: "random restriction ρ kills bottom AND/OR levels w.h.p."}]--> output: `s_random_restriction_argument`
3. input: `s_random_restriction_argument` --[t_exhaustion_squeeze {target: "iterated restriction reduces depth; surviving function is constant"}]--> output: `s_depth_reduction_to_constant`
4. input: `s_depth_reduction_to_constant` --[t_reductio_ad_absurdum {target: "parity not constant under any non-trivial restriction"}]--> output: `s_parity_not_in_ac0`

**Techniques used:** t_axiomatize_from_instances, t_probabilistic_existence, t_exhaustion_squeeze, t_reductio_ad_absurdum

---

### Håstad's switching lemma (cite: https://en.wikipedia.org/wiki/Switching_lemma)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_hastad_switching_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "k-DNF formula F and random restriction ρ keeping each var with prob p"}]--> output: `s_random_restriction_on_dnf`
2. input: `s_random_restriction_on_dnf` --[t_probabilistic_existence {target: "encode every bad decision-tree path as injection into restricted DNFs"}]--> output: `s_encoding_of_bad_paths`
3. input: `s_encoding_of_bad_paths` --[t_pigeonhole_collision {target: "counting injection ⇒ Pr[depth > t] ≤ (5pk)^t"}]--> output: `s_hastad_switching_lemma`

**Techniques used:** t_axiomatize_from_instances, t_probabilistic_existence, t_pigeonhole_collision

---

### Isolation lemma (Mulmuley–Vazirani–Vazirani) (cite: https://en.wikipedia.org/wiki/Isolation_lemma)

**Axioms:** `s_probability_axioms`
**Terminal:** `s_isolation_lemma_mvv` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_axiomatize_from_instances {target: "set system F ⊆ 2^[n] with random weights w_i ∈ [1..2n]"}]--> output: `s_random_weighted_set_system`
2. input: `s_random_weighted_set_system` --[t_probabilistic_existence {target: "Pr[unique minimum-weight S] ≥ 1/2 by union bound over each element"}]--> output: `s_isolation_lemma_mvv`

**Techniques used:** t_axiomatize_from_instances, t_probabilistic_existence

---

### Schwartz–Zippel lemma (cite: https://en.wikipedia.org/wiki/Schwartz%E2%80%93Zippel_lemma)

**Axioms:** `s_probability_axioms`
**Terminal:** `s_schwartz_zippel_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_axiomatize_from_instances {target: "nonzero polynomial P of total degree d over field F, sample S ⊆ F"}]--> output: `s_polynomial_and_sample_set`
2. input: `s_polynomial_and_sample_set` --[t_polynomial_method {target: "induction on variables: factor as P = Σ_i x_n^i Q_i(x_1,...,x_{n-1}); top Q is nonzero"}]--> output: `s_inductive_root_bound`
3. input: `s_inductive_root_bound` --[t_exhaustion_squeeze {target: "Pr[P(r)=0] ≤ d/|S|"}]--> output: `s_schwartz_zippel_lemma`

**Techniques used:** t_axiomatize_from_instances, t_polynomial_method, t_exhaustion_squeeze

---

### Valiant–Vazirani theorem (UNIQUE-SAT randomized hardness) (cite: https://en.wikipedia.org/wiki/Valiant%E2%80%93Vazirani_theorem)

**Axioms:** `s_cook_levin_theorem`, `s_probability_axioms`
**Terminal:** `s_valiant_vazirani` (kind: theorem)

**Steps:**
1. input: `⟨s_cook_levin_theorem⟩` --[t_axiomatize_from_instances {target: "SAT instance φ with unknown solution count S"}]--> output: `s_sat_instance_with_unknown_count`
2. input: `s_sat_instance_with_unknown_count` --[t_auxiliary_construction {target: "add random pairwise-independent hash constraints h(x) = 0 to thin out solutions"}]--> output: `s_hashed_sat_instance`
3. input: `s_hashed_sat_instance` --[t_probabilistic_existence {target: "for some hash size k, exactly one solution survives w.p. ≥ 1/(4n)"}]--> output: `s_valiant_vazirani`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_probabilistic_existence

---

## Interactive Proofs and Cryptography

### IP = PSPACE (Shamir) (cite: https://en.wikipedia.org/wiki/IP_(complexity))

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_ip_equals_pspace` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "TQBF as canonical PSPACE-complete problem with quantifier alternation"}]--> output: `s_tqbf_canonical_form`
2. input: `s_tqbf_canonical_form` --[t_polynomial_method {target: "arithmetize quantified Boolean formula to low-degree polynomial over 𝔽_p"}]--> output: `s_arithmetized_tqbf`
3. input: `s_arithmetized_tqbf` --[t_auxiliary_construction {target: "sum-check / degree-reduce protocol layer by layer with verifier random points"}]--> output: `s_sum_check_protocol`
4. input: `s_sum_check_protocol` --[t_compose_with_identity {target: "IP ⊆ PSPACE by simulating prover; IP ⊇ PSPACE by protocol"}]--> output: `s_ip_equals_pspace`

**Techniques used:** t_axiomatize_from_instances, t_polynomial_method, t_auxiliary_construction, t_compose_with_identity

---

### MIP = NEXP (Babai–Fortnow–Lund) (cite: https://en.wikipedia.org/wiki/MIP_(complexity))

**Axioms:** `s_turing_machine_model`, `s_ip_equals_pspace`
**Terminal:** `s_mip_equals_nexp` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "multi-prover protocol — non-communicating provers share strategy but not transcript"}]--> output: `s_multi_prover_model`
2. input: `s_multi_prover_model` --[t_polynomial_method {target: "scale arithmetization to exponential-size SAT (NEXP witness as multilinear polynomial)"}]--> output: `s_scaled_arithmetization_nexp`
3. input: `s_scaled_arithmetization_nexp` --[t_auxiliary_construction {target: "oracle protocol with two provers cross-checking polynomial evaluations"}]--> output: `s_two_prover_oracle_protocol`
4. input: `s_two_prover_oracle_protocol` --[t_duality {target: "MIP ⊇ NEXP via protocol; MIP ⊆ NEXP by guessing prover strategy"}]--> output: `s_mip_equals_nexp`

**Techniques used:** t_axiomatize_from_instances, t_polynomial_method, t_auxiliary_construction, t_duality

---

### GMW zero-knowledge for NP (cite: https://en.wikipedia.org/wiki/Zero-knowledge_proof)

**Axioms:** `s_cook_levin_theorem`, `s_probability_axioms`
**Terminal:** `s_gmw_zk_for_np` (kind: theorem)

**Steps:**
1. input: `⟨s_cook_levin_theorem⟩` --[t_reduce_to_canonical_form {target: "Karp-reduce NP language to 3-COLORING"}]--> output: `s_three_coloring_canonical_target`
2. input: `s_three_coloring_canonical_target` --[t_auxiliary_construction {target: "commit to random permutation of colors; verifier picks one edge"}]--> output: `s_commit_and_challenge_protocol`
3. input: `s_commit_and_challenge_protocol` --[t_probabilistic_existence {target: "simulator paradigm: indistinguishable transcript without witness, soundness 1/|E|"}]--> output: `s_gmw_zk_for_np`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_probabilistic_existence

---

## Information Theory and Coding Theory

### Shannon source coding theorem (cite: https://en.wikipedia.org/wiki/Shannon%27s_source_coding_theorem)

**Axioms:** `s_probability_axioms`
**Terminal:** `s_shannon_source_coding` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_axiomatize_from_instances {target: "i.i.d. source X with entropy H(X) := -Σ p log p"}]--> output: `s_iid_source_with_entropy`
2. input: `s_iid_source_with_entropy` --[t_probabilistic_existence {target: "typical set A_ε^(n) has size ≈ 2^{nH} and total probability ≈ 1"}]--> output: `s_typical_set`
3. input: `s_typical_set` --[t_pigeonhole_collision {target: "any code with < 2^{n(H-ε)} codewords misses positive mass of typical sequences"}]--> output: `s_shannon_source_coding`

**Techniques used:** t_axiomatize_from_instances, t_probabilistic_existence, t_pigeonhole_collision

---

### Shannon noisy channel coding theorem (cite: https://en.wikipedia.org/wiki/Noisy-channel_coding_theorem)

**Axioms:** `s_probability_axioms`
**Terminal:** `s_shannon_channel_coding` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_axiomatize_from_instances {target: "discrete memoryless channel W(y|x), capacity C := max_{p(x)} I(X;Y)"}]--> output: `s_dmc_capacity_definition`
2. input: `s_dmc_capacity_definition` --[t_probabilistic_existence {target: "random codebook of 2^{nR} i.i.d. codewords with R < C"}]--> output: `s_random_codebook_achievability`
3. input: `s_random_codebook_achievability` --[t_pigeonhole_collision {target: "Fano's inequality forces R ≤ C for any reliable code (converse)"}]--> output: `s_shannon_channel_coding`

**Techniques used:** t_axiomatize_from_instances, t_probabilistic_existence, t_pigeonhole_collision

---

### Shannon–Hartley theorem (cite: https://en.wikipedia.org/wiki/Shannon%E2%80%93Hartley_theorem)

**Axioms:** `s_probability_axioms`, `s_shannon_channel_coding`
**Terminal:** `s_shannon_hartley_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_shannon_channel_coding⟩` --[t_axiomatize_from_instances {target: "AWGN channel with bandwidth B, signal power S, noise power N"}]--> output: `s_awgn_channel_model`
2. input: `s_awgn_channel_model` --[t_svd_and_spectral_decomposition {target: "Gaussian input maximizes differential entropy; capacity = (1/2)log(1+S/N) per sample"}]--> output: `s_gaussian_capacity_formula`
3. input: `s_gaussian_capacity_formula` --[t_compose_with_identity {target: "Nyquist 2B samples/sec ⇒ C = B log₂(1+S/N) bits/sec"}]--> output: `s_shannon_hartley_theorem`

**Techniques used:** t_axiomatize_from_instances, t_svd_and_spectral_decomposition, t_compose_with_identity

---

### Kraft–McMillan inequality (cite: https://en.wikipedia.org/wiki/Kraft%E2%80%93McMillan_inequality)

**Axioms:** `s_probability_axioms`
**Terminal:** `s_kraft_mcmillan_inequality` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_axiomatize_from_instances {target: "uniquely decodable code with codeword lengths l_1,...,l_k over alphabet of size D"}]--> output: `s_uniquely_decodable_code_model`
2. input: `s_uniquely_decodable_code_model` --[t_pigeonhole_collision {target: "extension argument: (Σ D^{-l_i})^n counts n-fold concatenations injectively, so bounded by D^{n·l_max}"}]--> output: `s_extension_counting_bound`
3. input: `s_extension_counting_bound` --[t_exhaustion_squeeze {target: "take n-th root and limit ⇒ Σ D^{-l_i} ≤ 1"}]--> output: `s_kraft_mcmillan_inequality`

**Techniques used:** t_axiomatize_from_instances, t_pigeonhole_collision, t_exhaustion_squeeze

---

### Slepian–Wolf theorem (cite: https://en.wikipedia.org/wiki/Slepian%E2%80%93Wolf_coding)

**Axioms:** `s_probability_axioms`, `s_shannon_source_coding`
**Terminal:** `s_slepian_wolf_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_shannon_source_coding⟩` --[t_axiomatize_from_instances {target: "correlated sources (X,Y) encoded separately, decoded jointly"}]--> output: `s_correlated_source_model`
2. input: `s_correlated_source_model` --[t_probabilistic_existence {target: "random binning: assign each x to one of 2^{nR_X} bins uniformly"}]--> output: `s_random_binning_scheme`
3. input: `s_random_binning_scheme` --[t_pigeonhole_collision {target: "joint typicality decoder succeeds iff R_X ≥ H(X|Y), R_Y ≥ H(Y|X), R_X+R_Y ≥ H(X,Y)"}]--> output: `s_slepian_wolf_theorem`

**Techniques used:** t_axiomatize_from_instances, t_probabilistic_existence, t_pigeonhole_collision

---

### Wyner–Ziv theorem (cite: https://en.wikipedia.org/wiki/Wyner%E2%80%93Ziv_coding)

**Axioms:** `s_probability_axioms`, `s_shannon_channel_coding`
**Terminal:** `s_wyner_ziv_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_shannon_channel_coding⟩` --[t_axiomatize_from_instances {target: "lossy source coding with side info Y at decoder only"}]--> output: `s_side_info_source_model`
2. input: `s_side_info_source_model` --[t_auxiliary_construction {target: "auxiliary random variable U with Markov chain U–X–Y, rate I(X;U)−I(Y;U)"}]--> output: `s_auxiliary_u_construction`
3. input: `s_auxiliary_u_construction` --[t_probabilistic_existence {target: "random binning of U-codebook + joint typicality decoder achieves R_WZ(D)"}]--> output: `s_wyner_ziv_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_probabilistic_existence

---

### Singleton bound (cite: https://en.wikipedia.org/wiki/Singleton_bound)

**Axioms:** `s_probability_axioms`
**Terminal:** `s_singleton_bound` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_axiomatize_from_instances {target: "code C ⊆ Σ^n, |Σ|=q, minimum distance d, size M"}]--> output: `s_block_code_model`
2. input: `s_block_code_model` --[t_projection_to_subspace {target: "puncture d-1 coordinates: codewords remain distinct"}]--> output: `s_punctured_code_injection`
3. input: `s_punctured_code_injection` --[t_pigeonhole_collision {target: "M ≤ q^{n-d+1}"}]--> output: `s_singleton_bound`

**Techniques used:** t_axiomatize_from_instances, t_projection_to_subspace, t_pigeonhole_collision

---

### Plotkin bound (cite: https://en.wikipedia.org/wiki/Plotkin_bound)

**Axioms:** `s_probability_axioms`
**Terminal:** `s_plotkin_bound` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_axiomatize_from_instances {target: "binary code with d > n/2"}]--> output: `s_high_distance_binary_code`
2. input: `s_high_distance_binary_code` --[t_auxiliary_construction {target: "double-count sum of pairwise Hamming distances Σ_{i<j} d(c_i,c_j) over each coordinate"}]--> output: `s_double_count_pairwise_distances`
3. input: `s_double_count_pairwise_distances` --[t_exhaustion_squeeze {target: "M·(M-1)·d ≤ n·M²/2 ⇒ M ≤ 2d/(2d-n)"}]--> output: `s_plotkin_bound`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_exhaustion_squeeze

---

### Hamming (sphere-packing) bound (cite: https://en.wikipedia.org/wiki/Hamming_bound)

**Axioms:** `s_probability_axioms`
**Terminal:** `s_hamming_bound` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_axiomatize_from_instances {target: "code with distance d=2t+1 corrects t errors"}]--> output: `s_t_error_correcting_code`
2. input: `s_t_error_correcting_code` --[t_auxiliary_construction {target: "Hamming balls of radius t around codewords are disjoint"}]--> output: `s_disjoint_hamming_balls`
3. input: `s_disjoint_hamming_balls` --[t_pigeonhole_collision {target: "M · Σ_{i=0}^t C(n,i)(q-1)^i ≤ q^n"}]--> output: `s_hamming_bound`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_pigeonhole_collision

---

### Gilbert–Varshamov bound (cite: https://en.wikipedia.org/wiki/Gilbert%E2%80%93Varshamov_bound)

**Axioms:** `s_probability_axioms`
**Terminal:** `s_gilbert_varshamov_bound` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_axiomatize_from_instances {target: "greedy/random construction of code with min distance d"}]--> output: `s_greedy_code_construction`
2. input: `s_greedy_code_construction` --[t_probabilistic_existence {target: "random codeword avoids all forbidden balls if |C|·V(n,d-1) < q^n"}]--> output: `s_gilbert_varshamov_bound`

**Techniques used:** t_axiomatize_from_instances, t_probabilistic_existence

---

### MRRW (linear programming) bound (cite: https://en.wikipedia.org/wiki/Linear_programming_bound)

**Axioms:** `s_probability_axioms`
**Terminal:** `s_mrrw_lp_bound` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_axiomatize_from_instances {target: "distance distribution {A_i} of code on Hamming scheme"}]--> output: `s_distance_distribution_polynomials`
2. input: `s_distance_distribution_polynomials` --[t_character_decomposition_count {target: "Krawtchouk polynomials = characters of binary Hamming association scheme; Delsarte LP"}]--> output: `s_delsarte_linear_program`
3. input: `s_delsarte_linear_program` --[t_duality {target: "feasible dual polynomial f with f̂ ≥ 0 bounds |C|"}]--> output: `s_mrrw_dual_polynomial`
4. input: `s_mrrw_dual_polynomial` --[t_polynomial_method {target: "explicit dual built from Krawtchouk roots; asymptotic rate-distance tradeoff"}]--> output: `s_mrrw_lp_bound`

**Techniques used:** t_axiomatize_from_instances, t_character_decomposition_count, t_duality, t_polynomial_method

---

### Reed–Solomon distance / BCH bound (cite: https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction)

**Axioms:** `s_polynomial_ring`
**Terminal:** `s_reed_solomon_distance` (kind: theorem)

**Steps:**
1. input: `⟨s_polynomial_ring⟩` --[t_axiomatize_from_instances {target: "RS code = evaluations of degree < k polynomials over F_q at n points"}]--> output: `s_rs_code_definition`
2. input: `s_rs_code_definition` --[t_polynomial_method {target: "nonzero polynomial of degree < k has < k roots"}]--> output: `s_root_count_argument`
3. input: `s_root_count_argument` --[t_exhaustion_squeeze {target: "min distance ≥ n - k + 1; Singleton attained (MDS)"}]--> output: `s_reed_solomon_distance`

**Techniques used:** t_axiomatize_from_instances, t_polynomial_method, t_exhaustion_squeeze

---

## Convex Geometry and Discrete Math

### Helly's theorem (cite: https://en.wikipedia.org/wiki/Helly%27s_theorem)

**Axioms:** `s_real_vector_space`
**Terminal:** `s_helly_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_real_vector_space⟩` --[t_axiomatize_from_instances {target: "finite family of convex sets in ℝ^d, every d+1 have nonempty intersection"}]--> output: `s_helly_local_hypothesis`
2. input: `s_helly_local_hypothesis` --[t_auxiliary_construction {target: "induction: pick a_i ∈ ∩_{j≠i} C_j; apply Radon partition of {a_0,...,a_d+1}"}]--> output: `s_radon_partition_step`
3. input: `s_radon_partition_step` --[t_exhaustion_squeeze {target: "Radon intersection point lies in every C_j ⇒ global intersection"}]--> output: `s_helly_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_exhaustion_squeeze

---

### Carathéodory's theorem (convex hull) (cite: https://en.wikipedia.org/wiki/Carath%C3%A9odory%27s_theorem_(convex_hull))

**Axioms:** `s_real_vector_space`
**Terminal:** `s_caratheodory_convex` (kind: theorem)

**Steps:**
1. input: `⟨s_real_vector_space⟩` --[t_axiomatize_from_instances {target: "point x in conv(S) ⊆ ℝ^d expressed as Σ λ_i p_i with λ_i ≥ 0, Σλ_i=1"}]--> output: `s_convex_combination_with_k_points`
2. input: `s_convex_combination_with_k_points` --[t_reduce_to_canonical_form {target: "if k > d+1, points p_i are affinely dependent ⇒ Σ μ_i p_i = 0 with Σ μ_i = 0"}]--> output: `s_affine_dependence_relation`
3. input: `s_affine_dependence_relation` --[t_exhaustion_squeeze {target: "slide λ + tμ until one λ_i = 0; reduces support"}]--> output: `s_caratheodory_convex`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

### Radon's theorem (cite: https://en.wikipedia.org/wiki/Radon%27s_theorem)

**Axioms:** `s_real_vector_space`
**Terminal:** `s_radon_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_real_vector_space⟩` --[t_axiomatize_from_instances {target: "d+2 points in ℝ^d"}]--> output: `s_d_plus_two_points`
2. input: `s_d_plus_two_points` --[t_reduce_to_canonical_form {target: "homogenize: (d+2) vectors in ℝ^{d+1} are linearly dependent"}]--> output: `s_linear_dependence_in_d_plus_one`
3. input: `s_linear_dependence_in_d_plus_one` --[t_auxiliary_construction {target: "split coefficients by sign into two groups; convex combinations agree"}]--> output: `s_radon_theorem`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form, t_auxiliary_construction

---

### Tverberg's theorem (cite: https://en.wikipedia.org/wiki/Tverberg%27s_theorem)

**Axioms:** `s_real_vector_space`, `s_radon_theorem`
**Terminal:** `s_tverberg_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_radon_theorem⟩` --[t_axiomatize_from_instances {target: "(r-1)(d+1)+1 points in ℝ^d to be partitioned into r convex-overlapping parts"}]--> output: `s_tverberg_input_count`
2. input: `s_tverberg_input_count` --[t_raise_dimension {target: "lift to deleted-join configuration space; equivariant under symmetric group action"}]--> output: `s_deleted_join_configuration_space`
3. input: `s_deleted_join_configuration_space` --[t_obstruction_class {target: "equivariant topology: no S_r-map to sphere of low dimension ⇒ Tverberg partition exists"}]--> output: `s_tverberg_theorem`

**Techniques used:** t_axiomatize_from_instances, t_raise_dimension, t_obstruction_class

---

### Colored Tverberg (Bárány–Larman / Blagojević–Matschke–Ziegler) (cite: https://en.wikipedia.org/wiki/Tverberg%27s_theorem#Colored_Tverberg_theorem)

**Axioms:** `s_real_vector_space`, `s_tverberg_theorem`
**Terminal:** `s_colored_tverberg` (kind: theorem)

**Steps:**
1. input: `⟨s_tverberg_theorem⟩` --[t_axiomatize_from_instances {target: "rainbow partition: pick one point per color class so r parts each rainbow"}]--> output: `s_rainbow_partition_problem`
2. input: `s_rainbow_partition_problem` --[t_raise_dimension {target: "constrained configuration space — chessboard complex of color classes"}]--> output: `s_chessboard_complex`
3. input: `s_chessboard_complex` --[t_obstruction_class {target: "equivariant cohomology of chessboard complex; vanishing index for r prime"}]--> output: `s_colored_tverberg`

**Techniques used:** t_axiomatize_from_instances, t_raise_dimension, t_obstruction_class

---

### Bárány's point-selection theorem (cite: https://en.wikipedia.org/wiki/B%C3%A1r%C3%A1ny%27s_theorem)

**Axioms:** `s_real_vector_space`, `s_tverberg_theorem`
**Terminal:** `s_barany_point_selection` (kind: theorem)

**Steps:**
1. input: `⟨s_tverberg_theorem⟩` --[t_axiomatize_from_instances {target: "n points in ℝ^d, consider all C(n,d+1) simplices"}]--> output: `s_simplex_family_on_n_points`
2. input: `s_simplex_family_on_n_points` --[t_probabilistic_existence {target: "first-moment: some point p hits ≥ c_d fraction of simplices by Tverberg partition averaging"}]--> output: `s_barany_point_selection`

**Techniques used:** t_axiomatize_from_instances, t_probabilistic_existence

---

## Linear Programming and Polyhedral Duality

### LP strong duality (cite: https://en.wikipedia.org/wiki/Linear_programming#Duality)

**Axioms:** `s_real_vector_space`
**Terminal:** `s_lp_strong_duality` (kind: theorem)

**Steps:**
1. input: `⟨s_real_vector_space⟩` --[t_axiomatize_from_instances {target: "primal max c^T x s.t. Ax ≤ b, x ≥ 0; dual min b^T y s.t. A^T y ≥ c, y ≥ 0"}]--> output: `s_primal_dual_lp_pair`
2. input: `s_primal_dual_lp_pair` --[t_compose_with_identity {target: "weak duality c^T x ≤ y^T A x ≤ b^T y at any feasible pair"}]--> output: `s_lp_weak_duality`
3. input: `s_lp_weak_duality` --[t_duality {target: "Farkas separation: if optimal gap > 0, hyperplane certificate contradicts feasibility"}]--> output: `s_lp_strong_duality`

**Techniques used:** t_axiomatize_from_instances, t_compose_with_identity, t_duality

---

### Farkas's lemma (cite: https://en.wikipedia.org/wiki/Farkas%27_lemma)

**Axioms:** `s_real_vector_space`
**Terminal:** `s_farkas_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_real_vector_space⟩` --[t_axiomatize_from_instances {target: "either Ax = b has x ≥ 0 solution, or A^T y ≤ 0, b^T y > 0 has a solution"}]--> output: `s_farkas_alternatives`
2. input: `s_farkas_alternatives` --[t_projection_to_subspace {target: "cone(A) is closed convex; separate b from cone by hyperplane (Hahn–Banach in ℝ^n)"}]--> output: `s_separating_hyperplane_for_cone`
3. input: `s_separating_hyperplane_for_cone` --[t_duality {target: "hyperplane normal y witnesses the second alternative"}]--> output: `s_farkas_lemma`

**Techniques used:** t_axiomatize_from_instances, t_projection_to_subspace, t_duality

---

### Gordan's theorem of alternatives (cite: https://en.wikipedia.org/wiki/Theorem_of_alternatives)

**Axioms:** `s_real_vector_space`, `s_farkas_lemma`
**Terminal:** `s_gordan_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_farkas_lemma⟩` --[t_axiomatize_from_instances {target: "either Ax < 0 has a solution, or A^T y = 0, y ≥ 0, y ≠ 0 has a solution"}]--> output: `s_gordan_alternatives`
2. input: `s_gordan_alternatives` --[t_duality {target: "specialize Farkas to strict inequality cone"}]--> output: `s_gordan_theorem`

**Techniques used:** t_axiomatize_from_instances, t_duality

---

### Stiemke's theorem (cite: https://en.wikipedia.org/wiki/Theorem_of_alternatives#Stiemke's_lemma)

**Axioms:** `s_real_vector_space`, `s_farkas_lemma`
**Terminal:** `s_stiemke_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_farkas_lemma⟩` --[t_axiomatize_from_instances {target: "either A^T y ≤ 0, y > 0 has a solution, or Ax ≥ 0, Ax ≠ 0 has a solution"}]--> output: `s_stiemke_alternatives`
2. input: `s_stiemke_alternatives` --[t_duality {target: "polar/dual form of Farkas with strict-positivity on multipliers"}]--> output: `s_stiemke_theorem`

**Techniques used:** t_axiomatize_from_instances, t_duality

---

### Ellipsoid method polynomial-time (Khachiyan) (cite: https://en.wikipedia.org/wiki/Ellipsoid_method)

**Axioms:** `s_real_vector_space`, `s_lp_strong_duality`
**Terminal:** `s_khachiyan_ellipsoid` (kind: theorem)

**Steps:**
1. input: `⟨s_lp_strong_duality⟩` --[t_reduce_to_canonical_form {target: "LP feasibility = find x in convex polytope P with separation oracle"}]--> output: `s_separation_oracle_lp`
2. input: `s_separation_oracle_lp` --[t_auxiliary_construction {target: "ellipsoid E_k containing P; query oracle; cut and update center; new ellipsoid shrinks volume"}]--> output: `s_ellipsoid_volume_shrinkage_iteration`
3. input: `s_ellipsoid_volume_shrinkage_iteration` --[t_exhaustion_squeeze {target: "vol(E_k)/vol(E_0) ≤ e^{-k/(2(n+1))}; poly iterations suffice"}]--> output: `s_khachiyan_ellipsoid`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_exhaustion_squeeze

---

### Karmarkar interior-point polynomial-time (cite: https://en.wikipedia.org/wiki/Karmarkar%27s_algorithm)

**Axioms:** `s_real_vector_space`, `s_lp_strong_duality`
**Terminal:** `s_karmarkar_polynomial_lp` (kind: theorem)

**Steps:**
1. input: `⟨s_lp_strong_duality⟩` --[t_reduce_to_canonical_form {target: "projective-scaling form of LP on simplex with center e/n"}]--> output: `s_projective_lp_form`
2. input: `s_projective_lp_form` --[t_auxiliary_construction {target: "potential function f(x) = Σ log(c^T x / x_i) decreases by Ω(1) per scaled projection step"}]--> output: `s_karmarkar_potential_decrease`
3. input: `s_karmarkar_potential_decrease` --[t_exhaustion_squeeze {target: "O(nL) iterations reach optimum to bit precision L"}]--> output: `s_karmarkar_polynomial_lp`

**Techniques used:** t_reduce_to_canonical_form, t_auxiliary_construction, t_exhaustion_squeeze

---

## Combinatorial Optimization and Matroids

### König's theorem (bipartite max-matching = min vertex cover) (cite: https://en.wikipedia.org/wiki/K%C5%91nig%27s_theorem_(graph_theory))

**Axioms:** `s_graph_definition`
**Terminal:** `s_konig_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition⟩` --[t_axiomatize_from_instances {target: "bipartite graph G=(L⊔R, E); matching M; vertex cover C"}]--> output: `s_bipartite_matching_cover_pair`
2. input: `s_bipartite_matching_cover_pair` --[t_auxiliary_construction {target: "alternating-path Hungarian construction from maximum matching"}]--> output: `s_alternating_path_construction`
3. input: `s_alternating_path_construction` --[t_duality {target: "vertices unreachable on L plus reachable on R form min cover = |M|"}]--> output: `s_konig_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_duality

---

### Max-flow min-cut theorem (Ford–Fulkerson) (cite: https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem)

**Axioms:** `s_graph_definition`
**Terminal:** `s_max_flow_min_cut` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition⟩` --[t_axiomatize_from_instances {target: "network with source s, sink t, capacities c; flow f; s-t cut (S,T)"}]--> output: `s_network_flow_model`
2. input: `s_network_flow_model` --[t_auxiliary_construction {target: "residual graph G_f; augmenting path increases flow"}]--> output: `s_residual_graph_construction`
3. input: `s_residual_graph_construction` --[t_compactness_argument {target: "no augmenting path ⇒ S = vertices reachable from s in G_f; cut value = flow value"}]--> output: `s_no_augmenting_path_implies_min_cut`
4. input: `s_no_augmenting_path_implies_min_cut` --[t_duality {target: "max flow = min cut (LP-dual program)"}]--> output: `s_max_flow_min_cut`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_compactness_argument, t_duality

---

### Menger's theorem (cite: https://en.wikipedia.org/wiki/Menger%27s_theorem)

**Axioms:** `s_graph_definition`, `s_max_flow_min_cut`
**Terminal:** `s_menger_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition⟩` --[t_axiomatize_from_instances {target: "k internally-disjoint s–t paths vs s–t cut of size k"}]--> output: `s_disjoint_paths_vs_cut`
2. input: `s_disjoint_paths_vs_cut` --[t_reduce_to_canonical_form {target: "split each non-terminal vertex into (v_in,v_out) with unit capacity edge"}]--> output: `s_vertex_split_unit_capacity_network`
3. input: `s_vertex_split_unit_capacity_network` --[t_duality {target: "apply max-flow min-cut on unit-capacity reduction"}]--> output: `s_menger_theorem`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form, t_duality

---

### Hall's marriage theorem (cite: https://en.wikipedia.org/wiki/Hall%27s_marriage_theorem)

**Axioms:** `s_graph_definition`
**Terminal:** `s_hall_marriage_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition⟩` --[t_axiomatize_from_instances {target: "bipartite graph (X,Y,E); Hall condition |N(S)| ≥ |S| for all S ⊆ X"}]--> output: `s_hall_condition`
2. input: `s_hall_condition` --[t_auxiliary_construction {target: "induction / augmenting path: any non-saturated X-vertex extends matching"}]--> output: `s_augmenting_step_under_hall`
3. input: `s_augmenting_step_under_hall` --[t_reductio_ad_absurdum {target: "blocked augmentation gives Hall-violating set"}]--> output: `s_hall_marriage_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_reductio_ad_absurdum

---

### Edmonds' matroid intersection theorem (cite: https://en.wikipedia.org/wiki/Matroid_intersection)

**Axioms:** `s_graph_definition`
**Terminal:** `s_edmonds_matroid_intersection` (kind: theorem)

**Steps:**
1. input: `⟨s_graph_definition⟩` --[t_axiomatize_from_instances {target: "matroids M_1, M_2 on common ground set E with rank functions r_1, r_2"}]--> output: `s_two_matroids_on_e`
2. input: `s_two_matroids_on_e` --[t_auxiliary_construction {target: "exchange digraph on independent set I; augment via shortest alternating path"}]--> output: `s_exchange_digraph_construction`
3. input: `s_exchange_digraph_construction` --[t_duality {target: "max |I| = min_{A⊆E} r_1(A) + r_2(E\\A)"}]--> output: `s_edmonds_matroid_intersection`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_duality

---

## Algorithms and Algebraic Computation

### AKS primality test (deterministic polynomial-time) (cite: https://en.wikipedia.org/wiki/AKS_primality_test)

**Axioms:** `s_polynomial_ring`, `s_naturals_with_multiplication`
**Terminal:** `s_aks_primality_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_polynomial_ring, s_naturals_with_multiplication⟩` --[t_axiomatize_from_instances {target: "n prime ⇔ (X+a)^n ≡ X^n + a (mod n) in ℤ[X]"}]--> output: `s_aks_polynomial_identity`
2. input: `s_aks_polynomial_identity` --[t_reduce_to_canonical_form {target: "test identity modulo (X^r − 1) for small r with ord_r(n) > log²n"}]--> output: `s_aks_reduced_identity_modulo_x_r_minus_1`
3. input: `s_aks_reduced_identity_modulo_x_r_minus_1` --[t_polynomial_method {target: "introspective set argument: composite n forces too many polynomial relations in 𝔽_p[X]/(h(X))"}]--> output: `s_introspective_set_bound`
4. input: `s_introspective_set_bound` --[t_reductio_ad_absurdum {target: "size bound forces n to be a prime power; rule out non-prime powers by trial division"}]--> output: `s_aks_primality_theorem`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form, t_polynomial_method, t_reductio_ad_absurdum

---

### Cantor–Zassenhaus factorization (cite: https://en.wikipedia.org/wiki/Cantor%E2%80%93Zassenhaus_algorithm)

**Axioms:** `s_polynomial_ring`, `s_probability_axioms`
**Terminal:** `s_cantor_zassenhaus` (kind: theorem)

**Steps:**
1. input: `⟨s_polynomial_ring⟩` --[t_axiomatize_from_instances {target: "squarefree f(X) over 𝔽_q, factored into equal-degree d pieces"}]--> output: `s_equal_degree_factor_setting`
2. input: `s_equal_degree_factor_setting` --[t_auxiliary_construction {target: "random h(X) of deg < n; compute h(X)^{(q^d-1)/2} mod f"}]--> output: `s_random_h_power_construction`
3. input: `s_random_h_power_construction` --[t_probabilistic_existence {target: "gcd(h^{(q^d-1)/2} − 1, f) splits f nontrivially w.p. ≥ 1/2 per factor pair"}]--> output: `s_cantor_zassenhaus`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_probabilistic_existence

---

### Berlekamp factorization (cite: https://en.wikipedia.org/wiki/Berlekamp%27s_algorithm)

**Axioms:** `s_polynomial_ring`
**Terminal:** `s_berlekamp_factorization` (kind: theorem)

**Steps:**
1. input: `⟨s_polynomial_ring⟩` --[t_axiomatize_from_instances {target: "squarefree f(X) ∈ 𝔽_q[X]; quotient ring R = 𝔽_q[X]/(f)"}]--> output: `s_quotient_ring_for_f`
2. input: `s_quotient_ring_for_f` --[t_svd_and_spectral_decomposition {target: "Frobenius F: g ↦ g^q on R; Berlekamp subalgebra B = ker(F − I)"}]--> output: `s_berlekamp_subalgebra`
3. input: `s_berlekamp_subalgebra` --[t_structural_isomorphism {target: "B ≅ 𝔽_q^k for k irreducible factors (CRT)"}]--> output: `s_subalgebra_crt_decomposition`
4. input: `s_subalgebra_crt_decomposition` --[t_auxiliary_construction {target: "basis vectors of B give gcds that separate factors"}]--> output: `s_berlekamp_factorization`

**Techniques used:** t_axiomatize_from_instances, t_svd_and_spectral_decomposition, t_structural_isomorphism, t_auxiliary_construction

---

### LLL lattice basis reduction (cite: https://en.wikipedia.org/wiki/Lenstra%E2%80%93Lenstra%E2%80%93Lov%C3%A1sz_lattice_basis_reduction_algorithm)

**Axioms:** `s_real_vector_space`
**Terminal:** `s_lll_algorithm_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_real_vector_space⟩` --[t_axiomatize_from_instances {target: "lattice L ⊂ ℝ^n with basis B; Gram–Schmidt orthogonalization B*"}]--> output: `s_lattice_basis_with_gso`
2. input: `s_lattice_basis_with_gso` --[t_auxiliary_construction {target: "size-reduction + Lovász swap condition ‖b*_{i+1}‖² ≥ (3/4 − μ²)‖b*_i‖²"}]--> output: `s_lll_swap_and_reduce_step`
3. input: `s_lll_swap_and_reduce_step` --[t_exhaustion_squeeze {target: "potential Π‖b*_i‖^{2(n-i)} strictly decreases by factor < 3/4 per swap"}]--> output: `s_lll_potential_decrease`
4. input: `s_lll_potential_decrease` --[t_compose_with_identity {target: "polynomial iterations yield basis with ‖b_1‖ ≤ 2^{(n-1)/2} λ_1(L)"}]--> output: `s_lll_algorithm_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_exhaustion_squeeze, t_compose_with_identity

---

### Lovász local lemma (cite: https://en.wikipedia.org/wiki/Lov%C3%A1sz_local_lemma)

**Axioms:** `s_probability_axioms`
**Terminal:** `s_lovasz_local_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_probability_axioms⟩` --[t_axiomatize_from_instances {target: "bad events A_1,...,A_n with dependency graph of max degree d, Pr[A_i] ≤ p"}]--> output: `s_dependency_graph_setup`
2. input: `s_dependency_graph_setup` --[t_auxiliary_construction {target: "inductive bound Pr[A_i | ∩_{j∈S} A_j^c] ≤ x_i = 1/(d+1)·e if e·p·(d+1) ≤ 1"}]--> output: `s_inductive_conditional_bound`
3. input: `s_inductive_conditional_bound` --[t_probabilistic_existence {target: "Pr[∩ A_i^c] > 0 ⇒ some assignment avoids all bad events"}]--> output: `s_lovasz_local_lemma`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_probabilistic_existence

---

### Master theorem for divide-and-conquer recurrences (cite: https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))

**Axioms:** `s_real_analysis`
**Terminal:** `s_master_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_real_analysis⟩` --[t_axiomatize_from_instances {target: "recurrence T(n) = a·T(n/b) + f(n), a ≥ 1, b > 1"}]--> output: `s_divide_and_conquer_recurrence`
2. input: `s_divide_and_conquer_recurrence` --[t_reduce_to_canonical_form {target: "recursion tree: level k has a^k subproblems of size n/b^k, cost f(n/b^k)"}]--> output: `s_recursion_tree_decomposition`
3. input: `s_recursion_tree_decomposition` --[t_exhaustion_squeeze {target: "compare f(n) vs n^{log_b a}: three cases (leaves dominate / balanced / root dominates)"}]--> output: `s_master_theorem`

**Techniques used:** t_axiomatize_from_instances, t_reduce_to_canonical_form, t_exhaustion_squeeze

---

## Formal Languages and Automata (round-out)

### Pumping lemma for regular languages (cite: https://en.wikipedia.org/wiki/Pumping_lemma_for_regular_languages)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_pumping_lemma_regular` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "regular language = recognized by DFA with p states"}]--> output: `s_dfa_with_p_states`
2. input: `s_dfa_with_p_states` --[t_pigeonhole_collision {target: "any accepted string of length ≥ p revisits a state; identify pumping loop"}]--> output: `s_revisited_state_loop`
3. input: `s_revisited_state_loop` --[t_exhaustion_squeeze {target: "x y^i z ∈ L for all i ≥ 0"}]--> output: `s_pumping_lemma_regular`

**Techniques used:** t_axiomatize_from_instances, t_pigeonhole_collision, t_exhaustion_squeeze

---

### Myhill–Nerode theorem (cite: https://en.wikipedia.org/wiki/Myhill%E2%80%93Nerode_theorem)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_myhill_nerode_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "equivalence x ~_L y iff ∀z (xz ∈ L ⇔ yz ∈ L)"}]--> output: `s_nerode_equivalence_relation`
2. input: `s_nerode_equivalence_relation` --[t_structural_isomorphism {target: "minimal DFA has one state per ~_L-class"}]--> output: `s_minimal_dfa_isomorphism`
3. input: `s_nerode_equivalence_relation` --[t_compose_with_identity {target: "L regular ⇔ ~_L has finite index"}]--> output: `s_myhill_nerode_theorem`

**Techniques used:** t_axiomatize_from_instances, t_structural_isomorphism, t_compose_with_identity

---

### Kleene's theorem (regex = DFA) (cite: https://en.wikipedia.org/wiki/Kleene%27s_theorem)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_kleene_regex_dfa` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "regular expressions: ∅, ε, a, +, ·, *"}]--> output: `s_regex_syntax`
2. input: `s_regex_syntax` --[t_auxiliary_construction {target: "Thompson construction: build NFA inductively from regex"}]--> output: `s_thompson_nfa_construction`
3. input: `s_thompson_nfa_construction` --[t_structural_isomorphism {target: "subset construction NFA → DFA; state-elimination DFA → regex (converse)"}]--> output: `s_kleene_regex_dfa`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism

---

### Chomsky–Schützenberger representation theorem (cite: https://en.wikipedia.org/wiki/Chomsky%E2%80%93Sch%C3%BCtzenberger_representation_theorem)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_chomsky_schutzenberger` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "context-free language L over alphabet Σ"}]--> output: `s_cfl_definition`
2. input: `s_cfl_definition` --[t_auxiliary_construction {target: "Dyck language D_k on k pairs of brackets — universal CF object"}]--> output: `s_dyck_language_universal`
3. input: `s_dyck_language_universal` --[t_structural_isomorphism {target: "L = h(D_k ∩ R) for some regular R and homomorphism h"}]--> output: `s_chomsky_schutzenberger`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism

---

### Parikh's theorem (cite: https://en.wikipedia.org/wiki/Parikh%27s_theorem)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_parikh_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "Parikh image of L ⊆ Σ* in ℕ^|Σ| via letter counts"}]--> output: `s_parikh_map`
2. input: `s_parikh_map` --[t_auxiliary_construction {target: "parse tree pumping: any sufficiently long CF derivation has repeated nonterminals → linear contribution"}]--> output: `s_cf_parse_tree_pumping_step`
3. input: `s_cf_parse_tree_pumping_step` --[t_compose_with_identity {target: "Parikh image of CFL = semilinear set in ℕ^k = Parikh image of some regular language"}]--> output: `s_parikh_theorem`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_compose_with_identity

---

### Ogden's lemma (cite: https://en.wikipedia.org/wiki/Ogden%27s_lemma)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_ogden_lemma` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "context-free L, mark k positions in long string w ∈ L"}]--> output: `s_marked_string_in_cfl`
2. input: `s_marked_string_in_cfl` --[t_pigeonhole_collision {target: "parse tree of w has a path with ≥ log k marked positions and repeated nonterminal"}]--> output: `s_marked_parse_path_pumping`
3. input: `s_marked_parse_path_pumping` --[t_exhaustion_squeeze {target: "decomposition uvxyz with marked vy nonempty and pumpable"}]--> output: `s_ogden_lemma`

**Techniques used:** t_axiomatize_from_instances, t_pigeonhole_collision, t_exhaustion_squeeze

---

### Rabin–Scott subset construction (NFA = DFA) (cite: https://en.wikipedia.org/wiki/Powerset_construction)

**Axioms:** `s_turing_machine_model`
**Terminal:** `s_rabin_scott_subset_construction` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model⟩` --[t_axiomatize_from_instances {target: "NFA N with state set Q, nondeterministic transitions"}]--> output: `s_nfa_model`
2. input: `s_nfa_model` --[t_auxiliary_construction {target: "DFA D with state set 2^Q tracking reachable subsets"}]--> output: `s_subset_dfa_construction`
3. input: `s_subset_dfa_construction` --[t_structural_isomorphism {target: "L(D) = L(N); equivalence of regular language classes"}]--> output: `s_rabin_scott_subset_construction`

**Techniques used:** t_axiomatize_from_instances, t_auxiliary_construction, t_structural_isomorphism

---

### Trakhtenbrot's theorem (finite-model satisfiability undecidable) (cite: https://en.wikipedia.org/wiki/Trakhtenbrot%27s_theorem)

**Axioms:** `s_turing_machine_model`, `s_undecidability_of_halting`, `s_first_order_peano_arithmetic`
**Terminal:** `s_trakhtenbrot_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_turing_machine_model, s_first_order_peano_arithmetic⟩` --[t_arithmetize_syntax {target: "encode TM computation as first-order sentence φ_M about finite structure"}]--> output: `s_fo_encoding_of_tm_computation`
2. input: `s_fo_encoding_of_tm_computation` --[t_auxiliary_construction {target: "φ_M has finite model ⇔ M halts on empty input"}]--> output: `s_finite_model_iff_halting`
3. input: `⟨s_finite_model_iff_halting, s_undecidability_of_halting⟩` --[t_reductio_ad_absurdum {target: "decidable finite-sat would decide halting"}]--> output: `s_trakhtenbrot_theorem`

**Techniques used:** t_arithmetize_syntax, t_auxiliary_construction, t_reductio_ad_absurdum

---
