# Problem-Solver Tests — Concrete Probing of A1-A7, B1-B7

**Role**: problem solver on 7-person research team. Each of the 14 candidates
has been put through (a) specific small examples computed by hand/Python,
(b) counterexamples at flagged and unflagged edges, (c) derivation-step audits
where at least two steps were re-computed, (d) boundary/degenerate tests.

Source: `theorist_A_candidates.md`, `theorist_B_candidates.md`,
`recon_leverage_points.md`.

---

## Candidate A1 — Grothendieck–Galois via the Colimit Lift

- **Concrete test 1 (𝔽₂ case).** Finite separable extensions of 𝔽₂ are
  exactly 𝔽_{2ⁿ}, one per n≥1. Gal(𝔽_{2ⁿ}/𝔽₂) = ℤ/n (Frobenius x↦x²).
  Inverse limit under divisibility is ℤ̂ = ∏_p ℤ_p. Finite continuous
  ℤ̂-sets = ⊔_n ℤ/nℤ-sets. The equivalence FinSep(𝔽₂)^op ≃ FinCont-ℤ̂-Set
  sends 𝔽_{2ⁿ} ↦ ℤ/n. Textbook Grothendieck–Galois.
- **Concrete test 2 (inseparable edge).** K=𝔽_p(t), L=𝔽_p(t^{1/p}).
  Gal(L/K) trivial although [L:K]=p. Statement correctly restricted to
  FinSep(K); purely inseparable excluded.
- **Concrete test 3 (K=K̄ degenerate).** FinSep(K) = {K}, Gal(K̄/K) trivial,
  both categories one-object. Vacuous but holds.
- **Derivation step audit.** Step 3 (L₁⊆L₂ → Gal(L₂/K)→Gal(L₁/K)): the
  standard restriction map with kernel Gal(L₂/L₁); correct. Step 6 (Krull
  topology) is EXTERNAL: I grep'd the graph for "Krull topology" — zero
  hits. Genuinely not in the graph (as the theorist flagged). The topology
  is the projective-limit topology; cofinite-index normal subgroups form a
  basis at identity (Krull 1928).
- **Verdict: SURVIVES-TESTS.** SGA1 Exp. V, classical.
- **Notes.** Value purely graph-hygiene (colimit edge is genuinely missing).

## Candidate A2 — Representable-Functor Formulation of Stone Duality

- **Concrete test 1 (B = P({a,b})).** 4-element Boolean algebra.
  Hom_BA(B, **2**) = principal ultrafilters at a or b. Spec(B) = {a,b}
  discrete Stone space. Clopen({a,b}) has 4 elements = B. Yoneda identifies
  both directions.
- **Concrete test 2 (distributive-lattice edge).** Open sets of [0,1]:
  distributive but not Boolean. Replacing **2** by Sierpiński {0<1} gives
  Priestley duality for distributive lattices. Statement correctly
  restricted to BoolAlg.
- **Concrete test 3 (ZF edge).** Spec(B) requires BPI (Boolean prime ideal
  theorem, weaker than AC). In ZF without BPI, Spec(B) may be empty for
  non-trivial B — duality fails. Correctly flagged.
- **Derivation step audit.** Step 2 (ultrafilters of B = Hom(B, **2**)):
  an ultrafilter assigns 0/1 to each element consistent with Boolean ops;
  this is a Boolean hom. Step 5 (Yoneda uniqueness): two representing
  objects are uniquely isomorphic. Both safe.
- **Verdict: SURVIVES-TESTS.** Johnstone *Stone Spaces* §VI.3.
- **Notes.** Stone embedding B ↪ **2**^{Spec B} falls out by Yoneda; no
  new content.

## Candidate A3 — Forcing-Parametrised Stone Duality

- **Concrete test 1 (trivial P).** Spec_P(B) = Spec(B). Core reduces to
  classical Stone duality.
- **Concrete test 2 (Cohen, B = free BA on ω).** Spec(B) = 2^ω (Cantor).
  Cohen-forcing adds a real r; η: Spec^V(B) → Spec_P(B) is nontrivial on
  Aut — the Balcar-Simon / Rudin / Shelah–Veličković fingerprint is
  precisely this nontriviality (known for ω* = βω\ω).
