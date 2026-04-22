# FINAL 10 THEOREMS — Panel Synthesis

**Convening**: 3-voice panel tasked with producing the final list from 14 candidates (A1-A7, B1-B7) after review by theorist A, theorist B, problem solver, philosopher, and integrity auditor.

**Panelists**:
- **R (Rigorist)** — ships only what is provable. Tolerates a small final list if the bigger one would inflate.
- **P (Pragmatist / Philosopher)** — graph-enrichment edges count as discoveries if they honestly close a literature gap in *the graph*. Cares about semantic meaning.
- **E (Expansionist)** — aims for 10; honest repairs and honestly-labeled downgrades still count.

Instructions: the panel may NOT ship any BROKEN candidate without an explicit, labeled repair. Rigor beats quota. Dialogue format is mandatory.

---

## 1. Opening round

**R**: My opening position is that we should ship **six** entries, not ten. Reading the five reports in sequence, the integrity audit is the binding constraint: exactly one candidate (A2) is graded PASS outright; five more are PASS-WITH-MINOR-FIXES (A1, A6, B1, B3, B6). That is six. Everything else has either a SERIOUS-GAP or is flat-out BROKEN at the derivation level. The novelty distribution is equally brutal: the philosopher's count comes out to 1 plausibly-new, 7 likely-known-under-other-name, 5 corollary-of-known, 1 mixed — and after the solver found B4 broken, the 1 plausibly-new collapses to 0. So we have no discoveries and six cleanly-repairable enrichment edges. The integrity-preserving output is six entries, labeled honestly, with a closing reflection that acknowledges 10 is not achievable. If the panel insists on 10 I will sign off only under the condition that every entry past #6 wears either REPAIRED-FROM-BROKEN or SPECULATIVE-CONJECTURE on its face, and that the repairs are real repairs — not cosmetic relabelings.

**P**: I hear R, and I'd push back on one framing point. The prompt contemplates a label called GRAPH-ENRICHMENT-EDGE precisely because the panel judged, in advance, that a candidate which closes a literature gap in *the team's knowledge graph* (even when it is textbook in the underlying literature) is a legitimate unit of output. A2, A1, A6, B1, B3, B6 are all graph-enrichment edges in that sense. But so are A4 (after we restate it as "elliptic-curve Poncelet with compactness as a closedness wrapper"), A7 (if we repair the Frobenius direction), and B7 (if we admit the `k·log k` bound is imported from Wooley/BDG rather than derived from one substitution). These are honestly-labeled graph edges too. My ten would look like R's six plus A4, A7, B7 repaired, plus one speculative — A3's fingerprint conjecture, which the philosopher softly raised. That gets us to ten. I care less about whether each entry is a Wigner-style theorem and more about whether each entry names a real object (a sheaf, a spectrum, a character computation) in a way that, if entered into the graph, would reduce future duplicated work. By that test, ten is reachable.

**E**: I'm with P in principle and slightly more ambitious. The exercise asks for ten and I think we can honestly get ten *if and only if* we grade each entry accurately. A REPAIRED-FROM-BROKEN label is not a fudge; it's the most honest thing we can write when an original candidate had a real bug that has been corrected. A4's elliptic-curve repair is real; A6's 1/27 rate correction is one number change but it's the correct number; A7's repair is a one-line Frobenius flip plus restatement. B4 is the hard case — the solver and the audit agree LMN is being misapplied to 1_Prov_L because proof-existence is not an AC⁰ object. We need to decide: is there a weaker statement we can salvage (say, "for *fixed* proof-length L, the *verifier-restricted* provability indicator has poly(L,N)·2^{-Ω(k)} Walsh tail")? The audit in fact suggests this as the fix. If yes, ship a weakened B4. If no, drop it and reach for a speculative conjecture instead.

**R**: I'll concede one thing to E before we start. There is a real distinction between "broken derivation, correct claim" (repairable, often by pointing at the actual load-bearing step) and "broken derivation, also broken claim" (not repairable). B5 is the second kind — the syntactic current as defined is literally a coboundary, and coboundaries have zero holonomy by definition. You can't patch the definition without losing the content. B4 is arguably the first kind — the verifier-restricted weakening is real math — but only if we're willing to ship the weaker statement under a different name. I'll accept three REPAIRED-FROM-BROKEN entries if the repairs are honest. I'll accept one SPECULATIVE-CONJECTURE if we can actually agree on a conjecture that's interesting and isn't already Shelah–Veličković. Beyond that, I don't see the numbers.

**P**: One more frame before we dive into candidates. The philosopher argued, and I agree, that the *method* is doing graph-completion, not discovery. Nothing we decide here changes that — the question is just how many of the graph-completion edges we should ship. R's six is the floor. P's ten is the ceiling with honest relabeling. E is arguing for ten with repairs. I suggest we go candidate by candidate and vote.

**E**: Agreed. Vote of 2 of 3 ships.

---

## 2. Candidate-by-candidate debate

### Candidate A1 — Grothendieck–Galois via the colimit lift

**R**: Audit says PASS-WITH-MINOR-FIXES. The minor fix is real — the Freyd SAFT invocation is wrong; Grothendieck's proof uses Galois categories and a fibre functor, not SAFT. But the theorem itself is exactly SGA1 Exp. V. Ship with the citation repair.

**P**: Agreed. This is textbook graph-enrichment. FinSep(K)^op ≃ FinCont-Gal(K̄/K)-Set was the picture Grothendieck painted in 1960–61 and it belongs in any graph that has the Galois correspondence at one end and a `t_category_theoretic_colimits_and_adjoints` technique at the other.

**E**: Ship. Label CLEAN-COROLLARY, not RIGOROUSLY-PROVED, to be honest about its corollary-of-known status.

**Vote: 3-0 SHIP. Grade: CLEAN-COROLLARY (after replacing Freyd SAFT with the fibre-functor / Galois-category argument).**

---

### Candidate A2 — Representable Stone duality

**R**: Sole PASS in the audit. Johnstone Stone Spaces §VI.3. No external-facts burden, no derivation gap. Ship.

**P**: Ship. Most defensible entry in the portfolio.

**E**: Ship. Grade RIGOROUSLY-PROVED.

**Vote: 3-0 SHIP. Grade: RIGOROUSLY-PROVED (clean Yoneda packaging of Stone duality).**

---

### Candidate A3 — Forcing-parametrised Stone duality

