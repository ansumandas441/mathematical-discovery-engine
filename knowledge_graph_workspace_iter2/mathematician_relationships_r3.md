# Mathematician's Relationships — Round 3 (Chapters 05 & 06, iter-2 completion)

**Author role:** Mathematician C, iteration 2.
**Scope:** Every level-3 heading in `05_early_twentieth_century.md` and `06_modern_contemporary.md` that is NOT already chained in iter-1 (`mathematician_relationships.md`).
**Format:** identical to iter-1 Part A. Reuses canonical node ids from `knowledge_graph_workspace_iter2/canonical_node_index.md`.

Notation:
- `--[t_foo {param: v}]-->` = technique `t_foo` applied with parameter binding on the edge.
- `⟨s_a, s_b⟩` = multiple inputs fed into the same technique.
- `⚠ not in toolbox:` flags a step without a good toolbox match.
- New state ids are prefixed `s_` and only introduced for theorem-specific intermediate/terminal states.

---

## Audit — what's missing

### Chapter 5 headings in source
1. Hilbert's Basis Theorem — iter-1 DONE
2. Hilbert's Nullstellensatz — iter-1 DONE
3. **Zermelo's Well-Ordering** — MISSING
4. Brouwer FPT — iter-1 DONE
5. Noether's Theorem (symmetry) — iter-1 DONE
6. **Noether's Isomorphism Theorems** — MISSING
7. **Gödel's Completeness** — MISSING
8. Gödel's Incompleteness — iter-1 DONE
9. **Banach–Tarski Paradox** — MISSING
10. Banach FPT — iter-1 DONE
11. Hahn–Banach — iter-1 DONE
12. **Stone–Weierstrass** — MISSING
13. **Stone Representation** — MISSING
14. Tychonoff — iter-1 DONE
15. Church–Turing Halting — iter-1 DONE
16. Gödel's CH+GCH consistency — iter-1 DONE
17. Ramsey — iter-1 DONE (covers both finite & infinite)
18. Birkhoff Ergodic — iter-1 DONE

**Missing in Ch. 5 = 6 chains to write.**

### Chapter 6 headings in source
1. Atiyah–Singer — iter-1 DONE
2. CFSG — iter-1 DONE
3. Cohen CH Independence — iter-1 DONE
4. Four Color — iter-1 DONE
5. Faltings / Mordell — iter-1 DONE
6. **Modularity Theorem (full, BCDT 2001)** — iter-1 only covers FLT via Wiles semistable; full is MISSING as a distinct terminal
7. Wiles FLT — iter-1 DONE
8. Poincaré / Geometrization — iter-1 DONE
9. Kepler / Hales — iter-1 DONE
10. Green–Tao — iter-1 DONE
11. Zhang / Maynard bounded gaps — iter-1 DONE
12. Helfgott weak Goldbach — iter-1 DONE
13. **abc Conjecture — Mochizuki (disputed)** — MISSING
14. Robertson–Seymour — iter-1 DONE
15. Szemerédi — iter-1 DONE

**Missing in Ch. 6 = 2 chains to write.** (Most of ch. 6 was aggressively covered in iter-1.)

Total new chains this round: **8**.

---

## Part A — New derivation chains

### Zermelo's Well-Ordering Theorem (Ch. 5)

**Axiom / starting states:** `s_zfc_axioms`, `s_infinite_set`, `s_axiom_of_choice_function_phi` *(new)*
**Terminal theorem state:** `s_zermelo_well_ordering` *(new, kind: theorem)*

**Steps:**
1. input: `⟨s_zfc_axioms, s_infinite_set⟩` --[t_axiomatize_from_instances {isolate: a choice function φ on the power-set minus ∅}]--> output: `s_axiom_of_choice_function_phi`
2. input: `s_axiom_of_choice_function_phi` --[t_auxiliary_construction {build "γ-sets": well-ordered subsets whose successor equals φ applied to the remaining complement}]--> output: `s_maximal_gamma_set_on_M` *(new)*
3. input: `s_maximal_gamma_set_on_M` --[t_reductio_ad_absurdum {if the union of γ-sets misses any x ∈ M, extending by φ(remainder) yields a strictly larger γ-set, contradicting maximality}]--> output: `s_zermelo_well_ordering`

