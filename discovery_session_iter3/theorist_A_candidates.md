# Theorist A — Candidate Theorems (Categorical / Stone / Galois / Cluster‑12 Frontier)

**Author role**: Theorist A
**Portfolio**: cluster‑12 (homological/categorical) × edge‑state nodes in clusters 02/03/05/06/09/10.
**Source graph**: `/Users/primetrce/Documents/maths/knowledge_graph.json` (752 nodes, 1258 edges).
**Recon report**: `/Users/primetrce/Documents/maths/discovery_session_iter3/recon_leverage_points.md`.

I have selected 7 candidates. Each is derived by re‑running a specific technique (already in the graph) against an edge‑state or near‑edge node (already in the graph) where that pairing is absent from the edge list. I have self‑graded harshly: four are COROLLARY‑OF‑KNOWN, two are LIKELY‑KNOWN‑UNDER‑OTHER‑NAME, one is LIKELY‑KNOWN with a SPECULATIVE corollary. No candidate is graded PLAUSIBLY‑NEW — the graded honesty *is* the contribution.

---

### Candidate A1 — Grothendieck–Galois via the Colimit Lift

**Derivation chain**: `s_fundamental_theorem_of_galois_theory` --[`t_category_theoretic_colimits_and_adjoints`]--> `s_profinite_galois_adjunction` (new state) --[`t_structural_isomorphism`]--> `T_A1`.

Recon seed 2. The precursor chain `s_field_extension_L_over_K → t_axiomatize_from_instances → s_galois_group → t_duality → s_galois_correspondence → t_structural_isomorphism → s_fundamental_theorem_of_galois_theory` is lifted by re‑feeding `s_galois_correspondence` into `t_category_theoretic_colimits_and_adjoints` (compound `sg_category_colimits_adjoints`), which was never applied.

**Statement (plain)**: The classical Galois correspondence — subgroups of Gal(L/K) trade places with intermediate fields — is the surface of a deeper adjunction. Taking the colimit of all finite Galois correspondences as L ranges over finite Galois subextensions of an algebraic closure recovers Grothendieck's form: finite separable extensions of K are equivalent to finite continuous sets acted on by the absolute Galois group Gal(K̄/K).

**Statement (formal)**:
- **Inherited (unsurprising)**: for each finite Galois L/K, the maps H ↦ L^H and M ↦ Gal(L/M) are a contravariant equivalence between (Sub Gal(L/K))^op and IntField(L/K). This is `s_galois_correspondence`.
- **Newly claimed**: the system {FinGal(L/K)} is directed under containment; Gal(K̄/K) := lim Gal(L/K) is a profinite group, and the adjoint pair (fixed‑points of Gal(K̄/K)) ⊣ Hom_K(−, K̄) is an adjoint equivalence between FinSep(K)^op and the category of finite continuous Gal(K̄/K)‑sets.
- **Speculative**: the same pattern upgrades to "étale sheaves on Spec K ↔ continuous Gal(K̄/K)‑sets" (SGA1, Exp. V); not currently wired in the graph.

**Derivation sketch**:
1. Start from `s_fundamental_theorem_of_galois_theory`.
2. Instantiate `sg_cat.s_diagram_in_C` with J = poset of finite Galois subextensions of K̄/K, C = Cat, F(L) = the Galois correspondence at L.
3. Apply `sg_cat.t_colimit_left_adjoint`: inclusions L₁ ⊆ L₂ induce restrictions Gal(L₂/K) → Gal(L₁/K).
4. Apply `sg_cat.t_yoneda_embed`: the dual tower is representable by the inverse limit Gal(K̄/K).
5. Invoke `sg_cat.t_freyd_adjoint_theorem`: solution‑set condition holds because each L/K is finite; adjoint pair exists.
6. External fact required: the Krull topology on Gal(K̄/K) — initial topology making all projections to finite quotients continuous (Krull 1928). Not in graph.
7. Apply `t_structural_isomorphism` on the limit diagram to upgrade "lattice anti‑iso" to "contravariant equivalence of categories".
8. Conclude: FinSep(K)^op ≃ FinCont‑Gal(K̄/K)‑Set.

