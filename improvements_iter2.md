# Improvements · Iteration 2 — Graph Completion Plan

Follow-up to the Ch. 11 knowledge-graph round (commit `c7b5f99`). Objective: bring the graph to **full corpus coverage** — every theorem in chapters 01–07 represented as a terminal state node with a valid derivation chain back to at least one axiom, zero orphan nodes, and the philosopher's corrections applied consistently across the entire graph.

This is a scoped execution plan: concrete agent roles, phase ordering, quality gates, and effort estimates. It does **not** tackle the schema extensions in `future_works.md` — those are reserved for a separate iteration 3 so they don't destabilize the completion work.

---

## §1 Baseline (as of c7b5f99)

| Quantity | Value | Commentary |
|---|---|---|
| Total nodes | 352 | 94 axiom / 140 state / 53 technique / 65 theorem |
| Edges | 343 | top-level; subgraph-internal ≈ 95 |
| Subgraphs | 12 | compound-technique elaborations |
| Theorem derivation chains | 63 | from `mathematician_relationships.md` |
| Orphan nodes | 70 | 56 axioms + 14 techniques with no incident edges |
| Giant connected component | 282 nodes (80%) | 70 singletons form the rest |

**Corpus universe** (what "complete" means):

| Source | Theorems | Currently in graph | Missing |
|---|---|---|---|
| Chapters 01–06 deep dives (level-3 headings) | ~105 | ~65 | ~40 |
| Chapter 07 brief catalog (bulleted entries) | ~231 | 0 | ~231 |
| **Total** | **~336** | **65** | **~271** |

Chapter-by-chapter deep-dive counts: Ch1 = 15, Ch2 = 18, Ch3 = 17, Ch4 = 22, Ch5 = 18, Ch6 = 15.

---

## §2 Goal & non-goals

### Goal

After iteration 2:

1. Every deep-dive theorem from chapters 01–06 has a 3–6-step derivation chain in the graph.
2. Every brief-catalog theorem from chapter 07 has at least a minimal skeleton entry (`axioms → technique → theorem`, 1–2 steps).
3. Zero orphan state or axiom nodes. Every node has either incoming or outgoing edges (or both).
4. All 17 philosopher corrections from Ch. 11 §6 applied uniformly across the whole JSON, not just the landmark-path subset.
5. Every theorem's chain passes a typed-correctness check (technique input types match feeding states).
6. Viewer remains performant: ≤ 3-second initial render for the full graph at 600+ nodes.

### Non-goals

1. Implementing the five schema extensions from `future_works.md` (lifecycle, counterexample-first, Lakatos loops, translation, failed attempts). These are iteration 3.
2. Expanding beyond the existing corpus. If a theorem isn't already discussed in chapters 01–07, it stays out.
3. Proving new mathematics. This is a curation/integration round, not a discovery round (though the result enables better discovery probes).
4. Re-opening the 57-technique toolbox itself. Techniques are frozen at their current definitions; we only add *uses*.

---

## §3 Phased execution

Rounds 0 → 4 are sequential at the round level, but within each round agents run in parallel.

### Phase 0 — Clean baseline (Round 0)

**Before any new theorem is added**, bring the existing graph to a consistent state.

Work items:

1. **Apply Ch. 11 §6 corrections uniformly to JSON.** The landmark-path rewrites (auxiliary construction, reductio, projection-to-subspace, etc.) were described in prose. They need to be pushed through all 343 edges — rename the technique nodes they reference, update the `from`/`to` fields, and refresh the Mermaid diagrams in 11_knowledge_graph.md.
2. **Orphan audit.** Categorize the 70 orphans:
   - **Type A (fixable, state used implicitly):** axiom or state that a chain consumes but didn't record as an edge. Example: `s_polygon_area_formula` is used inside Archimedes' circle-quadrature chain but no edge records it.
   - **Type B (umbrella, routes via subgraph):** a composite technique whose action happens inside its subgraph. Example: `t_atiyah_singer_index_machinery`. These need an explicit "this node's top-level role is to host subgraph `sg_X`" flag.
   - **Type C (genuine bug):** a state the chain names but doesn't connect. Example: `s_projective_plane` (Desargues uses it but the edge was missed).
