# Philosopher's Assessment — 14 Candidate Theorems from Iter-3

**Author role**: Philosopher (independent assessment).
**Reviewed**: `theorist_A_candidates.md`, `theorist_B_candidates.md`, `recon_leverage_points.md`.
**Background**: `00_introduction.md`, `08_epilogue.md`, `09_discovery_techniques.md`.

This is an *independent* opinion. I agree with the theorists' harsh grading on most candidates, disagree on two, and take a stronger position on what the exercise collectively demonstrates about graph-driven discovery. My reading is that the iter-3 recon has produced exactly what one should *expect* it to produce, and that this is useful diagnostic information about the method, not a cause to celebrate or to despair.

---

## §1 — What counts as a new theorem?

A theorem is a proved statement. *Discovery* — the verb the recon is claiming to do — requires more. Four qualitative tests, in descending order of strength:

**(a) Wigner-style unreasonable new structure.** The statement is a fact about the mathematical world that was not visible from the precursors. Gödel's first incompleteness theorem did not follow from Hilbert's program by mechanical re-deployment of technique; it required seeing that syntax could be arithmetised, a move without antecedent in the program itself. Mordell–Faltings did not follow from the Mordell conjecture by technique reshuffling; Faltings had to invent the geometry of heights on the moduli space of abelian varieties. On this test, almost no candidate in iter-3 qualifies, and that is not a failure of the candidates — it is the definition.

**(b) Graph-completion.** The statement is a fact the graph does not encode but the literature does. It is *new to the graph, old to mathematics*. A1 (Grothendieck–Galois via the colimit lift) is the textbook case: SGA1 Exp. V has this exactly, and so does every treatment of étale fundamental groups; the graph is catching up to 1960. Graph-completion is useful knowledge-graph maintenance; it is not discovery in sense (a). The theorists correctly label most of their output this way.

