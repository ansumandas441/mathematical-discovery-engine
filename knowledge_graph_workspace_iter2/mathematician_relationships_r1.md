# Mathematician A — Iteration 2, Round 1: missing deep-dive theorem chains (Chapters 01–02)

Deliverable: derivation chains for every `### <Theorem>` heading in `01_ancient.md` and `02_renaissance_17c.md` not already represented in `mathematician_relationships.md` (iter-1).

Node-id conventions: reuse existing ids from `canonical_node_index.md` verbatim; introduce new `s_*` ids only for states that are genuinely new to these missing theorems. Edge labels must match a toolbox technique or one of the C1–C12 Round-0 additions. Ch.11 §6 corrections applied (`t_auxiliary_construction`, `t_reductio_ad_absurdum`, `t_projection_to_subspace`).

---

## Chapter 1 — Ancient & Medieval (missing chains)

Total headings in Ch. 1: 15. Already covered in iter-1: Pythagorean, Thales, Infinitude of Primes, Fundamental Theorem of Arithmetic, Archimedes Quadrature, Ptolemy, Chinese Remainder, Bhāskara Chakravāla (8). Missing: 7 (below).

---

### Heron's Formula (Ch. 1)

**Axiom / starting states:** `s_euclidean_plane`, `s_pythagorean_theorem`, `s_polygon_area_formula`
**Terminal theorem state:** `s_heron_formula` *(new)*

**Steps:**
1. input: `s_euclidean_plane` --[t_auxiliary_construction {construct: incircle with inradius r and tangent-segment decomposition s = x+y+z, a = y+z, b = x+z, c = x+y}]--> output: `s_incircle_tangent_decomposition` *(new)*
2. input: `⟨s_incircle_tangent_decomposition, s_pythagorean_theorem⟩` --[t_compose_with_identity {identity: area = r·s, r² = (s−a)(s−b)(s−c)/s via similar right triangles at tangent points}]--> output: `s_area_squared_equals_s_times_product` *(new)*
3. input: `s_area_squared_equals_s_times_product` --[t_reduce_to_canonical_form {form: A = √[s(s−a)(s−b)(s−c)]}]--> output: `s_heron_formula`

**Techniques used:** C2 auxiliaryConstruction; 5 composeWithIdentity; 4 reduceToCanonicalForm

---

### Menelaus's Theorem (Ch. 1)

**Axiom / starting states:** `s_euclidean_plane`, `s_similar_triangle_criterion`
**Terminal theorem state:** `s_menelaus_theorem` *(new)*

**Steps:**
1. input: `s_euclidean_plane` --[t_auxiliary_construction {construct: transversal line ℓ crossing BC at D, CA at E, AB at F; drop perpendiculars from A, B, C to ℓ of lengths hₐ, h_b, h_c}]--> output: `s_perpendiculars_from_vertices_to_transversal` *(new)*
2. input: `⟨s_perpendiculars_from_vertices_to_transversal, s_similar_triangle_criterion⟩` --[t_compose_with_identity {identity: BD/DC = h_b/h_c, CE/EA = h_c/hₐ, AF/FB = hₐ/h_b — pairwise similar right triangles}]--> output: `s_ratio_product_cancels_heights` *(new)*
3. input: `s_ratio_product_cancels_heights` --[t_conserved_quantity {signed product of three ratios = −1 is an invariant of the transversal}]--> output: `s_menelaus_theorem`

**Techniques used:** C2 auxiliaryConstruction; 5 composeWithIdentity; 7 conservedQuantity

---

### Brahmagupta's Formula (Ch. 1)

**Axiom / starting states:** `s_euclidean_plane`, `s_cyclic_quadrilateral`, `s_heron_formula`
**Terminal theorem state:** `s_brahmagupta_formula` *(new)*

