# Mathematician 3 — Fresh vocabulary / new primitive objects

**Role.** Propose cross-tradition combinations and invent new primitives for attacking
3D NSE global regularity, while labeling novelty honestly. Iter 3 collapsed because
PLAUSIBLY-NEW proposals turned out to be repackagings; I name the repackaging
candidate out loud for every proposal. STANDARD techniques (fixed point, L-P, Picard,
rescaling) I treat as exhausted; my priors are stochastic regularization,
renormalization, optimal transport, information/entropy, ergodic correspondence,
formal verification. I skip category-theoretic framings (UNLIKELY per scout).

Each "compose X with Y" proposal must clear: (i) is the composition already named
in the literature; (ii) does it use a feature not preserved under Tao's cascade-hollow
averaging; (iii) what does it prove, at what cost in hypotheses.

---

## Part A — Attack proposals

### Proposal A1 — Zero-noise-limit pathwise entropy (Otto × Flandoli × ESS)

**Target.** Prove: for 3D NSE on 𝕋³ with smooth mean-zero divergence-free datum u₀,
the pathwise solution arising as the zero-noise limit from a class of stochastic NSE
with strictly-coloured dissipative noise inherits a *monotone Wasserstein-2 action*
that, combined with ESS continuity (Seregin 2012), forbids `‖u(t)‖_{L³}` from touching
infinity. This does **not** solve Clay — it conditionally replaces "no L³ blowup" with
"no L³ blowup if one very specific Otto-style monotone quantity is indeed monotone."

**Core idea.** Two ingredients nobody has combined cleanly:

1. Flandoli–Gubinelli–Priola multiplicative transport noise
   `du = (νΔu − (u·∇)u − ∇p)dt + Σ_k σ_k·∇u ∘ dB_k`, with σ_k chosen so the
   Itô-to-Stratonovich correction yields a noise-enhanced dissipation (ν + ν_LES)Δ.
2. On W₂(𝕋³, vorticity densities), read the stochastic vorticity equation
   `dω = (νΔω + (ω·∇)u − (u·∇)ω)dt + noise` as a stochastic gradient flow of
   relative entropy `H(ρ|Leb) = ∫ ρ log ρ dx`. Otto-calculus-on-vorticity, not
   velocity; vorticity has an L¹ conservation that velocity lacks.

**Graph techniques.** `t_probabilistic_existence` + `t_conserved_quantity` (if the
entropy is monotone) + `t_ergodic_correspondence` (for the zero-noise limit step) +
`t_duality` (for Otto structure). This is a genuine cross-cluster combination:
clusters 03, 09, 11 wired together.

**Derivation sketch.**
  - (known) For each ε > 0, stochastic NSE with noise-enhanced viscosity `ν + ε`
    has pathwise global smooth solutions for a dense set of initial data (Flandoli
    2011 gives stationary measures; pathwise smoothness holds in the hyperviscous
    regime).
  - (new) Pathwise Otto action along a realisation:
      `𝒜_ε(u) = ∫₀ᵀ ‖∂_t ρ_ω‖²_{W₂,μ_t} dt − ∫₀ᵀ H(ρ_ω | Leb) dt`,
    ρ_ω the vorticity absolute-value density.
  - Claim: `𝒜_ε` is monotone non-increasing under the stochastic flow, *uniformly in ε*.
  - Γ-convergence 𝒜_ε → 𝒜₀ as ε → 0; any L³-unbounded Leray–Hopf makes 𝒜₀ explode.

**Escapes Tao barrier?** Partially. Otto/W₂ structure lives on the vorticity
distribution, which is *not* preserved under Tao's cascade-hollow averaging (F_avg
decouples Fourier modes Otto couples through spatial geometry). So not ruled out by
the averaged-NSE argument. Catch: whether 𝒜_ε is actually monotone is the open
question; reducing to energy dissipation (critical) or enstrophy (supercritical-uncontrolled)
both kill the approach.

**External inputs.** Flandoli–Gubinelli–Priola 2010 (Inventiones 180), Agresti–Veraar
stochastic maximal regularity, Otto 2001 JDE Wasserstein framework, Villani's *Optimal
Transport: Old and New*, Seregin 2012 L³ continuity.

