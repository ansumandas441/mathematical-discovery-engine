# Iter-3 Agent Brief (read before drafting)

## Your job

You are one of ~13 parallel drafting agents expanding the mathematics knowledge graph at `/Users/primetrce/Documents/maths/`. You will be given **one domain** (e.g., Number Theory) and a **target count** (e.g., 90 theorems). You will:

1. Web-scour authoritative sources (Wikipedia "List of <domain> theorems", MathWorld, nLab, Princeton Companion references) to enumerate the canonical named theorems in your domain.
2. For each theorem, draft a **full 3–6-step derivation chain** in the deep-dive format below, using **only the 62 frozen toolbox techniques** from `TECHNIQUES.md` as edge labels.
3. Emit `drafts/area_<DOMAIN>_chains.md` (your output file — path will be given in your prompt).

## Hard constraints

- **No new techniques.** Use ids from `TECHNIQUES.md` only. If a theorem genuinely needs a process not on the list, mark that step `⚠ needs new technique` and continue.
- **Dedupe against existing graph.** Read `canonical_node_index.md` first. If a theorem already has an id there, **skip it** (do not re-derive) and note the skip in your output's preamble. Do not invent a duplicate id.
- **One `t_*` per step, snake_case `s_*` for all states.** Stable, descriptive snake_case ids.
- **Inline web citation** per theorem (one URL is fine — Wikipedia or MathWorld).
- **3–6 steps per chain.** Fewer is OK if the theorem is genuinely short (e.g., direct corollary). More than 6 should be rare.

## Output format (exact)

```markdown
# Area <DOMAIN> Derivation Chains (iter-3)

**Source pages:** <list 3–5 master URLs you scoured>
**Target:** <N> chains. **Drafted:** <M>. **Skipped (already in graph):** <K, with ids>.
**Flagged (`⚠ needs new technique`):** <count, with theorem names>.

---

### <Theorem name> (cite: <URL>)

**Axioms:** `s_axiom_one`, `s_axiom_two`
**Terminal:** `s_theorem_id` (kind: theorem)

**Steps:**
1. input: `⟨s_a, s_b⟩` --[t_technique_id {param: value}]--> output: `s_intermediate_state`
2. input: `s_intermediate_state` --[t_other_technique {param: value}]--> output: `s_theorem_id`

**Techniques used:** t_technique_id, t_other_technique

---

### <Next theorem> ...
```

## Style guide (lifted from iter-2 deep-dive entries)

- State ids are *mathematical objects*, not phrases. `s_finite_abelian_group`, `s_l2_function_on_torus`, `s_elliptic_curve_over_q`. Not `s_we_now_consider_X`.
- Parameter bindings on edges are concrete: `{group: SO(3)}`, `{dimension: n}`, `{field: ℝ}`, `{form: depressed_cubic}`. Avoid vague targets like `{step: "use Cauchy-Schwarz"}`.
- Compound techniques (`t_fourier_transform`, `t_svd_and_spectral_decomposition`, `t_galois_correspondence`, `t_wiles_modularity`, `t_godel_numbering`, `t_atiyah_singer_index_machinery`, `t_circle_method`, `t_selberg_sieve_method`, `t_ricci_flow_with_surgery`, `t_furstenberg_correspondence_principle`, `t_category_theoretic_colimits_and_adjoints`, `t_ergodic_correspondence`) are fine as atomic arrows when a theorem cites them whole; you don't need to expand the subgraph.
- For very short proofs, a 2-step chain is acceptable; prefer 3+ when possible.

## Tools you have

- `WebSearch` for finding source pages.
- `WebFetch` for reading a specific URL.
- `Read` for reading `canonical_node_index.md` and `TECHNIQUES.md`.
- `Write` for emitting your `drafts/area_<DOMAIN>_chains.md`.

## What you should NOT do

- Don't edit `knowledge_graph.json` directly. Integration is a separate round.
- Don't re-derive theorems already in `canonical_node_index.md`.
- Don't invent new techniques or new technique ids.
- Don't write proofs — write **discovery chains** (the high-level moves), not formal derivations.
- Don't try to web-fetch every theorem individually — scour the master list pages first, then verify selectively.

## Quality bar

A chain is acceptable if a competent mathematician reading it would say "yes, that's roughly how this theorem is discovered/proved, and these technique tags are the right ones." Hand-wave through technical lemmas; capture the structural moves.
