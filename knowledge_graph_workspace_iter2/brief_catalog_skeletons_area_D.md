# Brief Catalog Skeletons — Area D (Logic/Foundations + Set Theory + Combinatorics)

## Logic and Foundations

### Compactness theorem
**Terminal:** `s_compactness_theorem_fol`
**Axioms:** `s_first_order_peano_arithmetic`, `s_zfc_axioms`
**Steps:**
1. input: `⟨s_first_order_peano_arithmetic, s_zfc_axioms⟩` --[t_ultraproduct_transfer {target: "satisfiability lifts from finite subsets"}]--> output: `s_compactness_theorem_fol`

### Löwenheim–Skolem theorem
**Terminal:** `s_lowenheim_skolem`
**Axioms:** `s_first_order_peano_arithmetic`, `s_zfc_axioms`
**Steps:**
1. input: `⟨s_first_order_peano_arithmetic, s_zfc_axioms⟩` --[t_compactness_argument {target: "models of every infinite cardinality"}]--> output: `s_lowenheim_skolem`

### Church–Rosser theorem
**Terminal:** `s_church_rosser`
**Axioms:** `s_zfc_axioms`
**Steps:**
1. input: `⟨s_zfc_axioms⟩` --[t_reduce_to_canonical_form {target: "confluence of β-reduction"}]--> output: `s_church_rosser`

### Deduction theorem
**Terminal:** `s_deduction_theorem`
**Axioms:** `s_first_order_peano_arithmetic`
**Steps:**
1. input: `⟨s_first_order_peano_arithmetic⟩` --[t_axiomatize_from_instances {target: "Γ∪{A}⊢B ↔ Γ⊢A→B"}]--> output: `s_deduction_theorem`

### Łoś's theorem
**Terminal:** `s_los_theorem`
**Axioms:** `s_first_order_peano_arithmetic`, `s_zfc_axioms`
**Steps:**
1. input: `⟨s_first_order_peano_arithmetic, s_zfc_axioms⟩` --[t_ultraproduct_transfer {target: "first-order truth in ultraproduct ↔ factor truth"}]--> output: `s_los_theorem`

### Craig's interpolation theorem
**Terminal:** `s_craig_interpolation`
**Axioms:** `s_first_order_peano_arithmetic`
**Steps:**
1. input: `⟨s_first_order_peano_arithmetic⟩` --[t_axiomatize_from_instances {target: "interpolant in shared vocabulary"}]--> output: `s_craig_interpolation`

### Beth's definability theorem
**Terminal:** `s_beth_definability`
**Axioms:** `s_first_order_peano_arithmetic`
**Steps:**
1. input: `⟨s_first_order_peano_arithmetic⟩` --[t_axiomatize_from_instances {target: "implicit ⇔ explicit definability"}]--> output: `s_beth_definability`

### Lindström's theorem
**Terminal:** `s_lindstrom_theorem`
**Axioms:** `s_first_order_peano_arithmetic`, `s_compactness_theorem_fol`, `s_lowenheim_skolem`
**Steps:**
1. input: `⟨s_compactness_theorem_fol, s_lowenheim_skolem⟩` --[t_axiomatize_from_instances {target: "characterize first-order logic uniquely"}]--> output: `s_lindstrom_theorem`

### Morley's categoricity theorem
**Terminal:** `s_morley_categoricity`
**Axioms:** `s_first_order_peano_arithmetic`, `s_zfc_axioms`
**Steps:**
1. input: `⟨s_first_order_peano_arithmetic, s_zfc_axioms⟩` --[t_ultraproduct_transfer {target: "categoricity transfers to all uncountable cardinals"}]--> output: `s_morley_categoricity`

### Martin's Borel determinacy theorem
**Terminal:** `s_martin_borel_determinacy`
**Axioms:** `s_zfc_axioms`
**Steps:**
1. input: `⟨s_zfc_axioms⟩` --[t_axiomatize_from_instances {target: "Borel games determined via iterated replacement"}]--> output: `s_martin_borel_determinacy`

### Cohen's forcing theorems
**Terminal:** `s_cohen_forcing`
**Axioms:** `s_zfc_axioms`, `s_model_of_ZFC_plus_not_CH`
**Steps:**
1. input: `⟨s_zfc_axioms, s_model_of_ZFC_plus_not_CH⟩` --[t_force_independence {target: "CH and AC independent of ZF"}]--> output: `s_cohen_forcing`

### Matiyasevich's theorem (MRDP)
**Terminal:** `s_mrdp_theorem`
**Axioms:** `s_turing_machine_model`, `s_first_order_peano_arithmetic`
**Steps:**
1. input: `⟨s_turing_machine_model, s_first_order_peano_arithmetic⟩` --[t_arithmetize_syntax {target: "recursive sets are Diophantine"}]--> output: `s_mrdp_theorem`