**Steps:**
1. input: `s_cyclic_quadrilateral` --[t_auxiliary_construction {construct: split by diagonal into two triangles sharing opposite cyclic angles θ and π−θ}]--> output: `s_two_triangles_with_supplementary_angles` *(new)*
2. input: `⟨s_two_triangles_with_supplementary_angles, s_heron_formula⟩` --[t_compose_with_identity {identity: sin θ = sin(π−θ) ⇒ area = ½(ab+cd) sin θ; law of cosines eliminates diagonal}]--> output: `s_area_squared_symmetric_in_four_sides` *(new)*
3. input: `s_area_squared_symmetric_in_four_sides` --[t_reduce_to_canonical_form {factor: (s−a)(s−b)(s−c)(s−d)}]--> output: `s_brahmagupta_formula`

**Techniques used:** C2 auxiliaryConstruction; 5 composeWithIdentity; 4 reduceToCanonicalForm

---

### Brahmagupta's Theorem (Ch. 1)

**Axiom / starting states:** `s_euclidean_plane`, `s_cyclic_quadrilateral`
**Terminal theorem state:** `s_brahmagupta_midpoint_theorem` *(new)*

**Steps:**
1. input: `s_cyclic_quadrilateral` --[t_symmetry_reduction {restrict to: orthodiagonal subclass — diagonals meet at M with ⟂}]--> output: `s_orthodiagonal_cyclic_quadrilateral` *(new)*
2. input: `s_orthodiagonal_cyclic_quadrilateral` --[t_auxiliary_construction {construct: perpendicular from intersection M to side AB, extended to hit CD at F}]--> output: `s_perpendicular_from_diagonal_intersection_to_side` *(new)*
3. input: `s_perpendicular_from_diagonal_intersection_to_side` --[t_compose_with_identity {identity: inscribed-angle theorem gives ∠FMC = ∠MDC and ∠FMD = ∠MCD, forcing FM = FC = FD}]--> output: `s_brahmagupta_midpoint_theorem`

**Techniques used:** 6 symmetryReduction; C2 auxiliaryConstruction; 5 composeWithIdentity

---

### Aryabhata's Theorems (Ch. 1)

**Axiom / starting states:** `s_real_analysis`, `s_sine_function`, `s_integers`, `s_divisibility_definition`
**Terminal theorem state:** `s_aryabhata_sine_pi_kuttaka` *(new)* — a bundle for the three Āryabhaṭīya results (sine second-difference, π ≈ 3.1416, kuṭṭaka).

**Steps:**
1. input: `s_sine_function` --[t_spot_pattern_in_table {tabulate sin(3°45′·k), compute Δ²sin values, observe Δ²sin ≈ −(225/3438)·sin}]--> output: `s_sine_second_difference_recurrence` *(new)*
2. input: `s_sine_second_difference_recurrence` --[t_verify_on_special_cases {check: sin(90°) recovers 3438 within tabular precision}]--> output: `s_aryabhata_sine_table` *(new)*
3. input: `s_aryabhata_sine_table` --[t_exhaustion_squeeze {inscribe polygon and use sine table to bound π; Aryabhata records 62832/20000}]--> output: `s_aryabhata_pi_3_1416` *(new)*
4. input: `⟨s_integers, s_divisibility_definition⟩` --[t_infinite_descent {measure: |b| in ax + by = c; pulverize (a, b) → (b, a mod b) until residue = 0}]--> output: `s_kuttaka_extended_euclid` *(new)*
5. input: `⟨s_aryabhata_sine_table, s_aryabhata_pi_3_1416, s_kuttaka_extended_euclid⟩` --[t_compose_with_identity {bundle the three Āryabhaṭīya results}]--> output: `s_aryabhata_sine_pi_kuttaka`

**Techniques used:** 1 spotPatternInTable; 2 verifyOnSpecialCases; 9 exhaustionSqueeze; 21 infiniteDescent; 5 composeWithIdentity

---

### Al-Khwārizmī's Quadratic Framework (Ch. 1)

