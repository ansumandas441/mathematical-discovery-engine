# Future Works

Forward-looking agenda: gaps and extensions surfaced during the knowledge-graph round (Ch. 11) that were deliberately deferred because they require changes beyond what the current schema supports. Each item is a candidate for a future round.

Source: philosopher's review (`knowledge_graph_workspace/philosopher_review.md` §5) plus one schema-level item from §6.

---

## 1. Conjecture ↔ negation dynamics

**Gap.** The current graph represents theorems as terminal state nodes with `kind: theorem`. It has no way to represent the *life cycle* of a mathematical claim: `conjectured → refined → proved` or `conjectured → refuted`.

**Concrete example it fails to capture.** Gauss (1793) conjectured π(x) ∼ x/ln x from a log-table. Legendre (1798) refined it to x / (ln x − B). Chebyshev (1850) proved partial bounds. Riemann (1859) reframed via ζ zeros. Hadamard and de la Vallée Poussin (1896) proved the full theorem. Today's graph flattens this to a single chain and labels the refinement as `t_verify_on_special_cases` or `t_conjecture_refinement`. The status transitions are invisible.

**Schema change required.**
- Add a `status` field to state nodes of `kind: theorem`: `conjectured | refined | partially_proved | proved | refuted`.
- Add a new edge kind: **lifecycle edges** that connect the same underlying claim across status transitions, distinct from derivation edges.
- Add a new node attribute `claim_id` so the multiple status-variants of one claim (Gauss-version, Legendre-version, Riemann-version, Hadamard-version of PNT) share identity.

**Estimated scope.** ~150 theorem nodes to revisit and annotate; maybe ~40 that have substantive lifecycle. Schema extension is the main work. A mini-round with one agent could do it.

---

## 2. Counterexample-first exploration

**Gap.** The graph treats counterexamples as side outputs of `t_verify_on_special_cases`. But for several landmark results the counterexample **is** the theorem.

**Concrete examples it fails to capture cleanly.**
- Milnor (1956): exotic 7-spheres — the theorem *is* "there exist smooth structures on S⁷ not diffeomorphic to the standard one."
- Hilbert's 16th (topology of real algebraic curves): progress has largely come through Viro's patchworking, which *builds* curves with specified topology.
- Julia and Fatou sets: discovered by explicitly constructing iterated-rational-map orbits.
- Kakeya set: Besicovitch's construction of a set of measure zero containing a unit line segment in every direction.

**Schema change required.**
- Add `t_construct_counterexample` as a new technique in Cluster 1 (Experimental), sibling to `t_spot_pattern_in_table` and `t_verify_on_special_cases`.
- Distinguish from `t_auxiliary_construction` (which builds a helper object inside a proof) — `t_construct_counterexample` produces a terminal state.
- Consider whether Cluster 1 should be renamed from "Experimental & numerical discovery" to include explicit construction, or if this warrants a new Cluster 13 "Constructive exploration".

**Estimated scope.** ~10–15 theorems to reclassify; single new technique with ~5 documented uses. Small round.

---

## 3. Iterative refinement of proof (Lakatos monster-barring)

**Gap.** The graph is a **DAG**. Every theorem is a linear chain from axioms to terminal state. This leaves out the back-and-forth that Lakatos documents in *Proofs and Refutations* (1963): proof → counterexample → monster-barring / exception-tweaking → refined definition → new proof → …

**Concrete example it fails to capture.** The Euler polyhedron formula V − E + F = 2. The first proof (Cauchy, 1813) assumed convex polyhedra. Lhuilier (1812) found counterexamples (polyhedra with tunnels). Definitions of "polyhedron" were patched. Then Poincaré (1895) generalized the whole thing to simplicial complexes of arbitrary dimension, at which point V − E + F was recognized as the Euler characteristic χ. The graph records only the end-state.

**Schema change required.** Substantial — moves the graph from DAG to general directed graph.
- Allow **non-terminal states to loop back** and modify earlier edges or definitions.
- Add an edge kind `t_refine_definition` that takes (current_definition, counterexample) and produces a new definition.
- Add a `generation` field to state nodes so a "patched" state is distinguishable from the original.
- Consider a companion visualization mode that shows the history vs. a snapshot mode that shows only the final DAG.