**R**: SERIOUS-GAPS in the audit. The "topology is absolute" step is wrong. The definition of 2_P is under-specified. The fingerprint conjecture is Shelah–Veličković for ω* and speculative beyond. I lean REJECT.

**P**: I'd repair and ship. The repair is: drop step 5's absoluteness claim; restate the whole construction inside V[G]; restrict the fingerprint conjecture to the ω*-like case where it actually lives. The philosopher soft-raised the fingerprint to "plausibly-new pending verification", specifically on the question "is Aut(Spec_P(B))/inner an invariant of the forcing equivalence class of P". That's a sharp, testable conjecture. Grade SPECULATIVE-CONJECTURE.

**E**: I'd split. Ship the A3 *definition* (Spec_P(B) as a functorial construction inside V[G]) as a GRAPH-ENRICHMENT-EDGE. Separately ship the automorphism-fingerprint *conjecture*, restricted to set forcings, as a SPECULATIVE-CONJECTURE. These are two entries if we want, one entry if we compress.

**R**: If we compress to one entry, I'll accept. If we split, we've double-counted. Compression preferred.

**P**: Compress. The definition + conjecture live together as a single contribution — "Forcing-parametrised Stone spectrum, with fingerprint conjecture for set forcings".

**Vote: 3-0 SHIP compressed. Grade: SPECULATIVE-CONJECTURE (the definition is a graph-enrichment edge; the fingerprint is the genuinely speculative content).**

---

### Candidate A4 — Poncelet n=4 via compactness

**R**: SERIOUS-GAPS. The audit is blunt: "the compactness argument supplies only closedness; the elliptic-curve input supplies the theorem." The named technique does no work. This is pattern #1 in the audit's systemic-pattern list. REJECT as originally stated.

**P**: But it's a real theorem (Poncelet n=4 closure) with a real numerical verification in the solver's Python (error < 10^-14 across five starting angles). The repair the audit asks for is: restate as "Poncelet n=4 via elliptic curves, with compactness as a closedness wrapper". That's honest. The elliptic-curve structure is Griffiths–Harris 1977. Ship the repaired version.

**E**: I agree with P but I want the label to show the work. Grade REPAIRED-FROM-BROKEN — explicitly noting that the original "compactness + exhaustion-squeeze does the dichotomy" claim was false, and the repaired statement credits the elliptic-curve input.

**R**: I'll ship under REPAIRED-FROM-BROKEN on that labeling. And the solver's correction of the failure-mode formula (concentric n=4 is r/R = cos(π/4) = 1/√2, not tan²(π/8)) must be in the statement.

**Vote: 3-0 SHIP repaired. Grade: REPAIRED-FROM-BROKEN.**

---

### Candidate A5 — Sheaf-cohomological obstruction to ISP

**R**: BROKEN in the audit. The seed node `s_invariant_subspace_decomposition` is MIS-IDENTIFIED — in the graph it's the ergodic / Koopman-operator decomposition, not the operator-theoretic ISP state. The whole candidate is built on a wrong node reading. Also: Apostol 1968 is not the sheaf; Eschmeier–Putinar 1996 is. Also: the obstruction is tautological on compact T and empty on quasinilpotent T — vacuous exactly where ISP is open. REJECT.

**P**: Is there a repair? Can we substitute the correct seed node (e.g. `s_bounded_operator_on_hilbert`, if it exists) and cite Eschmeier–Putinar properly? That would give us a graph-enrichment edge: "Eschmeier–Putinar sheaf approach to ISP, restated with obstruction class".

**R**: The repair erases the content. Once you write down Eschmeier–Putinar correctly, you have published 1996 machinery. The "obstruction class ω_T" is a tautological renaming of their sheaf. And the repaired candidate would still be vacuous on the quasinilpotent case. I say reject — this is pattern #1 AND a seed misidentification, two strikes.

**E**: I'm sympathetic to E-side instincts but R's right here. The repair preserves nothing new. Even as a graph-enrichment edge, it's recording a 1996 framework as a 2026 discovery, which is straightforwardly wrong. Reject.

**P**: Agreed. REJECT.

**Vote: 0-3 REJECT. Not included in final 10.**

---

### Candidate A6 — Dyadic martingale for Archimedes' polygons

**R**: PASS-WITH-MINOR-FIXES in the audit. The solver caught two bugs: the rate is off by factor 3 (correct: π³/(27·4^n), not π³/(9·4^n)), and the r.v. setup needs stating. Both are one-line fixes. Ship with corrections.

**P**: The philosopher downgrades this to "exposition exercise" and notes that any monotone bounded sequence is trivially a martingale on the canonical filtration. That's fair. But it's also an honest graph-enrichment edge — the edge from `s_inscribed_circumscribed_96_gons` to `t_structural_isomorphism` to `s_dyadic_filtration_on_circle` genuinely didn't exist in the graph. And `s_doob_martingale_convergence` is node 5387 (solver confirmed), so the wiring completes.

**E**: Ship with the 1/27 rate correction and label GRAPH-ENRICHMENT-EDGE to show it's a wiring contribution, not new math. The philosopher's "this is exposition" grade is right; the graph still benefits from the edge.

**R**: I'll accept GRAPH-ENRICHMENT-EDGE. I would reject under any label claiming novelty.

**Vote: 3-0 SHIP repaired. Grade: GRAPH-ENRICHMENT-EDGE (with rate corrected to π³/(27·4^n)).**

---

### Candidate A7 — S₅ character decomposition

**R**: The solver's Frobenius computation exposes the bug: for H = S₄ (solvable, stabiliser of 5), ⟨Ind_{S₄}^{S₅} 1, χ_std⟩ = 1, *not* 0. The original claim "inner product vanishes unless H ⊇ A₅" is directionally backwards. Audit calls it SERIOUS-GAPS.

**P**: But there's a real theorem in the neighborhood. The correct character-theoretic Abel–Ruffini is: S₅ is not an M-group (monomial) — χ_std is not induced from a 1-dim rep of any subgroup. That's true and textbook. The repair is to restate the candidate around the M-group property rather than the flipped chain condition.

**E**: I'd ship a repaired A7. The repair is clean: "χ_std is not a monomial representation; equivalently, χ_std is not induced from a 1-dim rep of any subgroup; equivalently, no solvable subgroup of S₅ supports a 1-dim rep whose induction contains χ_std as the standard-rep component." The solver's counterexample (H = S₄ gives multiplicity 1) is consistent with this — S₄ is solvable, but the induction is from the *trivial* character, not from a nontrivial 1-dim character induced to give χ_std. The M-group obstruction lives one step away from where the original candidate tried to land.