**Failure modes.** (1) 𝒜_ε reduces under IBP to `ν‖∇u‖²_{L²}` + l.o.t. — i.e. is
dissipation in disguise (most likely). (2) Γ-convergence fails because the W₂
tangent cone degenerates at blowup time. (3) Zero-noise limit is non-unique (Brézis–Ekeland).

**Honest grade.** SPECULATIVE. ~20% new functional; ~60% collapses to dissipation;
remainder inconsistent. Worth 1 postdoc-year.

---

### Proposal A2 — Regularity-structures reclassification of NSE subcriticality

**Target.** Prove the precise statement: *3D NSE is locally subcritical in the sense
of Hairer's regularity structures* (as an SPDE driven by arbitrarily small white
noise) but only marginally, at distance O(log log) from criticality. Then use the
Bruned–Chandra–Chevyrev–Hairer algebraic renormalization machinery to conclude that
the renormalization constants for NSE do not diverge, hence stochastic NSE admits
global mild solutions with noise intensity set to any fixed positive value.

**Core idea.** Hairer/GIP tools target subcritical SPDEs (KPZ, Φ⁴₃). Conventional
reading: 3D NSE is *not* subcritical for these tools because u·∇u exactly matches
the smoothness budget. Inversion: drive with *weak* additive noise smoother than
white (Besov regularity `−1/2 − ν`, small ν > 0); nonlinearity is then subcritical
by the ν margin. Does the margin carry information back to deterministic NSE at ν → 1/2?

**Graph techniques.** `t_axiomatize_from_instances` (formalise what subcriticality
means for NSE), `t_frequency_decomposition` (paraproduct bookkeeping), `t_probabilistic_existence`
(stochastic lifting), `t_transference_bridge` (from SPDE-with-δ-noise back to deterministic,
this is the speculative bridge).

**Derivation sketch.** (1) ξ ∈ `B^{−1/2−ν,∞,∞}`, ν ∈ (0, 1/2). (2) Regularity
structures gives local well-posedness with renormalization constants C_ν,
divergent as ν → 1/2. (3) Estimate C_ν: if C_ν = O(|log ν|) or O(1), get uniform-in-ν
solution on [0, T(u₀, ν)]. (4) If T(u₀, ν) → T★ > 0, extract a quantitative
Koch–Tataru-style criterion improved by one log.

**Escapes Tao barrier?** No. Regularity structures are L-P-based, hence in Tao's
averaging-invariant world. Their extra power (Hopf algebra of labelled trees, BPHZ)
is algebraic, not scaling-breaking. Acknowledgment: this does not break Tao. It
sharpens Koch-Tataru — publishable but not Clay.

**External inputs.** Hairer 2014 *A theory of regularity structures* (Inventiones 198),
Bruned–Chandra–Chevyrev–Hairer 2021 algebraic renormalization, Gubinelli–Imkeller–Perkowski
2015 paracontrolled distributions, Catellier–Chouk 2018 for the relevant SPDE analysis.

**Failure modes.** (1) C_ν diverges polynomially — ε → 0 limit not uniform. (2)
ν → 1/2 and ξ → 0 limits do not commute (Φ⁴₃ precedent). (3) Margin is single-log,
improvement quantitatively inside Koch-Tataru.

**Honest grade.** SPECULATIVE. ~10% of beating KT by measurable factor; 0% of Clay.
Pursue as sub-problem only.

---

### Proposal A3 — Ergodic dimension-3 lifting of a Foias–Prodi statistical regularity

**Target.** Prove: if the invariant measure μ of forced 3D NSE (with *any*
non-degenerate additive forcing ensuring ergodicity) concentrates on a
finite-Hausdorff-dimensional attractor A ⊂ L² with `dim_H(A) < ∞`, then μ-almost
every trajectory originating from u₀ ∈ A is globally smooth; further, the "bad"
initial data forming the non-smooth Leray-Hopf extensions have μ-measure zero.
Then use a *descending-ergodic-hierarchy* lift (Foias–Prodi determining modes
+ Furstenberg-correspondence-style selection) to show this null set is also
Lebesgue-null on the space of smooth initial data.