3. **Emit an orphan-fix edge list** (plain CSV or JSON-patch) and apply.
4. **Automated integrity checks:**
   - No two state nodes with the same `type_signature` unless declared aliases.
   - Every technique node has `cluster` set correctly.
   - Every edge's `parameter_binding` keys are declared on the parent technique's `parameters` list.
   - Every subgraph's `entry_points` and `exit_points` are actual node ids present in the subgraph.

**Agents:** single graph theorist (no mathematician needed — no new theorems), single philosopher for the automated-check spec.
**Output:** `round0_cleanup.md` + rewritten `knowledge_graph.json`.
**Gate:** orphan count = 0 OR all remaining orphans are Type-B with explicit `subgraph_host: true` flag.
**Est. tokens:** ~80 k.

### Phase A — Complete deep-dive theorems (Rounds 1–3)

Three parallel mathematician rounds, one per era-pair. Each round produces a `mathematician_relationships_rN.md` for the remaining deep-dives in its chapters.

| Round | Chapters | Theorems already in | To add | Mathematician agent |
|---|---|---|---|---|
| 1 | 01 + 02 | ~15 | ~18 | A |
| 2 | 03 + 04 | ~18 | ~21 | B |
| 3 | 05 + 06 | ~16 | ~17 | C |

Rounds 1–3 can run **in parallel** (no dependency) because each agent touches only its own chapters and writes its own file. Graph theorist integrates the three outputs together.

Work items per round:

1. Mathematician reads its two chapters plus `10_toolbox.md` plus the existing `mathematician_relationships.md` to avoid duplication.
2. Extracts one derivation chain per missing theorem, following the established schema (3–6 atomic steps, parameter bindings on edges, technique ids matching toolbox names).
3. Flags any step that doesn't match a toolbox entry with `⚠ not in toolbox: <proposed name>` — the graph theorist will decide whether to add the technique or re-route.
4. Produces a Part B inventory of any *new* recurring states introduced.

After all three mathematician outputs are in, a single graph theorist round (call it Round 3.5) does:

5. Merge the three outputs into the canonical JSON.
6. Deduplicate new state nodes against existing ones.
7. Update Mermaid diagrams in 11_knowledge_graph.md where the top-level view needs revision.
8. Check: every new theorem has ≥ 1 path to an axiom.

**Agents:** 3 × mathematician + 1 × graph theorist.
**Output:** `mathematician_relationships_r{1,2,3}.md` + updated JSON + updated 11_knowledge_graph.md.
**Gate:** all deep-dive theorems in chapters 01–06 present as theorem nodes with ≥ 1 chain.
**Est. tokens:** 3 × ~120 k (mathematicians) + ~100 k (graph theorist) = ~460 k.

### Phase B — Brief-catalog sweep (Round 4)

The 231 brief-catalog theorems (chapter 07) don't warrant full 3–6-step chains. They get **minimal skeleton entries**: 1–2 steps connecting an axiom through one or two techniques to the theorem.

Example skeleton:
```
Heron's formula (Ch. 7)
  s_triangle_with_sides_abc → t_compose_with_identity → s_heron_formula
```

Chapter 07 is already organized by area (number theory, geometry, algebra, analysis, etc.). Parallelize by **area**, roughly 8–12 sections. One mathematician per 2–3 sections → ~5 mathematician agents.

Work items per agent:

1. Read the assigned sections of `07_brief_catalog.md` (each bullet has a short description).
2. For each theorem, produce a minimal skeleton: 1 axiom + 1 technique + theorem. If the technique isn't obvious from the bullet, mark `⚠ technique inference needed`.
3. Favor **reuse of existing states and techniques** — the brief-catalog phase is where fan-in should explode. If a brief theorem introduces genuinely new material, flag it and consider whether it merits a full chain (i.e., demote to Phase A or accept as skeleton).

