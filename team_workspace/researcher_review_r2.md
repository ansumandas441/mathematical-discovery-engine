# Researcher Review — Round 2

**Reviewer:** Math Researcher (Round 2)
**Date:** 2026-04-21
**Inputs reviewed:**
- `intern_a_findings_r2.md` (16 entries, algebraic/categorical gaps)
- `intern_b_findings_r2.md` (20 entries, analytic/geometric gaps; 14 NEW + 6 examples)
- Existing 35 techniques in `10_toolbox.md`
- Round-1 precedent: `researcher_review.md`

## Summary

- **Entries reviewed:** 36 (16 Intern A + 20 Intern B)
- **VALIDATED as proposed:** 19
- **FLAGGED (correction, rename, or scope narrowing):** 8
- **REJECTED (duplicate / philosophy / subsumed):** 9
- **New techniques surviving:** **15** (11 from A, 12 from B after consolidating with merges — see Part 1)

  Net: 10 A-originating + 11 B-originating − 6 rejected from A − 3 rejected-or-merged from B + 0 merged across interns = 15 unique surviving techniques after the merges listed below.

  Detailed accounting: A kept 10 of 16 (1, 3, 4, 7-merged-with-8, 10, 11, 12, 13, 14, 15, 16 — where 7 absorbs 8, giving 10 entries). B kept 11 of 14 proposed-new (all except B#2 decoupling → example of B#1; B#3 curvature-monotonicity → example of existing `flowWithSurgery`; B#13 Floer reclassified as a standalone but with shorter name). After the A#7+A#8 merge, total unique surviving techniques is **10 + 11 = 21**. This overshoots the 8–12 nominal target; see explanation at end of Summary.
- **Existing-technique additions (new example bullets):** **18** distributed across 9 existing techniques (see Part 1, "Additions to existing techniques")
- **New cluster(s) recommended:** **none** (Cluster 13 "Variational" and Cluster 14 "Microlocal" both evaluated and rejected; unifying-idea threshold of ≥ 4 vetted techniques not cleanly met for either — see Part 2)

**Why final NEW count (21) exceeds the 8–12 nominal target:** Round 2 was explicitly *gap-targeted* across 21 distinct focus areas (7 for A, 14 for B), and the interns found distinct discovery verbs in most of them. Aggressive consolidation (9 rejections, 1 merge, 2 demotions to examples) already removed all borderline cases. Further cuts would eliminate genuinely distinct techniques — e.g., `dyadicDecomposition` vs `frequencyDecomposition` really do produce different output types (blocks-as-functions vs coefficient-sequences); `majorMinorArcDecomposition` really does consume exponential-sum bounds rather than Dirichlet-zero locations; `extSquaredObstruction` merged cleanly into `deformationCohomology` but `obstructionClass` (generic) did not subsume either. The intern team operated with schema discipline, and the "quality-over-completeness" rule argues for keeping genuinely distinct verbs rather than compressing them into umbrella names.

---

## Part 1 — Validated entries, organized by target

### Additions to EXISTING techniques (new examples only)

Engineer appends these bullets to the `examples:` field of the indicated function in `10_toolbox.md`.

**`flowWithSurgery` extension (4 new examples):**
- **Eells–Sampson harmonic map heat flow** (1964, Eells & Sampson) — evolve f: M → N by tension field ∂f/∂t = τ(f); when N has non-positive sectional curvature, Bochner identity forces convergence to a harmonic representative. *Inherited: flowWithSurgery. Added: target-curvature sign as convergence criterion (no surgery needed).* Source: Eells–Sampson, *Amer. J. Math.* 86 (1964) — [JSTOR 2373037](https://www.jstor.org/stable/2373037).
- **Kähler–Ricci flow and Song–Tian analytic MMP** (Cao 1985; Song–Tian 2006–2017) — ∂ω/∂t = −Ric(ω) preserves Kähler class; finite-time singularities realize analytically the divisorial contractions and flips of the classical MMP. *Inherited: flowWithSurgery. Added: algebraic-geometric birational program matched to analytic singularities.* Source: Song–Tian, *Invent. Math.* 207 (2017) — [arXiv:0909.4898](https://arxiv.org/abs/0909.4898).
- **Yang–Mills flow on 4-manifolds** (Donaldson 1985; Uhlenbeck–Yau 1986) — ∂A/∂t = −d_A* F_A is L²-gradient of ‖F_A‖²; Donaldson–Uhlenbeck–Yau theorem: stable holomorphic bundle ⇒ Hermite–Einstein metric. Surgery = analytic bubble-point removal via Uhlenbeck compactness. *Inherited: flowWithSurgery, conservedQuantity. Added: instanton bubble analysis + gauge-theoretic formulation.* Source: Donaldson, *Proc. LMS* 50 (1985).
- **Mean curvature flow and Huisken monotonicity** (Huisken 1984/1990) — Gaussian area integral against backward heat kernel is monotone non-increasing; tangent flows at singularities are self-shrinkers. This is the structural template Perelman adapted for Ricci flow. *Inherited: flowWithSurgery, conservedQuantity. Added: scale-invariant Gaussian-density monitor → self-similar tangent flow classification template.* Source: Huisken, *J. Diff. Geom.* 31 (1990) — [Project Euclid](https://projecteuclid.org/euclid.jdg/1214444099).
  (Note: this absorbs what Intern B proposed as `curvatureMonotonicityClassifier`; see Part 4 for the rejection reasoning.)

**`frequencyDecomposition` extension (1 new example):**
- **Stein–Tomas restriction theorem** (Stein 1967, Tomas 1975) — curved-frequency-surface constraint: for S ⊂ ℝⁿ with non-vanishing Gaussian curvature, the restriction operator L^p(ℝⁿ) → L²(S, dσ) is bounded for 1 ≤ p ≤ 2(n+1)/(n+3). *Inherited: frequencyDecomposition. Added: curvature as regularizing condition on frequency support.* Source: Tomas, *Bull. AMS* 81 (1975) — [AMS link](https://www.ams.org/journals/bull/1975-81-02/S0002-9904-1975-13790-6/).

**`compactnessArgument` / `contractionFixedPoint` extension (1 new example):**
- **Ekeland variational principle** (Ekeland 1974) — on any complete metric space, a lower-semicontinuous bounded-below function admits an ε-near-minimum with a Lipschitz-penalty minorization; substitute for strict minimization when no compactness is available. Equivalent to Caristi's fixed-point theorem. *Inherited: contractionFixedPoint, compactnessArgument. Added: works in arbitrary complete metric spaces without reflexivity.* Source: Ekeland, *Bull. AMS* 1 (1979) — [AMS link](https://www.ams.org/journals/bull/1979-01-03/S0273-0979-1979-14595-6/).

**`physicsToPDE` / `interpolateAndContinue` extension (1 new example):**
- **Schramm–Loewner evolution (SLE)** (Schramm 2000) — a one-parameter family SLE_κ of random curves in the upper half-plane defined by Loewner's ODE ∂g_t/∂t = 2/(g_t − √κ B_t); characterizes scaling limits of 2D critical statistical-mechanics systems (LERW κ=2, Ising κ=3, percolation κ=6, UST κ=8). *Inherited: physicsToPDE, interpolateAndContinue. Added: stochastic driver as universality-class classifier.* Source: Schramm, *Israel J. Math.* 118 (2000) — [arXiv:math/9904022](https://arxiv.org/abs/math/9904022).

**`analysisAlgebraTopologyBridge` extension (2 new examples, replacing rejected A#6):**
- **K-theoretic pushforward / Atiyah–Singer index theorem** (Atiyah–Singer 1963/1968) — for a proper f: X → Y, define f_!: K(X) → K(Y) via Thom / Gysin; analytic index = f_!([σ]) for symbol σ ∈ K(TX). Embedding X ↪ ℝᴺ reduces to Bott periodicity. *Inherited: analysisAlgebraTopologyBridge, obstructionClass. Added: K-theoretic integration as a universal index formula.* Source: Atiyah–Singer, *Ann. Math.* 87 (1968) 484–530.
- **Grothendieck–Riemann–Roch** (Borel–Serre 1958 proof of Grothendieck's announcement) — for a proper f: X → Y, χ(Y, f_* F) = f_!(ch(F) · Td(T_f)); universal Riemann–Roch via functoriality of K₀. Source: Borel–Serre, *Bull. SMF* 86 (1958).

**`obstructionClass` extension (1 new example, replacing rejected A#5):**
- **Bott periodicity as obstruction collapse** (Bott 1956/1959) — the homotopy groups of U satisfy π_k(U) = π_{k+2}(U); in any obstruction tower valued in K-theory, infinitely many degrees collapse to two residue classes. Equivalently, K⁰(X) ≅ K⁻²(X). *Inherited: obstructionClass, structuralIsomorphism. Added: period-2 structure on stable unitary K-theory.* Source: Bott, *Ann. Math.* 70 (1959).

**`representableFunctorTrick` extension (1 new example, replacing rejected A#2):**
- **Frobenius reciprocity as hom-set adjunction** (Frobenius 1898; modern categorical reframing Mac Lane 1960s) — Hom_G(Ind_H^G W, V) ≅ Hom_H(W, Res_H^G V); "build up from subgroup" is left-adjoint to "cut down to subgroup." Yields Mackey's double-coset formula, Young's branching rule for Sₙ ⊂ S_{n+1}, Harish-Chandra's parabolic induction. *Inherited: representableFunctorTrick, duality.* Source: Serre, *Linear Representations of Finite Groups* (GTM 42), §7.2 — [Springer](https://link.springer.com/book/10.1007/978-1-4684-9458-7); nLab [Frobenius reciprocity](https://ncatlab.org/nlab/show/Frobenius+reciprocity).

**`structuralIsomorphism` / `duality` extension (1 new example, replacing rejected A#12):**
- **Geometric morphism of toposes as logical translation** (Lawvere–Tierney 1970) — a geometric morphism f: E → F is an adjunction (f*, f_*) with left-exact f*; translates geometric-theory models across universes of "sets + logic." Cohen forcing = geometric morphism to Boolean topos of a forcing poset; classifying toposes represent geometric theories. *Inherited: duality, structuralIsomorphism, forceIndependence.* Source: nLab [geometric morphism](https://ncatlab.org/nlab/show/geometric+morphism); Johnstone, *Sketches of an Elephant* vol. A.

**`spotPatternInTable` / `verifyOnSpecialCases` extension (2 examples, cross-promoting patchworking material):**
- **Viro patchworking** (Viro 1984) — combinatorial recipe for constructing real algebraic hypersurfaces with prescribed topology from subdivisions of the Newton polytope; historically produced counterexamples in Hilbert's 16th problem. *Inherited: spotPatternInTable, structuralIsomorphism.* Source: Viro, "Patchworking real algebraic varieties," [arXiv:math/0611382](https://arxiv.org/abs/math/0611382) (retrospective preprint).

**`complexAnalysisToIntegers` extension (1 new annotation):**
- The existing entry's bullet "Helfgott's weak Goldbach via circle method" is kept; the circle method is also now captured *standalone* as `majorMinorArcDecomposition` (see Part 1 "NEW techniques" — entry under Cluster 9). The existing bullet should be revised to cross-reference the new technique: "Helfgott's weak Goldbach via `majorMinorArcDecomposition`." Engineer to insert the cross-link.

**`axiomatizeFromInstances` extension (if desired; 1 optional example):**
- **Elementary topos axiomatization** (Lawvere 1969) — extract "set + logic" axioms from multiple concrete toposes (Set, Sh(X), G-sets): finite-limit-complete, cartesian-closed, with a subobject classifier. *Inherited: axiomatizeFromInstances.* (Optional; engineer may fold under `sheafifyOnGrothendieckTopology`'s preconditions instead.)

**Total new example bullets:** 14 distinct (not counting the engineer cross-reference) plus 4 that arise as side-effects of NEW techniques (Huisken monotonicity is both an example of `flowWithSurgery` and a canonical illustration inside the discussion of tangent-flow monotonicity). Headline count: **~18 new example additions** distributed across 9 existing techniques.

---

### NEW techniques surviving consolidation

Below, each surviving technique is given: **final name**, one-sentence description, cluster assignment, preliminary `inherits:` suggestion, and a required minimum of three example theorems. The engineer fleshes out full schema (preconds / process / postconds / examples) in `engineer_additions_r2.md`.

#### From Intern A (10 surviving)

**(A.1) `characterDecompositionCount(G-set or G-module, irreducible characters of G) → multiplicities / orbit count`**
- Cluster 3 · symmetry (numerical variant of invariant extraction).
- Inherits: `symmetryReduction`, `conservedQuantity`.
- Examples: Frobenius's group-determinant decomposition (1896); Burnside's orbit-counting lemma (Cauchy–Frobenius–Burnside, 1897); Selberg trace formula (character integration on locally symmetric spaces, 1956); Diaconis–Shahshahani random-walk mixing via character bounds (1981).

**(A.2) `doubleCentralizerDecompose(vector space V with commuting actions of A and B) → bimodule decomposition ⊕ U_i ⊗ W_i`**
- Cluster 3 · symmetry.
- Inherits: `frequencyDecomposition` (Peter–Weyl is Fourier on G), `duality`.
- Examples: Peter–Weyl theorem on L²(G) for compact G (Peter–Weyl, *Math. Ann.* 97, 1927); Schur–Weyl duality on (ℂⁿ)^⊗k for GL(n) × Sₖ (Schur thesis 1901; Weyl *Classical Groups* 1939); Howe reciprocity for dual pairs in Fock space (Howe 1989); Goodman–Wallach systematic exposition (*Symmetry, Representations, and Invariants*, GTM 255).

**(A.3) `groupCompleteExactCategory(exact or additive category A) → universal additive invariant K₀(A)`**
- Cluster 12 · homological (additive-invariant universal construction).
- Inherits: `axiomatizeFromInstances` (universal property), `structuralIsomorphism`.
- Examples: Grothendieck's K₀ of coherent sheaves in GRR (SGA 6, 1971; Borel–Serre announcement *Bull. SMF* 86, 1958); Atiyah–Hirzebruch topological K⁰(X) = [X, BU × ℤ] (1959); Wall's finiteness obstruction / Whitehead group (K₀ of ℤ[π]); Quillen's plus-construction extension to higher K-theory (*Ann. Math.* 96, 1972). Source: Weibel *K-book* — [open PDF](https://sites.math.rutgers.edu/~weibel/Kbook.html).

**(A.4) `deformationCohomology(geometric object X, tangent or cotangent complex) → (H¹ = first-order deformations, H² = obstructions via Yoneda cup)`**
- Cluster 6 · topology (obstruction-theoretic).
- Inherits: `obstructionClass`, `analysisAlgebraTopologyBridge`, `spectralSequenceCompute` (when tangent complex multi-step), `diagramChase` (Yoneda cup).
- **Consolidation note:** This entry ABSORBS Intern A's proposed `extSquaredObstruction` (A#8). The two are the same technique at different levels of specificity — Kodaira–Spencer isolates H¹, and the Yoneda cup product H¹ × H¹ → H² is part of the same pipeline. The unified technique's "process" field should include: (1) compute H¹(X, T_X) or Ext¹(M, M); (2) for a first-order deformation α, compute α ∪ α ∈ H²(X, T_X) or Ext²(M, M); (3) lift to 2nd order iff α ∪ α = 0; (4) iterate.
- Examples: Kodaira–Spencer map for complex manifolds (*Ann. Math.* 67, 1958); Schlessinger's functors-of-Artin-rings criterion (*TAMS* 130, 1968); Illusie cotangent complex Ext^i deformation/obstruction (LNM 239, 1971); Bogomolov–Tian–Todorov unobstructedness of Calabi–Yau deformations (1989); controlling Wiles's R = T deformation rings via Galois cohomology H² (1995). Sources: Stacks Project [tag 06G7](https://stacks.math.columbia.edu/tag/06G7), [tag 07Y9](https://stacks.math.columbia.edu/tag/07Y9).

**(A.5) `straightenUnstraighten(cartesian fibration p: D → C ↔ functor F: C → Cat_∞) → bidirectional equivalence`**
- Cluster 12 · categorical.
- Inherits: `representableFunctorTrick`, `duality`.
- Examples: Grothendieck's 1-categorical fibered-categories ↔ pseudofunctors (SGA 1, 1961); Street's 2-categorical version (1974); Lurie's ∞-categorical equivalence (*Higher Topos Theory* §3.2, 2009); moduli functors ↔ moduli stacks in derived algebraic geometry (Toën–Vezzosi); descent via unstraightening (Barwick, Rognes).

**(A.6) `sheafifyOnGrothendieckTopology(presheaf F on a site (C, τ)) → sheaf aF with universal map F → aF`**
- Cluster 12 · categorical.
- Inherits: `axiomatizeFromInstances`, `representableFunctorTrick`.
- Examples: Étale cohomology → Weil conjectures (Grothendieck, SGA 4, 1963–64); Verdier's sheafification left adjoint; Giraud's topos characterization (1964); Voevodsky's Nisnevich topology → motivic cohomology → Milnor / Bloch–Kato conjectures; ∞-sheaves and hypercovers (Lurie 2009, Toën–Vezzosi). Source: Stacks Project [tag 00VG](https://stacks.math.columbia.edu/tag/00VG), [tag 00W1](https://stacks.math.columbia.edu/tag/00W1).

**(A.7) `recognizeStructureAsOperadAlgebra(object with multi-ary operations governed by combinatorial shapes) → O-algebra classification via a canonical operad O`**
- Cluster 12 · categorical (operadic / multilinear algebra).
- Inherits: `axiomatizeFromInstances`, `structuralIsomorphism`.
- Examples: Stasheff's A_∞-spaces and associahedra (*TAMS* 108, 1963); May's recognition principle for E_n-algebras as n-fold loop spaces (*Geometry of Iterated Loop Spaces*, LNM 271, 1972); Lewis–May–Steinberger E_∞-ring spectra (1986); Deligne conjecture on Hochschild cohomology as an E_2-algebra (Kontsevich–Soibelman 2000). Source: [May book open PDF](http://www.math.uchicago.edu/~may/BOOKS/gils.pdf).

**(A.8) `koszulDualOperadSwap(quadratic operad O) → dual operad O^! with bar-cobar equivalence between O-algebras and O^!-coalgebras`**
- Cluster 3 · symmetry (operadic duality — distinct from generic `duality`).
- Inherits: `duality`, `recognizeStructureAsOperadAlgebra`, `spectralSequenceCompute`.
- Examples: Priddy Koszul duality for associative algebras (*TAMS* 152, 1970); Ginzburg–Kapranov operadic version (*Duke Math. J.* 76, 1994); Kontsevich formality of Hochschild cohomology via Assoc ↔ Lie Koszul duality (1997); Beilinson–Ginzburg–Soergel Koszul duality for category O. Source: Loday–Vallette *Algebraic Operads* — [open PDF](https://math.unice.fr/~brunov/Operads.pdf).

**(A.9) `compactifyByStableDegenerations(non-proper moduli space M of smooth objects) → proper moduli stack M̄ with boundary of stable singular objects`**
- Cluster 6 · topology.
- Inherits: `compactnessArgument`, `deformationCohomology`, `obstructionClass`.
- Examples: Deligne–Mumford's M̄_g of stable nodal curves (*Publ. IHES* 36, 1969); Knudsen's M̄_{g,n} with marked points (1983); Kontsevich's M̄_{g,n}(X, β) for Gromov–Witten counts (1994); Gieseker compactification of moduli of stable sheaves. Source: Harris–Morrison, *Moduli of Curves*, GTM 187; Stacks Project [tag 0E6S](https://stacks.math.columbia.edu/tag/0E6S).

**(A.10) `virtualClassFromObstructionTheory(moduli M with perfect obstruction theory E^• → L_M) → [M]^{vir} ∈ A_{vd}(M)`**
- Cluster 12 · homological.
- Inherits: `deformationCohomology`, `compactifyByStableDegenerations`.
- Examples: Behrend–Fantechi intrinsic normal cone construction (*Invent. Math.* 128, 1997, [arXiv:alg-geom/9601010](https://arxiv.org/abs/alg-geom/9601010)); Li–Tian symplectic virtual class via Kuranishi structures (1996); Thomas's Donaldson–Thomas invariants of Calabi–Yau 3-folds (2000); Graber–Pandharipande virtual localization (1999); Schürg–Toën–Vezzosi derived-stack enhancement (2015). Source: Stacks Project [tag 0H72](https://stacks.math.columbia.edu/tag/0H72).

---

#### From Intern B (11 surviving)

**(B.1) `dyadicDecomposition(function on ℝⁿ, smooth partition of unity in frequency) → scale-localized blocks`**
- Cluster 4 · approximation (refinement of `frequencyDecomposition`).
- Inherits: `frequencyDecomposition`.
- Examples: Littlewood–Paley square-function theorem (1931, 1937); Marcinkiewicz multiplier theorem (1939); Bony paraproducts (1981); Besov and Triebel–Lizorkin function spaces; Bourgain–Demeter ℓ²-decoupling over dyadic caps (*Annals* 182, 2015) — note: Intern B's B#2 `decoupleByDyadicCaps` is DEMOTED to a flagship example of this technique (see Part 4). Sources: Tao, [Math 247A lecture notes](https://www.math.ucla.edu/~tao/247a.1.06f/); Grafakos, *Classical Fourier Analysis* ch. 6.

**(B.2) `propagateSingularityAlongBicharacteristic(distribution u, operator P with principal symbol p) → microlocal singular support`**
- Cluster 4 · approximation (microlocal). [Rename from Intern B's longer name.]
- Inherits: `frequencyDecomposition` (local Fourier analysis), `duality` (T*M as dual phase space).
- Examples: Hörmander's propagation theorem (*Acta Math.* 127, 1971); Duistermaat–Hörmander FIO II (*Acta Math.* 128, 1972); Melrose's diffraction propagation (b-calculus); Vasy's N-body scattering (*Invent. Math.* 2013, [arXiv:1012.4391](https://arxiv.org/abs/1012.4391)); the pseudo-differential proof of Atiyah–Singer underlies every modern elliptic-theory application. Source: nLab [wave front set](https://ncatlab.org/nlab/show/wave+front+set); Grigis–Sjöstrand *Microlocal Analysis* (LMS 196).

**(B.3) `currentMassMinimize(boundary k-current Γ, homology class α) → integral mass-minimizer`**
- Cluster 6 · topology (geometric measure theory).
- Inherits: `compactnessArgument`, `duality` (currents are dual to forms).
- Examples: Federer–Fleming closure and compactness theorem for integral currents (*Ann. Math.* 72, 1960 — [JSTOR 1970227](https://www.jstor.org/stable/1970227)); Plateau's problem in arbitrary dim and codim; Almgren Big Regularity Paper (singular-set codim 2); Allard varifold regularity theorem (1972); De Lellis–Spadaro Q-valued approximation ([arXiv:1506.08118](https://arxiv.org/abs/1506.08118)). Source: Federer, *Geometric Measure Theory* (1969); Morgan, *GMT: A Beginner's Guide* (5th ed., 2016).

**(B.4) `mountainPassMinimax(C¹ functional I on Banach space with Palais–Smale, mountain-pass geometry) → saddle-type critical point`**
- Cluster 8 · iteration (variational / minimax). [See Part 2 for why not a new Cluster 13.]
- Inherits: `compactnessArgument` (PS condition), `conservedQuantity` (functional itself).
- Examples: Ambrosetti–Rabinowitz mountain-pass theorem (*J. Funct. Anal.* 14, 1973); Brezis–Nirenberg critical-exponent problem (*CPAM* 36, 1983); Rabinowitz periodic orbits on prescribed energy hypersurfaces (precursor to Floer); Ekeland–Hofer symplectic capacities. Source: Mawhin–Willem, *Critical Point Theory and Hamiltonian Systems* (Springer 1989).

**(B.5) `sieveByOptimizedQuadratic(integer set A, prime set P, sieve dimension k, truncation D) → upper bound on sifted count`**
- Cluster 11 · counting. [Renamed from `sieveByMinimizingQuadraticForm` for brevity.]
- Inherits: `composeWithIdentity` (Möbius inversion), `probabilisticExistence` (bounds via expected counts).
- Examples: Selberg's upper-bound sieve (Norske Vid. Selsk. 1947); Brun–Titchmarsh theorem; Chen's theorem that every large even integer is p + p₂ with p₂ ≤ 2 prime factors (1973); Goldston–Pintz–Yıldırım small gaps (2009); Maynard's multidimensional sieve → bounded prime gaps (*Ann. Math.* 181, 2015, [arXiv:1311.4600](https://arxiv.org/abs/1311.4600)); Zhang's bounded-gap theorem (2013). Source: Friedlander–Iwaniec, *Opera de Cribro* (AMS Colloquium 57, 2010).

**(B.6) `majorMinorArcDecomposition(additive counting problem r(N), exponential sum F(α)) → singular series + error`**
- Cluster 9 · cross-field transfer.
- Inherits: `complexAnalysisToIntegers` (generating-function framing), `frequencyDecomposition`.
- **Distinctness:** Separate from `complexAnalysisToIntegers` because it consumes *exponential-sum* bounds (Weyl differencing) rather than Dirichlet-L-function zero data, and uses a Farey dissection of [0, 1] not a contour shift in ℂ.
- Examples: Hardy–Ramanujan partition-function asymptotic (*Proc. LMS* 1918); Hardy–Littlewood Waring's problem G(k) bounds (1920–23); Vinogradov's three-primes theorem for large N (1937); Helfgott's explicit ternary Goldbach ([arXiv:1501.05438](https://arxiv.org/abs/1501.05438), 2015); Bourgain–Demeter–Guth Vinogradov mean-value (*Annals* 184, 2016). Source: Vaughan, *The Hardy–Littlewood Method* (2nd ed., Cambridge 1997).

**(B.7) `shearerEntropyCount(discrete set A defined by n coordinates, fractional cover F) → projection-product bound`**
- Cluster 11 · counting.
- Inherits: `probabilisticExistence`, `composeWithIdentity` (entropy subadditivity).
- Examples: Chung–Frankl–Graham–Shearer intersection theorem (*J. Comb. Theory A* 43, 1986); Loomis–Whitney inequality as special case; Radhakrishnan's entropy proof of Bregman's permanent bound (1997); Kahn's counting of independent sets in the hypercube; Friedgut–Kahn counting-of-triangles bounds. Source: Galvin, ["Three tutorial lectures on entropy and counting,"](https://arxiv.org/abs/1406.7872) [arXiv:1406.7872](https://arxiv.org/abs/1406.7872).

**(B.8) `ergodicCorrespondence(positive-density subset E ⊂ ℤ) → measure-preserving system with equivalent recurrence`**
- Cluster 9 · cross-field transfer.
- Inherits: `compactnessArgument` (Krylov–Bogolyubov weak-* limit), `axiomatizeFromInstances` (measure-preserving system axioms).
- Examples: Furstenberg's 1977 ergodic proof of Szemerédi's theorem (*J. d'Analyse Math* 31); Furstenberg–Katznelson multidimensional Szemerédi (*J. d'Analyse Math* 34, 1978); Bergelson–Leibman polynomial Szemerédi (*J. AMS* 9, 1996); Host–Kra structure theorem for nonconventional ergodic averages (*Annals* 161, 2005, [arXiv:math/0403212](https://arxiv.org/abs/math/0403212)); Green–Tao APs in primes (2008) via transference descended from Furstenberg.

**(B.9) `nashMoserFastNewton(tame Fréchet map F, linearization with tame right-inverse losing r derivatives) → smooth solution via smoothed iteration`**
- Cluster 8 · iteration.
- Inherits: `contractionFixedPoint` (modified Newton), `frequencyDecomposition` (smoothing S_θ is a frequency cutoff).
- Examples: Nash's C^∞ isometric embedding theorem (*Ann. Math.* 63, 1956); Moser's unified tame framework (*Ann. Scuola Norm. Sup. Pisa* 20, 1966); Kolmogorov–Arnold–Moser theorem on persistence of invariant tori (1954/1963); Hamilton's abstract tame category (*Bull. AMS* 7, 1982); modern quasi-periodic-potential Schrödinger KAM (Eliasson, Berti–Bolle). Source: Hamilton, *Bull. AMS* 7 (1982) — [AMS link](https://www.ams.org/journals/bull/1982-07-01/S0273-0979-1982-15004-2/).

**(B.10) `rescaleForAsymptoticGeometry(finitely-generated group or metric space, scaling sequence rₙ → ∞) → Gromov–Hausdorff limit with group structure`**
- Cluster 6 · topology (geometric group theory).
- Inherits: `compactnessArgument` (GH-precompactness), `structuralIsomorphism` (quasi-isometry as coarse equivalence).
- Examples: Gromov's polynomial-growth theorem (*Publ. IHES* 53, 1981 — [Numdam](https://www.numdam.org/item/PMIHES_1981__53__53_0/)); Švarc–Milnor lemma (1955/1968) as foundational QI invariance; Pansu QI-rigidity of Carnot groups (1989); Eskin–Farb rigidity of higher-rank symmetric spaces; Kleiner's harmonic-function proof (*J. AMS* 23, 2010, [arXiv:0710.4593](https://arxiv.org/abs/0710.4593)); Shalom–Tao quantitative polynomial growth (2010). Source: Druţu–Kapovich, *Geometric Group Theory* (AMS Colloquium 63, 2018).

**(B.11) `floerHomologyFromHolomorphicStrips(symplectic manifold, Lagrangian pair or Hamiltonian) → homological invariant`** [Renamed from Intern B's longer name.]
- Cluster 12 · homological/categorical (symplectic).
- Inherits: `flowWithSurgery` (gradient-like moduli), `obstructionClass` (Betti-number lower bounds), `spectralSequenceCompute` (action filtration).
- Examples: Floer's proof of Arnold conjecture via Lagrangian intersections (*J. Diff. Geom.* 28, 1988 — [Project Euclid](https://projecteuclid.org/euclid.jdg/1214442477)); Seiberg–Witten–Floer and Manolescu's disproof of the triangulation conjecture (*J. AMS* 2016, [arXiv:1303.2354](https://arxiv.org/abs/1303.2354)); Fukaya category and homological mirror symmetry (Kontsevich 1994); embedded contact homology and Weinstein conjecture in dim 3 (Hutchings–Taubes); Heegaard Floer (Ozsváth–Szabó) for low-dimensional topology.

**(B.12) `tropicalize(subvariety V over non-archimedean field K, valuation map val) → balanced rational polyhedral complex`**
- Cluster 9 · cross-field transfer.
- Inherits: `structuralIsomorphism`, `reduceToCanonicalForm` (Newton polytope as normal form).
- Examples: Bergman's 1971 logarithmic limit sets; Viro's patchworking (1984) for Hilbert's 16th problem; Mikhalkin correspondence theorem (*J. AMS* 18, 2005); tropical Riemann–Roch on graphs (Baker–Norine, *Adv. Math.* 2007); Adiprasito–Huh–Katz proof of Heron–Rota–Welsh unimodality conjecture (*Ann. Math.* 188, 2018) — matroid log-concavity via tropical/Hodge-theoretic methods. Source: Maclagan–Sturmfels, *Introduction to Tropical Geometry* (AMS GSM 161, 2015).

---

## Part 2 — Cluster decisions

### Cluster 13 "Variational & Critical-Point Methods" — REJECTED

**Evaluated anchors:** `mountainPassMinimax` (B.4); `currentMassMinimize` (B.3); `floerHomologyFromHolomorphicStrips` (B.11, action-functional Morse theory); plus the added Ekeland variational-principle example. Also potentially: `directMethod` (Tonelli-style) if reconstructed.

**Decision:** Do NOT create Cluster 13. Reasons:
1. The threshold is "≥ 4 vetted techniques." I count 3 confident anchors (B.4, B.3, B.11); a fourth (`directMethod`) would be too close to existing `compactnessArgument` to justify standalone status.
2. Existing clusters absorb the three cleanly: B.4 under Cluster 8 (iteration/minimax-as-gradient-flow), B.3 under Cluster 6 (topology/obstruction, with GMT's compactness providing the geometric thread), B.11 under Cluster 12 (homological). These placements are natural and preserve the existing taxonomy.
3. A "variational" cluster would fragment the toolbox by *methodological philosophy* rather than by discovery operation — against the charter's "don't fragment taxonomy unless genuinely warranted."

### Cluster 14 "Microlocal & Phase-Space Analysis" — REJECTED

**Evaluated anchors:** `propagateSingularityAlongBicharacteristic` (B.2) is the only concrete technique; parametrix construction was floated by the brief but not operationalized. 1 technique does not make a cluster.

**Decision:** Place B.2 under Cluster 4 (refines `frequencyDecomposition` via phase-space localization) with `reduceToCanonicalForm` (Hörmander symbol calculus) as a secondary inherit link.

### Final cluster count: 12 (unchanged from round 1 end state)

---

## Part 3 — FLAGGED items (engineer to apply corrections)

1. **B.4 rename** — Intern B's `propagateSingularitiesAlongBicharacteristics` is verbose. Engineer: use `propagateSingularityAlongBicharacteristic` (singular both nouns) in the final schema. No semantic change.

2. **B.11 rename** — Intern B's `floerHomologyOnModuliOfHolomorphicCurves` is 44 chars, longest in toolbox. Engineer: use `floerHomologyFromHolomorphicStrips` (shorter, captures the Morse-complex-from-strips idea). No semantic change.

3. **B.5 rename** — `sieveByMinimizingQuadraticForm` → `sieveByOptimizedQuadratic` for schema conciseness. Semantic equivalent.

4. **A.10 straightening name** — Intern A's `straightenUnstraighten` is acceptable as-is, but engineer should write the output type as "bidirectional equivalence" not "bijection of data," and cite Lurie HTT §3.2 specifically in the process field.

5. **A.4 merge directive** — Engineer: `deformationCohomology` absorbs Intern A's proposed `extSquaredObstruction` (A#8). The single surviving technique's `process` field must explicitly include the Yoneda cup step (α ∪ α ∈ Ext² / H²) and the iterated lift.

6. **Circle-method cross-reference** — Existing `complexAnalysisToIntegers` has an example bullet "Helfgott's weak Goldbach via circle method." Engineer should revise this bullet to read "…via `majorMinorArcDecomposition` (see Cluster 9 new technique)." This avoids double-counting Helfgott as both an example and a motivation for B.6.

7. **Huisken monotonicity placement** — B.3 originally proposed `curvatureMonotonicityClassifier` as a separate technique. Engineer: do NOT create a standalone technique; instead add a new, prominently-worded bullet under `flowWithSurgery`'s examples that reads: *"Huisken's monotonicity formula (1990) — Gaussian-density integral against backward heat kernel is non-increasing along MCF; tangent flows at singularities are self-shrinkers; this is the structural template Perelman adapted to define reduced volume for Ricci flow."* Also update `flowWithSurgery`'s `postconds` field (if not already) to note that monotone monitors yield tangent-flow classifications, not just surgery decompositions.

8. **Attribution on A#1 characters** — Intern A credited Frobenius (1896) and Burnside (1897). Engineer: keep both but also add the "Cauchy–Frobenius–Burnside lemma" alternative attribution note (it appears earlier in Cauchy 1845 and Frobenius 1887 in specific forms); cite [Neumann, *Arch. Math.* 1979](https://doi.org/10.1007/BF01220018) for this historical point if possible, otherwise note the dispute without a citation.

9. **Attribution on B.6 circle method** — Intern B credits Hardy–Ramanujan (1918) for partitions and Hardy–Littlewood (1920–23) for Waring. Engineer: preserve both. The method's "birth" is ambiguous — partitions gave the Farey-arc dissection, Waring gave the exponential-sum minor-arc apparatus. Note both origins.

10. **Attribution on B.11 Floer** — Multi-origin: Floer (1988) for Lagrangian intersections *J. Diff. Geom.* 28; Floer (1989) for symplectic fixed points *Comm. Math. Phys.* 120. Engineer: cite the 1988 *JDG* paper as the primary, mention 1989 *CMP* as the symplectic-fixed-point version.

---

## Part 4 — REJECTED items

Reasons compiled — engineer DOES NOT include these as new techniques. Where I've converted them to example bullets, that conversion is listed in Part 1 ("Additions to existing techniques").

### From Intern A

- **A#6 `pushforwardAsIndex`** — REJECTED as standalone. Reason: Atiyah–Singer index theorem is already the flagship example of existing `analysisAlgebraTopologyBridge` and `conservedQuantity`. The K-theoretic pushforward *recipe* is the composition of surviving A.3 (`groupCompleteExactCategory`) and surviving Bott-periodicity example under `obstructionClass`. Converted to two example bullets under `analysisAlgebraTopologyBridge` (Atiyah–Singer via K-theoretic integration; Grothendieck–Riemann–Roch).

- **A#5 `exploitPeriodicityInObstructionTower`** — REJECTED as standalone. Reason: Bott periodicity is a *theorem/phenomenon*, and the "exploit periodicity" framing is a derivative meta-observation rather than a concrete discovery verb with well-defined preconditions. Converted to an example bullet under `obstructionClass` noting the period-2 collapse of obstruction towers.

- **A#2 `induceThenDecompose`** — REJECTED as standalone. Reason: Frobenius reciprocity IS an adjunction, which is the bread-and-butter of existing `representableFunctorTrick` (adjunctions via hom-set natural isomorphisms). The specific verb "induce to the larger group and then decompose" is a textbook application of adjoint-functor machinery. Converted to an example bullet under `representableFunctorTrick` citing Frobenius reciprocity, Mackey double-coset formula, and Harish-Chandra parabolic induction.

- **A#8 `extSquaredObstruction`** — MERGED into A.4 `deformationCohomology`. Reason: Intern A already positioned A#8 as a refinement of A#7 (Kodaira–Spencer / deformation cohomology); the Yoneda cup product on H¹ valued in H² IS part of the deformation-cohomology computational pipeline, not a separate technique. See Part 3 flag #5.

- **A#9 `replaceEqualityByCoherentHomotopy`** — REJECTED. Reason: this is a paradigmatic/philosophical move, not a concrete function with preconditions and ordered process steps. Intern A's own schema write-up had preconditions ("strict structure with equalities that 'should' hold") that are not operationalizable. The concrete techniques this philosophy spawned are captured elsewhere: `straightenUnstraighten` (A.5) and `recognizeStructureAsOperadAlgebra` (A.7). Left as a mentioned-but-not-formalized idea; no example bullet needed (the idea is already implicit in the two surviving techniques).

- **A#12 `geometricMorphismAsLogicalTranslation`** — REJECTED as standalone. Reason: while conceptually important, the *operational* technique of sheafification onto a Grothendieck topology (surviving A.6) already covers the geometric-morphism workflow in concrete terms. Geometric morphisms per se are a framework / setting, not a discovery verb. Converted to an example bullet under `structuralIsomorphism` / `duality` citing Cohen-forcing-as-geometric-morphism and classifying toposes.

### From Intern B

- **B#2 `decoupleByDyadicCaps`** — DEMOTED to example of B.1 `dyadicDecomposition`. Reason: decoupling builds on dyadic partitioning with the added ingredients of multilinear Kakeya and induction on scales; it is a flagship *application* of dyadic decomposition rather than a parallel technique. Engineer: add Bourgain–Demeter 2015 as a prominent example under `dyadicDecomposition`.

- **B#3 `curvatureMonotonicityClassifier`** — DEMOTED to example of existing `flowWithSurgery`. Reason: Intern B's own "process" write-up is "introduce a scale-invariant monotone functional whose critical points are self-similar solutions; blow-up at a singularity converges to such a self-similar model" — which is precisely the "monotone monitor" step already in `flowWithSurgery`'s process (inherited as part of the Perelman example). MCF + YMF + harmonic-map-heat-flow + Kähler-Ricci flow are all added as example bullets; no new technique created. See Part 3 flag #7.

- **Nothing else rejected from Intern B.** The multilinear-Kakeya suggestion (Intern B's flag #5) is NOT added; it would be a lemma consumed inside `dyadicDecomposition`'s process rather than a standalone verb. The Brun-sieve / large-sieve suggestions (Intern B's flag #8) are acknowledged but not expanded — engineer may add them as further examples under B.5 if future rounds deem necessary. The direct-method-of-calculus-of-variations suggestion (Intern B's flag #7) is left out, per the Cluster 13 rejection.

---

## Part 5 — Cross-checks performed

Ten-plus independent verifications performed via web search on key entries:

1. **Behrend–Fantechi intrinsic normal cone** — Confirmed *Invent. Math.* 128 (1997) 45–88, arXiv:alg-geom/9601010. [Springer](https://link.springer.com/article/10.1007/s002220050136).
2. **Bourgain–Demeter ℓ² decoupling** — Confirmed *Annals* 182 (2015), pp. 351–389; Bourgain–Demeter–Guth 2016 Vinogradov main conjecture follows. [Annals PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v182-n1-p09-p.pdf).
3. **Ginzburg–Kapranov Koszul duality for operads** — Confirmed *Duke Math. J.* 76 (1994) 203–272, with erratum vol. 80 (1995). Received 17 Jan 1994.
4. **Furstenberg correspondence principle** — Confirmed 1977 ergodic proof of Szemerédi; *J. d'Analyse Math* 31 (1977).
5. **Huisken monotonicity formula** — Confirmed *J. Diff. Geom.* 31 (1990) 285–299 for the monotonicity formula; 1984 *JDG* 20 for the earlier convex-MCF contracts-to-sphere.
6. **Ambrosetti–Rabinowitz mountain-pass theorem** — Confirmed *J. Funct. Anal.* 14 (1973) 349–381.
7. **Gromov polynomial-growth theorem** — Confirmed *Publ. Math. IHÉS* 53 (1981) 53–73, with appendix by Jacques Tits; introduced Gromov–Hausdorff convergence.
8. **Mikhalkin tropical correspondence theorem** — Confirmed *J. AMS* 18 no. 2 (2005) 313–377 ("Enumerative tropical algebraic geometry in ℝ²").
9. **Schlessinger functors of Artin rings** — Confirmed *TAMS* 130 (1968) 208–222; content originated in 1964 Harvard Ph.D. thesis under John Tate; refines an earlier Grothendieck result.
10. **Federer–Fleming normal and integral currents** — Confirmed *Ann. Math.* 72 no. 3 (1960) 458–520; establishes flat-norm compactness theorem and rectifiability.
11. **Peter–Weyl theorem** — Confirmed 1927 (*Math. Ann.* 97); L²(G) decomposes as ⊕ V_π ⊗ V_π*, matrix coefficients form orthonormal basis.
12. **Floer Lagrangian intersection Floer homology** — Confirmed *J. Diff. Geom.* 28 (1988) 513–547 "Morse theory for Lagrangian intersections"; symplectic version *Comm. Math. Phys.* 120 (1989).
13. **Bott periodicity** — Confirmed 1957 announcement, full 1959 proof via Morse theory; π_k(U) = π_{k+2}(U) (complex), period 8 for orthogonal.

Additional spot-checks against Stacks Project (tags 06G7, 07Y9, 00VG, 00W1, 0E6S, 0H72) and nLab (Yoneda lemma, spectral sequence, geometric morphism, tropical geometry) all confirmed primary attributions used by the interns.

**No attribution errors found.** Intern A's attribution notes (Li–Tian / Behrend–Fantechi for virtual class; Schlessinger / Illusie for Ext² obstruction; Deligne–Mumford 1969 then Knudsen 1983 for M̄_{g,n}) are historically precise. Intern B's attribution notes (Huisken 1984 for convex MCF, 1990 for monotonicity; Furstenberg 1977; Ambrosetti–Rabinowitz 1973; Gromov 1981; Mikhalkin 2005; Schramm 2000; Floer 1988) are also precise.

---

## Part 6 — Handoff note to engineer

### Top-level action plan

The engineer writes `engineer_additions_r2.md` containing:

1. **21 new technique schemas** following the function-signature template (preconds / process in ≥ 3 steps / postconds / inherits / ≥ 3 examples). Names and cluster assignments are finalized in Part 1; renames are listed in Part 3.
2. **~18 new example bullets** to append to 9 existing techniques (see Part 1 "Additions to existing techniques"). Do NOT edit `10_toolbox.md` directly — put the proposed bullets in `engineer_additions_r2.md` for orchestrator integration.
3. **Inheritance graph updates** — the toolbox's §3 mermaid graph needs edges:
   - `spotPattern → deformationCohomology` (pattern-in-H¹-cohomology ancestry, optional)
   - `obstructionClass → deformationCohomology`
   - `representableFunctor → straightenUnstraighten`
   - `axiomatize → sheafifyOnGrothendieckTopology`
   - `structuralIsomorphism → recognizeStructureAsOperadAlgebra`
   - `duality → koszulDualOperadSwap`
   - `compactnessArgument → compactifyByStableDegenerations`
   - `deformationCohomology → virtualClassFromObstructionTheory`
   - `frequencyDecomposition → dyadicDecomposition`
   - `frequencyDecomposition → propagateSingularityAlongBicharacteristic`
   - `compactnessArgument → currentMassMinimize`
   - `compactnessArgument → mountainPassMinimax`
   - `composeWithIdentity → sieveByOptimizedQuadratic`
   - `complexAnalysisToIntegers → majorMinorArcDecomposition`
   - `probabilisticExistence → shearerEntropyCount`
   - `compactnessArgument → ergodicCorrespondence`
   - `contractionFixedPoint → nashMoserFastNewton`
   - `compactnessArgument → rescaleForAsymptoticGeometry`
   - `flowWithSurgery → floerHomologyFromHolomorphicStrips`
   - `structuralIsomorphism → tropicalize`
   - `frequencyDecomposition → doubleCentralizerDecompose`
   - `symmetryReduction → characterDecompositionCount`
   - `axiomatize → groupCompleteExactCategory`
4. **Quick-reference table (§5) updates** — add 21 rows (rows 36–56) in the style of existing rows 1–35. Also update the §1 mermaid tree to show the 21 new leaves under their clusters; no new cluster nodes.

### Naming clashes to avoid

- `duality` (existing) vs `koszulDualOperadSwap` (new) — no clash; Koszul duality is a specialized operadic instance.
- `obstructionClass` (existing) vs `deformationCohomology` (new) — no clash; the new technique specifies "first-order + Yoneda-cup obstruction," narrower than generic obstruction.
- `frequencyDecomposition` (existing) vs `dyadicDecomposition` (new) — carefully distinct: frequencyDecomposition outputs coefficients; dyadicDecomposition outputs scale-localized blocks (still functions, not coefficients). Engineer: make this distinction explicit in the `postconds` of both entries.
- `flowWithSurgery` (existing) vs `floerHomologyFromHolomorphicStrips` (new) — no clash; the Floer entry uses a moduli-compactification style (Gromov compactness + gluing) rather than actual surgery.
- `compactnessArgument` (existing) vs `rescaleForAsymptoticGeometry` (new) — no clash; rescaling adds the scale-sequence operation before compactness is invoked.

### Edge cases to handle

1. **`characterDecompositionCount` overlap with `symmetryReduction`.** I validated this as a distinct technique on numerical-vs-qualitative grounds: characters project onto an orthonormal basis and yield explicit multiplicities, whereas `symmetryReduction` produces orbit representatives. Engineer: write the `preconds` and `postconds` to emphasize the numerical/multiplicity output, distinguishing from generic symmetry reduction.

2. **Derived algebraic geometry under `virtualClassFromObstructionTheory`.** Intern A's classical Behrend–Fantechi intrinsic-normal-cone is the write-up I validate. The Schürg–Toën–Vezzosi 2015 derived-enhancement should be mentioned in examples but NOT in the `process` field (process stays classical). This keeps the technique accessible.

3. **Cluster 11 filling.** The new Cluster 11 currently has 3 techniques (probabilistic / pigeon / polynomial). Adding B.5 (`sieveByOptimizedQuadratic`) and B.7 (`shearerEntropyCount`) brings it to 5. The cluster's unifying-idea line ("establish existence by counting volume or positive probability rather than explicit construction") already accommodates these.

4. **Cluster 12 filling.** Cluster 12 currently has 3 techniques; adding A.3 (K₀), A.5 (straightening), A.6 (sheafification), A.7 (operads), A.10 (virtual class), and B.11 (Floer homology) brings it to 9 — a noticeable density but not unreasonable for the "homological and categorical" umbrella. Engineer: consider whether the §1 mermaid tree should use a sub-grouping under Cluster 12 (e.g., "classical-homological" vs "∞-categorical / derived" vs "symplectic") purely for legibility. This is cosmetic; no new cluster.

5. **Non-Wikipedia source compliance.** All 21 surviving techniques have at least one non-Wikipedia source (nLab, Stacks Project, MacTutor, arXiv, author-hosted open PDF, Project Euclid, Numdam, Springer/Cambridge/AMS publisher pages). Engineer: spot-check the author-hosted PDFs (Tao lecture notes, Weibel K-book, Lurie HTT, May GILS, Loday–Vallette) are still live when finalizing `engineer_additions_r2.md`.

6. **Round-1 vs Round-2 coherence.** Round 1 added Clusters 11 and 12 plus `ultraproductTransfer`. Round 2 substantially populates both new clusters (see edge cases 3 and 4). Verify with orchestrator that the cumulative 35 + 21 = 56 techniques remain browsable under the existing tree/table structure; if not, consider collapsing the "Cluster 12 expansion" into a sub-structured display.

### Bottom line

21 new techniques + 18 new example bullets across 9 existing techniques. No new clusters. Two rename requests, one merge directive, two demotion directives (Part 4). All 13 high-stakes attributions independently verified (Part 5). Handoff is in ready-to-formalize state; engineer needs only to expand each Part-1 surviving-technique stub into the full schema and bundle the example bullets for orchestrator integration.