### Paris–Harrington theorem
**Terminal:** `s_paris_harrington`
**Axioms:** `s_first_order_peano_arithmetic`, `s_ramsey_theorem_infinite`
**Steps:**
1. input: `⟨s_first_order_peano_arithmetic, s_ramsey_theorem_infinite⟩` --[t_diagonalize {target: "true-in-ℕ but PA-unprovable Ramsey statement"}]--> output: `s_paris_harrington`

### Gentzen's consistency proof
**Terminal:** `s_gentzen_consistency`
**Axioms:** `s_first_order_peano_arithmetic`
**Steps:**
1. input: `⟨s_first_order_peano_arithmetic⟩` --[t_infinite_descent {target: "transfinite induction up to ε₀ bounds cut-elimination"}]--> output: `s_gentzen_consistency`

## Set Theory

### Axiom of choice equivalents
**Terminal:** `s_ac_equivalents`
**Axioms:** `s_zfc_axioms`
**Steps:**
1. input: `⟨s_zfc_axioms⟩` --[t_structural_isomorphism {target: "Zorn ↔ well-ordering ↔ Tychonoff ↔ trichotomy"}]--> output: `s_ac_equivalents`

### Schröder–Bernstein theorem
**Terminal:** `s_schroder_bernstein`
**Axioms:** `s_zfc_axioms`
**Steps:**
1. input: `⟨s_zfc_axioms⟩` --[t_structural_isomorphism {target: "build bijection from mutual injections"}]--> output: `s_schroder_bernstein`

### Hartogs's theorem
**Terminal:** `s_hartogs_theorem`
**Axioms:** `s_zfc_axioms`, `s_infinite_set`
**Steps:**
1. input: `⟨s_zfc_axioms, s_infinite_set⟩` --[t_reductio_ad_absurdum {target: "least ordinal not injecting into X exists"}]--> output: `s_hartogs_theorem`

### König's theorem (cardinal)
**Terminal:** `s_konig_cardinal_theorem`
**Axioms:** `s_zfc_axioms`
**Steps:**
1. input: `⟨s_zfc_axioms⟩` --[t_diagonalize {target: "Σκᵢ < Πλᵢ via diagonal construction"}]--> output: `s_konig_cardinal_theorem`

### Reflection principle
**Terminal:** `s_reflection_principle`
**Axioms:** `s_zfc_axioms`
**Steps:**
1. input: `⟨s_zfc_axioms⟩` --[t_axiomatize_from_instances {target: "truths in V reflected to stages Vα"}]--> output: `s_reflection_principle`

### Silver's theorem
**Terminal:** `s_silver_theorem`
**Axioms:** `s_zfc_axioms`
**Steps:**
1. input: `⟨s_zfc_axioms⟩` --[t_compactness_argument {target: "GCH cannot first fail at singular of uncountable cofinality"}]--> output: `s_silver_theorem`

## Combinatorics

### Hall's marriage theorem
**Terminal:** `s_hall_marriage`
**Axioms:** `s_graph_definition`
**Steps:**
1. input: `⟨s_graph_definition⟩` --[t_pigeonhole_collision {target: "deficiency condition forces matching"}]--> output: `s_hall_marriage`

### König's lemma
**Terminal:** `s_konig_lemma`
**Axioms:** `s_graph_definition`, `s_infinite_set`
**Steps:**
1. input: `⟨s_graph_definition, s_infinite_set⟩` --[t_pigeonhole_collision {target: "infinite tree + finite branching ⇒ infinite path"}]--> output: `s_konig_lemma`

### Kőnig's theorem (bipartite)
**Terminal:** `s_konig_bipartite`
**Axioms:** `s_graph_definition`
**Steps:**
1. input: `⟨s_graph_definition⟩` --[t_duality {target: "max matching = min vertex cover via LP duality"}]--> output: `s_konig_bipartite`

### Dilworth's theorem
**Terminal:** `s_dilworth_theorem`
**Axioms:** `s_graph_definition`
**Steps:**
1. input: `⟨s_graph_definition⟩` --[t_duality {target: "max antichain = min chain cover"}]--> output: `s_dilworth_theorem`

### Mirsky's theorem
**Terminal:** `s_mirsky_theorem`
**Axioms:** `s_graph_definition`
**Steps:**
1. input: `⟨s_graph_definition⟩` --[t_duality {target: "max chain = min antichain cover (dual of Dilworth)"}]--> output: `s_mirsky_theorem`

### Turán's theorem
**Terminal:** `s_turan_theorem`
**Axioms:** `s_graph_definition`
**Steps:**
1. input: `⟨s_graph_definition⟩` --[t_sieve_by_optimized_quadratic {target: "balanced r-partite extremal for K_{r+1}-free"}]--> output: `s_turan_theorem`

### Erdős–Ko–Rado theorem
**Terminal:** `s_erdos_ko_rado`
**Axioms:** `s_zfc_axioms`
**Steps:**
1. input: `⟨s_zfc_axioms⟩` --[t_sieve_by_optimized_quadratic {target: "bound intersecting k-family by shifting"}]--> output: `s_erdos_ko_rado`