**Techniques used:** 12 axiomatizeFromInstances; C2 auxiliaryConstruction; C7 reductioAdAbsurdum

---

### Noether's Isomorphism Theorems (Ch. 5)

**Axiom / starting states:** `s_finite_group` (or generic algebraic object), `s_normal_subgroup_N_in_G` *(new)*, `s_group_homomorphism_f` *(new)*
**Terminal theorem state:** `s_noether_isomorphism_theorems` *(new, kind: theorem)*

**Steps:**
1. input: `⟨s_group_homomorphism_f, s_normal_subgroup_N_in_G⟩` --[t_axiomatize_from_instances {abstract from Dedekind/Jordan specific cases: subobject + quotient + morphism pattern}]--> output: `s_abstract_subobject_quotient_morphism_pattern` *(new)*
2. input: `s_abstract_subobject_quotient_morphism_pattern` --[t_reduce_to_canonical_form {canonical map g·ker(f) ↦ f(g)}]--> output: `s_canonical_quotient_by_kernel_map` *(new)*
3. input: `s_canonical_quotient_by_kernel_map` --[t_structural_isomorphism {G/ker(f) ≅ im(f); HN/N ≅ H/(H∩N); (G/N)/(K/N) ≅ G/K}]--> output: `s_noether_isomorphism_theorems`

**Techniques used:** 12 axiomatizeFromInstances; 4 reduceToCanonicalForm; 13 structuralIsomorphism

---

### Gödel's Completeness Theorem (Ch. 5)

**Axiom / starting states:** `s_first_order_logic_language` *(new)*, `s_consistent_first_order_theory_T` *(new)*, `s_zfc_axioms` *(for the Zorn step via Choice)*
**Terminal theorem state:** `s_godel_completeness_theorem` *(new, kind: theorem)*

**Steps:**
1. input: `s_consistent_first_order_theory_T` --[t_auxiliary_construction {add countably many fresh constants c_0, c_1, …; add witness axiom φ(c_i) for each ∃x φ(x)}]--> output: `s_consistent_theory_with_witnesses` *(new)*
2. input: `s_consistent_theory_with_witnesses` --[t_compactness_argument {Zorn / choice: extend to a maximal consistent theory T* with the Henkin witness property}]--> output: `s_maximal_consistent_henkin_theory_T_star` *(new)*
3. input: `s_maximal_consistent_henkin_theory_T_star` --[t_structural_isomorphism {term model: domain = closed-term equivalence classes mod T*; predicates/functions read off syntax}]--> output: `s_godel_completeness_theorem`

**Techniques used:** C2 auxiliaryConstruction; 16 compactnessArgument; 13 structuralIsomorphism

---

### Banach–Tarski Paradox (Ch. 5)

**Axiom / starting states:** `s_zfc_axioms`, `s_euclidean_3_space`, `s_free_group_F2_on_two_generators` *(new)*
**Terminal theorem state:** `s_banach_tarski_paradox` *(new, kind: theorem)*

**Steps:**
1. input: `s_free_group_F2_on_two_generators` --[t_symmetry_reduction {paradoxical self-decomposition: F₂ = {e} ⊔ W(a) ⊔ W(a⁻¹) ⊔ W(b) ⊔ W(b⁻¹) with aW(a⁻¹) ⊇ {e} ⊔ W(a⁻¹) ⊔ W(b) ⊔ W(b⁻¹)}]--> output: `s_paradoxical_decomposition_of_F2` *(new)*
2. input: `s_paradoxical_decomposition_of_F2` --[t_structural_isomorphism {embed F₂ ↪ SO(3) via two generic rotations of ℝ³}]--> output: `s_F2_as_subgroup_of_SO3` *(new)*
3. input: `⟨s_F2_as_subgroup_of_SO3, s_zfc_axioms⟩` --[t_auxiliary_construction {AC: choose one representative per F₂-orbit on S²}]--> output: `s_paradoxical_sphere_decomposition` *(new)*
4. input: `s_paradoxical_sphere_decomposition` --[t_raise_dimension {radial suspension from S² to the punctured ball, then handle the center point}]--> output: `s_banach_tarski_paradox`

