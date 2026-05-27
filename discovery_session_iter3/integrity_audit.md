# Proof-Integrity Audit — Candidates A1–A7, B1–B7

**Role**: proof-integrity checker.
**Sources audited**: `theorist_A_candidates.md`, `theorist_B_candidates.md`.
**Verification tools used**: Python parsing of `knowledge_graph.json` (752 top-level + 111 subgraph-internal nodes, 1258 edges, 12 subgraphs); direct mathematical computation of characters, algebraic identities, and complexity-class boundaries.

---

## Candidate A1 — Grothendieck–Galois via the Colimit Lift

**Statement coherence**: separability hypothesis included; directed system over `FinGal(L/K)` well-defined. Slip in step 2: `F(L) = the Galois correspondence at L` is a functor-valued entry, not an object of `Cat` — needs 2-categorical bookkeeping.

**Step-by-step audit**:
- Steps 1–3: VALID.
- Step 4 (Yoneda): MINOR-GAP. "Representable by the inverse limit Gal(K̄/K)" conflates "representable by a limit" with "Yoneda embedding into presheaves".
- **Step 5 (Freyd solution-set condition): SERIOUS-GAP.** Freyd SAFT requires the source category be complete, but `FinSep(K)^op` is not — infinite products of finite separable extensions are not finite. Grothendieck's actual proof does NOT use SAFT; it uses the fibre functor and pro-representability. "Solution-set holds because each L/K is finite" conflates two different finiteness conditions.
- Step 6 (Krull topology): VALID; flagged external by theorist.
- Step 7: MINOR-GAP. Upgrade from lattice anti-iso to categorical equivalence requires morphism check (not just objects).
- Step 8: VALID conditional on 5, 7.

**Node-ID verification**: `s_fundamental_theorem_of_galois_theory`, `t_category_theoretic_colimits_and_adjoints`, `s_galois_correspondence`, `sg_cat.s_diagram_in_C`, `sg_cat.t_yoneda_embed`, `sg_cat.t_freyd_adjoint_theorem`, `sg_cat.t_colimit_left_adjoint` — all EXIST. `s_profinite_galois_adjunction` NEW (expected).

**External-facts audit**: Krull topology — TRUE. Tannakian/pro-representability correctly describes what's happening but not cited.

**Verdict**: PASS-WITH-MINOR-FIXES.

**Required fixes**: replace Freyd SAFT by the Galois-category/fibre-functor argument of SGA1 Exp. V; add morphism check in Step 7.

---

## Candidate A2 — Representable-Functor Formulation of Stone Duality

**Statement coherence**: clean. Small-BoolAlg restriction and BPI (vs AC) acknowledged.

**Step-by-step audit**: steps 1–8 all VALID. Ultrafilters = Boolean homs `B → 2` (step 2), Yoneda with representing object (3), Tychonoff for Stone products (6), Stone embedding as corollary (7), dualising pair identification (8) — all textbook.

**Node-ID verification**: `s_stone_representation_theorem`, `t_representable_functor_trick`, `s_compact_totally_disconnected_stone_space`, `s_ultrafilter_spectrum_Spec_B`, `s_boolean_algebra_B`, `t_auxiliary_construction`, `t_compactness_argument` — all EXIST. `s_stone_spectrum_is_representable` declared NEW (expected).

**External-facts audit**: Johnstone §VI.3 citation correct; no non-trivial external facts.

**Verdict**: PASS. Clean re-packaging of textbook result.

**Required fixes**: none.

**Required fixes**: none. Optionally note that step 3's "representing object" argument uses that `BoolAlg` has the zero-morphism structure that makes `2` a generator (trivial here).

---

## Candidate A3 — Forcing-Parametrised Stone Duality

**Statement coherence**: "P-generic spectrum" is self-referentially defined via "P-generic filters". Truth-evaluation at G yields a Boolean hom `B → 2` only if G is V-generic over `B_P`.