**What's inherited vs. added**:
- Inherited: lattice anti‑iso at each finite level; edge `t_duality → s_galois_correspondence`; Yoneda and adjoint‑functor machinery.
- Newly added: the colimit/limit across finite subextensions; upgrade to category equivalence indexed by Gal(K̄/K). The finite case and categorical machinery sit separately in the graph; the wiring is new.

**Novelty assessment**: COROLLARY‑OF‑KNOWN. This is Grothendieck's Galois theory (SGA1 Exp. V, 1960–61), restated in Milne, Lenstra, Szamuely (*Galois Groups and Fundamental Groups*). The graph reproduces it mechanically — exactly the "this ought to be there" kind of theorem the recon flagged.

**Failure modes**:
1. **Inseparable extensions** — fails if separability is dropped. Test: K = 𝔽_p(t), L = 𝔽_p(t^{1/p}). The statement must quantify over FinSep(K).
2. **Non‑algebraic extensions** — transcendental extensions produce no continuous action.
3. **Topology** — must be Krull topology, not discrete. Mis‑stating collapses the equivalence.

**Proof‑integrity risk**: LOW. Textbook routine once the colimit step is identified.

---

### Candidate A2 — Representable‑Functor Formulation of Stone Duality

**Derivation chain**: `s_stone_representation_theorem` --[`t_representable_functor_trick`]--> `s_stone_spectrum_is_representable` (new state) --[`t_duality`]--> `T_A2`.

Recon seed 5 (representability half). Re‑feeds `s_compact_totally_disconnected_stone_space` and `s_ultrafilter_spectrum_Spec_B` into `t_representable_functor_trick`, which never touches either.

**Statement (plain)**: Stone's duality between Boolean algebras and Stone spaces is representable: there is a single universal Boolean algebra **2** = {0, 1} and a single universal Stone space **Ω** = {0, 1} (two‑point discrete) such that Spec(B) = Hom_{BoolAlg}(B, **2**) and Clopen(X) = Hom_{StoneSp}(X, **Ω**). Stone duality is Yoneda applied to the two‑element object on each side.

**Statement (formal)**:
- **Inherited**: BoolAlg^op ≃ StoneSp (this is `s_stone_representation_theorem`).
- **Newly claimed**: Spec : BoolAlg^op → StoneSp is naturally iso to Hom_BoolAlg(−, **2**); Clopen : StoneSp → BoolAlg^op is naturally iso to Hom_StoneSp(−, **Ω**). Together (**2**, **Ω**) is a *dualising pair* in the sense of Johnstone, *Stone Spaces* §VI.3.
- **Corollary (immediate from Yoneda)**: (**2**, **Ω**) is unique up to unique iso; every Boolean algebra embeds into some power of **2** — Stone's original embedding theorem (1936).