**Core idea.** Forced NSE has a global attractor of conjectured finite dim (CFT 1985).
Assuming finite-dim: Foias–Prodi determining modes + Kuksin–Shirikyan ergodicity
gives rigidity — μ-a.s. trajectories are slaved by low-mode projection. Novel step:
use `t_furstenberg_correspondence_principle` to transport statistical regularity to
individual-trajectory regularity. Furstenberg maps density-of-a-set ↔ recurrence-of-a-trajectory.
For NSE: μ-density of smooth trajectories ⇒ smoothness of "generic" individual
trajectory in a natural topology on initial data. Known direction in ergodic theory
(Weyl, multiple recurrence); application to PDE attractors is not standard.

**Graph techniques.** `t_furstenberg_correspondence_principle` (composite) + `t_ergodic_correspondence` +
`t_compactness_argument` (for finite-dim attractor) + `t_conserved_quantity` (the invariant measure
itself). This binds clusters 06, 09, 11.

**Derivation sketch.** (1) f smooth non-degenerate; μ exists and ergodic
(Hairer–Mattingly flavour). (2) Hypothesis dim_H(supp μ) < ∞ ⇒ finite-dim inertial
manifold M (also hypothesis). (3) Foias-Prodi on M: flow is Lipschitz ODE, smooth.
(4) Furstenberg correspondence: refine μ-null to Lebesgue-null in a natural topology
via dynamical ε-net adapted from Bourgain 1994 (2D NLS Gibbs). (5) f → 0 limit
collapses the attractor to {0} — killer for unforced Clay.

**Escapes Tao barrier?** Yes, genuinely: Tao's averaging destroys the
determining-modes geometry (F_avg pseudo-decouples Fourier triples, so Foias–Prodi
rigidity fails for averaged NSE). So this uses structure unavailable in the averaged
case. BUT vanishing-forcing limit collapses to trivial stationary solution — nothing
deterministic is extracted in the unforced Clay form.

**External inputs.** Foias–Prodi 1967, Hairer–Mattingly 2006 (Ann. Math.) for 2D
ergodicity, Kuksin–Shirikyan *Mathematics of Two-Dimensional Turbulence*, Constantin–
Foias–Temam 1985 for attractor dimension, Bourgain 1994 Gibbs measures for NLS.

**Failure modes.** (1) 3D attractor dim may be infinite. (2) f → 0 degeneracy
(no ergodic measure without forcing). (3) Furstenberg lift depends on measure-preservation;
NSE is dissipative, breaking the multiple-recurrence step.

**Honest grade.** SPECULATIVE for the forced statistical statement (approachable).
MOONSHOT for unforced Clay (failure 2).

---

### Proposal A4 — Formal-verification-driven search for a Perelman entropy analogue

**Target.** Use Lean 4 mathlib + a specific elliptic-regularity and monotone-quantity
library to *systematically enumerate and mechanically verify candidate monotone
quantities* Φ(u) under 3D NSE evolution. Enumeration over a polynomial-in-∇ᵏ basis
with degree ≤ D up to D = 4, coupled with a mechanised Leibniz-rule-and-integration-
by-parts engine, for each candidate produces `dΦ/dt = P(∇u, ...)` as a polynomial in
derivative invariants; sign-definiteness of P is then checked by Positivstellensatz
(or certified by interval arithmetic when coefficients are irrational).

**Core idea.** Perelman's W-entropy was guessed then verified. For NSE, 40 years of
guessing has failed. The scale-covariant polynomial-in-derivatives basis is finite
at each degree and can be enumerated. Positivstellensatz decides sign-definiteness
of polynomials. Lean certifies. This composition has not been run.

**Graph techniques.** `t_formal_verify` (cluster 10) + `t_conserved_quantity` (cluster 03)
+ `t_polynomial_method` (cluster 11) + `t_finite_case_check` (cluster 10). Four-way
composition.

