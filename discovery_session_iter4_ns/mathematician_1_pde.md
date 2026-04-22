# Mathematician 1 — PDE-analytic attack proposals (3D Navier–Stokes)

**Role.** Team member 1/9 on iteration 4 of a knowledge-graph-driven attempt at the Clay regularity problem for incompressible 3D Navier–Stokes. Portfolio: PDE-analytic attacks — scaling-critical analysis, frequency decomposition, quantitative regularity, hyperdissipation, Carleman estimates.

**Baseline.** Scout `ns_scout.md` is authoritative for prior art. Tao's supercritical barrier (arXiv:1402.0290) rules out proofs that work on every averaged NSE sharing scaling-invariant estimates. The quantitative ladder (ESS 2003 → Tao 2019 triple-exp → Palasek 2022 single-exp axisymmetric → Barker–Prange 2021) and SP4 (hyperdissipative α<5/4), SP5 (Tao-bound sharpening) are the live PDE edges. Every proposal includes a mandatory supercritical-barrier check.

None of what follows claims to solve Clay.

---

## Proposal M1.1 — Logarithmically supercritical hyperdissipation: closing the 5/4−ε gap via commutator-captured log-correction

**Target.** SP4 (hyperdissipative α < 5/4). Produce global regularity for 3D generalised Navier–Stokes with dissipation (−Δ)^α with α = 5/4 − c/log(1+|ξ|) for some fixed small c > 0, where the symbol is read in Fourier. This is not full Clay (α = 1). It is a strict extension of Tao 2009 (JAMS 19, which reached α = 5/4 with *one* log-correction stronger than needed) to one extra log weaker than Tao, i.e. moving one notch closer to the Laplacian in the logarithmic hierarchy.

**Core idea.** Tao 2009 introduced a logarithmic dissipation D(|ξ|) = |ξ|^{5/2}/g(|ξ|) and proved global regularity whenever g grows slightly slower than log^{1/4}. The frontier is: how much weaker than Tao's g can we take and still close the estimate? The gain I claim is a sharper paraproduct commutator estimate, exploiting the fact that the bad term in the energy budget is *always* of paraproduct type T_{low}(u_{high})·∇u_{high}, whose commutator with the dissipation yields an extra logarithmic gain not captured in Tao's analysis.

**Graph techniques used.** `t_frequency_decomposition` (Littlewood–Paley on the hyperdissipative system), `t_interpolate_and_continue` (Gagliardo–Nirenberg on fractional spaces), `t_conserved_quantity` (modified energy with log-weight), `t_exhaustion_squeeze` (continuation at Ḣ^s with s depending on α), `t_reductio_ad_absurdum` (assume first blowup time T★).

**Technical derivation sketch.**
1. Fix α = 5/4 − ε(|ξ|), ε(|ξ|) = c/log(2+|ξ|), c < c₀ to be determined. The dissipation operator is the Fourier multiplier D̂(ξ) = |ξ|^{5/2}/g(|ξ|), g(r) := r^{2c/log(2+r)} which is morally log^c.
2. Take the energy Ḣ^s inner product of the equation with u for s = 1/2 + ε₁, ε₁ small. Obtain d/dt ‖u‖²_{Ḣ^s} + 2ν‖D^{1/2} u‖²_{Ḣ^s} ≤ |⟨(u·∇)u, u⟩_{Ḣ^s}|.
3. Decompose nonlinearity via Bony: (u·∇)u = T_{u}∇u + T_{∇u}u + R(u,∇u). Use divergence-free to remove one paraproduct. The surviving bad term is T_{u_{low}}∇u_{high}.
4. Apply a commutator estimate [T_{u_{low}}, D^{1/2}]: the symbol inequality gives an extra factor log^{-1}|ξ_{high}| on the high-frequency side.
5. Bound the cubic nonlinearity by the dissipation using (3) and (4) plus Bernstein: ‖Δ_j u‖_{L^∞} ≲ 2^{3j/2} ‖Δ_j u‖_{L²}, so the bad sum becomes Σ_j 2^{(5 − 2·(5/2 − 2ε(2^j))) j} g(2^j)^{−1} ‖Δ_j u‖²_{Ḣ^s} + harmless remainder.
6. The exponent on 2^j at the top is 4ε(2^j) · j = 4c · j/log(2+2^j) ≈ 4c · (log 2). So the exponent in the bad sum is order 4c · log 2, a *constant* multiplied by the commutator log gain log^{−1}(2^j). Net: if c is chosen below (log 2)^{−1} times Tao's threshold, the commutator gain dominates and closes the budget.
7. Apply `t_exhaustion_squeeze`: fix hypothesised finite blowup time T★, apply Gronwall on the log-weighted energy, contradict. Conclude global smoothness.
8. Check that the log correction ε(|ξ|) = c/log(2+|ξ|) is *strictly weaker* than Tao's (whose g grows like log^{1/2}) — the claim is we save an order of log.

