# Integrity Audit — 3D Navier–Stokes iter-4 Proposals

**Role**: proof-integrity auditor on a 9-person team. Cold adversarial pass on the 17 attack proposals (M1.1–M1.6, G1–G6, A1–A5) plus the 4 new-technique nodes (B1–B4). Hunts: wrong inequality directions, missing hypotheses, scaling-computation errors, hand-waves, misattributed literature, circularity, norm conflation, forgotten decay/boundary conditions, mikado-flow pitfalls.

**Sources audited**: `ns_scout.md`, `mathematician_1_pde.md`, `mathematician_2_geometric.md`, `mathematician_3_vocabulary.md`, `problem_solver_tests.md`.

**Methodology**: per-proposal statement-coherence check → step-by-step audit with verdicts {VALID / MINOR-GAP / SERIOUS-GAP / WRONG} → probe the specific concerns flagged in the audit brief → cross-check cited literature → independent scaling-computation verification in Python → overall Verdict {PASS / PASS-WITH-MINOR-FIXES / SERIOUS-GAPS / BROKEN}.

---

## Part I — Proposal audits

### M1.1 — Logarithmically supercritical hyperdissipation

**Statement coherence.** Target is well-posed (α = 5/4 − c/log(1+|ξ|) global regularity); quantifiers on c, ν, and data class are present; domain 𝕋³ or ℝ³ is implicit but consistent with cited Tao 2009. *Missing hypothesis*: the Fourier multiplier must be a symmetric real positive operator; this is implicit but not stated, and for Littlewood–Paley / Bernstein to apply cleanly one should specify polynomial symbol class S^{5/2}_{1,0}, not just "morally log^c".

**Step-by-step audit.**
- **Step 1** [definition of D̂(ξ) = |ξ|^{5/2}/g(|ξ|), g(r) = r^{2c/log(2+r)}]: **WRONG.** Compute the asymptotics: log g(r) = (2c/log(2+r)) · log(r), so log g(r) → 2c as r → ∞, hence g(r) → e^{2c} (a constant). Numerical verification: at r = 10^12, g(r) = 1.2214… = e^{0.2} for c = 0.1. Thus the proposed dissipation is |ξ|^{5/2}/const, i.e. just α = 5/4 with ν rescaled by 1/e^{2c}. **This is not a log-correction at all.** M1.1's central claim — "weaker than Tao by one log" — is false as written; the formula gives a rescaling-equivalent to Tao's α = 5/4 case, not a weaker dissipation. Either a typo (the intended formula is plausibly g(r) = (log(2+r))^{c/log log(2+r)} or g(r) = log^{1/2−c}(2+r) matching a genuine log hierarchy), or conceptual confusion about what "log weaker" means.
- **Step 2** [Ḣ^s energy estimate]: VALID in principle but downstream of Step 1's error, the "critical" exponent s = 1/2 + ε₁ depends on what α actually is.
- **Step 3** [Bony decomposition, divergence-free kills one paraproduct]: VALID. Standard.
- **Step 4** [commutator [T_{u_low}, D^{1/2}] gives extra log^{-1}(|ξ_high|)]: **SERIOUS-GAP.** The standard Coifman–Meyer / Kato–Ponce commutator estimate for [T_a, D^σ] gains one DERIVATIVE (symbol class goes from S^σ to S^{σ−1}), not a log. A log-gain in the commutator would be a new result in multiplier theory, not a routine application. The proposal cites "Kato–Ponce / Christ–Weinstein" but those papers give derivative-order gain, not log-order gain. Failure mode 1 correctly identifies this as "the likeliest failure"; it is essentially a fatal flaw unless separately established. I could not locate the alleged log-gain commutator in the literature the proposal cites. **Circular suspicion**: if the log-gain were real, it would already have closed Tao 2009's threshold.
- **Steps 5–6** [Bernstein + sum closure, exponent 4c·log 2]: Numerical check confirms 4·ε(2^j)·j → 4c/log 2 ≈ 5.77c as j → ∞. So the exponent on 2^j in the bad sum is a FINITE constant ≈ 5.77c. That constant is always positive; it does not go to zero. So the bad sum looks like (constant)·block_energy², not (log 2^j)^{−1}·block_energy². The "log gain" is missing. Step 5 requires precisely the log^{−1} from Step 4 that the commutator literature does not deliver. **WRONG unless Step 4 rescued.**
- **Step 7** [Gronwall + contradiction]: standard technique, depends on Steps 4–6.
- **Step 8** [claim of strict improvement over Tao]: FALSE as a direct consequence of Step 1 analysis.

**Specific concerns verified.**
- The gain in hyperdissipative commutator bounds is *one derivative*, matching Bernstein exponent, not a log. Tao 2009 (arXiv:0906.3070) uses a Littlewood–Paley energy of precisely the form the proposal considers; if a log-gain commutator existed, Tao would have used it to push below α = 5/4. He did not.

**External facts.** Tao 2009, Katz–Pavlović 2002, Yamazaki 2015 cited correctly as references but their theorems do not imply the claimed commutator log-gain.

**Verdict**: **BROKEN** — scaling-computation error in the definition of g(r) plus an unsupported commutator log-gain. 

