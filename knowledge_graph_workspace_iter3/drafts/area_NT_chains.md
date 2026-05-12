# Area NT Derivation Chains (iter-3) — Number Theory

**Source pages:**
- https://en.wikipedia.org/wiki/Category:Theorems_in_number_theory
- https://en.wikipedia.org/wiki/List_of_number_theory_topics
- https://mathworld.wolfram.com/topics/NumberTheory.html
- https://en.wikipedia.org/wiki/Analytic_number_theory
- https://en.wikipedia.org/wiki/Algebraic_number_theory

**Target:** 85 chains. **Drafted:** 86. **Skipped (already in graph):** Chinese remainder theorem (`s_chinese_remainder_theorem`), Fermat's little theorem (`s_fermat_little_theorem`), Fermat's Last Theorem (`s_flt`), Lagrange four-square (`s_lagrange_four_squares`), Mordell–Faltings (`s_mordell_faltings`), prime number theorem (`s_prime_number_theorem`), Green–Tao (`s_green_tao`), Szemerédi (`s_szemeredi_theorem`), Euler four-square identity (`s_euler_four_square_identity`), Fermat two-squares (`s_fermat_two_squares`), Pell-solvability (`s_solvability_of_pell_equation`), semistable modularity (`s_semistable_modularity_theorem`), reciprocity conjecture node (`s_reciprocity_conjecture`).

**Flagged `⚠ needs new technique`:** 0.

---

## Elementary number theory

### Wilson's theorem (cite: https://en.wikipedia.org/wiki/Wilson%27s_theorem)
**Axioms:** `s_naturals_with_multiplication`, `s_fermat_little_theorem`
**Terminal:** `s_wilson_theorem` (kind: theorem)
**Steps:**
1. input: `s_naturals_with_multiplication` --[t_axiomatize_from_instances {abstracted_to: "p prime ⇒ (ℤ/p)* is a group"}]--> output: `s_multiplicative_group_mod_prime`
2. input: `s_multiplicative_group_mod_prime` --[t_symmetry_reduction {group: "pairing a ↔ a^{-1}, fixed points only ±1"}]--> output: `s_pairing_off_inverses_mod_p`
3. input: `s_pairing_off_inverses_mod_p` --[t_compose_with_identity {identity: "(p-1)! ≡ (-1) · ∏ pairs ≡ -1"}]--> output: `s_wilson_theorem`
**Techniques used:** t_axiomatize_from_instances, t_symmetry_reduction, t_compose_with_identity

### Euler's totient theorem (cite: https://en.wikipedia.org/wiki/Euler%27s_theorem)
**Axioms:** `s_naturals_with_multiplication`, `s_coprime_pair`
**Terminal:** `s_euler_totient_theorem` (kind: theorem)
**Steps:**
1. input: `⟨s_naturals_with_multiplication, s_coprime_pair⟩` --[t_axiomatize_from_instances {abstracted_to: "(ℤ/n)* is a finite abelian group of order φ(n)"}]--> output: `s_unit_group_mod_n`
2. input: `s_unit_group_mod_n` --[t_structural_isomorphism {invariant: "order of element divides group order (Lagrange)"}]--> output: `s_euler_totient_theorem`
**Techniques used:** t_axiomatize_from_instances, t_structural_isomorphism

### Wolstenholme's theorem (cite: https://en.wikipedia.org/wiki/Wolstenholme%27s_theorem)
**Axioms:** `s_naturals_with_multiplication`, `s_fermat_little_theorem`
**Terminal:** `s_wolstenholme_theorem` (kind: theorem)
**Steps:**
1. input: `s_naturals_with_multiplication` --[t_reduce_to_canonical_form {form: "binomial C(2p,p) − 2 modulo p^4"}]--> output: `s_normalized_central_binomial_mod_p4`
2. input: `s_normalized_central_binomial_mod_p4` --[t_compose_with_identity {identity: "harmonic sum H_{p-1} ≡ 0 mod p^3 for p≥5"}]--> output: `s_harmonic_congruence_mod_p3`
3. input: `s_harmonic_congruence_mod_p3` --[t_pigeonhole_collision {bin: "residues mod p^3 of partial sums pair up"}]--> output: `s_wolstenholme_theorem`
**Techniques used:** t_reduce_to_canonical_form, t_compose_with_identity, t_pigeonhole_collision

### Euclid–Euler theorem (even perfect numbers) (cite: https://en.wikipedia.org/wiki/Euclid%E2%80%93Euler_theorem)
**Axioms:** `s_naturals_with_multiplication`, `s_mersenne_prime_2p_minus_1`
**Terminal:** `s_euclid_euler_perfect_numbers` (kind: theorem)
**Steps:**
1. input: `s_naturals_with_multiplication` --[t_axiomatize_from_instances {abstracted_to: "multiplicativity of σ"}]--> output: `s_sigma_multiplicative`
2. input: `⟨s_sigma_multiplicative, s_mersenne_prime_2p_minus_1⟩` --[t_compose_with_identity {identity: "σ(2^{p-1}(2^p-1)) = 2 · 2^{p-1}(2^p-1)"}]--> output: `s_euclid_perfect_sufficient`
3. input: `s_euclid_perfect_sufficient` --[t_infinite_descent {measure: "odd part of an even perfect number"}]--> output: `s_euclid_euler_perfect_numbers`
**Techniques used:** t_axiomatize_from_instances, t_compose_with_identity, t_infinite_descent

### Pentagonal number theorem (Euler) (cite: https://en.wikipedia.org/wiki/Pentagonal_number_theorem)
**Axioms:** `s_formal_power_series_over_z`, `s_partition_generating_function_q_pochhammer`
**Terminal:** `s_pentagonal_number_theorem` (kind: theorem)
**Steps:**
1. input: `s_partition_generating_function_q_pochhammer` --[t_spot_pattern_in_table {observation: "expansion of (q;q)_∞ has very sparse coefficients ±1 at pentagonal exponents"}]--> output: `s_sparse_pentagonal_signature`
2. input: `s_sparse_pentagonal_signature` --[t_symmetry_reduction {group: "Franklin involution on partitions with distinct parts"}]--> output: `s_franklin_involution_cancellation`
3. input: `s_franklin_involution_cancellation` --[t_compose_with_identity {identity: "∏(1-q^n) = Σ (-1)^k q^{k(3k-1)/2}"}]--> output: `s_pentagonal_number_theorem`
**Techniques used:** t_spot_pattern_in_table, t_symmetry_reduction, t_compose_with_identity

### Zeckendorf's theorem (cite: https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem)
**Axioms:** `s_naturals_with_multiplication`, `s_fibonacci_numbers`
**Terminal:** `s_zeckendorf_theorem` (kind: theorem)
**Steps:**
1. input: `⟨s_naturals_with_multiplication, s_fibonacci_numbers⟩` --[t_exhaustion_squeeze {lower: "greedy pick F_k ≤ n", upper: "F_{k+1} > n"}]--> output: `s_greedy_fibonacci_decomposition`
2. input: `s_greedy_fibonacci_decomposition` --[t_infinite_descent {measure: "remainder n - F_k < F_{k-1}"}]--> output: `s_zeckendorf_theorem`
**Techniques used:** t_exhaustion_squeeze, t_infinite_descent

### Fermat's right-triangle theorem (cite: https://en.wikipedia.org/wiki/Fermat%27s_right_triangle_theorem)
**Axioms:** `s_integers`, `s_pythagorean_triple_primitive_parametrization`
**Terminal:** `s_fermat_right_triangle_no_rational_square_area` (kind: theorem)
**Steps:**
1. input: `s_pythagorean_triple_primitive_parametrization` --[t_reduce_to_canonical_form {form: "smallest primitive triple with square area"}]--> output: `s_smallest_squared_area_triple`
2. input: `s_smallest_squared_area_triple` --[t_compose_with_identity {identity: "construct strictly smaller triple from given one"}]--> output: `s_descended_smaller_triple`
3. input: `s_descended_smaller_triple` --[t_infinite_descent {measure: "minimal hypotenuse"}]--> output: `s_fermat_right_triangle_no_rational_square_area`
**Techniques used:** t_reduce_to_canonical_form, t_compose_with_identity, t_infinite_descent

### Sophie Germain's theorem (cite: https://en.wikipedia.org/wiki/Sophie_Germain%27s_theorem)
**Axioms:** `s_integers`, `s_flt_exponent_p_first_case`
**Terminal:** `s_sophie_germain_theorem` (kind: theorem)
**Steps:**
1. input: `s_flt_exponent_p_first_case` --[t_auxiliary_construction {object: "auxiliary prime q = 2p+1 (Sophie Germain prime)"}]--> output: `s_aux_sophie_germain_prime_q`
2. input: `s_aux_sophie_germain_prime_q` --[t_reduce_to_canonical_form {form: "x^p + y^p + z^p ≡ 0 mod q"}]--> output: `s_flt_residue_obstruction_mod_q`
3. input: `s_flt_residue_obstruction_mod_q` --[t_reductio_ad_absurdum {assume: "p doesn't divide xyz"}]--> output: `s_sophie_germain_theorem`
**Techniques used:** t_auxiliary_construction, t_reduce_to_canonical_form, t_reductio_ad_absurdum

### Fermat polygonal number theorem (cite: https://en.wikipedia.org/wiki/Fermat_polygonal_number_theorem)
**Axioms:** `s_naturals_with_multiplication`, `s_lagrange_four_squares`
**Terminal:** `s_fermat_polygonal_number_theorem` (kind: theorem)
**Steps:**
1. input: `s_lagrange_four_squares` --[t_reduce_to_canonical_form {form: "3-square ⇒ representation by triangular numbers (Gauss eureka)"}]--> output: `s_gauss_triangular_eureka`
2. input: `s_gauss_triangular_eureka` --[t_axiomatize_from_instances {abstracted_to: "for each k≥3, every n is sum of k k-gonal numbers"}]--> output: `s_fermat_polygonal_number_theorem`
**Techniques used:** t_reduce_to_canonical_form, t_axiomatize_from_instances

### Jacobi's four-square theorem (cite: https://en.wikipedia.org/wiki/Jacobi%27s_four-square_theorem)
**Axioms:** `s_integers`, `s_theta_function_jacobi_θ3`
**Terminal:** `s_jacobi_four_square_formula` (kind: theorem)
**Steps:**
1. input: `s_theta_function_jacobi_θ3` --[t_compose_with_identity {identity: "θ_3(q)^4 = 1 + 8Σ_{4∤n} σ(n) q^n"}]--> output: `s_θ3_pow4_lambert_series`
2. input: `s_θ3_pow4_lambert_series` --[t_spot_pattern_in_table {observation: "coefficient = 8(σ(n) - 4σ(n/4))"}]--> output: `s_r4_formula_8_times_sigma`
3. input: `s_r4_formula_8_times_sigma` --[t_complex_analysis_to_integers {object: "modular form weight 2 level 4"}]--> output: `s_jacobi_four_square_formula`
**Techniques used:** t_compose_with_identity, t_spot_pattern_in_table, t_complex_analysis_to_integers

### Legendre's three-square theorem (cite: https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem)
**Axioms:** `s_integers`, `s_quadratic_form_x2_y2_z2`
**Terminal:** `s_legendre_three_square_theorem` (kind: theorem)
**Steps:**
1. input: `s_quadratic_form_x2_y2_z2` --[t_reduce_to_canonical_form {form: "obstruction n = 4^a(8b+7)"}]--> output: `s_three_square_obstruction_modulo_8`
2. input: `s_three_square_obstruction_modulo_8` --[t_compactness_argument {target: "Minkowski lattice point in indefinite form"}]--> output: `s_lattice_point_in_genus`
3. input: `s_lattice_point_in_genus` --[t_axiomatize_from_instances {abstracted_to: "Hasse local-global for indefinite ternary forms"}]--> output: `s_legendre_three_square_theorem`
**Techniques used:** t_reduce_to_canonical_form, t_compactness_argument, t_axiomatize_from_instances

### Three-gap theorem (Steinhaus) (cite: https://en.wikipedia.org/wiki/Three-gap_theorem)
**Axioms:** `s_reals_with_topology`, `s_circle_t_1`
**Terminal:** `s_three_gap_theorem` (kind: theorem)
**Steps:**
1. input: `s_circle_t_1` --[t_symmetry_reduction {group: "ℤ-action by rotation α on 𝕋¹"}]--> output: `s_orbit_of_n_alpha_mod_1`
2. input: `s_orbit_of_n_alpha_mod_1` --[t_pigeonhole_collision {bin: "consecutive arc lengths in partitioned circle"}]--> output: `s_at_most_three_gap_lengths`
3. input: `s_at_most_three_gap_lengths` --[t_compose_with_identity {identity: "longest = sum of two shorter; continued-fraction convergents control gaps"}]--> output: `s_three_gap_theorem`
**Techniques used:** t_symmetry_reduction, t_pigeonhole_collision, t_compose_with_identity

### Hurwitz's theorem on Diophantine approximation (cite: https://en.wikipedia.org/wiki/Hurwitz%27s_theorem_(number_theory))
**Axioms:** `s_reals_with_topology`, `s_continued_fraction_expansion`
**Terminal:** `s_hurwitz_diophantine_approximation` (kind: theorem)
**Steps:**
1. input: `s_continued_fraction_expansion` --[t_reduce_to_canonical_form {form: "convergents p_n/q_n minimize |α - p/q|·q^2"}]--> output: `s_convergent_best_approximation`
2. input: `s_convergent_best_approximation` --[t_exhaustion_squeeze {lower: "infinitely many with q^2|α-p/q| < 1/√5", upper: "Markov spectrum"}]--> output: `s_markov_spectrum_minimal_gap_sqrt5`
3. input: `s_markov_spectrum_minimal_gap_sqrt5` --[t_compose_with_identity {identity: "constant √5 attained on golden ratio"}]--> output: `s_hurwitz_diophantine_approximation`
**Techniques used:** t_reduce_to_canonical_form, t_exhaustion_squeeze, t_compose_with_identity

### Dirichlet's approximation theorem (cite: https://en.wikipedia.org/wiki/Dirichlet%27s_approximation_theorem)
**Axioms:** `s_reals_with_topology`, `s_unit_interval`
**Terminal:** `s_dirichlet_approximation` (kind: theorem)
**Steps:**
1. input: `s_unit_interval` --[t_pigeonhole_collision {bin: "subdivide [0,1) into N equal cells, place {kα} for k=0,…,N"}]--> output: `s_two_close_kalpha_points`
2. input: `s_two_close_kalpha_points` --[t_compose_with_identity {identity: "|qα - p| < 1/N implies |α - p/q| < 1/(qN)"}]--> output: `s_dirichlet_approximation`
**Techniques used:** t_pigeonhole_collision, t_compose_with_identity

### Mihăilescu's theorem (Catalan) (cite: https://en.wikipedia.org/wiki/Catalan%27s_conjecture)
**Axioms:** `s_integers`, `s_cyclotomic_field_q_zeta_p`
**Terminal:** `s_mihailescu_catalan_theorem` (kind: theorem)
**Steps:**
1. input: `s_integers` --[t_reduce_to_canonical_form {form: "x^p - y^q = 1 with p,q odd primes"}]--> output: `s_catalan_equation_canonical`
2. input: `⟨s_catalan_equation_canonical, s_cyclotomic_field_q_zeta_p⟩` --[t_heights_and_galois_rep_bridge {bridge: "factorization in ℤ[ζ_p] forces class-group divisibility"}]--> output: `s_class_group_divisibility_obstruction`
3. input: `s_class_group_divisibility_obstruction` --[t_reductio_ad_absurdum {assume: "nontrivial solution exists"}]--> output: `s_mihailescu_catalan_theorem`
**Techniques used:** t_reduce_to_canonical_form, t_heights_and_galois_rep_bridge, t_reductio_ad_absurdum

---

## Multiplicative & algebraic number theory

