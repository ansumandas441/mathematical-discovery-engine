# Engineer Additions — Toolbox Expansion

**Author:** Computer Engineer (formalizer)
**Date:** 2026-04-21
**Inputs:** `researcher_review.md` (vetted list), `intern_a_findings.md`, `intern_b_findings.md`, current `10_toolbox.md`.

This file contains formatted additions for orchestrator integration into `10_toolbox.md`. No edits to `10_toolbox.md` are made here.

---

## Section A — Example appendages to EXISTING techniques

Append the bullets below to the `examples:` field of the named technique.

## spotPatternInTable — additions
Append these bullets to the `examples:` list:
- **Jia Xian / Yang Hui Binomial Triangle** (c. 1050 / published 1261) — tabulating binomial coefficients to read off Pascal recurrence C(n,k) = C(n−1,k−1) + C(n−1,k); (MacTutor Yang Hui).
- **Virahaṅka–Hemachandra Sequence** (c. 600, Virahaṅka) — tabulating mātrā-meter counts reveals M(n) = M(n−1) + M(n−2); earliest documented linear recurrence. (Singh, *Historia Mathematica* 1985).
- **Euler's Pentagonal Number Theorem** (1741 discovered, 1750 proved) — Euler noticed pentagonal-exponent pattern in ∏(1−xⁿ) after tabulating ~300 cases empirically. (Bell, *Arch. Hist. Exact Sci.* 2010).

## reduceToCanonicalForm — additions
Append these bullets to the `examples:` list:
- **Li Ye's *tian yuan shu*** (1248) — every geometric problem in *Cèyuán Hǎijìng* reduced to a polynomial in a "celestial element" via canonical counting-rod layout; (Britannica *Ceyuan-haijing*).
- **Stevin's decimal-fraction representation** (1585) — every real rendered as an infinite decimal; (MacTutor Stevin).
- **AKS primality test** (2004, Agrawal–Kayal–Saxena) — reduces primality to identity testing in ℤ_n[x]/(x^r − 1); (Ann. Math. 160).
- **Hörmander symbol calculus** (1965) — symbol a(x, ξ) as the canonical form for a pseudo-differential operator; composition and adjoint become asymptotic expansions. *Inherited: reduceToCanonicalForm. Added: Fourier-side bookkeeping.*

## composeWithIdentity — additions
Append these bullets to the `examples:` list:
- **Thābit ibn Qurra's amicable-number rule** (9th c.) — parameterized identity M = 2ⁿ·p·q, N = 2ⁿ·r from prime triple (p, q, r); first nontrivial amicable-pair algorithm. (Hogendijk, *Historia Math.* 1985).
- **Virahaṅka–Hemachandra recurrence** (c. 600) — 2-term additive composition M(n) = M(n−1) + M(n−2) from syllable-length decomposition.
- **Narayana Pandita's cow sequence** (1356) — 3-term composition aₙ = aₙ₋₁ + aₙ₋₃; characteristic root is the supergolden ratio. (MathWorld *NarayanaCowSequence*).
- **Viète's infinite product for π** (1593) — half-angle identity 2cos²(θ/2) = 1+cos θ iterated ad infinitum; first infinite product in Western mathematics.
- **Euler's Pentagonal Number Theorem** (1741/1750) — Franklin's 1881 sign-reversing involution gives the combinatorial composition rule on distinct-part partitions.
- **Jacobi Triple Product Identity** (1829) — composes Euler products with theta-style sums, unifying q-series and modular forms. (Andrews, *Theory of Partitions*, 1984).

## duality — additions
Append these bullets to the `examples:` list:
- **Legendre Transform** (1787) — canonical involution f ↔ f*; points ↔ tangent lines; (f*)* = f; backbone of Hamiltonian mechanics, convex analysis (Fenchel), thermodynamic potentials. (EoM *Legendre transform*).