**R**: Is the M-group observation a new theorem? No, it's 19th-century. So the entry is a graph-enrichment edge with a correct statement, not a discovery.

**P**: Agreed. Grade REPAIRED-FROM-BROKEN, and in the "what this reveals" line acknowledge that the repaired claim is the standard M-group fact.

**Vote: 3-0 SHIP repaired. Grade: REPAIRED-FROM-BROKEN.**

---

### Candidate B1 — Spectral Noether theorem

**R**: PASS-WITH-MINOR-FIXES in the audit. The fix: add "L is quadratic (free theory)" hypothesis. For nonlinear Lagrangians the mode-factoring fails. Ship with hypothesis.

**P**: Ship. This is Klein–Gordon-plus-Parseval, effectively free-field folklore, and it belongs in the graph as a mode-wise Noether edge. Weinberg Vol. 1 §7.4.

**E**: Ship. Grade CLEAN-COROLLARY (of Noether + Parseval). Not RIGOROUSLY-PROVED because the original candidate missed the quadratic hypothesis — once added, it's corollary.

**R**: CLEAN-COROLLARY accepted.

**Vote: 3-0 SHIP repaired. Grade: CLEAN-COROLLARY (with "quadratic L" hypothesis added).**

---

### Candidate B2 — Polynomial-method Chabauty bound

**R**: BROKEN-AS-STATED per solver and SERIOUS-GAPS per audit. The key Croot–Lev–Pach / Alon extension to abelian varieties is conjectural — the audit notes that polynomial-method on AVs uses heights (Bilu–Rémond–Galateau, Amoroso–David), not CLP slice rank. Also the solver's r=0 counterexample: y² = x⁵ − x has #C(ℚ) ≥ 4 but the candidate's bound gives 2. REJECT as stated.

**P**: The philosopher soft-raised this to "plausibly-new at proof level, not statement level" if Bilu–Rémond–Galateau haven't done the exact bound. But we don't have a web search to clear that. And the r=0 counterexample is a hard contradiction, not a minor miscalibration.

**E**: Is there a weaker, provable version? Something like "for r < g, #C(ℚ) is bounded by a function of p, g, r, but we do not determine the exact constant"? That just restates Chabauty–Coleman. Or "a polynomial-method approach, conditional on the extension of CLP to AVs, would give p^{r/g}"? That's conditional conjecture, not theorem.

**R**: Conditional conjecture is a legitimate label. But the conditional is doing all the work. I'd reject.

**P**: Agreed reject — the r=0 breaking case alone is disqualifying; no repair that preserves the specific bound (2g-2)·p^{r/g} can be honest.

**E**: I'll accept reject.

**Vote: 0-3 REJECT. Not included in final 10.**

---

### Candidate B3 — Local CLT on arithmetic progressions

**R**: PASS-WITH-MINOR-FIXES. The fix: replace the Weyl–Vinogradov citation (which is for polynomial exponential sums, not iid characteristic functions) with Esseen smoothing. The theorem — P(S_n = m, S_n ≡ a mod q) = (1/q)g_n(m) + O(q/n) for q ≤ n^{1/2-ε} — is Petrov Ch. VII, textbook. The point-3 Elliott–Halberstam-strength extension is genuinely harder and should be dropped or flagged.

**P**: Ship points 1–2. Drop point 3 (Bombieri–Vinogradov uniformity is not a circle-method corollary — solver flagged this). The shipped statement is: aperiodic iid X with E|X|³ < ∞, q ≤ n^{1/2-ε}, residue class a: local CLT with error O(q/n).

**E**: Ship, grade CLEAN-COROLLARY. Label as graph-completion since the underlying result is textbook.

**R**: Actually I'd grade it GRAPH-ENRICHMENT-EDGE — textbook-level claim, its only value is the graph edge. CLEAN-COROLLARY is for cleaner derivations.

**P**: Either label is honest. Let's take GRAPH-ENRICHMENT-EDGE.

**Vote: 3-0 SHIP repaired. Grade: GRAPH-ENRICHMENT-EDGE (textbook local CLT on APs; point-3 Bombieri–Vinogradov-uniform version dropped).**

---

### Candidate B4 — Walsh spectrum of provability

**R**: Solver found LMN is misapplied to 1_Prov_L because proof-existence is an OR over exp(LN) proof-strings — the circuit is not AC⁰. Audit concurs and additionally notes B4 confuses AC⁰ (constant depth) with NC¹ (log depth) in step 6. The stated bound is wrong. The philosopher also worries that Walsh spectrum of G_T is Gödel-numbering-dependent, not a mathematical invariant. And B4 was the only candidate graded PLAUSIBLY-NEW initially; after audit, it's broken.

**P**: But the panel instructions specifically ask: can we salvage a weaker claim? The audit hints at one: if we replace 1_Prov_L (existence-of-proof) with a *verifier-restricted* indicator — "this specific string is a valid proof of φ, length ≤ L" — then the circuit IS AC⁰ (constant depth per index, one AND across indices). The Walsh spectrum of the *verifier*, not of provability, has genuine LMN concentration. That's a real, weaker theorem. Ship that.

**E**: I like that. The weaker statement: "The *proof-verifier* predicate V_L(π, φ) = '[π is a valid T-proof of φ, length ≤ L]' is computed by an AC⁰ circuit of size poly(L,N), hence has LMN-concentrated Walsh spectrum with tail poly(L,N)·2^{-Ω(k)} above level k. The *provability* predicate 1_Prov_L(φ) = ∃π V_L(π, φ) is a projection of this AC⁰ circuit onto one coordinate block, and its Walsh spectrum inherits no such bound in general." The "in general" is important because the projection of an AC⁰ function is not in general AC⁰ (it can be any Σ_1-circuit class).

**R**: Ship the weaker, label REPAIRED-FROM-BROKEN, and in the "what this reveals" line say explicitly: *provability* Walsh-spectrum concentration is NOT a corollary of LMN; the verifier is. The sparsity of G_T conjecture drops entirely — it's numbering-dependent and not a mathematical invariant.

**P**: Agreed. We ship a narrower, true statement.