**Escapes the supercritical barrier?** **No — but only because SP4 is not Clay.** The averaged hyperdissipative NSE with the *same* α also has the same paraproduct commutator estimate, so the proof is averaging-invariant. However, for SP4 that is acceptable: there is no Tao-style averaged blowup construction at α ≥ 1 (Tao's construction is at α = 1 only and uses cascade dynamics that genuinely differ at α > 1). The barrier applies only at α = 1.

**External inputs needed.**
- Tao 2009, "Global regularity for a logarithmically supercritical hyperdissipative NSE" (JAMS 19). Available.
- Katz–Pavlović 2002 (for α = 5/4 base case). Available.
- Paraproduct commutator estimates of Kato–Ponce / Christ–Weinstein type. Available.
- Bernstein inequalities on dyadic frequencies. Available.
- Possibly: Yamazaki 2015 on logarithmically supercritical MHD, as a method parallel. Available.

**Failure modes.**
1. The "commutator gain" at step 4 might not be log^{−1} but only log^0 (i.e. no gain), in which case Tao's threshold is already sharp for commutator methods and the claimed extra log is illusory. This is the likeliest failure.
2. The log-weighted energy at step 6 needs the integral ∫ g(|ξ|)^{−1} dξ to interact well with the Littlewood–Paley sum; if g grows too slowly (which is exactly the goal) the sum becomes log-divergent at high frequencies, meaning the energy itself is undefined.
3. Dyadic/shell model falsifier: Katz–Pavlović 2005 have dyadic blowup for α < 5/4 without log correction. If the dyadic shell model (with this specific log correction) still blows up, the proposal is falsified at the toy level before touching real NSE.

**Honest grade.** INCREMENTAL-OVER-KNOWN. Polishing Tao 2009's threshold by one log is a real mathematical gain but does not reach the α < 5/4 gap.

---

## Proposal M1.2 — Carleman-sharpened quantitative ESS: from triple exponential to double exponential via a two-scale frequency envelope

**Target.** SP5 (Tao's bound sharpening). Sharpen Tao 2019 (arXiv:1908.04958) from ‖u(t)‖_{H^k} ≤ exp(exp(exp(A^{O(1)}))) to double-exponential exp(exp(A^{O(1)})), where A = ‖u‖_{L^∞_t L^3_x}. Palasek 2022 achieved *single* exponential for axisymmetric. The general-data gap remains.

**Core idea.** Tao's triple exponential arises from three stacked compactness/Carleman arguments: (i) epochs-of-regularity pigeonholing giving one exponential; (ii) back-propagation of enstrophy concentration giving a second; (iii) quantitative unique continuation via Carleman giving the third. Palasek removed (i) in the axisymmetric case because axisymmetry forces a one-parameter geometry. For general data I propose replacing (i) with a *two-scale frequency envelope* at the first bad epoch: track the enstrophy on two dyadic scales N_high > N_low simultaneously and show that one of them obeys a linear (not exponential) Gronwall, by trading one exponential for one integer (the number of dyadic levels between N_low and N_high, which is itself O(log A)).

**Graph techniques used.** `t_exhaustion_squeeze` (quantitative, in Tao 2019 sense), `t_frequency_decomposition` (Littlewood–Paley + the two-scale envelope), `t_compactness_argument` (quantified via Carleman, replacing qualitative compactness), `t_reductio_ad_absurdum` (hypothesis: triple-exponential bound is sharp — derive a Carleman-compatible structure).

**Technical derivation sketch.**
1. Assume ‖u‖_{L^∞_t L³_x} ≤ A on [0,T). Fix target regularity Ḣ¹, target bound B.
2. Following Tao 2019 §4, at the first bad epoch one identifies a "bubble" of enstrophy concentration at a scale N★(t) with magnitude ≳ exp(A^c₁).
3. **New step**: instead of one scale, track two scales N_low(t) = N★(t) and N_high(t) = 2^{k(t)} N★(t) with k(t) the smallest integer such that ‖Δ_{N_high} u‖_{L²} ≤ ‖Δ_{N_low} u‖_{L²}/2. Such k exists and is O(log A) by the Bernstein/energy budget (the solution has finite energy, so high-frequency tails must decay).
4. Local-in-time Carleman (Tao 2019 Prop 5.9) gives back-propagation of concentration from N_low to N_high at rate controlled by *only one* exponential of A times k(t) ≤ O(log A).
5. Run the back-propagation iteratively on k dyadic levels. The total multiplicative factor is (exp(A^c))^k = exp(A^c · log A) — absorbed into exp(A^{c+o(1)}).
6. Replace Tao's second exponential by this O(log A) factor. This removes one layer of the triple exponential.
7. The remaining Carleman step (layer (iii)) is intrinsic to quantitative backward uniqueness and cannot currently be removed without a new Liouville theorem; we accept it.
8. Net bound: ‖u(t)‖_{H^k} ≤ exp(exp(A^{c(k) · log log A})) ≤ exp(exp(A^{c'(k)})) — a clean double exponential.
9. Verify no averaged variant can saturate: the two-scale envelope depends on the *actual* finite-energy tail decay of u, which is lost under averaging (the averaged NSE does not conserve energy pointwise in frequency with the same structure).

**Escapes the supercritical barrier?** **Weak no.** The argument still works if we replace the nonlinearity by a Tao-averaged one that preserves energy, because the two-scale envelope uses only the scalar quantities ‖Δ_N u‖_{L²}. So this is a quantitative improvement within the scaling-invariant framework. The barrier does not forbid such improvements; it only forbids crossing the *conditional → unconditional* line. Tao-bound sharpening is allowed to use averaging-invariant ingredients and is all the more valuable because of it.

**External inputs needed.**
- Tao 2019, arXiv:1908.04958 — the full paper, especially §4–§6. Available.
- Palasek 2022, arXiv:2108.09108 — axisymmetric single-exponential. Available.
- Escauriaza–Kenig–Ponce–Vega Carleman estimates for parabolic operators. Available.
- Barker–Prange 2021 concentration framework (arXiv:2011.12704 or the 2022 CMP version). Available.
- Albritton–Barker 2023, structural refinements. Available.

**Failure modes.**
1. The k(t) that exists from energy decay might only be O(log A · log log A) rather than O(log A), giving log² A instead of log A in the exponent — which still gives double exponential, so this failure is mild.
2. The Carleman step (iii) might have a *hidden* second exponential that I conflated with step (ii). Tao's proof has delicate epoch-of-regularity counting that the two-scale envelope does not obviously replace — the iteration in step 5 might re-incur a Gronwall factor at each level.
3. Axisymmetric falsifier: Palasek's single-exponential uses one-parameter geometry; if the two-scale envelope reduces general data to essentially axisymmetric data along each epoch, then Palasek's bound should be achievable in full, not just double exponential, which is suspicious and suggests the envelope is doing less work than I claim.

**Honest grade.** INCREMENTAL-OVER-KNOWN, tending toward TOY-SUB-PROBLEM if the cleaner formulation below holds. The claim of one removable exponential is modest and plausible. Publishable if technically sound; does nothing for Clay.

---

## Proposal M1.3 — A larger-than-BMO⁻¹ critical space via vorticity-direction Lipschitz constraint

**Target.** Critical-norm dichotomy. Identify a critical Banach space X ⊃ BMO⁻¹ such that the Koch–Tataru Picard contraction closes globally for small data in X, using not size alone but a conditional Lipschitz bound on the vorticity direction. This is neither Clay nor SP-X from the scout; it lives in the "Axis 1 + mild-solution contraction at Koch–Tataru" combination.

**Core idea.** BMO⁻¹ is the largest known critical space for Picard contraction. Bourgain–Pavlović 2008 showed that Ḃ^{−1}_{∞,∞} (the ball immediately outside BMO⁻¹) is already ill-posed. But the Bourgain–Pavlović construction is specific to data with *arbitrary* vorticity direction. If we constrain the vorticity direction ξ = ω/|ω| to be Lipschitz near the concentration set (Constantin–Fefferman hypothesis), the bad high–high-to-low Mikado-style interaction is structurally suppressed, and Picard may close in a larger space. This gives a conditional largest critical space, parametrised by the Constantin–Fefferman geometric constant.

**Graph techniques used.** `t_contraction_fixed_point` (Koch–Tataru Picard), `t_frequency_decomposition` (paraproduct), `t_symmetry_reduction` (geometric, via the vorticity direction), `t_axiomatize_from_instances` (define X axiomatically from the Lipschitz constraint), `t_duality` (vorticity–velocity via Biot–Savart).

**Technical derivation sketch.**
1. Define X = {u : ∇·u=0, ‖u‖_{BMO⁻¹} < ∞, and ∃ κ : ξ = ω/|ω| is κ-Lipschitz on the support of Biot–Savart kernel values > 1}. Norm: ‖u‖_X = ‖u‖_{BMO⁻¹} + κ.
2. Verify X is a Banach space and is critical under u_λ(t,x) = λu(λ²t, λx) — the Lipschitz constant κ scales like λ⁰, matching BMO⁻¹'s invariance.
3. Set up the Picard map Φ(u)(t) = e^{tΔ}u₀ − ∫₀ᵗ e^{(t−s)Δ} ℙ(u⊗u) ds on a ball in X.
4. The bilinear estimate ‖B(u,v)‖_X ≤ C ‖u‖_X ‖v‖_X is the heart. The BMO⁻¹ part is Koch–Tataru. The Lipschitz part requires showing that the vorticity of B(u,v) inherits a Lipschitz direction from u and v; this uses the Constantin–Fefferman identity for the vortex-stretching term ω·∇u.
5. The "miracle" needed: the Biot–Savart integrand in ω-direction satisfies a better estimate than in ω-magnitude. Specifically, ‖ξ(B(u,v))‖_{Lip} ≤ C(κ_u, κ_v, ‖u‖_{BMO⁻¹}, ‖v‖_{BMO⁻¹}). This is the claim to verify.
6. Close Picard: small-data-in-X → global mild solution of NSE, hence smooth.
7. Demonstrate X ⊃ BMO⁻¹: exhibit functions with infinite BMO⁻¹ norm but finite X norm — e.g. specific swirl-type data with explicit vorticity direction.
8. The global smoothness of small-X-data now includes some data that BMO⁻¹ alone does not handle. This is the "larger critical Picard ball" claim.

**Escapes the supercritical barrier?** **Yes, for small data in this ball — not for Clay.** The Lipschitz-ξ constraint is not an averaging-invariant quantity. Tao's averaged NSE scrambles the sign and direction of ω at each frequency, so the averaged NSE does not preserve ‖u‖_X. Hence the proposal uses a property not shared with averaged NSE. BUT: the result is only small-data global (critical-space Picard is always small-data), so it is an enlargement of the Kato/Koch–Tataru ball, not an unconditional result. The barrier applies to unconditional global regularity, not to Picard balls.

**External inputs needed.**
- Koch–Tataru 2001 (Adv. Math. 157), BMO⁻¹ small-data global. Available.
- Constantin–Fefferman 1993 (Indiana Univ. J.), geometric depletion. Available.
- Bourgain–Pavlović 2008 (J. Funct. Anal.), ill-posedness immediately outside BMO⁻¹. Available.
- Chae 2003–2007 papers on vorticity-direction regularisation. Available.
- Beirão da Veiga–Berselli 2002 on Lipschitz-direction criteria. Available.

**Failure modes.**
1. The Lipschitz constant κ does not actually scale correctly under u_λ. The Lipschitz *constant* (with the usual normalisation) is dimensionless, but the Lipschitz norm on the appropriate domain (a ball of Biot–Savart support) might acquire a λ dependence through the domain size. If so, X is not scaling-invariant and the whole premise fails.
2. The bilinear estimate at step 5 is exactly the step the literature has never closed (Chae's Lipschitz-direction criteria are sub-critical). If closing it required solving a smaller but structurally identical problem, the proposal is circular.
3. Axisymmetric falsifier: axisymmetric solutions have trivially Lipschitz ω-direction (it's parallel to eθ), so the proposal would immediately give Koch–Tataru *+* axisymmetric global regularity for all data in X ∩ {axisymmetric}. Since axisymmetric Clay is already open for general swirl (it's essentially the Hou–Chen setting), if the proposal gave a global axisymmetric result that would be suspicious and likely indicates an error.

**Honest grade.** MOONSHOT, with a non-trivial route to TOY-SUB-PROBLEM status if the bilinear estimate in step 5 can be proved. Realistically, the scaling-invariance check in step 2 is the first likely failure.

---

## Proposal M1.4 — Frequency-envelope monotonicity with a non-scaling geometric budget: the Perelman-analogue attempt

**Target.** Full Clay (form A), named as a moonshot with expected failure. The deliverable is to state precisely what a Perelman-analogue for NSE would need and to identify where known candidates break.

**Core idea.** Perelman's W-entropy for Ricci flow was (i) supercritical w.r.t. Ricci's scaling, (ii) built from geometry (curvatures, volumes) not norms, (iii) valid for all smooth solutions. For NSE, seek Φ(u,t) with d/dt Φ ≤ 0 along NSE, Φ supercritical (scales as negative power of λ), Φ controlling enstrophy or higher. Concrete candidate — a vortex-stretching-budget

Φ(u,t) := ∫_{ℝ³} |ω|² · χ(ξ·e_max(S)) dx,

with ξ = ω/|ω|, S = (∇u+∇u^T)/2, e_max(S) the principal strain eigenvector, χ : [−1,1] → ℝ_≥0 monotone. When ω aligns with expanding strain, vortex-stretching grows Φ; rotation of ξ off the principal axis is the Constantin–Fefferman geometric depletion. Question: is there χ making Φ monotone non-increasing?

**Graph techniques used.** `t_conserved_quantity` (the target: a new conserved/monotone functional), `t_flow_with_surgery` (Perelman analogue), `t_duality` (vorticity–strain via Biot–Savart), `t_symmetry_reduction` (SO(3) action on (ω, S)), `t_auxiliary_construction` (constructing ψ explicitly).

**Technical derivation sketch.**
1. Vorticity evolution: ∂_t ω + (u·∇)ω = Sω + νΔω.
2. d/dt |ω|² = 2 Sω·ω + 2ν ω·Δω; hence d/dt ∫|ω|² ≤ 2∫(Sω·ω) − 2ν∫|∇ω|². The stretching term is the supercritical obstruction.
3. Decompose Sω·ω = |ω|² · (ξ·Sξ); alignment between ξ and λ_max(S) is the geometric quantity.
4. Compute d/dt Φ = (d|ω|²/dt) χ + |ω|² dχ/dt. The second term requires the vorticity-direction evolution.
5. Galanti–Gibbon–Heritage / Constantin 1994 identity: ∂_t ξ + (u·∇)ξ = P_{ξ^⊥}(Sξ). Rotation rate of ξ is controlled by the transverse component of Sξ — i.e. misalignment itself.
6. Needed miracle: χ can be chosen so that the rotation of ξ toward misalignment (term 2) compensates the vortex-stretching growth (term 1), yielding d/dt Φ ≤ 0.
7. Verify on explicit flows: 2D (Φ=0 trivially), axisymmetric no-swirl (Φ constant), Beltrami (ω∥u, Φ=∫|u|²χ(1) constant), Burgers vortex (Φ grows — potential counterexample, but Burgers uses background forcing; unforced NSE decays).
8. Even conditional monotonicity — over solutions in a restricted region — is a real step and is all that is realistically achievable.

**Escapes the supercritical barrier?** **Conditionally yes.** The geometric quantity ξ·e_max(S) depends on the pointwise alignment between vorticity and strain; Tao's averaged NSE randomises the direction of ω and S independently (the average is frequency-local, not pointwise geometric), so averaged NSE does not preserve Φ. This is exactly the kind of non-averaging-invariant input the barrier forces us to find. That said, the averaged NSE constructed by Tao does not obviously *violate* Φ-monotonicity either; it simply has no canonical analogue of Φ because there is no canonical ω/ξ/S structure.

**External inputs needed.**
- Perelman 2003, "The entropy formula for the Ricci flow and its geometric applications" (arXiv:math/0211159). Available.
- Constantin 1994 (J. Stat. Phys.), vortex-direction evolution identity. Available.
- Constantin–Fefferman 1993 (Indiana Univ. J.), geometric depletion. Available.
- Galanti–Gibbon–Heritage 1997 (Nonlinearity), orthonormal frame equations for vorticity. Available.
- Hou–Li 2008, Chae 2007, geometric criteria for no-blowup. Available.
- Burgers vortex literature (Gallay–Wayne 2005, Prochazka–Pullin 1995). Available.

**Failure modes.**
1. Burgers-vortex: even unforced, transient stretching gives finite-time Φ-growth, killing unconditional monotonicity. Conditional monotonicity is the best case.
2. e_max(S) is a discontinuous functional at spectral collisions of S. Singularities of χ(ξ·e_max(S)) wreck differentiability.
3. Axisymmetric falsifier: if Φ is unconditionally monotone for swirl-axisymmetric (still open), one should be suspicious — that would be a suspicious sub-result. If monotone only for no-swirl, it re-proves a known theorem.
4. Adversarial averaging: Tao's 2014 construction is flexible enough that a Φ-like averaged quantity can likely be built, so non-averaging-invariance needs to be verified against specific constructions, not asserted.

**Honest grade.** MOONSHOT. A candidate for the "named moonshot" of Axis 11 (§5 of the scout). Almost certainly fails at step 7 or 9. The value is in making the failure explicit, so the next iteration knows which geometric degree of freedom to replace.

---

## Proposal M1.5 — Quantitative backward-uniqueness with a sub-critical weight: pushing ESS into Besov

**Target.** SP3 (extending ESS L^∞_t L^3_x criterion) and SP7 (unique continuation). Prove: if u ∈ L^∞_t X for a critical Besov X strictly larger than L³, specifically X = Ḃ^{−1+3/p}_{p,∞} for some p > 3, then u cannot blow up. Equivalently, quantify Tao 2019's bound in Besov norms and close a Besov ESS.

**Core idea.** Chen–Strain–Tsai–Yau 2008 and others have critical-Besov criteria for *bounded* norms, but the Besov-ESS (the statement "if the norm is finite at the singular time, then the solution extends") is not fully closed. The gap is at backward uniqueness: ESS via Carleman works for u ∈ L^∞_t L^3_x because L³ gives enough local-pointwise compactness to run the Carleman on a blowup profile. For Besov the corresponding profile is less regular, and the Carleman weight needs a modification. Proposal: introduce a *Besov-adapted Carleman weight* e^{φ(t,x)} with φ a solution of an eikonal equation on a dyadic-frequency-indexed family, and close unique continuation in the larger norm.

**Graph techniques used.** `t_exhaustion_squeeze` (quantitative), `t_frequency_decomposition` (Littlewood–Paley in Besov), `t_compactness_argument` (profile extraction à la Gérard), `t_reductio_ad_absurdum` (assume Besov norm bounded, u blows up).

**Technical derivation sketch.**
1. Assume ‖u‖_{L^∞_t Ḃ^{−1+3/p}_{p,∞}} ≤ A on [0,T), T finite. Target: u extends past T with H^k bound.
2. Extract a blowup profile: zoom in near a would-be singular point (t★, x★), rescale u_λ(t,x) = λu(t★ + λ²t, x★ + λx). Pass to a weak limit U as λ→0. This is the ancient-solution step of ESS.
3. U is a nontrivial ancient solution (defined for t ∈ (−∞, 0]) in the Besov class, with ‖U‖_{L^∞_t Ḃ^{−1+3/p}_{p,∞}} ≤ A. Show U inherits scaling self-similarity.
4. Apply a Liouville theorem for ancient solutions in Besov: if U is bounded in critical Besov and ancient, then U ≡ 0. This is the step the literature has not closed uniformly for all critical Besov.
5. The Liouville step uses backward uniqueness, run via Carleman estimates of Escauriaza–Kenig–Ponce–Vega type. For L³ this is Tao 2019 Prop 5.x. For Besov, the weight φ needs to handle frequency-anisotropic decay: introduce a weight φ_j(x) = −|x|² · (1 + c_j) on each dyadic block Δ_j U, then sum with a frequency envelope.
6. The sum-over-frequencies needs the Besov embedding Ḃ^{−1+3/p}_{p,∞} → L^∞-dual-type; use Bernstein to turn Besov decay into L^∞_loc decay at each dyadic block.
7. Close Carleman block-wise and sum: the vanishing of each Δ_j U implies vanishing of U. Liouville closed.
8. Feed back: U ≡ 0 contradicts nontriviality of the rescaled blowup profile. Conclude: no blowup, i.e. the Besov norm cannot blow up finitely.
9. Quantitative version: same argument with explicit bounds gives ‖u(t)‖_{H^k} ≤ F(A) for some F that is at worst triple-exponential (as in Tao 2019) but perhaps improved via the frequency envelope of Proposal M1.2.

**Escapes the supercritical barrier?** **No, this is a critical-norm criterion.** Like ESS itself, the result is conditional on a critical-norm bound; it does not give unconditional global regularity. The averaged NSE shares the same Besov embedding and would admit the same conditional bound — but averaged NSE blows up, meaning the averaged-NSE Besov norm must actually reach ∞. That is consistent; the conditional criterion is still true for the averaged NSE, it just doesn't imply regularity because the hypothesis fails.

**External inputs needed.**
- Escauriaza–Seregin–Šverák 2003 (Russ. Math. Surv.), original ESS. Available.
- Tao 2019, arXiv:1908.04958. Available.
- Chen–Strain–Tsai–Yau 2008 and Dong–Du, critical-Besov regularity criteria. Available.
- Escauriaza–Kenig–Ponce–Vega, Carleman estimates for parabolic operators (Ann. of Math. 2008 and related). Available.
- Gérard's 1998 concentration–compactness profile decomposition for Strichartz. Available.
- Koch–Tataru 2009, Strichartz-BMO framework. Available.

**Failure modes.**
1. The Liouville theorem at step 4 may genuinely fail for Besov-bounded ancient solutions, e.g. admit non-trivial Beltrami-like steady states in Ḃ^{−1+3/p}_{p,∞} \ L³. This would be a counterexample that *predates* the Clay problem — it would settle Besov-ESS negatively.
2. The frequency-blocked Carleman at step 5 may have bad dependence on j, giving a constant that diverges in j and cannot be summed.
3. Non-uniqueness falsifier: Cheskidov–Luo 2022 produced non-unique solutions in L^p_t L^∞_x for p < 2, at the Serrin endpoint. This is the scaling-adjacent endpoint; if their construction can be adapted to Ḃ^{−1+3/p}_{p,∞} (which is more honest than L^∞_x), the whole Besov ESS statement would be false and the proposal collapses.
4. Shell-model falsifier: Cheskidov dyadic shell models have blowup in the Besov-analogue norms. If lifting preserves the structure, the proposal already fails at the model level.

**Honest grade.** INCREMENTAL-OVER-KNOWN to TOY-SUB-PROBLEM. Closing Besov ESS in a specific range of p is a legitimate sub-problem on the SP3 frontier; it has been partially done (CSTY 2008, Dong–Du) but the sharp endpoint and quantitative version are open. Realistic publishable target, zero progress toward Clay itself.

---

## Proposal M1.6 — Critical-space mild-solution globalisation via a new structural invariant: helicity-modified Koch–Tataru

**Target.** Enlarging the mild-solution global ball in a critical space using helicity. Supporting lemma, possibly feeding SP1 (uniqueness) or a sub-case of small-data global.

**Core idea.** Helicity H(u) = ∫ u·ω dx is *scaling-critical* (scales as λ⁻¹ ... no — check: H(u_λ) = ∫ λu(λ²t, λx) · λ²ω(λ²t, λx) dx = λ³ · λ⁻³ ∫ u·ω dy = ∫ u·ω dy, so it's scaling-invariant in 3D). It is conserved for smooth solutions of Euler and approximately conserved for NSE (dissipation rate is 2ν∫∇u:∇ω dx). Propose: extend Koch–Tataru to a ball parametrised not just by BMO⁻¹ size but by helicity, giving a larger global small-data ball for helicity-zero data.

The structural gain: **zero helicity is preserved by Tao-averaged NSE only if the averaging is helicity-respecting**, which is a genuine restriction on the averaging. Hence helicity-zero is a partially non-averaging-invariant condition, potentially escaping the barrier for its sub-class.

**Graph techniques used.** `t_conserved_quantity` (helicity), `t_contraction_fixed_point` (Koch–Tataru Picard), `t_symmetry_reduction` (parity-reversing symmetry preserving helicity-zero), `t_duality`.

**Technical derivation sketch.**
1. H(u) = ∫u·ω dx is scaling-invariant in 3D. Evolution: dH/dt = −2ν∫∇u:∇ω dx, not signed.
2. Helicity is not preserved exactly under NSE dissipation, only approximately. So instead of preservation, require |H(u(t))| stays small.
3. Claim: if ‖u₀‖_{BMO⁻¹} ≤ δ and |H(u₀)| ≤ δ, a Picard ball of radius 2δ in (BMO⁻¹, H)-joint-norm is stable.
4. Bilinear estimate to prove: ‖B(u,v)‖_{BMO⁻¹} + |H(B(u,v))| ≤ C δ². Compute the helicity component of B via dyadic-block Hölder.
5. If this closes, the admissible small-data ball is strictly larger than Koch–Tataru's along the helicity-zero axis.
6. Averaging check: Tao 2014 averaging preserves energy/scaling but is not explicitly helicity-preserving. If the construction can be extended to preserve helicity with blowup, the barrier applies; otherwise helicity-zero sub-class has genuine protection.

**Escapes the supercritical barrier?** **Partially.** The barrier blocks proofs that use only BMO⁻¹. Helicity is an additional scaling-invariant conserved (approximately) scalar. A proof using helicity + BMO⁻¹ is blocked iff Tao's averaging can be arranged to preserve *both*. This is a technical question with an answer in the literature only partially addressed. Tao's 2014 construction (arXiv:1402.0290) preserves energy but is not explicitly helicity-preserving; extending it to preserve helicity is a natural sub-problem. Tentatively: barrier does NOT immediately apply, but this needs to be checked, and I confess that most likely the barrier *can* be extended to cover helicity by an appropriate averaging construction.

**External inputs needed.**
- Moreau 1961, Moffatt 1969 on helicity as topological invariant. Available.
- Chae 2003 on helicity and regularity of NSE. Available.
- Koch–Tataru 2001 BMO⁻¹ theory. Available.
- Tao 2014 arXiv:1402.0290, for checking whether the averaging can or cannot preserve helicity. Available.

**Failure modes.**
1. Helicity is only approximately preserved under NSE; the small-helicity ball may close only over finite time with no net gain over Koch–Tataru.
2. The helicity bilinear estimate needs regularity that BMO⁻¹ alone does not supply: helicity involves ω = curl u, so BMO⁻¹ data makes ω live in Ḃ^{−2}-ish, where the pairing is ill-defined at the endpoint.
3. Adversarial averaging: Tao's construction can likely be extended to preserve helicity (a constraint on c(k,k₁,k₂)); if so, the barrier applies after all and this is BLOCKED-BY-BARRIER.
4. Axisymmetric no-swirl is already globally smooth with zero helicity (Ladyzhenskaya 1968), so no gain there. Swirl cases have generic non-zero helicity.

**Honest grade.** BLOCKED-BY-BARRIER, with low probability of MOONSHOT upgrade. Most likely the barrier kills this with an adapted Tao construction. The proposal is included to document the reasoning, so the next iteration can either execute the barrier extension (closing this line) or find a helicity-non-averaging argument (re-opening it).

---

## Appendix — self-audit

**Clay-solved claims?** None.

**Barrier summary.** M1.1: conditional on SP4, barrier does not apply at α>1. M1.2: improves within the conditional framework. M1.3: small-data Picard, uses non-averaging-invariant Lipschitz-ξ input. M1.4: explicitly names non-averaging-invariant alignment ξ·e_max(S); confessed that adapted averaging might still apply. M1.5: critical-norm conditional, parallel to ESS. M1.6: confessed probably BLOCKED-BY-BARRIER.

**Differential gain (what each proposal exploits that ESS/Serrin/Tao did not).**
- M1.1: paraproduct commutator log-gain absent from Tao 2009.
- M1.2: two-scale frequency envelope using energy-tail decay (replaces one compactness by log A).
- M1.3: Lipschitz vorticity direction as an extra norm component.
- M1.4: pointwise ξ·e_max(S) alignment — not captured by any Besov/BMO⁻¹ norm.
- M1.5: frequency-blocked Carleman weight matched to Besov profiles.
- M1.6: helicity as auxiliary scalar constraint.

**Portfolio priorities.** M1.2 is the highest-value target: directly on SP5 frontier, plausibly a publishable theorem in 1–3 months. M1.1 is second (SP4). M1.4 is the moonshot; even its failure mode (locating which geometric input fails) is useful as a new graph technique template for the Perelman-analogue axis. M1.3, M1.5, M1.6 hand off as sub-problems for other iterations.

**Out of scope for PDE-analytic portfolio.** Convex-integration non-uniqueness, Arnold/Riemannian geometry, computer-assisted proofs, stochastic regularisation, Type-II self-similar existence/exclusion — handled by other team members.
