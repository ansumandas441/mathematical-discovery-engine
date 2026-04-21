# Intern B — Round 2 Findings (Analytic & Geometric Gaps)

## Gap areas covered

1. Harmonic analysis decompositions beyond Fourier — Littlewood-Paley, wavelet, decoupling, restriction
2. Geometric flows beyond Ricci — mean curvature, harmonic map, Yang-Mills, Kahler-Ricci
3. Microlocal analysis — wavefront set, propagation of singularities, parametrix
4. Geometric measure theory — currents, varifolds, rectifiability, Plateau
5. Variational methods — direct method, Ekeland, mountain-pass, Morse
6. Sieve theory — Brun, Selberg, large sieve, Maynard
7. Circle method (Hardy-Littlewood) as a standalone
8. Entropy method in combinatorics — Shearer, Shannon counting
9. Ergodic recurrence — Furstenberg correspondence, multiple recurrence
10. KAM / Nash-Moser
11. Geometric group theory — quasi-isometry, Svarc-Milnor, polynomial growth
12. Symplectic / Floer homology — Lagrangian intersection, pseudo-holomorphic curves
13. Tropical geometry — tropicalization, Viro patchworking
14. Random-structure universality — SLE, local eigenvalue universality, Tracy-Widom beyond GUE

## Count

**20 entries** total. Fourteen propose NEW toolbox techniques; six are examples extending existing techniques.

## Table of contents

### New-technique proposals
1. Littlewood-Paley dyadic decomposition (1930s, Littlewood-Paley; codified Stein 1970s)
2. Bourgain-Demeter l^2 decoupling (2015, Bourgain-Demeter)
3. Mean curvature flow (Huisken monotonicity) (1984/1990, Huisken)
4. Wavefront set / propagation of singularities (1970, Hormander / Duistermaat-Hormander)
5. Currents and mass-minimization (1960, Federer-Fleming)
6. Mountain-pass / Palais-Smale minimax (1973, Ambrosetti-Rabinowitz)
7. Selberg sieve (1947, Selberg)
8. Hardy-Littlewood circle method (1918-1923, Hardy-Ramanujan / Hardy-Littlewood)
9. Shearer entropy inequality for counting (1986, Chung-Frankl-Graham-Shearer)
10. Furstenberg correspondence principle (1977, Furstenberg)
11. Nash-Moser implicit function theorem (1956/1966, Nash-Moser)
12. Gromov quasi-isometry invariance (1981, Gromov)
13. Floer homology via pseudo-holomorphic curves (1988, Floer)
14. Tropicalization map (1980s-2004, Bergman / Mikhalkin / Sturmfels)

### Example extensions of existing techniques
15. Harmonic map heat flow (Eells-Sampson 1964) — extends `flowWithSurgery`
16. Kahler-Ricci flow and Song-Tian analytic MMP — extends `flowWithSurgery`
17. Yang-Mills flow on 4-manifolds (Donaldson 1985) — extends `flowWithSurgery`
18. Stein-Tomas restriction theorem (1975) — extends `frequencyDecomposition`
19. Ekeland variational principle (1974) — extends `contractionFixedPoint` / `compactnessArgument`
20. Schramm-Loewner evolution (2000, Schramm) — extends `physicsToPDE` / `interpolateAndContinue`

---

## Entries

### Littlewood-Paley dyadic decomposition (1930s, J.E. Littlewood and R.E.A.C. Paley; codified by E.M. Stein)

**Statement / description:** Decompose a function f on R^n into a sum of frequency-localized pieces f_k, where f_k has Fourier support in a dyadic annulus |xi| ~ 2^k. Norms and derivatives of f are controlled by the square-function S(f) = (sum_k |f_k|^2)^{1/2}. This refines Fourier analysis by replacing pointwise frequency information with scale-localized packets.

**Discovery trigger:** Littlewood and Paley sought p-independent estimates for Fourier series (1931, 1937): the classical Riesz projection fails at p = 1 and p = infinity but Lp-boundedness needed a replacement for "almost orthogonality" that works off L^2. Dyadic blocks deliver almost-orthogonality in any L^p via the square function.

**Thought process / lineage:** Predecessors: Rademacher functions and Khintchine inequalities (random signs model independence of dyadic modes); Marcinkiewicz multiplier theorem (1939, which is effectively a dyadic Hormander-Mihlin statement). Stein's *Singular Integrals and Differentiability Properties* (1970) and *Topics in Harmonic Analysis* (1970) turned it into a systematic tool. Further lineages: Bony paraproducts (1981), Meyer wavelets (1986), Triebel-Lizorkin / Besov function spaces.

**Proof idea / process:** Fix a smooth bump phi with phi(xi) = 1 for |xi| <= 1, phi(xi) = 0 for |xi| >= 2; set psi_k(xi) = phi(2^{-k} xi) - phi(2^{-k+1} xi). Then 1 = sum psi_k(xi) is a smooth dyadic partition of unity in frequency. Define Delta_k f via Fourier multiplier psi_k. Khintchine's inequality on random signs gives ||f||_{L^p} ~_p ||(sum |Delta_k f|^2)^{1/2}||_{L^p} for 1 < p < infinity. Differentiation shifts blocks by a bounded multiplier on each annulus; a Bernstein inequality on each block converts derivatives to scalar factors 2^k.

**Impact:** Foundation of modern harmonic analysis: Calderon-Zygmund operators, Strichartz estimates, well-posedness of nonlinear wave / Schrodinger / Navier-Stokes (Bourgain, Tao, Koch-Tataru). Paraproduct calculus linearizes low-regularity products. Function spaces B^s_{p,q} (Besov) and F^s_{p,q} (Triebel-Lizorkin) are *defined* via Littlewood-Paley norms. Enables the modern decoupling and restriction theory in entry #2.

**Sources:**
- Tao, "Dyadic decomposition and Littlewood-Paley theory," Lecture notes Math 247A: https://www.math.ucla.edu/~tao/247a.1.06f/
- Stein-Shakarchi, *Functional Analysis* (Princeton Lectures IV), Ch. 1-2: https://press.princeton.edu/books/hardcover/9780691113876/functional-analysis
- Grafakos, *Classical Fourier Analysis*, 3rd ed. (Springer GTM 249), Chapter 6.

**Technique tag:** NEW — `dyadicDecomposition(function on R^n, smooth partition in frequency) -> scaleLocalizedBlocks` — decompose f = sum_k Delta_k f into dyadic frequency annuli and control norms / operators via the square function of the blocks.

---

### Bourgain-Demeter l^2 decoupling (2015, Jean Bourgain and Ciprian Demeter)

**Statement / description:** Let S be a smooth hypersurface (paraboloid, sphere, cone) in R^n with appropriate curvature, and partition S into caps theta of size delta^{1/2}. For f with Fourier support in the delta-neighborhood of S, decouple f = sum_theta f_theta obeys ||f||_{L^p} <= C_epsilon delta^{-epsilon} (sum_theta ||f_theta||_{L^p}^2)^{1/2} in the sharp range (p <= 2(n+1)/(n-1) for the paraboloid). The sharp loss is just delta^{-epsilon}.

**Discovery trigger:** The Vinogradov mean-value conjecture on J_{s,k}(N) = #{1 <= x_i, y_i <= N : sum x_i^j = sum y_i^j, j = 1..k}. Classical circle-method + Weyl sums gave only partial results; the full Main Conjecture was proved by Bourgain-Demeter-Guth 2016 as a corollary of decoupling applied to the moment curve.

**Thought process / lineage:** Predecessors: Stein-Tomas restriction (below), Bourgain's 1991 Fourier-restriction for Schrodinger, Wolff's l^p decoupling for cones (2000) — a weaker exponent but a correct template. Guth's polynomial method in incidence geometry. Bourgain-Demeter combined multilinear restriction (Bennett-Carbery-Tao 2006 multilinear Kakeya) with an "induction on scales" bootstrap — run the inequality at scale delta, use a ball-condition to pass to scale sqrt(delta), iterate.

**Proof idea / process:** (a) Decompose into caps theta. (b) On a ball of radius delta^{-1}, wave-packet localization relates f_theta to tubes of dimension delta^{-1/2} x delta^{-1}. (c) A multilinear Kakeya bound (Bennett-Carbery-Tao) controls the overlap of transverse tube families: |union of tubes|^{1/k} <= C prod |T_j|^{1/k}. (d) Induction on scales from delta down to 1 transfers multilinear to linear decoupling at the cost of C_epsilon delta^{-epsilon}.

**Impact:** Vinogradov Main Conjecture (Bourgain-Demeter-Guth 2016, *Annals*); best bounds for integer solutions to Waring-type Diophantine equations; progress on Montgomery's conjecture for the zeta function (Bourgain improvements to zero-density); Strichartz estimates on compact manifolds; Carleson's problem (pointwise convergence of Schrodinger). Used by Guth-Maynard on large gaps between primes (2024).

**Sources:**
- Bourgain-Demeter, "The proof of the l^2 decoupling conjecture," Annals of Math 182 (2015) — arXiv:1403.5335
- Bourgain-Demeter-Guth, "Proof of the main conjecture in Vinogradov's mean value theorem for degrees higher than three," Annals 184 (2016) — arXiv:1512.01565
- Tao, "Decoupling, restriction, and the moment curve," blog series: https://terrytao.wordpress.com/tag/decoupling/
- Demeter, *Fourier Restriction, Decoupling, and Applications* (Cambridge Studies 184, 2020).