**Derivation sketch.** (1) Derivative algebra `E_k = {∂^α u_i : |α| ≤ k}`;
basis invariants = SO(3) × translations × scaling-weighted polynomials in E_k.
(2) Fix supercritical target weight; enumerate degree ≤ 4. (3) For each Φ = ∫J(u)dx,
symbolically compute `dΦ/dt` via NSE + IBP → polynomial Q in E_m. (4) Test Q ≤ 0
pointwise by Positivstellensatz/SDP; certify in Lean. (5) Output: either a concrete
Φ with dΦ/dt ≤ 0, or a verified no-monotone-Φ-at-degree-D obstruction theorem. Both
publishable.

**Escapes Tao barrier?** Only if the found Φ uses IBP cancellations depending on
divergence-free + Leray structure rather than pure scaling. The scan by design uses
Leray projection, so any positive output is averaging-destroying. Negative output
(exhaustive obstruction) also informative.

**External inputs.** Lean 4 mathlib current state (as of 2025/2026), Parrilo-Lasserre
moment/SOS hierarchy for Positivstellensatz, Gorinov-Wilkening or Bernstein-Flajolet
type derivative-invariant enumeration.

**Failure modes.** (1) Combinatorial explosion at D ≥ 5; Perelman-analogue may need
degree 6–8. (2) Positivstellensatz certificate size can be exponential. (3) Success
≠ Clay: a monotone supercritical Φ may not control any critical norm.

**Honest grade.** REALISTIC as a 2-3 year project to degree 4. Publishable either
way. ~5% Clay-touching, ~70% publishable structural result.

The one proposal I think a small team should actually try.

---

### Proposal A5 — An information-theoretic "Fisher-like" monotone for vorticity

**Target.** Prove: for a Leray-Hopf solution of 3D NSE on 𝕋³, the *Fisher information
of the vorticity magnitude* `F(t) = ∫ |∇ log |ω|² |² |ω|² dx` (when defined, and in
a regularized sense otherwise) decays by at least `ν F(t) − C ν^{-1} F(t)^{γ}` for
some γ slightly above 1. If γ can be improved to γ = 1 with the correct constants,
this gives a new, genuinely supercritical differential inequality for the vorticity.

**Core idea.** Fisher information = Otto-gradient² of relative entropy wrt Leb; the
log-Sobolev-controlled quantity for heat equations. Applied to |ω|², it uniquely
combines: transport of |ω|² with stretching; diffusion νΔω; entropy-dissipation
interpretability. Previous Fisher-like quantities for NSE (Foias–Manley–Rosa–Temam,
Doering–Foias) use velocity-spectrum Fisher, not vorticity magnitude.

**Graph techniques.** `t_conserved_quantity` + `t_duality` (Otto calculus duality
of entropy and Fisher) + `t_interpolate_and_continue` (sharp log-Sobolev) +
`t_auxiliary_construction`.

**Derivation sketch.** (1) ρ = |ω|²/‖ω‖²_{L²}; F(t) is the Fisher of ρ.
(2) Compute dF/dt from NSE evolution of `∫|ω|² log|ω|² dx`. (3) Stretching term
`ω·∇u·ω` contributes both signs when integrated against `∇log|ω|²`; sort
definite/indefinite pieces. (4) Compare Chae 2007 (local vortex-direction
integrability prevents blowup): F is a weighted-global version of Chae's hypothesis.

**Escapes Tao barrier?** Marginal. Fisher is non-Fourier-local (log is a nonlinear
transform) so not preserved under Tao's averaging — in principle not barrier-limited.
But the sign of dF/dt is the open question; Chae-style attempts fail because the
nonlinear term gets cubic in F rather than quadratic.

**External inputs.** Villani's *Entropy Production and Convergence to Equilibrium*,
Bakry-Émery curvature-dimension theory (not directly but conceptually), Chae 2007
vortex-direction regularity, log-Sobolev for the heat kernel on 𝕋³.

**Failure modes.** (1) Cubic bound `C ν^{-1} F^{3/2}` gives blowup in F itself
(Chae wall). (2) Fisher ill-defined where ω vanishes on positive-measure set;
regularization breaks monotonicity. (3) Even monotone F may not control a critical
norm (F is supercritical by construction).

**Honest grade.** SPECULATIVE, tier A1. Overlap with Chae depletion is real; need to
show Fisher approach is distinct. Worth 6 postdoc-months.

---

## Part B — New technique node proposals

### B1 — `t_renormalization_group_flow_with_blowup_profile`

