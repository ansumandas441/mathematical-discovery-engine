# Brief Catalog Skeletons — Area F (Geometry & Topology)

Phase B bulk skeleton expansion for the 27 bulleted theorems in:
- `07_brief_catalog.md` §Topology (General and Algebraic) — 21 items
- `07_brief_catalog.md` §Differential Geometry — 6 items

Conventions: one-step skeletons, technique ids matched to canonical toolbox.

---

## Topology (General and Algebraic)

### Heine–Borel theorem
**Terminal:** `s_heine_borel`
**Axioms:** `s_real_numbers`
**Steps:**
1. input: `⟨s_real_numbers⟩` --[t_compactness_argument]--> output: `s_heine_borel`

### Urysohn's lemma
**Terminal:** `s_urysohn_lemma`
**Axioms:** `s_normal_hausdorff_space`
**Steps:**
1. input: `⟨s_normal_hausdorff_space⟩` --[t_exhaustion_squeeze]--> output: `s_urysohn_lemma`

### Tietze extension theorem
**Terminal:** `s_tietze_extension`
**Axioms:** `s_normal_hausdorff_space`
**Steps:**
1. input: `⟨s_normal_hausdorff_space⟩` --[t_exhaustion_squeeze]--> output: `s_tietze_extension`

### Urysohn metrization theorem
**Terminal:** `s_urysohn_metrization`
**Axioms:** `s_second_countable_regular_hausdorff_space`
**Steps:**
1. input: `⟨s_second_countable_regular_hausdorff_space⟩` --[t_axiomatize_from_instances]--> output: `s_urysohn_metrization`

### Alexandroff compactification (one-point)
**Terminal:** `s_alexandroff_compactification`
**Axioms:** `s_locally_compact_hausdorff_space`
**Steps:**
1. input: `⟨s_locally_compact_hausdorff_space⟩` --[t_compactness_argument]--> output: `s_alexandroff_compactification`

### Borsuk–Ulam theorem
**Terminal:** `s_borsuk_ulam`
**Axioms:** `s_continuous_map_Sn_to_Rn`
**Steps:**
1. input: `⟨s_continuous_map_Sn_to_Rn⟩` --[t_obstruction_class]--> output: `s_borsuk_ulam`

### Ham sandwich theorem
**Terminal:** `s_ham_sandwich`
**Axioms:** `s_n_measurable_bodies_in_Rn`
**Steps:**
1. input: `⟨s_n_measurable_bodies_in_Rn⟩` --[t_obstruction_class]--> output: `s_ham_sandwich`

### Jordan curve theorem
**Terminal:** `s_jordan_curve_theorem`
**Axioms:** `s_simple_closed_curve_in_plane`
**Steps:**
1. input: `⟨s_simple_closed_curve_in_plane⟩` --[t_obstruction_class]--> output: `s_jordan_curve_theorem`

### Hairy ball theorem
**Terminal:** `s_hairy_ball`
**Axioms:** `s_topological_sphere_S2`, `s_continuous_tangent_vector_field`
**Steps:**
1. input: `⟨s_topological_sphere_S2, s_continuous_tangent_vector_field⟩` --[t_obstruction_class]--> output: `s_hairy_ball`