**Required fixes**: (a) restate g(r) as a genuine slowly-growing function (e.g. g(r) = (log(2+r))^σ for σ < 1/2 per Tao's hierarchy); (b) produce an actual proof or citation for the log-gain commutator, separately from Tao 2009's paraproduct machinery; (c) show that after these fixes the argument is not merely a restatement of Tao 2009. Without (a)+(b), the proposal is not improving on the known threshold.

---

### M1.2 — Carleman-sharpened quantitative ESS, triple-exp → double-exp

**Statement coherence.** Target precise: sharpen Tao 2019 for general data (non-axisymmetric). Hypotheses correctly include ‖u‖_{L^∞_t L³_x} ≤ A on [0,T). Missing: regularity of data (u₀ Schwartz is implicit, should be stated), whether domain is 𝕋³ or ℝ³ (the Carleman weight differs; Tao 2019 does ℝ³).

**Step-by-step audit.**
- **Step 1** [bubble identification]: VALID. This is Tao 2019 §4.
- **Step 2** [two-scale envelope k(t) = log₂(N_high/N_low)]: **MINOR-GAP.** The "smallest k(t) such that ‖Δ_{N_high} u‖_{L²} ≤ ‖Δ_{N_low} u‖_{L²}/2" implicitly assumes monotone dyadic decay of the enstrophy profile, which need not hold: LP profiles can have multiple peaks. If the profile is multi-modal, k(t) is not well-defined by this convention. Define k(t) = min{ k : max_{j ≥ k} ‖Δ_{N_low · 2^j} u‖_{L²} ≤ ‖Δ_{N_low} u‖_{L²}/2} to repair.
- **Step 3** [k = O(log A)]: **MINOR-GAP.** This bound comes from Bernstein + L² energy finite. Specifically ‖Δ_N u‖_{L²} ≤ ‖u‖_{L²} is uniform, and by Plancherel ‖u‖²_{L²} = Σ_j ‖Δ_j u‖², so only O(log(‖u‖_{L²}/δ)) levels can have amplitude ≥ δ. The claim is "k = O(log A)" but the bound actually depends on E₀ = ‖u₀‖_{L²}, not directly on A. Claiming k = O(log A) requires relating E₀ to A; in Tao 2019 this is done but with additional factors. Expected: k = O(log(E₀·N_low/‖Δ_{N_low} u‖_{L²})); this is *not* automatically O(log A).
- **Step 4** [Carleman back-propagation, one exponential of A times k]: **SERIOUS-GAP.** Tao 2019's Carleman back-propagation Prop. 5.9 has a constant that depends exponentially on the scale ratio N_high/N_low. Running the back-propagation across k dyadic levels does NOT obviously multiply constants by k linearly; it can compound multiplicatively by exp(A^c) per level, giving (exp(A^c))^k = exp(A^c · k) = exp(A^c · log A), which is subsumed into one exponential only if A^c · log A ≤ A^{c+o(1)}, which holds. OK, step 4 is technically correct conditional on the iteration behaving linearly in k rather than quadratically or exponentially, but the proposal does not substantiate that linearity. Failure mode 2 (self-admitted) is precisely this issue.
- **Step 5** [iterate]: VALID modulo Step 4.
- **Step 6** [net bound]: depends on Step 4.
- **Step 7** [third Carleman layer accepted]: correctly acknowledges this is not removed.
- **Step 8** [double-exponential]: VALID modulo Step 4.
- **Step 9** [averaging non-saturation check]: The claim that averaged NSE does not conserve energy "pointwise in frequency with the same structure" is weak. Tao's averaged NSE *does* preserve the energy identity by construction, and the scalar LP norms ‖Δ_N u‖_{L²} are exactly what survive averaging. So the two-scale envelope IS averaging-invariant, and the proposal's own §"Escapes the supercritical barrier?" honestly admits this: "the argument still works if we replace the nonlinearity by a Tao-averaged one that preserves energy". That self-admission is correct. The value of M1.2 is not barrier-escape but conditional-regularity sharpening — fine, but the §9 claim of non-saturation is unsupported.

**Specific concerns verified.**
- The two-scale envelope does not avoid the A^{O(A)} factor if the Carleman back-propagation is multiplicative per dyadic level (the most natural reading of Tao 2019). The proposal is essentially gambling that the constants add, not multiply, across levels. This gamble is not resolved in the derivation.
- Compare Palasek 2022 (arXiv:2108.09108): single-exp axisymmetric uses the one-parameter geometry of ω_θ/r boundedness, which is absent for general data. M1.2's claim is to get "one less exponential than Palasek" for general data — if that were easy, Palasek would presumably have done it. Caveat-worth investigating.

**External facts.** Tao 2019, Palasek 2022, Barker–Prange 2021 cited correctly.

**Verdict**: **PASS-WITH-MINOR-FIXES**. The proposal is internally consistent as a *conditional* quantitative sharpening; the barrier-escape claim (§9) is wrong (the proposal admits this elsewhere). Required fixes: (a) rigorous accounting of the per-level Carleman constant iteration (Step 4 bullet); (b) fix k(t) definition for multi-modal profiles (Step 2); (c) retract the §9 non-saturation claim explicitly.

---

### M1.3 — Larger-than-BMO⁻¹ critical space via Lipschitz-ξ

**Statement coherence.** Target is clean: define X = BMO⁻¹ + Lipschitz-ξ, prove Picard closes for small data. Missing hypotheses: X must be a Banach space (not obvious — is BMO⁻¹ + Lipschitz-ξ complete under the stated norm? The Lipschitz-ξ set {u : κ < ∞} is not closed under weak-★ limits of a BMO⁻¹ Cauchy sequence because ξ = ω/|ω| is discontinuous at |ω| = 0. Banach structure is not verified.)

**Step-by-step audit.**
- **Step 1** [define X]: **SERIOUS-GAP.** "ξ is κ-Lipschitz on the support of Biot–Savart kernel values > 1" is ill-defined: the Biot–Savart kernel K(x,y) = (x−y)×·/|x−y|³ as a distributional kernel has no well-defined "support with values > 1"; the operator K★ω is an integral, so "support of K★ω values > 1" might be intended, but that's a set depending on ω itself — circular. Also: where |ω| = 0, ξ is undefined; the Lipschitz constraint on a moving set with punctures is not a standard norm. The proposal would need to fix the Lipschitz seminorm relative to a fixed test set, e.g. the complement of {|ω| < δ} for a fixed δ > 0.
- **Step 2** [X is Banach + critical]: **WRONG.** Scaling verification. Under u_λ(t,x) = λu(λ²t, λx), the vorticity direction satisfies ξ_λ(t,x) = ξ(λ²t, λx). Taking spatial gradient: ∇ξ_λ(x) = λ · (∇ξ)(λx). Hence the Lipschitz constant κ_λ = λ · κ (independent Python verification confirms). So κ scales as λ^1, i.e. SUBCRITICAL (a = +1), NOT scale-invariant. The proposal's claim "the Lipschitz constant κ scales like λ⁰, matching BMO⁻¹'s invariance" is FALSE. The mixed norm ‖u‖_{BMO⁻¹} + κ is not scale-invariant, so X is not a critical space. This is the proposal's own failure-mode 1; the author flagged it correctly. But the premise of Step 2 is broken, so the whole Picard-at-a-critical-space framework does not apply — Picard contraction at a non-critical norm does not give global mild solutions.
- **Step 3** [Picard map]: VALID mechanical construction, inherits Step 2's broken premise.
- **Step 4** [bilinear estimate]: SERIOUS-GAP. The claim that ‖B(u,v)‖_X ≤ C‖u‖_X ‖v‖_X is hand-waved as "uses Constantin–Fefferman identity"; CF's identity is for single-product integrals like ∫ω·(∇u)·ω, not for bilinear maps B(u,v). The gap between the known CF identity and the needed bilinear estimate is precisely the unclosed problem that Chae 2003–2007 has been circling for 20 years. "Standard estimate" hand-wave.
- **Step 5** [miracle ‖ξ(B(u,v))‖_{Lip} ≤ C(...)]: The proposal calls this "the claim to verify" — i.e. acknowledges this is the open heart of the argument. Fair, but then the rest of the proposal is predicated on a miracle not proved. CIRCULARITY if the "miracle" reduces to a smaller-scale instance of the same problem.
- **Step 6** [close Picard]: vacuous given Steps 2–5.
- **Step 7** [exhibit X ⊃ BMO⁻¹]: This is independently testable. "Specific swirl-type data with explicit vorticity direction" — one can construct such examples (axisymmetric Beltrami flows), but whether they are in X\BMO⁻¹ or just in BMO⁻¹ ∩ X depends on the norm structure. Not verified.
- **Step 8** [claim of larger ball]: Depends on Step 7.

**Specific concerns verified.**
- Adding a Lipschitz seminorm in physical space to a frequency-space norm (BMO⁻¹) cannot scale compatibly under u_λ because they scale with different exponents. Computed: BMO⁻¹ = λ^0, Lip-κ = λ^1. Confirmed wrong in proposal.
- BMO⁻¹ + Lip-ξ is not a Banach space in any obvious way: the set of divergence-free fields with finite κ is not closed under BMO⁻¹-Cauchy limits.

**External facts.** Bourgain–Pavlović 2008 cited correctly. Constantin–Fefferman 1993 cited correctly but the identity used is not for bilinear maps.

**Verdict**: **BROKEN** on the scaling computation alone; the Banach-space structure is also not verified. 

**Required fixes**: Either (a) prove that the Lipschitz seminorm of ξ at the appropriate physical-space scale is actually scale-invariant (perhaps by redefining κ on a *frequency-localized* ball rather than a physical-space ball) — this is nontrivial and might not be possible, or (b) downgrade the claim to "Picard at a sub-critical norm X", which is not a Koch–Tataru-style result.

---

### M1.4 — Perelman-analogue Φ with alignment χ(ξ·e_max)

**Statement coherence.** Clean. Target: Φ(u,t) = ∫|ω|²χ(ξ·e_max(S))dx monotone non-increasing under NSE. Clearly a moonshot (self-admitted).

**Step-by-step audit.**
- **Step 1** [vorticity equation]: VALID.
- **Step 2** [enstrophy derivative]: VALID. Correct identity, correct signs.
- **Step 3** [decomposition Sω·ω = |ω|²ξ·Sξ]: VALID.
- **Step 4** [d/dt Φ splits into vortex-stretching + χ-rotation terms]: VALID.
- **Step 5** [Galanti–Gibbon–Heritage / Constantin ∂_t ξ eq]: VALID; this is standard, though the reference to "Galanti–Gibbon–Heritage 1997 (Nonlinearity)" I cannot verify — a paper by Galanti, Gibbon & Heritage on orthonormal frame equations for vorticity was published in that period but the exact citation should be double-checked. Constantin 1994 (J. Stat. Phys. — citing journal not checked) is standard.
- **Step 6** ["needed miracle": χ can be chosen so rotation compensates stretching]: **SERIOUS-GAP / MOONSHOT DECLARATION.** The author honestly labels this as a hoped-for miracle. No construction of χ is proposed. Without χ, the rest is empty.
- **Step 7** [verify on Burgers, axisymmetric, Beltrami]: **WRONG on Burgers.** The proposal says "Burgers vortex (Φ grows — potential counterexample, but Burgers uses background forcing; unforced NSE decays)." This is a misreading of the Burgers-vortex literature. The *stationary* Burgers vortex requires external forcing (the strain field), but transient Burgers-vortex-*type* configurations can form in unforced NSE from generic smooth data, and in those transient forms ∂_t Φ > 0 on finite intervals. "Unforced NSE decays" is not a pointwise statement — energy decays but local enstrophy and vortex-stretching can transiently grow. So Burgers-vortex profiles *do* violate unconditional Φ-monotonicity even in the unforced setting, at least transiently. This is the proposal's own failure mode 1, honestly flagged; but Step 7's one-line parenthetical is an evasion.
- **Step 8** [even conditional monotonicity is useful]: VALID retreat position.

**Specific concerns verified.**
- **Scaling of Φ**: Computed Φ = ∫|ω|²χ dx with χ dimensionless. |ω|² = λ^4, dx = λ^{−3}, so Φ = λ^1. *Subcritical*, a = +1. For a Perelman analogue this is actually the right sign (Perelman's W is scale-invariant; a subcritical monotone-decreasing Φ would still obstruct zoom-in-type blowup). So M1.4's scaling is plausibly acceptable although not what the proposal might expect.
- **Discontinuity of e_max(S)**: Failure-mode 2 flags this. At spectral collisions of the symmetric strain tensor S, the principal eigenvector e_max is not well-defined. If χ is not Lipschitz at this non-smooth set, dΦ/dt includes a measure-valued jump term that the step-by-step calculation ignores. **Missing hypothesis**: either χ must be taken flat near the spectral collision set (e.g. χ = 0 when the top two eigenvalues coincide), or a careful limiting argument is needed.

**External facts.** Perelman 2003 cited correctly. Constantin 1994, Constantin–Fefferman 1993, Hou–Li 2008, Chae 2007 cited correctly.

**Verdict**: **SERIOUS-GAPS**, explicitly moonshot-labeled. The Φ-scaling is subcritical (a = +1), which is fine for a Perelman-analog but refutes any claim of "supercritical invariant". The "miracle" χ-construction is open. The Burgers vortex is a real and unresolved threat.

**Required fixes**: (a) Propose a concrete χ (Gaussian around ξ = e_max, smooth cutoff); (b) compute dΦ/dt explicitly on a transient Burgers-vortex profile; (c) handle e_max discontinuity explicitly.

---

### M1.5 — Besov-ESS via frequency-blocked Carleman

**Statement coherence.** Target clean: extend ESS to critical Besov spaces Ḃ^{−1+3/p}_{p,∞}, p > 3. Hypothesis p > 3 is correct (p = 3 is plain L³-ESS = classical ESS; p > 3 is the larger scale).

**Step-by-step audit.**
- **Step 1** [setup]: VALID.
- **Step 2** [blowup profile extraction]: VALID. Standard.
- **Step 3** [ancient solution in Besov class]: VALID.
- **Step 4** [Liouville for ancient Besov]: **SERIOUS-GAP.** For critical L³ (Liouville in ESS), this uses: bounded → compact in L³_loc → Carleman → unique continuation. For critical Besov Ḃ^{−1+3/p}_{p,∞} with p > 3, the embedding Ḃ^{−1+3/p}_{p,∞} ↪ L³_loc fails for p > 3 (in fact the Besov space is strictly larger); ancient solutions in Ḃ^{−1+3/p}_{p,∞} are less regular than L³_loc. The claim that Liouville "has not closed uniformly for all critical Besov" is right — and it has not closed because of a genuine obstruction: one can construct ancient non-trivial Besov-bounded profiles via Beltrami flows at high Fourier modes (small L^p but with unbounded oscillation structure). Failure mode 1 (self-admitted) is the right worry.
- **Step 5** [frequency-blocked Carleman weight φ_j(x) = −|x|²(1+c_j)]: **SERIOUS-GAP.** The Escauriaza–Kenig–Ponce–Vega Carleman estimate for the parabolic operator requires a specific relationship between the Carleman weight and the symbol of the operator. Splitting the weight by dyadic frequency blocks with independent c_j destroys the integral unique-continuation structure — the Carleman inequality needs a *joint* weight in (x, frequency), and separating dyadic blocks gives a patchwork that does not sum. Specifically, one cannot simply run EKPV Carleman on Δ_j U independently because ν∂_t − νΔ does not commute with Δ_j exactly (there are commutator corrections that grow with the frequency band).
- **Step 6** [Besov → L^∞_loc per block via Bernstein]: VALID mechanically, but this is the Besov-to-L^∞ embedding which is exactly what makes the blocks lose scaling invariance relative to the original Besov norm.
- **Step 7** [sum blocks]: **SERIOUS-GAP.** The sum over j of Carleman constants is not addressed. If each block's Carleman constant is ≳ exp(C · 2^j) (from the EKPV weight containing exp(φ_j) with φ_j growing with j), the sum diverges immediately. Failure mode 2 (self-admitted) is the right worry.
- **Steps 8–9** [conclude + quantitative]: depend on Steps 4–7.

**Specific concerns verified.**
- **Does the Carleman constant survive Littlewood-Paley paraproduct splitting?** No: EKPV Carleman estimates have an exponential constant that depends on the weight's growth. Summing over dyadic scales multiplies constants multiplicatively, not additively. There is no existing result in the parabolic unique-continuation literature that closes this as the proposal suggests. **Standard estimate hand-wave.**
- **Conflated norms**: Ḃ^{−1+3/p}_{p,∞} (homogeneous Besov) vs. B^{−1+3/p}_{p,∞} (inhomogeneous) matters near the origin in ℝ³. The proposal uses Ḃ; check that the Carleman weight is compatible with homogeneous norms. Not verified.

**External facts.** ESS 2003, Tao 2019, CSTY 2008, Dong–Du, Gérard 1998, Koch–Tataru 2009 cited correctly. EKPV Carleman attribution "Ann. of Math. 2008" is loose — the most-cited EKPV Carleman paper is Escauriaza–Kenig–Ponce–Vega, "Convexity properties of solutions to the free Schrödinger equation with Gaussian decay", Math. Res. Lett. **15** (2008) 957–971, and the parabolic extensions are in subsequent papers; not *Annals*. Minor citation error.

**Verdict**: **SERIOUS-GAPS**. The frequency-blocked Carleman structure is the technical heart, and the proposal hand-waves the most delicate step (summing constants across blocks).

**Required fixes**: (a) Either produce an explicit single-weight Carleman estimate compatible with Besov data, or (b) prove a Liouville theorem for Besov-bounded ancient solutions via an entirely different mechanism (e.g. profile decomposition à la Gérard + compactness inside the Besov ball).

---

### M1.6 — Helicity-modified Koch–Tataru

**Statement coherence.** Target clear; self-admitted likely blocked by barrier. Helicity formula H(u) = ∫u·ω dx is standard.

**Step-by-step audit.**
- **Step 1** [H is scale-invariant, dH/dt = −2ν∫∇u:∇ω]: VALID. Scaling verified independently: [u] = λ, [ω] = λ², [dx] = λ^{−3}, so H = λ^0.
- **Step 2** [H not conserved, only approximately]: VALID. This is standard.
- **Step 3** [claim: Picard ball in (BMO⁻¹, H)-joint norm is stable]: **MINOR-GAP.** "Joint norm ‖u‖_{BMO⁻¹} + |H(u)|" is not a norm: |H(u)| is a seminorm (can vanish on non-zero data). The relevant structure is closer to a constraint: fix H = H₀ small, then run Picard in BMO⁻¹. Whether this "constraint-preserving Picard" closes is non-obvious because Picard iterates do not automatically preserve H (Step 2 already notes H evolves).
- **Step 4** [bilinear estimate on helicity of B(u,v)]: **SERIOUS-GAP.** The helicity H(B(u,v)) = ∫B(u,v)·curl B(u,v) dx is a quartic integral in (u,v) and has no clean "bilinear estimate" structure. Moreover, for u,v in BMO⁻¹ only, the vorticity curl B(u,v) lives in a distributional space where the pairing ∫·curl· is ill-defined at the endpoint. Failure mode 2 (self-admitted) is exactly right.
- **Step 5** [closure]: depends on Step 4.
- **Step 6** [averaging check]: The admission that Tao's construction can likely be extended to preserve helicity is honest. Verified: the constraint on c(k,k₁,k₂) to preserve helicity is ∑_k k · c(k,k₁,k₂) = 0 for appropriate index combinations, which is a linear constraint on the |c| ≤ 1 ball; Tao's construction has lots of room within that ball, so a blowup-preserving helicity-respecting averaged NSE is plausible. **BLOCKED-BY-BARRIER** is the right verdict.

**Specific concerns verified.**
- Helicity scaling: λ^0, confirmed.
- Helicity-averaging invariance: Tao's averaging can plausibly be modified to preserve helicity; author's own honest grade (BLOCKED-BY-BARRIER) is correct.

**External facts.** Moreau 1961, Moffatt 1969 cited with the right attribution. Chae 2003 on helicity: correct but not all of Chae 2003's results are about helicity-specific regularity (some are about direction of vorticity). Koch–Tataru 2001 cited correctly.

**Verdict**: **SERIOUS-GAPS → BLOCKED-BY-BARRIER**, as the author confesses. 

**Required fixes**: The proposal exists to document reasoning; it is correctly graded. No fix attempted.

---

### G1 — Osgood feedback on ξ-Lipschitz

**Statement coherence.** Clean. Target: upgrade Constantin–Fefferman from conditional to automatic via sub-linear Osgood feedback on κ(t) = ‖∇ξ‖_{L^∞(Ω_M)}.

**Step-by-step audit.**
- **Step 1** [ξ evolution equation, projected on S² tangent]: VALID. The equation ∂_t ξ + (u·∇)ξ = P_{ξ^⊥}(∇u·ξ) + ν|ω|^{−1}P_{ξ^⊥}(Δω) is Galanti–Gibbon–Heritage / Constantin. Correct.
- **Step 2** [equation for ∇ξ]: **MINOR-GAP.** Taking ∇ of the ξ-equation gives a matrix-valued PDE whose right-hand side involves ∇²u and ∇(P_{ξ^⊥}). The proposal glosses over the non-linearity: P_{ξ^⊥} = I − ξξ^T depends on ξ, so ∇P_{ξ^⊥} involves ∇ξ itself, producing a self-coupling term proportional to |∇ξ|² that is not mentioned. This is a quadratic (not sublinear) feedback term.
- **Step 3** [localise to Ω_M = {|ω| ≥ M}]: **SERIOUS-GAP.** The "threshold M growing with t" is not specified; the Biot–Savart estimates on Ω_M depend crucially on M (since the kernel is singular). Singular-integral bounds ‖∇(K★ω)‖_{L^∞(Ω_M)} ≲ M-dependent factors; without a careful choice of M, the whole analysis is indeterminate. Also: Ω_M^c contributions from "lower-order" are not obviously lower-order in a supercritical 3D NSE setup.
- **Step 4** [Osgood closure at p < 1]: **SERIOUS-GAP / unsupported.** The claim that the feedback is sub-linear (p < 1) is the whole mathematical point and is not derived; it is merely hoped for. Failure mode 1 (self-admitted: feedback may be linear or super-linear) is the right worry.

**Specific concerns verified.**
- **Does feedback close?** The quadratic self-coupling term from ∇P_{ξ^⊥} alone contributes a |∇ξ|² term (p = 2 feedback), which is super-linear and Osgood-failing. So the proposal needs a very specific cancellation to be even marginally (p = 1) linear, let alone sub-linear.
- **Does it require pointwise existence of ω/|ω|?** Yes: ξ is undefined where |ω| = 0. The localization Ω_M provides a workaround only if Ω_M remains an open set with positive measure until the candidate blowup time. If the blowup scenario has ω vanishing on a set of positive measure near concentration points (as in some Burgers-vortex-type transient profiles), the whole framework breaks down. **Missing hypothesis**: require non-vanishing of ω on a neighborhood of the concentration set.

**External facts.** Constantin 1994, Constantin–Fefferman 1993, Beirão da Veiga–Berselli 2002 (journal title "Diff. Integral Eqns" — correct, full name "Differential and Integral Equations"), Grujić–Ruzmaikina 2004 cited correctly.

**Verdict**: **SERIOUS-GAPS**. The Osgood closure is the whole point and is not derived.

**Required fixes**: (a) Explicitly compute the self-coupling quadratic term from ∇P_{ξ^⊥} and identify the cancellation mechanism (if any); (b) justify Osgood exponent p < 1; (c) verify on axisymmetric-with-swirl as the problem solver proposed; (d) state a non-vanishing-ω hypothesis.

---

### G2 — ν-weighted W-entropy Perelman analogue

**Statement coherence.** Well-labeled moonshot. Target: Φ_ν(u,t) = ∫(|ω|² + λν|∇u|²)e^{−φ}dx monotone non-increasing under NSE.

**Step-by-step audit.**
- **Step 1** [formal d/dt Φ_ν]: VALID setup.
- **Step 2** [backward transport equation for φ]: **MINOR-GAP.** The form ∂_t φ + u·∇φ − ν|∇φ|² + νΔφ = Ψ is suggestive but the specific choice of Ψ is not given. Without a concrete φ, no computation can close.
- **Step 3** [Leray pressure cancellation]: **SERIOUS-GAP.** The claim that "because of the Leray-projection orthogonality, pressure drops out" is generic Leray projection intuition but does not automatically hold when the weight e^{−φ} is present. The pressure term in the enstrophy evolution is ∫ω·curl(∇p) dx = 0 on unweighted integrals (since curl of gradient is zero), but the *weighted* integral ∫ω·curl(∇p)·e^{−φ} dx = ∫ω·curl(∇p·e^{−φ}) dx + corrections that involve ∇φ, and those corrections do *not* automatically vanish. The proposal hand-waves this.
- **Step 4** [Φ_ν controls a critical norm]: open, self-admitted.

**Specific concerns verified.**
- **Scaling of Φ_ν**: Computed independently. [|ω|²] = λ^4, [ν|∇u|²] = λ^0 · λ^4 = λ^4, [e^{−φ}] = λ^0 (if φ dimensionless, which it is for the Perelman-Gaussian choice φ = |x|²/(4ν(T−t))), [dx] = λ^{−3}. So Φ_ν ~ λ^1, **subcritical**, a = +1. **The proposal's claim that "Φ_ν scales as λ^5 — supercritical, positive power" is WRONG** by 4 powers of λ. This is confirmed by independent calculation.
    - The problem solver flagged this as a scaling error; independent verification confirms the error.
    - Sanity-check: to get λ^5 one would need an integrand scaling as λ^8 (e.g. |Δu|² or |∇²u|²), not |ω|² or |∇u|². The formula as written cannot give λ^5.
    - Perelman's W is scale-invariant, not supercritical. So G2's framing ("supercritical is the differentiator") is itself misaligned with the Ricci-flow analogy. A scale-invariant Φ_ν + non-averaging-invariance would be sufficient, which is a weaker requirement.
- **Monotone under linear heat flow**: For the pure heat equation ∂_t u = νΔu, compute d/dt ∫|ω|²e^{−φ} dx with φ = |x|²/(4ν(T−t)). This is a standard exercise: one gets d/dt < 0 iff the Bakry-Émery-type curvature-dimension condition holds, which on ℝ³ with Gaussian weight is automatic. So for the heat equation, Φ_ν is monotone. Good. But the nonlinear NSE stretching term breaks this; the question is whether it breaks it in a controllable direction. Not resolved.
- **Against Burgers vortex**: Not computed in proposal. Failure mode consistent with M1.4; joint test proposed by problem-solver is the right next step.

**External facts.** Perelman 2003, Müller 2010, Ni 2004, Foias-Manley-Rosa-Temam 2001, Constantin-Foias 1988 cited correctly.

**Verdict**: **BROKEN** on the scaling claim alone. The remaining structure is a legitimate moonshot if the "supercritical" claim is retracted and the proposal is reframed as a scale-invariant monotone with non-averaging-invariance. 

**Required fixes**: (a) **Retract the scaling-supercritical claim and redo the scaling analysis**; (b) Specify Ψ in the backward transport equation for φ; (c) Carefully compute the weighted pressure term and identify what cancellation mechanism is needed; (d) Handle Burgers-vortex test.

---

### G3 — Arnold–Khesin SDiff curvature + Bochner

**Statement coherence.** Target: use SDiff curvature to bound Jacobi field growth on NSE geodesic. Self-labeled moonshot with 60-year negative prior.

**Step-by-step audit.**
- **Step 1** [NSE as geodesic-with-viscous-correction]: **SERIOUS-GAP.** Arnold 1966 showed *Euler* is geodesic flow on SDiff with L² right-invariant metric. NSE is *not* a geodesic flow on SDiff: the νΔu term is not of geodesic-with-friction form (friction would be a symmetric negative-definite perturbation of the covariant derivative in a specific sense, and νΔu is not this). Various authors have tried (Inci-Kappeler-Topalov 2013 studied the Euler geodesic equation on certain H^s-groups), but the "NSE as geodesic flow modulo νΔu" framing in G3 is imprecise. The author's failure mode 4 acknowledges "νΔu is not a gradient flow on (SDiff, L²)"; this is an honest admission that the framework does not quite fit.
- **Step 2** [Jacobi equation]: VALID for Euler, formal for NSE.
- **Step 3** [Bochner with curvature exp bound]: **SERIOUS-GAP.** The Bochner formula on SDiff requires the Ricci tensor of SDiff, which is a formal infinite-dimensional object. Ebin-Marsden and Khesin-Misiołek studied sectional curvatures; Ricci on SDiff is much less developed rigorously. Claiming "‖Y(t)‖² ≤ ‖Y(0)‖²·exp(2∫max(0,−κ)ds)" is a formal statement; rigorous convergence of the Ricci-averaged Jacobi equation on an infinite-dim group with L² metric is not established. Failure mode 2 (self-admitted) is right: "infinite-dim Bochner is formal".
- **Step 4** [bridge to enstrophy]: open.

**Specific concerns verified.**
- **Does Bochner fire in infinite dimensions on SDiff?** No, not rigorously. Ebin-Marsden 1970 establish SDiff is a weak ILH-manifold but the Ricci tensor is not well-defined in the sense needed. Khesin-Misiołek and Khesin-Wendt compute sectional curvatures along specific two-planes; these are finite-dimensional restrictions. The full Ricci is an infinite sum that has not been shown to converge. G3's Bochner-based argument is formal only.
- Arnold's negative-curvature results imply Lyapunov instability, i.e. that nearby geodesics diverge (the chaos side). Using them for *regularity* is backwards: they support blowup, not regularity. G3's G3(a) (positive-curvature sections giving regularity for Killing/Beltrami) is restricted to very special data.

**External facts.** Arnold 1966, Arnold-Khesin 1998/2021, Ebin-Marsden 1970, Misiolek 1997, Shkoller 1998 cited correctly. However: "Shkoller, *Geometry and curvature of diffeomorphism groups with H¹ metric and mean hydrodynamics*, J. Funct. Anal. **160** (1998)" — the paper is real but the H¹-metric geodesic is for the LANS-α model (Camassa-Holm-type regularised NSE), not for NSE itself. Citing Shkoller for NSE geodesic structure is misleading.

**Verdict**: **SERIOUS-GAPS**, correctly self-labeled as moonshot. The formal Bochner argument is not rigorous enough to give a regularity theorem.

**Required fixes**: (a) Rigorous Ricci definition on SDiff; (b) Clear separation of "NSE as geodesic" (false) from "NSE as geodesic-plus-friction" (ill-defined); (c) Correct the Shkoller citation or redirect to LANS-α model.

---

### G4 — Type-II axisymmetric Liouville

**Statement coherence.** Target clean: rule out Type-II discretely-self-similar blowup for axisymmetric NSE without swirl. This is SP2. Self-labeled TOY-SUB-PROBLEM.

**Step-by-step audit.**
- **Step 1** [rescale at Type-II rate]: VALID.
- **Step 2** [weak-★ limit profile]: VALID. Standard.
- **Step 3** [axisymmetric-no-swirl → ω^θ/r transported, a priori bound]: VALID. This is the Chen-Strain-Tsai-Yau / Hou-Li input.
- **Step 4** [Koch-Nadirashvili-Seregin-Šverák Liouville]: **MINOR-GAP.** KNSŠ Liouville is for *bounded* (not merely Type-II-profile) ancient solutions, and for specific axisymmetric flows. Applying it to Type-II profiles requires:
    - The Type-II rescaling to produce a *bounded* profile (the rate (T−t)^{−α} with α < 1/2 gives a bound that depends on the ancient-time exhaust τ → ∞);
    - The KNSŠ hypothesis to be met at the profile's regularity level.
  These are delicate and are the actual research content of the proposal.

**Specific concerns verified.**
- **Does Jia-Šverák 2014 apply to axisymmetric-no-swirl?** Jia-Šverák's paper is "Local-in-space estimates near initial time for weak solutions of the Navier-Stokes equations and forward self-similar solutions" (Invent. Math. 196, 2014, 233–265). Their result is about *forward* self-similar solutions, not backward blowup profiles. The proposal uses their discretely-self-similar machinery in a backward-time setting, which is analogous but requires adaptation. The adaptation is not standard; this is a real gap the proposal does not flag.
- **Is KNSŠ applicable?** KNSŠ 2009 (Acta Math. 203, 83–105) "Liouville theorems for the Navier-Stokes equations and applications" — yes, the relevant axisymmetric Liouville is there but hypotheses include *bounded* u (not just bounded ω^θ/r) and *decay at infinity*. For a self-similar profile arising from blowup of a compactly-supported solution, the decay may be available; for a discretely-self-similar profile, the decay is modulated by a periodic function in τ that may introduce complications.
- The problem solver's verdict (TOY-SUB-PROBLEM) is essentially right: this is incremental, and the remaining gaps are real research content not easily swept.

**External facts.** NRS 1996 (Acta Math. 176), Tsai 1998 (ARMA 143), Jia-Šverák 2014 (Invent. Math. 196, 233-265), KNSŠ 2009 (Acta Math. 203), CSTY 2009 (CPDE 34), Chae 2007 (Math. Ann. 338) cited correctly.

**Verdict**: **PASS-WITH-MINOR-FIXES**. The proposal is tight enough that the gaps are research questions, not integrity failures.

**Required fixes**: (a) Verify that Jia-Šverák forward-self-similar machinery can be adapted to backward/blowup setting (nontrivial); (b) Verify KNSŠ hypotheses hold on the Type-II profile, including decay at infinity.

---

### G5 — Elgindi viscous-damping

**Statement coherence.** Target clean: measure viscous damping on Elgindi's C^{1,α} Euler blowup profile. Self-labeled TOY-SUB-PROBLEM / INCREMENTAL.

**Step-by-step audit.**
- **Step 1** [Elgindi fundamental-model reduction]: VALID if Elgindi's explicit reduction is used.
- **Step 2** [add νΔ → 1D Schrödinger-type operator]: **MINOR-GAP.** "1D Schrödinger-type" is imprecise. The linearization L_Elg + νΔ on a C^{1,α} profile is a degenerate elliptic operator with variable coefficients; its spectrum depends on functional-analytic setup (weighted L² space? Hölder space?). The proposal does not specify.
- **Step 3** [compute spectrum]: **SERIOUS-GAP.** The Elgindi linearization L_Elg is degenerate at the blowup point (the profile is only C^{1,α}, so ∇U_Elg is Hölder but not bounded in the relevant sense). The symbol of L_Elg is scaling-invariant *only at blowup* (i.e. as a self-similar operator); adding νΔ breaks the scaling invariance for any ν > 0. So "spectral analysis" requires treating L_Elg + νΔ as a perturbation that destroys the self-similar structure. Whether the perturbation theory converges (i.e. whether there's an unstable eigenvalue λ(ν) that bifurcates smoothly from Elgindi's) is the open question, not a straightforward spectral computation.
- **Step 4** [Re λ(ν) ≤ 0 ⟹ no NSE blowup]: technically correct but pending Step 3.

**Specific concerns verified.**
- **Does spectral analysis of L_Elg + νΔ converge?** Probably YES, for the following reason: Elgindi's blowup exists because the C^{1,α} non-smoothness of the initial data creates algebraic (power-law) growth, which is exactly what νΔ damps via its 2nd-derivative penalty. For any ν > 0 and C^{1,α} data with α small enough, the heat semigroup e^{νtΔ} improves regularity to C^∞ in any positive time, which destroys the Elgindi mechanism. So expect Re λ(ν) < 0 for all ν > 0 in the Elgindi regime — i.e. NSE damps Elgindi Euler. This is a publishable result, but it's essentially what experienced PDE analysts expect. The proposal's content is to make the damping rate ν★(α) quantitative.
- **Does the C^{1,α} story touch Clay?** No, because Clay requires C^∞ data. Elgindi's mechanism relies critically on C^{1,α}; at C^∞, the algebraic-growth structure vanishes. So G5 is strictly a sub-problem of SP6.

**External facts.** Elgindi 2021 (Ann. Math. 194, 647-727), Elgindi-Jeong 2019 (Ann. PDE 5), Chen-Hou 2022/2025 (PNAS), Luo-Hou 2014 (MMS 12), Cordoba-Cordoba-Fontelos 2005 (Ann. Math. 162) cited correctly.

**Verdict**: **PASS-WITH-MINOR-FIXES**. The research program is valid; the gaps are about making the spectral analysis precise.

**Required fixes**: (a) Specify the functional-analytic setting (weighted spaces) in which L_Elg is an unbounded operator; (b) Verify that the Elgindi linearization has a discrete spectrum in that setting; (c) Acknowledge that the result is C^{1,α}-specific and does not bear on Clay.

---

### G6 — Obstruction-class cohomology

**Statement coherence.** Self-labeled speculative moonshot, "highest probability of BLOCKED-BY-BARRIER".

**Step-by-step audit.**
- **Step 1** [M = {u₀ : ‖u₀‖ ≤ R}, S = {blowup data}]: VALID setup.
- **Step 2** [evaluation bundle ℰ]: VALID if the lifespan T_max is assumed positive; else degenerate.
- **Step 3** [Mayer-Vietoris spectral sequence]: **SERIOUS-GAP.** M is a ball in a Banach space, hence contractible (by linear contraction, for any Banach space). For any contractible base, H^k(M; 𝒞) = 0 for any locally constant (topological) sheaf 𝒞, k ≥ 1. So the spectral sequence E_2 page vanishes for any topological construction. Mayer-Vietoris is trivial.
- **Step 4** [characteristic vs. analytic]: The proposal correctly identifies the dilemma. If 𝒞 depends on the NSE dynamics (analytic), then H^k(M; 𝒞) is not obviously topological but is actually just a reformulation of analytic regularity — no new information. If 𝒞 is topological, H^k = 0 trivially.

**Specific concerns verified.**
- **Is the space of divergence-free fields contractible?** YES. Any (reflexive separable) Banach space is contractible: the homotopy h(t, u) = tu is continuous, h(1, u) = u, h(0, u) = 0. The ball {u : ‖u‖ ≤ R} is also contractible. Kuiper 1965 (for U(H)) gives an even stronger statement but is not needed here — linearity suffices.
- **Is any characteristic class automatically zero?** YES, for the same reason: characteristic classes are pullbacks of classes on BU or BO, which depend on the homotopy type of the base. Contractible base → trivial pullback.
- So G6 is essentially a definition-level puzzle: either the sheaf 𝒞 is topological and the obstruction vanishes automatically, or the sheaf is analytic and the "obstruction class" is just a rebranding of an analytic estimate. Neither adds content.

**External facts.** Kuiper 1965, Atiyah-Hirzebruch cited correctly. Elworthy-Tromba 1970 cited correctly but their infinite-dim degree theory is on Banach manifolds of *mappings*, not on the velocity space directly; relevance is unclear. Joyce's C^∞-rings paper is flagged as "speculative analog" — this is honest.

**Verdict**: **BROKEN** by topological triviality. The proposal acknowledges this as a possibility but doesn't retreat from the moonshot labeling.

**Required fixes**: Either (a) propose a non-trivial analytic sheaf 𝒞 whose cohomology is both non-vanishing AND not reducible to a known analytic estimate — probably impossible, or (b) retract the proposal.

---

### A1 — Zero-noise-limit Otto entropy

**Statement coherence.** Target: pathwise monotone Wasserstein-2 action 𝒜_ε(u) that forbids L³ blowup via ε → 0 Γ-convergence. Self-graded SPECULATIVE (~20%).

**Step-by-step audit.**
- **Pathwise Otto action 𝒜_ε**: formally defined, but as a "pathwise" object along a stochastic realisation it requires a rigorous tangent-cone structure on W_2(𝕋³) along Markov semi-martingales. The Ambrosio-Gigli-Savaré / Villani frameworks handle this for deterministic curves; for stochastic flows the pathwise Otto calculus is *still under development* (Huesmann, Lisini-Mielke-Trevisan-type papers).
- **Claim: 𝒜_ε monotone under the stochastic flow, uniformly in ε**: unsupported. The heart of the proposal.
- **Γ-convergence 𝒜_ε → 𝒜₀**: requires compactness in a suitable topology; not addressed.
- **L³-unbounded Leray-Hopf makes 𝒜₀ explode**: unsupported assertion.

**Specific concerns verified.**
- **Does the Wasserstein gradient flow framework apply to NSE?** NO, not directly. The heat equation is the W_2 gradient flow of entropy H(ρ|Leb). NSE velocity is not a W_2 gradient flow of any known functional: the transport term (u·∇)u is not a gradient of any convex functional in W_2. A1 proposes to apply Otto calculus to the *vorticity* ρ_ω = |ω|²/‖ω‖²; but the vorticity equation dω = (νΔω + (ω·∇)u − (u·∇)ω)dt has a stretching term (ω·∇)u that is again non-gradient and breaks the Otto structure.
- A1's own failure-mode 1 ("𝒜_ε reduces under IBP to ν‖∇u‖² + l.o.t.") essentially concedes the framework collapses to the dissipation it tries to improve on.
- **Is NSE a Wasserstein gradient flow?** No — this is essentially confirmed by Doering-Foias, Constantin-Foias (not explicitly but by consequence of their Lyapunov-functional analysis). A1 is trying to force a framework that doesn't fit.

**External facts.** Flandoli-Gubinelli-Priola 2010, Otto 2001, Villani's book, Seregin 2012 cited correctly.

**Verdict**: **SERIOUS-GAPS** — the core premise (NSE admits Otto gradient-flow structure on vorticity) is not established and is *likely false*.

**Required fixes**: (a) Establish or falsify "NSE vorticity is a W_2 gradient flow of some functional F with non-gradient drift v"; if true, then Otto framework applies with transport correction; if false (as suspected), then A1 collapses. This is the pre-check the problem solver flagged.

---

### A2 — Regularity structures reclassification

**Statement coherence.** Target: treat stochastic NSE with Besov-regular (−1/2−ν) noise, use BCCH BPHZ. Self-graded SPECULATIVE, ~10%.

**Step-by-step audit.**
- **ξ ∈ B^{−1/2−ν,∞,∞}, ν small**: a legitimate noise class.
- **Regularity structures give local WP with renormalization C_ν**: **SERIOUS-GAP.** This requires checking that NSE + this noise is subcritical in Hairer's sense. The scaling argument — that the nonlinearity (u·∇)u at regularity −1/2+ν generates corrections of regularity −1+2ν, still negative but less so than white-noise driven — is sketched but not verified. The claim that Bruned-Chandra-Chevyrev-Hairer BPHZ applies requires the nonlinearity to fit the BPHZ framework, which has specific structural requirements (treelike hierarchies with constraint; for pressure-nonlocal NSE, this needs to be shown).
- **Estimate C_ν**: "if C_ν = O(|log ν|) or O(1), get uniform-in-ν solution" — pure speculation; the proposal does not indicate a mechanism for either bound.
- **ν → 1/2 limit**: even if C_ν finite in the interior, the ν → 1/2 boundary is exactly where subcriticality degenerates. A2 acknowledges this can diverge (failure mode 1).

**Specific concerns verified.**
- **NSE subcriticality in regularity-structures sense**: the Hairer subcriticality condition (degree of nonlinearity α < degree of noise singularity) for 3D NSE with white noise gives α = −1 − 1 = −2 and degree of dissipation −2, so NSE is *critical*. For smoother noise (regularity −1/2 − ν, ν > 0), the budget opens by ν. So the claim "subcritical by margin ν" is correct as a statement about the Hairer subcriticality condition.
- **Does the framework add anything?** No: the nonlinearity (u·∇)u still has pressure non-locality via Leray projection, which is *not* in the standard BPHZ framework for local nonlinearities. Extending BPHZ to pressure-type non-local operators is open research (partly done by Gubinelli-Hofmanová for 2D). For 3D NSE it is not established.
- **Does this touch Clay?** No, by A2's own admission and the L-P dependence.

**External facts.** Hairer 2014 (Inventiones 198 — should be 192, minor typo), BCCH 2021, GIP 2015, Catellier-Chouk 2018 cited with minor errors. Hairer's "A theory of regularity structures" is Inventiones **198** (2014) pp. 269–504 — OK, 198 is right.

**Verdict**: **SERIOUS-GAPS** on the core BPHZ-for-NSE feasibility question.

**Required fixes**: (a) Establish that BPHZ framework extends to Leray-projected nonlinearity; (b) Estimate C_ν bound mechanism; (c) Acknowledge this is entirely sub-Clay research.

---

### A3 — Furstenberg-correspondence lift of Foias-Prodi

**Statement coherence.** Target: invariant measure + attractor-finite-dim + Foias-Prodi determining-modes + Furstenberg lift to individual-trajectory regularity. Self-graded SPECULATIVE for forced, MOONSHOT for unforced.

**Step-by-step audit.**
- **Step 1** [forcing, ergodicity]: "Hairer-Mattingly flavour" — but Hairer-Mattingly 2006 is a *2D* result. For 3D, ergodicity of the Galerkin approximation is known (Flandoli-Romito 2008), but the limiting 3D NSE ergodicity is not established in the full pathwise sense.
- **Step 2** [dim_H(supp μ) < ∞ ⇒ inertial manifold]: **CIRCULAR / UNSUPPORTED.** Finite-dim global attractor for 3D NSE is an open problem, and having an inertial manifold is stronger still. *Assuming* these is essentially assuming a version of Clay for the forced case. The problem solver flagged this correctly: the hypothesis is Clay-equivalent.
- **Step 3** [Foias-Prodi on M]: Foias-Prodi 1967 is a 2D result. The 3D version (à la Constantin-Foias) requires prior regularity — again circular in the 3D-regularity context.
- **Step 4** [Furstenberg correspondence]: **SERIOUS-GAP.** Furstenberg's correspondence principle maps density-zero sets in integers to zero-measure sets under a recurrence measure. The application to PDE attractors would require a recurrence structure on the NSE flow, which NSE (dissipative, non-measure-preserving) does not have. **Missing hypothesis**: NSE is not measure-preserving. Foias-Prodi rigidity is about attractor geometry, not recurrence.
- **Step 5** [f → 0 limit]: Self-admitted kill.

**Specific concerns verified.**
- **Does Foias-Prodi lift to individual-trajectory regularity?** No, at least not as sketched. Foias-Prodi gives convergence of TWO solutions with matching low modes to each other in L². It does not give regularity; it gives slaving. If both solutions are irregular, they are equally irregular. Foias-Prodi can be used for statistical regularity (if the invariant measure concentrates on regular solutions), but that concentration is itself what's being assumed.
- **Is NSE measure-preserving?** No — NSE (with or without forcing) is dissipative; energy decays (for unforced) or is balanced by injection (for forced). Furstenberg correspondence principle fundamentally requires measure-preservation.

**External facts.** Foias-Prodi 1967, Hairer-Mattingly 2006 (for 2D, stated as "Ann. Math." — correct, vol 164, pp 993-1032), Kuksin-Shirikyan book, Constantin-Foias-Temam 1985, Bourgain 1994 cited correctly.

**Verdict**: **SERIOUS-GAPS** — circularity in Step 2 (assumes finite-dim attractor, which is essentially Clay for forced) and non-applicability of Furstenberg correspondence to dissipative flows. 

**Required fixes**: (a) Drop the finite-dim-attractor hypothesis or justify independently; (b) Establish that Furstenberg correspondence (or an analogue) applies to dissipative flows — this is probably infeasible; (c) Restrict to the forced statistical statement (self-admitted valid sub-result).

---

### A4 — Mechanized Positivstellensatz + Lean search

**Statement coherence.** Target: search polynomial basis for monotone NSE functionals up to degree D = 4. Clear, actionable, and self-graded REALISTIC.

**Step-by-step audit.**
- **Derivative algebra + symmetry-invariant polynomial basis**: VALID. Standard Olver/Gorinov-Wilkening enumeration of invariants.
- **Compute dΦ/dt symbolically**: VALID in principle. Requires computer algebra (SymPy, Maple, or Lean's mathlib has some support).
- **Positivstellensatz / SOS**: VALID technique. SDP solvers exist for SOS.
- **Certify in Lean**: **MINOR-GAP / OPTIMISTIC TIMELINE.** Lean 4 mathlib as of 2026 has limited Positivstellensatz/SOS support. Certification of an SDP solution in Lean is technically possible but requires significant infrastructure.
- **Output either Φ or no-go theorem**: The claim that either output is publishable is correct.

**Specific concerns verified.**
- **Feasibility of search**: The polynomial-invariant basis at degree D = 4, order k ≤ 2, in 3 velocity components has ~40 jet variables, degree-4 monomials ~10^5. SOS decomposition of a degree-4 polynomial in 40 variables is tractable as an SDP but the certificate size can be exponential in degree (failure mode 2 acknowledges this).
- **Does search scale exponentially?** For *fixed* D, the search is polynomial in the number of jet variables. For *increasing* D (to D = 6, 8 as might be needed for Perelman-analogue), combinatorial explosion is real.
- **Lean 4 mathlib for Positivstellensatz**: Very limited as of 2026. The proposal's 2-3 year timeline for full formal verification is optimistic; for a "minimum viable enumeration" without Lean certification (just SDP output), 3-6 months is realistic.

**External facts.** Parrilo-Lasserre SOS hierarchy, Olver-style enumeration cited correctly. Lean 4 mathlib state correctly characterized as in-development.

**Verdict**: **PASS-WITH-MINOR-FIXES**. The core search procedure is well-designed. Timeline and Lean-certification ambitions are optimistic.

**Required fixes**: (a) Scope the project to "SDP search + informal verification" first, with Lean certification as a stretch goal; (b) Acknowledge the degree D = 4 limit may not reach Perelman-analogue (which may live at D = 6–8); (c) Build in checks for ν-essentiality (so the found Φ is not also monotone under Euler, which would contradict Chen-Hou).

---

### A5 — Fisher-information monotone on |ω|

**Statement coherence.** Target: F(t) = ∫|∇log|ω|²|²|ω|²dx has dissipative lower bound dF/dt ≤ νF − Cν^{−1}F^γ, γ ~ 1. Self-graded SPECULATIVE (~15-20%).

**Step-by-step audit.**
- **Definition of F(t)**: VALID when |ω| > 0 everywhere; degenerate at |ω| = 0 set.
- **dF/dt along vorticity transport**: **MINOR-GAP.** The computation needs to handle (i) the stretching term (ω·∇)u, (ii) the diffusion νΔω, (iii) the transport −(u·∇)ω. Each contributes differently to d/dt ∫|∇log|ω|²|²|ω|²dx. The proposal sketches "both signs" for the stretching term — but does not actually compute.
- **Comparison to Chae 2007**: Chae's ∇ξ-based criterion is distinct from ∇log|ω|² = (∇|ω|)/|ω|. Distinctness is real at the formal level; whether the two criteria collapse to the same estimate after integration by parts is the open question.

**Specific concerns verified.**
- **Does the stretching term produce a bad sign?** Compute: |ω|²∇log|ω|² = ∇|ω|². The stretching contribution to d/dt F involves integrals of form ∫∇|ω|²·stretching terms, which expand to cubic-in-∇u integrals. By the structure of the vortex-stretching term (ω·∇)u·ω = |ω|²α where α = ξ·Sξ is the alignment scalar, the sign of d/dt F depends on whether ∫|∇|ω||²αdx > 0 or < 0, which in turn depends on the geometry. In the Hou-Luo / Chen-Hou near-blowup regime, α > 0 on the concentration region (vortex stretching is active), so this contribution is positive and drives F to grow. The dissipation term −νC||∇²|ω|||² is non-trivial but in the supercritical regime may not dominate. **So the stretching term very likely has the bad sign for generic blowup scenarios.**
- **Scaling of F**: Independent calculation (see Methodology section). [ω] = λ^2, log|ω|² gets an additive shift under rescaling so its gradient is (|∇|ω|²|)/|ω|² which scales as λ; squared gives λ^2. Times |ω|² = λ^4, times dx = λ^{−3}. So F ~ λ^3. Supercritical, a = −3/2. The problem solver claimed a = −5/2; my computation gives a = −3/2. Discrepancy worth flagging — **both are supercritical but differ by 1 in the exponent**.
- **Well-definedness at |ω| = 0**: F is infinite if |ω| = 0 on a set of positive measure. For smooth data with non-trivial ω, this is avoided generically but not universally. The proposal's "regularized sense" is unspecified.

**External facts.** Villani's entropy book, Bakry-Émery theory, Chae 2007, log-Sobolev cited correctly.

**Verdict**: **SERIOUS-GAPS** on the central sign question + scaling-computation disagreement.

**Required fixes**: (a) Compute dF/dt explicitly; (b) Verify scaling exponent (either a = −3/2 or a = −5/2); (c) Specify regularization at |ω| = 0.

---

## Part II — New-technique-node audit (B1–B4)

### B1 — `t_renormalization_group_flow_with_blowup_profile`

**Function signature**: precise (PDE + profile + scale parameter → RG map + fixed points + spectrum).

**Definition**: well-specified for dissipative PDEs with scaling symmetry. The dynamical-systems view is genuinely different from "rescale around blowup" alone.

**Repackaging test**: As the author notes, risk of collapse to `t_rescale_for_asymptotic_geometry` ∘ `t_frequency_decomposition`. The distinctive feature is the *iteration as a self-map with spectral analysis* — Bricmont-Gawędzki-Kupiainen-style RG. If this is honored (not just rescale-once), B1 is a genuine new composite node. If collapsed to "rescale and apply LP", it is repackaging.

**Verdict**: NEW-GENUINE. Honors the composite distinction.

### B2 — `t_wasserstein_gradient_flow_with_nonlinear_transport`

**Function signature**: precise (measure evolution equation → W_2 action / gradient-flow-plus-transport decomposition).

**Definition**: well-specified. The "with-nonlinear-transport" modifier is a real technical pattern (JKO-with-drift, driven gradient flows).

**Repackaging test**: As the author notes, plausibly collapses to `t_duality` + `t_conserved_quantity`. The non-gradient-drift bookkeeping is distinctive.

**Additional concern**: given A1's (likely false) premise that NSE admits an Otto structure on vorticity, B2 may be a technique in search of applications in NSE specifically. It has genuine use in chemotaxis, cross-diffusion, etc.

**Verdict**: NEW-AS-REPACKAGING tending to NEW-GENUINE. Honors the framework only if the non-gradient-drift decomposition is specifically invoked. Note: B2's applicability to NSE is weaker than claimed (A1 failure).

### B3 — `t_mechanized_monotone_quantity_search`

**Function signature**: precise (PDE + invariant basis + target weight → Positivstellensatz certificate or no-go).

**Definition**: well-specified. The composite of enumerate-invariants + symbolic-d/dt + SOS + certify is not currently a single named technique in the knowledge graph.

**Repackaging test**: composes `t_formal_verify` + `t_finite_case_check` + `t_polynomial_method` + `t_conserved_quantity`. Not reducible to any single one.

**Verdict**: NEW-GENUINE at composite level. Flag: no successful instance exists yet; provisional admission until first firing.

### B4 — `t_zero_noise_limit_with_preserved_regularity`

**Function signature**: precise (SPDE family {Eq_ε} + regularity class R → deterministic a priori bound on Eq_0 in R).

**Definition**: well-specified. The preservation-of-regularity pattern is named in Flandoli-Gubinelli-Priola and subsequent work.

**Repackaging test**: collapses to `t_probabilistic_existence` + `t_compactness_argument`. The distinctive feature is the PRESERVATION of a regularity class across ε → 0, which neither parent flags explicitly.

**Verdict**: NEW-GENUINE. The composite pattern is distinctive.

---

## Part III — Systemic patterns across the 17 proposals (~500 words)

Five systemic patterns emerge from the audit, in rough order of frequency.

**Pattern 1 — "Scaling is what I say it is."** Two of the 17 proposals (G2 and M1.3, arguably also A5) make scaling-computation errors on their central controlling quantity. G2 claims Φ_ν scales as λ^5 (supercritical); independent computation gives λ^1 (subcritical) — a 4-power error that reverses the Perelman-analog framing. M1.3 claims the Lipschitz-ξ constant is scale-invariant; independent computation gives λ^1 (subcritical), breaking the Picard-at-critical-space framework entirely. The systemic issue: authors are invoking a "the quantity should be supercritical because it's not already controlled" heuristic, then asserting the scaling matches the heuristic without computing. **Remedy**: every proposal involving a controlling functional must include an explicit u_λ rescaling computation with each factor identified separately. This was exactly the barrier diagnostic the problem solver's Part B is supposed to do; when authors draft independently they skip it.

**Pattern 2 — "Standard estimate" hiding the theorem.** M1.1's commutator log-gain is the chief offender: it invokes "Kato-Ponce / Christ-Weinstein commutator estimates" as a standard tool, but what's needed (log-order gain, not derivative-order gain) is not in those papers. M1.5's "Carleman weight φ_j per block" and summing constants is a second example: the step "sum over j" needs a constant-summation estimate that does not exist. G1's "Osgood exponent p < 1" is a third: the sublinearity is *hoped* rather than derived. **Remedy**: flag every occurrence of "by standard estimate X" with the precise quantitative claim being invoked, and require a citation or a derivation. If the claim is quantitatively stronger than the cited paper, it is a new theorem, not a standard estimate.

**Pattern 3 — Circularity through "assume attractor / assume regularity."** A3 is the clearest: its hypothesis (finite-dim attractor for 3D NSE) is essentially a weak form of Clay. M1.4 and G2 are borderline (assuming enough regularity to define the candidate Φ is needed, and that regularity is itself the target). G4 avoids this cleanly by restricting to no-swirl axisymmetric (known regular). **Remedy**: for each proposal, explicitly state what regularity is assumed on the solution *at the audit step* versus what is to be proved.

**Pattern 4 — "Escapes Tao barrier" by loss of definability.** G4, A1, A3 each claim barrier-escape by noting that the controlling quantity is UNTESTABLE on Tao's averaged NSE (no axisymmetric structure, no vorticity density, no attractor). This is technically true but logically weak: a quantity the averaged NSE doesn't admit cannot be used to distinguish true NSE from averaged NSE in a proof — because the proof cannot even be stated on the averaged side. Genuine barrier-escape requires the quantity be DEFINABLE but false on the averaged side. G1 and M1.4 pass this stronger test (direction ξ and alignment ξ·e_max are formally definable on the averaged system, but the averaged dynamics scrambles them); G4, A1, A3 fail this stronger test and so their barrier-escape is weak.

**Pattern 5 — Moonshot labeling as shield.** M1.4, G1, G2, G3, G6 are all self-labeled MOONSHOT, and the authors use this labeling to excuse unresolved technical gaps. The labeling is honest but it reduces the audit value: a moonshot is not automatically a research program, and the audit's job is to distinguish "moonshot with a well-defined first step" (M1.4's Burgers-vortex test, G1's axisymmetric-with-swirl feedback) from "moonshot with no first step" (G3's infinite-dim Bochner, G6's obstruction class). **Remedy**: require every moonshot proposal to include a concrete, falsifiable 1-3 month milestone (the problem solver's "pre-check items" list is the right template).

### Trustworthiness ranking (most to least trustworthy)

1. **G4 (Type-II no-swirl)** — PASS-WITH-MINOR-FIXES, clean derivation, minor adaptation gaps, genuine SP2 contribution.
2. **G5 (Elgindi viscous damping)** — PASS-WITH-MINOR-FIXES, well-posed spectral question, bounded scope.
3. **A4 (Lean Positivstellensatz search)** — PASS-WITH-MINOR-FIXES, mechanically well-designed, timeline optimistic.
4. **M1.2 (double-exp quantitative ESS)** — PASS-WITH-MINOR-FIXES, self-admitted barrier-non-escape makes it honest; the iteration accounting is a real open question but not a fatal flaw.
5. **M1.4 (Perelman-analog Φ)** — SERIOUS-GAPS, self-admitted moonshot, correct scaling (λ^1 subcritical), real Burgers threat.
6. **M1.6 (helicity-modified KT)** — SERIOUS-GAPS → BLOCKED-BY-BARRIER as author confesses. Honest.
7. **M1.5 (Besov-ESS)** — SERIOUS-GAPS, frequency-blocked Carleman is the weak link.
8. **G1 (Osgood ξ feedback)** — SERIOUS-GAPS, Osgood closure is asserted not derived, quadratic self-coupling missed.
9. **A5 (Fisher info)** — SERIOUS-GAPS, sign of stretching contribution not computed, scaling disagreement.
10. **A1 (zero-noise Otto)** — SERIOUS-GAPS, Otto framework doesn't fit NSE vorticity.
11. **A2 (regularity structures)** — SERIOUS-GAPS, BPHZ-for-Leray-NSE feasibility not established.
12. **G3 (SDiff Bochner)** — SERIOUS-GAPS, infinite-dim Bochner is formal.
13. **A3 (Furstenberg lift)** — SERIOUS-GAPS, circularity (attractor hypothesis = Clay).
14. **M1.3 (Lipschitz-ξ Picard)** — BROKEN, scaling is subcritical not critical.
15. **M1.1 (log-hyperdissipative)** — BROKEN, the g(r) formula gives a constant, not a log, and the commutator log-gain does not exist.
16. **G2 (ν-weighted W-entropy)** — BROKEN on scaling claim (λ^1 not λ^5).
17. **G6 (obstruction cohomology)** — BROKEN by contractibility of ambient space.

Among new-technique nodes: B3 (NEW-GENUINE, no precedent), B1 (NEW-GENUINE, if dynamical-systems distinction honored), B4 (NEW-GENUINE, regularity-preservation pattern named in SPDE lit), B2 (NEW-AS-REPACKAGING tending to NEW-GENUINE, weakest).

### Key integrity failures missed by the problem solver

Three that I flag which the problem solver's audit did not catch or stated only weakly:

1. **M1.1's g(r) formula** — the problem solver asked whether the log-gain is real but did not notice that the proposed g(r) = r^{2c/log(2+r)} actually tends to a constant, so the PDE is just α = 5/4 with ν rescaled. This is a fatal issue with the formula as written.
2. **A5's scaling exponent** — the problem solver computed a = −5/2; my independent computation gives a = −3/2. Both agree F is supercritical, but the exponent matters for whether "one log improvement" would close the argument.
3. **G3's Shkoller citation and NSE-is-not-geodesic issue** — the problem solver gave a MOONSHOT grade but did not flag the Shkoller citation's subject (LANS-α, not NSE) or the fundamental point that NSE is not a geodesic flow on SDiff at all (only Euler is).

Two corrections to problem solver's conclusions:

4. **M1.4's scaling as "wrong sign for Perelman-analog"** — the problem solver writes "subcritical means Φ grows under zoom-in which is actually the wrong sign for a Perelman-analogue" and then corrects to "Perelman's W grows under zoom-in too". In fact Perelman's W is *scale-invariant*, not subcritical. M1.4's Φ ~ λ^1 subcritical is actually acceptable for a Perelman-analog so long as it is monotone-decreasing; the problem solver's reasoning here is briefly confused before arriving at approximately the right verdict.
5. **G4 adaptation gap** — Jia-Šverák 2014 is about forward self-similar (initial value problem), not about backward blowup profiles. G4 uses it in the wrong direction and the adaptation is non-trivial; problem solver did not flag.