Graph theorist pass (Round 4.5):

4. Bulk-import the skeleton entries.
5. Detect new edges that lift existing techniques into higher-fan-in territory. The top 10 techniques' fan-in should roughly double.
6. Run the Phase 0 integrity checks again.

**Agents:** 5 × mathematician (parallel, by area) + 1 × graph theorist.
**Output:** `brief_catalog_skeletons.md` + updated JSON.
**Gate:** every bulleted theorem in chapter 07 represented as a theorem node with ≥ 1 incoming edge.
**Est. tokens:** 5 × ~80 k (mathematicians) + ~120 k (graph theorist) = ~520 k.

### Phase C — Cross-validation (Round 5)

A single philosopher round audits the completed graph.

Work items:

1. **Random spot-check** 25 new deep-dive chains against the original chapter prose. Each must be consistent with what the chapter says.
2. **Fan-in audit.** Every technique should now have fan-in ≥ 3 after brief-catalog expansion. Techniques still at fan-in < 3 either should be demoted to subgraph-only, merged with a near-neighbor, or explicitly flagged `single_use_landmark`.
3. **Typed-correctness sweep.** For every technique's incoming edges, verify that the feeding state's `type_signature` is compatible with the technique's input declaration. Flag mismatches.
4. **Semantic-coherence pass** on the ~50 newly-introduced state nodes (same methodology as the Ch. 11 review: coherent single idea? name specific enough? abstraction level consistent?).
5. **Derivation-path coverage.** Pick 15 "thread" theorems and verify each one has a clean path from axiom(s) to theorem, with every intermediate state accounted for.

**Agents:** 1 × philosopher.
**Output:** `philosopher_review_r2.md` + action list for graph theorist.
**Gate:** ≤ 5 unresolved flags (each with explicit orchestrator decision), 0 typed-correctness violations.
**Est. tokens:** ~150 k.

### Phase D — Viewer and docs update (Round 6)

With 600+ nodes, the viewer needs tuning.

Work items:

1. **Layout performance.** Physics solver settings tuned for ~600 nodes (increase `avoidOverlap`, reduce `gravitationalConstant`, cap stabilization iterations). Default the overview to show only the top ~100 by fan-in + all theorems, plus a "show full graph" toggle.
2. **Clustering in the view.** Render clusters as labeled groups (vis-network supports this via the `group` property we already set).
3. **New search features:**
   - Search by cluster.
   - Search by "theorems using technique T."
   - Path finder: click two nodes, highlight the shortest directed path.
4. **Updated prose sections** in `11_knowledge_graph.md`: refreshed statistics, updated Mermaid diagrams, updated "known gaps" reflecting what's no longer a gap.
5. **README update** with new counts and features.

**Agents:** no math agents needed; orchestrator-only.
**Output:** updated `graph_viewer.html`, updated `11_knowledge_graph.md`, updated `README.md`.
**Gate:** viewer renders full graph in < 3 seconds on a typical laptop, stays responsive during pan/zoom.
**Est. tokens:** ~60 k.

---

## §4 Team & parallelization

### Agent inventory for iteration 2

- **3 × mathematician (Phase A)** — one per chapter pair. Parallel.
- **5 × mathematician (Phase B)** — one per area cluster in ch. 07. Parallel.
- **2 × graph theorist** — one after Phase A (integrates 3 mathematician outputs), one after Phase B (bulk-imports skeletons). Sequential with each other.
- **1 × philosopher** — Phase C cross-validation.
- **1 × orchestrator** — Phase 0 + Phase D; also coordinates handoffs.

Total: 8 math-worker agents + 2 infra agents + 1 philosopher + 1 orchestrator = **12 distinct agent invocations**.

### Work dependencies

