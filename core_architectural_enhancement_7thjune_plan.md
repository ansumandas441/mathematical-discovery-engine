# Core Architectural Enhancement Plan — 7 June

**Goal:** Evolve the `discovery_engine/` (orchestrator + child-LLM workers + tree search over the knowledge-graph techniques) from an *idea/route generator* into a system that can produce and **verify** rigorous proofs.

---

## 1. Current State — what already exists

The "orchestrator selects techniques, child LLMs try them as a tree search over all KG techniques" design is **already built**:

| Concept | Repo component |
|---|---|
| Orchestrator selects techniques | `orchestrator.py` — `select_techniques()` / `select_techniques_llm()` score & rank from the graph |
| Child LLMs try techniques | `worker.py` — `Worker` (Haiku API), `CLIWorker` (`claude -p`, subscription), `MockWorker`; one technique → one state, parallel via `ThreadPoolExecutor` |
| Tree search | `search_tree.py` — nodes = math states, edges = techniques, frontier-priority expansion, `--max-depth 7`, `--max-iterations 200` |
| "All techniques from the KG" | `knowledge_graph.json` = **15,941 nodes, 1,223 techniques**; `graph.techniques_from(node)` enumerates them |
| Pruning | `pruner.py` — kills 100%-impossible branches, demotes uncertain ones |
| Resumable scheduling | checkpoint every N iterations |

The plumbing is sound. The gaps below are about depth of reasoning and trustworthiness of results, not about the orchestration mechanism.

---

## 2. Gaps blocking real proof discovery

1. **Worker output capped at `max_tokens=1024`, compact JSON only** (`new_state_description`, `proof_sketch`, `confidence`). Designed for a *sketch/route*, not a finished argument.
2. **Default worker is Haiku** — too weak for multi-step rigorous bookkeeping (error terms, edge cases, careful estimates).
3. **No real verification.** `check_goal_mock` = keyword overlap; `check_goal` = LLM yes/no. No formal/adversarial check, so "goal reached" can be confidently wrong.
4. **No synthesis layer** that expands a successful technique path into a complete, rigorous write-up.

---

## 3. Enhancement Plan

### 3.1 Tiered worker models (priority: HIGH)
- Use **Opus** for synthesis-layer workers (`--worker-model` or `--use-cli` with Opus); keep Haiku only for cheap breadth/triage.
- Per-depth or per-confidence model policy: cheap model for early breadth, strong model when a branch's confidence crosses a threshold or nears the goal.

### 3.2 Raise worker output budget (priority: HIGH)
- Lift worker `max_tokens` from 1024 → ~8k so a child can write a genuine lemma with full bookkeeping.
- Add a dedicated **synthesis worker** that takes a successful technique *path* and expands it into a complete, rigorous result.

### 3.3 Add a verification / critic stage (priority: HIGHEST — biggest missing piece)
- Insert an adversarial verify step after `check_goal`: spawn N independent skeptics prompted to **refute** the claimed result; accept only if a majority fail to refute.
- Use distinct verification lenses (correctness, error-term/edge-case rigor, counterexample search) rather than N identical checks.
- Optional: route the final candidate to a formal checker (e.g. Lean) when available.

### 3.4 Technique-coverage audit (priority: MEDIUM)
- Periodically check that the techniques a target domain needs actually exist as nodes; the tree cannot traverse what isn't in the graph.
- Add missing techniques as KG nodes before runs that depend on them.

### 3.5 Consider the Workflow harness as an alternative orchestrator (priority: MEDIUM)
- Claude Code's `Workflow` tool is itself a deterministic orchestrator (fan-out, pipeline stages, adversarial-verify panels, loop-until-dry) with verification patterns built in.
- Candidate pattern, reusing `knowledge_graph.json`:
  `fan out over candidate techniques from the KG → child agents attempt each → adversarial verify → synthesize`.
- Same concept as `discovery_engine`, but verification is first-class. Decide whether to invest in the custom engine or migrate.

---

## 4. Suggested sequencing

1. Add verification/critic stage (3.3) — without it, nothing else is trustworthy.
2. Tiered models + raised token budget (3.1, 3.2) — makes synthesis actually possible.
3. Technique-coverage audit (3.4) — ensures viable routes exist in the graph.
4. Evaluate Workflow harness vs. custom engine (3.5) — pick one to invest in.

---

## 5. Realistic expectation

Even fully enhanced, this is best understood as a **route-finder + draft-generator + verifier**, not a fully autonomous prover. Creative gap-closing steps still benefit from strong-model reasoning and human review. The value: narrow 1,223 techniques to a promising path, draft the argument, and adversarially stress-test it before a human finalizes.
