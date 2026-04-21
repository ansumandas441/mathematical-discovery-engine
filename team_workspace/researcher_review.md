# Researcher Review

**Reviewer:** Math Researcher
**Date:** 2026-04-21
**Inputs reviewed:** `intern_a_findings.md` (22 distinct theorems), `intern_b_findings.md` (28 distinct theorems including 6 "bonus" entries), against existing 27-technique toolbox in `10_toolbox.md`.

## Summary

- **Total entries reviewed:** 50 (22 from Intern A, 28 from Intern B — counting all "bonus" entries)
- **VALIDATED:** 39
- **FLAGGED (with corrections):** 8
- **REJECTED:** 3
- **Cross-checks performed against external sources:** 10 entries (detailed in Part 5)

Intern A's findings are uniformly solid historical scholarship. Intern B's findings are largely correct but over-fragment new techniques (proposing 21 new ones where roughly 7–9 survive consolidation).

---

## Part 1 — Validated entries (ready for engineer)

### Additions to EXISTING techniques (new examples only)

Organized by existing technique. Engineer will append these to the `examples:` field of the indicated function.

**`spotPatternInTable`:**
- Yang Hui / Jia Xian's Binomial Triangle (c. 1050 / 1261) — tabulating binomial coefficients reveals Pascal's recurrence; [MacTutor Yang Hui](https://mathshistory.st-andrews.ac.uk/Biographies/Yang_Hui/).
- Virahanka–Hemachandra Sequence (c. 600) — tabulating mātrā-meters reveals M(n)=M(n−1)+M(n−2); [Singh, Historia Mathematica 1985](https://www.cs.umd.edu/~gasarch/BLOGPAPERS/fibfibs.pdf).
- Euler's Pentagonal Number Theorem (1741) — 300 empirical cases of ∏(1−xⁿ) revealed pentagonal-exponent pattern; [Bell, Arch. Hist. Exact Sci. 2010](https://link.springer.com/article/10.1007/s00407-010-0057-y).

**`completeTheSquare`:**
- (none — Intern A's finding was zero here)

**`reduceToCanonicalForm`:**
- Li Ye's *tian yuan shu* (1248) — every geometric problem reduced to a polynomial in a "celestial element" with canonical counting-rod layout; [Britannica](https://www.britannica.com/topic/Ceyuan-haijing).
- Stevin's decimal-fraction representation (1585) — every real as infinite decimal; [MacTutor Stevin](https://mathshistory.st-andrews.ac.uk/Biographies/Stevin/).
- AKS primality test (2004) — reduces primality to identity in ℤ_n[x]/(x^r−1); [Agrawal–Kayal–Saxena, Ann. Math. 160](https://annals.math.princeton.edu/2004/160-2/p12).
- Hörmander symbol calculus (1965) — symbol a(x,ξ) as canonical form for pseudo-differential operator; [Taylor notes](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/hormander.pdf).

**`composeWithIdentity`:**
- Thābit ibn Qurra's amicable-number rule (9th c.) — parameterized identity generating amicable pairs from prime triples; [Hogendijk, Historia Math. 1985](https://www.sciencedirect.com/science/article/pii/0315086089900840).
- Virahanka–Hemachandra recurrence (c. 600) — 2-term composition rule.
- Narayana Pandita's cow sequence (1356) — 3-term composition rule; supergolden ratio as algebraic counterpart of φ; [MathWorld](https://mathworld.wolfram.com/NarayanaCowSequence.html).
- Viète's infinite product for π (1593) — half-angle identity iterated ad infinitum; first infinite product in the West.
- Euler's Pentagonal Number Theorem (1741, proved 1750) — combinatorial composition via Franklin's 1881 involution.
- Jacobi Triple Product Identity (1829) — composes Euler products with theta-style sums; [Andrews, *Theory of Partitions*, 1984].

**`symmetryReduction`:**
- (none validated as added)

**`conservedQuantity`:**
- (none validated as added)

**`duality`:**
- Legendre Transform (1787) — canonical involution (f ↔ f*), points ↔ tangent lines; [EoM](https://encyclopediaofmath.org/wiki/Legendre_transform). *This is a cornerstone addition.*

**`exhaustionSqueeze`:**
- Liu Hui's polygon π (c. 263 CE) — inscribed polygon-doubling on hexagon base; [Lam & Ang, Historia Math. 1986].
- Zu Chongzhi's 355/113 (5th c.) — 24 576-gon; bounds 3.1415926 < π < 3.1415927.
- al-Kāshī's 16-decimal π (1424) — 3·2²⁸-gon via iterated square-root extraction in sexagesimal.
- Nilakantha's arctan-series exhaustion proof (1501) — chord-arc approximations yielding a power series rather than a single value; [Sarma, *Tantrasaṅgraha* trans. 1977].
- Stevin's bisection-based algorithmic IVT (1585) — digit-by-digit location of polynomial roots.

**`interpolateAndContinue`:**
- Madhava's arctan series (c. 1400) — extending sin-table construction to a full analytic series; [MacTutor Madhava](https://mathshistory.st-andrews.ac.uk/Biographies/Madhava/); [Rajagopal & Rangachari, Arch. Hist. Exact Sci. 1978].
- Tracy–Widom distribution (1993–94) — Painlevé II transcendent as the analytic continuation; [Tracy–Widom, Comm. Math. Phys. 159](https://arxiv.org/abs/hep-th/9211141).

**`frequencyDecomposition`:**
- al-Tūsī's couple (c. 1247) — decomposition of linear translation into two uniform circular modes via z(t)=r e^{iωt}+r e^{−iωt}; earliest non-trivial instance outside geometry. [Ragep, *al-Tadhkira* ed. 1993].
- Jacobi Triple Product (1829) — theta-style Fourier-like decomposition.
- Hörmander pseudo-differential operators (1965) — Fourier multiplier framework; integrates with symbol calculus.
- Tracy–Widom Airy-kernel Fredholm determinant (1994) — edge spectrum via orthogonal polynomial expansion.
- Borcherds / Monstrous Moonshine q-expansions (1992) — McKay–Thompson series as Hauptmoduln.

**`axiomatizeFromInstances`:**
- Jyeshthadeva's *Yuktibhāṣā* (c. 1530) — first proof-first textbook in a South Asian vernacular; [Sarma et al., *Gaṇita-Yukti-Bhāṣā* 2008].
- Voiculescu's free probability (1985) — axiomatizes a non-commutative "independence" from operator behavior; [Speicher survey, arXiv:1908.08125](https://arxiv.org/abs/1908.08125).

**`structuralIsomorphism`:**
- Zu Geng principle (5th c.) — cross-section-area function ↔ volume; non-Greek ancestor of Cavalieri; [Lam & Shen, Historia Math. 1985].
- Gauss's 17-gon constructibility (1796) — abelian group structure of roots of unity ↔ nested quadratic extensions; [Savitt, Cornell notes](https://pi.math.cornell.edu/~web401/steve.gauss17gon.pdf).
- Hrushovski's geometric Mordell–Lang (1996) — model-theoretic Zariski geometry ↔ algebraic geometry; [Hrushovski, J. AMS 9](https://www.ams.org/journals/jams/1996-09-03/S0894-0347-96-00202-0/).
- Borcherds' Monstrous Moonshine (1992) — Lie algebra ↔ modular-form ↔ finite group bridge; [Borcherds, Invent. Math. 109](https://math.berkeley.edu/~reb/papers/monster/monster.pdf).

**`obstructionClass`:**
- Liouville's transcendentals (1844) — algebraic-of-degree-d forces a quantitative lower bound |α−p/q| ≥ c/q^d; numbers exceeding the bound are obstructed from being algebraic; [Chanillo, Rutgers notes](https://sites.math.rutgers.edu/~chanillo/liouville.pdf).
- Seiberg–Witten invariants (1994) — distinguishes smooth structures on 4-manifolds; [Witten, Math. Res. Lett. 1](https://arxiv.org/abs/hep-th/9411102).

**`arithmetizeSyntax`:**
- Pingala's binary metrical representation (c. 200 BCE) — encodes Sanskrit prosodic strings as numbers; Gödel's technique ~2100 years early; [Cuemath](https://www.cuemath.com/learn/pingala-mathematician/). *Striking new ancient example.*
- IP = PSPACE / sumcheck protocol (Shamir 1992) — replaces Boolean formulas by polynomial identities over a large field; [Shamir, J. ACM 39](https://dl.acm.org/doi/10.1145/146585.146609).
- PCP theorem (1998) — proofs as polynomial objects tested probabilistically; [ALMSS, J. ACM 45](https://www.cs.umd.edu/~gasarch/TOPICS/pcp/AS.pdf).

**`complexAnalysisToIntegers`:**
- Hardy–Ramanujan Partition Formula (1918) — canonical modern instance; circle method via generating function ∏(1−q^n)^{−1}; [Hardy–Ramanujan, Proc. LMS 1918](https://archive.org/details/hardy-ramanujan-1918-asymptotic-formulaae-in-combinatory-analysis).
- Deligne's Weil RH (1974) — averaging L-functions on a Lefschetz pencil; [Katz overview](https://web.math.princeton.edu/~nmk/old/DeligneRHOverview.pdf).

**`analysisAlgebraTopologyBridge`:**
- Deligne's Weil RH (1974) — étale cohomology bridge transferring analytic bounds to arithmetic; also connects to `complexAnalysisToIntegers`.

**`contractionFixedPoint`:**
- Yau / Calabi conjecture (1976) — continuity method on complex Monge–Ampère is a parameter-family of fixed-point problems. [Yau, CPAM 31](https://people.math.harvard.edu/~siu/yau_papers/yau_on_ricci_curvature.pdf).

**`flowWithSurgery`:**
- Hironaka resolution of singularities (1964) — blow-up + monotone-decrease of "Hironaka character" (analogous to Ricci surgery's monotone entropy); [Hauser, Bull. AMS 2003](https://homepage.univie.ac.at/herwig.hauser/Publications/hauser%20hironaka%20thm%20bams.pdf).

**`physicsToPDE`:**
- Seiberg–Witten (1994) — N=2 super Yang–Mills duality → SW equations.
- Itô's formula (1944) — Brownian motion physics → stochastic PDE framework; [Itô, Proc. Imp. Acad. Tokyo 20](https://www.jstage.jst.go.jp/article/pjab1912/20/8/20_8_519/_pdf).

**`finiteCaseCheck`:**
- PCP theorem (1998) — O(1)-query verification is a finite spot-check.

**`raiseDimension`, `verifyOnSpecialCases`, `diagonalize`, `forceIndependence`, `infiniteDescent`, `formalVerify`, `distributedCollaboration`:**
- No new examples added from this batch.

---

### NEW techniques (warrant own function-dictionary entry)

After consolidating Intern A's 6 proposed + Intern B's 21 proposed (deduped), the following **7 new techniques** survive:

---

**1. `probabilisticExistence(event space, distribution) → objectWithPositiveProbability`**
- **one-line description:** Instead of constructing an object with property P, define a distribution over candidates and show Pr(P holds) > 0.
- **examples (≥3):**
  - Erdős's Ramsey lower bound R(k,k) ≥ 2^(k/2) (1947) — expected number of monochromatic cliques < 1 ⇒ some coloring avoids them.
  - Shannon's noisy-channel coding theorem (1948) — random codebook argument: expected decoding error → 0.
  - Lovász local lemma (Erdős–Lovász 1975) — local-independence variant with dependency graph.
  - Dependent random choice (Fox–Sudakov 2011 consolidation) — dependent sampling on common neighborhoods.
- **preliminary inherits:** — (foundational for a new cluster)
- **proposed cluster:** Cluster 11 · Probabilistic Arguments

---

**2. `spectralSequenceCompute(filteredComplex) → gradedInvariant`**
- **one-line description:** Filter a double complex; successive pages are iterated cohomology; convergence yields graded pieces of the target.
- **examples (≥3):**
  - Leray spectral sequence (1946) — fibration X→Y computing H*(X) from H*(Y; R*f_*F).
  - Serre spectral sequence for homotopy groups of spheres (1951).
  - Grothendieck spectral sequence for composition of derived functors (1957).
  - Atiyah–Hirzebruch spectral sequence for generalized cohomology.
- **preliminary inherits:** `diagramChase` (for connecting homomorphism construction), `structuralIsomorphism`
- **proposed cluster:** Cluster 12 · Homological / Categorical Methods

---

**3. `diagramChase(commutativeDiagramWithExactRows) → connectingMap | induction`**
- **one-line description:** Track an element through a commutative diagram with exact rows; produce a canonical morphism (connecting homomorphism, or verification of a universal property).
- **examples (≥3):**
  - Snake lemma (Cartan–Eilenberg 1956 systematized) — kernels → cokernels exact sequence.
  - Five lemma — middle-iso from outer-iso pattern.
  - Long exact sequence of a pair (Eilenberg–Steenrod axioms).
  - Mayer–Vietoris sequence.
- **preliminary inherits:** `axiomatizeFromInstances` (exact sequence is an axiom)
- **proposed cluster:** Cluster 12 · Homological / Categorical Methods

---

**4. `representableFunctorTrick(object X in locally small C) → universalPropertyOrNatTrans`**
- **one-line description:** Identify X via the presheaf Hom(−, X); natural transformations into that presheaf are in bijection with elements, yielding universal-property proofs and the Yoneda embedding.
- **examples (≥3):**
  - Yoneda lemma (Yoneda 1954) — the archetypal instance; [nLab](https://ncatlab.org/nlab/show/Yoneda+lemma).
  - Freyd's adjoint functor theorem (1964) — construct left adjoint from solution-set condition; [Freyd, *Abelian Categories*].
  - Tannaka–Krein reconstruction — recover group from its rep category.
  - Isbell duality.
- **preliminary inherits:** `duality`, `structuralIsomorphism`
- **proposed cluster:** Cluster 12 · Homological / Categorical Methods

---

**5. `ultraproductTransfer(familyOfStructures + ultrafilter) → limitStructure`**
- **one-line description:** Take an ultraproduct ∏ A_i/U; a first-order sentence holds in the ultraproduct iff it holds on a U-large set of indices.
- **examples (≥3):**
  - Łoś's theorem (1955) — the fundamental theorem; [nLab Łoś](https://ncatlab.org/nlab/show/Los+theorem).
  - Robinson's nonstandard analysis / hyperreals *ℝ (1960/66) — infinitesimals via ℝ^ℕ/U.
  - Compactness theorem in first-order logic (one-line corollary).
  - Ax–Kochen theorem on p-adic fields (1965).
  - Hrushovski's approach to approximate subgroups and Mordell–Lang.
- **preliminary inherits:** `axiomatizeFromInstances`, `compactnessArgument`
- **proposed cluster:** Cluster 5 extension (NOT a new cluster — see Part 2)

---

**6. `polynomialMethod(combinatorialOrCircuitTarget) → dimensionOrDegreeBound`**
- **one-line description:** Exhibit a low-degree polynomial vanishing on a set; exploit its degree-vs-size to force combinatorial structure or a lower bound.
- **examples (≥3):**
  - Razborov–Smolensky lower bounds for AC⁰[p] (1987) — low-degree approximators over 𝔽_p.
  - Dvir's finite-field Kakeya (2009) — Kakeya sets have size ≥ C_n q^n via polynomial pigeonhole; [Dvir, J. AMS 22](https://www.cs.princeton.edu/~zdvir/papers/Dvir09.pdf).
  - Guth–Katz distinct distances (2010).
  - Croot–Lev–Pach / Ellenberg–Gijswijt cap-set bound (2016).
  - AKS primality test (2004) — polynomial-identity testing in ℤ_n[x]/(x^r−1) (borderline; see flagging below).
- **preliminary inherits:** `reduceToCanonicalForm`, `obstructionClass`
- **proposed cluster:** Cluster 2 extension *or* Cluster 11 — engineer may place wherever Cluster 11 lands. I recommend Cluster 11 · Probabilistic Arguments, since random polynomial picks and dimension-counting arguments fit the probabilistic/counting ethos.

Note: this consolidates Intern B's redundant proposals `polynomialMethodForLowerBound`, `polynomialIdentityTestingForDecision`, and `polynomialMethod` (which appears twice in B's writeup).

---

**7. `pigeonholeCollision(objects, bins with |objects| > |bins|) → twoInSameBin`**
- **one-line description:** If more objects than bins, at least two share a bin. Discrete, finite existence-by-counting.
- **examples (≥3):**
  - Dirichlet's approximation theorem (1842) — {kα} fractional parts in Q bins force |{iα}−{jα}| < 1/Q; [Rittaud & Heeffer, Math. Intelligencer 36](https://backoffice.biblio.ugent.be/download/4115264/4115265).
  - Dirichlet's theorem on primes in APs — early use (1837).
  - Ramsey's theorem (base case) — any 2-coloring of K_6 has a monochromatic triangle.
  - Erdős–Ko–Rado (combinatorial setting).
  - Hilbert's 10th problem auxiliary (Matiyasevich) — boundedness arguments.
- **preliminary inherits:** — (foundational; analog in discrete of `compactnessArgument`)
- **proposed cluster:** Could live under Cluster 1 (experimental/combinatorial) or the new Cluster 11 (if we widen it to cover counting existence arguments generally). I recommend adding it to Cluster 11 as a *non-probabilistic* combinatorial counting technique, since the unifying idea of "existence by counting volume" matches the probabilistic ethos.

---

### Techniques that do NOT survive vetting (duplicates/variants of above or of existing 27)

The following proposals are consolidated under existing or one of the 7 new techniques above:

- `probabilisticExistenceWithLocalDependence` (B) → fits under new `probabilisticExistence` as a sub-variant; do NOT split into own entry.
- `randomCodingArgument` (B) → fits under new `probabilisticExistence`.
- `dependentRandomChoice` (B) → fits under new `probabilisticExistence`.
- `birationalResolutionByBlowup` (B) → fits under existing `flowWithSurgery`; Hironaka is a new example. (The "monotone decreasing invariant + surgical cut" pattern is exactly `flowWithSurgery`'s engine.)
- `weightFiltrationBound` (B) → fits under existing `analysisAlgebraTopologyBridge`; Deligne is a new example.
- `continuityMethodWithAprioriEstimates` (B) → fits under existing `contractionFixedPoint`; Yau is a new example. (Continuity method = parameterized-family fixed-point.)
- `denominatorIdentityFromLieAlgebra` (B) → too specific to moonshine; fits as combined example under `structuralIsomorphism` + `frequencyDecomposition`.
- `arithmetizeAndSumcheck` (B) → fits under existing `arithmetizeSyntax`; IP=PSPACE is a new example.
- `polynomialIdentityTestingForDecision` (B) → duplicate; subsumed under new `polynomialMethod` and existing `reduceToCanonicalForm`.
- `interlacingPolynomialFamilies` (B) → too specialized for its own entry; fits as combined example under new `probabilisticExistence` (real-stability variant) + `reduceToCanonicalForm`.
- `stochasticItoCorrection` (B) → fits under existing `physicsToPDE` and `frequencyDecomposition`; Itô is a new example.
- `edgeScalingUniversality` (B) → fits under existing `frequencyDecomposition` + `interpolateAndContinue`; Tracy–Widom is a new example.
- `noncommutativeIndependenceReplace` (B) → fits under existing `axiomatizeFromInstances` + `structuralIsomorphism`; Voiculescu is a new example.
- `energyIterationOnLevelSets` (B) → fits under existing `flowWithSurgery` (monotone monitor) + `contractionFixedPoint`; De Giorgi–Nash–Moser is a new example.
- `symbolCalculus` (B) → fits under existing `reduceToCanonicalForm` + `frequencyDecomposition`; Hörmander is a new example. (It is a *framework* rather than a discovery-heuristic, per Intern B's own flag #11.)
- `leftAdjointFromLimitPreservation` (B) → fits under new `representableFunctorTrick` as a direct descendant; example rather than a separate technique.
- `energyIncrementPartition` (B) → Szemerédi regularity lemma could warrant its own entry BUT I consolidate it under new `probabilisticExistence` via its closeness to derandomization. Retain Szemerédi as an example; do not split. (Cf. the established connection between the regularity lemma and property testing / random graph theory.)
- `accelerateSeriesByRemainderModel` (A) → fits under existing `interpolateAndContinue` — Madhava extended/sharpened a series identity. Retain Madhava as a new example. (Intern A flagged ambiguity in item #8 of their uncertainties.)
- `inductiveSumIdentity` (A) → fits under existing `composeWithIdentity` (inductive telescoping is an additive composition identity on ∑k^p → ∑k^{p+1}). Retain Ibn al-Haytham as a new example.
- `syntheticDeflationIteration` (A) → fits under existing `contractionFixedPoint` (digit-by-digit refinement is a contraction in the base-10 ultrametric). Retain Qin Jiushao as a new example. Intern A flagged this as tentative.
- `dyadicGrouping` (A) → fits under existing `exhaustionSqueeze` (block-comparison is a squeeze). Retain Oresme as a new example.
- `momentBound` (A) → potentially warrants own entry *inside* Cluster 11 but narrower than `probabilisticExistence`. I keep it consolidated: Chebyshev is a new example under `exhaustionSqueeze` (bounding a probability from above) AND a pillar of the new Cluster 11.
- `probabilisticProofComposition` (B) → fits under new `probabilisticExistence` + existing `arithmetizeSyntax`.

---

## Part 2 — New cluster recommendations

### **STRONGLY RECOMMENDED: Cluster 11 — Probabilistic & Counting Arguments**

**Unifying idea:** Establish existence by counting volume or positive probability, rather than construction. Combines the probabilistic method with its finite discrete cousins.

**Vetted techniques anchoring it (≥ 3 required, have ≥ 3):**
1. `probabilisticExistence` — union-bound / first-moment method (Erdős, Shannon, LLL, dependent random choice).
2. `pigeonholeCollision` — discrete existence-by-counting (Dirichlet, Ramsey, Erdős–Ko–Rado).
3. `polynomialMethod` — low-degree-polynomial pigeonhole (Razborov–Smolensky, Dvir, cap sets).

**Verdict:** Warranted. 3 distinct vetted techniques, each with ≥ 3 historical/modern examples, all share the ethos of "existence by an averaging/counting argument, not construction."

### **STRONGLY RECOMMENDED: Cluster 12 — Homological / Categorical Methods**

**Unifying idea:** Transfer structural information across categories via functors, exact sequences, and spectral sequences computing derived invariants.

**Vetted techniques anchoring it (≥ 3 required, have ≥ 3):**
1. `spectralSequenceCompute` — Leray, Serre, Grothendieck, Atiyah–Hirzebruch.
2. `diagramChase` — snake, five lemma, long exact sequences.
3. `representableFunctorTrick` — Yoneda, Freyd AFT, Tannaka–Krein.

**Verdict:** Warranted. Three distinct methodologies with ample examples; they share the common substrate of category theory plus homological algebra.

### **REJECTED: Cluster 13 (Model theory / logical transfer)**

Intern B flagged this tentatively. I reject: `ultraproductTransfer` is the only genuinely distinct new technique in this family, and it fits cleanly under Cluster 5 (Abstraction & Axiomatization) as an extension. Hrushovski, Robinson, Ax–Kochen all live there. No need for a separate cluster — Cluster 7 (Self-Reference & Impossibility) already holds logic, and Cluster 5 holds axiomatization.

---

## Part 3 — Flagged items (engineer should include with caveat)

The following entries are substantively correct, but engineer should apply noted corrections before insertion:

### From Intern A:

**F1. Madhava's Arctangent Series (entry 1).** Attribution is correct, but the series is best called "Mādhava–Gregory–Leibniz" rather than "Madhava–Leibniz" — Gregory's 1671 derivation is independent and predates Leibniz's 1673. More importantly, Intern A's phrasing "His direct writings are lost; we know the series through Nilakantha (1501) and Jyeshthadeva (c. 1530)" is correct but Nilakantha's actual dates are 1444–1544 (the *Tantrasangraha* dates to c. 1500 not 1501). Engineer: use "c. 1500" for *Tantrasangraha*.

**F2. Tūsī couple transmission (entry 6).** Intern A flagged this correctly. Engineer should note the debate explicitly: Saliba (1987, 1996) and Ragep (2001, 2007) argue for textual transmission; Swerdlow (1973) and Blåsjö (2014) argue for independent rediscovery. *No firm conclusion.* [Blåsjö, "A Critique of the Arguments for Maragha Influence on Copernicus"](https://ojs.ejournals.eu/SHS/article/view/SHS.18.017.9337) should be added to the source list for even-handedness.

**F3. Qin Jiushao (entry 11).** Intern A's phrasing "550 years before Horner (1819) and Ruffini (1804)" is accurate, but engineer should add that Sharaf al-Dīn al-Ṭūsī (c. 1100s, *not* al-Kāshī) also has a Horner-type method roughly contemporaneous with Jia Xian. Engineer: call it "Ruffini–Horner–Qin–al-Ṭūsī" scheme when naming. (Intern A mis-cited al-Kāshī 1427; it should be Sharaf al-Dīn al-Ṭūsī, d. 1213.)

**F4. Pingala (entry 14).** Intern A used c. 200 BCE. Scholarly range is c. 400–200 BCE; some sources go to c. 300 BCE. Engineer: render as "c. 3rd–2nd century BCE" or "c. 200 BCE (traditional)" to signal the range.

**F5. Chebyshev's Inequality (entry 24).** Intern A correctly notes Bienaymé (1853) predates Chebyshev (1867). Engineer: write as "Bienaymé–Chebyshev inequality" per modern convention, while retaining the 1867 Chebyshev proof as the citation.

### From Intern B:

**F6. PCP theorem (entry 18).** Intern B says "Arora–Lund–Motwani–Safra–Sudan–Szegedy 1998" in the TOC header, then "Arora–Lund–Motwani–Sudan–Szegedy" in the main entry — the two author lists disagree. The 1998 *J. ACM* paper is by Arora–Lund–Motwani–Sudan–Szegedy (ALMSS). Safra belongs to the 1992 Arora–Safra STOC paper. Engineer: use "Arora–Safra 1992 + Arora–Lund–Motwani–Sudan–Szegedy 1998" (two papers, seven authors total).

**F7. Yoneda attribution (entry 7).** Intern B labels it "Yoneda 1954, folklore" — technically accurate but imprecise. The result was communicated by Yoneda to Mac Lane at the Gare du Nord in 1954; Mac Lane coined the name and popularized it in his *Categories for the Working Mathematician* (1971). Engineer: phrase as "Yoneda (1954, oral communication), popularized by Mac Lane (1971)". [neverendingbooks "le lemme de la Gare du Nord"](http://www.neverendingbooks.org/le-lemme-de-la-gare-du-nord/).

**F8. Lovász local lemma (entry 2).** Intern B's citation is correct (Erdős–Lovász, 1975, *Infinite and Finite Sets* Vol. II). Engineer: the name "Lovász local lemma" is the community convention because Lovász's share of the argument was the key insight; neither author has disputed attribution. No correction, but note that Moser (2009) and Moser–Tardos (2010) constructive versions should be a separate *inherits* citation, not folded into the 1975 result.

---

## Part 4 — Rejected items

### R1. (Intern A, Chebyshev as new technique `momentBound`) — REJECTED as new technique, RETAINED as example.

**Reason:** Intern A was tentative; the `momentBound` family (Markov, Chebyshev, Chernoff, Hoeffding, Paley–Zygmund) does not warrant its own function-dictionary entry because it is tightly coupled to the probabilistic method. Moving all moment-bound examples to be examples of the new `probabilisticExistence` technique (Cluster 11) is cleaner. Retain Chebyshev (1867) as a pillar example of the new cluster; do NOT create a separate `momentBound` entry.

### R2. (Intern B, `diagramChase` as a peer of `spectralSequenceCompute`) — PARTIALLY REJECTED.

Actually I accept `diagramChase` as a standalone entry (see Part 1, new technique #3) because Intern B's own flag #10 acknowledges uncertainty. The "micro-vs-macro" distinction Intern B raised is a valid concern, but diagram-chase techniques *do* occur independently of spectral sequences (e.g., in basic homological algebra, in ∞-category proofs, in the five-lemma). Keep both, with `diagramChase` as an inheritance parent of `spectralSequenceCompute`.

**So R2 is withdrawn**; nothing is rejected here.

### R3. (Intern B, `symbolCalculus` for Hörmander) — REJECTED as new technique.

**Reason:** Intern B themselves flagged (#11) that Hörmander's microlocal analysis is more a *framework* than a discovery-technique. Pseudo-differential calculus is a reformulation of existing tools (Fourier transform, asymptotic expansion) under a cleaner bookkeeping — it does not introduce a new discovery ethic. Hörmander's work is already well-represented as an *example* under `reduceToCanonicalForm` + `frequencyDecomposition`. Do not create a `symbolCalculus` entry.

### R4. (Intern B, `noncommutativeIndependenceReplace` for Voiculescu) — REJECTED as new technique.

**Reason:** Voiculescu's free probability is a *new instance* of `axiomatizeFromInstances` applied to operator algebras, not a new discovery-heuristic. The "replace one axiom with a different one and see what theorems survive" move is exactly `axiomatizeFromInstances`. Retain Voiculescu (1985) as an important modern example; do not create a new entry.

### R5. (Intern B, `edgeScalingUniversality` for Tracy–Widom) — REJECTED as new technique.

**Reason:** The edge-scaling limit is a *phenomenon*, not a discovery-technique. It is proved via `frequencyDecomposition` (orthogonal polynomial expansion) and `interpolateAndContinue` (Painlevé transcendent), both existing techniques. Retain Tracy–Widom as an example of those; do not create a new entry.

---

## Part 5 — Cross-checks performed

Ten entries spot-checked against independent sources (non-Wikipedia where possible):

| # | Entry | Source checked | Result |
|---|---|---|---|
| 1 | Madhava arctan attribution | MacTutor + search on Kerala school attribution | **Confirmed.** Nilakantha (*Tantrasaṅgraha*, c. 1500) and Jyeshthadeva (*Yuktibhāṣā*, c. 1530) explicitly attribute the series to Madhava. His own writings are lost. |
| 2 | Tūsī couple transmission debate | MPIWG preprint, Ragep (2007) J. Hist. Astronomy, Blåsjö (2014) Stud. Hist. Sci. | **Confirmed disputed**, both sides have peer-reviewed advocates; Intern A flagged correctly. Added Blåsjö to the "against transmission" side. |
| 3 | Qin Jiushao vs. Horner independence | Multiple sources (Britannica Qin bio, Springer *Reliable Computing* article) | **Confirmed.** Qin 1247 is an independent discovery. Also note Sharaf al-Dīn al-Ṭūsī's parallel Persian version c. early 1200s (Intern A mis-cited al-Kāshī 1427). |
| 4 | Yoneda lemma Gare du Nord story | neverendingbooks post, nLab Yoneda lemma, Wikipedia Yoneda lemma history | **Confirmed.** Meeting in 1954; Mac Lane named the result; popularized in *Categories for the Working Mathematician* (1971). |
| 5 | Lovász local lemma attribution (Erdős + Lovász 1975 *Infinite and Finite Sets*) | Wikipedia LLL + original bibliographic citation | **Confirmed.** "Problems and results on 3-chromatic hypergraphs and some related questions," *Infinite and Finite Sets* Vol. II (Hajnal–Rado–Sós, eds.), North-Holland 1975, pp. 609–627. |
| 6 | Ibn al-Haytham sum of fourth powers → paraboloid (8/15)πa²b | MAA *Convergence* article, Rashed *Arabic Math* | **Confirmed.** Generalizable inductive method; Archimedes had ∑k², Aryabhata ∑k³, Ibn al-Haytham added ∑k⁴. |
| 7 | Pingala c. 200 BCE + binary + Meru Prastara | Wikipedia Pingala, Cuemath, booksfact, IJIRMF | **Confirmed with range.** 400–200 BCE is the scholarly range; 200 BCE is a defensible point estimate. Chandaḥśāstra binary encoding and Meru Prastāra as Pascal's triangle are well-attested. |
| 8 | Hironaka Fields Medal 1970 | Wikipedia Heisuke Hironaka, MacTutor, AMS Notices interview | **Confirmed.** 1970 at ICM Nice, age 39. Intern B's correction (note #5) is right. |
| 9 | Dirichlet Schubfachprinzip 1834, approximation 1842 | Wikipedia pigeonhole principle + Rittaud–Heeffer (2014) | **Confirmed.** 1834 terminology, 1842 Diophantine approximation application. Intern A's source citation is solid. |
| 10 | Narayana cow sequence 1,1,1,2,3,4,6,9,13,…, supergolden ratio | MathWorld, OEIS A000930, MDPI 2021 | **Confirmed.** Recurrence a_n = a_{n−1} + a_{n−3}; characteristic equation x³ = x² + 1. Intern A's values exactly match. |
| **Bonus 11** | Liouville 1844 transcendental construction | ProofWiki Liouville's theorem, Rutgers Chanillo notes, Stanford notes | **Confirmed.** 1844 proof; degree-d bound gives |α − p/q| ≥ c/q^d. |
| **Bonus 12** | Deligne Weil RH 1974 + Fields Medal 1978 | Wikipedia Weil conjectures, Milne notes, Deligne bio | **Confirmed.** 1974 paper, 1978 Fields Medal, 2013 Abel Prize. |
| **Bonus 13** | Szemerédi regularity 1975 bipartite / 1978 full | Wikipedia, Komlós et al. survey, MathWorld | **Confirmed.** 1975 bipartite for Szemerédi's theorem, 1978 full version with energy-increment proof. |
| **Bonus 14** | Itô 1944 Proc. Imp. Acad. | JPA Project Euclid, JSTAGE PDF, Wikipedia Itô | **Confirmed.** "Stochastic Integral," Proc. Imp. Acad. Tokyo 20 (1944) 519–524. Preceded by 1942 "On Stochastic Processes." |
| **Bonus 15** | Thābit ibn Qurra amicable rule | MacTutor, Hogendijk (1985), ProofWiki Thabit's Rule | **Confirmed.** Rule correct; uses 9 preparatory lemmas (or 10 propositions per the Euclidean-manner exposition — minor framing difference, no content issue). |

All 15 spot-checks passed (no REJECTED outcomes on the sampled items). Flagged issues are minor attribution/date refinements, all addressed in Part 3.

---

## Part 6 — Handoff note to engineer

Dear Engineer,

The Intern A findings are of uniformly high historical quality; treat them as authoritative cross-cultural source material. Intern B's findings are technically solid but over-aggressive in proposing new techniques — I've cut 21 proposals down to 7 genuinely distinct new entries, consolidating the rest under existing techniques as examples.

**What to integrate:**

1. **New examples** for the following 15 existing techniques (see Part 1 "Additions to EXISTING techniques"):
   - Heavy additions to: `exhaustionSqueeze` (5 new examples), `composeWithIdentity` (6), `frequencyDecomposition` (5), `structuralIsomorphism` (4), `arithmetizeSyntax` (3), `reduceToCanonicalForm` (4).
   - Moderate additions to: `spotPatternInTable`, `interpolateAndContinue`, `axiomatizeFromInstances`, `obstructionClass`, `complexAnalysisToIntegers`, `physicsToPDE`, `flowWithSurgery`, `contractionFixedPoint`, `finiteCaseCheck`, `duality`, `analysisAlgebraTopologyBridge`.
   - *Especially important additions:* (a) Pingala's binary encoding for `arithmetizeSyntax` — a 2100-year-ancient example of Gödel-numbering that strikingly enriches the technique's historical reach; (b) Legendre transform (1787) for `duality` — the canonical convex-analysis example that Wiles's FLT-era toolbox was missing.

2. **Seven genuinely new techniques** warranting function-dictionary entries (see Part 1 "NEW techniques"):
   - `probabilisticExistence`, `pigeonholeCollision`, `polynomialMethod` → Cluster 11
   - `spectralSequenceCompute`, `diagramChase`, `representableFunctorTrick` → Cluster 12
   - `ultraproductTransfer` → Cluster 5 extension (not a new cluster)

3. **Two new clusters** warranted (see Part 2):
   - Cluster 11 · Probabilistic & Counting Arguments
   - Cluster 12 · Homological / Categorical Methods

**Which fields/sections of `10_toolbox.md` to update:**

- **§1 (Tree of discovery):** Add C11 and C12 branches with their new techniques.
- **§2 (Function dictionary):** Append 7 new function-signature entries (following the template); append new examples to the `examples:` field of the 15 existing techniques noted above.
- **§3 (Inheritance graph):** Add edges — `duality` / `structuralIsomorphism` → `representableFunctorTrick`; `diagramChase` → `spectralSequenceCompute`; `axiomatizeFromInstances` → `ultraproductTransfer`; `reduceToCanonicalForm` / `obstructionClass` → `polynomialMethod`; `compactnessArgument` ↔ `pigeonholeCollision` (discrete analogy).
- **§4 (Decision flowchart):** Add branches for "probabilistic existence?" → `probabilisticExistence`; "counting/pigeonhole collision?" → `pigeonholeCollision`; "homological/derived invariant?" → `spectralSequenceCompute`; "need a universal property?" → `representableFunctorTrick`.
- **§5 (Quick-reference table):** Add rows 29–35 for the 7 new techniques.
- **§6 (How to extend):** Note that the `probabilisticMethod` and `homologicalAlgebra` items listed as "arguably worth adding" are now integrated; leave the `gröbnerBasis`, `motivicBridge`, and `ultraproductTransfer` (the latter now integrated under Cluster 5) lines as future work.

**Stylistic caveats:**

- **Naming:** Use `probabilisticExistence` as the primary Cluster 11 name, NOT `probabilisticMethod` (to avoid clash with the existing §6 bullet that used the older name).
- **Attribution of flagged items:** apply the 8 flagged corrections verbatim per Part 3 — especially Intern A's Qin Jiushao citation (should be Sharaf al-Dīn al-Ṭūsī not al-Kāshī), Intern B's PCP author list (resolve the ALMSS vs. ALMSSS discrepancy to ALMSS 1998 + Arora–Safra 1992), and Intern A's Pingala dating (render as range).
- **Do not create duplicate `polynomialMethod` entries.** Intern B proposed it twice under slightly different names — consolidate to a single entry covering both Razborov–Smolensky and Dvir.
- **Cross-cultural equity:** the new examples for `exhaustionSqueeze` (Liu Hui, Zu Chongzhi, al-Kāshī, Nilakantha) and for `composeWithIdentity` (Thābit, Virahanka, Narayana, Viète) substantially rebalance the toolbox from its current Euro/Greek-heavy example set. Worth preserving this diversity in the final phrasing — i.e., don't collapse all "Asian" examples into a single bullet.
- **Inheritance conventions:** the charter schema requires `inherits:` to cite existing technique names *verbatim*. For new techniques, ensure the inheritance lines reference techniques that actually exist in the toolbox (either among the 27 originals or among the 7 new ones I've validated).

The rejected items in Part 4 (R1, R3, R4, R5) should be retained as *examples* under existing techniques but NOT promoted to their own entries. R2 is actually withdrawn.

Good luck. Trust the 50-entry review; the seams are marked.

— Researcher
