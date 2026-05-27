# Mathematician 2 — Geometric / Dynamical Attacks on 3D Navier–Stokes Global Regularity

**Portfolio**: vorticity geometry, Riemannian geometry on SDiff(Ω), Perelman-style monotonicity, self-similar (Type-II) blowup, flow-with-surgery, obstruction classes.
**Inputs**: `ns_scout.md` (scout reconnaissance, iter 4) and `knowledge_graph.json`.
**Rule of engagement carried from iter 3**: honesty over novelty claims; Tao's supercritical barrier (arXiv:1402.0290) is the mandatory checkpoint for every proposal.

Six proposals below (G3 subdivided into paired (a)/(b) variants). Each entry: Target, Core idea, Graph techniques, Derivation sketch, Supercritical-barrier check, External inputs, Failure modes, Honest grade.

Grade legend: **TOY-SUB-PROBLEM** (genuinely reducible; modest publishable result likely); **INCREMENTAL-OVER-KNOWN** (sharpens an existing theorem, not a regularity proof); **MOONSHOT** (would be decisive if it worked; probability of closure small); **BLOCKED-BY-BARRIER** (ruled out on its face by Tao's averaging argument or an equivalent structural obstruction).

---

## Proposal G1 — Forced Lipschitz-direction self-consistency for ω/|ω|

### Target
Upgrade the Constantin–Fefferman 1993 geometric depletion criterion from *conditional* ("*if* ξ = ω/|ω| is Lipschitz on the high-vorticity region, no blowup by BKM") to *automatic* ("ξ is necessarily Lipschitz on any candidate first blowup time") — at least for a structurally restricted class of candidate singularities.

### Core idea
Constantin–Fefferman: |α(x,t)| = |⟨ξ·∇u·ξ⟩| ≤ C·M(t)·κ(x,t), with M(t) a velocity bound and κ a weighted Lipschitz seminorm of ξ = ω/|ω| on the high-vorticity region. If κ ∈ L¹_t L^∞_x near a candidate blowup, BKM forbids blowup.

Close a self-consistency loop. Via Biot–Savart u = K★ω, write ∇ξ as a singular integral in ω. Set up a Picard-style equation for κ(t) with viscous smoothing (schematic: ξ is unit-length, so use the ω-equation and project onto ξ^⊥). Target an inequality

&nbsp;&nbsp;&nbsp;&nbsp;κ(t) ≤ Cν · ∫₀ᵗ κ(s)^{p} ds   with p < 1,

so Osgood closes and κ stays finite. The hope: the 0/0 cancellation in ξ = K★ω / |K★ω| (ξ divides by |ω|, small exactly where ω vanishes) yields sublinear feedback p < 1.

### Graph techniques
- `t_conserved_quantity` (the target is a Bootstrapped quantity that is *not* conserved but, conjecturally, monotone-controlled)
- `t_auxiliary_construction` (Constantin–Fefferman α-scalar, viscous regularisation of the direction field)
- `t_symmetry_reduction` (on the high-vorticity region, use vorticity axis as a preferred frame)
- `t_exhaustion_squeeze` (Picard-style fixed point in κ)
- `t_reductio_ad_absurdum` (suppose κ blows up, derive a contradiction)

### Derivation sketch
1. From the vorticity equation ∂ₜω + (u·∇)ω = (ω·∇)u + νΔω, project onto the unit-length constraint to obtain

&nbsp;&nbsp;&nbsp;&nbsp;∂ₜξ + (u·∇)ξ = P_ξ⊥(∇u · ξ) + ν|ω|⁻¹ P_ξ⊥(Δω),

&nbsp;&nbsp;where P_ξ⊥ is orthogonal projection onto the tangent space of S² at ξ.
2. Apply ∇ to obtain an equation for ∇ξ whose right-hand side contains (i) the matrix ∇u evaluated via Biot–Savart on ω, (ii) a viscous term that is *formally dissipative* but singular as |ω| → 0 (harmless because the singular points are low-vorticity), and (iii) transport terms that satisfy energy-type bounds.
3. Localise to Ω_M = {|ω| ≥ M} with M a threshold growing with t. On Ω_M, singular-integral estimates for ∇(K★ω) in terms of ω on Ω_M itself plus lower-order contributions from Ω_M^c can be closed because ‖ω‖_{L²} is globally bounded by enstrophy.
4. If the combined feedback on κ(t) = ‖∇ξ‖_{L^∞(Ω_M(t))} is strictly sub-linear, Osgood closure forbids finite-time blowup of κ.

### Supercritical-barrier check
Strongest point. The Lipschitz seminorm of ξ is not preserved by Tao's averaging: averaging replaces the specific Biot–Savart symbol k_i k_j/|k|² with generic |c(k,k₁,k₂)| ≤ 1, destroying the stretching-vs-rotation angle decomposition. Averaged NSE has no ξ-direction field controlling anything. **Escapes the barrier.**

### External inputs
- Constantin, *Geometric statistics in turbulence*, SIAM Rev. **36** (1994) 73–98.
- Constantin & Fefferman, *Direction of vorticity and the problem of global regularity for the Navier–Stokes equations*, Indiana Univ. Math. J. **42** (1993) 775–789.
- Beirão da Veiga & Berselli, *On the regularizing effect of the vorticity direction*, Diff. Integral Eqns **15** (2002) 345–356.
- Chae, various 2003–2007 papers on direction-of-vorticity criteria.
- Grujić & Ruzmaikina, *Interpolation between algebraic and geometric conditions for smoothness of the vorticity*, Indiana Univ. Math. J. **53** (2004).

### Failure modes
- Feedback inequality is linear (p = 1): Grönwall gives only exponential growth, no blowup exclusion.
- Localised viscous term ν|ω|⁻¹ P_ξ⊥(Δω) is supercritical in 3D, fails to dominate stretching — exactly the Clay difficulty.
- Constantin's Biot–Savart cancellation is fragile: pointwise a.e. but breaks under L^p integration for generic p.
- At genuine singularities |ω| → ∞ and ξ become simultaneously discontinuous; decoupling "|ω| big" from "ξ smooth" is a hope, not a theorem.

### Honest grade
**MOONSHOT** as full Clay. **TOY-SUB-PROBLEM** if narrowed to: "axisymmetric NSE with swirl — Lipschitz seminorm of ξ satisfies sub-linear Osgood feedback." Swirl/meridional decouple with known coupling; partial result extends Chae's direction-of-vorticity criteria without claiming Clay.

---

## Proposal G2 — Perelman-analogue functional for NSE: a ν-weighted W-entropy candidate

### Target
Construct a functional Φ(u, t) that is (i) defined on smooth divergence-free u, (ii) supercritical with respect to the NS scaling u_λ(t,x) = λu(λ²t, λx) (so not already controlled by Leray energy or Ḣ^{1/2}), and (iii) monotone non-increasing along the NSE flow, possibly up to an explicit correction that is itself scaling-subcritical. If such Φ exists and bounds a critical norm, it breaks the Clay barrier.

### Core idea
Perelman's W(g, f, τ) = ∫[τ(R + |∇f|²) + f − n]·(4πτ)^{−n/2} e^{−f} dV is monotone along Ricci flow when f, τ evolve by dual backward heat. Structural ingredients: (i) gradient-flow derivation from λ-entropy, (ii) reference weight e^{−f}dV, (iii) cancellation between reaction R and Laplacian-of-weight (Bakry–Émery Ricci).

NSE analogues: (i) not a gradient flow in energy, but vorticity has quasi-gradient structure under a weight; (ii) Gaussian weight e^{−|u|²/(2σ²)} or a Perelman-style e^{−|x|²/(4ν(T−t))}; (iii) vortex-stretching (ω·∇)u·ω = α|ω|² ↔ R; viscous ν|∇ω|² ↔ Laplacian-of-weight.

Ansatz:

&nbsp;&nbsp;&nbsp;&nbsp;Φ_ν(u, t) = ∫(|ω|² + λν|∇u|²)·e^{−φ(x,t)} dx,

φ co-evolving so that the Leray pressure contribution to dΦ_ν/dt cancels part of stretching. Target:

&nbsp;&nbsp;&nbsp;&nbsp;dΦ_ν/dt ≤ −ν·(coercive) + ν·Σ(t),  Σ ∈ L¹(0, ∞) subcritical.

If Φ_ν controls a critical norm, regularity follows.

### Graph techniques
- `t_conserved_quantity` (target a *monotone* quantity, a generalisation)
- `t_ricci_flow_with_surgery` (template: Perelman's entropy construction; see knowledge_graph.json lines 2640–2655, marked as the canonical instantiation of t_flow_with_surgery with Perelman entropy package)
- `t_duality` (Leray projection; dual weight via Legendre transform of kinetic energy)
- `t_analysis_algebra_topology_bridge` (Ricci-to-NSE analogy)
- `t_rescale_for_asymptotic_geometry` (scaling-supercritical property is the differentiator)

### Derivation sketch
1. Compute d/dt of candidate Φ_ν using the NSE equations and the transport equation for the weight e^{−φ}. Any time-derivative of a spatial integrand involving u and ω produces: viscous term (−ν|∇·|² coercive), pressure term (integrate by parts using ∇·u = 0; this is where the Leray projection helps), vortex-stretching term (indefinite in sign).
2. Choose φ(x, t) to satisfy a backward-in-time transport equation coupled to u: ∂ₜφ + u·∇φ − ν|∇φ|² + ν Δφ = Ψ(u, ω), for some functional Ψ of the current velocity field. This is the NSE analogue of Perelman's backward heat equation for the conjugate heat kernel.
3. The combined quantity Φ_ν(u(t), t) then satisfies a closed differential inequality. The hope: because of the Leray-projection orthogonality, pressure drops out, and because of the specific sign of ν, the stretching term can be partially absorbed.
4. Show that Φ_ν controls a critical or sub-critical norm (e.g. Ḣ^{1/2} or L³) — this is the link that would close global regularity.

### Supercritical-barrier check
Under u_λ(t,x) = λu(λ²t, λx) with Perelman-Gaussian φ(x,t) = |x|²/(4ν(T−t)) (dimensionless), Φ_ν scales as λ⁵ — supercritical, positive power. Right sign: quantity grows under zoom-in, so forward-in-time monotonicity forbids zoom-in-type blowup. **If monotonicity closes, escapes the barrier.** F_avg has no analogue of the Leray-projection dual weight or of the pressure–stretching cancellation.

### External inputs
- Perelman, *The entropy formula for the Ricci flow and its geometric applications*, arXiv:math/0211159 (2002).
- Müller, *Monotone volume formulas for geometric flows*, J. Reine Angew. Math. **643** (2010) 39–57.
- Ni, *The entropy formula for linear heat equation*, J. Geom. Anal. **14** (2004).
- Foias, Manley, Rosa, Temam, *Navier–Stokes Equations and Turbulence*, Cambridge 2001 — for statistical-solution functionals that formally resemble an entropy.
- Constantin, Foias, *Navier–Stokes Equations*, Chicago Lectures 1988.

### Failure modes
- Pressure term does not drop out for any choice of φ: Leray non-locality breaks translation invariance in exactly the way that blocks IBP.
- Even with monotonicity, Φ_ν may control only weighted-L² of vorticity — supercritical, gives nothing new over enstrophy.
- Core structural gap: Ricci flow is a gradient flow of Perelman's λ (up to diffeomorphism). NSE is not a gradient flow of any known Lyapunov functional.
- Historical evidence: Doering, Gibbon, Constantin, Titi have searched extensively; known NSE Lyapunov functionals (energy, helicity, enstrophy) are all critical or subcritical, never supercritical-yet-monotone.

### Honest grade
**MOONSHOT**. Highest-value axis if it works; scout §5 Axis 11 "named moonshot". Full solution: very low. Partial monotone quantity on a sub-class: moderate. Publishable intermediate framing: "construct Φ_ν monotone along NSE for Beltrami-type initial data".

---

## Proposal G3 — Arnold–Khesin SDiff curvature as geometric obstruction

### Target
Exploit Arnold's realisation of Euler (and, with viscous friction, NSE) as a geodesic-flow-with-damping on SDiff(Ω), and use the *sign* of the sectional curvature of SDiff to produce either (a) an enstrophy-like monotone quantity from curvature geometry, or (b) an obstruction to Lyapunov-type growth of the Jacobi field that would otherwise drive blowup.

### Core idea
Arnold (1966): Euler on compact Riemannian Ω is geodesic flow on G = SDiff(Ω) with right-invariant L² metric. NSE is geodesic-with-viscous-correction. Sectional curvature K_σ of SDiff has mixed sign, generically negative on "turbulent" 2-planes (Misiolek, Khesin–Wendt) — the geometric origin of Lagrangian instability.

**G3(a)** — Positive-curvature monotonicity. On positive-K_σ sections (Killing fields, Beltrami modes), Jacobi fields cannot grow super-exponentially. Decompose NSE energy into positive-curvature components + dissipatively-controlled remainder; Jacobi growth (infinitesimal vortex stretching) is bounded.

**G3(b)** — Ricci as obstruction. Compute Ricci of SDiff restricted to the attractor. Bochner formula

&nbsp;&nbsp;&nbsp;&nbsp;½ Δ|Y|² = |∇Y|² + ⟨Ric(Y), Y⟩ + ⟨Y, ΔY⟩

for Jacobi Y along the NSE geodesic. If Ric ≥ −Λ with Λ viscosity-controlled, |Y|² grows at most exponentially; associated enstrophy cannot blow up finitely.

### Graph techniques
- `t_analysis_algebra_topology_bridge` (Arnold bridge: NSE ↔ Riemannian geometry on SDiff)
- `t_structural_isomorphism` (NSE-as-geodesic-flow)
- `t_symmetry_reduction` (exploit the right-invariance of the L² metric)
- `t_conserved_quantity` (curvature-bounded Jacobi energy)
- `t_auxiliary_construction` (extended Bochner formula on infinite-dim Lie group)

### Derivation sketch
1. NSE on 𝕋³ or ℝ³ as ∂ₜu + ∇_u u = −ν ∇_u⊥ u (schematic; ∇_u u covariant derivative on SDiff with L² metric, νΔu gradient-type correction).
2. Jacobi equation along NSE trajectory: D²Y/Dt² + R(Y, ∂_t φ_t)∂_t φ_t = (viscous terms). In Eulerian variables: perturbed ω-transport with curvature correction.
3. Bochner on SDiff: ‖Y(t)‖² ≤ ‖Y(0)‖² · exp(2∫₀ᵗ max(0, −κ(s)) ds), κ(s) minimal sectional curvature along the geodesic. If ∫max(0, −κ) bounded by viscosity (via Khesin–Wendt curvature-vorticity formulas), Jacobi growth controlled → vortex stretching controlled.
4. Bridge: right-translated L²-norm of Y ↔ perturbative enstrophy. Boundedness of perturbative enstrophy near every trajectory is substantial progress toward regularity.

### Supercritical-barrier check
SDiff curvature is geometric, not a scaling-invariant functional norm. It depends on the commutator [u, v], which in Fourier is triadic symmetric — averaging destroys the Jacobi identity [[u,v],w]+cyc = 0 that makes curvature a tensor. **Escapes the barrier** heuristically. F_avg does not correspond to a geodesic flow on any Lie group.

### External inputs
- Arnold, *Sur la géométrie différentielle des groupes de Lie de dimension infinie et ses applications à l'hydrodynamique des fluides parfaits*, Ann. Inst. Fourier **16** (1966) 319–361.
- Arnold & Khesin, *Topological Methods in Hydrodynamics*, Springer 1998, 2nd ed. 2021. Chapters II, IV, VI.
- Ebin & Marsden, *Groups of diffeomorphisms and the motion of an incompressible fluid*, Ann. Math. **92** (1970) 102–163.
- Misiolek, *Conjugate points in the Bott–Virasoro group and the KdV equation*, Proc. AMS **125** (1997); and works of Khesin–Wendt on curvature of SDiff.
- Shkoller, *Geometry and curvature of diffeomorphism groups with H¹ metric and mean hydrodynamics*, J. Funct. Anal. **160** (1998) 337–365.

### Failure modes
- SDiff has both curvature signs; negative sections dominate for turbulent directions, so Bochner gives exponential Jacobi growth, not a regularity theorem — the geometric origin of chaos, already in Arnold's original.
- Infinite-dim Bochner is formal; rigorous Ricci on SDiff needs regularisation and may not converge.
- 60-year negative empirical prior: Arnold's framework has not produced a single 3D NSE regularity theorem.
- νΔu is not a gradient flow on (SDiff, L²). Making it gradient requires switching to L² on symmetric operators, breaking the geodesic interpretation.

### Honest grade
**MOONSHOT** for the full claim; **INCREMENTAL-OVER-KNOWN** for G3(b) restricted to near-Beltrami data, where SDiff curvature is explicit and Bochner gives a conditional enstrophy bound. Narrow result publishable as an extension of Shkoller / Khesin–Wendt.

---

## Proposal G4 — Type-II self-similar blowup ruling-out via Jia–Šverák rigidity

### Target
Sharpen the Nečas–Růžička–Šverák 1996 exclusion of Type-I self-similar blowup to a meaningful partial exclusion of Type-II self-similar blowup for 3D NSE. Specifically: rule out Type-II discretely-self-similar blowup for axisymmetric solutions without swirl. This is SP2 in the scout's roadmap.

### Core idea
Type-I: ‖u(t)‖_∞ ≤ C/√(T−t). NRS 1996 ruled out via ancient Liouville rigidity. Type-II: slower, e.g. (T−t)^{−α}, α < 1/2 (possibly log corrections). Profile equation in ξ = x/√(T−t), τ = −log(T−t):

&nbsp;&nbsp;&nbsp;&nbsp;∂_τ U − ½U − ½ξ·∇U + (U·∇)U = −∇P + νΔU,  ∇·U = 0.

For Type-I, stationary U(ξ) are classified (NRS + Tsai 1998). Type-II allows slowly-growing U(τ); Jia–Šverák (2014) developed the relevant discretely-self-similar machinery (for forced NSE).

Attack: combine Jia–Šverák + Chae Liouville + Koch–Nadirashvili–Seregin–Šverák 2009 (ancient axisymmetric Liouville) to show axisymmetric-no-swirl NSE admits no non-trivial Type-II profile. Closes SP2 (at least no-swirl).

### Graph techniques
- `t_rescale_for_asymptotic_geometry` (canonical self-similar blowup analysis; NRS, CKN, ESS all use this)
- `t_infinite_descent` (rescaling around the candidate singularity gives a smaller-scale problem of the same type)
- `t_verify_on_special_cases` (axisymmetric, no-swirl is the "special case" where the Biot–Savart kernel simplifies)
- `t_symmetry_reduction` (axisymmetric SO(2) reduction to (r, z)-plane equations)
- `t_reductio_ad_absurdum` (assume Type-II profile; derive rigidity contradiction)

### Derivation sketch
1. Assume axisymmetric-no-swirl NSE blowup at (x★, T★) with Type-II rate (T−t)^{−α}, 0 < α < 1/2. Rescale with λ(t) = (T−t)^α.
2. Weak-* limit U(τ, ξ) along τ → ∞ solves modified profile equation with drift αξ·∇U + αU (replacing ½ from Type-I). U is ancient in τ, bounded in L^∞_τ L^p_ξ.
3. In axisymmetric no-swirl, ω^θ/r is transported (Hou–Li, Chen–Strain–Tsai–Yau) and a-priori bounded from smooth data. Injects into profile: U has bounded ω^θ/r.
4. Koch–Nadirashvili–Seregin–Šverák Liouville: ancient bounded axisymmetric-no-swirl NS with bounded ω^θ/r is trivial. So U ≡ 0, contradiction.

### Supercritical-barrier check
Profile analysis is geometric-asymptotic, not functional-norm-based. Pointwise bound on ω^θ/r is supercritical — Chen–Strain–Tsai–Yau 2008 use it precisely because it breaks scaling. F_avg does not commute with SO(2)-rotation about z (generic c(k,k₁,k₂) destroys the symmetry), so averaged NSE has no axisymmetric sector. **Escapes the barrier** in the axisymmetric sector.

### External inputs
- Nečas, Růžička, Šverák, *On Leray's self-similar solutions of the Navier–Stokes equations*, Acta Math. **176** (1996) 283–294.
- Tsai, *On Leray's self-similar solutions of the Navier–Stokes equations satisfying local energy estimates*, Arch. Ration. Mech. Anal. **143** (1998) 29–51.
- Jia & Šverák, *Local-in-space estimates near initial time for weak solutions of the Navier–Stokes equations and forward self-similar solutions*, Invent. Math. **196** (2014) 233–265.
- Koch, Nadirashvili, Seregin, Šverák, *Liouville theorems for the Navier–Stokes equations and applications*, Acta Math. **203** (2009) 83–105.
- Chen, Strain, Tsai, Yau, *Lower bounds on the blow-up rate of the axisymmetric Navier–Stokes equations II*, CPDE **34** (2009).
- Chae, *Nonexistence of asymptotically self-similar singularities in the Euler and the Navier–Stokes equations*, Math. Ann. **338** (2007) 435–449.

### Failure modes
- With swirl, ω^θ/r is no longer transported and KNSŠ Liouville does not apply. No-swirl tractable; full axisymmetric is the next wall.
- Discretely-self-similar profiles require parabolic Liouville on ℝ × (ξ-space), known only under smallness/positivity.
- Time-varying α (non-self-similar blowup): no limit profile, method silent.
- Axis advances incrementally; no reason to expect a single-paper Clay jump.

### Honest grade
**TOY-SUB-PROBLEM**, a good one. Publishable advance on SP2; active frontier (Jia–Šverák, Chae, Chen–Strain–Tsai–Yau); graph techniques feed in directly. Not Clay; reach limited by axisymmetric reduction.

---

## Proposal G5 — Quantitative viscous damping against the Elgindi profile

### Target
Take Elgindi's 2021 C^{1,α} finite-time singularity for axisymmetric Euler (no swirl) and quantitatively measure viscous damping against the Elgindi profile. The target is either (a) an explicit lower bound α_crit(ν) such that no Elgindi-type profile persists for α below α_crit(ν), giving a viscosity-regularised no-go, or (b) a conditional "NSE blows up in the Elgindi regime" statement that would push toward Clay-(B).

### Core idea
Elgindi (Ann. Math. 194, 2021): 3D Euler axisymmetric no-swirl with C^{1,α}, α small, blows up in finite time. Fundamental-model reduction makes Biot–Savart explicit; self-similar profile with algebraic rate driven by non-smoothness. Chen–Hou (PNAS 2025): C^∞ axisymmetric Euler blowup in bounded cylinder, computer-assisted.

NSE with ν > 0: Elgindi's profile is not blowup — viscosity damps the cascade. Quantify: plant U_Elg into NSE, compute perturbation growth. L_Elg = Euler linearisation (explicit from Elgindi), D_ν = νΔ. Spectral question: does L_Elg + D_ν have unstable eigenvalue λ(ν) > 0 for all ν > 0, or does ν★(α) exist with Re λ ≤ 0 above it?

If the latter: NSE blowup in Elgindi regime requires ν < ν★(α). Combined with α ≥ α_min(ν) for smoother data, Elgindi mechanism is ruled out for all ν above absolute threshold — structural "NSE damps Euler" theorem.

### Graph techniques
- `t_verify_on_special_cases` (axisymmetric no-swirl; C^{1,α} regime; Elgindi's explicit profile)
- `t_symmetry_reduction` (axisymmetric reduction, same as G4)
- `t_rescale_for_asymptotic_geometry` (self-similar Elgindi profile analysis)
- `t_auxiliary_construction` (explicit Biot–Savart-in-fundamental-model reduction, Elgindi's technical device)
- `t_exhaustion_squeeze` (spectral bootstrap)

### Derivation sketch
1. Import Elgindi's fundamental-model reduction: axisymmetric-no-swirl Euler near blowup is a 1D integro-differential equation along a radial slice.
2. Add νΔ → 1D Schrödinger-type operator with explicit symbol. Compute its spectrum against the Elgindi linearisation.
3. Elgindi's linearisation has one unstable direction (self-similar scaling). Question: does ν · (1D Laplacian) overcome this eigenvalue?
4. Re λ_Elg(ν) ≤ 0 ⟹ no NSE blowup near U_Elg (semigroup bounds). Re λ_Elg(ν) > 0 ⟹ Hadamard-type instability near U_Elg — not a blowup proof but a candidate mechanism for Clay-(B).

### Supercritical-barrier check
Elgindi profile is C^{1,α}, not smooth. Tao's averaging is at C^∞ level; does not accommodate C^{1,α} naturally. Fundamental-model reduction exploits the specific Biot–Savart kernel (Calderón-like 1D operator), averaging-destroyed. **Escapes the barrier** in C^{1,α} regime. Caveat: Clay requires C^∞ data; C^{1,α} success does not directly give Clay, but a quantitative ν★(α) with α → 0 asymptotics informs where C^∞ data could develop singularities.

### External inputs
- Elgindi, *Finite-time singularity formation for C^{1,α} solutions to the incompressible Euler equations on ℝ³*, Ann. Math. **194** (2021) 647–727.
- Elgindi–Jeong, *Finite-time singularity formation for strong solutions to the axisymmetric 3D Euler equations*, Ann. PDE **5** (2019).
- Chen, Hou, *Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler equations with smooth data*, arXiv:2210.07191 and PNAS version (2025).
- Luo, Hou, *Toward the finite-time blowup of the 3D axisymmetric Euler equations: a numerical investigation*, MMS **12** (2014).
- Cordoba, Cordoba, Fontelos, *Formation of singularities for a transport equation with nonlocal velocity*, Ann. Math. **162** (2005) — model context for Elgindi-type profiles.

### Failure modes
- Spectral analysis may not close: eigenvalue may have non-trivial ν-dependence without sign flip; neither conclusion forced.
- Fundamental-model reduction is on a 1D slice; full 3D NSE viscosity couples radial/axial modes beyond what the reduction captures.
- Elgindi exploits C^{1,α} non-smoothness essentially (algebraic structure of Biot–Savart at the singular point). For C^∞ data this structure vanishes; Elgindi mechanism does not operate. C^{1,α}-only does not bear on Clay.

### Honest grade
**TOY-SUB-PROBLEM / INCREMENTAL-OVER-KNOWN**. Quantitative ν★(α) is a natural next step post Elgindi 2021 + Chen–Hou 2025; publishable. Does not touch Clay (smoothness gap); honest SP6 advance.

---

## Proposal G6 — Obstruction-class formulation (speculative)

### Target
Interpret "NSE develops a finite-time singularity from smooth data" as the non-vanishing of a cohomology class [blowup] in some bundle over the space of divergence-free Schwartz fields. A non-vanishing class would imply singularity genericity; a vanishing class would imply genericity of regularity. The Clay problem is then translated into a characteristic-class computation.

### Core idea
M = {u₀ ∈ H^s_{div}(ℝ³) : ‖u₀‖ ≤ R, s large}. E → M, fibre over u₀ is [0, T_max(u₀)). Singular set S = {u₀ : T_max < ∞} is conjecturally empty (Clay-(A)) or generic (Clay-(B)).

If S is non-empty open, define first-singularity map σ : S → M_sing; try to identify obstruction in sheaf cohomology of M with coefficients in a lifespan-data sheaf 𝒞 whose non-vanishing ↔ S ≠ ∅.

Concretely, a complex 𝒜⁰ → 𝒜¹ → … where 𝒜^i consists of cocycle functionals on i-parameter families of initial data tied to NSE evolution. Blowup class [σ] ∈ H^k(M; 𝒞):
- H^k(M; 𝒞) = 0 topologically ⟹ Clay-(A).
- [σ] ≠ 0 detected ⟹ Clay-(B).

### Graph techniques
- `t_obstruction_class` (the core technique; knowledge_graph.json line 2261)
- `t_sheafify_on_grothendieck_topology` (sheafify the local-in-time mild-solution presheaf; knowledge_graph.json line 2541)
- `t_deformation_cohomology` (deform ν → 0 or hyperdissipation → Laplacian; blowup as jump in deformation class; line 2285)
- `t_analysis_algebra_topology_bridge` (the bridge between NSE analysis and characteristic classes)
- `t_auxiliary_construction` (the bundle E, the sheaf 𝒞)

### Derivation sketch
1. T_max : M → (0, ∞] is lower semi-continuous (Leray); S = T_max^{-1}([0, ∞)) is Borel.
2. On M \ S, define evaluation bundle ℰ(u₀, t) = u(t); ∂S captures "singular boundary data".
3. Mayer–Vietoris spectral sequence over a Picard-neighbourhood cover of M. E_2 page carries the gluing obstruction — a bona fide cohomology class.
4. Key: is this class characteristic (topological) or analytic? Topological ⟹ likely zero (Hilbert ball contractible). Analytic ⟹ new invariant, must be computed.

### Supercritical-barrier check
Achilles' heel. Characteristic classes on infinite-dim manifolds are generically trivial (Kuiper: U(H) contractible). M Hilbert-ball has trivial topology. Non-trivial [σ] must be analytic not topological. But if the class is defined generically for bilinear maps B with critical scaling, it detects F_avg-blowup as much as F_true-blowup — thus *incorrectly* predicting true-NSE blowup. **Likely BLOCKED-BY-BARRIER** unless the class depends on specific Leray structure (vortex stretching, pressure non-locality), in which case the construction is no longer topological but a disguised analytic estimate.

### External inputs
- Atiyah, Hirzebruch, *Characteristic classes of fibre bundles*; standard references.
- Kuiper, *The homotopy type of the unitary group of Hilbert space*, Topology **3** (1965) 19–30 — the contractibility result that trivialises naive topological approaches.
- Elworthy, Tromba, *Degree theory on Banach manifolds*, Proc. Symp. Pure Math. **18** (1970) — for infinite-dimensional degree-theoretic obstruction.
- Joyce, *Algebraic geometry over C^∞-rings*, arXiv:1001.0023 — speculative analog for a sheaf-theoretic PDE framework.
- Tao, Blog posts on "hidden structure in the Navier–Stokes equations" — conceptual background for why topological invariants alone do not solve analytic problems.

### Failure modes
- Class is trivial by Kuiper; no information.
- Class is equivalent to known analytic estimate (Serrin, BKM, ESS); topological language adds nothing.
- Sheaf cohomology of the mild-solution presheaf is uncomputable — sheafification over Hilbert-ball base is pathological.
- Averaging-invariance: algebraic properties of B may be the ones preserved; class fails the barrier check.
- 40-year negative empirical prior: no serious NSE program in this direction.

### Honest grade
**MOONSHOT with high probability of being BLOCKED-BY-BARRIER on inspection.** Included per the portfolio brief's "very speculative" instruction. Lowest priority of the six. Serious engagement requires first establishing — via a toy PDE (dyadic shell model) — that a non-trivial obstruction class can even be defined. Only after that toy-feasibility returns positive should theorist-time be budgeted.

---

## Summary table

| ID | Axis | Barrier? | Grade |
|---|---|---|---|
| G1 | Lipschitz-direction self-consistency | Escapes | MOONSHOT (TOY-SUB-PROBLEM for axisymmetric restriction) |
| G2 | Perelman-analogue W-functional | Escapes (if closes) | MOONSHOT |
| G3 | SDiff Riemannian curvature + Bochner | Escapes | MOONSHOT (INCREMENTAL for near-Beltrami) |
| G4 | Type-II self-similar no-swirl | Escapes | TOY-SUB-PROBLEM |
| G5 | Viscous damping vs Elgindi profile | Escapes (C^{1,α} regime) | TOY-SUB-PROBLEM / INCREMENTAL-OVER-KNOWN |
| G6 | Obstruction-class cohomology | Probably BLOCKED | MOONSHOT, likely futile |

Two of the six (G4, G5) are credibly publishable sub-problem attacks; two (G2, G3) are in the genuinely "Perelman-tier moonshot" bucket that the scout flagged as the highest-value long-shots; G1 is a bridge between sub-problem and moonshot depending on restriction; G6 is flagged for inclusion but with a warning.

No proposal claims a Clay-level result. Each proposal names at least one concrete failure mode that a competent referee would raise. The three graph-technique nodes most heavily leveraged — `t_conserved_quantity`, `t_rescale_for_asymptotic_geometry`, `t_ricci_flow_with_surgery` — align with the scout's identification of the SPEC-PLAUS bucket as where novelty can enter.

### Differential gain — non-averaging-invariant structures exploited

- G1: pointwise direction field ξ = ω/|ω|, Biot–Savart 0/0 cancellation.
- G2: Leray pressure–velocity duality; specific vortex-stretching sign.
- G3: Lie-algebraic curvature tensor on SDiff (Jacobi identity).
- G4: pointwise a priori bound on ω^θ/r (supercritical, transport-conserved in no-swirl axisymmetric).
- G5: Elgindi's explicit Biot–Savart fundamental-model reduction (C^{1,α}-regime algebraic structure).
- G6: (if any) analytic-not-topological cohomological structure; uncertain.

All but G6 identify a concrete structure that Tao's F_avg destroys. That is the minimum bar for escaping the supercritical barrier and is the reason each of G1–G5 is worth keeping on the board.
