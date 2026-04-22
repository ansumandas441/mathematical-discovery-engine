# MonoQuant Research Plans

Five concrete research plans using MonoQuant v0.2 + targeted extensions.
Each plan specifies: scope, what's known vs. what's not, required engineering,
monthly milestones, deliverables, risk assessment, and honest novelty grading.

Plans are sized so that plans 1 and 2 can run in parallel (complementary
extensions); plans 3, 4, 5 are sequential in that they build on the tool
improvements in plans 1 and 2.

---

## Plan 1 — KdV Hierarchy Enumeration in Lean

**Effort**: 1 month, one researcher.
**Novelty**: Low (results are known). Utility: high (verifiable reference).
**Grade**: Infrastructure / formal-mathematics contribution.

### 1.1 Problem statement

The KdV equation ∂_t u + 6u∂_x u + ∂³_x u = 0 admits an infinite tower of
conservation laws
  H_1[u] = ∫ u dx
  H_2[u] = ∫ u² dx
  H_3[u] = ∫ (u³ − ½u_x²) dx
  H_4[u] = ∫ (5u⁴ − 10u·u_x² + u_xx²) dx
  H_5[u] = ∫ (5u⁵ − 25u²·u_x² − 5u·u_xx² + ...) dx (coefficients rarely tabulated)
  ...

Produced by Miura (1968), Gardner (1971), Magri (1978) via the bi-Hamiltonian
recursion R: H_{n+1} = R · H_n. The recursion operator is standard; applying
it is tedious. Beyond H_5, explicit formulas are rarely written down in one
place.

### 1.2 What's known

