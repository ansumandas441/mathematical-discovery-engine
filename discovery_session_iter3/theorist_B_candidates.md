# Theorist B — Candidate New Theorems

**Role**: Theorist B (analytic / number-theoretic / polynomial-method / frequency-decomposition frontier).
**Graph**: `/Users/primetrce/Documents/maths/knowledge_graph.json` (752 nodes, 1258 edges, 12 compound subgraphs).
**Recon**: `/Users/primetrce/Documents/maths/discovery_session_iter3/recon_leverage_points.md`.

Every derivation step cites a node ID; external facts are flagged. Candidates are self-graded TRIVIAL / COROLLARY-OF-KNOWN / LIKELY-KNOWN-UNDER-OTHER-NAME / PLAUSIBLY-NEW / SPECULATIVE, and proof-integrity risk LOW / MEDIUM / HIGH.

7 candidates. Rejected seeds: 6 (heat conservation — would grade TRIVIAL, classical energy/maximum-principle) and 10 (axiomatic Green–Tao transference — subsumed by Conlon–Fox–Zhao, Tao–Ziegler).

---

## Candidate B1 — Spectral Noether Theorem (mode-wise conservation)

**Derivation chain**: push `t_frequency_decomposition` onto `s_infinitesimal_action_variation` (near-edge node, currently only used once via `t_conserved_quantity` to produce `s_noether_theorem`). Formally: `s_infinitesimal_action_variation --[t_frequency_decomposition]--> T_B1`.

**Statement (plain)**: For a Lagrangian field theory with a 1-parameter symmetry, decompose each field into Fourier modes. Noether's theorem then gives a family of conserved charges — one per mode — provided the symmetry commutes with spatial translation. The sum over modes recovers the classical Noether charge; each mode's charge is independently conserved.

**Statement (formal)**:
Let `L(φ, ∂φ)` be a Lagrangian density on `ℝ^d × ℝ_t` invariant under `g_s: φ ↦ φ + s·X(φ)`. Suppose `X` commutes with spatial translation (i.e. is a Fourier multiplier). Decompose `φ(x,t) = ∫ φ̂(k,t) e^{ik·x} dk`. Then:

1. *(corollary of graph machinery)* For each `k`, a mode-wise current `j_k^μ(t)` satisfies `∂_μ j_k^μ = 0` on-shell; `J^μ = ∫ j_k^μ dk` recovers the classical current.

2. *(new claim)* If the symmetry acts on modes by character `χ(k)`, the mode-wise charge `Q(k)` is conserved pointwise in `k` a.e., with coercivity `|Q(k)| ≤ C(1+|k|)^m · E^{1/2}`, `m` the order of `X`.

3. *(speculative)* Second-quantised `Q̂(k)` generate a commutative subalgebra whose spectral decomposition refines Peter–Weyl.

**Derivation sketch**:
1. Hypotheses of `s_noether_theorem`: Lagrangian `L`, `δS=0`, 1-param symmetry.
2. Invoke `s_infinitesimal_action_variation`: `δS` under the generator vanishes on-shell.
3. Apply `t_frequency_decomposition` to the field inside `S`: `φ = ∑_k φ̂(k) e^{ik·x}`.
4. *External fact*: translation-invariance of `X` implies `X` acts on mode `k` by `χ(k)`. Parseval: `S = ∫ L̂(φ̂(k),∂_t φ̂(k)) dk`.
5. Apply `t_conserved_quantity` mode-wise: each `φ̂(k)` satisfies its own Euler–Lagrange equation with its own 1-param symmetry acting by `χ(k)`.
6. Invoke `s_noether_theorem` at each `k`: produces `Q(k)` conserved.
7. Plancherel: `J^μ = ∫ j_k^μ dk`.
8. Energy bound on `φ̂(k)` gives `|Q(k)| ≤ C(1+|k|)^m E^{1/2}`.

