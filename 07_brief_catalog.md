# 7. Brief Catalog of Named Theorems

Abbreviated reference for theorems not covered in depth in Chapters 1–6. Entries are organized by subfield, with discoverer and approximate year where known. Entries use the format:

**Theorem name** (*Discoverer, year*) — One-line statement or significance.

---

## Logic and Foundations

- **Compactness theorem** (*Gödel 1930, Malcev 1936 for uncountable*) — A set of first-order sentences is satisfiable iff every finite subset is. Cornerstone of model theory.
- **Löwenheim–Skolem theorem** (*Löwenheim 1915, Skolem 1920*) — Any first-order theory with an infinite model has models of every infinite cardinality. Implies the "Skolem paradox" about countable models of set theory.
- **Church–Rosser theorem** (*Church and Rosser, 1936*) — In lambda calculus, reduction is confluent: the order of reduction steps does not affect the final normal form.
- **Deduction theorem** (*Herbrand 1930, Tarski*) — In a formal system, Γ ∪ {A} ⊢ B iff Γ ⊢ A → B.
- **Łoś's theorem** (*Jerzy Łoś, 1955*) — First-order truths in an ultraproduct are determined by truths in the factor structures. Foundation of nonstandard analysis.
- **Craig's interpolation theorem** (*William Craig, 1957*) — If A ⊢ B, there is a formula C using only symbols common to A and B such that A ⊢ C and C ⊢ B.
- **Beth's definability theorem** (*Evert Beth, 1953*) — Implicit definability equals explicit definability in first-order logic.
- **Lindström's theorem** (*Per Lindström, 1969*) — First-order logic is the strongest logic with the compactness property and the Löwenheim–Skolem property. A uniqueness result for first-order logic.
- **Morley's categoricity theorem** (*Michael Morley, 1965*) — If a countable first-order theory is categorical in some uncountable cardinal, it is categorical in all of them. The founding theorem of modern model theory.
- **Martin's Borel determinacy theorem** (*Donald A. Martin, 1975*) — Every Borel set in the Baire space is determined. Requires a remarkable amount of set-theoretic strength.
- **Cohen's forcing theorems** (*Paul Cohen, 1963*) — Technical machinery showing CH and AC are independent of ZF.
- **Matiyasevich's theorem / MRDP theorem** (*Yuri Matiyasevich, 1970, after Robinson-Davis-Putnam*) — Hilbert's 10th problem is unsolvable: no algorithm decides whether a Diophantine equation has integer solutions.
- **Paris–Harrington theorem** (*1977*) — A Ramsey-type statement true in ℕ but unprovable in Peano arithmetic. A natural Gödel-incomplete statement.
- **Gentzen's consistency proof** (*Gerhard Gentzen, 1936*) — PA is consistent, provable using transfinite induction up to ε₀. A constructive response to Gödel.

## Set Theory

- **Axiom of choice equivalents** — Zorn's lemma, Zermelo's well-ordering theorem, Tukey's lemma, Tychonoff's theorem (for Hausdorff), and the trichotomy of cardinals are all provably equivalent over ZF.
- **Schröder–Bernstein theorem** (*Cantor 1887, Dedekind, Schröder 1898, Bernstein 1905*) — If |A| ≤ |B| and |B| ≤ |A|, then |A| = |B|. Proved without AC.
- **Hartogs's theorem** (*Friedrich Hartogs, 1915*) — For any set X there is a least ordinal not injectable into X.
- **König's theorem** (*Julius König, 1905*) — If κᵢ < λᵢ for all i in an index set I, then Σκᵢ < Πλᵢ. A strict inequality among cardinals.
- **Reflection principle** (*Lévy, Montague*) — Truths in V are reflected by set-sized stages Vα.
- **Silver's theorem** (*Jack Silver, 1974*) — GCH cannot first fail at a singular cardinal of uncountable cofinality. A surprising constraint.

## Combinatorics