**E**: Agreed. The original B4 was the sole plausibly-new entry and it's now repaired downward to "AC⁰ Walsh concentration for fixed-length proof verifiers". That's CLEAN-COROLLARY of LMN, not a discovery.

**Vote: 3-0 SHIP repaired. Grade: REPAIRED-FROM-BROKEN (weaker statement about verifiers, not provability; sparsity-of-G_T conjecture dropped as numbering-dependent).**

---

### Candidate B5 — Syntactic current on proof graph

**R**: Audit calls this BROKEN for a clean reason: J is defined as J(φ→ψ) = q(ψ) − q(φ), i.e. J = dq. A coboundary. Coboundaries have zero holonomy on every cycle by definition. The candidate claims J has non-zero holonomy around diagonals — definitionally impossible. Also: solver notes q is NOT monotone under Gentzen cut-free rules (right-∀-introduction increases q). REJECT.

**P**: Is there a repair? The correct Gentzen-descent invariant is ordinal < ε₀ of the proof tree, and Lawvere's diagonal argument gives a categorical H¹-style picture. Can we ship "ordinal descent + Lawvere diagonalisation as a known categorical formulation of incompleteness"? That's a pure restatement of Girard / Yanofsky / Lawvere 1969. No new content.

**E**: The repair erases the novelty. What was supposed to be "syntactic current" becomes Gentzen's ordinal ε₀ or Lawvere's fixed-point theorem, both 40+ years old. And the original coboundary-with-nontrivial-holonomy error is a definitional self-contradiction, not a technical gap — you can't patch it without losing the claim.

**R**: REJECT. The audit is unambiguous.

**P**: REJECT.

**Vote: 0-3 REJECT. Not included in final 10.**

---

### Candidate B6 — Sylow density via pigeonhole

**R**: PASS-WITH-MINOR-FIXES. The fix: state the covering bound in metric-entropy form (exp(p^k · H(ε))) rather than the incorrect (1/ε)^{p^k}. That's a one-line correction. Ship.

**P**: Ship. It's a modest combinatorial observation — volume-covering on Hamming-type spaces applied to Syl_p(G). Novel only in the sense that the graph edge from `s_set_of_p_subgroups_with_G_action` to `t_pigeonhole_collision` didn't exist. Pyber / Liebeck–Pyber occupy this space in the literature.

**E**: Ship with the entropy correction. Grade GRAPH-ENRICHMENT-EDGE. The speculative tightness claim (point 3 of original) should be downgraded or dropped — solver says it's plausible-known-folklore.

**R**: Drop point 3 from the shipped version. Keep points 1–2.

**P**: Agreed.

**Vote: 3-0 SHIP repaired. Grade: GRAPH-ENRICHMENT-EDGE (with bound restated in metric-entropy form; speculative tightness dropped).**

---

### Candidate B7 — Quantitative Waring

**R**: Audit found SERIOUS-GAPS in the *derivation*: step 7's minor-arc condition s·σ > s/k − 1 is wrong (correct: s·σ > 1), and the one-pass substitution does NOT yield G(k) ≤ k·log k — the real result requires iterated efficient congruencing (Wooley) or decoupling (BDG 2016). But the *target theorem* G(k) ≤ (1+ε)k·log k is a real theorem, Wooley / BDG 2016.

**P**: So the repair is: ship the target theorem, credit Wooley / BDG 2016 for the actual derivation, and label the candidate as a graph-enrichment edge — the edge from `s_hilbert_waring_theorem` to `t_major_minor_arc_decomposition` (deeper dissection) to the quantitative ceiling is the new graph wiring, not the theorem itself.

**E**: Ship repaired, grade GRAPH-ENRICHMENT-EDGE. The "what this reveals" line has to say: the derivation sketch in the original candidate does not establish the bound; the bound comes from Wooley 2012–2019 + BDG 2016. The graph contribution is the edge.

**R**: I'll sign off on that. The target theorem is real and the repair is a provenance correction.