**Inherited vs. added**: *Inherited*: Noether, Fourier decomposition of fields (standard in `s_fourier_theorem_heat`). *Added*: commutation hypothesis making decomposition exact; explicit coercivity bound; independent-mode conservation (as opposed to a sum recovering the classical current).

**Novelty**: **COROLLARY-OF-KNOWN**. Classical-field folklore: free-theory mode decomposition gives infinitely many conserved currents (Klein–Gordon modes). This is implicit in canonical-quantisation textbooks and is effectively a Peter–Weyl / spectral-decomposition statement of symmetry representations on the Hilbert space of states. The coercivity bound is Plancherel, not a theorem. The commutation hypothesis rules out gauge symmetries, where the non-trivial version lives. Overlap: Weinberg QFT Vol. 1 §7.4, DeWitt's *Global Approach to QFT*.

**Failure modes**:
- Non-translation-invariant `X` (e.g. Lorentz boost): commutation fails, step 4 breaks.
- Gauge symmetries: modes mix, charges not gauge-invariant.
- Interactions (e.g. `φ^4`): `L̂` doesn't factorise over modes; only free theories give independent mode currents.

**Proof-integrity risk**: **LOW**. Fourier + Noether under a transparent hypothesis.

---

## Candidate B2 — Polynomial-Method Chabauty Bound

**Derivation chain**: `s_curve_inside_abelian_variety --[t_polynomial_method]--> T_B2`. Recon flags the target as near-edge (only `t_analysis_algebra_topology_bridge` currently outgoing); `t_polynomial_method` has 0 top-level uses in the graph.

**Statement (plain)**: For a genus-`g ≥ 2` curve `C/ℚ` with Mordell–Weil rank `r`, if `r < g` then `#C(ℚ)` admits an explicit bound `O((2g-2) · p^{r/g})` via a polynomial-method argument on the reduction `C(ℚ) → J_C(𝔽_p)`.

**Statement (formal)**:
Let `C/ℚ` have genus `g ≥ 2`, Jacobian `J_C`, Mordell–Weil rank `r`, prime `p ≥ 2g+1` of good reduction.

1. *(corollary)* `#C(ℚ) < ∞` — this is `s_mordell_faltings`.

2. *(new claim)* If `r < g`, there exists `F ∈ ℚ[x₀,…,x_g]` of explicit degree `D=D(g,r,p)` vanishing on the Abel–Jacobi image of `C(ℚ)` mod `p`, with `#C(ℚ) ≤ (2g-2) · D · p^{r/g}`.

3. *(speculative)* For `p ≫ g`, this matches or beats Chabauty–Coleman `#C(ℚ) ≤ #C(𝔽_p)+2r`.

**Derivation sketch**:
1. Hypotheses of `s_mordell_faltings`: `g ≥ 2`.
2. Invoke `s_curve_inside_abelian_variety`: `C ↪ J_C`.
3. Invoke `s_mordell_weil_theorem`: `J_C(ℚ) ≅ ℤ^r ⊕ T` finitely generated.
4. Reduction: `C(ℚ) → J_C(𝔽_p)`; image lies in a rank-≤`r` subgroup `H ⊂ J_C(𝔽_p)`.
5. Apply `t_polynomial_method`: for `|H| ≤ p^r` points in a variety of dim `g`, a polynomial `F` of degree `D ≤ |H|^{1/g} ≤ p^{r/g}` vanishes on `H` (Croot–Lev–Pach / Alon Nullstellensatz style).
6. `#(C ∩ V(F))(𝔽_p) ≤ (2g-2)·D` by Bezout since `C` is a curve.
7. Every rational point maps into `V(F) mod p`, giving the bound.
8. *External fact required*: CLP/Alon polynomial-method construction extended from `𝔽_p^n` to abelian varieties.