**Axiom / starting states:** `s_integers`, `s_euclidean_plane`, `s_polygon_area_formula`
**Terminal theorem state:** `s_alkhwarizmi_six_quadratic_types` *(new)*

**Steps:**
1. input: `s_integers` --[t_axiomatize_from_instances {instances: diverse inheritance / surveying / commerce quadratic word-problems; extract six positive-coefficient normal forms}]--> output: `s_six_canonical_quadratic_forms` *(new)*
2. input: `⟨s_six_canonical_quadratic_forms, s_polygon_area_formula⟩` --[t_complete_the_square {geometric: attach rectangles of width b/(2a) around a square of side x; add corner-square to make a perfect square}]--> output: `s_geometric_completion_of_square` *(new)*
3. input: `s_geometric_completion_of_square` --[t_reduce_to_canonical_form {operations: al-jabr (restoration) + al-muqābala (balancing) reduce any instance to one of the six forms and solve}]--> output: `s_alkhwarizmi_six_quadratic_types`

**Techniques used:** 12 axiomatizeFromInstances; 3 completeTheSquare; 4 reduceToCanonicalForm

---

### Omar Khayyām's Geometric Solution of Cubics (Ch. 1)

**Axiom / starting states:** `s_euclidean_plane`, `s_conic_sections`, `s_alkhwarizmi_six_quadratic_types`
**Terminal theorem state:** `s_khayyam_cubic_geometric_solution` *(new)*

