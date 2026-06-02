# 13. Automated Theorem Discovery Workflow

## An LLM-orchestrated search tree over the knowledge graph

This document describes a concrete system architecture for **automated theorem discovery** using the knowledge graph (`knowledge_graph.json`) as the search space. The core idea: mathematical proof is path-finding through a finite directed graph, where **nodes are mathematical states** (axioms, intermediate results, theorems) and **edges are techniques** (the 62 operations cataloged in Ch. 10). An orchestrator LLM directs the search; worker LLMs attempt each technique application; a pruner eliminates impossible branches.

---

## 1. Architecture

```
                    ┌──────────────────────┐
                    │   ORCHESTRATOR LLM   │
                    │                      │
                    │  - Reads the problem  │
                    │  - Picks start nodes  │
                    │  - Selects techniques │
                    │  - Evaluates results  │
                    │  - Decides next path  │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┼─────────────┐
                 │             │             │
          ┌──────▼──────┐ ┌───▼────────┐ ┌──▼───────────┐
          │  WORKER A   │ │  WORKER B  │ │  WORKER C    │
          │             │ │            │ │              │
          │ Tries       │ │ Tries      │ │ Tries        │
          │ Technique 1 │ │ Technique 2│ │ Technique 3  │
          │ on state S  │ │ on state S │ │ on state S   │
          └──────┬──────┘ └───┬────────┘ └──┬───────────┘
                 │            │             │
                 ▼            ▼             ▼
          ┌────────────────────────────────────────┐
          │           RESULT COLLECTOR             │
          │                                        │
          │  Each worker returns:                  │
          │    - new_state: mathematical result    │
          │    - confidence: 0.0 - 1.0             │
          │    - reasoning: proof sketch           │
          │    - impossible: true/false             │
          └────────────────────┬───────────────────┘
                               │
                        ┌──────▼──────┐
                        │   PRUNER    │
                        │             │
                        │ Kills only  │
                        │ branches    │
                        │ that are    │
                        │ 100% dead   │
                        └──────┬──────┘
                               │
                        ┌──────▼──────┐
                        │ SEARCH TREE │
                        │  (updated)  │
                        └─────────────┘
```

### 1.1 The Orchestrator

A high-capability LLM (e.g., Claude Opus, GPT-5+) that:

1. **Parses the target problem** into the graph's vocabulary: identify which existing nodes (axioms, states, theorems) are the starting conditions, and what the goal state looks like.
2. **Queries the knowledge graph** for nearby nodes and available techniques from those nodes.
3. **Selects 2-5 candidate techniques** to try in parallel, ranked by heuristic relevance.
4. **Dispatches workers** — one per technique — with a precise prompt containing the current state, the technique's signature (from Ch. 10), and the goal.
5. **Evaluates worker results**, decides whether to continue expanding a branch, backtrack, or declare a path found.
6. **Maintains the search tree** as a JSON structure (see §3).

The orchestrator does NOT attempt proofs itself. It is a **router and evaluator**.

### 1.2 The Workers

Smaller or equal-capability LLMs, each given a single task:

> "You are given mathematical state S. Apply technique T (defined below) to S. Return either:
> (a) A new state S' with a proof sketch of S →[T]→ S', or
> (b) A declaration that T cannot apply to S, with justification."

Each worker receives:
- The **current state** (a mathematical object or proposition)
- The **technique signature** from Ch. 10 (inputs, process, outputs, preconditions, postconditions)
- The **goal** (so the worker can orient its output toward the target)
- Relevant **graph context** (nearby nodes, known theorems that might help)

Workers are stateless — they see only their assigned (state, technique, goal) triple, not the full search history.

### 1.3 The Pruner

A verification layer that kills branches **only when impossibility is certain** (100%). The pruner checks:

1. **Type mismatch**: technique T requires input of type X, but state S is type Y with no known conversion.
2. **Known impossibility theorems**: the repo catalogs these in Ch. 9 §4 — Abel-Ruffini (no radical formula for degree ≥ 5), Gödel (no complete consistent system), Turing (no halting decider), etc.
3. **Logical contradiction**: the worker's output contradicts a known theorem in the graph.
4. **Vacuous application**: the technique's preconditions are provably unsatisfied.

**Critical rule: if the pruner is not 100% certain, the branch survives.** Uncertain branches get deprioritized but not killed. Many breakthroughs come from paths that "look wrong" at first.

---

## 2. The Search Tree

### 2.1 Structure

The search tree is a rooted tree where:

- **Root node** = the problem statement, decomposed into starting axioms/states from the knowledge graph
- **Internal nodes** = intermediate mathematical results (new states produced by technique application)
- **Edges** = techniques applied (labeled with the technique ID from the graph)
- **Leaf nodes** = either:
  - **Goal reached** (the target theorem/result has been derived)
  - **Dead end** (pruned as impossible, or all techniques exhausted)
  - **Frontier** (unexplored — candidates for the next iteration)

```
                    [Problem: Prove f(A) ≤ f(primes)]
                    /           |              \
            [t_axiomatize]  [t_compose]    [t_reduce_canonical]
               /                |                  \
    [S: antichain ↔      [S: f(A) as         [S: factorization
     divisibility poset]   Dirichlet series]   as sequence]
         |                    |                    |
    [t_compose]          [t_complex_to_int]   [t_probabilistic]
         |                    |                    |
    [S: FTA + Euler      [S: von Mangoldt    [S: Markov chain
     product link]        weights extracted]   on primes]
         |                    |                    |
         ├──── MERGE ─────────┤                    |
         |                                         |
    [t_exhaustion_squeeze]                    [t_reduce_canonical]
         |                                         |
    [S: bound via                             [S: ergodic
     Mertens estimates]                        stationary dist.]
         |                                         |
         └──────────── MERGE ──────────────────────┘
                           |
                    [t_reductio + squeeze]
                           |
                    [GOAL: f(A) ≤ f(primes)]
```

### 2.2 Node format

Each node in the search tree is a JSON object:

```json
{
  "id": "search_node_0042",
  "state": {
    "description": "The sum f(A) can be encoded as a Dirichlet series Σ a_n / n^s where a_n = 1/(n log n) if n ∈ A, else 0",
    "formal": "f(A) = Σ_{n ∈ A} 1/(n log n) ≤ Σ_p 1/(p log p)",
    "graph_nodes_used": ["s_divisibility_definition", "s_euler_product_zeta", "s_dirichlet_series"],
    "graph_nodes_produced": ["search_state_dirichlet_encoding_of_fA"]
  },
  "parent": "search_node_0038",
  "technique_applied": "t_complex_analysis_to_integers",
  "confidence": 0.7,
  "children": ["search_node_0043", "search_node_0044"],
  "status": "frontier | expanded | pruned | goal",
  "depth": 3,
  "pruned_reason": null
}
```

### 2.3 Edge format

```json
{
  "from": "search_node_0038",
  "to": "search_node_0042",
  "technique": "t_complex_analysis_to_integers",
  "worker_output": {
    "new_state": "Dirichlet series encoding of f(A)",
    "proof_sketch": "By unique factorization (FTA), each n ∈ A has a unique prime factorization. The sum f(A) = Σ 1/(n log n) can be written as ...",
    "confidence": 0.7,
    "impossible": false
  }
}
```

---

## 3. The Algorithm

### 3.1 Main loop