**Inherited vs. added**: *Inherited*: `s_mordell_faltings`, `s_curve_inside_abelian_variety`, `s_mordell_weil_theorem`, Bezout. *Added*: explicit `p^{r/g}` constant, polynomial-method (not `p`-adic log) construction, comparison with Chabauty–Coleman.

**Novelty**: **LIKELY-KNOWN-UNDER-OTHER-NAME**. Neighborhood: Stoll's uniform Mordell via Chabauty, Katz–Rabinoff effective Chabauty, Dimitrov–Gao–Habegger 2021 uniform Mordell; polynomial-method on abelian varieties by Bilu–Rémond–Galateau; Bombieri–Pila / Pila–Wilkie-type point counting. The bound `(2g-2)·p^{r/g}` resembles Coleman's with a polynomial-method twist but is likely a reformulation.

**Failure modes**:
- `r = g`: image fills Jacobian mod p, degree blows up; statement vacuous.
- `p < 2g+1` or bad reduction: injectivity fails.
- CM Jacobian: image lies in a proper subgroup, bound is wasteful.

**Proof-integrity risk**: **MEDIUM**. Step 5 on an abelian variety (rather than `𝔽_p^n`) is the risky technical step.

---

## Candidate B3 — Local CLT on Arithmetic Progressions (circle-method error)

**Derivation chain**: `s_characteristic_function_of_sum --[t_major_minor_arc_decomposition]--> T_B3`, combined with the existing `s_limit_characteristic_function_equals_gaussian` (near-edge, only `t_compactness_argument` currently). `t_circle_method` has 2 top-level uses, neither on CLT.

**Statement (plain)**: For `S_n = X_1+…+X_n`, iid integer-valued, mean 0, variance 1, aperiodic, the probability `P(S_n = m, S_n ≡ a mod q)` equals `(1/q)·g_n(m) + O(q·n^{-1})` uniformly in `a` for `q ≤ n^{1/2-ε}`, where `g_n` is the Gaussian local density. The error comes from the minor arcs of a Farey dissection of the characteristic function.

**Statement (formal)**:
`X_i` iid on ℤ, `E[X]=0, E[X^2]=1, E[|X|^3]<∞`, `gcd{x: P(X=x)>0}=1`. Then for `q ≤ n^{1/2-ε}`, uniformly in residue `a mod q`:

1. *(corollary)* `P(S_n ≤ x√n) → Φ(x)` — this is `s_central_limit_theorem`.

2. *(new quantitative claim)* `P(S_n=m, S_n ≡ a mod q) = (1/q)·g_n(m) + O(q·n^{-1}·m_3^{1/2})`, `g_n(m)=(2πn)^{-1/2}e^{-m²/2n}`, `m_3=E[|X|^3]`.

3. *(speculative)* Error strengthens to `O(q^{1/2}·n^{-1}·(log n)^C)` via Elliott–Halberstam-style level of distribution, up to `q = n^{1/2}`.

**Derivation sketch**:
1. Hypotheses of `s_central_limit_theorem`.
2. Invoke `s_characteristic_function_of_sum`: `φ_{S_n}(t)=φ_X(t)^n`.
3. Fourier inversion: `P(S_n=m) = (1/2π) ∫_{-π}^{π} φ_{S_n}(t) e^{-itm} dt`.
4. Character orthogonality: `𝟙[S_n ≡ a mod q] = (1/q) ∑_{b mod q} e^{2πib(S_n-a)/q}`.
5. Apply `t_major_minor_arc_decomposition` on `[-π,π]`.
6. Major arc at `t=0`: Taylor gives Gaussian main `g_n(m)`; arcs at `t=2πb/q, b≠0` cancel by aperiodicity.
7. Minor arcs: `sg_circle.t_weyl_vinogradov` gives `|φ_X(t)| ≤ 1 - c·dist(t,2πℤ)^2`; integral contributes `O(q·n^{-1})`.
8. `sg_circle.t_combine_main_error` assembles main + error.