### Quadratic reciprocity (cite: https://en.wikipedia.org/wiki/Quadratic_reciprocity)
**Axioms:** `s_integers`, `s_legendre_symbol_definition`
**Terminal:** `s_quadratic_reciprocity` (kind: theorem)
**Steps:**
1. input: `s_legendre_symbol_definition` --[t_auxiliary_construction {object: "Gauss sum g_p = Σ (n/p) ζ_p^n"}]--> output: `s_gauss_sum_g_p`
2. input: `s_gauss_sum_g_p` --[t_compose_with_identity {identity: "g_p^2 = (-1)^{(p-1)/2} p"}]--> output: `s_gauss_sum_squared`
3. input: `s_gauss_sum_squared` --[t_galois_correspondence {field_tower: "Q(ζ_p)/Q, Frobenius at q"}]--> output: `s_quadratic_reciprocity`
**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_galois_correspondence

### Cubic reciprocity (Eisenstein) (cite: https://en.wikipedia.org/wiki/Cubic_reciprocity)
**Axioms:** `s_eisenstein_integers_z_omega`, `s_integers`
**Terminal:** `s_cubic_reciprocity` (kind: theorem)
**Steps:**
1. input: `s_eisenstein_integers_z_omega` --[t_axiomatize_from_instances {abstracted_to: "primary primes π ≡ 2 mod 3 in ℤ[ω]"}]--> output: `s_primary_eisenstein_primes`
2. input: `s_primary_eisenstein_primes` --[t_galois_correspondence {field_tower: "Q(ω, π^{1/3})/Q(ω)"}]--> output: `s_cubic_residue_symbol_reciprocal_law`
3. input: `s_cubic_residue_symbol_reciprocal_law` --[t_compose_with_identity {identity: "(α/π)_3 (π/α)_3 = 1 for primary coprime α,π"}]--> output: `s_cubic_reciprocity`
**Techniques used:** t_axiomatize_from_instances, t_galois_correspondence, t_compose_with_identity

### Quartic / biquadratic reciprocity (cite: https://en.wikipedia.org/wiki/Quartic_reciprocity)
**Axioms:** `s_gaussian_integers_z_i`, `s_integers`
**Terminal:** `s_quartic_reciprocity` (kind: theorem)
**Steps:**
1. input: `s_gaussian_integers_z_i` --[t_axiomatize_from_instances {abstracted_to: "primary primes π ≡ 1 mod (1+i)^3 in ℤ[i]"}]--> output: `s_primary_gaussian_primes`
2. input: `s_primary_gaussian_primes` --[t_galois_correspondence {field_tower: "Q(i, π^{1/4})/Q(i)"}]--> output: `s_quartic_residue_symbol`
3. input: `s_quartic_residue_symbol` --[t_compose_with_identity {identity: "Eisenstein quartic reciprocity formula"}]--> output: `s_quartic_reciprocity`
**Techniques used:** t_axiomatize_from_instances, t_galois_correspondence, t_compose_with_identity

### Jacobi triple product (cite: https://en.wikipedia.org/wiki/Jacobi_triple_product)
**Axioms:** `s_formal_power_series_over_z`, `s_q_pochhammer_symbol`
**Terminal:** `s_jacobi_triple_product` (kind: theorem)
**Steps:**
1. input: `s_q_pochhammer_symbol` --[t_symmetry_reduction {group: "shift z ↦ qz functional equation"}]--> output: `s_quasiperiodic_shift_z_qz`
2. input: `s_quasiperiodic_shift_z_qz` --[t_compose_with_identity {identity: "Σ z^n q^{n(n-1)/2} = ∏(1-q^n)(1+zq^{n-1})(1+z^{-1}q^n)"}]--> output: `s_jacobi_triple_product`
**Techniques used:** t_symmetry_reduction, t_compose_with_identity

### Hasse–Minkowski theorem (cite: https://en.wikipedia.org/wiki/Hasse%E2%80%93Minkowski_theorem)
**Axioms:** `s_rationals_q`, `s_p_adic_completions_q_p`, `s_quadratic_form_over_q`
**Terminal:** `s_hasse_minkowski` (kind: theorem)
**Steps:**
1. input: `s_quadratic_form_over_q` --[t_reduce_to_canonical_form {form: "diagonalize quadratic form over ℚ"}]--> output: `s_diagonal_quadratic_form`
2. input: `⟨s_diagonal_quadratic_form, s_p_adic_completions_q_p⟩` --[t_transference_bridge {bridge: "Hilbert symbol product formula"}]--> output: `s_hilbert_symbol_product_formula`
3. input: `s_hilbert_symbol_product_formula` --[t_axiomatize_from_instances {abstracted_to: "local solubility at all places ⇒ global"}]--> output: `s_hasse_minkowski`
**Techniques used:** t_reduce_to_canonical_form, t_transference_bridge, t_axiomatize_from_instances

### Meyer's theorem (indefinite quadratic in ≥5 variables) (cite: https://en.wikipedia.org/wiki/Meyer%27s_theorem)
**Axioms:** `s_quadratic_form_over_q`, `s_hasse_minkowski`
**Terminal:** `s_meyer_theorem_indefinite` (kind: theorem)
**Steps:**
1. input: `s_quadratic_form_over_q` --[t_reduce_to_canonical_form {form: "rank ≥ 5 indefinite"}]--> output: `s_indefinite_form_rank_ge_5`
2. input: `⟨s_indefinite_form_rank_ge_5, s_hasse_minkowski⟩` --[t_compose_with_identity {identity: "rank ≥ 5 always solvable over every ℚ_p"}]--> output: `s_meyer_theorem_indefinite`
**Techniques used:** t_reduce_to_canonical_form, t_compose_with_identity

### Brauer's theorem on forms (cite: https://en.wikipedia.org/wiki/Brauer%27s_theorem_on_forms)
**Axioms:** `s_finite_field_f_q`, `s_homogeneous_form_degree_d`
**Terminal:** `s_brauer_forms_theorem` (kind: theorem)
**Steps:**
1. input: `s_homogeneous_form_degree_d` --[t_axiomatize_from_instances {abstracted_to: "Chevalley–Warning forces ≥ 2 zeros if n > d"}]--> output: `s_chevalley_warning_zero_count`
2. input: `s_chevalley_warning_zero_count` --[t_compose_with_identity {identity: "iterated to common zero in many variables"}]--> output: `s_brauer_forms_theorem`
**Techniques used:** t_axiomatize_from_instances, t_compose_with_identity

### Bhargava–Hanke 15 and 290 theorems (cite: https://en.wikipedia.org/wiki/15_and_290_theorems)
**Axioms:** `s_positive_definite_integral_quadratic_form`, `s_naturals_with_multiplication`
**Terminal:** `s_bhargava_290_theorem` (kind: theorem)
**Steps:**
1. input: `s_positive_definite_integral_quadratic_form` --[t_finite_case_check {bound: "test universality on integers 1..290"}]--> output: `s_universality_witness_set_290`
2. input: `s_universality_witness_set_290` --[t_axiomatize_from_instances {abstracted_to: "form represents 1..290 ⇒ form represents all positive integers"}]--> output: `s_bhargava_290_theorem`
**Techniques used:** t_finite_case_check, t_axiomatize_from_instances

### Eisenstein's irreducibility criterion (cite: https://en.wikipedia.org/wiki/Eisenstein%27s_criterion)
**Axioms:** `s_polynomial_ring_z_x`, `s_prime_p`
**Terminal:** `s_eisenstein_criterion` (kind: theorem)
**Steps:**
1. input: `⟨s_polynomial_ring_z_x, s_prime_p⟩` --[t_reduce_to_canonical_form {form: "coefficient divisibilities a_0, …, a_{n-1} divisible by p, a_0 not by p²"}]--> output: `s_eisenstein_coefficient_profile`
2. input: `s_eisenstein_coefficient_profile` --[t_reductio_ad_absurdum {assume: "f = gh nontrivial factorization mod p forces both factors with a_0 share factor p"}]--> output: `s_eisenstein_criterion`
**Techniques used:** t_reduce_to_canonical_form, t_reductio_ad_absurdum

### Hilbert's irreducibility theorem (cite: https://en.wikipedia.org/wiki/Hilbert%27s_irreducibility_theorem)
**Axioms:** `s_polynomial_ring_in_two_vars_q_t_x`, `s_thin_set_in_an`
**Terminal:** `s_hilbert_irreducibility` (kind: theorem)
**Steps:**
1. input: `s_polynomial_ring_in_two_vars_q_t_x` --[t_axiomatize_from_instances {abstracted_to: "irreducibility is generic in t"}]--> output: `s_generic_specialization_remains_irreducible`
2. input: `s_generic_specialization_remains_irreducible` --[t_sieve_by_optimized_quadratic {sieve: "count exceptional t via thin-set density"}]--> output: `s_thin_exceptional_set`
3. input: `s_thin_exceptional_set` --[t_compose_with_identity {identity: "complement of thin set is Zariski-dense"}]--> output: `s_hilbert_irreducibility`
**Techniques used:** t_axiomatize_from_instances, t_sieve_by_optimized_quadratic, t_compose_with_identity

### Dedekind discriminant theorem (cite: https://en.wikipedia.org/wiki/Dedekind%27s_discriminant_theorem)
**Axioms:** `s_number_field_k`, `s_ring_of_integers_o_k`
**Terminal:** `s_dedekind_discriminant_theorem` (kind: theorem)
**Steps:**
1. input: `s_ring_of_integers_o_k` --[t_axiomatize_from_instances {abstracted_to: "different ideal D_{K/Q}, N(D)=|disc|"}]--> output: `s_different_ideal_definition`
2. input: `s_different_ideal_definition` --[t_compose_with_identity {identity: "p ramifies iff p | disc(K/Q)"}]--> output: `s_dedekind_discriminant_theorem`
**Techniques used:** t_axiomatize_from_instances, t_compose_with_identity

### Dedekind–Kummer theorem (cite: https://en.wikipedia.org/wiki/Dedekind%E2%80%93Kummer_theorem)
**Axioms:** `s_ring_of_integers_o_k`, `s_minimal_polynomial_theta`
**Terminal:** `s_dedekind_kummer_theorem` (kind: theorem)
**Steps:**
1. input: `⟨s_ring_of_integers_o_k, s_minimal_polynomial_theta⟩` --[t_reduce_to_canonical_form {form: "factor minimal polynomial mod p"}]--> output: `s_minimal_poly_factorization_mod_p`
2. input: `s_minimal_poly_factorization_mod_p` --[t_structural_isomorphism {invariant: "factorization of pO_K mirrors factorization mod p when p ∤ [O_K:ℤ[θ]]"}]--> output: `s_dedekind_kummer_theorem`
**Techniques used:** t_reduce_to_canonical_form, t_structural_isomorphism

### Kummer's theorem on cyclotomic ideal factorization (cite: https://en.wikipedia.org/wiki/Kummer%27s_theorem)
**Axioms:** `s_cyclotomic_field_q_zeta_p`, `s_prime_p`
**Terminal:** `s_kummer_cyclotomic_factorization` (kind: theorem)
**Steps:**
1. input: `s_cyclotomic_field_q_zeta_p` --[t_galois_correspondence {field_tower: "Q(ζ_n)/Q with Gal = (ℤ/n)*"}]--> output: `s_cyclotomic_galois_structure`
2. input: `s_cyclotomic_galois_structure` --[t_reduce_to_canonical_form {form: "order of p mod n controls residue degree"}]--> output: `s_kummer_cyclotomic_factorization`
**Techniques used:** t_galois_correspondence, t_reduce_to_canonical_form

### Kummer's congruence (Bernoulli) (cite: https://en.wikipedia.org/wiki/Kummer%27s_congruence)
**Axioms:** `s_bernoulli_numbers_b_n`, `s_p_adic_completions_q_p`
**Terminal:** `s_kummer_congruence` (kind: theorem)
**Steps:**
1. input: `s_bernoulli_numbers_b_n` --[t_complex_analysis_to_integers {object: "p-adic L-function L_p(s,χ)"}]--> output: `s_p_adic_l_function`
2. input: `s_p_adic_l_function` --[t_compose_with_identity {identity: "B_m/m ≡ B_n/n mod p^a when m ≡ n mod (p-1)p^{a-1}, p-1 ∤ m,n"}]--> output: `s_kummer_congruence`
**Techniques used:** t_complex_analysis_to_integers, t_compose_with_identity

### Von Staudt–Clausen theorem (cite: https://en.wikipedia.org/wiki/Von_Staudt%E2%80%93Clausen_theorem)
**Axioms:** `s_bernoulli_numbers_b_n`, `s_rationals_q`
**Terminal:** `s_von_staudt_clausen_theorem` (kind: theorem)
**Steps:**
1. input: `s_bernoulli_numbers_b_n` --[t_reduce_to_canonical_form {form: "B_{2n} + Σ_{(p-1)|2n} 1/p ∈ ℤ"}]--> output: `s_bernoulli_integer_part_formula`
2. input: `s_bernoulli_integer_part_formula` --[t_axiomatize_from_instances {abstracted_to: "denominator of B_{2n} = ∏_{(p-1)|2n} p"}]--> output: `s_von_staudt_clausen_theorem`
**Techniques used:** t_reduce_to_canonical_form, t_axiomatize_from_instances

### Apéry's theorem (ζ(3) irrational) (cite: https://en.wikipedia.org/wiki/Ap%C3%A9ry%27s_theorem)
**Axioms:** `s_rationals_q`, `s_riemann_zeta_function`
**Terminal:** `s_apery_zeta3_irrational` (kind: theorem)
**Steps:**
1. input: `s_riemann_zeta_function` --[t_auxiliary_construction {object: "Apéry recurrence: a_n, b_n satisfying n³ u_n = (34n³ − 51n² + 27n − 5) u_{n-1} − (n-1)³ u_{n-2}"}]--> output: `s_apery_recurrence_sequences`
2. input: `s_apery_recurrence_sequences` --[t_exhaustion_squeeze {lower: "0 < b_n ζ(3) − a_n", upper: "decays faster than any 1/q_n^c with c>1"}]--> output: `s_super_dirichlet_approximation_of_zeta3`
3. input: `s_super_dirichlet_approximation_of_zeta3` --[t_reductio_ad_absurdum {assume: "ζ(3) ∈ ℚ"}]--> output: `s_apery_zeta3_irrational`
**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_reductio_ad_absurdum

### Chebotarev density theorem (cite: https://en.wikipedia.org/wiki/Chebotarev%27s_density_theorem)
**Axioms:** `s_number_field_k`, `s_galois_extension_l_over_k`
**Terminal:** `s_chebotarev_density` (kind: theorem)
**Steps:**
1. input: `s_galois_extension_l_over_k` --[t_axiomatize_from_instances {abstracted_to: "Frobenius conjugacy class Frob_p for unramified p"}]--> output: `s_frobenius_conjugacy_class_distribution`
2. input: `s_frobenius_conjugacy_class_distribution` --[t_character_decomposition_count {basis: "irreducible characters of Gal(L/K)"}]--> output: `s_density_via_character_sums`
3. input: `s_density_via_character_sums` --[t_complex_analysis_to_integers {object: "Artin L-functions, non-vanishing at s=1"}]--> output: `s_chebotarev_density`
**Techniques used:** t_axiomatize_from_instances, t_character_decomposition_count, t_complex_analysis_to_integers

### Dirichlet's theorem on primes in arithmetic progressions (cite: https://en.wikipedia.org/wiki/Dirichlet%27s_theorem_on_arithmetic_progressions)
**Axioms:** `s_naturals_with_multiplication`, `s_dirichlet_character_mod_q`
**Terminal:** `s_dirichlet_primes_in_ap` (kind: theorem)
**Steps:**
1. input: `s_dirichlet_character_mod_q` --[t_character_decomposition_count {basis: "characters mod q project to single residue class"}]--> output: `s_indicator_via_character_sum`
2. input: `s_indicator_via_character_sum` --[t_complex_analysis_to_integers {object: "Dirichlet L-function L(s,χ)"}]--> output: `s_dirichlet_l_function_log_derivative`
3. input: `s_dirichlet_l_function_log_derivative` --[t_compose_with_identity {identity: "L(1,χ) ≠ 0 for nontrivial χ ⇒ divergence of Σ 1/p over class"}]--> output: `s_dirichlet_primes_in_ap`
**Techniques used:** t_character_decomposition_count, t_complex_analysis_to_integers, t_compose_with_identity

