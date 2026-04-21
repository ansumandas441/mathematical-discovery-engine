# 0. Introduction: What is a theorem, and how is one discovered?

## What counts as a theorem

A **theorem** is a statement proved from accepted starting points (axioms) and previously established results, using logical deduction. The term is Greek — *theorema*, "that which is viewed" — from the same root as *theater*. The Greeks regarded a theorem as something you could *see* to be true once the right arrangement of ideas was laid out before you.

The words **theorem**, **lemma**, **corollary**, **proposition**, and **postulate** have overlapping meanings:

- **Axiom / Postulate** — accepted without proof as a starting point. Euclid's postulates; Peano's axioms; the ZFC axioms.
- **Theorem** — a statement proved from axioms. Typically labeled "theorem" only for significant results.
- **Lemma** — a helper result used on the way to a theorem. Some lemmas become more famous than the theorems they were invented to prove (Zorn's, Itô's, Schwarz's).
- **Proposition** — a proved statement of lesser importance than a theorem.
- **Corollary** — a result that follows easily from a theorem.
- **Conjecture** — a stated but unproved claim. Famous conjectures (Riemann Hypothesis, P vs NP) drive whole fields.

These are editorial conventions. The Pythagorean theorem could be called a proposition; Schwarz's lemma could be called a theorem. What matters is that the statement has a valid proof.

## How theorems are actually discovered

From the historical record, a theorem typically arises in one of a handful of ways:

### 1. A practical problem forces the question
- **Egyptian rope-stretchers** needed right angles to re-mark fields after Nile floods; the 3-4-5 triangle and proto-Pythagorean reasoning followed.
- **Fourier** studied heat conduction in solids for Napoleon's artillery needs; the theory of Fourier series followed.
- **Turing** studied the Entscheidungsproblem — whether mathematics could be mechanized — and the theory of computation followed.

### 2. A paradox or unexpected failure demands a new framework
- **Russell's paradox** in naive set theory forced Zermelo's axiomatization and the rise of formal set theory.
- **Non-convergent Fourier series** and **pathological functions** (Weierstrass's nowhere-differentiable continuous function) forced 19th-century analysis to re-examine what "function" and "continuity" mean.
- **The Banach–Tarski paradox** (a ball split into 5 pieces and reassembled into two balls) forced mathematicians to confront the axiom of choice.

### 3. Generalization of a known result
- **Fermat's little theorem** → **Euler's totient theorem** (generalized to non-prime moduli) → **Lagrange's theorem in group theory** (generalized to arbitrary finite groups).
- **Green's theorem** in 2D → **Stokes' theorem** in 3D → **generalized Stokes' theorem** on manifolds of any dimension. One idea, successively abstracted.

### 4. Cross-pollination between fields
- **Analytic number theory** — complex analysis applied to prime numbers, yielding the Prime Number Theorem.
- **Algebraic topology** — algebraic tools applied to geometric shapes, yielding homology theory.
- **Modular forms** connected to elliptic curves — the Modularity Theorem, which plugged Fermat's Last Theorem.

### 5. Pattern noticed in data or examples
- **Gauss** computing prime counts in tables, noticing π(x) ≈ x/ln(x) — the Prime Number Theorem conjecture.
- **Ramanujan** filling notebooks with identities, many without proof, from experimentation.
- **The four color conjecture** arose from Francis Guthrie coloring a map of English counties.

### 6. A question asked purely for its own sake
- **Cantor** asked: are there different sizes of infinity? He found there are.
- **Hilbert** asked: can we mechanize mathematical reasoning? Gödel and Turing answered no.
- **Erdős and Ko** asked: how large can an intersecting family of sets be? — a question that opened extremal set theory.

## A note on thought process

The proofs you see in textbooks are cleaned-up presentations. They hide:

- False starts and wrong turns (Wiles had a gap in his 1993 FLT proof; he spent a year patching it).
- Competing approaches (Newton's fluxions vs. Leibniz's differentials: the same calculus, two notations, decades of bitter priority dispute).
- Philosophical resistance (Cantor's work on infinity was attacked by Kronecker as "corrupting youth"; Gödel's incompleteness was denied by Zermelo for years).
- Community effort across generations (Fermat stated FLT in 1637; it took 358 years and work by Kummer, Ribet, Frey, Wiles, Taylor, and hundreds of others to close).

The chapters that follow try to preserve this texture. When Gauss writes in his diary *"EUREKA! num = Δ + Δ + Δ"* — recording the day he proved every positive integer is the sum of at most three triangular numbers — you see a mathematician at the moment of discovery, not the cleaned-up proof that appeared years later. When Galois, the night before his duel, scribbles *"I have no time"* in the margin of his manuscript, you see the urgency that shaped what became Galois theory.

The history of mathematics is the history of specific humans, specific puzzles, specific moments of insight — and the slow, communal refinement that turns insight into rigor.