- **Abstract existence**: the full tower, via bi-Hamiltonian structure
  (Magri, Gel'fand-Dikii).
- **Explicit formulas**: H_1-H_5 are in Drazin-Johnson, Ablowitz-Clarkson,
  but with inconsistent sign/coefficient conventions across sources.
- **Computer algebra packages**: SymPy, Maple, and Mathematica can compute
  these case-by-case with manual IBP, but no standardised library exists.

### 1.3 What's not known (in usable form)

- A **single reference** that tabulates H_1-H_{10} with a uniform sign
  convention, each checked against a machine-verified identity dH_n/dt ≡ 0.
- A **Lean 4 mathlib contribution** that exports these as formally-verified
  lemmas.
- The **computational cost** of the search at high degree (is H_{10}
  tractable with current tools?).

### 1.4 Engineering required

- **v0.2.1 — push the basis**: currently MonoQuant caps total derivative order
  at `max_derivative_order`. H_{10} has terms like u_xxxxxxxxxx u_xxxxx or
  similar high-order products. We need degree ≤ 10 and derivative order ≤ 8
  simultaneously. The basis enumerator will produce O(10⁴) monomials.
  Optimisation: prune by **scaling weight** — KdV has scaling
  u_λ(t,x) = λ²u(λ³t, λx), so H_n has definite scaling weight; exclude
  monomials whose scaling doesn't match.

- **v0.2.2 — canonical-form reduction**: multiple "equivalent" conservation
  laws can appear (differing by total derivatives). Add a post-processor
  that picks the form with minimum number of terms and lowest maximum
  derivative order.

- **v0.2.3 — Lean export**: generate Lean 4 source that declares each H_n
  as a functional and proves dH_n/dt = 0 modulo IBP, using mathlib's
  calculus library.

### 1.5 Schedule

- **Week 1**: Basis-enumeration scaling-weight filter. Push MonoQuant to find
  H_4, H_5. Cross-check against Drazin-Johnson.
- **Week 2**: Find H_6-H_8 mechanically. Verify via Magri recursion
  R (implemented separately as a symbolic operator, independent check).
- **Week 3**: Canonical-form reducer. Emit clean formulae for H_1-H_10.
- **Week 4**: Lean 4 translation; submit to mathlib as a focused PR
  `Mathlib.Analysis.PDE.KdV.Hierarchy`.

### 1.6 Deliverables

1. `monoquant/examples/kdv_hierarchy.py` — extended search, outputs formulas.
2. `paper/kdv_hierarchy_tabulation.md` — 15-page survey with all 10 H's
   typeset, historical attribution, cross-reference with Magri recursion.
3. `Lean/KdVHierarchy.lean` — mathlib PR.
4. One arXiv preprint: "A mechanized conservation-law tabulation for KdV."

### 1.7 Risks

- **Low probability**: MonoQuant can't close the IBP canonicalisation at H_8+.
  Fallback: ship H_1-H_7 only; still publishable.
- **Low probability**: Lean mathlib review rejects submission; ship as
  standalone Lean library.

### 1.8 Honest novelty grading

- **Mathematics**: 0 / 10. All results known.
- **Infrastructure**: 7 / 10. First mechanized, uniformly-formatted,
  machine-verified tabulation of the KdV tower.
- **Publication track**: J. Symbolic Comp., Adv. Comp. Math., or SIGSAM Bulletin.

---

## Plan 2 — Fractional Burgers α × Φ Threshold Census

**Effort**: 2 months, one researcher.
**Novelty**: Medium. Individual thresholds often known; systematic matrix not.
**Grade**: Survey paper with 1-3 possibly-new sharp thresholds.

### 2.1 Problem statement

The fractional Burgers equation
  ∂_t u + u ∂_x u = −ν(−Δ)^α u
interpolates between
  α = 0 (no dissipation, inviscid Burgers, develops shocks)
  α = 1 (standard viscous Burgers, globally smooth)
  α → ∞ (very strong dissipation, trivially smooth).

Global well-posedness and monotone-functional structure depend on α:
- α ≥ 1: energy ∫u² decays, smoothness global.
- α = ½ (Kiselev-Nazarov-Shterenberg 2008): critical Besov regularity.
- α < ½: supercritical; finite-time blow-up possible (Alibaud-Droniou-Vovelle).

### 2.2 What's known

- Well-posedness thresholds: α = ½ critical for H^{½−α} scaling.
- Energy monotonicity (L²) at any α > 0: trivially known.
- L^p maximum principle at α = 1: known (Aronson-Serrin style).
- L^p at α < 1: less understood; Kiselev-Nazarov and Silvestre have
  partial results.

### 2.3 What's not known (in a systematic map)

- For each candidate functional Φ ∈ {
  L²/2, L⁴/4, L⁶/6, u log u,
  Ḣ^β for β ∈ [0,1],
  weighted norms ∫w(x)·u² dx for various weights,
  entropy with α-dependent kernel ∫u · (-Δ)^{(1-α)/2} log u dx
  }, at which α_crit(Φ) does monotonicity fail?

- Are there **α-specific monotone functionals** that exist only in
  windows like α ∈ [0.6, 0.9]?

- **Sharp thresholds** for L^p conservation/monotonicity as a function
  of α are partially known but not exhaustively tabulated.

### 2.4 Engineering required

- **v0.2.4 — parameterised-PDE factory**: allow α to be a symbolic
  parameter; sweep across a grid of α values efficiently with caching.

- **v0.2.5 — weighted functional support**: allow Φ = ∫w(x) · ρ(u) dx
  where w is a prescribed weight function.

- **v0.2.6 — α-interval sign tracker**: instead of point-wise α ∈ ℚ
  evaluations, track sign of Q as α varies. Emit certificates like
  "MONOTONE for α ∈ [0.63, 0.80]; INDEFINITE otherwise."

- **No new dependencies**: fractional Laplacian is already supported.

### 2.5 Schedule

- **Weeks 1-2**: Parameterised-PDE factory + α-sweep orchestrator.
  Automated sweep over (α, Φ) grid of size 20 × 30.
- **Weeks 3-4**: Weighted functional support + critical-Sobolev Φ
  candidates. Sweep the Ḣ^β × α matrix.
- **Weeks 5-6**: Identify at least three distinct α-threshold patterns:
  (i) monotone for all α > α*, (ii) window-monotone, (iii) never monotone.
  Check against published sharp thresholds for calibration.
- **Weeks 7-8**: Write up. If any found threshold is sharper than
  literature, produce a stand-alone proof.

### 2.6 Deliverables

1. `monoquant/examples/frac_burgers_sweep.py`.
2. `paper/frac_burgers_monotone_census.md` — 25-30 page survey with
   ~100-entry table + ~5 published-sharp threshold verifications + 1-3
   candidate new thresholds with human-verified proof.
3. arXiv preprint + submission to Nonlinearity or SIAM J. Math. Anal.

### 2.7 Risks

- **Medium probability**: every threshold we find is already in the
  literature. Fallback: ship as a systematic census with historical
  attribution — still publishable.
- **Low probability**: the α-interval tracker is unstable. Fallback:
  report only pointwise verdicts.

### 2.8 Honest novelty grading

- **Mathematics**: 3 / 10 (possibly 5 if one new threshold is found).
- **Survey value**: 8 / 10 (no such systematic census exists).
- **Publication track**: Nonlinearity, CMP, J. Differential Equations.

---

## Plan 3 — Mass-Critical gKdV Conservation Enumeration

**Effort**: 3 months, one researcher.
**Novelty**: Medium-high. A focused problem where the answer is genuinely open.
**Grade**: Either new conservation laws or a clean non-existence theorem;
both are real findings.

### 3.1 Problem statement

The generalised Korteweg-de Vries equation
  ∂_t u + ∂_x(u^p / p) + ∂³_x u = 0
is integrable only for p = 2 (KdV) and p = 3 (modified KdV). For p ≥ 4 it's
non-integrable. Among non-integrable gKdVs, p = 4 is distinguished as
"mass-critical": the mass-conservation functional ∫u² dx is scale-invariant
under u_λ(t,x) = λ^{1/2} u(λ³t, λx).

### 3.2 What's known

- **Three conservation laws**: mass ∫u², momentum ∫xu (modulo gauge),
  energy ∫(u_x²/2 − u^5/20).
- **Blow-up structure**: Merle 2001; Martel-Merle: solutions with mass
  above the ground-state mass can blow up in finite time in H¹ via
  self-similar profile.
- **Scattering below ground-state**: Dodson 2017 for mass-critical gKdV,
  radial or cylindrical restricted.
- **Recursion operator**: the bi-Hamiltonian structure of KdV does NOT
  extend to gKdV p=4 in a useful way; no recursion generates further
  conservation laws from the existing three.

### 3.3 What's not known

- Does gKdV at p=4 admit a **polynomial-differential conservation law of
  degree 4 or higher** beyond {mass, momentum, energy}?
- If yes: what is it? It would be a substantial structural finding.
- If no: a machine-verified **non-existence theorem** at a bounded
  polynomial-degree / derivative-order up to D × N.
- Similar questions for gKdV p = 5, 6 ("mass-supercritical" and "energy-critical").

### 3.4 Engineering required

- **v0.2.7 — scaling-weight prefilter**: for gKdV at p, a candidate
  Φ must respect the scaling symmetry. Add a preprocessing step that
  enumerates only scaling-compatible monomials. Dramatically shrinks
  the basis and enables deg≤8, deriv≤4 searches.

- **v0.2.8 — gauge-invariant conservation detection**: conservation
  laws modulo spatial translation gauge. Currently the tool finds the
  obvious ones; we need to filter out trivial-by-gauge duplicates.

### 3.5 Schedule

- **Month 1**: Engineering (scaling-weight prefilter, gauge-invariant
  filter). Sanity check: recover KdV p=2 hierarchy at deg≤6 deriv≤3.
  Verify it finds mass, momentum, energy for p=4 and nothing else
  at low basis.

- **Month 2**: Push the basis. Run p=4 search at deg≤8 deriv≤6. Two
  possible branches:
  - (A) A candidate Φ survives all IBP reductions as a conservation
    law → manual verification + independent computer-algebra cross-check.
  - (B) No candidate survives → frame as non-existence theorem at the
    tested basis and document.

- **Month 3**: If branch (A): write up the new conservation law with
  a human-readable proof. If branch (B): write up the exhaustive-search
  non-existence theorem with a basis-completeness argument.

### 3.6 Deliverables

1. `monoquant/examples/gkdv_p4_search.py`.
2. `paper/gkdv_mass_critical_conservation.md`.
3. arXiv preprint, submission to CMP or J. Nonlinear Sci.
4. If branch (A): a Lean 4 verification of the new conservation law.

### 3.7 Risks

- **Medium-high probability** of branch (B) (non-existence): this is
  itself publishable but less exciting. Mitigation: include in the
  same paper a sharp **finite-complexity statement**: "gKdV p=4 admits
  exactly 3 conservation laws of polynomial differential type at
  deg ≤ D and derivative order ≤ N, for (D, N) up to (8, 6)."

- **Low probability** of branch (A) finding a previously-unknown
  conservation law for p=4 that turns out to be in some obscure
  reference. Mitigation: extensive literature scan before publication.

### 3.8 Honest novelty grading

- **Mathematics**: 5-7 / 10 depending on branch.
- **Publication track**: CMP, Invent. Math. (if branch A), or
  J. Nonlinear Sci. / J. Differential Equations.

---

## Plan 4 — 2D Keller-Segel Full-Coupling Lyapunov Census

**Effort**: 3 months, one researcher.
**Novelty**: Medium-high. The critical-mass structure is active research.
**Grade**: Parameter-map paper with 1-3 new sharp Lyapunov inequalities
plausible.

### 4.1 Problem statement

The 2D parabolic-elliptic Keller-Segel system
  ∂_t n = Δn − χ ∇·(n ∇c)
  −Δc = n − ⟨n⟩
models chemotactic aggregation. Critical mass M_c = 8π/χ: for total mass
below, solutions are global; above, finite-time blow-up can occur.

Below critical mass, the free energy
  F[n] = ∫(n log n − ½ n c) dx
is monotone decreasing. This was established by Blanchet-Dolbeault-Perthame
(2006) et seq.

### 4.2 What's known

- Critical mass 8π/χ (Jäger-Luckhaus, Nagai 1995).
- Monotonicity of F below critical mass (Blanchet-Dolbeault-Perthame 2006).
- Logarithmic Hardy-Littlewood-Sobolev sharp constant (Beckner 1993, Carlen-Loss).
- **Variants**: logistic Keller-Segel (∂_t n = Δn − χ∇·(n∇c) + n(1-n)),
  anisotropic, cross-diffusion — partially understood.

### 4.3 What's not known

- **Sharp Lyapunov functionals for cross-diffusion variants**:
  predator-prey chemotaxis, multi-species KS, with entropy-like structure
  still being developed.
- **Porous-medium KS**: ∂_t n = Δn^m − χ∇·(n∇c) for m > 1: Lyapunov
  structure as a function of m is known asymptotically but not sharply.
- **Logistic KS**: does the Lyapunov structure persist? How does the
  growth term interact with the chemotactic term?
- **Fully-nonlinear cross-diffusion (SKT)**: ∂_t n = Δ(d(n)n) + lower
  order — sharp entropy inequalities unresolved.

### 4.4 Engineering required

- **v0.3.1 — non-local operator support**: MonoQuant needs to understand
  (−Δ)⁻¹ applied to a scalar field. Representation: Fourier-side multiplier
  |ξ|⁻², with symbolic rules for integration-by-parts. Substantial extension
  (2-3 weeks).

- **v0.3.2 — elliptic-constraint-aware IBP**: when c is defined via
  −Δc = n, any expression involving c should be replaced by its
  defining integral kernel under IBP. Implement as a constraint-
  propagation rule.

- **v0.3.3 — parameter-sweeping for multi-parameter PDEs**: KS has χ
  and possibly m (porous-medium), r (logistic). Multi-parameter sweep.

### 4.5 Schedule

- **Month 1**: Engineering (non-local operator + elliptic constraint).
  Test by recovering F = ∫(n log n − ½ n c) as monotone under classical
  KS, sanity-check against BDP.

- **Month 2**: Sweep candidate variants:
  - Porous-medium KS at m ∈ [1, 3] in steps of 0.25.
  - Logistic KS at growth rate r ∈ [0, 2].
  - Cross-diffusion SKT.
  For each, run MonoQuant on a parameterised Lyapunov family.

- **Month 3**: Pick the 2-3 most promising variants where MonoQuant
  reports a candidate Lyapunov. Verify by hand. If one holds, prove
  sharpness by optimising the candidate family.

### 4.6 Deliverables

1. `monoquant/pdes/keller_segel_full.py` with full elliptic coupling.
2. `paper/keller_segel_lyapunov_census.md`.
3. Possibly 1-3 Lean 4 proofs of sharp Lyapunov inequalities.
4. arXiv preprint.

### 4.7 Risks

- **Medium probability**: the engineering for (−Δ)⁻¹ is harder than
  expected. Fallback: ship the simplified scalar KS + other variants
  that don't need elliptic coupling.
- **Low-medium probability**: no new sharp Lyapunov found.
  Fallback: publish as a systematic map + calibration paper.

### 4.8 Honest novelty grading

- **Mathematics**: 4-7 / 10, branch-dependent.
- **Publication track**: CVPDE, J. Math. Biol., or SIAM J. Math. Anal.

---

## Plan 5 — Ricci-Flow / Mean-Curvature-Flow Entropy Enumeration

**Effort**: 6 months, one researcher (can be shorter with 2 researchers).
**Novelty**: High. This is the B3 moonshot from iter-4 portfolio.
**Grade**: Moonshot. Most likely outcome: rebuild of Perelman's W (validation)
+ obstruction theorems for generalisations. Upside: new monotone functional
for Kähler-Ricci or harmonic map flow.

### 5.1 Problem statement

Perelman's W-entropy (2002) for Ricci flow
  W(g, f, τ) = ∫_M [τ(R + |∇f|²) + f − n] · (4πτ)^{−n/2} e^{−f} d V_g
is monotone non-decreasing under coupled Ricci flow + backward heat + scaling.
This monotonicity was the key step in the proof of the Poincaré conjecture.

Analogous questions for other geometric flows (mean curvature flow, Yamabe
flow, Kähler-Ricci flow, harmonic map heat flow) have partial answers
and open cases.

### 5.2 What's known

- **Perelman's W and reduced volume** for Ricci flow (2002-2003).
- **Huisken's monotonicity** for mean curvature flow (1990).
- **Cao's and Song-Tian's results** for Kähler-Ricci: monotone quantities
  in the Kähler setting, partial.
- **Struwe's monotonicity** for harmonic map heat flow, restricted
  settings.

### 5.3 What's not known

- **Entropy functionals for Kähler-Ricci flow** on non-Fano manifolds.
- **Perelman-W analogues for MCF** in codimension > 1: partially
  understood by Smoczyk, White.
- **Yamabe flow entropy**: limited.
- **Harmonic map heat flow** entropies beyond energy.
- **Ricci-DeTurck flow** monotonicity structure is underdeveloped.

### 5.4 Engineering required

This is the biggest engineering lift of the five plans.

- **v0.3.4 — tensor-valued fields**: MonoQuant's scalar/vector PDE
  framework needs a tensor extension. Atoms: g_ij, R_ijkl (Riemann),
  R_ij (Ricci), R (scalar curvature), covariant derivatives ∇_k T.
  Index manipulations, contractions, Bianchi identities.

- **v0.3.5 — coordinate-free symbolic basis**: work entirely in index
  notation with automatic contraction; Young-tableau reduction of
  tensor polynomials.

- **v0.3.6 — Ricci flow RHS**: ∂_t g_ij = −2 R_ij plus coupled flows
  (backward heat, scaling). Multi-field PDE support.

- **v0.3.7 — geometric-Lagrangian-to-Euler-Lagrange**: given a
  candidate W[g, f, τ], compute dW/dt along the coupled flow,
  including all geometric terms (derivative of curvature tensors
  under Ricci flow).

Estimated engineering: 4 months full-time.

### 5.5 Schedule

- **Month 1-2**: Tensor symbolic engine + basis enumeration over
  curvature polynomials. Index reduction + Bianchi-identity
  canonicalisation. Sanity check: recover trivial conservation laws
  on Einstein manifolds.

- **Month 3**: Ricci flow RHS as a PDE in MonoQuant's framework.
  Verify: under Ricci flow, scalar curvature satisfies
  ∂_t R = Δ R + 2|Ric|² — a classical identity. MonoQuant must
  reproduce this.

- **Month 4**: Run the W-entropy verification. The tool should
  certify monotonicity of Perelman's W along coupled Ricci flow +
  backward heat. This is the validation milestone.

- **Month 5**: Run searches for generalised Perelman entropies on
  geometric variants:
  - Kähler-Ricci flow: candidate K[g, f, τ] with the Kähler-Einstein
    factor R_ij = λ g_ij substituted.
  - MCF codim-2: similar tensor-polynomial basis.
  - Yamabe flow: conformal-class constrained.

- **Month 6**: Write-up. Either a validation-only paper (Month 4
  result + one extension) or, if Month 5 yields a novel functional,
  a focused paper on the new entropy.

### 5.6 Deliverables

1. `monoquant/tensor/` — tensor extension module (~3000 lines).
2. `monoquant/pdes/ricci_flow.py`, `mcf.py`, `kahler_ricci.py`.
3. `paper/mechanized_perelman_entropy_search.md`.
4. If Month 5 yields: a focused arXiv paper on the new monotone
   functional.

### 5.7 Risks

- **High probability**: the tensor-extension engineering takes 50%
  longer than estimated (6 months → 9 months total). This is the
  single biggest risk. Mitigation: recruit a second researcher for
  months 2-3.

- **Medium probability**: no new monotone functional found. Expected
  outcome is validation + 1-2 obstruction theorems.

- **Low probability**: the tool produces a formally-monotone
  functional that turns out to be known under another name (e.g.
  Huisken-Sinestrari for MCF at specific codimension). Mitigation:
  extensive literature review before publication.

- **Very low probability**: genuine novel Perelman-analogue found.
  This would be a major contribution to the field.

### 5.8 Honest novelty grading

- **Mathematics**: 5 / 10 (validation-only) to 9 / 10 (new Kähler-
  Ricci W-entropy).
- **Engineering**: 9 / 10 (first mechanized Ricci-flow symbolic
  engine).
- **Publication track**: if new: Invent. Math., Ann. Math., GAFA.
  If validation: J. Differential Geom., Comm. Math. Phys., or
  Adv. Math.

---

## Recommended sequencing

A realistic portfolio:

**Quarter 1 (months 1-3)**: Run plans 1 and 2 in parallel.
- Plan 1 ships in month 1 (KdV hierarchy). Stable, low-risk win.
- Plan 2 runs months 1-2 (fractional Burgers census).
- Outputs: 2 arxiv preprints, 1 Lean mathlib PR.

**Quarter 2 (months 4-6)**: Plan 3 (gKdV p=4).
- 3 months, either one new conservation law or a non-existence theorem.
- Uses infrastructure from plans 1 and 2.
- Outputs: 1 arxiv preprint.

**Quarter 3-4 (months 7-12)**: Plan 4 (full Keller-Segel) + Plan 5 start.
- Plan 4 requires (−Δ)⁻¹ support; ~3 months.
- Plan 5 tensor engine begins month 10, continues into year 2.

**Year 2**: Plan 5 completes.

Alternative: replace Plan 5 with a second iteration on Plans 2-4 to
find a higher-novelty yield. The moonshot of Plan 5 is the big prize
if the engineering completes cleanly.

---

## Budget and deliverables across all five plans

| Plan | Effort | Cost (researcher-months) | Output |
|------|--------|-------------------------|--------|
| 1 | 1 month | 1 | Lean mathlib PR + survey |
| 2 | 2 months | 2 | arXiv + census |
| 3 | 3 months | 3 | arXiv (new conservation OR non-existence) |
| 4 | 3 months | 3 | arXiv + Lyapunov map |
| 5 | 6 months | 6 | Mechanized geometric-flow tool + paper |
| **Total** | **15 months** | **15** | **5 papers + Lean PR + tool release** |

Across all five plans: **5 papers**, **1 mathlib PR**, **1 tensor-extended
tool**, **0 confirmed Clay-Millennium progress**. That last fact is
non-negotiable — none of these plans promises to solve NSE, Clay, or
any named unsolved open problem. They promise real, modest research
contributions in adjacent specialised areas.

The main ethical point: every plan in this document has been graded
honestly. Plan 1 is graded novelty 0/10. Plan 5 best-case is 9/10 but
most likely 5/10. No plan guarantees a major breakthrough. What all
plans guarantee is **mechanization of verification** — the piece of
mathematics infrastructure the AI era genuinely enables.

---

## Meta-plan: how to decide which to run

If the goal is **shortest time to a real artifact**: Plan 1.

If the goal is **best chance of a published paper**: Plan 2.

If the goal is **highest expected-value research impact**: Plan 3 (gKdV p=4).
Either outcome of Plan 3 is a real contribution.

If the goal is **ambitious moonshot with managed downside**: Plan 5
(Ricci flow). The downside is month 4 produces a validation-only
paper; the upside is potentially a genuinely novel entropy functional
that might influence the Ricci-flow / Kähler-Ricci community.

If unsure: **run Plan 1 first**. It produces a concrete artifact in 1
month and validates the tool chain. Then decide on subsequent plans
based on the Plan 1 experience.

---

*Written: iteration 4 post-extension, tool at v0.2.*
*Honest scope: contributions to specialised PDE infrastructure; not*
*a path to solving Clay-Millennium-tier open problems.*