## exhaustionSqueeze — additions
Append these bullets to the `examples:` list:
- **Liu Hui's polygon π** (c. 263 CE) — inscribed polygon-doubling on hexagon base; explicit passage to limit ("cut again and again until one can cut no more"). (Lam & Ang, *Historia Math.* 1986).
- **Zu Chongzhi's 355/113** (5th c.) — 24 576-gon yielding 3.1415926 < π < 3.1415927; bound stood 900 years.
- **al-Kāshī's 16-decimal π** (1424) — 3·2²⁸-gon via iterated square-root extraction in sexagesimal. (Luckey, *Die Rechenkunst bei al-Kashi*, 1951).
- **Nilakantha's arctan-series exhaustion proof** (c. 1500) — chord-arc squeeze yielding a power series rather than a single real value. (Sarma, *Tantrasaṅgraha* ed. 1977).
- **Stevin's bisection-based algorithmic IVT** (1585) — digit-by-digit location of polynomial roots via decimal interval halving.

## interpolateAndContinue — additions
Append these bullets to the `examples:` list:
- **Mādhava's Arctangent Series** (c. 1400) — extending Aryabhata's sine-table construction to a full analytic series for arctan; (MacTutor Madhava). Referred to in the literature as the Mādhava–Gregory–Leibniz series.
- **Tracy–Widom Distribution** (1993–94) — Painlevé II transcendent continued as the edge-scaling limit of GUE top eigenvalue; (arXiv:hep-th/9211141). *Inherited: interpolateAndContinue. Added: integrable-systems τ-function technology.*

## frequencyDecomposition — additions
Append these bullets to the `examples:` list:
- **al-Ṭūsī's couple** (c. 1247) — linear translation decomposed into two uniform circular modes z(t) = r e^{iωt} + r e^{−iωt}; earliest non-trivial frequency decomposition outside geometry. (Ragep, *al-Tadhkira* ed. 1993).
- **Jacobi Triple Product Identity** (1829) — theta-style Fourier-like decomposition of an infinite product as a lattice sum.
- **Hörmander pseudo-differential operators** (1965) — Fourier-multiplier framework with symbol calculus; unifies elliptic, hypoelliptic, wave-propagation theory.
- **Tracy–Widom Airy-kernel Fredholm determinant** (1994) — edge spectrum via orthogonal-polynomial expansion.
- **Borcherds / Monstrous Moonshine q-expansions** (1992) — McKay–Thompson series as Hauptmoduln; q-expansion is the frequency decomposition of a vertex operator algebra character.

## axiomatizeFromInstances — additions
Append these bullets to the `examples:` list:
- **Jyeshthadeva's *Yuktibhāṣā*** (c. 1530) — first proof-first mathematics textbook in a South Asian vernacular; axiomatizes Kerala series methods from concrete numerical instances. (Sarma et al., *Gaṇita-Yukti-Bhāṣā*, 2008).
- **Voiculescu's free probability** (1985) — axiomatizes non-commutative "free independence" from observed operator behavior in L(F_n); (arXiv:1908.08125).

## structuralIsomorphism — additions
Append these bullets to the `examples:` list:
- **Zu Geng principle** (5th c.) — cross-section-area function ↔ volume; equal cross-sections imply equal volumes; 11 centuries before Cavalieri. (Lam & Shen, *Historia Math.* 1985).
- **Gauss's 17-gon constructibility** (1796) — abelian-group structure of 17th roots of unity ↔ nested quadratic extensions; cyclic Galois group of order 2⁴ diagonalized by tower of square roots. (Savitt, Cornell notes).
- **Hrushovski's geometric Mordell–Lang** (1996) — model-theoretic Zariski geometry ↔ algebraic-geometric subvariety structure; function-field case in all characteristics. (J. AMS 9).
- **Borcherds' Monstrous Moonshine** (1992) — Monster Lie algebra ↔ modular-form Hauptmoduln ↔ finite simple group bridge; (Invent. Math. 109).

## obstructionClass — additions
Append these bullets to the `examples:` list:
- **Liouville's transcendentals** (1844) — being algebraic of degree d forces quantitative lower bound |α − p/q| ≥ c/q^d; any number exceeding the bound is obstructed from being algebraic. (Chanillo, Rutgers notes).
- **Seiberg–Witten invariants** (1994) — SW(X, s) distinguishes smooth structures on 4-manifolds; nonzero SW obstructs certain metric/topological properties (e.g., Einstein metrics per LeBrun). (arXiv:hep-th/9411102).

