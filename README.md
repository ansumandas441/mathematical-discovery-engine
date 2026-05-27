# How Mathematics Was Discovered

## A report on the major theorems, their origins, and the minds that proved them

This report traces ~100 of the most consequential theorems in mathematics — from Pythagoras through Perelman — with the discovery context, motivation, and thought process behind each. It is organized chronologically so you can see how ideas beget ideas: how Fermat reading Diophantus triggered the 358-year saga of the Last Theorem; how Fourier's study of heat conduction forced mathematicians to re-examine what a function even *is*; how a duel-eve letter from a 20-year-old named Galois seeded an entire branch of algebra.

### Scope

Wikipedia's *List of theorems* catalogs roughly 400–500 named results across ~58 subdisciplines. This report does two things:

1. **Deep treatment** of ~100 pivotal theorems — statement, motivation, the triggering question or phenomenon, the discoverer's documented thought process, the mathematical lineage it built on, the proof idea, and its downstream impact.
2. **Brief catalog** of the remaining named theorems with one-line summaries, for reference.

### How to read this

- Each chapter covers an era. Read in order for the narrative arc, or jump by area using [`INDEX.md`](INDEX.md).
- Mathematical statements are given in accessible form first, then with formal notation where useful.
- Legendary anecdotes (Archimedes' "Eureka!", Newton's apple, Galois's duel) are flagged as such when the evidence is thin — but the best-documented ones are real and are told.

### Chapters

| | File | Era | Focus |
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
| 9 | [`09_discovery_techniques.md`](09_discovery_techniques.md) | cross-cutting | Taxonomy of discovery techniques: 10 clusters, inheritance chains, decision tree, impossibility warnings |
| 10 | [`10_toolbox.md`](10_toolbox.md) | cross-cutting | Structured toolbox: Mermaid tree of 57 techniques across 12 clusters, function-style dictionary, inheritance graph, decision flowchart, quick-reference table |
| 11 | [`11_knowledge_graph.md`](11_knowledge_graph.md) | cross-cutting | Bipartite directed knowledge graph: 752 nodes (115 axioms + 239 states + 336 theorems + 62 techniques), 1258 edges, 12 compound-technique subgraphs. JSON companion at `knowledge_graph.json` (~370 KB). Built over 2 iterations — iter 1 (63 landmark chains) + iter 2 (42 deep-dive completions + 229 brief-catalog skeletons covering all of chapters 01–07). |
| 12 | [`12_ai_solvable_discoveries.md`](12_ai_solvable_discoveries.md) | 2026 | Recently solved problems (Erdős #1196, #728, #397, #729) traced through the knowledge graph — every proof path was latent in the existing nodes and techniques. |
| 13 | [`13_workflow.md`](13_workflow.md) | cross-cutting | Automated theorem discovery workflow: orchestrator/worker LLM architecture, search tree over the knowledge graph (nodes = states, edges = techniques), pruning rules, worked example, implementation notes. |

### Discovery engine

`discovery_engine/` is a Python orchestrator that searches for proofs through the knowledge graph. It dispatches worker LLMs to apply techniques, prunes dead ends, and tracks a frontier of promising states.

#### Quick start

```bash
# Dry run (mock workers, no API cost)
python3 -m discovery_engine.discover --dry-run "Prove the Erdős primitive set conjecture"

# With Claude Code as worker (uses your subscription, no API key needed)
python3 -m discovery_engine.discover --use-cli \
    --start s_divisibility_definition,s_antichain_in_boolean_lattice \
    --goal "f(A) = sum 1/(a log a) is maximized when A is the set of primes" \
    "Erdős primitive set conjecture"

# With Claude API workers
export ANTHROPIC_API_KEY=sk-...
python3 -m discovery_engine.discover "Prove the Erdős primitive set conjecture"
```

#### Checkpointing and resume

Long runs save periodic checkpoints so you can stop and resume without losing progress. Ctrl+C triggers a graceful save before exiting.

```bash
# Run with auto-checkpointing (saves every 3 iterations)
python3 -m discovery_engine.discover --use-cli \
    --checkpoint-dir checkpoints --checkpoint-every 3 \
    --start s_divisibility_definition,s_antichain_in_boolean_lattice \
    --goal "For every c >= 0, the density f(c) of integers n for which (p_{n+1} - p_n)/log p_n < c exists and is a continuous function of c." \
    "Prime gap density continuity conjecture"

# Resume from last checkpoint
python3 -m discovery_engine.discover --use-cli \
    --resume checkpoints/checkpoint_latest.json \
    "ignored — problem is restored from checkpoint"
```

| Flag | Default | Description |
|---|---|---|
| `--checkpoint-dir <path>` | off | Directory for periodic checkpoint files |
| `--checkpoint-every N` | 5 | Save every N iterations |
| `--resume <path>` | — | Resume from a checkpoint JSON file |
| `--save-tree <path>` | — | Save final search tree to JSON (no resume support) |

#### Other flags

| Flag | Default | Description |
|---|---|---|
| `--dry-run` | — | Mock workers, zero API cost |
| `--use-cli` | — | Use `claude -p` subprocess as worker |
| `--llm-orchestrate` | — | LLM picks techniques + checks goal (more expensive) |
| `--start <ids>` | auto | Comma-separated start node IDs |
| `--goal <text>` | auto | Goal description |
| `--max-depth N` | 7 | Maximum search tree depth |
| `--max-iterations N` | 200 | Maximum search iterations |
| `--candidates N` | 4 | Techniques to try per step |
| `--workers N` | 2 (cli) / 5 (api) | Number of parallel workers |
| `--model <id>` | claude-sonnet-4-20250514 | Orchestrator model |
| `--worker-model <id>` | claude-haiku-4-5-20251001 | Worker model |

### Interactive viewer

`graph_viewer.html` renders the whole knowledge graph in a browser using vis-network (CDN). Filter by kind/cluster, search by name, click a node to see details, double-click a compound technique to open its subgraph, or use the "Subgraph browser" mode to navigate any of the 12 elaborations directly.

Launch with:

```bash
./serve_viewer.sh       # runs `python3 -m http.server 8765` and opens the viewer
```

or manually:

```bash
python3 -m http.server 8765
open http://localhost:8765/graph_viewer.html
```

Opening the HTML file directly (`file://`) will not work — `fetch()` of `knowledge_graph.json` is blocked by the browser's same-origin policy. The viewer shows a banner with the server command when this happens.

### A note on "how things are discovered"

Mathematical discovery rarely looks like the polished proof in a textbook. It usually begins with a puzzle, a pattern noticed, a physical question, an unsuccessful attempt by a predecessor, or a technical nuisance that refuses to go away. Where primary sources survive — Euler's letters, Gauss's diaries, Ramanujan's notebooks, Wiles's interviews — the real reasoning is visible and often strange. This report draws from those primary sources where possible.
