# NS-Scout — 3D Navier–Stokes Global Regularity: reconnaissance

**Role**: iteration-4 scout for a knowledge-graph-driven discovery attempt on the Clay Millennium problem for 3D incompressible Navier–Stokes.
**Graph source**: `/Users/primetrce/Documents/maths/knowledge_graph.json` (752 nodes, 62 techniques, 12 toolbox clusters).
**Lesson carried from iter 3**: novelty appears where an OPEN problem meets known technique, not where a solved theorem meets an unused technique. The NS graph footprint is essentially empty (grep of `knowledge_graph.json` and chapters 01–07 returns only Stokes' theorem, a different object). The scout's job is therefore to populate the relevant terrain before any theorist tries to push in.

---

## §1 — Problem statement

Fix viscosity ν > 0 and a domain Ω ∈ {ℝ³, 𝕋³}. Given divergence-free Schwartz (or C^∞ periodic) initial datum u₀ : Ω → ℝ³ with ∇·u₀ = 0, consider the incompressible Navier–Stokes system

    ∂ₜu + (u·∇)u = −∇p + νΔu,     ∇·u = 0,     u|_{t=0} = u₀,                    (NS)

with u : [0, ∞) × Ω → ℝ³ the velocity and p : [0, ∞) × Ω → ℝ the pressure (determined up to a constant by the incompressibility constraint via p = (−Δ)⁻¹ ∇·((u·∇)u), i.e. the Leray projection eliminates p). The Clay prize formulation asks, in one of two equivalent affirmative forms:

  (A) **Global smooth existence.** For every such u₀ there exists u ∈ C^∞([0, ∞) × Ω) solving (NS) with finite kinetic energy ∫|u(t,·)|² dx bounded in t.
  (B) **Finite-time blowup.** Negate (A): exhibit smooth decaying u₀ and a finite T★ < ∞ such that ‖u(t)‖_{H^s} → ∞ as t ↑ T★ for some s.

The Clay problem is open; either (A) or (B) is an accepted resolution.

The surrounding theorem landscape has several components that must not be confused with (A):

- **Global weak solutions** (Leray 1934, Hopf 1951). For any u₀ ∈ L² divergence-free, there exists u ∈ L^∞_t L²_x ∩ L²_t H¹_x satisfying (NS) in distributions and the energy inequality ½‖u(t)‖²_{L²} + ν∫₀ᵗ‖∇u‖²_{L²} ≤ ½‖u₀‖²_{L²}. Existence: settled. Regularity & uniqueness of Leray–Hopf: open.
- **Uniqueness of distributional weak solutions**, dropping the energy inequality. Buckmaster–Vicol 2019 used convex integration to produce infinitely many non-conservative weak solutions with prescribed kinetic energy profile. In the Leray–Hopf class (with energy inequality) uniqueness was also disproved, but only for *forced* NSE (Albritton–Brué–Colombo 2022). Uniqueness for *unforced* Leray–Hopf is still open and is the true companion of the Clay problem.
- **Smoothness of weak Leray–Hopf** = the Clay statement, i.e. any energy-class weak solution with smooth initial data is actually smooth.
- **2D case**: Ladyzhenskaya 1959, Ladyzhenskaya–Solonnikov, Lions: globally smooth. The barrier is the scaling law and the vorticity transport structure; neither carries to 3D.
- **Domain variants**: periodic 𝕋³, whole-space ℝ³, bounded domain with no-slip. Clay accepts 𝕋³ or ℝ³; bounded-domain with boundary is physically more delicate (boundary-layer separation) and not the Clay target.

---

## §2 — What is known

### A. Local existence and short-time smoothness

Organised by the norm at which the solution is tracked.

1. **Leray 1934**. Weak solutions exist globally in L²; uniqueness fails (or is unknown); some regularity holds on an open set. Method: Galerkin projection + L² energy bound + weak compactness (`t_compactness_argument`, `t_conserved_quantity`). **Not enough**: 2D compactness happens to be just enough because ‖∇u‖² controls ‖u‖^4; in 3D ‖∇u‖² only controls ‖u‖^{6/5}, breaking the closure step.
2. **Fujita–Kato 1964**. Local-in-time smooth solutions for u₀ ∈ Ḣ^{1/2}(ℝ³). Method: heat-semigroup mild formulation u = e^{νtΔ}u₀ − ∫₀ᵗ e^{ν(t−s)Δ}ℙ(u⊗u)(s)ds + contraction-mapping (`t_contraction_fixed_point`, `t_fourier_transform`). Critical scaling: Ḣ^{1/2} is scaling-invariant under u_λ(t,x) = λu(λ²t, λx). **Not enough**: the Picard ball depends on ‖u₀‖_{Ḣ^{1/2}} and the time of existence likewise; no global bound.
3. **Kato 1984**. Same strategy in L³(ℝ³), also scaling-critical. Local in time, small-data global.
4. **Cannone 1995, Planchon 1996, Koch–Tataru 2001**. Local existence in ever-larger critical spaces: Besov Ḃ^{−1+3/p}_{p,∞}, BMO⁻¹ (= (−Δ)^{−1/2}·BMO, the largest known critical space). Method: paraproduct + fixed-point. **Not enough**: small-data global only; large-data time of existence tends to 0 as norm grows.
5. **Regularity of strong solutions**. If u ∈ C([0,T]; H^s) for s > 5/2 then u ∈ C^∞((0,T)×Ω). Bootstrap via (`t_exhaustion_squeeze` + `t_frequency_decomposition`). **Not enough**: needs a priori control of an H^s norm; global control of H^s fails at every s ≥ 1/2 in the large-data regime.

### B. Conditional regularity / blowup criteria

Hypotheses under which blowup is excluded ("if u stays controlled in *this* norm, then u is smooth").

6. **Serrin 1962, Ladyzhenskaya–Prodi–Serrin**. If u ∈ L^p_t L^q_x with 2/p + 3/q ≤ 1, 3 < q ≤ ∞, then u is smooth. All such norms are scaling-subcritical or scaling-critical. Method: energy estimates + embedding + Grönwall.
7. **Beale–Kato–Majda 1984**. Smooth solution to 3D Euler or NSE persists past T iff ∫₀ᵀ ‖ω(s)‖_{L^∞} ds < ∞, where ω = curl u. Method: vorticity transport + log-Sobolev. Parallel companion: **Constantin–Fefferman 1993** geometric depletion — if the vorticity direction ξ = ω/|ω| is Lipschitz (in certain averaged sense) on the high-vorticity region, BKM does not fire.
8. **Escauriaza–Seregin–Šverák 2003** (ESS). If ‖u‖_{L^∞_t L^3_x} < ∞ on [0,T), u extends past T. Replaces the L^{∞,3} endpoint of Serrin. Method: blowup profile limits + Liouville theorem for ancient solutions + unique continuation via Carleman. The critical L^3 norm cannot blow up finitely.
9. **Seregin 2012** refinement. If ‖u‖_{L^∞_t L^3_x} remains bounded, then actually ‖u‖_{L^∞_t L^3_x} is continuous at the first possible singular time; hence blowup in L^3 cannot happen as a clean jump.
10. **Chen–Strain–Tsai–Yau 2008, Dong–Du, Kim–Kozono**. Critical-Besov variants, B^{−1+3/p}_{p,∞}-type criteria. Sharper but same scaling.
11. **Quantitative ESS: Tao 2019** (arXiv:1908.04958). If ‖u‖_{L^∞_t L^3_x} ≤ A on [0,T), then ‖u(t)‖_{H^k} is bounded by a triple exponential in A. Replaces every compactness step by a Carleman-quantitative one (`t_exhaustion_squeeze` made effective). Consequence: if a blowup happens, ‖u(t)‖_{L³} grows at least like (log log log 1/(T−t))^c.
12. **Barker–Prange 2021** (CMP), Palasek 2021 — concentration-to-quantitative-regularity, axi-symmetric sharpening of Tao's bound to a single exponential.

All conditional criteria are scaling-subcritical or borderline-critical. None of them unconditionally global because you cannot establish the critical-norm bound a priori.

### C. Partial regularity

Results about the *size* of the singular set.

13. **Scheffer 1976–77**. Hausdorff dimension of the space–time singular set S(u) for a Leray solution is at most 5/3.
14. **Caffarelli–Kohn–Nirenberg 1982** (CKN). For *suitable* weak solutions (Leray–Hopf + local energy inequality), the 1-dimensional parabolic Hausdorff measure of S(u) is zero. Method: local energy inequality + ε-regularity (`t_compactness_argument` + `t_rescale_for_asymptotic_geometry`). This remains the strongest unconditional regularity result.
15. **Lin 1998, Ladyzhenskaya–Seregin**. Short proofs of CKN via De Giorgi / Moser-style iteration.
16. **Vasseur 2007, Choi–Vasseur**. De Giorgi method for suitable weak solutions, pointwise boundedness away from singular set.

**Barrier**: CKN does not exclude a single space–time point singularity. Removing the remaining point is exactly the Clay problem.

### D. Scaling-critical framework and Tao's supercritical barrier

17. A norm X is *scaling-invariant* if ‖u_λ‖_X = ‖u‖_X for u_λ(t,x)=λu(λ²t,λx). Examples: Ḣ^{1/2}, L³, Ḃ^{−1+3/p}_{p,∞}, BMO⁻¹, L^∞_t L^3_x. Subcritical: H^s, s > 1/2; L²-energy is *supercritical* for 3D (‖u_λ‖_{L²} = λ^{−1/2}‖u‖_{L²}). Subcritical norms are preserved under subtle time-scaling; supercritical are not.
18. **Tao 2009/2014** (Finite-time blowup for an averaged 3D NSE, arXiv:1402.0290). Constructs a frequency-local averaged NSE whose nonlinearity is cascade-hollow and proves finite-time blowup via a self-similar tower-of-frequencies mechanism. Interpretation: any proof of global regularity that *only* uses scaling-invariant (critical or subcritical) functional estimates must fail on the averaged variant and therefore on the true NSE, because the averaged NSE shares those exact estimates. Barrier formalised: new attack must exploit something not preserved by the averaging — probably a geometric, structural, or non-scaling property.

### E. Non-uniqueness / wild solutions

19. **De Lellis–Székelyhidi 2009–2014**. Convex integration for Euler, producing infinitely many energy-admissible weak solutions. Gave the h-principle a PDE face.
20. **Isett 2018, Buckmaster–De Lellis–Szekelyhidi–Vicol 2019**. Onsager conjecture: Euler in C^{1/3−} is non-unique with energy dissipation.
21. **Buckmaster–Vicol 2019** (Annals). Infinitely many *weak* solutions of 3D NSE with the same smooth initial datum, violating neither energy inequality on average nor smoothness constraints except that they live in L²_t L²_x only. Does not contradict Leray–Hopf because these solutions fail the energy inequality.
22. **Albritton–Brué–Colombo 2022** (Annals 196-1). Non-uniqueness of Leray–Hopf solutions for *forced* NSE with a specific vortex-ring forcing, using Vishik's 2D instability vortex. Forced case closed.
23. **Cheskidov–Luo 2022** (Inventiones 229, pp. 987–1054). Sharp non-uniqueness: for any p < 2, infinitely many weak non-Leray–Hopf NSE solutions in L^p_t L^∞_x, matching Serrin-endpoint scaling.
24. **Cheskidov–Luo 2024** (arXiv:2412.09637). Extends sharp non-uniqueness to ℝ³ in scaling-critical spaces.
25. **Stochastic variant**: Hofmanová–Zhu–Zhu, sharp non-uniqueness of stochastic NSE (SIAM J. Math. Anal. 2023).

**Barrier**: convex integration cannot produce smooth-in-x solutions at fixed t because the iteration requires high-frequency Mikado flows whose gradient is unbounded. Any convex-integration-based non-uniqueness destroys H^s for s large — hence compatible with global smoothness.

### F. Blowup of related systems

26. **Tao 2014** averaged 3D NSE: blowup proven. See §2.D.
27. **Hou–Luo 2014** numerical. Axisymmetric Euler in bounded cylinder with boundary develops finite-time singularity at the corner {r=1}∩{z=0} in simulations.
28. **Chen–Hou 2022–2025** (PNAS 2025). Computer-assisted rigorous proof of finite-time nearly-self-similar singularity for 3D axisymmetric Euler in a smooth bounded cylinder with smooth initial data. Interior blowup, not just boundary. Uses stability analysis of a nearly-self-similar approximate profile plus interval arithmetic.
29. **Elgindi 2019/2021** (Ann. Math. 194-3). 3D axisymmetric Euler, no swirl, C^{1,α} initial velocity (not C^∞) develops finite-time singularity in ℝ³. Self-similar profile. Method: Biot–Savart simplification + fundamental model reduction + non-smoothness exploited to give algebraic structure.
30. **De Gregorio model, Constantin–Lax–Majda models, CKM, HL shell, dyadic and GOY models**: blowup proven for many of these 1D/discrete surrogates.

**Barrier for NSE Clay**: every blowup result uses one of (i) a boundary, (ii) non-smooth initial data, (iii) an averaged or truncated nonlinearity, (iv) a lower-dimensional reduction. None exhibits a smooth compactly-supported initial datum on ℝ³ producing a genuine 3D NSE (ν > 0) blowup. The viscous regularising effect is exactly what has resisted every such transfer.

### G. Lower-dimensional / toy models

31. **Dyadic shell models** (Katz–Pavlović 2005, Cheskidov 2008, Cheskidov–Friedlander–Pavlović 2010). Truncated wavelet NSE cascade in which blowup is proved. Sub-critical dissipation ∥v∥_{L²} controls nothing forward. Relation to real NSE: weak — the Mikado-flow non-uniqueness and the shell-model blowup are both "cascade runaway" phenomena suppressed by the true vortex-stretching geometry.
32. **Hyperdissipative NSE** (−Δ)^α, α ≥ 5/4. Global smoothness known (Katz–Pavlović 2002, Tao 2009 log-correction down to α = 5/4). α < 5/4 is open; α = 1 is Clay.
33. **Fractional NSE**, **generalised NSE**, **Boussinesq** with varying dissipation laws.

### H. Probabilistic / statistical hydrodynamics

34. **Flandoli–Romito 2008**, **Flandoli 2011**. Regularisation of 3D NSE by noise in the Markovian-selection sense: stationary measures exist, but they do not imply pathwise smoothness.
35. **Hairer regularity structures 2014** / **Gubinelli–Imkeller–Perkowski paracontrolled calculus 2015**. Meant for subcritical stochastic PDEs (KPZ, Φ⁴₃). 3D NSE is critical for these tools — they do not apply directly.
36. **Hofmanová–Zhu–Zhu 2022+**. Stochastic NSE global weak existence in strong topology.

**Barrier**: probabilistic regularisation so far gives existence of invariant measures, not deterministic smoothness.

---

## §3 — Tao's supercritical barrier (2009/2014)

Tao's argument formalises the folklore "no currently-available PDE technique touches the true NSE because all of them respect scaling in a way the true blowup would have to violate."

**Statement.** Let F_avg be an "averaged" bilinear map on the divergence-free vector fields on 𝕋³ of the form
  F_avg(u,v)(k) = Σ c(k,k₁,k₂) P(u(k₁)⊗v(k₂))
with |c(k,k₁,k₂)| ≤ 1 on the support required by the paraproduct geometry. Consider the averaged NSE ∂ₜu = νΔu + F_avg(u,u), with same energy inequality and same critical-norm scaling as true NSE. Tao constructs a specific F_avg for which there is a finite-time blowup from smooth data.

**Interpretation.** The averaged NSE shares with the true NSE every scaling-invariant a priori estimate (every L^p_t L^q_x, Besov, BMO⁻¹ bound), every local energy inequality, every critical-space fixed-point theorem. Therefore, if the Clay regularity (A) were provable using *only* those, the same proof would also give regularity for the averaged NSE. The averaged NSE has a blowup. Contradiction. Hence any successful attack must use a property not shared with some averaged variant.

**What this rules out.**
  - Picard iteration at any scaling-critical Banach space alone.
  - Energy method on any purely scaling-invariant quantity.
  - Littlewood–Paley + Bony paraproducts alone.
  - All "frequency-localised X-norm" global regularity attempts.
  - Any version of the Koch–Tataru fixed point that only uses Besov or BMO⁻¹.

**What it does NOT rule out.**
  - Exploiting the precise sign of the quadratic form u·∇u (the averaged NSE randomises this).
  - Vortex-stretching geometric depletion (Constantin–Fefferman): uses ω·∇u · ω/|ω|² pointwise, not averaged.
  - A conserved / monotone quantity that is supercritical but genuine (e.g. helicity is critical; an unknown supercritical invariant would qualify).
  - Pressure–velocity duality specific to the true Leray projection.

**Graph-level implication.** Of the 62 techniques, the ones that deal *only* with scaling and critical norms (`t_frequency_decomposition`, `t_fourier_transform`, `t_contraction_fixed_point` alone, `t_exhaustion_squeeze` in critical spaces alone) hit a wall. The ones that might punch through are those that break averaging symmetry: geometric (`t_symmetry_reduction` with the *specific* vortex-stretching direction), monotone (`t_conserved_quantity` with a *genuinely new* supercritical invariant), obstruction-theoretic (`t_obstruction_class` identifying blowup as an obstruction whose class is not Littlewood–Paley-invariant), flow-with-surgery (`t_flow_with_surgery` for a Perelman-style monotonicity). This is the true signal of the barrier.

---

## §4 — Graph-technique applicability matrix

Each of the 62 techniques rated against NSE-Clay. Rating scale:

- **STANDARD**: already the core of a mainstream NSE approach. No novelty but must be accounted for.
- **SPEC-PLAUS**: speculative but plausible — has been tried or suggested, not yet decisive.
- **UNCLEAR**: structural match exists, outcome unpredictable, worth a theorist's look.
- **UNLIKELY**: 90 years of PDE has shown this technique is not the right shape for NSE.

| Technique | Cluster | Rating | One-line application |
|---|---|---|---|
| `t_spot_pattern_in_table` | 01 | UNLIKELY | Numerical pattern-spotting has produced Hou–Luo Euler candidate; for NSE the viscosity averages out patterns. |
| `t_verify_on_special_cases` | 01 | STANDARD | Axisymmetric, 2D, Beltrami, symmetric data are the "special cases" — all globally smooth or still open. |
| `t_complete_the_square` | 02 | UNLIKELY | No quadratic to complete at the level of the energy; pressure is non-local. |
| `t_reduce_to_canonical_form` | 02 | STANDARD | Leray projection → (NS) in Ω^⊥; self-similar ansatz u(t,x)=(T−t)^{−1/2}U(x/(T−t)^{1/2}); vorticity formulation. |
| `t_compose_with_identity` | 02 | UNLIKELY | Purely algebraic glue; NSE is nonlinear-analytic, no identity-composition route. |
| `t_symmetry_reduction` | 03 | STANDARD | Axisymmetric (Hou–Chen, Elgindi for Euler), helical (Mahalov–Titi), 2D limit, Beltrami flows. Each slice is either solved or sharp-open. |
| `t_conserved_quantity` | 03 | STANDARD (and the frontier) | Energy (sub-critical!), helicity (critical), enstrophy (super-critical, not globally conserved in 3D). A new supercritical conserved/monotone quantity is exactly what's missing. |
| `t_duality` | 03 | STANDARD | Leray projection ℙ = δ−∇Δ⁻¹∇· (Riesz transform); pressure–velocity duality. Pre-dual of BMO. |
| `t_character_decomposition_count` | 03 | SPEC-PLAUS | On 𝕋³: Fourier series u(x) = Σ_k û(k)e^{2πik·x}, structure constants ⟨k, k₁⊗k₂⟩ constrained by divergence-free and triangle inequalities. A genuine Fourier-arithmetic identity for the cubic interaction is the kind of thing Tao has been chipping at. |
| `t_exhaustion_squeeze` | 04 | STANDARD | Picard iteration + continuation to maximal time; contradiction via blowup criterion. All known conditional regularity results. |
| `t_interpolate_and_continue` | 04 | STANDARD | Gagliardo–Nirenberg, Hölder–Besov, real interpolation. Used everywhere; not a new attack but necessary glue. |
| `t_frequency_decomposition` | 04 | STANDARD | Littlewood–Paley, Bony paraproducts, Koch–Tataru, Kato–Ponce. All modern NSE estimates live here. |
| `t_axiomatize_from_instances` | 05 | SPEC-PLAUS | Open question: what *is* the "right" critical norm? BMO⁻¹ is the largest known, but perhaps a new one tied to vorticity *direction* (Constantin–Fefferman flavour) axiomatises better. |
| `t_structural_isomorphism` | 05 | UNCLEAR | Volume-preserving diffeomorphism group with right-invariant L² metric is formally isomorphic (Arnold) to NS as a geodesic flow; structural isomorphism between NSE and a curvature flow on Diff_vol(ℝ³) is a real known bridge that has not yielded. |
| `t_ultraproduct_transfer` | 05 | UNLIKELY | Nonstandard analysis of NSE has been tried (Capiński–Cutland); produced only what standard arguments do. |
| `t_raise_dimension` | 06 | UNCLEAR | Embedding 3D NSE into 4D or into infinite-dim (Galerkin) may separate modes; Temam et al. tried; nothing new. |
| `t_obstruction_class` | 06 | SPEC-PLAUS | Interpret blowup as an obstruction class in some cohomology on 𝕋³ × [0,T] (e.g. motivic cohomology of the space of solutions, or an ad hoc H²). Not been tried seriously. |
| `t_compactness_argument` | 06 | STANDARD (how Leray worked) | Galerkin + weak-★ compactness → weak solution. Aubin–Lions for nonlinear term. Quantifying (Tao 2019) is where the live edge is. |
| `t_deformation_cohomology` | 06 | UNCLEAR | Deforming the dissipation (hyper- to Laplacian) defines a family; blowup as jump in deformation class. Speculative. |
| `t_rescale_for_asymptotic_geometry` | 06 | STANDARD | CKN and self-similar blowup ansatz. Nečas–Růžička–Šverák 1996 ruled out non-trivial self-similar of type I. Type-II self-similar open. |
| `t_diagonalize` | 07 | UNLIKELY | No enumeration to diagonalise against. |
| `t_arithmetize_syntax` | 07 | UNLIKELY | NSE is not a formal system to arithmetise. |
| `t_force_independence` | 07 | UNLIKELY | Not an independence question; the claim is objectively true or false. |
| `t_contraction_fixed_point` | 08 | STANDARD | Fujita–Kato, Kato, Koch–Tataru, Cannone mild solutions. Limited to small data or local time. |
| `t_infinite_descent` | 08 | UNCLEAR | Hypothesis: if a smooth solution blows up at T, its rescaling around the singular point is a smaller-scale blowup; descend indefinitely. Used implicitly in self-similar analysis (Nečas–Růžička–Šverák, ESS). |
| `t_flow_with_surgery` | 08 | SPEC-PLAUS | Perelman-style: introduce a regulariser that surgerises singularities; show the surgery times are a null set. Not been attempted because NSE is second-order parabolic without the Ricci-flow monotonicity. |
| `t_physics_to_pde` | 09 | STANDARD | NSE itself is the classical physics→PDE exemplar. No new PDE from this step. |
| `t_complex_analysis_to_integers` | 09 | UNLIKELY | Complex-variable in fluid dynamics is 2D only. |
| `t_analysis_algebra_topology_bridge` | 09 | SPEC-PLAUS | Arnold: NSE ↔ geodesic flow on Diff_vol with a curvature-modified connection (dissipation term). The Riemannian geometry of this group is known to have negative sectional curvature in many directions, implying Lyapunov instability — the "turbulence" side. |
| `t_major_minor_arc_decomposition` | 09 | SPEC-PLAUS | Circle-method-style split of the nonlinearity in Fourier into "resonant" and "non-resonant" triples; used in modified-scattering analyses of dispersive PDE. Not systematically deployed for NSE. |
| `t_ergodic_correspondence` | 09 | SPEC-PLAUS | Furstenberg-style: a density-counterexample (persistent supercritical region) ↔ a measure-preserving system (statistical solution). Kolmogorov 1941 and Foias–Manley–Rosa–Temam statistical solutions are precursors. |
| `t_finite_case_check` | 10 | UNLIKELY | NSE has infinite-dimensional state space; no finite enumeration. |
| `t_formal_verify` | 10 | UNLIKELY | Not a decidable statement; Coq/Lean would help a Chen–Hou-type computer-assisted proof, not the full Clay. |
| `t_distributed_collaboration` | 10 | STANDARD (meta) | Polymath attempts exist (Tao launched Polymath on averaged NSE); none resolved Clay. |
| `t_probabilistic_existence` | 11 | SPEC-PLAUS | Bourgain-style invariant Gibbs-measure existence in low regularity; stochastic regularisation by noise. Flandoli, Hofmanová et al. have touched. |
| `t_pigeonhole_collision` | 11 | UNLIKELY | No obvious counting structure. |
| `t_sieve_by_optimized_quadratic` | 11 | UNLIKELY | Sieve is for primes / integers. |
| `t_group_complete_exact_category` | 12 | UNLIKELY | K-theory of NSE solutions is not a natural object. |
| `t_sheafify_on_grothendieck_topology` | 12 | UNCLEAR | Sheafify the local-in-time mild-solution presheaf on a topology on spacetime adapted to vortex-stretching; might give a local-to-global obstruction. Very speculative. |
| `t_representable_functor_trick` | 12 | UNLIKELY | No obvious moduli functor. |
| `t_polynomial_method` | 11/12 | UNLIKELY | Velocity field is not polynomial; no finite-dimensional zero set to bound. |
| `t_double_centralizer_decompose` | 03 | UNLIKELY | No (G,H)-bimodule structure. |
| `t_fourier_transform` (composite) | 04 | STANDARD | Already counted. |
| `t_svd_and_spectral_decomposition` (composite) | 04 | STANDARD | Spectral decomposition of ν(−Δ) + advection operator is the Oseen framework. |
| `t_galois_correspondence` (composite) | 05 | UNLIKELY | No Galois structure on fluid velocity. |
| `t_ricci_flow_with_surgery` (composite) | 08 | SPEC-PLAUS | **Key analogue**. Ricci flow blows up, Perelman surgerises using a monotone entropy. NSE blows up (hypothetically) and we lack such an entropy. Searching for a Perelman-entropy-analogue is the single most-named speculative attack. |
| `t_wiles_modularity` (composite) | 06 | UNLIKELY | No modular form in sight. |
| `t_godel_numbering` (composite) | 07 | UNLIKELY | |
| `t_atiyah_singer_index_machinery` (composite) | 12 | UNLIKELY | No elliptic operator whose index is the obstruction. |
| `t_selberg_sieve_method` (composite) | 11 | UNLIKELY | |
| `t_circle_method` (composite) | 09 | SPEC-PLAUS | Resonance analysis in triadic Fourier interactions — see `t_major_minor_arc_decomposition`. |
| `t_furstenberg_correspondence_principle` (composite) | 09 | SPEC-PLAUS | See `t_ergodic_correspondence`. |
| `t_category_theoretic_colimits_and_adjoints` (composite) | 12 | UNLIKELY | |
| `t_auxiliary_construction` | C2 | STANDARD | Leray projection, vorticity, stream function, Clebsch potentials all count. |
| `t_conjecture_refinement` | C1 | STANDARD | Every ESS → Tao-quantitative → Barker–Prange refinement. |
| `t_reductio_ad_absurdum` | C7 | STANDARD | All blowup criteria use "suppose u is smooth up to but not including T★; derive …"; all non-uniqueness results contradict a supposed rigidity. |
| `t_projection_to_subspace` | C6 | STANDARD | Leray projection onto divergence-free fields. |
| `t_sheaf_cohomology_bridge` | C12 | UNLIKELY | |
| `t_k_theoretic_index_bridge` | C12 | UNLIKELY | |
| `t_heights_and_galois_rep_bridge` | C9 | UNLIKELY | |
| `t_level_lowering_bridge` | C9 | UNLIKELY | |
| `t_transference_bridge` | C9 | UNCLEAR | Transfer 2D regularity to 3D-like pseudorandom sparse sub-families of Fourier support? Speculative. |

Summary count: 15 STANDARD, 11 SPEC-PLAUS, 7 UNCLEAR, 29 UNLIKELY. The STANDARD bucket is exactly the set of techniques the last 90 years of PDE has already exhausted against NSE; the SPEC-PLAUS + UNCLEAR = 18 techniques are where any novelty can enter.

---

## §5 — Promising attack axes

Each axis: name, graph techniques, reduced problem, prior art, plausibility. Plausibility is "chance this axis yields a Clay-level breakthrough in the next 10 years" — not "chance it yields anything useful" (which is higher).

**Axis 1 — Geometric vorticity depletion.**
Graph: `t_symmetry_reduction`, `t_conserved_quantity`, `t_auxiliary_construction`.
Reduced problem: prove that the vorticity direction ξ = ω/|ω| is Lipschitz in a neighbourhood of maximal vorticity. Then BKM prevents blowup.
Prior: Constantin–Fefferman 1993, Beirão da Veiga–Berselli, Chae 2003–2007, Grujić–Ruzmaikina.
Plausibility: MEDIUM. Real but doesn't explain why ξ would be Lipschitz for generic data.

**Axis 2 — Critical-norm quantitative regularity extensions.**
Graph: `t_exhaustion_squeeze` (quantitative), `t_frequency_decomposition`, `t_compactness_argument`.
Reduced problem: sharpen Tao's triple-exponential ‖u‖_{H^k} ≤ exp(exp(exp(A^c))) to polynomial. Or extend to L^∞_t BMO⁻¹.
Prior: Tao 2019, 2021; Barker–Prange 2021; Palasek 2022; Albritton–Barker 2023.
Plausibility: MEDIUM. Produces partial quantitative scenarios; doesn't close Clay because still conditional on L³ bound.

**Axis 3 — Self-similar / Type-II blowup search.**
Graph: `t_rescale_for_asymptotic_geometry`, `t_infinite_descent`, `t_verify_on_special_cases`.
Reduced problem: show no smooth non-trivial discretely-self-similar blowup profile for 3D NSE (Type I ruled out by Nečas–Růžička–Šverák 1996; Type II = non-self-similar open). Or exhibit one.
Prior: NRS 1996, Tsai 1998, Chae 2015, Guevara–Phuc, Jia–Šverák 2014.
Plausibility: MEDIUM–LOW for exhibiting one; MEDIUM for ruling out.

**Axis 4 — Convex integration for smooth solutions.**
Graph: `t_auxiliary_construction`, `t_obstruction_class`, `t_infinite_descent`.
Reduced problem: extend convex integration to produce non-unique *smooth* solutions. Currently structurally blocked because Mikado flows are singular.
Prior: Buckmaster–Vicol, Albritton–Brué–Colombo, Cheskidov–Luo. Breakthrough would force (B) not (A).
Plausibility: LOW (currently a theorem: convex integration in H^s for s large is impossible).

**Axis 5 — Dyadic / shell model reduction.**
Graph: `t_reduce_to_canonical_form`, `t_structural_isomorphism`, `t_verify_on_special_cases`.
Reduced problem: prove that shell-model blowup does not lift to NSE because of inter-scale phase cancellation. Or conversely: lift a shell blowup to a genuine NSE one.
Prior: Katz–Pavlović 2005, Cheskidov 2008, Cheskidov–Shvydkoy.
Plausibility: LOW for Clay; shell models are widely regarded as insufficient witnesses.

**Axis 6 — Probabilistic / regularisation by noise.**
Graph: `t_probabilistic_existence`, `t_ergodic_correspondence`, `t_conserved_quantity`.
Reduced problem: show that NSE driven by *any* non-degenerate noise has pathwise global smoothness with probability 1, and then take noise → 0.
Prior: Flandoli–Romito, Flandoli, Hofmanová–Zhu–Zhu, Da Prato–Debussche.
Plausibility: LOW — noise regularisation so far gives Markov selection, not pathwise smoothness; vanishing-noise limit is ill-posed exactly where Clay lives.

**Axis 7 — Keller–Segel-style concentration control.**
Graph: `t_conserved_quantity`, `t_auxiliary_construction`, `t_rescale_for_asymptotic_geometry`.
Reduced problem: adapt Keller–Segel concentration–compactness (Merle–Raphaël type) to the vorticity gradient ∇ω. Identify mass-concentration threshold below which no blowup.
Prior: Raphaël–Schweyer 2014 on 2D KS; analogy to NSE by Chae, Lemarié-Rieusset.
Plausibility: LOW–MEDIUM. The analogue fails at several steps (no drift term of the right sign in NSE vorticity eqn).

**Axis 8 — Attractor / infinite-dimensional dynamics.**
Graph: `t_compactness_argument`, `t_conserved_quantity`, `t_structural_isomorphism`.
Reduced problem: characterise the global attractor of 3D NSE with forcing; show it is finite-dimensional; deduce a priori bounds.
Prior: Foias, Constantin, Temam, Robinson, Doering.
Plausibility: LOW. Assumes existence of strong solutions forward in time, which is exactly Clay.

**Axis 9 — Arnold / Riemannian geometry of Diff_vol.**
Graph: `t_analysis_algebra_topology_bridge`, `t_structural_isomorphism`, `t_ricci_flow_with_surgery`.
Reduced problem: interpret NSE on ℝ³ as geodesic flow with viscous friction on Diff_vol(ℝ³) with L² right-invariant metric; use negative sectional curvature results (Arnold) and Weil-style Laplacian estimates.
Prior: Arnold 1966, Ebin–Marsden 1970, Shkoller 2000, Khesin–Wendt 2009.
Plausibility: LOW for Clay; framework is appreciated but has not produced a single regularity theorem for 3D NSE.

**Axis 10 — Renormalisation group.**
Graph: `t_frequency_decomposition`, `t_conserved_quantity`, `t_compactness_argument`.
Reduced problem: iterate a block-spin (frequency-halving) RG map on 3D NSE; identify the fixed point and its basin; regularity of basin implies Clay.
Prior: Bricmont–Gawędzki–Kupiainen 1994, Gallay–Wayne 2002–2005 (for 2D NSE with scaling self-similar asymptotics), Moise–Ziane.
Plausibility: LOW for Clay; works as heuristic only. RG fixed point for NSE is non-trivial (Kolmogorov-energy-cascade) and unstable.

**Axis 11 — Monotone / Perelman-analogue quantity.**
Graph: `t_conserved_quantity`, `t_ricci_flow_with_surgery`, `t_duality`.
Reduced problem: find a functional Φ(u(t)) supercritical (so not already-controlled) and monotonically non-increasing under NSE flow. Perelman found such a Φ for Ricci (the reduced-volume / W-entropy). For NSE, this is the single "named moonshot".
Prior: Perelman 2003 for Ricci; for NSE no successful analogue found. Some candidates (Foias–Prodi-like functionals, vortex stretching budgets) are only conditionally monotone.
Plausibility: LOW but would be decisive if found. Very high-value target.

**Axis 12 — Carleman-estimate quantitative package.**
Graph: `t_exhaustion_squeeze`, `t_compactness_argument` (quantitative substitute), `t_reductio_ad_absurdum`.
Reduced problem: extend Tao's 2019 Carleman-driven quantitative bound from L^∞_t L³_x to L^∞_t X for wider critical X (e.g. critical Besov, Morrey), with sharper (single-exponential) dependence; or derive a uniform-in-energy bound below the Clay threshold.
Prior: Tao 2019, Barker–Prange, Palasek, Albritton.
Plausibility: LOW–MEDIUM for Clay (since still conditional), HIGH for publishable progress on sub-problems.

---

## §6 — Sub-problems likely tractable by the downstream theorists

These are targets that do not solve Clay but constitute real progress. Best targets for iterations 5–10.

**SP1. Uniqueness of Leray–Hopf solutions for *unforced* NSE.**
Currently: proved non-unique under external forcing (Albritton–Brué–Colombo 2022). Unforced case open. If non-uniqueness carries over, Clay in form (B) is advanced structurally. Technique: extend Vishik instability to the unforced setting.

**SP2. Ruling out Type-II self-similar blowup for axisymmetric NSE.**
Nečas–Růžička–Šverák 1996 killed Type I. Tsai 1998, Jia–Šverák 2014 advanced. Completely closing Type II for axisymmetric (or even just no-swirl) is tractable and important. Technique: `t_rescale_for_asymptotic_geometry` + Liouville theorems for ancient solutions.

**SP3. Extend ESS L^∞_t L^3_x criterion.**
Seregin 2012 made it "continuity at first singular time". Possible next: replace L^3 by the weakest critical space such that a finite bound → regularity. Technique: Carleman + concentration–compactness.

**SP4. Global regularity for generalised NSE with fractional dissipation (−Δ)^α, α slightly below 5/4.**
Tao 2009 gets α = 5/4 with log-correction. Pushing α to 5/4 − ε remains open. Technique: `t_frequency_decomposition` + refined multiplicative estimates.

**SP5. Single-exponential Tao-quantitative bound.**
Tao 2019: triple exponential. Single-exponential for axisymmetric (Palasek 2022). For general flows: open. Technique: sharper Carleman + better unique continuation.

**SP6. Rigorous blowup for a 2.5D / axisymmetric NSE model with *positive viscosity*.**
Chen–Hou 2025 did Euler. The NSE analogue (with ν > 0) has resisted every attempt because viscosity damps the candidate singularity. Even partial progress (e.g. conditional blowup: if data concentrates enough, blowup) would be notable. Technique: computer-assisted + interval arithmetic + stability of near-self-similar profile.

**SP7. Unique continuation for NSE.**
Backward uniqueness: Escauriaza–Seregin–Šverák 2003, Tao 2019. Forward-in-time unique continuation from regularity on a set of times is open and connects to SP1.

---

## §7 — Honest assessment

Tao (2014): "many of us expect finite-time blowup for true NSE but we do not know how to prove it." That is the baseline epistemic state. The recent 2022–2025 wave (Albritton–Brué–Colombo, Cheskidov–Luo, Chen–Hou, Elgindi) has sharpened *around* the Clay problem — non-uniqueness for forced Leray–Hopf, sharp Serrin-endpoint non-uniqueness for weak solutions, Euler-side blowup with boundary or C^{1,α} data — but has not reached unforced Clay.

A multi-agent knowledge-graph-guided exercise will not resolve Clay. The realistic deliverables of iterations 5–10 are:

  (a) A clean **attack-axis map** (axes 1–12 in §5), each linked to the graph techniques that feed it and to the sub-problems (§6) that isolate its core difficulty.

  (b) Identification of **tractable sub-problems** (SP1–SP7) where modest progress is possible and publishable, several of which (SP1, SP2, SP5) are active research frontiers where a careful application of graph techniques already in the graph may add 10–20% value.

  (c) Possibly a few **new technique nodes** for the graph — notably a **Perelman-style monotone-quantity-with-surgery** technique template (currently `t_ricci_flow_with_surgery` is single-use), a **quantitative-compactness/Carleman** package (currently diffuse across `t_exhaustion_squeeze` and `t_compactness_argument`), and a **supercritical-barrier diagnostic** that labels techniques by whether they are averaging-invariant.

Any claim of a Clay-level result from this exercise should be treated as a hallucination. What to look for instead: a single new well-formed sub-conjecture that is both (i) structurally tight against one of the 12 axes and (ii) accessible to a small team using the techniques in the graph.

---

## Appendix — pointers for downstream theorists

- Clay problem statement and official description: the Clay Mathematics Institute problem writeup (Fefferman 2000/2006).
- Canonical survey: *Lemarié-Rieusset, Recent Developments in the Navier–Stokes Problem*, 2002; *The Navier–Stokes Problem in the 21st Century*, 2016.
- Modern quantitative program: Tao 2019 (arXiv:1908.04958), Tao 2021 survey, Barker–Prange 2022 (arXiv:2211.16215).
- Non-uniqueness wave: Buckmaster–Vicol (Annals 2019); Albritton–Brué–Colombo (Annals 2022, vol 196, pp 415–455); Cheskidov–Luo (Inventiones 229, 2022).
- Euler-side singularity: Elgindi (Annals 2021, vol 194, pp 647–727); Chen–Hou (PNAS 2025).
- Supercritical barrier: Tao "Finite time blowup for an averaged 3D NSE" (arXiv:1402.0290).

All graph-technique IDs cited are canonical node IDs in `/Users/primetrce/Documents/maths/knowledge_graph.json`.
