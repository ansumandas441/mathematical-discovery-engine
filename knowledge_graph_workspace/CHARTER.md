# Charter — Knowledge Graph Team

## Team

| Role | Responsibility | Output file |
|---|---|---|
| **Mathematician** | Extract relationships from the existing corpus. For each representative theorem, list the sequence of (input states → technique → output states) steps that produced it. | `mathematician_relationships.md` |
| **Graph theorist** | Normalize the mathematician's relationships into a formal knowledge graph: deduplicate nodes, design subgraph hierarchy, produce Mermaid + JSON. | `graph_theorist_graph.md` + `graph_theorist_graph.json` |
| **Philosopher** | Review the resulting graph for semantic coherence. Challenge every node: does it actually represent a single coherent mathematical idea? Does reversing the edge break meaning? | `philosopher_review.md` |

All three read `SCHEMA.md` before starting.

## Working directory

`/Users/primetrce/Documents/maths/knowledge_graph_workspace/`

## Sources to draw from

- `10_toolbox.md` — authoritative list of 57 techniques across 12 clusters. Every technique node must trace back to a toolbox entry.
- `01_ancient.md` through `06_modern_contemporary.md` — narrative chapters. Each chapter is the source of truth for theorem content.
- `09_discovery_techniques.md` — prior prose taxonomy (useful but not authoritative; toolbox supersedes).

## Sequence

1. **Phase 1** — Mathematician works alone. Produces `mathematician_relationships.md`.
2. **Phase 2** — Graph theorist and philosopher work in parallel:
   - Graph theorist normalizes the mathematician's output into `graph_theorist_graph.md` (+ .json).
   - Philosopher reviews the mathematician's output for semantic soundness AND flags any ontological mismatches in the schema itself. Writes `philosopher_review.md`.
3. **Phase 3** — Orchestrator integrates all three into `/Users/primetrce/Documents/maths/11_knowledge_graph.md` and applies philosopher's corrections.

## Scope discipline

- **Representative coverage over exhaustive coverage.** Cover ~40–50 theorems in the main graph, elaborate ~10–15 techniques with subgraphs. The quick-reference table in `10_toolbox.md` already indexes all 57 techniques.
- **Reuse is the point.** If only one theorem uses a technique, consider whether it belongs at the top level at all or should be inside a subgraph.
- **Parameters on edges, not nodes.** Dimension, axis, field, base ring — these go on the edge. Create a new technique node only if the underlying math is structurally different.

## Success criteria (for orchestrator verification)

1. Every theorem in the graph has a path back to at least one axiom/definition node.
2. Every technique node in the top-level graph has fan-in ≥ 2 or fan-out ≥ 2 (or is explicitly flagged as "single-use landmark").
3. No duplicated state nodes (two nodes referring to the same mathematical object).
4. Every compound technique with `has_subgraph: true` has its subgraph actually written out.
5. The philosopher's coherence review surfaces no unresolved flags.

## Round 1 (this round)

File naming has no `_r1` suffix — this is the first and (hopefully) only round. If philosopher flags major incoherence, we iterate with `_r2` suffixes.
