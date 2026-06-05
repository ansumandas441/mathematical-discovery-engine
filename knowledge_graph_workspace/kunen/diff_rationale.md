# Kunen (1980) Diff Rationale — GAP = Kunen candidates − existing coverage

Candidates scanned: 113 (from `candidates.md`). Refs: 171 Jech-added + 1224 existing set-theory nodes.
Result: **16 KEPT, 97 SKIPPED.** Set theory was already very deeply covered (Jech 2003 just integrated), so the large majority are duplicates under some existing name.

## KEPT (16) — genuinely absent mathematical identities

| Candidate | New id | Why kept |
|---|---|---|
| Ordered Pair (Kuratowski) | `s_ordered_pair_kuratowski` | No ordered-pair / Kuratowski node anywhere. |
| Relation / Function | `s_relation_function` | No "relation/function as a set of pairs" node. |
| Transitive Set | `s_transitive_set_def` | Only `s_transitive_closure` (the operation) exists; the bare notion was missing. |
| Natural Numbers ω | `s_natural_numbers_omega` | ω as least limit ordinal / finite ordinals not present as a node. |
| Transfinite Induction | `t_transfinite_induction` | Only `t_well_founded_recursion` and `t_epsilon_induction` exist; ordinal-indexed induction technique absent. |
| Transfinite Recursion | `t_transfinite_recursion` | Same — recursion along On as a distinct technique was missing. |
| Cumulative Hierarchy V_α | `s_kunen_cumulative_hierarchy` | Only `s_rank_function` (rank) and `s_mostowski_rank_function` exist; the V_α hierarchy itself was absent. |
| Well-Ordering Theorem | `s_well_ordering_theorem` | Only `s_constructible_wellordering` (<_L) and `s_axiom_of_choice`; Zermelo's "every set well-orderable ⇔ AC" not present. |
| Δ_0 / Σ_0 Formula | `s_delta_0_formula` | `s_levy_hierarchy` covers Σ_n/Π_n but the Δ_0/bounded-formula base level (absolute for transitive models) had no node. |
| Relativization φ^M | `t_relativization` | Only `s_relative_constructibility_L_A` and a relativization *barrier*; the φ^M technique itself absent. |
| Transitive Model | `s_kunen_transitive_model` | Only specific models (`s_HOD_..._inner_model`, `s_model_of_ZFC_plus_not_CH`); the general "transitive M ⊨ T" notion missing. |
| Countable Transitive Model (CTM) | `s_countable_transitive_model` | The forcing ground-model object; no CTM node existed. |
| Löwenheim–Skolem → CTM | `s_lowenheim_skolem_ctm` | Only `t_skolem_hull` technique; the downward-LS theorem yielding a countable transitive model had no node. |
| Con(ZFC) Not Provable in ZFC | `s_con_zfc_unprovable_in_zfc` | Gödel's 2nd incompleteness applied to ZFC — no incompleteness node in the set-theory corpus. |
| ◊⁺ (Diamond-Plus) | `s_diamond_plus` | Only `s_diamond_principle_on_omega_1` and `s_club_principle`; ◊⁺ absent. |
| ◊⁺ ⇒ Kurepa Tree | `s_diamond_plus_kurepa` | `s_kurepa_tree_in_L` exists but the ◊⁺ → Kurepa implication does not. |

## SKIPPED (97) — duplicates of existing coverage (representative mapping)

