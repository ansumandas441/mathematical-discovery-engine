# Walters, *An Introduction to Ergodic Theory* (Springer GTM 79, 1982) — Extraction Candidates

Flat list grouped by chapter. Each item: **name** — *kind* — description — (deps).
Kinds: axiom (definition/structure) | state (derived object/construction) | theorem (proved named result) | technique (proof method/transform).

## Chapter 0 — Preliminaries

1. **Measure space / probability space (X, B, m)** — axiom — A set X with a σ-algebra B and a (probability) measure m; the basic stage for ergodic theory. — (set theory, σ-algebra).
2. **Lebesgue space (Lebesgue space mod 0)** — axiom — A measure space isomorphic mod null sets to an interval plus countably many atoms; the standard regularity hypothesis. — (measure space, isomorphism mod 0).
3. **L^p spaces and the spaces L^p(m)** — state — Banach spaces of p-integrable functions modulo null functions; L^2 is a Hilbert space. — (measure space, integration).
4. **Conditional expectation E(f | A)** — state — The unique A-measurable function equal to f in integral over every A-set; orthogonal projection onto L^2(A) when p=2. — (sub-σ-algebra A, Radon–Nikodym).
5. **Conditional expectation properties (tower, positivity, contraction)** — theorem — E(E(f|A)|C)=E(f|C) for C⊂A, monotone, and an L^1/L^p contraction. — (conditional expectation).
6. **Radon–Nikodym theorem** — theorem — An absolutely continuous measure has a density (derivative) w.r.t. the dominating measure. — (σ-finite measures, absolute continuity).
7. **Monotone class / approximation by algebra** — technique — Sets in B are approximated in measure by an algebra generating B; reduces proofs to a generating semi-algebra. — (σ-algebra, measure).

## Chapter 1 — Measure-Preserving Transformations