**(c) Reformulation vs. rediscovery.** A reformulation changes the *linguistic register* but not the theorem: "Stone duality is Yoneda applied to the two-element object" (A2) is a reformulation of a 1982 observation by Johnstone. A rediscovery is what happens when a mathematician, ignorant of prior work, proves the same theorem from scratch; this is common in human mathematics (chakravāla and Fermat's descent; Abel and Ruffini) and does not count as discovery *in 2026 with a literature search available*. Because the team has no web search, some of what they self-grade as LIKELY-KNOWN may be literature-gap hedging rather than genuine rediscovery, but the epistemic ceiling is the same: if the literature has it, it isn't new.

**(d) Role of the precursor theorem.** Every iter-3 candidate sits at recursion-depth-1 from its precursor: take a named terminal theorem (Noether, Stone, Mordell–Faltings, Gödel), apply one technique that the graph has not yet applied, get a derived statement. By construction, the output shares the precursor's conceptual shape. If the technique is drawn from the same era/tradition as the precursor (compactness on a cyclic quadrilateral; Yoneda on Stone), the product is almost always a known corollary — the mathematical community has already followed every such obvious edge. If the technique is drawn from *a different era or tradition* (Walsh analysis on Gödel; polynomial method on Mordell), the product has a genuine chance of being new, because the cross-tradition move has not always been attempted.

My working definition for this assessment: a candidate *counts as a discovery* if either (i) it meets test (a), or (ii) after a reasonable literature check the statement is not findable in published mathematics, and (iii) the derivation adds mathematical content beyond composing pre-existing theorems. The candidates must pass all three; passing (ii) alone gets them classified as "plausibly new, pending verification".

By this standard, the bar for declaring a candidate a discovery is high. I apply it per-candidate in §2.

---

## §2 — Per-candidate verdict

### A1 — Grothendieck–Galois via colimit lift
**Theorist grade**: COROLLARY-OF-KNOWN. **My grade**: COROLLARY-OF-KNOWN, agreed. The statement *FinSep(K)^op ≃ FinCont-Gal(K̄/K)-Set* is Grothendieck, SGA1 Exp. V (1960–61), and is in every graduate text (Szamuely, Lenstra, Milne ANT). The "colimit of finite Galois correspondences" framing is how the theorem is *always* taught. Meaning: there is no new structure here; the category-theoretic language makes the proof cleaner but does not change what is provable. Discovery? No. This is a graph-completion edge. Value is pedagogical — the graph should have had this.

### A2 — Representable-functor formulation of Stone duality
**Theorist**: COROLLARY-OF-KNOWN. **Me**: COROLLARY-OF-KNOWN, agreed. Johnstone's *Stone Spaces* §VI.3 (1982) frames dualities via dualising objects precisely this way; Lambek–Scott and Mac Lane–Moerdijk make it the canonical example. Stone's 1936 embedding theorem is the one-line corollary. The only novelty is the identification of (**2**, **Ω**) as a *pair* of dualising objects, which is standard once you accept the categorical viewpoint. Discovery? No — graph-completion.

### A3 — Forcing-parametrised Stone duality ("P-Stone spectrum")
**Theorist**: LIKELY-KNOWN core + SPECULATIVE fingerprint. **Me**: **I disagree modestly — I'd grade the core COROLLARY-OF-KNOWN and the fingerprint LIKELY-KNOWN-UNDER-OTHER-NAME**, rather than a harder-to-pin "SPECULATIVE". The core is Boolean-valued models / Boolean ultrapowers, worked out by Scott, Solovay, Vopěnka and Bukovský in the 1960s–70s; Jech's *Set Theory* (3rd ed.) treats this in Ch. 14. The fingerprint for ω* is Balcar–Simon, Rudin 1956, Shelah–Veličković 1989, Farah–Shelah: automorphisms of ω* are nontrivial under CH and trivial under PFA (Shelah's theorem, made definitive by Veličković). The theorist correctly cites this literature. The claim that "Spec_P is functorial in P with a characterisable kernel beyond ω*" is a reasonable conjecture that is probably either folklore in the set-theoretic topology community or a special case of Farah's work on Čech–Stone remainders. Meaning: this is the most *interesting* of the A-side because it identifies a real structural question (how does forcing change the Stone spectrum?), but I do not see a specific open problem here that isn't covered by the existing automorphism-of-ω* literature. Discovery? No — rediscovery under categorical wrapping. Recommendation: not worth prioritising for proof-writing.

### A4 — Poncelet n=4 via compactness
**Theorist**: COROLLARY-OF-KNOWN. **Me**: COROLLARY-OF-KNOWN, agreed — but with a caveat. The Bos–Kers–Oort–Raven survey (1987) gives the compactness-route Poncelet proof. The derivation as written is *incomplete* — step 6 (elliptic-curve translation structure) is doing the real work, and the "compactness argument" is cosmetic on top of Griffiths–Harris 1977. That is, the technique the graph applied (`t_compactness_argument`) is not the load-bearing ingredient. Discovery? No; this is a mis-labelling of what is really an elliptic-curve argument.

### A5 — Sheaf-cohomological obstruction to invariant subspaces
**Theorist**: LIKELY-KNOWN-UNDER-OTHER-NAME. **Me**: **Partial disagreement**. The sheaf-theoretic framework exists (Eschmeier–Putinar 1996, Putinar's earlier work, Apostol 1968–1980s, Bishop–Vasilescu functional calculus) and the obstruction-class language is natural inside it. But I would distinguish two sub-claims: (i) a cohomological *reformulation* of ISP, and (ii) the *specific* sheaf `ℱ_T = H/(T−λ)H̄` with stalk described. Sub-claim (i) is Eschmeier–Putinar; sub-claim (ii) is the standard "quotient sheaf" construction and is plausibly novel in this exact phrasing though it is a cosmetic variant of what they already do. More important: the reformulation *does not reduce* to the quasinilpotent case, which is where ISP is actually stuck. So the candidate has the structural defect that it is strongest precisely where ISP is easiest (compact T, disconnected-spectrum T) and weakest where ISP is hardest (σ(T) = {0}). Meaning: this is wrapping, not content. Discovery? No.

### A6 — Dyadic martingale structure for Archimedes' 96-gons
**Theorist**: COROLLARY-OF-KNOWN. **Me**: agreed, but **I'd downgrade further to TRIVIAL or "pedagogical observation"**. The inscribed/circumscribed sequences are monotone and bounded, so they converge; dressing them as sub/super-martingales with respect to the dyadic filtration generated by polygon vertices adds no mathematical content — it is an instance of the general fact that any monotone bounded sequence becomes a (sub-/super-)martingale under the canonical filtration that refines it. The O(2^{−2n}) rate is Taylor-expansion of sin(θ/2)², pre-existing in every calculus text. Meaning: *none*. Discovery? No — this is exposition.

### A7 — Character decomposition of S₅ orbits on splitting fields
**Theorist**: LIKELY-KNOWN-UNDER-OTHER-NAME. **Me**: agreed. The character-theoretic non-solvability observation is 19th-century (Frobenius) and the effective Galois-group algorithm is Stauduhar 1973, deployed in PARI/GP, Magma, SageMath for fifty years. The standard representation's non-induction from solvable subgroups is a standard exercise. Meaning: graph-completion in the graph's Galois chain. Discovery? No.

### B1 — Spectral Noether theorem
**Theorist**: COROLLARY-OF-KNOWN. **Me**: agreed, with emphasis — this is *free-theory folklore*. The hypothesis that the symmetry commutes with spatial translation kills everything interesting; as the theorist acknowledges, this rules out gauge symmetries, which is exactly where the non-trivial version of this story lives (BRST, Ward identities, soft-pion theorems). What's left is Parseval: a free theory decomposes into independent oscillators, and each has its own conserved charge. Meaning: none that isn't in Weinberg Vol. 1 Ch. 7. Discovery? No.

### B2 — Polynomial-method Chabauty bound
**Theorist**: LIKELY-KNOWN-UNDER-OTHER-NAME. **Me**: **Partial disagreement — I would grade this LIKELY-KNOWN for points 1–2 but I am less sure about point 3.** The Stoll / Katz–Rabinoff / Dimitrov–Gao–Habegger (2021) uniform Mordell programme occupies this space, with bounds of shape O((2g−2)·p^{r/g})-ish arising naturally. Bilu–Rémond–Galateau have polynomial-method-on-abelian-varieties arguments that look structurally close. But the *specific* constant `(2g−2)·p^{r/g}` via Croot–Lev–Pach on an abelian variety (rather than `𝔽_p^n`) is, on my reading, not a standard statement; the literature reaches analogous bounds through Chabauty–Coleman with ℓ-adic logarithms rather than CLP polynomials. If this derivation actually works — and step 5 is risky — it might be a modest technical contribution, not a new theorem but a new proof of a known-shape theorem. Discovery? No; technique-transfer of mild interest.

### B3 — Local CLT on arithmetic progressions via circle method
**Theorist**: LIKELY-KNOWN-UNDER-OTHER-NAME (effectively TRIVIAL). **Me**: **I'd downgrade to COROLLARY-OF-KNOWN or TRIVIAL.** The local CLT for lattice distributions on APs is in Petrov's *Limit Theorems of Probability Theory* and in every analytic-number-theory text that treats the circle method. The `O(q·n^{−1})` error is Esseen-smoothing + character orthogonality, textbook in Tenenbaum Part II. The `n^{1/2}` uniformity claim (point 3) is Bombieri–Vinogradov-style and *much harder* than the derivation admits; conflating the easy and hard claims is the main risk here. Meaning: graph-completion. Discovery? No.

### B4 — Walsh spectrum of the provability predicate
**Theorist**: PLAUSIBLY-NEW (with caveats). **Me**: **Agreed, PLAUSIBLY-NEW at the level of statement. This is the only candidate I would promote to "worth verification effort".** Two reasons to take it seriously: (i) the combination *Walsh analysis × formal provability* is not a standard combination in the literature I know; Razborov–Smolensky circuit lower bounds for arithmetic and Krajíček's forcing in bounded arithmetic are the closest, but they are not this statement. (ii) The LMN concentration for the *truncated* provability predicate (proofs of length ≤ L) is a genuine corollary of LMN 1993 because a proof verifier is a low-depth circuit, so point 2 should hold once the depth/size accounting is done. (iii) Point 3 — sparsity of the Gödel sentence itself — is the actually interesting speculation and it is not obvious.

Reasons for residual scepticism: (a) Gödel numberings are not canonical; sparsity of Ĝ may be numbering-dependent and thus not a property of `G` but of the encoding. This is the same issue Chaitin's Ω suffers — Ω depends on the universal machine — and the candidate does not adequately address it. (b) The proof-theoretic literature (Krajíček's *Bounded Arithmetic, Propositional Logic, and Complexity Theory*; Cook–Nguyen; Beckmann) may contain spectral statements about bounded provability that this candidate rediscovers. A literature check in proof complexity is needed. (c) Aaronson–Drucker and more recent AI-safety work on Boolean Fourier of bounded computations sit nearby.

Conditional conclusion: if a proof-complexity specialist hasn't written this down in the last 10 years, this is a small but genuine discovery — not in the Wigner sense, but a plausible new connection between two mature toolboxes. Meaning: provability *as a Boolean function* is a quietly different object than provability as a formula, and low-degree concentration would be the analytic fingerprint of bounded-depth verifiers. Discovery? **Plausibly, yes — conditional on literature clearance.** I recommend this for B-priority: write it up, search the proof-complexity literature carefully, then decide.

### B5 — Syntactic current (conserved quantity on the proof graph)
**Theorist**: LIKELY-KNOWN-UNDER-OTHER-NAME. **Me**: agreed. This is a reformulation of Gentzen's ordinal assignment (ε_0) and Lawvere's categorical fixed-point theorem. The "holonomy class in H^1(Γ_T)" is plausibly expressible as something in the Gentzen / Takeuti proof-theoretic derived category tradition, and more likely already expressed as such by Girard in *Proof Theory and Logical Complexity* or Troelstra–Schwichtenberg. The claim that the Gödel sentence is a non-trivial holonomy class is Lawvere's 1969 diagonal argument in dressed-up form. Meaning: a change of wrapping on an old theorem. Discovery? No.

### B6 — Sylow density via pigeonhole on conjugation orbits
**Theorist**: LIKELY-KNOWN-UNDER-OTHER-NAME (points 1–2), PLAUSIBLY-NEW (point 3). **Me**: **Disagreement — I'd grade points 1–2 more harshly (COROLLARY-OF-KNOWN / elementary) and I'd grade point 3 more sceptically too.** The `|G|`-independent cover bound is a volume-argument on Hamming-type spaces and follows from standard metric-entropy estimates; the specific application to Sylow subgroups, indexed by Hamming distance, is a clean observation but not a theorem in the sense needed. Pyber, Liebeck–Pyber, Babai–Pyber, Jaikin-Zapirain have extensive work on asymptotic subgroup structure with covering-type bounds. Point 3 (tightness via `G = H × H × ...`) is plausibly-known in finite group theory folklore. Meaning: modest combinatorial bookkeeping, no structural content. Discovery? No.

### B7 — Quantitative Waring via refined Farey dissection
**Theorist**: LIKELY-KNOWN-UNDER-OTHER-NAME. **Me**: agreed. `G(k) ≤ (1+ε)·k·log k` for large `k` is, modulo constants, the state of the art after Wooley's and Bourgain–Demeter–Guth's 2016 resolution of Vinogradov's mean-value theorem; the three-level Farey dissection is standard in Vaughan's *Hardy–Littlewood Method* 2nd ed. Ch. 5. Meaning: graph-completion inside the circle-method subgraph. Discovery? No.

**Per-candidate summary**. Of 14 candidates, I see **1 plausibly-new (B4)**, **2 where my grade is stricter than the theorist's** (A6 downgrades to trivial, B3 downgrades to trivial/COK), and **1 where my grade is subtly different but not more lenient** (A3's speculative fingerprint is more likely a reformulation of existing ω*-automorphism results than a novel conjecture). No candidate has merited an *upgrade* from COROLLARY-OF-KNOWN to PLAUSIBLY-NEW against the theorist's assessment, except possibly B4 which the theorist *already* graded plausibly-new and where I would only add conditional endorsement.

---

## §3 — What the grade distribution means

Of 14 candidates the overall distribution is roughly: **1 PLAUSIBLY-NEW (B4), 7 LIKELY-KNOWN-UNDER-OTHER-NAME, 5 COROLLARY-OF-KNOWN, 1 mixed**. The theorists' harsh self-grading is essentially honest; my adjustments are smaller than the theorists' own range.

Three hypotheses are offered in the philosopher's brief:

**(A) The graph's techniques × states matrix is near-saturated.**
**(B) Recursion-depth-1 from precursor is too shallow.**
**(C) The technique vocabulary at this abstraction level is vocabulary-complete; missing edges are literature-gap edges not theorem-gap edges.**

I argue for a **combination of (B) and (C), with (C) as the dominant factor**. Here is the case.

The recon report identifies 172 forward-boundary nodes and 170 zero-interaction cross-cluster pairs. These are *graph-structural* gaps. The fact that every top-10 technique is absent from cluster 12 is a graph-internal fact, not a fact about what mathematics is missing; SGA1 is *extensive* on compactness × categorical machinery, it is just that nobody has typed those edges into this JSON. When a theorist pushes `t_category_theoretic_colimits_and_adjoints` onto `s_galois_correspondence`, the output is Grothendieck's étale fundamental-group formalism; that pairing exists in every algebraic geometer's head, but *of course* it is not in a 752-node graph that was hand-curated from narrative chapters.

This is the core diagnostic. The recon has correctly identified that the graph is incomplete; the theorists have correctly observed that filling those holes almost always produces known mathematics; the combination tells us the recon is doing graph-completion search, not theorem-discovery search. That is hypothesis (C), and it is a structural fact about the method, not a failure of the team.

Hypothesis (A) is the weaker version of (C). Technically the matrix is not saturated — the theorists can generate more candidates if asked — but the (technique, precursor) pairs that are both (i) absent from the graph and (ii) productive of *new* mathematics are almost a null set at recursion-depth-1, because the literature has already followed every such edge within a given tradition.

Hypothesis (B) has force for the specific winner B4. The depth-1 recursion from `s_self_referential_godel_sentence_G` via `t_frequency_decomposition` lands in a cross-tradition territory (proof theory × Boolean Fourier) precisely because the graph's cluster structure happens to have kept those traditions separate. So *some* depth-1 recursions *do* produce plausibly new material — the ones that bridge clusters whose working mathematical communities don't overlap. This is a refinement of (B): depth-1 is fine *if the cluster-crossing is semantic as well as syntactic*. The recon's "cross-cluster analogy" table (§5) is explicitly targeting exactly this property.

The predictable-productive recipe: find pairs (technique P, precursor state S) such that P and S come from traditions that do *not* already have a canonical cross-reference in the published literature. Apply P to S. The output is a candidate. Check whether the two traditions' communities have discovered each other in the intervening years (often they have). If they haven't, you have a candidate at the Wigner level or close to it.

By this diagnostic, I would expect the ratio to *improve* for depth-2 recursions, but not because the mathematics gets harder — rather, because depth-2 reduces the likelihood that a single specialist has already connected the relevant ideas. A two-step chain is less likely to be a named theorem in any one subfield's textbook. On the other hand, depth-2 makes proof-integrity-risk explode, because each uncontrolled step compounds. My best guess is that depth-2 gives a ratio of maybe 1 in 5 plausibly-new, with a corresponding rise in wrong-or-vacuous candidates.

Implication for the method: *this is working as designed*. An automated recon that finds missing edges will produce graph-completion candidates. The 1-in-14 PLAUSIBLY-NEW ratio at depth-1 is roughly the base rate for "cross-tradition recon-driven proposals over-a-curated-1000-node-graph". If you run the exercise again on a *different* graph, or on a graph that had already absorbed the iter-3 edges, the new plausibly-new candidates would most likely sit in the corresponding new cross-cluster-gaps — i.e. C07×C04 (B4's location), C07×C11, C07×C12 (the theorist B's own extrapolation).

The deeper lesson is that *the graph is a map of what the team has written, not a map of what mathematics has proven*. Until the graph is made to span the actual literature — something no team of seven humans can do — the graph-completion interpretation will remain correct.

---

## §4 — When should this method be trusted?

The machinery "apply existing technique P to edge state S" is a useful research heuristic. It fails in predictable ways. Here are the conditions I would require a candidate to meet before treating it as a live discovery:

**(i) Cross-tradition check.** Are P and S drawn from mathematical sub-communities that routinely talk to each other? If yes (compactness × analysis, Yoneda × category theory, circle method × additive number theory), the candidate is almost certainly COROLLARY-OF-KNOWN; the experts in both traditions have thought about the combination. If no (Walsh analysis × Gödel incompleteness, ergodic theory × operator algebras pre-1970, polynomial method × curves), the candidate has a chance. The iter-3 batch confirms this: every candidate with intra-tradition (P, S) is graph-completion; the only plausibly-new candidate is cross-tradition.

**(ii) Load-bearing step audit.** When the derivation is written out, is the named technique actually doing the work, or is it cosmetic? A4's compactness argument is cosmetic; the elliptic-curve translation structure (step 6) is load-bearing. A6's martingale wrapping is cosmetic; monotone convergence is load-bearing. If the named technique is not the binding step, you have rediscovered the binding step's theorem in new language. Test: write the proof without the named technique. If it still goes through, the named technique is not earning its place.

**(iii) Failure-mode robustness.** Does the statement degrade gracefully outside its hypotheses, or does it collapse to vacuity? A5's obstruction vanishes trivially on the quasinilpotent case, which is exactly where ISP is open — vacuous at the interesting spot. B1 requires the symmetry to commute with translation, which rules out every interesting gauge theory. If the interesting cases are *excluded by hypothesis*, the theorem is harmless and lives inside a trivial subclass.

**(iv) Literature-gap vs. theorem-gap.** The critical distinction. "Not in the graph" is a graph fact; "not in the literature" is a mathematics fact. These are different properties by a factor of maybe 50:1 for the current graph. Checks: (a) does a textbook on the *precursor's home field* have it? (b) does a survey by a leading practitioner cite it? (c) has the cross-tradition been attempted by a prior researcher with both backgrounds? For B4 the answer to (a) is probably no (proof theory texts don't do Walsh analysis), to (b) is unclear, to (c) is the risk. For A1–A7 the answer to (a) is yes.

