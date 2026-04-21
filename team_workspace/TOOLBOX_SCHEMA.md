# Toolbox Schema

All new **techniques** must conform to the schema below, matching the existing 27 in `10_toolbox.md`.

## Function-signature entry template

```markdown
#### `techniqueName(inputs) → outputs`
- **category:** Cluster N · short-tag (e.g., "experimental", "iteration", "topology")
- **preconds:** what must be true / what you must have to apply it
- **process:**
  1. Ordered step
  2. Ordered step
  3. Ordered step
- **postconds:** what is produced / guaranteed after applying
- **inherits:** other technique names this depends on (or —)
- **examples:** Theorem Name (chapter ref) — one-line note how this technique is used; *Inherited: X. Added: Y.* [add inherited/added clause only when illuminating]
```

## Naming conventions

- **camelCase** function name; verbs preferred (`spotPatternInTable`, `raiseDimension`, `diagonalize`).
- Arguments in parens describe *types* of input, not specific values.
- Return type short and descriptive (`→ conjecture`, `→ uniqueFixedPoint`, `→ invariantI`).

## Cluster conventions

Existing clusters (1–10):

1. Experimental & Numerical
2. Algebraic Manipulation
3. Symmetry & Invariants
4. Approximation & Limits
5. Abstraction & Axiomatization
6. Topology & Obstruction
7. Self-Reference & Impossibility
8. Iteration & Fixed Points
9. Cross-Field Transfer
10. Computer-Assisted & Collaborative

Proposing Cluster 11+: state the unifying idea in one sentence. Don't fragment the taxonomy unless genuinely warranted.

## Example existing technique (for reference)

```markdown
#### `contractionFixedPoint(T on complete space X) → uniqueFixedPoint`
- **category:** Cluster 8 · iteration
- **preconds:** complete metric space; self-map that strictly shrinks distances (d(Tx, Ty) ≤ k·d(x,y) with k < 1)
- **process:**
  1. Start with any x₀.
  2. Iterate xₙ₊₁ = T(xₙ).
  3. Sequence is Cauchy; converges by completeness.
  4. Limit is the unique fixed point.
- **postconds:** existence + uniqueness + constructive approximation
- **inherits:** —
- **examples:** Banach fixed-point theorem (Ch. 5); Picard–Lindelöf existence for ODEs (Ch. 7); Newton's method (classical); implicit function theorem; Nash equilibrium via Kakutani (Ch. 7)
```

## For new *examples* (not new techniques)

Simpler — just produce a line in the format:

```
**TechniqueName extension:**
- Theorem Name (year, discoverer) — one-line note on how it illustrates the technique; source: [MacTutor link / nLab link / etc.]
```

## Checklist the engineer will apply

- [ ] Name is camelCase verb-ish
- [ ] Category references an existing or newly-proposed cluster
- [ ] Preconds non-trivial (not "— ")
- [ ] Process has ≥ 3 ordered steps
- [ ] Postconds answer "what did I gain by doing this?"
- [ ] Inherits cites existing technique names verbatim
- [ ] At least 3 examples, each with chapter/source reference