- **Concrete test 3 (distributive forcing).** Lévy collapse Col(ω₁, ω) is
  (ω₁, ∞)-distributive: no new reals. For countable B, η_P is the identity.
  Failure mode correctly flagged.
- **Derivation step audit.** Step 3 (P-generic G gives Boolean hom B→**2**):
  correct if B is interpreted as the regular open algebra ro(P), so G
  corresponds to a truth-evaluation. Step 5 (absoluteness of "compact
  Hausdorff" under set forcing): correct; the property is Δ₁ in the
  relevant parameters.
- **Verdict: SURVIVES-WITH-CAVEAT.** Core definition SURVIVES.
  Fingerprint conjecture (general P, general B) is genuinely open.
- **Notes.** Core is LIKELY-KNOWN-UNDER-OTHER-NAME (Scott-Solovay-Vopěnka);
  generalization beyond ω* is the speculative piece.

## Candidate A4 — Compactness Closure for Cyclic Quadrilaterals (Poncelet n=4)

- **Concrete test 1 (Fuss/Cayley n=4 condition, bicentric).** I chose R=2,
  r=1 and solved Fuss' theorem 2r²(R²+d²) = (R²−d²)² for d, getting
  d² ≈ 0.8769, d ≈ 0.9364. Simulated the Poncelet map φ on C (Python,
  exact up to floating precision) starting from five initial angles
  θ₀ ∈ {0, π/4, π/2, 2.3, −1.5}. After 4 iterations, all five closed with
  error < 3·10⁻¹⁴. Poncelet n=4 closure verified numerically.
- **Concrete test 2 (concentric n=4 edge).** Concentric circles R=2,
  r varies. For r = R cos(π/4) = √2 ≈ 1.4142, closure at n=4 holds
  exactly (numerical error 3·10⁻¹⁵). For r=1.0 (NOT satisfying the
  concentric n=4 condition), all starting angles give |P₄ − P₀| = 3.464,
  clearly NOT closing. Consistent with Cayley obstruction.
  **Note the theorist's failure mode has a bug**: the condition "radius
  ratio not tan²(π/8)" is WRONG. For concentric n=4, the Cayley condition
  is r/R = cos(π/4) = 1/√2 ≈ 0.707, NOT tan²(π/8) ≈ 0.172. Tan²(π/8) is
  the r/R for a different Cayley case (probably n=8 or similar).
- **Concrete test 3 (n=3 and n=5 sanity).** Concentric n=3: r = R/2 = 1.0.
  Simulated 3-step closure: error < 3·10⁻¹⁵. Good. Concentric n=5:
  r = R cos(π/5) ≈ 1.618 (golden-ratio). Simulated 5-step closure: error
  < 6·10⁻¹⁵. Good. Same compactness argument handles all n.
- **Derivation step audit.** Step 3 (φ continuous): true — tangent-line to
  inner circle from external point varies smoothly with base point, and
  tangent-line meets outer circle at unique second point, smooth function.
  Step 6 (elliptic-curve translation structure, Griffiths–Harris 1977):
  EXTERNAL FACT, not in graph. The Poncelet-to-elliptic-curve translation
  is well-known: the map φ is a translation on E = double cover of C
  branched over four tangency points. Correctly flagged.
- **Verdict: SURVIVES-TESTS** for the closure statement itself. **BROKEN**
  for the specific "tan²(π/8)" failure-mode formula. Core theorem classical.
- **Notes.** Poncelet (1822); Bos–Kers–Oort–Raven (1987) give the
  compactness-route proof. Grading COROLLARY-OF-KNOWN accurate. The
  tan²(π/8) typo is the kind of error that a problem solver catches
  immediately in a numerical sandbox — a caution about "self-reviewed
  failure modes." Theorist's flagged `(R-d)^2` would more plausibly appear
  in Fuss' formula, so I suspect the original intent was "not Fuss' value
  for d given R,r" rather than "tan²(π/8)".

## Candidate A5 — Cohomological Obstruction to Invariant Subspaces

- **Concrete test 1 (compact T).** T = diag(1, 1/2, 1/3, …). σ(T) countable
  with 0 accumulating. H¹(σ(T), Aut) = 0 (totally disconnected → Čech
  1-cohomology vanishes). So ω_T = 0; span{e₁,…,e_k} is T-invariant.
  Aronszajn–Smith recovered.
- **Concrete test 2 (Volterra, quasinilpotent).** Vf(x)=∫₀^x f(t)dt on L²[0,1],
  σ(V) = {0}. H¹ of a single point = 0 trivially, so ω_V = 0 vacuously.
  V has invariant subspaces M_a = {f : f|_{[0,a]}=0} but the sheaf argument
  yields NO information about WHY. The obstruction class is CONTENT-FREE
  on quasinilpotent.
- **Concrete test 3 (non-normal, σ(T) connected).** ω_T = 0 becomes a
  restatement of ISP existence — no new content.
- **Derivation step audit.** Step 3 (sheaf from spectral measure for normal T):
  stalk H/(T−λ)H̄ well-defined. Step 4 (Apostol decomposition): EXTERNAL
  (Apostol 1968, "Spectral capacity"). Correctly flagged.
- **Verdict: SURVIVES-WITH-CAVEAT.** Valid reformulation; content-free on
  hard case (quasinilpotent) where ISP is open.
- **Notes.** Eschmeier-Putinar (1996) has this framework. Wiring only.

## Candidate A6 — Dyadic Martingale Structure for Archimedes' Polygons

- **Concrete test 1 (numerical rate of convergence).** L_n^in = N_n·2sin(π/N_n)
  with N_n = 3·2ⁿ. Computed:
  - n=5 (N=96): 2π − L_5^in = 1.121·10⁻³
  - n=10 (N=3072): 2π − L_10^in = 1.095·10⁻⁶
  - n=15 (N=98304): 2π − L_15^in = 1.070·10⁻⁹

  The candidate claims rate π³/(9·2²ⁿ). Comparing at n=5: claimed
  = 3.364·10⁻³; true ratio π³/(9·4ⁿ) ≠ measured. The correct Taylor
  expansion gives 2π − L_n^in ~ π³/(3·N_n²) = π³/(3·9·4ⁿ) = π³/(27·4ⁿ).
  **The candidate's rate is off by factor of 3**: claimed π³/(9·4ⁿ);
  correct π³/(27·4ⁿ). At n=5, 2π − L_5^in numerically ≈ 1.121·10⁻³, which
  matches π³/(27·4⁵) ≈ 1.121·10⁻³ exactly. The claim is wrong by factor 3.
- **Concrete test 2 (Koch snowflake edge).** Replace circle by Koch
  snowflake: length diverges (fractal, not rectifiable). Archimedes'
  doubling still produces inscribed/circumscribed polygonal sequences
  but with UNBOUNDED perimeter. Dyadic filtration still refines a σ-algebra
  but the "length" functional is not L¹-integrable in the limit.
  Theorist's failure mode "rectifiability used crucially" is correct.
- **Concrete test 3 (trisection instead of bisection).** If we trisect
  arcs, the filtration on circle becomes triadic, not dyadic. Still a
  martingale w.r.t. its own filtration; Doob still applies. So "non-regular
  refinements" doesn't universally break — only bisection-specific identities
  (half-angle) fail. The theorist's failure mode is overstated.
- **Derivation step audit.** Step 2 (structural isomorphism between
  doubling lattice and dyadic filtration): questionable phrasing. The
  DOUBLING of polygon vertex count corresponds to BISECTION of arcs, which
  IS a dyadic filtration of the circle's σ-algebra. Identification is sound.
  Step 4 (Doob martingale convergence in graph): **I grep'd — `s_doob_martingale_convergence`
  IS in the graph** (as node 5387). So the "flag as possibly missing" was
  unnecessary; Doob is already wired.
- **Verdict: SURVIVES-WITH-CAVEAT.** The martingale reading is FORMALLY
  correct but VACUOUS as stated: L_n^in is a CONSTANT random variable on
  the probability space (C, Haar), and constant increasing sequences are
  trivially submartingales. The specific claim "half-angle identity IS the
  conditional expectation formula" is a rhetorical flourish — half-angle
  is a recursion, not a conditional expectation identity. Rate off by factor
  of 3.
- **Notes.** Grading COROLLARY-OF-KNOWN accurate. The idea of "Archimedes
  as martingale" is more metaphor than math. The genuine content (monotone
  convergence of inscribed/circumscribed perimeters) predates Doob by
  ~2200 years. Value is purely wiring.