**Cluster.** 06_topology_and_obstruction (because RG fixed-point analysis is
fundamentally an obstruction-theoretic statement: a blowup is an obstruction to
extending the RG flow past the fixed point).

**Function signature.** `(PDE, self-similar ansatz, scale hierarchy) → (RG map R_λ, fixed points, basins of attraction)`
More precisely: Input X = (evolution PDE `∂_t u = F(u, ∇u, ...)` with scaling
symmetry, a candidate blowup profile u★, a block-spin transformation parameter λ).
Process P = construct the renormalization map `R_λ : u(·, T − λ²t) ↦ λ^α u(λx, T − λ²t)`,
compose with mode-integration, iterate. Output Y = fixed points of `R_λ`, basins,
linearized spectrum around fixed points.

**Definition.** Given a dissipative PDE with scaling symmetry and a candidate blowup
profile u★ at time T, the renormalization map `R(u)(t, x) = λ^α u(T − λ²(T−t), λx)`
composed with block-spin (integrating out modes of wavelength ≥ 1 in a
partial-coherent-state sense) defines a self-map of profiles modulo fast modes.
Fixed points of R are candidate self-similar profiles; eigenvalues of dR at the
fixed point give stability. Blowup iff trajectory reaches a fixed point whose
unstable manifold meets the initial data. Imports Bricmont–Gawędzki–Kupiainen from
KPZ to general dissipative PDE.

**Invocations.** Bricmont–Gawędzki–Kupiainen 1994 (rigorous RG for KPZ/Φ⁴₃);
Gallay–Wayne 2002 (2D NSE self-similar asymptotics); Feigenbaum–Coullet–Tresser
period-doubling. Unlocks: disciplined search for NSE self-similar blowup as R-fixed
point with spectral condition as verifiable criterion; or rigorous Type-I
non-existence via absence of stable R-fixed point.

**Risk of being a repackaging.** Real. `t_rescale_for_asymptotic_geometry` covers
"rescale around putative blowup and study the profile." What's new in B1 is
*iteration* of rescaling with mode integration — the block-spin step. If one insists
block-spin = L-P decomposition of a rescaled profile, B1 collapses to
`t_rescale_for_asymptotic_geometry` ∘ `t_frequency_decomposition`. The distinct
feature is the *dynamical-systems view* of R (self-map, fixed-point structure,
spectral analysis of dR) — not captured by either ingredient alone.

**Grade.** NEW-GENUINE as a composite node (analogous to how `t_ricci_flow_with_surgery`
composes `t_flow_with_surgery`). If the graph collapses rescale + iterate, demote
to NEW-AS-REPACKAGING.

---

### B2 — `t_wasserstein_gradient_flow_with_nonlinear_transport`

**Cluster.** 09_cross_world_bridges (because Otto calculus itself is the
PDE↔optimal-transport bridge).

**Function signature.** `(Evolution equation on measures with an advection term) → (Benamou-Brenier action / Wasserstein pseudo-gradient flow interpretation)`
Input X = a PDE for a positive measure ρ of the form `∂_t ρ = div(a(ρ, ∇ρ, ...)∇δF/δρ) + div(v ρ)` where F is a functional on densities, `δF/δρ` its functional derivative, and v is a (possibly nonlinear, possibly non-gradient) velocity.
Process P = express the equation as `∂_t ρ = −∇_{W₂} F[ρ] + div(v ρ)` in the formal Riemannian geometry of W₂, then identify the *deviation* from being a pure gradient flow as `div(v ρ)`, and derive an Otto-style entropy dissipation inequality.
Output Y = an entropy-dissipation inequality `d/dt F[ρ] ≤ −C‖∇_{W₂}F‖²_{tangent} + R(v, ρ)` where R is the correction due to the non-gradient velocity.

**Definition.** On (𝒫₂(𝕋³), W₂), the W₂-gradient flow of a convex F is
`∂_t ρ = div(ρ ∇ δF/δρ)`. When the PDE has an extra advection `v ρ` not derivable
from an energy, it is W₂-gradient-flow-plus-transport. The technique packages:
(i) the decomposition into gradient and transport parts; (ii) JKO scheme for
solutions; (iii) entropy-dissipation inequality with explicit transport correction;
(iv) criteria for when transport is dominated by dissipation.

