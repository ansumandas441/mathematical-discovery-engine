# Team Charter — Toolbox Expansion

## Mission
Expand `/Users/primetrce/Documents/maths/10_toolbox.md` — currently 27 techniques across 10 clusters — with additional techniques and theorem examples drawn from **sources beyond Wikipedia**.

## Roles and file ownership

| Role | Agent name | Writes to (only) | Reads from |
|---|---|---|---|
| Math Intern A — historical & cross-cultural | `intern_a` | `intern_a_findings.md` | CHARTER, SCHEMA, `10_toolbox.md`, web |
| Math Intern B — modern & specialized | `intern_b` | `intern_b_findings.md` | CHARTER, SCHEMA, `10_toolbox.md`, web |
| Math Researcher (coordinator, validator) | `researcher` | `researcher_review.md` | CHARTER, SCHEMA, `10_toolbox.md`, both intern files, web |
| Computer Engineer (formalizer) | `engineer` | `engineer_additions.md` | CHARTER, SCHEMA, `10_toolbox.md`, `researcher_review.md` |

## Rules

1. **Single write target.** Each agent writes to exactly one file. Never edit another agent's file.
2. **Non-Wikipedia enrichment required.** Every finding must cite at least one source other than Wikipedia (MacTutor, Encyclopedia of Mathematics, nLab, Stacks Project, arXiv, primary texts, textbooks via URL).
3. **Only proved theorems.** No conjectures unless historically important as stated but unproven (e.g., Riemann Hypothesis) — in which case flag explicitly.
4. **Attribution honesty.** If attribution is disputed, note the dispute with both candidates and a brief reason.
5. **Schema compliance.** When proposing new *techniques* (not just new examples), follow the function-signature schema in `TOOLBOX_SCHEMA.md` exactly.
6. **No duplication.** Before proposing, check `10_toolbox.md`'s existing 27 techniques — your finding may be a new *example* of an existing technique, not a new technique.
7. **No web-paywall scraping.** Open references only.

## Workflow

```
Phase 1 (parallel):  intern_a  + intern_b   →  intern_a_findings.md, intern_b_findings.md
Phase 2:             researcher              →  researcher_review.md
Phase 3:             engineer                →  engineer_additions.md
Phase 4:             orchestrator integrates →  10_toolbox.md, commit, push
```

No back-and-forth between agents. If a finding is ambiguous, the researcher flags and the engineer skips. Re-runs are a separate invocation.

## Deliverable targets

- 30–50 new theorem examples distributed across existing techniques
- 10–20 new techniques formalized in schema
- 1–2 new clusters if merited by the research