```
FUNCTION discover(problem, knowledge_graph, max_depth=8, max_iterations=1000):

    # Step 1: Parse the problem
    start_nodes = orchestrator.identify_start_nodes(problem, knowledge_graph)
    goal_description = orchestrator.identify_goal(problem)

    # Step 2: Initialize search tree
    root = create_root_node(start_nodes, problem)
    tree = SearchTree(root)
    frontier = PriorityQueue()  # ordered by promise score
    frontier.push(root, priority=1.0)

    iteration = 0

    WHILE frontier is not empty AND iteration < max_iterations:
        iteration += 1

        # Step 3: Orchestrator selects the most promising frontier node
        current = frontier.pop()

        IF current.depth >= max_depth:
            current.status = "depth_limit"
            CONTINUE

        # Step 4: Orchestrator selects candidate techniques
        candidates = orchestrator.select_techniques(
            current_state = current.state,
            goal = goal_description,
            graph = knowledge_graph,
            already_tried = tree.techniques_tried_at(current),
            max_candidates = 5
        )

        # Step 5: Dispatch workers IN PARALLEL
        results = parallel_map(
            lambda technique: worker.apply_technique(
                state = current.state,
                technique = knowledge_graph.get_technique(technique),
                goal = goal_description,
                context = knowledge_graph.neighborhood(current.state.graph_nodes, radius=2)
            ),
            candidates
        )

        # Step 6: Process results
        FOR (technique, result) IN zip(candidates, results):

            IF result.impossible:
                # Pruner verification
                IF pruner.confirm_impossible(current.state, technique, result.reason):
                    child = create_node(result, parent=current, status="pruned")
                    tree.add(child)
                    CONTINUE
                ELSE:
                    # Pruner disagrees — demote but don't kill
                    result.confidence *= 0.3

            child = create_node(result, parent=current, status="frontier")
            tree.add(child)

            # Step 7: Check if goal is reached
            IF orchestrator.is_goal_reached(child.state, goal_description):
                child.status = "goal"
                RETURN tree.extract_path(root, child)

            # Step 8: Score and add to frontier
            score = orchestrator.score_promise(
                state = child.state,
                goal = goal_description,
                depth = child.depth,
                confidence = result.confidence
            )
            frontier.push(child, priority=score)

    RETURN tree  # no solution found; return full search tree for analysis
```

### 3.2 Orchestrator: technique selection heuristic

The orchestrator selects techniques using a priority score based on:

```
score(technique T, state S, goal G) =
    w1 * graph_proximity(T.outputs, G)          # how close T's outputs are to the goal in the graph
  + w2 * precondition_match(T.preconditions, S) # how well S satisfies T's input requirements
  + w3 * historical_success(T, problem_class)    # how often T appears in similar proofs in the graph
  + w4 * bridge_potential(T)                     # does T connect two different clusters?
  - w5 * depth_penalty                           # prefer shorter proofs
```

The **bridge_potential** term is critical: techniques that connect nodes in different clusters (e.g., number theory ↔ probability) get a bonus because cross-field transfers are where novel proofs live (see Ch. 12 §5).

Weights w1-w5 are tunable. Initial values from the graph analysis:

```
w1 = 0.30  (proximity to goal)
w2 = 0.25  (precondition match)
w3 = 0.15  (historical success rate)
w4 = 0.20  (bridge potential — high because novelty lives here)
w5 = 0.10  (depth penalty)
```

### 3.3 Worker prompt template

```markdown
## Task

You are a mathematician applying a specific technique to a mathematical state.
Your goal is to produce a new mathematical result.

## Current State

{state.description}

Formal: {state.formal}

## Technique to Apply

**Name:** {technique.name}
**Signature:** Input({technique.inputs}) → Process({technique.process}) → Output({technique.outputs})
**Preconditions:** {technique.preconditions}
**Postconditions:** {technique.postconditions}
**Known examples:** {technique.examples[:3]}

## Goal (for orientation — you do NOT need to reach it in one step)

{goal_description}

## Nearby known results (from the knowledge graph)

{context_nodes}

## Instructions

1. Check whether the technique's preconditions are satisfied by the current state.
2. If YES: apply the technique. Describe the new mathematical state you produce.
   Give a proof sketch (informal is fine). Rate your confidence 0.0 to 1.0.
3. If NO: explain why the technique cannot apply. Is this a fundamental
   impossibility (100% certain) or just a difficulty you can't resolve?

Return your answer as:
- new_state: [description of the new mathematical state]
- formal: [formal statement if possible]
- proof_sketch: [your reasoning]
- confidence: [0.0 to 1.0]
- impossible: [true/false]
- impossible_reason: [if impossible, why — and is this 100% certain?]
- graph_nodes_used: [which knowledge graph nodes you referenced]
```

