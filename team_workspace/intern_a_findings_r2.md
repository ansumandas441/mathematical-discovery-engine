# Intern A — Round 2 Findings (Algebraic & Categorical Gaps)

## Gap areas covered

1. Representation theory as a discovery technique — 3 entries
2. K-theory as a computational tool — 3 entries
3. Deformation theory as a standalone method — 2 entries
4. Higher category / ∞-category techniques — 2 entries
5. Topos theory / internal logic — 2 entries
6. Operad theory — 2 entries
7. Moduli-space methods — 2 entries

## Count

**16 entries** total across the seven gap areas. All 16 correspond to proposed NEW techniques (with the exception of entry 1 "Character-theoretic counting," which doubles as a new technique and also supplies new examples for the existing `symmetryReduction` and `conservedQuantity`).

## Table of contents

1. [Character-theoretic counting / Burnside & Frobenius](#1-character-theoretic-counting-1896-frobenius--burnside)
2. [Frobenius reciprocity / induction–restriction adjunction](#2-frobenius-reciprocity-induction-restriction-adjunction-1898-frobenius)
3. [Peter–Weyl & Schur–Weyl duality as a discovery engine](#3-peterweyl-expansion-1927-peter-weyl--schurweyl-duality-1927-schur-weyl)
4. [Grothendieck group / K₀ construction](#4-grothendieck-group-k-construction-1957-grothendieck)
5. [Bott periodicity as a structural shortcut](#5-bott-periodicity-1959-bott)
6. [K-theoretic pushforward and the index theorem](#6-k-theoretic-pushforward-1963-atiyah-singer)
7. [Kodaira–Spencer deformation map](#7-kodairaspencer-deformation-map-1958-kodairaspencer)
8. [Obstruction theory in Ext² (deformation obstructions)](#8-obstruction-in-ext-1968-schlessinger--1973-illusie)
9. [Coherent-replacement-of-equality in ∞-categories](#9-coherent-replacement-of-equality-19732009-boardmanvogt--lurie)
10. [Straightening–unstraightening / Grothendieck construction](#10-straighteningunstraightening-2009-lurie)
11. [Sheafification via Grothendieck topology](#11-sheafification-via-grothendieck-topology-1962-grothendieck--verdier)
12. [Geometric morphism as logical translation](#12-geometric-morphism-1970-lawverestreet-lawveretierney)
13. [Algebra over an operad / recognition principle](#13-algebra-over-an-operad-1972-may--boardmanvogt-recognition)
14. [Koszul duality of operads](#14-koszul-duality-of-operads-1994-ginzburgkapranov)
15. [Deligne–Mumford compactification of moduli](#15-delignemumford-compactification-1969-delignemumford)
16. [Virtual fundamental class / moduli-count counting](#16-virtual-fundamental-class-1996-liantianbehrendfantechi)

---

### 1. Character-theoretic counting (1896, Frobenius; Burnside)

**Statement / description:** To count or classify objects with group symmetry, do *not* enumerate configurations — instead compute sums of characters χ(g) (traces of representations) and apply orthogonality. Burnside's lemma counts orbits as (1/|G|)∑|Fix(g)|; Frobenius's formula lets you compute the number of factorizations in a finite group purely in terms of character ratios.

**Discovery trigger:** Frobenius wanted to generalize Dedekind's *Gruppendeterminante* puzzle — factor the determinant of a group's multiplication table. He found the factor-degrees are exactly the irreducible character dimensions. Characters turned "why does this product decompose?" into a linear-algebra-on-traces question.

**Thought process / lineage:** Dedekind (1880s, letters) posed the group-determinant problem to Frobenius. Frobenius (1896) invented characters of non-abelian groups as solution. Burnside (1897 *Theory of Groups*) gave the orbit-counting lemma (later shown present in Cauchy and Frobenius, hence "Cauchy–Frobenius–Burnside lemma"). Schur (1905) simplified via the Schur orthogonality relations.

**Proof idea / process:**
1. Decompose the regular representation of G into irreducibles.
2. Traces of these irreducibles (characters) form an orthonormal basis of class functions under ⟨χ, ψ⟩ = (1/|G|)∑χ(g)ψ(g̅).
3. Any G-invariant counting problem has a character expansion; fixed-point / orbit / multiplicity formulas fall out as inner products.

**Impact:** Enabled the entire classification of finite simple groups (character tables were the main invariant), Frobenius's theorem on character kernels, the analytic theory of automorphic representations (Selberg trace formula = character integration on a locally symmetric space), Diaconis–Shahshahani random-walk mixing on groups via character bounds.

**Sources (≥1 non-Wikipedia):**
- MacTutor biography of Frobenius: https://mathshistory.st-andrews.ac.uk/Biographies/Frobenius/
- Curtis, *Pioneers of Representation Theory* (AMS History of Mathematics vol. 15), chap. 3, selection via AMS: https://bookstore.ams.org/hmath-15

**Technique tag:** NEW — `characterDecompositionCount(G-set or G-module, irreducible characters of G) → multiplicities / orbit count / factorization count` — extract numerical information from a G-action by projecting a class function onto the orthonormal character basis. (Also supplies additional examples for existing `symmetryReduction` and `conservedQuantity`, since characters are *the* canonical G-invariants.)

---

### 2. Frobenius reciprocity / induction-restriction adjunction (1898, Frobenius)

**Statement / description:** For H ≤ G, the functors Ind_H^G and Res_H^G between representation categories are adjoint: Hom_G(Ind_H^G W, V) ≅ Hom_H(W, Res_H^G V). So "building up" representations from a subgroup is dual to "cutting down" a G-rep to H.

**Discovery trigger:** Frobenius wanted to understand which irreducible characters of S_n arise from a given parabolic subgroup — how do representations of a subgroup "propagate" to the whole group and vice versa? The reciprocity is the statement that the two directions are adjoint (in modern language).

**Thought process / lineage:** Frobenius (1898) proved the character version χ^G(g) ↔ χ(h) summation identity. Mackey (1952) reformulated as the double-coset formula. The modern adjunction framing is due to the categorical reformulation in the 1960s (Mac Lane, Freyd). Branching rules for S_n ⊂ S_{n+1} (Young's rule) and for U(n) ⊂ U(n+1) (Weyl's branching rule) are direct applications.

**Proof idea / process:**
1. Define induced representation as ℂ[G] ⊗_{ℂ[H]} W (or equivalently functions f: G → W with f(hg) = h·f(g)).
2. A G-linear map Ind W → V restricts to an H-linear map W → V on the image of W ⊗ 1.
3. Conversely, any H-map W → V extends G-equivariantly by averaging over coset representatives.
4. Bijection ⇒ adjunction.

**Impact:** Harish-Chandra's entire theory of admissible representations of real reductive groups (parabolic induction as the *primary* construction); Langlands' automorphic induction; Mackey theory of irreducibles; modern use: if you want irreducibles of G, induce from all subgroups and decompose — the irreducible is "seen" by Frobenius reciprocity.

**Sources (≥1 non-Wikipedia):**
- nLab, "Frobenius reciprocity": https://ncatlab.org/nlab/show/Frobenius+reciprocity
- Serre, *Linear Representations of Finite Groups* (Springer GTM 42), §7.2, publisher page: https://link.springer.com/book/10.1007/978-1-4684-9458-7

**Technique tag:** NEW — `induceThenDecompose(representation W of H ≤ G) → G-representation with Frobenius-reciprocity multiplicity formula` — lift a known smaller-group rep to the larger group, then read off multiplicities of irreducibles via the adjunction. *Inherits: `representableFunctorTrick` (adjunction is the hom-set iso), `duality`.*

---

### 3. Peter–Weyl expansion (1927, Peter–Weyl) & Schur–Weyl duality (1927, Schur–Weyl)

**Statement / description:** Two complementary decompositions: (Peter–Weyl) L²(G) of a compact group G decomposes as the orthogonal direct sum ⊕ V_π ⊗ V_π* over irreducibles π — Fourier on non-abelian groups. (Schur–Weyl) The tensor-power space (ℂ^n)^⊗k carries commuting actions of GL(n) and S_k, and decomposes as ⊕_λ S^λ(ℂ^n) ⊗ V_λ indexed by partitions λ; the two actions are mutual commutants.

**Discovery trigger:** Weyl wanted the representation theory of a compact Lie group to look like Fourier analysis on the circle. Schur (earlier, in his thesis 1901) wanted to decompose polynomial invariants of matrix groups — discovering that the symmetric group and the general linear group commute on tensor space was the surprise.

**Thought process / lineage:** Schur's 1901 thesis (Berlin, under Frobenius) identified the GL(n)–S_k double centralizer. Peter & Weyl (1927, *Math. Ann.* 97) proved the L²(G) decomposition for compact G using integral operators. Weyl's 1939 book *The Classical Groups* packaged both as the "double centralizer" principle. Howe (1989) extended to dual pairs — the reciprocity between two centralizing group actions in a Fock space.

**Proof idea / process:**
1. Given two groups A, B commuting on vector space V, decompose V as a bimodule: V = ⊕ U_i ⊗ W_i.
2. The U_i are irreps of A, the W_i are irreps of B, and the labeling i gives a bijection between the irreps that *appear* in each summand.
3. Extract representation-theoretic info on one side from combinatorial info on the other.

**Impact:** Weyl's character formula and dimension formula (counts multiplicities via characters); Young tableaux combinatorics from Schur–Weyl (partitions λ index *both* S_k-irreps and GL(n)-polynomial irreps); Howe reciprocity unifying theta correspondences in automorphic forms; modern categorification (Khovanov–Lauda–Rouquier) and tensor-network renormalization in physics.

**Sources (≥1 non-Wikipedia):**
- nLab, "Peter-Weyl theorem": https://ncatlab.org/nlab/show/Peter-Weyl+theorem
- nLab, "Schur–Weyl duality": https://ncatlab.org/nlab/show/Schur-Weyl+duality
- Goodman & Wallach, *Symmetry, Representations, and Invariants* (Springer GTM 255), §4.2 Schur–Weyl, §C.2 Peter–Weyl: https://link.springer.com/book/10.1007/978-0-387-79852-3

**Technique tag:** NEW — `doubleCentralizerDecompose(vector space V with commuting actions of A and B) → bimodule decomposition ⊕ U_i ⊗ W_i` — when two groups (or algebras) commute on one space, each determines the other's irreducibles that appear. *Inherits: `frequencyDecomposition` (Peter–Weyl is Fourier on G), `duality`.*

---

### 4. Grothendieck group / K₀ construction (1957, Grothendieck)

**Statement / description:** Given an additive category (or exact category, or scheme X with vector bundles), form the free abelian group on isomorphism classes modulo the relations [A] + [C] = [B] for every exact sequence 0 → A → B → C → 0. The result K₀ is the universal "additive invariant" — every such invariant (rank, dimension, Euler characteristic, χ(X, F)) factors through K₀.

**Discovery trigger:** Grothendieck wanted a Riemann–Roch theorem for arbitrary projective morphisms, not just curves. The obstacle: Euler characteristic of a coherent sheaf is not multiplicative for a general morphism. Solution: work in a group where exact sequences become additive, so the Euler characteristic is forced to factor through the universal such group.

**Thought process / lineage:** Grothendieck–Riemann–Roch was announced in Bonn (1957), proved in SGA 6 and by Borel–Serre (1958, *Bull. SMF* 86). The topological version K^0(X) = [X, BU × ℤ] was introduced by Atiyah–Hirzebruch (1959). Quillen (1973) extended to higher K-theory via the plus-construction and Q-construction.

**Proof idea / process:**
1. Take the free abelian group on objects of the category.
2. Impose the relation [B] = [A] + [C] for each short exact sequence.
3. The universal property: any additive invariant to an abelian group factors uniquely through K₀.
4. For a scheme X, K₀(X) is generated by vector bundles modulo exact sequences, with tensor product making it a ring K⁰(X).

**Impact:** Grothendieck–Riemann–Roch (functoriality of χ through f_!: K(X) → K(Y)); Atiyah–Singer index theorem (analytic index factors through K⁰(TX)); topological K-theory of C*-algebras → Baum–Connes conjecture; K₀ of representations = representation ring R(G); algebraic K-theory K₀ of a ring = Whitehead group / Wall finiteness obstruction.

**Sources (≥1 non-Wikipedia):**
- Stacks Project, tag 0FJF "K-theory of coherent sheaves": https://stacks.math.columbia.edu/tag/0FJF
- Weibel, *The K-book: An Introduction to Algebraic K-theory*, chap. II (Grothendieck's K₀), open online: https://sites.math.rutgers.edu/~weibel/Kbook.html
- nLab, "Grothendieck group": https://ncatlab.org/nlab/show/Grothendieck+group

**Technique tag:** NEW — `groupCompleteExactCategory(exact or additive category A) → universalAdditiveInvariantK0(A)` — turn a category of objects with exact sequences into the initial abelian group receiving all additive invariants. *Inherits: `axiomatizeFromInstances` (universal property), `structuralIsomorphism`.*

---

### 5. Bott periodicity (1959, Bott)

**Statement / description:** The homotopy groups of the unitary group stabilize with period 2: π_k(U) = ℤ if k odd, 0 if k even. Equivalently, K⁰(X) ≅ K^{−2}(X). For the orthogonal group the period is 8. Discovery tool: whenever you face an infinite tower of obstructions, check if a Bott-like periodicity collapses it to finitely many cases.

**Discovery trigger:** Bott was computing the topology of symmetric spaces via Morse theory on the path space. He observed that Ω(U(n)) ~ ΩU has the homotopy type of U × ℤ after stabilization — an "accidental" periodicity that turned out to be the deepest property of K-theory.

**Thought process / lineage:** Bott (1956, 1959, *Ann. Math.* 70) proved it via Morse theory on Ω(SU). Atiyah–Bott (1964) gave an elementary K-theoretic proof using external products. Atiyah (1968) gave a purely topological proof. Wood (1966) and Karoubi (1978) extended it to Clifford algebra periodicity. The analogous Bott periodicity in symplectic K-theory, algebraic K-theory of finite fields (Quillen), and motivic cohomology (Voevodsky) all followed.

**Proof idea / process:**
1. Represent K⁰(X) by classifying maps X → BU × ℤ.
2. Using the tautological bundle on ℂP¹, construct a map β: K⁰(X) → K^{−2}(X) (Bott element multiplication).
3. Show β is an isomorphism either via Morse theory (original), external tensor product (Atiyah–Bott), or elementary topology using Fredholm operators (Atiyah).
4. Iterate to collapse ℤ-graded K-theory to ℤ/2-graded.

**Impact:** K-theory becomes a 2-periodic cohomology theory — dramatic computational simplification. The index theorem's K-theoretic formulation and its proofs. Clifford-algebra classification of symmetric spaces (Cartan → Milnor → Atiyah–Bott–Shapiro). Topological classification of insulators (Kitaev 2009) via the "tenfold way" — Bott periodicity in disguise is a physically measurable symmetry.

**Sources (≥1 non-Wikipedia):**
- nLab, "Bott periodicity": https://ncatlab.org/nlab/show/Bott+periodicity
- MacTutor biography of Bott: https://mathshistory.st-andrews.ac.uk/Biographies/Bott/
- Atiyah–Bott, "On the periodicity theorem for complex vector bundles," *Acta Math.* 112 (1964) — freely summarized in Atiyah's *K-theory* (Benjamin 1967), chap. 2.

**Technique tag:** NEW — `exploitPeriodicityInObstructionTower(sequence of obstructions K^n) → finite-case reduction via period p` — if the invariant group is periodic in its grading, infinitely many dimensions collapse to finitely many residues. *Inherits: `obstructionClass`, `structuralIsomorphism`.*

---

### 6. K-theoretic pushforward (1963, Atiyah–Singer)

**Statement / description:** A proper map f: X → Y of smooth manifolds (or schemes) defines a pushforward f_!: K(X) → K(Y), which for X pt is *the index*. The Atiyah–Singer theorem identifies analytic index (ker minus coker of an elliptic operator) with the K-theoretic pushforward of its symbol class in K(TX) — index computed by a topological integration.

**Discovery trigger:** Gelfand had conjectured that the index of an elliptic operator should be expressible in terms of topological data of its symbol. Riemann–Roch and Hirzebruch's signature theorem were existing instances. The universal answer required working in K-theory (not cohomology) to accommodate arbitrary elliptic symbols.

**Thought process / lineage:** Atiyah–Singer (1963, *Bull. AMS* 69) sketched; full proof (1968, *Ann. Math.* 87). Later Atiyah–Singer (1968–71) gave a K-theoretic proof via embedding X ↪ S^N and reducing to Bott periodicity. Connes (1982+) extended to non-commutative K-theoretic pushforward; Baum–Douglas (1982) gave a geometric K-theory K^geom. Grothendieck's algebraic GRR (1957) is the analog for coherent sheaves: χ(Y, f_* F) = f_!(ch(F)·Td(T_f)).

**Proof idea / process:**
1. Define the analytic index ind(D) = dim ker D − dim coker D for an elliptic operator D on X.
2. Embed X ↪ ℝ^N; use excision to push the symbol class forward from K(TX) to K(T ℝ^N) = K(pt) via Thom isomorphism.
3. The pushforward f_!: K(TX) → K(pt) = ℤ evaluates to the index; Bott periodicity / Thom isomorphism reduces the computation to a universal K-theoretic integral.
4. For schemes: f_![F] = ∑ (-1)^i [R^i f_* F]; GRR says ch ∘ f_! = f_* ∘ (ch · Td(T_f)).

**Impact:** Hirzebruch–Riemann–Roch (curves and surfaces), Gauss–Bonnet (χ as index of d+d*), signature theorem (sig as index of signature operator), Hirzebruch's proof of the Todd genus. In physics: anomaly cancellation (Alvarez-Gaumé–Witten), D-brane charges as K-theory classes (Minasian–Moore 1997), quantum Hall effect and topological phases. Algebraically, GRR underpins modern intersection theory on schemes.

**Sources (≥1 non-Wikipedia):**
- nLab, "Atiyah–Singer index theorem": https://ncatlab.org/nlab/show/index+theorem
- Stacks Project, tag 0FE6 "Gysin / pushforward in K-theory (Chow)": https://stacks.math.columbia.edu/tag/0FE6
- Atiyah, *K-Theory*, chap. 3 (open lecture notes); Atiyah–Singer original papers, *Ann. Math.* 87 (1968) 484–530.

**Technique tag:** NEW — `pushforwardAsIndex(elliptic symbol σ ∈ K(TX), proper f: X → pt) → integer invariant via K-theoretic integration` — treat a hard analytic index as a K-theoretic integration (Gysin / Thom / Bott) over a pullback cotangent bundle. *Inherits: `analysisAlgebraTopologyBridge`, `obstructionClass`, `exploitPeriodicityInObstructionTower`.*

---

### 7. Kodaira–Spencer deformation map (1958, Kodaira–Spencer)

**Statement / description:** Given a smooth family π: 𝒳 → B of complex manifolds with 𝒳_0 = X, the derivative at 0 is the Kodaira–Spencer map ρ: T_0 B → H^1(X, T_X), measuring the first-order change in complex structure. H^1(X, T_X) is the space of infinitesimal deformations; H^2(X, T_X) contains obstructions. To discover whether a complex manifold has moduli, *compute these cohomology groups*.

**Discovery trigger:** Riemann's original moduli-count 3g − 3 for curves was intuitive but non-rigorous. Kodaira–Spencer wanted a conceptual theory: which complex manifolds deform, and in how many directions? They identified the tangent sheaf T_X and H^1(X, T_X) as the precise infinitesimal answer.

**Thought process / lineage:** Kodaira–Spencer (1958, *Ann. Math.* 67 and 68) for complex-analytic case. Grothendieck (1960, FGA) abstracted to schemes: cotangent complex L_X controls deformations. Illusie (1971) gave the derived cotangent complex in full generality. Schlessinger (1968) characterized which functors of Artin rings are representable by formal moduli. Artin (1969) proved algebraization.

**Proof idea / process:**
1. Cover X by charts; each chart is fixed, but gluings depend on base point b ∈ B.
2. Differentiating the gluing cocycle with respect to b gives a Čech 1-cocycle with values in T_X — the Kodaira–Spencer class.
3. Independence of choice of charts ⇒ class lives in H^1(X, T_X).
4. The integrability obstruction (can you complete a 1st-order deformation to 2nd-order?) lives in H^2(X, T_X).

**Impact:** Moduli of curves, abelian varieties, surfaces, Calabi–Yau manifolds — all dimension counts are H^1(T) minus automorphism H^0(T) computations. Mirror symmetry's discovery (Candelas–de la Ossa–Green–Parkes 1991) was via computing H^1(T) of a Calabi–Yau and matching it to a Hodge-dual group on the mirror. Variations of Hodge structure (Griffiths transversality) use the Kodaira–Spencer map to compute periods.

**Sources (≥1 non-Wikipedia):**
- Stacks Project, tag 06G7 "Deformation theory": https://stacks.math.columbia.edu/tag/06G7
- nLab, "Kodaira-Spencer map": https://ncatlab.org/nlab/show/Kodaira-Spencer+map
- Sernesi, *Deformations of Algebraic Schemes* (Springer Grundlehren 334), §1.2: https://link.springer.com/book/10.1007/978-3-540-30615-3

**Technique tag:** NEW — `deformationCohomology(geometric object X, tangent/cotangent complex) → (H¹ = deformations, H² = obstructions)` — classify/compute first-order deformations and their obstructions via explicit cohomology groups of the tangent (or cotangent) complex. *Inherits: `obstructionClass`, `analysisAlgebraTopologyBridge`, `spectralSequenceCompute` (when the tangent complex is multi-step).*

---

### 8. Obstruction in Ext² (1968, Schlessinger; 1973, Illusie)

**Statement / description:** For deformations of a scheme, sheaf, or module M, the first-order deformations form a torsor over Ext¹(M, M) (or Ext¹(L_X, 𝒪_X)), and there is a canonical obstruction map o: Ext¹ × Ext¹ → Ext² such that a first-order deformation extends to second order iff o vanishes. Discovery rule: "any extension problem has its existence obstruction one Ext-degree higher."

**Discovery trigger:** Schlessinger wanted Kodaira–Spencer for general functors on Artin local rings (not just families of complex manifolds). Abstracting the argument isolated the two cohomology groups and gave a criterion (Schlessinger's criteria H1–H4) for when a functor of Artin rings is pro-representable.

**Thought process / lineage:** Schlessinger (1968 thesis, 1968 *TAMS* 130) gave the functorial conditions. Illusie (1971) introduced the cotangent complex L_{X/S} and showed Ext^i(L, 𝒪) generalize deformations (i=1) and obstructions (i=2). Deligne's use in Hodge theory and Artin's approximation theorem followed. The obstruction-theoretic style — "try to lift an existing solution step-by-step, accumulating classes in Ext^{n+1}" — pervades modern algebraic geometry.

**Proof idea / process:**
1. Deform M over dual numbers k[ε]/ε²: a first-order deformation ⇔ a class α ∈ Ext¹(M, M).
2. Try to extend to k[ε]/ε³: compute the cup product α ∪ α ∈ Ext²(M, M) using the Yoneda pairing.
3. Extension exists iff α ∪ α = 0. If so, space of extensions is a torsor over Ext¹.
4. Iterate at each order; the obstruction tower lives in Ext²; if Ext² vanishes, all obstructions vanish ("unobstructed").

**Impact:** Deformations of Calabi–Yau are unobstructed (Bogomolov–Tian–Todorov 1989) — proved via showing the obstruction Ext² cup product is a coboundary. Deformations of coherent sheaves → moduli of stable sheaves (Mukai, Simpson). Modular deformation rings R in Wiles's R = T theorem controlled by Ext² in Galois cohomology. Derived moduli (Toën–Vezzosi, Lurie) systematize the whole tower.

**Sources (≥1 non-Wikipedia):**
- Stacks Project, tag 07Y9 "Deformation theory of algebras and obstruction classes": https://stacks.math.columbia.edu/tag/07Y9
- Illusie, *Complexe cotangent et déformations I, II* (Lecture Notes in Math. 239 & 283, Springer 1971–72). Publisher: https://link.springer.com/book/10.1007/BFb0059052
- nLab, "formal moduli problem": https://ncatlab.org/nlab/show/formal+moduli+problem

**Technique tag:** NEW — `extSquaredObstruction(first-order deformation α ∈ Ext¹(M,M)) → obstruction α∪α ∈ Ext²(M,M); lift exists iff obstruction vanishes` — use Yoneda cup product to turn "can I extend my solution?" into a cohomology class one step up. *Inherits: `deformationCohomology`, `obstructionClass`, `diagramChase`.*

---

### 9. Coherent replacement of equality (1973–2009, Boardman–Vogt → Lurie)

**Statement / description:** In an ∞-category, two objects are not either "equal" or "not equal"; rather, "equality" is replaced by a space (or ∞-groupoid) of identifications. Commutative diagrams do not commute on the nose, but up to a specified coherence — a homotopy — which itself is subject to higher coherences. Discovery shift: a structure satisfied "up to isomorphism plus coherence" is often the *correct* statement, while strict equality was an artifact.

**Discovery trigger:** Boardman–Vogt (1973) observed that loop spaces ΩX are not strictly associative monoids — concatenation of loops is only associative up to homotopy, but with a *canonical* associator, and pentagon-of-associators, and so on ad infinitum. Calling this a "monoid up to coherent homotopy" turned infinitely many conditions into a single A_∞-structure.

**Thought process / lineage:** Stasheff (1963) introduced A_∞-spaces with associahedra. Boardman–Vogt (1973) and May (1972) reformulated via operads. Joyal (1980s+) developed quasicategories as a model. Lurie (*Higher Topos Theory* 2009, *Higher Algebra* 2017) gave the complete ∞-categorical foundation. Cisinski, Rezk, Bergner, Barwick — model-category comparisons.

**Proof idea / process:**
1. Instead of a set of morphisms X → Y, take a space Map(X, Y) — a topological / simplicial set.
2. Composition X → Y → Z is not a single operation but a homotopy-coherent family parameterized by associahedra (or Joyal's horn-filling).
3. A "commutative square" becomes a homotopy H between two composites; "commutative cube" becomes a homotopy between homotopies.
4. Every diagram is a functor from a shape-category I into the ∞-category C — enforced by simplicial horn filling (Joyal) or Segal conditions.

**Impact:** Derived algebraic geometry (Toën–Vezzosi, Lurie), where moduli-stacks always satisfy descent up to coherent homotopy. Modern stable homotopy — derived categories of sheaves, derived pullback behaves correctly. Cobordism hypothesis (Baez–Dolan 1995, Lurie 2009) — fully extended TQFTs classified by (∞,n)-categories. All the pathologies of strict categorification (failure of gluing, phantom maps, etc.) dissolve.

**Sources (≥1 non-Wikipedia):**
- nLab, "(infinity,1)-category": https://ncatlab.org/nlab/show/%28infinity%2C1%29-category
- Lurie, *Higher Topos Theory* (Princeton Annals of Math Studies 170, 2009), chaps. 1–2. Open PDF: https://www.math.ias.edu/~lurie/papers/HTT.pdf
- Riehl & Verity, *Elements of ∞-Category Theory* (Cambridge 2022). Open PDF: https://emilyriehl.github.io/files/elements.pdf

**Technique tag:** NEW — `replaceEqualityByCoherentHomotopy(strict structure with equalities that "should" hold) → ∞-categorical structure with coherent-homotopy data` — when "=" causes obstructions or rigidity, weaken to ≃ plus an infinite tower of coherences; the weakening often is the correct statement. *Inherits: `axiomatizeFromInstances`, `structuralIsomorphism`.*

---

### 10. Straightening–unstraightening (2009, Lurie)

**Statement / description:** A functor F: C → Cat from a category (or ∞-category) to the ∞-category of ∞-categories is equivalent data to a *cartesian fibration* p: D → C. One direction ("unstraighten") sends F to its category of elements / Grothendieck construction; the other ("straighten") recovers F from the fibers and the cartesian lifts. This is the canonical way to convert between fibered and functorial descriptions.

**Discovery trigger:** Grothendieck (1961) proved the 1-categorical version: fibered categories over C ↔ pseudofunctors C^op → Cat. Lurie needed the ∞-categorical analog to treat moduli problems, where the "cartesian fibration" encoding a moduli stack is much easier to describe concretely than the corresponding functor.

**Thought process / lineage:** Grothendieck (SGA 1, 1961) introduced fibered categories. Street (1974, 2004) formalized 2-categorical versions. Joyal (1990s) made the ∞-analogue precise for quasicategories. Lurie (*Higher Topos Theory* §3.2, 2009) proved the straightening–unstraightening equivalence between cocartesian fibrations and functors to ∞-categories — a Quillen equivalence of model categories.

**Proof idea / process:**
1. Given p: D → C cocartesian, fiber over c ∈ C is D_c; a morphism f: c → c' in C lifts cocartesianly to D_c → D_{c'}, inducing f_!: D_c → D_{c'}.
2. Package fibers and induced functors into a pseudofunctor F: C → Cat_∞. This is straightening.
3. Conversely, given F, build D whose objects are pairs (c, x ∈ F(c)) and morphisms (c, x) → (c', x') are pairs (f: c → c', x' → F(f)(x)). This is unstraightening.
4. Lurie's theorem: these are mutually inverse equivalences of (∞,1)-categories.

**Impact:** Backbone of higher category theory — virtually every construction in *HTT* / *HA* uses it (tangent complex as a straightening, stable ∞-categories, presentable ∞-categories, descent, monoidal structures). In derived algebraic geometry, moduli functors ↔ their moduli stacks via this equivalence. Homotopy-theoretic descent (Barwick, Rognes) relies on unstraightening.

**Sources (≥1 non-Wikipedia):**
- nLab, "straightening and unstraightening": https://ncatlab.org/nlab/show/straightening+functor
- Lurie, *Higher Topos Theory*, §§2.2, 3.2: https://www.math.ias.edu/~lurie/papers/HTT.pdf
- Mazel-Gee, "A user's guide to co/cartesian fibrations," arXiv:1510.02402.

**Technique tag:** NEW — `straightenUnstraighten(cartesian fibration p: D → C ↔ functor F: C → Cat_∞) → bidirectional equivalence` — convert between "total category with projection" (easy geometry) and "diagram of categories" (easy algebra). *Inherits: `representableFunctorTrick`, `duality`, `replaceEqualityByCoherentHomotopy`.*

---

### 11. Sheafification via Grothendieck topology (1962, Grothendieck–Verdier)

**Statement / description:** A Grothendieck topology on a category C is a choice, for each object U, of "covering families" {U_i → U}. A sheaf is a presheaf F: C^op → Set such that F(U) is recovered from F(U_i) via compatible restrictions (equalizer condition). Sheafification is the left adjoint to inclusion Sh(C, τ) ↪ PSh(C) — the universal way to force a presheaf to satisfy descent. Discovery tool: whenever a "local-to-global" problem fails, try to sheafify your functor.

**Discovery trigger:** Grothendieck needed étale cohomology to prove the Weil conjectures. The étale topology on a scheme has no underlying topological space — "coverings" are surjective étale maps, which don't all come from open subsets. Defining cohomology required building all sheaf machinery *purely categorically* from a coverage.

**Thought process / lineage:** Leray (1940s) developed sheaves on topological spaces. Cartan seminar (1950s) systematized. Grothendieck (Tohoku 1957; SGA 4, 1963–64) generalized to sites: replace open covers by axiomatic covering families. Verdier formalized sheafification and derived functors. Giraud's theorem (1964) characterized Grothendieck toposes as left-exact reflective subcategories of presheaves.

**Proof idea / process:**
1. Specify covering families: sieves that include identities, stable under pullback, local ("covering of a covering is a covering").
2. A presheaf F is a sheaf iff for every cover {U_i → U}, F(U) = eq(∏F(U_i) ⇒ ∏F(U_i ×_U U_j)).
3. Sheafification: take the plus-construction F⁺(U) = colim over covers of matching families; apply twice if necessary.
4. Universal property: any presheaf morphism to a sheaf factors uniquely through the sheafification.

**Impact:** Étale cohomology (Grothendieck, Deligne → Weil conjectures). Crystalline cohomology (Berthelot 1974), ℓ-adic cohomology, flat cohomology. Topos-theoretic semantics of intuitionistic logic. Voevodsky's Nisnevich topology → motivic cohomology → Milnor/Bloch–Kato conjectures. In ∞-category theory: hypercovers and ∞-sheaves (Lurie, Toën–Vezzosi) enable derived algebraic geometry.

**Sources (≥1 non-Wikipedia):**
- Stacks Project, tag 00VG "Sites and sheaves": https://stacks.math.columbia.edu/tag/00VG
- Stacks Project, tag 00W1 "Sheafification": https://stacks.math.columbia.edu/tag/00W1
- nLab, "sheafification": https://ncatlab.org/nlab/show/sheafification

**Technique tag:** NEW — `sheafifyOnGrothendieckTopology(presheaf F on a site (C,τ)) → sheaf aF with universal map F → aF` — universally force local-to-global gluing on any presheaf; enables "cohomology" on categories without a topological space. *Inherits: `axiomatizeFromInstances`, `representableFunctorTrick`.*

---

### 12. Geometric morphism (1970, Lawvere; Street, Lawvere–Tierney)

**Statement / description:** A geometric morphism f: E → F of toposes is an adjunction (f^*, f_*) where f^* preserves finite limits — the categorical shadow of a continuous map of spaces. It translates the *internal logic* of one topos into another. Classifying toposes: for every geometric theory 𝕋 there is a topos Set[𝕋] such that geometric morphisms F → Set[𝕋] correspond to 𝕋-models in F.

**Discovery trigger:** Lawvere (1969–70) wanted a categorical language unifying the topos of sheaves on a topological space, the topos of G-sets, and the Zariski topos. Geometric morphisms generalize continuous maps, equivariant maps, and morphisms of schemes under one roof.

**Thought process / lineage:** Grothendieck–Verdier (SGA 4, 1963–64) defined Grothendieck toposes and geometric morphisms for sites. Lawvere (1969) axiomatized elementary toposes via subobject classifiers. Lawvere–Tierney (1970) introduced "local" geometric morphisms and internal Heyting algebra. Makkai–Reyes and Johnstone in the 1970s–80s connected toposes to categorical logic and classifying toposes. Joyal and others extended to ∞-toposes (Lurie 2009).

**Proof idea / process:**
1. Given f: X → Y continuous, get (f^*, f_*) between Sh(X) and Sh(Y) with f^* ⊣ f_* and f^* left-exact.
2. Abstract: a geometric morphism E → F is such an adjunction preserving finite limits in the left adjoint.
3. Geometric formulas (those built from ∧, ∃, ⊤, = under arbitrary disjunction) are preserved by f^*.
4. Hence a model of a geometric theory in F pulls back along f to a model in E, and classifying toposes represent theories.

**Impact:** Internal logic of a topos (Mitchell–Bénabou language) gives intuitionistic set theory; forcing in set theory is a geometric morphism to the Boolean topos of a forcing poset; Cohen's independence proof recast (Tierney). Classifying toposes unify model theory and geometry. Realizability toposes (Hyland 1982) turn constructive logic into arithmetic. Joyal–Tierney (1984) recast descent for stacks as geometric morphisms.

**Sources (≥1 non-Wikipedia):**
- nLab, "geometric morphism": https://ncatlab.org/nlab/show/geometric+morphism
- nLab, "classifying topos": https://ncatlab.org/nlab/show/classifying+topos
- Johnstone, *Sketches of an Elephant: A Topos Theory Compendium* (Oxford 2002), vol. A, part C. Author page: http://www.dpmms.cam.ac.uk/~ptj/

**Technique tag:** NEW — `geometricMorphismAsLogicalTranslation(topos E, topos F) → adjunction (f* ⊣ f_*) with left-exact f* translating geometric theories` — convert a problem in one universe of "sets + logic" into another by pulling back along a continuous logical functor. *Inherits: `duality`, `structuralIsomorphism`, `forceIndependence` (forcing is a geometric morphism).*

---

### 13. Algebra over an operad (1972, May + Boardman–Vogt recognition)

**Statement / description:** An operad O = {O(n)}_{n≥0} specifies an abstract species of "n-ary operation with symmetry"; an algebra over O is a space/object A with maps O(n) × A^n → A compatible with composition and S_n-action. To discover/classify homotopy-coherent algebraic structures (A_∞, E_∞, L_∞, Gerstenhaber), identify them as algebras over a canonical operad. Recognition principle (May 1972): a space with an E_n-algebra structure is equivalent (after group-completion) to an n-fold loop space.

**Discovery trigger:** Stasheff (1963) needed associahedra to describe the "up to homotopy associativity" of loop space multiplication — but the combinatorics became unmanageable for higher-arity coherences. Operads packaged all higher coherences into a single structure. May (1972) applied to recognize E_n-spaces as n-fold loop spaces.

**Thought process / lineage:** Stasheff (1963, *TAMS* 108) — A_∞ associahedra. Boardman–Vogt (1973) — PROPs and operads for loop spaces. May (1972, *The Geometry of Iterated Loop Spaces*) — coined "operad" and proved recognition. Markl–Shnider–Stasheff (2002) — systematic textbook. Ginzburg–Kapranov (1994) added Koszul duality (see next entry). Kontsevich's formality (1997) proved Hochschild cohomology is an E_2-algebra; Deligne conjecture via operads.

**Proof idea / process:**
1. Define operad O(n) = space of "abstract n-ary operations"; include composition O(n) × O(k_1) × ⋯ × O(k_n) → O(k_1 + ⋯ + k_n) and S_n action.
2. An O-algebra is A equipped with structure maps respecting all O-operations.
3. Examples: Assoc (A_∞) has O(n) = associahedron K_n; Comm (E_∞) has O(n) = configuration space of n points in ℝ^∞; Lie has O(n) from the Lie operad (generated by bracket).
4. Recognition: prove your space is O-algebra for the right O → conclude it's a loop space (resp. ring spectrum, resp. A_∞-space, …).

**Impact:** Recognition principle classified what loop spaces "are." E_∞-ring spectra (Lewis–May–Steinberger 1986) → structured ring spectra, THH, topological André–Quillen. Hochschild cohomology of associative algebras is E_2-algebra (Deligne conjecture, Kontsevich–Soibelman). Deformation quantization (Kontsevich 1997) via L_∞-algebras. Goodwillie calculus. Factorization algebras (Beilinson–Drinfeld, Costello–Gwilliam) for perturbative QFT.

**Sources (≥1 non-Wikipedia):**
- nLab, "operad": https://ncatlab.org/nlab/show/operad
- nLab, "recognition principle for iterated loop spaces": https://ncatlab.org/nlab/show/May+recognition+theorem
- May, *The Geometry of Iterated Loop Spaces*, Lecture Notes in Math 271, Springer 1972. Open: http://www.math.uchicago.edu/~may/BOOKS/gils.pdf

**Technique tag:** NEW — `recognizeStructureAsOperadAlgebra(object with complicated multi-ary operations) → O-algebra for an identified operad O, with induced classification theorems` — when operations look governed by abstract combinatorial shapes, name the operad O and import every theorem known about O-algebras. *Inherits: `axiomatizeFromInstances`, `structuralIsomorphism`.*

---

### 14. Koszul duality of operads (1994, Ginzburg–Kapranov)

**Statement / description:** Certain operads O (quadratic ones) have a "Koszul dual" operad O^! such that the bar-cobar construction relates O-algebras and coalgebras over O^!. Classical examples: Assoc^! = Assoc, Comm^! = Lie, Lie^! = Comm. So the theory of commutative algebras and the theory of Lie algebras are Koszul-dual. Tool: use one side when the other is hard.

**Discovery trigger:** Priddy (1970) had shown polynomial rings are "Koszul" for cohomology computations: the bar construction on the symmetric algebra is small (the Koszul complex). Ginzburg–Kapranov asked which operads admit such resolutions — answer: quadratic operads whose Koszul dual is also quadratic — and the duality exchanges Assoc, Comm, Lie pairwise.

**Thought process / lineage:** Priddy (1970, *TAMS* 152) — Koszul duality for associative algebras. Ginzburg–Kapranov (1994, *Duke Math. J.* 76) — operadic generalization. Loday–Vallette (2012, *Algebraic Operads*, Springer Grundlehren 346) — book-length modern treatment. Drinfeld–Beilinson on chiral algebras, Costello on renormalization, Kontsevich's formality theorem — all use Koszul duality of operads.

**Proof idea / process:**
1. Write operad O as ℱ(E)/(R), free on generators E modulo quadratic relations R.
2. Define dual O^! = ℱ(E^*)/(R^⊥), dualizing generators and taking the annihilator of R.
3. Build the Koszul complex: O ⊗ (O^!)^* with differential from the evaluation pairing.
4. O is Koszul iff this complex is a resolution of O ⊗ O^! ≃ the unit; equivalently, Ext over O-algebras equals Tor over O^!-coalgebras.

**Impact:** Enables minimal resolutions (free models) of A_∞, L_∞, C_∞ algebras; these are the cofibrant replacements that computations of Hochschild / Chevalley–Eilenberg / Harrison cohomology actually use. Kontsevich's formality (1997): the Hochschild cohomology HH^*(A) of a smooth commutative algebra is L_∞-quasi-isomorphic to polyvector fields — *via Koszul duality between Assoc and Lie operads*. Beilinson–Ginzburg–Soergel Koszul duality for category O in representation theory. Factorization-algebra methods in QFT.

**Sources (≥1 non-Wikipedia):**
- nLab, "Koszul duality": https://ncatlab.org/nlab/show/Koszul+duality
- Loday & Vallette, *Algebraic Operads*, Springer Grundlehren 346 (2012), chap. 7. Open PDF: https://math.unice.fr/~brunov/Operads.pdf
- Ginzburg & Kapranov, "Koszul duality for operads," arXiv preprint 1994; published Duke Math. J. 76 (1994) 203–272. arXiv: https://arxiv.org/abs/0709.1228 (later reprint)

**Technique tag:** NEW — `koszulDualOperadSwap(quadratic operad O) → dual operad O^! with bar-cobar equivalence between O-algebras and O^!-coalgebras` — exchange a category of algebras for one of coalgebras over the dual operad; the dual side often has the computation you need. *Inherits: `duality`, `recognizeStructureAsOperadAlgebra`, `spectralSequenceCompute` (bar spectral sequence).*

---

### 15. Deligne–Mumford compactification (1969, Deligne–Mumford)

**Statement / description:** The moduli space M_g of smooth curves of genus g is not proper — curves can degenerate to singular ones. Deligne–Mumford enlarge M_g to M̄_g by adding *stable* nodal curves (finite automorphism, nodes only, each rational irreducible component meets the rest in ≥3 points). M̄_g is a smooth proper Deligne–Mumford stack with boundary stratification by dual graphs. Discovery principle: the correct completion of a moduli space is the one that makes specialization well-defined and the universal family proper.

**Discovery trigger:** Deligne–Mumford (1969) proved irreducibility of M_g in any characteristic. The obstacle was that M_g is not compact — they needed a compactification supporting a universal family. Stable curves — nodes and no infinite automorphisms — turned out to be the unique "good" degeneration.

**Thought process / lineage:** Mumford's GIT (1965) had built M_g as a quasi-projective scheme. Deligne–Mumford (1969, *Publ. IHES* 36) added stable-curve boundary; introduced *algebraic stacks* to handle curves with nontrivial automorphisms. Knudsen (1983) extended to M̄_{g,n}. Keel (1992) proved M̄_{0,n} is a blow-up of projective space. Kontsevich (1994) used M̄_{g,n}(X, β) to define Gromov–Witten invariants (see entry 16).

**Proof idea / process:**
1. Define stability: a nodal curve C with marked points {p_i} is *stable* iff every smooth rational component has ≥3 "special points" (nodes + marked points).
2. Show stable curves form a bounded family — proper because semistable reduction (Deligne–Mumford) lets you fill any one-parameter family.
3. Construct M̄_g as a proper smooth DM stack by descent from a finite cover via Hilbert schemes; boundary ∂M̄_g stratifies by stable dual graphs.
4. Universal stable curve C̄_g → M̄_g exists, enabling enumerative geometry.

**Impact:** Witten's conjecture (Kontsevich's proof 1992) — integrals on M̄_{g,n} satisfy KdV hierarchy. Gromov–Witten invariants as integrals on M̄_{g,n}(X, β). Mirror symmetry A-side. Intersection theory of the tautological ring (Faber–Pandharipande). Modular forms from Hodge bundle on M̄_g. All of enumerative geometry on curves "lives on" M̄_{g,n}.

**Sources (≥1 non-Wikipedia):**
- Stacks Project, tag 0E6S "Algebraic stacks / moduli of curves": https://stacks.math.columbia.edu/tag/0E6S
- Harris & Morrison, *Moduli of Curves* (Springer GTM 187, 1998), chap. 3: https://link.springer.com/book/10.1007/b98867
- Vistoli, "Notes on Grothendieck topologies, fibered categories and descent theory," arXiv:math/0412512.

**Technique tag:** NEW — `compactifyByStableDegenerations(moduli space M of smooth objects) → proper moduli stack M̄ with boundary of canonical stable singular objects` — fill in a non-proper moduli space by allowing only the "mildest" singular objects with finite automorphism; recover properness and a stratified boundary. *Inherits: `compactnessArgument`, `deformationCohomology`, `obstructionClass`.*

---

### 16. Virtual fundamental class (1996, Li–Tian; Behrend–Fantechi)

**Statement / description:** When a moduli space M has expected dimension d but actual dimension > d (excess intersection), the virtual fundamental class [M]^{vir} ∈ A_d(M) is a canonical class in the Chow group of the expected dimension. Integration against [M]^{vir} defines Gromov–Witten invariants, Donaldson–Thomas invariants, and general "enumerative counts" on obstructed moduli. Discovery rule: never count naively on a non-smooth moduli space — construct and integrate against [M]^{vir}.

**Discovery trigger:** Gromov–Witten invariants were supposed to count pseudo-holomorphic curves in a symplectic manifold, giving numbers independent of the almost-complex structure. But the moduli space M̄_{g,n}(X, β) is in general not smooth and may not have expected dimension. A correct number required a virtual class.

**Thought process / lineage:** Li–Tian (1996, arXiv:alg-geom/9602007) gave the symplectic / analytic version via Kuranishi structures. Behrend–Fantechi (1997, *Invent. Math.* 128) gave the algebraic version using the intrinsic normal cone and a perfect obstruction theory. Siebert (1996) via derived schemes; Kontsevich earlier ideas on virtual counting. Donaldson–Thomas invariants for sheaves (Thomas 2000) follow the same template. Modern derived-algebraic-geometry formulation (Schürg–Toën–Vezzosi 2015): [M]^{vir} is the ordinary fundamental class of a derived enhancement of M.

**Proof idea / process:**
1. Equip M with a *perfect obstruction theory*: a morphism E^• → L_M in the derived category where E^• is a 2-term complex of vector bundles [E^{−1} → E^0] and the map induces an iso on H^0 and a surjection on H^{−1}.
2. Form the intrinsic normal cone C_M inside the bundle stack h^1/h^0(E^•∨); it is pure of the expected dimension.
3. Intersect with the zero section of E_1 = (E^{−1})^∨ to cut down to a class of dimension rank E^0 − rank E^{−1}.
4. [M]^{vir} ∈ A_{vd}(M) with vd = rank E^0 − rank E^{−1} the expected (virtual) dimension.

**Impact:** Rigorous definition of Gromov–Witten invariants for any smooth projective variety (Li–Tian, Behrend–Fantechi; Ruan–Tian symplectic). Donaldson–Thomas invariants of Calabi–Yau threefolds. Wall-crossing formulas (Joyce–Song, Kontsevich–Soibelman) operating on virtual classes. MNOP conjecture (Maulik–Nekrasov–Okounkov–Pandharipande 2006) relating GW and DT. Vafa–Witten invariants of four-manifolds. Virtual localization (Graber–Pandharipande 1999) reduces GW counts to fixed loci under torus actions.

**Sources (≥1 non-Wikipedia):**
- Stacks Project, tag 0H72 "Virtual fundamental classes and obstruction theories": https://stacks.math.columbia.edu/tag/0H72
- nLab, "virtual fundamental class": https://ncatlab.org/nlab/show/virtual+fundamental+class
- Behrend & Fantechi, "The intrinsic normal cone," *Invent. Math.* 128 (1997), arXiv preprint: https://arxiv.org/abs/alg-geom/9601010

**Technique tag:** NEW — `virtualClassFromObstructionTheory(moduli M with perfect obstruction theory E^• → L_M) → [M]^{vir} ∈ A_{vd}(M) of expected dimension, suitable for enumerative integration` — carve a correctly-dimensioned enumerative class out of a non-smooth moduli space using its obstruction complex. *Inherits: `deformationCohomology`, `extSquaredObstruction`, `compactifyByStableDegenerations`, `pushforwardAsIndex`.*

---

## Summary breakdown

### By gap area

| Gap area | Count | Entries |
|---|---|---|
| 1. Representation theory | 3 | 1, 2, 3 |
| 2. K-theory | 3 | 4, 5, 6 |
| 3. Deformation theory | 2 | 7, 8 |
| 4. Higher / ∞-category | 2 | 9, 10 |
| 5. Topos theory | 2 | 11, 12 |
| 6. Operad theory | 2 | 13, 14 |
| 7. Moduli-space methods | 2 | 15, 16 |
| **Total** | **16** | |

### By existing-tag-extension vs. new-technique proposal

| Type | Count | Notes |
|---|---|---|
| Pure **NEW** technique proposals | 16 | Each entry defines a new camelCase technique function with precondition / process / postcondition. See tags column below. |
| Existing-technique extensions (examples added to a pre-existing function) | 0 pure, 1 shared | Entry 1 also supplies new examples for existing `symmetryReduction` and `conservedQuantity` (character tables ARE the canonical group invariants) — flagged for the researcher to consider folding that aspect into those existing entries. |

All 16 NEW technique names:
1. `characterDecompositionCount`
2. `induceThenDecompose`
3. `doubleCentralizerDecompose`
4. `groupCompleteExactCategory`
5. `exploitPeriodicityInObstructionTower`
6. `pushforwardAsIndex`
7. `deformationCohomology`
8. `extSquaredObstruction`
9. `replaceEqualityByCoherentHomotopy`
10. `straightenUnstraighten`
11. `sheafifyOnGrothendieckTopology`
12. `geometricMorphismAsLogicalTranslation`
13. `recognizeStructureAsOperadAlgebra`
14. `koszulDualOperadSwap`
15. `compactifyByStableDegenerations`
16. `virtualClassFromObstructionTheory`

### Inheritance density observation

These 16 new techniques cite each other extensively, forming a dense subgraph:
- Chain 7 → 8 → 16 (deformations → Ext² obstruction → virtual class) is a single computational pipeline.
- Chain 4 → 5 → 6 (K₀ → Bott periodicity → K-theoretic index) is the complete K-theory backbone.
- 13 → 14 (operads → Koszul duality) and 9 → 10 (coherent equality → straightening) are each internally coupled.
- Across clusters: 16 depends on 15 (moduli compactification), 8 (obstructions), 7 (deformation); 6 depends on 5 (periodicity) and ultimately K₀ (4); the operad and ∞-category strands interact via E_n-algebras.

### Cluster placement recommendations (for researcher/engineer)

- **Cluster 12 (Homological & Categorical)** absorbs entries 4, 8, 9, 10, 11, 12 cleanly.
- **Cluster 6 (Topology & Obstruction)** absorbs 5, 6, 7, 13, 16.
- **Cluster 3 (Symmetry & Invariants)** absorbs 1, 2, 3, 14 (representation theory + Koszul duality).
- Entry 15 (Deligne–Mumford compactification) most naturally joins **Cluster 6** (compactification-as-obstruction-removal).
- No new cluster required. The 12 existing clusters comfortably accommodate all 16.

### Flags for the researcher

1. **Entry 1 overlap:** `characterDecompositionCount` is deeply related to existing `symmetryReduction` and `conservedQuantity` (characters ARE class-function invariants). I propose it stand alone because characters give *numerical* (not just qualitative) decomposition — a distinct discovery verb. Researcher may prefer to merge.

2. **Entry 4 vs. existing `obstructionClass`:** K₀ as "universal additive invariant" overlaps with the obstruction-class philosophy but differs fundamentally in being *constructive* (a free abelian group) rather than *negative* (vanishing-as-obstruction). I kept them separate.

3. **Entries 9 & 10 (∞-category):** these are broad-methodological rather than theorem-shaped. I framed them as verbs ("replace equality by coherent homotopy," "straighten–unstraighten") to fit the schema. Engineer should ensure preconditions aren't too vague.

4. **Entry 16 depends on derived geometry:** the modern derived-scheme definition of [M]^{vir} (Schürg–Toën–Vezzosi) may deserve mention in the process steps; I used the classical Behrend–Fantechi intrinsic-normal-cone formulation which is better-documented in open sources.

5. **Attribution notes:**
 - Entry 8: "Ext² obstruction" is Schlessinger (functor-of-Artin-rings version, 1968) and Illusie (cotangent-complex version, 1971) jointly. I credited both; primary citation is Illusie LNM 239 for the general formulation.
 - Entry 15: Deligne–Mumford (1969) proved the compactification; Knudsen (1983) added n marked points. I focused on the 1969 landmark.
 - Entry 16: Li–Tian (symplectic, 1996) and Behrend–Fantechi (algebraic, 1997) are *independent, near-simultaneous* constructions. I credited both.

6. **One omission flagged:** "Brauer induction" (listed in the brief) I did not give a dedicated entry — it is a classical *theorem* rather than a discovery *technique* in the toolbox sense (it states every character is an integer combination of inductions from elementary subgroups; its use as a verb is folded under entry 2 `induceThenDecompose`). Researcher may want to add it as an example under entry 2 rather than as a separate technique.

7. **Source-diversity note:** Every entry has at least one non-Wikipedia primary source (nLab, Stacks, arXiv, MacTutor, or author-hosted open PDF). I avoided Wikipedia entirely for this round. Several entries cite author-hosted open PDFs of textbooks (Lurie HTT, Weibel K-book, May recognition book, Loday–Vallette Operads) — these are stable open links but should be spot-checked.