**Steps:**
1. input: `s_alkhwarizmi_six_quadratic_types` --[t_axiomatize_from_instances {extend al-Khwārizmī's classification to positive-coefficient cubics; remove degree-reducible cases; obtain 14 irreducible types}]--> output: `s_fourteen_irreducible_cubic_types` *(new)*
2. input: `⟨s_fourteen_irreducible_cubic_types, s_conic_sections⟩` --[t_auxiliary_construction {for each type, construct a pair of conics (parabola + circle / parabola + hyperbola / two parabolas) whose intersection abscissa solves the cubic}]--> output: `s_cubic_as_intersection_of_two_conics` *(new)*
3. input: `s_cubic_as_intersection_of_two_conics` --[t_structural_isomorphism {cubic-equation solving ↔ conic-intersection problem via shared algebraic identity}]--> output: `s_khayyam_cubic_geometric_solution`

**Techniques used:** 12 axiomatizeFromInstances; C2 auxiliaryConstruction; 13 structuralIsomorphism

---

## Chapter 2 — Renaissance & 17c (missing chains)

Total headings in Ch. 2: 18. Already covered in iter-1: Cardano, Ferrari, Fermat Little, Fermat Two Squares, Desargues, FTC, Kepler (7). Missing: 11 (below).

---

### Viète's Formulas (Ch. 2)

**Axiom / starting states:** `s_complex_numbers`, `s_polynomial_ring`
**Terminal theorem state:** `s_viete_formulas` *(new)*

**Steps:**
1. input: `s_polynomial_ring` --[t_auxiliary_construction {write monic polynomial as factored form ∏(x − rᵢ) using roots as auxiliaries}]--> output: `s_polynomial_as_product_of_root_factors` *(new)*
2. input: `s_polynomial_as_product_of_root_factors` --[t_compose_with_identity {identity: expand ∏(x − rᵢ) by distributive law; coefficient of xⁿ⁻ᵏ is (−1)ᵏ · eₖ(r₁,…,rₙ)}]--> output: `s_elementary_symmetric_polynomials` *(new)*
3. input: `s_elementary_symmetric_polynomials` --[t_structural_isomorphism {polynomial coefficients ↔ elementary symmetric functions of roots — lays groundwork for Galois correspondence}]--> output: `s_viete_formulas`

**Techniques used:** C2 auxiliaryConstruction; 5 composeWithIdentity; 13 structuralIsomorphism

---

### Fermat's Last Theorem, Origin — n = 4 descent (Ch. 2)

**Axiom / starting states:** `s_integers`, `s_pythagorean_theorem`
**Terminal theorem state:** `s_flt_n_equals_4` *(new)* — Fermat's margin-claim as actually provable by his method; distinct from the full `s_flt` terminal (Wiles) already in index.

**Steps:**
1. input: `s_integers` --[t_conjecture_refinement {generalize Pythagorean-triple problem: no positive integer solutions to xⁿ + yⁿ = zⁿ for n > 2}]--> output: `s_flt_general_conjecture` *(new)*
2. input: `s_flt_general_conjecture` --[t_verify_on_special_cases {special case: n = 4; strengthen to x⁴ + y⁴ = z² (implies n = 4 FLT)}]--> output: `s_flt_n_4_strengthened_claim` *(new)*
3. input: `s_flt_n_4_strengthened_claim` --[t_infinite_descent {measure: z; from any hypothetical (x, y, z) construct (x′, y′, z′) with z′ < z via primitive-triple parametrization}]--> output: `s_flt_n_equals_4`

**Techniques used:** C1 conjectureRefinement; 2 verifyOnSpecialCases; 21 infiniteDescent

---

### Descartes' Rule of Signs (Ch. 2)

**Axiom / starting states:** `s_real_numbers`, `s_polynomial_ring`
**Terminal theorem state:** `s_descartes_rule_of_signs` *(new)*

**Steps:**
1. input: `s_polynomial_ring` --[t_spot_pattern_in_table {tabulate #sign-changes vs #positive-roots across small polynomials; observe equality or shortfall by an even number}]--> output: `s_sign_change_parity_conjecture` *(new)*
2. input: `s_sign_change_parity_conjecture` --[t_compose_with_identity {identity: multiplying p(x) by (x − r) with r > 0 raises the positive-root count by 1 and the sign-change count by an odd number}]--> output: `s_sign_change_increment_under_positive_factor` *(new)*
3. input: `s_sign_change_increment_under_positive_factor` --[t_conserved_quantity {invariant: #positiveRoots ≡ #signChanges (mod 2), with difference bounded by #signChanges}]--> output: `s_descartes_rule_of_signs`

**Techniques used:** 1 spotPatternInTable; 5 composeWithIdentity; 7 conservedQuantity

---

### Descartes' Theorem on Total Angular Defect (Ch. 2)

**Axiom / starting states:** `s_convex_polyhedron`, `s_euclidean_3_space`
**Terminal theorem state:** `s_descartes_angular_defect` *(new)*

**Steps:**
1. input: `s_convex_polyhedron` --[t_auxiliary_construction {for each vertex v, compute angular defect δ(v) = 2π − Σ(face angles at v)}]--> output: `s_vertex_angular_defect` *(new)*
2. input: `s_vertex_angular_defect` --[t_compose_with_identity {sum over V: Σ δ(v) = 2πV − Σ(all face angles) = 2πV − Σ_face (nᵢ − 2)π = 2π(V − E + F)}]--> output: `s_total_defect_equals_2pi_chi` *(new)*
3. input: `⟨s_total_defect_equals_2pi_chi, s_euler_polyhedron_formula⟩` --[t_conserved_quantity {χ = V − E + F = 2 for convex polyhedra ⇒ total defect = 4π}]--> output: `s_descartes_angular_defect`

**Techniques used:** C2 auxiliaryConstruction; 5 composeWithIdentity; 7 conservedQuantity

---

### Pascal's Theorem on Hexagons in a Conic / Mystic Hexagram (Ch. 2)

**Axiom / starting states:** `s_projective_plane`, `s_conic_sections`, `s_projective_space_axioms`
**Terminal theorem state:** `s_pascal_mystic_hexagram` *(new)*

**Steps:**
1. input: `s_conic_sections` --[t_reduce_to_canonical_form {projective transformation carries any conic to a circle}]--> output: `s_inscribed_hexagon_in_circle` *(new)*
2. input: `s_inscribed_hexagon_in_circle` --[t_auxiliary_construction {construct three pairs of opposite-side extensions, obtaining three candidate intersection points}]--> output: `s_three_opposite_side_intersection_points` *(new)*
3. input: `s_three_opposite_side_intersection_points` --[t_duality {Pascal ↔ Brianchon: inscribed conic theorem ↔ circumscribed conic theorem}]--> output: `s_pascal_line` *(new)*
4. input: `s_pascal_line` --[t_conserved_quantity {collinearity invariant under projective transformation; lift circle result back to any conic}]--> output: `s_pascal_mystic_hexagram`

**Techniques used:** 4 reduceToCanonicalForm; C2 auxiliaryConstruction; 8 duality; 7 conservedQuantity

---

### Pascal's Triangle Identity (Ch. 2)

**Axiom / starting states:** `s_naturals_with_multiplication`
**Terminal theorem state:** `s_pascal_triangle_identity` *(new)*

**Steps:**
1. input: `s_naturals_with_multiplication` --[t_spot_pattern_in_table {tabulate C(n, k) triangle; observe each entry = sum of two above}]--> output: `s_binomial_recurrence_conjecture` *(new)*
2. input: `s_binomial_recurrence_conjecture` --[t_auxiliary_construction {distinguish one element of the n-set; split k-subsets into "contains" and "excludes" this element}]--> output: `s_distinguished_element_bijection` *(new)*
3. input: `s_distinguished_element_bijection` --[t_compose_with_identity {identity: C(n, k) = C(n−1, k−1) + C(n−1, k); combinatorial composition]]--> output: `s_pascal_triangle_identity`

**Techniques used:** 1 spotPatternInTable; C2 auxiliaryConstruction; 5 composeWithIdentity

---

### Newton's Generalized Binomial Theorem (Ch. 2)

**Axiom / starting states:** `s_real_numbers`, `s_pascal_triangle_identity`
**Terminal theorem state:** `s_newton_binomial_theorem` *(new)*

**Steps:**
1. input: `s_pascal_triangle_identity` --[t_interpolate_and_continue {extend C(n, k) = n!/k!(n−k)! to real (or complex) r via falling factorial C(r, k) = r(r−1)⋯(r−k+1)/k!}]--> output: `s_generalized_binomial_coefficient` *(new)*
2. input: `s_generalized_binomial_coefficient` --[t_compose_with_identity {formal identity: (1+x)ʳ · (1+x)ˢ = (1+x)^{r+s}; compare series coefficients on both sides}]--> output: `s_vandermonde_convolution_extended` *(new)*
3. input: `s_vandermonde_convolution_extended` --[t_compactness_argument {convergence for |x| < 1 established by ratio test; term-by-term verification of the ODE y′ = r y/(1+x)}]--> output: `s_newton_binomial_theorem`

**Techniques used:** 10 interpolateAndContinue; 5 composeWithIdentity; 16 compactnessArgument

---

### Newton's Identities (Ch. 2)

**Axiom / starting states:** `s_polynomial_ring`, `s_viete_formulas`
**Terminal theorem state:** `s_newton_identities` *(new)*

**Steps:**
1. input: `s_viete_formulas` --[t_auxiliary_construction {construct generating function P(t) = ∏(1 − xᵢ t) = Σ (−1)ᵏ eₖ tᵏ; take logarithmic derivative}]--> output: `s_log_derivative_generating_function` *(new)*
2. input: `s_log_derivative_generating_function` --[t_frequency_decomposition {expand −P′(t)/P(t) = Σ xᵢ/(1−xᵢt) = Σ pₖ tᵏ⁻¹ as power-sum generating series}]--> output: `s_power_sum_series` *(new)*
3. input: `s_power_sum_series` --[t_compose_with_identity {identity: P′(t) = −P(t) · Σ pₖ tᵏ⁻¹; compare coefficients yielding pₖ − e₁ pₖ₋₁ + ⋯ + (−1)ᵏ⁻¹ k eₖ = 0}]--> output: `s_newton_identities`

**Techniques used:** C2 auxiliaryConstruction; 11 frequencyDecomposition; 5 composeWithIdentity

---

### Rolle's Theorem (Ch. 2)

**Axiom / starting states:** `s_continuous_function_on_closed_interval`, `s_real_analysis`
**Terminal theorem state:** `s_rolle_theorem` *(new)*

**Steps:**
1. input: `s_continuous_function_on_closed_interval` --[t_compactness_argument {continuous f on [a,b] attains max and min (extreme value theorem)}]--> output: `s_attained_extrema_on_closed_interval` *(new)*
2. input: `s_attained_extrema_on_closed_interval` --[t_auxiliary_construction {hypothesis f(a) = f(b); either an interior extremum exists, or f is constant — trivially}]--> output: `s_interior_extremum_or_constant` *(new)*
3. input: `s_interior_extremum_or_constant` --[t_conserved_quantity {Fermat's stationary-point condition: f′ = 0 at an interior extremum}]--> output: `s_rolle_theorem`

**Techniques used:** 16 compactnessArgument; C2 auxiliaryConstruction; 7 conservedQuantity

---

### Torricelli's Law (Ch. 2)

**Axiom / starting states:** `s_newtonian_inverse_square_force` (Galilean free-fall specialization), `s_real_analysis`
**Terminal theorem state:** `s_torricelli_law` *(new)*

**Steps:**
1. input: `s_newtonian_inverse_square_force` --[t_physics_to_pde {near-surface idealization: uniform gravity g; falling body from rest at height h acquires speed v = √(2gh) — Galileo's law}]--> output: `s_galilean_free_fall_speed` *(new)*
2. input: `s_galilean_free_fall_speed` --[t_structural_isomorphism {analogy: water column is a family of "falling stacks" of free-fall elements; streamline-energy balance maps rigid body to inviscid fluid}]--> output: `s_fluid_column_energy_balance` *(new)*
3. input: `s_fluid_column_energy_balance` --[t_conserved_quantity {energy conservation along streamline: ρgh = ½ρv² ⇒ v = √(2gh) at orifice}]--> output: `s_torricelli_law`

**Techniques used:** 23 physicsToPDE; 13 structuralIsomorphism; 7 conservedQuantity

---

### Wallis Product for π (Ch. 2)

**Axiom / starting states:** `s_real_analysis`, `s_sine_function`, `s_integral_as_limit_of_sums`
**Terminal theorem state:** `s_wallis_product` *(new)*

**Steps:**
1. input: `s_integral_as_limit_of_sums` --[t_spot_pattern_in_table {tabulate I(n, m) = ∫₀¹ (1 − x^{1/m})ⁿ dx for small integer m, n; observe product-pattern of ratios}]--> output: `s_wallis_integer_quadrature_table` *(new)*
2. input: `s_wallis_integer_quadrature_table` --[t_interpolate_and_continue {extend ∫₀¹ (1 − x²)ⁿ dx to n = 1/2 — the circle-segment area π/4 — by forcing the ratio-pattern to persist}]--> output: `s_wallis_half_integer_interpolation` *(new)*
3. input: `⟨s_wallis_half_integer_interpolation, s_sine_function⟩` --[t_exhaustion_squeeze {squeeze: sin^{2k+1} ≤ sin^{2k} ≤ sin^{2k−1} gives ratio → 1; unwind via reduction formula Iₙ = (n−1)/n · Iₙ₋₂}]--> output: `s_wallis_product`

**Techniques used:** 1 spotPatternInTable; 10 interpolateAndContinue; 9 exhaustionSqueeze

---

## Summary

- **Ch. 1 headings:** 15. Missing chains produced: **7** (Heron, Menelaus, Brahmagupta's Formula, Brahmagupta's Theorem, Aryabhata's Theorems, Al-Khwārizmī, Omar Khayyām).
- **Ch. 2 headings:** 18. Missing chains produced: **11** (Viète, FLT n=4 origin, Descartes' Rule of Signs, Descartes' Angular Defect, Pascal's Hexagram, Pascal's Triangle, Newton's Binomial, Newton's Identities, Rolle, Torricelli, Wallis).
- **Total new chains:** **18**.
- **"⚠ not in toolbox" flags:** none. Every step mapped to an existing 57-toolbox technique or to a Round-0 C1/C2/C6/C7/C9/C12 addition.
- **New state-node ids introduced** (for these missing theorems — no existing canonical id fit):
  - Ch. 1: `s_heron_formula`, `s_incircle_tangent_decomposition`, `s_area_squared_equals_s_times_product`, `s_menelaus_theorem`, `s_perpendiculars_from_vertices_to_transversal`, `s_ratio_product_cancels_heights`, `s_brahmagupta_formula`, `s_two_triangles_with_supplementary_angles`, `s_area_squared_symmetric_in_four_sides`, `s_brahmagupta_midpoint_theorem`, `s_orthodiagonal_cyclic_quadrilateral`, `s_perpendicular_from_diagonal_intersection_to_side`, `s_aryabhata_sine_pi_kuttaka`, `s_sine_second_difference_recurrence`, `s_aryabhata_sine_table`, `s_aryabhata_pi_3_1416`, `s_kuttaka_extended_euclid`, `s_alkhwarizmi_six_quadratic_types`, `s_six_canonical_quadratic_forms`, `s_geometric_completion_of_square`, `s_khayyam_cubic_geometric_solution`, `s_fourteen_irreducible_cubic_types`, `s_cubic_as_intersection_of_two_conics`.
  - Ch. 2: `s_viete_formulas`, `s_polynomial_as_product_of_root_factors`, `s_elementary_symmetric_polynomials`, `s_flt_n_equals_4`, `s_flt_general_conjecture`, `s_flt_n_4_strengthened_claim`, `s_descartes_rule_of_signs`, `s_sign_change_parity_conjecture`, `s_sign_change_increment_under_positive_factor`, `s_descartes_angular_defect`, `s_vertex_angular_defect`, `s_total_defect_equals_2pi_chi`, `s_pascal_mystic_hexagram`, `s_inscribed_hexagon_in_circle`, `s_three_opposite_side_intersection_points`, `s_pascal_line`, `s_pascal_triangle_identity`, `s_binomial_recurrence_conjecture`, `s_distinguished_element_bijection`, `s_newton_binomial_theorem`, `s_generalized_binomial_coefficient`, `s_vandermonde_convolution_extended`, `s_newton_identities`, `s_log_derivative_generating_function`, `s_power_sum_series`, `s_rolle_theorem`, `s_attained_extrema_on_closed_interval`, `s_interior_extremum_or_constant`, `s_torricelli_law`, `s_galilean_free_fall_speed`, `s_fluid_column_energy_balance`, `s_wallis_product`, `s_wallis_integer_quadrature_table`, `s_wallis_half_integer_interpolation`.
- **Reuse of existing canonical ids** (verified against `canonical_node_index.md`): `s_euclidean_plane`, `s_pythagorean_theorem`, `s_polygon_area_formula`, `s_similar_triangle_criterion`, `s_cyclic_quadrilateral`, `s_heron_formula` (self-reuse after first introduction), `s_real_analysis`, `s_sine_function`, `s_integers`, `s_divisibility_definition`, `s_euclidean_3_space`, `s_conic_sections`, `s_complex_numbers`, `s_polynomial_ring`, `s_naturals_with_multiplication`, `s_real_numbers`, `s_projective_plane`, `s_projective_space_axioms`, `s_convex_polyhedron`, `s_euler_polyhedron_formula`, `s_continuous_function_on_closed_interval`, `s_newtonian_inverse_square_force`, `s_integral_as_limit_of_sums`.
