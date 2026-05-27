# Improvements · Iteration 3 — Domain-by-Domain Expansion

Follow-up to iter-2 (commit `aa5b27f`, 336 theorems across chapters 01–07). Objective: expand the graph **beyond the chapter-01–07 corpus** to cover ~1000 additional canonical theorems across the modern mathematical landscape, with **full 3–6-step derivation chains** for every entry. Web-sourced (Wikipedia category trees, MathWorld, nLab, Princeton Companion, AMS MSC2020) and routed through the frozen 62-technique toolbox.

This is a scoped execution plan. It does **not** introduce new techniques to the toolbox (the C1–C12 clusters and 62 nodes are frozen at iter-2 state); it only adds *uses*. It does **not** tackle the schema extensions in `future_works.md` — those remain reserved for a future iteration.

---

## §1 Baseline (entering iter-3, commit `ee4088b`)

| Quantity | Value |
|---|---|
| Total theorem nodes | 336 |
| Total state nodes (axiom + state + theorem) | ~750 |
| Technique nodes | 62 (frozen) |
| Subgraphs | 12 |
| Top-level edges | ~1258 |
| Giant connected component | 97.6 % |

Corpus universe (currently in graph):
- Chapters 01–06 deep dives: ~105 theorems, all with 3–6-step chains.
- Chapter 07 brief catalog: ~231 theorems, with 1–2-step skeletons.

Iter-3 expands the universe to the **standard modern mathematics curriculum** — well beyond the chapter corpus.

---

## §2 Goal & non-goals

### Goal

After iter-3:

1. ~1000 additional named theorems modeled, each with a **full 3–6-step derivation chain** through the frozen 62-technique toolbox.
2. Domain coverage matches the AMS MSC2020 top-level classification (≥ 80 % of the major branches represented).
3. Every new theorem dedupes against `canonical_node_index.md` — no duplicate ids for already-present theorems (FLT, PNT, etc.).
4. Every new chain passes typed-correctness checks (technique input types match feeding states).
5. Giant connected component remains ≥ 95 % of total nodes.
6. `11_knowledge_graph.md` updated with new stats, new top-level Mermaid, and per-domain coverage table.
7. Web sources cited inline (Wikipedia / MathWorld / nLab URLs) on each new chain so future verification is cheap.

### Non-goals

1. **No new techniques.** If a theorem genuinely needs a process not in the 62-technique toolbox, flag it `⚠ needs new technique` and leave it for an iter-4 toolbox-expansion round. Don't invent ad-hoc techniques.
2. **No new schema fields.** Schema is frozen at iter-2; lifecycle / counterexample-first / Lakatos-loop extensions remain in `future_works.md`.
3. **No rewriting of existing chains.** Iter-2 chains are immutable. Iter-3 only appends.
4. **No proof reconstruction.** A 3–6-step chain is a *discovery* skeleton, not a proof. Skipping technical lemmas is fine if the high-level moves are right.
5. **No literature deep-dives.** First-pass web sourcing (Wikipedia + MathWorld + 1–2 authoritative survey links per entry) is enough. We are building an index, not a textbook.

---

## §3 Domain inventory (~12 domains, target ~80–100 theorems each)

| # | Domain | MSC2020 | Target | Sample flagship theorems |
|---|---|---|---|---|
| NT | Number Theory | 11 | 90 | Quadratic reciprocity*, Dirichlet on primes in AP, Roth's theorem, Mordell–Weil, Hasse–Minkowski, Faltings*, Mazur torsion, Vinogradov 3-primes |
| AL | Algebra & Galois | 12–20 | 90 | Sylow, Jordan–Hölder, Krull–Schmidt, Schreier, Wedderburn–Artin, Maschke, Burnside p^a q^b, Feit–Thompson, Frobenius reciprocity |
| AN | Real & Complex Analysis | 26–32 | 100 | Stone–Weierstrass, Arzelà–Ascoli, Baire category, Banach–Steinhaus, open mapping, Vitali covering, Lebesgue diff, Picard, Riemann mapping*, Hardy–Littlewood maximal |
| FA | Functional Analysis & Operators | 46–47 | 80 | Hahn–Banach*, Krein–Milman, Gelfand–Naimark, spectral theorem (bounded SA), Riesz representation, Lax–Milgram, Sobolev embedding, Atiyah–Singer* |
| TO | Topology | 54–55 | 90 | Tychonoff, Urysohn, Brouwer*, Borsuk–Ulam, Jordan curve, Poincaré duality, Whitehead, Hurewicz, Künneth, van Kampen, Smale h-cobordism |
| GE | Geometry (Diff/Alg/Riemannian) | 51–53 | 100 | Gauss–Bonnet*, Hopf–Rinow, Myers, Synge, Bonnet–Myers, Cheeger–Gromoll, Hironaka resolution, Mori cone, Kodaira embedding, Calabi–Yau |
| CO | Combinatorics & Graph Theory | 05 | 80 | Ramsey*, Erdős–Ko–Rado, Hall marriage, Menger, Dilworth, Turán, Szemerédi regularity, Erdős–Stone, Kővári–Sós–Turán, Robertson–Seymour* |
| LO | Logic & Foundations | 03 | 70 | Compactness*, Löwenheim–Skolem*, completeness, incompleteness*, MRDP*, Paris–Harrington*, forcing*, large-cardinal hierarchy, Borel determinacy* |
| PR | Probability & Stochastic | 60 | 80 | LLN strong & weak, CLT*, Lindeberg, Berry–Esseen, martingale convergence, Donsker invariance, Itô isometry, Girsanov, ergodic theorem*, large deviations |
| PD | ODE / PDE | 34–35 | 90 | Picard–Lindelöf, Peano, Cauchy–Kowalevskaya, Hille–Yosida, energy estimates, Hopf max principle, De Giorgi–Nash–Moser, Hörmander, Strichartz |
| DS | Dynamical Systems & Ergodic | 37 | 70 | Poincaré recurrence, KAM, Smale horseshoe, Sharkovskii, structural stability, Pesin, Oseledec, Furstenberg multiple recurrence, Margulis arithmeticity |
| MP | Mathematical Physics | 70–82 | 60 | Noether*, Stone–von Neumann, Wightman reconstruction, Reeh–Schlieder, Coleman–Mandula, index theorem*, Yang–Mills mass-gap (status), Verlinde formula |
| CS | Discrete Math & TCS | 03/68/94 | 60 | Cook–Levin, time-hierarchy, Savitch, PCP*, IP=PSPACE, Toda, Karp–Lipton, Lovász local lemma, Shannon coding, Reed–Solomon distance |