### Bertrand's postulate / Chebyshev (cite: https://en.wikipedia.org/wiki/Bertrand%27s_postulate)
**Axioms:** `s_naturals_with_multiplication`, `s_binomial_coefficient_2n_choose_n`
**Terminal:** `s_bertrand_postulate` (kind: theorem)
**Steps:**
1. input: `s_binomial_coefficient_2n_choose_n` --[t_exhaustion_squeeze {lower: "4^n/(2n+1)", upper: "(2n)^{π(2n)} × something"}]--> output: `s_binomial_size_bounds`
2. input: `s_binomial_size_bounds` --[t_reductio_ad_absurdum {assume: "no prime in (n,2n]"}]--> output: `s_bertrand_postulate`
**Techniques used:** t_exhaustion_squeeze, t_reductio_ad_absurdum

### Chebyshev's bounds on π(x) (cite: https://en.wikipedia.org/wiki/Chebyshev_function)
**Axioms:** `s_naturals_with_multiplication`, `s_chebyshev_function_theta_psi`
**Terminal:** `s_chebyshev_pi_bounds` (kind: theorem)
**Steps:**
1. input: `s_chebyshev_function_theta_psi` --[t_reduce_to_canonical_form {form: "ψ(x) − ψ(x/2) ≤ log binomial(2n,n) ≤ ψ(x)"}]--> output: `s_psi_squeeze_via_central_binomial`
2. input: `s_psi_squeeze_via_central_binomial` --[t_exhaustion_squeeze {lower: "log 2", upper: "log 4"}]--> output: `s_chebyshev_pi_bounds`
**Techniques used:** t_reduce_to_canonical_form, t_exhaustion_squeeze

### Mertens' theorems (cite: https://en.wikipedia.org/wiki/Mertens%27_theorems)
**Axioms:** `s_naturals_with_multiplication`, `s_chebyshev_function_theta_psi`
**Terminal:** `s_mertens_theorems` (kind: theorem)
**Steps:**
1. input: `s_chebyshev_function_theta_psi` --[t_compose_with_identity {identity: "Abel summation transfers θ-asymptotic to Σ log p/p"}]--> output: `s_log_p_over_p_partial_sums`
2. input: `s_log_p_over_p_partial_sums` --[t_interpolate_and_continue {target: "Σ 1/p = log log x + M + o(1)"}]--> output: `s_mertens_constant_M`
3. input: `s_mertens_constant_M` --[t_compose_with_identity {identity: "∏(1-1/p) ~ e^{-γ}/log x"}]--> output: `s_mertens_theorems`
**Techniques used:** t_compose_with_identity, t_interpolate_and_continue

### Brun's theorem on twin primes (cite: https://en.wikipedia.org/wiki/Brun%27s_theorem)
**Axioms:** `s_naturals_with_multiplication`, `s_twin_prime_set`
**Terminal:** `s_brun_twin_prime_constant_finite` (kind: theorem)
**Steps:**
1. input: `s_twin_prime_set` --[t_selberg_sieve_method {parameters: "Brun pure sieve, level y = x^{1/10}"}]--> output: `s_pi_2_x_upper_bound`
2. input: `s_pi_2_x_upper_bound` --[t_compose_with_identity {identity: "π_2(x) ≪ x (log log x)² / (log x)²"}]--> output: `s_brun_twin_prime_constant_finite`
**Techniques used:** t_selberg_sieve_method, t_compose_with_identity

### Brun–Titchmarsh inequality (cite: https://en.wikipedia.org/wiki/Brun%E2%80%93Titchmarsh_theorem)
**Axioms:** `s_naturals_with_multiplication`, `s_dirichlet_character_mod_q`
**Terminal:** `s_brun_titchmarsh_inequality` (kind: theorem)
**Steps:**
1. input: `s_dirichlet_character_mod_q` --[t_selberg_sieve_method {parameters: "Selberg Λ² sieve on AP a mod q"}]--> output: `s_sifted_count_primes_in_ap`
2. input: `s_sifted_count_primes_in_ap` --[t_compose_with_identity {identity: "π(x;q,a) ≤ 2x/(φ(q) log(x/q))"}]--> output: `s_brun_titchmarsh_inequality`
**Techniques used:** t_selberg_sieve_method, t_compose_with_identity

### Selberg–Erdős elementary proof of PNT (cite: https://en.wikipedia.org/wiki/Elementary_proof_of_the_prime_number_theorem)
**Axioms:** `s_chebyshev_function_theta_psi`, `s_naturals_with_multiplication`
**Terminal:** `s_selberg_erdos_elementary_pnt` (kind: theorem)
**Steps:**
1. input: `s_chebyshev_function_theta_psi` --[t_compose_with_identity {identity: "Selberg's formula Σ_{p≤x}(log p)² + Σ_{pq≤x} log p log q ~ 2x log x"}]--> output: `s_selberg_symmetry_formula`
2. input: `s_selberg_symmetry_formula` --[t_reduce_to_canonical_form {form: "iterate to remove oscillation in ψ(x)/x - 1"}]--> output: `s_psi_minus_x_decay`
3. input: `s_psi_minus_x_decay` --[t_compose_with_identity {identity: "ψ(x) ~ x ⇒ PNT"}]--> output: `s_selberg_erdos_elementary_pnt`
**Techniques used:** t_compose_with_identity, t_reduce_to_canonical_form

### Wiener–Ikehara Tauberian theorem (cite: https://en.wikipedia.org/wiki/Wiener%E2%80%93Ikehara_theorem)
**Axioms:** `s_dirichlet_series`, `s_riemann_zeta_function`
**Terminal:** `s_wiener_ikehara_theorem` (kind: theorem)
**Steps:**
1. input: `s_dirichlet_series` --[t_complex_analysis_to_integers {object: "boundary behavior of -ζ'/ζ at Re(s)=1"}]--> output: `s_simple_pole_at_s_eq_1`
2. input: `s_simple_pole_at_s_eq_1` --[t_frequency_decomposition {domain: "Fourier transform of mollified counting function"}]--> output: `s_tauberian_fourier_input`
3. input: `s_tauberian_fourier_input` --[t_compose_with_identity {identity: "Wiener's Tauberian: boundary analyticity ⇒ asymptotic"}]--> output: `s_wiener_ikehara_theorem`
**Techniques used:** t_complex_analysis_to_integers, t_frequency_decomposition, t_compose_with_identity

### Vinogradov's three-prime theorem (cite: https://en.wikipedia.org/wiki/Vinogradov%27s_theorem)
**Axioms:** `s_naturals_with_multiplication`, `s_circle_t_1`
**Terminal:** `s_vinogradov_three_prime_theorem` (kind: theorem)
**Steps:**
1. input: `s_naturals_with_multiplication` --[t_circle_method {decomposition: "major/minor arcs at Re(α) = a/q"}]--> output: `s_major_minor_arc_decomposition_for_3p`
2. input: `s_major_minor_arc_decomposition_for_3p` --[t_compose_with_identity {identity: "exponential sum over primes bounded on minor arcs by Vinogradov"}]--> output: `s_minor_arc_bound`
3. input: `s_minor_arc_bound` --[t_complex_analysis_to_integers {object: "main-term singular series 𝔖(N)"}]--> output: `s_vinogradov_three_prime_theorem`
**Techniques used:** t_circle_method, t_compose_with_identity, t_complex_analysis_to_integers

### Vinogradov mean-value theorem (cite: https://en.wikipedia.org/wiki/Vinogradov%27s_mean-value_theorem)
**Axioms:** `s_polynomial_ring_z_x`, `s_exponential_sum`
**Terminal:** `s_vinogradov_mean_value_theorem` (kind: theorem)
**Steps:**
1. input: `s_exponential_sum` --[t_compose_with_identity {identity: "J_{s,k}(N) counts integer solutions of Vinogradov system"}]--> output: `s_vinogradov_system_count`
2. input: `s_vinogradov_system_count` --[t_polynomial_method {form: "efficient congruencing / decoupling"}]--> output: `s_efficient_congruencing_bound`
3. input: `s_efficient_congruencing_bound` --[t_axiomatize_from_instances {abstracted_to: "J_{s,k}(N) ≪ N^{2s − k(k+1)/2 + ε} for s ≥ k(k+1)/2"}]--> output: `s_vinogradov_mean_value_theorem`
**Techniques used:** t_compose_with_identity, t_polynomial_method, t_axiomatize_from_instances

### Bombieri–Vinogradov theorem (cite: https://en.wikipedia.org/wiki/Bombieri%E2%80%93Vinogradov_theorem)
**Axioms:** `s_dirichlet_character_mod_q`, `s_naturals_with_multiplication`
**Terminal:** `s_bombieri_vinogradov` (kind: theorem)
**Steps:**
1. input: `s_dirichlet_character_mod_q` --[t_complex_analysis_to_integers {object: "large sieve for Dirichlet L-functions"}]--> output: `s_large_sieve_inequality`
2. input: `s_large_sieve_inequality` --[t_major_minor_arc_decomposition {decomposition: "explicit-formula + zero-density Linnik"}]--> output: `s_zero_density_combined`
3. input: `s_zero_density_combined` --[t_compose_with_identity {identity: "Σ_{q≤x^{1/2}/(log x)^A} max_{(a,q)=1} |ψ(x;q,a) − x/φ(q)| ≪ x/(log x)^B"}]--> output: `s_bombieri_vinogradov`
**Techniques used:** t_complex_analysis_to_integers, t_major_minor_arc_decomposition, t_compose_with_identity

### Linnik's theorem on smallest prime in AP (cite: https://en.wikipedia.org/wiki/Linnik%27s_theorem)
**Axioms:** `s_dirichlet_character_mod_q`, `s_dirichlet_l_function`
**Terminal:** `s_linnik_smallest_prime_in_ap` (kind: theorem)
**Steps:**
1. input: `s_dirichlet_l_function` --[t_complex_analysis_to_integers {object: "log-free zero-density and Deuring–Heilbronn repulsion"}]--> output: `s_zero_density_and_repulsion`
2. input: `s_zero_density_and_repulsion` --[t_compose_with_identity {identity: "p(a,q) ≪ q^L for absolute L (Linnik's constant)"}]--> output: `s_linnik_smallest_prime_in_ap`
**Techniques used:** t_complex_analysis_to_integers, t_compose_with_identity

### Pólya–Vinogradov inequality (cite: https://en.wikipedia.org/wiki/P%C3%B3lya%E2%80%93Vinogradov_inequality)
**Axioms:** `s_dirichlet_character_mod_q`, `s_exponential_sum`
**Terminal:** `s_polya_vinogradov_inequality` (kind: theorem)
**Steps:**
1. input: `s_dirichlet_character_mod_q` --[t_frequency_decomposition {domain: "finite Fourier transform mod q"}]--> output: `s_character_in_additive_frequencies`
2. input: `s_character_in_additive_frequencies` --[t_compose_with_identity {identity: "|Σ_{n≤N} χ(n)| ≤ √q log q"}]--> output: `s_polya_vinogradov_inequality`
**Techniques used:** t_frequency_decomposition, t_compose_with_identity

### Burgess bound on character sums (cite: https://en.wikipedia.org/wiki/Burgess_bound)
**Axioms:** `s_dirichlet_character_mod_q`, `s_exponential_sum`
**Terminal:** `s_burgess_bound` (kind: theorem)
**Steps:**
1. input: `s_dirichlet_character_mod_q` --[t_compose_with_identity {identity: "shift-and-average: |Σ χ(n+t)|^r"}]--> output: `s_shifted_character_moment`
2. input: `s_shifted_character_moment` --[t_complex_analysis_to_integers {object: "Weil's RH for curves over F_q, bounds for short character sums"}]--> output: `s_short_character_sum_bound`
3. input: `s_short_character_sum_bound` --[t_compose_with_identity {identity: "|Σ_{N<n<N+H} χ(n)| ≪ H^{1-1/r} q^{(r+1)/(4r²)+ε}"}]--> output: `s_burgess_bound`
**Techniques used:** t_compose_with_identity, t_complex_analysis_to_integers

### Selberg's 1/4 conjecture status / Kim–Sarnak bound (cite: https://en.wikipedia.org/wiki/Selberg%27s_1/4_conjecture)
**Axioms:** `s_modular_forms_holomorphic_or_maass`, `s_dirichlet_l_function`
**Terminal:** `s_kim_sarnak_bound` (kind: theorem)
**Steps:**
1. input: `s_modular_forms_holomorphic_or_maass` --[t_complex_analysis_to_integers {object: "symmetric square / fourth power L-functions"}]--> output: `s_symmetric_power_l_functions`
2. input: `s_symmetric_power_l_functions` --[t_compose_with_identity {identity: "non-vanishing on Re(s)=1 of Sym^n L"}]--> output: `s_kim_sarnak_bound`
**Techniques used:** t_complex_analysis_to_integers, t_compose_with_identity

### Hardy–Ramanujan partition asymptotic (cite: https://en.wikipedia.org/wiki/Hardy%E2%80%93Ramanujan_formula)
**Axioms:** `s_integer_partitions`, `s_eta_function_dedekind`
**Terminal:** `s_hardy_ramanujan_partition_asymptotic` (kind: theorem)
**Steps:**
1. input: `s_integer_partitions` --[t_complex_analysis_to_integers {object: "generating function 1/η(τ) and modular transformation"}]--> output: `s_modular_transformation_of_eta`
2. input: `s_modular_transformation_of_eta` --[t_circle_method {decomposition: "Farey arcs at rationals p/q"}]--> output: `s_farey_arc_contributions`
3. input: `s_farey_arc_contributions` --[t_compose_with_identity {identity: "p(n) ~ exp(π√(2n/3)) / (4n√3)"}]--> output: `s_hardy_ramanujan_partition_asymptotic`
**Techniques used:** t_complex_analysis_to_integers, t_circle_method, t_compose_with_identity

### Rademacher exact formula for p(n) (cite: https://en.wikipedia.org/wiki/Rademacher%27s_formula)
**Axioms:** `s_integer_partitions`, `s_eta_function_dedekind`
**Terminal:** `s_rademacher_exact_formula_partition` (kind: theorem)
**Steps:**
1. input: `s_eta_function_dedekind` --[t_circle_method {decomposition: "Rademacher contour replacing Hardy–Ramanujan major arcs"}]--> output: `s_rademacher_contour_integral`
2. input: `s_rademacher_contour_integral` --[t_compose_with_identity {identity: "p(n) = (1/π√2) Σ_{k=1}^∞ A_k(n)√k d/dn[sinh(...)/√(...)]"}]--> output: `s_rademacher_exact_formula_partition`
**Techniques used:** t_circle_method, t_compose_with_identity

### Erdős–Kac theorem (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Kac_theorem)
**Axioms:** `s_naturals_with_multiplication`, `s_additive_function_omega`
**Terminal:** `s_erdos_kac_theorem` (kind: theorem)
**Steps:**
1. input: `s_additive_function_omega` --[t_axiomatize_from_instances {abstracted_to: "ω(n) is a sum of nearly-independent random indicators 1_{p|n}"}]--> output: `s_quasi_independence_decomposition`
2. input: `s_quasi_independence_decomposition` --[t_probabilistic_existence {distribution: "Lindeberg CLT with prime densities 1/p"}]--> output: `s_clt_for_omega`
3. input: `s_clt_for_omega` --[t_compose_with_identity {identity: "(ω(n) − log log n)/√log log n → 𝒩(0,1)"}]--> output: `s_erdos_kac_theorem`
**Techniques used:** t_axiomatize_from_instances, t_probabilistic_existence, t_compose_with_identity

### Erdős–Wintner theorem (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Wintner_theorem)
**Axioms:** `s_naturals_with_multiplication`, `s_additive_function_f`
**Terminal:** `s_erdos_wintner_theorem` (kind: theorem)
**Steps:**
1. input: `s_additive_function_f` --[t_axiomatize_from_instances {abstracted_to: "convergence criteria of three series Σ f(p)/p, Σ f(p)²/p, Σ_{|f(p)|≥1} 1/p"}]--> output: `s_three_series_criterion`
2. input: `s_three_series_criterion` --[t_probabilistic_existence {distribution: "limiting law from independent Bernoullis"}]--> output: `s_erdos_wintner_theorem`
**Techniques used:** t_axiomatize_from_instances, t_probabilistic_existence