**Technique tag:** NEW — `decoupleByDyadicCaps(function with Fourier support on delta-neighborhood of curved surface S, partition of S into curvature-scale caps) -> l^pToL2DecouplingInequality` — turn constructive interference on a curved surface into an almost-orthogonal sum with epsilon-loss. *Inherits: dyadicDecomposition; multilinearKakeya (new below).*

---

### Mean curvature flow and Huisken monotonicity (1984/1990, Gerhard Huisken)

**Statement / description:** An immersion F: M^n -> R^{n+1} evolves by d F/d t = H nu where H is mean curvature and nu the outward normal. Convex hypersurfaces contract to a round point in finite time (Huisken 1984). Huisken's monotonicity formula: the Gaussian area integral Theta(x_0, t_0)(t) = integral_{M_t} rho_{(x_0, t_0)} dH^n over M_t against the backward heat kernel rho is monotone non-increasing in t. Singularities are classified by tangent flows — self-shrinkers sum_k lambda_k = H.

**Discovery trigger:** Sought a geometric PDE that shrinks surfaces to minimize area and classifies singular behavior (model: Huisken wanted an MCF analog of Hamilton's Ricci-flow program for surfaces in Euclidean space). Original impetus: surface-tension physics and bubble minimization.

**Thought process / lineage:** Predecessors: Brakke's varifold formulation (1978), mean-curvature motion as L^2-gradient of area functional. Hamilton's (1982) Ricci-flow analogy. Huisken imported the "preserved convexity + pinching" scheme from Hamilton. Later: Ilmanen (1995) level-set MCF via weak formulation; White regularity theorem; Colding-Minicozzi classification of generic singularities (2012, arXiv:0908.3788).

**Proof idea / process:** Convex hypersurface: evolve by H. Derive evolution equations for (g, H, A, |A|^2). Max-principle arguments on |A|^2 / H^2 show eigenvalues of A pinch; convexity preserved; rescaling at blow-up converges to the shrinking sphere. Monotonicity formula: chain rule on the heat-kernel integral gives d Theta / d t = - integral (H - <x - x_0, nu> / (2(t_0 - t)))^2 rho dH^n <= 0.

**Impact:** Classifies singularities of moving hypersurfaces; key technical tool in general relativity (Huisken-Ilmanen proof of Riemannian Penrose inequality, 2001); Brendle-Schoen differentiable sphere theorem uses Ricci-flow analog; Colding-Minicozzi generic MCF program; Bamler-Kleiner's 2018 uniqueness of generic MCF. *Huisken's monotonicity formula is a structural template copied by Perelman* for Ricci flow (local monotonicity, F and W entropy).

**Sources:**
- Huisken, "Flow by mean curvature of convex surfaces into spheres," J. Differential Geom. 20 (1984): https://projecteuclid.org/euclid.jdg/1214438998
- Huisken, "Asymptotic behavior for singularities of the mean curvature flow," J. Differential Geom. 31 (1990): https://projecteuclid.org/euclid.jdg/1214444099
- Colding-Minicozzi, "Generic mean curvature flow I," Annals of Math 175 (2012) — arXiv:0908.3788
- Ecker, *Regularity Theory for Mean Curvature Flow* (Birkhauser 2004).
- MacTutor biographical: https://mathshistory.st-andrews.ac.uk/ (Huisken entry)

**Technique tag:** NEW — `curvatureMonotonicityClassifier(geometric flow, Gaussian or reduced-volume functional) -> singularityModelByTangentFlow` — introduce a scale-invariant monotone functional whose critical points are self-similar solutions; blow-up at a singularity converges to such a self-similar model, classifying the local geometry. *Inherits: flowWithSurgery, conservedQuantity.* (MCF merits its own entry because the Gaussian-density monotonicity is a new template distinct from Ricci-flow reduced volume; `flowWithSurgery` covers the generic surgery program, but MCF-style monotonicity classification is a separately named and separately applicable technique.)

---

### Wavefront set and propagation of singularities (1970, Lars Hormander / 1972 Duistermaat-Hormander)

**Statement / description:** For a distribution u on a manifold, the wavefront set WF(u) ⊂ T^*M \ 0 is the set of (x, xi) where u is not microlocally smooth: local Fourier transforms near x fail to decay in direction xi. Hormander's theorem: for a properly supported pseudodifferential operator P with principal symbol p, WF(Pu) ⊂ WF(u) ⊂ WF(Pu) ∪ Char(P), and singularities of solutions to Pu = 0 propagate along the null bicharacteristics of p (integral curves of the Hamilton vector field H_p on p = 0).

**Discovery trigger:** The Cauchy problem for the wave equation: classically, singularities of the initial data propagate along light rays. Hormander sought a microlocal formulation that extended this to general (non-elliptic) principal-type operators — why do hyperbolic solutions have sharply defined singular supports?

**Thought process / lineage:** Predecessors: Sato's hyperfunctions and analytic wavefront SS (Kyoto school, 1969-71); Maslov's canonical operator method; Ludwig-Keller asymptotic ray expansion. Hormander (1971) combined pseudodifferential and Fourier integral operators into a unified symbol calculus. Further: Duistermaat-Hormander Fourier integral operators II (1972) — FIOs as "quantizations" of canonical transformations.

**Proof idea / process:** Locally write u = (2 pi)^{-n} integral e^{i<x, xi>} hat{u}(xi) dxi and define WF(u) as the conic set where hat(phi u) fails polynomial decay for any cutoff phi near x. For Pu = 0, the symbol p(x, xi) vanishes on Char(P). The commutator [P, Q] with a well-chosen microlocal cutoff Q has principal symbol {p, q} (Poisson bracket = Hamilton vector field). Positive commutator / Hormander-type energy estimate shows singularities can only move along bicharacteristic flow.

**Impact:** Microlocal analysis as a subject. Applications: local solvability (Lewy's example of non-solvable PDE), propagation in diffraction (Melrose), scattering theory, analytic singularity tracking, Cauchy problem in general relativity, AdS/CFT boundary propagation, adiabatic limits, parametrix constructions for index theorems (Hormander's general FIO calculus underpins the Atiyah-Singer pseudo-differential proof). Vasy's "N-body Fredholm" scattering (2013, arXiv:1012.4391) extends propagation to asymptotically hyperbolic settings.

**Sources:**
- Hormander, *Fourier Integral Operators I*, Acta Math 127 (1971): https://projecteuclid.org/euclid.acta/1485889436
- Duistermaat-Hormander, *Fourier Integral Operators II*, Acta Math 128 (1972): https://projecteuclid.org/euclid.acta/1485889458
- Hormander, *The Analysis of Linear Partial Differential Operators*, Vol. I-IV (Springer 1983-85).
- nLab: wavefront set — https://ncatlab.org/nlab/show/wave+front+set
- Grigis-Sjostrand, *Microlocal Analysis for Differential Operators* (LMS Lecture Note Series 196, 1994).

**Technique tag:** NEW — `propagateSingularitiesAlongBicharacteristics(distribution u, operator P with principal symbol p) -> microlocalSingularSupport` — locate singularities of u in phase space T^*M; control how they move under P by integrating the Hamilton vector field H_p on the characteristic variety. *Inherits: frequencyDecomposition (local Fourier analysis), duality (T^*M as dual phase space).*

---

### Currents and mass-minimization (1960, Herbert Federer and Wendell Fleming)

**Statement / description:** A k-current on R^n is a continuous linear functional on smooth compactly-supported k-forms (dual to Omega^k_c). The boundary operator d^* on currents extends the classical boundary in a way that subsumes rectifiable sets. Federer-Fleming Closure Theorem: the class of integral k-currents with bounded mass and bounded boundary mass is compact in the flat-norm topology. Therefore any k-dimensional homology class admits a *mass-minimizing* representative.

**Discovery trigger:** The Plateau problem in high dimensions / codimension: does every k-dimensional boundary in R^n bound a k-dimensional minimal surface? Classical Douglas-Rado (1931) solved the 2-dimensional disk case. De Giorgi (1954) handled codimension 1 via perimeter/Caccioppoli sets. Federer-Fleming generalized to arbitrary k and n.

**Thought process / lineage:** Predecessors: de Rham currents as distribution-valued forms (1955); Whitney's geometric integration theory (1957); Caccioppoli perimeters; De Giorgi's reduced boundary. Federer-Fleming added rectifiability + integer multiplicity + flat norm compactness. Later Almgren's Big Regularity Paper (1972-83, published 2000) completed the regularity for area-minimizing currents in higher codim.

**Proof idea / process:** Define flat norm F(T) = inf{M(A) + M(B) : T = A + dB}. Polyhedral currents with integer multiplicity are dense. A mass-bounded sequence admits an F-convergent subsequence (this is the *compactness-for-currents* analog of Banach-Alaoglu). Rectifiability (Federer-Fleming closure) shows the limit is an integral k-current supported on a k-rectifiable set. Minimizing mass over a given homology class yields a minimal surface.

**Impact:** Solved Plateau in arbitrary dimension and codimension. Geometric measure theory as a named discipline (Federer's 1969 book *Geometric Measure Theory*). Almgren's regularity (singular set codim 2); later Preiss's rectifiability via tangent measures (1987); Allard's varifold regularity theorem (1972); modern work of De Lellis-Spadaro on Almgren's Q-valued maps. Foundational for general-relativity positive-mass arguments (Schoen-Yau) and minimal-surface construction of Scharlemann, Simon.

**Sources:**
- Federer-Fleming, "Normal and integral currents," Annals of Math 72 (1960): https://www.jstor.org/stable/1970227
- Federer, *Geometric Measure Theory* (Springer 1969, reprinted Classics in Math 1996).
- Morgan, *Geometric Measure Theory: A Beginner's Guide*, 5th ed. (Elsevier 2016).
- De Lellis, "The size of the singular set of area-minimizing currents," arXiv:1506.08118.
- nLab: current — https://ncatlab.org/nlab/show/current

**Technique tag:** NEW — `currentMassMinimize(boundary k-current Gamma, homology class alpha) -> integralMassMinimizer` — extend polyhedral chains to integral currents with a flat-norm compactness theorem; extract a mass-minimizer in any homology class. *Inherits: compactnessArgument, duality (currents are dual to forms).*

---

### Mountain-pass lemma and Palais-Smale minimax (1973, Antonio Ambrosetti and Paul Rabinowitz; Palais-Smale 1964)

**Statement / description:** Let E be a Banach space and I: E -> R a C^1 functional satisfying the Palais-Smale condition (every sequence with bounded I(u_n) and DI(u_n) -> 0 has a convergent subsequence). If I(0) = 0, there exists e in E with I(e) <= 0, and there exists r > 0 such that I(u) >= alpha > 0 for ||u|| = r (a "mountain-pass geometry"), then c := inf_{gamma} max_{t in [0,1]} I(gamma(t)) >= alpha is a critical value of I, where the inf is over continuous paths gamma: [0,1] -> E with gamma(0) = 0, gamma(1) = e.

**Discovery trigger:** Nonlinear elliptic PDEs of variational type — u'' + f(u) = 0 with f superlinear and subcritical — for which direct minimization fails because the functional is unbounded below, yet saddle-point critical points exist and correspond to solutions.

**Thought process / lineage:** Predecessors: Morse theory (1930s) on finite-dim manifolds — critical points tied to topology. Palais-Smale (1964) formulated the Condition (C) needed for Morse theory in infinite dimensions. Ljusternik-Schnirelman (1930s) category theory for multiple critical points on projective spaces. Ambrosetti-Rabinowitz's 1973 J. Funct. Anal. paper abstracted mountain-pass geometry and proved it via a pseudo-gradient deformation argument. Subsequent: Ekeland variational principle (1974) gave a fixed-point flavored proof.

**Proof idea / process:** Suppose c > alpha is not a critical value; then by Sard-like deformation, the sub-level set {I < c} is a strong deformation retract of {I < c + epsilon}. Using the PS condition, construct a pseudo-gradient vector field V with DI(V) >= (1/2) ||DI|| on a shell around level c. Flow along -V: any path gamma with max I(gamma) close to c can be deformed to a path with max I(gamma) < c - delta, contradicting the inf definition.

**Impact:** Foundation of critical-point theory for nonlinear PDE and Hamiltonian systems. Applications: existence of multiple solutions to elliptic BVPs (Brezis-Nirenberg 1983 critical exponent problem, CPAM 36), Rabinowitz periodic orbits on prescribed energy hypersurfaces in symplectic manifolds (precursor to Floer homology!), Ekeland-Hofer symplectic capacities. Linking theorems, limit-index theorems, and fountain theorems all descend from this.

**Sources:**
- Ambrosetti-Rabinowitz, "Dual variational methods in critical point theory and applications," J. Funct. Anal. 14 (1973): https://doi.org/10.1016/0022-1236(73)90051-7
- Rabinowitz, *Minimax Methods in Critical Point Theory with Applications to Differential Equations* (CBMS Regional Conf. 65, 1986).
- Mawhin-Willem, *Critical Point Theory and Hamiltonian Systems* (Springer Applied Math Sciences 74, 1989).
- Ekeland, *Convexity Methods in Hamiltonian Mechanics* (Springer Ergebnisse 3F-19, 1990).

**Technique tag:** NEW — `mountainPassMinimax(C^1 functional I on Banach space satisfying Palais-Smale, mountain-pass geometry) -> criticalPoint` — produce saddle-type critical points of unbounded functionals via minimax over paths; PS compactness turns an infinite-dim variational problem into a topological Morse-style argument. *Inherits: compactnessArgument, conservedQuantity (the functional itself).*

---

### Selberg sieve (1947, Atle Selberg)

**Statement / description:** Given a set A of integers and a set P of primes, let S(A, P, z) = #{n in A : gcd(n, prod_{p in P, p <= z} p) = 1}. Selberg's upper-bound sieve: choose weights lambda_d (lambda_1 = 1) and write S(A, P, z) <= sum_{n in A} (sum_{d | n, d <= sqrt(D)} lambda_d)^2. Optimizing lambda_d by Lagrange multipliers (a quadratic form in lambda) gives bounds of the shape |A| / (log D)^k for k-fold sifted sets, with constants sharper than the Brun pure sieve.

**Discovery trigger:** Improve Brun's sieve of 1919. Brun's pure sieve gave Brun's constant B_2 = sum (1/p + 1/(p+2)) < infinity for twin primes but with mediocre constants; Selberg sought the optimal elementary upper-bound sieve by squaring and minimizing a quadratic form.

**Thought process / lineage:** Predecessors: Legendre-Eratosthenes sieve (inclusion-exclusion, exact but ruined by error accumulation); Brun's pure sieve (1919) — truncated inclusion-exclusion with Brun's fundamental lemma; Jurkat-Richert refined to the linear sieve; Iwaniec's 1980 combinatorial sieve. Later: Goldston-Pintz-Yildirim (2009) approximated the Selberg weight (log d / log z)^k and detected small gaps between primes; Maynard (2015) and Tao independently replaced the 1D Selberg weight by a multidimensional weight, yielding bounded gaps without Elliott-Halberstam.

**Proof idea / process:** The crucial inequality is the trivial 1_{(n, P(z)) = 1} <= (sum_{d | n, d <= D} lambda_d)^2 whenever lambda_1 = 1 and D^2 < z. Expand the square, sum over n in A, get a quadratic form Q(lambda) = sum_{d_1, d_2} lambda_{d_1} lambda_{d_2} #{n : [d_1, d_2] | n}. Rewrite n-count as g([d_1, d_2]) |A| + error, diagonalize Q by Mobius-inverting to new variables y_d, minimize via Cauchy-Schwarz to get S(A, P, z) <= |A| / sum_{d <= D, d squarefree, d | P(z)} g(d)^{-1}.

**Impact:** Brun-Titchmarsh theorem (canonical sieve upper bound); Bombieri-Vinogradov theorem (large-sieve refinement); Chen Jingrun's 1973 theorem "every large even integer is p + p_2" where p_2 has <=2 prime factors (closest to Goldbach); Goldston-Pintz-Yildirim small gaps (2009); Zhang's bounded gaps (2013) and Maynard-Tao's multidimensional generalization (2014) — currently 246 as the proven gap bound. Now a central tool in analytic number theory alongside the circle method.

**Sources:**
- Selberg, "On an elementary method in the theory of primes," Norske Vid. Selsk. Forh. 19 (1947).
- Friedlander-Iwaniec, *Opera de Cribro* (AMS Colloquium Publications 57, 2010).
- Maynard, "Small gaps between primes," Annals of Math 181 (2015) — arXiv:1311.4600
- Tao, "The Selberg sieve," blog post: https://terrytao.wordpress.com/2011/02/12/the-selberg-sieve/
- Cojocaru-Murty, *An Introduction to Sieve Methods and their Applications* (LMS Student Texts 66, 2005).

**Technique tag:** NEW — `sieveByMinimizingQuadraticForm(integer set A, prime set P, sieve dimension k, truncation level D) -> upperBoundOnSiftedCount` — upper-bound the count of A-elements coprime to all primes up to a threshold via a square-of-sum cutoff with weights optimized by a quadratic-form minimization. *Inherits: composeWithIdentity (Mobius inversion), probabilisticExistence (bounds via expected counts).*

---

### Hardy-Littlewood circle method (1918-1923, G.H. Hardy and S. Ramanujan; Hardy and J.E. Littlewood)

**Statement / description:** To count representations r(N) of N as a sum of structured pieces (primes, k-th powers, etc.), encode r(N) as a contour integral: r(N) = integral_0^1 F(alpha)^s e^{-2 pi i N alpha} d alpha, where F(alpha) = sum_{n <= N} e^{2 pi i n alpha} restricted to the structured set. Decompose [0,1] into *major arcs* (alpha close to rationals a/q with q <= Q small) where F admits an asymptotic via Euler-product / local analysis, and *minor arcs* (everything else) where F is bounded by Weyl-type exponential-sum estimates. Major-arc contribution is the expected singular series; minor-arc is an error.

**Discovery trigger:** Hardy-Ramanujan (1918) attacked the partition function p(n) via contour integration of the generating function 1/prod(1 - q^n); the modular transformation q -> q^{-1} forced a decomposition into Farey arcs. Hardy-Littlewood (1920-23) generalized to Waring's problem g(k): every integer is a sum of G(k) k-th powers.

**Thought process / lineage:** Predecessors: Farey dissection (Hardy-Littlewood, adapting Farey fractions for a partition of [0,1]); Cauchy contour manipulation. Later: Vinogradov (1937) sharpened Weyl sums and proved the ternary Goldbach theorem for all sufficiently large N; Davenport cubic forms; Birch-Davenport on simultaneous Diophantine equations; Vaughan's identity refinement (1977); Iwaniec-Kowalski *Analytic Number Theory* modern treatment. Helfgott (2013-15) completed ternary Goldbach using fully explicit circle-method bounds. Bourgain-Demeter-Guth's decoupling in entry #2 sharpens Vinogradov mean values central to the method.

**Proof idea / process:** (a) Encode r(N) as integral_0^1 F(alpha)^s e^{-2 pi i N alpha} d alpha via orthogonality integral_0^1 e^{2 pi i m alpha} d alpha = [m = 0]. (b) For alpha = a/q + beta near a rational with q small, use local (p-adic + archimedean) Euler-product approximation for F. The singular series S(N) = prod_p (local density) emerges. (c) For alpha far from any small-denominator rational, Weyl-differencing gives |F(alpha)| << N^{1-1/K} via diophantine rational approximation of alpha. (d) Combine: major-arc contribution asymptotically N^{s-1} * S(N); minor-arc bounded by (max |F|)^{s - s_0} * integral |F|^{s_0} which is smaller if s is large.

**Impact:** Proved Waring's problem for g(k), partition asymptotics (Hardy-Ramanujan-Rademacher formula), ternary Goldbach (Vinogradov 1937, fully explicit Helfgott 2013), 3-term APs in primes (Vinogradov/van der Corput), Davenport-Heilbronn cubic surface local-global, Birch's theorem on cubic hypersurfaces. Remains the standard tool for additive-combinatorial Diophantine problems. Combined with decoupling it yielded Bourgain-Demeter-Guth's Vinogradov mean value.

**Sources:**
- Vaughan, *The Hardy-Littlewood Method*, 2nd ed. (Cambridge Tracts 125, 1997): https://doi.org/10.1017/CBO9780511470929
- Davenport, *Analytic Methods for Diophantine Equations and Diophantine Inequalities*, 2nd ed. (Cambridge 2005).
- Helfgott, "The ternary Goldbach problem," arXiv:1501.05438 (2015).
- Iwaniec-Kowalski, *Analytic Number Theory* (AMS Colloquium 53, 2004), Ch. 20.
- Tao, "254a Notes 5: The Hardy-Littlewood circle method": https://terrytao.wordpress.com/2014/11/02/

**Technique tag:** NEW — `majorMinorArcDecomposition(additive counting problem r(N), generating exponential sum F(alpha)) -> singularSeriesPlusError` — encode an additive counting problem as integral_0^1 F(alpha)^s e^{-2 pi i N alpha} dalpha, split [0,1] into small-denominator major arcs (computed via Euler-product singular series) and minor arcs (bounded by Weyl sums). *Inherits: complexAnalysisToIntegers (generating functions as asymptotic tool), frequencyDecomposition.*

Note: `complexAnalysisToIntegers` currently lists "Helfgott's weak Goldbach via circle method" as a single-line example. The circle method deserves its own entry because (a) the Farey/major-minor decomposition is a *distinct technique* from contour-integration asymptotics of Dirichlet series; (b) it consumes exponential-sum bounds rather than zero-density information; and (c) modern decoupling is a direct descendant.

---

### Shearer entropy inequality for counting (1986, Chung-Graham-Frankl-Shearer)

**Statement / description:** Let X = (X_1, ..., X_n) be a random vector, and let F be a family of subsets of {1, ..., n} such that each index i is covered by at least t members of F. Then H(X) <= (1/t) sum_{S in F} H(X_S). As a corollary for counting: if A is a set of objects specified by n coordinates and each coordinate is determined by some chosen set of projections, then |A| <= prod_{S in F} |A_S|^{1/t} where A_S is the projection to coordinates in S.

**Discovery trigger:** Chung-Graham-Frankl-Shearer (1986) sought combinatorial bounds on set-systems where direct double-counting fails. Shearer observed that Shannon entropy subadditivity (H(X,Y) <= H(X) + H(Y)) generalizes to fractional covers of coordinates — giving Loomis-Whitney-style bounds without induction.

**Thought process / lineage:** Predecessors: Loomis-Whitney inequality (1949) — a body in R^n has volume <= (prod of (n-1)-dim shadow volumes)^{1/(n-1)}. Shannon entropy subadditivity (1948). Han's inequality (1978). Shearer's lemma is the exact entropic generalization of Loomis-Whitney to arbitrary fractional covers. Later: Radhakrishnan's elegant proof of Bregman's permanent bound (1997); Friedgut-Kahn on counting triangles; Kahn-Lovasz-style entropy methods; Alon-Newman-Shapira-Yuster.

**Proof idea / process:** Chain rule H(X_1, ..., X_n) = sum_i H(X_i | X_{<i}). For each set S in the cover F, H(X_S) >= sum_{i in S} H(X_i | X_{<i, i in S}). Conditioning on fewer variables gives larger conditional entropy: H(X_i | X_{<i, i in S}) >= H(X_i | X_{<i}) so sum_{S in F, i in S} H(X_S) >= sum_{S in F, i in S} H(X_i | X_{<i}) = (cover weight at i) * H(X_i | X_{<i}) >= t * H(X_i | X_{<i}). Summing over i gives t * H(X) <= sum H(X_S). For counting, H(Uniform on A) = log |A| and H(X_S) <= log |A_S|.

**Impact:** Loomis-Whitney revisited; Radhakrishnan's proof of Bregman's permanent bound |per(A)| <= prod (r_i!)^{1/r_i}; counting graph homomorphisms (Friedgut-Kahn); Kahn's entropy proof of the Brundan-Bowman bound; counting triangles in sparse graphs; modern entropy-method combinatorics (Balister-Bollobas-Morris, Jukna). Underpins Bukh-Conlon forbidden-subgraph density bounds. A clean tool for showing a discrete set has a quantitative constraint by projecting to lower dim and invoking the fractional Loomis-Whitney.

**Sources:**
- Chung-Graham-Frankl-Shearer, "Some intersection theorems for ordered sets and graphs," J. Combinatorial Theory A 43 (1986): https://doi.org/10.1016/0097-3165(86)90019-1
- Radhakrishnan, "Entropy and counting," Computational Mathematics, Modelling, and Algorithms (Narosa 2003) — notes: https://www.tcs.tifr.res.in/~jaikumar/mypage.html
- Tao, "Shearer's entropy inequality," blog post: https://terrytao.wordpress.com/2009/11/05/
- Galvin, "Three tutorial lectures on entropy and counting," arXiv:1406.7872
- Alon-Spencer, *The Probabilistic Method*, 4th ed., Ch. 15.

**Technique tag:** NEW — `shearerEntropyCount(discrete set A defined by n coordinates, fractional cover F of the coordinates) -> projectionProductBound` — bound |A| by the product of sizes of its projections under any fractional covering via Shannon-entropy subadditivity; the entropy method replaces multiple-induction case analysis. *Inherits: probabilisticExistence, composeWithIdentity (subadditivity identity).*

---

### Furstenberg correspondence principle (1977, Hillel Furstenberg)

**Statement / description:** Given a subset E ⊂ N of positive upper Banach density d*(E) > 0, there exists a measure-preserving system (X, B, mu, T) and a set A in B with mu(A) = d*(E) such that d*(E ∩ (E - n_1) ∩ ... ∩ (E - n_k)) >= mu(A ∩ T^{-n_1} A ∩ ... ∩ T^{-n_k} A) for all n_1, ..., n_k. Combinatorial recurrence in the integers is controlled by ergodic multiple-recurrence in an abstract dynamical system. Coupled with Furstenberg's multiple recurrence theorem (limsup of mu(A ∩ T^{-n}A ∩ T^{-2n}A ∩ ... ∩ T^{-kn}A) > 0 as n -> infinity), this proves Szemeredi's theorem on arithmetic progressions.

**Discovery trigger:** Furstenberg (1977) wanted an ergodic proof of Szemeredi's theorem (1975) on k-term APs in positive-density subsets of the integers. Szemeredi's proof was a tour de force of combinatorics (regularity lemma). Furstenberg re-cast it as a recurrence statement in ergodic theory.

**Thought process / lineage:** Predecessors: Poincare recurrence (1890); Khintchine recurrence (1934); von Neumann mean-ergodic (1932); Birkhoff pointwise-ergodic (1931); Roth's theorem on 3-APs via Fourier (1953); Szemeredi's theorem (1975). Furstenberg's key insight: translate combinatorics to ergodic theory via a Krylov-Bogolyubov-type construction, then use a structure theorem (factors: Kronecker -> compact-extensions -> weak-mixing) for MPS. Later: Furstenberg-Katznelson density-IP Szemeredi (1978); Bergelson-Leibman polynomial Szemeredi (1996); Host-Kra / Ziegler structure theorem (2005, Annals); Green-Tao primes-APs (2008) using a transference to pseudorandom sets.

**Proof idea / process:** Encode E via its indicator 1_E in l^infinity(Z). Define a shift-invariant finitely-additive density-like functional on the orbit closure of 1_E. By Krylov-Bogolyubov, extend to a T-invariant probability measure mu on the closure X = {-1, 0, 1}^Z / shift. Let A = {omega in X : omega(0) = 1}. Then mu(A) = d*(E), and simultaneous membership of {omega_0, omega_{n_1}, ..., omega_{n_k}} in A ↔ {0, n_1, ..., n_k} in E's shift translates to intersections of T^{-n_i} A.

**Impact:** Ergodic proof of Szemeredi; Furstenberg-Katznelson multidim Szemeredi (1978); polynomial Szemeredi (Bergelson-Leibman 1996); Host-Kra structure theorem (2005, *Annals*); Green-Tao APs in primes (2008) — relies on the transference heuristic descended from Furstenberg. Now a standard bridge between combinatorial number theory and ergodic theory. Used in Conze-Lesigne, Ziegler nilsequences.

**Sources:**
- Furstenberg, "Ergodic behavior of diagonal measures and a theorem of Szemeredi on arithmetic progressions," J. d'Analyse Math 31 (1977): https://doi.org/10.1007/BF02813304
- Furstenberg, *Recurrence in Ergodic Theory and Combinatorial Number Theory* (Princeton 1981).
- Bergelson-Leibman, "Polynomial extensions of van der Waerden's and Szemeredi's theorems," J. AMS 9 (1996): https://doi.org/10.1090/S0894-0347-96-00194-4
- Host-Kra, "Nonconventional ergodic averages and nilmanifolds," Annals of Math 161 (2005) — arXiv:math/0403212
- Kra, "The Green-Tao theorem on arithmetic progressions in the primes: an ergodic point of view," Bull. AMS 43 (2006): https://www.ams.org/journals/bull/2006-43-01/

**Technique tag:** NEW — `ergodicCorrespondence(positive-density subset E of Z) -> measurePreservingSystemWithEquivalentRecurrence` — translate combinatorial density / recurrence statements about E to measure-preserving dynamics via a weak-* limit, where ergodic structure theorems become available. *Inherits: compactnessArgument (Krylov-Bogolyubov weak-* limit), axiomatizeFromInstances (measure-preserving system axioms).*

---

### Nash-Moser implicit function theorem (1956 Nash, 1966 Moser; Hamilton 1982 tame category)

**Statement / description:** For a smooth map F between tame Frechet spaces (e.g., C^infinity sections of a vector bundle) whose linearization L = DF(u) has a tame right-inverse with a loss of finitely many derivatives, the equation F(u) = v is solvable for v near F(u_0) by a rapidly convergent modified Newton iteration that compensates the derivative loss with smoothing projections.

**Discovery trigger:** Nash (1956): the isometric embedding problem — any C^k Riemannian manifold (M, g) embeds isometrically in some R^N. The linearized embedding equation loses a derivative (solving L u = v requires v to be one derivative smoother than u). Classical contraction-mapping IFT fails because successive Newton iterations lose derivatives indefinitely. Nash introduced smoothing regularization to compensate.

**Thought process / lineage:** Predecessors: Kolmogorov (1954) and Arnold (1963) KAM theorem — small-divisor problems in Hamiltonian perturbation theory; overcome derivative loss from small divisors (1 / (k · omega)) by super-exponentially convergent Newton. Moser (1966) unified Nash and KAM. Hamilton's 1982 *Bull. AMS* paper gave the tame-Frechet abstract framework. Later applications: Hormander's parametrix + Nash-Moser for nonlinear elliptic; Ekeland-Severi weak-KAM; Ekeland's approach to bifurcation; Sergeraert's ILH geometry; Chaperon and Thom-Mather work on singularities.

**Proof idea / process:** Standard Newton in Banach space: u_{n+1} = u_n - L(u_n)^{-1} F(u_n), quadratic convergence ||u_{n+1} - u|| <= C ||u_n - u||^2 if L is invertible in one norm. In Frechet/tame: L(u_n)^{-1} loses r derivatives — after n iterations, infinitely many. Fix: introduce smoothing operators S_{theta_n} that restrict to frequencies <= theta_n. Modified Newton: u_{n+1} = u_n - S_{theta_n} L(u_n)^{-1} F(u_n) with theta_n growing fast (theta_n = theta_0^{(3/2)^n} works). The "Nash" estimate: ||S_theta - I|| applied to a C^{k+r} function is theta^{-r} * C^{k+r}-norm, giving super-exponential decay at the cost of a fixed derivative loss that is absorbed by the quadratic convergence.

**Impact:** Nash's C^infinity isometric embedding theorem; KAM theorem (Kolmogorov-Arnold-Moser on persistence of quasi-periodic tori under Hamiltonian perturbation); Hamilton-Nash-Moser applied to Ricci-flow short-time existence (DeTurck preferred but Nash-Moser was pioneering); free-boundary problems (water waves, Shatah-Wu); Eliasson's KAM for Schrodinger with quasi-periodic potential. Standard reference for any problem where the linearized inverse loses derivatives.

**Sources:**
- Hamilton, "The inverse function theorem of Nash and Moser," Bull. AMS 7 (1982): https://www.ams.org/journals/bull/1982-07-01/S0273-0979-1982-15004-2/
- Moser, "A rapidly convergent iteration method and non-linear partial differential equations," Ann. Scuola Norm. Sup. Pisa 20 (1966).
- Saint-Raymond, "Un théorème de fonctions implicites dans des espaces de Fréchet," J. Funct. Anal. 87 (1989).
- Berti-Bolle, "A Nash-Moser approach to KAM theory," Fields Institute Communications 2015 — arXiv:1404.3122
- nLab: Nash-Moser theorem — https://ncatlab.org/nlab/show/Nash-Moser+theorem

**Technique tag:** NEW — `nashMoserFastNewton(tame Frechet map F, linearization with tame right-inverse losing r derivatives) -> smoothSolutionViaSmoothedIteration` — solve F(u) = v in a Frechet space by modified Newton with smoothing projections, compensating derivative loss via super-exponentially convergent iterations. *Inherits: contractionFixedPoint (modified Newton), frequencyDecomposition (smoothing S_theta is a frequency cutoff).*

---

### Gromov quasi-isometry invariance and polynomial-growth theorem (1981, Mikhael Gromov)

**Statement / description:** A map f: X -> Y between metric spaces is a quasi-isometry if there exist A, B, C with (1/A) d_X(x, x') - B <= d_Y(f(x), f(x')) <= A d_X(x, x') + B and every point of Y is within C of f(X). Quasi-isometry is the correct notion of "coarse equivalence" for finitely generated groups (Cayley graphs under different finite generating sets are QI). Gromov's polynomial growth theorem (1981): a finitely generated group with polynomial growth (ball size <= C r^d) is virtually nilpotent. This is a deep example of QI invariance because growth is a QI-invariant.

**Discovery trigger:** Milnor (1968) and Wolf (1968) showed that solvable groups of polynomial growth are virtually nilpotent; Milnor's problem asked whether every group of polynomial growth is virtually nilpotent. Gromov (1981) resolved this via a radical new idea: rescale the Cayley graph and take a Gromov-Hausdorff limit, obtaining a locally compact topological group, then apply Montgomery-Zippin to resolve Hilbert's fifth problem on that limit.

**Thought process / lineage:** Predecessors: Hilbert's Fifth Problem solved by Montgomery-Zippin-Gleason (1952) — locally compact topological groups with small-dimension manifold structure are Lie groups. Svarc-Milnor lemma (1955/1968): if G acts properly discontinuously and cocompactly by isometries on a metric space X, then G is QI to X. Milnor, Wolf, Bass (1972) handled growth for solvable groups. Gromov combined rescaling + Gromov-Hausdorff compactness + H5 rigidity. Later: Kleiner's 2010 harmonic-function-based proof of polynomial growth (arXiv:0710.4593); Shalom-Tao quantitative polynomial-growth theorem (2010).

**Proof idea / process:** (a) Assume G has polynomial growth of degree d. (b) Rescale Cayley graph by 1/r_n with r_n -> infinity. (c) By polynomial growth, the rescaled balls are uniformly finite-dimensional (Gromov-Hausdorff pre-compact — Gromov's precompactness theorem). Extract a subsequential Gromov-Hausdorff limit (X, d). (d) The limit X admits a transitive action by a locally compact group H extending G. (e) Montgomery-Zippin: H is a Lie group. (f) Use the virtual-nilpotent structure of H and descent to G via properties preserved under QI.

**Impact:** Established geometric group theory as a discipline centered on QI invariants. Invariants: growth, hyperbolic group (Gromov 1987), number of ends (Stallings), asymptotic dimension, Dehn function. Rigidity results: Mostow (hyperbolic-manifold fundamental groups), Pansu (Carnot groups), Eskin-Farb (irreducible higher-rank symmetric spaces). QI classification of nilpotent groups (Pansu 1989), hyperbolic 3-manifold groups (Agol 2013). Motivates cube complexes, CAT(0) geometry, Rips complexes, boundaries-at-infinity.

**Sources:**
- Gromov, "Groups of polynomial growth and expanding maps," Publ. Math. IHES 53 (1981): https://www.numdam.org/item/PMIHES_1981__53__53_0/
- Kleiner, "A new proof of Gromov's theorem on groups of polynomial growth," J. AMS 23 (2010) — arXiv:0710.4593
- de la Harpe, *Topics in Geometric Group Theory* (Chicago Lectures 2000).
- Druţu-Kapovich, *Geometric Group Theory* (AMS Colloquium 63, 2018).
- MacTutor biographical: https://mathshistory.st-andrews.ac.uk/Biographies/Gromov/

**Technique tag:** NEW — `rescaleForAsymptoticGeometry(finitely-generated group / metric space, scaling sequence r_n -> infinity) -> gromovHausdorffLimitSpaceWithGroupStructure` — take a Gromov-Hausdorff limit of rescaled Cayley graphs to reveal large-scale geometric structure (asymptotic cone / coarse limit), then apply rigidity theorems (Montgomery-Zippin, Pansu) on the limit. *Inherits: compactnessArgument (GH-precompactness), structuralIsomorphism (QI as a coarse equivalence).*

---

### Floer homology via pseudo-holomorphic curves (1988, Andreas Floer)

**Statement / description:** For a compact symplectic manifold (M, omega) and a pair (L_0, L_1) of transverse Lagrangian submanifolds, define a chain complex CF(L_0, L_1) generated by intersection points L_0 ∩ L_1. The boundary operator counts pseudo-holomorphic strips u: R × [0,1] -> M with u(·, 0) in L_0, u(·, 1) in L_1, converging to intersection points at ±infinity. Its cohomology HF(L_0, L_1) is invariant under Hamiltonian isotopy of each L_i. The Arnold conjecture (lower bound on fixed-point count of a Hamiltonian diffeomorphism by sum of Betti numbers) follows.

**Discovery trigger:** Arnold conjecture: a Hamiltonian diffeomorphism phi of a compact symplectic manifold has at least sum dim H_k(M) fixed points. Conley-Zehnder (1983) proved it for tori. Floer sought a general Morse-theoretic approach using the symplectic action functional (which has neither lower bound nor PS compactness in the naive sense).

**Thought process / lineage:** Predecessors: Gromov's compactness theorem for pseudo-holomorphic curves (1985, Invent. Math.) — moduli spaces of J-hol curves are compact modulo bubbling + broken trajectories. Witten's 1982 Morse-theoretic reformulation — Morse complex via counting gradient flow lines. Conley-Zehnder (1983) and Hofer (1988). Floer combined: symplectic action as a generalized Morse function (despite being unbounded), J-hol curves as "gradient flow lines" of A with respect to an L^2 metric determined by J. Later: Fukaya category (1993); Seiberg-Witten-Floer (Kronheimer-Mrowka); embedded contact homology (Hutchings); symplectic cohomology; wrapped Fukaya.

**Proof idea / process:** Choose an almost-complex structure J compatible with omega. Lagrangian intersection points x in L_0 ∩ L_1 are the critical points of A on a suitable path space. The L^2-gradient of A is d u / d s + J(u) (d u / d t - X_H(u)) for strips u(s, t); zero-gradient solutions are pseudo-holomorphic strips. (a) Generic J makes all strips Fredholm-regular (transversality). (b) Index-1 moduli M(x, y) / R are 0-dim manifolds (ell(y) - ell(x) = 1); count signed points. (c) Define d x = sum (# M(x, y)) · y. Gromov compactness + gluing: d^2 x corresponds to broken strips entering a common index-2 stratum, whose boundary cancels pairwise ⟹ d^2 = 0. (d) A symplectic/Hamiltonian isotopy of L_0 induces a chain homotopy — homology is an invariant.

**Impact:** Proof of the Arnold conjecture in wide generality (Floer for monotone Lagrangians, later Fukaya-Oh-Ohta-Ono 2009 and Abouzaid-Blumberg for general). Symplectic topology as a subject. Fukaya category and its role in homological mirror symmetry (Kontsevich 1994). Seiberg-Witten-Floer homology → proof of triangulation conjecture (Manolescu 2013, arXiv:1303.2354, *J. AMS* 2016). Heegaard Floer (Ozsvath-Szabo) and knot Floer — tied to low-dimensional topology, concordance, surgery. Embedded contact homology (Hutchings-Taubes) resolves the Weinstein conjecture in dim 3.

**Sources:**
- Floer, "Morse theory for Lagrangian intersections," J. Differential Geom. 28 (1988): https://projecteuclid.org/euclid.jdg/1214442477
- Floer, "Symplectic fixed points and holomorphic spheres," Comm. Math. Phys. 120 (1989).
- Fukaya-Oh-Ohta-Ono, *Lagrangian Intersection Floer Theory: Anomaly and Obstruction*, Part I-II (AMS-IP Studies 2009).
- McDuff-Salamon, *J-holomorphic Curves and Symplectic Topology*, 2nd ed. (AMS Colloquium 52, 2012).
- Auroux, "A beginner's introduction to Fukaya categories," arXiv:1301.7056
- nLab: Floer homology — https://ncatlab.org/nlab/show/Floer+homology

**Technique tag:** NEW — `floerHomologyOnModuliOfHolomorphicCurves(symplectic manifold (M, omega), Lagrangian pair or Hamiltonian) -> homologicalInvariantViaHolomorphicStrips` — count pseudo-holomorphic curves between critical points of the symplectic action functional, using Gromov compactness + gluing to build a chain complex whose cohomology is a Hamiltonian-isotopy invariant. *Inherits: flowWithSurgery (gradient-like moduli compactification), obstructionClass (Betti-number lower bound), spectralSequenceCompute (action filtration gives a spectral sequence).*

---

### Tropicalization map (1980s Bergman, Sturmfels 2002, Mikhalkin 2005, Viro 1984 for patchworking)

**Statement / description:** For a subvariety V ⊂ (C*)^n, its tropicalization trop(V) ⊂ R^n is the image of V under coordinate-wise valuation log|·|_t as t -> 0 (equivalently, the limit of amoeba(V_t) for a family V_t). trop(V) is a polyhedral complex of dimension dim V satisfying a balancing condition. Tropical curves (dim 1) are metric graphs with integer edge weights and vertex balance. Mikhalkin's correspondence theorem (2005): the number of plane tropical curves of genus g and degree d through 3d-1+g points equals the classical Gromov-Witten number of such curves in P^2.

**Discovery trigger:** Viro (1984) sought a combinatorial method to construct real algebraic curves with prescribed topology — patchworking — which implicitly uses tropical geometry. Bergman (1971) defined logarithmic limit sets (today's tropical varieties). Sturmfels-Speyer-Mikhalkin (2000-05) connected these to GW theory; Itenberg-Mikhalkin-Shustin (2007) to real enumerative geometry.

**Thought process / lineage:** Predecessors: Bergman's logarithmic limits of algebraic varieties (1971); Kapranov's non-archimedean analytic view (Berkovich 1990); Maslov dequantization (1990s) — (a, b) -> a + b replaced by max; Viro's patchworking (1984, *Izvestiya*). Sturmfels popularized via solving-polynomial-systems motivations; Mikhalkin's 2003-05 *J. AMS* papers connected tropical curves to GW enumeration; Gathmann-Markwig, Nishinou-Siebert refined the theory. Modern extensions: Kontsevich-Soibelman tropical vertex, Gross-Siebert mirror symmetry via tropical data.

**Proof idea / process:** (a) Replace the field C by a non-archimedean field K = C{{t}} (Puiseux series). (b) Apply valuation val: K* -> R (val(sum a_i t^i) = min{i : a_i ≠ 0}). (c) trop(V) = val(V(K)). (d) Equivalently, for a polynomial f = sum c_I x^I, its tropicalization is trop(f)(x) = min_I (val(c_I) + <I, x>); trop(V(f)) is the non-smooth locus of trop(f) (where the min is attained twice). (e) Balancing at each codim-1 face = degree-preservation across the transition. Mikhalkin's correspondence: classical counts = tropical counts via Newton polygon degeneration.

**Impact:** Enumerative geometry reduced to polyhedral combinatorics (Mikhalkin's GW counts, Welschinger invariants for real curves). Non-archimedean analytic geometry. Tropical linear spaces & matroid theory (Speyer-Sturmfels). Tropical Riemann-Roch (Baker-Norine 2007, Adv. Math.) for divisors on graphs. Huh's 2012 solution of Rota's log-concavity conjecture used tropical / Hodge-theoretic ideas (leading to the Adiprasito-Huh-Katz 2015 breakthrough). Patchworking produces real hypersurfaces with prescribed Betti data — Hilbert's 16th problem. Mikhalkin-Zharkov tropical Jacobians; Brill-Noether theory on graphs.

**Sources:**
- Mikhalkin, "Enumerative tropical algebraic geometry in R^2," J. AMS 18 (2005) — arXiv:math/0312530
- Maclagan-Sturmfels, *Introduction to Tropical Geometry* (AMS Graduate Studies 161, 2015): https://bookstore.ams.org/gsm-161
- Viro, "Patchworking real algebraic varieties," preprint 1994, arXiv:math/0611382 (retrospective)
- Itenberg-Mikhalkin-Shustin, *Tropical Algebraic Geometry*, Oberwolfach Seminars 35, 2nd ed. (Birkhauser 2009).
- Gathmann, "Tropical algebraic geometry," Jber. DMV 108 (2006) — arXiv:math/0601322
- nLab: tropical geometry — https://ncatlab.org/nlab/show/tropical+geometry

**Technique tag:** NEW — `tropicalize(subvariety V over non-archimedean field, valuation map) -> polyhedralCombinatorialShadow` — replace an algebraic variety by its valuation image (a balanced rational polyhedral complex); enumerative, moduli, and topological invariants are computable combinatorially on the tropical shadow. *Inherits: structuralIsomorphism (tropical-classical correspondence), reduceToCanonicalForm (Newton polytope normal form).*

---

### Harmonic map heat flow (Eells-Sampson 1964) — EXAMPLE extending `flowWithSurgery`

**Eells-Sampson harmonic map flow** (1964, James Eells and J.H. Sampson): Given a map f: M -> N between compact Riemannian manifolds with N of non-positive sectional curvature, the flow d f / d t = tau(f) (tension field) converges to a smooth harmonic map homotopic to f as t -> infinity. This *proves the existence of harmonic representatives* in any homotopy class — a direct variational result via flow rather than direct minimization (which fails when the energy is not lower-semicontinuous on weak-limit sequences). Negative curvature of N is essential: the Bochner formula gives |d f|^2 a sub-heat-equation inequality, which combined with the maximum principle yields a priori bounds preventing finite-time blow-up. **Example note:** this is an archetype of `flowWithSurgery` where no surgery is needed — the obstruction to non-convergence (curvature of target) is geometric not analytic. Sacks-Uhlenbeck (1981) handle target S^2 by explicit bubbling analysis; Struwe (1985) for surfaces. Inherits from Eells-Sampson: Simon-Struwe a priori Bochner estimates; Hamilton (1975) nonlinear-heat-equation survey inspired Hamilton's later Ricci flow. *Inherited: flowWithSurgery. Added: target-curvature sign as a convergence criterion.*

**Source:** Eells-Sampson, "Harmonic mappings of Riemannian manifolds," Amer. J. Math. 86 (1964): https://www.jstor.org/stable/2373037 ; Hamilton, *Harmonic Maps of Manifolds with Boundary*, Springer LNM 471 (1975).

---

### Kahler-Ricci flow and analytic MMP (Song-Tian / Tsuji 1988 / Cao 1985) — EXAMPLE extending `flowWithSurgery`

**Kahler-Ricci flow** (H.D. Cao 1985; Tsuji 1988): On a Kahler manifold (X, omega), the flow d omega / d t = -Ric(omega) preserves the Kahler class (mod first Chern class). Cao reproved Yau's Calabi-conjecture solution by flowing on a canonical Kahler class. Song-Tian (2006-09, *Invent. Math.*; arXiv:0909.4898) developed an "analytic minimal model program": on a projective manifold, Kahler-Ricci flow with finite-time singularity analytically realizes divisorial contractions and flips of the classical MMP; the long-time limit is either the canonical model (if K_X is big) or a flat Calabi-Yau fibration. **Example note:** connects `flowWithSurgery` directly to algebraic-geometric MMP. Surgery in the analytic sense = algebraic divisorial contraction. Work of Song-Weinkove, Tian-Zhang, Gross-Tosatti-Zhang extends to collapsing. *Inherited: flowWithSurgery. Added: algebraic-geometric birational program matched to analytic singularities.*

**Source:** Cao, "Deformation of Kahler metrics to Kahler-Einstein metrics on compact Kahler manifolds," Invent. Math. 81 (1985) ; Song-Tian, "The Kahler-Ricci flow through singularities," Invent. Math. 207 (2017) — arXiv:0909.4898 ; Song-Weinkove, "An introduction to the Kahler-Ricci flow," in *An Introduction to the Kahler-Ricci Flow*, LNM 2086 (2013).

---

### Yang-Mills flow on 4-manifolds (Donaldson 1985) — EXAMPLE extending `flowWithSurgery`

**Yang-Mills flow** (S.K. Donaldson 1985, *J. Differential Geom.*; Uhlenbeck-Yau 1986): On a Hermitian vector bundle E over a compact Kahler manifold, the flow d A / d t = -d_A^* F_A is the L^2-gradient flow of the Yang-Mills functional ||F_A||^2. Donaldson used Yang-Mills flow to prove that a stable holomorphic bundle admits a Hermite-Einstein metric (Donaldson-Uhlenbeck-Yau theorem). Variants: Hermitian-Einstein flow for bundles, anti-self-dual instanton equation in dim 4. Sacks-Uhlenbeck removable-singularity theorem allows "bubbling off" of energy in point singularities. **Example note:** classical `flowWithSurgery` application where surgery = analytic removal of bubble points. The monotone quantity is the Yang-Mills energy itself; the Uhlenbeck compactness theorem is the analogue of Gromov compactness for J-hol curves. Foundation for Donaldson invariants and Floer instanton homology. *Inherited: flowWithSurgery, conservedQuantity. Added: instanton bubble analysis + gauge-theoretic formulation.*

**Source:** Donaldson, "Anti self-dual Yang-Mills connections over complex algebraic surfaces and stable vector bundles," Proc. LMS 50 (1985) ; Donaldson-Kronheimer, *The Geometry of Four-Manifolds* (Oxford Math. Mono. 1990) ; Rade, "On the Yang-Mills heat equation in two and three dimensions," J. Reine Angew. Math. 431 (1992).

---

### Stein-Tomas restriction theorem (1975) — EXAMPLE extending `frequencyDecomposition`

**Stein-Tomas restriction** (E.M. Stein 1967, P. Tomas 1975): For a smooth compact hypersurface S ⊂ R^n with everywhere non-vanishing Gaussian curvature (e.g., sphere), the Fourier restriction operator R: L^p(R^n) -> L^2(S, d sigma) is bounded for p in the range 1 <= p <= 2(n+1)/(n+3). Dually, the extension operator E: L^2(S) -> L^{2(n+1)/(n-1)}(R^n) is bounded. **Example note:** this is the archetypal curved-frequency-surface constraint, and the direct ancestor of the Stein restriction conjecture (fully open: the sharp range for the sphere in R^3 is p <= 4, proved only by Guth 2016 with polynomial partitioning). A flagship example of `frequencyDecomposition` where the restriction to a curved subset of frequency space is itself a nontrivial *mapping* problem. Modern refinements: Bourgain-Guth multilinear + polynomial partitioning; Bourgain-Demeter decoupling (entry 2 above) as a square-function refinement. *Inherited: frequencyDecomposition. Added: curvature as a regularizing condition on the frequency support.*

**Source:** Tomas, "A restriction theorem for the Fourier transform," Bull. AMS 81 (1975): https://www.ams.org/journals/bull/1975-81-02/S0002-9904-1975-13790-6/ ; Stein, *Harmonic Analysis: Real-Variable Methods, Orthogonality, and Oscillatory Integrals*, Princeton 1993, Ch. IX ; Tao, "Some recent progress on the restriction conjecture," arXiv:math/0303136.

---

### Ekeland variational principle (1974) — EXAMPLE extending `contractionFixedPoint` / `compactnessArgument`

**Ekeland variational principle** (I. Ekeland 1974): Let (X, d) be a complete metric space and F: X -> R ∪ {+infinity} lower-semicontinuous, bounded below, proper. For any epsilon > 0 and x_0 with F(x_0) < inf F + epsilon, there exists x* in X such that: F(x*) <= F(x_0), d(x*, x_0) <= 1, and F(x*) < F(x) + epsilon d(x, x*) for all x ≠ x*. **Example note:** a perturbed-minimum existence principle — even without compactness, one can find a point that is "almost a minimum and almost stationary". The "almost-minimum + minorization by a Lipschitz penalty" is a workable substitute for strict minima. Applications: existence of approximate critical points for a C^1 functional (PS-like sequences), Brezis-Ekeland-Hofer applications to convex analysis, dual approach to nonlinear eigenvalue problems, generalizations of Banach's fixed point (Caristi's fixed-point theorem is equivalent to Ekeland). *Inherited: contractionFixedPoint, compactnessArgument. Added: works in arbitrary complete metric spaces without reflexivity.*

**Source:** Ekeland, "On the variational principle," J. Math. Anal. Appl. 47 (1974): https://doi.org/10.1016/0022-247X(74)90025-0 ; Ekeland, "Nonconvex minimization problems," Bull. AMS 1 (1979): https://www.ams.org/journals/bull/1979-01-03/S0273-0979-1979-14595-6/ ; Aubin-Ekeland, *Applied Nonlinear Analysis* (Wiley 1984).

---

### Schramm-Loewner evolution (SLE, Schramm 2000) — EXAMPLE extending `physicsToPDE` / `interpolateAndContinue`

**Schramm-Loewner evolution** (Oded Schramm 2000, *Israel J. Math.* arXiv:math/9904022): The family SLE_kappa of random curves in the upper half-plane is defined by Loewner's classical equation d g_t(z) / d t = 2 / (g_t(z) - sqrt(kappa) B_t) where B_t is standard Brownian motion. For a scaling limit of a 2D statistical-mechanics critical system (loop-erased random walk at kappa=2, Ising interfaces at kappa=3, percolation at kappa=6, uniform spanning tree at kappa=8), conformal invariance and a domain Markov property *uniquely* determine the law as an SLE. **Example note:** extends `physicsToPDE` in a probabilistic direction — the phenomenological scaling limit is *characterized* by a PDE (Loewner's chordal equation), driven by a one-parameter family of stochastic drivers, and the parameter kappa encodes the universality class. Extends `interpolateAndContinue` because the continuous family kappa is an analytic interpolation through discrete lattice-model universality classes. Lawler-Schramm-Werner series proved conformal invariance for LERW, UST; Smirnov proved it for percolation (2001) and Ising (2010). Fields Medal: Werner 2006, Smirnov 2010, Schramm (posthumously honored). *Inherited: physicsToPDE, interpolateAndContinue. Added: stochastic driver as a classifier of universality classes.*

**Source:** Schramm, "Scaling limits of loop-erased random walks and uniform spanning trees," Israel J. Math. 118 (2000) — arXiv:math/9904022 ; Lawler, *Conformally Invariant Processes in the Plane* (AMS Math. Surveys 114, 2005) ; Werner, "Random planar curves and Schramm-Loewner evolutions," in *Ecole d'Ete de Probabilites de St-Flour XXXII*, LNM 1840 (2004) — arXiv:math/0303354.

---

## Summary tables

### Breakdown by technique-proposal vs. example-extension

**New techniques proposed (14):**

| # | Proposed technique | Cluster fit |
|---|---|---|
| 1 | `dyadicDecomposition` | Cluster 4 (Approximation) — refines `frequencyDecomposition` |
| 2 | `decoupleByDyadicCaps` | Cluster 4 — inherits dyadic |
| 3 | `curvatureMonotonicityClassifier` (MCF monotonicity) | Cluster 8 — refines `flowWithSurgery` |
| 4 | `propagateSingularitiesAlongBicharacteristics` | Cluster 4 or new "Microlocal" — new style |
| 5 | `currentMassMinimize` | Cluster 6 (Topology/Obstruction) or new "Geometric measure" |
| 6 | `mountainPassMinimax` | NEW Cluster 13 "Variational / Calculus of Variations" candidate, or Cluster 8 |
| 7 | `sieveByMinimizingQuadraticForm` | Cluster 11 (Probabilistic/Counting) — sieve is a counting method |
| 8 | `majorMinorArcDecomposition` (circle method) | Cluster 9 (Cross-Field Transfer) — refines `complexAnalysisToIntegers` |
| 9 | `shearerEntropyCount` | Cluster 11 — entropy as counting |
| 10 | `ergodicCorrespondence` | Cluster 9 or new "Ergodic" — cross-field transfer combinatorics↔dynamics |
| 11 | `nashMoserFastNewton` | Cluster 8 (Iteration) — modified Newton |
| 12 | `rescaleForAsymptoticGeometry` | Cluster 6 (Topology) — Gromov-Hausdorff compactness |
| 13 | `floerHomologyOnModuliOfHolomorphicCurves` | Cluster 12 (Homological/Categorical) or Cluster 6 |
| 14 | `tropicalize` | Cluster 9 (Transfer) or Cluster 5 (Abstraction) — structural translation |

**Example extensions (6):**

| # | Example | Existing technique tag |
|---|---|---|
| 15 | Harmonic map heat flow (Eells-Sampson) | `flowWithSurgery` |
| 16 | Kahler-Ricci flow & analytic MMP (Cao, Song-Tian) | `flowWithSurgery` |
| 17 | Yang-Mills flow (Donaldson, Uhlenbeck-Yau) | `flowWithSurgery` |
| 18 | Stein-Tomas restriction (Tomas 1975) | `frequencyDecomposition` |
| 19 | Ekeland variational principle | `contractionFixedPoint` / `compactnessArgument` |
| 20 | Schramm-Loewner evolution | `physicsToPDE` / `interpolateAndContinue` |

### Researcher flags

1. **Cluster proliferation risk.** Six or seven of the proposed new techniques (variational/microlocal/geometric-measure/sieve/ergodic/symplectic) sit awkwardly in Cluster 6, 8, or 9. The researcher may consider whether to add:
   - Cluster 13 *Variational & Critical-Point Methods* (Ekeland, mountain-pass, Morse, direct method)
   - Cluster 14 *Microlocal & Phase-Space Analysis* (wavefront set, pseudo-differential, FIO, parametrix construction — already hinted at by the Hormander entry under `reduceToCanonicalForm`/`frequencyDecomposition` in Round 1)
   - Merge the Round-2 geometric flows into an expanded `flowWithSurgery` description rather than creating sub-techniques. I took the middle path: promoted MCF monotonicity (because it's a template separately applicable outside flows) but kept MCF / YMF / harmonic map flow / Kahler-Ricci flow *as examples* of `flowWithSurgery`.

2. **Circle method vs. `complexAnalysisToIntegers`.** The Round-1 technique has "Helfgott ternary Goldbach" as a one-line example; I recommend promoting the Hardy-Littlewood circle method to its own technique because the Farey/major-minor arc dissection is distinct from Dirichlet-series contour-shifting (different input class — exponential sums over a structured set vs. L-function zeros).

3. **Tracy-Widom.** Already present in Round 1 under `interpolateAndContinue` and `frequencyDecomposition` examples. I added SLE (Schramm) as a *separate* universality-class example and did not duplicate TW.

4. **Dyadic decomposition vs. `frequencyDecomposition`.** These are different: `frequencyDecomposition` returns continuous coefficients of a basis expansion; `dyadicDecomposition` returns a *sequence of functions* (frequency-localized blocks, not coefficients). The square-function norm operates on blocks as functions in physical space. I propose `dyadicDecomposition` as a new technique that *inherits from* `frequencyDecomposition` rather than replacing it.

5. **Decoupling + multilinear Kakeya.** I included decoupling but deliberately did NOT add a separate entry for "multilinear Kakeya" (Bennett-Carbery-Tao 2006). It is a *lemma* consumed by decoupling; if the engineer wants it as a stand-alone technique, the entry should cite Bennett-Carbery-Tao, *Acta Math* 196 (2006), arXiv:math/0509262. Flagged for researcher to decide.

6. **Varifolds vs. currents.** I wrote `currentMassMinimize` based on Federer-Fleming. Allard's varifold regularity is a separate technique that could warrant its own entry: first-variation formula + monotonicity + tilt-excess decay (Allard, Annals 95, 1972). If the researcher wants a varifold technique, use tag `varifoldFirstVariation(integral varifold V, test vector field X) -> regularityViaMonotonicity`.

7. **Direct method of calculus of variations.** I folded this into the mountain-pass entry's preamble rather than giving it a separate slot — direct method is the "coercive + wlsc + reflexive space" recipe, which is a trivial existence of minimizers. If the researcher wants a dedicated entry, tag it `directMethodCalculusVariations(coercive lsc functional on reflexive Banach space) -> minimizer`; primary source Tonelli (1921), textbook Dacorogna *Direct Methods in the Calculus of Variations* (Springer 2008).

8. **Brun sieve and large sieve.** I wrote up Selberg sieve as the central sieve technique. Brun's sieve (1919) and the large sieve (Linnik 1941 / Renyi / Bombieri-Vinogradov) are historically important and could each be separate entries OR additional Selberg-sieve examples. Folded as pipe-dream here; recommend the researcher judge whether to expand.

9. **KAM theorem as stand-alone.** I folded KAM into Nash-Moser because they share the super-exponentially-convergent Newton machinery; the KAM theorem on persistence of invariant tori could alternatively get its own entry (Kolmogorov 1954, Arnold 1963). If so: tag `kamPersistsInvariantTori(integrable Hamiltonian + small Diophantine-frequency perturbation) -> measure-positive set of persistent tori`.

10. **Svarc-Milnor lemma.** Folded into the Gromov entry as predecessor but not given its own slot. Svarc-Milnor is the key "proper cocompact isometric action ⟹ QI to the acted-upon space" lemma, deserves its own example if an engineer wants to add it.

11. **Viro patchworking.** Folded into the tropicalization entry; one could argue it's a separate combinatorial-to-real technique. Kept as a single entry.

12. **Tracy-Widom universality beyond GUE.** This is already cited in Round 1. For "local eigenvalue statistics" beyond GUE, the key modern technique is the Erdős-Schlein-Yau / Tao-Vu "four-moment theorem" + local relaxation flow (arXiv:0906.0510). Not written up as a separate entry because it largely functions as a PDE-heat-flow argument matched to Dyson Brownian motion — an example of `flowWithSurgery` with a probabilistic target. Flagged for researcher/engineer to add as a `flowWithSurgery` example if desired.
