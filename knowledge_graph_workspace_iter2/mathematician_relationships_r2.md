# Mathematician's Relationships — Iteration 2 (Mathematician B)

Deep-dive derivation chains for the chapters 03–04 theorems missing from iter-1. Format is identical to iter-1's `mathematician_relationships.md`: `--[t_technique {param: value}]--> s_state`, with `⟨s_a, s_b⟩` for multi-input arrows, and `⚠ not in toolbox` where no entry fits.

Existing canonical ids (from `canonical_node_index.md`) are reused verbatim. New state ids (prefixed `s_`) are listed at the bottom of this file.

Ch. 11 §6 corrections applied: where iter-1 would have written `t_infinite_descent` for "assume, derive contradiction" with no descending integer measure, this file instead writes `t_reductio_ad_absurdum`; where iter-1 would have written `t_analysis_algebra_topology_bridge` for a specialization, the appropriate bridge node (`t_sheaf_cohomology_bridge`, `t_heights_and_galois_rep_bridge`, `t_level_lowering_bridge`, `t_transference_bridge`, `t_k_theoretic_index_bridge`) is used. Auxiliary constructions (Frey curve, resolvent cubic, Chevalier's helper function g(x)) that are *not* projections or completions are tagged with `t_auxiliary_construction`. Linear / Hilbert-space projections onto a subspace use `t_projection_to_subspace`. Diagonalizations of matrices and operators (as opposed to Cantor / halting-problem diagonalization) use `t_svd_and_spectral_decomposition`.

---

## Chapter 3 — Eighteenth Century (new chains)

### Bernoulli's Law of Large Numbers (Ch. 3)

**Axiom / starting states:** `s_probability_axioms`, `s_iid_sequence_finite_variance`
**Terminal theorem state:** `s_bernoulli_lln` (kind: theorem)

**Steps:**
1. input: `s_iid_sequence_finite_variance` --[t_reduce_to_canonical_form {binomial tail: each Xᵢ ~ Bernoulli(p), sum is Binomial(n,p)}]--> output: `s_binomial_tail_ratios`
2. input: `s_binomial_tail_ratios` --[t_pigeonhole_collision {bound peak/tail ratios of C(n,k) to squeeze P(|Xₙ−p| ≥ ε)}]--> output: `s_binomial_tail_bound`
3. input: `s_binomial_tail_bound` --[t_exhaustion_squeeze {n → ∞: tail probability vanishes}]--> output: `s_bernoulli_lln`

**Techniques used:** 4 reduceToCanonicalForm; 30 pigeonholeCollision; 9 exhaustionSqueeze

---

### De Moivre–Laplace Theorem (Ch. 3)

**Axiom / starting states:** `s_probability_axioms`, `s_iid_sequence_finite_variance`, `s_analytic_exponential_series`
**Terminal theorem state:** `s_de_moivre_laplace` (kind: theorem)

**Steps:**
1. input: `s_iid_sequence_finite_variance` --[t_reduce_to_canonical_form {central-term binomial C(n,n/2)(1/2)ⁿ via Stirling}]--> output: `s_stirling_central_term_asymptotic`
2. input: `s_stirling_central_term_asymptotic` --[t_interpolate_and_continue {Taylor-expand log of ratio of k-th to central term in k − np}]--> output: `s_gaussian_density_as_limit`
3. input: `s_gaussian_density_as_limit` --[t_exhaustion_squeeze {integrate the limiting density; sums → ∫ e^{−t²/2} dt / √(2π)}]--> output: `s_de_moivre_laplace`

**Techniques used:** 4 reduceToCanonicalForm; 10 interpolateAndContinue; 9 exhaustionSqueeze

---

### Euler's Totient Theorem (Ch. 3)

**Axiom / starting states:** `s_integers`, `s_coprime_pair`, `s_fermat_little_theorem`
**Terminal theorem state:** `s_euler_totient_theorem` (kind: theorem)

**Steps:**
1. input: `s_integers` --[t_axiomatize_from_instances {unit residues mod n: (ℤ/nℤ)*}]--> output: `s_unit_group_mod_n`
2. input: `⟨s_unit_group_mod_n, s_coprime_pair⟩` --[t_symmetry_reduction {multiplication-by-a is a bijection on (ℤ/nℤ)*}]--> output: `s_orbit_of_a_mod_n`
3. input: `s_orbit_of_a_mod_n` --[t_conserved_quantity {product of all units is invariant under multiplication by a; cancel to get a^φ(n) ≡ 1}]--> output: `s_euler_totient_theorem`

**Techniques used:** 12 axiomatizeFromInstances; 6 symmetryReduction; 7 conservedQuantity

---

### Euler's Theorem on Homogeneous Functions (Ch. 3)

**Axiom / starting states:** `s_smooth_function`, `s_real_line`
**Terminal theorem state:** `s_euler_homogeneous_functions` (kind: theorem)

**Steps:**
1. input: `s_smooth_function` --[t_axiomatize_from_instances {defining identity f(tx)=tᵏf(x) ∀ t>0}]--> output: `s_homogeneous_function_definition`
2. input: `s_homogeneous_function_definition` --[t_symmetry_reduction {one-parameter scaling group ℝ₊ acting by dilation}]--> output: `s_scaling_vector_field_identity`
3. input: `s_scaling_vector_field_identity` --[t_conserved_quantity {infinitesimal generator: d/dt|_{t=1} of both sides yields Σ xᵢ ∂f/∂xᵢ = k·f}]--> output: `s_euler_homogeneous_functions`

**Techniques used:** 12 axiomatizeFromInstances; 6 symmetryReduction; 7 conservedQuantity

---

### Lagrange's Mean Value Theorem (Ch. 3)

**Axiom / starting states:** `s_real_line`, `s_continuous_function_on_interval`, `s_smooth_function`
**Terminal theorem state:** `s_lagrange_mvt` (kind: theorem)

**Steps:**
1. input: `s_continuous_function_on_interval` --[t_auxiliary_construction {g(x) = f(x) − [(f(b)−f(a))/(b−a)](x − a) so g(a) = g(b)}]--> output: `s_auxiliary_function_with_equal_endpoints`
2. input: `s_auxiliary_function_with_equal_endpoints` --[t_compactness_argument {continuous on compact [a,b] attains max/min in (a,b) ⇒ Rolle: ∃ c with g'(c) = 0}]--> output: `s_rolle_interior_critical_point`
3. input: `s_rolle_interior_critical_point` --[t_compose_with_identity {g'(c) = 0 ⇒ f'(c) = (f(b) − f(a))/(b − a)}]--> output: `s_lagrange_mvt`

**Techniques used:** C2 auxiliaryConstruction; 16 compactnessArgument; 5 composeWithIdentity

---

### Wilson's Theorem (Ch. 3)

**Axiom / starting states:** `s_integers`, `s_prime_p`, `s_fermat_little_theorem`
**Terminal theorem state:** `s_wilson_theorem` (kind: theorem)

**Steps:**
1. input: `⟨s_fermat_little_theorem, s_prime_p⟩` --[t_auxiliary_construction {view x^(p−1) − 1 ∈ 𝔽_p[x]; Fermat says all of 1,…,p−1 are roots}]--> output: `s_polynomial_x_p_minus_1_factored_mod_p`
2. input: `s_polynomial_x_p_minus_1_factored_mod_p` --[t_reduce_to_canonical_form {over the field 𝔽_p a degree-(p−1) poly has at most p−1 roots ⇒ x^(p−1) − 1 ≡ ∏(x − k)}]--> output: `s_factored_form_of_cyclic_unit_polynomial`
3. input: `s_factored_form_of_cyclic_unit_polynomial` --[t_compose_with_identity {evaluate at x = 0 and collect signs: −1 ≡ (p−1)! (mod p)}]--> output: `s_wilson_theorem`

**Techniques used:** C2 auxiliaryConstruction; 4 reduceToCanonicalForm; 5 composeWithIdentity

---

### Bayes's Theorem (Ch. 3)

**Axiom / starting states:** `s_probability_axioms`
**Terminal theorem state:** `s_bayes_theorem` (kind: theorem)

**Steps:**
1. input: `s_probability_axioms` --[t_axiomatize_from_instances {conditional probability: P(A | B) := P(A ∩ B)/P(B)}]--> output: `s_conditional_probability_definition`
2. input: `s_conditional_probability_definition` --[t_duality {swap roles of A and B: P(A∩B) = P(A|B)P(B) = P(B|A)P(A)}]--> output: `s_symmetric_chain_rule_for_intersection`
3. input: `s_symmetric_chain_rule_for_intersection` --[t_compose_with_identity {divide through by P(B)}]--> output: `s_bayes_theorem`

**Techniques used:** 12 axiomatizeFromInstances; 8 duality; 5 composeWithIdentity

---

## Chapter 4 — Nineteenth Century (new chains)

### Cauchy–Schwarz Inequality (Ch. 4)

**Axiom / starting states:** `s_real_vector_space`, `s_L2_function_space`
**Terminal theorem state:** `s_cauchy_schwarz` (kind: theorem)

**Steps:**
1. input: `s_real_vector_space` --[t_axiomatize_from_instances {inner product ⟨·,·⟩ with positivity ⟨v,v⟩ ≥ 0}]--> output: `s_inner_product_space`
2. input: `s_inner_product_space` --[t_auxiliary_construction {the non-negative quadratic Q(t) = ‖u − tv‖² = ‖u‖² − 2t⟨u,v⟩ + t²‖v‖²}]--> output: `s_non_negative_quadratic_in_t`
3. input: `s_non_negative_quadratic_in_t` --[t_complete_the_square {minimize at t = ⟨u,v⟩/‖v‖²; non-negativity of min ⇒ discriminant ≤ 0}]--> output: `s_cauchy_schwarz`

**Techniques used:** 12 axiomatizeFromInstances; C2 auxiliaryConstruction; 3 completeTheSquare

---

### Bolzano's Intermediate Value Theorem (Ch. 4)

**Axiom / starting states:** `s_real_numbers`, `s_continuous_function_on_closed_interval`
**Terminal theorem state:** `s_bolzano_ivt` (kind: theorem)

**Steps:**
1. input: `s_continuous_function_on_closed_interval` --[t_auxiliary_construction {S = {x ∈ [a,b] : f(x) < 0}; non-empty and bounded above}]--> output: `s_supremum_set_S`
2. input: `s_supremum_set_S` --[t_compactness_argument {completeness of ℝ ⇒ c = sup S exists in [a,b]}]--> output: `s_candidate_root_c_as_sup`
3. input: `s_candidate_root_c_as_sup` --[t_reductio_ad_absurdum {if f(c) > 0 or f(c) < 0, continuity gives neighbourhood violating sup property ⇒ f(c) = 0}]--> output: `s_bolzano_ivt`

**Techniques used:** C2 auxiliaryConstruction; 16 compactnessArgument; C7 reductioAdAbsurdum

---

### Bolzano–Weierstrass Theorem (Ch. 4)

**Axiom / starting states:** `s_real_numbers`, `s_bounded_sequence_in_Rn`
**Terminal theorem state:** `s_bolzano_weierstrass` (kind: theorem)

**Steps:**
1. input: `s_bounded_sequence_in_Rn` --[t_reduce_to_canonical_form {enclose in a closed box [a,b]ⁿ; treat coordinate-by-coordinate}]--> output: `s_bounded_sequence_in_closed_box`
2. input: `s_bounded_sequence_in_closed_box` --[t_pigeonhole_collision {halve interval; one half holds infinitely many terms; iterate}]--> output: `s_nested_intervals_with_infinitely_many_terms`
3. input: `s_nested_intervals_with_infinitely_many_terms` --[t_compactness_argument {nested-interval theorem + diagonal selection ⇒ convergent subsequence}]--> output: `s_bolzano_weierstrass`

**Techniques used:** 4 reduceToCanonicalForm; 30 pigeonholeCollision; 16 compactnessArgument

---

### Green's Theorem (Ch. 4)

**Axiom / starting states:** `s_euclidean_plane`, `s_smooth_function`, `s_differential_form`
**Terminal theorem state:** `s_greens_theorem` (kind: theorem)

**Steps:**
1. input: `s_euclidean_plane` --[t_reduce_to_canonical_form {decompose region D into vertically- and horizontally-simple sub-regions}]--> output: `s_simple_region_decomposition_in_R2`
2. input: `s_simple_region_decomposition_in_R2` --[t_exhaustion_squeeze {Fubini + fundamental theorem of calculus on each slice}]--> output: `s_per_slice_ftoc_identity`
3. input: `s_per_slice_ftoc_identity` --[t_duality {boundary vs. interior: interior edges cancel in pairs; ∫∫(∂Q/∂x − ∂P/∂y)dA = ∮(P dx + Q dy)}]--> output: `s_greens_theorem`

**Techniques used:** 4 reduceToCanonicalForm; 9 exhaustionSqueeze; 8 duality

---

### Divergence Theorem / Gauss–Ostrogradsky (Ch. 4)

**Axiom / starting states:** `s_euclidean_3_space`, `s_smooth_function`, `s_differential_form`
**Terminal theorem state:** `s_divergence_theorem` (kind: theorem)

**Steps:**
1. input: `s_euclidean_3_space` --[t_reduce_to_canonical_form {decompose V into z-simple sub-regions g(x,y) ≤ z ≤ h(x,y)}]--> output: `s_z_simple_region_decomposition_in_R3`
2. input: `s_z_simple_region_decomposition_in_R3` --[t_exhaustion_squeeze {Fubini + FTOC on z-slice: ∫∂F₃/∂z dV reduces to top/bottom flux}]--> output: `s_per_axis_flux_identity`
3. input: `s_per_axis_flux_identity` --[t_duality {symmetric x-, y-, z-axis contributions + cancellation of interior faces ⇒ ∫∫∫∇·F dV = ∫∫_{∂V} F·dS}]--> output: `s_divergence_theorem`

**Techniques used:** 4 reduceToCanonicalForm; 9 exhaustionSqueeze; 8 duality

---

### Liouville's Theorem (complex analysis) (Ch. 4)

**Axiom / starting states:** `s_complex_numbers`, `s_holomorphic_function_on_domain`, `s_cauchy_integral_formula`
**Terminal theorem state:** `s_liouville_bounded_entire` (kind: theorem)

**Steps:**
1. input: `⟨s_cauchy_integral_formula, s_holomorphic_function_on_domain⟩` --[t_compose_with_identity {Cauchy formula for derivative: f'(a) = (1/2πi)∮ f(z)/(z−a)² dz on |z−a| = R}]--> output: `s_cauchy_derivative_bound`
2. input: `s_cauchy_derivative_bound` --[t_exhaustion_squeeze {if |f| ≤ M globally, then |f'(a)| ≤ M/R → 0 as R → ∞}]--> output: `s_vanishing_derivative_on_all_of_C`
3. input: `s_vanishing_derivative_on_all_of_C` --[t_reductio_ad_absurdum {f' ≡ 0 on ℂ ⇒ f constant; non-constant entire ⇒ unbounded}]--> output: `s_liouville_bounded_entire`

**Techniques used:** 5 composeWithIdentity; 9 exhaustionSqueeze; C7 reductioAdAbsurdum

---

### Cayley–Hamilton Theorem (Ch. 4)

**Axiom / starting states:** `s_polynomial_ring`, `s_real_vector_space`
**Terminal theorem state:** `s_cayley_hamilton` (kind: theorem)

**Steps:**
1. input: `s_real_vector_space` --[t_axiomatize_from_instances {square matrix A over a commutative ring; characteristic polynomial p(λ) = det(λI − A)}]--> output: `s_square_matrix_with_char_poly`
2. input: `s_square_matrix_with_char_poly` --[t_auxiliary_construction {adjugate identity (λI − A)·adj(λI − A) = p(λ)·I in ℤ[λ]}]--> output: `s_adjugate_matrix_polynomial_identity`
3. input: `s_adjugate_matrix_polynomial_identity` --[t_svd_and_spectral_decomposition {expand adj as Σ λᵏBₖ; compare powers of λ; substitute A and telescope → p(A) = 0}]--> output: `s_cayley_hamilton`

**Techniques used:** 12 axiomatizeFromInstances; C2 auxiliaryConstruction; C6 svdAndSpectralDecomposition

---

### Cantor–Bernstein–Schroeder Theorem (Ch. 4)

**Axiom / starting states:** `s_zfc_axioms`, `s_infinite_set`
**Terminal theorem state:** `s_cantor_bernstein_schroeder` (kind: theorem)

**Steps:**
1. input: `s_infinite_set` --[t_axiomatize_from_instances {two injections f: A ↪ B, g: B ↪ A; define A-orphans = A ∖ g(B)}]--> output: `s_pair_of_injections_with_orphans`
2. input: `s_pair_of_injections_with_orphans` --[t_iteration_of_trajectories {trace each x ∈ A backward via g⁻¹, f⁻¹, …; partition A into A_A, A_B, A_∞}]--> output: `s_trajectory_partition_of_A` ⚠ not in toolbox: trajectory-partition (closest match is `t_symmetry_reduction` by the orbit of the composite g∘f; adopting that)
3. input: `s_trajectory_partition_of_A` --[t_symmetry_reduction {orbits of the partial map g∘f give canonical bijection: h = f on A_A ∪ A_∞, h = g⁻¹ on A_B}]--> output: `s_cantor_bernstein_schroeder`

**Techniques used:** 12 axiomatizeFromInstances; 6 symmetryReduction (applied to the partial dynamical system g∘f). The middle step is borderline — it is a finite-case / orbit analysis that isn't the same as cluster-8 `t_contraction_fixed_point` or cluster-11 pigeonhole; flagged above.

---

### Poincaré Recurrence Theorem (Ch. 4)

**Axiom / starting states:** `s_probability_axioms`, `s_measure_preserving_transformation`
**Terminal theorem state:** `s_poincare_recurrence` (kind: theorem)

**Steps:**
1. input: `⟨s_measure_preserving_transformation, s_measurable_set_of_positive_measure⟩` --[t_auxiliary_construction {B = {x ∈ A : Tⁿ(x) ∉ A for all n ≥ 1}, the "non-returning" subset}]--> output: `s_non_returning_subset_B`
2. input: `s_non_returning_subset_B` --[t_pigeonhole_collision {preimages T⁻ⁱ(B), T⁻ʲ(B) must be disjoint by definition; but they all have measure μ(B) in a space of total measure 1}]--> output: `s_disjoint_preimages_of_B_sum_bounded`
3. input: `s_disjoint_preimages_of_B_sum_bounded` --[t_reductio_ad_absurdum {Σ μ(B) ≤ 1 forces μ(B) = 0; iterate to get infinitely-many-returns variant}]--> output: `s_poincare_recurrence`

**Techniques used:** C2 auxiliaryConstruction; 30 pigeonholeCollision; C7 reductioAdAbsurdum

---

## New state ids created

Listed here so the canonical index can ingest them in the next round. Each is `kind: state` unless explicitly marked as `kind: theorem`.

### Theorem terminals (kind: theorem)

- `s_bernoulli_lln` — Bernoulli's Law of Large Numbers
- `s_de_moivre_laplace` — De Moivre–Laplace theorem (normal approximation to binomial)
- `s_euler_totient_theorem` — Euler's totient theorem a^φ(n) ≡ 1 (mod n)
- `s_euler_homogeneous_functions` — Euler's theorem on homogeneous functions
- `s_lagrange_mvt` — Lagrange's mean value theorem
- `s_wilson_theorem` — Wilson's theorem (n−1)! ≡ −1 (mod n) iff n prime
- `s_bayes_theorem` — Bayes's theorem for conditional probability
- `s_cauchy_schwarz` — Cauchy–Schwarz inequality |⟨u,v⟩| ≤ ‖u‖‖v‖
- `s_bolzano_ivt` — Bolzano's intermediate value theorem
- `s_bolzano_weierstrass` — Bolzano–Weierstrass compactness theorem
- `s_greens_theorem` — Green's theorem in the plane
- `s_divergence_theorem` — Divergence (Gauss–Ostrogradsky) theorem
- `s_liouville_bounded_entire` — Liouville's theorem on bounded entire functions
- `s_cayley_hamilton` — Cayley–Hamilton theorem p(A) = 0
- `s_cantor_bernstein_schroeder` — Cantor–Bernstein–Schroeder theorem
- `s_poincare_recurrence` — Poincaré recurrence theorem

### Intermediate states (kind: state)

- `s_binomial_tail_ratios` — ratios of successive binomial coefficients (Bernoulli LLN workspace)
- `s_binomial_tail_bound` — explicit tail bound on P(|Xₙ − p| ≥ ε)
- `s_stirling_central_term_asymptotic` — central term of binomial approximated by √(2/πn)
- `s_gaussian_density_as_limit` — pointwise limit of rescaled binomial as e^{−t²/2}/√(2π)
- `s_unit_group_mod_n` — the group (ℤ/nℤ)*
- `s_orbit_of_a_mod_n` — orbit/permutation of units by multiplication by a
- `s_homogeneous_function_definition` — the functional equation f(tx) = tᵏf(x)
- `s_scaling_vector_field_identity` — identity from differentiating along the scaling flow
- `s_auxiliary_function_with_equal_endpoints` — Lagrange's helper g(x) with g(a)=g(b) (Rolle trick)
- `s_rolle_interior_critical_point` — interior point c ∈ (a,b) with g'(c) = 0
- `s_polynomial_x_p_minus_1_factored_mod_p` — x^(p−1) − 1 has all nonzero residues as roots mod p
- `s_factored_form_of_cyclic_unit_polynomial` — x^(p−1) − 1 ≡ ∏_{k=1}^{p−1}(x − k) (mod p)
- `s_conditional_probability_definition` — P(A | B) = P(A ∩ B)/P(B)
- `s_symmetric_chain_rule_for_intersection` — P(A|B)P(B) = P(B|A)P(A)
- `s_inner_product_space` — abstract real inner product space (pre-Hilbert)
- `s_non_negative_quadratic_in_t` — the quadratic Q(t) = ‖u − tv‖² ≥ 0
- `s_bounded_sequence_in_Rn` — bounded sequence in ℝⁿ
- `s_bounded_sequence_in_closed_box` — bounded sequence enclosed in [a,b]ⁿ
- `s_nested_intervals_with_infinitely_many_terms` — shrinking nested intervals, each containing ∞ sequence terms
- `s_supremum_set_S` — the sup-set S = {x : f(x) < 0} for Bolzano IVT
- `s_candidate_root_c_as_sup` — c = sup S
- `s_simple_region_decomposition_in_R2` — decomposition of D ⊂ ℝ² into simple pieces (Green workspace)
- `s_per_slice_ftoc_identity` — fundamental-theorem-of-calculus identity slice-by-slice (Green/div)
- `s_z_simple_region_decomposition_in_R3` — decomposition of V ⊂ ℝ³ into z-simple pieces
- `s_per_axis_flux_identity` — per-axis flux-volume identity (divergence workspace)
- `s_cauchy_derivative_bound` — Cauchy bound |f'(a)| ≤ M/R from Cauchy formula for f'
- `s_vanishing_derivative_on_all_of_C` — f' ≡ 0 on ℂ (Liouville intermediate)
- `s_square_matrix_with_char_poly` — square matrix A with char poly p(λ) = det(λI − A)
- `s_adjugate_matrix_polynomial_identity` — (λI − A)·adj(λI − A) = p(λ)·I
- `s_pair_of_injections_with_orphans` — (A, B, f, g, orphans A ∖ g(B))
- `s_trajectory_partition_of_A` — partition of A into A_A, A_B, A_∞ by trajectory behaviour
- `s_measurable_set_of_positive_measure` — measurable A ⊂ X with μ(A) > 0 (Poincaré recurrence input)
- `s_non_returning_subset_B` — non-returning subset B ⊆ A
- `s_disjoint_preimages_of_B_sum_bounded` — Σ μ(T⁻ⁱB) = ∞·μ(B) ≤ 1

---

## Flags and notes

### `⚠ not in toolbox` flags raised in this round

1. **Cantor–Bernstein–Schroeder, middle step.** The combinatorial trajectory-tracing construction (follow each x backward via g⁻¹, f⁻¹, g⁻¹, …) is not cleanly in the 57-tool toolbox. I assimilated it to `t_symmetry_reduction` by treating it as orbit-analysis of the partial map g∘f on A. A cleaner taxonomy would add a dedicated "orbit partition of a partial injection" technique, or classify it under an expanded `t_symmetry_reduction` with parameter `{partial: true, orbits: finite | infinite}`. Flagging for the philosopher round.

### Deliberate reuses of existing canonical ids (no duplicates created)

- `s_probability_axioms`, `s_iid_sequence_finite_variance`, `s_integers`, `s_prime_p`, `s_coprime_pair`, `s_fermat_little_theorem`, `s_real_line`, `s_smooth_function`, `s_continuous_function_on_interval`, `s_continuous_function_on_closed_interval`, `s_real_numbers`, `s_real_vector_space`, `s_L2_function_space`, `s_euclidean_plane`, `s_euclidean_3_space`, `s_differential_form`, `s_complex_numbers`, `s_holomorphic_function_on_domain`, `s_cauchy_integral_formula`, `s_polynomial_ring`, `s_zfc_axioms`, `s_infinite_set`, `s_measure_preserving_transformation`, `s_analytic_exponential_series` — all reused verbatim.

### Round-0 corrections applied

- `t_reductio_ad_absurdum` used in **Bolzano IVT**, **Liouville**, **Poincaré recurrence** — each case is "assume ¬conclusion, derive contradiction" with **no** descending integer measure, so `t_infinite_descent` would be wrong (that mis-tagging was common in iter-1).
- `t_auxiliary_construction` used in **Lagrange MVT** (helper g), **Wilson** (polynomial x^(p−1)−1), **Cauchy–Schwarz** (quadratic Q(t)), **Bolzano IVT** (sup-set S), **Cayley–Hamilton** (adjugate identity), **Poincaré recurrence** (non-returning B) — these are genuine construct-an-auxiliary-object moves, distinct from `t_compose_with_identity` (algebraic identity reuse) and `t_reduce_to_canonical_form` (change of basis / normalization).
- `t_svd_and_spectral_decomposition` used in **Cayley–Hamilton** for the matrix-coefficient expansion of the adjugate — the step factorizes a matrix-valued polynomial into eigenspace/power pieces, which is the spectral-decomposition flavour rather than `t_frequency_decomposition` (which is for functions on a group/space) or generic `t_reduce_to_canonical_form`.
- `t_projection_to_subspace` was **not** needed in any of the 15 chains; none of the derivations did an explicit orthogonal-projection-onto-subspace. (For completeness: it would be the natural tag if, e.g., Hahn–Banach's extension step were being reformulated, but that chain lives in iter-1 already.)
- **Bridge specializations** (sheaf cohomology / heights-Galois / level-lowering / transference / K-theoretic index) were **not** needed here; none of ch. 3–4's missing theorems cross analysis/algebra/topology in the highly specific ways those bridges are reserved for. They are for Wiles, Faltings, Riemann–Roch, Green–Tao, Atiyah–Singer (all in iter-1, ch. 6).

### Summary (for the report)

- **Chapter 3 new chains: 7** (Bernoulli LLN, De Moivre–Laplace, Euler totient, Euler homogeneous, Lagrange MVT, Wilson, Bayes).
- **Chapter 4 new chains: 9** (Cauchy–Schwarz, Bolzano IVT, Bolzano–Weierstrass, Green's, Divergence, Liouville, Cayley–Hamilton, Cantor–Bernstein–Schroeder, Poincaré recurrence).
- **Total new chains: 16.**
- **`⚠ not in toolbox` flags: 1** (Cantor–Bernstein–Schroeder middle step — trajectory partition of a partial injection).
- **New state ids: 49** (16 theorem terminals + 33 intermediate states).