### Turán–Kubilius inequality (cite: https://en.wikipedia.org/wiki/Tur%C3%A1n%E2%80%93Kubilius_inequality)
**Axioms:** `s_naturals_with_multiplication`, `s_additive_function_f`
**Terminal:** `s_turan_kubilius_inequality` (kind: theorem)
**Steps:**
1. input: `s_additive_function_f` --[t_compose_with_identity {identity: "variance Σ |f(n) − A(x)|² ≤ x B(x)²"}]--> output: `s_second_moment_bound`
2. input: `s_second_moment_bound` --[t_axiomatize_from_instances {abstracted_to: "Chebyshev concentration for additive functions"}]--> output: `s_turan_kubilius_inequality`
**Techniques used:** t_compose_with_identity, t_axiomatize_from_instances

### Erdős–Fuchs theorem (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Fuchs_theorem)
**Axioms:** `s_naturals_with_multiplication`, `s_additive_basis`
**Terminal:** `s_erdos_fuchs_theorem` (kind: theorem)
**Steps:**
1. input: `s_additive_basis` --[t_reductio_ad_absurdum {assume: "r_2(n) = cn + O(n^{1/4}(log n)^{-1/2})"}]--> output: `s_proposed_smooth_error_term`
2. input: `s_proposed_smooth_error_term` --[t_frequency_decomposition {domain: "Fourier on the circle"}]--> output: `s_fourier_error_obstruction`
3. input: `s_fourier_error_obstruction` --[t_compose_with_identity {identity: "no smoother error term possible"}]--> output: `s_erdos_fuchs_theorem`
**Techniques used:** t_reductio_ad_absurdum, t_frequency_decomposition, t_compose_with_identity

### Erdős–Ginzburg–Ziv theorem (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Ginzburg%E2%80%93Ziv_theorem)
**Axioms:** `s_integers`, `s_finite_abelian_group_zn`
**Terminal:** `s_erdos_ginzburg_ziv_theorem` (kind: theorem)
**Steps:**
1. input: `s_finite_abelian_group_zn` --[t_pigeonhole_collision {bin: "subset sums among 2n-1 integers"}]--> output: `s_subset_sum_pigeonhole`
2. input: `s_subset_sum_pigeonhole` --[t_polynomial_method {form: "Chevalley–Warning on two quadratics over F_p"}]--> output: `s_erdos_ginzburg_ziv_theorem`
**Techniques used:** t_pigeonhole_collision, t_polynomial_method

### Freiman's theorem (cite: https://en.wikipedia.org/wiki/Freiman%27s_theorem)
**Axioms:** `s_finite_abelian_group_zn`, `s_finite_subset_a_in_z`
**Terminal:** `s_freiman_theorem` (kind: theorem)
**Steps:**
1. input: `s_finite_subset_a_in_z` --[t_compose_with_identity {identity: "small doubling |A+A| ≤ K|A|"}]--> output: `s_small_doubling_set`
2. input: `s_small_doubling_set` --[t_frequency_decomposition {domain: "Bohr set capture in Fourier spectrum"}]--> output: `s_bohr_set_inside_a`
3. input: `s_bohr_set_inside_a` --[t_structural_isomorphism {invariant: "Bohr set ≅ generalized arithmetic progression"}]--> output: `s_freiman_theorem`
**Techniques used:** t_compose_with_identity, t_frequency_decomposition, t_structural_isomorphism

### Plünnecke–Ruzsa inequality (cite: https://en.wikipedia.org/wiki/Pl%C3%BCnnecke%E2%80%93Ruzsa_inequality)
**Axioms:** `s_finite_subset_a_in_z`
**Terminal:** `s_plunnecke_ruzsa_inequality` (kind: theorem)
**Steps:**
1. input: `s_finite_subset_a_in_z` --[t_auxiliary_construction {object: "Petridis magnification ratio"}]--> output: `s_petridis_optimal_subset`
2. input: `s_petridis_optimal_subset` --[t_compose_with_identity {identity: "|nA - mA| ≤ K^{n+m} |A|"}]--> output: `s_plunnecke_ruzsa_inequality`
**Techniques used:** t_auxiliary_construction, t_compose_with_identity

### Roth's theorem on 3-APs (cite: https://en.wikipedia.org/wiki/Roth%27s_theorem_on_arithmetic_progressions)
**Axioms:** `s_finite_subset_a_in_z`, `s_circle_t_1`
**Terminal:** `s_roth_theorem_3_aps` (kind: theorem)
**Steps:**
1. input: `s_finite_subset_a_in_z` --[t_frequency_decomposition {domain: "Fourier transform on ℤ/Nℤ"}]--> output: `s_fourier_density_increment`
2. input: `s_fourier_density_increment` --[t_compose_with_identity {identity: "density increment on a sub-progression iterates"}]--> output: `s_density_increment_iteration`
3. input: `s_density_increment_iteration` --[t_axiomatize_from_instances {abstracted_to: "positive-density set in [N] contains 3-AP"}]--> output: `s_roth_theorem_3_aps`
**Techniques used:** t_frequency_decomposition, t_compose_with_identity, t_axiomatize_from_instances

### Roth's theorem on Diophantine approximation (cite: https://en.wikipedia.org/wiki/Roth%27s_theorem)
**Axioms:** `s_algebraic_number_alpha`, `s_rationals_q`
**Terminal:** `s_roth_diophantine_approximation` (kind: theorem)
**Steps:**
1. input: `s_algebraic_number_alpha` --[t_auxiliary_construction {object: "Thue–Siegel–Roth auxiliary polynomial in many variables"}]--> output: `s_aux_multivariate_polynomial`
2. input: `s_aux_multivariate_polynomial` --[t_compose_with_identity {identity: "index of vanishing forces large height"}]--> output: `s_index_height_obstruction`
3. input: `s_index_height_obstruction` --[t_reductio_ad_absurdum {assume: "|α − p/q| < q^{-2-ε} infinitely often"}]--> output: `s_roth_diophantine_approximation`
**Techniques used:** t_auxiliary_construction, t_compose_with_identity, t_reductio_ad_absurdum

### Thue's theorem (cite: https://en.wikipedia.org/wiki/Thue%27s_theorem)
**Axioms:** `s_algebraic_number_alpha`, `s_rationals_q`
**Terminal:** `s_thue_theorem` (kind: theorem)
**Steps:**
1. input: `s_algebraic_number_alpha` --[t_auxiliary_construction {object: "auxiliary polynomial of high degree (Thue)"}]--> output: `s_thue_aux_polynomial`
2. input: `s_thue_aux_polynomial` --[t_exhaustion_squeeze {lower: "two close rationals p_i/q_i", upper: "polynomial gap"}]--> output: `s_two_good_approx_obstruction`
3. input: `s_two_good_approx_obstruction` --[t_axiomatize_from_instances {abstracted_to: "Thue equation F(x,y)=m has finitely many integer solutions"}]--> output: `s_thue_theorem`
**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_axiomatize_from_instances

### Subspace theorem (Schmidt) (cite: https://en.wikipedia.org/wiki/Subspace_theorem)
**Axioms:** `s_rationals_q`, `s_linear_form_l_i`
**Terminal:** `s_schmidt_subspace_theorem` (kind: theorem)
**Steps:**
1. input: `s_linear_form_l_i` --[t_raise_dimension {dimension: "n linear forms in n variables, generalize from Roth"}]--> output: `s_higher_dim_diophantine_inequality`
2. input: `s_higher_dim_diophantine_inequality` --[t_compose_with_identity {identity: "integer points outside small product fall in finite union of hyperplanes"}]--> output: `s_schmidt_subspace_theorem`
**Techniques used:** t_raise_dimension, t_compose_with_identity

### Lindemann–Weierstrass theorem (cite: https://en.wikipedia.org/wiki/Lindemann%E2%80%93Weierstrass_theorem)
**Axioms:** `s_algebraic_number_alpha`, `s_exponential_function_complex`
**Terminal:** `s_lindemann_weierstrass` (kind: theorem)
**Steps:**
1. input: `s_exponential_function_complex` --[t_auxiliary_construction {object: "Hermite-style auxiliary integral ∫ t^{p-1}((t-α_1)...(t-α_n))^p e^{-t} dt"}]--> output: `s_hermite_integral`
2. input: `s_hermite_integral` --[t_exhaustion_squeeze {lower: "nonzero integer", upper: "small in absolute value"}]--> output: `s_integer_vs_small_obstruction`
3. input: `s_integer_vs_small_obstruction` --[t_reductio_ad_absurdum {assume: "Σ c_i e^{α_i} = 0 with α_i algebraic distinct"}]--> output: `s_lindemann_weierstrass`
**Techniques used:** t_auxiliary_construction, t_exhaustion_squeeze, t_reductio_ad_absurdum

### Gelfond–Schneider theorem (cite: https://en.wikipedia.org/wiki/Gelfond%E2%80%93Schneider_theorem)
**Axioms:** `s_algebraic_number_alpha`, `s_logarithm_function_complex`
**Terminal:** `s_gelfond_schneider_theorem` (kind: theorem)
**Steps:**
1. input: `s_algebraic_number_alpha` --[t_auxiliary_construction {object: "auxiliary function f(z) = Σ p(x,y) α^{xz} β^{yz}"}]--> output: `s_gelfond_aux_function`
2. input: `s_gelfond_aux_function` --[t_interpolate_and_continue {target: "f vanishes on many points ⇒ extrapolation gives more"}]--> output: `s_extrapolation_zeroes`
3. input: `s_extrapolation_zeroes` --[t_reductio_ad_absurdum {assume: "α^β algebraic with α algebraic ≠ 0,1, β irrational algebraic"}]--> output: `s_gelfond_schneider_theorem`
**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_reductio_ad_absurdum

### Baker's theorem on linear forms in logarithms (cite: https://en.wikipedia.org/wiki/Baker%27s_theorem)
**Axioms:** `s_algebraic_number_alpha`, `s_logarithm_function_complex`
**Terminal:** `s_baker_theorem` (kind: theorem)
**Steps:**
1. input: `s_algebraic_number_alpha` --[t_auxiliary_construction {object: "many-variable auxiliary with vanishing of high order at 0"}]--> output: `s_baker_auxiliary_many_vars`
2. input: `s_baker_auxiliary_many_vars` --[t_interpolate_and_continue {target: "extrapolation to a derivative that must be a nonzero algebraic integer"}]--> output: `s_baker_nonzero_integer_too_small`
3. input: `s_baker_nonzero_integer_too_small` --[t_compose_with_identity {identity: "effective lower bound |Λ| = |b_1 log α_1 + … + b_n log α_n| > C(α)·B^{-κ}"}]--> output: `s_baker_theorem`
**Techniques used:** t_auxiliary_construction, t_interpolate_and_continue, t_compose_with_identity

### Six exponentials theorem (cite: https://en.wikipedia.org/wiki/Six_exponentials_theorem)
**Axioms:** `s_complex_numbers`, `s_algebraic_number_alpha`
**Terminal:** `s_six_exponentials_theorem` (kind: theorem)
**Steps:**
1. input: `s_complex_numbers` --[t_auxiliary_construction {object: "interpolation determinant à la Schneider on 2×3 grid"}]--> output: `s_2x3_interpolation_determinant`
2. input: `s_2x3_interpolation_determinant` --[t_pigeonhole_collision {bin: "vanish on chosen grid → integrality"}]--> output: `s_vanishing_determinant_pigeonhole`
3. input: `s_vanishing_determinant_pigeonhole` --[t_axiomatize_from_instances {abstracted_to: "at least one of six exponentials e^{x_i y_j} is transcendental"}]--> output: `s_six_exponentials_theorem`
**Techniques used:** t_auxiliary_construction, t_pigeonhole_collision, t_axiomatize_from_instances

### Schneider–Lang theorem (cite: https://en.wikipedia.org/wiki/Schneider%E2%80%93Lang_theorem)
**Axioms:** `s_meromorphic_function_finite_order`, `s_algebraic_number_alpha`
**Terminal:** `s_schneider_lang_theorem` (kind: theorem)
**Steps:**
1. input: `s_meromorphic_function_finite_order` --[t_compose_with_identity {identity: "algebraic differential ring closed under d/dz"}]--> output: `s_meromorphic_algebraic_ring`
2. input: `s_meromorphic_algebraic_ring` --[t_auxiliary_construction {object: "auxiliary polynomial in two functions"}]--> output: `s_schneider_lang_aux`
3. input: `s_schneider_lang_aux` --[t_axiomatize_from_instances {abstracted_to: "only finitely many algebraic points where both functions take algebraic values"}]--> output: `s_schneider_lang_theorem`
**Techniques used:** t_compose_with_identity, t_auxiliary_construction, t_axiomatize_from_instances

### Wüstholz analytic subgroup theorem (cite: https://en.wikipedia.org/wiki/Analytic_subgroup_theorem)
**Axioms:** `s_commutative_algebraic_group_g_over_q_bar`, `s_logarithm_function_complex`
**Terminal:** `s_wustholz_analytic_subgroup_theorem` (kind: theorem)
**Steps:**
1. input: `s_commutative_algebraic_group_g_over_q_bar` --[t_axiomatize_from_instances {abstracted_to: "u ∈ Lie(G) with exp_G(u) algebraic, lies on a proper algebraic Lie subalgebra over ℚ̄"}]--> output: `s_wustholz_analytic_subgroup_statement`
2. input: `s_wustholz_analytic_subgroup_statement` --[t_compose_with_identity {identity: "unifies Baker, Gelfond–Schneider, Lindemann–Weierstrass"}]--> output: `s_wustholz_analytic_subgroup_theorem`
**Techniques used:** t_axiomatize_from_instances, t_compose_with_identity

---

## Arithmetic geometry & L-functions

### Weil conjectures (over finite fields) (cite: https://en.wikipedia.org/wiki/Weil_conjectures)
**Axioms:** `s_smooth_projective_variety_over_fq`, `s_etale_cohomology`
**Terminal:** `s_weil_conjectures_complete` (kind: theorem)
**Steps:**
1. input: `s_smooth_projective_variety_over_fq` --[t_complex_analysis_to_integers {object: "zeta function Z(X,t) = exp(Σ #X(F_{q^n}) t^n/n)"}]--> output: `s_zeta_function_of_variety`
2. input: `⟨s_zeta_function_of_variety, s_etale_cohomology⟩` --[t_analysis_algebra_topology_bridge {bridge: "ℓ-adic cohomology trace = point count"}]--> output: `s_etale_trace_formula`
3. input: `s_etale_trace_formula` --[t_deformation_cohomology {target: "Poincaré duality + RH for eigenvalues of Frobenius |λ| = q^{i/2}"}]--> output: `s_weil_conjectures_complete`
**Techniques used:** t_complex_analysis_to_integers, t_analysis_algebra_topology_bridge, t_deformation_cohomology

### Hasse–Weil bound for curves over F_q (cite: https://en.wikipedia.org/wiki/Hasse%27s_theorem_on_elliptic_curves)
**Axioms:** `s_smooth_projective_curve_over_fq`, `s_riemann_hypothesis_for_curves`
**Terminal:** `s_hasse_weil_bound` (kind: theorem)
**Steps:**
1. input: `s_smooth_projective_curve_over_fq` --[t_complex_analysis_to_integers {object: "L-function of curve, eigenvalues |λ_i| = √q"}]--> output: `s_curve_l_function_eigenvalues`
2. input: `s_curve_l_function_eigenvalues` --[t_compose_with_identity {identity: "|#X(F_q) − (q+1)| ≤ 2g√q"}]--> output: `s_hasse_weil_bound`
**Techniques used:** t_complex_analysis_to_integers, t_compose_with_identity