### Menger's theorem
**Terminal:** `s_menger_theorem`
**Axioms:** `s_graph_definition`
**Steps:**
1. input: `⟨s_graph_definition⟩` --[t_duality {target: "max vertex-disjoint paths = min vertex cut"}]--> output: `s_menger_theorem`

### Max-flow min-cut theorem
**Terminal:** `s_maxflow_mincut`
**Axioms:** `s_graph_definition`
**Steps:**
1. input: `⟨s_graph_definition⟩` --[t_duality {target: "LP duality between flow and cut"}]--> output: `s_maxflow_mincut`

### Kuratowski's theorem
**Terminal:** `s_kuratowski_planarity`
**Axioms:** `s_graph_definition`, `s_planar_graph`
**Steps:**
1. input: `⟨s_graph_definition, s_planar_graph⟩` --[t_obstruction_class {target: "K₅, K_{3,3} subdivisions are only obstructions"}]--> output: `s_kuratowski_planarity`

### Wagner's theorem
**Terminal:** `s_wagner_planarity`
**Axioms:** `s_graph_definition`, `s_planar_graph`, `s_minor_ordering`
**Steps:**
1. input: `⟨s_graph_definition, s_planar_graph, s_minor_ordering⟩` --[t_obstruction_class {target: "K₅, K_{3,3} minors are only obstructions"}]--> output: `s_wagner_planarity`

### Schur's theorem (Ramsey)
**Terminal:** `s_schur_ramsey`
**Axioms:** `s_integers`, `s_k_coloring_of_pairs`
**Steps:**
1. input: `⟨s_integers, s_k_coloring_of_pairs⟩` --[t_pigeonhole_collision {target: "monochromatic x+y=z in r-colored {1..N}"}]--> output: `s_schur_ramsey`

### Van der Waerden's theorem
**Terminal:** `s_van_der_waerden`
**Axioms:** `s_integers`, `s_k_coloring_of_pairs`
**Steps:**
1. input: `⟨s_integers, s_k_coloring_of_pairs⟩` --[t_pigeonhole_collision {target: "monochromatic AP of length k"}]--> output: `s_van_der_waerden`

### Hales–Jewett theorem
**Terminal:** `s_hales_jewett`
**Axioms:** `s_k_coloring_of_pairs`
**Steps:**
1. input: `⟨s_k_coloring_of_pairs⟩` --[t_pigeonhole_collision {target: "combinatorial line in high-dim cube"}]--> output: `s_hales_jewett`

### Hindman's theorem
**Terminal:** `s_hindman_theorem`
**Axioms:** `s_integers`, `s_infinite_set`
**Steps:**
1. input: `⟨s_integers, s_infinite_set⟩` --[t_compactness_argument {target: "finite-sums set via Stone–Čech idempotents"}]--> output: `s_hindman_theorem`

### Cayley's formula
**Terminal:** `s_cayley_formula`
**Axioms:** `s_graph_definition`
**Steps:**
1. input: `⟨s_graph_definition⟩` --[t_structural_isomorphism {target: "Prüfer bijection trees ↔ sequences"}]--> output: `s_cayley_formula`

### Matrix-tree theorem
**Terminal:** `s_matrix_tree`
**Axioms:** `s_graph_definition`
**Steps:**
1. input: `⟨s_graph_definition⟩` --[t_character_decomposition_count {target: "spanning tree count = Laplacian cofactor"}]--> output: `s_matrix_tree`

### BEST theorem
**Terminal:** `s_best_theorem`
**Axioms:** `s_graph_definition`, `s_eulerian_path_criterion`
**Steps:**
1. input: `⟨s_graph_definition, s_eulerian_path_criterion⟩` --[t_character_decomposition_count {target: "Eulerian circuits via arborescences × degrees"}]--> output: `s_best_theorem`

### Burnside's lemma
**Terminal:** `s_burnside_lemma`
**Axioms:** `s_finite_group`, `s_group_action`
**Steps:**
1. input: `⟨s_finite_group, s_group_action⟩` --[t_character_decomposition_count {target: "#orbits = avg #fixed points"}]--> output: `s_burnside_lemma`

### Pólya enumeration theorem
**Terminal:** `s_polya_enumeration`
**Axioms:** `s_finite_group`, `s_group_action`, `s_burnside_lemma`
**Steps:**
1. input: `⟨s_finite_group, s_group_action, s_burnside_lemma⟩` --[t_character_decomposition_count {target: "cycle-index generating function for colorings"}]--> output: `s_polya_enumeration`

### Pigeonhole principle
**Terminal:** `s_pigeonhole_principle`
**Axioms:** `s_zfc_axioms`
**Steps:**
1. input: `⟨s_zfc_axioms⟩` --[t_pigeonhole_collision {target: "n+1 objects in n boxes ⇒ collision"}]--> output: `s_pigeonhole_principle`