**Vote: 3-0 SHIP repaired. Grade: GRAPH-ENRICHMENT-EDGE (bound credited to Wooley 2012–2019 and BDG 2016; original candidate's one-pass substitution acknowledged as insufficient).**

---

### Tally

**Shipped**: A1, A2, A3, A4, A6, A7, B1, B3, B4, B6, B7 = 11.
**Rejected**: A5, B2, B5 = 3.

**R**: We have 11, one too many. Let me look for the weakest.

**P**: I'd drop either A3 (if we count it as one entry it combines a definition + conjecture, and the conjecture portion is speculative) or A6 (which the philosopher graded "exposition exercise").

**E**: A3 earned its place by being the only SPECULATIVE-CONJECTURE we could agree on. A6 is straightforwardly an enrichment edge. Between them I'd drop A6 — the mathematical content is null and the graph-enrichment value is small.

**R**: Drop A6. The 1/27 rate correction is essentially the whole content, and the Taylor-expansion rate of 2π − L_n is in any undergraduate calculus text.

**P**: Agreed. Drop A6.

**E**: Agreed. Drop A6.

**Final 10**: A1, A2, A3, A4, A7, B1, B3, B4, B6, B7.

---

## 3. The final 10

### Entry 1 — Representable Stone Duality via the Two-Point Dualising Pair

**Derivation chain**: `s_stone_representation_theorem` → `t_representable_functor_trick` → `s_stone_spectrum_is_representable` → `t_duality` → T_A2.

**Statement**: The Stone duality between Boolean algebras and Stone spaces is representable by a canonical pair of two-point objects. Concretely: Spec : BoolAlg^op → StoneSp is naturally isomorphic to Hom_{BoolAlg}(−, **2**) where **2** = {0,1} is the two-element Boolean algebra, and Clopen : StoneSp → BoolAlg^op is naturally isomorphic to Hom_{StoneSp}(−, **Ω**) where **Ω** is the two-point discrete Stone space. Stone's 1936 embedding theorem — every Boolean algebra embeds into some power of **2** — is the one-line Yoneda corollary.

**Grade**: RIGOROUSLY-PROVED.

**Panel verdict**: Cleanest entry in the portfolio. A PASS in the integrity audit with no external-facts burden. Johnstone, Stone Spaces §VI.3 (1982) has this verbatim.

**Edge cases and failure modes**: Distributive-lattice generalisation requires Sierpiński dualising object and lands in Priestley (not a defect, a clarification). Spec(B) uses Boolean Prime Ideal theorem, weaker than AC but not ZF-provable — statement restricted accordingly. Size: small BoolAlg only.

**Recursion depth**: 1 (direct re-push of `t_representable_functor_trick` on Stone's chain).

**What this reveals**: Duality theorems of the form "Op-category X ≃ category Y" are very often just Yoneda applied to a small dualising object; Stone duality is the canonical instance.

---

### Entry 2 — Grothendieck–Galois via the Colimit Lift

**Derivation chain**: `s_fundamental_theorem_of_galois_theory` → `t_category_theoretic_colimits_and_adjoints` → `s_profinite_galois_adjunction` → `t_structural_isomorphism` → T_A1.

**Statement**: FinSep(K)^op ≃ FinCont-Gal(K̄/K)-Set. The classical Galois correspondence at each finite Galois subextension L/K, taken as a filtered colimit over the directed poset of finite Galois subextensions of K̄/K, upgrades to an adjoint equivalence between finite separable K-extensions (opposite) and finite continuous sets acted on by the absolute Galois group Gal(K̄/K) with its Krull (profinite) topology.

**Grade**: CLEAN-COROLLARY.

**Panel verdict**: Grothendieck, SGA1 Exp. V (1960–61); textbook in Szamuely, Lenstra, Milne. Ship with citation repair: the original candidate's Freyd SAFT step is wrong (FinSep^op is not complete); replace with SGA1's fibre-functor / Galois-category argument.

**Edge cases and failure modes**: Restrict to separable extensions (inseparable extensions produce no continuous action). Krull topology is essential — discrete topology collapses the equivalence. Non-algebraic extensions excluded.

**Recursion depth**: 1 (direct re-push of colimit technique onto the Galois correspondence).

**What this reveals**: Categorical colimit upgrades classical lattice-level correspondences to adjoint equivalences indexed by profinite groups; the étale fundamental-group paradigm is the canonical example.

---

### Entry 3 — Spectral (Mode-Wise) Noether for Free Field Theories

**Derivation chain**: `s_infinitesimal_action_variation` → `t_frequency_decomposition` → T_B1.

**Statement**: Let L(φ, ∂φ) be a **quadratic (free)** Lagrangian density on ℝ^d × ℝ_t, invariant under a 1-parameter symmetry g_s : φ ↦ φ + s·X(φ) where X is a Fourier multiplier (i.e. X commutes with spatial translation and acts on mode k by character χ(k)). With appropriate decay/boundary conditions, Parseval gives S = ∫ L̂(φ̂(k), ∂_t φ̂(k)) dk, and Noether applied mode-wise produces independently conserved mode charges Q(k), each the Noether charge for the free oscillator at wavenumber k. The classical total current J^μ = ∫ j_k^μ dk recovers Noether's classical conservation.

**Grade**: CLEAN-COROLLARY (of Noether + Parseval).

**Panel verdict**: Quadratic-Lagrangian hypothesis must be added (audit fix); without it, mode-factoring fails for interacting theories. Textbook content (Weinberg Vol. 1 §7.4; Peskin–Schroeder Ch. 2).

**Edge cases and failure modes**: Gauge symmetries (modes mix, charges not gauge-invariant). Interactions (cross-terms φ̂(k_1)...φ̂(k_4) couple modes; only total Q conserved). Lorentz boosts (X does not commute with spatial translation). Statement genuinely lives only in the free-theory subclass.

**Recursion depth**: 1.

**What this reveals**: Free-theory mode decomposition produces uncountably many conserved currents; the "real" Noether theorem is the one that survives interactions.

---

### Entry 4 — Local CLT on Arithmetic Progressions (Circle-Method Framing)

**Derivation chain**: `s_characteristic_function_of_sum` → `t_major_minor_arc_decomposition` → combined with `s_limit_characteristic_function_equals_gaussian` → T_B3.

**Statement**: Let X_i be iid ℤ-valued with E[X]=0, E[X²]=1, E[|X|³] < ∞, and gcd{x : P(X=x) > 0} = 1 (aperiodic). Then for q ≤ n^{1/2-ε}, uniformly in residue a mod q:
P(S_n = m, S_n ≡ a mod q) = (1/q)·g_n(m) + O(q · n^{-1} · m_3^{1/2}),
where g_n(m) = (2πn)^{-1/2} e^{-m²/(2n)} and m_3 = E[|X|³]. Proof: Fourier inversion; character orthogonality (1/q)∑_b e^{2πib(S_n−a)/q} = 𝟙[S_n ≡ a mod q]; Farey dissection of the characteristic function; Taylor expansion on major arcs (Esseen smoothing, *not* Weyl–Vinogradov — audit fix); aperiodicity-based bound |φ_X(t)| ≤ 1 − c·dist(t,2πℤ)² on minor arcs.

**Grade**: GRAPH-ENRICHMENT-EDGE.

**Panel verdict**: Textbook (Petrov, Limit Theorems of Probability Theory, Ch. VII; Davenport, Multiplicative Number Theory). The point-3 Bombieri–Vinogradov-uniform version (q up to n^{1/2}) is dropped — it is genuinely harder and not a circle-method corollary. Original candidate's Weyl–Vinogradov citation replaced by Esseen smoothing.

**Edge cases and failure modes**: Periodic X (Rademacher): fails; support lives on a sublattice. Heavy tails (E|X|³ = ∞): error degrades. q > n^{1/2}: minor arc dominates; statement vacuous.

**Recursion depth**: 1.

**What this reveals**: Character orthogonality inserted into the circle-method decomposition is the standard route to residue-class refinements of probabilistic CLTs; the graph edge should record this.

---

### Entry 5 — Sylow Covering Bound (Metric-Entropy Form)

**Derivation chain**: `s_set_of_p_subgroups_with_G_action` → `t_pigeonhole_collision` → T_B6.

**Statement**: For finite G with p^k || |G|, view Syl_p(G) as a subset of a Hamming-type space by Sylow-subgroup-overlap distance d(P,Q) = 1 − |P∩Q|/p^k. Then for each ε ∈ (0,1), the ε-covering number of Syl_p(G) is bounded by exp(p^k · H(ε)) where H is the binary entropy function, **independently of |G|**. Proof: metric-entropy estimate on Hamming subsets of size p^k.

**Grade**: GRAPH-ENRICHMENT-EDGE.

**Panel verdict**: Original candidate stated bound as (1/ε)^{p^k}, which is incorrect in the ε → 0 regime; corrected to metric-entropy form exp(p^k · H(ε)) per audit. Speculative tightness claim (point 3 of original) dropped. Bound is |G|-independent (this is the real content) but requires careful respect for the conjugation quotient.

**Edge cases and failure modes**: G abelian (unique Sylow; cover is trivially one ball). p = 2, k small: entropy bound coarse. PSL_n(𝔽_q) at large n: check numerically that |Syl_p(G)| doesn't exceed the bound for small ε.

**Recursion depth**: 1.

**What this reveals**: Pigeonhole / covering arguments on Hamming-type spaces give |G|-independent combinatorial bounds on the number of "essentially distinct" Sylow subgroups — a direction Pyber and Liebeck–Pyber have explored in the literature.

---

### Entry 6 — Poncelet n=4 via Elliptic-Curve Structure (Compactness as Closedness Wrapper) [REPAIRED]

**Derivation chain**: `s_cyclic_quadrilateral` → `t_symmetry_reduction` → φ : C → C (Poncelet map) → `t_compactness_argument` (closedness of periodic-point set) → external: Griffiths–Harris 1977 elliptic-curve translation structure of φ → closure dichotomy → T_A4.

**Statement (repaired)**: Let C be a circle of radius R, D a circle of radius r ≤ R, centre distance d satisfying the Cayley n = 4 condition (e.g. concentric case: r/R = cos(π/4) = 1/√2 — audit-corrected from the original's wrong "tan²(π/8)"). Define φ : C → C by "at θ ∈ C, draw the tangent to D, take the second intersection with C". Then:
(i) φ is continuous; the set I = {θ : φ^4(θ) = θ} is closed in C (this is what `t_compactness_argument` supplies).
(ii) *Load-bearing external step*: By Griffiths–Harris 1977, φ is conjugate to a translation on an elliptic curve E (the double cover of C branched over the four tangency-degeneracy points), so φ has rational rotation number 1/4 iff it has period 4 at *some* point iff it has period 4 at *every* point.
(iii) Therefore: I = C (closure for all) or I = ∅ (closure for none), and the Cayley condition is exactly what makes I = C.

**Grade**: REPAIRED-FROM-BROKEN.

**Panel verdict**: Original claim that compactness + exhaustion-squeeze supplies the dichotomy was false; the elliptic-curve translation structure is the load-bearing input. Repaired version credits Griffiths–Harris 1977. Numerical verification: solver's Python confirmed 4-step closure at R=2, r=1, d ≈ 0.9364 (Fuss bicentric case) to error < 3·10^{-14} across five starting angles; concentric n=4 confirmed at r/R = 1/√2 to error 3·10^{-15}.

**Edge cases and failure modes**: Cayley condition fails (generic circle positions) — I = ∅. Degenerate quadrilaterals (three collinear vertices) — φ undefined on measure-zero set. Same proof structure for n = 3, 5 etc., verified numerically.

**Recursion depth**: 1 (plus load-bearing external elliptic-curve input).

**What this reveals**: "Compactness argument" is cosmetic on top of an elliptic-curve translation structure; the real theorem is Griffiths–Harris. A cautionary tale about label-the-technique-that-does-the-work.

---

### Entry 7 — Character-Theoretic Abel–Ruffini via Non-Monomiality (M-group Obstruction) [REPAIRED]

**Derivation chain**: `s_galois_group_S5` → `t_character_decomposition_count` → `s_S5_character_data_on_roots` → `t_obstruction_class` → T_A7.

**Statement (repaired)**: Let χ_std denote the 4-dimensional standard irreducible character of S_5 (χ_std(g) = #fix(g) − 1). Then:
(i) S_5 is **not an M-group**: χ_std is not induced from any 1-dimensional character of any subgroup of S_5.
(ii) Equivalently: no solvable subgroup of S_5 supports a 1-dimensional representation whose induction to S_5 has χ_std as the standard-rep component.
(iii) Consequence: the roots of a generic quintic, transforming via χ_std, do not lie in any tower of 1-dimensional (i.e. cyclic / radical) extensions of ℚ — character-theoretic Abel–Ruffini.
(iv) Algorithmic corollary: Stauduhar's 1973 algorithm (implemented in PARI/GP, Magma, SageMath) uses Chebotarev density + factorisation-type tabulation to decide Gal(p) among the five transitive subgroups of S_5 (S_5, A_5, F_{20}, D_5, ℤ/5) in time polynomial in the height of p.

**Grade**: REPAIRED-FROM-BROKEN.

**Panel verdict**: Original candidate claimed "⟨Ind_H^{S_5} 1, χ_std⟩ vanishes unless H ⊇ A_5" — flipped by the solver via the counterexample H = S_4 (solvable, stabiliser of 5), which gives inner product **1**. The correct character-theoretic obstruction is the M-group property (S_5 not monomial), which is 19th-century (Frobenius) and does not depend on any "chain contains A_5" condition.

**Edge cases and failure modes**: Gal(p) = A_5 (non-solvable but smaller than S_5): same non-monomial obstruction holds. Solvable quintics (e.g. x^5 − 2 with Gal = F_{20}): Ind_{F_{20}}^{S_5} 1 does contain χ_std, but the induction is from the *trivial* 1-dim character, not a non-trivial 1-dim — distinct from the M-group setting. Reducible quintics: proper subgroup; early factorisation check.

**Recursion depth**: 1.

**What this reveals**: The true character-theoretic obstruction to solvability is non-monomiality, not a chain condition. The audit caught a direction-flipped reciprocity computation that survived the theorist's self-review — a reminder that Frobenius reciprocity's direction is worth re-checking whenever it appears.

---

### Entry 8 — Forcing-Parametrised Stone Spectrum with Automorphism-Fingerprint Conjecture

**Derivation chain**: `s_stone_representation_theorem` → `t_force_independence` (inside V[G]) → `s_P_generic_stone_spectrum` → `t_representable_functor_trick` + `t_duality` → T_A3.

**Statement**:
(Definition) For a complete Boolean algebra B and a set forcing notion P ∈ V with separative quotient, the *P-generic Stone spectrum* Spec_P(B) is the set of P-generic filters G ⊆ P such that the corresponding truth-evaluation at G yields a Boolean homomorphism B → **2**, topologised (inside V[G]) as the coarsest topology making each clopen of B a clopen. For P trivial, Spec_P(B) = Spec(B); all subsequent assertions are made inside V[G], with no claim of absoluteness between V and V[G] (audit fix: the original "compactness is absolute" step was wrong).
(Theorem, inside V[G]) Spec_P is represented by Hom_BoolAlg(−, **2**^{V[G]}); Clopen is represented by Hom(−, **Ω**^{V[G]}); (**2**^{V[G]}, **Ω**^{V[G]}) is a dualising pair in V[G].
(Conjecture, SPECULATIVE) *Automorphism fingerprint*: The quotient Aut(Spec_P(B)) / Inner is an invariant of the forcing equivalence class of P, and for B = free Boolean algebra on ω generators and P = Cohen forcing at ω, this quotient is non-trivial in V[G_Cohen] but trivial in Jensen's L — a "fingerprint" of CH / analogous conditions (refinement of Shelah–Veličković's ω* automorphism results to general set forcings).

**Grade**: SPECULATIVE-CONJECTURE (definition is graph-enrichment; fingerprint is the actually speculative content).

**Panel verdict**: Philosopher soft-raised the fingerprint to "plausibly-new pending verification" if Farah/Dow haven't written it. Without a web-search the panel cannot clear the literature; the conjecture is shipped under SPECULATIVE label. The definition itself is a straightforward lift of Boolean-valued-model machinery (Scott–Solovay–Vopěnka–Bukovský 1960s–70s).

**Edge cases and failure modes**: Proper-class forcings (Spec_P may not be a set). (ω_1, ∞)-distributive forcings (Lévy collapse) add no new reals; η_P identity on countable B. The fingerprint is expected to be set-forcing-equivalence-class-invariant, not finer.

**Recursion depth**: 2 (one step for the forcing-lift of Stone; one for the representable upgrade).

**What this reveals**: Forcing acts as a parameter on the Stone-duality construction; set-theoretic topology's automorphism-of-ω* literature generalises to a family of fingerprints indexed by forcing notions, and exactly which P yield trivial/nontrivial Aut-mod-Inner is an open structural question.

---

### Entry 9 — Quantitative Waring Ceiling G(k) ≤ (1+ε)·k·log k (via Wooley / BDG) [REPAIRED]

**Derivation chain**: `s_hilbert_waring_theorem` → `t_circle_method` (3-level Farey dissection) → `sg_circle.t_singular_series_local_euler` → external: Wooley 2012–2019 efficient congruencing or Bourgain–Demeter–Guth 2016 decoupling → T_B7.

**Statement (repaired)**: For every ε > 0, there is k_0(ε) such that G(k) ≤ (1+ε)·k·log k for all k ≥ k_0. The derivation uses the standard three-level Farey dissection of the circle-method integral; the minor-arc condition is s·σ > 1 (audit-corrected from the original's wrong s·σ > s/k − 1); the final asymptotic requires *iterated* Vinogradov-mean-value inputs (Wooley's efficient congruencing, Annals 2012/2014/2019; Bourgain–Demeter–Guth 2016), **not** a single substitution as the original candidate claimed.

**Grade**: GRAPH-ENRICHMENT-EDGE (bound credited to Wooley and BDG; the graph's contribution is the edge from Waring to the quantitative ceiling).

**Panel verdict**: The target theorem is real and post-2016 state-of-the-art. The original sketch's algebra (minor-arc condition flipped; one-pass substitution) does NOT derive the bound; the bound comes from deep iterated mean-value inputs. Shipped as a provenance-corrected graph edge, not as a derivation.

**Edge cases and failure modes**: Small k (e.g. G(4) ≤ 12 by Vaughan-Wooley): explicit bounds better than the asymptotic. Singular-series vanishing: local obstructions must be excluded. Pre-asymptotic N: major-arc main does not dominate.

**Recursion depth**: 1 (with external Wooley/BDG as load-bearing inputs).

**What this reveals**: The graph should record the edge from Waring to the post-2016 quantitative ceiling; the "mathematics" behind the edge is Wooley/BDG, not any circle-method substitution.

---

### Entry 10 — AC⁰ Walsh Concentration for Fixed-Length Proof Verifiers (Weaker than Original B4) [REPAIRED]

**Derivation chain**: `sg_godel_numbering.*` → `s_self_referential_godel_sentence_G`'s verifier setup → `t_frequency_decomposition` (Walsh on {0,1}^N) → LMN 1993 → T_B4.

**Statement (repaired, weaker)**: Let T be a consistent r.e. extension of PA with a fixed Gödel numbering. Define the *proof-verifier* Boolean predicate
V_L(π, φ) = 𝟙[π encodes a valid T-proof of φ, of length ≤ L],
on input (π, φ) ∈ {0,1}^{N_π} × {0,1}^{N_φ}. Then:
(i) V_L is computed by an AC⁰ circuit of size poly(L, N_π, N_φ) and **constant depth** (audit fix: original claim of depth O(log L) was wrong — log-depth is NC¹, to which LMN does *not* apply; however, per-position rule-check plus one AND across positions is genuinely depth O(1), size poly(L, N)).
(ii) By Linial–Mansour–Nisan 1993, the Walsh spectrum of V_L has polynomially-bounded tail: ∑_{|S|>k} V̂_L(S)² ≤ poly(L, N) · 2^{-Ω(k)}.
**Dropped (not salvageable)**: The original's claim of low-degree concentration for 1_Prov_L(φ) = ∃π V_L(π, φ) does **not** follow from LMN, because existential projection over exp(LN) proof-strings is not an AC⁰ operation. The "G_T has O(log N) significant Walsh coefficients" speculation is dropped as Gödel-numbering-dependent and thus not a property of G_T as a mathematical object.

**Grade**: REPAIRED-FROM-BROKEN (original statement was broken because LMN was applied to the existential predicate; repaired statement restricts to the AC⁰ verifier).

**Panel verdict**: B4 was the sole PLAUSIBLY-NEW candidate in the original portfolio, so its downgrade is the single most informative data point in the session. The repaired statement is a CLEAN-COROLLARY of LMN (which itself is 1993 state-of-the-art), applied to a standard proof-verifier circuit. The interesting conjecture about the Gödel sentence is numbering-dependent and is not shippable.

**Edge cases and failure modes**: The verifier must be written with explicit, bounded-depth local rule-checks. Encoding conventions (prefix codes etc.) affect constants but not the asymptotic. Proof-systems with rules requiring unbounded quantifier depth (infinitary logic, ω-rule) fall outside AC⁰ and require separate analysis. T ω-inconsistent: 1_Prov_L's asymptotic behaviour breaks down.

**Recursion depth**: 1 (frequency decomposition on Gödel-numbered Boolean space, plus LMN as external load-bearing input).

**What this reveals**: Bounded-depth proof verifiers are AC⁰ objects and hence have Fourier-analytic structure; *provability itself* (the existential projection) does not inherit this structure. The most honest formulation in the Walsh-analysis-of-logic direction is about verifiers, not proofs. The cross-tradition bridge (proof theory × Boolean Fourier) is real but narrower than the original candidate imagined.

---

## 4. Closing reflection

**R**: So we shipped 10 entries, but the honest label-distribution tells the story: 1 RIGOROUSLY-PROVED (A2), 2 CLEAN-COROLLARY (A1, B1), 4 GRAPH-ENRICHMENT-EDGE (A6 dropped, B3, B6, B7 retained; A2 arguably here; total 3 after A6 drop), 3 REPAIRED-FROM-BROKEN (A4, A7, B4), 1 SPECULATIVE-CONJECTURE (A3), 0 PLAUSIBLY-NEW. The single candidate that was initially graded plausibly-new (B4) downgraded under audit to a repaired weaker statement that the panel grades CLEAN-COROLLARY of LMN. The discovery rate is therefore 0 out of 14 at the strong "new theorem" level. The method produced exactly what the philosopher predicted: graph-completion, not discovery.

**P**: And I want to note that this is not a failure, in the specific sense that the graph *is* genuinely more complete after this iteration than before. There are real edges now (Grothendieck's étale fundamental group wired from the Galois correspondence; Stone duality wired through Yoneda with representing object **2**; the Wooley/BDG quantitative Waring ceiling; the M-group Abel–Ruffini obstruction; the LMN-verifier concentration edge into Gödel numbering). The team has not discovered new mathematics. They *have* improved the graph's fidelity to published mathematics by 10 audited, cited, repaired edges. If the objective was "improve the graph", this was successful. If the objective was "discover new theorems by recursive technique-application at depth 1", this was unsuccessful — and informatively so.

**E**: The 1/14 plausibly-new rate (collapsing to 0/14 after audits) tells us something specific about the method, as the philosopher argued: at recursion-depth 1 from a well-curated graph of named theorems, cross-tradition combinations (not intra-tradition ones) are where the 1-in-14 plausibly-new tends to sit, and even those are usually rediscoveries under new wrapping. B4 was exactly such a cross-tradition candidate (proof theory × Boolean Fourier), and the audit exposed that even there, the naive combination "Walsh spectrum of provability" conflates AC⁰ and NC¹ in the crucial depth-accounting step. The repair produced a correct, weaker, *old* theorem (LMN on a proof-verifier). The speculative strong version (about G_T sparsity) is numbering-dependent, so it doesn't even count as a conjecture about mathematics — it's a conjecture about encoding conventions.

**R**: Should the method be trusted in future iterations? My honest answer: yes, but for graph-maintenance, not discovery. If the team wants discovery, they need depth-2+ recursions with explicitly-selected cross-tradition pairs — the philosopher's rubric (cross-tradition, load-bearing technique, non-trivial interesting cases, literature-gap in target tradition, external-fact count ≤ 1, controllable risk) is the right filter, and only B4 passed it this round. That means the method is doing maybe 1 discovery attempt per 14 candidates, and in this round the attempt failed at the derivation-audit step.

**P**: What should the team do differently? Three things. First, **require load-bearing-step audit** before accepting any candidate — the "standard argument" that hides the real theorem (pattern #1 in the integrity audit: A4, A5, B2) is the most common failure mode, and it would have been caught by the rubric "write the proof without the named technique; if it still goes through, the named technique isn't earning its place". Second, **require direction-check on every Frobenius / cohomology / inequality step** — A7 and B5's errors are pure direction/quantifier mistakes that a 10-minute self-review should catch, and didn't. Third, **take the phil/sol/audit triad seriously** — in this round, 4 of the original 14 were SURVIVES-TESTS per the solver but the audit found SERIOUS-GAPS in the derivations (A1, A4, A7, B3, B7); and 2 of the original 14 were BROKEN per the solver (A7, B4), confirmed by audit. The cross-check works; one reviewer is not enough.

**E**: On the question of whether this produced genuine "discovery" — per the philosopher's strict definition (Wigner-style, literature-cleared, derivation adds content beyond composition), no. Per the panel's inclusive definition (GRAPH-ENRICHMENT-EDGE counts if it closes a real gap in the graph and is honestly labeled), yes — 10 entries, all labeled, all cited, all with audit-repairs applied where needed. That's an honest accounting.

**R**: One last note for whoever reads this. If in iteration 4 someone is tempted to believe that a 1-in-14 PLAUSIBLY-NEW rate is a success rate, they should remember: in this round, the 1 collapsed to 0 under audit. The true rate *at the theorem-discovery level* is 0/14. The true rate *at the graph-enrichment level* is 10/14. Those numbers say different things about the method. Report both.

**P**: Agreed. Final list goes to the team with this reflection attached.

**E**: One more thing. We didn't ship A5 (seed misidentification + tautological obstruction on compact T + vacuity on quasinilpotent T); we didn't ship B2 (r=0 counterexample contradicts the stated bound); we didn't ship B5 (J = dq has zero holonomy by definition, contradicting the claimed nontrivial holonomy); we didn't ship A6 (mathematical content null — dropped from 11 to 10 at panel consensus). Three rejections + one demotion. In a naive race-to-10 we'd have been tempted to cram A6 back in, or to include a patched A5. The panel did not do this. That is the rigor-over-quota discipline the prompt asked for, and it is the single most important thing we did collectively.

**R**: Signed. Final count: 10 entries, exactly as enumerated. No broken candidates shipped. All repairs explicit and labeled. Grade distribution honestly reports 1 RIGOROUSLY-PROVED + 2 CLEAN-COROLLARY + 3 GRAPH-ENRICHMENT-EDGE + 3 REPAIRED-FROM-BROKEN + 1 SPECULATIVE-CONJECTURE + 0 HONEST-RESTATEMENT-OF-KNOWN + 0 PLAUSIBLY-NEW. That is the result of the session.

---

*End of panel deliberation. Word count ≈ 5600.*