## arithmetizeSyntax — additions
Append these bullets to the `examples:` list:
- **Piṅgala's binary metrical representation** (c. 3rd–2nd century BCE) — encodes Sanskrit prosodic L/G strings as binary numbers via explicit two-way algorithm; Gödel-numbering ~2100 years early. (Cuemath, Hayashi in *Studies in History of Indian Mathematics*, 2010).
- **IP = PSPACE / sumcheck protocol** (Shamir 1992) — replaces quantified Boolean formulas by polynomial identities over a large field, verified by interactive sumcheck. (J. ACM 39).
- **PCP theorem** (Arora–Safra 1992 + Arora–Lund–Motwani–Sudan–Szegedy 1998) — proofs arithmetized as polynomial objects tested probabilistically with O(log n) randomness and O(1) queries. (ALMSS, J. ACM 45).

## complexAnalysisToIntegers — additions
Append these bullets to the `examples:` list:
- **Hardy–Ramanujan Partition Formula** (1918) — canonical modern instance; generating function ∏(1−qⁿ)⁻¹, contour over |q| = r < 1, major/minor arcs, modular transformation on the dominant arc. Launched the circle method. (Proc. LMS 1918).
- **Deligne's Weil RH** (1974) — averages L-functions on a Lefschetz pencil; weight filtration on étale cohomology controls archimedean bounds of Frobenius eigenvalues. (Katz overview, Princeton notes). *Inherited: complexAnalysisToIntegers. Added: étale-cohomology bridge.*

## analysisAlgebraTopologyBridge — additions
Append these bullets to the `examples:` list:
- **Deligne's Weil RH** (1974) — étale-cohomology bridge transfers analytic archimedean bounds into arithmetic weight statements about Frobenius eigenvalues; also engages `complexAnalysisToIntegers`. (Publ. IHES 43).

## contractionFixedPoint — additions
Append these bullets to the `examples:` list:
- **Yau / Calabi conjecture** (1976, Shing-Tung Yau) — continuity method on the complex Monge–Ampère equation is a parameter-family of fixed-point problems; openness via implicit function theorem, closedness via C⁰/C²/C³ a priori estimates. (CPAM 31). *Inherited: contractionFixedPoint. Added: a priori estimates via De Giorgi–Nash–Moser iteration.*
- **Qin Jiushao's digit-by-digit root-finding** (1247) — iterated polynomial deflation P(c+y) at each digit is a contraction in the base-10 ultrametric; 550 years before Ruffini and Horner, contemporaneous with Sharaf al-Dīn al-Ṭūsī's Persian version. Scheme is Ruffini–Horner–Qin–al-Ṭūsī. (Libbrecht, MIT Press 1973).

## flowWithSurgery — additions
Append these bullets to the `examples:` list:
- **Hironaka resolution of singularities** (1964, Fields Medal 1970) — blow up centers where the "Hironaka character" is maximized; invariant strictly decreases under admissible blowups; terminates with smooth model. Analogous to Ricci-flow entropy monotone monitor. (Hauser, *Bull. AMS* 2003).

## physicsToPDE — additions
Append these bullets to the `examples:` list:
- **Seiberg–Witten equations** (1994) — N = 2 super Yang–Mills duality in physics (Aug 1994) distilled by Witten (Oct–Nov 1994) into U(1)-connection + spinor equations F_A⁺ = σ(Φ), D_A Φ = 0. (arXiv:hep-th/9411102).
- **Itô's formula** (1944, Kiyosi Itô) — Brownian-motion physics distilled into stochastic integral + second-order "Itô correction" chain rule; foundation of stochastic PDE and mathematical finance. (Proc. Imp. Acad. Tokyo 20).

## finiteCaseCheck — additions
Append these bullets to the `examples:` list:
- **PCP theorem** (Arora–Safra 1992 + ALMSS 1998) — verifier reads O(log n) random bits and queries O(1) bits of the proof; a constant-query verification is a finite spot-check of an arithmetized proof.

---

## Section B — NEW technique dictionary entries

Seven new function-signature entries, following the schema exactly.

---