**(v) External-fact cost.** Every derivation sketch flags "external facts required". Count them. If the derivation needs three pieces of external machinery (Krull topology, Apostol decomposition, Wooley's mean-value theorem), the named technique is the glue, not the mathematics. At some point the candidate is *a composition of known deep theorems*, which is not a new theorem; it is a piece of exposition.

**(vi) Proof-integrity risk × specialist access.** The team grades proof-integrity risk, which is honest self-assessment. But the risk is uneven: MEDIUM-HIGH on A5 means the theorist is waving at Eschmeier–Putinar; LOW on A2 means Yoneda is mechanical. Candidates with MEDIUM risk in unfamiliar literatures (B2 polynomial-method-on-abelian-varieties, B4 proof-complexity lower bounds) have hidden literature traps.

**A usable rubric.** A candidate deserves a proof-writing effort only if: cross-tradition (i); the named technique does more than dress (ii); the statement is nontrivial on the interesting cases (iii); a literature-gap check of the *target tradition*, not just the precursor tradition, shows absence (iv); the external-fact count is ≤ 1 (v); and the risk is controllable by the writers (vi).

Applying the rubric to iter-3: only **B4** passes all six tests cleanly, and it only passes (iv) conditional on a proof-complexity literature clearance that the team could not perform (no WebSearch). A3 passes (i) and (iv) weakly, but fails (ii) — the representable-functor wrapping is cosmetic over the forcing-Stone combination which Scott–Solovay already did.

This rubric implies that the team's output is approximately correctly graded. The deeper implication is that the *method* should be scored not by hit rate on novelty but by hit rate on *candidates that pass rubric (i–vi)*. By that metric, 1/14 is fine; by the metric "interesting theorem production", 1/14 over a well-curated knowledge graph is honest.

---

## §5 — Counter-question: any grade I'd raise?

One candidate has a claim I take more seriously than the theorist does: **A3's automorphism-fingerprint conjecture, restricted to forcings generic enough to kill the ω*-automorphism structure.** The Shelah–Veličković result says `Aut(ω*)` is trivial-modulo-inner under PFA and nontrivial under CH. Generalising this to `Aut(Spec_P(B))` for different `P` and `B`, with the statement "the automorphism group mod inner is an invariant of the forcing equivalence class of P", is *probably* folklore in set-theoretic topology but I am not certain it has been written down in exactly this form outside of special cases (Farah's work on coronas and Čech–Stone quotients). The theorist flagged this as SPECULATIVE; I'd flag it as LIKELY-KNOWN but *worth a literature pass*, because if Farah or Dow has not written it, it would be a modest contribution to set-theoretic topology. Not a Wigner-level discovery but a real one. My grade adjustment: from SPECULATIVE to PLAUSIBLY-NEW-PENDING-VERIFICATION, i.e. a soft *raise*.