* = already in graph; new entries dedupe against `canonical_node_index.md`.

**Cumulative target:** 13 × ~80 = ~1040 theorems. Leaves slack for dedupes against existing 336.

---

## §4 Phased execution

Rounds are sequential at the round level; agents within a round run in parallel.

### Round 0 — Workspace prep
- Create `knowledge_graph_workspace_iter3/{drafts,checks,scripts}/`.
- Copy `canonical_node_index.md` from iter-2 (do not re-derive existing ids).
- Update `MEMORY.md` pointer if iter-2 ids are forgotten between agents.
- **Agents:** none (single Claude pass).
- **Output:** workspace tree.

### Round 1 — Domain target inventory (this doc, §3)
- Build the table above with realistic per-domain targets and named flagships.
- Web-sample 1–2 list pages per domain to verify the inventory is feasible.
- **Output:** §3 of this doc.

### Round 2 — Parallel domain drafting (the bulk of iter-3)
- **One subagent per domain (13 in parallel batches).** Each agent:
  1. WebSearch + WebFetch the canonical "List of <domain> theorems" Wikipedia page and the relevant MathWorld category.
  2. Enumerate ~80–100 named theorems for its domain, prioritizing curriculum/Princeton-Companion-style flagships.
  3. For each: draft a 3–6-step chain in the iter-1 deep-dive format (see iter-2 `mathematician_relationships.md`). Use **only the 62 frozen toolbox techniques** as edge labels. Reference `canonical_node_index.md` for already-present ids.
  4. Emit `drafts/area_<DOMAIN>_chains.md` (300–800 lines).
  5. Flag any theorem that doesn't fit the toolbox with `⚠ needs new technique`.
- **Quality bar:** every chain has Axioms / Terminal / Steps in the iter-1 format. Inline URL citation per theorem.
- **Effort:** ~1.5 k tokens of output per chain × 1000 chains ≈ 1.5 M tokens of agent output. This is the expensive round.

### Round 3 — Bulk integration into JSON
- `scripts/bulk_import_iter3.py`:
  1. Parse each `area_<DOMAIN>_chains.md`.
  2. Dedupe state ids against existing graph.
  3. Append theorem nodes, intermediate state nodes, and all input/output edges to `knowledge_graph.json`.
  4. Emit a `phase_c_iter3` metadata block with per-domain counts.
- **Output:** updated `knowledge_graph.json` (~750 KB → ~1.6 MB).

### Round 4 — Integrity checks
- Re-run `philosopher_typed_check.py` against the expanded JSON.
- Orphan audit; aim for zero new orphans (Type-A and Type-C must be fixed; Type-B "subgraph host" stubs are OK).
- Giant-component recompute; aim ≥ 95 %.

### Round 5 — Documentation + viewer perf
- Update `11_knowledge_graph.md`: stats block, per-domain coverage table, updated top-level Mermaid.
- Confirm `graph_viewer.html` still renders ≤ 5 s at ~1700 nodes (may need to add level-of-detail filtering).

---

## §5 Realism note

This is multi-conversation work. A single Claude session can realistically execute Rounds 0–2 for **a subset of the 13 domains** (perhaps 3–5 domains, ~250–400 chains) plus integration. Remaining domains will be staged across follow-up sessions, each one resuming from `knowledge_graph_workspace_iter3/drafts/` and updating the per-domain progress table at the end of this file.

| Domain | Drafted? | Integrated? | Conversation |
|---|---|---|---|
| NT | – | – | – |
| AL | – | – | – |
| AN | – | – | – |
| FA | – | – | – |
| TO | – | – | – |
| GE | – | – | – |
| CO | – | – | – |
| LO | – | – | – |
| PR | – | – | – |
| PD | – | – | – |
| DS | – | – | – |
| MP | – | – | – |
| CS | – | – | – |

(Updated after each round.)

---

## §6 What "complete" means after iter-3

A theorem is **canonical** in the modern mathematics curriculum if it appears in:
- The Princeton Companion to Mathematics index, OR
- The lead Wikipedia article for one of the AMS MSC2020 top-level branches, OR
- A standard graduate textbook in the corresponding domain (e.g., Hartshorne for AG, Hatcher for AT, Folland for analysis).

After iter-3, the graph should contain ≥ 80 % of canonical-by-this-definition theorems. Edge cases, niche subfields, and recent (post-2020) results may remain absent and become iter-4 fodder.