```
Round 0 (orchestrator + graph theorist cleanup)
   │
   └─▶ Rounds 1, 2, 3 (three mathematicians, parallel)
         │
         └─▶ Round 3.5 (graph theorist integration)
               │
               └─▶ Round 4 (five mathematicians, parallel)
                     │
                     └─▶ Round 4.5 (graph theorist bulk-import)
                           │
                           └─▶ Round 5 (philosopher audit)
                                 │
                                 └─▶ Round 6 (viewer & docs)
```

Critical path is 6 sequential rounds; wall time is dominated by graph-theorist integration passes. Rough estimate: **2–3 hours of active work** end-to-end if agents run near full utilization, **1 day** if run serially with review gates in between.

### Token budget

Summing the phase estimates: ~80 k + 460 k + 520 k + 150 k + 60 k = **~1.27 M tokens** across all agent invocations. Roughly comparable to the Ch. 11 round (~0.9 M) plus 40% for the brief-catalog bulk work.

---

## §5 Workspace layout

```
/Users/primetrce/Documents/maths/
├── knowledge_graph_workspace/           # existing (iter 1 artefacts)
│   ├── CHARTER.md
│   ├── SCHEMA.md
│   ├── mathematician_relationships.md
│   ├── graph_theorist_graph.md/.json
│   └── philosopher_review.md
├── knowledge_graph_workspace_iter2/     # NEW
│   ├── CHARTER_iter2.md                 # this plan, trimmed to actionable form
│   ├── round0_cleanup.md                # orphan audit + correction patches
│   ├── mathematician_relationships_r1.md   # ch. 01-02
│   ├── mathematician_relationships_r2.md   # ch. 03-04
│   ├── mathematician_relationships_r3.md   # ch. 05-06
│   ├── brief_catalog_skeletons_area_{1..5}.md
│   ├── graph_theorist_integration_A.md     # post-phase A
│   ├── graph_theorist_integration_B.md     # post-phase B
│   └── philosopher_review_r2.md
```

Iter-1 files stay in `knowledge_graph_workspace/` as frozen reference.

---

## §6 Quality gates

Each round has an explicit gate. If the gate fails, iterate that round before proceeding.

| Round | Gate | How to check |
|---|---|---|
| 0 | Orphan count = 0 (or all remaining Type-B with `subgraph_host: true`) | connectedness script on JSON |
| 1–3 | All deep-dive theorems present as theorem nodes | diff chapter-heading list vs. `{n : n.kind == "theorem"}` |
| 3.5 | Every new theorem has a path to an axiom | BFS from each theorem node |
| 4 | Every ch. 07 bullet represented as theorem node | diff catalog bullet list vs. theorem nodes |
| 4.5 | Top 10 techniques' fan-in roughly doubled | fan-in script pre/post |
| 5 | ≤ 5 unresolved philosopher flags, 0 typed-correctness violations | philosopher output |
| 6 | Viewer renders full graph in < 3 s | browser timing |

These gates are encoded as scripts in `knowledge_graph_workspace_iter2/checks/` — one python script per gate. Gates fail-loud: a gate's script exits non-zero and the round blocks.

---

## §7 Anticipated friction points

**(a) The brief-catalog "technique inference" problem.** Bullet entries often don't name the technique used — the mathematician has to infer it from context. Signal: many `⚠ technique inference needed` flags. Mitigation: establish a cheat-sheet at the start of Phase B ("if the bullet says 'counts', try `t_pigeonhole_collision` or `t_character_decomposition_count`; if it says 'bounds', try `t_exhaustion_squeeze` or `t_inequality_chain`...") and let the agent iterate with the cheat-sheet as a checklist.

**(b) Duplicate state-node proliferation.** Each of the 8 mathematicians will invent state-node ids independently. After 8 parallel runs, there will be many near-duplicates (`s_polynomial_ring` vs `s_polynomial_ring_over_Q` vs `s_univariate_polynomial_ring`). Mitigation: the graph-theorist integration passes use a fuzzy-match pre-filter on new state ids and flag any with `type_signature` cosine-similarity ≥ 0.8 to an existing node. The mathematician charter explicitly encourages reuse of existing ids listed in the shared canonical-state index.