**Invocations.** Otto 2001 (porous medium as q-Rényi gradient flow);
Jordan–Kinderlehrer–Otto 1998 (Fokker–Planck); Carrillo–McCann–Villani (granular
media); Ambrosio–Gigli–Savaré framework. Unlocks (NSE): A1/A5-style Wasserstein
structure on vorticity, with `(u·∇)ω` as the non-gradient term. Unlocks (elsewhere):
Fokker–Planck + non-gradient advection, cross-diffusion, chemotaxis with flow.

**Risk of being a repackaging.** Moderate. Otto calculus could be absorbed into
`t_duality` (entropy–Fisher duality). What's new is the *with-nonlinear-transport*
modifier and its bookkeeping. PDE literature has "driven JKO" or "W-gradient flow
with constraint" but they are fragmented. Honest risk: collapses to `t_duality` +
`t_conserved_quantity`.

**Grade.** NEW-AS-REPACKAGING tending to NEW-GENUINE. Add as composite with
explicit subgraph refs; distinctive feature is the transport-correction bookkeeping.

---

### B3 — `t_mechanized_monotone_quantity_search`

**Cluster.** 10_empirical_and_computational (home of `t_formal_verify` and
`t_finite_case_check`).

**Function signature.** `(Evolution PDE, invariant-polynomial basis, target weight) → (Positivstellensatz certificate of monotonicity or an obstruction theorem)`
Input X = an evolution PDE; a basis of symmetry-invariant polynomial derivative invariants parametrized by degree D, weight w, and derivative order k; a target "supercritical" weight bound.
Process P = enumerate candidate functionals at fixed (D, w, k); for each, symbolically compute the time-derivative under the PDE, apply integration by parts, reduce to a polynomial in a finite basis of point-wise derivative quantities; call a Positivstellensatz solver to decide sign-definiteness; optionally certify in Lean.
Output Y = a (possibly empty) finite list of monotone functionals at the given (D, w, k), plus a formally-verified proof of their monotonicity or a formally-verified proof that no such functional exists in the enumerated class.

**Definition.** Given `∂_t u = F(u, ∇u, …, ∇ᵏu)` with Lie symmetry G, parameters
(D, w, k) cut out the space Ω(D, w, k) of G-invariant polynomials in jet variables
up to order k, degree D, scaling weight w. For Φ = ∫J dx ∈ Ω, `dΦ/dt` is an integral
of a polynomial Q symbolically computable. Pipeline: enumerate Ω, compute Q, run
SOS/Positivstellensatz for Q ≤ 0, certify in Lean, aggregate.

**Invocations.** Classical monotonicity discoveries (Perelman W-entropy; Li–Yau
Harnack; Hamilton 2D Ricci entropy; Huisken MCF). Olver invariant-basis enumeration.
Unlocks: systematic Perelman-analogue search across NSE, Euler, compressible fluid,
wave, Schrödinger; rigorous low-degree obstructions; mechanised "find monotone Φ
for any evolution PDE" service. Meta-level: a data-augmented technique search over
the graph itself.

**Risk of being a repackaging.** Conflict candidates: `t_formal_verify`,
`t_finite_case_check`, `t_conserved_quantity`, `t_polynomial_method`. B3 composes
these (objective / search space / enumeration / certification); none alone is the
technique. Sharper risk: "enumerate + mechanically verify" is the universal
computer-assisted template and may be too general to merit its own name.
Counter-argument: Perelman's W-entropy was a singular discovery; a mechanized
enumeration that *finds such things* is qualitatively different — analogous to
`t_contraction_fixed_point` (general) vs `t_wiles_modularity` (specific composite).

**Grade.** NEW-GENUINE at the composite level. Flag: no successful instance yet.
Recommend adding provisional; un-provisionalise on first firing (NSE or other).

---

### B4 — `t_zero_noise_limit_with_preserved_regularity`

**Cluster.** 11_probabilistic_and_counting (home of `t_probabilistic_existence`).