8. **Measure-preserving transformation (T)** — axiom — A measurable map T:X→X with m(T^{-1}E)=m(E) for all measurable E. — (measure space).
9. **Invertible measure-preserving transformation** — axiom — A bijective m.p.t. whose inverse is also measurable and measure-preserving. — (m.p.t.).
10. **Criterion for measure preservation on a semi-algebra** — theorem — T is m.p. iff m(T^{-1}E)=m(E) on a generating semi-algebra. — (m.p.t., semi-algebra, approximation).
11. **Rotation of the circle (T(x)=x+a)** — state — Rotation of the unit circle / [0,1) preserving Lebesgue/Haar measure. — (compact group, Haar measure).
12. **Group rotation / translation on a compact group** — state — T(x)=ax on a compact group G preserving Haar measure. — (compact group, Haar measure).
13. **Endomorphism/automorphism of a compact group** — state — A continuous (surjective) homomorphism of a compact group, preserving Haar measure. — (compact group, Haar measure).
14. **Endomorphism/automorphism of the torus (matrix A ∈ GL_n(ℤ))** — state — T(x)=Ax mod 1 on 𝕋^n with integer matrix A of determinant ±1 (automorphism) preserving Lebesgue measure. — (torus, integer matrix).
15. **Bernoulli shift** — state — Two-sided/one-sided shift on a product probability space (p_0,…,p_{k-1})^ℤ with the product measure. — (product measure, shift).
16. **Markov shift** — state — Shift on sequence space with measure from a stochastic matrix P and invariant probability vector p (pP=p). — (stochastic matrix, stationary vector).
17. **(Two-sided) shift map σ** — axiom — The coordinate shift on a sequence space, preserving any shift-invariant measure. — (sequence space).
18. **Gauss map / continued fraction transformation T(x)={1/x}** — state — The map on [0,1) preserving the Gauss measure dm = (1/ln2)·dx/(1+x). — (interval, Gauss measure).
19. **Gauss measure** — axiom — The T-invariant probability (1/ln2)·dx/(1+x) for the Gauss map. — (Gauss map).
20. **Poincaré recurrence theorem** — theorem — For a m.p.t. and a set E of positive measure, almost every point of E returns to E infinitely often. — (m.p.t., finite measure).
21. **Induced (first-return) transformation T_A** — state — On a set A of positive measure, T_A(x)=T^{n(x)}(x) with n(x) the first return time; it is m.p. for the normalized restriction. — (m.p.t., Poincaré recurrence, return-time function).
22. **First return-time function n_A(x)** — state — The least n≥1 with T^n x ∈ A; integrable with integral ≤ 1 (Kac's lemma). — (induced transformation).
23. **Kac's lemma** — theorem — The integral of the first-return time over A equals m(∪ of the tower) (=1 if T ergodic); average return time = 1/m(A). — (induced transformation, ergodicity).
24. **Rokhlin (Kakutani–Rokhlin) lemma** — theorem — For aperiodic invertible m.p.t., given n and ε there is a set F with F,TF,…,T^{n-1}F disjoint and complement of measure < ε. — (aperiodic m.p.t., Lebesgue space).
25. **Tower / skyscraper construction** — technique — Building a transformation from a base map and a height/return function (Kakutani towers). — (induced transformation).

## Chapter 2 — Isomorphism, Conjugacy, Spectral Isomorphism

26. **Conjugacy (point isomorphism) of m.p.t.'s** — axiom — An invertible m.p. map φ with φ∘T₁ = T₂∘φ a.e. intertwining two systems. — (m.p.t., measure isomorphism).
27. **Isomorphism mod 0 (measure-theoretic isomorphism)** — axiom — Conjugacy after deleting invariant null sets; the basic equivalence of ergodic theory. — (conjugacy).
28. **Measure-algebra isomorphism / conjugacy of measure algebras** — axiom — A measure-preserving Boolean isomorphism of the measure algebras commuting with the induced maps. — (measure algebra).
29. **Koopman operator / associated unitary operator U_T** — state — The isometry (U_T f)=f∘T on L²(m), unitary when T is invertible. — (m.p.t., L²).
30. **Spectral isomorphism (unitary equivalence of U_T)** — axiom — Existence of a unitary W with W U_{T₁} = U_{T₂} W; weaker than isomorphism. — (Koopman operator).
31. **Spectral invariant** — state — Any property of U_T invariant under unitary equivalence (e.g. eigenvalues, mixing). — (Koopman operator).
32. **Point spectrum / eigenvalues and eigenfunctions of U_T** — state — λ∈ℂ with f∘T = λ f a.e. for nonzero f; eigenvalues form a subgroup of the circle. — (Koopman operator).
33. **Eigenvalues have modulus 1; eigenfunctions have constant modulus** — theorem — For ergodic T, |λ|=1 and |f| is constant a.e.; eigenfunctions for distinct eigenvalues are orthogonal. — (Koopman operator, ergodicity).
34. **Conjugacy implies spectral isomorphism** — theorem — Isomorphic systems are spectrally isomorphic (converse false). — (conjugacy, Koopman operator).

## Chapter 3 — Measure-Theoretic Recurrence / Ergodicity Setup

35. **Invariant set / invariant function** — axiom — A set E with T^{-1}E = E (mod 0), or a function with f∘T = f a.e. — (m.p.t.).
36. **Ergodicity** — axiom — Every invariant set has measure 0 or 1 (equivalently invariant functions are constant a.e.). — (invariant set).
37. **Equivalent characterizations of ergodicity** — theorem — Ergodic iff invariant functions constant a.e. iff for all A,B (1/n)Σ m(T^{-i}A∩B)→m(A)m(B). — (ergodicity, averages).
38. **Ergodicity of rotations** — theorem — A rotation by a is ergodic iff a is irrational (iff a generates a dense subgroup). — (rotation, ergodicity).
39. **Ergodicity of group rotations** — theorem — Rotation by a on compact group G is ergodic iff {aⁿ} is dense in G. — (group rotation, ergodicity).
40. **Ergodicity of toral automorphisms** — theorem — A toral endomorphism A is ergodic iff no eigenvalue of A is a root of unity. — (toral automorphism, characters, ergodicity).
41. **Ergodicity / mixing of Bernoulli and Markov shifts** — theorem — Bernoulli shifts are strong-mixing; a Markov shift is ergodic iff the matrix is irreducible. — (shift, stochastic matrix).
42. **Character / Fourier analysis technique on groups** — technique — Using characters (Fourier coefficients) of a compact abelian group to test invariance under T. — (compact abelian group, Pontryagin duality).

## Chapter 4 — The Ergodic Theorems

43. **von Neumann mean ergodic theorem** — theorem — For an isometry U on a Hilbert space, the averages (1/n)Σ U^i f converge in norm to the projection of f onto the U-invariant subspace. — (Hilbert space, isometry).
44. **Birkhoff pointwise ergodic theorem** — theorem — For f∈L¹, (1/n)Σ f(T^i x) converges a.e. to an invariant f*; if ergodic, f* = ∫f dm. — (m.p.t., L¹, maximal ergodic theorem).
45. **Maximal ergodic theorem / maximal inequality** — theorem — ∫_{E_N} f dm ≥ 0 where E_N is the set where some average of partial sums is positive. — (m.p.t., integrable function).
46. **Birkhoff averages / time average vs. space average** — state — A_n f = (1/n)Σ_{i<n} f∘T^i; ergodicity ⇔ time average = space average a.e. — (ergodic theorem).
47. **Hopf / Garsia maximal-function argument** — technique — Proving the maximal inequality via a max of partial sums and a clever telescoping. — (maximal ergodic theorem).
48. **L^p mean ergodic theorem** — theorem — Birkhoff averages converge in L^p (1≤p<∞) for f∈L^p. — (ergodic theorem, L^p).
49. **Normal numbers / Borel's theorem (via ergodicity)** — theorem — Almost every real number is normal to every base, as an application of Birkhoff. — (Birkhoff theorem, shift).

## Chapter 5 — Mixing

50. **Weak-mixing** — axiom — (1/n)Σ |m(T^{-i}A∩B) − m(A)m(B)| → 0 for all A,B. — (m.p.t.).
51. **Strong-mixing** — axiom — m(T^{-n}A∩B) → m(A)m(B) for all A,B. — (m.p.t.).
52. **Hierarchy: strong-mixing ⇒ weak-mixing ⇒ ergodic** — theorem — Implications among mixing notions, all strict. — (mixing definitions).
53. **Weak-mixing ⇔ no nonconstant eigenfunctions (continuous spectrum)** — theorem — T weak-mixing iff 1 is the only eigenvalue of U_T and is simple. — (weak-mixing, point spectrum).
54. **Weak-mixing ⇔ T×T ergodic ⇔ T×T weak-mixing** — theorem — Product characterization of weak-mixing. — (weak-mixing, product transformation).
55. **Weak-mixing of all powers** — theorem — T weak-mixing iff Tⁿ ergodic for all n≥1; all powers are weak-mixing. — (weak-mixing).
56. **Convergence in density / sets of density zero** — technique — Cesàro-average condition recast as convergence along a density-1 subsequence (Koopman–von Neumann lemma). — (density, weak-mixing).
57. **Koopman–von Neumann lemma** — theorem — A bounded sequence Cesàro-averages to 0 in absolute value iff it tends to 0 along a set of density 1. — (density).
58. **Spectral characterization via the maximal spectral measure** — theorem — Mixing properties of T expressed through the spectral measures of U_T (continuous vs. atomic). — (Koopman operator, spectral measure).

## Chapter 6 — Discrete Spectrum / Spectral Theory

59. **Discrete (pure point) spectrum** — axiom — L²(m) is spanned by eigenfunctions of U_T. — (point spectrum).
60. **Ergodic + discrete spectrum ⇒ eigenvalues simple, form a group** — theorem — For ergodic T the eigenvalues form a subgroup of the circle and each is simple. — (discrete spectrum, ergodicity).
61. **Halmos–von Neumann theorem** — theorem — An ergodic m.p.t. with discrete spectrum is conjugate to an ergodic rotation on a compact abelian group (determined up to conjugacy by its eigenvalue group). — (discrete spectrum, group rotation, character theory).
62. **Discrete spectrum ⇒ spectral isomorphism = conjugacy** — theorem — For discrete-spectrum systems, spectral isomorphism implies conjugacy (eigenvalues are a complete invariant). — (Halmos–von Neumann, spectral isomorphism).
63. **Group rotation as model** — state — The canonical realization of a discrete-spectrum system as rotation on the dual group of the eigenvalue group. — (Halmos–von Neumann, Pontryagin duality).
64. **Eigenvalue group as complete conjugacy invariant** — state — The subgroup of the circle of eigenvalues classifies ergodic discrete-spectrum systems. — (Halmos–von Neumann).

## Chapter 7 — Entropy

65. **Partition (finite/countable measurable partition ξ)** — axiom — A collection of disjoint measurable sets covering X mod 0. — (measure space).
66. **Entropy of a partition H(ξ)** — state — H(ξ) = −Σ m(A) log m(A) over atoms A of ξ. — (partition).
67. **Join of partitions ξ ∨ η** — state — The partition by intersections of atoms; refinement operation. — (partition).
68. **Conditional entropy H(ξ | η)** — state — Average uncertainty of ξ given η: −Σ m(A∩B) log(m(A∩B)/m(B)). — (partition, conditional expectation).
69. **Basic entropy (in)equalities** — theorem — Subadditivity H(ξ∨η)≤H(ξ)+H(η); monotonicity; H(ξ∨η)=H(η)+H(ξ|η); concavity. — (entropy, conditional entropy).
70. **Entropy of a transformation w.r.t. a partition h(T,ξ)** — state — lim (1/n) H(⋁_{i=0}^{n-1} T^{-i}ξ); the limit exists by subadditivity. — (partition, m.p.t., subadditive limit).
71. **Subadditive sequence limit lemma (Fekete)** — technique — A subadditive sequence a_{m+n}≤a_m+a_n has lim a_n/n = inf a_n/n. — (subadditivity).
72. **Entropy of a transformation h(T)** — state — sup over finite partitions of h(T,ξ); an isomorphism invariant. — (h(T,ξ)).
73. **Properties of h(T): h(T^k)=k·h(T), h(T^{-1})=h(T)** — theorem — Behaviour of entropy under powers and inverses. — (entropy).
74. **Kolmogorov–Sinai theorem (generators)** — theorem — If ξ is a generator (⋁ T^{-i}ξ = B mod 0 / two-sided for invertible) then h(T)=h(T,ξ). — (generator, entropy).
75. **Generator (one-sided / two-sided)** — axiom — A partition whose iterated joins generate the full σ-algebra mod 0. — (partition, σ-algebra).
76. **Krieger generator theorem** — theorem — An ergodic invertible T with h(T)<∞ has a finite generator (with at most e^{h(T)}+1 atoms). — (entropy, generator, ergodicity).
77. **Entropy of Bernoulli shift** — theorem — h(σ) = −Σ p_i log p_i for the (p_0,…,p_{k-1}) Bernoulli shift. — (Bernoulli shift, Kolmogorov–Sinai).
78. **Entropy of Markov shift** — theorem — h(σ) = −Σ_{i,j} p_i P_{ij} log P_{ij}. — (Markov shift, Kolmogorov–Sinai).
79. **Entropy of an automorphism of the torus** — theorem — h(A) = Σ_{|λ_i|>1} log|λ_i| (sum of logs of eigenvalues of modulus > 1). — (toral automorphism, generators).
80. **Bernoulli shifts with different entropy are non-isomorphic** — theorem — Entropy distinguishes Bernoulli shifts (e.g. (1/2,1/2) vs (1/3,1/3,1/3)). — (entropy invariance).
81. **Shannon–McMillan–Breiman theorem** — theorem — For ergodic T, −(1/n) log m(ξⁿ(x)) → h(T,ξ) a.e. and in L¹, where ξⁿ is the n-fold join atom of x. — (entropy, Birkhoff theorem, martingale convergence).
82. **Pinsker σ-algebra / Pinsker partition** — state — The largest sub-σ-algebra on which T has zero entropy. — (entropy, sub-σ-algebra).
83. **K-system (Kolmogorov automorphism)** — axiom — A system with a partition whose past generates a σ-algebra with trivial tail (positive entropy of every nontrivial partition). — (entropy, generator).
84. **K-system ⇒ strong-mixing (of all orders)** — theorem — Kolmogorov systems are mixing of all orders. — (K-system, mixing).
85. **Abramov's formula** — theorem — For the induced transformation T_A: h(T_A) = h(T)/m(A). — (induced transformation, entropy, Kac's lemma).
86. **Entropy of induced/integral transformations** — theorem — Relation of h between a tower (integral transformation) and its base (companion to Abramov). — (tower, entropy).
87. **Conditional entropy continuity / Rokhlin metric d(ξ,η)** — technique — The partition metric d(ξ,η)=H(ξ|η)+H(η|ξ) making entropy continuous. — (conditional entropy).

