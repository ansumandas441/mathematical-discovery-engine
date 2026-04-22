# FINAL PORTFOLIO — Iter-4, 3D Navier–Stokes Global Regularity (Clay)

**Format.** Three-voice dialogue panel. **R**igorist / **P**ragmatist / **E**xpansionist.
**Inputs.** `ns_scout.md`, `mathematician_1_pde.md`, `mathematician_2_geometric.md`,
`mathematician_3_vocabulary.md`, `problem_solver_tests.md`, `integrity_audit.md`,
`philosopher_assessment.md`.
**Rule.** None of this session's output solves Clay. We do not pretend otherwise.
The portfolio converts 17 attack proposals + 4 new-technique nodes into a small,
honest shortlist plus a documented no-go ledger.

---

## §1 — Opening positions

**R (Rigorist).** My baseline count is 3. If I strip out everything the integrity
audit flagged BROKEN with no repair on the table, the portfolio collapses to three
technically survivable entries: **G4** (Type-II no-swirl self-similar exclusion),
**G5** (quantitative viscous damping of the Elgindi C^{1,α} profile), and **A4**
(mechanised Positivstellensatz + Lean search). Everything else is either a known
barrier-casualty, a known scaling-error, or a moonshot with no falsifiable 3-month
milestone. I am willing to entertain a narrowed G1 and M1.2 as probation cases,
but my prior is to ship 3 and stop.

**P (Pragmatist).** I disagree on size but agree on posture. A Clay-tier session's
job is not to ship theorems; it is to ship well-framed **attack strategies** (tier b),
**productive no-gos** (tier f), and **new technique nodes with life beyond NSE** (tier e).
By the philosopher's own six-tier accounting, this session produced 1 tier-(e) candidate
(B3), a substantial tier-(f) block via the barrier diagnostic, and 2-3 tier-(b)
attempts. I want the portfolio to reflect that honestly. My count is 5-6: the three
R would ship, plus G1-axi as a narrowed attack strategy, plus A4's companion
new-technique node B3, plus the documented barrier no-gos as a single diagnostic
entry. I'm with R on not inflating to hit a quota; I'm against R on treating
tier-(b) and tier-(e) as non-outputs.

**E (Expansionist).** I will lose this argument but I'll make it anyway. An honestly
labelled portfolio of 7 entries is better than a constricted portfolio of 3. We have
SP2 covered (G4), SP5 covered (M1.2), SP6 covered (G5), a Perelman-search meta-program
(A4) with a genuine new-technique node (B3), a narrowed geometric-depletion moonshot
(G1-axi), and a documented no-go ledger (M1.1-weight, G2-scaling, G3-Shkoller,
G6-Kuiper, M1.6-helicity). That is 6 portfolio entries plus 1 no-go ledger = 7 total,
each labelled at its real grade. If we cap at 4, we lose either the sub-problem
roadmap coverage or the technique-node output — both of which are the session's
strongest legitimate contributions.

**What we reject on sight.**
R: M1.1 (the log-weight tends to a constant, which the author's own formula shows on
inspection — the integrity audit ran the asymptotics), M1.3 (Lipschitz constant scales
as λ¹, not λ⁰ — X is not a critical space, so the Koch-Tataru framework the proposal
invokes does not apply), G2 (Φ_ν scales as λ¹ not λ⁵ — the Perelman-analogue framing
evaporates), G3 (Shkoller 1998 is about LANS-α, not NSE; NSE is not geodesic on
SDiff), G6 (Kuiper contractibility + analytic-estimate-rebranding horn).

P: Same five, plus M1.6 as an outright reject because the author confessed
BLOCKED-BY-BARRIER without a repair.

E: Same five. I'd argue M1.6 survives as a documented no-go but doesn't merit a
shortlist slot. We agree.

**The table is set.** 5 rejections before the per-proposal debate. 12 proposals +
4 B-nodes to adjudicate. We proceed.

---

## §2 — Per-proposal debate

Votes: **SHIP**, **REJECT**, **PARK-AS-SUBPROBLEM**, **PARK-AS-NEW-TECHNIQUE-NODE**.

### M1.1 — Logarithmically supercritical hyperdissipation

**R.** REJECT. Integrity audit's Step-1 asymptotic check: log g(r) = 2c·log(r)/log(2+r)
→ 2c, so g asymptotes to e^{2c} (constant). The proposal is α = 5/4 with ν rescaled,
not log-weaker. Claimed commutator log-gain is an independent failure: Kato–Ponce
gains one derivative, not a log.

**P.** Agree REJECT. Author's own failure-mode 1 flagged the commutator issue; the
audit goes further and breaks the formula itself.

**E.** REJECT, record as no-go: the particular log-correction route is arithmetically
closed.

Vote: **REJECT** (unanimous). Add to no-go ledger.

### M1.2 — Two-scale frequency envelope, Tao triple → double exponential

**R.** PARK-AS-SUBPROBLEM. Integrity audit: PASS-WITH-MINOR-FIXES. Author concedes
the barrier-escape claim is false (two-scale envelope is averaging-invariant). What
survives is a conditional quantitative sharpening on SP5. Per-level Carleman
multiplicativity question (Step 4) is a real open question, not fatal.

**P.** SHIP as sub-problem. Live community (Tao, Palasek, Barker–Prange,
Albritton–Barker).

**E.** SHIP. Philosopher's #4 dissertation pick.

Vote: **PARK-AS-SUBPROBLEM** (SP5 entry).

### M1.3 — Lipschitz-ξ critical space larger than BMO⁻¹

**R.** REJECT. Integrity audit: BROKEN on scaling. κ_λ = λ·κ (subcritical, a=+1),
not scale-invariant. X is not critical, so the Koch-Tataru framework does not apply.

**P.** The residue (Picard in subcritical X) is a different, smaller project. The
author's "larger critical Picard ball" framing is false.

**E.** REJECT. Step-5 bilinear estimate is the 20-year stuck step of Chae's
program. Even with scaling repaired, "do what Chae couldn't" is not a roadmap.

Vote: **REJECT** (unanimous). No-go ledger as scaling casualty.

### M1.4 — Perelman-candidate Φ = ∫|ω|² χ(ξ·e_max(S)) dx

**R.** SERIOUS-GAPS, moonshot-confessed. Integrity audit's Step-7 critique
decisive: "unforced NSE decays" is not pointwise; transient Burgers-type profiles
break unconditional monotonicity.