**Techniques used:** 6 symmetryReduction; 13 structuralIsomorphism; C2 auxiliaryConstruction; 14 raiseDimension

---

### Stone–Weierstrass Theorem (Ch. 5)

**Axiom / starting states:** `s_compact_hausdorff_space` *(new)*, `s_point_separating_unital_subalgebra_A_of_C_X_R` *(new)*, `s_weierstrass_approximation` (reused: polynomial approximation of |t|)
**Terminal theorem state:** `s_stone_weierstrass_theorem` *(new, kind: theorem)*

**Steps:**
1. input: `⟨s_point_separating_unital_subalgebra_A_of_C_X_R, s_weierstrass_approximation⟩` --[t_compose_with_identity {apply polynomial approx to |t| on the closure of A to obtain |f| ∈ closure(A) for every f ∈ A; then max(f,g) = ½(f+g+|f−g|)}]--> output: `s_closure_of_A_is_a_lattice` *(new)*
2. input: `s_closure_of_A_is_a_lattice` --[t_auxiliary_construction {for each pair x ≠ y, build f_{xy} ∈ closure(A) matching target g at x, y via separation + constants}]--> output: `s_pointwise_matching_family_f_xy` *(new)*
3. input: `s_pointwise_matching_family_f_xy` --[t_compactness_argument {finite-cover piecing via min/max of finitely many f_{xy} on X compact}]--> output: `s_stone_weierstrass_theorem`

**Techniques used:** 5 composeWithIdentity; C2 auxiliaryConstruction; 16 compactnessArgument

---

### Stone Representation Theorem (Ch. 5)

**Axiom / starting states:** `s_boolean_algebra_B` *(new)*, `s_zfc_axioms` (for Boolean prime ideal theorem ≈ weak AC)
**Terminal theorem state:** `s_stone_representation_theorem` *(new, kind: theorem)*

**Steps:**
1. input: `s_boolean_algebra_B` --[t_auxiliary_construction {Spec(B) = set of ultrafilters; basic clopen U(a) = {F : a ∈ F}}]--> output: `s_ultrafilter_spectrum_Spec_B` *(new)*
2. input: `s_ultrafilter_spectrum_Spec_B` --[t_compactness_argument {Tychonoff applied to 2^B with Boolean prime ideal theorem gives compact Hausdorff totally disconnected topology}]--> output: `s_compact_totally_disconnected_stone_space` *(new)*
3. input: `s_compact_totally_disconnected_stone_space` --[t_duality {contravariant equivalence: Boolean algebras ↔ Stone spaces; a ↔ U(a) is an isomorphism onto the clopen algebra}]--> output: `s_stone_representation_theorem`

**Techniques used:** C2 auxiliaryConstruction; 16 compactnessArgument; 8 duality

---

### Modularity Theorem — full, Breuil–Conrad–Diamond–Taylor 2001 (Ch. 6)

**Axiom / starting states:** `s_elliptic_curve_over_Q`, `s_galois_representation`, `s_modular_form`, `s_semistable_modularity_theorem` (from iter-1 Wiles chain — reused as lemma)
**Terminal theorem state:** `s_full_modularity_theorem_BCDT` *(new, kind: theorem)*