**Inherited vs. added**: *Inherited*: `s_central_limit_theorem`, `s_characteristic_function_of_sum`, all of `sg_circle_method`, character orthogonality. *Added*: combining character orthogonality *inside* the circle-method decomposition to produce residue-class asymptotics with explicit error.

**Novelty**: **LIKELY-KNOWN-UNDER-OTHER-NAME** (probably TRIVIAL under the right name). This is a **local limit theorem for lattice distributions on APs**. The `O(q·n^{-1})` error matches Davenport *Multiplicative Number Theory* and Petrov *Limit Theorems* Ch. VII; the proof is essentially Esseen-smoothing local CLT + character orthogonality. Point 3 (uniform up to `n^{1/2}`) is Bombieri-Vinogradov-style and almost certainly strictly harder than the circle-method decomposition alone. **Do not claim novelty.** The only graph-level contribution is making the residue-class refinement edge explicit.

**Failure modes**:
- `X` periodic (period > 1): aperiodicity fails; `P(S_n=m)` lives on a sublattice.
- Heavy tails `E[X^3]=∞`: Taylor fails, error degrades.
- `q > n^{1/2}`: minor arc dominates, statement vacuous.

**Proof-integrity risk**: **LOW** for 1-2 (textbook); **HIGH** for 3 (genuine Bombieri-Vinogradov strength).

---

## Candidate B4 — Walsh Spectrum of the Provability Predicate

**Derivation chain**: `s_self_referential_godel_sentence_G --[t_frequency_decomposition]--> T_B4`. Cross-cluster #3 in recon: C04 technique pushed onto C07 self-reference state.

**Statement (plain)**: View the provability predicate as a Boolean function on Gödel-numbered formulas. Walsh–Fourier decomposition reveals that provable sentences, as a subset of `{0,1}^N`, have a concentrated low-degree Walsh spectrum reflecting bounded quantifier depth of proofs; the Gödel sentence `G` itself is a sparse Walsh vector, an analytic fingerprint of diagonalisation.

**Statement (formal)**:
`T` consistent r.e. ⊇ PA, Gödel numbering `⌜·⌝`. Let `1_Prov_L: 2^N → {0,1}` = indicator of Gödel numbers of sentences with a `T`-proof of length ≤ `L`. Walsh transform `f̂_L(S) = 2^{-N} ∑_x (-1)^{S·x} 1_Prov_L(x)`.

1. *(corollary)* `1_Prov = lim 1_Prov_L` is r.e. not recursive (`s_godel_incompleteness`).

2. *(new claim)* Walsh spectrum is low-degree concentrated: `∑_{|S|>k} |f̂_L(S)|^2 ≤ L · 2^{-N/2} · e^{-c·k/log L}`.

3. *(speculative)* `G_T` has at most `O(log N)` Walsh coefficients above `2^{-N/3}`.

**Derivation sketch**:
1. Hypotheses of `s_self_referential_godel_sentence_G`.
2. Invoke `sg_godel_numbering`: `s_formal_system, t_prime_power_encoding, s_gödel_numbers, t_primitive_recursive_predicates, s_representable_relations, t_fixed_point_lemma, s_self_referential_sentence`. Gödel numbers bijective with bit-strings.
3. `1_Prov_L` is total recursive (bounded search over proofs ≤ L).
4. Apply `t_frequency_decomposition` (Walsh on `{0,1}^N`).
5. *External fact*: LMN (Linial–Mansour–Nisan 1993): depth-`d` size-`s` AC^0 circuits have Walsh mass concentrated on levels ≤ `k` up to `s·2^{-k/O(d)}`.
6. Proof-verifier is depth `O(log L)`, size `poly(L,N)` (parallel axiom/rule-check).
7. Apply LMN: `∑_{|S|>k}|f̂_L(S)|^2 ≤ poly(L,N)·2^{-k/O(log L)}`.
8. For point 3: `G_T` comes from a primitive-recursive fixed point (`t_fixed_point_lemma`); Bourgain-style spectrum bounds for AC^0-like functions give sparsity.