### Honda–Tate theorem (cite: https://en.wikipedia.org/wiki/Honda%E2%80%93Tate_theorem)
**Axioms:** `s_abelian_variety_over_fq`, `s_weil_q_numbers`
**Terminal:** `s_honda_tate_theorem` (kind: theorem)
**Steps:**
1. input: `s_abelian_variety_over_fq` --[t_axiomatize_from_instances {abstracted_to: "Frobenius eigenvalue is a Weil q-number"}]--> output: `s_frobenius_to_weil_number`
2. input: `s_frobenius_to_weil_number` --[t_structural_isomorphism {invariant: "simple abelian varieties over F_q up to isogeny ↔ Galois orbits of Weil q-numbers"}]--> output: `s_honda_tate_theorem`
**Techniques used:** t_axiomatize_from_instances, t_structural_isomorphism

### Tate's isogeny theorem (cite: https://en.wikipedia.org/wiki/Tate%27s_isogeny_theorem)
**Axioms:** `s_abelian_variety_over_fq`, `s_l_adic_tate_module`
**Terminal:** `s_tate_isogeny_theorem` (kind: theorem)
**Steps:**
1. input: `s_abelian_variety_over_fq` --[t_heights_and_galois_rep_bridge {bridge: "Galois representation on T_ℓ(A)"}]--> output: `s_galois_action_on_tate_module`
2. input: `s_galois_action_on_tate_module` --[t_structural_isomorphism {invariant: "Hom(A,B) ⊗ ℤ_ℓ ≅ Hom_{Gal}(T_ℓ A, T_ℓ B)"}]--> output: `s_tate_isogeny_theorem`
**Techniques used:** t_heights_and_galois_rep_bridge, t_structural_isomorphism

### Mordell–Weil theorem (cite: https://en.wikipedia.org/wiki/Mordell%E2%80%93Weil_theorem)
**Axioms:** `s_abelian_variety_over_q`, `s_naive_height_on_an`
**Terminal:** `s_mordell_weil_theorem` (kind: theorem)
**Steps:**
1. input: `s_abelian_variety_over_q` --[t_compose_with_identity {identity: "weak Mordell–Weil: A(K)/nA(K) is finite"}]--> output: `s_weak_mordell_weil_quotient_finite`
2. input: `⟨s_weak_mordell_weil_quotient_finite, s_naive_height_on_an⟩` --[t_heights_and_galois_rep_bridge {bridge: "Néron–Tate canonical height"}]--> output: `s_canonical_height_on_abelian_variety`
3. input: `s_canonical_height_on_abelian_variety` --[t_infinite_descent {measure: "Néron–Tate height of generator candidates"}]--> output: `s_mordell_weil_theorem`
**Techniques used:** t_compose_with_identity, t_heights_and_galois_rep_bridge, t_infinite_descent

### Siegel's theorem on integral points (cite: https://en.wikipedia.org/wiki/Siegel%27s_theorem_on_integral_points)
**Axioms:** `s_smooth_projective_curve_over_q`, `s_mordell_weil_theorem`
**Terminal:** `s_siegel_integral_points_theorem` (kind: theorem)
**Steps:**
1. input: `⟨s_smooth_projective_curve_over_q, s_mordell_weil_theorem⟩` --[t_heights_and_galois_rep_bridge {bridge: "embed into Jacobian, use Mordell–Weil"}]--> output: `s_curve_in_jacobian_finite_generation`
2. input: `s_curve_in_jacobian_finite_generation` --[t_compose_with_identity {identity: "Roth's theorem on each coordinate"}]--> output: `s_siegel_integral_points_theorem`
**Techniques used:** t_heights_and_galois_rep_bridge, t_compose_with_identity

### Nagell–Lutz theorem (cite: https://en.wikipedia.org/wiki/Nagell%E2%80%93Lutz_theorem)
**Axioms:** `s_elliptic_curve_over_q`, `s_torsion_subgroup`
**Terminal:** `s_nagell_lutz_theorem` (kind: theorem)
**Steps:**
1. input: `s_elliptic_curve_over_q` --[t_reduce_to_canonical_form {form: "minimal Weierstrass model y² = x³ + ax + b"}]--> output: `s_minimal_weierstrass_form`
2. input: `s_minimal_weierstrass_form` --[t_compose_with_identity {identity: "torsion point (x,y) has integer coords, y=0 or y² | disc"}]--> output: `s_nagell_lutz_theorem`
**Techniques used:** t_reduce_to_canonical_form, t_compose_with_identity

### Mazur's torsion theorem (cite: https://en.wikipedia.org/wiki/Torsion_conjecture)
**Axioms:** `s_elliptic_curve_over_q`, `s_modular_curve_x0_n`
**Terminal:** `s_mazur_torsion_theorem` (kind: theorem)
**Steps:**
1. input: `s_modular_curve_x0_n` --[t_heights_and_galois_rep_bridge {bridge: "study rational points on modular curves X_1(N)"}]--> output: `s_rational_points_on_x1_n`
2. input: `s_rational_points_on_x1_n` --[t_compose_with_identity {identity: "non-cusp rational points absent for N > 12, except N=14,15,16,18,20,21,24,25,27"}]--> output: `s_modular_curves_no_extra_rational_points`
3. input: `s_modular_curves_no_extra_rational_points` --[t_axiomatize_from_instances {abstracted_to: "torsion subgroup of E(ℚ) is one of 15 explicit groups"}]--> output: `s_mazur_torsion_theorem`
**Techniques used:** t_heights_and_galois_rep_bridge, t_compose_with_identity, t_axiomatize_from_instances

### Merel's uniform boundedness (cite: https://en.wikipedia.org/wiki/Torsion_conjecture)
**Axioms:** `s_elliptic_curve_over_q`, `s_modular_curve_x1_n`
**Terminal:** `s_merel_uniform_boundedness` (kind: theorem)
**Steps:**
1. input: `s_modular_curve_x1_n` --[t_heights_and_galois_rep_bridge {bridge: "Eisenstein quotient analysis over number fields of bounded degree"}]--> output: `s_eisenstein_quotient_bound`
2. input: `s_eisenstein_quotient_bound` --[t_axiomatize_from_instances {abstracted_to: "|E(K)_tor| bounded only in terms of [K:ℚ]"}]--> output: `s_merel_uniform_boundedness`
**Techniques used:** t_heights_and_galois_rep_bridge, t_axiomatize_from_instances

### Manin–Drinfeld theorem (cite: https://en.wikipedia.org/wiki/Manin%E2%80%93Drinfeld_theorem)
**Axioms:** `s_modular_curve_x0_n`, `s_cusp_divisors`
**Terminal:** `s_manin_drinfeld_theorem` (kind: theorem)
**Steps:**
1. input: `s_cusp_divisors` --[t_complex_analysis_to_integers {object: "Eisenstein series differential have rational q-expansion"}]--> output: `s_eisenstein_divisor_rationality`
2. input: `s_eisenstein_divisor_rationality` --[t_compose_with_identity {identity: "differences of cusps are torsion in J_0(N)"}]--> output: `s_manin_drinfeld_theorem`
**Techniques used:** t_complex_analysis_to_integers, t_compose_with_identity

### Tunnell's theorem (congruent numbers) (cite: https://en.wikipedia.org/wiki/Tunnell%27s_theorem)
**Axioms:** `s_elliptic_curve_over_q`, `s_modular_forms_holomorphic_or_maass`
**Terminal:** `s_tunnell_theorem` (kind: theorem)
**Steps:**
1. input: `s_elliptic_curve_over_q` --[t_complex_analysis_to_integers {object: "modular form of weight 3/2 associated to E_n: y²=x³-n²x"}]--> output: `s_weight_three_halves_form`
2. input: `s_weight_three_halves_form` --[t_compose_with_identity {identity: "(assuming BSD for E_n) n congruent iff weight-3/2 coefficient = 0"}]--> output: `s_tunnell_theorem`
**Techniques used:** t_complex_analysis_to_integers, t_compose_with_identity

### Modularity theorem (full, Breuil–Conrad–Diamond–Taylor) (cite: https://en.wikipedia.org/wiki/Modularity_theorem)
**Axioms:** `s_elliptic_curve_over_q`, `s_modular_forms_holomorphic_or_maass`
**Terminal:** `s_modularity_theorem_full` (kind: theorem)
**Steps:**
1. input: `s_elliptic_curve_over_q` --[t_heights_and_galois_rep_bridge {bridge: "ℓ-adic Galois rep ρ_E,ℓ from Tate module"}]--> output: `s_l_adic_galois_representation_of_E`
2. input: `s_l_adic_galois_representation_of_E` --[t_wiles_modularity {variant: "extend semistable case to all by R=T at potentially semistable primes"}]--> output: `s_full_modularity_lift_machine`
3. input: `s_full_modularity_lift_machine` --[t_axiomatize_from_instances {abstracted_to: "every E/ℚ is modular"}]--> output: `s_modularity_theorem_full`
**Techniques used:** t_heights_and_galois_rep_bridge, t_wiles_modularity, t_axiomatize_from_instances

### Ribet's level-lowering theorem (cite: https://en.wikipedia.org/wiki/Ribet%27s_theorem)
**Axioms:** `s_modular_forms_holomorphic_or_maass`, `s_galois_representation_residual`
**Terminal:** `s_ribet_level_lowering` (kind: theorem)
**Steps:**
1. input: `s_galois_representation_residual` --[t_level_lowering_bridge {bridge: "if ρ̄ unramified at p, level can be reduced"}]--> output: `s_residual_unramified_at_p_consequence`
2. input: `s_residual_unramified_at_p_consequence` --[t_compose_with_identity {identity: "Serre's epsilon conjecture, level drops"}]--> output: `s_ribet_level_lowering`
**Techniques used:** t_level_lowering_bridge, t_compose_with_identity

### Eichler–Shimura congruence (cite: https://en.wikipedia.org/wiki/Eichler%E2%80%93Shimura_congruence_relation)
**Axioms:** `s_modular_curve_x0_n`, `s_hecke_operator`
**Terminal:** `s_eichler_shimura_congruence` (kind: theorem)
**Steps:**
1. input: `⟨s_modular_curve_x0_n, s_hecke_operator⟩` --[t_reduce_to_canonical_form {form: "reduce mod p, identify T_p with Frob + Verschiebung"}]--> output: `s_hecke_mod_p_decomposition`
2. input: `s_hecke_mod_p_decomposition` --[t_compose_with_identity {identity: "T_p ≡ Frob_p + p · V_p mod p on J_0(N)"}]--> output: `s_eichler_shimura_congruence`
**Techniques used:** t_reduce_to_canonical_form, t_compose_with_identity

### Khare–Wintenberger (Serre's modularity conjecture) (cite: https://en.wikipedia.org/wiki/Serre%27s_modularity_conjecture)
**Axioms:** `s_galois_representation_residual`, `s_modular_forms_holomorphic_or_maass`
**Terminal:** `s_khare_wintenberger_serre_modularity` (kind: theorem)
**Steps:**
1. input: `s_galois_representation_residual` --[t_wiles_modularity {variant: "modularity lifting along p-stable Galois deformation"}]--> output: `s_modularity_lifting_for_residual_rep`
2. input: `s_modularity_lifting_for_residual_rep` --[t_axiomatize_from_instances {abstracted_to: "every odd irreducible 2-dim mod-p Galois rep comes from a modular form"}]--> output: `s_khare_wintenberger_serre_modularity`
**Techniques used:** t_wiles_modularity, t_axiomatize_from_instances

### Waldspurger's theorem (cite: https://en.wikipedia.org/wiki/Waldspurger%27s_theorem)
**Axioms:** `s_modular_forms_holomorphic_or_maass`, `s_l_function_central_value`
**Terminal:** `s_waldspurger_theorem` (kind: theorem)
**Steps:**
1. input: `s_modular_forms_holomorphic_or_maass` --[t_compose_with_identity {identity: "Shimura correspondence: weight 2k ↔ weight k+1/2 forms"}]--> output: `s_shimura_correspondence_pair`
2. input: `s_shimura_correspondence_pair` --[t_compose_with_identity {identity: "central L-value = |Fourier coeff of half-integer form|²"}]--> output: `s_waldspurger_theorem`
**Techniques used:** t_compose_with_identity

### Gross–Zagier formula (cite: https://en.wikipedia.org/wiki/Gross%E2%80%93Zagier_theorem)
**Axioms:** `s_elliptic_curve_over_q`, `s_heegner_points`
**Terminal:** `s_gross_zagier_formula` (kind: theorem)
**Steps:**
1. input: `s_heegner_points` --[t_heights_and_galois_rep_bridge {bridge: "Néron–Tate height of Heegner point on E"}]--> output: `s_heegner_height`
2. input: `s_heegner_height` --[t_compose_with_identity {identity: "ĥ(y_K) = c · L'(E/K, 1)"}]--> output: `s_gross_zagier_formula`
**Techniques used:** t_heights_and_galois_rep_bridge, t_compose_with_identity

### Kolyvagin's theorem (cite: https://en.wikipedia.org/wiki/Kolyvagin%27s_theorem)
**Axioms:** `s_elliptic_curve_over_q`, `s_euler_system_kolyvagin`
**Terminal:** `s_kolyvagin_theorem` (kind: theorem)
**Steps:**
1. input: `s_euler_system_kolyvagin` --[t_galois_correspondence {field_tower: "anti-cyclotomic tower over imaginary quadratic K"}]--> output: `s_anti_cyclotomic_compatible_system`
2. input: `s_anti_cyclotomic_compatible_system` --[t_compose_with_identity {identity: "Heegner point nontorsion ⇒ rank ≤ 1 and Sha finite for analytic rank ≤ 1"}]--> output: `s_kolyvagin_theorem`
**Techniques used:** t_galois_correspondence, t_compose_with_identity

### Iwasawa main conjecture (Mazur–Wiles, total) (cite: https://en.wikipedia.org/wiki/Iwasawa_theory)
**Axioms:** `s_cyclotomic_z_p_extension`, `s_p_adic_l_function`
**Terminal:** `s_iwasawa_main_conjecture` (kind: theorem)
**Steps:**
1. input: `s_cyclotomic_z_p_extension` --[t_axiomatize_from_instances {abstracted_to: "Iwasawa algebra Λ = ℤ_p[[T]] acts on class groups"}]--> output: `s_class_group_inverse_limit_module`
2. input: `s_class_group_inverse_limit_module` --[t_heights_and_galois_rep_bridge {bridge: "characteristic ideal = Kubota–Leopoldt L_p"}]--> output: `s_iwasawa_main_conjecture`
**Techniques used:** t_axiomatize_from_instances, t_heights_and_galois_rep_bridge

### Class number formula (Dirichlet) (cite: https://en.wikipedia.org/wiki/Class_number_formula)
**Axioms:** `s_number_field_k`, `s_dedekind_zeta_function`
**Terminal:** `s_class_number_formula` (kind: theorem)
**Steps:**
1. input: `s_dedekind_zeta_function` --[t_complex_analysis_to_integers {object: "residue at s=1 of ζ_K(s)"}]--> output: `s_residue_of_dedekind_zeta`
2. input: `s_residue_of_dedekind_zeta` --[t_compose_with_identity {identity: "Res_{s=1} ζ_K = (2^{r_1}(2π)^{r_2} h_K R_K)/(w_K √|disc|)"}]--> output: `s_class_number_formula`
**Techniques used:** t_complex_analysis_to_integers, t_compose_with_identity

### Dirichlet's unit theorem (cite: https://en.wikipedia.org/wiki/Dirichlet%27s_unit_theorem)
**Axioms:** `s_ring_of_integers_o_k`, `s_logarithmic_embedding_into_rn`
**Terminal:** `s_dirichlet_unit_theorem` (kind: theorem)
**Steps:**
1. input: `s_ring_of_integers_o_k` --[t_projection_to_subspace {subspace: "logarithmic embedding into hyperplane of ℝ^{r_1+r_2}"}]--> output: `s_log_lattice_in_hyperplane`
2. input: `s_log_lattice_in_hyperplane` --[t_compose_with_identity {identity: "discrete + cocompact ⇒ full lattice of rank r_1+r_2-1"}]--> output: `s_dirichlet_unit_theorem`
**Techniques used:** t_projection_to_subspace, t_compose_with_identity