#### `probabilisticExistence(event space Ω, distribution μ, target property P) → objectWithPositiveProbability`
- **category:** Cluster 11 · probabilistic
- **preconds:** a set of candidate objects you cannot easily construct directly; a probability distribution over candidates; quantifiable "bad events" whose avoidance encodes P.
- **process:**
  1. Define a distribution μ over candidate objects.
  2. Compute or bound the expected count of P-violations (union bound, first-moment method).
  3. If E[violations] < 1 (or Pr(all good) > 0), some realization achieves P.
  4. Variants: Lovász local lemma when violations are only locally correlated via a dependency graph; dependent random choice when you select on common neighborhoods.
- **postconds:** existence of an object with property P, with no construction.
- **inherits:** —
- **examples:** Erdős's Ramsey lower bound R(k,k) ≥ 2^{k/2} (1947, Erdős) — random 2-coloring of K_N, expected monochromatic K_k count < 1; (Alon, *Notices AMS*). Shannon's noisy-channel coding theorem (1948) — random codebook, expected decoding error → 0. Lovász Local Lemma (1975, Erdős–Lovász) — local-dependence variant with dependency graph; Moser–Tardos (2010) made it constructive; (Alon & Spencer, *The Probabilistic Method*). Dependent random choice (Fox–Sudakov 2011) — conditional sampling on common neighborhoods; (arXiv:0909.3271). Marcus–Spielman–Srivastava / Kadison–Singer (2015) — interlacing polynomial families as a real-stability refinement; (arXiv:1306.3969). Szemerédi regularity lemma (1975/78) — energy-increment partition as a derandomization analog; (Szemerédi, *Colloques Int. CNRS* 260).

---

#### `pigeonholeCollision(objects, bins with |objects| > |bins|) → twoInSameBin`
- **category:** Cluster 11 · counting
- **preconds:** a finite (or measurably finite) collection of objects and a partition into strictly fewer bins; some map objects → bins.
- **process:**
  1. Identify objects and bins; verify |objects| > |bins|.
  2. By counting alone, at least two objects land in the same bin.
  3. Extract and use the colliding pair; often the difference or ratio of two colliding objects is the sought-for witness.
- **postconds:** existence of a collision — a nontrivial near-equality, a cycle, a repeated configuration.
- **inherits:** — (foundational; discrete analog of `compactnessArgument`)
- **examples:** Dirichlet's approximation theorem (1842, Dirichlet) — Q+1 fractional parts {kα} in Q bins of length 1/Q force |{iα} − {jα}| < 1/Q, hence |α − p/q| < 1/(qQ); (Rittaud & Heeffer, *Math. Intelligencer* 36). Ramsey's theorem base case — any 2-coloring of K_6 has a monochromatic triangle by pigeonholing 5 edges at a vertex into 2 colors. Erdős–Ko–Rado (1961) — pigeonholing intersecting families of k-subsets. Dirichlet's theorem on primes in arithmetic progressions (1837, Schubfachprinzip application). *Inherited: —. Added: discrete existence without topology.*

---

#### `polynomialMethod(combinatorial or circuit target, ambient field 𝔽) → dimensionOrDegreeBound`
- **category:** Cluster 11 · algebra-meets-counting
- **preconds:** a target set or function over a field 𝔽; a meaningful notion of "low-degree" polynomial vanishing or approximating on the target.
- **process:**
  1. Count: exhibit a nonzero low-degree polynomial P that vanishes on the target (by dimension-counting: if target is smaller than the space of degree-≤d polynomials, pigeonhole gives one).
  2. Exploit structure: P restricted to a structured subfamily (a line, a subspace, an affine subspace) is univariate and has too many zeros, forcing a contradiction or a size bound.
  3. Alternatively: approximate a target function by low-degree polynomials (Razborov–Smolensky); then a function resisting low-degree approximation cannot be computed by small low-depth circuits.
- **postconds:** a combinatorial size bound, a circuit lower bound, or a structural decomposition.
- **inherits:** `reduceToCanonicalForm`, `obstructionClass`
- **examples:** Razborov–Smolensky AC⁰[p] lower bounds (1987, Razborov and Smolensky independently) — low-degree polynomial approximators over 𝔽_p; MOD_q resists approximation by degree (log s)^d; (Smolensky, STOC 1987). Dvir's finite-field Kakeya theorem (2009, Dvir) — if |K| < C(n+q−1, n), some low-degree P vanishes on K, but then vanishes on a line in every direction, contradicting ≠ 0; (J. AMS 22). Guth–Katz distinct distances (2010) — polynomial partitioning in ℝ². Croot–Lev–Pach / Ellenberg–Gijswijt cap-set bound (2016) — low-degree polynomial method over 𝔽_3ⁿ.