**Estimated scope.** The most ambitious item on this list. Schema rewrite plus ~8–12 classic examples (Euler's formula, Lakatos's own dialogues, the definition of "continuous function" in 19c analysis, the definition of "curve" at Cantor / Peano). Would probably be its own round.

---

## 4. Translation as its own move

**Gap.** Some landmark moves are not proofs but *reformulations*: they translate a question into a new language where it becomes either tractable or already-solved. The graph currently folds these into `t_structural_isomorphism` or `t_analysis_algebra_topology_bridge`.

**Concrete examples it fails to distinguish.**
- Taniyama–Shimura–Weil: "every elliptic curve over ℚ is modular." Before modularity is *proved*, it is first *stated* — and stating it requires recognizing that elliptic curves and modular forms are two faces of the same object.
- Langlands reciprocity: reformulates Galois representations as automorphic representations.
- Grothendieck's functor-of-points: reformulates "a scheme is a locally ringed space" as "a scheme is a representable functor on rings."
- Category-theoretic foundations: reformulates set-theoretic statements in arrow-and-object language.

These are *meta-moves*: they do not prove new theorems, they make existing questions reformulable. Within the current graph they end up tagged with structural-isomorphism or some bridge, which misses the point — the move is a change of ambient language, not the transport of one specific structure.

**Schema change required.**
- Add `t_reformulate_in_new_category` (or similar name) as a new technique, probably Cluster 12 (Homological & Categorical).
- Parameters on the edge: `{source_category, target_category, equivalence_kind}`.
- Consider a `kind: claim_reformulation` for state nodes that are the *reformulated question*, to distinguish from regular intermediate states.
- Decide the relationship to the existing `t_structural_isomorphism` — is this a specialization, a sibling, or a parent?

**Estimated scope.** One new technique, ~10 documented uses across Langlands, Grothendieck, category theory, moduli problems. Small–medium round.

---

## 5. Failed attempts

**Gap.** The graph records successful derivations only. A richer "discovery graph" would include failed edges — attempts that turned out not to work, and why.

**Concrete examples it fails to capture.**
- Kummer's ideal numbers and regular primes (1840s–1850s) — a sustained attempt at FLT that succeeded only for regular primes, motivated class field theory, and ultimately was superseded by modularity 150 years later.
- Hilbert's program (1920s) — attempt to prove the consistency of arithmetic by finitary means; refuted by Gödel's second incompleteness theorem.
- Ramanujan's mock theta conjectures — many of his unproven claims; some refuted (a few of Ramanujan's series identities had minor errors), some still open, some proved decades later by Zwegers et al.
- Hilbert's 10th problem — attempts to find a decision procedure for Diophantine equations, conclusively refuted by Matiyasevich (1970).
- Proposed quintic radical formulas in the 18th century — various attempts superseded by Abel–Ruffini.

**Schema change required.**
- Add `status: refuted | superseded | abandoned | open_partial` to edges and/or states.
- Add a `refuted_by` cross-reference so a failed attempt points to the result that killed it (Gödel ⇾ Hilbert's program; Matiyasevich ⇾ Hilbert's 10th).
- Consider whether "failed attempts" deserve their own visualization layer, optionally hidden in a clean view but visible when learning history.

**Estimated scope.** ~15–25 documented failed/superseded attempts across the corpus. New schema field; new edge annotations. Medium round.

---

## 6. Problem identity — canonical encoding of a claim regardless of phrasing

**Gap.** A node's identity is currently its surface text. The same problem stated in different words, different notation, a different order, or a different language produces *different* nodes — so the graph cannot guarantee that "Solve 2x = 4 for x" and "Find x if 2x = 4" are one node, nor that a translation of a theorem reuses the existing node instead of creating a duplicate. Item 1's `claim_id` asserts that lifecycle-variants share identity but provides no *mechanism* to compute that identity from an arbitrary input. This blocks reliable dedup on ingest (the iter-2/iter-3 web-sourced rounds rely on text matching) and blocks robust query-time lookup.

**Concrete example it fails to capture.** During an integration run, the Prime Number Theorem arrives once as "π(x) ∼ x/ln x", once as "the number of primes below x is asymptotic to x over the natural log of x", and once from a non-English source. Today these risk landing as three nodes (or being silently dropped by a brittle string match). We want any of them to resolve to the *same* PNT node with high recall and near-zero false merges.