Foundations / axioms (all SKIP): ZFC Axioms → `s_zfc_axioms`; the nine individual axioms (Extensionality, Foundation, Pairing, Union, Power Set, Infinity, Comprehension, Replacement, Choice) are subsumed by `s_zfc_axioms` + `s_axiom_of_choice` (corpus does not split them out and Kunen's list adds no new identity beyond the package); Ordinal → `s_ordinal_number`; Successor/Limit Ordinals → `s_successor_ordinal` + `s_limit_ordinal`; Rank of a Set → `s_rank_function`.

Cardinals: Cardinality/Cardinal → `s_cardinal_number`; Aleph Function → `s_aleph_function`; Cardinal Arithmetic → `s_cardinal_arithmetic`; Cofinality → `s_cofinality`; Regular/Singular → `s_regular_cardinal`/`s_singular_cardinal`; Successor Cardinal Regular → `s_successor_cardinals_regular`; König's Theorem → `s_konig_cardinal_theorem`; GCH → `s_generalized_continuum_hypothesis`; CH → covered via `s_continuum_hypothesis_or_GCH` / `s_ch_independent_of_zfc`.

Infinitary combinatorics: Club → `s_club_set`; Club Filter → `s_club_filter`; Diagonal Intersection → `s_diagonal_intersection_club`; Stationary → `s_stationary_subset_of_kappa`; Fodor → `s_fodor_lemma`; Δ-System & Lemma & Method → `s_sunflower_lemma_erdsko`; Tree / Levels / Branch → `s_tree_set_theoretic`, `s_tree_branch_level_height`; Aronszajn & existence → `s_aronszajn_tree`(+`_existence`); Suslin tree/line/SH → `s_suslin_tree`, `s_suslin_problem`, `s_suslin_tree_line_equivalence`; Kurepa → `s_kurepa_tree`; Partition Calculus → `s_partition_calculus`; Ramsey → `s_ramsey_theorem_infinite`; Erdős–Rado → `s_erdos_rado_theorem`.

Martin's Axiom block: MA(κ) → `s_martins_axiom_MA_kappa`; MA → `s_martins_axiom`; MA ⇒ ¬Suslin → `s_MA_implies_SH`; MA(κ) ⇒ 2^ℵ0>κ → `s_MA_aleph1_negates_CH`; MA & AD families and MA ⇒ union meager/null → `s_MA_measure_category`; Almost Disjoint Family → folded into `s_MA_measure_category` context (no standalone gap kept, per "don't inflate"); Diamond ◊ → `s_diamond_principle_on_omega_1`; ◊⇒CH → `s_diamond_implies_ch`; ◊⇒Suslin → `s_diamond_implies_suslin_tree`; Club Principle ♣ → `s_club_principle`.

Models/absoluteness: Absoluteness → `t_absoluteness`/`s_mostowski_absoluteness`; Lévy Hierarchy → `s_levy_hierarchy`; Σ_1/Π_1 & basic-notion absoluteness → `t_absoluteness`+`s_shoenfield_absoluteness`; Reflection Theorem & Method → `s_reflection_principle` / `s_levy_reflection`; Mostowski Collapse & Lemma → `s_mostowski_collapse` (+`t` form); Well-Founded Relation → `s_well_founded_relation`; ZF without AC → covered by `s_axiom_of_choice` context.

Constructibility/HOD: Gödel Operations → `t_godel_operations`; L_α → `s_L_hierarchy_L_alpha`; L → `s_constructible_universe_L`; V=L → `s_v_l_axiom_of_constructibility`; L inner model of ZF → `s_L_models_ZF`; Condensation → `t_fine_structural_condensation`; L⊨AC → `s_constructible_wellordering`; L⊨GCH → `s_GCH_in_L`; L⊨◊ → `s_diamond_holds_in_L`; Con(ZFC)→Con(ZFC+GCH) → `s_con_zfc_gch`; L⊨□ → `s_square_holds_in_L`; L[A] → `s_relative_constructibility_L_A`; Absoluteness of L → `s_absoluteness_to_L`; HOD/OD/HOD⊨ZFC → `s_HOD_R_ordinals_inner_model`.

Consistency framing: Consistency/Con(T), Relative Consistency Proof, Finite ZFC Fragments, Formalizing the Metatheory, Relative-Consistency Framework, Independence of CH → covered by `s_con_zfc_gch`, `s_con_zfc_not_ch_cohen`, `s_ch_independent_of_zfc`, `s_cohens_independence_of_ch`, `s_reflection_schema_for_finite_subtheory`. (Only the Gödel-2nd-incompleteness item was a true gap → KEPT.)

Forcing (Ch VII): Forcing Poset → `s_notion_of_forcing`; Dense → `s_dense_predense`; Compatible/Incompatible/antichain → `s_compatible_conditions`; Filter/Generic Filter → `s_generic_filter`; Generic existence (Rasiowa–Sikorski) → `s_rasiowa_sikorski_lemma`; P-Name → `t_p_names`; Valuation/Interpretation → folded into `s_forcing_extension_mg` machinery; Generic Extension M[G] → `s_forcing_extension_mg`; Canonical Names → `t_canonical_names`; Forcing Relation → `s_forcing_relation`; Definability Lemma → `s_definability_lemma_forcing`; Truth Lemma → `s_truth_lemma`; Forcing Theorem → `s_forcing_theorem`; M[G]⊨ZFC → covered by `s_forcing_theorem`/`s_maximum_principle_forcing`; Forcing Method → `t_forcing_technique`; ccc & preservation → `s_ccc_forcing`, `s_ccc_preserves_cardinals`; κ-closed & no-new-sequences → `s_kappa_closed_forcing`, `s_closed_forcing_adds_no_sequences`; Cohen forcing/real/ccc → `t_cohen_forcing`, `s_cohen_forcing_is_ccc`, `s_cohen_forcing`; Con(¬CH) → `s_con_zfc_not_ch_cohen`; Con(CH) via forcing → covered by closed-forcing nodes; Product Forcing & Lemma → `s_product_forcing_lemma`; Collapsing Cardinals / Lévy Collapse → `t_levy_collapse`, `s_levy_collapse_model`; Separative & Quotient → `t_separative_quotient`; Regular Open Algebra → `s_regular_open_algebra`; Boolean-Valued Model & Method & Equivalence → `s_boolean_valued_universe`, `t_boolean_truth_value`; Easton Forcing & Theorem → `s_easton_class_forcing`, `s_easton_theorem`; Random Real → `s_random_real_forcing`, `s_generic_random_real`; Nice Name & Counting & Preservation-of-GCH → `t_nice_names`.

Iteration (Ch VIII): Two-Step P∗Q̇ & theorem → `t_two_step_iteration`; Finite Support Iteration → `t_finite_support_iteration`; Direct/Inverse Limit → covered by FS/CS iteration techniques; ccc preserved under FS → `s_fs_iteration_ccc`; Solovay–Tennenbaum → `s_con_MA_not_CH`(+`s_con_SH`); Iterated Forcing Method → `t_iterated_forcing`; Bookkeeping → subsumed by `t_iterated_forcing` (no distinct identity, SKIP per don't-inflate).

## Notes on judgment calls

- **Almost Disjoint Family** and **Bookkeeping** were treated as not-distinct-enough (covered by `s_MA_measure_category` and `t_iterated_forcing` respectively) and SKIPPED to avoid inflation.
- The nine **individual ZFC axioms** were SKIPPED because the corpus represents them as the bundled `s_zfc_axioms`; splitting would add naming, not new mathematical identity.
- The four small **Ch I encoding nodes** (ordered pair, relation/function, transitive set, ω) were KEPT because no node of that identity exists at all — they are foundational vocabulary the graph genuinely lacked, not redundant restatements.