### Minkowski's theorem on lattices (cite: https://en.wikipedia.org/wiki/Minkowski%27s_theorem)
**Axioms:** `s_lattice_in_rn`, `s_convex_symmetric_body`
**Terminal:** `s_minkowski_lattice_theorem` (kind: theorem)
**Steps:**
1. input: `⟨s_lattice_in_rn, s_convex_symmetric_body⟩` --[t_compactness_argument {target: "volume comparison vol(K) > 2^n vol(fundamental domain)"}]--> output: `s_volume_dominance_condition`
2. input: `s_volume_dominance_condition` --[t_pigeonhole_collision {bin: "K/2 translates overlap mod lattice"}]--> output: `s_minkowski_lattice_theorem`
**Techniques used:** t_compactness_argument, t_pigeonhole_collision

### Minkowski bound for class group (cite: https://en.wikipedia.org/wiki/Minkowski%27s_bound)
**Axioms:** `s_ring_of_integers_o_k`, `s_minkowski_lattice_theorem`
**Terminal:** `s_minkowski_class_number_bound` (kind: theorem)
**Steps:**
1. input: `s_ring_of_integers_o_k` --[t_compose_with_identity {identity: "every ideal class has representative of norm ≤ M_K = (4/π)^{r_2}(n!/n^n)√|disc|"}]--> output: `s_class_rep_below_minkowski_bound`
2. input: `s_class_rep_below_minkowski_bound` --[t_axiomatize_from_instances {abstracted_to: "class group is finite"}]--> output: `s_minkowski_class_number_bound`
**Techniques used:** t_compose_with_identity, t_axiomatize_from_instances

### Stark conjectures (rank-0 abelian case, proven) (cite: https://en.wikipedia.org/wiki/Stark_conjectures)
**Axioms:** `s_artin_l_function`, `s_abelian_extension_of_number_field`
**Terminal:** `s_stark_rank_0_abelian` (kind: theorem)
**Steps:**
1. input: `s_artin_l_function` --[t_complex_analysis_to_integers {object: "leading Taylor coefficient L^*(0,χ) of partial zeta"}]--> output: `s_stark_unit_candidate`
2. input: `s_stark_unit_candidate` --[t_axiomatize_from_instances {abstracted_to: "rank-0 case proven via class number formula"}]--> output: `s_stark_rank_0_abelian`
**Techniques used:** t_complex_analysis_to_integers, t_axiomatize_from_instances

### Brauer–Siegel theorem (cite: https://en.wikipedia.org/wiki/Brauer%E2%80%93Siegel_theorem)
**Axioms:** `s_number_field_k`, `s_dedekind_zeta_function`
**Terminal:** `s_brauer_siegel_theorem` (kind: theorem)
**Steps:**
1. input: `s_dedekind_zeta_function` --[t_complex_analysis_to_integers {object: "log h_K R_K ~ log √|disc|"}]--> output: `s_log_hr_asymptotic`
2. input: `s_log_hr_asymptotic` --[t_compose_with_identity {identity: "as disc → ∞ within families with bounded degree"}]--> output: `s_brauer_siegel_theorem`
**Techniques used:** t_complex_analysis_to_integers, t_compose_with_identity

### Heegner's theorem (class number 1) (cite: https://en.wikipedia.org/wiki/Stark%E2%80%93Heegner_theorem)
**Axioms:** `s_imaginary_quadratic_field`, `s_class_number`
**Terminal:** `s_heegner_class_number_one` (kind: theorem)
**Steps:**
1. input: `s_imaginary_quadratic_field` --[t_complex_analysis_to_integers {object: "Hilbert class polynomial and j-invariant integrality"}]--> output: `s_hilbert_class_polynomial`
2. input: `s_hilbert_class_polynomial` --[t_axiomatize_from_instances {abstracted_to: "only nine imaginary quadratic fields with class number 1"}]--> output: `s_heegner_class_number_one`
**Techniques used:** t_complex_analysis_to_integers, t_axiomatize_from_instances

### Goldfeld's effective lower bound on class number (cite: https://en.wikipedia.org/wiki/Effective_results_in_number_theory)
**Axioms:** `s_imaginary_quadratic_field`, `s_l_function_central_value`
**Terminal:** `s_goldfeld_effective_class_number` (kind: theorem)
**Steps:**
1. input: `s_l_function_central_value` --[t_compose_with_identity {identity: "use elliptic curve with L'(1)≠0 and L(1)=0 (rank ≥ 2) via Gross–Zagier"}]--> output: `s_gross_zagier_input`
2. input: `s_gross_zagier_input` --[t_compose_with_identity {identity: "h(d) ≫ (log|d|)^{1-ε} effective"}]--> output: `s_goldfeld_effective_class_number`
**Techniques used:** t_compose_with_identity

### Faltings' product theorem (cite: https://en.wikipedia.org/wiki/Faltings%27_product_theorem)
**Axioms:** `s_smooth_projective_variety_over_q`, `s_arakelov_geometry`
**Terminal:** `s_faltings_product_theorem` (kind: theorem)
**Steps:**
1. input: `s_smooth_projective_variety_over_q` --[t_auxiliary_construction {object: "global section of arithmetic line bundle of high index"}]--> output: `s_high_index_arakelov_section`
2. input: `s_high_index_arakelov_section` --[t_compose_with_identity {identity: "rational points concentrate in proper algebraic subset of product"}]--> output: `s_faltings_product_theorem`
**Techniques used:** t_auxiliary_construction, t_compose_with_identity

### Lang–Vojta conjecture (status / Vojta height inequality) (cite: https://en.wikipedia.org/wiki/Vojta%27s_conjecture)
**Axioms:** `s_smooth_projective_variety_over_q`, `s_naive_height_on_an`
**Terminal:** `s_vojta_height_inequality_statement` (kind: theorem)
**Steps:**
1. input: `s_smooth_projective_variety_over_q` --[t_heights_and_galois_rep_bridge {bridge: "Vojta dictionary between diophantine and Nevanlinna"}]--> output: `s_vojta_diophantine_dictionary`
2. input: `s_vojta_diophantine_dictionary` --[t_axiomatize_from_instances {abstracted_to: "h(K_X+D) ≤ (1+ε) h_A − h_disc + O(1) on integral points"}]--> output: `s_vojta_height_inequality_statement`
**Techniques used:** t_heights_and_galois_rep_bridge, t_axiomatize_from_instances

### Bounded gaps between primes (Zhang / Maynard) (cite: https://en.wikipedia.org/wiki/Bounded_gaps_between_primes) — extension of `s_bounded_gaps_between_primes`
**Axioms:** `s_naturals_with_multiplication`, `s_admissible_k_tuple`
**Terminal:** `s_maynard_bounded_gaps_improved` (kind: theorem)
**Steps:**
1. input: `s_admissible_k_tuple` --[t_selberg_sieve_method {parameters: "Maynard multidimensional weight"}]--> output: `s_multidim_selberg_weight`
2. input: `s_multidim_selberg_weight` --[t_compose_with_identity {identity: "lim inf (p_{n+m} − p_n) < ∞ for any m"}]--> output: `s_maynard_bounded_gaps_improved`
**Techniques used:** t_selberg_sieve_method, t_compose_with_identity

### Heath-Brown three-cubes representation (cite: https://en.wikipedia.org/wiki/Sums_of_three_cubes)
**Axioms:** `s_integers`, `s_circle_t_1`
**Terminal:** `s_heath_brown_three_cubes_density` (kind: theorem)
**Steps:**
1. input: `s_integers` --[t_circle_method {decomposition: "minor arcs via three-cube exponential sum"}]--> output: `s_three_cubes_minor_arc_bound`
2. input: `s_three_cubes_minor_arc_bound` --[t_compose_with_identity {identity: "density of n representable as x³+y³+z³ is positive (modulo 9 obstruction)"}]--> output: `s_heath_brown_three_cubes_density`
**Techniques used:** t_circle_method, t_compose_with_identity

### Hooley on Artin's primitive-root conjecture (under GRH) (cite: https://en.wikipedia.org/wiki/Artin%27s_conjecture_on_primitive_roots)
**Axioms:** `s_naturals_with_multiplication`, `s_grh_for_dedekind_zeta`
**Terminal:** `s_hooley_artin_primitive_root_grh` (kind: theorem)
**Steps:**
1. input: `s_grh_for_dedekind_zeta` --[t_complex_analysis_to_integers {object: "Chebotarev with explicit error"}]--> output: `s_grh_chebotarev_explicit`
2. input: `s_grh_chebotarev_explicit` --[t_sieve_by_optimized_quadratic {sieve: "inclusion–exclusion over Kummer towers Q(ζ_p, a^{1/p})"}]--> output: `s_hooley_artin_primitive_root_grh`
**Techniques used:** t_complex_analysis_to_integers, t_sieve_by_optimized_quadratic

### Hardy–Littlewood prime k-tuples conjecture (status / circle-method input) (cite: https://en.wikipedia.org/wiki/First_Hardy%E2%80%93Littlewood_conjecture) — note: a conjecture, but the circle-method singular-series predictor is a theorem
**Axioms:** `s_naturals_with_multiplication`, `s_admissible_k_tuple`
**Terminal:** `s_hardy_littlewood_singular_series_predictor` (kind: theorem)
**Steps:**
1. input: `s_admissible_k_tuple` --[t_circle_method {decomposition: "major arcs only — heuristic correct count"}]--> output: `s_singular_series_major_arc_count`
2. input: `s_singular_series_major_arc_count` --[t_axiomatize_from_instances {abstracted_to: "asymptotic count = 𝔖(𝓗) · x/(log x)^k under conjecture"}]--> output: `s_hardy_littlewood_singular_series_predictor`
**Techniques used:** t_circle_method, t_axiomatize_from_instances

### Brun–Hooley sieve / linear sieve fundamental lemma (cite: https://en.wikipedia.org/wiki/Sieve_theory)
**Axioms:** `s_naturals_with_multiplication`, `s_sieve_problem_axiomatic`
**Terminal:** `s_fundamental_lemma_of_sieve` (kind: theorem)
**Steps:**
1. input: `s_sieve_problem_axiomatic` --[t_selberg_sieve_method {parameters: "dimension κ, level D"}]--> output: `s_selberg_upper_lower_bounds`
2. input: `s_selberg_upper_lower_bounds` --[t_compose_with_identity {identity: "main term · (1 + O(e^{-s log s})) for s = log D / log z"}]--> output: `s_fundamental_lemma_of_sieve`
**Techniques used:** t_selberg_sieve_method, t_compose_with_identity

### Hasse principle failure / Reichardt–Lind counterexample (cite: https://en.wikipedia.org/wiki/Hasse_principle)
**Axioms:** `s_smooth_projective_curve_over_q`, `s_hasse_minkowski`
**Terminal:** `s_hasse_principle_failure_genus_one` (kind: theorem)
**Steps:**
1. input: `s_smooth_projective_curve_over_q` --[t_auxiliary_construction {object: "Reichardt–Lind curve 2y² = 1 − 17x⁴"}]--> output: `s_reichardt_lind_curve_specific`
2. input: `s_reichardt_lind_curve_specific` --[t_compose_with_identity {identity: "locally soluble everywhere, no rational point"}]--> output: `s_hasse_principle_failure_genus_one`
**Techniques used:** t_auxiliary_construction, t_compose_with_identity

### Birch's theorem on systems of forms (cite: https://en.wikipedia.org/wiki/Birch%27s_theorem)
**Axioms:** `s_homogeneous_form_degree_d`, `s_circle_t_1`
**Terminal:** `s_birch_theorem_systems_of_forms` (kind: theorem)
**Steps:**
1. input: `s_homogeneous_form_degree_d` --[t_circle_method {decomposition: "Birch's high-dimensional major/minor arcs"}]--> output: `s_birch_circle_method_setup`
2. input: `s_birch_circle_method_setup` --[t_axiomatize_from_instances {abstracted_to: "system of R forms of degree d has nontrivial integer zero if n ≥ R · constant(d,R)"}]--> output: `s_birch_theorem_systems_of_forms`
**Techniques used:** t_circle_method, t_axiomatize_from_instances

### Mahler's compactness theorem (cite: https://en.wikipedia.org/wiki/Mahler%27s_compactness_theorem)
**Axioms:** `s_lattice_in_rn`, `s_space_of_unimodular_lattices`
**Terminal:** `s_mahler_compactness_theorem` (kind: theorem)
**Steps:**
1. input: `s_space_of_unimodular_lattices` --[t_compactness_argument {target: "subsets of lattices with uniform shortest-vector bound"}]--> output: `s_mahler_pre_compact_criterion`
2. input: `s_mahler_pre_compact_criterion` --[t_axiomatize_from_instances {abstracted_to: "lim of unimodular lattices with bounded systole has subsequential limit"}]--> output: `s_mahler_compactness_theorem`
**Techniques used:** t_compactness_argument, t_axiomatize_from_instances

### Ax–Kochen theorem (cite: https://en.wikipedia.org/wiki/Ax%E2%80%93Kochen_theorem)
**Axioms:** `s_p_adic_completions_q_p`, `s_homogeneous_form_degree_d`
**Terminal:** `s_ax_kochen_theorem` (kind: theorem)
**Steps:**
1. input: `s_p_adic_completions_q_p` --[t_ultraproduct_transfer {target: "ultraproduct of ℚ_p ≅ ultraproduct of F_p((t))"}]--> output: `s_ultraproduct_isomorphism_local_fields`
2. input: `s_ultraproduct_isomorphism_local_fields` --[t_axiomatize_from_instances {abstracted_to: "every degree-d form in n > d² variables over ℚ_p has nontrivial zero for p sufficiently large"}]--> output: `s_ax_kochen_theorem`
**Techniques used:** t_ultraproduct_transfer, t_axiomatize_from_instances

### Skolem–Mahler–Lech theorem (cite: https://en.wikipedia.org/wiki/Skolem%E2%80%93Mahler%E2%80%93Lech_theorem)
**Axioms:** `s_linear_recurrence_sequence`, `s_p_adic_completions_q_p`
**Terminal:** `s_skolem_mahler_lech_theorem` (kind: theorem)
**Steps:**
1. input: `s_linear_recurrence_sequence` --[t_interpolate_and_continue {target: "p-adic analytic continuation of n ↦ a_n"}]--> output: `s_p_adic_analytic_extension`
2. input: `s_p_adic_analytic_extension` --[t_compose_with_identity {identity: "zero set of p-adic analytic function on ℤ_p is finite union of arithmetic progressions"}]--> output: `s_skolem_mahler_lech_theorem`
**Techniques used:** t_interpolate_and_continue, t_compose_with_identity

### Mahler's theorem on continuous p-adic functions (cite: https://en.wikipedia.org/wiki/Mahler%27s_theorem)
**Axioms:** `s_p_adic_completions_q_p`, `s_continuous_function_qp_to_qp`
**Terminal:** `s_mahler_continuous_p_adic` (kind: theorem)
**Steps:**
1. input: `s_continuous_function_qp_to_qp` --[t_axiomatize_from_instances {abstracted_to: "binomial polynomials C(x,n) are uniformly dense in C(ℤ_p, ℚ_p)"}]--> output: `s_mahler_expansion_basis`
2. input: `s_mahler_expansion_basis` --[t_compose_with_identity {identity: "f(x) = Σ a_n C(x,n) with a_n → 0"}]--> output: `s_mahler_continuous_p_adic`
**Techniques used:** t_axiomatize_from_instances, t_compose_with_identity

### Mahler's theorem on transcendence of e (special case) (cite: https://en.wikipedia.org/wiki/E_(mathematical_constant)#Proofs)
**Axioms:** `s_exponential_function_complex`, `s_rationals_q`
**Terminal:** `s_e_transcendental` (kind: theorem)
**Steps:**
1. input: `s_exponential_function_complex` --[t_auxiliary_construction {object: "Hermite integral I_k = ∫_0^k t^{p-1}((t-1)…(t-n))^p e^{-t} dt"}]--> output: `s_hermite_integral_for_e`
2. input: `s_hermite_integral_for_e` --[t_reductio_ad_absurdum {assume: "e algebraic"}]--> output: `s_e_transcendental`
**Techniques used:** t_auxiliary_construction, t_reductio_ad_absurdum