**P.** The differential gain is real — averaged NSE does not preserve pointwise
alignment ξ·e_max(S). Barrier-free in principle. The miracle at Step 6 and the
Burgers wall are the real obstacles.

**E.** PARK-AS-SUBPROBLEM of A4: the mechanised search would test this exact
candidate-form at degree ≥ 4. Don't ship standalone.

**R.** Agreed — collision #3 in problem solver's C.4.

Vote: **REJECT-AS-STANDALONE, absorbed into A4 candidate space**.

### M1.5 — Besov-ESS via frequency-blocked Carleman

**R.** Integrity audit: SERIOUS-GAPS at Step 5 (EKPV Carleman constants multiply,
not add, across dyadic scales). SP3 target is live.

**P.** Cheskidov–Luo 2022 falsifier (pre-check C.7 item 2) is the real threat.
Mandatory pre-check before investment.

**E.** Borderline ship. If CL-lift kills Besov-ESS, becomes a productive no-go.

Vote: **PARK-AS-SUBPROBLEM** with pre-check gate. Subsumed under SP3 in roadmap;
does not enter top-tier shortlist.

### M1.6 — Helicity-modified Koch–Tataru

**R.** REJECT. Author self-confesses BLOCKED-BY-BARRIER. Helicity-preserving
constraint on c(k,k₁,k₂) is linear; Tao's ball absorbs it.

**P.** Agree. Productive no-go: single conserved scalar cannot save critical-space
global regularity.

**E.** Agree.

Vote: **REJECT** (unanimous). No-go ledger entry.

### G1 — Constantin–Fefferman Osgood feedback on κ = ‖∇ξ‖_{L^∞(Ω_M)}

**R.** Uneasy. Integrity audit: SERIOUS-GAPS. ∇P_{ξ^⊥} self-coupling gives p=2
(super-linear), not sub-linear. Threshold M unspecified. Osgood p<1 is hoped,
not derived.

**P.** The narrowed version (axi-with-swirl) is a different object. Problem solver
top-3; philosopher's #3 dissertation pick. Biot–Savart has more structure there;
Hou-Lei-Li and Palasek are active.

**E.** SHIP narrowed. 1-3 month calculation: if κ-feedback p<1, extension of
Chae-Lee 2002 and CSTY 2008. If p≥1, documented no-go on SP-axi.

**R.** Conditional ship, contingent on quadratic self-coupling cancellation check
in axi-swirl.

Vote: **PARK-AS-ATTACK-STRATEGY (narrowed)**. Shortlist as G1-axi, with
mandatory pre-check on the self-coupling cancellation.

### G2 — ν-weighted W-entropy Perelman analogue Φ_ν

**R.** REJECT. BROKEN scaling (audit + philosopher §3): Φ_ν ∼ λ¹ (subcritical),
not λ⁵. What remains is weighted enstrophy, known not monotone in 3D since
Constantin–Foias 1988.

**P.** Deeper mismatch: NSE is not a gradient flow; Perelman's W is *forced* by
Ricci flow's gradient-flow structure.

**E.** REJECT. No-go lesson: Perelman-analogue cannot be constructed by
weighted-enstrophy ansätze.

Vote: **REJECT** (unanimous). No-go ledger, scaling casualty.

### G3 — Arnold/Khesin SDiff curvature + Bochner