---

#### `spectralSequenceCompute(filteredComplex) → gradedInvariant`
- **category:** Cluster 12 · homological
- **preconds:** a filtered chain/cochain complex, a double complex, or a fibration; an abelian (or triangulated) category of coefficients.
- **process:**
  1. Choose a filtration of the complex compatible with differentials.
  2. Form the E₁-page from associated graded pieces; compute iterated cohomology page-by-page.
  3. Identify when the spectral sequence collapses or degenerates at a known page; read off the graded pieces of the target cohomology.
  4. Assemble extensions to recover the target up to isomorphism of filtered groups.
- **postconds:** the target invariant computed up to filtration, often sharply.
- **inherits:** `diagramChase`, `structuralIsomorphism`
- **examples:** Leray spectral sequence (1946, Leray) — E₂^{p,q} = H^p(Y; R^q f_* F) ⟹ H^{p+q}(X; F) for a map f: X → Y; invented with sheaf theory in a POW camp. (nLab *spectral sequence*). Serre spectral sequence (1951) — fibration version; computed homotopy groups of spheres. Grothendieck spectral sequence (1957) — composition of derived functors. Atiyah–Hirzebruch spectral sequence — generalized cohomology from ordinary cohomology. Eilenberg–Moore spectral sequence.

---

#### `diagramChase(commutative diagram with exact rows) → connectingMap | induction`
- **category:** Cluster 12 · homological
- **preconds:** a commutative diagram in an abelian category with exact rows (or columns); selected hypotheses on some vertical maps (mono, epi, iso).
- **process:**
  1. Pick an element in a specified kernel/cokernel position.
  2. Lift through exactness along a row; apply a vertical map; project via exactness of the next row.
  3. Verify that the construction is well-defined (independent of choices) by re-chasing.
  4. Package the result as a canonical morphism (connecting homomorphism) or a direct conclusion (isomorphism of a middle vertical).
- **postconds:** a long exact sequence, a connecting homomorphism, or a verified universal property.
- **inherits:** `axiomatizeFromInstances`
- **examples:** Snake lemma (Cartan–Eilenberg 1956 systematized) — kernels → cokernels exact sequence with connecting ∂; (nLab *snake lemma*). Five lemma (folklore, Cartan–Eilenberg 1956) — middle vertical iso from outer-four hypotheses. Long exact sequence of a pair (Eilenberg–Steenrod axioms) — homology of (X, A) from H_*(A) → H_*(X). Mayer–Vietoris sequence — homology of X = U ∪ V from U, V, U ∩ V. Nine lemma.

---

#### `representableFunctorTrick(object X in locally small category C) → universalPropertyOrNatTrans`
- **category:** Cluster 12 · categorical
- **preconds:** a locally small category C; an object X ∈ C (or a functor X: C^op → Set); interest in morphisms into X or in structural characterization of X.
- **process:**
  1. Replace X by its presheaf Hom(−, X): C^op → Set (Yoneda embedding).
  2. Any natural transformation Hom(−, X) ⟹ F is determined by its value on id_X, yielding bijection Nat(Hom(−, X), F) ≅ F(X).
  3. Translate construction/characterization problems about X into problems about Hom(−, X); use universal properties (limits, adjoints) in the functor category.
  4. Transport the solution back to X via the bijection.
- **postconds:** characterization of X up to isomorphism via its represented functor; construction of canonical morphisms by building natural transformations.
- **inherits:** `duality`, `structuralIsomorphism`
- **examples:** Yoneda lemma (Yoneda 1954, oral communication at Gare du Nord; popularized by Mac Lane 1971) — the archetypal result; Nat(Hom(−, c), X) ≅ X(c). (nLab *Yoneda lemma*). Freyd's adjoint functor theorem (1964, Freyd) — left adjoint of a limit-preserving R: C → D exists given the solution-set condition; (Freyd, *Abelian Categories*). Tannaka–Krein reconstruction — a group recovered from its category of representations. Isbell duality — adjunction between presheaves and co-presheaves.

---