**Approach — a layered identity cascade, strict→flexible** (no single method is both reliable and flexible; precision and recall pull apart, so layer them):
1. **Canonical fingerprint** (exact, zero false positives). Normalize before hashing: lowercase, strip whitespace, normalize math notation, rename bound variables to canonical names (x, y, …), sort commutative terms, evaluate constants → SHA-256. Catches re-encounters and notational variants. (Computing a canonical form of structured math is equivalent to graph canonical form.)
2. **Embedding ANN lookup** (flexible recall, cross-lingual). Encode each claim with a *multilingual* sentence encoder (e.g. LaBSE) into a vector; retrieve top-k nearest existing nodes by cosine similarity. Handles rewording and translation — different language lands at nearly the same vector. This is the Quora-question-pairs / semantic-textual-similarity problem.
3. **Verification gate** (precision, math-specific). For candidates above threshold, confirm with a structural/symbolic check, or — strongest — autoformalize to Lean and test **bidirectional equivalence** (A provable from B and B from A). This kills the false merges that pure embeddings create before two claims collapse to one node.

**Schema change required.**
- Add to state nodes of `kind: theorem`/`claim`: `canonical_fingerprint` (hash string), `embedding` (vector ref / external index id), and `aliases` (list of observed surface forms + language tags). This is the CESI pattern — many surface forms, one canonical node.
- Optional `formal_statement` field (Lean) for nodes where equivalence has been verified, reused by the verification gate.
- Make `claim_id` from item 1 *derived* from `canonical_fingerprint` rather than assigned by hand, so lifecycle-variants and phrasing-variants share one identity mechanism.
- Ingest pipeline change (not just schema): the cascade runs on every incoming node before it is added.

**Estimated scope.** Schema fields are small; the work is the ingest cascade and standing up a vector index. Layers 1–2 are a medium round and would immediately de-duplicate the existing graph (good ROI given the multi-source iter-2/iter-3 corpus). Layer 3 (Lean equivalence) is research-grade and optional — defer unless a round specifically needs provable identity. See [[Source.md]] / the research notes for the surveyed methods (entity resolution, STS, LSH/MinHash, autoformalization).

---

## Suggested ordering if tackling these

1. **Item 2 (counterexample-first)** — smallest, adds one technique, no schema rewrite. Good warm-up.
2. **Item 4 (translation as its own move)** — also small, one technique, low risk.
3. **Item 1 (conjecture ↔ negation dynamics)** — requires schema extension (`status` field, lifecycle edges, `claim_id`) but the pattern is clean and well-scoped.
4. **Item 5 (failed attempts)** — natural follow-on to item 1 (both are about non-trivial status handling). Reuses the `status` infrastructure.
5. **Item 3 (Lakatos monster-barring)** — most ambitious. Tackle after the schema has already absorbed status fields and lifecycle edges from items 1 and 5; otherwise the DAG→general-graph move is too much to combine with content work.

**Item 6 (problem identity)** is somewhat orthogonal and high-ROI: layers 1–2 can be done independently at any time and would clean up duplicates from the multi-source rounds. Best sequenced *before or alongside item 1*, since item 1's `claim_id` is meant to be derived from item 6's canonical fingerprint.

---

## Meta: what each item would actually produce

None of these change the ~100 theorems of chapters 01–06 or the 57 techniques of the toolbox. They change **how the graph is able to talk about** discovery:

- After item 1: the graph distinguishes "Gauss conjectured PNT" from "Hadamard proved PNT" as different lifecycle stages of one claim.
- After item 2: "Milnor exotic 7-sphere" is derived via `t_construct_counterexample`, not shoehorned into `t_verify_on_special_cases`.
- After item 3: Euler's formula has *two* entries — the 1813 proof for convex polyhedra AND the 1895 generalization with a "monster-barring" edge between them.
- After item 4: Taniyama–Shimura has a `t_reformulate_in_new_category` edge making explicit that the translation came before the proof.
- After item 5: Kummer's regular-primes attempt at FLT appears as a `status: superseded` subgraph, with an explicit `refuted_by` link to Wiles.

The graph grows in **expressive power** rather than in size. A reader who wants the clean picture can still read the proved-only DAG; a reader who wants the history of discovery sees the richer structure.
