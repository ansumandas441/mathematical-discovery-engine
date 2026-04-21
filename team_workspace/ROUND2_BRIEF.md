# Round 2 Brief — Gap-Targeted Expansion

## What changed from Round 1

Round 1 produced the current 35 techniques across 12 clusters. Round 2 targets **specific gap areas** identified as missing from the toolbox. Charter and schema rules are unchanged — see `CHARTER.md` and `TOOLBOX_SCHEMA.md`.

## File naming convention (round 2)

- `intern_a_findings_r2.md`
- `intern_b_findings_r2.md`
- `researcher_review_r2.md`
- `engineer_additions_r2.md`

Round-1 artifacts remain in place as reference.

## Gap assignments

### Intern A — Algebraic & Categorical gaps

Target areas (produce 1–3 distinct techniques per area, as merited):

1. **Representation theory as a discovery technique** — character theory (counting by traces); induction/restriction + Frobenius reciprocity; Peter–Weyl; branching rules; Schur–Weyl duality; Brauer induction.
2. **K-theory as a computational tool** — Bott periodicity; K₀ / Grothendieck group; K-theory long exact sequence; index as K-theoretic pushforward.
3. **Deformation theory as a standalone method** — Kuranishi family; obstruction classes in Ext²; Kodaira–Spencer; formal moduli problems.
4. **Higher category / ∞-category techniques** — replacing equality with coherent data; Dwyer–Kan localization; presentable ∞-categories; straightening–unstraightening.
5. **Topos theory / internal logic** — sheafification; Grothendieck topology; geometric morphisms as logical translations.
6. **Operad theory** — algebras over operads; Koszul duality of operads; little disks; recognition principles for loop spaces.
7. **Moduli-space methods** — Deligne–Mumford compactification; virtual fundamental class; Gromov–Witten / counting via moduli.

Target: **12–18 techniques-or-examples**. If a gap area yields only extra examples for an existing technique, note that explicitly.

### Intern B — Analytic & Geometric gaps

Target areas (produce 1–3 distinct techniques per area, as merited):

1. **Harmonic analysis decompositions beyond Fourier** — Littlewood–Paley / dyadic decomposition; wavelet multiresolution; Bourgain–Demeter decoupling; Bennett–Carbery–Tao multilinear Kakeya; Stein–Tomas restriction.
2. **Geometric flows beyond Ricci** — mean curvature flow (Huisken); harmonic map heat flow (Eells–Sampson); Yang–Mills flow (Donaldson); Kähler–Ricci flow.
3. **Microlocal analysis** — wavefront set; propagation of singularities; parametrix construction.
4. **Geometric measure theory** — currents (Federer–Fleming); varifolds; rectifiability; Plateau problem resolution.
5. **Variational methods** — direct method of calculus of variations; Ekeland variational principle; Palais–Smale minimax; Morse inequalities / mountain-pass.
6. **Sieve theory** — Brun's pure sieve; Selberg sieve; large sieve; Maynard multidimensional sieve.
7. **Circle method** (Hardy–Littlewood, as a standalone technique) — major-arc / minor-arc decomposition; exponential-sum bounds.
8. **Entropy method in combinatorics** — Shannon entropy as a counting tool; Shearer's inequality; Radhakrishnan-style bounds.
9. **Ergodic recurrence** — Furstenberg correspondence principle; multiple recurrence theorem; Szemerédi via ergodic theory.
10. **KAM / Nash–Moser** — small-divisor problems; rapidly convergent Newton iteration in Fréchet spaces.
11. **Geometric group theory** — quasi-isometry invariance (Gromov); Svarc–Milnor lemma; polynomial growth theorem.
12. **Symplectic / Floer homology** — Floer's Lagrangian intersection; symplectic action functional; pseudo-holomorphic curves.
13. **Tropical geometry** — tropicalization map; tropical curves; Viro's patchworking as a discovery technique.
14. **Random-structure universality** — Tracy–Widom universality (beyond GUE); SLE (Schramm–Loewner evolution); local eigenvalue statistics.

Target: **15–22 techniques-or-examples**. Quality over quantity; some areas will merit only one.

## Rules specific to round 2

1. **Avoid redundancy with round 1.** Before proposing any technique, grep `10_toolbox.md` for the name — if anything close exists, propose an example addition instead.
2. **Source diversity.** Prefer survey papers, textbooks (cited by URL if open), arXiv, nLab, Stacks Project, Encyclopedia of Mathematics. Wikipedia allowed as one source out of two minimum.
3. **Operational framing.** The toolbox is about verbs. If a "gap area" is really a field rather than a technique (e.g., "geometric measure theory"), extract the *technique* from it (e.g., "tangent measure analysis" or "currents as limits of polyhedral chains").
4. **Flag honestly.** If a gap area doesn't yield a genuine function-signature-shaped technique, say so.

## Deliverable targets (Round 2 total)

- ~25–35 new examples (distributed)
- ~10–15 new technique functions
- 0–2 additional clusters (unlikely; most gaps fit existing 12 or justify a Cluster 13)