#### `ultraproductTransfer(family of L-structures (A_i)_{i∈I}, ultrafilter U on I) → limitStructure`
- **category:** Cluster 5 · abstraction-logic
- **preconds:** a family of structures for a first-order language L; an ultrafilter U on the index set I.
- **process:**
  1. Form the set-theoretic product ∏ A_i and quotient by the U-equivalence: (a_i) ~_U (b_i) iff {i : a_i = b_i} ∈ U.
  2. Interpret L-symbols componentwise, noting that ultrafilter decisions make quotients respect Boolean connectives.
  3. By Łoś's theorem, a first-order sentence φ holds in ∏ A_i/U iff {i : A_i ⊨ φ} ∈ U.
  4. Use the transfer principle to move a sentence true "on U-many factors" into a theorem about the ultraproduct, and back (when U is principal or the theorem is first-order absolute).
- **postconds:** a limit structure in which first-order truth is preserved from U-large subsets of the family.
- **inherits:** `axiomatizeFromInstances`, `compactnessArgument`
- **examples:** Łoś's theorem (1955, Jerzy Łoś) — the fundamental transfer principle; (nLab *Los theorem*). Robinson's nonstandard analysis and hyperreals *ℝ (1960/66, Abraham Robinson) — ℝ^ℕ/U gives infinitesimals and infinite elements with first-order transfer. Compactness theorem in first-order logic — one-line corollary via ultraproducts of finite-satisfaction families. Ax–Kochen theorem on p-adic fields (1965) — ultraproduct of ℚ_p across p matches ultraproduct of 𝔽_p((t)). Hrushovski's geometric Mordell–Lang (1996) — model-theoretic Zariski geometries applied to function-field arithmetic.

---

## Section C — New clusters

### Cluster 11 — Probabilistic & Counting Arguments

*Unifying idea:* Establish existence by counting volume or positive probability rather than explicit construction.

Techniques in this cluster:
- probabilisticExistence
- pigeonholeCollision
- polynomialMethod

### Cluster 12 — Homological / Categorical Methods

*Unifying idea:* Transfer structural information across categories via functors, exact sequences, and spectral sequences computing derived invariants.

Techniques in this cluster:
- spectralSequenceCompute
- diagramChase
- representableFunctorTrick

---

## Section D — Mermaid diagram fragments

### D1. Cluster-tree additions (append to §1 master tree)

```
  ROOT --> C11[Cluster 11<br/>Probabilistic &<br/>Counting]
  ROOT --> C12[Cluster 12<br/>Homological &<br/>Categorical]

  C11 --> probExist[probabilisticExistence]
  C11 --> pigeonCollide[pigeonholeCollision]
  C11 --> polyMethod[polynomialMethod]

  C12 --> specSeq[spectralSequenceCompute]
  C12 --> diagChase[diagramChase]
  C12 --> repFunctor[representableFunctorTrick]

  C5 --> ultraTransfer[ultraproductTransfer]
```

### D2. Inheritance-graph additions (append to §3 graph)

```
  canonical --> polyMethod
  obstruct --> polyMethod
  spotPattern --> probExist
  diagChase --> specSeq
  isom --> specSeq
  axiom --> diagChase
  duality --> repFunctor
  isom --> repFunctor
  axiom --> ultraTransfer
  compact --> ultraTransfer
  conserved --> flow
  probExist --> pigeonCollide
```

### D3. Decision-flowchart additions (append to §4 flowchart)

```
  EXIST --> PROB{Need existence<br/>without construction?}
  PROB -->|positive-probability argument works| probExist2[probabilisticExistence]
  PROB -->|discrete counting only| pigeonCollide2[pigeonholeCollision]

  COUNT --> POLY{Algebraic-counting<br/>hybrid?}
  POLY -->|low-degree polynomial vanishes on target| polyMethod2[polynomialMethod]

  START --> DERIVED{Derived invariant<br/>or filtered complex?}
  DERIVED -->|filtration + iterated cohomology| specSeq2[spectralSequenceCompute]
  DERIVED -->|exact rows in a diagram| diagChase2[diagramChase]
  DERIVED -->|universal property needed| repFunctor2[representableFunctorTrick]

  STUCK -->|first-order transfer from a family| ultraTransfer2[ultraproductTransfer]
```

---