**Function signature.** `(Family of SPDEs {Eq_ε}_{ε > 0}, regularity class R) → (A priori bound on deterministic Eq_0 in R via Γ-convergence of SPDE solutions)`
Input X = a family of SPDEs parametrized by ε (typically noise intensity or
viscosity perturbation or a coupling parameter), each with pathwise smooth
solutions in a regularity class R_ε, plus a limiting deterministic equation Eq_0
at ε = 0.
Process P = (a) prove R_ε ⊂ R for all ε > 0 with a uniform-in-ε bound via
stochastic maximal regularity (Agresti–Veraar-style); (b) prove Γ-convergence of
the solution operators as ε → 0 in a suitable path-space topology; (c) transport
the uniform-in-ε bound to a bound on Eq_0 solutions by lower-semicontinuity.
Output Y = a deterministic a priori bound on Eq_0 solutions in R, inherited
from the stochastic family.

**Definition.** Given `du_ε = A(u_ε) dt + ε B(u_ε) dW`, suppose for all ε > 0 that
u_ε has pathwise-unique global smooth solutions with bound `‖u_ε‖_R ≤ C_ε(‖u₀‖_R)`.
Technique: (i) uniform-in-ε bound on C_ε; (ii) Γ-convergence of u_ε → u_0; (iii)
transport bound to u_0 by LSC. Key design: noise B must regularize enough for ε > 0
global smoothness but not so much that ε → 0 is vacuous.

**Invocations.** Flandoli–Gubinelli–Priola 2010 (noise regularises transport);
Hairer–Mattingly 2006 (2D NSE degenerate-noise ergodicity); Delarue–Flandoli–Vincenzi
and Krylov–Röckner (strong uniqueness for SDEs with singular drift). Unlocks:
systematic use of SPDE theory as a pathway to *deterministic* a priori bounds (not
just existence/uniqueness); specifically powers A1.

**Risk of being a repackaging.** `t_probabilistic_existence` in the graph is the
Erdős flavour (random colorings → nonzero probability), not SPDE flavour — the
probabilistic object here is a time-evolution process. So `t_probabilistic_existence`
does not cover B4. Real risk: B4 = `t_probabilistic_existence` (broadly) +
`t_compactness_argument` (Γ-convergence). That's what it is; the composite pattern
is distinctive in the *preservation of regularity* across ε → 0, which neither
parent singles out.

**Grade.** NEW-GENUINE at the composite level. Argues for inclusion: the pattern
is specifically named in the SPDE literature; recognising it links clusters 04, 09, 11.

---

## Summary of honesty labels

| Proposal | Clay-touching? | Probabilistic plausibility of the claim as stated | Repackaging candidate |
|---|---|---|---|
| A1 | No; conditional L³-no-blowup refinement | 15-20% of yielding something not collapsing to dissipation | Otto-action ≈ Doering-Foias energy dissipation |
| A2 | No; quantitative Koch-Tataru refinement | 10% of beating KT by measurable factor | Regularity structures are Littlewood-Paley in disguise |
| A3 | Conditionally, for forced NSE | 5% for forced statistical; ~0% for unforced | Inertial manifold theory |
| A4 | Possibly if scan succeeds | 5% for Clay-touching output; 70% for structural output | Already a concrete research program |
| A5 | No; new conditional criterion | 15-20% | Chae geometric depletion |
| B1 | — | Composite — real composite of rescale + LP + dynamical systems | `t_rescale_for_asymptotic_geometry` ∘ `t_frequency_decomposition` |
| B2 | — | Composite, risk of collapse to `t_duality` | `t_duality` + `t_conserved_quantity` |
| B3 | — | Genuinely new pattern, untested | `t_formal_verify` ∘ `t_polynomial_method` ∘ `t_finite_case_check` |
| B4 | — | Genuinely new composite for SPDE → deterministic | `t_probabilistic_existence` ∘ `t_compactness_argument` |

None of A1–A5 solves Clay. Two of them (A1, A3) arguably advance the forced /
conditional version by clarifying reductions. A4 is the most actionable and the most
likely to produce publishable output within 2-3 years, regardless of whether it
touches Clay.

All Part-B nodes are marked with explicit repackaging candidates; under strict
repackaging test, B2 is the weakest (plausibly collapses), B3 the most defensible
as a new composite.