## Chapter 8 — Topological Dynamics

88. **Topological dynamical system (X,T) with X compact metric** — axiom — A continuous map T of a compact metric space. — (compact metric space, continuity).
89. **Topological transitivity** — axiom — Existence of a dense orbit, equivalently every pair of open sets is connected by an iterate. — (topological system).
90. **Minimality / minimal set** — axiom — Every orbit is dense; no proper closed invariant subset. — (topological system).
91. **Existence of minimal sets (Zorn)** — theorem — Every compact system contains a minimal closed invariant set. — (compactness, Zorn's lemma).
92. **Topological entropy via open covers (Adler–Konheim–McAndrew)** — state — h_top(T)=sup_𝒰 lim (1/n) log N(⋁ T^{-i}𝒰), where N is the minimal subcover cardinality. — (open covers, subadditive limit).
93. **Separated set / (n,ε)-separated set** — state — A set whose points are pairwise distinguished within ε over n iterates; s(n,ε) its max cardinality. — (metric, T).
94. **Spanning set / (n,ε)-spanning set** — state — A set that ε-approximates every orbit over n steps; r(n,ε) its min cardinality. — (metric, T).
95. **Bowen–Dinaburg topological entropy** — theorem — h_top(T)=lim_{ε→0} limsup (1/n) log s(n,ε) = …log r(n,ε); equals the open-cover entropy. — (separated/spanning sets).
96. **Bowen metric d_n** — state — d_n(x,y)=max_{0≤i<n} d(T^i x, T^i y); the dynamical metric defining separated/spanning sets. — (metric, T).
97. **Topological entropy of examples** — theorem — Computations: identity has 0, full shift on k symbols has log k, toral automorphism Σ log|λ_i| (|λ_i|>1). — (topological entropy).
98. **Equicontinuity / distal systems** — axiom — Systems whose iterates form an equicontinuous (or distal) family; have zero topological entropy. — (topological system).

## Chapter 9 — Invariant Measures for Continuous Transformations

99. **Space M(X) of Borel probability measures** — state — Compact convex set of probabilities on X with the weak* topology. — (compact metric space, Riesz representation).
100. **Space M(X,T) of T-invariant probabilities** — state — Nonempty compact convex subset of M(X) of T-invariant measures. — (M(X), invariance).
101. **Krylov–Bogolyubov existence theorem** — theorem — For continuous T on compact metric X, M(X,T) is nonempty (weak* limits of (1/n)Σ T^i_*δ_x are invariant). — (M(X), compactness, weak* limits).
102. **Ergodic measures = extreme points of M(X,T)** — theorem — The ergodic invariant measures are exactly the extreme points; M(X,T) is a Choquet simplex. — (M(X,T), extreme points).
103. **Ergodic decomposition** — theorem — Every invariant measure is a barycenter (integral) of ergodic measures. — (ergodic measures, Choquet theory).
104. **Unique ergodicity** — axiom — M(X,T) is a singleton (exactly one invariant probability). — (M(X,T)).
105. **Characterizations of unique ergodicity** — theorem — Uniquely ergodic iff (1/n)Σ f(T^i x) converges uniformly to a constant for every continuous f. — (unique ergodicity, ergodic averages).
106. **Weyl equidistribution theorem (via unique ergodicity)** — theorem — {nα} is equidistributed mod 1 for irrational α, since the rotation is uniquely ergodic. — (unique ergodicity, irrational rotation).
107. **Topological pressure P(T,f)** — state — P(T,f)=lim_{ε→0} limsup (1/n) log Σ over (n,ε)-separated sets of exp(Σ f(T^i x)); generalizes topological entropy (f=0). — (separated sets, continuous potential f).
108. **Properties of pressure** — theorem — P is monotone, convex in f, |P(f)−P(g)|≤‖f−g‖, P(f+c)=P(f)+c, P(f∘T−f)=P(0), etc. — (topological pressure).
109. **Pressure via open covers / spanning sets** — theorem — Equivalent definitions of P(T,f) using open covers, spanning sets, and separated sets. — (open covers, spanning sets).
110. **Variational principle for entropy** — theorem — h_top(T) = sup{ h_μ(T) : μ ∈ M(X,T) }. — (topological entropy, measure entropy, M(X,T)).
111. **Variational principle for pressure** — theorem — P(T,f) = sup{ h_μ(T) + ∫ f dμ : μ ∈ M(X,T) }. — (pressure, measure entropy).
112. **Equilibrium state** — state — An invariant measure μ attaining the sup: h_μ(T)+∫f dμ = P(T,f). — (variational principle for pressure).
113. **Existence of equilibrium states** — theorem — If the entropy map μ↦h_μ(T) is upper semicontinuous, equilibrium states exist for every continuous f. — (upper semicontinuity of entropy, variational principle).
114. **Upper semicontinuity of the entropy map** — theorem — Condition (e.g. expansive T) under which μ↦h_μ(T) is u.s.c., giving existence (and on expansive systems uniqueness for nice f). — (measure entropy, expansiveness).
115. **Expansive homeomorphism** — axiom — A homeomorphism with an expansive constant c: distinct orbits separate by c. — (topological system, metric).
116. **Pressure determines M(X,T) (tangent functionals)** — theorem — Equilibrium states are the tangent functionals to the convex pressure function; M(X,T) is recovered from pressure. — (pressure convexity, functional analysis).

## Chapter 10 — Applications

117. **Equidistribution / equidistributed sequences mod 1** — state — A sequence whose empirical distribution converges to Lebesgue measure on the circle. — (unique ergodicity).
118. **Weyl's theorem on polynomial sequences** — theorem — Sequences like {p(n)} with irrational leading coefficient are equidistributed mod 1 (via van der Corput / unique ergodicity of nilrotations). — (equidistribution, weak-mixing).
119. **Continued fraction expansion & Gauss map ergodicity** — theorem — The Gauss map is ergodic (indeed exact/mixing) w.r.t. the Gauss measure; gives metric properties of continued fractions. — (Gauss map, ergodicity).
120. **Lévy / Khinchin constants** — theorem — A.e. continued fraction has geometric-mean partial quotients → Khinchin's constant; denominator growth → Lévy's constant (Birkhoff applied to Gauss map). — (Gauss map ergodicity, Birkhoff theorem).
121. **Shannon's theorem / information-theoretic interpretation** — theorem — Entropy h(T) as asymptotic information rate of the associated stationary source (SMB). — (Shannon–McMillan–Breiman, entropy).
122. **Borel normal-number theorem (continued-fraction version)** — theorem — Frequency statistics of digits/partial quotients for a.e. point from ergodicity. — (ergodicity, Birkhoff theorem).
