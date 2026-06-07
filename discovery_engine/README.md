# Discovery Engine

Automated theorem discovery via LLM-orchestrated search over the knowledge graph.

## Architecture

```
knowledge_graph.json (6,225 nodes, 62 techniques, 10,556 edges)
        │
        ▼
┌─────────────────┐     ┌──────────────────────────────┐
│  Orchestrator    │────▶│  Worker LLMs (Claude Haiku)  │
│  (Sonnet/Opus)   │◀────│  Prompt-cached system prompt  │
│                  │     └──────────────────────────────┘
│  search_tree.py  │     ┌──────────────┐
│                  │────▶│   Pruner     │
│                  │◀────│  (pruner.py) │
└─────────────────┘     └──────────────┘
        │
        ▼
   Search Tree (JSON) — nodes=states, edges=techniques
```

## Setup

```bash
pip install -r discovery_engine/requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
```

## Usage

### Dry run (no API cost, mock workers)

```bash
python -m discovery_engine --dry-run \
    --start s_divisibility_definition,s_antichain_in_boolean_lattice,s_fundamental_theorem_of_arithmetic \
    --goal "f(A) = sum 1/(a log a) is maximized when A is the set of primes" \
    "Prove the Erdős primitive set conjecture"
```

### Live run using Claude Code subscription (no API key needed)

```bash
python -m discovery_engine --use-cli \
    --start s_divisibility_definition,s_antichain_in_boolean_lattice \
    --goal "f(A) = sum 1/(a log a) is maximized when A is the set of primes" \
    "Prove the Erdős primitive set conjecture"
```

### Live run with API (Haiku workers, cheapest)

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python -m discovery_engine \
    --start s_divisibility_definition,s_antichain_in_boolean_lattice \
    --goal "f(A) = sum 1/(a log a) is maximized when A is the set of primes" \
    "Prove the Erdős primitive set conjecture"
```

### Live run with Sonnet workers (more capable, ~20x more expensive)

```bash
python -m discovery_engine \
    --worker-model claude-sonnet-4-20250514 \
    "Prove the Erdős primitive set conjecture"
```

### Full LLM orchestration (LLM picks techniques + checks goal)

```bash
python -m discovery_engine --llm-orchestrate \
    "Prove the Erdős primitive set conjecture"
```

### Wide exploration — level-by-level parallel BFS

Expand *every* node at a tree depth in parallel before descending to the next
depth. `--workers` is the total concurrency, shared across all nodes in the
level (so it fans out across *different states*, not just techniques of one
state):

```bash
python -m discovery_engine --use-cli --llm-orchestrate --level-parallel \
    --workers 6 \
    --goal "sum_{a in A} 1/(a log a) < 1 + o(1) for any primitive A in [x,inf)" \
    "Prove the Erdős primitive set 1+o(1) bound"
```

Each iteration is one full BFS wave; `--level-parallel` forces BFS ordering.
Interruptible/resumable: partially-expanded nodes resume first.

### Save and inspect the search tree

```bash
python -m discovery_engine --dry-run --save-tree output.json --print-tree \
    "Prove that every large even number is the sum of two primes"
```

## Options

| Flag | Default | Description |
|------|---------|-------------|
| `--dry-run` | off | Mock workers, no API calls |
| `--use-cli` | off | Use `claude -p` as worker (subscription, no API key) |
| `--llm-orchestrate` | off | LLM selects techniques and checks goal |
| `--start` | auto | Comma-separated start node IDs |
| `--goal` | auto | Goal description |
| `--graph` | auto-detect | Path to knowledge_graph.json |
| `--max-depth` | 7 | Max search tree depth |
| `--max-iterations` | 200 | Max search iterations |
| `--candidates` | 4 | Techniques to try per step |
| `--model` | claude-sonnet-4-20250514 | Claude model for orchestrator |
| `--worker-model` | claude-haiku-4-5-20251001 | Claude model for workers |
| `--save-tree` | none | Save search tree JSON |
| `--print-tree` | off | Print tree at end |
| `--quiet` | off | Suppress progress output |
| `--bfs` | off | Breadth-first (level-order) search instead of best-first priority search |
| `--level-parallel` | off | Strict level-by-level BFS: expand *every* node at a depth in parallel before descending. Spreads `--workers` across different nodes (forces BFS). |
| `--workers` | 6 (CLI) / 5 (API) | Max concurrent worker calls (total, shared across all nodes in a level) |
| `--runs-dir` | `<repo>/runs` | Where the problem registry + per-problem state live |
| `--restart` | off | Ignore saved state for this problem and start fresh |
| `--list-problems` | off | List every problem the engine has been given, then exit |
| `--inspect <id>` | none | Print the saved tree + per-level attempt ledger for a problem, then exit |

## Continuable runs (registry + resumable state)

Every problem you give is recorded in a **registry** (`runs/registry.json`) under a
stable id (hash of the problem + goal). Give the *same* problem again and the engine
recognizes it and **resumes from where it stopped** instead of starting over —
no flags needed.

```bash
# First run (Ctrl-C any time — state is saved)
python -m discovery_engine --use-cli --bfs "Prove <X>"