**Inherited vs. added**: *Inherited*: `s_self_referential_godel_sentence_G`, `s_godel_incompleteness`, `sg_godel_numbering`. *Added*: `Prov` as Boolean function, LMN concentration for truncated provability, sparsity of `G_T`.

**Novelty**: **PLAUSIBLY-NEW**, with caveats. Ingredients are standard (LMN is 1993; bounded-depth provability verifiers are classical), but the specific combination "Walsh spectrum of provability" is, to my knowledge, not a named theorem. Closest neighborhood: Allender–Gore-type circuit lower bounds, Razborov's propositional proof complexity, Aaronson–Drucker-type circuit-Fourier connections. Risk: after proof-complexity literature diligence, may downgrade to COROLLARY-OF-KNOWN.

**Failure modes**:
- LMN requires constant depth; `L ≪ 2^{N/k}` regime only.
- Gödel numbering is not canonical; sparsity of `G_T` is numbering-dependent.
- `T` ω-inconsistent: `1_Prov` near-constant, spectrum collapses to `S=∅`.

**Proof-integrity risk**: **MEDIUM**. Point 2 tight (LMN is real); point 3 depends on a fixed-point-lemma circuit-depth bound not carefully checked.

---

## Candidate B5 — Syntactic Current (Conserved Quantity on the Proof Graph)

**Derivation chain**: `s_self_referential_godel_sentence_G --[t_conserved_quantity]--> T_B5`. Cross-cluster #4 in recon: C03 technique on C07 state, absent from graph.

**Statement (plain)**: Interpret the proof graph `Γ_T` as a discrete dynamical system on Gödel numbers; each inference rule moves a formula's quantifier depth by a definite amount. Then `J(φ→ψ)=q(ψ)−q(φ)` is a "syntactic current" which is conserved around every deduction cycle *except at fixed-point / diagonal substitutions*. The Gödel sentence `G` is the carrier of a non-zero holonomy class — incompleteness as a conservation-law obstruction.

**Statement (formal)**:
`T ⊇ PA` consistent r.e. `Γ_T` = directed graph with vertices = Gödel numbers of sentences, edges = one-step inferences. `q(φ)` = quantifier depth.

1. *(corollary)* `q` is non-increasing under cut-free inferences (Gentzen).

2. *(new claim)* `J(φ→ψ)=q(ψ)−q(φ)` has holonomy only around fixed-point diagonals: `h(G)=q(G)−q(¬Prov(⌜G⌝)) ≠ 0`, and this non-triviality is equivalent to `s_godel_incompleteness`.

3. *(speculative)* `G` uniquely (up to provable equivalence) maximizes `h` over diagonal fixed points; `h(G)=1`, the single quantifier-alternation of diagonalisation.

**Derivation sketch**:
1. Hypotheses: `s_self_referential_godel_sentence_G`, `sg_godel_numbering`.
2. Construct `Γ_T` (external).
3. `sg_godel.t_primitive_recursive_predicates`: each rule computable on Gödel numbers.
4. Apply `t_conserved_quantity`: seek vertex-potential with zero differential along edges.
5. *External fact*: `q` is Gentzen-monotone under cut-free rules; can increase at instantiation but only by bounded amount.
6. `J` is the discrete differential of `q`; `∑J=0` on cycles avoiding diagonalisation.
7. `sg_godel.t_fixed_point_lemma`: `G ↔ ¬Prov(⌜G⌝)`. Compute `h(G)`.
8. Invoke `s_godel_incompleteness`: `G` not connected to `⊤` or `⊥` by finite `J`-balanced path.
9. Reformulate: incompleteness ↔ non-trivial holonomy class in `H^1(Γ_T; ℤ)`.