### Transcendence of π (Lindemann) (cite: https://en.wikipedia.org/wiki/Pi#Irrationality_and_transcendence)
**Axioms:** `s_complex_numbers`, `s_lindemann_weierstrass`
**Terminal:** `s_pi_transcendental` (kind: theorem)
**Steps:**
1. input: `s_lindemann_weierstrass` --[t_compose_with_identity {identity: "if π were algebraic then iπ algebraic, but e^{iπ} = −1 ∈ ℚ contradicts L–W"}]--> output: `s_pi_transcendental`
**Techniques used:** t_compose_with_identity

### Euler product expansion for ζ(s) (cite: https://en.wikipedia.org/wiki/Euler_product)
**Axioms:** `s_riemann_zeta_function`, `s_fundamental_theorem_of_arithmetic`
**Terminal:** `s_euler_product_zeta` (kind: theorem)
**Steps:**
1. input: `s_fundamental_theorem_of_arithmetic` --[t_compose_with_identity {identity: "geometric series 1/(1-p^{-s}) = Σ p^{-ks}"}]--> output: `s_prime_local_factor_geometric`
2. input: `s_prime_local_factor_geometric` --[t_axiomatize_from_instances {abstracted_to: "ζ(s) = ∏_p (1-p^{-s})^{-1}"}]--> output: `s_euler_product_zeta`
**Techniques used:** t_compose_with_identity, t_axiomatize_from_instances

### Functional equation of ζ(s) (Riemann) (cite: https://en.wikipedia.org/wiki/Riemann_zeta_function#The_functional_equation)
**Axioms:** `s_riemann_zeta_function`, `s_theta_function_jacobi_θ3`
**Terminal:** `s_zeta_functional_equation` (kind: theorem)
**Steps:**
1. input: `s_theta_function_jacobi_θ3` --[t_frequency_decomposition {domain: "Poisson summation on ℤ ⊂ ℝ"}]--> output: `s_theta_modular_inversion`
2. input: `s_theta_modular_inversion` --[t_complex_analysis_to_integers {object: "Mellin transform ξ(s) = π^{-s/2} Γ(s/2) ζ(s)"}]--> output: `s_completed_xi_function`
3. input: `s_completed_xi_function` --[t_symmetry_reduction {group: "s ↦ 1-s"}]--> output: `s_zeta_functional_equation`
**Techniques used:** t_frequency_decomposition, t_complex_analysis_to_integers, t_symmetry_reduction

### Riemann hypothesis equivalents (Robin, Mertens-type) (cite: https://en.wikipedia.org/wiki/Riemann_hypothesis#Equivalent_statements)
**Axioms:** `s_riemann_zeta_function`, `s_naturals_with_multiplication`
**Terminal:** `s_rh_equivalents_robin` (kind: theorem)
**Steps:**
1. input: `s_riemann_zeta_function` --[t_complex_analysis_to_integers {object: "Mertens function M(x) bound and σ(n) inequality"}]--> output: `s_mertens_and_sigma_translations`
2. input: `s_mertens_and_sigma_translations` --[t_structural_isomorphism {invariant: "RH ⟺ Robin σ(n) < e^γ n log log n for n > 5040"}]--> output: `s_rh_equivalents_robin`
**Techniques used:** t_complex_analysis_to_integers, t_structural_isomorphism

### Riemann–von Mangoldt explicit formula (cite: https://en.wikipedia.org/wiki/Explicit_formulae_(L-function))
**Axioms:** `s_riemann_zeta_function`, `s_chebyshev_function_theta_psi`
**Terminal:** `s_riemann_von_mangoldt_explicit_formula` (kind: theorem)
**Steps:**
1. input: `s_riemann_zeta_function` --[t_complex_analysis_to_integers {object: "Perron integral for ψ(x)"}]--> output: `s_perron_for_psi`
2. input: `s_perron_for_psi` --[t_compose_with_identity {identity: "ψ(x) = x − Σ_ρ x^ρ/ρ − log 2π − (1/2) log(1 − x^{-2})"}]--> output: `s_riemann_von_mangoldt_explicit_formula`
**Techniques used:** t_complex_analysis_to_integers, t_compose_with_identity

### Zero-free region (de la Vallée Poussin) (cite: https://en.wikipedia.org/wiki/Prime_number_theorem)
**Axioms:** `s_riemann_zeta_function`
**Terminal:** `s_de_la_vallee_poussin_zero_free_region` (kind: theorem)
**Steps:**
1. input: `s_riemann_zeta_function` --[t_compose_with_identity {identity: "3 + 4cos θ + cos 2θ ≥ 0 identity"}]--> output: `s_3_4_cos_trick`
2. input: `s_3_4_cos_trick` --[t_complex_analysis_to_integers {object: "ζ(σ)^3 |ζ(σ+it)|^4 |ζ(σ+2it)| ≥ 1"}]--> output: `s_de_la_vallee_poussin_zero_free_region`
**Techniques used:** t_compose_with_identity, t_complex_analysis_to_integers

### Riemann's prime-counting formula (cite: https://en.wikipedia.org/wiki/Prime-counting_function#Other_prime-counting_functions)
**Axioms:** `s_riemann_zeta_function`, `s_naturals_with_multiplication`
**Terminal:** `s_riemann_pi_x_formula` (kind: theorem)
**Steps:**
1. input: `s_riemann_zeta_function` --[t_complex_analysis_to_integers {object: "Möbius inversion of J(x) and explicit ψ formula"}]--> output: `s_j_x_inversion`
2. input: `s_j_x_inversion` --[t_compose_with_identity {identity: "π(x) = Σ μ(n)/n J(x^{1/n})"}]--> output: `s_riemann_pi_x_formula`
**Techniques used:** t_complex_analysis_to_integers, t_compose_with_identity

### Ramanujan's congruences (cite: https://en.wikipedia.org/wiki/Ramanujan%27s_congruences)
**Axioms:** `s_integer_partitions`, `s_modular_forms_holomorphic_or_maass`
**Terminal:** `s_ramanujan_partition_congruences` (kind: theorem)
**Steps:**
1. input: `s_integer_partitions` --[t_complex_analysis_to_integers {object: "1/η as weakly holomorphic modular form"}]--> output: `s_partition_generating_modular`
2. input: `s_partition_generating_modular` --[t_compose_with_identity {identity: "p(5n+4) ≡ 0 (mod 5), p(7n+5) ≡ 0 (mod 7), p(11n+6) ≡ 0 (mod 11)"}]--> output: `s_ramanujan_partition_congruences`
**Techniques used:** t_complex_analysis_to_integers, t_compose_with_identity

### Deligne's bound for τ (Ramanujan conjecture) (cite: https://en.wikipedia.org/wiki/Ramanujan%E2%80%93Petersson_conjecture)
**Axioms:** `s_modular_forms_holomorphic_or_maass`, `s_etale_cohomology`
**Terminal:** `s_deligne_tau_bound` (kind: theorem)
**Steps:**
1. input: `s_modular_forms_holomorphic_or_maass` --[t_heights_and_galois_rep_bridge {bridge: "Galois rep attached to cuspidal newform"}]--> output: `s_modular_galois_rep`
2. input: `⟨s_modular_galois_rep, s_etale_cohomology⟩` --[t_analysis_algebra_topology_bridge {bridge: "Frobenius eigenvalues from étale cohomology of Kuga–Sato variety"}]--> output: `s_frobenius_eigenvalues_modular`
3. input: `s_frobenius_eigenvalues_modular` --[t_compose_with_identity {identity: "|τ(p)| ≤ 2 p^{11/2}"}]--> output: `s_deligne_tau_bound`
**Techniques used:** t_heights_and_galois_rep_bridge, t_analysis_algebra_topology_bridge, t_compose_with_identity

### Selberg trace formula (cite: https://en.wikipedia.org/wiki/Selberg_trace_formula)
**Axioms:** `s_hyperbolic_surface`, `s_modular_forms_holomorphic_or_maass`
**Terminal:** `s_selberg_trace_formula` (kind: theorem)
**Steps:**
1. input: `s_hyperbolic_surface` --[t_character_decomposition_count {basis: "Maass-form spectrum + Eisenstein continuous spectrum"}]--> output: `s_spectral_side_decomposition`
2. input: `s_spectral_side_decomposition` --[t_duality {pair: "spectral ↔ length spectrum (closed geodesics)"}]--> output: `s_spectral_length_duality`
3. input: `s_spectral_length_duality` --[t_compose_with_identity {identity: "Σ h(r_j) = (vol/4π)∫h(r)r tanh(πr) dr + Σ_{γ} ĝ(ℓ_γ)/(2 sinh(ℓ_γ/2))"}]--> output: `s_selberg_trace_formula`
**Techniques used:** t_character_decomposition_count, t_duality, t_compose_with_identity

### Arthur–Selberg trace formula (overview) (cite: https://en.wikipedia.org/wiki/Arthur%E2%80%93Selberg_trace_formula)
**Axioms:** `s_reductive_algebraic_group`, `s_adeles_a`
**Terminal:** `s_arthur_selberg_trace_formula` (kind: theorem)
**Steps:**
1. input: `s_reductive_algebraic_group` --[t_character_decomposition_count {basis: "automorphic spectrum of L²(G(ℚ)\\G(𝔸))"}]--> output: `s_automorphic_spectral_side`
2. input: `s_automorphic_spectral_side` --[t_duality {pair: "spectral ↔ unipotent + elliptic + parabolic geometric side"}]--> output: `s_geometric_side_decomposition`
3. input: `s_geometric_side_decomposition` --[t_compose_with_identity {identity: "spectral side = geometric side with weighted orbital integrals"}]--> output: `s_arthur_selberg_trace_formula`
**Techniques used:** t_character_decomposition_count, t_duality, t_compose_with_identity

### Langlands functoriality (transferring from one group to another — known cases, e.g. Arthur for classical groups) (cite: https://en.wikipedia.org/wiki/Langlands_program)
**Axioms:** `s_reductive_algebraic_group`, `s_automorphic_representation`
**Terminal:** `s_langlands_functoriality_known_cases` (kind: theorem)
**Steps:**
1. input: `s_automorphic_representation` --[t_axiomatize_from_instances {abstracted_to: "L-group homomorphism ^LH → ^LG"}]--> output: `s_l_group_functoriality_setup`
2. input: `s_l_group_functoriality_setup` --[t_compose_with_identity {identity: "Arthur classification for classical groups transfers automorphic forms"}]--> output: `s_langlands_functoriality_known_cases`
**Techniques used:** t_axiomatize_from_instances, t_compose_with_identity

### Local Langlands for GL_n (cite: https://en.wikipedia.org/wiki/Local_Langlands_conjectures)
**Axioms:** `s_local_field_k`, `s_galois_representation_residual`
**Terminal:** `s_local_langlands_gl_n` (kind: theorem)
**Steps:**
1. input: `s_local_field_k` --[t_heights_and_galois_rep_bridge {bridge: "Weil–Deligne representations of W_K"}]--> output: `s_weil_deligne_rep_side`
2. input: `s_weil_deligne_rep_side` --[t_structural_isomorphism {invariant: "bijection with irreducible admissible smooth GL_n(K)-reps"}]--> output: `s_local_langlands_gl_n`
**Techniques used:** t_heights_and_galois_rep_bridge, t_structural_isomorphism

### Global Langlands for GL_n over function fields (Lafforgue) (cite: https://en.wikipedia.org/wiki/Langlands_program#Function_field_analogue)
**Axioms:** `s_function_field_over_fq`, `s_automorphic_representation`
**Terminal:** `s_lafforgue_global_langlands_function_field` (kind: theorem)
**Steps:**
1. input: `s_function_field_over_fq` --[t_heights_and_galois_rep_bridge {bridge: "ℓ-adic representations from étale cohomology of Drinfeld shtukas"}]--> output: `s_shtuka_cohomology_galois_reps`
2. input: `s_shtuka_cohomology_galois_reps` --[t_axiomatize_from_instances {abstracted_to: "automorphic for GL_n ↔ irreducible n-dim Galois reps with bounded ramification"}]--> output: `s_lafforgue_global_langlands_function_field`
**Techniques used:** t_heights_and_galois_rep_bridge, t_axiomatize_from_instances

### Carmichael's theorem (orders) (cite: https://en.wikipedia.org/wiki/Carmichael%27s_theorem)
**Axioms:** `s_naturals_with_multiplication`, `s_lucas_sequence`
**Terminal:** `s_carmichael_theorem_orders` (kind: theorem)
**Steps:**
1. input: `s_lucas_sequence` --[t_compose_with_identity {identity: "primitive divisor existence for U_n beyond n ≤ 12"}]--> output: `s_primitive_divisor_existence`
2. input: `s_primitive_divisor_existence` --[t_axiomatize_from_instances {abstracted_to: "every term of nondegenerate Lucas sequence (n>12) has a primitive prime divisor"}]--> output: `s_carmichael_theorem_orders`
**Techniques used:** t_compose_with_identity, t_axiomatize_from_instances

### Zsigmondy's theorem (cite: https://en.wikipedia.org/wiki/Zsigmondy%27s_theorem)
**Axioms:** `s_naturals_with_multiplication`, `s_cyclotomic_polynomial_phi_n`
**Terminal:** `s_zsigmondy_theorem` (kind: theorem)
**Steps:**
1. input: `s_cyclotomic_polynomial_phi_n` --[t_reduce_to_canonical_form {form: "a^n − b^n = ∏ Φ_d(a,b)"}]--> output: `s_lifting_exponent_factor_decomposition`
2. input: `s_lifting_exponent_factor_decomposition` --[t_axiomatize_from_instances {abstracted_to: "a^n − b^n has a prime divisor not dividing any a^k − b^k for k < n, with explicit exceptions"}]--> output: `s_zsigmondy_theorem`
**Techniques used:** t_reduce_to_canonical_form, t_axiomatize_from_instances

### Lamé's theorem on Euclidean algorithm (cite: https://en.wikipedia.org/wiki/Lam%C3%A9%27s_theorem)
**Axioms:** `s_integers`, `s_fibonacci_numbers`
**Terminal:** `s_lame_euclidean_algorithm_bound` (kind: theorem)
**Steps:**
1. input: `s_integers` --[t_compose_with_identity {identity: "worst case of GCD is consecutive Fibonacci numbers"}]--> output: `s_worst_case_consecutive_fibs`
2. input: `⟨s_worst_case_consecutive_fibs, s_fibonacci_numbers⟩` --[t_axiomatize_from_instances {abstracted_to: "Euclidean algorithm terminates in O(log_φ(min(a,b))) steps"}]--> output: `s_lame_euclidean_algorithm_bound`
**Techniques used:** t_compose_with_identity, t_axiomatize_from_instances

### Midy's theorem (cite: https://en.wikipedia.org/wiki/Midy%27s_theorem)
**Axioms:** `s_rationals_q`, `s_decimal_expansion_repetend`
**Terminal:** `s_midy_theorem` (kind: theorem)
**Steps:**
1. input: `s_decimal_expansion_repetend` --[t_symmetry_reduction {group: "halving the repetend"}]--> output: `s_two_halves_of_repetend`
2. input: `s_two_halves_of_repetend` --[t_compose_with_identity {identity: "halves sum to 10^{k/2} − 1"}]--> output: `s_midy_theorem`
**Techniques used:** t_symmetry_reduction, t_compose_with_identity

### Beatty's theorem (cite: https://en.wikipedia.org/wiki/Beatty_sequence)
**Axioms:** `s_reals_with_topology`, `s_naturals_with_multiplication`
**Terminal:** `s_beatty_theorem` (kind: theorem)
**Steps:**
1. input: `s_reals_with_topology` --[t_axiomatize_from_instances {abstracted_to: "positive irrationals r, s with 1/r + 1/s = 1"}]--> output: `s_complementary_irrationals_pair`
2. input: `s_complementary_irrationals_pair` --[t_exhaustion_squeeze {lower: "count {⌊nr⌋} below N", upper: "count {⌊ns⌋} below N"}]--> output: `s_beatty_partition_count_match`
3. input: `s_beatty_partition_count_match` --[t_compose_with_identity {identity: "ℕ⁺ = {⌊nr⌋} ⊔ {⌊ns⌋}"}]--> output: `s_beatty_theorem`
**Techniques used:** t_axiomatize_from_instances, t_exhaustion_squeeze, t_compose_with_identity