# Later: same command resumes automatically
python -m discovery_engine --use-cli --bfs "Prove <X>"

# See everything you've worked on
python -m discovery_engine --list-problems

# See exactly which techniques were tried at which level (and what was pruned)
python -m discovery_engine --inspect <problem-id>

# Throw away saved progress and start the problem fresh
python -m discovery_engine --restart "Prove <X>"
```

**What the state remembers.** Each search node keeps an *attempt ledger*: the ordered
candidate techniques chosen for it and, per technique, the outcome
(`child` / `pruned` / `impossible`). So on resume:

- **Untried techniques run first.** If level 1 was trying `[fourier, laplace]` and you
  interrupted after `fourier`, resume runs `laplace` before descending to level 2.
- **Dead directions stay dead.** A technique that returned `impossible` (or was pruned)
  is never retried.
- **BFS ordering is preserved** (`--bfs`): all techniques at one level before the next,
  with partially-expanded nodes re-queued at the front so they finish first.

Interrupt granularity is the worker window (`--workers`); use `--workers 1` for strict
one-technique-at-a-time resumption.

## Worker Modes

Three ways to run the workers — pick based on what you're paying for:

| Mode | Flag | Billing | Speed | API key? |
|------|------|---------|-------|----------|
| **CLI** | `--use-cli` | Claude Code subscription | ~5-10s/call | No |
| **API (Haiku)** | *(default)* | Anthropic API pay-per-token | ~1-2s/call | Yes |
| **API (Sonnet)** | `--worker-model claude-sonnet-4-20250514` | Anthropic API | ~2-4s/call | Yes |
| **Dry run** | `--dry-run` | Free | instant | No |

**If you have a Claude Code Max subscription**, use `--use-cli`. It calls
`claude -p "prompt"` as a subprocess — same billing as your terminal session,
no API key needed. Workers run up to 2 in parallel (adjustable to avoid rate limits).

**If you have an API key**, the default Haiku workers are cheapest (~$0.03 per
50 calls). Use `--worker-model` to upgrade individual runs to Sonnet.

## Token Optimizations

Three optimizations reduce API cost by ~85-95%:

### 1. Haiku workers (default) — ~20x cheaper per call

Workers apply a single technique to a single state — a focused task that
doesn't need Sonnet/Opus reasoning. Haiku handles it well at $0.25/MTok
input vs $3/MTok for Sonnet.

```
Workers:      Haiku  ($0.25/MTok in, $1.25/MTok out)
Orchestrator: Sonnet ($3/MTok in, $15/MTok out)  — only used with --llm-orchestrate
```

Override with `--worker-model claude-sonnet-4-20250514` for harder problems.

### 2. Prompt caching — ~90% savings on repeated system prompts

The worker system prompt is identical across all calls. By setting
`cache_control: {"type": "ephemeral"}`, the Anthropic API caches it for
5 minutes. After the first call:

- Cache write: 25% premium (once)
- Cache read:  90% discount (all subsequent calls within 5 min)

For a typical run with 40-100 worker calls, the system prompt (~150 tokens)
is cached after call #1 and read from cache for calls #2-100.

### 3. Shorter prompts — ~60% fewer input tokens per worker call

The worker user prompt was trimmed from ~600 tokens to ~200-400 tokens:
- 3 example inputs/outputs (was 5)
- 8 context nodes on one line (was 15 with bullets)
- No verbose instruction block (moved to system prompt)
- No technique ID or edge count details

### Combined savings estimate

| Scenario | Without optimizations | With optimizations | Savings |
|----------|----------------------|-------------------|---------|
| 50 worker calls (Sonnet, no cache, verbose) | ~$0.50 | — | — |
| 50 worker calls (Haiku, cached, trimmed) | — | ~$0.03 | **94%** |
| 200 worker calls + LLM orchestration | ~$3.00 | ~$0.25 | **92%** |

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

## How it works

1. **Parse problem** → identify start nodes in the knowledge graph
2. **Select techniques** → score candidates by proximity to goal, precondition match, bridge potential
3. **Dispatch workers** → each worker tries one technique on the current state via Claude API (Haiku default)
4. **Prune** → kill branches only if 100% impossible; demote uncertain ones
5. **Repeat** → expand the most promising frontier node
6. **Goal check** → LLM or heuristic decides if the goal is reached

See `13_workflow.md` for the full design document.
