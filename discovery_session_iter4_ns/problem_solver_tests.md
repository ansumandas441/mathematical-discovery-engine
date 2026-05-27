# Problem-Solver Tests — 3D Navier–Stokes Regularity

**Role**: problem-solver on a 9-person NSE attack team. This document is the reduced-case test matrix and supercritical-barrier diagnostic that every proposal from M1 (PDE), M2 (geometric), and M3 (fresh-vocab) must survive.

**Source for landscape**: `/Users/primetrce/Documents/maths/discovery_session_iter4_ns/ns_scout.md`.

**Adversarial stance**: every attack proposal is presumed wrong until it survives the matrix. A proposal that "sees through" every reduced case unchanged is almost certainly proving too much — the reduced cases were engineered by Katz–Pavlović, Tao, Elgindi, Hou, Chen et al. precisely to rule out classes of would-be arguments.

---

## Part A — Reduced-case test matrix

Each entry gives: (i) the model, (ii) its known status and citation, (iii) what an attack proposal must do on this model to be consistent with the known status — i.e. what the test **rejects** — and (iv) what the test **cannot see**. When an attack fails against a reduced case, we write FAIL; survival is a necessary but never sufficient condition.

### A.1 — 2D NSE (ℝ² or 𝕋²)

**Model.** ∂ₜu + (u·∇)u = −∇p + νΔu on ℝ²or 𝕋² with ∇·u=0. Vorticity ω = ∂₁u₂ − ∂₂u₁ is a scalar transported with diffusion: ∂ₜω + u·∇ω = νΔω.

**Known status.** Global smoothness for all smooth finite-energy data. Ladyzhenskaya 1959; Ladyzhenskaya–Solonnikov 1960s; Lions 1969. Standard textbook material; see Constantin–Foias *Navier–Stokes Equations* (1988) and Lemarié-Rieusset *Recent Developments* (2002) ch. 14.

**What this test rejects.** Any attack whose central estimate, applied verbatim in 2D, would predict blowup — or conversely, any attack that claims global smoothness in 3D by a mechanism that already holds in 2D. A proposal that says "the vorticity transport equation + maximum principle gives global smoothness" is FAIL-2D in the sense that it proves too little: it works in 2D by the *scalar* maximum principle on ω. In 3D ω is a vector, there is no scalar maximum principle, and a vortex-stretching term ω·∇u reappears. An attack must **engage the vortex-stretching term** explicitly or explain why its mechanism applies without a scalar ω.

**What this test can't see.** Many 2D arguments use global L^∞ control of ω via the transport structure; this is a feature absent in 3D entirely. Thus 2D can appear as a "free pass" — a proposal that engages 2D at all is already differentiated from pure-scaling attempts. It does **not** test whether the attack handles the 3D geometry.

### A.2 — Hyperdissipative NSE, α ≥ 5/4

**Model.** ∂ₜu + (u·∇)u = −∇p − ν(−Δ)^α u, ∇·u=0 on 𝕋³ or ℝ³.

**Known status.** Global smoothness for α ≥ 5/4. Katz–Pavlović 2002 (JAMS 15, 445–495) showed α > 5/4 via Littlewood–Paley energy. Tao 2009 (Anal. PDE 2, 361–366; arXiv:0906.3070) pushed α = 5/4 with a logarithmic correction: ∂ₜu = −ν D² u where D² has symbol |ξ|^{5/2} / (log(2 + |ξ|²))^{1/2}. The case α < 5/4 (including Clay α = 1) is open.

**What this test rejects.** Any attack whose argument *worsens* with decreasing α: if the proposal purports to give global regularity at α = 1, it must also give it at α = 5/4 with the same or better ease. More sharply: the KP/Tao proofs use a critical Besov energy that scales as supercritical by a factor λ^{2α − 5/2}. A proposal claiming scaling-based control of a norm that is supercritical at α=1 by margin 1/2 but subcritical at α = 5/4 by margin 0 must show continuity of its estimate across α — otherwise it is FAIL-HYPERDISS by producing a trivial argument at α = 5/4 where the margin collapses.

**What this test can't see.** Hyperdissipative NSE smooths *too* effectively. The blowup/no-blowup threshold is scaling-driven; the geometry of vortex stretching (a 3D phenomenon) is largely orthogonal. An attack purely geometric in spirit (Axis 1, Constantin–Fefferman) can ignore α and still succeed; thus surviving hyperdissipative tests says little about a geometric attack.

### A.3 — Fractional NSE, α < 5/4

**Model.** Same with 1 ≤ α < 5/4.

**Known status.** Open for 1 ≤ α < 5/4. The open interval (1, 5/4) is where all currently-plausible "scaling-plus-ε" arguments would have to live.

**What this test rejects.** If a proposal gives regularity at α = 1, it gives it uniformly on [1, 5/4), *including* α = 1. So a proposal at α = 1 is testable: does it degrade gracefully, or does the proof rely on a *non-smooth* dependence on α at α = 1? A proof that *cannot* be re-derived at α = 1.1 is FAIL-FRAC. Concretely: if the proposal's scheme hinges on a fixed spectral cut at frequency λ₀ that is only closed via α = 1, with a constant that is O(1/(5/4 − α)), the argument degenerates at α = 5/4 (where we have other proofs) but also fails to be *continuous at α = 1*. Check the α-derivative of every closing estimate.

**What this test can't see.** Fractional α is a pure scaling lever, so it is blind to geometric content.

### A.4 — Dyadic shell model (Katz–Pavlović, Cheskidov)

**Model.** ODE hierarchy on scalar amplitudes a_n(t), n ∈ ℤ_{≥0}, with λ_n = 2^n:
  da_n/dt = λ_n a_{n−1}² − λ_{n+1} a_n a_{n+1} − ν λ_n^{2α} a_n.
Represents the triadic energy cascade with critical dissipation scaling.

**Known status.** Katz–Pavlović 2005 (Trans. AMS 357, 695–708; arXiv:math/0211073) — finite-time blowup for α < 1/4 (when the dissipation term loses to the cascade). Cheskidov 2008 (Trans. AMS 360, 5101–5120; arXiv:math/0502227) — the critical threshold is α_crit = 5/4 adjusted for the shell scaling (equivalently α ≥ 1/2 in shell variables suffices for global existence). Cheskidov–Friedlander–Pavlović 2010. The model has explicit forward-cascade blowup under subcritical dissipation.

**What this test rejects.** Any attack for 3D NSE that does **not use a cancellation specific to the full 3D geometry** — one that is absent in the shell. Equivalently: if the proposed estimate reads, in Littlewood–Paley language,
  (d/dt)½‖Δ_j u‖² + ν λ_j² ‖Δ_j u‖² ≤ C λ_j ‖Δ_{j-1} u‖² ‖Δ_j u‖
with C uniform in j, then the shell model *is a special case with equality*, and KP showed this fails at α ≤ 1/4 (equivalently Clay α). FAIL-SHELL. The proposal must use either (a) triangle-constrained interactions (divergence-free forces cosines to average out), (b) sign/phase information, or (c) a genuine 3D geometric input such as helicity sign or vortex-line topology.

**What this test can't see.** The shell is a blind witness for any non-Fourier attack. A purely Lagrangian-geometric argument (particle trajectories, vortex line topology) has no shell counterpart, so it passes trivially and we learn nothing about it. Mark "UNTESTABLE-ON-THIS-MODEL" for purely Lagrangian proposals.

### A.5 — Tao's averaged NSE (arXiv:1402.0290)

**Model.** Modified nonlinearity F_avg(u,u) of the form Σ c(k,k₁,k₂) P(u(k₁) ⊗ u(k₂)) with frequency-local symbol, designed to have the same energy identity and the same scaling-critical estimates as true NSE but with a cascade-hollow, averaging-invariant structure that admits a tower-of-scales blowup.

**Known status.** Tao 2014 (published J. Amer. Math. Soc. 29, 601–674, 2016) proved finite-time blowup for smooth initial data.