One candidate I would *lower*: **A6, dyadic martingale for 96-gons.** The theorist calls it COROLLARY-OF-KNOWN; I call it an exposition exercise. The martingale wrapping adds nothing mathematical. A better use of the Archimedes node would be to apply `t_reduce_to_canonical_form` in a way that targets the *rate* of convergence as a function of angle-halving iteration depth, potentially linking to the theory of continued-fraction approximants to π — that direction would at least produce a result with number-theoretic content.

A hedged observation on **B2** (polynomial method on curves in Jacobians): if Bilu–Rémond–Galateau haven't done this exact bound, the proof of point 2 is a modest technical contribution to effective Mordell, with a proof route distinct from p-adic Chabauty. I would not call it a discovery — the shape of the theorem was anticipated — but I would call it a worth-writing-up result. Theorist graded LIKELY-KNOWN; I would soft-raise to PLAUSIBLY-NEW-AT-PROOF-LEVEL, not at statement level.

In short: the candidate distribution is mostly honest, my adjustments are minor, and **B4 remains the only plausibly-new statement**. The team has performed graph-completion well; they have not performed discovery, except arguably once. I disagree with the framing that this is a failure. The method is doing what it is instrumented to do, and the data from this iteration is informative about how and where to look in iter-4 (cross-tradition gaps with large semantic distance, depth-2 chains, and external-fact cost ≤ 1).

Recommendation to the team: proceed to B4 as the sole proof-writing target; treat A1–A7 and B1, B3, B5, B6, B7 as graph-enrichment edges (write them into the knowledge graph with citations to the literature); optionally explore B2's proof and A3's fingerprint as literature-clearance tasks, not discovery tasks.

---

**Word count**: ~3900 words.