---

## 4. Pruning Rules

### 4.1 Hard prunes (100% certain — kill the branch)

These correspond to the impossibility theorems cataloged in Ch. 9 §4:

| Rule | Source theorem | Example |
|---|---|---|
| No radical formula for degree ≥ 5 | Abel-Ruffini / Galois | Don't try to find a closed-form quintic root formula |
| No decision procedure for arbitrary Diophantine equations | MRDP / Matiyasevich | Don't try to build a general solver |
| No consistent complete axiomatization of arithmetic | Gödel | Don't try to prove consistency from within |
| No algorithm deciding program halting | Turing | Don't try to build a general halting checker |
| Type mismatch: technique requires topology, state is purely algebraic with no topological structure | Structural | Technique physically cannot engage |
| Contradicts known theorem in graph | Logical | Worker's output implies a known-false statement |

### 4.2 Soft demotions (uncertain — deprioritize but keep alive)

| Signal | Action | Reason |
|---|---|---|
| Worker confidence < 0.2 | Multiply priority by 0.3 | Low confidence suggests poor fit, but might be wrong |
| Technique has never been used in this problem class | Multiply priority by 0.5 | Unusual, but cross-field novelty comes from exactly this |
| State is "far" from goal in graph distance | Multiply priority by 0.7 | Indirect paths are longer but sometimes necessary |
| Multiple workers failed on this state | Multiply priority by 0.4 | State may be a dead end, but not proven impossible |

### 4.3 Anti-pruning rules (never prune these)

| Signal | Reason |
|---|---|
| Cross-cluster bridge technique | Novelty almost always comes from cross-field transfer |
| Worker says "I can't do it but it might be possible" | Uncertainty means the branch lives |
| State resembles a known open problem's neighborhood | Proximity to hard problems means proximity to discoveries |
| Depth < 3 | Too early to prune — most proofs need at least 3-4 steps |

---

## 5. Worked Example: Discovering the Primitive Set Proof

Here is a step-by-step trace of how the algorithm would discover the proof of Erdős Problem #1196.

### Iteration 1: Problem parsing

**Orchestrator** reads: "For any primitive set A, prove f(A) = Σ 1/(a log a) ≤ f(primes)."

Identifies start nodes:
- `s_divisibility_definition` (axiom)
- `s_antichain_in_boolean_lattice` (axiom)
- `s_fundamental_theorem_of_arithmetic` (theorem)

Identifies goal: a bound on f(A) showing primes maximize it.

### Iteration 2: First technique selection

Orchestrator queries the graph for techniques reachable from these nodes. Selects:

| Candidate | Rationale |
|---|---|
| `t_axiomatize_from_instances` | Formalize the primitive set structure |
| `t_compose_with_identity` | Connect FTA to analytic objects |
| `t_complex_analysis_to_integers` | Encode f(A) as a Dirichlet-type sum |
| `t_probabilistic_existence` | Bridge score is high (connects to both NT and prob) |
| `t_reduce_to_canonical_form` | Generic but high-connectivity technique |

Dispatches 5 workers in parallel.

### Iteration 3: Worker results

| Worker | Technique | Result | Confidence |
|---|---|---|---|
| A | Axiomatize | "Primitive set = antichain in (Z_{>1}, |). No element divides another." | 0.95 |
| B | Compose with identity | "f(A) = Σ 1/(a log a). By FTA, each a = Π p_i^{e_i}. Can rewrite using multiplicative structure." | 0.80 |
| C | Complex analysis to integers | "Encode f(A) as a sum weighted by 1/log a ≈ Λ(a) inverse. Von Mangoldt connection: Λ(n) = log p if n = p^k." | 0.65 |
| D | Probabilistic existence | "The number of prime factors ω(n) satisfies Erdős-Kac: (ω(n) - log log n)/√(log log n) → N(0,1). Factorization is 'random.'" | 0.50 |
| E | Reduce to canonical form | "Can normalize primitive sets by replacing each a with its 'prime signature' — the multiset of exponents." | 0.40 |