**What this test rejects.** Any attack for 3D NSE whose every estimate is averaging-invariant (i.e. survives replacing the true bilinear c(k,k₁,k₂) by Tao's |c| ≤ 1 symbol) is FAIL-AVG — it would extend to Tao's averaged NSE where the conclusion is false. This is the **supercritical barrier** itself (§2.D of the scout). Every attack must identify a specific mechanism that breaks under averaging.

**What this test can't see.** The averaged NSE is not physical: it has no pressure, no Leray projection, no vortex-stretching geometry. Attacks that explicitly use any of these may not even be definable on the averaged model. Those attacks are provisionally "not blocked", but still must be checked against the true NSE. The barrier is a necessary filter, not sufficient.

### A.6 — Axisymmetric 3D Euler with boundary (Hou–Luo, Chen–Hou)

**Model.** 3D Euler ∂ₜu + (u·∇)u = −∇p, ∇·u = 0, on a bounded solid cylinder {(r,θ,z) : r ≤ 1, −1 ≤ z ≤ 1} with no-flux boundary, axisymmetric data with swirl.

**Known status.** Hou–Luo 2014 numerical (PNAS 111, 12968–12973) — strong evidence of finite-time singularity at corner {r=1, z=0}. Chen–Hou 2022–2025 (PNAS 2025, "Stable nearly self-similar blowup…") — computer-assisted rigorous proof of finite-time nearly-self-similar singularity in smooth bounded cylinder with smooth axisymmetric data, interior blowup. Uses stability of an approximate self-similar profile + interval arithmetic.

**What this test rejects.** Any attack claiming global regularity for 3D NSE by a mechanism that also applies to 3D Euler **in this geometry**. Specifically: if the attack argument remains when you send ν → 0, and does not rely on any parabolic regularising property, then it would apply to Euler in the Chen–Hou setup — contradiction. FAIL-AX-EULER. A proposal must identify where ν > 0 enters in an essential way (not merely in a regularising first step that then disappears).

**What this test can't see.** The Chen–Hou blowup uses a boundary. Clay is Ω ∈ {ℝ³, 𝕋³} without boundary. So this test is strict *only* against Euler-style arguments in geometries that already blow up at Euler level. A pure-NSE argument using ν > 0 can still survive if it uses viscous dissipation in an essential way.

### A.7 — Elgindi C^{1,α} 3D Euler (no-swirl)

**Model.** 3D axisymmetric Euler, no swirl, on ℝ³ (no boundary), with initial velocity in C^{1,α} for α ∈ (0, α₀] small.

**Known status.** Elgindi 2019/2021 (Ann. Math. 194, 647–727; arXiv:1904.04795) — finite-time blowup from C^{1,α} data via a self-similar profile. Uses a Biot–Savart simplification near axis and the lower regularity to give the nonlinearity algebraic (not transcendental) structure. **No swirl, no boundary**, C^∞ data still open.

**What this test rejects.** Any attack that relies on using only Lipschitz (C^{0,1}) regularity of the velocity — since Elgindi data is more regular than Lipschitz velocity (C^{1,α} velocity means Hölder gradient, stronger than Lipschitz, so velocity is C^1+). Wait — C^{1,α} is *stronger* than merely C^1, meaning ∇u exists and is Hölder; however it is *weaker* than C^∞. So an attack using **only** C^∞ data at t=0 is safe; an attack that works for any C^{1,α} data would FAIL-ELGINDI for Euler.

More precisely: the NSE regularity claim is for C^∞ data. If the proposal's proof works for *generic* C^{1,α} data, it is over-strong: Elgindi says NO at Euler level. The proposal must use **smoothness** (at least C^{1,α₀+}) or **viscosity** in an essential way. FAIL-ELGINDI means the argument does not crucially use ν > 0 or initial smoothness.

**What this test can't see.** No-swirl axisymmetric is a 2D-like reduction; the lack of vortex stretching in that direction is why Elgindi's argument works. A full-3D attack has no Elgindi analogue. Still, the fact that C^{1,α} suffices at the Euler level tells us the *margin* between known-Euler-blowup and hoped-for-NSE-regularity is thin — only ν > 0 separates them.

### A.8 — De Gregorio / Constantin–Lax–Majda 1D models

**Model.** ∂ₜω + c u ∂_x ω = c' ω ∂_x u, where u = H(ω) (Hilbert transform); CLM is c=0, c'=1; De Gregorio is c=c'=1.

**Known status.** CLM (Constantin–Lax–Majda 1985 CPAM 38, 715–724) — explicit finite-time blowup. De Gregorio 1990 — self-similar blowup, rigorously proved by Chen–Hou–Huang 2021 (Comm. Math. Phys. 383, 1559–1667; arXiv:1905.06387); also Chen 2021, Jia–Stewart–Šverák 2019. Okamoto–Sakajo–Wunsch family interpolates.

**What this test rejects.** Any attack purporting to show 3D NSE regularity by appealing only to the Biot–Savart-like structure (vorticity drives velocity, velocity transports vorticity, vortex-stretching closes the loop) — the 1D toy reproduces exactly this structure and blows up. FAIL-1D. An attack must use the 3D dimensional enhancement: e.g., three-dimensional vortex-line topology, scale-by-scale triad cancellations, or divergence-free structure that is nontrivial in 3D but trivial in 1D.

**What this test can't see.** The 1D models have no dissipation; NSE has ν Δ. An attack purely about viscous regularisation at a critical α cannot be tested here.

### A.9 — Buckmaster–Vicol non-unique weak solutions

**Model.** Standard 3D NSE, but solutions allowed to be distributional (no energy inequality enforced).

**Known status.** Buckmaster–Vicol 2019 (Ann. Math. 189, 101–144; arXiv:1709.10033) — infinitely many non-energy-admissible *distributional* weak solutions with prescribed smooth initial data. The non-uniqueness is in L²_t L²_x only, not H^s for any s large. Extensions: Cheskidov–Luo 2022 (Inventiones 229, 987–1054); Albritton–Brué–Colombo 2022 (Ann. Math. 196, 415–455) — Leray–Hopf non-uniqueness, but *forced*.

**What this test rejects.** An attack claiming **any** form of global uniqueness without using the energy inequality or a specific smoothness threshold is FAIL-BV. The convex-integration construction is smoothness-breaking, so the attack's regularity class must exceed convex-integration reach (which currently lives below H^{1/2+ε}). More importantly: an attack claiming uniqueness at the weak/distributional level for unforced NSE contradicts an already-known theorem for forced NSE and is suspicious until checked.

**What this test can't see.** Convex integration cannot produce smooth-in-x solutions at fixed t. An attack that works entirely in H^s, s large, does not encounter BV non-uniqueness. The test is a filter against attacks that over-claim at low regularity.

### A.10 — 1D Burgers with ν > 0

**Model.** ∂ₜu + u ∂_x u = ν ∂_x² u.

**Known status.** Global smoothness (Hopf–Cole transform linearises it). No blowup for any smooth data.

**What this test rejects.** An attack whose central estimate, applied in 1D, would predict blowup — the test rules out over-aggressive "energy flow to small scales" arguments. Less strictly, it rules out estimates that do not see the sign of u ∂_x u (which creates shocks in inviscid Burgers at finite time). A proposal must at minimum reproduce the Hopf–Cole / maximum-principle argument in 1D.

**What this test can't see.** 1D Burgers is scalar; no vortex stretching, no pressure. Any 3D-specific geometric attack is trivially unaffected (UNTESTABLE-ON-THIS-MODEL).

### A.11 — Beale–Kato–Majda / ESS criteria (not reduced models, but blowup criteria)

**Model.** 3D NSE, but with hypothesised bounds: ∫₀^{T*} ‖ω‖_{L∞} dt < ∞ (BKM) or ‖u‖_{L^∞_t L³_x} < ∞ (ESS).

**Known status.** BKM 1984 (Comm. Math. Phys. 94, 61–66) — such control extends smooth solution past T*. ESS 2003 (Acta Math. 189, 45–80) — same for L^{∞,3}. Quantitative version: Tao 2019 arXiv:1908.04958 — triple-exponential bound.

**What this test rejects.** An attack proposal that claims a novel a priori bound on a *weaker* norm than BMO⁻¹ or L³ must confront: why does the existing ESS machinery not already give it for free? If the claim is control of L^{5/2} for instance (subcritical — supercritical), it cannot be deduced a priori and the attack must explain why.

**What this test can't see.** BKM/ESS criteria are conditional; the test checks consistency, not the ability to break the conditional.

### A.12 — Axisymmetric NSE without boundary (ℝ³, swirl)

**Model.** Full 3D NSE on ℝ³, data axisymmetric: u(r, θ, z, t) = u^r e_r + u^θ e_θ + u^z e_z with no θ-dependence. Swirl u^θ is retained.

**Known status.** Open in full generality. With zero swirl (u^θ ≡ 0), global smoothness — Ladyzhenskaya 1968, Ukhovskii–Yudovich 1968. With swirl, conditional results only: Chae–Lee 2002, Hou–Lei 2009, Chen–Strain–Tsai–Yau 2008, Koch–Nadirashvili–Seregin–Šverák 2009, Pan 2016, Palasek 2022 single-exponential quantitative. No Type-I self-similar blowup (Chen–Strain–Tsai–Yau).

**What this test rejects.** An attack that does *not* close the axisymmetric-with-swirl case is considered not tight: axisymmetric with swirl is the simplest still-open NSE setting. FAIL-AX-SWIRL means the attack cannot handle the case where 3D geometry reduces to 2D + swirl. Conversely, an attack that closes only axisymmetric-no-swirl is merely reproducing known theorems (SP2 territory).

**What this test can't see.** Axisymmetric breaks the full translation/rotation symmetry, and may allow more leverage than general data. An attack specific to axisymmetric might not generalise.

### A.13 — Beltrami flows / stationary critical points

**Model.** Stationary solutions u with ω = λu (Beltrami), or general stationary solutions to −νΔu + (u·∇)u + ∇p = 0.

**Known status.** On 𝕋³: bounded-energy stationary Beltrami flows exist (ABC flows). On ℝ³: rigid Liouville theorem — under suitable decay, stationary solutions vanish (Galdi, Koch–Nadirashvili–Seregin–Šverák 2009 Acta Math. 203, 83–105).

**What this test rejects.** An attack using steady-state methods where Beltrami flows are a counterexample must confront them. The test is a consistency filter.

**What this test can't see.** Stationary-case tests are about steady states, not dynamics; they do not test blowup.

---

## Part B — Supercritical-barrier diagnostic

Tao's averaged NSE (arXiv:1402.0290) formalises the supercritical barrier: any proof of global regularity for 3D NSE that uses *only* scaling-invariant functional estimates and averaging-respecting structures will also prove regularity for Tao's averaged NSE — but the averaged NSE blows up. Any valid attack must therefore exploit a property that is **not averaging-invariant**.

This diagnostic is a 4-step checklist applied to every attack proposal.

### B.0 — Setup

Given an attack "proposal P", extract its **controlling estimate**: the central inequality or identity the proposal uses to propagate regularity or close a bootstrap. If there are several, treat each separately; the proposal is blocked iff each is blocked.

### B.1 — Step 1: Identify the controlling quantities

List every norm, seminorm, integral functional or functional inequality used by the proposal. For each, record:
  - functional form (e.g. ‖∇u‖_{L²}, ‖u‖_{BMO⁻¹}, ‖ω‖_{L^p}, ∫ |u·∇u|² dx);
  - type (energy, enstrophy, pressure-velocity integral, geometric functional);
  - physical dimension in mass/length/time.

### B.2 — Step 2: Scaling check

For each quantity, compute its scaling: under u_λ(t,x) = λ u(λ²t, λx), does the quantity rescale as λ^a for some exponent a?
  - If **a > 0** (quantity shrinks under rescaling): subcritical. Propagating a control on it means more than scaling — this is a good sign, but subcritical norms are known to fail a priori global control at α = 1.
  - If **a = 0**: scaling-invariant (critical). This is where all the classical attacks die.
  - If **a < 0**: supercritical (quantity grows under rescaling). Control here is **not** implied by scaling — this is where the genuinely new lives.

Failure mode: if every controlling quantity has a ≤ 0, the proposal is essentially a critical/subcritical method. It **may** still escape the barrier via Step 3, but not by scaling alone.

### B.3 — Step 3: Averaging check

For each of the controlling estimates, write it in Littlewood–Paley form (or bilinear-Fourier form if it involves the nonlinearity). Now perform Tao's averaging transformation: replace the true bilinear symbol c_true(k, k₁, k₂) ≤ |k| coming from (u·∇)u by any averaged symbol c(k,k₁,k₂) with |c| ≤ 1 on the same paraproduct support.

Ask: does the controlling estimate still hold under this replacement?

Three outcomes:
- **YES — estimate survives averaging.** The estimate sees only the size of the bilinear kernel, not its phase/sign. Combined with a = 0 from Step 2, the proposal is BLOCKED-BY-BARRIER.
- **NO — estimate fails because of a sign/phase/direction argument specific to the true NSE.** The proposal has Tao-escape potential. Identify the **differential gain**: the exact inequality or cancellation the proposal uses that fails on the averaged NSE.
- **UNCLEAR — can't easily tell without computation.** Mark UNCLEAR and demand the proposal's author produce the averaged-NSE analogue.

### B.4 — Step 4: Verdict

- **a = 0 at Step 2 AND YES at Step 3**: BLOCKED-BY-BARRIER. The argument would apply to averaged NSE; averaged NSE blows up; contradiction. Proposal cannot work as stated.
- **a > 0 at Step 2 AND YES at Step 3**: Still potentially blocked. Subcritical norms are not a priori globally controllable in the Clay regime. Demand: how is the subcritical norm controlled globally?
- **a < 0 at Step 2 (supercritical quantity) OR NO at Step 3 (averaging-breaking estimate)**: NOT-BLOCKED. Proposal survives the barrier. This does not mean the proposal succeeds — it means only that Tao's 2014 obstruction does not apply. The proposal must still survive the Part-A test matrix.

### B.5 — Worked example 1: "Pure energy method"

**Proposal.** Control ‖u‖_{L²}² + 2ν∫ ‖∇u‖_{L²}² dt ≤ ‖u₀‖_{L²}². Bootstrap to higher regularity via Gronwall-type argument on ‖u‖_{H^s} with s = 1 and the trilinear estimate |⟨(u·∇)u, Δu⟩| ≤ C ‖∇u‖_{L²}^{3/2} ‖Δu‖_{L²}^{3/2} (Gagliardo–Nirenberg in 3D).

- **Step 1.** Control: ‖u‖_{L²}, ‖∇u‖_{L²_t L²_x}, ‖∇u‖_{L∞_t L²_x}.
- **Step 2.** ‖u_λ‖_{L²} = λ^{−1/2} ‖u‖_{L²}: **supercritical, a = −1/2** (quantity grows as we zoom in). ‖∇u_λ‖_{L²} = λ^{1/2} ‖∇u‖_{L²}: subcritical, a = +1/2. The energy-dissipation integral ∫ ‖∇u‖² dt scales as λ⁰: **critical**. The controlling estimate is the trilinear Gagliardo–Nirenberg: it needs ‖∇u‖_{L²}^{3/2} ‖Δu‖_{L²}^{3/2} ≤ C ‖∇u‖_{L²}³ + ε ‖Δu‖^2, closing only when ‖∇u‖_{L²}⁶ ≤ const/ε — **supercritical closure fails**.
- **Step 3.** Does the trilinear estimate survive averaging? **YES.** The Gagliardo–Nirenberg bound |⟨(u·∇)u, Δu⟩| ≤ C ‖∇u‖^{3/2} ‖Δu‖^{3/2} uses only Sobolev embedding and Hölder; the sign of u·∇u is irrelevant. The averaged-NSE has the same energy identity and the same Gagliardo–Nirenberg bound.
- **Step 4.** Critical quantity (∫ ‖∇u‖²) + averaging-invariant estimate (Gagliardo–Nirenberg) → **BLOCKED-BY-BARRIER**. This is the classical "90 years of failure of the energy method in 3D" made precise.

### B.6 — Worked example 2: Constantin–Fefferman geometric depletion

**Proposal.** Let ξ(t, x) = ω(t, x)/|ω(t, x)|. If ξ is **Lipschitz in x** on the high-vorticity region (or more generally: if |ξ(t, x) − ξ(t, y)| ≤ L|x − y| for (x, y) in the high-|ω| set), then the vortex-stretching term ω·∇u · ω/|ω|² is depleted by a factor of ω-orthogonal differences, and a BKM-type bound closes.

- **Step 1.** Controlling quantity: Lipschitz constant of ξ, call it L(t) = sup_{(x,y) ∈ S} |ξ(t,x) − ξ(t,y)|/|x−y|, where S is the {|ω| > λ} superlevel set.
- **Step 2.** Under u_λ(t,x) = λ u(λ²t, λx), ω_λ = λ² ω(λ²t, λx) and ξ_λ(t,x) = ξ(λ²t, λx) — the direction is **unchanged**. Its spatial Lipschitz constant rescales: L_λ = λ L. So a = **+1** — **subcritical** in the direction space. Note this is not the standard (u, x) scaling behaviour: ξ lives on the **sphere bundle** and its Lipschitz constant scales with the length-rescaling, not with velocity. This is the first indicator of a non-averaging-invariant quantity.
- **Step 3.** Does the Lipschitz-direction estimate survive averaging? **NO.** Here is the differential gain. The Constantin–Fefferman (1993, Indiana Univ. Math. J. 42, 775–789) key identity reads, for the vortex-stretching integral, ∫ (ω·∇u)·ω dx = ∫ ω(x) ω(y) (ξ(x) × ξ(y)) K(x−y) dx dy (up to constants and a Riesz-kernel K). When ξ(x) ≈ ξ(y) the cross product ξ(x) × ξ(y) vanishes — this is the geometric depletion. Replace c_true(k, k₁, k₂) by the averaged |c| ≤ 1: the sign structure ξ(x) × ξ(y) is destroyed. **The depletion argument does not even make sense on the averaged NSE**, because averaging scrambles the vector direction of ω(k) between paraproduct levels.
- **Step 4.** Subcritical in the direction Lipschitz norm + averaging-breaking estimate → **NOT-BLOCKED**. The proposal survives Tao's barrier. Differential gain: the identity ξ(x) × ξ(y) is pointwise in physical space, uses Lipschitz continuity of ξ (not of ω itself), and uses the cross-product structure — none of which survives averaging.

This does **not** prove Constantin–Fefferman closes Clay — the open question is precisely whether L(t) remains finite for generic data (it does not in the Hou–Luo Euler scenario). But the proposal is barrier-free.

---

## Part C — Audit of mathematicians' proposals

Files now present: `mathematician_1_pde.md` (6 proposals M1.1–M1.6), `mathematician_2_geometric.md` (6 proposals G1–G6), `mathematician_3_vocabulary.md` (5 Part-A proposals A1–A5 plus 4 Part-B technique nodes B1–B4, audited here for A1–A5 only since Part-B nodes are graph meta-objects, not attack proposals).

Each audit: controlling quantity, Part-A survival over the reduced cases (only cases that are actually testable are listed — UNTESTABLE skipped to save space), Part-B diagnostic verdict, overall judgement.

### C.1 — M1 (PDE) audits

**M1.1 — Logarithmically supercritical hyperdissipation, closing the 5/4 − ε gap.**

- Controlling quantity: log-weighted Ḣ^s energy ‖u‖²_{Ḣ^s} with Fourier weight g(|ξ|) = |ξ|^{2c/log(2+|ξ|)}; bilinear paraproduct commutator [T_{u_{low}}, D^{1/2}].
- Part A:
  - 2D: PASS — 2D NSE is global; the proposal is α-strict dissipation above 1, consistent.
  - Hyperdissipative α ≥ 5/4: PASS by definition (Katz–Pavlović 2002, Tao 2009 handle this).
  - Fractional α ∈ (1, 5/4): this **is** the target regime. M1.1 claims α = 5/4 − c/log. FAIL-TEST is avoided *only* if the commutator log-gain is real. The proposal's own failure-mode 3 identifies the right falsifier: the *Katz–Pavlović 2005 dyadic shell model* with this specific log-corrected dissipation. Dyadic shell: if the shell with log-weighted dissipation g(λ_n) = λ_n^{2c/log(2+λ_n)} still has finite-time blowup at c ≤ c₀ of the KP constant, the PDE proposal is **preempted** at the toy level. I mark this as MANDATORY-PRE-CHECK. Until done, status is UNVERIFIED.
  - Tao averaged NSE at α = 5/4 − ε: Tao's 2014 construction is at α = 1; the scout does not have the averaged-hyperdissipative blowup result. M1.1 correctly notes that Tao's construction does not obviously extend above α = 1. Provisional PASS.
  - Chen–Hou Euler: PASS (ν = 0 destroys the log-correction anyway).
  - Elgindi Euler: PASS.
- Part B:
  - Step 1: log-weighted Ḣ^s energy, commutator log-gain.
  - Step 2: with the hyperdissipative modification, the critical Ḣ^s has s = 5/2 − 2α (adjusted): above α = 5/4 with log, the controlling quantity is at critical scaling; the log-gain is dimensionless. a = 0.
  - Step 3 (averaging): YES, the proposal explicitly concedes averaging-invariance. The commutator estimate uses paraproduct symbol size only, not sign — it survives Tao's averaging.
  - Step 4: BLOCKED-BY-BARRIER **at α = 1**; NOT-BARRIER-APPLICABLE at α > 1 (Tao's construction has not been lifted above 1). Proposal's self-audit matches.
- Overall: INCREMENTAL, provisionally sound. **Concrete test**: run the proposed estimate on the Katz–Pavlović shell with dissipation g. If the shell still blows up under this log-correction, the PDE version is impossible — this is a 1-week calculation. If the shell closes, the PDE attempt is worth a 3-month effort. Rank: MEDIUM.

**M1.2 — Two-scale frequency envelope, Tao triple-exp → double-exp.**

- Controlling quantity: ‖Δ_N u‖_{L²} at two dyadic levels N_low < N_high, with k = k(t) = log₂(N_high/N_low).
- Part A:
  - 2D: PASS (2D ESS is trivial because L^∞_t L³_x is a priori finite in 2D).
  - Hyperdissipative α ≥ 5/4: PASS.
  - Tao averaged NSE: M1.2 *explicitly concedes* that the two-scale envelope depends only on scalar LP norms, which the averaged NSE preserves. So if the argument gave an unconditional bound, it would close averaged NSE — contradiction. But M1.2 gives only *conditional* improvement (under hypothesised L^∞_t L³_x), and averaged NSE violates the hypothesis. PASS, by consistency with the conditional form.
  - Chen–Hou / Elgindi Euler: PASS (ν = 0 makes the Carleman step vacuous).
  - Shell: UNTESTABLE (no L³ concept on the shell).
- Part B:
  - Step 1: L^∞_t L³_x hypothesis; N_low, N_high, k; Carleman weight.
  - Step 2: L³ is critical (a = 0); k is dimensionless; the bound is critical.
  - Step 3: YES — averaging-invariant, by the proposal's own admission. The two-scale envelope uses only the scalar energy ‖Δ_N u‖².
  - Step 4: BLOCKED-BY-BARRIER if read as a *globally-regular* argument. But M1.2 is a *quantitative-conditional* sharpening — it only claims "if L³ is bounded by A, H^k is bounded by exp(exp(A^c))". This conditional is **not** blocked by the barrier, because averaged NSE's L³ is ∞ (the hypothesis fails), so the conditional conclusion says nothing about averaged NSE. NOT-BLOCKED as conditional.
- Overall: PUBLISHABLE if technically correct; zero Clay progress. Specific test the proposal should survive: compute the k(t)-accounting on a specific near-singular scenario (e.g., a scaled Hou–Luo-type self-similar profile with ν > 0) to verify the k = O(log A) claim. Rank: HIGH among incremental targets.

**M1.3 — Larger-than-BMO⁻¹ critical space via Lipschitz-ξ constraint.**

- Controlling quantity: ‖u‖_X = ‖u‖_{BMO⁻¹} + κ, where κ = Lipschitz constant of ξ = ω/|ω|.
- Part A:
  - 2D: PASS (in 2D, ξ is trivially constant ±e_z, κ = 0, so X reduces to BMO⁻¹).
  - Hyperdissipative α ≥ 5/4: PASS.
  - Elgindi C^{1,α} Euler: **CRITICAL TEST**. Elgindi's profile has velocity C^{1,α} and *vorticity direction* that aligns with the self-similar collapse; Elgindi's construction explicitly has ξ near-singular at the blowup. If M1.3's ball Picard-closes globally-small for data with Lipschitz ξ, and if Elgindi-type data (restricted to be small enough) have finite κ away from the blowup, we must ask: does the Picard ball include the Elgindi near-data-small version? If YES, M1.3 would give global regularity for Euler-near-Elgindi — FAIL-ELGINDI. The viscosity ν > 0 is what saves M1.3: the Picard map uses e^{νtΔ}, so ν = 0 breaks the heat-semigroup contraction. Hence M1.3 passes Elgindi *only because* it is intrinsically NSE-specific. PASS (ν-essential).
  - Chen–Hou axi Euler: PASS by same argument (boundary + ν = 0).
  - Axisymmetric no-swirl NSE: the proposal's own failure-mode 3 notes: axisymmetric no-swirl has ξ = ±e_θ trivially, so κ ≡ 0, and M1.3 would give Koch–Tataru in axisymmetric (globally) — but that's already known (Ladyzhenskaya 1968). OK consistent. For axisymmetric **with swirl**, ξ is non-trivially r,z-dependent; M1.3 would give small-data global regularity for data with small X-norm *and* Lipschitz ξ. **This is not obviously known**; it would be new, though only small-data. PASS with a research sub-target.
  - BV non-uniqueness: PASS (works in BMO⁻¹ or X, both much stronger than L^p_t L^2_x where BV lives).
  - Tao averaged NSE: the Lipschitz-ξ constraint is not definable on averaged NSE (no pointwise vorticity direction that transforms correctly under averaging). PASS-by-irrelevance.
- Part B:
  - Step 1: ‖u‖_{BMO⁻¹}, κ.
  - Step 2: BMO⁻¹ critical (a = 0); κ scaling is the proposal's failure-mode 1. In the normalisation "Lip-constant on unit ball in physical space", κ scales as λ (subcritical, a = +1). On the Biot–Savart support (which itself rescales), the effective scaling is more subtle. The proposal's own concern is right: if κ scales non-trivially, X is not scale-invariant and the whole Picard framework fails. Status: NEEDS-VERIFICATION. Provisionally assume the scaling works out to a = 0 with a non-trivial direction-Lipschitz constant.
  - Step 3: NO, strongly. This is essentially worked example B.6: Lipschitz-ξ is exactly the Constantin–Fefferman geometric-depletion quantity, which averaging destroys (Tao's averaged NSE has no pointwise vector direction of vorticity).
  - Step 4: NOT-BLOCKED. Differential gain: Lipschitz vorticity direction on Biot–Savart support.
- Overall: the proposal is moonshot-level but explicitly only small-data. The barrier is escaped. The real open question is failure-mode 2: closing the bilinear estimate. This is precisely the step that has blocked Chae 2003–2007 and Grujić–Ruzmaikina. Specific test: isolate the bilinear estimate ‖ξ(B(u,v))‖_{Lip} ≤ F(κ_u, κ_v, ‖u‖_{BMO⁻¹}, ‖v‖_{BMO⁻¹}) and attempt it on a tube-of-vorticity test case where both u and v are explicit. Rank: HIGH among moonshots.

**M1.4 — Frequency-envelope monotonicity with vortex-stretching-budget Φ = ∫|ω|² χ(ξ·e_max(S)) dx.**

- Controlling quantity: Φ(u), a functional on vorticity alignment with principal strain axis.
- Part A:
  - 2D NSE: PASS trivially (ω ⊥ plane, ξ·e_max(S) is either undefined or constant; Φ = 0 or constant). No information.
  - Axisymmetric no-swirl NSE: PASS, Φ = 0 or constant (ω = ω_θ e_θ, e_max may lie outside e_θ).
  - **Chen–Hou axi Euler with boundary: CRITICAL TEST**. The Chen–Hou blowup has smooth data → smooth blowup at finite time. If Φ is monotone under Euler in this setup, it gives a contradiction with the Chen–Hou proof (which rigorously shows blowup). Hence **Φ MUST NOT be monotone under inviscid Euler** — the ν = 0 flow must admit Φ growth. The proposal's own step 2 shows d/dt ∫|ω|² = 2∫Sω·ω + 2ν∫ω·Δω; setting ν = 0 gives d/dt Φ = 2∫(Sω·ω)χ + |ω|²(dχ/dt), and the proposal hopes ν-dependent cancellation makes this ≤ 0 only when ν > 0. That is the right structure — PASS, ν-essential. But **verify explicitly**: compute d/dt Φ on the Chen–Hou near-blowup profile as ν → 0 and confirm it is positive there.
  - **Elgindi C^{1,α} Euler: CRITICAL TEST**. Same logic: Φ must not be monotone under Euler on the Elgindi profile. Since Elgindi is axisymmetric no-swirl, ω ∥ e_θ, Φ = 0 structurally, so not informative. PASS-by-triviality.
  - **Burgers vortex**: the proposal's own failure-mode 1. Burgers vortex is a forced stationary NSE solution where Φ > 0 constant. Unforced Burgers-type profiles have transient Φ growth; this kills unconditional monotonicity. FAIL-UNCONDITIONAL. The proposal confesses this: only conditional Φ-monotonicity is realistic. **Unconditional version is FAIL-BURGERS**.
  - Dyadic shell: UNTESTABLE (no vector ω, no strain tensor, no e_max).
  - Tao averaged NSE: UNTESTABLE (no canonical ω/ξ/S).
- Part B:
  - Step 1: Φ, ξ·e_max(S) alignment.
  - Step 2: Φ has dimensions of |ω|² · volume; |ω|_λ = λ² ω, volume scales as λ⁻³, so Φ scales as λ^{4−3} = λ. **Subcritical** (a = +1); growing under zoom-in would imply control... wait, subcritical means Φ grows under zoom-in which is actually the *wrong* sign for a Perelman-analogue (Perelman's W grows under zoom-in too, but *decreases* under flow; the combination is the trick). So Φ being subcritical is fine if d/dt Φ ≤ 0.
  - Step 3: NO. The eigenvector e_max(S) is a pointwise geometric functional of ∇u_sym; averaging destroys this geometric pointwise structure (Tao's averaged NSE does not preserve even the symmetric gradient meaningfully).
  - Step 4: NOT-BLOCKED. Differential gain: pointwise alignment ξ·e_max(S), which is a genuinely geometric-not-averaging-invariant quantity.
- Overall: MOONSHOT, already self-confessed. Primary test the proposal should survive: **compute d/dt Φ on the Burgers vortex explicitly** and on the axisymmetric-with-swirl approach to singularity (Hou–Lei-style conjectural profile). If Φ is *not* monotone on any plausible near-singular NSE flow, the approach collapses to "Φ monotone on generic data only" which is not enough. Rank: MEDIUM (high-variance moonshot).

**M1.5 — Besov-ESS via frequency-blocked Carleman.**

- Controlling quantity: ‖u‖_{L^∞_t Ḃ^{−1+3/p}_{p,∞}} for p > 3; Liouville theorem for ancient solutions at this regularity.
- Part A:
  - 2D NSE: PASS (L^∞_t L³_x is bounded, so Besov is also bounded a priori in 2D). No new information.
  - Hyperdissipative α ≥ 5/4: PASS.
  - **Shell falsifier (failure-mode 4)**: Cheskidov dyadic shells have blowup in Besov-analogue norms. If the proposal's ESS extends to the shell model, FAIL-SHELL. The proposal itself flags this. **Mandatory pre-check**: compute the Cheskidov shell analogue of ‖·‖_{Ḃ^{−1+3/p}_{p,∞}} and verify it actually grows to ∞ before blowup. If yes, consistent (shell blowup corresponds to Besov blowup, and the proposed ESS says "finite Besov → regular" which does not apply).
  - **Cheskidov–Luo 2022 falsifier (failure-mode 3)**: non-unique weak solutions in L^p_t L^∞_x for p < 2. This is a **Serrin-scaling-endpoint** sharp result. The proposal's X = Ḃ^{−1+3/p}_{p,∞} is at a related but different scaling; if Cheskidov–Luo can be lifted to this Besov space, Besov-ESS fails. Pre-check required.
  - Tao averaged NSE: The Besov-ESS is a conditional criterion (finite norm → smooth). On averaged NSE the norm goes to ∞ (since averaged NSE blows up), so the conditional vacuously holds. PASS-by-vacuity.
  - Chen–Hou Euler: PASS (ν essential for Carleman).
- Part B:
  - Step 1: Besov Ḃ^{−1+3/p}_{p,∞} norm, Carleman weight with frequency-block structure, ancient-profile Liouville.
  - Step 2: critical (a = 0).
  - Step 3: UNCLEAR tending to NO. The Carleman estimate uses the νΔ parabolic positivity. The Liouville step uses scaling rigidity + a priori Besov bound. If the Liouville closes via classification of ancient solutions using the *specific* Biot–Savart / pressure structure, that is non-averaging-invariant. If it closes via generic critical-Besov bounds, averaging-invariant.
  - Step 4: depends on Liouville structure. Provisional NOT-BLOCKED (parallel to ESS itself, which has always been read as barrier-free as a conditional criterion).
- Overall: INCREMENTAL on SP3. Test the proposal: check whether the Besov-blocked Carleman sums in j — failure-mode 2 is the technical gating step. Rank: HIGH among incremental targets (on SP3 frontier).

**M1.6 — Helicity-modified Koch–Tataru.**

- Controlling quantity: ‖u‖_{BMO⁻¹} + |H(u)|, H(u) = ∫ u·ω dx.
- Part A:
  - 2D NSE: PASS (H identically zero for planar flow, no constraint).
  - Axisymmetric no-swirl NSE: PASS, H = 0 identically (u^θ = 0 → ω^θ dominates; u·ω = u^r ω^r + u^z ω^z, and in no-swirl u^θ = 0, ω has only θ-component — so u·ω = 0).
  - **Shell model**: UNTESTABLE (no helicity analogue on scalar amplitudes).
  - **Tao averaged NSE**: the proposal's own failure-mode 3 is the decisive test. Tao's 2014 construction preserves energy but was not designed to preserve helicity. Q: can Tao's construction be modified to preserve helicity? Answer: the constraint on c(k,k₁,k₂) to preserve helicity is an additional bilinear identity; it is plausible that a modified Tao construction with this constraint still admits blowup. **Pending verification**, tentatively FAIL-AVG (M1.6's own honest grade is "BLOCKED-BY-BARRIER, probably").
  - Chen–Hou Euler: the viscous dissipation term in dH/dt, −2ν∫∇u:∇ω, vanishes. Euler conserves helicity exactly. The Chen–Hou blowup has smooth initial data with some specific helicity; the blowup scenario has helicity preserved up to the singularity, so H(u(t)) = H(u₀) for all t < T★ — finite. This does not contradict "|H(u)| small implies regularity". No contradiction, PASS. BUT the point is that helicity is preserved under Euler, not non-increasing; so the proposal's picture of helicity as *small* being preserved is correct for Euler. For NSE with dissipation, the proposal's failure-mode 1 is right: helicity can grow or shrink in NSE.
  - Elgindi C^{1,α} Euler (no swirl): helicity is identically zero (same argument as axisymmetric no-swirl NSE). The Elgindi blowup has H = 0 throughout, which is consistent with the proposal's "small H → regularity" only if the proposal also requires small BMO⁻¹, which Elgindi's data can violate. PASS (Elgindi data has large BMO⁻¹ equivalent).
- Part B:
  - Step 1: ‖u‖_{BMO⁻¹}, H(u).
  - Step 2: BMO⁻¹ critical (a = 0); H(u) is 3D scale-invariant (scout line 71, confirmed by the author's computation). Both a = 0.
  - Step 3: YES, provisionally. The bilinear Koch–Tataru closure is paraproduct-based and averaging-invariant. Helicity's preservation constraint can likely be built into a modified averaged NSE.
  - Step 4: BLOCKED-BY-BARRIER, consistent with proposal's self-audit.
- Overall: Low-priority per proposal's own confession. The test that would unambiguously confirm the block: construct Tao's averaged NSE with helicity-preserving c(k,k₁,k₂) and verify finite-time blowup still occurs. Rank: LOW.

### C.2 — M2 (geometric) audits

**G1 — Lipschitz-direction self-consistency for ξ = ω/|ω|.**

- Controlling quantity: κ(t) = ‖∇ξ‖_{L^∞(Ω_M(t))}, Osgood-style feedback κ(t) ≤ C_ν ∫₀ᵗ κ(s)^p ds, p < 1.
- Part A:
  - 2D NSE: PASS trivially (ξ = ±e_z constant, κ = 0).
  - Axisymmetric no-swirl NSE: PASS trivially (ξ = ±e_θ, κ = 0 in the bulk, singular on axis only — and axis is a measure-zero set).
  - Chen–Hou axi Euler with boundary: **CRITICAL TEST**. Chen–Hou has blowup. Their blowup profile has well-characterized ξ structure: ξ is nearly self-similar, with ∇ξ developing a specific blow-up rate. In the Chen–Hou setup ν = 0, so the proposal's viscous-smoothing mechanism does not apply. PASS (ν-essential).
  - Elgindi C^{1,α} Euler no-swirl: Elgindi's blowup has ω = ω_θ e_θ, so ξ is constant in the bulk. Not a testing case.
  - Hou–Luo axisymmetric Euler with swirl: the numerical scenario has ω concentrating near the corner; ξ direction twisting there. **If** the proposal's argument (sub-linear Osgood feedback with viscous smoothing) applies at ν = 0, it contradicts Hou–Luo, FAIL-HL. If ν > 0 is essential, PASS. The proposal's viscous term in the ξ-evolution (step 1) is ν|ω|⁻¹P_{ξ^⊥}(Δω), which vanishes at ν = 0. PASS (ν-essential), with the warning that this is exactly the delicate place where the Osgood inequality must fail at ν = 0.
  - Dyadic shell: UNTESTABLE (no vector ξ).
  - Tao averaged NSE: UNTESTABLE (no pointwise ω/|ω|).
- Part B:
  - Step 1: κ(t).
  - Step 2: κ subcritical (a = +1, length-rescaling).
  - Step 3: NO. This is essentially worked example B.6. Averaging destroys the pointwise direction ξ.
  - Step 4: NOT-BLOCKED. Differential gain: pointwise vorticity-direction Lipschitz + Biot–Savart 0/0 cancellation.
- Overall: barrier-free. Real test (proposal's own failure-mode 1): verify the Osgood feedback is actually sub-linear (p < 1) and not linear (p = 1). The proposal sketches a route through |ω|⁻¹ Biot–Savart cancellation. A specific first check: on the axisymmetric-with-swirl case, compute the κ-feedback explicitly. If sub-linear there, the narrowed result of G1 is genuinely new. Rank: HIGH.

**G2 — Perelman-analogue W-entropy Φ_ν(u, t) = ∫(|ω|² + λν|∇u|²) e^{−φ} dx.**

- Controlling quantity: Φ_ν with co-evolving weight φ satisfying a backward heat equation.
- Part A:
  - 2D NSE: PASS — check that Φ_ν reduces to a known 2D functional. ω is scalar, |ω|² transports, ∫|ω|² e^{−φ} with φ a Gaussian-in-x is a weighted-enstrophy functional known in 2D; well-defined, consistent with 2D global regularity. PASS.
  - Hyperdissipative α ≥ 5/4: PASS (Φ_ν well-defined; no constraint).
  - **Chen–Hou axi Euler: CRITICAL TEST**. ν = 0 version: Φ_0 = ∫|ω|² e^{−φ} dx. Does Φ_0 stay bounded along the Chen–Hou blowup, or grow? Chen–Hou's vorticity concentrates and |ω| → ∞ on a ball of shrinking radius; ∫|ω|² grows. With Gaussian e^{−φ(x,t)}, locally near blowup e^{−φ} is bounded below; so Φ_0 grows. This is CONSISTENT with Euler blowup (Φ_0 is *not* monotone under Euler). The proposal must show ν > 0 makes Φ_ν monotone. PASS (ν-essential at the structural level).
  - **Elgindi C^{1,α} Euler**: same structure. Φ_0 grows through the Elgindi blowup. ν-essential. PASS.
  - Axisymmetric NSE (no-swirl): ω scalar (ω = ω_θ/r · r), Φ_ν well-defined, consistent with known global smoothness. PASS.
  - Dyadic shell: UNTESTABLE (no |ω|² or |∇u|²).
  - Tao averaged NSE: M2's Part-B self-audit claims that averaging destroys the pressure-stretching cancellation. Genuine: the weight φ is chosen so that the Leray-projection pressure term integrates to zero; Tao's averaged NSE has no Leray projection, so no analogue of φ. UNTESTABLE on averaged NSE, hence PASS-by-non-applicability.
  - Burgers vortex: the proposal's step 5 key term is d χ(alignment)/dt; M1.4's failure-mode 1 (Burgers-vortex counterexample) applies here too — if Φ_ν is not monotone on Burgers, the unconditional version fails. M2 does not explicitly treat this; **pre-check: evaluate Φ_ν's time derivative on the Burgers vortex.** Flagged CONSISTENCY-WITH-M1.4.
- Part B:
  - Step 1: Φ_ν, weight φ.
  - Step 2: M2 computes Φ_ν scales as λ⁵ under u_λ (supercritical, a = −5/2... wait, check: |ω|² scales as λ⁴, |∇u|² scales as λ⁴, volume scales as λ⁻³, so Φ_ν scales as λ^{4−3} = λ. That is subcritical, a = +1, NOT supercritical as M2 claims). Let me recheck M2's computation: "[velocity]² · [length]³ · e^{−φ}". Velocity squared is |u|², not |ω|² or |∇u|². If it's really the kinetic energy density |u|²/2 integrated with weight, that scales as λ² · λ⁻³ = λ⁻¹, supercritical. But the proposal writes |ω|² + λν|∇u|², both of which scale as λ⁴ * λ⁻³ = λ, subcritical. **M2's scaling claim is incorrect** — or relies on a choice of λν term the paper does not spell out. Flagged as SCALING-ERROR; the Perelman-analogue claim that Φ_ν is supercritical likely needs reformulation.
  - Step 3: NO, averaging destroys Leray-pressure cancellation. Genuine.
  - Step 4: NOT-BLOCKED if the supercritical claim is repaired; **blocked/empty** if Φ_ν is actually subcritical (then it's just a weighted enstrophy, which is well-known not to be monotone).
- Overall: MOONSHOT. **Mandatory first check**: redo the scaling computation. If Φ_ν is subcritical, the proposal collapses. If supercritical (via a term M2 has in mind but did not spell out), then M1.4-style Burgers-vortex checks apply, and so does the d/dt-under-Euler-growth test (positive on Chen–Hou profile). Rank: MEDIUM (high variance).

**G3 — Arnold/Khesin SDiff curvature + Bochner.**

- Controlling quantity: Jacobi-field growth ‖Y(t)‖² along NSE geodesic; SDiff sectional curvature K_σ.
- Part A:
  - 2D NSE: Arnold's SDiff(𝕋²) has sectional curvatures computed (Arnold 1966 explicitly); they are known to be of mixed sign but the 2D case has enough positive curvature to be consistent with global smoothness. PASS but tautological.
  - 3D Chen–Hou Euler with boundary: the Arnold framework for bounded domains with boundary is delicate (Ebin–Marsden have it on closed manifolds; bounded with boundary has extra layer). At minimum, the Chen–Hou blowup must be consistent with SDiff geodesic-flow framework: indeed a smooth Euler solution on its lifespan is a smooth geodesic; the blowup at T★ is a geodesic incompleteness. The SDiff manifold is geodesically incomplete — this is well-documented (Ebin–Marsden 1970 noted such). So no contradiction; PASS. But also: the SDiff curvature framework has existed 60 years without producing a regularity theorem, and it is consistent with known blowup. PASS-by-consistency, no new content.
  - Elgindi C^{1,α} Euler: the Arnold framework requires enough smoothness for geodesic computations; C^{1,α} is on the edge. UNTESTABLE at this regularity.
  - Dyadic shell: UNTESTABLE (no Lie group).
  - Tao averaged NSE: UNTESTABLE. M2 correctly notes averaged NSE has no geodesic-flow interpretation.
- Part B:
  - Step 1: K_σ, ‖Y(t)‖², Bochner formula on SDiff.
  - Step 2: curvature scales as λ²; Y ~ velocity scales as λ. Jacobi energy scales accordingly. Mixed.
  - Step 3: NO. Lie bracket structure is non-averaging-invariant (averaging destroys Jacobi identity).
  - Step 4: NOT-BLOCKED in principle.
- Overall: M2's own honest grade — MOONSHOT, 60-year negative empirical prior. Specific test: compute SDiff Ricci on the specific Euler trajectory that Chen–Hou shows blows up. If Ricci goes to −∞ there, it's the right sign for "Jacobi instability = blowup"; if it stays bounded, the Bochner program fails at the target case. Rank: LOW.

**G4 — Type-II self-similar blowup no-swirl axisymmetric.**

- Controlling quantity: pointwise a priori bound on ω^θ/r (supercritical, transport-conserved).
- Part A:
  - 2D NSE: N/A (not 3D axisymmetric).
  - Axisymmetric no-swirl NSE: this is the target regime. **Known globally smooth** (Ladyzhenskaya 1968). So what is G4 actually adding? G4 aims to close the Type-II self-similar case, which is a statement about the structure of *hypothetical* ancient profiles; since no-swirl is globally smooth, all ancient profiles must be trivial — this is what Koch–Nadirashvili–Seregin–Šverák 2009 already establishes under bounded-profile hypotheses. G4 sharpens to Type-II self-similar class. PASS. (Incremental over known, by proposal's own honest grade.)
  - Axisymmetric with swirl: proposal's own failure-mode 1 notes ω^θ/r is no longer transported. G4's method does not extend. Consistent.
  - Chen–Hou Euler: ν = 0, G4's Liouville chain uses NSE-specific KNSŠ theorems; PASS (ν-essential, inapplicable to Euler).
  - Tao averaged NSE: M2 correctly notes averaging destroys axisymmetry. UNTESTABLE → PASS-by-non-applicability.
- Part B:
  - Step 1: self-similar profile equation, bounded ω^θ/r, Liouville.
  - Step 2: ω^θ/r is a pointwise bound, supercritical (a < 0). KNSŠ's Liouville is a scaling-rigidity statement.
  - Step 3: NO. The pointwise bound uses axisymmetric transport structure.
  - Step 4: NOT-BLOCKED.
- Overall: INCREMENTAL, on SP2 frontier. Genuine publishable target. Rank: HIGH among incremental targets.

**G5 — Quantitative viscous damping against Elgindi profile.**

- Controlling quantity: eigenvalue λ(ν) of L_Elg + νΔ.
- Part A:
  - 2D NSE: N/A.
  - Elgindi C^{1,α} Euler: the *input model*. At ν = 0, Elgindi proves blowup. G5's question: does νΔ stabilise? This is a well-posed spectral question.
  - Chen–Hou axi Euler: different blowup scenario, different linearisation; G5's specific L_Elg does not apply.
  - Dyadic shell, Tao averaged NSE: UNTESTABLE (no Biot–Savart-in-fundamental-model reduction).
- Part B:
  - Step 1: L_Elg linearisation around Elgindi profile; νΔ.
  - Step 2: Elgindi profile is at C^{1,α} regularity which is *not* a Clay regularity setting. The comparison is with a non-smooth ancient solution, not with Clay smooth data. a depends on whether we consider the profile's scaling (self-similar) or the full NSE scaling. Within Elgindi's fundamental-model reduction, the relevant scaling is specific. Provisionally a = 0 (critical within that regime).
  - Step 3: NO. Elgindi's Biot–Savart fundamental-model reduction is averaging-destroying; averaging has no C^{1,α} analogue.
  - Step 4: NOT-BLOCKED.
- Overall: INCREMENTAL / SP6. The proposal's own honest grade is right. Note: this does not touch C^∞ Clay (Elgindi's mechanism vanishes at C^∞). Rank: HIGH among C^{1,α}-targeted sub-problems.

**G6 — Obstruction-class cohomology.**

- Controlling quantity: cohomology class [σ] ∈ H^k(M; 𝒞).
- Part A: UNTESTABLE on every reduced model until the sheaf 𝒞 is concretely defined. 
- Part B: UNTESTABLE by the diagnostic — the proposal itself concedes the class may either be trivial (Kuiper) or equivalent to an analytic estimate already known. **If equivalent to averaging-invariant analytic estimate, BLOCKED-BY-BARRIER.** If genuinely non-analytic (topological), trivial by Kuiper.
- Overall: M2's own honest grade — LOW priority, likely BLOCKED. Rank: VERY LOW. Skip unless a toy-model feasibility check (e.g., a meaningful non-trivial obstruction class on the dyadic shell model) returns positive.

### C.3 — M3 (fresh-vocabulary) audits

**A1 — Zero-noise-limit pathwise Wasserstein Otto action.**

- Controlling quantity: 𝒜_ε(u), pathwise Otto action.
- Part A:
  - 2D NSE: PASS trivially (unforced 2D is globally smooth; 𝒜_ε presumably finite).
  - **Shell**: no vorticity density in the Otto-calculus sense on discrete amplitudes — UNTESTABLE.
  - **Tao averaged NSE**: A1's own Part-B notes averaging destroys the mass-transport structure of ρ_ω. UNTESTABLE → PASS-by-non-applicability.
  - Chen–Hou Euler: ν = 0, A1 uses stochastic NSE with ν + ε viscosity, ε → 0. Not directly applicable to Euler.
  - Forced NSE uniqueness (Albritton–Brué–Colombo): A1 uses additive noise (transport-like); the ABC non-uniqueness is for a specific vortex-ring forcing. Different context. No conflict.
- Part B:
  - Step 1: 𝒜_ε, Wasserstein-2 tangent metric, relative entropy H(ρ_ω | Leb).
  - Step 2: A1 proposes a supercritical or at-best-critical quantity; the proposal's own failure-mode 1 is that 𝒜_ε reduces to ν∫|∇u|² (critical), i.e., **A1's own honest audit says the quantity may collapse to critical dissipation**, in which case a = 0. Without collapse, supercritical.
  - Step 3: NO, provisionally — Otto calculus on ρ_ω uses spatial geometry (mass transport) that averaging destroys. A1 correctly argues this.
  - Step 4: NOT-BLOCKED (if not collapsed). BLOCKED (if collapsed).
- Overall: 20% chance barrier-free, per A1's own estimate. Specific test: compute 𝒜_ε on a scaled Navier-Stokes solution (e.g., self-similar Leray ansatz) and check whether 𝒜_ε reduces to ν∫|∇u|² up to lower-order terms. If yes, collapse; if no, genuine new functional. Rank: MEDIUM.

**A2 — Regularity-structures reclassification with δ-margin subcriticality.**

- Controlling quantity: renormalisation constants C_ν for SPDE with Besov-(−1/2−ν) noise.
- Part A:
  - 2D NSE: PASS, not in the target regime.
  - **Tao averaged NSE**: **A2 concedes its argument is Littlewood–Paley-based, averaging-invariant**. Would extend to averaged NSE. But averaged NSE does not even admit a natural Hairer-regularity-structures framework; the analysis is about the true paraproduct. Regardless, a critical-margin bound on deterministic NSE via this route would be averaging-invariant. FAIL-AVG under the (presumed) extension of averaging to the SPDE regime.
  - Chen–Hou Euler: ν_noise = 0, A2 is SPDE-based; does not apply.
- Part B:
  - Step 1: C_ν, regularity-structures renormalisation, Bruned–Chandra–Chevyrev–Hairer Hopf algebra.
  - Step 2: critical at the ν = 1/2 limit.
  - Step 3: YES. A2 concedes this explicitly.
  - Step 4: BLOCKED-BY-BARRIER **if read as a route to Clay**. As a sharpening of Koch–Tataru small-data threshold, potentially BARRIER-IRRELEVANT (because all small-data Koch–Tataru is already critical and OK within the barrier).
- Overall: 10% chance of even measurable improvement over Koch–Tataru. No Clay-touching. Rank: LOW.

**A3 — Ergodic-hierarchy Furstenberg lift on statistical regularity.**

- Controlling quantity: invariant measure μ, Foias–Prodi determining-mode rigidity.
- Part A:
  - 2D NSE: PASS trivially (Hairer–Mattingly ergodicity holds, 2D is globally smooth).
  - **Forced NSE (general)**: this is A3's target. Forced case has non-uniqueness open (ABC 2022 settled it negatively for a specific forcing). A3's claim is about the *generic* forced case. Consistent with ABC (which is a specific data counterexample).
  - **Unforced Clay**: A3's failure-mode 2 confesses the f → 0 limit is vacuous. A3's own honest grade: MOONSHOT for unforced. Skip this direction.
  - Chen–Hou Euler: ν = 0, no invariant measure in the usual sense. UNTESTABLE.
  - Tao averaged NSE: A3 correctly notes averaging destroys Foias–Prodi rigidity. UNTESTABLE → barrier-escape.
- Part B:
  - Step 1: μ, Foias–Prodi determining modes.
  - Step 2: the determining-modes rigidity is scaling-aware but the rigidity claim is dimension-theoretic (finite Hausdorff dim of attractor), not norm-based. Not obviously scaling-critical.
  - Step 3: NO (Foias–Prodi rigidity is non-averaging per A3's argument).
  - Step 4: NOT-BLOCKED.
- Overall: for **forced** NSE statistical regularity, real research target; for unforced Clay, kills itself on f → 0. A3's own grade is right. Rank: MEDIUM for forced statistical sub-problem.

**A4 — Mechanized polynomial search for Perelman-analogue.**

- Controlling quantity: polynomial invariants J(u, ∇u, ..., ∇^k u); Positivstellensatz certificates.
- Part A: the proposal is a **search procedure**, not an attack; its reduced-case audit is about the search's outputs, not the procedure itself.
  - For any candidate Φ returned by the search, we would re-apply the full Part A matrix.
  - **Consistency check**: the search enumerates symmetry-invariant polynomials and tests monotonicity. If it returns Φ monotone under NSE but *also* monotone under Euler, that contradicts Chen–Hou. Hence the search must be configured so that monotonicity depends on ν > 0, or flagged if Φ is ν-independent.
  - A4 identifies the scaling weight explicitly (supercritical target), which rules out Φ = enstrophy (critical) and Φ = energy (supercritical by λ⁻¹ but already known not monotone in 3D).
  - **Limitation** (A4's own failure-mode 1): combinatorial explosion at degree ≥ 5. The known Perelman W-entropy for Ricci is built from curvature scalars that are degree-2 in curvature = degree-4 in the metric; plausibly an NSE analogue lives at degree 4–8.
- Part B:
  - Step 1: the search space of polynomial Φ.
  - Step 2: A4 restricts to a chosen supercritical weight — by construction, a < 0.
  - Step 3: for each candidate, the diagnostic must be applied individually. A4 builds in Leray projection, so candidates using pressure non-locally are non-averaging-invariant.
  - Step 4: the search procedure is not itself blocked; its outputs must be audited one by one.
- Overall: A4 is a **meta-strategy**. Value: high, because even a negative result (provably no low-degree Perelman-analogue) is a publishable obstruction theorem; positive result would be transformative. Rank: **HIGHEST among M3 proposals** (7% Clay-touching chance is very high in this portfolio).

**A5 — Fisher information of vorticity magnitude.**

- Controlling quantity: F(t) = ∫ |∇ log |ω|²|² |ω|² dx.
- Part A:
  - 2D NSE: F is well-defined; 2D enstrophy bound implies finite F. Consistent with 2D global smoothness. PASS.
  - Chen–Hou axi Euler: at ν = 0 the dissipation term −ν F in A5's inequality vanishes; F can grow freely. Consistent with Euler blowup. PASS (ν-essential).
  - Elgindi C^{1,α} Euler: same, ν = 0. PASS.
  - **Chae 2007 geometric depletion**: A5 explicitly acknowledges overlap with Chae's ∇(ω/|ω|) estimates. Claim that A5 is distinct: Chae uses the direction ∇ξ; A5 uses the magnitude ∇log|ω|² = 2∇|ω|/|ω|. Logically distinct. Whether Chae's failure extends to A5 is **exactly the open question**.
  - Shell: UNTESTABLE.
  - Tao averaged NSE: A5 correctly notes Fisher involves log, a nonlinear transform; not a Fourier norm; averaging-breaking. UNTESTABLE on averaged NSE → PASS-by-non-applicability.
- Part B:
  - Step 1: F(t).
  - Step 2: F ~ ν⁻¹ · ‖∇ω‖², hence supercritical (‖∇ω‖² scales as λ⁷, ν⁻¹ scales as λ⁻², so F scales as λ⁵). a = −5/2.
  - Step 3: NO, per A5's argument (log is not Fourier-local).
  - Step 4: NOT-BLOCKED.
- Overall: sub-problem target. The question is whether dF/dt is bounded by F linearly or sub-linearly (A5's failure-mode 1: cubic bound would give finite-time blowup of F itself). Specific test: compute dF/dt on the Hou–Luo near-singular profile and see whether the nonlinear term dominates the dissipation term. Rank: MEDIUM.

### C.4 — Cross-proposal collisions and complementarities

**Collision 1**: M1.4's Φ = ∫|ω|² χ(ξ·e_max(S)) dx and G2's Φ_ν = ∫(|ω|² + λν|∇u|²) e^{−φ} dx are both Perelman-analogue candidates. Both confess the Burgers-vortex threat. Verdict: **consistent** in confessing the Burgers obstruction; neither fully resolves it. **Joint test**: compute each candidate on the same Burgers-vortex profile and on the Hou–Lei axisymmetric-with-swirl conjectural profile.

**Collision 2**: M1.3 (Lipschitz-ξ) and G1 (self-consistent κ) both use the Constantin–Fefferman vorticity-direction input. Verdict: **complementary**. M1.3 is a small-data Picard-ball enlargement. G1 is a self-consistency feedback for κ on the candidate blowup. Joint route: **first** prove G1's Osgood feedback (sub-linear closure of κ) for axisymmetric-with-swirl; **then** use M1.3 to extract a larger critical-Picard ball in that class. Candidate joint sub-problem for an 8th mathematician.

**Collision 3**: A4 (Lean-driven search) and both M1.4 and G2. A4's search procedure would run the Perelman-analogue search *automatically* over the polynomial space that includes M1.4 and G2 as specific candidates. Verdict: **A4 subsumes M1.4 and G2 as search-targets**. Proposed execution: code A4's degree-4 enumeration, verify that M1.4's alignment-χ candidate and G2's weighted-(|ω|² + λν|∇u|²) candidate are both in the search space, and see if Positivstellensatz verifies or refutes each.

**Collision 4**: M1.5 (Besov-ESS) and the Cheskidov–Luo sharp non-uniqueness (2022 Inventiones). The proposal's own failure-mode 3 flags this; it is the weak link.

**Complementarity 5**: G4 (Type-II self-similar no-swirl) and G5 (Elgindi viscous damping). Both target axisymmetric sub-problems; together they would give a dual picture of NSE's axisymmetric regime — ruling out ancient profiles (G4) on the NSE side, measuring viscous damping of Euler profiles (G5) on the Euler-limit side. Joint deliverable: a unified "axisymmetric NSE damps axisymmetric Euler singularities" theorem.

### C.5 — Ranked shortlist (top proposals by survival × barrier-escape × testability)

Top 3 proposals that (a) survive Part A on at least 10 of 12 testable reduced cases, (b) are NOT-BLOCKED at Part B, (c) have a concrete falsifying test an 8th mathematician could attempt in 1–3 months:

1. **A4 (mechanized monotone-quantity search)**. Survives: all cases vacuously (is a procedure, not an attack). Not blocked. Concrete test: code degree-4 enumeration in Lean 4 + Positivstellensatz over SDP, run on NSE with Leray-projected transport; output either Φ-candidate or obstruction. 2–3 year project, but 3-month "minimum viable enumeration" can give first results. Recommended as **flagship**.

2. **G1 narrowed to axisymmetric-with-swirl (Lipschitz-ξ self-consistency)**. Survives all 2D/shell/averaged-NSE/Chen–Hou/Elgindi tests on ν-essentiality grounds. Not blocked (B.6 worked example). Concrete test: on axisymmetric-with-swirl NSE, compute the Osgood feedback on κ = ‖∇ξ‖_{L^∞} and check whether p < 1 (sub-linear) or p = 1 (linear) — 1–3 month focused PDE calculation. Recommended as **narrow moonshot with concrete falsifier**.

3. **G4 (Type-II self-similar no-swirl exclusion)**. Survives all tests (axisymmetric no-swirl NSE is globally smooth anyway, so the exclusion is consistency-level; the technical content is excluding Type-II ancient profiles). Not blocked. Concrete test: extend Koch–Nadirashvili–Seregin–Šverák's Liouville from bounded to Type-II self-similar class, in the no-swirl axisymmetric setting. Publishable increment on SP2. Recommended as **highest-probability publishable output**.

Honorable mention: **M1.2 (double-exponential Tao quantitative bound)** — not on top-3 because it is purely incremental and does not escape the barrier as a path to Clay, but it is the second-highest publishability estimate after G4.

### C.6 — Proposals that should be **deprioritised**

- **M1.6 (helicity-modified Koch–Tataru)**: proposal's own confession of likely barrier-blockage via a modified Tao averaging.
- **G6 (obstruction-class cohomology)**: triviality by Kuiper or collapse to known analytic estimate; >40 years of no serious engagement in the literature is a strong prior.
- **A2 (regularity-structures reclassification)**: proposal's own concession of averaging-invariance.
- **A3 unforced-Clay version**: proposal's own f → 0 vacuity. Only the forced-statistical sub-problem is worth pursuing.

### C.7 — Open pre-check items to resolve before serious investment

These are fast calculations that can flip a proposal from UNVERIFIED to VERIFIED or KILLED:

1. **M1.1**: run the Katz–Pavlović shell with log-corrected dissipation g(λ_n) = λ_n^{2c/log(2+λ_n)}. Does the shell still blow up? (If yes: M1.1's PDE program is impossible.)
2. **M1.5**: check whether Cheskidov–Luo 2022's construction can be lifted to Ḃ^{−1+3/p}_{p,∞} for p > 3. (If yes: Besov-ESS fails in that range.)
3. **M1.6**: attempt a helicity-preserving Tao construction with blowup. (If succeeds: M1.6 is BLOCKED confirmed.)
4. **M1.4, G2**: evaluate each candidate Φ on the Burgers vortex profile. (If not monotone: unconditional version fails; only conditional remains.)
5. **G2 scaling**: redo the scaling computation of Φ_ν; confirm whether it is super- or sub-critical. (As written, it looks subcritical, which collapses the Perelman-analogue claim.)
6. **A1**: compute 𝒜_ε on a scaled self-similar Leray ansatz; check for reduction to ν∫|∇u|². (If reduces: A1 is repackaged dissipation.)
7. **A5**: compute dF/dt's dominant nonlinear term on Hou–Luo-like profile; identify whether γ < 1 (A5 closes), γ = 1 (linear), γ > 1 (blowup of F).

Each is a 1–4 week single-researcher task. Results will narrow the 17 audited proposals (M1.1–M1.6, G1–G6, A1–A5) to a shortlist for serious investment.

---

## Appendix — Key citations (arXiv preferred)

- Tao 2014 averaged NSE: arXiv:1402.0290 (JAMS 2016).
- Tao 2019 quantitative ESS: arXiv:1908.04958.
- Katz–Pavlović shell: arXiv:math/0211073 (Trans. AMS 2005).
- Cheskidov dyadic: arXiv:math/0502227 (Trans. AMS 2008).
- Chen–Hou axisymmetric Euler: PNAS 2025.
- Elgindi C^{1,α} Euler: arXiv:1904.04795 (Ann. Math. 2021).
- Buckmaster–Vicol NSE non-uniqueness: arXiv:1709.10033 (Ann. Math. 2019).
- Albritton–Brué–Colombo forced Leray–Hopf non-uniqueness: Ann. Math. 196 (2022), 415–455.
- Cheskidov–Luo sharp non-uniqueness: Inventiones 229 (2022), 987–1054.
- Barker–Prange survey: arXiv:2211.16215.
- Constantin–Fefferman geometric depletion: Indiana Univ. Math. J. 42 (1993), 775–789.
- Chen–Hou–Huang De Gregorio: arXiv:1905.06387.
- Escauriaza–Seregin–Šverák L^∞_t L³_x: Acta Math. 189 (2003), 45–80.
- Beale–Kato–Majda: CMP 94 (1984), 61–66.
- Ladyzhenskaya 2D: Russian Math. Surveys 14 (1959); Comm. Pure Appl. Math. 13 (1960).