**Steps:**
1. input: `s_elliptic_curve_over_Q` --[t_reduce_to_canonical_form {stratify by conductor N and by ramification type at 3 and 5 using Breuil's finite flat group scheme classification}]--> output: `s_ramification_stratification_of_elliptic_curves` *(new)*
2. input: `⟨s_ramification_stratification_of_elliptic_curves, s_semistable_modularity_theorem⟩` --[t_wiles_modularity {modularity-lifting: extend R = T theorem beyond semistable, case-by-case at 3 using Langlands–Tunnell for the residual rep}]--> output: `s_non_semistable_modularity_cases_handled` *(new)*
3. input: `s_non_semistable_modularity_cases_handled` --[t_level_lowering_bridge {Diamond, Conrad–Diamond–Taylor, Breuil refinements glue together residually modular ⇒ modular for every conductor}]--> output: `s_full_modularity_theorem_BCDT`

**Techniques used:** 4 reduceToCanonicalForm; t_wiles_modularity (umbrella); C9 levelLoweringBridge

---

### abc Conjecture — Mochizuki's disputed proof (Ch. 6)

**Axiom / starting states:** `s_elliptic_curve_over_Q`, `s_coprime_triple_a_b_c_with_a_plus_b_equals_c` *(new)*, `s_mochizuki_IUT_framework` *(new, as an auxiliary axiomatic input declared by the disputed proof)*
**Terminal theorem state:** `s_abc_conjecture_mochizuki_claimed` *(new, kind: theorem — with caveat: contested as of 2026; the chain below reports the claimed derivation as published in PRIMS 2021)*

**Steps:**
1. input: `s_coprime_triple_a_b_c_with_a_plus_b_equals_c` --[t_structural_isomorphism {associate the Frey-like elliptic curve y² = x(x − a)(x + b); anabelian reconstruction recovers arithmetic from étale fundamental group}]--> output: `s_anabelian_reconstruction_of_E` *(new)*
2. input: `⟨s_anabelian_reconstruction_of_E, s_mochizuki_IUT_framework⟩` --[t_auxiliary_construction {Hodge theaters, log-shells, theta-link — a non-ring-theoretic bridge between two "universes"}]--> output: `s_theta_link_between_hodge_theaters` *(new)*
3. input: `s_theta_link_between_hodge_theaters` --[t_heights_and_galois_rep_bridge {track log-volume deformations across the theta-link to obtain a global height inequality}]--> output: `s_log_volume_inequality` *(new)*
4. input: `s_log_volume_inequality` --[t_reductio_ad_absurdum {finitely many triples can violate c > rad(abc)^{1+ε}; all others are ruled out by the inequality — ⚠ community-disputed: Scholze–Stix 2018 identify this step as either trivial or invalid}]--> output: `s_abc_conjecture_mochizuki_claimed`

**Techniques used:** 13 structuralIsomorphism; C2 auxiliaryConstruction; C9 heightsAndGaloisRepBridge; C7 reductioAdAbsurdum

**Note:** This chain is flagged as contested. The orchestrator may wish to mark `s_abc_conjecture_mochizuki_claimed` with `status: disputed` in the graph, distinct from accepted theorems.

---

## Part B — Summary of new nodes

### B1. New state ids introduced (18 total)

**Theorem / terminal nodes (8, kind: theorem):**
- `s_zermelo_well_ordering` — Zermelo's Well-Ordering Theorem
- `s_noether_isomorphism_theorems` — Noether's three isomorphism theorems
- `s_godel_completeness_theorem` — Gödel's completeness theorem for first-order logic
- `s_banach_tarski_paradox` — Banach–Tarski paradox
- `s_stone_weierstrass_theorem` — Stone–Weierstrass approximation
- `s_stone_representation_theorem` — Stone representation / Boolean-algebra duality
- `s_full_modularity_theorem_BCDT` — Full modularity (Breuil–Conrad–Diamond–Taylor 2001)
- `s_abc_conjecture_mochizuki_claimed` — abc, Mochizuki's contested proof (status: disputed)

**Axiom / input nodes (4):**
- `s_axiom_of_choice_function_phi` — choice function φ on power-set minus ∅
- `s_first_order_logic_language` — first-order language (signature + variables)
- `s_consistent_first_order_theory_T` — consistent first-order theory T
- `s_normal_subgroup_N_in_G` — normal subgroup
- `s_group_homomorphism_f` — group homomorphism f
- `s_compact_hausdorff_space` — compact Hausdorff space (reused pattern)
- `s_point_separating_unital_subalgebra_A_of_C_X_R` — point-separating unital subalgebra
- `s_boolean_algebra_B` — Boolean algebra B
- `s_coprime_triple_a_b_c_with_a_plus_b_equals_c` — coprime (a,b,c), a+b=c
- `s_mochizuki_IUT_framework` — IUT framework (disputed auxiliary axiomatic input)
- `s_free_group_F2_on_two_generators` — free group F₂

**Intermediate state nodes (8):**
- `s_maximal_gamma_set_on_M` — maximal γ-set (Zermelo)
- `s_abstract_subobject_quotient_morphism_pattern` — Noether isomorphism abstract pattern
- `s_canonical_quotient_by_kernel_map` — canonical map G/ker(f) → im(f)
- `s_consistent_theory_with_witnesses` — Henkin witness extension (stage 1)
- `s_maximal_consistent_henkin_theory_T_star` — maximal Henkin theory T*
- `s_paradoxical_decomposition_of_F2` — paradoxical decomposition of F₂
- `s_F2_as_subgroup_of_SO3` — F₂ embedded in SO(3)
- `s_paradoxical_sphere_decomposition` — paradoxical S² decomposition
- `s_closure_of_A_is_a_lattice` — closure of A is a lattice (Stone–Weierstrass)
- `s_pointwise_matching_family_f_xy` — family {f_{xy}} matching g at pairs
- `s_ultrafilter_spectrum_Spec_B` — Spec(B), ultrafilter spectrum
- `s_compact_totally_disconnected_stone_space` — Stone space of B
- `s_ramification_stratification_of_elliptic_curves` — stratification by conductor + ramification
- `s_non_semistable_modularity_cases_handled` — non-semistable cases proven modular
- `s_anabelian_reconstruction_of_E` — anabelian reconstruction of Frey-like E
- `s_theta_link_between_hodge_theaters` — theta-link
- `s_log_volume_inequality` — log-volume / height inequality (Mochizuki)

(Count note: 8 axioms + 8 theorems + 11 intermediates = 27 new ids. Of these, a few axiom candidates — `s_compact_hausdorff_space`, `s_coprime_triple_a_b_c_with_a_plus_b_equals_c` — are generic enough that Round-5 dedup may merge them with existing ids if the philosopher finds near-duplicates.)

### B2. Technique fan-in audit

- **t_auxiliary_construction** (C2): 6 new usages — Zermelo γ-sets, Gödel completeness Henkin constants, Banach–Tarski orbit selection, Stone–Weierstrass f_{xy}, Stone representation Spec(B), Mochizuki Hodge theaters. Confirms the Round-0 addition was essential for chapter-5 classics.
- **t_reductio_ad_absurdum** (C7): 2 new usages — Zermelo maximality contradiction, Mochizuki abc inequality. Previously in iter-1 `t_infinite_descent {dual form}` was used for Brouwer/Halting; the new C7 node fits these "pure" contradictions more cleanly than the "descent-style" reading.
- **t_structural_isomorphism** (C5): 4 new usages (Gödel completeness term model, Noether iso, Banach–Tarski F₂ ↪ SO(3), Mochizuki anabelian reconstruction) — solidifies it as one of the most-reused techniques across chapters.
- **t_wiles_modularity** (umbrella, C6/C9) + **t_level_lowering_bridge** (C9): first usages of the modern "umbrella + specialization" pattern as instructed by the Round-0 corrections. Shows the bridge-specialization fan-in coming online.
- **t_heights_and_galois_rep_bridge** (C9): first usage (Mochizuki step 3). Previously absent; Round-0 addition validated.
- **t_compactness_argument** (C6): 3 new usages (Gödel completeness Zorn step, Stone–Weierstrass finite-cover piecing, Stone representation via Tychonoff). Continues as the workhorse of "choose a good maximal/accumulation element."
- **t_duality** (C3): 1 new usage (Stone representation). Complements iter-1 duality usages (Galois, Nullstellensatz, Stokes, Desargues); Stone completes the algebra↔topology-duality quadrant at the top level.

### B3. Flags

- **⚠ disputed chain:** `s_abc_conjecture_mochizuki_claimed` — the community has not accepted this proof as of 2026; the Scholze–Stix objection pinpoints step 3's "theta-link tracking" as the locus of failure. Marked with `status: disputed` recommendation.
- **⚠ partial-fit: IUT framework as axiom.** The node `s_mochizuki_IUT_framework` is declared as an auxiliary axiomatic input to reflect that, from the standpoint of the rest of mathematics, IUT's basic constructions (Hodge theaters, log-shells) are taken on their own terms. If Round 5 formalizes, an alternative is to treat the whole IUT machinery as a single compound technique node `t_iut_theta_link` with subgraph — flagged for orchestrator decision.
- **⚠ partial-fit: ZFC axiom bundled with AC.** In Zermelo, Banach–Tarski, and Gödel completeness, I treat `s_zfc_axioms` as including Choice, but the historical papers explicitly isolate AC. If the graph distinguishes ZF vs ZFC, add a separate axiom node `s_axiom_of_choice` (weaker than full ZFC) and let the three chains depend on `⟨s_zf_axioms, s_axiom_of_choice⟩`. In Stone representation, the weaker Boolean Prime Ideal Theorem suffices — flagged for possible refinement.
- **⚠ no new not-in-toolbox flags.** Every step maps cleanly to an existing toolbox entry (including the Round-0 additions `t_auxiliary_construction`, `t_reductio_ad_absurdum`, `t_heights_and_galois_rep_bridge`, `t_level_lowering_bridge`). The Round-0 cleanup was sufficient for chapters 5–6.

---

## Self-audit (Part C)

- **Theorem count per chapter (in source):**
  - Ch. 5: 18 level-3 theorem headings.
  - Ch. 6: 15 level-3 theorem headings (includes abc Mochizuki as a distinct heading; does not count FLT/Modularity as duplicates — counted once each).
- **Iter-1 coverage:**
  - Ch. 5: 12 of 18 covered. (Hilbert Basis, Nullstellensatz, Brouwer, Noether sym., Gödel Inc., Banach FPT, Hahn–Banach, Tychonoff, Halting, Con(ZFC+GCH), Ramsey, Birkhoff.)
  - Ch. 6: 13 of 15 covered. (Atiyah–Singer, CFSG, Cohen CH, Four Color, Faltings, Wiles FLT, Perelman, Kepler, Green–Tao, Zhang/Maynard, Helfgott, Robertson–Seymour, Szemerédi.)
- **New chains in this round:** 8 (6 in Ch. 5, 2 in Ch. 6).
- **Combined iter-1 + iter-2 chapter coverage after this round:** 18/18 = 100% Ch. 5; 15/15 = 100% Ch. 6.
- **New state ids created:** 27 (8 theorems + 8–11 axioms + 8–11 intermediates; see B1).
- **New technique nodes created:** 0 (all steps mapped to existing techniques, including the Round-0 specializations).
- **⚠ not-in-toolbox flags:** 0 firm. 3 partial-fit / sociological flags (IUT framework handling; ZFC vs ZF+AC split; disputed Mochizuki status).

The prompt's expected target of "~18 in ch. 05 and ~15 in ch. 06 (minus whatever is already in iter-1)" resolves, on actual chapter content, to 6 + 2 = 8 missing. I wrote chains for all 8.