No branch pruned. All 5 children added to frontier.

### Iteration 4: Orchestrator evaluates and expands

Highest-promise node: Worker C's result (von Mangoldt connection).

Orchestrator selects techniques for this state:
- `t_compose_with_identity` (connect von Mangoldt to Chebyshev ψ)
- `t_reduce_to_canonical_form` (reformulate using Λ-weights)
- `t_exhaustion_squeeze` (bound using Mertens)

Also expands Worker D's result (factorization is random):
- `t_reduce_to_canonical_form` (formalize as Markov chain)
- `t_probabilistic_existence` (apply ergodic theorem)

### Iteration 5: The breakthrough path

Worker on D's branch + `t_reduce_to_canonical_form` returns:

> "Model the prime factorization of n as a Markov chain. State space: partial products. Transition from m to mp with probability proportional to Λ(p)/(p log p). This is an irreducible aperiodic Markov chain on a countable state space."
>
> Confidence: 0.55

Worker on D's branch + `t_probabilistic_existence` returns:

> "By the Markov chain ergodic theorem, the stationary distribution exists. The sum f(A) for a primitive set A is bounded by the total weight of the stationary measure on single-prime states. These weights are exactly 1/(p log p) for each prime p."
>
> Confidence: 0.60

**Orchestrator merges** the von Mangoldt branch (C) with the Markov chain branch (D) — both reference Chebyshev ψ and Λ(n).

### Iteration 6: Closing the proof

Merged state → `t_exhaustion_squeeze`:

> "The Markov chain's stationary distribution is unique. For any primitive set A (antichain), the induced measure on A is dominated by the stationary measure. By Mertens' theorem, Σ_p 1/(p log p) converges. Therefore f(A) ≤ Σ_p 1/(p log p) = f(primes)."
>
> Confidence: 0.75

**Orchestrator recognizes goal is reached.** Extracts the full path:

```
Root -> [t_axiomatize] -> antichain formalized
     -> [t_compose] -> FTA + multiplicative structure
     -> [t_complex_to_int] -> von Mangoldt weights
     -> [t_reduce_canonical] -> Markov chain model
     -> [t_probabilistic + ergodic] -> stationary distribution bound
     -> [t_exhaustion_squeeze] -> f(A) ≤ f(primes). QED.
```

Total depth: 6. Total iterations: ~15-20 (with parallel workers). Total worker calls: ~40-60.

---

## 6. Implementation Notes

### 6.1 Knowledge graph as the search space

The system reads `knowledge_graph.json` directly:

```python
import json

with open('knowledge_graph.json') as f:
    graph = json.load(f)

nodes = {n['id']: n for n in graph['nodes']}  # 6,225 nodes
edges = graph['edges']                          # 10,556 edges

techniques = {n['id']: n for n in graph['nodes'] if n['kind'] == 'technique'}  # 62 techniques
```

For each technique, the system reads its full signature from Ch. 10 (`10_toolbox.md`) — inputs, process, outputs, preconditions, postconditions, and examples.

### 6.2 Graph neighborhood queries

```python
def neighborhood(node_ids, radius=2):
    """Return all nodes within `radius` hops of any node in `node_ids`."""
    visited = set(node_ids)
    frontier = set(node_ids)
    for _ in range(radius):
        next_frontier = set()
        for e in edges:
            if e['from'] in frontier and e['to'] not in visited:
                next_frontier.add(e['to'])
                visited.add(e['to'])
            if e['to'] in frontier and e['from'] not in visited:
                next_frontier.add(e['from'])
                visited.add(e['from'])
        frontier = next_frontier
    return {nid: nodes[nid] for nid in visited if nid in nodes}
```