**R.** REJECT. Three independent failures: (i) NSE is not geodesic on SDiff; only
Euler is (author's failure-mode 4 admits). (ii) Shkoller 1998 citation is for
LANS-α, not NSE — misattribution. (iii) Bochner on infinite-dim SDiff is formal;
Ricci is not rigorously established.

**P.** 60-year negative empirical prior; curvature is mixed-sign and negative
sections dominate turbulent directions.

**E.** No-go note: do not restart without a new geometric ingredient.

Vote: **REJECT** (unanimous). No-go ledger with Shkoller + NSE-not-geodesic
clarifications.

### G4 — Type-II self-similar no-swirl axisymmetric exclusion

**R.** SHIP. Integrity audit: PASS-WITH-MINOR-FIXES. Gaps are research gaps
(Jia–Šverák 2014 is forward-self-similar, backward adaptation non-trivial), not
integrity failures. Targets SP2.

**P.** SHIP. Philosopher's #1 dissertation pick. Live community.

**E.** SHIP. Most-confident entry.

Vote: **SHIP** (targets SP2).

### G5 — Quantitative viscous damping against the Elgindi C^{1,α} profile

**R.** SHIP. Integrity audit: PASS-WITH-MINOR-FIXES. Well-posed spectral question;
expected answer is "yes NSE damps Elgindi Euler". Value is making ν★(α)
quantitative.

**P.** SHIP with literature-scan caveat (Elgindi/Jeong/students may have already
done it).

**E.** SHIP. Targets SP6.

Vote: **SHIP** (SP6, with literature-scan caveat).

### G6 — Obstruction-class cohomology

**R.** REJECT. BROKEN by contractibility. M is a Banach ball; linear homotopy
h(t,u) = tu kills topological characteristic classes. Analytic sheaves rebrand
known estimates.

**P.** Session's clearest tier-(d) block.

**E.** REJECT.

Vote: **REJECT** (unanimous). No-go ledger entry.

### A1 — Zero-noise-limit pathwise Otto Wasserstein action

**R.** REJECT. Core premise (NSE admits Otto gradient-flow structure on vorticity)
is unsupported and likely false. Author's failure-mode 1 concedes collapse to
ν∫|∇u|².

**P.** Retain as diagnostic exercise under B2.

**E.** Agree.

Vote: **REJECT-AS-ATTACK-STRATEGY, absorbed into B2 diagnostic**.

### A2 — Regularity-structures reclassification

**R.** REJECT. BPHZ-for-Leray-NSE feasibility unsupported. Author concedes
averaging-invariance.

**P.** Fallback (sharpen Koch-Tataru) also has no mechanism.

**E.** Agree.

Vote: **REJECT** (unanimous). Unsupported proposal, not a no-go discovery.

### A3 — Furstenberg-ergodic statistical regularity lift

**R.** REJECT. Circularity (finite-dim 3D attractor is Clay-adjacent) +
Furstenberg requires measure-preservation (NSE is dissipative) + f→0 vacuity
for unforced.

**P.** Forced-statistical sub-version is saturated by Hairer–Mattingly.

**E.** Agree.

Vote: **REJECT** (unanimous).

### A4 — Mechanised Positivstellensatz + Lean monotone-quantity search

**R.** SHIP. PASS-WITH-MINOR-FIXES. Minimum-viable-enumeration (Python/SymPy +
SDP at D=4) is publishable either way.

**P.** SHIP. Philosopher's #1 tier-(e) pick. Only cross-disciplinary proposal.

**E.** SHIP. Must-include with B3 as pair.

Vote: **SHIP as attack-strategy + new-technique-node** (A4 + B3 pair).

### A5 — Fisher information of |ω|²

**R.** REJECT standalone. Stretching contribution has bad sign on Hou-Luo /
Chen-Hou regime (Chae wall). Scaling exponent disputed (audit: a=-3/2; problem
solver: a=-5/2).

**P.** Absorb into A4 candidate space.

**E.** Agree.

Vote: **REJECT-AS-STANDALONE, absorbed into A4 candidate space**.

### B1 — `t_renormalization_group_flow_with_blowup_profile`

**R.** Philosopher grades harder: "essentially the Bricmont–Gawędzki–Kupiainen
template." Bookkeeping novelty.

**P.** Ship as NEW-GENUINE at composite level; the dynamical-systems self-map +
spectral analysis of dR is not in a single parent.

**E.** SHIP with honest composite label.

Vote: **PARK-AS-NEW-TECHNIQUE-NODE**.

### B2 — `t_wasserstein_gradient_flow_with_nonlinear_transport`

**R.** Weakest of the four B-nodes. Already in Carrillo-McCann-Villani.

**P.** Include only as HONEST-RESTATEMENT with cross-reference.

**E.** Concede. Secondary composite, honest labelling.

Vote: **PARK-AS-NEW-TECHNIQUE-NODE, labelled as repackaging**.

### B3 — `t_mechanized_monotone_quantity_search`

**R.** SHIP. Three-auditor convergence on NEW-GENUINE. No precedent for the
composite (invariant-enumerate + symbolic-d/dt + SDP + Lean certify). Value
independent of Clay: applicable to Ricci, MCF, compressible Euler, Schrödinger,
KdV.

**P.** SHIP, strongest tier-(e) entry.

**E.** SHIP.

Vote: **SHIP as NEW-TECHNIQUE-NODE** (A4 companion).

### B4 — `t_zero_noise_limit_with_preserved_regularity`

**R.** Moderate. NEW-GENUINE; named in SPDE literature (FGP and successors).
A1's NSE failure slightly weakens the case.

**P.** Ship with "applicable to SPDE generally; NSE-unclear" labelling.

**E.** SHIP.

Vote: **PARK-AS-NEW-TECHNIQUE-NODE** with applicability caveat.

### Tally after debate

- **SHIP**: G4, G5, A4, M1.2 (as sub-problem), G1-axi (narrowed), B3
- **PARK-AS-NEW-TECHNIQUE-NODE**: B1, B2, B4 (honestly-graded, composite labels)
- **REJECT**: M1.1, M1.3, M1.6, G2, G3, G6, A2, A3
- **REJECT-AS-STANDALONE, ABSORBED**: M1.4 → A4; M1.5 → SP3 pre-check; A1 → B2
  diagnostic; A5 → A4 candidate space

---

## §3 — The shortlist

Seven entries. Attack strategies + sub-problems + new-technique nodes + one no-go
ledger. Ordered by panel confidence and dissertation-feasibility.

### Entry 1 — G4 / Type-II self-similar exclusion (no-swirl axisymmetric NSE)

- **Type**: SUB-PROBLEM (doubles as ATTACK-STRATEGY for SP2).
- **Target sub-problem**: SP2 (ruling out Type-II self-similar blowup for
  axisymmetric NSE).
- **Summary.** Sharpen Nečas–Růžička–Šverák 1996 (Type-I exclusion for
  self-similar Leray profiles) to a Type-II exclusion under the no-swirl axisymmetric
  restriction. Rescale a hypothetical Type-II blowup at rate (T−t)^{−α}, α < 1/2;
  extract a weak-∗ limit ancient profile; combine Koch–Nadirashvili–Seregin–Šverák
  2009 Liouville (bounded axisymmetric NS ancient solutions trivial under
  ω^θ/r-boundedness) with Chen–Strain–Tsai–Yau 2008 (ω^θ/r a priori bound from
  transport in the no-swirl sector) to force the profile to zero, contradicting
  non-triviality.
- **Dissertation-feasibility**: 3-5 year dissertation. Standard.
- **Required pre-checks**. (i) Verify Jia–Šverák 2014's discretely-self-similar
  machinery (which was set up for the forward-self-similar / initial-value problem)
  adapts to the backward / blowup-profile direction — the integrity audit flags this
  as non-trivial and not flagged by the problem solver. (ii) Check that KNSŠ 2009
  Liouville hypotheses (decay at infinity) hold on the Type-II profile as modulated
  by the periodic-in-τ function that accompanies discrete self-similarity.
- **Panel grade**: **RIGOROUS-SUB-PROBLEM-CANDIDATE**.
- **Panel verdict**. Highest-confidence entry in the portfolio. Integrity audit
  PASS-WITH-MINOR-FIXES; philosopher's #1 dissertation pick; live research
  community. Publishable on SP2 frontier whether the full Type-II exclusion closes
  or only a subclass.
- **Edge cases / failure modes**. If a Type-II profile exists outside
  KNSŠ's hypothesis class (e.g., non-decaying at infinity), the exclusion misses
  it; no-swirl sector is the only tractable piece and does not generalise to swirl
  by this method.

### Entry 2 — A4 / Mechanised Positivstellensatz + Lean monotone-quantity search

- **Type**: ATTACK-STRATEGY (meta-level) + companion NEW-TECHNIQUE-NODE B3.
- **Target sub-problem**: directly targets Axis 11 (Perelman-analogue); also
  produces tier-(d) obstruction theorems at each degree.
- **Summary.** Enumerate SO(3)×translation×scaling-invariant polynomial
  functionals in jet variables ∂^α u up to degree D and order k under a fixed
  (supercritical or critical) scaling weight. For each candidate Φ, symbolically
  compute dΦ/dt under NSE + divergence-free + Leray projection + integration by
  parts, reducing to a polynomial Q in pointwise derivative invariants. Call an
  SDP Positivstellensatz solver on Q ≤ 0. Outputs either (i) a candidate monotone
  Φ certified by SDP + manual Lean proof, or (ii) a formally verified "no such
  Φ exists at this (D, weight, k)" obstruction theorem. Minimum viable scope:
  Python/SymPy + SDP at degree 4, no Lean certification (3-6 months). Full Lean
  integration is a 2-3 year stretch.
- **Dissertation-feasibility**: 1-3 year post-doc / 3-5 year dissertation depending
  on Lean ambition. Minimum-viable-enumeration path is post-doc-scale.
- **Required pre-checks**. (i) Engineering: symbolic engine for NSE + IBP must
  handle Leray projection cleanly (pressure-non-local terms are outside the
  standard SOS template). (ii) Scoping: ensure the scan flags Φ that are
  ν-independent, so outputs can be tested for Chen-Hou consistency (any Φ monotone
  under Euler at ν=0 contradicts Chen-Hou 2025). (iii) Combinatorial scaling at
  D ≥ 5 is a real concern; scope should start at D = 2 (to recover 2D enstrophy
  as a sanity check) then D = 3, 4.
- **Panel grade**: **GENUINE-NEW-TECHNIQUE-NODE** for the companion B3, plus
  **SPECULATIVE-BUT-STRUCTURALLY-COHERENT** for A4 as an attack strategy.
- **Panel verdict**. Philosopher's #1 in tier-(e) novelty and the only
  cross-disciplinary proposal (computational algebra × PDE × formal verification)
  in the session. Value is independent of Clay: applicable to Ricci flow (would
  re-derive Perelman W as a specific output if the basis includes curvature
  scalars), MCF, compressible Euler, Schrödinger, KdV.
- **Edge cases / failure modes**. Combinatorial explosion at D ≥ 5; Perelman's
  original W is degree 2 in curvature but degree ≈ 4 in the metric, so an NSE
  analogue may live at D ≥ 6-8 where the search is infeasible. Negative output
  at D = 4 is still publishable as an obstruction theorem.

### Entry 3 — G1-axi / Lipschitz-ξ Osgood feedback on axisymmetric-with-swirl NSE

- **Type**: ATTACK-STRATEGY (narrowed moonshot).
- **Target sub-problem**: axisymmetric-with-swirl NSE global regularity (the
  simplest still-open 3D NSE sector).
- **Summary.** On axisymmetric-with-swirl NSE, compute the Osgood-type feedback
  on κ(t) = ‖∇ξ‖_{L^∞(Ω_M)}, where ξ = ω/|ω| and Ω_M = {|ω| ≥ M}. The claim is
  that viscous smoothing in the ξ-evolution equation (via the P_{ξ^⊥}(Δω) term)
  produces a sub-linear feedback κ(t) ≤ C_ν ∫₀ᵗ κ(s)^p ds with p < 1, forcing
  Osgood closure and preventing blowup of κ — which by Constantin–Fefferman's
  BKM-depletion would prevent NSE blowup in the axi-with-swirl sector.
- **Dissertation-feasibility**: 3-5 year dissertation, with a 1-3 month pre-check
  that determines whether the project is viable.
- **Required pre-checks**. (i) Compute explicitly the self-coupling quadratic
  term from ∇P_{ξ^⊥} in the ∇ξ-evolution (integrity audit Step 2 gap); in general
  3D this contributes a |∇ξ|² feedback (p = 2, super-linear). Axi-with-swirl may
  have a cancellation by symmetry — this must be verified, not assumed. (ii) Specify
  the threshold M(t) as a function of sup|ω|(t) and verify Biot–Savart singular-integral
  estimates on Ω_M. (iii) State a non-vanishing-ω hypothesis on a neighbourhood
  of the candidate concentration set. If the quadratic self-coupling does not
  cancel in axi-with-swirl, the project is dead at pre-check.
- **Panel grade**: **WELL-DEFINED-ATTACK-STRATEGY** if pre-check passes;
  **PRODUCTIVE-NO-GO** on SP-axisymmetric if pre-check fails.
- **Panel verdict**. Problem solver's C.5 top-3; philosopher's #3 dissertation
  pick. Narrowed to an accessible sub-problem of Chae's 20-year-stuck bilinear
  program; the narrowing exploits the extra Biot–Savart structure of the axi-swirl
  sector. Win either way: Osgood closure = extension of Chae-Lee 2002 and
  CSTY 2008; failure = documented concrete obstruction.
- **Edge cases / failure modes**. The quadratic self-coupling from ∇P_{ξ^⊥} is
  the most likely killer; if it does not cancel in axi-swirl by symmetry, the
  entire Osgood programme for axi-swirl is dead. Hou-Luo numerical scenario is
  precisely the kind of profile this would need to tame.

### Entry 4 — M1.2 / Quantitative ESS: triple → double exponential

- **Type**: SUB-PROBLEM (conditional quantitative sharpening).
- **Target sub-problem**: SP5 (Tao 2019 quantitative-bound sharpening).
- **Summary.** Replace one of the three stacked compactness/Carleman steps in
  Tao 2019's triple-exponential bound ‖u(t)‖_{H^k} ≤ exp(exp(exp(A^c))) — where
  A = ‖u‖_{L^∞_t L³_x} — with an O(log A) counting argument via a two-scale
  frequency envelope tracking ‖Δ_{N_low} u‖ and ‖Δ_{N_high} u‖ at a dyadic distance
  k(t) = log₂(N_high/N_low) with k = O(log A). Net: ‖u(t)‖_{H^k} ≤ exp(exp(A^c)).
  Palasek 2022 achieved single-exponential in the axi-symmetric sector; this
  proposal targets double-exponential for general data.
- **Dissertation-feasibility**: 3-5 year dissertation (strong harmonic analysis
  background required).
- **Required pre-checks**. (i) Multi-modal profile handling: k(t) definition
  fails on profiles with multiple dyadic peaks (integrity audit Step 2). Repair
  to k(t) = min{k : max_{j ≥ k} ‖Δ_{N_low·2^j} u‖_{L²} ≤ ‖Δ_{N_low} u‖_{L²}/2}.
  (ii) Rigorous accounting of per-level Carleman constant iteration across k dyadic
  levels. Tao 2019's Prop. 5.9 has per-level constants that may multiply, not add;
  if they multiply, the two-scale envelope does not remove an exponential
  (integrity audit Step 4).
- **Panel grade**: **RIGOROUS-SUB-PROBLEM-CANDIDATE**.
- **Panel verdict**. Integrity audit PASS-WITH-MINOR-FIXES. Author honestly
  concedes the barrier-escape claim (the two-scale envelope uses only scalar LP
  norms, averaging-invariant). Value is sub-Clay only; does not touch unconditional
  global regularity. Live community (Tao, Palasek, Barker–Prange, Albritton–Barker).
- **Edge cases / failure modes**. Per-level Carleman multiplicativity is the
  gating question; if constants multiply, the gain is illusory and the paper
  does not improve Tao 2019.

### Entry 5 — G5 / Quantitative viscous damping of the Elgindi C^{1,α} profile

- **Type**: SUB-PROBLEM (Euler→NSE damping, non-smooth regime).
- **Target sub-problem**: SP6 (NSE-analogue of Chen–Hou-style Euler blowup).
- **Summary.** Take Elgindi's 2021 C^{1,α} axisymmetric-no-swirl Euler
  self-similar blowup profile. Linearise L_{Elg} around it, add νΔ, and compute
  the spectrum of L_{Elg} + νΔ in an appropriate weighted functional-analytic
  setting. Target output: ν★(α) such that for ν > ν★(α), the unstable direction
  of L_{Elg} is stabilised by νΔ. Publishable as "NSE damps Elgindi-type Euler
  blowup for any ν > 0 with quantitative ν★(α)".
- **Dissertation-feasibility**: 1-3 year post-doc work. Clean spectral perturbation.
- **Required pre-checks**. (i) Specify the functional-analytic setting (weighted
  L² or Hölder; C^{1,α} is on the boundary of standard spectral theory). (ii)
  Verify that L_{Elg} has a discrete spectrum in that setting (continuous
  spectrum would complicate eigenvalue-based stability). (iii) **Literature scan:
  check whether Elgindi, Jeong, or their students have already done this.** The
  philosopher flags real uncertainty here; if the spectral perturbation is
  already in a preprint, G5 drops out of the dissertation ranking.
- **Panel grade**: **RIGOROUS-SUB-PROBLEM-CANDIDATE** if literature scan clears;
  **HONEST-RESTATEMENT-OF-KNOWN-APPROACH** if the spectral analysis already
  exists.
- **Panel verdict**. Integrity audit PASS-WITH-MINOR-FIXES. Clean post-Elgindi +
  Chen-Hou question. Does not touch Clay (Elgindi mechanism vanishes at C^∞
  data; Clay requires C^∞); honest SP6 contribution.
- **Edge cases / failure modes**. Duplicate-work risk via literature scan.
  Eigenvalue might depend non-trivially on ν without sign flip, giving no clean
  ν★(α). Spectral analysis of a degenerate-at-blowup operator can be delicate
  in the C^{1,α} functional setting.

### Entry 6 — B3 / `t_mechanized_monotone_quantity_search` (new technique node)

- **Type**: NEW-TECHNIQUE-NODE.
- **Target**: graph-level contribution; not NSE-specific.
- **Summary.** A composite technique whose signature is
  (evolution PDE + invariant-polynomial basis + target scaling weight) →
  (Positivstellensatz certificate of monotonicity, or formally verified no-go
  theorem). Composes `t_formal_verify` + `t_finite_case_check` +
  `t_polynomial_method` + `t_conserved_quantity`; not reducible to any single
  parent. The distinctive composite pattern is: symmetry-invariant enumeration of
  a search space + symbolic time-derivative engine + SDP Positivstellensatz +
  (optional) Lean certification. Provides a mechanised "find a monotone Φ for
  this evolution PDE" service.
- **Dissertation-feasibility**: companion to A4. Infrastructure is re-usable across
  Ricci flow, MCF, compressible Euler, Schrödinger, KdV, so the node has
  beyond-NSE life regardless of whether A4 closes any specific question.
- **Required pre-checks**: same as A4.
- **Panel grade**: **GENUINE-NEW-TECHNIQUE-NODE**.
- **Panel verdict**. Strongest tier-(e) deliverable of the session. Philosopher:
  "the one [new technique node] I'd insist on adding." Integrity audit: NEW-GENUINE
  at composite level. No single named precedent in the literature.
- **Edge cases / failure modes**. Provisional until first firing; if the
  infrastructure never produces an interesting positive or negative output on any
  PDE at D ≥ 4, the composite is a structural curiosity rather than a working
  technique.

### Entry 7 — No-go ledger (consolidated)

- **Type**: NO-GO-DIAGNOSTIC (consolidated entry).
- **Target**: meta-level — documents where NOT to spend effort, by integrated
  finding.
- **Summary.** Six independent no-gos the session identified, each with a
  specific future-worker lesson:
  - **M1.1**: g(r) = r^{2c/log(2+r)} asymptotes to the constant e^{2c}. The
    proposed "log-weaker than Tao" dissipation is actually α = 5/4 with ν rescaled.
    Paraproduct commutator gains one derivative, not a log. Lesson: log-correction
    hierarchies below Tao 2009 are not reachable by commutator estimates alone;
    any route must supply the log-gain by a genuinely new multiplier theorem.
  - **G2**: Φ_ν = ∫(|ω|² + λν|∇u|²) e^{-φ} dx scales as λ¹ (subcritical), not λ⁵.
    The Perelman-analogue framing evaporates; what remains is weighted enstrophy,
    known not monotone in 3D since Constantin–Foias 1988. Lesson: a
    Perelman-analogue for NSE cannot be constructed by weighted-enstrophy ansätze.
    A new structural principle is required.
  - **G3 (and Shkoller misattribution)**: NSE is not a geodesic flow on SDiff;
    only Euler is. The Shkoller 1998 citation the proposal used is about LANS-α
    (Camassa-Holm-regularised NSE), a different equation. Bochner on infinite-dim
    SDiff is formal. Lesson: the Arnold-geometric program for 3D NSE regularity
    has a structural mismatch (NSE is not geodesic) compounding its 60-year
    negative-prior. Do not restart without a new structural ingredient that
    makes νΔu geometrically interpretable.
  - **G6**: topological obstruction classes cannot work on a contractible
    initial-data manifold — the linear homotopy h(t,u) = tu kills any topological
    characteristic class. Analytic sheaves collapse to rebrandings of known
    analytic estimates. Lesson: topological/sheaf-cohomological formulations of
    the Clay problem add no content. The dichotomy (topological: trivial by
    contractibility; analytic: rebranding) is clean.
  - **M1.6**: single conserved scalar (helicity) cannot save critical-space global
    regularity; Tao's averaging admits a modification preserving the helicity
    linear constraint on c(k,k₁,k₂) while retaining blowup. Lesson: the barrier
    extends to single-scalar invariants; multi-scalar or geometric-pointwise
    ingredients are needed.
  - **M1.4 author-confession (absorbed into A4 + Burgers-vortex check)**: the
    alignment-weighted Φ cannot be unconditionally monotone because transient
    Burgers-vortex-type profiles in unforced NSE admit finite-interval dΦ/dt > 0.
    Lesson: any Perelman-analogue Φ must either accept conditional monotonicity,
    or replace the alignment weight by something vanishing on Burgers-type
    profiles.
- **Dissertation-feasibility**: not applicable; this is a negative ledger.
- **Required pre-checks**: none.
- **Panel grade**: **PRODUCTIVE-NO-GO** (consolidated).
- **Panel verdict**. The session's most frequent legitimate output by volume.
  None of these no-gos is a Clay dent, but each saves a future worker 1-12 months
  of re-derivation.
- **Edge cases / failure modes**. None — a no-go ledger is maintained, not ranked.

---

## §4 — Sub-problem roadmap

The scout identified seven tractable sub-problems (SP1–SP7). Coverage assessment:

- **SP1** (uniqueness of Leray–Hopf for unforced NSE). **Orphan.** No proposal
  in the session addressed SP1. Forced case is closed negatively
  (Albritton–Brué–Colombo 2022); the unforced companion is the nearest sub-target
  to actual Clay. No-one in the session picked it up. Recommended for iter-5.
- **SP2** (ruling out Type-II self-similar blowup for axisymmetric NSE).
  **Covered by Entry 1 (G4)**, no-swirl sector. Swirl sector remains open and
  is a natural follow-on after no-swirl.
- **SP3** (extending ESS L^∞_t L³_x to wider critical spaces). **Partially covered
  by M1.5** (Besov-ESS), which did not make the shortlist but exists as a
  sub-problem pre-check (Cheskidov–Luo 2022 lift test). A focused SP3 attack
  remains open.
- **SP4** (hyperdissipative α < 5/4). **Orphan after M1.1 rejection.** The one
  attack failed the arithmetic check. SP4 is a live frontier and a future worker
  could try again with a genuine (not self-cancelling) log-correction.
- **SP5** (quantitative bound sharpening). **Covered by Entry 4 (M1.2)**.
- **SP6** (rigorous blowup for axisymmetric NSE with ν > 0). **Covered obliquely
  by Entry 5 (G5)**, which asks the complementary question (does viscosity
  stabilise the Elgindi Euler profile). A direct SP6 attack (construct a blowup)
  remains open and is what Chen–Hou 2025 did for Euler.
- **SP7** (unique continuation, forward in time). **Orphan.** No proposal
  addressed SP7.

**Coverage score: 3.5 / 7.** Three sub-problems are clearly covered (SP2, SP5,
SP6-adjacent via G5), one partially (SP3 via a pre-check), three orphaned
(SP1, SP4, SP7).

**Recommended 2-year research program ordering** for a small team using this
session's outputs:

1. **Month 0-3**: A4 minimum-viable-enumeration at D = 2 (sanity-check: recovers
   2D enstrophy), then D = 3, 4. This produces either a candidate monotone Φ
   (unlikely at D ≤ 4 but publishable if found) or an obstruction theorem
   (guaranteed publishable). Uses B3 as the technique template.
2. **Month 0-3 in parallel**: G1-axi pre-check (quadratic self-coupling cancellation
   on axi-with-swirl). Either proceeds to the full κ-Osgood calculation
   (months 3-24) or is documented as a no-go.
3. **Month 0-24**: G4 full derivation (extend KNSŠ Liouville from bounded to
   Type-II profiles in no-swirl axisymmetric). Low-risk; clear sub-problem.
4. **Month 0-12, literature-gated**: G5 spectral perturbation after literature
   scan. If clear, 1-year post-doc project.
5. **Month 12-36**: M1.2 quantitative sharpening. Strong harmonic analysis
   background required; not a starter project.
6. **Future iterations (iter-5 onward)**: SP1 and SP7 as orphan targets; SP4 with
   a new log-correction mechanism.

---

## §5 — No-gos documented

Five no-gos plus one author-confession, each converted into a specific
future-worker instruction:

- **M1.1 / fake log-weight.** g(r) = r^{2c/log(2+r)} → e^{2c}; the Fourier
  multiplier |ξ|^{5/2}/g(|ξ|) is indistinguishable (up to a ν-rescaling) from
  the Tao 2009 α = 5/4 dissipation. **Lesson**: if you want to push below Tao's
  log-threshold with a specific weight g, first check the asymptotic behaviour
  of log g(r) before building a PDE argument on it. In combination with the
  independent failure of the claimed commutator log-gain (Kato–Ponce gives one
  derivative, not a log), M1.1's route is closed. Any future attack on SP4 has
  to supply the log-gain via a genuinely new multiplier theorem, not by citing
  standard commutator bounds.

- **G2 / scaling error (λ¹ not λ⁵).** The functional Φ_ν = ∫(|ω|² + λν|∇u|²)e^{-φ}dx
  has all three terms scaling: |ω|² ∼ λ⁴, |∇u|² ∼ λ⁴, dx ∼ λ⁻³, and the dimensionless
  Gaussian e^{-φ} is λ⁰. Product ∼ λ¹, subcritical. **Lesson**: a
  Perelman-analogue for NSE is not reachable by weighted-enstrophy ansätze. The
  deeper structural point (per philosopher §3) is that NSE is not a gradient
  flow of any known functional, whereas Perelman's W is *forced* by Ricci-flow's
  gradient-flow structure. The analogy breaks at the load-bearing step. Future
  workers searching for a Perelman-analogue must either (a) accept a different
  structural principle (e.g., non-gradient-flow monotonicity framework), or (b)
  abandon the framing.

- **G3 / Shkoller misquote + NSE-not-geodesic.** Two distinct errors. (i) NSE is
  not a geodesic flow on SDiff(Ω); only Euler is. The νΔu term is not of
  geodesic-with-friction form (integrity audit, confirmed by Ebin-Marsden 1970's
  original framing). (ii) The cited Shkoller 1998 paper is about LANS-α (a
  Camassa-Holm-regularised NSE), not NSE itself. **Lesson**: the
  Arnold-Khesin-geometric program for NSE regularity compounds a 60-year
  negative empirical prior with a structural mismatch. Do not restart without
  a new geometric ingredient that makes νΔu intrinsically interpretable in the
  SDiff framework. The Shkoller citation should not be used as an NSE reference;
  it is LANS-α-specific.

- **G6 / Kuiper-contractibility kill.** The initial-data manifold M is a ball
  in a Banach space, hence contractible via the linear homotopy h(t,u) = tu.
  Contractibility trivialises any topological characteristic class; you do not
  even need Kuiper's theorem for U(H) — linearity of the space suffices. The
  complementary horn (analytic sheaves on M) reduces to rebranding known
  analytic estimates in cohomological language; no new content. **Lesson**:
  topological or sheaf-cohomological formulations of Clay add nothing. The
  dichotomy is clean and decisive.

- **M1.6 / helicity-modified Koch-Tataru.** Helicity is a single scalar invariant;
  the constraint on Tao's averaging symbol c(k,k₁,k₂) to preserve helicity is
  linear. Tao's bilinear |c| ≤ 1 ball has room to absorb it, so a
  helicity-preserving averaged NSE still admits the 2014 cascade-hollow blowup.
  **Lesson**: the supercritical barrier extends to single-scalar-invariant
  extensions of the BMO⁻¹ Picard framework. To escape, one needs either a
  multi-scalar invariant system or a geometric-pointwise ingredient (Constantin–Fefferman
  direction, alignment ξ·e_max(S), etc.).

- **M1.4 author-confessed modified-KT barrier / Burgers-vortex wall.** The
  alignment-weighted Φ cannot be unconditionally monotone because transient
  Burgers-vortex-type profiles in unforced NSE admit finite-interval dΦ/dt > 0.
  **Lesson**: a Perelman-analogue Φ candidate in the polynomial-invariant space
  must either (a) be vanishing on all Burgers-type transients, or (b) accept
  conditional monotonicity. This constraint should be coded into A4's search
  (exclude Φ that fail the Burgers-vortex test) and into any standalone
  Perelman-analogue attempt.

All five (plus the Burgers-wall) now enter the no-go ledger as Entry 7 of the
shortlist. Collectively they represent the session's highest-volume legitimate
output.

---

## §6 — Did the graph help?

**R.** The honest answer is mostly no, with two qualifications. The philosopher
is right that a Vicol/Seregin/Tao/Šverák-level expert solo in a week would produce
a list strongly overlapping with this session's output: Constantin-Fefferman
direction, Perelman-analogue, Type-II self-similar, quantitative ESS,
axisymmetric-with-swirl, hyperdissipative α<5/4, convex integration, Arnold
geometry, Elgindi viscous damping, SPDE regularization, Fisher depletion,
helicity, Besov criteria. Every M1.x / G1-G5 / A1, A3, A5 is in this expert-generated
list. The graph did not generate novelty beyond the expert's mental map.

**P.** R is understating the qualifications. The graph enforced two valuable
features no expert survey does reliably: (i) a mandatory barrier-check on every
proposal, which produced the explicit tagging of M1.6 BLOCKED, A2 BLOCKED, G6
BLOCKED that an expert survey would typically leave implicit; (ii) explicit
technique-tagging that made cross-proposal collisions visible (Collision #3:
A4 subsumes M1.4 and G2 as search-targets — this observation requires technique-
level tagging to surface cleanly). Neither feature adds mathematical content,
but both add structure and honesty.

**E.** And there is the one genuinely novel item: A4 + B3. The philosopher
flagged that A4 is the only proposal that "crosses out of the target problem's
native discipline into a neighbor's tooling" — computational algebra (SOS /
Positivstellensatz) + formal verification (Lean mathlib) + PDE target (Perelman
search). That cross-disciplinary combination did not come from a PDE-expert's
mental map; it came from having all three clusters explicitly in the technique
graph and combining them. The graph added value there.