**Derivation sketch**:
1. Start from `s_compact_totally_disconnected_stone_space` (produced by `t_compactness_argument` in Stone's chain).
2. Observe `s_boolean_algebra_B --t_auxiliary_construction--> s_ultrafilter_spectrum_Spec_B`: ultrafilters of B = Boolean homs B → **2**.
3. Apply `sg_cat.t_yoneda_embed` with representing object **2** in BoolAlg and **Ω** in StoneSp.
4. Use edge `t_duality → s_stone_representation_theorem` for the categorical equivalence.
5. By Yoneda, any functor naturally iso to Hom(−, A) is represented by A up to unique iso; representability is determined by (**2**, **Ω**).
6. `t_compactness_argument` on products: Tychonoff (implicit in Stone chain) ensures ∏_I **Ω** is Stone.
7. Stone embedding: B ↪ **2**^{Spec B} by evaluation; dually X ↪ **Ω**^{Clopen X}.
8. Conclude: (**2**, **Ω**) is a dualising pair; Stone equivalence is representable on both sides.

**What's inherited vs. added**:
- Inherited: Stone equivalence; the representing role of ultrafilters; Spec and Clopen functors.
- Newly added: explicit statement that both sides are representable by the two‑point object, and the Yoneda upgrade identifying (**2**, **Ω**) as the universal dualising pair. Stone embedding falls out as a one‑line corollary.

**Novelty assessment**: COROLLARY‑OF‑KNOWN. Johnstone's *Stone Spaces* §VI.3 (1982) has this exactly, and every categorical‑logic textbook (Lambek–Scott, Mac Lane–Moerdijk) treats Stone duality as the canonical instance of duality via dualising object. Wiring value is real; mathematical content is textbook.

**Failure modes**:
1. **Distributive‑lattice generalisation** — replacing Boolean with distributive lattice forces Sierpiński dualising object and lands in Priestley spaces. Test: B = open sets of [0, 1].
2. **Size** — statement restricted to small BoolAlg; proper‑class Boolean algebras need care.
3. **Without choice** — Spec B = ultrafilters uses BPI (Boolean prime ideal theorem), strictly weaker than AC but not provable in ZF. Test in Fraenkel–Mostowski.

**Proof‑integrity risk**: LOW. Yoneda is mechanical; only wrinkle is discrete‑not‑Sierpiński topology on **Ω**, determined by the Boolean (not Heyting) structure on **2**.

---

### Candidate A3 — Forcing‑Parametrised Stone Duality ("P‑Stone Spectrum")

**Derivation chain**: `s_stone_representation_theorem` --[`t_force_independence`]--> `s_P_generic_stone_spectrum` (new, defined below) --[`t_representable_functor_trick` + `t_duality`]--> `T_A3`.

Recon seed 5 (forcing half; the speculative part). `t_force_independence` has five inputs in the graph but none is `s_ultrafilter_spectrum_Spec_B`.

**Statement (plain)**: Replace the ultrafilter spectrum of a Boolean algebra B with a "generic" spectrum obtained by forcing with a notion P, to get a Stone duality parametrised by P. Classical Stone duality is the P = trivial case; Cohen forcing gives a different Stone space; a structural comparison theorem says how much the choice of P matters.

**Statement (formal)**: Fix a complete Boolean algebra B and a forcing notion P ∈ V with separative quotient B_P.

**Definition (new, precise)**: The *P‑generic Stone spectrum* Spec_P(B) is the set of P‑generic filters G ⊆ P such that truth‑evaluation at G yields a Boolean homomorphism B → **2**, topologised as the coarsest topology making every "clopen of B" a clopen. When P is trivial, Spec_P(B) = Spec(B).

- **Inherited**: Stone duality at P = trivial (`s_stone_representation_theorem`).
- **Newly claimed**: for any set forcing P, Spec_P : BoolAlg^op → StoneSp is represented by **2**_P (the two‑valued model in V[G] under its natural Boolean structure). There is a natural transformation η_P : Spec → Spec_P whose cokernel measures how much P changes the spectrum.
- **Speculative corollary (explicit conjecture)**: for P = Cohen forcing at ω and B the free Boolean algebra on ω generators, Aut(Spec_P(B) / Spec(B)) modulo inner permutations is nontrivial in V[G_Cohen] but trivial in Jensen's L — a *fingerprint* of CH.

**Derivation sketch**:
1. Start from `s_stone_representation_theorem` via `s_ultrafilter_spectrum_Spec_B`.
2. Apply `t_force_independence` with P. Re‑use the move from `s_ch_independent_of_zfc` that reindexes ZFC‑models by P‑generic filters.
3. In V[G], every P‑generic G yields a Boolean hom B → **2** (truth evaluation); package as a new point of Spec_P(B).
4. Apply A2's representable formulation: Spec_P(B) = Hom(B, **2**_P).
5. Specialise `t_compactness_argument` to V[G]: gives compact‑Hausdorff topology; the argument transfers because the relevant language is absolute.
6. Apply `t_duality` within V[G] to obtain relative Stone equivalence BoolAlg^{V[G],op} ≃ StoneSp^{V[G]}.
7. The canonical V → V[G] induces η_P : Spec^V → Spec_P — the forcing fingerprint of B.
8. For atomless free B on ω generators, check η_P in L and in V[Cohen‑generic]; the conjecture predicts different kernels.

**What's inherited vs. added**:
- Inherited: Spec as representable functor (A2); forcing applied to ZFC (graph's `s_ch_independent_of_zfc`); Stone duality.
- Newly added: definition of Spec_P(B), η_P, fingerprint conjecture.

**Novelty assessment**: LIKELY‑KNOWN‑UNDER‑OTHER‑NAME. Forcing‑relativised Boolean‑valued models are Scott, Solovay, Vopěnka, Bukovský (1960s–70s); the Stone dual of a complete Boolean algebra is the ultrafilter space, close to Boolean ultrapowers. Balcar–Simon + Rudin (1956) + Shelah–Veličković (1989) established the ω* fingerprint: under CH, Aut(ω*) has size 2^{2^ℵ_0}; under PFA, only trivial automorphisms. So the fingerprint is *known* for ω*; my contribution is only to wrap it in representable‑functor language and parametrise by general P.

Grade: LIKELY‑KNOWN‑UNDER‑OTHER‑NAME for the core; SPECULATIVE for the claim that Spec_P is functorial in P with a characterisable kernel beyond the ω* case.

**Failure modes**:
1. **Proper class forcings** — Spec_P may not be a set; restrict to set forcings.
2. **Distributive forcings** — (ω₁, ∞)‑distributive P adds no new reals; η_P is identity on countable B. Test: Lévy collapse.
3. **Fingerprint scope** — Shelah's absoluteness work suggests Aut(Spec_P(B)) is *always* nontrivial after a Cohen real, so the conjecture must be stated "modulo inner permutations".

**Proof‑integrity risk**: MEDIUM. Representable part is safe; fingerprint is an honest conjecture requiring PFA / iterated forcing beyond the graph's scope.

---

### Candidate A4 — Compactness Closure for Cyclic Quadrilaterals (Poncelet n = 4)

**Derivation chain**: `s_cyclic_quadrilateral` --[`t_compactness_argument`]--> `s_limit_cyclic_quadrilateral` (new) --[`t_exhaustion_squeeze`]--> `T_A4`.

Recon cross‑cluster #1. `t_compactness_argument` has never been applied to `s_cyclic_quadrilateral`.

**Statement (plain)**: Consider all cyclic quadrilaterals inscribed in one fixed circle and tangent to another fixed inner circle. The set is compact; a limiting argument gives a closure theorem — if *one* such quadrilateral exists, then *every* starting vertex on the outer circle can be completed to one. This is Poncelet's closure theorem for n = 4 via compactness on `s_cyclic_quadrilateral`.

**Statement (formal)**: Let C be a circle of radius R, D a circle of radius r ≤ R, centre distance d satisfying the Cayley n = 4 condition.
- **Inherited**: for any cyclic quadrilateral inscribed in C, the inscribed‑angle theorem holds.
- **Newly claimed**: "continue one side tangent to D, move to next vertex on C" is a continuous self‑map φ : C → C; by `t_compactness_argument` on C and `t_exhaustion_squeeze` on {φ^k(x)}, φ has period 4 for every starting point or for none. "Closure for one" ⇒ "closure for all".
- **Sharpening**: the Cayley criterion is necessary and sufficient. Necessity needs elliptic‑curve translation structure (Griffiths–Harris 1977); the graph supplies only sufficiency via compactness.

**Derivation sketch**:
1. Start from `s_cyclic_quadrilateral` with vertices on C.
2. Apply `t_symmetry_reduction` (already used via `s_ptolemys_theorem`): parametrise vertices by angle θ ∈ ℝ/2πℤ.
3. Define φ : C → C by "at θ, draw tangent to D, intersect C at next vertex". φ is continuous (tangent‑intersection is smooth).
4. Apply `t_compactness_argument`: the set I = {θ : φ^4(θ) = θ} is closed. Either I = C or I ≠ C.
5. External fact: Cayley condition ⇒ I ≠ ∅ (Cayley 1853). Not in graph.
6. External fact: φ has elliptic‑curve translation structure (Griffiths–Harris 1977) ⇒ φ is either a rational rotation of exact order 4 (I = C) or irrational (I = ∅). Not in graph.
7. Combine with `t_exhaustion_squeeze` to conclude I = C.
8. Closure theorem follows.

**What's inherited vs. added**:
- Inherited: `s_cyclic_quadrilateral`, inscribed‑angle theorem, Ptolemy, `t_compactness_argument`, `t_exhaustion_squeeze`.
- Newly added: identification of φ as continuous self‑map of C; dichotomy via compactness + squeeze. Step 6 (elliptic structure) is flagged external.

**Novelty assessment**: COROLLARY‑OF‑KNOWN. Poncelet (1822). Compactness route is standard (Bos–Kers–Oort–Raven 1987, *Poncelet's Closure Theorem*, Enseignement Math.). The graph didn't contain it; wiring is worthwhile but content is classical.

**Failure modes**:
1. **Cayley condition fails** — generic circle positions give I = ∅. Edge test: concentric circles with radius ratio not tan²(π/8).
2. **Degenerate quadrilaterals** — three collinear vertices make φ undefined; the compactness argument must exclude a measure‑zero set.
3. **Higher n** — same proof structure works, Cayley minor changes; verify n = 3 and n = 5.

**Proof‑integrity risk**: MEDIUM. Step 6 is a genuine black box requiring elliptic curves.

---

### Candidate A5 — Cohomological Obstruction to Invariant Subspaces (sheaf formulation)

**Derivation chain**: `s_invariant_subspace_decomposition` --[`t_obstruction_class`]--> `s_invariant_subspace_cohomological_obstruction` (new) --[`t_duality`]--> `T_A5` (conditional).

Recon cross‑cluster #6. `t_obstruction_class` has 25 uses but has never touched `s_invariant_subspace_decomposition`.

**Statement (plain)**: A bounded operator T on a separable Hilbert space has a nontrivial closed invariant subspace iff a certain cohomology class [T] in a sheaf on σ(T) vanishes. If the class is nonzero, no subspace exists; if zero, the construction is unobstructed. Whether the class always vanishes on Hilbert is the Invariant Subspace Problem and remains open.

**Statement (formal)**: Let H be separable complex Hilbert, T ∈ B(H), σ(T) the spectrum. Build sheaf ℱ_T on σ(T) with stalk at λ equal to H / (T − λ)H̄.
- **Inherited**: Schur‑type results at group‑algebra level (`s_schur_lemma`, `s_artin_wedderburn_theorem`), not yet B(H).
- **Newly claimed**: ω_T := [ℱ_T] ∈ H^1(σ(T), Aut(ℱ_T)) measures failure of local triviality.
  (a) ω_T = 0 ⇒ T has a nontrivial closed invariant subspace (image of a global section of ℱ_T on some closed subset).
  (b) T compact ⇒ σ(T) countable with 0 accumulation ⇒ H^1 = 0 ⇒ ω_T = 0 ⇒ recovers Aronszajn–Smith (1954).
- **Conjectural**: for every bounded T on separable H, ω_T = 0. Restatement of ISP on Hilbert.
- **Speculative but verified in cases**: ω_T = 0 for polynomially compact T, hyponormal T with σ(T) totally disconnected, subnormal T (Brown–Chevreau–Pearcy 1988, Scott Brown 1978) — the candidate reformulates these as "ω_T vanishes".

**Derivation sketch**:
1. Start from `s_invariant_subspace_decomposition` (originally from `t_frequency_decomposition` in Birkhoff chain).
2. Apply `t_obstruction_class` targeting existence of nontrivial closed invariant subspace.
3. Sheaf construction: for normal T, use `s_spectral_theorem_self_adjoint` to build ℱ_T from the spectral measure P_T. For non‑normal T, use Apostol's decomposition (1968).
4. External fact: existence of Apostol's decomposition. Not in graph.
5. Apply `t_duality`: H^1(σ(T), Aut(ℱ_T)) measures twisting.
6. Compact T: σ(T) countable ⇒ H^1 = 0 ⇒ ω_T = 0 ⇒ subspace exists (Aronszajn–Smith).
7. T with disconnected σ(T): clopen partition gives nontrivial spectral projection (Riesz–Dunford calculus); subspace exists.
8. Quasinilpotent (σ(T) = {0}): H^1 is trivially 0 but the conclusion is empty — this is the hard case where the reformulation gives no new information.

**What's inherited vs. added**:
- Inherited: `s_invariant_subspace_decomposition`, `s_spectral_theorem_self_adjoint`, `t_obstruction_class`, `t_duality`, `s_schur_lemma`.
- Newly added: sheaf ℱ_T, class ω_T, ISP restated as "ω_T = 0 always on Hilbert".

**Novelty assessment**: LIKELY‑KNOWN‑UNDER‑OTHER‑NAME. Sheaf‑theoretic approaches to operator theory are Eschmeier–Putinar, *Spectral Decompositions and Analytic Sheaves* (1996), and Atzmon 1995. The obstruction‑class wrapping is natural once the sheaf is named; it almost certainly appears in Eschmeier–Putinar. Grade: LIKELY‑KNOWN‑UNDER‑OTHER‑NAME. Wiring value but no new theorem.

**Failure modes**:
1. **Quasinilpotent case** — σ(T) = {0} ⇒ H^1 = 0 trivially but no subspace is produced. This is exactly where Enflo–Read's Banach counterexamples live (Read 1984). Test Volterra operator.
2. **Non‑normal T** — spectral measure may not exist; Apostol's construction may give a *different* sheaf whose H^1 is nonzero for unrelated reasons.
3. **Banach vs. Hilbert** — the obstruction formulation makes sense on Banach, where counterexamples exist. The ω_T = 0 conjecture is only credible on Hilbert.

**Proof‑integrity risk**: MEDIUM‑HIGH. Sheaf construction is delicate; obstruction wrapping is cosmetic without new input; quasinilpotent case is the actually‑open case of ISP.

---

### Candidate A6 — Dyadic Martingale Structure for Archimedes' Polygon Sequence

**Derivation chain**: `s_inscribed_circumscribed_96_gons` --[`t_structural_isomorphism`]--> `s_dyadic_filtration_on_circle` (new) --[`t_axiomatize_from_instances`]--> `T_A6`.

Recon cross‑cluster #8. `t_structural_isomorphism` has 30 uses but none on `s_inscribed_circumscribed_96_gons`.

**Statement (plain)**: Archimedes' doubling procedure (3 → 6 → 12 → 24 → 48 → 96 regular polygons) generates inscribed and circumscribed polygons whose lengths converge to 2πR. Re‑read as measure theory: doubling is a dyadic filtration on the circle, and the two perimeter sequences are a sub‑martingale and super‑martingale with respect to it. Archimedes' squeeze is Doob's martingale convergence specialised here.

**Statement (formal)**: Let C be the unit circle, μ Haar measure. Let 𝒫_n be the σ‑algebra generated by the 3·2^n‑regular polygon vertices. Let L_n^{in}, L_n^{out} be inscribed/circumscribed 3·2^n‑gon perimeters as random variables on C.
- **Inherited**: L_n^{in} ↑ 2π and L_n^{out} ↓ 2π (from `s_area_of_circle`).
- **Newly claimed**: (L_n^{in}) is a sub‑martingale, (L_n^{out}) a super‑martingale, under (𝒫_n); both converge a.s. and in L¹ to 2π. The half‑angle identity sin(θ/2) = √((1 − cos θ)/2) that Archimedes uses is exactly the conditional‑expectation formula for this filtration.
- **Corollary**: 2π − L_n^{in} ~ π³/(9·2^{2n}) as n → ∞ — Archimedes' known error bound, now a martingale convergence rate.

**Derivation sketch**:
1. Start from `s_inscribed_circumscribed_96_gons` (used only by `t_exhaustion_squeeze` in `s_area_of_circle`).
2. Apply `t_structural_isomorphism` between "lattice of 3·2^n‑inscribed polygons" and "dyadic filtration on C": each 3·2^n‑gon vertex is the arc midpoint of a 3·2^{n+1}‑gon arc.
3. `t_compactness_argument` on C: (𝒫_n) increasing, completes to the Borel σ‑algebra.
4. External fact: Doob martingale convergence (1953). I have not confirmed it lives in the graph under this exact name; flag.
5. Apply `t_axiomatize_from_instances`: for each tail functional (perimeter, area, inscribed radius), the bisection gives a sub/super‑martingale.
6. Re‑prove Archimedes' squeeze as Doob L¹ convergence.
7. Rate O(2^{−2n}) from sin(θ/2)² ≈ θ²/4.

**What's inherited vs. added**:
- Inherited: `s_inscribed_circumscribed_96_gons`, `t_exhaustion_squeeze`, `s_area_of_circle`.
- Newly added: identification of doubling as dyadic filtration, martingale reading, rate as convergence rate.

**Novelty assessment**: COROLLARY‑OF‑KNOWN. Dyadic martingales are standard (Bass, *Probabilistic Techniques in Analysis*; Stroock). Re‑reading Archimedes this way is pedagogically nice but not a new theorem. Wiring an ancient geometry node to modern probability is the only novelty.

**Failure modes**:
1. **Non‑regular refinements** — the martingale property uses *bisection* specifically. Trisection may fail.
2. **Non‑rectifiable curves** — fractal boundary diverges; rectifiability is used crucially. Test: replace C by a Koch snowflake.
3. **Discrete circle** — on ℤ/Nℤ for prime N, the dyadic filtration doesn't refine to an atomic σ‑algebra; no limit.

**Proof‑integrity risk**: LOW. Martingale convergence is robust; identification with conditional expectation is mechanical.

---

### Candidate A7 — Character‑Decomposition of S₅ Orbits on Splitting Fields

**Derivation chain**: `s_galois_group_S5` --[`t_character_decomposition_count`]--> `s_S5_character_data_on_roots` (new) --[`t_obstruction_class`]--> `T_A7`.

Recon edge‑state push #7 (variant). `s_galois_group_S5` has only `t_obstruction_class` applied; adding `t_character_decomposition_count` opens a different route, in parallel to its existing use on `s_galois_group` for `s_chebotarev_density_theorem`.

**Statement (plain)**: When Gal(splitting field / ℚ) is the full S₅, the roots of the quintic form an orbit transforming as the standard S₅ representation. The character table of S₅ gives bookkeeping for any S₅‑invariant polynomial in the roots. The unsolvability of the generic quintic becomes: the standard 4‑dim representation is not induced from a 1‑dim representation of any solvable subgroup — a pure character‑theoretic obstruction, parallel to but distinct from the `t_obstruction_class` argument already in the graph.

**Statement (formal)**:
- **Inherited** (graph, `s_abel_ruffini`): Gal(L/ℚ) = S₅ generically; A₅ is simple non‑abelian; no solvable tower exists.
- **Newly claimed**: if χ = standard 4‑dim character of S₅ (χ(g) = #fixed(g) − 1), then χ is irreducible and does *not* factor through any solvable quotient of any subgroup of S₅. For every chain S₅ ⊃ H_1 ⊃ ... ⊃ {e} with each H_{i+1} normal in H_i, ⟨Ind_{H_k}^{S₅} 1, χ⟩ ≠ 0 at some k only if some H_i contains A₅ (non‑abelian simple).
- **Algorithmic corollary**: ⟨χ, χ⟩_{S₅} = 1 plus Frobenius reciprocity on subgroups gives, for a degree‑5 p(x) ∈ ℚ[x], an effective algorithm deciding Gal(p) = S₅ in time polynomial in height of p, by tabulating factorisation types of p mod ℓ for ℓ up to O((log disc p)²) and comparing to Chebotarev predictions.

**Derivation sketch**:
1. Start from `s_galois_group_S5`.
2. Apply `t_character_decomposition_count` (already wired to `s_finite_group` in Burnside, Pólya, Feit–Thompson, and to `s_galois_group` in `s_chebotarev_density_theorem`).
3. Enumerate S₅'s 7 conjugacy classes: {e}, (12), (12)(34), (123), (123)(45), (1234), (12345). Seven irreducibles: trivial, sign, standard (4), standard⊗sign (4), adjoint (5), adjoint⊗sign (5), 6‑dim. Character table is classical.
4. Compute ⟨1_H↑^{S₅}, χ⟩ for all subgroup classes and each irrep. For χ = standard 4‑dim: inner product vanishes unless H acts transitively on 5 points ⇒ H ⊇ 5‑cycle ⇒ H ⊇ A₅.
5. Apply `t_obstruction_class`: if Gal(p) = S₅, no solvable tower supports the standard rep ⇒ Abel–Ruffini.
6. Invoke `s_chebotarev_density_theorem`: Frobenius at unramified primes equidistributes.
7. Algorithm: for p ∈ ℚ[x] of deg 5, compute factorisation types mod ℓ for small ℓ; tabulate Frobenius classes; compare Chebotarev prediction for the five transitive subgroups of S₅ (S₅, A₅, F_{20}, D_5, ℤ/5).
8. Output: Gal(p).

**What's inherited vs. added**:
- Inherited: `s_galois_group_S5`, `t_obstruction_class`, `t_character_decomposition_count`, `s_chebotarev_density_theorem`.
- Newly added: explicit pairing between standard 4‑dim character and the solvable‑chain obstruction; algorithmic consequence via Frobenius tabulation.

**Novelty assessment**: LIKELY‑KNOWN‑UNDER‑OTHER‑NAME. Character‑theoretic non‑solvability is Frobenius 1890s. Effective Galois‑group computation via resolvents + factorisation types is Stauduhar (1973), implemented in PARI/GP, Magma, SageMath. Fully classical content. The contribution is wiring `t_character_decomposition_count` into the Abel–Ruffini chain, which the recon flagged as missing.

**Failure modes**:
1. **Gal(p) = A₅** (non‑solvable but smaller than S₅) — obstruction still holds; character decomposition differs; verify.
2. **Solvable quintics** — e.g., x⁵ − 2 has Gal = F_{20}; verify ⟨χ, Ind 1⟩ is consistent with F_{20}.
3. **Reducible quintics** — proper subgroup; need early factorisation check.

**Proof‑integrity risk**: LOW. Textbook components; only risk is character‑table correctness and identifying the five transitive subgroups of S₅.

---

## Summary and self‑assessment

| # | Candidate | Grade | Risk |
|---|-----------|-------|------|
| A1 | Grothendieck–Galois via colimit lift | COROLLARY‑OF‑KNOWN | LOW |
| A2 | Representable Stone duality | COROLLARY‑OF‑KNOWN | LOW |
| A3 | Forcing‑parametrised Stone duality | LIKELY‑KNOWN (core) / SPECULATIVE (fingerprint) | MEDIUM |
| A4 | Poncelet n = 4 via compactness | COROLLARY‑OF‑KNOWN | MEDIUM |
| A5 | Sheaf obstruction to invariant subspaces | LIKELY‑KNOWN‑UNDER‑OTHER‑NAME | MEDIUM‑HIGH |
| A6 | Dyadic martingale for Archimedes 96‑gons | COROLLARY‑OF‑KNOWN | LOW |
| A7 | S₅ character decomposition on roots | LIKELY‑KNOWN‑UNDER‑OTHER‑NAME | LOW |

No candidate here is graded PLAUSIBLY‑NEW in the strong sense. This is deliberate: each wiring exists somewhere in the literature of the last century. Value is in making the graph's technique × state grid denser, with precise attribution to Grothendieck/SGA1, Johnstone, Balcar–Simon / Shelah, Poncelet / Griffiths–Harris, Eschmeier–Putinar, Doob / Bass, and Frobenius / Stauduhar respectively.

The closest thing to a new conjecture is A3's fingerprint corollary — and there I have explicitly flagged that the substance of the conjecture for ω* is Balcar–Simon–Rudin–Shelah already, and my statement is a reformulation in representable‑functor language. A truly novel result would require probing beyond the graph's horizon; the recon's portfolio is (correctly) structured to harvest near‑misses rather than far‑shots.

**External facts used that are not in the graph** (flagged per candidate):
- Krull topology on absolute Galois group (A1).
- Elliptic‑curve translation structure of the Poncelet map φ (A4).
- Apostol's decomposition for non‑normal operators (A5).
- Doob martingale convergence theorem (A6) — verify against graph.
- S₅ character table and Stauduhar's algorithm (A7).

**Recommendation for the problem‑solver**: start with A2 and A6 (lowest risk, highest pedagogical clarity); then A1 and A7 (classical but needing external table/topology); then A4 (needs external elliptic structure); then A5 (verify against Eschmeier–Putinar); lastly A3 (the speculative fingerprint). Any truly new result is most likely to be in A3's fingerprint or A5's non‑normal cohomology, and is most likely reinvention rather than discovery.