- **Hall's marriage theorem** (*Philip Hall, 1935*) — A bipartite graph G = (X ∪ Y, E) has a perfect matching saturating X iff |N(S)| ≥ |S| for every S ⊆ X.
- **König's lemma** (*Dénes Kőnig, 1927*) — Every infinite finitely-branching tree has an infinite path. Foundational in combinatorial logic.
- **Kőnig's theorem** (*Dénes Kőnig, 1931*) — In bipartite graphs, max matching = min vertex cover.
- **Dilworth's theorem** (*Robert Dilworth, 1950*) — In any finite poset, max antichain size = min number of chains covering the poset.
- **Mirsky's theorem** (*Leon Mirsky, 1971*) — Dual of Dilworth's: max chain size = min antichain cover.
- **Turán's theorem** (*Paul Turán, 1941*) — The densest K_{r+1}-free graph on n vertices is the balanced r-partite graph. Foundation of extremal graph theory.
- **Erdős–Ko–Rado theorem** (*1961*) — A family of k-element subsets of {1,...,n} with pairwise nonempty intersection has size at most (n−1 choose k−1).
- **Menger's theorem** (*Karl Menger, 1927*) — Max vertex-disjoint paths between two vertices equals min vertex cut separating them. Graph-theoretic max-flow-min-cut.
- **Max-flow min-cut theorem** (*Ford–Fulkerson, 1956*) — The max flow in a network equals the min capacity of an s–t cut.
- **Kuratowski's theorem** (*Kazimierz Kuratowski, 1930*) — A graph is planar iff it contains no subdivision of K₅ or K_{3,3}.
- **Wagner's theorem** (*Klaus Wagner, 1937*) — A graph is planar iff it contains no K₅ or K_{3,3} minor. Equivalent but in the minor-closed formulation.
- **Schur's theorem (Ramsey)** (*Issai Schur, 1916*) — For any r, if N is large enough and {1,...,N} is r-colored, some monochromatic x + y = z exists.
- **Van der Waerden's theorem** (*Bartel van der Waerden, 1927*) — For any r, k there is N such that every r-coloring of {1,...,N} contains a monochromatic arithmetic progression of length k.
- **Hales–Jewett theorem** (*Alfred Hales and Robert Jewett, 1963*) — A Ramsey-theoretic statement about combinatorial lines in high-dimensional cubes. Proves van der Waerden etc.
- **Hindman's theorem** (*Neil Hindman, 1974*) — Any finite partition of ℕ has a cell containing all finite sums from some infinite set. Proved using Stone–Čech compactification.
- **Cayley's formula** (*Arthur Cayley, 1889*) — The number of labeled trees on n vertices is n^(n−2). Many proofs (Prüfer, bijective, matrix-tree).
- **Matrix-tree theorem** (*Kirchhoff, 1847*) — The number of spanning trees of a graph equals any cofactor of its Laplacian matrix.
- **BEST theorem** (*de Bruijn, van Aardenne-Ehrenfest, Smith, Tutte*) — Counts Eulerian circuits in a directed graph via arborescences and degrees.
- **Burnside's lemma / Cauchy–Frobenius lemma** (*1887 attribution issue*) — Number of orbits = average number of fixed points. Foundational counting tool under group action.
- **Pólya enumeration theorem** (*George Pólya, 1937*) — Generating-function generalization of Burnside for counting colorings under symmetry.
- **Pigeonhole principle** (*Dirichlet, 1834*) — If n+1 pigeons sit in n holes, some hole holds at least 2.

## Number Theory