## Candidate A7 — Character-Decomposition of S₅ Orbits on Splitting Fields

- **Concrete test 1 (character table verification).** S₅ has 7 conjugacy
  classes (sizes 1, 10, 15, 20, 20, 30, 24 totaling 120 = 5!) and seven
  irreducibles (dims 1, 1, 4, 4, 5, 5, 6; sum of squares = 120).
  χ_std takes values (4, 2, 0, 1, −1, 0, −1). I verified all 28
  orthogonality relations ⟨χ_i, χ_j⟩ = δ_{ij} numerically.
- **Concrete test 2 (THE claim with counterexample).** For H = S₄
  (stabilizer of 5 in S₅, solvable, order 24) I computed by Frobenius:
  ⟨Ind_{S₄}^{S₅} 1, χ_std⟩ = (1/24)(χ(id)·1 + χ((12))·6 + χ((12)(34))·3
  + χ((123))·8 + χ((1234))·6) = (1/24)(4+12+0+8+0) = **1**, not zero.
  This matches the standard fact Ind_{S₄}^{S₅} 1 = permutation rep on 5 cosets
  = triv + std. S₄ is solvable and does NOT contain A₅ — so the candidate's
  claim "vanishes unless H contains A₅" is FALSE for unrestricted H.
  If instead we require NORMAL chains from S₅ (as the candidate's wording
  may intend), the only nontrivial chain is S₅ ⊃ A₅ ⊃ {e} (A₅ simple
  so no refinement), and A₅ is automatically in the chain. The claim is
  then VACUOUSLY TRUE.