**Step-by-step audit**:
- Steps 1–3: VALID at the formal level.
- Step 4: MINOR-GAP. `2_P` = "two-valued model in V[G] under its natural Boolean structure" is under-defined.
- **Step 5 (topology/compactness transfer V → V[G] because "language is absolute"): SERIOUS-GAP.** Compactness is NOT absolute between V and V[G]; only Σ₀ formulae are. `Spec_P(B)` is compact in V[G] (Tychonoff holds there) but not as a V-object. The phrase "transfers because the relevant language is absolute" conflates two distinct absoluteness statements.
- Step 6: VALID within V[G].
- Step 7: MINOR-GAP. Functoriality of η_P in P requires forcing to preserve Boolean-algebra morphisms (holds for set forcing, not stated).
- Step 8: SPECULATIVE (theorist acknowledges).

**Node-ID verification**: `t_force_independence`, `s_ch_independent_of_zfc`, `s_ultrafilter_spectrum_Spec_B` — all EXIST. `s_P_generic_stone_spectrum` declared NEW.

**External-facts audit**: Balcar–Simon, Shelah–Veličković on Aut(ω*) — correctly cited. The PFA result concerns a specific P, not arbitrary P.

**Verdict**: SERIOUS-GAPS.

**Required fixes**: rewrite Step 5 to stay within V[G], drop the absoluteness claim; define `2_P` precisely in Step 4; justify Step 7 functoriality.

---

## Candidate A4 — Compactness Closure for Cyclic Quadrilaterals (Poncelet n=4)

**Statement coherence**: mixes the dichotomy (one closes ⇒ all close) with Cayley necessity-and-sufficiency (strictly stronger). Statement is fine once the dichotomy is isolated.

**Step-by-step audit**:
- Steps 1–3: VALID (parametrise vertices by `θ`; define `φ` by tangent construction).
- Step 4: MINOR-GAP. `I = {θ : φ⁴(θ) = θ}` is closed. But "`I = C` or `I ≠ C`" is a tautology; the INTENDED dichotomy is "`I = C` or `I = ∅`", which closedness alone does not give.
- Step 5 (Cayley): flagged external, VALID as black-box.
- **Step 6 (elliptic-curve translation structure): SERIOUS-GAP.** The invocation IS the theorem. A smooth self-map of S¹ with irrational rotation number has dense orbits and no period-4 points, giving `I = ∅` with `I` not full and not empty in intermediate cases (periodic points of higher period) absent the elliptic structure. "Compactness + squeeze" gives only closedness; the elliptic structure gives the rotation-number dichotomy.
- Steps 7–8: VALID given Step 6.

**Node-ID verification**: `s_cyclic_quadrilateral`, `t_compactness_argument`, `t_exhaustion_squeeze`, `t_symmetry_reduction`, `s_ptolemys_theorem` — all EXIST. Graph confirms `s_cyclic_quadrilateral` has no existing edge to `t_compactness_argument` (recon claim VERIFIED). `s_limit_cyclic_quadrilateral` declared NEW.

**External-facts audit**: Griffiths–Harris 1977 elliptic structure — TRUE but load-bearing; cannot be demoted to "external aside".

**Verdict**: SERIOUS-GAPS. The compactness chain supplies closedness; the elliptic-curve input supplies the theorem.

**Required fixes**: restate as "Poncelet n=4 via elliptic curves, with compactness as a closedness wrapper"; do not claim the compactness + squeeze chain supplies the dichotomy.

---

## Candidate A5 — Cohomological Obstruction to Invariant Subspaces (Sheaf Formulation)