**Inherited vs. added**: *Inherited*: `s_self_referential_godel_sentence_G`, `sg_godel_numbering`, `s_godel_incompleteness`, Gentzen. *Added*: reformulation as holonomy; potential function `q`.

**Novelty**: **LIKELY-KNOWN-UNDER-OTHER-NAME**. Topos-theoretic / category-theoretic Gödel (Lawvere's diagonal argument, Yanofsky, Joyal arithmetic universes) express the same fixed-point-obstruction idea. Gentzen cut-elimination has been recycled by Buss, Kohlenbach, Girard. The "syntactic current" is likely a reformulation of Gentzen ordinal assignment `ε_0`. Overlap: ordinal proof theory, Kreisel no-counterexample, Girard proof-nets.

**Failure modes**:
- `q` not canonical — depends on formalism.
- Non-classical logic: `q` changes meaning.
- Rosser's sentence has different `h` than Gödel's when ω-consistency fails.

**Proof-integrity risk**: **MEDIUM–HIGH**. "Holonomy class" needs proper formalisation (likely `Ext^1` in a proof-theoretic derived category), which risks collapsing into known ordinal proof theory.

---

## Candidate B6 — Sylow Density via Pigeonhole on Conjugation Orbits

**Derivation chain**: `s_set_of_p_subgroups_with_G_action --[t_pigeonhole_collision]--> T_B6`. Cross-cluster #10 in recon: C11 technique pushed onto C03 state.

**Statement (plain)**: For finite `G` with `p^k || |G|`, define two Sylow `p`-subgroups as ε-close if they share `≥(1-ε)·p^k` elements. A pigeonhole argument bounds the number of ε-equivalence classes in `Syl_p(G)` by `(1/ε)^{p^k}`, a bound *independent of `|G|`*.

**Statement (formal)**: `d(P,Q)=1-|P∩Q|/p^k` on `Syl_p(G)`.

1. *(corollary)* `|Syl_p(G)| ≡ 1 mod p` — classical `s_sylow_theorems`.

2. *(new claim)* For `ε∈(0,1)`, `Syl_p(G)` has a cover by `≤(1/ε)^{p^k}` ε-balls, independently of `|G|`.

3. *(speculative)* Tightness: for each `k,ε` there exist `G` with `|Syl_p(G)|` unbounded but cover size reaching `(1/ε)^{Θ(p^k)}`.

**Derivation sketch**:
1. Hypotheses of `s_set_of_p_subgroups_with_G_action`.
2. Invoke `s_sylow_theorems`: existence, conjugacy, count.
3. Each Sylow is a size-`p^k` subset of `G`; view `Syl_p(G)` inside a Hamming space.
4. Apply `t_pigeonhole_collision`: compact Hamming-type space of covering dimension `D` admits `(1/ε)^D` covers.
5. Covering dimension ≤ `p^k` (points in `G^{p^k}` up to permutation).
6. Conclude bound.
7. Tightness (3): external construction `G=H×H×…×H` for controlled blow-up.

**Inherited vs. added**: *Inherited*: `s_set_of_p_subgroups_with_G_action`, `s_sylow_theorems`, conjugacy. *Added*: Hamming reformulation, `|G|`-independent bound, covering-dimension estimate.

**Novelty**: **LIKELY-KNOWN-UNDER-OTHER-NAME** for 1-2; **PLAUSIBLY-NEW** for 3. Overlap: Pyber, Liebeck–Pyber on almost-equal / commensurable subgroups, asymptotic group theory. The volume-covering argument is folk. Point 3's tight construction less clearly known.

**Failure modes**:
- `G` abelian: unique Sylow, cover is trivially one ball.
- `p=2, k` small: overlap distance coarse; bound `(1/ε)^{2^k}` possibly loose.
- `PSL_n(𝔽_q)` large-`n`: check whether `|Syl_p|` exceeds the bound for small `ε`.

**Proof-integrity risk**: **MEDIUM**. Step 4's covering-dimension on a conjugation-quotiented Hamming space is the non-trivial step; probable need for a log-factor correction.

---

## Candidate B7 — Quantitative Waring via Refined Farey Dissection

**Derivation chain**: `s_hilbert_waring_theorem ← t_circle_method` already exists; push `t_major_minor_arc_decomposition` (currently only on `s_vinogradov_three_primes_theorem`) onto Waring's problem with a deeper dissection.

**Statement (plain)**: By refining the standard Farey dissection of the circle-method integral — using a three-level major/intermediate/minor arc split with optimised singular series — the Waring asymptotic constant `G(k)` admits the bound `G(k) ≤ (1+ε)·k·log k` for `k` sufficiently large.

**Statement (formal)**: `r_{k,s}(N)` = # representations of `N` as `x_1^k+…+x_s^k`, `G(k)` = least `s` guaranteeing `r_{k,s}(N)>0` for large `N`.

1. *(corollary)* `G(k) < ∞` — this is `s_hilbert_waring_theorem`.

2. *(new — quantitative)* For every ε>0, there is `k_0(ε)` with `G(k) ≤ (1+ε)·k·log k` for `k ≥ k_0`. Proof: three-level Farey dissection + optimised singular-series estimate from `sg_circle.t_singular_series_local_euler`.

3. *(speculative)* `G(k) = (1+o(1))·k·log k`; Hardy–Littlewood `G(k) ≥ k+1`.

**Derivation sketch**:
1. Hypotheses of `s_hilbert_waring_theorem`.
2. Invoke `sg_circle_method`: `r_{k,s}(N) = ∫ F(α)^s e^{-2πiαN}dα`, `F(α) = ∑_{x≤N^{1/k}} e^{2πiαx^k}`.
3. `sg_circle.t_farey_dissection`: partition `[0,1]` into major arcs `q ≤ Q` and minor arcs.
4. `sg_circle.t_singular_series_local_euler`: major-arc main ≈ `N^{s/k-1}·𝔖(N)·𝒥(N)`.
5. Apply `t_major_minor_arc_decomposition` at a second level: subdivide major arcs by `q`-size; intermediate arcs get Weyl–van der Corput bounds.
6. `sg_circle.t_weyl_vinogradov`: `|F(α)| ≤ C·N^{1/k-σ(k,s)}` on minor arcs.
7. Minor-arc dominance: need `s·σ(k,s) > s/k-1`.
8. *External*: Vinogradov mean-value — resolved 2016 by Wooley and Bourgain–Demeter–Guth: `σ(k,s) ≥ (s-k^2)/(2sk)` for large `s`.
9. Substitute: `s ≥ k·log k·(1+o(1))` suffices.

**Inherited vs. added**: *Inherited*: `s_hilbert_waring_theorem`, `sg_circle_method`, Vinogradov mean-value (external). *Added*: the quantitative `(1+ε)·k·log k` bound fed by the Wooley/BDG input; three-level Farey refinement.

**Novelty**: **LIKELY-KNOWN-UNDER-OTHER-NAME**. Point 2 is essentially the Vaughan–Wooley state-of-the-art on `G(k)`, see Vaughan *The Hardy-Littlewood Method* 2nd ed. Ch. 5. The 2016 Vinogradov resolution gave exactly this ceiling. Point 3 is the asymptotic Hardy-Littlewood heuristic, open. Graph contribution: filling the missing `(Waring, quantitative)` edge — not new mathematics.

**Failure modes**:
- Small `k` (4–6): known explicit bounds (Davenport `G(4)≤16`) beat the asymptotic.
- Singular-series vanishing: must exclude local obstructions.
- Pre-asymptotic `N`: major-arc main not dominant.

**Proof-integrity risk**: **LOW**, conditional on Wooley/BDG input. Skeleton is standard `sg_circle_method`.

---

## Summary table

| # | Candidate | Technique pushed | Target seed | Novelty grade | Proof-integrity risk |
|---|-----------|------------------|-------------|---------------|----------------------|
| B1 | Spectral Noether | `t_frequency_decomposition` | `s_infinitesimal_action_variation` | COROLLARY-OF-KNOWN | LOW |
| B2 | Polynomial-method Mordell | `t_polynomial_method` | `s_curve_inside_abelian_variety` | LIKELY-KNOWN-UNDER-OTHER-NAME | MEDIUM |
| B3 | Local CLT on APs | `t_circle_method` + `t_major_minor_arc_decomposition` | `s_limit_characteristic_function_equals_gaussian` | LIKELY-KNOWN-UNDER-OTHER-NAME (TRIVIAL for ptwise; HIGH for uniform) | LOW/HIGH split |
| B4 | Walsh spectrum of provability | `t_frequency_decomposition` | `s_self_referential_godel_sentence_G` | PLAUSIBLY-NEW | MEDIUM |
| B5 | Syntactic current | `t_conserved_quantity` | `s_self_referential_godel_sentence_G` | LIKELY-KNOWN-UNDER-OTHER-NAME | MEDIUM–HIGH |
| B6 | Sylow density bound | `t_pigeonhole_collision` | `s_set_of_p_subgroups_with_G_action` | LIKELY-KNOWN-UNDER-OTHER-NAME (pt3 PLAUSIBLY-NEW) | MEDIUM |
| B7 | Quantitative Waring | `t_major_minor_arc_decomposition` (deeper) | `s_hilbert_waring_theorem` | LIKELY-KNOWN-UNDER-OTHER-NAME | LOW |

## Meta-observation

Of 7 candidates: **0 TRIVIAL, 0 SPECULATIVE(-only), 1 COROLLARY-OF-KNOWN, 5 LIKELY-KNOWN-UNDER-OTHER-NAME, 1 PLAUSIBLY-NEW** (B4, with caveats).

**Priority for the problem-solver**:
- **B4** is the only candidate I consider plausibly-new at the "statement" level. The Walsh-spectrum concentration of truncated provability is an instance of LMN applied to a proof-verifier, which is mechanical; what is *not* mechanical is point 3 (sparsity of the Gödel sentence). B4 should be the candidate to verify first. Its literature risk is in proof complexity (Razborov, Aaronson, Krajíček on Fourier and circuit lower bounds on formal systems).
- **B1, B3, B7** are honest re-derivations of classical facts. Their value is purely graph-maintenance: the graph has no edge from `s_infinitesimal_action_variation` to mode-wise Noether, from `s_characteristic_function_of_sum` to a residue-class refined CLT, or from `s_hilbert_waring_theorem` to the Vaughan–Wooley `G(k) ≤ k log k` ceiling. These should be added as enrichment edges, not as new theorems.
- **B2, B5, B6** sit in literatures where specialist overlap is likely but not verified. A one-pass literature check (Dimitrov–Gao–Habegger for B2; Girard/Yanofsky for B5; Pyber/Liebeck for B6) will decide each. If any turns out to be genuinely missing from the literature, it is a modest but real contribution.

**The general lesson of this recon-driven exercise**: applying well-known techniques to well-known terminal theorems rarely produces new mathematics; it more often produces "graph-completion" — explicit edges that the specialist community has known for decades but that the knowledge graph does not yet encode. "Never pushed in the graph" and "never pushed in the literature" are *very* different properties. The recon's identification of forward-boundary states is a reliable way to find edges the graph is missing; it is a less reliable way to find theorems the literature is missing. The one exception in this batch (B4) is where a cross-field combination (proof theory × Boolean Fourier analysis) was structurally implicit in the graph's C07×C04 gap and happens not to be a well-trodden combination in the literature either. That intersection — graph-missing *and* literature-missing — is the honest discovery target. Seven candidates gave one such intersection; by extrapolation, the remaining C07×C04, C07×C11, and C07×C12 gaps are where a second round should look.