- **Concrete test 3 (solvable quintic x⁵−2, Gal = F₂₀).** F₂₀ ≅ ℤ/5 ⋊ ℤ/4,
  solvable, transitive on 5 points. Ind_{F₂₀}^{S₅} 1 has dim 120/20 = 6,
  and χ_std DOES appear as constituent (the 5-dim transitive perm rep ⊃ std).
  So solvable Gal does not prevent χ_std from appearing in an induced rep.
- **Derivation step audit.** Step 3 (character table): correct. Step 4:
  "H acts transitively on 5 points ⇒ H ⊇ A₅" is WRONG — F₂₀, D₅, ℤ/5 all
  act transitively on 5 points and are solvable, not containing A₅.
- **Verdict: BROKEN-AS-STATED.** Claim is false (unrestricted chains) or
  vacuous (normal chains only).
- **Notes.** The correct obstruction is that S₅ is NOT an M-group: χ_std
  is not induced from a 1-dim rep of any subgroup. No subgroup of order 30
  exists in S₅ (verified via Sylow structure of A₅). This IS the
  character-theoretic Abel-Ruffini obstruction, but the candidate's
  formulation mangles it.

## Candidate B1 — Spectral Noether Theorem

- **Concrete test 1 (free Klein–Gordon + U(1)).** L = |∂φ|² − m²|φ|²,
  φ → e^{iα}φ. Noether current j^μ = i(φ*∂^μφ − c.c.). Mode-wise Q(k) =
  |a(k)|² − |b(k)|² (particle number at momentum k). Conserved mode-wise
  because free modes decouple. Peskin-Schroeder Ch. 2.
- **Concrete test 2 (Lorentz boost).** K = x∂_t + t∂_x. [K, ∂_x] = ∂_t ≠ 0.
  Boost does NOT commute with translation; Fourier modes mix. Hypothesis
  "X commutes with spatial translation" correctly excludes boosts.
- **Concrete test 3 (φ⁴).** Interaction ∫ φ̂(k₁)φ̂(k₂)φ̂(k₃)φ̂(k₄)δ(∑k)dk
  couples modes. Only total Q = ∫Q(k)dk conserved. Correctly flagged.
- **Derivation step audit.** Step 4 (Parseval factorisation of S): correct
  for quadratic L; fails for interactions. Step 5 (mode-wise EL equations):
  correct for free theory. Consistent with stated hypotheses.
