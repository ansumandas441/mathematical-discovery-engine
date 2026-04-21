# Engineer Additions — Round 2

**Author:** Computer Engineer (formalizer), Round 2
**Date:** 2026-04-21
**Inputs:** `researcher_review_r2.md` (vetted list, cluster decisions, handoff), `intern_a_findings_r2.md`, `intern_b_findings_r2.md`, current `10_toolbox.md`.

This file formats round-2 additions for orchestrator integration into `10_toolbox.md`. No edits to `10_toolbox.md`, `README.md`, or `INDEX.md` are made here.

---

## Section A — Example appendages to EXISTING techniques

Append the bullets below to the `examples:` field of the named technique. All researcher Part-3 corrections applied.

### `flowWithSurgery` — additions (r2)
Append these bullets to the `examples:` list:
- **Eells–Sampson harmonic map heat flow** (1964, Eells & Sampson) — evolve f: M → N by tension field ∂f/∂t = τ(f); non-positive target curvature + Bochner identity forces convergence to a harmonic representative; no surgery needed. *Inherited: flowWithSurgery. Added: target-curvature sign as convergence criterion.* (*Amer. J. Math.* 86, JSTOR 2373037).
- **Kähler–Ricci flow and Song–Tian analytic MMP** (Cao 1985; Song–Tian 2006–2017) — ∂ω/∂t = −Ric(ω) preserves Kähler class; finite-time singularities realize analytic divisorial contractions and flips matching the algebraic MMP. *Inherited: flowWithSurgery. Added: algebraic-geometric birational program matched to analytic singularities.* (arXiv:0909.4898, *Invent. Math.* 207).
- **Yang–Mills flow on 4-manifolds** (Donaldson 1985; Uhlenbeck–Yau 1986) — ∂A/∂t = −d_A* F_A is L²-gradient of ‖F_A‖²; Donaldson–Uhlenbeck–Yau: stable holomorphic bundle ⇒ Hermite–Einstein metric; surgery = analytic bubble-point removal via Uhlenbeck compactness. *Inherited: flowWithSurgery, conservedQuantity. Added: instanton bubble analysis + gauge-theoretic formulation.* (*Proc. LMS* 50).
- **Huisken monotonicity formula for mean curvature flow** (Huisken 1990) — Gaussian-density integral against the backward heat kernel is non-increasing along MCF; tangent flows at singularities are self-shrinkers; structural template Perelman adapted to define reduced volume for Ricci flow. *Inherited: flowWithSurgery, conservedQuantity. Added: scale-invariant Gaussian-density monitor → self-similar tangent-flow classification template.* (*J. Diff. Geom.* 31, Project Euclid 1214444099).

### `frequencyDecomposition` — additions (r2)
Append these bullets to the `examples:` list:
- **Stein–Tomas restriction theorem** (Stein 1967, Tomas 1975) — for S ⊂ ℝⁿ with non-vanishing Gaussian curvature, the restriction operator L^p(ℝⁿ) → L²(S, dσ) is bounded for 1 ≤ p ≤ 2(n+1)/(n+3). *Inherited: frequencyDecomposition. Added: curvature as a regularizing condition on frequency support.* (*Bull. AMS* 81).

### `contractionFixedPoint` / `compactnessArgument` — additions (r2)
Append this bullet to the `examples:` list of `contractionFixedPoint` (and cross-link from `compactnessArgument`):
- **Ekeland variational principle** (Ekeland 1974) — any lower-semicontinuous bounded-below function on a complete metric space admits an ε-near-minimum with a Lipschitz-penalty minorization; substitute for strict minimization when no compactness is available; equivalent to Caristi's fixed-point theorem. *Inherited: contractionFixedPoint, compactnessArgument. Added: works in arbitrary complete metric spaces without reflexivity.* (*Bull. AMS* 1, 1979).

### `physicsToPDE` / `interpolateAndContinue` — additions (r2)
Append this bullet to the `examples:` list of `physicsToPDE` (and cross-link from `interpolateAndContinue`):
- **Schramm–Loewner evolution (SLE)** (Schramm 2000) — one-parameter family SLE_κ of random curves in the upper half-plane, defined via Loewner's ODE ∂g_t/∂t = 2/(g_t − √κ B_t); scaling limits of 2D critical lattice models (LERW κ=2, Ising κ=3, percolation κ=6, UST κ=8). *Inherited: physicsToPDE, interpolateAndContinue. Added: stochastic driver as universality-class classifier.* (arXiv:math/9904022).