## Section E — Quick-reference table rows

Append these rows to the §5 table (continue after row 28):

```
| 29 | probabilisticExistence | 11 | event space + distribution | object with positive probability | Erdős Ramsey 1947 | Marcus–Spielman–Srivastava Kadison–Singer |
| 30 | pigeonholeCollision | 11 | objects + bins, |obj|>|bins| | collision pair | Dirichlet approx 1842 | Ramsey theory / EKR |
| 31 | polynomialMethod | 11 | target + field | degree / dimension bound | Razborov–Smolensky 1987 | Dvir Kakeya / cap sets |
| 32 | spectralSequenceCompute | 12 | filtered complex | graded invariant | Leray 1946 | Grothendieck / Atiyah–Hirzebruch |
| 33 | diagramChase | 12 | commutative diagram + exact rows | connecting map | Snake / Five lemma 1956 | Mayer–Vietoris / LES |
| 34 | representableFunctorTrick | 12 | object in locally small C | universal property | Yoneda 1954 | Freyd AFT / Tannaka–Krein |
| 35 | ultraproductTransfer | 5 | family + ultrafilter | limit structure | Łoś 1955 | Hrushovski Mordell–Lang |
```

---

## Section F — Integration instructions for orchestrator

Modifications to `10_toolbox.md`, in order:

- **§1 (Tree of discovery):** Insert the two new ROOT→C11 and ROOT→C12 lines at the end of the existing ROOT branch list, after `ROOT --> C10`. Append the three `C11 -->` leaves and the three `C12 -->` leaves at the end of the mermaid block. Insert `C5 --> ultraTransfer[ultraproductTransfer]` alongside the existing C5 leaves (`C5 --> axiom`, `C5 --> isom`).
- **§2 (Function dictionary):** Append new examples from Section A of this file to the `examples:` field of each named existing technique (15 techniques get additions). After the existing "### Cluster 10 — Computer-Assisted & Collaborative" block, insert a new `### Cluster 5 extension` note for `ultraproductTransfer` OR append the `ultraproductTransfer` entry inside the existing Cluster 5 subsection after `structuralIsomorphism`. Then append two new top-level headers "### Cluster 11 — Probabilistic & Counting Arguments" and "### Cluster 12 — Homological / Categorical Methods", each followed by the three schema entries from Section B.
- **§3 (Inheritance graph):** Append the edges in Section D2 to the existing `graph LR` block.
- **§4 (Decision flowchart):** Append the Section D3 branches to the existing `flowchart TD` block; the PROB and POLY branches attach under the existing EXIST and COUNT nodes respectively; DERIVED branches off from START; the ultraproduct branch attaches under STUCK.
- **§5 (Quick-reference table):** Append the seven rows from Section E directly after row 28 (`distributedCollaboration`).
- **§6 (How to extend the toolbox):** Strike the `probabilisticMethod`, `homologicalAlgebra`, and `ultraproductTransfer` bullets (now integrated); retain `gröbnerBasis` and `motivicBridge` as future work.

---

## DEFER notes

- Intern A's flagged Brahmagupta–Fibonacci identity, Eisenstein's criterion, Euler–Maclaurin, al-Khwārizmī *mu'āmalāt*, Bhāskara I sine approximation (item #9 of their uncertainties) were excluded from the researcher's vetted list. Not acted on here; candidates for a future expansion round.
- Intern B's `leftAdjointFromLimitPreservation` (Freyd AFT) was consolidated by the researcher into `representableFunctorTrick`. Freyd AFT is listed as an example of the latter; no separate entry was created. If the orchestrator prefers a standalone `leftAdjointFromLimitPreservation` entry, the Freyd example can be split off.
- Intern B's `energyIncrementPartition` (Szemerédi regularity) was folded into `probabilisticExistence` examples per the researcher. A purist may want Szemerédi regularity as its own entry; left as DEFER.
- The researcher's instruction to append `compactnessArgument ↔ pigeonholeCollision` as a discrete-analogy inheritance edge is ambiguous about direction. I chose `probExist --> pigeonCollide` in D2 as the cleaner within-Cluster-11 relation, and did not force a cross-cluster edge from `compact`. Orchestrator may add `compact --> pigeonCollide` if the graph is to capture the discrete analogy explicitly.
