# Memorandum: Scope, Structure, and Extension Guide

## What this is

`/Users/primetrce/Documents/maths/` contains a ~72,000-word report titled *How Mathematics Was Discovered*. It covers ~100 major theorems in depth, plus ~300 more in a brief catalog, organized both chronologically (Chapters 1–6) and cross-sectionally by discovery technique (Chapter 9). The report is written from primary-source-informed history rather than a textbook's polished presentation, so it includes triggering events, documented reasoning, and the mathematical lineage of each result.

The report was built in two phases:

1. **Chronological narrative** — six era chapters plus an intro, abbreviated catalog, and epilogue. Each deep-dive theorem has a fixed template: Statement / Historical context / Trigger-motivation / Thought process / Lineage from prior math / Proof idea / Why it matters.
2. **Cross-cutting taxonomy** — Chapter 9 re-reads the same theorems as a playbook of techniques: 10 clusters, 28 named methods, 8 inheritance chains, a decision tree, and a list of permanent obstructions.

All theorems cited in Chapter 9 are real examples from Chapters 1–6 or the brief catalog. No theorems are introduced in Chapter 9 that aren't discussed elsewhere.

## File structure

```
/Users/primetrce/Documents/maths/
├── README.md                         — Cover, scope note, chapter table
├── INDEX.md                          — Cross-reference by mathematical area
├── 00_introduction.md                — "What is a theorem; how are theorems discovered"
├── 01_ancient.md                     — Prehistory through ~1400 CE (15 theorems)
├── 02_renaissance_17c.md             — 1400–1700 (17 theorems)
├── 03_eighteenth_century.md          — 1700–1800 (16 theorems)
├── 04_nineteenth_century.md          — 1800–1900 (22 theorems)
├── 05_early_twentieth_century.md     — 1900–1950 (18 theorems)
├── 06_modern_contemporary.md         — 1950–present (15 theorems)
├── 07_brief_catalog.md               — ~300 supplementary theorems, one line each
├── 08_epilogue.md                    — Cross-era patterns and reflections
├── 09_discovery_techniques.md        — Taxonomy of techniques (10 clusters + tree)
└── memorandum.md                     — This file
```

Chapters 1–6 share one template; Chapter 7 is a reference catalog; Chapter 8 is prose; Chapter 9 has its own template (signature + examples).

## Content & depth conventions

### Template for a deep-dive theorem (Chapters 1–6)

```markdown
### [Theorem name] (year, Discoverer)

**Statement:** [One or two sentences — actual content, accessible.]

**Historical context:** [The era, the broader project, who was working nearby.]

**The trigger / motivation:** [The specific problem, phenomenon, or failure that prompted the work.]

**Thought process:** [What we actually know from letters, papers, diaries. Flag legend vs. documented.]

**Lineage from prior math:** [What earlier work this built on.]

**Proof idea:** [The key technical move, in plain language.]

**Why it matters / what it enabled:** [Downstream impact.]
```

Length: typically 350–600 words per entry. The 19th-century chapter runs longer per entry (400–700 words) because of the density of results.

### Template for a technique (Chapter 9)

```markdown
#### N.k Technique name
**Signature:** *Input → Process → Output*

**Examples:**
- **Theorem** (Ch. X) — one-sentence description of how it used this technique. *Inherited: Y. Added: Z.*
- ...
```

Every theorem cited in Chapter 9 carries a parenthetical chapter reference (`Ch. 1`, `Ch. 7 catalog`, etc.) so readers can jump to the narrative treatment.

### Stylistic rules in force

- **Legend vs. documented.** Apocryphal stories (Archimedes' "Eureka!", Newton's apple, Galois's duel circumstances) are flagged as legend or marked with their source and century gap. Well-documented events (Wiles's 19 September 1994 fix; Gauss's diary entries; Galois's duel-eve manuscript with *"Je n'ai pas le temps"* in the margin) are told as history.
- **Primary sources over secondary.** Where possible, citations reference actual letters and published titles (e.g., Euler's 1734 letter to Daniel Bernoulli; Fermat's October 1640 letter to Frénicle).
- **Minimal hedging.** Dates and attributions are stated directly; scholarly uncertainty is noted when it affects the story (e.g., "Pythagoras' own contributions vs. his school's").
- **No prose about process.** Chapters are content, not meta-commentary about the writing.
- **Flat formatting.** Headings (`###`), bold **key terms**, occasional tables. No nested subsection numbering within a theorem entry. No admonition boxes.

### What the report deliberately omits

- **Exhaustive Wikipedia coverage.** Wikipedia's *List of theorems* catalogs ~400–500 named results; we deep-dive ~100 and brief-catalog ~300. Anything more would be shallow by necessity.
- **Full proofs.** Each "Proof idea" section sketches the key technique only. Readers wanting full proofs should consult textbooks.
- **20th-century applied math** (numerical analysis, optimization, statistics proper, numerical PDE): mostly represented only in the brief catalog. The report focuses on *theorems*, not methods.
- **Contemporary physics theorems** (CPT, spin-statistics, Bell, Kochen–Specker) appear only in the brief catalog. They could be deep-dived if the reader wants more mathematical physics.
- **Non-Western mathematics post-1500.** Islamic, Indian, Chinese traditions are well-represented in Chapter 1 but thin in later chapters, because the centers of gravity shifted — though modern Japanese (Iwasawa, Shimura, Taniyama, Itô, Mochizuki), Russian (Kolmogorov, Perelman, Zhang), Chinese (Chern, Yau), and Indian (Ramanujan, Bhargava) mathematicians are named where relevant.