### Poincaré–Hopf theorem
**Terminal:** `s_poincare_hopf`
**Axioms:** `s_compact_smooth_manifold`, `s_continuous_tangent_vector_field`
**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_continuous_tangent_vector_field⟩` --[t_obstruction_class]--> output: `s_poincare_hopf`

### Brouwer's invariance of domain
**Terminal:** `s_invariance_of_domain`
**Axioms:** `s_continuous_injection_between_Rn_opens`
**Steps:**
1. input: `⟨s_continuous_injection_between_Rn_opens⟩` --[t_obstruction_class]--> output: `s_invariance_of_domain`

### de Rham's theorem
**Terminal:** `s_de_rham_theorem`
**Axioms:** `s_smooth_manifold_with_boundary`, `s_differential_form`
**Steps:**
1. input: `⟨s_smooth_manifold_with_boundary, s_differential_form⟩` --[t_structural_isomorphism]--> output: `s_de_rham_theorem`

### Whitney embedding theorem
**Terminal:** `s_whitney_embedding`
**Axioms:** `s_compact_smooth_manifold`
**Steps:**
1. input: `⟨s_compact_smooth_manifold⟩` --[t_raise_dimension]--> output: `s_whitney_embedding`

### Nash embedding theorem
**Terminal:** `s_nash_embedding`
**Axioms:** `s_riemannian_metric`, `s_compact_smooth_manifold`
**Steps:**
1. input: `⟨s_riemannian_metric, s_compact_smooth_manifold⟩` --[t_raise_dimension]--> output: `s_nash_embedding`

### Mostow rigidity theorem
**Terminal:** `s_mostow_rigidity`
**Axioms:** `s_closed_hyperbolic_manifold_dim_ge_3`
**Steps:**
1. input: `⟨s_closed_hyperbolic_manifold_dim_ge_3⟩` --[t_structural_isomorphism]--> output: `s_mostow_rigidity`

### Thurston's geometrization theorem
**Terminal:** `s_geometrization_theorem` *(already canonical)*
**Axioms:** `s_closed_3_manifold`
**Steps:**
1. input: `⟨s_closed_3_manifold⟩` --[t_ricci_flow_with_surgery]--> output: `s_geometrization_theorem`

### Smale's h-cobordism theorem
**Terminal:** `s_h_cobordism`
**Axioms:** `s_simply_connected_manifold_dim_ge_5`, `s_h_cobordism_between_manifolds`
**Steps:**
1. input: `⟨s_simply_connected_manifold_dim_ge_5, s_h_cobordism_between_manifolds⟩` --[t_obstruction_class]--> output: `s_h_cobordism`

### Freedman's theorem
**Terminal:** `s_freedman_theorem`
**Axioms:** `s_topological_4_manifold`
**Steps:**
1. input: `⟨s_topological_4_manifold⟩` --[t_obstruction_class]--> output: `s_freedman_theorem`

### Donaldson's theorem
**Terminal:** `s_donaldson_theorem`
**Axioms:** `s_smooth_4_manifold`
**Steps:**
1. input: `⟨s_smooth_4_manifold⟩` --[t_obstruction_class]--> output: `s_donaldson_theorem`

### Alexander duality
**Terminal:** `s_alexander_duality`
**Axioms:** `s_subspace_of_Sn`
**Steps:**
1. input: `⟨s_subspace_of_Sn⟩` --[t_duality]--> output: `s_alexander_duality`

### Poincaré duality
**Terminal:** `s_poincare_duality`
**Axioms:** `s_closed_oriented_n_manifold`
**Steps:**
1. input: `⟨s_closed_oriented_n_manifold⟩` --[t_duality]--> output: `s_poincare_duality`

---

## Differential Geometry

### Hopf–Rinow theorem
**Terminal:** `s_hopf_rinow`
**Axioms:** `s_riemannian_metric`, `s_connected_riemannian_manifold`
**Steps:**
1. input: `⟨s_riemannian_metric, s_connected_riemannian_manifold⟩` --[t_compactness_argument]--> output: `s_hopf_rinow`

### Cartan–Hadamard theorem
**Terminal:** `s_cartan_hadamard`
**Axioms:** `s_complete_simply_connected_nonpositive_curvature_manifold`
**Steps:**
1. input: `⟨s_complete_simply_connected_nonpositive_curvature_manifold⟩` --[t_rescale_for_asymptotic_geometry]--> output: `s_cartan_hadamard`

### Myers's theorem
**Terminal:** `s_myers_theorem`
**Axioms:** `s_riemannian_metric`, `s_ricci_curvature_positive_lower_bound`
**Steps:**
1. input: `⟨s_riemannian_metric, s_ricci_curvature_positive_lower_bound⟩` --[t_compactness_argument]--> output: `s_myers_theorem`

### Hodge theorem
**Terminal:** `s_hodge_theorem`
**Axioms:** `s_compact_riemannian_manifold`, `s_differential_form`
**Steps:**
1. input: `⟨s_compact_riemannian_manifold, s_differential_form⟩` --[t_structural_isomorphism]--> output: `s_hodge_theorem`

### Chern–Gauss–Bonnet theorem
**Terminal:** `s_chern_gauss_bonnet`
**Axioms:** `s_compact_smooth_manifold`, `s_riemannian_metric`
**Steps:**
1. input: `⟨s_compact_smooth_manifold, s_riemannian_metric⟩` --[t_duality]--> output: `s_chern_gauss_bonnet`

### Uniformization theorem
**Terminal:** `s_uniformization_theorem`
**Axioms:** `s_simply_connected_riemann_surface`
**Steps:**
1. input: `⟨s_simply_connected_riemann_surface⟩` --[t_structural_isomorphism]--> output: `s_uniformization_theorem`

---

## Report

(a) **Per-section counts:**
- Topology (General and Algebraic): 21 / 21
- Differential Geometry: 6 / 6
- Total: 27 / 27

(b) **⚠ technique inference flags:** None. All 27 skeletons use existing toolbox ids (`t_compactness_argument`, `t_exhaustion_squeeze`, `t_axiomatize_from_instances`, `t_obstruction_class`, `t_structural_isomorphism`, `t_raise_dimension`, `t_ricci_flow_with_surgery`, `t_duality`, `t_rescale_for_asymptotic_geometry`).

(c) **New techniques proposed:** 0 (as expected).

**Notes on node reuse:**
- `s_geometrization_theorem` reused from canonical index (not re-derived).
- `s_compact_smooth_manifold`, `s_riemannian_metric`, `s_differential_form`, `s_smooth_manifold_with_boundary`, `s_topological_sphere_S2`, `s_closed_3_manifold`, `s_real_numbers` all reused verbatim from canonical axiom list.
- Remaining axioms (e.g. `s_normal_hausdorff_space`, `s_closed_oriented_n_manifold`, `s_subspace_of_Sn`, `s_simply_connected_riemann_surface`) are natural new area-F axioms; Phase A integration can deduplicate against any pre-existing nodes.