- **Verdict: SURVIVES-TESTS.** Textbook free-theory content.
- **Notes.** Coercivity bound |Q(k)| ≤ C(1+|k|)^m E^{1/2} is Sobolev-type;
  for U(1), Q(k) = |a(k)|² bounded by E/m (not E^{1/2}). Exact form
  depends on X. Weinberg QFT Vol 1 §7.4.

## Candidate B2 — Polynomial-Method Chabauty Bound

- **Concrete test 1 (y² = x⁵ − x, genus 2, rank 0).** Weierstrass points
  (0,0), (1,0), (−1,0) plus one ∞ point (odd-degree model) give
  #C(ℚ) ≥ 4. Jacobian rank 0.
  Candidate's bound: (2g−2)·p^{r/g} = 2·p^0 = **2**.
  Observed 4 ≥ 4. **Bound 2 contradicts observed 4**. BROKEN at r=0.
  The theorist's flagged failure modes don't include r=0.
- **Concrete test 2 (compare with Chabauty-Coleman, r=1, g=2, p=7).**
  Chabauty-Coleman: #C(ℚ) ≤ #C(𝔽₇) + 2r ≈ 10 + 2 = 12.
  B2: (2g−2)·p^{r/g} = 2·√7 ≈ 5.3. ASYMPTOTICALLY better — but
  polynomial-method on abelian variety is hand-waved.
- **Concrete test 3 (r = g − 1 edge).** B2 gives 2p^{1/2} for g=2, r=1;
  Chabauty gives p. B2 much better for large p, but relies on unverified
  polynomial-method extension.
- **Derivation step audit.** Step 5 (polynomial-method on abelian variety):
  on A dim g, dim H⁰(A, L^D) ~ D^g (Riemann-Roch), so D ≥ |H|^{1/g} for a
  polynomial to vanish on H. OK structurally. Step 6 (Bezout on A):
  intersection of a curve C ⊂ A with divisor V(F) depends on theta-class;
  the bound (2g−2)·D comes from genus formula on C, requiring care
  about how F restricts. Not routinely (2g−2)·deg(F) — depends on
  embedding. Details hand-waved.
- **Verdict: BROKEN-AS-STATED.** Contradicted at r=0 edge. Bezout step
  and polynomial-method-on-A are both open issues.
- **Notes.** Should downgrade to UNPROVEN-AS-STATED. Asymptotic bound
  p^{r/g} (if proven) would genuinely beat Chabauty-Coleman at large p.
  Closest established analog: Katz-Rabinoff effective Chabauty.

## Candidate B3 — Local CLT on Arithmetic Progressions

- **Concrete test 1 (Rademacher, period 2).** X_i uniform on {±1}.
  P(S_n = m) = C(n, (n+m)/2)/2ⁿ for m+n even; zero otherwise. Rademacher
  has period 2 (support differences all ±2), NOT aperiodic. Computed
  ∑_m |P_actual − (1/q)g_n(m)| over m ≡ 2 mod 5, m ∈ [−100,100], n=1000:
  0.1997 (large). Confirms aperiodicity is essential.
- **Concrete test 2 (aperiodic X).** X uniform on {−1, 0, 1}, gcd = 1.
  Textbook local CLT (Petrov Ch. 7) gives exactly
  P(S_n=m, S_n≡a mod q) = (1/q)g_n(m) + O(q/n) for q ≤ n^{1/2−ε}.
  Matches B3 point 2 verbatim.
- **Concrete test 3 (q > √n edge).** Error bound becomes loose; theorist
  correctly flags.
- **Derivation step audit.** Step 4 (character orthogonality): the identity
  (1/q)∑_b e^{2πib(S−a)/q} = 𝟙[S ≡ a mod q] is standard. Step 6 (Taylor
  on major arc): φ_X(t) = 1 − σ²t²/2 + O(|t|³E|X|³), giving Gaussian main
  after Fourier inversion. Correct.
- **Verdict: SURVIVES-TESTS.** Petrov Ch. 7, textbook.
- **Notes.** Point 2 is TRIVIAL at textbook level. Point 3 (uniform up to
  q = n^{1/2}) is Bombieri-Vinogradov-strong, genuinely harder and not
  given by circle method alone — theorist's bipartite risk grading is
  accurate. Graph edge is missing; wiring only.