## How to extend

### Add a theorem to an existing chapter

1. Identify the target chapter by date.
2. Write a new entry using the 7-field template. Target 400–600 words.
3. Insert in rough chronological order within the chapter (not strict — thematic neighbors sometimes trump strict chronology).
4. Add a one-line entry to `INDEX.md` under the appropriate mathematical-area section.
5. If the theorem illustrates a technique from Chapter 9, add it as a bullet under the relevant cluster.

### Add a new chapter

Unlikely to be needed for era coverage (1–6 already span prehistory to present) but reasonable for new cross-cutting perspectives. Example candidates:

- A chapter organizing the same theorems by **difficulty of original problem statement** — from "obvious once you see it" to "took three centuries to formulate the question."
- A chapter of **counterexamples and pathologies** that reshaped their fields (Weierstrass's nowhere-differentiable continuous function, Peano curve, Banach–Tarski, Volterra's example, Gromov's monster groups).
- A chapter on the **institutional sociology**: the Paris Academy, the Berlin school, Göttingen, the IAS, Bourbaki, Bletchley Park, Polymath.

Conventions: number sequentially (`10_...`), add to README table and INDEX, keep the established heading pattern.

### Add a technique cluster to Chapter 9

The 10 existing clusters are not exhaustive. Candidates for an 11th:

- **Probabilistic / random arguments** — Erdős probabilistic method, random matrix theory, probabilistic combinatorics.
- **Homological / derived / spectral sequence computations** — the heavy machinery of algebraic topology.
- **Model-theoretic transfer** — using non-standard analysis, ultraproducts, or elementary equivalence.
- **Motivic / cohomological bridges** in algebraic geometry.

Each new cluster should follow the pattern: unifying idea, 2–4 named techniques, signatures, 3–6 examples per technique with chapter references.

### Correct errors

Known sources of likely error:
- **Dates** of publication vs. submission vs. presentation can differ by years; the report usually gives publication year. If correcting, prefer the year the mathematics was *first communicated*, then note publication date if significantly later.
- **Attribution disputes** (Cayley–Hamilton, Cantor–Bernstein, Bunyakovsky–Schwarz, Cauchy–Bolzano) are generally resolved toward earliest verified priority with secondary attributions noted.
- **Legendary anecdotes** may have slipped through as though documented. If you find one, add a parenthetical flag: "(legend from [source], c. [later date])."

To correct: edit in place, then grep for other occurrences of the same claim and fix consistently.

### Change voice or audience

The current voice is: informed, dry-ish, willing to include detail, assumes the reader is curious but not yet a specialist. If retargeting:

- **For students**: add a glossary section, expand "Proof idea" fields, add exercises.
- **For researchers**: cut historical narrative, expand "Lineage" and "Why it matters," add references.
- **For general readers**: trim the proof ideas, expand the human stories, drop the brief catalog.

Each of these is a substantial rewrite, not a local edit.

## Known gaps and next steps

Items that would meaningfully improve the report and are not yet done:

1. **Proof-sketch rigor review.** Some "Proof idea" sections gloss over subtleties (e.g., Tychonoff → AC equivalence requires more than the sketch gives; Gödel's encoding assumes primitive-recursive representability). A pass by a logician / analyst would catch these.
2. **Consistency of em-dashes, symbol rendering.** The report uses Unicode mathematical symbols (ℕ, ℝ, ℂ, π, ζ, ≤). A render check in the target viewer (GitHub, Obsidian, Marked, etc.) should confirm these display correctly; if not, fall back to `\mathbb{N}` etc.
3. **Citations to specific passages.** The report names primary sources (letters, treatises) but doesn't supply page-level citations. For an academic version, add footnote-style references.
4. **The `08_epilogue.md` and `09_discovery_techniques.md` overlap.** The epilogue's "patterns of discovery" section is now partly superseded by Chapter 9. Either (a) trim the epilogue to pure reflection and cross-reference Chapter 9, or (b) leave both as intentionally overlapping from different angles.
5. **Mermaid / diagram rendering** for the decision tree and inheritance chains. Currently they are in indented prose. For a web-rendered version, converting to Mermaid flowcharts would improve navigability.
6. **Brief catalog expansion.** `07_brief_catalog.md` has ~300 entries but is still far short of Wikipedia's ~500. Extending to full coverage is mechanical but tedious. Prioritize: applied math, mathematical physics, differential equations, number theory reciprocity laws.
7. **Index by period AND area.** `INDEX.md` indexes by area only. A period-slicing view (e.g., "Everything proved in 1820–1850") would help readers tracking specific eras.

## Working with the report going forward

- **To add content**: edit the relevant chapter file directly. There is no build step.
- **To re-render**: any Markdown viewer works; GitHub and Obsidian render the Unicode math correctly.
- **To verify cross-references**: use `Grep` for the theorem name in the target chapter file. Every Chapter 9 citation should resolve; every INDEX.md entry should map to a real `###` heading.
- **If regenerating from scratch**: the chronological chapters were built in parallel via research subagents (one per era), then assembled. Chapter 9 was built after, using a single research-pass over the completed chapters. The research-pass approach is reproducible if a new perspective chapter is desired.

— end memorandum