**R.** Conceding partial value. The graph's value is:
  - in (a) tier-f barrier-filtering (the no-gos documented in §5 all emerged from
    the diagnostic);
  - in (b) tier-e cross-cluster combination (A4 + B3 specifically);
  - in (c) organizational structure that makes repackaging flags visible
    (B1, B2's honest grading).

The graph's failure modes are:
  - inside pure PDE, where graph technique IDs are labels not proof schemas,
    they contribute no derivation content (M1.4's use of `t_conserved_quantity`
    label does not help construct χ);
  - in sparse cases, cross-cluster combinations produced A1 (collapse to
    dissipation likely), A3 (circularity), A2 (averaging-invariant) — more failed
    combinations than successes.

**P.** Quantify: of 5 cross-cluster attempts (A1, A2, A3, A4, A5), only A4 is a
genuine success. That is a 20% hit rate. For a method billed as "discovery via
combination," 20% is modest; for a method billed as "structured survey with
honesty checks," 20% is a bonus on top of the main deliverable.

**E.** Fair. The honest verdict: the graph is an organization + honesty amplifier,
not a discovery engine. Its iter-4 dividend was A4 + B3 + a cleaner no-go ledger.
Its iter-4 cost was the saturation issue the philosopher flags (NSE is
over-saturated with known attack axes; the graph mostly rediscovered the expert
landscape). The method works best in cross-disciplinary seams and loses
efficiency in pure-native-discipline work.

**Consensus.** The graph added value in three specific ways (barrier-filtering,
cross-cluster combination A4, repackaging-flagging). It did not add value inside
pure PDE analysis. A Vicol/Tao-solo would have produced higher technical depth
with lower coverage systematicity and no barrier-filter; the session produced
lower per-proposal depth with higher coverage + mandatory rigor checks. The
structure-and-honesty dividend is real but modest.

---

## §7 — Closing reflection — what we actually produced

**Grade distribution of the shortlist.**

| Entry | Grade |
|---|---|
| 1. G4 | RIGOROUS-SUB-PROBLEM-CANDIDATE |
| 2. A4 + B3 | SPECULATIVE-BUT-STRUCTURALLY-COHERENT + GENUINE-NEW-TECHNIQUE-NODE |
| 3. G1-axi | WELL-DEFINED-ATTACK-STRATEGY (conditional on pre-check) |
| 4. M1.2 | RIGOROUS-SUB-PROBLEM-CANDIDATE |
| 5. G5 | RIGOROUS-SUB-PROBLEM-CANDIDATE (conditional on literature scan) |
| 6. B3 | GENUINE-NEW-TECHNIQUE-NODE (counted with A4) |
| 7. No-go ledger | PRODUCTIVE-NO-GO (consolidated, 6 items) |

**Honest final count.** 3 attack strategies (G4 targets SP2; A4 targets
Axis-11 / Perelman-search; G1-axi targets axisymmetric-with-swirl) + 2 pure
sub-problems (M1.2 on SP5, G5 on SP6) + 1 new-technique node (B3, with B1/B2/B4
as secondary composites in the back-pocket) + 1 consolidated no-go ledger
(6 individual no-gos) = **7 total portfolio entries**.

Distribution check against R's opening position of 3: R wanted to ship only G4,
G5, A4. The panel added M1.2 (sub-problem, live community), G1-axi (narrowed
from moonshot to conditional attack strategy), B3 (the tier-e node companion
to A4), and the consolidated no-go ledger. R accepted the expansion because
each addition was honestly labelled and none was inflated to hit a quota.

**Comparison with iter-3's ten entries.** Iter-3 produced a list of 10
graph-enrichment edges for proved theorems — a completion exercise for a closed
problem space. Iter-4 produced 7 entries in the portfolio: attack strategies
for an open problem. The distribution is:
  - iter-3: 10 completions of closed material;
  - iter-4: 3 attack strategies + 2 sub-problems + 1 technique-node + 1 no-go
    ledger = mixed types, including the strongest tier-(e) deliverable the
    method has produced.

**Is attacking an open problem more generative than attacking closed edge states?**
P's view: yes, by count of tier-(e) outputs (A4 would not have been produced
against a closed problem because there's nothing to search). R's view: no, by
count of theorems-produced (iter-3 produced rigorous graph-enrichment edges;
iter-4 produced zero theorems). E's view: the right comparison is the *type*
of output. Iter-3 had 100% completion / restatement; iter-4 had ≈ 43% attack /
30% sub-problem / 14% technique / 14% no-go. The open-problem setting produced
a more structurally varied portfolio.

**What this tells us about the method.** The graph-driven method's comparative
advantage is generating cross-disciplinary combinations (A4's computational-algebra
× formal-verification × PDE combination) and enforcing structural honesty
(mandatory barrier-check, explicit repackaging flags). Its comparative
disadvantage is that inside pure native-discipline work (M1.x on PDE analysis),
it does not generate insight beyond an expert mental map. The iter-4 yield
dividend over iter-3 came almost entirely from one cross-disciplinary
combination (A4 + B3); the M1.x / G1-G6 PDE-native proposals mostly
rediscovered landscape an NSE expert already knows. The lesson is that the
method's edge is cross-disciplinary, not depth-within-discipline.

**Final honest panel tally.**
- Attack strategies (X): **3** — G4, A4, G1-axi.
- Sub-problems (Y): **2** — M1.2, G5.
- New-technique nodes (Z): **1** — B3. (B1, B2, B4 admitted as secondary
  composites, honestly labelled, not counted as primary entries.)
- Productive no-gos (W): **6** consolidated into 1 ledger — M1.1-weight,
  G2-scaling, G3-Shkoller + NSE-not-geodesic, G6-contractibility, M1.6-helicity,
  M1.4-Burgers-wall.

**N total portfolio entries = 7** (X + Y + Z + consolidated W = 3 + 2 + 1 + 1 = 7).

This is honest. It is not Clay-denting. It is a respectable iter-4 output.

---

## §8 — Iter-5 recommendation

Synthesising the panel's position with the philosopher's §6:

**Primary recommendation.** Restrict iter-5's scope to **one named sub-problem**
from {SP1, SP4, SP7} — the three sub-problems this session left orphaned.
Framing "attack Clay" invites MOONSHOT-grade noise (M1.3, M1.4, G2, G3 all
self-labelled moonshot and most failed on the scaling or structural-mismatch
check). Framing "attack SP1 / SP4 / SP7 deeply" reduces noise and invites
concrete technical work. The philosopher's #1 iter-5 recommendation is
"restrict scope to tractable sub-problems and skip the full Clay framing" —
the panel endorses this.

**Secondary recommendation.** Structure iter-5 as a **deep recursion on the iter-4
top-3** (A4 + G4 + G1-axi), not as another broad survey. Specifically:

- For A4: a mathematician actually codes the degree-2 enumeration in Python/SymPy
  and runs it on the known 2D NSE case (where monotone quantities are known) as
  a sanity check, then proceeds to degree-3 NSE. Output: concrete SDP results.
- For G4: a mathematician works through the KNSŠ Liouville argument line-by-line
  and attempts the Type-II backward-profile adaptation for the simplest no-swirl
  ancient case. Output: either partial progress or a concrete obstruction.
- For G1-axi: a mathematician computes the κ-Osgood feedback quadratic
  self-coupling explicitly on the axi-with-swirl Biot–Savart structure.
  Output: either cancellation (→ proceed to full Osgood calculation) or
  non-cancellation (→ documented no-go on SP-axisymmetric).

The session would lose breadth but gain actionable depth.

**Tertiary recommendation.** Introduce **domain-expert prompted agents**
("you are Vicol thinking about the Buckmaster-Vicol-to-Leray-Hopf gap"
rather than "you are generic Mathematician 1"). Philosopher's §6 ranked this
#2; the panel endorses.

**What to avoid.** Do not add more mathematicians — iter-4 had diminishing
returns past 3. Do not pivot to a different open problem yet; iter-4 produced
enough attack-axis structure on NSE that a depth-recursion iter-5 has a
well-defined target set. Do not trust MOONSHOT grades as research targets;
treat them as "this person does not have a credible plan" flags.

**Single meta-observation carried from philosopher §6.** Graph-driven
combinations produce novelty when they cross out of the target problem's
native discipline into a neighbor's tooling. A4 (PDE × computational algebra ×
formal verification) was the one iter-4 success of this kind. Iter-5 should
actively search for similar cross-disciplinary combinations: PDE ×
computational algebra, PDE × probability theory, PDE × information theory,
PDE × geometric group theory. More of these, fewer re-derivations of Chae's
direction-of-vorticity criteria, and iter-5 will clear the bar iter-3 set and
iter-4 only partially reached.

**End of portfolio.**
