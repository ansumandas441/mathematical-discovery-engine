# Knowledge Graph Schema

## Purpose

Turn the ~100 deep-dive theorems (chapters 01–06) and the 57 discovery techniques (10_toolbox.md) into a single **bipartite directed knowledge graph** where:

- **State nodes** = mathematical objects / intermediate results (a Hamiltonian, a matrix, a surface, a sheaf, a finite group, …).
- **Technique nodes** = processes that transform input states into output states. Think of them as typed functions.
- **Edges** are directed and connect exclusively `state → technique` (as an input) or `technique → state` (as an output). No state→state or technique→technique edges at the top level.

Theorems are **terminal state nodes** (marked `kind: theorem`). Axioms/definitions that start a derivation are **source state nodes** (marked `kind: axiom`).

## Node types

### 1. State node

```yaml
id: s_riemannian_manifold
kind: state            # state | theorem | axiom
name: Riemannian manifold (M, g)
type_signature: ManifoldWithMetric
description: A smooth manifold equipped with a positive-definite metric tensor g.
aliases: [riemannian surface, metric manifold]
```

- `kind: theorem` for terminal results (e.g., Gauss–Bonnet, FLT, Perelman).
- `kind: axiom` for starting points that are not themselves products of another technique (e.g., "ZFC", "the real numbers ℝ", "smooth manifold").
- `kind: state` for everything else (intermediate objects).

### 2. Technique node

```yaml
id: t_fourier_transform
kind: technique
name: Fourier transform
cluster: 04_approximation_and_limits         # references a toolbox cluster
function_signature: (L^2 function on ℝⁿ) → (L^2 function on frequency space)
parameters:                                   # captured when instantiated
  - dimension: n
  - domain: ℝⁿ | 𝕋ⁿ | finite group
  - variant: continuous | discrete | FFT
preconditions:
  - input is measurable and square-integrable
postconditions:
  - Plancherel isometry holds
  - convolution becomes pointwise multiplication
has_subgraph: true                             # elaborates to a sub-level graph
subgraph_ref: sg_fourier
toolbox_ref: 10_toolbox.md#4.3
```

- `has_subgraph: true` signals that the technique is itself composite; see §Subgraphs.
- `parameters` is the list of dials that distinguish concrete applications (e.g., "SVD along rows" vs "SVD along columns" use the same technique node with different parameters bound on the *edge*, not the node).

### 3. Edge (application)

```yaml
edge_id: e_0427
from: s_heat_equation_on_circle
to: t_fourier_transform
role: input                    # input | output
parameter_binding:
  dimension: 1
  domain: 𝕋¹ (circle)
  variant: continuous
used_in_theorem: s_fouriers_theorem_heat
```

or

```yaml
edge_id: e_0428
from: t_fourier_transform
to: s_frequency_decomposition
role: output
parameter_binding:
  dimension: 1
used_in_theorem: s_fouriers_theorem_heat
```

Every application of a technique in a specific theorem produces **(k + m) edges**: k input edges and m output edges, all tagged with the same `parameter_binding` and `used_in_theorem`. This is how we preserve "SVD along which axis" — the axis lives on the edge, not the technique node.

## Subgraphs (hierarchical elaboration)

A compound technique (Fourier, SVD, Galois correspondence, Ricci flow with surgery, Atiyah–Singer machinery, …) gets both:

1. A single top-level technique node (so theorems can cite it as an atomic arrow).
2. A subgraph that internally decomposes it into its own bipartite state/technique graph.

The subgraph reuses the same schema. Cross-references are allowed: a subgraph may reference a technique that also appears at the top level (e.g., the Fourier subgraph uses "orthogonal projection onto basis", which also appears in SVD's subgraph).

```yaml
subgraph_id: sg_fourier
belongs_to: t_fourier_transform
nodes: [s_..., t_..., ...]
edges: [e_..., ...]
entry_points: [s_l2_function]          # maps to t_fourier_transform's inputs
exit_points: [s_spectrum]              # maps to t_fourier_transform's outputs
```

## Deduplication rules (for the graph theorist)

1. **States are deduplicated by mathematical identity**, not name. "The Riemann zeta function" and "ζ(s)" are one node. Aliases live in the node record.
2. **Techniques are deduplicated by function signature + cluster**. Different parameter bindings do NOT create new technique nodes — they create new edges.
3. **Near-duplicates** (e.g., "integration by parts" vs "Stokes' theorem in 1D") stay separate at the top level if they have different preconditions/postconditions, but the subgraph can show their relationship.
4. **Fan-in / fan-out is desirable**: a technique reused across N theorems should show N incoming edge-bundles and N outgoing edge-bundles — that is the whole point of a knowledge graph.

## Parameter convention

Parameters that vary by application site (dimension, axis, field characteristic, base ring, domain shape) are recorded **on edges**, not on nodes. Parameters that are intrinsic to the technique (the variant "continuous Fourier" vs "discrete Fourier" where the underlying math genuinely differs) MAY warrant separate technique nodes connected by a parent–variant relationship — but default to one node with `variant` as an edge parameter unless the math is structurally different.

## Coherence rules (for the philosopher)

A proposed node/edge must pass all four:

1. **Typed correctness** — the input types of a technique match the types of the state nodes feeding it.
2. **Direction meaningfulness** — reversing the edge would be nonsense or require a different technique (SVD and its inverse reconstruction are different nodes).
3. **Reusability** — the technique node should describe something more general than a single theorem's step. If it is unique to one theorem, demote it to a subgraph-only node.
4. **Non-redundancy** — if another technique node captures the same process at the same abstraction level, merge them.

## Output formats

1. **Canonical YAML/JSON** for the full graph (nodes + edges). Easy to query, easy to extend.
2. **Mermaid diagrams** (flowchart LR / graph TD) for the top-level view and each subgraph.
3. **Prose derivation paths** for 20–30 landmark theorems, showing the chain `axiom → … → theorem` as it traverses the graph.