### Davenport–Schmidt theorem (cite: https://en.wikipedia.org/wiki/Davenport%E2%80%93Schmidt_theorem)
**Axioms:** `s_algebraic_number_alpha`, `s_continued_fraction_expansion`
**Terminal:** `s_davenport_schmidt_theorem` (kind: theorem)
**Steps:**
1. input: `s_algebraic_number_alpha` --[t_compose_with_identity {identity: "approximation by quadratic irrationals analog of Roth"}]--> output: `s_quadratic_approximation_bounds`
2. input: `s_quadratic_approximation_bounds` --[t_axiomatize_from_instances {abstracted_to: "best approximation by algebraic α of degree ≤ d to non-algebraic ξ"}]--> output: `s_davenport_schmidt_theorem`
**Techniques used:** t_compose_with_identity, t_axiomatize_from_instances

### Lehmer pair / Lehmer's conjecture (Mahler measure) — Smyth's theorem on non-reciprocal polynomials (cite: https://en.wikipedia.org/wiki/Mahler_measure)
**Axioms:** `s_polynomial_ring_z_x`, `s_mahler_measure_function`
**Terminal:** `s_smyth_lower_bound_non_reciprocal` (kind: theorem)
**Steps:**
1. input: `s_mahler_measure_function` --[t_compose_with_identity {identity: "for non-reciprocal integer polynomials, M(P) ≥ Lehmer-style θ_0 ≈ 1.32"}]--> output: `s_smyth_lower_bound_non_reciprocal`
**Techniques used:** t_compose_with_identity

### Stickelberger's theorem (cite: https://en.wikipedia.org/wiki/Stickelberger%27s_theorem)
**Axioms:** `s_cyclotomic_field_q_zeta_p`, `s_class_group`
**Terminal:** `s_stickelberger_theorem` (kind: theorem)
**Steps:**
1. input: `s_cyclotomic_field_q_zeta_p` --[t_auxiliary_construction {object: "Stickelberger element θ ∈ ℚ[Gal]"}]--> output: `s_stickelberger_element`
2. input: `s_stickelberger_element` --[t_compose_with_identity {identity: "θ annihilates the ideal class group of ℚ(ζ_n)"}]--> output: `s_stickelberger_theorem`
**Techniques used:** t_auxiliary_construction, t_compose_with_identity

### Hilbert's Theorem 90 (cite: https://en.wikipedia.org/wiki/Hilbert%27s_Theorem_90)
**Axioms:** `s_galois_extension_l_over_k`, `s_cyclic_galois_group`
**Terminal:** `s_hilbert_90` (kind: theorem)
**Steps:**
1. input: `s_galois_extension_l_over_k` --[t_galois_correspondence {field_tower: "cyclic L/K with generator σ"}]--> output: `s_galois_action_on_units`
2. input: `s_galois_action_on_units` --[t_compose_with_identity {identity: "H¹(Gal(L/K), L*) = 0 ⟺ norm-1 elements are σ(β)/β"}]--> output: `s_hilbert_90`
**Techniques used:** t_galois_correspondence, t_compose_with_identity

### Artin reciprocity (cite: https://en.wikipedia.org/wiki/Artin_reciprocity)
**Axioms:** `s_abelian_extension_of_number_field`, `s_idele_class_group`
**Terminal:** `s_artin_reciprocity_law` (kind: theorem)
**Steps:**
1. input: `s_idele_class_group` --[t_axiomatize_from_instances {abstracted_to: "global reciprocity map θ_K: C_K → Gal(K^{ab}/K)"}]--> output: `s_global_reciprocity_map`
2. input: `s_global_reciprocity_map` --[t_structural_isomorphism {invariant: "θ_K continuous surjection with kernel = connected component of identity"}]--> output: `s_artin_reciprocity_law`
**Techniques used:** t_axiomatize_from_instances, t_structural_isomorphism

### Local class field theory (cite: https://en.wikipedia.org/wiki/Local_class_field_theory)
**Axioms:** `s_local_field_k`, `s_lubin_tate_formal_group`
**Terminal:** `s_local_class_field_theory` (kind: theorem)
**Steps:**
1. input: `s_local_field_k` --[t_galois_correspondence {field_tower: "K^{ab}/K with Galois group ≅ K̂^×"}]--> output: `s_local_reciprocity_isomorphism`
2. input: `⟨s_local_reciprocity_isomorphism, s_lubin_tate_formal_group⟩` --[t_compose_with_identity {identity: "totally ramified part built via Lubin–Tate formal groups"}]--> output: `s_local_class_field_theory`
**Techniques used:** t_galois_correspondence, t_compose_with_identity

### Kronecker–Weber theorem (cite: https://en.wikipedia.org/wiki/Kronecker%E2%80%93Weber_theorem)
**Axioms:** `s_abelian_extension_of_number_field`, `s_cyclotomic_field_q_zeta_p`
**Terminal:** `s_kronecker_weber_theorem` (kind: theorem)
**Steps:**
1. input: `s_abelian_extension_of_number_field` --[t_galois_correspondence {field_tower: "ramification analysis at each prime"}]--> output: `s_local_kronecker_weber_components`
2. input: `s_local_kronecker_weber_components` --[t_compose_with_identity {identity: "every abelian extension of ℚ lies in some Q(ζ_n)"}]--> output: `s_kronecker_weber_theorem`
**Techniques used:** t_galois_correspondence, t_compose_with_identity

### Chebotarev with effective bound under GRH (cite: https://en.wikipedia.org/wiki/Chebotarev%27s_density_theorem#Effective_version) — extends `s_chebotarev_density`
**Axioms:** `s_galois_extension_l_over_k`, `s_grh_for_dedekind_zeta`
**Terminal:** `s_chebotarev_effective_grh` (kind: theorem)
**Steps:**
1. input: `⟨s_galois_extension_l_over_k, s_grh_for_dedekind_zeta⟩` --[t_complex_analysis_to_integers {object: "zero-density estimate for Hecke L"}]--> output: `s_grh_zero_density_input`
2. input: `s_grh_zero_density_input` --[t_compose_with_identity {identity: "π_C(x,L/K) = |C|/|G| · Li(x) + O(|C|/|G| · √x · log(disc_L · x))"}]--> output: `s_chebotarev_effective_grh`
**Techniques used:** t_complex_analysis_to_integers, t_compose_with_identity

### Equidistribution of n·α mod 1 (Weyl) (cite: https://en.wikipedia.org/wiki/Equidistribution_theorem)
**Axioms:** `s_reals_with_topology`, `s_circle_t_1`
**Terminal:** `s_weyl_equidistribution` (kind: theorem)
**Steps:**
1. input: `s_circle_t_1` --[t_frequency_decomposition {domain: "Fourier basis on 𝕋¹"}]--> output: `s_weyl_criterion_fourier`
2. input: `s_weyl_criterion_fourier` --[t_compose_with_identity {identity: "geometric sum Σ e^{2πi k n α} bounded for irrational α"}]--> output: `s_weyl_equidistribution`
**Techniques used:** t_frequency_decomposition, t_compose_with_identity

### Weyl's polynomial equidistribution (cite: https://en.wikipedia.org/wiki/Weyl_equidistribution)
**Axioms:** `s_polynomial_ring_z_x`, `s_circle_t_1`
**Terminal:** `s_weyl_polynomial_equidistribution` (kind: theorem)
**Steps:**
1. input: `s_polynomial_ring_z_x` --[t_compose_with_identity {identity: "Weyl differencing reduces degree"}]--> output: `s_weyl_differencing_reduction`
2. input: `s_weyl_differencing_reduction` --[t_axiomatize_from_instances {abstracted_to: "{p(n) mod 1} is equidistributed iff at least one non-constant coefficient is irrational"}]--> output: `s_weyl_polynomial_equidistribution`
**Techniques used:** t_compose_with_identity, t_axiomatize_from_instances

### Three-distance / Sárközy-on-squares (cite: https://en.wikipedia.org/wiki/S%C3%A1rk%C3%B6zy%27s_theorem)
**Axioms:** `s_naturals_with_multiplication`, `s_finite_subset_a_in_z`
**Terminal:** `s_sarkozy_theorem_squares` (kind: theorem)
**Steps:**
1. input: `s_finite_subset_a_in_z` --[t_frequency_decomposition {domain: "Fourier analysis on ℤ/Nℤ with weight 1_{squares}"}]--> output: `s_squares_fourier_input`
2. input: `s_squares_fourier_input` --[t_compose_with_identity {identity: "positive-density set in [N] contains x, x+k² for some k > 0"}]--> output: `s_sarkozy_theorem_squares`
**Techniques used:** t_frequency_decomposition, t_compose_with_identity

### Furstenberg correspondence — application to NT (already a composite in graph) — record specific NT use:

### Behrend's construction of dense 3-AP-free set (cite: https://en.wikipedia.org/wiki/Salem%E2%80%93Spencer_set)
**Axioms:** `s_finite_subset_a_in_z`, `s_high_dimensional_sphere`
**Terminal:** `s_behrend_3_ap_free_set` (kind: theorem)
**Steps:**
1. input: `s_high_dimensional_sphere` --[t_raise_dimension {dimension: "embed [N] via base-b digits into ℤ^d"}]--> output: `s_high_dim_sphere_lattice_layer`
2. input: `s_high_dim_sphere_lattice_layer` --[t_compose_with_identity {identity: "sphere is convex ⇒ no 3-term AP on sphere ⇒ inverse-image is 3-AP-free with size N/exp(c√log N)"}]--> output: `s_behrend_3_ap_free_set`
**Techniques used:** t_raise_dimension, t_compose_with_identity

### Bloom–Sisask on Roth (cite: https://en.wikipedia.org/wiki/Roth%27s_theorem_on_arithmetic_progressions)
**Axioms:** `s_finite_subset_a_in_z`
**Terminal:** `s_bloom_sisask_roth_bound` (kind: theorem)
**Steps:**
1. input: `s_finite_subset_a_in_z` --[t_frequency_decomposition {domain: "Bohr-set + density-increment"}]--> output: `s_bohr_density_increment`
2. input: `s_bohr_density_increment` --[t_compose_with_identity {identity: "r_3(N) ≪ N / (log N)^{1+c}"}]--> output: `s_bloom_sisask_roth_bound`
**Techniques used:** t_frequency_decomposition, t_compose_with_identity

### Gowers norms and inverse theorem (cite: https://en.wikipedia.org/wiki/Gowers_norm)
**Axioms:** `s_finite_abelian_group_zn`, `s_function_f_g_to_c`
**Terminal:** `s_gowers_inverse_theorem` (kind: theorem)
**Steps:**
1. input: `s_function_f_g_to_c` --[t_frequency_decomposition {domain: "U^k norm via box-and-difference"}]--> output: `s_gowers_uk_definition`
2. input: `s_gowers_uk_definition` --[t_structural_isomorphism {invariant: "large U^{k+1} norm ⟺ correlation with degree-k nilsequence"}]--> output: `s_gowers_inverse_theorem`
**Techniques used:** t_frequency_decomposition, t_structural_isomorphism

### Szemerédi–Trotter incidence theorem (cite: https://en.wikipedia.org/wiki/Szemer%C3%A9di%E2%80%93Trotter_theorem)
**Axioms:** `s_points_in_plane`, `s_lines_in_plane`
**Terminal:** `s_szemeredi_trotter_incidences` (kind: theorem)
**Steps:**
1. input: `⟨s_points_in_plane, s_lines_in_plane⟩` --[t_polynomial_method {form: "cell decomposition by polynomial of degree ≈ (m+n)^{1/2}"}]--> output: `s_cell_decomposition_of_plane`
2. input: `s_cell_decomposition_of_plane` --[t_compose_with_identity {identity: "I(m,n) ≪ (mn)^{2/3} + m + n"}]--> output: `s_szemeredi_trotter_incidences`
**Techniques used:** t_polynomial_method, t_compose_with_identity

### Erdős distinct-distances (Guth–Katz) (cite: https://en.wikipedia.org/wiki/Erd%C5%91s_distinct_distances_problem)
**Axioms:** `s_points_in_plane`, `s_lines_in_r3_as_ruled_surfaces`
**Terminal:** `s_guth_katz_distinct_distances` (kind: theorem)
**Steps:**
1. input: `s_points_in_plane` --[t_polynomial_method {form: "Elekes–Sharir transform + Cayley–Salmon on doubly-ruled surfaces"}]--> output: `s_elekes_sharir_lines_in_r3`
2. input: `s_elekes_sharir_lines_in_r3` --[t_compose_with_identity {identity: "distinct distances of n points ≫ n/log n"}]--> output: `s_guth_katz_distinct_distances`
**Techniques used:** t_polynomial_method, t_compose_with_identity

### Erdős–Szemerédi sum–product (cite: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Szemer%C3%A9di_theorem)
**Axioms:** `s_finite_subset_a_in_z`
**Terminal:** `s_erdos_szemeredi_sum_product` (kind: theorem)
**Steps:**
1. input: `s_finite_subset_a_in_z` --[t_compose_with_identity {identity: "max(|A+A|,|A·A|) ≥ |A|^{1+c}"}]--> output: `s_sum_product_basic_bound`
2. input: `s_sum_product_basic_bound` --[t_polynomial_method {form: "elekes-style point–line via incidences"}]--> output: `s_erdos_szemeredi_sum_product`
**Techniques used:** t_compose_with_identity, t_polynomial_method

### Three-distance theorem (Steinhaus, distinct from three-gap) (cite: https://en.wikipedia.org/wiki/Three-distance_theorem)
**Axioms:** `s_reals_with_topology`, `s_circle_t_1`
**Terminal:** `s_three_distance_theorem` (kind: theorem)
**Steps:**
1. input: `s_circle_t_1` --[t_symmetry_reduction {group: "ℤ-action by rotation"}]--> output: `s_circle_orbit_partition`
2. input: `s_circle_orbit_partition` --[t_compose_with_identity {identity: "at most 3 distinct arc lengths among first N points"}]--> output: `s_three_distance_theorem`
**Techniques used:** t_symmetry_reduction, t_compose_with_identity

### Khintchine's theorem on Diophantine approximation (cite: https://en.wikipedia.org/wiki/Khinchin%27s_theorem_on_Diophantine_approximation)
**Axioms:** `s_reals_with_topology`, `s_borel_cantelli_lemma`
**Terminal:** `s_khintchine_diophantine_theorem` (kind: theorem)
**Steps:**
1. input: `s_reals_with_topology` --[t_probabilistic_existence {distribution: "Lebesgue measure on [0,1]"}]--> output: `s_random_alpha_uniform`
2. input: `⟨s_random_alpha_uniform, s_borel_cantelli_lemma⟩` --[t_compose_with_identity {identity: "Σ ψ(q)·q diverges ⇒ |α − p/q| < ψ(q)/q infinitely often a.s."}]--> output: `s_khintchine_diophantine_theorem`
**Techniques used:** t_probabilistic_existence, t_compose_with_identity

### Davenport–Erdős theorem on multiples (cite: https://en.wikipedia.org/wiki/Davenport%E2%80%93Erd%C5%91s_theorem)
**Axioms:** `s_naturals_with_multiplication`
**Terminal:** `s_davenport_erdos_density_multiples` (kind: theorem)
**Steps:**
1. input: `s_naturals_with_multiplication` --[t_axiomatize_from_instances {abstracted_to: "set of multiples M(A) has logarithmic density = lower asymptotic density"}]--> output: `s_density_equality_for_multiples_sets`
2. input: `s_density_equality_for_multiples_sets` --[t_compose_with_identity {identity: "M(A) has equal lower and logarithmic density"}]--> output: `s_davenport_erdos_density_multiples`
**Techniques used:** t_axiomatize_from_instances, t_compose_with_identity

### Schinzel hypothesis H — note as conjecture, omit
### Bunyakovsky conjecture — note as conjecture, omit

---

## End of file. Drafted 86 chains across elementary, multiplicative, analytic, transcendence, arithmetic-geometry, additive-combinatorial NT slices. Skipped 13 already-in-graph theorems. Flagged 0 `⚠ needs new technique`.