## Candidate B4 — Walsh Spectrum of the Provability Predicate

**(Graded PLAUSIBLY-NEW; deepest test.)**

- **Concrete test 1 (toy Prov, N=5, random 4-element subset).** Computed
  Walsh coefficients: max |f̂(S)| = 4/32 = 0.125 (at S=∅). Mass by degree:
  0.016, 0.023, 0.039, 0.039, 0.008, 0. Mass is SPREAD, not concentrated.
  A random sparse indicator shows no low-degree concentration.
- **Concrete test 2 (singleton indicator).** f̂(S) = ±2⁻ᴺ for all S.
  Every coefficient has magnitude 2⁻ᴺ. For N ≥ 3, NO coefficient exceeds
  2^{−N/3}. So the candidate's claim "G_T has O(log N) coefficients above
  2^{−N/3}" is VACUOUSLY TRUE (zero exceed threshold) for a singleton G_T
  indicator — no useful content.
- **Concrete test 3 (AC⁰ benchmark: Maj3).** Majority has mass 3/4 at deg 1,
  1/4 at deg 3. Low-degree concentration genuine. But this requires the
  predicate to be an AC⁰-describable function of its inputs.
- **Derivation step audit.** Step 5 (LMN: depth-d size-s AC⁰ mass concentrates
  on levels ≤ k up to s·2^{−k/O(d)}): CORRECTLY stated (Linial-Mansour-Nisan
  1993). Step 6 (verifier depth O(log L), size poly(L, N)): **This is the
  failure.** Verifying a SINGLE proof of length L is depth O(log L), size
  poly(LN). BUT 1_Prov_L(x) = "there EXISTS a proof of length ≤ L proving x"
  is an OR over exp(O(LN)) proof-strings. The resulting circuit has size
  exp(O(LN)), not poly. LMN then gives bound exp(O(LN)) · 2^{−k/O(log L)},
  VACUOUS for k ≤ LN. **LMN applies to verifier-of-fixed-proof, not
  existence-of-proof.**
- **Verdict: BROKEN-AS-STATED.** The stated bound L·2^{−N/2}·exp(−ck/log L)
  is TOO STRONG relative to what LMN delivers for existence-of-proof.
  Additionally: Walsh spectrum is Gödel-numbering-dependent, so any "G_T
  sparsity" statement is not a mathematical invariant.
- **Notes.** This was the PLAUSIBLY-NEW candidate. The idea
  (Fourier-analyze provability) is attractive but the specific quantitative
  bound misapplies LMN at the key step. Correct version for fixed-proof
  verifier is trivial (AC⁰ fan-in small) and numbering-dependent.
  Proof-complexity literature (Razborov, Krajíček) studies related
  Fourier/circuit bounds, but none go by "Walsh spectrum of provability"
  because the core object is ill-defined under re-numbering. Grade should
  DOWNGRADE to LIKELY-INCORRECT-OR-TRIVIAL.

## Candidate B5 — Syntactic Current (Conserved Quantity on Proof Graph)

- **Concrete test 1 (propositional).** ⊢A, ⊢A→B ⊢ B: all q=0, J=0, no
  holonomy. Baseline trivial.
- **Concrete test 2 (∀ instantiation).** ⊢ ∀x (x+0=x) ⊢ 0+0=0. q(∀x P(x))
  = 1, q(P(0)) = 0. J = −1. But the right-∀-introduction rule (Γ⊢P(a)
  ⊢ Γ⊢∀xP(x)) INCREASES q by 1 in cut-free Gentzen. So q is NOT monotone
  cut-free. The correct monotone quantity in Gentzen is the ordinal < ε₀
  of the proof tree (ordinal descent), NOT quantifier depth.
- **Concrete test 3 (diagonal G ↔ ¬Prov(⌜G⌝)).** q(G) ≈ 1 (one quantifier
  from Prov inside); q(¬Prov(⌜G⌝)) ≈ 2 (negation + ∃). So h(G) ≈ −1,
  not the "+1 single quantifier alternation" the candidate speculates.
  Value is encoding-dependent anyway.
