# Mathematical Discovery Engine (MDE)

> **Treat mathematical proof as path-finding through a graph.** A knowledge graph of 15,941 mathematical states and 1,223 proof techniques — from Pythagoras to Perelman — that an LLM searches to discover new theorems.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Knowledge Graph Nodes](https://img.shields.io/badge/Nodes-15%2C941-brightgreen.svg)](#knowledge-graph)
[![Knowledge Graph Edges](https://img.shields.io/badge/Edges-26%2C614-brightgreen.svg)](#knowledge-graph)
[![Proof Techniques](https://img.shields.io/badge/Techniques-1%2C223-orange.svg)](#knowledge-graph)
[![Theorems](https://img.shields.io/badge/Theorems-5%2C055-purple.svg)](#knowledge-graph)
[![GitHub stars](https://img.shields.io/github/stars/ansumandas441/mathematical-discovery-engine?style=social)](https://github.com/ansumandas441/mathematical-discovery-engine)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/ansumandas441/mathematical-discovery-engine/pulls)

<p align="center">
  <a href="https://ansumandas441.github.io/mathematical-discovery-engine/"><b>▶ Explore the live interactive 3D graph →</b></a>
  &nbsp;·&nbsp; no install, runs in your browser
</p>

<p align="center">
  <a href="https://ansumandas441.github.io/mathematical-discovery-engine/">
    <img src="assets/knowledge_graph_3d_preview.gif" alt="3D Knowledge Graph — 15,941 mathematical nodes connected by 26,614 edges — click to explore live" width="720">
  </a>
  <br>
  <sub>15,941 nodes · 26,614 edges · 1,223 proof techniques · 5,055 theorems — <a href="https://ansumandas441.github.io/mathematical-discovery-engine/">click the graph to explore it in 3D</a></sub>
</p>

## What This Repository Does

This repository **encodes the structure of mathematical knowledge as a graph and uses it to discover new theorems automatically**.

It starts from a simple observation: every major theorem in mathematics was discovered by applying known techniques to known facts. Galois used symmetry reduction on polynomial roots. Cantor used diagonalization on real numbers. Wiles used a bridge between modular forms and elliptic curves. The techniques are reusable — the same method of proof appears across centuries and subdisciplines.

This project does three things:

1. **Collects the knowledge.** A detailed report covering ~100 of the most consequential theorems in mathematics — from Pythagoras through Perelman — with the discovery context, motivation, thought process, and proof ideas behind each. The report spans 13 chapters organized chronologically, drawing from primary sources (Euler's letters, Gauss's diaries, Ramanujan's notebooks, Wiles's interviews) where they survive.

2. **Builds a knowledge graph.** The report is distilled into a structured directed graph: 15,941 nodes (4,135 axioms, 5,528 intermediate states, 5,055 theorems, 1,223 techniques) connected by 26,614 edges. Each technique has a formal signature — inputs, process, outputs, preconditions — organized into 12 clusters (algebraic manipulation, symmetry & invariants, cross-field transfer, topology & obstruction, etc.). The graph captures not just *what* is true, but *how* each truth was reached from earlier ones.

3. **Proposes and implements a discovery engine.** Mathematical proof is reframed as **path-finding through this finite graph**. An orchestrator LLM selects which techniques to try; worker LLMs attempt each technique application in parallel; a pruner eliminates impossible branches using known impossibility theorems (Abel-Ruffini, Gödel, Turing). The search tree grows until a path from the starting axioms to the goal theorem is found — or the frontier is exhausted.

The key insight: instead of searching over all possible mathematical statements (infinite), the engine searches over **compositions of 1,223 known techniques applied to 15,941 known states** (finite, tractable). Each solved problem adds new edges back to the graph, creating a self-improving system.

---

## How It Works

Mathematical proof is path-finding through a finite directed graph. Nodes are mathematical states (axioms, intermediate results, theorems). Edges are techniques (the 1,223 operations cataloged across 12 clusters). An orchestrator LLM directs the search; worker LLMs attempt each technique application; a pruner eliminates impossible branches.

```
                    ┌──────────────────────┐
                    │   ORCHESTRATOR LLM   │  (Sonnet — strategic decisions)
                    │                      │
                    │  - Parses problem    │
                    │  - Picks techniques  │
                    │  - Evaluates results │
                    │  - Decides next path │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┼─────────────┐
                 │             │             │
          ┌──────▼──────┐ ┌───▼────────┐ ┌──▼───────────┐
          │  WORKER A   │ │  WORKER B  │ │  WORKER C    │  (Haiku — cheap, parallel)
          │  Tries      │ │  Tries     │ │  Tries       │
          │  Technique 1│ │  Technique 2│ │  Technique 3 │
          └──────┬──────┘ └───┬────────┘ └──┬───────────┘
                 │            │             │
                 ▼            ▼             ▼
          ┌────────────────────────────────────────┐
          │           RESULT COLLECTOR             │
          │  Each worker returns:                  │
          │    - new_state: mathematical result    │
          │    - confidence: 0.0 - 1.0             │
          │    - proof_sketch: reasoning           │
          │    - impossible: true/false             │
          └────────────────────┬───────────────────┘
                               │
                        ┌──────▼──────┐
                        │   PRUNER    │  Kills only branches that are 100% dead
                        └──────┬──────┘
                               │
                        ┌──────▼──────┐
                        │ SEARCH TREE │  Priority queue — expands most promising node
                        └─────────────┘
```

### The Search Loop

1. **Parse problem** — identify start nodes in the knowledge graph and define the goal state
2. **Select techniques** — score all 1,223 techniques using a weighted heuristic
3. **Dispatch workers in parallel** — each worker applies ONE technique to ONE state, returns a new state with confidence and proof sketch
4. **Prune** — kill branches violating impossibility theorems (Abel-Ruffini, Gödel, Turing, etc.); demote low-confidence branches
5. **Check goal** — does the new state match the target?
6. **Repeat** — expand the most promising frontier node next

### Technique Scoring Heuristic

The orchestrator ranks techniques using:

```
score = 0.30 * proximity_to_goal
      + 0.25 * precondition_match
      + 0.15 * historical_success
      + 0.20 * bridge_potential       ← cross-cluster novelty bonus
      - 0.10 * depth_penalty
```

The **bridge_potential** term is critical: techniques that connect nodes across different clusters (e.g., number theory ↔ probability) get a bonus because cross-field transfers are where novel proofs live.

### Pruning Rules

**Hard prunes (100% certain — kill the branch):**
- No radical formula for degree ≥ 5 (Abel-Ruffini)
- No decision procedure for arbitrary Diophantine equations (MRDP)
- No consistent complete axiomatization of arithmetic (Gödel)
- No algorithm deciding program halting (Turing)
- Type mismatch or logical contradiction with a known theorem

**Soft demotions (uncertain — deprioritize but keep alive):**
- Worker confidence < 0.2 → multiply priority by 0.3
- Worker says impossible but reason isn't definitive → multiply by 0.3

**Anti-pruning (never prune these):**
- Cross-cluster bridge techniques
- Any branch at depth < 3

---

## Setup

### Requirements

- Python 3
- Two pip packages

```bash
pip install anthropic networkx
```

Or from the requirements file:

```bash
pip install -r discovery_engine/requirements.txt
```

### Knowledge Graph

The graph ships as `knowledge_graph.json` (5 MB) in the repo root. No separate database or server needed — the engine loads it directly into memory via NetworkX.

| Metric | Count |
|---|---|
| Axiom nodes | 4,135 |
| State nodes | 5,528 |
| Theorem nodes | 5,055 |
| Technique nodes | 1,223 |
| Total edges | 26,614 |

---

## Configuring Worker APIs

Workers are the LLMs that attempt each technique application. Three modes are available:

### Mode 1: Dry Run (free, no API)

Uses mock workers that return synthetic results based on graph structure. Good for testing the search logic.

```bash
python3 -m discovery_engine.discover --dry-run \
    "Prove that for any primitive set A, f(A) <= f(primes)"
```

### Mode 2: CLI Workers (uses Claude Code subscription)

Spawns `claude -p` subprocesses. No API key needed — uses your existing Claude Code subscription billing.

```bash
python3 -m discovery_engine.discover --use-cli \
    --start s_divisibility_definition,s_antichain_in_boolean_lattice \
    --goal "f(A) = sum 1/(a log a) is maximized when A is the set of primes" \
    "Erdős primitive set conjecture"
```

Default: 2 parallel workers. Override with `--workers N`.

### Mode 3: API Workers (Anthropic API key)

Direct API calls with prompt caching. The cheapest per-call option for large searches.

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python3 -m discovery_engine.discover \
    "Prove the Erdős primitive set conjecture"
```

Default worker model: `claude-haiku-4-5-20251001` (~20x cheaper than Sonnet). Override with `--worker-model`.

Default: 5 parallel workers. Override with `--workers N`.

#### Token Optimizations

Three optimizations reduce API cost by ~90-95%:

1. **Haiku workers** — workers apply a single technique to a single state, a focused task that Haiku handles well
2. **Prompt caching** — the static worker system prompt is marked with `cache_control: {"type": "ephemeral"}`, so after the first call all subsequent calls within 5 minutes pay only ~10% for that block
3. **Trimmed prompts** — user prompts are ~200-400 tokens (3 example inputs/outputs, 8 context nodes, no verbose instructions)

| Scenario | Naive (Sonnet, no cache) | Optimized (Haiku, cached) | Savings |
|---|---|---|---|
| 50 worker calls | ~$0.50 | ~$0.03 | 94% |
| 200 worker calls | ~$3.00 | ~$0.25 | 92% |
| 500 worker calls | ~$8.00 | ~$0.50 | 94% |

---

## Configuring the Orchestrator (Master AI)

The orchestrator is the "brain" that parses problems, selects techniques, and evaluates results. It runs separately from the workers.

### Heuristic Mode (default)

No LLM calls for technique selection or goal checking — uses keyword matching and graph structure. Free.

```bash
python3 -m discovery_engine.discover --dry-run \
    --start s_divisibility_definition \
    --goal "f(A) is maximized by primes" \
    "Erdős primitive set conjecture"
```

### LLM Orchestration Mode

The orchestrator uses Claude to parse the problem, select techniques, and verify goals. Smarter but costs orchestrator tokens.

```bash
python3 -m discovery_engine.discover --llm-orchestrate \
    --model claude-sonnet-4-20250514 \
    "Prove the Erdős primitive set conjecture"
```

Default orchestrator model: `claude-sonnet-4-20250514`. Override with `--model`.

---

## Running a Discovery

### Basic Examples

```bash
# Dry run — test the search logic for free
python3 -m discovery_engine.discover --dry-run \
    "Prove the Erdős primitive set conjecture"

# CLI workers — uses your Claude Code subscription
python3 -m discovery_engine.discover --use-cli \
    --start s_divisibility_definition,s_antichain_in_boolean_lattice \
    --goal "f(A) = sum 1/(a log a) is maximized when A is the set of primes" \
    "Erdős primitive set conjecture"

# Full API mode with LLM orchestration
export ANTHROPIC_API_KEY=sk-ant-...
python3 -m discovery_engine.discover --llm-orchestrate \
    --model claude-sonnet-4-20250514 \
    --worker-model claude-haiku-4-5-20251001 \
    --workers 5 --max-depth 7 --max-iterations 200 --candidates 4 \
    "Prove the Erdős primitive set conjecture"
```

### Checkpointing and Resume

Long runs save periodic checkpoints. Ctrl+C triggers a graceful save before exiting.

```bash
# Run with auto-checkpointing (saves every 3 iterations)
python3 -m discovery_engine.discover --use-cli \
    --checkpoint-dir checkpoints --checkpoint-every 3 \
    --start s_divisibility_definition,s_antichain_in_boolean_lattice \
    --goal "density f(c) exists and is continuous" \
    "Prime gap density continuity conjecture"

# Resume from last checkpoint
python3 -m discovery_engine.discover --use-cli \
    --resume checkpoints/checkpoint_latest.json \
    "ignored — problem is restored from checkpoint"
```

### Continuable runs: problem registry + per-level resume

Every problem you give is recorded in a **registry** (`runs/registry.json`) under a
stable id (hash of the problem + goal). Give the **same problem again** and the engine
recognizes it and **resumes from where it stopped** — no `--resume` path needed.

```bash
# Start a run (Ctrl-C any time — state is saved). --bfs = level-order tree search.
python3 -m discovery_engine --use-cli --bfs "Prove <X>"

# Later: the SAME command auto-resumes (untried techniques first, pruned ones skipped)
python3 -m discovery_engine --use-cli --bfs "Prove <X>"

# List every problem you've worked on (status, iterations, last updated)
python3 -m discovery_engine --list-problems

# Inspect a problem: tree + per-level ledger of which technique was tried at which level
python3 -m discovery_engine --inspect <problem-id>

# Discard saved progress and start the problem fresh
python3 -m discovery_engine --restart "Prove <X>"
```

**What the saved state remembers** (in `runs/<id>/state.json`): each search node keeps an
*attempt ledger* — the ordered candidate techniques and, per technique, the outcome
(`child` / `pruned` / `impossible`). So on resume, **untried techniques run before
descending a level** (e.g. `[fourier, laplace]` interrupted after `fourier` resumes at
`laplace`), and **dead directions stay dead** (an `impossible` technique is never retried).
Interrupt granularity is the worker window — use `--workers 1` for strict
one-technique-at-a-time resumption.

### Example Output

```
Loading knowledge graph from knowledge_graph.json...
Loaded in 0.8s — {'nodes': 15941, 'edges': 26614, 'techniques': 1223}
Mode: LIVE (API)
  Orchestrator model: claude-sonnet-4-20250514
  Worker model:       claude-haiku-4-5-20251001
  Prompt caching:     ON

Problem: Prove the Erdős primitive set conjecture
Start nodes: ['s_divisibility_definition', 's_antichain_in_boolean_lattice']
Goal: f(A) = sum 1/(a log a) is maximized when A is the set of primes

--- Iteration 1 | Expanding sn_0001 (depth 0) | Frontier: 0 ---
  State: Erdős primitive set conjecture
  Candidates: ['t_axiomatize_from_instances', 't_compose_with_identity',
               't_complex_analysis_to_integers', 't_probabilistic_existence']
  ○ t_axiomatize -> sn_0002 (conf=95%) Primitive set = antichain in (Z>1, |)
  ○ t_compose -> sn_0003 (conf=80%) FTA + multiplicative structure
  ○ t_complex -> sn_0004 (conf=65%) Von Mangoldt weights
  ○ t_probabilistic -> sn_0005 (conf=50%) Erdős-Kac connection

--- Iteration 2 | Expanding sn_0004 (depth 1) | Frontier: 3 ---
  ...

★ GOAL REACHED at sn_0042!

=== DISCOVERED PATH ===
  Layer 0: [START] -> Erdős primitive set conjecture (conf=100%)
  Layer 1: [t_axiomatize_from_instances] -> antichain formalized (conf=95%)
  Layer 2: [t_compose_with_identity] -> FTA + multiplicative structure (conf=80%)
  Layer 3: [t_complex_analysis_to_integers] -> von Mangoldt weights (conf=65%)
  Layer 4: [t_reduce_to_canonical_form] -> Markov chain model (conf=55%)
  Layer 5: [t_probabilistic_existence] -> stationary distribution bound (conf=60%)
  Layer 6: [t_exhaustion_squeeze] -> f(A) ≤ f(primes). QED. (conf=75%)
=== END ===

============================================================
Discovery complete in 42.3s
Stats: {"iterations": 15, "worker_calls": 47, "pruned": 12, "goal_found": true}

--- Token Usage ---
  Input tokens:    12,450
  Output tokens:   8,200
  Cache reads:     7,350 (saved ~90% on these)
  Cache creates:   150
  Worker calls:    47
  Cache hit rate:  37%
```

---

## All CLI Flags

| Flag | Default | Description |
|---|---|---|
| `--dry-run` | — | Mock workers, zero API cost |
| `--use-cli` | — | Use `claude -p` subprocess as worker (subscription billing) |
| `--llm-orchestrate` | — | LLM picks techniques + checks goal (more expensive) |
| `--start <ids>` | auto | Comma-separated start node IDs |
| `--goal <text>` | auto | Goal description |
| `--graph <path>` | auto-detect | Path to `knowledge_graph.json` |
| `--max-depth N` | 7 | Maximum search tree depth |
| `--max-iterations N` | 200 | Maximum search iterations |
| `--candidates N` | 4 | Techniques to try per step |
| `--workers N` | 2 (cli) / 5 (api) | Number of parallel workers |
| `--model <id>` | `claude-sonnet-4-20250514` | Orchestrator model |
| `--worker-model <id>` | `claude-haiku-4-5-20251001` | Worker model |
| `--save-tree <path>` | — | Save search tree to JSON |
| `--print-tree` | — | Print tree structure at the end |
| `--checkpoint-dir <path>` | off | Directory for periodic checkpoints |
| `--checkpoint-every N` | 5 | Save checkpoint every N iterations |
| `--resume <path>` | — | Resume from a checkpoint file |
| `--bfs` | — | Breadth-first (level-order) search instead of best-first priority search |
| `--runs-dir <path>` | `<repo>/runs` | Where the problem registry + per-problem state live |
| `--restart` | — | Ignore saved state for this problem and start fresh |
| `--list-problems` | — | List every problem the engine has been given, then exit |
| `--inspect <id>` | — | Print saved tree + per-level attempt ledger for a problem, then exit |
| `--quiet` | — | Suppress progress output |

---

## Interactive 3D Graph Viewer

The entire knowledge graph is explorable in an interactive 3D visualization — orbit, zoom, click, and trace the connections between axioms, techniques, and theorems.

<!-- <p align="center">
  <img src="assets/knowledge_graph_3d_preview.gif" alt="3D Knowledge Graph Viewer" width="680">
  <br>
  <sub>Nodes glow by type · Particles flow along proof paths · Hover to highlight connections</sub>
</p> -->

<!-- REPLACE_WITH_VIDEO: Once you have a user-attachments URL, put it on its own line here to get inline playback -->


https://github.com/user-attachments/assets/e6afe79e-9c0c-41e5-a049-af1aba319a31




**TL;DR:** Every node is a mathematical object (axiom, state, theorem, or technique). Every edge is a logical dependency. Hover a node to see its connections light up. Double-click to explore its neighborhood. Particles flowing along edges show the direction of mathematical reasoning — from axioms through techniques to theorems.

### Quick start

The simplest way is the bundled launcher — it frees the port, starts a local server, and opens the 3D viewer automatically:

```bash
./run_graph.sh           # serves on port 8765 and opens the 3D viewer
./run_graph.sh 9000      # use a custom port
```

Prefer the 2D viewer (lighter)? Use `./serve_viewer.sh` instead, or start a server by hand:

```bash
python3 -m http.server 8765
open http://localhost:8765/graph_viewer_3d.html    # 3D viewer (recommended)
open http://localhost:8765/graph_viewer.html        # 2D viewer (lighter)
```

Opening HTML files directly (`file://`) won't work — `fetch()` of `knowledge_graph.json` is blocked by the browser's same-origin policy. Use a local server.

### What you can do

| Action | How |
|---|---|
| **Orbit & zoom** | Drag to rotate, scroll to zoom, right-drag to pan |
| **Inspect a node** | Click — details panel slides in with description, connections, cluster |
| **Explore neighborhood** | Double-click any node — see it + all its connections in a focused view |
| **Filter by kind** | Toggle axiom / state / theorem / technique checkboxes |
| **Filter by cluster** | Select one of 12 technique clusters (e.g. "Symmetry & invariants") |
| **Search** | Type any name or ID, press Enter |
| **Neighborhood mode** | Switch mode dropdown — search a node to center the graph on it |

### Visual encoding

| Element | Meaning |
|---|---|
| **Gray dots** | Axioms — foundational definitions and objects |
| **Blue dots** | States — intermediate results |
| **Green stars** | Theorems — proved results |
| **Colored diamonds** | Techniques — sized by number of connections, colored by cluster |
| **Flowing particles** | Direction of logical dependency (axiom → technique → theorem) |
| **Bright edges on hover** | Direct connections to the hovered node |

---

## The Report

The knowledge graph is built from a companion report tracing ~100 pivotal theorems with their discovery context, motivation, and thought process.

### Chapters

| # | File | Era | Focus |
|---|---|---|---|
| 0 | [`00_introduction.md`](00_introduction.md) | — | What is a theorem, and how are theorems discovered? |
| 1 | [`01_ancient.md`](01_ancient.md) | prehistory – 1400 CE | Babylonian, Greek, Indian, Chinese, Islamic foundations |
| 2 | [`02_renaissance_17c.md`](02_renaissance_17c.md) | 1400 – 1700 | Cubic equations, analytic geometry, calculus |
| 3 | [`03_eighteenth_century.md`](03_eighteenth_century.md) | 1700 – 1800 | Euler, the Bernoullis, Lagrange, Laplace |
| 4 | [`04_nineteenth_century.md`](04_nineteenth_century.md) | 1800 – 1900 | Gauss, Cauchy, Galois, Riemann, Cantor |
| 5 | [`05_early_twentieth_century.md`](05_early_twentieth_century.md) | 1900 – 1950 | Hilbert, Noether, Gödel, Turing |
| 6 | [`06_modern_contemporary.md`](06_modern_contemporary.md) | 1950 – present | Wiles, Perelman, computer-assisted proofs |
| 7 | [`07_brief_catalog.md`](07_brief_catalog.md) | all | Abbreviated reference for remaining theorems |
| 8 | [`08_epilogue.md`](08_epilogue.md) | — | Patterns in mathematical discovery |
| 9 | [`09_discovery_techniques.md`](09_discovery_techniques.md) | cross-cutting | 1,223 techniques across 12 clusters |
| 10 | [`10_toolbox.md`](10_toolbox.md) | cross-cutting | Function-style technique dictionary with Mermaid diagrams |
| 11 | [`11_knowledge_graph.md`](11_knowledge_graph.md) | cross-cutting | Knowledge graph documentation |
| 12 | [`12_ai_solvable_discoveries.md`](12_ai_solvable_discoveries.md) | 2026 | Recently solved problems traced through the graph |
| 13 | [`13_workflow.md`](13_workflow.md) | cross-cutting | Discovery engine architecture and worked examples |

Read in order for the narrative arc, or jump by area using [`INDEX.md`](INDEX.md).

---

## Recent Improvements

### 2026-06-07 — Continuable runs: problem registry + per-level resumable state

The engine now remembers problems across sessions and resumes searches at
technique-level granularity.

- **Problem registry (`runs/registry.json`).** Every problem is recorded under a stable
  id (`sha1` of the normalized problem + goal). Re-giving the same problem is detected
  automatically and resumes its saved state instead of starting over.
  New: `--list-problems`, `--inspect <id>`, `--restart`, `--runs-dir`.
- **Per-(node, technique) attempt ledger.** Each search node stores its ordered
  `candidates` and an `attempts` map (`technique → child | pruned | impossible`),
  persisted in `runs/<id>/state.json`. `--inspect` prints the per-level ledger so you can
  see exactly which technique was tried at which level and what was pruned.
- **BFS / level-order mode (`--bfs`).** FIFO frontier: every technique at one level
  before descending — the explicit tree-search picture (`[fourier, laplace]` per level).
- **Exact, granular resume.** On Ctrl-C, a partially-expanded node is marked `partial`
  and re-queued at the front; on resume its **untried** techniques run before descending,
  and `impossible`/`pruned` directions are **never retried**. Final state is also saved on
  normal completion, so re-runs continue rather than restart.

Implementation: new `discovery_engine/registry.py`; `search_tree.py` gains the `partial`
status, ledger fields, a BFS FIFO frontier, `requeue_front`, and an `attempt_report`;
`orchestrator.py` expands nodes via a resumable, per-technique `_expand_node`;
`discover.py` wires the registry, the new flags, and auto-resume. Backward compatible with
existing checkpoints. See [`discovery_engine/README.md`](discovery_engine/README.md#continuable-runs-registry--resumable-state)
for details.

## Roadmap

Where this is headed — see [`future_works.md`](future_works.md) for the full list:

- Expand the graph beyond ~100 theorems toward full subdiscipline coverage
- Formal-verification backend (Lean/Coq) to machine-check discovered proof paths
- Richer impossibility-theorem pruner with more hard-prune rules
- Feed each solved problem's path back as new edges (self-improving loop)
- Benchmark suite of open problems with reproducible discovery runs

---

## Contributing

Contributions are welcome — issues and PRs both. Good first contributions:

- **Add nodes/edges** to the knowledge graph (new theorems, techniques, or connections)
- **Report a discovery run** — open an issue with the problem, flags used, and the path found
- **Improve the viewer** — interactions, performance, or visual encoding in `graph_viewer_3d.html`
- **Fix or extend the report** — corrections and citations in the chapter files

Please open an issue first for larger changes so we can align on direction. Use [GitHub Issues](https://github.com/ansumandas441/mathematical-discovery-engine/issues) for bugs and ideas, and [GitHub Discussions](https://github.com/ansumandas441/mathematical-discovery-engine/discussions) for open-ended questions.

---

## Citation

If you use this work in your research, please cite:

```bibtex
@software{das2026mathsdiscovery,
  author       = {Das, Ansuman},
  title        = {Mathematical Discovery Engine: Automated Theorem Discovery via Knowledge Graphs},
  year         = {2026},
  url          = {https://github.com/ansumandas441/mathematical-discovery-engine},
  note         = {ORCID: 0000-0001-9695-9408. Knowledge graph of 15,941
                  mathematical nodes and 26,614 edges with an
                  LLM-orchestrated proof search engine}
}
```

Or in prose:

> Ansuman Das, *Mathematical Discovery Engine: Automated Theorem Discovery via Knowledge Graphs*, 2026. Available at https://github.com/ansumandas441/mathematical-discovery-engine

---

## License

This project is licensed under the [MIT License](LICENSE).