### 6.3 Technique-to-cluster mapping

Each technique belongs to one of 12 clusters (Ch. 10 §1). Cross-cluster applications get the bridge bonus:

```python
CLUSTER = {
    't_spot_pattern_in_table': 1,
    't_verify_on_special_cases': 1,
    't_complete_the_square': 2,
    't_reduce_to_canonical_form': 2,
    't_compose_with_identity': 2,
    't_symmetry_reduction': 3,
    't_conserved_quantity': 3,
    't_duality': 3,
    't_character_decomposition_count': 3,
    't_exhaustion_squeeze': 4,
    't_interpolate_and_continue': 4,
    't_frequency_decomposition': 4,
    't_axiomatize_from_instances': 5,
    't_structural_isomorphism': 5,
    't_ultraproduct_transfer': 5,
    't_raise_dimension': 6,
    't_obstruction_class': 6,
    't_compactness_argument': 6,
    't_diagonalize': 7,
    't_arithmetize_syntax': 7,
    't_force_independence': 7,
    't_contraction_fixed_point': 8,
    't_infinite_descent': 8,
    't_flow_with_surgery': 8,
    't_physics_to_pde': 9,
    't_complex_analysis_to_integers': 9,
    't_analysis_algebra_topology_bridge': 9,
    't_major_minor_arc_decomposition': 9,
    't_ergodic_correspondence': 9,
    't_finite_case_check': 10,
    't_formal_verify': 10,
    't_distributed_collaboration': 10,
    't_probabilistic_existence': 11,
    't_pigeonhole_collision': 11,
    't_polynomial_method': 11,
    't_sieve_by_optimized_quadratic': 11,
    # ... remaining techniques in clusters 12, composite, etc.
}

def bridge_potential(technique_id, current_cluster):
    """Higher score if technique is from a different cluster than the current state."""
    t_cluster = CLUSTER.get(technique_id, 0)
    if t_cluster != current_cluster and t_cluster != 0:
        return 1.0  # cross-cluster: maximum bridge potential
    return 0.2      # same cluster: low bridge potential
```

### 6.4 Parallelism

Workers are independent and stateless — they can run in full parallel. For a branching factor of 5 techniques per node and depth 6:

- **Sequential**: 5^6 = 15,625 worker calls worst case
- **Parallel at each level**: 5 workers × 6 levels = 30 sequential rounds, 15,625 total calls
- **With pruning**: empirically ~40-100 worker calls to find a proof (most branches die early)

### 6.5 Merging branches

When two branches produce states that reference the **same knowledge graph nodes**, the orchestrator can merge them. This is detected by set intersection:

```python
def should_merge(state_a, state_b):
    overlap = set(state_a.graph_nodes_used) & set(state_b.graph_nodes_used)
    return len(overlap) >= 2  # at least 2 shared nodes suggests convergence
```

Merging creates a new node whose state combines both branches' results, potentially unlocking techniques that neither branch could access alone.

---

## 7. Scaling Considerations

### 7.1 Current graph size

| Metric | Count |
|---|---|
| Axiom nodes | 3,791 |
| State nodes | 4,994 |
| Theorem nodes | 4,262 |
| Technique nodes | 873 |
| Edges | 23,397 |
| Average edges per technique | 27 |
| Max edges (Auxiliary construction) | 2,580 |
| Search tree branching factor | 3-5 (after heuristic selection) |
| Typical proof depth | 3-6 |

### 7.2 Token optimizations (implemented)

Three optimizations reduce API cost by ~85-95% compared to a naive approach:

#### Optimization 1: Haiku workers (~20x cheaper per call)

Workers apply a single technique to a single state — a focused task that Haiku handles well. The orchestrator (which needs strategic reasoning) stays on Sonnet or Opus.

```
Workers default:      Haiku  ($0.25/MTok in,  $1.25/MTok out)
Orchestrator default: Sonnet ($3.00/MTok in, $15.00/MTok out)
```