- **Derivation step audit.** Step 5 ("q Gentzen-monotone under cut-free"):
  FALSE — right-∀-introduction ADDS a quantifier. Step 9 (H¹(Γ_T; ℤ)
  nontrivial ⟺ incompleteness): no honest definition of cohomology on the
  proof graph is supplied.
- **Verdict: BROKEN-AS-STATED.** Quantifier depth is the wrong invariant.
- **Notes.** The intuition (diagonalization breaks a conservation law) is
  honest; the correct realization is Gentzen/Schütte/Girard ordinal proof
  theory, not a ℤ-valued syntactic current. Lawvere's / Yanofsky's
  fixed-point theorems subsume the categorical version.

## Candidate B6 — Sylow Density via Pigeonhole on Conjugation Orbits

- **Concrete test 1 (S₄, p=2).** Three 2-Sylow subgroups (|P| = 8 each),
  stabilizers of the three pairings of {1,2,3,4}. Computed: |P_i ∩ P_j| = 4
  (shared V₄) for all i ≠ j. So d(P_i, P_j) = 1 − 4/8 = 0.5 uniformly.
  All three share V₄. For ε = 0.5, cover size = 3, bound (1/ε)^{p^k} =
  2⁸ = 256, trivially satisfied.
- **Concrete test 2 (S₄, p=3).** |Syl₃| = 4, each order 3; pairwise
  intersections = {e}; d = 2/3. For ε = 0.5, cover = 4, bound (1/0.5)³ = 8.
  OK.
- **Concrete test 3 (S₃ × S₃, p=2).** |Syl₂| = 9 products of transpositions.
  Pairwise d ∈ {1/2, 3/4}. For ε = 0.4, cover = 9, bound (1/0.4)⁴ ≈ 39. OK.
- **Derivation step audit.** Step 4 (covering-dim ≤ p^k): the naive
  Hamming-covering bound on size-p^k subsets of G gives (1/ε)^{O(p^k log |G|)},
  which is |G|-DEPENDENT. The |G|-independence claimed requires careful
  quotienting by conjugation. This is a real technical gap, not a
  cosmetic step.
- **Verdict: SURVIVES-WITH-CAVEAT.** The concrete bound is plausible; the
  |G|-independence step needs justification.
- **Notes.** Pyber and Liebeck-Pyber have related density results.
  Tightness (point 3) would require an explicit construction; I did not
  find one.

## Candidate B7 — Quantitative Waring via Refined Farey Dissection

- **Concrete test 1 (small k).** G(4) ≤ 16 (Davenport 1939) → ≤ 12
  (Vaughan-Wooley). The asymptotic (1+ε)k log k at k=4 gives ≈ 5.5,
  but the asymptotic only applies for k ≥ k₀(ε). For small k, explicit
  bounds are better. Correctly flagged.
- **Concrete test 2 (asymptotic rate).** At k=100, (1+ε)·100·log 100
  ≈ 461. k log k grows faster than any k^{1+δ} — log factor is right.
- **Concrete test 3 (pre-asymptotic N).** Major-arc main doesn't dominate
  for small N; bound is about large N.
- **Derivation step audit.** Step 8 (Vinogradov mean-value, BDG 2016):
  CORRECTLY CITED. Bourgain-Demeter-Guth (2016) and Wooley's
  efficient-congruencing (2016) resolve the main conjecture. The exact
  form σ(k, s) ≥ (s − k²)/(2sk) is consistent with Wooley's bounds (one
  would need to reconcile indices). Step 9 (s ≥ k log k (1+o(1))
  suffices): standard circle-method arithmetic.
- **Verdict: SURVIVES-TESTS.** Vaughan-Wooley state-of-the-art after 2016.
- **Notes.** Edge `s_hilbert_waring → t_major_minor_arc` genuinely missing;
  wiring value is real. Point 3 (asymptotic equality) = Hardy-Littlewood,
  open.

---

## Summary table