- **Fermat's two-square theorem** (*Fermat 1640, proved Euler 1747*) — An odd prime p is a sum of two squares iff p ≡ 1 (mod 4).
- **Lagrange's four-square theorem** (*Lagrange, 1770*) — Every natural number is a sum of four integer squares. Generalized by Hilbert–Waring.
- **Legendre's three-square theorem** (*Legendre, 1797–98*) — n is a sum of three squares iff n is not of the form 4^a(8b+7).
- **Bertrand's postulate / Chebyshev's theorem** (*conjectured Bertrand 1845, proved Chebyshev 1852*) — For any n ≥ 1 there is a prime p with n < p < 2n.
- **Dirichlet's theorem on primes in arithmetic progressions** (*Dirichlet, 1837*) — For gcd(a,d) = 1, infinitely many primes ≡ a (mod d). Founded analytic number theory with L-functions.
- **Dirichlet's unit theorem** (*Dirichlet, 1846*) — Structure of the unit group in a number field's ring of integers.
- **Minkowski's theorem on convex bodies** (*Hermann Minkowski, 1896*) — A centrally-symmetric convex body in ℝⁿ of volume > 2ⁿ contains a nonzero lattice point. Founded geometry of numbers.
- **Hilbert–Waring theorem** (*Hilbert, 1909*) — For every k there is g(k) such that every natural number is a sum of g(k) k-th powers.
- **Thue's theorem** (*Axel Thue, 1909*) — Rational approximations to an algebraic number of degree n ≥ 3 have bounded quality; ⇒ Thue equations have finitely many integer solutions.
- **Roth's theorem** (*Klaus Roth, 1955*) — An algebraic irrational α cannot be approximated by rationals p/q to order better than 2+ε. Sharpening of Thue–Siegel.
- **Siegel's theorem on integral points** (*Carl Ludwig Siegel, 1929*) — An algebraic curve of genus ≥ 1 has finitely many integer points.
- **Mordell–Weil theorem** (*Mordell 1922 for ℚ, Weil 1929 for number fields*) — The group of rational points on an abelian variety over a number field is finitely generated.
- **Hasse–Minkowski theorem** (*Hasse, 1920s*) — A quadratic form over ℚ has a nontrivial zero iff it has one over every completion ℚ_p and ℝ. Local-global principle.
- **Hasse's theorem on elliptic curves** (*Hasse, 1930s*) — For E/F_q, |#E(F_q) − (q+1)| ≤ 2√q. A Riemann hypothesis for curves.
- **Weil conjectures (Deligne's theorem)** (*Weil 1949 conjectures, Dwork 1960 rationality, Grothendieck cohomology, Deligne 1974 RH*) — Deep properties of zeta functions of varieties over finite fields; Deligne's proof earned the Fields Medal.
- **Chebotarev density theorem** (*Nikolai Chebotarev, 1922*) — The distribution of Frobenius elements in the Galois group of a number field extension follows the density proportional to conjugacy class size.
- **Main theorem of class field theory** (*Takagi 1920, Artin 1927*) — Abelian extensions of a number field correspond to generalized ideal class groups.
- **Artin reciprocity law** (*Emil Artin, 1927*) — The Artin map gives an explicit isomorphism in class field theory. Generalizes quadratic reciprocity.
- **Erdős–Ginzburg–Ziv theorem** (*1961*) — Any 2n−1 integers have n whose sum is divisible by n.
- **Chen's theorem** (*Chen Jingrun, 1966*) — Every sufficiently large even integer is the sum of a prime and a product of at most two primes. Closest we have to Goldbach.
- **Vinogradov's theorem** (*Ivan Vinogradov, 1937*) — Every sufficiently large odd integer is a sum of three primes. Predates Helfgott's full weak Goldbach.

## Field Theory & Polynomials

- **Eisenstein's criterion** (*Gotthold Eisenstein, 1850*) — An irreducibility test for polynomials over ℤ using a prime p.
- **Gauss's lemma (polynomials)** (*Gauss, 1801*) — The product of primitive polynomials over ℤ is primitive; irreducibility over ℤ ⇔ over ℚ for primitives.
- **Primitive element theorem** (*Abel, Galois, Steinitz*) — A finite separable extension has a primitive element: K(α).
- **Artin–Schreier theorem** (*1927*) — Real closed fields are exactly the fields fixed by an involution in the algebraic closure of index 2.
- **Hilbert's theorem 90** (*Hilbert, Zahlbericht 1897*) — For a cyclic Galois extension, the first cohomology of the multiplicative group vanishes.
- **Lüroth's theorem** (*Jakob Lüroth, 1876*) — Every subfield of k(t) between k and k(t) is of the form k(u) for some u.

## Commutative Algebra

- **Nakayama's lemma** (*Tadashi Nakayama, ca. 1950s*) — For a finitely generated module M over a ring with Jacobson radical J, if JM = M, then M = 0. The workhorse lemma of commutative algebra.
- **Krull's principal ideal theorem (Hauptidealsatz)** (*Wolfgang Krull, 1928*) — In a Noetherian ring, the height of a principal prime ideal is at most 1.
- **Krull intersection theorem** (*Krull, 1938*) — For a Noetherian ring R and ideal I, ∩ Iⁿ = 0 on any f.g. module when R is an integral domain or local.
- **Krull–Akizuki theorem** — Integral closure of a Noetherian 1-dim domain in a finite field extension is Noetherian.
- **Cohen structure theorem** (*Irvin Cohen, 1946*) — Complete Noetherian local rings are quotients of power series rings.
- **Hilbert's syzygy theorem** (*Hilbert, 1890*) — Modules over polynomial rings have finite free resolutions of length ≤ number of variables.
- **Auslander–Buchsbaum formula** (*1957*) — For f.g. modules of finite projective dimension over a Noetherian local ring: pdim + depth = depth of the ring.
- **Going-up and going-down theorems** (*Cohen–Seidenberg, 1946*) — Behavior of prime ideals under integral extensions.

## Algebraic Geometry

- **Bézout's theorem** (*Étienne Bézout, 1779*) — Two projective plane curves of degrees m, n with no common component meet in mn points (with multiplicity).
- **Chow's theorem** (*Wei-Liang Chow, 1949*) — An analytic subvariety of projective space is algebraic. Bridges analytic and algebraic geometry.
- **Hironaka's resolution of singularities** (*Heisuke Hironaka, 1964*) — In characteristic zero, any variety admits a resolution by successive blowups. Fields Medal 1970.
- **Serre duality** (*Jean-Pierre Serre, 1955*) — For smooth projective varieties, Hⁱ(X,F) is dual to H^(n−i)(X, F^∨ ⊗ ω_X).
- **Grothendieck–Riemann–Roch** (*Grothendieck, 1957*) — Vast generalization of Riemann–Roch tracking Euler characteristics under proper morphisms.
- **Zariski's main theorem** — Many forms; one: a birational, quasi-finite morphism into a normal scheme is an open immersion.
- **Kodaira vanishing theorem** (*Kunihiko Kodaira, 1953*) — Hⁱ(X, ω_X ⊗ L) = 0 for i > 0 when L is ample on a smooth projective variety over ℂ.
- **Lefschetz hyperplane theorem** — Homotopy/cohomology of a smooth projective variety is determined through middle dimension by a hyperplane section.

## Linear and Multilinear Algebra

- **Rank–nullity theorem** — dim(ker T) + dim(im T) = dim(domain).
- **Spectral theorem (finite dim)** — A normal operator on a finite-dim complex inner product space is unitarily diagonalizable.
- **Schur decomposition** (*Issai Schur, 1909*) — Every square matrix over ℂ is unitarily similar to an upper triangular matrix.
- **Jordan normal form** (*Camille Jordan, 1870*) — Any matrix over an algebraically closed field is similar to a block-diagonal matrix of Jordan blocks.
- **Singular value decomposition** (*Beltrami, Jordan, Sylvester, late 19c*) — Every matrix factors as UΣV* with Σ diagonal nonnegative.
- **Perron–Frobenius theorem** (*Oskar Perron 1907, Georg Frobenius 1912*) — A positive (resp. nonneg irreducible) matrix has a unique largest positive eigenvalue with a positive eigenvector. Foundation of Markov chains, Google PageRank.
- **Gershgorin circle theorem** (*Semyon Gershgorin, 1931*) — Eigenvalues of a matrix lie in the union of disks around diagonal entries with radii equal to row sums of off-diagonals.
- **Sylvester's law of inertia** (*1852*) — The signature of a real quadratic form is invariant under change of basis.
- **Gram–Schmidt process** — Produces an orthonormal basis from any basis; not a theorem per se but a constructive algorithm.
- **Cramer's rule** (*Gabriel Cramer, 1750*) — Determinantal formula for solutions to a square linear system with nonzero determinant.

## Group Theory

- **Cauchy's theorem (group theory)** (*Cauchy, 1845*) — If p | |G| and p is prime, G has an element of order p. Precursor of Sylow.
- **Jordan–Hölder theorem** (*Jordan 1869, Hölder 1889*) — Composition series of a group have uniquely determined factor groups (up to permutation).
- **Krull–Schmidt theorem** — Decompositions of a group into indecomposable factors are unique up to isomorphism.
- **Feit–Thompson theorem (odd order theorem)** (*Walter Feit and John Thompson, 1963*) — Every group of odd order is solvable. Its proof, at 255 pages, launched the classification of finite simple groups.
- **Schur–Zassenhaus theorem** — Every normal Hall subgroup has a complement; all complements are conjugate.
- **Structure theorem for finitely generated abelian groups** — Every f.g. abelian group is isomorphic to ℤⁿ ⊕ ℤ/d₁ ⊕ ... ⊕ ℤ/dₖ with d_i | d_{i+1}.
- **Frattini's argument** — If G has a normal subgroup H with Sylow p-subgroup P, then G = H · N_G(P).
- **Jordan's theorem on finite linear groups** (*Jordan, 1878*) — A finite subgroup of GL_n(ℂ) has an abelian normal subgroup of bounded index.
- **Burnside's p^a q^b theorem** (*William Burnside, 1904*) — Every group of order p^a q^b is solvable. The original impetus to classify finite simple groups.
- **Higman–Neumann–Neumann theorem** — Every countable group embeds in a 2-generator group.

## Representation Theory

- **Maschke's theorem** (*Heinrich Maschke, 1899*) — A representation of a finite group G over a field k with char k ∤ |G| is completely reducible.
- **Schur's lemma** (*Issai Schur, 1905*) — A morphism between irreducible representations is either zero or an isomorphism; over ℂ, an intertwiner of an irrep with itself is a scalar.
- **Wedderburn's theorem (finite division rings)** (*Joseph Wedderburn, 1905*) — Every finite division ring is a field. (Surprising, since division rings like quaternions exist.)
- **Artin–Wedderburn theorem** — Every semisimple ring is a finite product of matrix rings over division rings.
- **Peter–Weyl theorem** (*1927*) — L²(G) for compact G decomposes as a Hilbert direct sum over irreducible unitary representations. Foundation of non-abelian Fourier analysis.
- **Frobenius reciprocity** — Induction and restriction of representations are adjoint functors.

## Topology (General and Algebraic)

- **Heine–Borel theorem** (*Heine 1872, Borel 1895*) — A subset of ℝⁿ is compact iff it is closed and bounded.
- **Urysohn's lemma** (*Pavel Urysohn, 1925*) — In a normal Hausdorff space, disjoint closed sets can be separated by a continuous function.
- **Tietze extension theorem** (*Heinrich Tietze, 1915*) — Continuous real-valued functions on closed subsets of normal spaces extend to the whole space.
- **Urysohn metrization theorem** (*Urysohn, 1925*) — A second-countable regular Hausdorff space is metrizable.
- **Alexandroff compactification (one-point)** — Every locally compact Hausdorff space embeds in a compact Hausdorff space by adding one point at infinity.
- **Borsuk–Ulam theorem** (*Karol Borsuk, 1933*) — Any continuous map Sⁿ → ℝⁿ sends some antipodal pair to the same point. Implications for fair division, algorithms.
- **Ham sandwich theorem** (*Stone and Tukey, 1942*) — Given n measurable objects in ℝⁿ, a single hyperplane can bisect all of them simultaneously.
- **Jordan curve theorem** (*Camille Jordan 1887, proofs refined*) — A simple closed curve in the plane divides it into an interior and exterior.
- **Hairy ball theorem** (*Poincaré 1885, Brouwer 1912*) — Every continuous tangent vector field on S² has a zero. "You can't comb a hairy ball flat."
- **Poincaré–Hopf theorem** — On a compact manifold, the sum of indices of a vector field's zeros equals the Euler characteristic.
- **Brouwer's invariance of domain** (*Brouwer, 1912*) — Open subsets of ℝⁿ stay open under continuous injections. Implies ℝⁿ ≇ ℝᵐ for n ≠ m.
- **de Rham's theorem** (*Georges de Rham, 1931*) — De Rham cohomology = singular cohomology with real coefficients, on smooth manifolds.
- **Whitney embedding theorem** (*Hassler Whitney, 1944*) — Every smooth n-manifold embeds in ℝ^(2n).
- **Nash embedding theorem** (*John Nash, 1954/1956*) — Every Riemannian manifold embeds isometrically in Euclidean space. Pioneered the h-principle techniques.
- **Mostow rigidity theorem** (*George Mostow, 1968*) — Hyperbolic structures on closed manifolds of dim ≥ 3 are unique up to isometry.
- **Thurston's geometrization theorem** (*Thurston conjecture 1982, proved via Perelman 2003*) — Every closed 3-manifold decomposes into pieces of 8 canonical geometries. Implies Poincaré.
- **Smale's h-cobordism theorem** (*Stephen Smale, 1962*) — An h-cobordism between simply-connected manifolds of dim ≥ 5 is a cylinder. Proved higher-dimensional Poincaré.
- **Freedman's theorem** (*Michael Freedman, 1982*) — Topological 4-manifolds are classified by intersection form. Solved topological Poincaré in dim 4. Fields Medal.
- **Donaldson's theorem** (*Simon Donaldson, 1983*) — Smooth 4-manifold intersection forms are extremely restricted. Implies exotic ℝ⁴s exist.
- **Alexander duality** (*James Alexander, 1915*) — Relates homology of a subspace of Sⁿ to that of its complement.
- **Poincaré duality** — On a closed oriented n-manifold, Hᵏ ≅ H_{n−k}.

## Differential Geometry

- **Hopf–Rinow theorem** (*Heinz Hopf and Willi Rinow, 1931*) — A connected Riemannian manifold is geodesically complete iff it is metrically complete. Any two points are joined by a minimizing geodesic.
- **Cartan–Hadamard theorem** — A complete simply-connected Riemannian manifold of nonpositive curvature is diffeomorphic to ℝⁿ via the exponential map.
- **Myers's theorem** (*Sumner Myers, 1941*) — A Riemannian manifold with Ricci curvature bounded below by a positive constant is compact.
- **Hodge theorem** (*W.V.D. Hodge, 1941*) — On a compact Riemannian manifold, each de Rham cohomology class has a unique harmonic representative.
- **Chern–Gauss–Bonnet theorem** (*Shiing-Shen Chern, 1944*) — Generalizes Gauss–Bonnet to even-dim Riemannian manifolds: integral of the Pfaffian of curvature equals Euler characteristic.
- **Uniformization theorem** (*Koebe and Poincaré, 1907*) — Every simply-connected Riemann surface is conformally equivalent to ℂ, ĉ (sphere), or the disk. Unifies the three geometries.

## Real Analysis / Measure Theory

- **Monotone convergence theorem** (*Lebesgue, 1904*) — For nonneg measurable fₙ ↑ f, ∫fₙ ↑ ∫f.
- **Fatou's lemma** (*Pierre Fatou, 1906*) — ∫lim inf fₙ ≤ lim inf ∫fₙ for nonneg measurable fₙ.
- **Dominated convergence theorem** (*Lebesgue*) — If |fₙ| ≤ g (integrable) and fₙ → f pointwise, then ∫fₙ → ∫f.
- **Fubini's theorem** (*Guido Fubini, 1907*) — For integrable f, iterated integrals equal the product integral.
- **Tonelli's theorem** (*Leonida Tonelli, 1909*) — Fubini for nonnegative measurable f, without integrability hypothesis.
- **Radon–Nikodym theorem** (*Radon 1913, Nikodym 1930*) — An absolutely continuous signed measure has a density (Radon–Nikodym derivative).
- **Lebesgue differentiation theorem** — f'(x) = lim_{r→0} (1/|B_r|)∫_{B_r} f a.e. for locally integrable f.
- **Vitali covering lemma** (*Giuseppe Vitali, 1908*) — A disjoint subcollection of a Vitali cover, tripled in radius, still covers.
- **Egorov's theorem** (*Dmitri Egorov, 1911*) — Pointwise a.e. convergence on a finite measure space is uniform convergence off a set of arbitrarily small measure.
- **Lusin's theorem** (*Nikolai Lusin, 1912*) — A measurable function is continuous on the complement of a small set. (Measurable ≈ continuous.)
- **Rademacher's theorem** (*Hans Rademacher, 1919*) — Lipschitz functions on ℝⁿ are differentiable a.e.
- **Sard's theorem** (*Arthur Sard, 1942*) — The image of the critical set of a smooth map has measure zero.
- **Baire category theorem** (*René-Louis Baire, 1899*) — A complete metric space is not a countable union of nowhere-dense sets.
- **Arzelà–Ascoli theorem** (*Giulio Ascoli 1883, Cesare Arzelà 1895*) — A pointwise bounded, equicontinuous family of continuous functions on a compact set has a uniformly convergent subsequence.

## Complex Analysis

- **Picard's little theorem** (*Émile Picard, 1879*) — A non-constant entire function takes every complex value with at most one exception.
- **Picard's great theorem** — Near an essential singularity, a function takes every value infinitely often, with one possible exception.
- **Casorati–Weierstrass theorem** — Near an essential singularity, a function comes arbitrarily close to every value.
- **Residue theorem** (*Cauchy, 1826*) — Contour integral = 2πi × sum of residues inside. Workhorse of complex analysis.
- **Argument principle** (*Cauchy*) — ∮ f'/f = 2πi(#zeros − #poles) inside a contour.
- **Rouché's theorem** (*Eugène Rouché, 1862*) — If |f − g| < |g| on a contour, f and g have the same number of zeros inside.
- **Morera's theorem** (*Giacinto Morera, 1886*) — Converse of Cauchy: if ∮f = 0 on every closed contour, f is holomorphic.
- **Schwarz lemma** (*Hermann Schwarz*) — A holomorphic self-map of the unit disk fixing 0 satisfies |f(z)| ≤ |z|; equality implies f is a rotation.
- **Phragmén–Lindelöf principle** — Maximum modulus principle extended to unbounded regions under growth conditions.
- **Mittag-Leffler theorem** (*Gösta Mittag-Leffler, 1876*) — One can construct meromorphic functions with prescribed poles and principal parts.
- **Weierstrass factorization theorem** (*Weierstrass, 1876*) — Every entire function factors as a product over its zeros × an exponential factor.
- **Montel's theorem** (*Paul Montel, 1907*) — A locally uniformly bounded family of holomorphic functions is normal (has convergent subsequences).
- **Hurwitz's theorem** (*Adolf Hurwitz, 1889*) — If holomorphic fₙ → f uniformly on compacts, the zeros of f are limits of zeros of fₙ.
- **Bloch's theorem** (*André Bloch, 1924*) — A holomorphic function on the unit disk with f'(0) = 1 covers a disk of universal radius.
- **Gauss–Lucas theorem** — The zeros of f' lie in the convex hull of the zeros of f.

## Functional Analysis

- **Banach–Steinhaus theorem / uniform boundedness principle** (*Banach and Hugo Steinhaus, 1927*) — A family of bounded operators on a Banach space that is pointwise bounded is uniformly bounded.
- **Open mapping theorem** (*Banach, 1929*) — A surjective bounded operator between Banach spaces is open.
- **Closed graph theorem** (*Banach, 1932*) — A linear map between Banach spaces is continuous iff its graph is closed.
- **Banach–Alaoglu theorem** (*Banach 1932, Alaoglu 1940*) — The closed unit ball of X* is weak-* compact.
- **Kreĭn–Milman theorem** (*1940*) — A compact convex set in a locally convex space is the closed convex hull of its extreme points.
- **Riesz representation theorems** — Multiple: continuous linear functionals on C(K) are signed measures; on L^p (1 < p < ∞) are integration against L^q functions; on Hilbert spaces are inner products.
- **Spectral theorem for self-adjoint operators** (*Hilbert, von Neumann*) — A self-adjoint operator on a Hilbert space is unitarily equivalent to multiplication by a real function on some measure space.
- **Gelfand–Naimark theorem** (*1943*) — Every commutative C*-algebra is isomorphic to C₀(X) for a locally compact Hausdorff X. Foundation of non-commutative geometry.
- **Lax–Milgram lemma** (*Peter Lax and Arthur Milgram, 1954*) — A bilinear form that is bounded and coercive on a Hilbert space gives rise to an isomorphism. Foundation of finite element methods.
- **Sobolev embedding theorem** (*Sergei Sobolev, 1938*) — Sobolev spaces embed into continuous function spaces or L^p spaces depending on the indices.
- **Rellich–Kondrachov theorem** — Sobolev embeddings are compact under appropriate indices. Key to PDE existence theory.
- **Stone's theorem on one-parameter unitary groups** (*Marshall Stone, 1930*) — Continuous one-parameter unitary groups are generated by self-adjoint operators. Mathematical basis of the Schrödinger equation.
- **Riesz–Fischer theorem** — L² is complete; Fourier coefficients converge in L² iff their square-sum is finite.

## Harmonic Analysis

- **Plancherel theorem** (*Michel Plancherel, 1910*) — The Fourier transform is an isometry of L²(ℝⁿ).
- **Riesz–Thorin interpolation theorem** (*Marcel Riesz 1927, Olof Thorin 1948*) — Interpolates L^p bounds for operators in a convex manner.
- **Marcinkiewicz interpolation theorem** (*Józef Marcinkiewicz, 1939*) — Weak-type interpolation result, broader than Riesz–Thorin.
- **Carleson's theorem** (*Lennart Carleson, 1966*) — Fourier series of L² functions converge almost everywhere. Answered an old question of Luzin.
- **Hardy–Littlewood maximal inequality** — Bounds the L^p norm of the maximal function in terms of the original.

## Differential Equations

- **Picard–Lindelöf theorem** (*Picard 1890, Lindelöf 1894*) — Lipschitz ODEs have unique local solutions. Foundational existence/uniqueness.
- **Peano existence theorem** (*Giuseppe Peano, 1886*) — Continuous ODEs have local solutions (but not necessarily unique).
- **Cauchy–Kovalevskaya theorem** (*Cauchy 1842, Kovalevskaya 1875*) — Analytic Cauchy problems for PDEs have local analytic solutions. Sofia Kovalevskaya's doctoral work.
- **Frobenius theorem** (*Ferdinand Frobenius, 1877*) — A distribution of tangent subspaces is integrable iff it is involutive.
- **Poincaré–Bendixson theorem** (*Poincaré 1892, Bendixson 1901*) — In 2D continuous dynamical systems, bounded orbits limit to equilibria or periodic orbits. No chaos in 2D.
- **Hartman–Grobman theorem** (*Philip Hartman and David Grobman, 1960*) — Near a hyperbolic equilibrium, a nonlinear system is topologically conjugate to its linearization.
- **KAM theorem** (*Kolmogorov 1954, Arnold 1963, Moser 1962*) — Most quasiperiodic motions of integrable Hamiltonian systems persist under small perturbations.

## Probability

- **Kolmogorov's 0–1 law** (*Andrey Kolmogorov, 1933*) — A tail event of independent random variables has probability 0 or 1.
- **Kolmogorov's extension theorem** — Consistent finite-dimensional distributions define a stochastic process on a product measure space.
- **Borel–Cantelli lemma** — If Σ P(Aₙ) < ∞, then P(Aₙ i.o.) = 0; conversely for independent Aₙ, if Σ = ∞ then P = 1.
- **Doob's martingale convergence theorem** (*Joseph Doob, 1940*) — A bounded martingale converges a.s.
- **Doob's optional stopping theorem** — Martingale property extends to bounded stopping times under mild conditions.
- **Itô's lemma** (*Kiyoshi Itô, 1944*) — Stochastic change-of-variable formula; the product rule of stochastic calculus.
- **Feynman–Kac formula** — Links PDEs of parabolic type to expectations of Wiener-process functionals.
- **Girsanov's theorem** (*Igor Girsanov, 1960*) — Change of measure for Brownian motion with drift. Foundation of mathematical finance.
- **Glivenko–Cantelli theorem** — The empirical distribution function converges uniformly to the true distribution almost surely.
- **Donsker's theorem** (*Monroe Donsker, 1952*) — Functional central limit theorem: rescaled random walks converge in distribution to Brownian motion.
- **Lindeberg–Feller central limit theorem** — Generalization of CLT to independent but not identically distributed variables.

## Dynamical Systems (Extra)

- **Sharkovskii's theorem** (*Oleksandr Sharkovskii, 1964*) — For continuous maps of an interval, a period-3 orbit implies all periods exist (in a specific ordering). Period-3 implies chaos.
- **Birkhoff ergodic theorem** — Time averages equal space averages for ergodic measure-preserving transformations.
- **Oseledets multiplicative ergodic theorem** (*Valery Oseledets, 1965*) — Foundation of Lyapunov exponents theory.

## Category Theory

- **Yoneda lemma** (*Nobuo Yoneda, 1954*) — Nat(Hom(−,A), F) ≅ F(A). "An object is determined by its outgoing morphisms." One of the most important theorems in category theory despite its apparent simplicity.
- **Adjoint functor theorem** (*Peter Freyd*) — A functor has a left adjoint iff it preserves small limits and satisfies a solution-set condition.

## Computer Science / Computability and Complexity

- **Rice's theorem** (*Henry Gordon Rice, 1953*) — Any nontrivial semantic property of programs is undecidable. Extends Turing's halting problem.
- **Cook–Levin theorem** (*Stephen Cook 1971, Leonid Levin 1973*) — SAT is NP-complete. Founded NP-completeness theory.
- **Time hierarchy theorem** (*Hartmanis and Stearns, 1965*) — More time gives strictly more computational power. Founded complexity theory.
- **Space hierarchy theorem** — Analog for space.
- **Ladner's theorem** (*Richard Ladner, 1975*) — If P ≠ NP, then NP-intermediate problems exist.
- **Immerman–Szelepcsényi theorem** (*1987–88*) — Nondeterministic space classes are closed under complement. NL = coNL.
- **PCP theorem** (*Arora, Safra, Lund, Motwani, Sudan, Szegedy, 1990s*) — Every NP proof can be probabilistically checked by examining a constant number of bits. Basis of hardness-of-approximation theory.
- **Gödel speed-up theorem** (*Gödel 1936*) — Stronger theories admit exponentially shorter proofs for the same statements.
- **Savitch's theorem** (*Walter Savitch, 1970*) — NSPACE(s) ⊆ DSPACE(s²).

## Information Theory

- **Shannon's source coding theorem** (*Claude Shannon, 1948*) — Entropy is the minimum expected codeword length for lossless compression.
- **Shannon's noisy-channel coding theorem** (*Shannon, 1948*) — Reliable communication is possible up to the channel capacity. Founded information theory.
- **Shannon–Hartley theorem** — C = B log₂(1 + S/N). Relates bandwidth, signal, noise to channel capacity.
- **Kraft's inequality** — A prefix-free code exists with given codeword lengths iff Σ 2^(−ℓᵢ) ≤ 1.

## Mathematical Physics

- **CPT theorem** (*Lüders and Pauli, ca. 1954–55*) — Any Lorentz-invariant quantum field theory is invariant under combined charge, parity, and time reversal.
- **Spin-statistics theorem** (*Pauli, 1940*) — Particles with integer spin are bosons; half-integer spin are fermions.
- **Haag's theorem** (*Rudolf Haag, 1955*) — The interaction picture does not exist in relativistic QFT. A technical obstruction to naive formulations.
- **Noether's second theorem** — A gauge symmetry implies a set of constraints among Euler–Lagrange equations.
- **Reeh–Schlieder theorem** (*1961*) — In QFT, the vacuum is cyclic for local observables: any state can be approximated by local perturbations of the vacuum.
- **Bell's theorem** (*John Bell, 1964*) — Quantum mechanics cannot be reproduced by local hidden variable theories.
- **Kochen–Specker theorem** (*1967*) — Context-independent hidden variables cannot reproduce quantum predictions in dim ≥ 3.

## Game Theory / Economics (mathematical)

- **Von Neumann's minimax theorem** (*John von Neumann, 1928*) — Two-player zero-sum games have a value; optimal mixed strategies exist.
- **Nash's existence theorem** (*John Nash, 1950*) — Every finite game has a mixed-strategy equilibrium. One-page proof via Kakutani's fixed-point theorem.
- **Arrow's impossibility theorem** (*Kenneth Arrow, 1951*) — No social welfare function with ≥ 3 alternatives satisfies unanimity, IIA, non-dictatorship together.
- **Gibbard–Satterthwaite theorem** (*1973/1975*) — Every non-dictatorial voting rule with ≥ 3 alternatives is manipulable.

---

## Closing note

This catalog is not exhaustive — mathematics generates new named theorems faster than any reference can absorb. The authoritative database **zbMATH Open** indexes millions of results. But these ~300 supplement the deep-dive chapters with the proper names most working mathematicians recognize. Cross-reference the [INDEX](INDEX.md) to find deeper treatments of the flagship theorems.