**(c) Cluster imbalance after brief-catalog sweep.** Some clusters (combinatorics, computer-assisted) will grow disproportionately; others (self-reference) barely. This is real, not a bug — it reflects the shape of mathematics. But the viewer's default "show top techniques by cluster" needs to accommodate wildly different cluster sizes without one swamping others.

**(d) Subgraph proliferation.** As new theorems are added, some will use compound techniques whose subgraphs are currently only 4–8 nodes. Bigger fan-in justifies richer subgraphs. Separate question for Phase D: should some subgraphs be expanded? Probably yes for `sg_fourier` (deserves more dyadic / Littlewood–Paley detail after the CLT and ergodic-theorem chains come in).

**(e) Philosopher fatigue.** The Ch. 11 philosopher review was thorough at 65 theorems; at 336 theorems the cost of exhaustive review is 5×. Mitigation: Phase C philosopher focuses on *new* material and on invariants (typed-correctness, fan-in thresholds) rather than node-by-node commentary.

---

## §8 Decisions required before kickoff

1. **Bundle future_works item 1 (lifecycle status)?** If yes, add a `status` field to every theorem node now rather than in iter 3. Adds ~5% to total work but avoids a schema migration later. **Default: NO** — keep iter 2 strictly about completion.
2. **Bundle orphan auto-fix with integrity checks?** Some orphans need human judgment. **Default: YES for Type A and C (auto-fix), NO for Type B (surface for review).**
3. **Brief-catalog depth.** Minimum 1 input + 1 technique + theorem, or require 2+ techniques? **Default: 1 + 1 + 1 is acceptable; agents allowed to go deeper if obvious.**
4. **Provisional technique nodes.** Are brief-catalog agents allowed to propose new techniques, or must they reuse existing 57? **Default: reuse only; flag anything new to orchestrator for post-hoc decision.**
5. **Viewer redesign scope.** Keep current viewer and just tune it, or add new features (path finder, timeline view)? **Default: tune + add cluster-groups and path-finder only.**

None of these are blocking; orchestrator should lock defaults at kickoff and revisit only if a phase surfaces a clear reason.

---

## §9 Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Mathematician agents produce inconsistent node ids across parallel rounds | High | Medium | Shared canonical-state index built from iter-1 JSON, distributed with each mathematician prompt |
| Graph theorist integration takes longer than estimated due to dedup load | Medium | Low | Two integration rounds (A and B) rather than one single mega-integration |
| Philosopher surfaces schema-level concerns that invalidate earlier rounds | Medium | High | Restrict iter-2 philosopher scope to coherence/typed-correctness; explicit schema changes deferred to iter 3 |
| Viewer performance degrades unacceptably at 600+ nodes | Medium | Medium | Default view shows reduced subset; "full graph" is opt-in with warning |
| Token overrun beyond 1.5 M | Low | Low | Monitor after each round; if Phase B is running long, reduce brief-catalog to top-priority areas and defer lesser ones |
| Duplicate discovery: two agents independently derive the same theorem twice with different techniques | Medium | Low | Post-integration dedup on theorem node `name` field; keep whichever chain is more consistent with the chapter prose |

---

## §10 Success criteria (single-line summary)

Iteration 2 is complete when: **(a)** every theorem discussed in chapters 01–07 appears as a terminal state node with ≥ 1 derivation chain back to an axiom, **(b)** the full graph has zero orphan nodes, **(c)** philosopher review shows ≤ 5 unresolved coherence flags, and **(d)** the viewer renders the complete graph in under 3 seconds with usable filter UX.

At that point the graph goes from "curated sample of 63 theorems" to "authoritative cross-cutting index of ~336 theorems" — a coverage jump of ~5×. The infrastructure for iteration 3 (schema extensions from `future_works.md`) is then unblocked.