| # | Candidate | Verdict | Most telling test |
|---|-----------|---------|-------------------|
| A1 | Grothendieck-Galois colimit | SURVIVES-TESTS | 𝔽₂ case computed |
| A2 | Representable Stone | SURVIVES-TESTS | P({a,b}) example |
| A3 | Forcing-Stone | SURVIVES-WITH-CAVEAT | Core OK; fingerprint speculative |
| A4 | Poncelet n=4 | SURVIVES-TESTS | Python Fuss+closure verified; minor bug in stated failure formula |
| A5 | Sheaf obstruction ISP | SURVIVES-WITH-CAVEAT | Volterra vacuously consistent |
| A6 | Archimedes martingale | SURVIVES-WITH-CAVEAT | Rate WRONG by factor 3 |
| A7 | S₅ character chain | BROKEN-AS-STATED | S₄ gives nonzero inner product |
| B1 | Spectral Noether | SURVIVES-TESTS | Klein-Gordon + U(1) |
| B2 | Polynomial Mordell | BROKEN-AS-STATED | r=0, g=2 explicit failure |
| B3 | Local CLT on APs | SURVIVES-TESTS | Textbook, Rademacher edge |
| B4 | Walsh provability | BROKEN-AS-STATED | LMN misapplied to existence-of-proof |
| B5 | Syntactic current | BROKEN-AS-STATED | q is wrong invariant; Gentzen uses ordinals |
| B6 | Sylow density | SURVIVES-WITH-CAVEAT | Covering-dimension step unclear |
| B7 | Quantitative Waring | SURVIVES-TESTS | Wooley/BDG 2016 |

**Breakdown**: 6 SURVIVES, 4 SURVIVES-WITH-CAVEAT, 4 BROKEN-AS-STATED,
0 UNTESTABLE.

**Biggest surprises**:
1. **B4 (the lone PLAUSIBLY-NEW)** is broken: LMN is applied to
   1_Prov_L as an AC⁰ circuit, but proof-existence requires an OR
   over exp(LN) proofs → circuit size exp(LN) → LMN bound is vacuous.
   The plausibly-new candidate turns out to misapply its key external fact.
2. **A6's rate is off by factor 3**: candidate says π³/(9·4ⁿ), correct is
   π³/(27·4ⁿ). Simple Taylor expansion computation finds this; the theorist's
   self-review didn't catch it.
3. **A7's "solvable chain" claim** is either false (with unrestricted chains,
   S₄ gives multiplicity 1 in Ind) or vacuous (with normal chains, every
   chain from S₅ contains A₅ by A₅'s simplicity). The character-theoretic
   analog of Abel-Ruffini exists but is stated in terms of M-groups /
   monomial representations, not the candidate's chain condition.
4. **B2's polynomial-method bound fails at r=0**: for the specific
   genus-2 curve y² = x⁵ − x, we have #C(ℚ) ≥ 4 but the candidate bound
   (2g−2)·p^{r/g} = 2. A factor-of-2 gap, caused by the polynomial-method
   extension to abelian varieties that B2 hand-waves.
5. **A4's failure mode formula is wrong**: "tan²(π/8)" should be "cos(π/4)
   = 1/√2" for the concentric n=4 Cayley condition. Easy to catch in
   simulation.
6. **A6's Doob reference**: theorist flagged uncertain presence in graph;
   in fact `s_doob_martingale_convergence` is node 5387 in the graph.
   The flag was over-cautious.
7. **B5's quantifier-depth argument**: q is NOT monotone under Gentzen
   cut-free rules (the ∀-introduction rule increases q). The correct
   monotone invariant is the ordinal < ε₀ of the proof tree (Gentzen's
   ordinal analysis). The "holonomy" framing is a metaphor, not a
   mathematical identity.

**Highest-value candidate after testing**: A3's representable
forcing-Stone. The core construction is a valid definition, the fingerprint
conjecture is genuinely open (and the ω* / PFA instance is known only for
ω*, not general P), and both the forcing step and the representable functor
step are in the graph. This is the least-damaged of the speculative
entries.

**Recommendation**: All BROKEN-AS-STATED candidates (A7, B2, B4, B5)
should be rewritten before being added to the knowledge graph — the
current statements contain errors that a careful referee would flag. The
SURVIVES entries (A1, A2, A4 core, B1, B3, B7) are textbook and can be
added as enrichment edges. A3, A5, A6, B6 should be added with caveats
explicitly noted. No candidate produces new mathematics at the "theorem"
level; the honest contribution is graph-completion, as the theorists
themselves noted in their meta-observations.