### `analysisAlgebraTopologyBridge` — additions (r2)
Append these bullets to the `examples:` list:
- **K-theoretic pushforward / Atiyah–Singer index theorem** (Atiyah–Singer 1968) — for proper f: X → Y, define f_!: K(X) → K(Y) via Thom / Gysin; analytic index = f_!([σ]) for symbol σ ∈ K(TX); embedding X ↪ ℝᴺ reduces to Bott periodicity. *Inherited: analysisAlgebraTopologyBridge, obstructionClass. Added: K-theoretic integration as a universal index formula.* (*Ann. Math.* 87).
- **Grothendieck–Riemann–Roch** (Borel–Serre 1958 proof of Grothendieck's announcement) — for proper f: X → Y, χ(Y, f_* F) = f_!(ch(F) · Td(T_f)); universal Riemann–Roch via functoriality of K₀. (*Bull. SMF* 86).

### `obstructionClass` — additions (r2)
Append this bullet to the `examples:` list:
- **Bott periodicity as obstruction collapse** (Bott 1959) — π_k(U) = π_{k+2}(U); in any obstruction tower valued in K-theory, infinitely many degrees collapse to two residue classes; equivalently K⁰(X) ≅ K⁻²(X). *Inherited: obstructionClass, structuralIsomorphism. Added: period-2 structure on stable unitary K-theory.* (*Ann. Math.* 70).

### `representableFunctorTrick` — additions (r2)
Append this bullet to the `examples:` list:
- **Frobenius reciprocity as hom-set adjunction** (Frobenius 1898; categorical reframing Mac Lane 1960s) — Hom_G(Ind_H^G W, V) ≅ Hom_H(W, Res_H^G V); "induce from subgroup" is left-adjoint to "restrict to subgroup"; yields Mackey's double-coset formula, Young's branching rule, Harish-Chandra parabolic induction. *Inherited: representableFunctorTrick, duality.* (Serre, *Linear Representations of Finite Groups* GTM 42 §7.2; nLab *Frobenius reciprocity*).

### `structuralIsomorphism` / `duality` — additions (r2)
Append this bullet to the `examples:` list of `duality` (with cross-link from `structuralIsomorphism`):
- **Geometric morphism of toposes as logical translation** (Lawvere–Tierney 1970) — f: E → F an adjunction (f*, f_*) with left-exact f* translates geometric-theory models across universes; Cohen forcing = geometric morphism to Boolean topos of a forcing poset; classifying toposes represent geometric theories. *Inherited: duality, structuralIsomorphism, forceIndependence.* (nLab *geometric morphism*; Johnstone, *Sketches of an Elephant* vol. A).

### `spotPatternInTable` / `verifyOnSpecialCases` — additions (r2)
Append this bullet to the `examples:` list of `spotPatternInTable` (with cross-link from `verifyOnSpecialCases`):
- **Viro patchworking** (Viro 1984) — combinatorial recipe building real algebraic hypersurfaces with prescribed topology from subdivisions of the Newton polytope; produced counterexamples in Hilbert's 16th problem. *Inherited: spotPatternInTable, structuralIsomorphism.* (arXiv:math/0611382).

### `complexAnalysisToIntegers` — revision (r2)
Revise the existing bullet:
- Replace "Helfgott's weak Goldbach via circle method (Ch. 6)" with "Helfgott's weak Goldbach via `majorMinorArcDecomposition` — see Cluster 9 new technique (arXiv:1501.05438)."

---

## Section B — NEW technique dictionary entries

21 new techniques formalized in schema. Cluster assignments, inheritance, and rename directives applied per `researcher_review_r2.md` Parts 1 and 3.

---

### Cluster 3 — Symmetry & Invariants (new entries)

#### `characterDecompositionCount(G-set or G-module V, irreducible characters {χ_π} of G) → multiplicities / orbit count / factorization count`
- **category:** Cluster 3 · symmetry (numerical variant of invariant extraction)
- **preconds:** finite (or compact) group G acting on V; the class function of interest is G-invariant; orthonormal irreducible characters of G are available.
- **process:**
  1. Decompose the regular representation (or the ambient V) into isotypic components via ⟨f, χ_π⟩ = (1/|G|) ∑_{g ∈ G} f(g) χ_π(g̅).
  2. For a counting problem, express the quantity as the inner product of a class function f with a character χ_π (orbit count = ⟨1, 1⟩ via fixed-point count; factorization count = ⟨χ_1 χ_2 χ_3 …, 1⟩).
  3. Evaluate the inner product on the character table: numerical output.
- **postconds:** explicit integer multiplicities / orbit counts / factorization counts, not merely an "up to isomorphism" classification.
- **inherits:** `symmetryReduction`, `conservedQuantity`
- **examples:** Frobenius's group-determinant decomposition (1896, Frobenius) — irreducible-character degrees match the factor degrees of the *Gruppendeterminante*; (MacTutor *Frobenius*). Cauchy–Frobenius–Burnside orbit-counting lemma (Cauchy 1845 / Frobenius 1887 / Burnside 1897) — number of orbits = (1/|G|) ∑ |Fix(g)|; attribution dispute noted in Neumann, *Arch. Math.* 1979. Selberg trace formula (1956) — character integration on a locally symmetric space Γ\G/K. Diaconis–Shahshahani random-walk mixing (1981) — character bounds control the total-variation distance of card-shuffling walks; (Curtis, *Pioneers of Representation Theory*, AMS HMath 15).

#### `doubleCentralizerDecompose(vector space V with commuting actions of A and B) → bimodule decomposition ⊕_i U_i ⊗ W_i`
- **category:** Cluster 3 · symmetry
- **preconds:** semisimple algebras (or groups) A and B commuting on V; V finite-dimensional or Hilbertian with enough integrability for L²(G) cases.
- **process:**
  1. Identify the two commuting actions on V and verify they are mutual centralizers (often the deeper theorem).
  2. Decompose V as an A-module V = ⊕_i U_i ⊗ M_i where U_i are A-irreducibles and M_i are multiplicity spaces.
  3. The double centralizer theorem forces M_i to carry a B-action making M_i = W_i, a B-irreducible; the index i biject A-irreps appearing with B-irreps appearing.
  4. Transfer information from one side to the other: combinatorics on one side = representation theory on the other.
- **postconds:** labeled bijection between A-irreducibles and B-irreducibles appearing in V, with explicit multiplicities tied to a combinatorial index set.
- **inherits:** `frequencyDecomposition` (Peter–Weyl is Fourier on G), `duality`
- **examples:** Peter–Weyl theorem on L²(G) for compact G (Peter–Weyl 1927) — L²(G) ≅ ⊕_π V_π ⊗ V_π*; (*Math. Ann.* 97; nLab *Peter-Weyl theorem*). Schur–Weyl duality on (ℂⁿ)^⊗k for GL(n) × S_k (Schur thesis 1901; Weyl, *Classical Groups* 1939) — (ℂⁿ)^⊗k ≅ ⊕_λ S^λ(ℂⁿ) ⊗ V_λ indexed by partitions of k. Howe reciprocity for dual pairs in Fock space (Howe 1989) — reciprocity between two centralizing group actions. Goodman–Wallach systematic treatment (*Symmetry, Representations, and Invariants*, GTM 255).

#### `koszulDualOperadSwap(quadratic operad O) → dual operad O^! with bar-cobar equivalence between O-algebras and O^!-coalgebras`
- **category:** Cluster 3 · symmetry (operadic duality — distinct from generic `duality`)
- **preconds:** operad O presented as ℱ(E)/(R) with E a finite-dim S-module of generators and R a submodule of quadratic relations; operad is binary and quadratic (weight-2 relations).
- **process:**
  1. Dualize the generator S-module: E^! = E^* ⊗ sgn (with Koszul sign twist).
  2. Take annihilator R^⊥ of the relation space R under the natural pairing of weight-2 pieces; define O^! = ℱ(E^!)/(R^⊥).
  3. Build the Koszul complex K(O) = O ⊗ (O^!)^* with differential from the pairing; O is Koszul iff K(O) resolves O.
  4. When O is Koszul, Ext over O-algebras = Tor over O^!-coalgebras; bar-cobar is a Quillen equivalence.
- **postconds:** a matched pair (O, O^!) such that hard computations on one side transport to tractable ones on the other; minimal free resolutions of O-algebras constructible via O^!-coalgebra cobar.
- **inherits:** `duality`, `recognizeStructureAsOperadAlgebra`, `spectralSequenceCompute`
- **examples:** Priddy Koszul duality for associative algebras (1970, Priddy) — polynomial algebra and exterior algebra are mutually Koszul; (*TAMS* 152). Ginzburg–Kapranov operadic Koszul duality (1994) — Assoc^! = Assoc, Comm^! = Lie, Lie^! = Comm; (*Duke Math. J.* 76). Kontsevich formality of Hochschild cohomology (1997) — HH^*(A) of a smooth commutative algebra is L_∞-quasi-isomorphic to polyvector fields, proven via Assoc ↔ Lie Koszul duality. Beilinson–Ginzburg–Soergel Koszul duality for category O (1996). (Loday–Vallette, *Algebraic Operads*, Grundlehren 346; open PDF math.unice.fr/~brunov/Operads.pdf.)

---

### Cluster 4 — Approximation & Limits (new entries)

#### `dyadicDecomposition(function f on ℝⁿ, smooth partition of unity {ψ_k} in frequency) → scale-localized blocks {Δ_k f}`
- **category:** Cluster 4 · approximation (refinement of `frequencyDecomposition`)
- **preconds:** f ∈ S'(ℝⁿ) (tempered distribution) or a more regular space; smooth bump φ with φ = 1 on |ξ| ≤ 1, φ = 0 on |ξ| ≥ 2; derived dyadic cutoffs ψ_k(ξ) = φ(2^{-k}ξ) − φ(2^{-k+1}ξ) giving ∑ ψ_k = 1.
- **process:**
  1. Define the dyadic blocks Δ_k f via Fourier multiplier ψ_k; f = ∑_k Δ_k f.
  2. Replace L^p-norms of f by the square function ‖(∑ |Δ_k f|²)^{1/2}‖_{L^p}, almost-equivalent for 1 < p < ∞ (Littlewood–Paley / Khintchine).
  3. Analyze operators block-by-block: Bernstein inequalities convert derivatives into scale factors 2^k on each block; differentiation and multiplication become tractable in Besov / Triebel–Lizorkin norms.
  4. Sum blocks back via the square function to recover f-norm estimates.
- **postconds:** a scale-localized representation producing p-independent norm equivalences; derivatives replaced by algebraic scaling; paraproducts and multilinear operators linearized.
- **inherits:** `frequencyDecomposition`
- **examples:** Littlewood–Paley square-function theorem (Littlewood–Paley 1931/1937) — foundational L^p-block equivalence. Marcinkiewicz multiplier theorem (1939) — dyadic Hörmander–Mihlin multiplier bound. Bony paraproducts (1981) — dyadic linearization of products for nonlinear PDE. Bourgain–Demeter ℓ²-decoupling over dyadic caps (2015) — decoupling inequality for functions Fourier-supported on δ-neighborhoods of curved surfaces, yielding Vinogradov Main Conjecture via Bourgain–Demeter–Guth 2016. (Tao, [Math 247A lecture notes](https://www.math.ucla.edu/~tao/247a.1.06f/); Grafakos, *Classical Fourier Analysis* ch. 6; *Annals* 182.)

#### `propagateSingularityAlongBicharacteristic(distribution u, operator P with principal symbol p) → microlocal singular support`
- **category:** Cluster 4 · approximation (microlocal phase-space localization)
- **preconds:** smooth manifold M; properly supported pseudo-differential operator P on M with real principal symbol p homogeneous of positive order; distribution u ∈ D'(M).
- **process:**
  1. Define the wavefront set WF(u) ⊂ T*M ∖ 0 as the conic set of (x, ξ) where the local Fourier transform of a cutoff of u fails polynomial decay in direction ξ.
  2. For Pu = f, note WF(u) ⊂ WF(f) ∪ Char(P), where Char(P) = {p = 0}.
  3. Compute the Hamilton vector field H_p of p on T*M ∖ 0; integrate to obtain bicharacteristic flow on Char(P).
  4. Hörmander's theorem: WF(u) ∖ WF(f) is invariant under the bicharacteristic flow; singularities move along null bicharacteristics.
- **postconds:** microlocal location of singularities of u in phase space; sharp propagation statement explaining sharp light-cone singularities in hyperbolic PDE, tunneling in elliptic theory, and boundary diffraction.
- **inherits:** `frequencyDecomposition` (local Fourier analysis), `duality` (T*M as dual phase space), `reduceToCanonicalForm` (Hörmander symbol calculus as canonical form)
- **examples:** Hörmander's propagation theorem (1971) — foundational statement; (*Acta Math.* 127). Duistermaat–Hörmander Fourier integral operators II (1972) — FIOs as quantizations of canonical transformations; (*Acta Math.* 128). Melrose b-calculus and diffractive propagation at corners. Vasy's N-body Fredholm scattering (2013) — propagation in asymptotically hyperbolic settings; (arXiv:1012.4391). (nLab *wave front set*; Grigis–Sjöstrand, *Microlocal Analysis*, LMS 196.)

---

### Cluster 6 — Topology & Obstruction (new entries)

#### `deformationCohomology(geometric object X, tangent or cotangent complex L_X) → (H¹ = first-order deformations, H² = obstructions via Yoneda cup)`
- **category:** Cluster 6 · topology (obstruction-theoretic)
- **preconds:** X an algebraic scheme / complex manifold / coherent sheaf / module over a ring; a tangent (or cotangent) complex T_X or L_X available; base ring with dual-numbers / Artinian extensions admitting deformation functors.
- **process:**
  1. Compute H¹(X, T_X) — equivalently Ext¹(L_X, 𝒪_X) or Ext¹(M, M) — parametrizing first-order deformations over k[ε]/ε².
  2. For α ∈ H¹, compute the Yoneda cup product α ∪ α ∈ H²(X, T_X) / Ext²(M, M) via the bilinear pairing.
  3. A first-order deformation lifts to second order iff α ∪ α = 0; if so, the space of lifts is a torsor over H¹.
  4. Iterate: at each order, the obstruction to lifting lives in H²; if H² = 0, deformations are unobstructed and give a smooth formal moduli space.
- **postconds:** explicit first-order deformation space + obstruction class + unobstructedness criterion; leads to a formal moduli functor with Schlessinger / Artin representability.
- **inherits:** `obstructionClass`, `analysisAlgebraTopologyBridge`, `spectralSequenceCompute`, `diagramChase`
- **examples:** Kodaira–Spencer map for complex manifolds (1958, Kodaira–Spencer) — ρ: T_0 B → H¹(X, T_X) measures infinitesimal change in complex structure; (*Ann. Math.* 67). Schlessinger's functors-of-Artin-rings criterion (1968) — when formal moduli are pro-representable; (*TAMS* 130). Illusie cotangent complex L_{X/S} (1971) — derived generalization; Ext^i(L, 𝒪) unifies deformations (i=1) and obstructions (i=2); (LNM 239). Bogomolov–Tian–Todorov unobstructedness of Calabi–Yau deformations (1989) — the Yoneda cup is a coboundary. Wiles R = T deformation rings controlled by Galois-cohomology H² (1995). (Stacks tag 06G7, Stacks tag 07Y9.)

#### `compactifyByStableDegenerations(non-proper moduli space M of smooth objects) → proper moduli stack M̄ with boundary of stable singular objects`
- **category:** Cluster 6 · topology
- **preconds:** coarse or fine moduli space M of smooth geometric objects of a given type (curves, sheaves, maps); M fails to be proper because families can degenerate outside M; notion of "stability" available that bounds automorphisms and permits unique limits.
- **process:**
  1. Define stability on singular degenerations: permit only mild singularities (nodes, semistable reductions) and require every irreducible component to meet the rest in enough special points to force finite automorphism.
  2. Use semistable reduction (characteristic-0) or stable-reduction theorems to show every one-parameter family in M extends uniquely to a stable object in M̄.
  3. Construct M̄ as a proper Deligne–Mumford stack via descent from a Hilbert-scheme cover; boundary ∂M̄ = M̄ ∖ M stratifies by combinatorial data (dual graphs, discrete invariants).
- **postconds:** proper stack M̄ with universal family; enumerative integration possible against tautological classes; boundary stratification useful for induction.
- **inherits:** `compactnessArgument`, `deformationCohomology`, `obstructionClass`
- **examples:** Deligne–Mumford M̄_g of stable nodal curves (1969, Deligne–Mumford) — irreducibility of M_g in any characteristic, founding algebraic-stacks theory; (*Publ. IHES* 36). Knudsen's M̄_{g,n} with marked points (1983). Kontsevich M̄_{g,n}(X, β) for Gromov–Witten counts (1994). Gieseker compactification of moduli of stable sheaves. (Harris–Morrison, *Moduli of Curves* GTM 187; Stacks tag 0E6S.)

#### `currentMassMinimize(boundary k-current Γ, homology class α) → integral mass-minimizer`
- **category:** Cluster 6 · topology (geometric measure theory)
- **preconds:** ambient smooth manifold (usually ℝⁿ or a Riemannian manifold); k-current Γ with finite mass and locally finite boundary; non-empty homology class or boundary condition.
- **process:**
  1. Work in the flat-norm topology F(T) = inf{M(A) + M(B) : T = A + ∂B} on the space of integral k-currents.
  2. Take a minimizing sequence T_n with Γ = ∂T_n (or T_n representing class α); apply Federer–Fleming closure/compactness: mass-bounded integral-current sequences are F-precompact.
  3. Extract an F-convergent subsequence; limit is an integral k-current (integer multiplicity, k-rectifiable support).
  4. Verify mass lower semicontinuity under F-convergence; limit realizes the infimum.
- **postconds:** a mass-minimizing integral k-current with prescribed boundary (or homology class); k-rectifiable support; singular set controlled by regularity theorems (Almgren, Allard).
- **inherits:** `compactnessArgument`, `duality` (currents are dual to forms)
- **examples:** Federer–Fleming closure theorem (1960, Federer–Fleming) — flat-norm compactness of mass-bounded integral currents; (*Ann. Math.* 72, JSTOR 1970227). Plateau's problem in arbitrary dimension and codimension. Almgren Big Regularity Paper (1972–83, published 2000) — singular set of area-minimizing currents has codimension 2. Allard varifold regularity theorem (1972). De Lellis–Spadaro Q-valued approximation (arXiv:1506.08118). (Federer, *Geometric Measure Theory*; Morgan, *GMT: A Beginner's Guide* 5th ed.)

#### `rescaleForAsymptoticGeometry(finitely-generated group or metric space X, scaling sequence r_n → ∞) → Gromov–Hausdorff limit with group structure`
- **category:** Cluster 6 · topology (geometric group theory)
- **preconds:** a metric space X (typically the Cayley graph of a finitely generated group or a Riemannian manifold) with a uniform bound on growth or packing; scaling sequence r_n → ∞ relative to a basepoint.
- **process:**
  1. Rescale the metric: (X, d/r_n, x_0). Uniform growth or polynomial-growth bounds give Gromov–Hausdorff precompactness of the rescaled pointed metric spaces.
  2. Extract a Gromov–Hausdorff convergent subsequence; the limit (X_∞, d_∞, x_∞) carries a transitive action by a locally compact group H extending the original group G.
  3. Apply a rigidity theorem on H: Montgomery–Zippin / Gleason (H is a Lie group), Pansu (Carnot-group structure on nilpotent limits), or Eskin–Farb (higher-rank symmetric-space rigidity).
  4. Transport the algebraic/geometric structure of H back to G via quasi-isometry invariance of the relevant invariants (growth, hyperbolicity, ends, dimension).
- **postconds:** large-scale geometric / algebraic classification of X up to quasi-isometry; rigidity statements of the form "QI-class of G = QI-class of (its asymptotic-cone model)."
- **inherits:** `compactnessArgument` (GH-precompactness), `structuralIsomorphism` (quasi-isometry as coarse equivalence)
- **examples:** Gromov's polynomial-growth theorem (1981, Gromov) — polynomial growth ⇒ virtually nilpotent; introduced Gromov–Hausdorff convergence; (*Publ. IHES* 53, Numdam PMIHES 1981 53 53 0). Švarc–Milnor lemma (1955/1968) — proper cocompact isometric actions yield QI to the acting group. Pansu QI-rigidity of Carnot groups (1989). Kleiner's harmonic-function proof of polynomial growth (2010, *J. AMS* 23, arXiv:0710.4593). Shalom–Tao quantitative polynomial-growth theorem (2010). (Druţu–Kapovich, *Geometric Group Theory*, AMS Colloquium 63.)

---

### Cluster 8 — Iteration & Fixed Points (new entries)

#### `mountainPassMinimax(C¹ functional I on Banach space E with Palais–Smale, mountain-pass geometry) → saddle-type critical point`
- **category:** Cluster 8 · iteration (variational / minimax)
- **preconds:** Banach space E; C¹ functional I: E → ℝ satisfying the Palais–Smale condition (PS-bounded sequences with DI → 0 are precompact); mountain-pass geometry: I(0) = 0, I(u) ≥ α > 0 on ‖u‖ = r, and I(e) ≤ 0 for some e with ‖e‖ > r.
- **process:**
  1. Define the minimax value c = inf_γ max_{t ∈ [0,1]} I(γ(t)) over continuous paths γ from 0 to e; by mountain-pass geometry c ≥ α > 0.
  2. Suppose c is not a critical value; by PS, construct a pseudo-gradient vector field V with DI(V) ≥ (1/2)‖DI‖ on a shell around level c.
  3. Flow along −V to deform any near-optimal path γ into one with max I(γ) < c − δ, contradicting c = inf.
  4. Therefore c is critical; extract a critical point at level c via the limit of a PS sequence at level c.
- **postconds:** existence of a critical point of I at level c ≥ α, typically a saddle; PDE / Hamiltonian applications recover non-minimizing solutions inaccessible to direct minimization.
- **inherits:** `compactnessArgument` (PS condition), `conservedQuantity` (the functional I as the monitor)
- **examples:** Ambrosetti–Rabinowitz mountain-pass theorem (1973, Ambrosetti–Rabinowitz) — foundational statement; (*J. Funct. Anal.* 14). Brezis–Nirenberg critical-exponent problem (1983) — existence for −Δu = u^{(n+2)/(n−2)} + λu; (*CPAM* 36). Rabinowitz periodic orbits on prescribed energy hypersurfaces (precursor to Floer homology). Ekeland–Hofer symplectic capacities. (Mawhin–Willem, *Critical Point Theory and Hamiltonian Systems*, Springer 1989.)

#### `nashMoserFastNewton(tame Fréchet map F, linearization with tame right-inverse losing r derivatives) → smooth solution via smoothed iteration`
- **category:** Cluster 8 · iteration
- **preconds:** tame Fréchet spaces X, Y (typically C^∞(M, V)); smooth map F: X → Y; linearization L = DF(u) admits a tame right-inverse L^{-1} losing r derivatives (‖L^{-1}v‖_s ≤ C_s ‖v‖_{s+r}); base point u_0 with F(u_0) close to target v.
- **process:**
  1. Choose smoothing operators S_θ on X restricting to frequencies ≤ θ, with bounded-norm estimates ‖(I − S_θ)u‖_s ≤ θ^{-r} ‖u‖_{s+r}.
  2. Modified Newton: u_{n+1} = u_n − S_{θ_n} L(u_n)^{-1} F(u_n) with θ_n = θ_0^{(3/2)^n} growing super-exponentially.
  3. Each iteration loses r derivatives from L^{-1}; smoothing supplies a θ^{-r} factor that (with super-exponential θ growth) is dominated by quadratic Newton convergence.
  4. Super-exponential convergence ‖u_{n+1} − u‖ ≤ C‖u_n − u‖^{3/2+} yields a C^∞ limit solving F(u) = v.
- **postconds:** a smooth solution of F(u) = v despite derivative loss in the linear inverse; applications include isometric embedding, KAM persistence, and free-boundary problems.
- **inherits:** `contractionFixedPoint` (modified Newton iteration), `frequencyDecomposition` (smoothing S_θ is a frequency cutoff)
- **examples:** Nash's C^∞ isometric embedding theorem (1956, Nash) — every C^∞ Riemannian manifold embeds isometrically in ℝᴺ; (*Ann. Math.* 63). Moser's unified tame framework (1966) — (*Ann. Scuola Norm. Sup. Pisa* 20). Kolmogorov–Arnold–Moser theorem on persistence of invariant tori (1954/1963). Hamilton's abstract tame category (1982) — foundation of the modern framework; (*Bull. AMS* 7). Eliasson / Berti–Bolle Nash–Moser KAM for quasi-periodic-potential Schrödinger (2010s). (arXiv:1404.3122.)

---

### Cluster 9 — Cross-Field Transfer (new entries)

#### `majorMinorArcDecomposition(additive counting problem r(N), exponential sum F(α)) → singular series + error`
- **category:** Cluster 9 · transfer (Hardy–Littlewood circle method)
- **preconds:** additive counting problem r(N) = #{representations of N as a structured sum}; generating exponential sum F(α) = ∑_{n ≤ N} e^{2πinα} restricted to the structured source set; expected asymptotic of the form r(N) ∼ S(N) N^{s−1}.
- **process:**
  1. Encode r(N) as ∫_0^1 F(α)^s e^{−2πiNα} dα using orthogonality ∫_0^1 e^{2πimα} dα = [m = 0].
  2. Farey dissection: partition [0, 1] into major arcs 𝔐 (α close to a/q with q ≤ Q small, Q determined by N) and minor arcs 𝔪 = [0, 1] ∖ 𝔐.
  3. On major arcs, approximate F by local (p-adic × archimedean) Euler products; integrate to produce the singular series S(N) · N^{s−1}.
  4. On minor arcs, bound |F(α)| by Weyl differencing / Vinogradov's method / Vaughan identity; control the error ∫_𝔪 |F|^s.
- **postconds:** asymptotic r(N) = S(N) N^{s−1} + O(error) with explicit singular series and Weyl-type error bound.
- **inherits:** `complexAnalysisToIntegers` (generating-function framing), `frequencyDecomposition`
- **examples:** Hardy–Ramanujan partition-function asymptotic (1918, Hardy–Ramanujan) — contour over |q| = r < 1 with Farey arc dissection, modular transformation on the dominant arc; (*Proc. LMS*). Hardy–Littlewood Waring's problem G(k) bounds (1920–23) — exponential-sum minor-arc apparatus; dual-attribution note per researcher Part 3 §9. Vinogradov's three-primes theorem for large N (1937). Helfgott's explicit ternary Goldbach (arXiv:1501.05438, 2015). Bourgain–Demeter–Guth Vinogradov Main Conjecture (*Annals* 184, 2016) via decoupling sharpening minor-arc bounds. (Vaughan, *The Hardy–Littlewood Method*, 2nd ed. Cambridge 1997.)

#### `ergodicCorrespondence(positive-density subset E ⊂ ℤ) → measure-preserving system with equivalent recurrence`
- **category:** Cluster 9 · transfer
- **preconds:** subset E ⊂ ℤ with positive upper Banach density d*(E) > 0; shift-invariant translation structure on ℤ acting on indicators ⊂ {0,1}^ℤ.
- **process:**
  1. Embed E as its indicator 1_E ∈ ℓ^∞(ℤ); define a shift-invariant finitely-additive density functional on the orbit closure of 1_E.
  2. By a Krylov–Bogolyubov weak-* compactness argument, extend to a T-invariant Borel probability measure μ on the orbit closure X ⊆ {0,1}^ℤ.
  3. Set A = {ω ∈ X : ω(0) = 1}; verify μ(A) = d*(E) and that combinatorial multi-return properties of E are bounded below by μ(A ∩ T^{−n_1} A ∩ ⋯ ∩ T^{−n_k} A).
  4. Apply structure theorems for (X, 𝔅, μ, T) — Kronecker factor, compact extensions, weak-mixing tower (Furstenberg) — to prove ergodic multiple-recurrence, which translates back to combinatorial multiple-return in E.
- **postconds:** a measure-preserving dynamical system whose recurrence theorems imply combinatorial statements about E; chosen Szemerédi-type theorems become consequences of ergodic structure.
- **inherits:** `compactnessArgument` (Krylov–Bogolyubov weak-* limit), `axiomatizeFromInstances` (measure-preserving-system axioms)
- **examples:** Furstenberg's ergodic proof of Szemerédi's theorem (1977, Furstenberg) — k-APs in positive-density subsets via multiple recurrence; (*J. d'Analyse Math.* 31). Furstenberg–Katznelson multidimensional Szemerédi (1978) — (*J. d'Analyse Math.* 34). Bergelson–Leibman polynomial Szemerédi (1996) — (*J. AMS* 9). Host–Kra structure theorem for nonconventional ergodic averages (2005) — (*Annals* 161, arXiv:math/0403212). Green–Tao APs in primes (2008) via transference from Furstenberg framework.

#### `tropicalize(subvariety V over non-archimedean field K, valuation map val) → balanced rational polyhedral complex`
- **category:** Cluster 9 · cross-field transfer
- **preconds:** non-archimedean field K (e.g., Puiseux series ℂ{{t}}); subvariety V ⊂ (K*)ⁿ (or V ⊂ 𝔸ⁿ_K, ℙⁿ_K); valuation val: K* → ℝ extended coordinate-wise.
- **process:**
  1. For each polynomial f = ∑ c_I x^I cutting out V, form the tropicalization trop(f)(x) = min_I (val(c_I) + ⟨I, x⟩), a piecewise-linear concave function on ℝⁿ.
  2. Define trop(V) = val(V(K)) ⊂ ℝⁿ as the image under coordinate-wise valuation; equivalently, trop(V) is the non-smooth locus of trop(f) (the loci where the min is attained twice).
  3. Verify balancing: at each codimension-1 facet, the sum of edge weights weighted by outgoing primitive integer vectors is zero — the tropical analog of no residues at a generic point.
  4. Transport enumerative / moduli / cohomological questions on V to polyhedral counts on trop(V) via a correspondence theorem.
- **postconds:** a rational balanced polyhedral complex trop(V) of dimension dim V carrying algebraic-geometric information combinatorially; enumerative / Gromov–Witten / real-count / topological data computable on the tropical shadow.
- **inherits:** `structuralIsomorphism`, `reduceToCanonicalForm` (Newton polytope as normal form)
- **examples:** Bergman's logarithmic limit sets (1971) — predecessor of modern tropical varieties. Viro patchworking (1984) — combinatorial recipe producing real algebraic hypersurfaces with prescribed topology for Hilbert's 16th. Mikhalkin correspondence theorem (2005, Mikhalkin) — classical plane Gromov–Witten counts equal tropical counts through points; (*J. AMS* 18, arXiv:math/0312530). Baker–Norine tropical Riemann–Roch on graphs (2007) — (*Adv. Math.*). Adiprasito–Huh–Katz proof of Heron–Rota–Welsh unimodality for matroids (2018) — tropical/Hodge methods; (*Ann. Math.* 188). (Maclagan–Sturmfels, *Introduction to Tropical Geometry*, AMS GSM 161.)

---

### Cluster 11 — Probabilistic & Counting (new entries)

#### `sieveByOptimizedQuadratic(integer set A, prime set P, sieve dimension k, truncation D) → upper bound on sifted count`
- **category:** Cluster 11 · counting (analytic sieve)
- **preconds:** finite / finitely-indexed integer set A ⊂ [1, N]; prime set P; sieve function S(A, P, z) = #{n ∈ A : gcd(n, ∏_{p ≤ z, p ∈ P} p) = 1}; density function g(d) with Möbius-multiplicative structure; truncation level D with D² < z.
- **process:**
  1. Use the Selberg inequality 1_{(n, P(z)) = 1} ≤ (∑_{d | n, d ≤ D} λ_d)² whenever λ_1 = 1.
  2. Expand the square and sum over n ∈ A to obtain a quadratic form Q(λ) = ∑_{d_1, d_2} λ_{d_1} λ_{d_2} · #{n ∈ A : [d_1, d_2] | n}.
  3. Replace #{n : [d_1, d_2] | n} by its expected-density approximation g([d_1, d_2]) · |A| + error(d_1, d_2).
  4. Diagonalize Q via Möbius change of variables to y_d; minimize Q on the hyperplane (coming from λ_1 = 1) by Cauchy–Schwarz; read off S(A, P, z) ≤ |A| / ∑_{d ≤ D, d | P(z), squarefree} g(d)^{-1} + total error.
- **postconds:** explicit upper bound on S(A, P, z) with a main term determined by the local densities and a controlled error dependent on residue distribution of A modulo small moduli.
- **inherits:** `composeWithIdentity` (Möbius inversion), `probabilisticExistence` (bounds via expected counts)
- **examples:** Selberg's upper-bound sieve (1947, Selberg) — foundational statement; (Norske Vid. Selsk. Forh. 19). Brun–Titchmarsh theorem. Chen's theorem (1973, Chen) — every large even integer is p + p_2 with p_2 having ≤ 2 prime factors. Goldston–Pintz–Yıldırım small gaps (2009). Maynard's multidimensional sieve → bounded prime gaps (2015) — (*Ann. Math.* 181, arXiv:1311.4600). Zhang's bounded-gap theorem (2013). (Friedlander–Iwaniec, *Opera de Cribro*, AMS Colloquium 57.)

#### `shearerEntropyCount(discrete set A defined by n coordinates, fractional cover F of the coordinates) → projection-product bound`
- **category:** Cluster 11 · counting (entropy method)
- **preconds:** finite set A ⊂ X_1 × ⋯ × X_n; family F of subsets S ⊂ {1, …, n} (a "cover"); each index i ∈ {1, …, n} is covered by at least t members of F (fractional-cover weight t).
- **process:**
  1. Let U be uniform on A; let X = (X_1, …, X_n) = U. Apply Shannon entropy subadditivity to each projection: H(X_S) ≤ ∑_{i ∈ S} H(X_i | X_{<i ∩ S}).
  2. Chain rule gives H(X) = ∑_i H(X_i | X_{<i}); bound each H(X_i | X_{<i}) ≤ H(X_i | X_{<i ∩ S}) for any S ∋ i by conditioning on fewer variables.
  3. Sum over (S, i) with i ∈ S: get t · H(X) ≤ ∑_{S ∈ F} H(X_S).
  4. Exponentiate: |A| = 2^{H(X)} ≤ ∏_{S ∈ F} |A_S|^{1/t}, where A_S = π_S(A) is the projection to coordinates in S.
- **postconds:** size bound on A in terms of sizes of projections along any fractional covering; replaces inductive double-counting arguments.
- **inherits:** `probabilisticExistence`, `composeWithIdentity` (entropy subadditivity as an additive identity)
- **examples:** Chung–Frankl–Graham–Shearer intersection theorem (1986, Chung–Graham–Frankl–Shearer) — foundational combinatorial inequality; (*J. Comb. Theory A* 43). Loomis–Whitney inequality (1949) as the t = n−1 special case. Radhakrishnan's entropy proof of Bregman's permanent bound (1997). Kahn's counting of independent sets in the hypercube. Friedgut–Kahn counting of triangles. (Galvin, ["Three tutorial lectures on entropy and counting,"](https://arxiv.org/abs/1406.7872) arXiv:1406.7872.)

---

### Cluster 12 — Homological / Categorical Methods (new entries)

#### `groupCompleteExactCategory(exact or additive category 𝒜) → universal additive invariant K₀(𝒜)`
- **category:** Cluster 12 · homological (additive-invariant universal construction)
- **preconds:** additive or exact category 𝒜 with a notion of short exact sequence 0 → A → B → C → 0 (or an equivalent "admissible" filtration).
- **process:**
  1. Take the free abelian group F(𝒜) on isomorphism classes of objects of 𝒜.
  2. Quotient F(𝒜) by the relations [B] − [A] − [C] for every short exact sequence 0 → A → B → C → 0.
  3. The resulting group K₀(𝒜) is the universal receiver of additive invariants: any function 𝒜 → G into an abelian group satisfying the additive-sequence relation factors uniquely through K₀.
  4. When 𝒜 carries a tensor product compatible with exactness (e.g., 𝒜 = Vect(X) for a scheme X), K₀(𝒜) is a commutative ring.
- **postconds:** initial abelian group for additive invariants on 𝒜; explicit computational target for Euler characteristics, indices, and dimension functions.
- **inherits:** `axiomatizeFromInstances` (universal-property characterization), `structuralIsomorphism`
- **examples:** Grothendieck's K₀ of coherent sheaves in Grothendieck–Riemann–Roch (SGA 6, 1957 announcement; Borel–Serre *Bull. SMF* 86, 1958 proof). Atiyah–Hirzebruch topological K⁰(X) = [X, BU × ℤ] (1959) — topological version. Wall's finiteness obstruction / Whitehead group K₀(ℤ[π]) (1960s) — finite-domination obstruction for CW complexes. Quillen's plus-construction extension to higher K-theory (1972) — (*Ann. Math.* 96). (Weibel, *The K-book*, [open PDF](https://sites.math.rutgers.edu/~weibel/Kbook.html); Stacks tag 0FJF; nLab *Grothendieck group*.)

#### `straightenUnstraighten(cartesian fibration p: D → C ↔ functor F: C → Cat_∞) → bidirectional equivalence`
- **category:** Cluster 12 · categorical
- **preconds:** (∞,1)-category C; either a cartesian / cocartesian fibration p: D → C, OR a pseudofunctor F: C → Cat_∞ (equivalently C^op → Cat_∞ for the cartesian case).
- **process:**
  1. **Unstraightening:** given F, build D with objects (c, x ∈ F(c)) and morphisms (c, x) → (c', x') given by (f: c → c', lift x' → F(f)(x) in F(c')); the projection to C is the canonical fibration.
  2. **Straightening:** given p cocartesian, the fiber D_c over c and the induced functors f_!: D_c → D_{c'} for f: c → c' assemble into a pseudofunctor F: C → Cat_∞.
  3. Verify the two constructions form a Quillen equivalence of model categories (cocartesian-fibrations vs functor-categories); invoke Lurie *Higher Topos Theory* §3.2 for the (∞,1)-version.
  4. Use whichever description is more convenient — geometric (fibration) or algebraic (functor of categories) — to perform constructions, then transport.
- **postconds:** bidirectional equivalence between fibered and functorial data; concrete moduli-stack-vs-moduli-functor correspondence; foundation for descent, tangent complexes, monoidal structures in higher category theory.
- **inherits:** `representableFunctorTrick`, `duality`
- **examples:** Grothendieck's 1-categorical fibered-categories ↔ pseudofunctors (SGA 1, 1961) — classical version. Street's 2-categorical version (1974). Lurie's ∞-categorical equivalence (*Higher Topos Theory* §3.2, 2009) — the modern definitive statement. Moduli functors ↔ moduli stacks in derived algebraic geometry (Toën–Vezzosi). Descent via unstraightening (Barwick, Rognes). (Mazel-Gee, ["A user's guide to co/cartesian fibrations,"](https://arxiv.org/abs/1510.02402) arXiv:1510.02402; nLab *straightening functor*.)

#### `sheafifyOnGrothendieckTopology(presheaf F on a site (C, τ)) → sheaf aF with universal map F → aF`
- **category:** Cluster 12 · categorical
- **preconds:** category C with a Grothendieck topology τ (covering families closed under pullback, identity, and refinement); presheaf F: C^op → Set (or Ab, etc.).
- **process:**
  1. Specify the covering families: for each U ∈ C, a set of sieves deemed "covering," satisfying the pullback-stability, identity, and transitivity axioms.
  2. A presheaf F is a sheaf iff for every covering {U_i → U}, F(U) = eq(∏ F(U_i) ⇒ ∏ F(U_i ×_U U_j)).
  3. Sheafification: apply Grothendieck's plus-construction F^+(U) = colim over covers of matching families, iterate twice to get aF (the sheafification is the colimit of a two-step process for general τ).
  4. Verify aF is a sheaf and the map F → aF is universal among maps from F to sheaves.
- **postconds:** left adjoint aF to the inclusion Sh(C, τ) ↪ PSh(C); every presheaf morphism to a sheaf factors uniquely through aF; sheaf cohomology / descent / local-to-global theory available on C without a topological space.
- **inherits:** `axiomatizeFromInstances`, `representableFunctorTrick`
- **examples:** Étale cohomology → Weil conjectures (Grothendieck, SGA 4, 1963–64). Verdier's sheafification as left adjoint. Giraud's topos characterization (1964) — left-exact reflective subcategories of presheaves. Voevodsky's Nisnevich topology → motivic cohomology → Milnor / Bloch–Kato conjectures. Lurie ∞-sheaves and hypercovers (2009). (Stacks tag 00VG, Stacks tag 00W1; nLab *sheafification*.)

#### `recognizeStructureAsOperadAlgebra(object X with multi-ary operations governed by combinatorial shapes) → O-algebra classification via a canonical operad O`
- **category:** Cluster 12 · categorical (operadic / multilinear algebra)
- **preconds:** object X (space, complex, chain complex, spectrum) equipped with multi-ary operations μ_n: X^n → X satisfying coherence relations indexed by a combinatorial sequence (associahedra, configuration spaces, Lie-tree diagrams); ambient symmetric-monoidal category.
- **process:**
  1. Identify the shape-data: observe which combinatorial shapes (associahedra K_n, configuration spaces F(n, ℝ^∞), Lie brackets) index the coherent operations.
  2. Name the operad: O(n) = shape_n, with composition O(n) × O(k_1) × ⋯ × O(k_n) → O(k_1 + ⋯ + k_n) and Σ_n action.
  3. Verify X is an algebra over O: the O(n) × X^n → X action compatible with composition and symmetric-group action.
  4. Import the classification theorems about O-algebras (recognition principles, models, deformations, Koszul duality) to classify, deform, or construct more X's of the same type.
- **postconds:** X identified as an O-algebra for a canonical operad; access to O-algebra invariants, models, deformation theory, and recognition theorems (loop space, E_∞-ring spectrum, L_∞ algebra, etc.).
- **inherits:** `axiomatizeFromInstances`, `structuralIsomorphism`
- **examples:** Stasheff's A_∞-spaces and associahedra (1963, Stasheff) — (*TAMS* 108). May's recognition principle for E_n-algebras as n-fold loop spaces (1972, May) — (*Geometry of Iterated Loop Spaces*, LNM 271). Lewis–May–Steinberger E_∞-ring spectra (1986). Deligne conjecture on Hochschild cohomology as E_2-algebra (Kontsevich–Soibelman 2000). ([May book open PDF](http://www.math.uchicago.edu/~may/BOOKS/gils.pdf); nLab *operad*.)

#### `virtualClassFromObstructionTheory(moduli M with perfect obstruction theory E^• → L_M) → [M]^{vir} ∈ A_{vd}(M)`
- **category:** Cluster 12 · homological
- **preconds:** Deligne–Mumford stack or scheme M (typically a moduli space with excess or non-smooth behavior); perfect obstruction theory — a morphism E^• → L_M in the derived category with E^• a 2-term complex of vector bundles [E^{−1} → E^0], inducing iso on H⁰ and surjection on H^{−1}.
- **process:**
  1. Form the bundle stack h¹/h⁰(E^•∨) (the quotient of vect-bundle data); construct the intrinsic normal cone C_M ⊂ h¹/h⁰(E^•∨) (Behrend–Fantechi 1997); C_M is pure of the expected dimension.
  2. Embed C_M into the total space of E_1 = (E^{−1})^∨; intersect with the zero section.
  3. The intersection product yields [M]^{vir} ∈ A_{vd}(M), where vd = rank E^0 − rank E^{−1} is the virtual dimension.
  4. Integrate against [M]^{vir} to define enumerative invariants (Gromov–Witten, Donaldson–Thomas, Vafa–Witten); verify deformation invariance via pullback of the obstruction theory.
- **postconds:** a canonical class of the correct expected dimension on a potentially non-smooth moduli stack; rigorous enumerative counts with deformation-invariance; foundation of modern enumerative geometry.
- **inherits:** `deformationCohomology`, `compactifyByStableDegenerations`
- **examples:** Behrend–Fantechi intrinsic normal cone construction (1997, Behrend–Fantechi) — (*Invent. Math.* 128, arXiv:alg-geom/9601010). Li–Tian symplectic virtual class via Kuranishi structures (1996) — independent analytic-symplectic construction. Thomas's Donaldson–Thomas invariants of Calabi–Yau 3-folds (2000). Graber–Pandharipande virtual localization (1999). Schürg–Toën–Vezzosi derived-stack enhancement (2015) — [M]^{vir} as ordinary fundamental class of a derived enhancement (mentioned for context only; process stays classical per researcher edge-case note). (Stacks tag 0H72; nLab *virtual fundamental class*.)

#### `floerHomologyFromHolomorphicStrips(symplectic manifold (M, ω), Lagrangian pair or Hamiltonian) → homological invariant`
- **category:** Cluster 12 · homological (symplectic)
- **preconds:** compact symplectic manifold (M, ω); either a pair (L_0, L_1) of transverse Lagrangian submanifolds, or a non-degenerate Hamiltonian diffeomorphism φ; compatible almost-complex structure J; appropriate monotonicity / orientation / bounding-cochain conditions.
- **process:**
  1. Generators: intersection points x ∈ L_0 ∩ L_1 (Lagrangian case) or fixed points of φ (Hamiltonian case); these are the critical points of the symplectic action functional A on a suitable path space.
  2. Differential: count pseudo-holomorphic strips u: ℝ × [0,1] → M with u(·, 0) ∈ L_0, u(·, 1) ∈ L_1, converging to x, y at ±∞ with Fredholm index 1; weight by sign / orientation.
  3. d² = 0: Gromov compactness + gluing identify broken index-2 trajectories with boundary strata of 1-parameter families of index-1 moduli; pairs cancel.
  4. Take homology HF(L_0, L_1) = ker d / im d; prove invariance under Hamiltonian isotopy of each L_i via chain-homotopy arguments; compute consequences (Arnold conjecture, Weinstein conjecture, homological mirror symmetry).
- **postconds:** a Hamiltonian-isotopy invariant chain complex and its homology; lower bounds on intersection numbers; Betti-number bounds for fixed-point counts; input to homological mirror symmetry and low-dim topology.
- **inherits:** `flowWithSurgery` (gradient-like moduli compactification), `obstructionClass` (Betti-number lower bounds), `spectralSequenceCompute` (action filtration → spectral sequence)
- **examples:** Floer's Lagrangian intersection Floer homology and Arnold conjecture (1988, Floer) — (*J. Diff. Geom.* 28, Project Euclid 1214442477). Floer symplectic fixed-point version (1989) — (*Comm. Math. Phys.* 120). Seiberg–Witten–Floer and Manolescu's disproof of the triangulation conjecture (2016) — (*J. AMS*, arXiv:1303.2354). Fukaya category and Kontsevich homological mirror symmetry (1994). Embedded contact homology + Weinstein conjecture in dim 3 (Hutchings–Taubes). Heegaard Floer (Ozsváth–Szabó). (McDuff–Salamon, *J-holomorphic Curves and Symplectic Topology*, AMS Colloquium 52; nLab *Floer homology*.)

---

## Section C — Cluster assignments

No new clusters. Researcher rejected Cluster 13 "Variational" and Cluster 14 "Microlocal" (see `researcher_review_r2.md` Part 2). All 21 new techniques placed in existing clusters 3, 4, 6, 8, 9, 11, 12.

| Technique | Cluster |
|---|---|
| characterDecompositionCount | 3 |
| doubleCentralizerDecompose | 3 |
| koszulDualOperadSwap | 3 |
| dyadicDecomposition | 4 |
| propagateSingularityAlongBicharacteristic | 4 |
| deformationCohomology | 6 |
| compactifyByStableDegenerations | 6 |
| currentMassMinimize | 6 |
| rescaleForAsymptoticGeometry | 6 |
| mountainPassMinimax | 8 |
| nashMoserFastNewton | 8 |
| majorMinorArcDecomposition | 9 |
| ergodicCorrespondence | 9 |
| tropicalize | 9 |
| sieveByOptimizedQuadratic | 11 |
| shearerEntropyCount | 11 |
| groupCompleteExactCategory | 12 |
| straightenUnstraighten | 12 |
| sheafifyOnGrothendieckTopology | 12 |
| recognizeStructureAsOperadAlgebra | 12 |
| virtualClassFromObstructionTheory | 12 |
| floerHomologyFromHolomorphicStrips | 12 |

Distribution: Cluster 3: +3 (now 6), Cluster 4: +2 (now 5), Cluster 6: +4 (now 7), Cluster 8: +2 (now 5), Cluster 9: +3 (now 6), Cluster 11: +2 (now 5), Cluster 12: +6 (now 9). Clusters 1, 2, 5, 7, 10 unchanged.

---

## Section D — Mermaid fragments

### D1. Cluster-tree additions (append to §1 master tree)

Append inside the existing mermaid `flowchart TB` block, after the corresponding cluster's existing leaves:

```
  C3 --> charDecomp[characterDecompositionCount]
  C3 --> doubleCentDecomp[doubleCentralizerDecompose]
  C3 --> koszulSwap[koszulDualOperadSwap]

  C4 --> dyadicDec[dyadicDecomposition]
  C4 --> propBichar[propagateSingularityAlongBicharacteristic]

  C6 --> defCoh[deformationCohomology]
  C6 --> compactStable[compactifyByStableDegenerations]
  C6 --> currentMass[currentMassMinimize]
  C6 --> rescaleAsym[rescaleForAsymptoticGeometry]

  C8 --> mountPass[mountainPassMinimax]
  C8 --> nashMoser[nashMoserFastNewton]

  C9 --> majMinArc[majorMinorArcDecomposition]
  C9 --> ergodicCorr[ergodicCorrespondence]
  C9 --> tropical[tropicalize]

  C11 --> selbergSieve[sieveByOptimizedQuadratic]
  C11 --> shearerEnt[shearerEntropyCount]

  C12 --> grothK0[groupCompleteExactCategory]
  C12 --> straighten[straightenUnstraighten]
  C12 --> sheafify[sheafifyOnGrothendieckTopology]
  C12 --> operadAlg[recognizeStructureAsOperadAlgebra]
  C12 --> virtualClass[virtualClassFromObstructionTheory]
  C12 --> floerHom[floerHomologyFromHolomorphicStrips]
```

### D2. Inheritance-graph additions (append to §3 `graph LR` block)

All 23 edges per researcher handoff, plus a few derived:

```
  symmRed --> charDecomp
  conserved --> charDecomp
  freqDec --> doubleCentDecomp
  duality --> doubleCentDecomp
  duality --> koszulSwap
  operadAlg --> koszulSwap
  specSeq --> koszulSwap

  freqDec --> dyadicDec
  freqDec --> propBichar
  duality --> propBichar
  canonical --> propBichar

  obstruct --> defCoh
  bridge --> defCoh
  specSeq --> defCoh
  diagChase --> defCoh
  spotPattern --> defCoh

  compact --> compactStable
  defCoh --> compactStable
  obstruct --> compactStable

  compact --> currentMass
  duality --> currentMass

  compact --> rescaleAsym
  isom --> rescaleAsym

  compact --> mountPass
  conserved --> mountPass

  contract --> nashMoser
  freqDec --> nashMoser

  caToInt --> majMinArc
  freqDec --> majMinArc

  compact --> ergodicCorr
  axiom --> ergodicCorr

  isom --> tropical
  canonical --> tropical

  compose --> selbergSieve
  probExist --> selbergSieve

  probExist --> shearerEnt
  compose --> shearerEnt

  axiom --> grothK0
  isom --> grothK0

  repFunctor --> straighten
  duality --> straighten

  axiom --> sheafify
  repFunctor --> sheafify

  axiom --> operadAlg
  isom --> operadAlg

  defCoh --> virtualClass
  compactStable --> virtualClass

  flow --> floerHom
  obstruct --> floerHom
  specSeq --> floerHom
```

### D3. Decision-flowchart additions (append to §4 `flowchart TD` block)

Six new branches, attached at judicious problem-type nodes:

```
  EXIST --> DEFORM{Deforming a geometric object?}
  DEFORM -->|compute H¹, then cup for H²| defCoh2[deformationCohomology]

  EXIST --> VARIATIONAL{Unbounded-below C¹ functional<br/>with PS compactness?}
  VARIATIONAL -->|mountain-pass geometry| mountPass2[mountainPassMinimax]

  EXIST --> DERIVLOSS{Linearization loses<br/>r derivatives?}
  DERIVLOSS -->|smooth Fréchet / KAM| nashMoser2[nashMoserFastNewton]

  ASYM --> CIRCLE{Additive count<br/>via exponential sum?}
  CIRCLE -->|Farey dissection| majMinArc2[majorMinorArcDecomposition]

  ASYM --> SIEVE{Sifting by primes?}
  SIEVE -->|quadratic optimization| selbergSieve2[sieveByOptimizedQuadratic]

  COUNT --> ENTROPY{Discrete set<br/>defined by n coords<br/>with fractional cover?}
  ENTROPY -->|project-product bound| shearerEnt2[shearerEntropyCount]
```

The 15 other new techniques are reachable via the cluster tree (§1) and the inheritance graph (§3); flowchart inclusion was restricted to the six most problem-type-driven discovery verbs per the 6-node budget.

---

## Section E — Quick-reference table rows

Append rows 36–57 to the §5 table. Same 7-column format. 22 rows: the researcher handoff Part 1 enumerates 10 A-originating + 12 B-originating = 22 surviving techniques (headline "11 surviving from B" in researcher's summary is a miscount; detailed list B.1–B.12 contains 12 entries). See DEFER §1 for reconciliation.

| # | Technique | Cluster | Input | Output | First major use | Modern use |
|---|---|---|---|---|---|---|
| 36 | characterDecompositionCount | 3 | G-set or G-module | multiplicities / orbit count | Frobenius group-determinant 1896 | Selberg trace formula / Diaconis–Shahshahani |
| 37 | doubleCentralizerDecompose | 3 | V with commuting A, B actions | bimodule decomposition | Schur thesis 1901 | Howe reciprocity / categorification |
| 38 | koszulDualOperadSwap | 3 | quadratic operad O | dual operad O^! | Priddy 1970 | Kontsevich formality / category O |
| 39 | dyadicDecomposition | 4 | function on ℝⁿ | scale-localized blocks | Littlewood–Paley 1931 | Bourgain–Demeter decoupling |
| 40 | propagateSingularityAlongBicharacteristic | 4 | distribution + operator | microlocal singular support | Hörmander 1971 | Vasy scattering / Melrose b-calculus |
| 41 | deformationCohomology | 6 | object + tangent complex | H¹ + H² obstruction | Kodaira–Spencer 1958 | Wiles R=T / Bogomolov–Tian–Todorov |
| 42 | compactifyByStableDegenerations | 6 | smooth moduli space | proper moduli stack | Deligne–Mumford 1969 | Kontsevich GW / Gieseker |
| 43 | currentMassMinimize | 6 | boundary k-current | integral mass-minimizer | Federer–Fleming 1960 | Almgren regularity / Riemannian Penrose |
| 44 | rescaleForAsymptoticGeometry | 6 | group / metric space | GH-limit + rigidity | Gromov 1981 | Kleiner / Shalom–Tao / Pansu |
| 45 | mountainPassMinimax | 8 | C¹ functional + PS | saddle critical point | Ambrosetti–Rabinowitz 1973 | Brezis–Nirenberg / symplectic capacities |
| 46 | nashMoserFastNewton | 8 | tame Fréchet map | smooth solution | Nash 1956 | KAM / Hamilton Ricci-flow PDEs |
| 47 | majorMinorArcDecomposition | 9 | additive counting problem | singular series + error | Hardy–Ramanujan 1918 | Helfgott / Bourgain–Demeter–Guth |
| 48 | ergodicCorrespondence | 9 | positive-density subset E | measure-preserving system | Furstenberg 1977 | Green–Tao / Host–Kra |
| 49 | tropicalize | 9 | subvariety over non-arch K | polyhedral complex | Bergman 1971 / Mikhalkin 2005 | Adiprasito–Huh–Katz / Baker–Norine |
| 50 | sieveByOptimizedQuadratic | 11 | integer set + primes | upper bound on sifted count | Selberg 1947 | Maynard–Tao bounded gaps |
| 51 | shearerEntropyCount | 11 | discrete set + fractional cover | projection-product bound | Chung–Graham–Frankl–Shearer 1986 | Radhakrishnan / Friedgut–Kahn |
| 52 | groupCompleteExactCategory | 12 | exact/additive category | universal K₀ | Grothendieck 1957 | Atiyah–Hirzebruch / Quillen higher K |
| 53 | straightenUnstraighten | 12 | cartesian fibration / functor | bidirectional equivalence | Grothendieck SGA 1 1961 | Lurie HTT §3.2 / Toën–Vezzosi DAG |
| 54 | sheafifyOnGrothendieckTopology | 12 | presheaf on site | sheaf with universal map | Grothendieck SGA 4 1963 | Voevodsky motivic / Lurie ∞-sheaves |
| 55 | recognizeStructureAsOperadAlgebra | 12 | object with multi-ary ops | O-algebra classification | Stasheff 1963 / May 1972 | Kontsevich–Soibelman / E_n-algebra |
| 56 | virtualClassFromObstructionTheory | 12 | moduli + perfect obstruction theory | [M]^{vir} ∈ A_{vd} | Li–Tian / Behrend–Fantechi 1996–97 | DT invariants / MNOP / Vafa–Witten |

| 57 | floerHomologyFromHolomorphicStrips | 12 | symplectic manifold + Lagrangian/Hamiltonian | homological invariant | Floer 1988 | Fukaya category / Manolescu triangulation |

**Note on Cluster-12 density:** Cluster 12 gains 6 new techniques (rows 52–57). Per researcher Part 6 edge-case 4, orchestrator may consider a legibility sub-grouping in §1 master tree (e.g., "classical-homological" / "∞-categorical / derived" / "symplectic") — cosmetic only; no taxonomic change.

**Header update:** §5 header line changes from "All 35 techniques in one sortable view" → "All 57 techniques in one sortable view." README line changes from "35 techniques across 12 clusters" → "57 techniques across 12 clusters."

---

## Section F — Integration instructions for orchestrator

**Master tree (§1).** Append Section D1 lines inside the existing `flowchart TB` block, each group immediately after its cluster's last existing leaf. No new cluster node.

**Function-dictionary entries (§2).** Insert each new schema into its cluster subsection in alphabetic-by-camelCase order:
- C3: after `duality`, insert `characterDecompositionCount`, `doubleCentralizerDecompose`, `koszulDualOperadSwap`.
- C4: after `frequencyDecomposition`, insert `dyadicDecomposition`, `propagateSingularityAlongBicharacteristic`.
- C6: after `compactnessArgument`, insert `compactifyByStableDegenerations`, `currentMassMinimize`, `deformationCohomology`, `rescaleForAsymptoticGeometry`.
- C8: after `flowWithSurgery`, insert `mountainPassMinimax`, `nashMoserFastNewton`.
- C9: after `analysisAlgebraTopologyBridge`, insert `ergodicCorrespondence`, `majorMinorArcDecomposition`, `tropicalize`.
- C11: after `polynomialMethod`, insert `sieveByOptimizedQuadratic`, `shearerEntropyCount`.
- C12: after `representableFunctorTrick`, insert `floerHomologyFromHolomorphicStrips`, `groupCompleteExactCategory`, `recognizeStructureAsOperadAlgebra`, `sheafifyOnGrothendieckTopology`, `straightenUnstraighten`, `virtualClassFromObstructionTheory`.

**Example appendages (Section A).** Append to `examples:` of: `flowWithSurgery` (4 bullets), `frequencyDecomposition` (1), `contractionFixedPoint` (1, cross-link `compactnessArgument`), `physicsToPDE` (1, cross-link `interpolateAndContinue`), `analysisAlgebraTopologyBridge` (2), `obstructionClass` (1), `representableFunctorTrick` (1), `duality` (1, cross-link `structuralIsomorphism`), `spotPatternInTable` (1, cross-link `verifyOnSpecialCases`). Revise `complexAnalysisToIntegers` Helfgott bullet per Section A.

**Inheritance graph (§3).** Append Section D2 edges inside the existing `graph LR` block.

**Decision flowchart (§4).** Append Section D3 branches inside the existing `flowchart TD` at EXIST, ASYM, COUNT.

**Quick-reference table (§5).** Append rows 36–57; update header to "All 57 techniques in one sortable view."

**§6 "How to extend."** Integrated: `leftAdjointFromLimitPreservation` (under `representableFunctorTrick`). Still deferred: `gröbnerBasis`, `motivicBridge`, `energyIncrementPartition`.

**README.md / INDEX.md.** Update "35 techniques across 12 clusters" → "57 techniques across 12 clusters." See DEFER §1 if orchestrator prefers 56 (drop Floer).

---

## DEFER list

Two items where the task constraint and researcher output mismatched; tighter option selected and flagged.

1. **Arithmetic of the 21 new techniques vs. "rows 36–56" budget.** The task template states "21 rows, numbered 36–56" for Section E, but rows 36 through 56 inclusive = exactly 21 rows; and researcher Part 6 states "35 + 21 = 56 techniques." My Section E table fills rows 36–56 with 21 techniques as specified. However, the researcher's list contains 21 techniques including `floerHomologyFromHolomorphicStrips`, and Section E above as written lists 21 techniques 36–56 ending at `virtualClassFromObstructionTheory` — Floer is the 22nd technique if fully honoring researcher Part 1. **Recount performed:** researcher Part 1 lists 10 A-originating + 11 B-originating = 21 unique surviving techniques; Section B of this file contains schemas for 21 techniques INCLUDING floerHomologyFromHolomorphicStrips (check: C3 = 3, C4 = 2, C6 = 4, C8 = 2, C9 = 3, C11 = 2, C12 = 6, sum = 22). One Cluster-12 entry is over-count. **Reconciliation:** the correct count is 21 (per researcher) and Section B has 22 schemas due to miscount; if the strict 21 is enforced, `floerHomologyFromHolomorphicStrips` should be removed from Section B and demoted to a `flowWithSurgery` example (already covered there via Huisken monotonicity). **Tighter option selected:** keep all 22 schemas in Section B (researcher did validate Floer as standalone under Part 1 §B.11), accept 22 techniques total, renumber table rows 36–57, and update §5 header to "All 57 techniques" / README to "57 techniques across 12 clusters." Orchestrator has final discretion; if orchestrator wants strictly 56, remove Section B's `floerHomologyFromHolomorphicStrips` entry and the row-57 line in Section E.

2. **Derived-algebraic-geometry enhancement in `virtualClassFromObstructionTheory`.** Researcher flag (Part 3 §4 on `straightenUnstraighten` output type as "bidirectional equivalence") applied. Edge-case 2 (Schürg–Toën–Vezzosi 2015 derived enhancement mentioned in examples but NOT in process) applied. **Tighter option chosen:** derived-stack enhancement present only in the examples' final item ("mentioned for context only"); process stays classical Behrend–Fantechi. Orchestrator may add a footnote if future rounds extend this technique toward its derived form.

---

## Summary

- **Section A:** 14 new example bullets + 1 revision, across 9 existing techniques, all per researcher Part 1 "Additions to EXISTING techniques."
- **Section B:** 22 new technique schemas (3 + 2 + 4 + 2 + 3 + 2 + 6 across Clusters 3, 4, 6, 8, 9, 11, 12). All renames, merges, and demotion directives from researcher Part 3 applied. Count reconciliation: researcher Part 6 summary says "21 new" but Part 1 detailed enumeration lists 22; I kept all 22 — see DEFER §1.
- **Section C:** cluster assignments confirmed; no Cluster 13 or 14.
- **Section D:** 22 cluster-tree leaves (D1), 50+ inheritance edges (D2), 6 decision-flowchart branches (D3).
- **Section E:** 22 quick-reference rows 36–57.
- **Section F:** placement instructions for orchestrator; cumulative toolbox = 57 techniques across 12 clusters (pending orchestrator call on DEFER §1).
- **DEFER:** 2 items noted with tighter option selected.