Override: `--worker-model claude-sonnet-4-20250514` for harder problems.

#### Optimization 2: Prompt caching (~90% savings on system prompts)

The worker system prompt is identical across all calls. The Anthropic API's prompt caching (`cache_control: {"type": "ephemeral"}`) caches it for 5 minutes:

- First call: 25% write premium on system prompt
- Calls 2-N: 90% discount (cache read)

For 50 worker calls, the ~150-token system prompt is paid in full once, then read from cache 49 times at 10% cost.

#### Optimization 3: Shorter prompts (~60% fewer input tokens per worker)

Worker user prompts trimmed from ~600 tokens to ~200-400 tokens:
- 3 example inputs/outputs (was 5)
- 8 context nodes on one semicolon-separated line (was 15 with bullet points)
- No verbose instruction block (moved into system prompt)
- No technique ID or edge count details

#### Combined cost estimate

| Scenario | Naive (Sonnet, no cache, verbose) | Optimized (Haiku, cached, trimmed) | Savings |
|---|---|---|---|
| 50 worker calls | ~$0.50 | ~$0.03 | **94%** |
| 200 worker calls + LLM orchestration | ~$3.00 | ~$0.25 | **92%** |
| 500 worker calls (deep search) | ~$8.00 | ~$0.50 | **94%** |

Token usage is printed at the end of each run:

```
--- Token Usage ---
  Input tokens:    12,450
  Output tokens:   8,200
  Cache reads:     7,350 (saved ~90% on these)
  Cache creates:   150
  Worker calls:    49
  Cache hit rate:  37%
```

### 7.3 When to stop

The system should stop when:
1. **Goal reached**: a path from root to goal with all workers' confidence ≥ 0.5.
2. **Frontier exhausted**: all frontier nodes are pruned or depth-limited.
3. **Iteration limit**: max_iterations reached (configurable, default 1000).
4. **Diminishing returns**: the highest-priority frontier node's score drops below a threshold (e.g., 0.05).

---

## 8. Relationship to Existing Systems

| System | Approach | This workflow's advantage |
|---|---|---|
| AlphaProof (DeepMind) | RL + Lean search | This uses a curated knowledge graph with human-organized technique signatures, reducing the search space from "all possible Lean tactics" to 62 named techniques |
| GPT-5 "vibe maths" | Single-shot prompting | This decomposes the problem into a structured search with verification at each step |
| Aristotle (Harmonic) | Auto-formalization | Complementary — Aristotle could serve as the formal-verify worker in this pipeline |
| Lean/Mathlib | Tactic search | This operates at a higher abstraction level (technique-level, not tactic-level) |

The key differentiator: **the knowledge graph constrains the search**. Instead of searching over all possible mathematical statements (infinite), the system searches over compositions of 62 known techniques applied to 6,225 known mathematical states (finite, tractable).

---

## 9. Extending the Graph

When the system discovers a new proof, the path should be **added back to the knowledge graph** as new edges:

```python
def integrate_discovery(tree, path, knowledge_graph):
    """Add a discovered proof path back into the knowledge graph."""
    for i, node in enumerate(path):
        if node.state not in knowledge_graph.nodes:
            knowledge_graph.add_node({
                'id': f's_discovered_{node.id}',
                'kind': 'state',
                'name': node.state.description[:80],
                'description': node.state.formal
            })
        if i > 0:
            knowledge_graph.add_edge({
                'from': path[i-1].state.graph_node_id,
                'to': node.state.graph_node_id,
                'technique': node.technique_applied,
                'role': 'discovered',
                'used_in_theorem': f's_discovered_theorem_{path[-1].id}'
            })
```

This creates a **self-improving system**: each solved problem adds new edges to the graph, making future searches more likely to find cross-field connections. The Primitive Sets proof, once integrated, would add the "factorization → Markov chain" edge that enables future problems in integer anatomy to find probabilistic paths more quickly.