**Statement coherence**: the candidate uses `s_invariant_subspace_decomposition` as seed. **Critical error**: that node in the graph has type signature `OrthogonalDecomp(L²)` and description "Spectral decomp of Koopman U" — it is the ergodic/Schur/Artin–Wedderburn/Frobenius-reciprocity state, NOT the operator-theoretic invariant-subspace-problem setup. Graph edges confirm: it feeds `t_symmetry_reduction` (for Schur's lemma) and `t_conserved_quantity` (for Birkhoff). The whole candidate is built on a node misidentification.

**Step-by-step audit**:
- Step 1: WRONG (seed node misidentified).
- Step 2: SERIOUS-GAP given wrong seed.
- Step 3: MINOR-GAP. Normal T ≠ self-adjoint; the graph's `s_spectral_theorem_self_adjoint` is for self-adjoint only.
- **Step 4 (Apostol's decomposition produces the sheaf): SERIOUS-GAP.** Apostol's 1968 decomposition is a GLOBAL subspace decomposition, not a sheaf. The stalk prescription `H/(T-λ)H̄` is the local analytic sheaf of Eschmeier–Putinar (1996), not Apostol's. The cited Apostol decomposition and the claimed sheaf are structurally different objects.
- Step 5: VALID at formal level (no computation attempted).
- Step 6: MINOR-GAP. "σ(T) countable ⇒ H¹ = 0" needs specifying the coefficient sheaf `Aut(ℱ_T)` and citing Grothendieck vanishing for 0-dim spaces.
- Step 7: VALID.
- Step 8 (quasinilpotent): CORRECTLY flagged as the open case where the reformulation says nothing new.

**Node-ID verification**: seed exists but is read as a different mathematical object than the graph defines — most serious node-ID problem in the portfolio.

**External-facts audit**: Apostol 1968 exists but is not a sheaf. Eschmeier–Putinar 1996 is the correct citation for `ℱ_T`. Aronszajn–Smith 1954, Brown–Chevreau–Pearcy, Scott Brown — TRUE.

**Verdict**: BROKEN.

**Required fixes**: (i) replace seed with correct operator-theory state (e.g., `s_bounded_operator_on_hilbert`; verify graph); (ii) replace Apostol with Eschmeier–Putinar; (iii) specify coefficient sheaf for H¹; (iv) admit the wrapping is tautological for compact T and empty for quasinilpotent T.

---

## Candidate A6 — Dyadic Martingale Structure for Archimedes' Polygon Sequence

**Statement coherence**: quantifier order fine. Filtration generates Borel σ-algebra.

**Step-by-step audit**:
- Steps 1–3: VALID.
- Step 4 (Doob convergence, flagged external): Doob 1953 is the correct citation.
- **Step 5 (sub/super-martingale claim): MINOR-GAP bordering SERIOUS.** `L_n^{in}` and `L_n^{out}` as stated are DETERMINISTIC numbers. To be martingales they must be random variables on a probability space. The natural r.v. is "length of a uniformly chosen arc's chord"; then `L_n^{in}` becomes a r.v. and sub-martingality follows from `sin(θ/2) < θ/2`. The sketch asserts the half-angle identity IS the conditional-expectation formula but does not verify it.
- Step 6: VALID given the r.v. setup.
- Step 7: VALID algebra.

**Node-ID verification**: `s_inscribed_circumscribed_96_gons`, `t_structural_isomorphism`, `t_axiomatize_from_instances`, `t_compactness_argument`, `s_area_of_circle`, `t_exhaustion_squeeze` — all EXIST. `s_dyadic_filtration_on_circle` NEW.

**External-facts audit**: Doob — TRUE.

**Verdict**: PASS-WITH-MINOR-FIXES. Essentially trivial (deterministic sequences can always be "martingaled" on a degenerate probability space) but coherent.

**Required fixes**: (i) state the r.v. setup (sample an arc uniformly); (ii) verify half-angle ↔ conditional-expectation rather than assert.

---

## Candidate A7 — Character-Decomposition of S₅ Orbits

**Statement coherence**: quantifier "only if some H_i contains A₅" is the right form.

**Step-by-step audit**:
- Steps 1–2: VALID.
- Step 3 (S₅ character table): VALID. 7 classes, dims `1,1,4,4,5,5,6`; `1+1+16+16+25+25+36 = 120`.
- **Step 4 (Frobenius reciprocity computation): WRONG.** By Frobenius, `⟨Ind_H^{S₅} 1, χ_std⟩_{S₅} = ⟨1, Res_H χ_std⟩_H =` number of trivial constituents in `Res_H χ_std =` (H-orbits on {1,…,5}) − 1. So the inner product is ZERO iff H is transitive. Direct checks:
  - `H = Z/5` (transitive): `(1/5)(4 + 4(-1)) = 0`.
  - `H = A₅` (transitive): `(1/60)(4 + 0·15 + 1·20 + (-1)·24) = 0`.
  - `H = S₄` (stabiliser of 5, two orbits {1,…,4} and {5}): inner product = 1.
  But `S₄` IS SOLVABLE (`S₄ ⊃ A₄ ⊃ V₄ ⊃ 1`). So a SOLVABLE H gives NON-ZERO inner product with `χ_std` — the exact opposite of the theorist's claim "inner product vanishes unless H ⊇ A₅". The claim that transitivity implies non-zero inner product is directionally backwards.
- Step 5: SERIOUS-GAP inherited.
- Steps 6–8 (Chebotarev + Stauduhar): VALID as classical; independent of step 4's error.

**Node-ID verification**: `s_galois_group_S5`, `t_character_decomposition_count`, `t_obstruction_class`, `s_chebotarev_density_theorem`, `s_abel_ruffini` — all EXIST. `s_S5_character_data_on_roots` NEW. The recon claim that `t_character_decomposition_count` is wired to `s_chebotarev_density_theorem` is CONFIRMED.

**External-facts audit**: `⟨χ_std, χ_std⟩_{S₅} = 1` — TRUE. Stauduhar — TRUE.

**Verdict**: SERIOUS-GAPS. The Frobenius reciprocity step is computed in the wrong direction; the "obstruction to solvability" claim is falsified by the concrete example `H = S₄`.

**Required fixes**: (i) recompute `⟨Ind_H 1, χ_std⟩ = (orbits) − 1`; (ii) replace the "obstruction to solvability" with a correct character-theoretic statement (e.g., A₅ has no non-trivial 1-dim rep); (iii) note `H = S₄` as a concrete counterexample to the stated inequality.

---

## Candidate B1 — Spectral Noether Theorem (mode-wise conservation)

**Statement coherence**: "X commutes with spatial translation" stated. Missing: boundary/decay condition for the Plancherel integration by parts.

**Step-by-step audit**:
- Steps 1–4: VALID.
- **Step 5 (mode-wise Euler–Lagrange + mode-wise 1-param symmetry): SERIOUS-GAP.** TRUE only for QUADRATIC (free) Lagrangians. For nonlinear L (e.g. φ⁴), the Lagrangian in momentum space has cross-terms `φ̂(k₁)φ̂(k₂)φ̂(k₃)φ̂(-k₁-k₂-k₃)`, so the EL for `φ̂(k)` couples to all modes. "Each mode has its own EL with symmetry χ(k)" is FALSE for interacting theories. Boundary-term vanishing also needs hypothesis (compact domain or decay).
- Steps 6–8: VALID given quadratic L.

**Node-ID verification**: `s_infinitesimal_action_variation`, `t_frequency_decomposition`, `t_conserved_quantity`, `s_noether_theorem`, `s_fourier_theorem_heat` — all EXIST. Recon claim that `s_infinitesimal_action_variation` has only one existing edge is CONFIRMED.

**External-facts audit**: Parseval/Plancherel — TRUE.

**Verdict**: PASS-WITH-MINOR-FIXES. The theorist acknowledges interactions break the mode-factoring in failure modes but the derivation sketch retains the wrong Step 5.

**Required fixes**: (i) add "L is quadratic" hypothesis; (ii) state boundary condition; (iii) note that for interacting theories mode-wise charges are NOT independently conserved.

---

## Candidate B2 — Polynomial-Method Chabauty Bound

**Statement coherence**: r < g, p ≥ 2g+1 stated.

**Step-by-step audit**:
- Steps 1–4: VALID.
- **Step 5 (CLP/Alon polynomial method on abelian variety): SERIOUS-GAP.** Croot–Lev–Pach (2017) and Alon's Combinatorial Nullstellensatz are constructed for `𝔽_p^n` or grids in affine space with product-coordinate structure. `J_C(𝔽_p)` is a finite abelian group of size ~ `p^g`, structured as a product of cyclic groups, NOT as `𝔽_p^g`; natural "coordinates" on an abelian variety are global sections of line bundles, not coordinate functions. Polynomial method on abelian varieties that exists (Amoroso–David, Bilu–Rémond, Galateau) uses HEIGHTS, not CLP slice rank, and gives different bounds. The theorist flags this as external — but "polynomial of degree `D ≤ p^{r/g}` vanishes on H" via CLP is NOT established here.
- Step 6 (Bezout): MINOR-GAP. Bezout on an AV translates through canonical embedding + heights; the `(2g-2)·D` genus-degree bound presumes a canonical embedding.
- Step 7: VALID given 5–6.

**Node-ID verification**: `s_curve_inside_abelian_variety`, `t_polynomial_method`, `s_mordell_faltings`, `s_mordell_weil_theorem` — all EXIST. Recon claim "`t_polynomial_method` has 0 top-level uses" is CONFIRMED (zero edges).

**External-facts audit**: CLP on `𝔽_p^n` — TRUE. Extension to abelian varieties — CONJECTURAL, flagged correctly.

**Verdict**: SERIOUS-GAPS. Step 5 technical core unestablished.

**Required fixes**: either replace CLP with Bilu–Rémond/Amoroso–David height machinery (with correspondingly different bounds), restrict to a split setting where CLP genuinely applies, or downgrade the statement to CONDITIONAL on CLP-type bounds extending to AVs.

---

## Candidate B3 — Local CLT on Arithmetic Progressions

**Statement coherence**: third moment, aperiodicity, range `q ≤ n^{1/2-ε}` all stated.

**Step-by-step audit**:
- Steps 1–6: VALID.
- **Step 7 (Weyl–Vinogradov bound for iid characteristic function): WRONG citation.** `sg_circle.t_weyl_vinogradov` is for polynomial exponential sums `∑e(αx^k)` — NOT for iid characteristic-function tails. The stated bound `|φ_X(t)| ≤ 1 - c·dist(t,2πℤ)²` follows from Taylor expansion of `log φ_X(t)` to order 3 (using `Var(X)=1`) + global bound from aperiodicity. Correct technique: Esseen smoothing, not Weyl–Vinogradov. The claimed error `O(q·n^{-1})` may be correct via the right route.
- Step 8: VALID.

**Node-ID verification**: `s_characteristic_function_of_sum`, `t_major_minor_arc_decomposition`, `s_limit_characteristic_function_equals_gaussian`, `t_circle_method`, `sg_circle.t_weyl_vinogradov`, `sg_circle.t_combine_main_error` — all EXIST.

**External-facts audit**: Davenport, Petrov Ch. VII — TRUE citations. Point 3 Elliott–Halberstam-strength claim is genuinely hard (not at CLT level).

**Verdict**: PASS-WITH-MINOR-FIXES. The theorem is classical; the citation is misrouted.

**Required fixes**: (i) cite Esseen smoothing + Taylor in step 7; (ii) justify the `q` factor as arising from summing over q characters, not from minor-arc estimates.

---

## Candidate B4 — Walsh Spectrum of the Provability Predicate

**Statement coherence**: L, N defined; `L ≪ 2^{N/k}` acknowledged.

**Step-by-step audit**:
- Steps 1–4: VALID.
- Step 5 (LMN theorem): VALID citation. LMN 1993: for Boolean f computed by depth-d size-s AC⁰ circuit, `∑_{|S|>k} f̂(S)² ≤ 2s · 2^{-k^{1/d}/20}`.
- **Step 6 (proof-verifier is depth O(log L), size poly(L, N)): WRONG.** AC⁰ requires CONSTANT depth, not logarithmic. Proof-verifier on a length-L proof string can be built in DEPTH O(1), size poly(L, N): for each index i ∈ 1..L, locally check that step i follows from earlier steps by one of finitely many rules (constant-depth per index; one extra AND layer for all indices). Depth O(log L) would put it in NC¹, to which LMN does NOT apply (bound degrades because `k^{1/log L} ≈ 1`).
- **Step 7 (substitute): WRONG bound.** With the corrected d = O(1), the LMN bound is `poly(L,N) · 2^{-Ω(k)}`. The stated `L · 2^{-N/2} · e^{-c·k/log L}` mixes different regimes and has unjustified prefactors.
- Step 8: SPECULATIVE as theorist acknowledges; fixed-point-lemma circuit depth not worked out.

**Node-ID verification**: `s_self_referential_godel_sentence_G`, `t_frequency_decomposition`, `sg_godel.s_formal_system`, `sg_godel.t_prime_power_encoding`, `sg_godel.s_gödel_numbers`, `sg_godel.t_primitive_recursive_predicates`, `sg_godel.s_representable_relations`, `sg_godel.t_fixed_point_lemma`, `sg_godel.s_self_referential_sentence` — all EXIST with `sg_godel.` prefix. Theorist cites WITHOUT prefix (minor citation hygiene); also treats `sg_godel_numbering` (subgraph ID) as a state node — slight abuse.

**External-facts audit**: LMN — TRUE. Application requires AC⁰ = constant depth.

**Verdict**: SERIOUS-GAPS. Step 6 confuses AC⁰ with NC¹; Step 7 derives from that wrong depth. The target theorem (Walsh concentration of provability) may still hold but not via this sketch.

**Required fixes**: (i) rewrite Step 6 with proof-verifier depth O(1); (ii) re-derive Step 7 bound as `poly(L,N) · 2^{-Ω(k)}`; (iii) formally compute Walsh decomposition for the fixed-point construction in step 8.

---

## Candidate B5 — Syntactic Current (Conserved Quantity on the Proof Graph)

**Statement coherence**: "holonomy" on the directed proof graph needs specification.

**Step-by-step audit**:
- Steps 1–3: VALID.
- **Step 4 (seek vertex-potential `q` with `J = q(ψ) - q(φ)` the differential): INTERNALLY INCONSISTENT.** If `J = dq` then J is BY CONSTRUCTION a COBOUNDARY in the cellular cochain complex of the proof graph. Coboundaries have ZERO holonomy on every cycle — this is the defining property. But the candidate claims (step 7) that J has non-zero holonomy around fixed-point diagonals, which is IMPOSSIBLE for a coboundary. Non-zero holonomy requires J to be a cocycle NOT cohomologous to zero, i.e., a class in H¹(Γ_T; ℤ). The construction as written makes J trivially cohomologous to 0.
- Steps 5–7: invalidated by step 4.
- Step 8: SERIOUS-GAP inherited.
- Step 9 (H¹ non-triviality ↔ incompleteness): an attractive Lawvere-diagonal-style picture, but the construction in steps 4–8 does not deliver it.

**Node-ID verification**: `s_self_referential_godel_sentence_G`, `s_godel_incompleteness`, `t_conserved_quantity`, `sg_godel.t_primitive_recursive_predicates`, `sg_godel.t_fixed_point_lemma` — all EXIST. `sg_godel_numbering` is a subgraph abused as a state node.

**External-facts audit**: Gentzen cut-elimination — TRUE. Ordinal ε₀ — TRUE; candidate notes in Novelty that "syntactic current" is likely a reformulation of ordinal proof theory.

**Verdict**: BROKEN. Central construction is self-contradictory: J is defined as a coboundary but asserted to have non-zero holonomy.

**Required fixes**: (i) redefine J as a cocycle that is NOT a coboundary (e.g., add an indicator-of-diagonalisation term that makes J a true topological defect); (ii) compute explicitly whether this cocycle is trivial in H¹; (iii) formalise with cochain complexes on the proof DAG.

---

## Candidate B6 — Sylow Density via Pigeonhole on Conjugation Orbits

**Statement coherence**: k, ε, p defined.

**Step-by-step audit**:
- Steps 1–3: VALID. Embedding `Syl_p(G)` into a Hamming-like space is fine.
- **Step 4 (covering-dimension on conjugation-quotiented Hamming space): MINOR-to-SERIOUS-GAP.** "(1/ε)^D covers" is a Euclidean-doubling statement. On the Hamming cube with normalised distance, ε-covering number is `exp(n·H(ε))` with H binary entropy — NOT `(1/ε)^n`. On the conjugation quotient, the right bound is at best `exp(p^k · H(ε))`. The stated `(1/ε)^{p^k}` is tighter than true metric-entropy bounds in the ε→0 regime.
- Step 5: MINOR-GAP. Lebesgue covering dimension of a finite set is 0; the theorist means doubling/metric-entropy "dimension", which should be stated explicitly. Order of magnitude p^k is reasonable.
- Step 6: VALID given weakened bound.
- Step 7: SPECULATIVE as flagged.

**Node-ID verification**: `s_set_of_p_subgroups_with_G_action`, `t_pigeonhole_collision`, `s_sylow_theorems` — all EXIST.

**External-facts audit**: Pyber, Liebeck–Pyber references exist but do not contain exactly this covering bound; the bound on "conjugation-quotiented Hamming space" is a reformulation the theorist constructs, not cited from literature.

**Verdict**: PASS-WITH-MINOR-FIXES.

**Required fixes**: (i) restate bound as `exp(p^k · H(ε))` using metric entropy; (ii) clarify "covering dimension" on a quotient; (iii) verify pigeonhole respects the G-action.

---

## Candidate B7 — Quantitative Waring via Refined Farey Dissection

**Statement coherence**: ε, k, s dependencies stated.

**Step-by-step audit**:
- Steps 1–6: VALID.
- **Step 7 (minor-arc dominance: `s·σ(k,s) > s/k − 1`): WRONG.** Main term magnitude `N^{s/k - 1}`; minor-arc contribution bound `N^{s(1/k - σ)}·(arc length)`. For minor arcs to be lower order, need `s(1/k - σ) < s/k - 1`, i.e., `s·σ > 1`. The stated `s·σ > s/k − 1` is off.
- Step 8 (Wooley / BDG bound `σ ≥ (s-k²)/(2sk)`): approximately correct (constants vary by source).
- **Step 9 (substitute ⇒ `s ≥ k·log k`): ALGEBRAICALLY WRONG.** From the CORRECT condition `s·σ > 1`: `(s-k²)/(2k) > 1` ⇒ `s > k²+2k = k(k+2)`. This gives `s = O(k²)`, NOT `s ∼ k·log k`. From the STATED (wrong) condition: `s - k² > 2s - 2k` ⇒ `s < 2k - k²`, which is NEGATIVE for k ≥ 3 — unsatisfiable. Either way, the substitution does NOT yield `k·log k`. Vaughan–Wooley's actual `G(k) ≤ k·log k·(1+o(1))` requires ITERATED efficient congruencing / mean-value bounds, not a one-pass substitution.

**Node-ID verification**: `s_hilbert_waring_theorem`, `t_major_minor_arc_decomposition`, `s_vinogradov_three_primes_theorem`, `sg_circle.t_farey_dissection`, `sg_circle.t_singular_series_local_euler`, `sg_circle.t_weyl_vinogradov` — all EXIST.

**External-facts audit**: Wooley (Annals 2012/2014/2019), Bourgain–Demeter–Guth (Annals 2016), Vaughan Ch. 5 — TRUE; the target theorem is real.

**Verdict**: SERIOUS-GAPS. The target is a real theorem but the sketch does not derive it.

**Required fixes**: (i) correct Step 7's inequality to `s·σ > 1`; (ii) replace one-pass substitution with the iterated Wooley scheme; (iii) explicitly state `k·log k` requires iterated mean-value inputs, not a single substitution.

---

## Summary

### Grade distribution

| Verdict | Count | Candidates |
|---|---|---|
| PASS | 1 | A2 |
| PASS-WITH-MINOR-FIXES | 5 | A1, A6, B1, B3, B6 |
| SERIOUS-GAPS | 6 | A3, A4, A7, B2, B4, B7 |
| BROKEN | 2 | A5, B5 |

Total: 14. Distribution: 36% serious or broken; 57% minor issues; 7% clean.

### Systemic patterns observed

**Pattern 1 — "Standard argument" hides the theorem.** A4, A5, B2 all cite a major external fact as a "standard input" when that fact IS the mathematical content of the candidate. A4's elliptic-curve translation structure is the Poncelet theorem itself; the compactness argument supplies only closedness. A5's Apostol (really Eschmeier–Putinar) sheaf carries all the weight; the obstruction class is tautological once you have the sheaf. B2's CLP-on-abelian-variety is unestablished and is the entire technical core.

**Pattern 2 — Mis-cited technique from the correct subgraph.** B3 invokes Weyl–Vinogradov for i.i.d. characteristic functions (wrong; correct tool is Esseen smoothing). B1 invokes `sg_circle.t_weyl_vinogradov` for a probabilistic CLT error. These are mathematically similar-looking but STRUCTURALLY DIFFERENT techniques; the circle-method Weyl bound is for polynomial phases, not random-variable characteristic functions.

**Pattern 3 — Quantifier / condition-direction errors.** A7's Frobenius reciprocity direction is flipped: "transitivity ⇒ non-zero inner product" is backwards (transitivity gives ZERO; non-transitivity gives non-zero). B7's minor-arc condition `s·σ > s/k − 1` is algebraically off from the correct `s·σ > 1`. B4 confuses AC⁰ (constant depth) with NC¹ (log depth).

**Pattern 4 — "It's a coboundary but has holonomy"-style self-contradictions.** B5 defines `J = dq` (manifestly a coboundary) and then claims non-trivial holonomy (impossible). This is a pure definitional error that a re-reading would have caught.

**Pattern 5 — Node-ID misidentification.** A5 builds on `s_invariant_subspace_decomposition`, treating it as the operator-theoretic invariant-subspace-problem state. The graph defines that node as "Orthogonal decomp of L² / Spectral decomp of Koopman U" — the ergodic/representation-theoretic node. The whole candidate is built on a wrong node reading.

**Pattern 6 — Unprefixed subgraph-internal IDs.** Several B candidates cite `s_formal_system`, `t_fixed_point_lemma` etc. when the actual graph IDs are `sg_godel.s_formal_system`, `sg_godel.t_fixed_point_lemma`. Minor citation hygiene, but the graph's namespace convention is being ignored in places.

### Ranked reliability (most → least trustworthy)

**Most trustworthy:**
1. **A2** — clean Yoneda wrapper of textbook Stone duality. No mathematical errors; no external load-bearing facts.
2. **A6** — essentially trivial martingale reformulation; mathematical content is modest but self-consistent.
3. **B3** — mis-cites Weyl–Vinogradov, but the theorem itself is a classical local CLT on APs with a well-established proof.
4. **A1** — Grothendieck's Galois theory, packaged unconventionally; Freyd SAFT citation is wrong but the result is correct and the patch is mechanical.
5. **B1** — needs the "quadratic Lagrangian" hypothesis added, but otherwise a correct mode-wise Noether for free theories.
6. **B6** — reformulation exercise; bound needs to be restated in entropy terms, but the idea is sound.

**Least trustworthy:**

7. **A4** — compactness argument does no work; elliptic-curve structure is the theorem.
8. **B7** — arithmetic substitution step is wrong in both directions; the `k·log k` conclusion requires techniques not present in the sketch.
9. **B2** — CLP polynomial method on abelian varieties is unestablished; step 5 is a conjectural leap.
10. **A3** — "topology is absolute V → V[G]" is wrong; the whole step 5 transfer argument breaks.
11. **A7** — Frobenius reciprocity computed in the wrong direction; `H = S₄` is a solvable concrete counterexample.
12. **B4** — confuses AC⁰ with NC¹; the LMN bound derived is a mix-up of two non-existing regimes.
13. **A5** — seed-node misidentified; Apostol citation builds the wrong sheaf; cohomological obstruction is tautological in the only regime where the construction is clean (compact T).
14. **B5** — self-contradictory core (`J = dq` has zero holonomy by definition but is claimed to have non-zero holonomy).

### Overall summary

Of the 14 candidates, only ONE (A2) is fully clean. Five need minor patches; six have serious gaps requiring structural rewrites; two are fundamentally BROKEN. The common failure mode is glossing a non-trivial analytic/computational step under an authoritative citation ("by standard argument", "by a known theorem of Apostol / Weyl–Vinogradov / LMN") when the cited theorem does not supply what is needed. Theorists A and B are well-calibrated on NOVELTY grading (most candidates are honestly graded as COROLLARY or LIKELY-KNOWN), but the derivation sketches are not held to the same standard of internal scrutiny as the novelty claims.

**Recommended triage for the problem-solver**: accept A2 as-is; patch A1/A6/B1/B3/B6 with the minor fixes above; return A3/A4/A7/B2/B4/B7 to their theorists with specific error notes; reject A5/B5 pending substantial restructuring. The single most mechanically catchable error is B5's coboundary-with-non-trivial-holonomy self-contradiction; the single most subtle error is A7's Frobenius reciprocity direction (requires computing `H = S₄` explicitly to expose it).
