# Proof Verification and Completion Prompt

Use this prompt with Claude to rigorously work through the discovered proof path.

---

## Prompt

You are a research mathematician specializing in analytic number theory and probability. A computational discovery engine has found a candidate proof strategy for the following conjecture. Your job is to:

1. **Verify each step** — check if the mathematical reasoning is correct, identify any gaps or errors
2. **Fill in missing details** — provide rigorous proofs where the sketches are incomplete
3. **Assess the overall argument** — determine whether this constitutes a valid proof (possibly conditional on stated hypotheses)
4. **State clearly** what is proved unconditionally vs. what requires additional conjectures

### The Conjecture

For every $c \geq 0$, the density
$$f(c) = \lim_{N \to \infty} \frac{1}{N} \#\left\{ n \leq N : \frac{p_{n+1} - p_n}{\log p_n} < c \right\}$$
exists and is a continuous function of $c$.

### Discovered Proof Path (8 Steps)

The discovery engine found this path through a knowledge graph of mathematical techniques. Each step applies a named technique to transform the mathematical state. Confidence scores are the worker LLM's self-assessment (not formal verification).

---

**Step 0 — START (100%)**

The problem statement as given above.

---

**Step 1 — Axiomatize from Instances (55%)**

Define a "Cramér-class sequence" by axioms abstracted from the primes:
- **(C1)** Counting function: $A(x) \sim x/L(x)$ for slowly varying $L(x) \to \infty$
- **(C2)** Short-interval equidistribution: $A(x+h) - A(x) \sim h/L(x)$ for $L(x)^{1+\varepsilon} \leq h \leq x$
- **(C3)** Poisson occupancy: the count of elements in $[x, x + \lambda L(x)]$ converges in distribution to $\text{Poisson}(\lambda)$

**Claim:** For any Cramér-class sequence, the normalized gap density $f(c) = \lim_{N \to \infty} N^{-1} \#\{n \leq N : (a_{n+1} - a_n)/L(a_n) < c\}$ exists and equals $1 - e^{-c}$, which is continuous. The original conjecture reduces to verifying (C1)–(C3) for the primes with $L(x) = \log x$.

**Proof sketch:** Given (C3), gaps between consecutive elements in $[x, x+T]$ for large $T$ behave as inter-arrival times of a Poisson process with rate $1/L(x)$. Normalized by $L(x)$, these are i.i.d. $\text{Exp}(1)$. The Glivenko–Cantelli theorem then gives $f(c) = 1 - e^{-c}$ a.s.

**Formal:** A sequence $S = (a_n)$ is Cramér-class with scale $L$ if:
- $(C1)$ $\#\{a_n \leq x\} \sim x/L(x)$, $L$ slowly varying, $L \to \infty$
- $(C2)$ $\forall \varepsilon > 0$, $h \in [L(x)^{1+\varepsilon}, x] \implies \#\{a_n \in (x, x+h]\} \sim h/L(x)$
- $(C3)$ $\forall \lambda > 0$, $\#\{a_n \in [x, x + \lambda L(x)]\} \to^d \text{Poisson}(\lambda)$

**Theorem:** $S$ Cramér-class $\implies f_S(c) := \lim_{N \to \infty} N^{-1}|\{n \leq N : (a_{n+1} - a_n)/L(a_n) < c\}| = 1 - e^{-c}$ for all $c \geq 0$, and $f_S \in C^\infty([0, \infty))$.

---

**Step 2 — Structural Isomorphism (82%)**

Establish a categorical framework for locally-scaled point processes and show Cramér-class sequences are structurally isomorphic (in finite-dimensional distributions) to a rate-1 Poisson process.

**Key construction:** Define the category $\mathbf{PtProc}$:
- Objects: pairs $(S, L)$ of an increasing integer sequence $S$ and slowly varying scale $L$
- Morphisms: asymptotic equivalences of rescaled point measures

Axiom (C3) states precisely that the rescaled point measure $\mu_S^x = \sum_n \delta_{(a_n - x)/L(x)}$ converges in distribution to a Poisson point process $\Pi_1$ of unit rate.

**The gap CDF functor** $F: \mathbf{PtProc} \to \mathbf{CDF}$ sends $(S, L)$ to the limiting normalized gap distribution. It respects isomorphisms by the continuous mapping theorem applied to the gap functional $g(\mu) = \inf\{t > 0 : \mu((0, t]) \geq 1\}$, which is a.s. continuous w.r.t. $\Pi_1$.

Therefore $F(S, L) = F(\Pi_1) = 1 - e^{-c}$.

**Formal:** $\Phi: N_s \to (0,\infty)^\mathbb{N}$ defined by $\Phi(\sum_i \delta_{t_i}) = (t_1, t_2 - t_1, t_3 - t_2, \ldots)$ where $t_1 < t_2 < \ldots$ is a bimeasurable bijection with $\Phi_*(\Pi_1|_{N_s}) = \text{Exp}(1)^{\otimes \mathbb{N}}$.

---

**Step 3 — Reduce to Canonical Form (82%)**

Eliminate the categorical language. The "depressed" canonical form has three layers:

- **(D1) Density Normalization:** $\pi(x) \sim x/\log x$ ensures $L = \log x$ is the correct rescaling
- **(D2) Tail Control:** Short-interval estimate $\pi(x+h) - \pi(x) \sim h/\log x$ for $h \geq (\log x)^{1+\varepsilon}$ ensures no mass escapes
- **(D3) Poisson Convergence:** The rescaled point measure $\mu^x$ converges in f.d.d. to $\Pi_1$

The "functor" reduces to applying the continuous mapping theorem to $g(\mu) = \inf\{t > 0 : \mu((0,t]) \geq 1\}$. The conclusion $f(c) = e^{-c}$, $F(c) = 1 - e^{-c}$ follows by Poisson nearest-neighbor distribution computation.

---

**Step 4 — Second Canonical Reduction (93%)**

Further specialize to primes. The problem is now: verify three explicit conditions for $(p_n)$ with $L(x) = \log x$:

- **(D1)** $\pi(x) = x/\log x + O(x/\log^2 x)$ — **Prime Number Theorem, unconditional ✓**
- **(D2)** $\forall \varepsilon > 0$, uniformly for $h \in [(\log x)^{1+\varepsilon}, x]$: $\pi(x+h) - \pi(x) = \frac{h}{\log x}(1 + o(1))$ — **Known unconditionally for $h \geq x^{7/12+\varepsilon}$ (Huxley 1972). Conditional on RH for smaller $h$.**
- **(D3)** Joint Poisson convergence of prime counts in disjoint intervals of length $O(\log x)$ — **Gallagher 1976, conditional on Hardy–Littlewood $k$-tuple conjecture**

**Canonical Theorem (unconditional given D1–D3):** The gap functional $g$ is Borel measurable; $\Pi_1$-a.s. continuous (Poisson process has no atoms at fixed points); by (D3) + continuous mapping theorem, $g(\mu_S^x) \to^d g(\Pi_1) = \text{Exp}(1)$; by (D2), no mass escapes to $\infty$; combining: $\lim_{N \to \infty} N^{-1}|\{n \leq N : (p_{n+1} - p_n)/\log p_n < c\}| = 1 - e^{-c}$.

---

**Step 5 — Structural Isomorphism Upgrade (88%)**

The inter-arrival map $\Phi: \mathcal{N}_s \to (0, \infty)^\mathbb{N}$, sending a simple point measure $\mu = \sum \delta_{t_i}$ to the gap sequence $(t_1, t_2 - t_1, t_3 - t_2, \ldots)$, is a measurable isomorphism with:
- $\Phi_*\Pi_1 = \text{Exp}(1)^{\otimes \mathbb{N}}$ (Poisson inter-arrival theorem)
- $g = \pi_1 \circ \Phi$ (gap functional = first coordinate after isomorphism)
- So $g(\Pi_1) \sim \text{Exp}(1)$ is a tautology

This upgrades the result: (D3) gives convergence of the full point process $\mu_x \to^d \Pi_1$, which via $\Phi$ gives joint convergence of ALL normalized gaps $(G_1^x, \ldots, G_k^x) \to^d (E_1, \ldots, E_k)$ with $E_i$ i.i.d. $\text{Exp}(1)$, for every fixed $k$.

The one-dimensional marginal $f(c) = e^{-c}$ is a projection of this richer structure.

---

**Step 6 — Axiomatize from Instances (88%)** [truncated in logs]

The structural isomorphism form is axiomatized into an abstract framework.

---

**Step 7 — Final Structural Isomorphism (82%)** [truncated in logs]

The inter-arrival map $\Phi: \mathcal{N}_s \to (0, \infty)^\mathbb{N}$ is identified as the structural isomorphism completing the proof.

---

### Your Tasks

1. **Step-by-step verification:** For each step, state whether the mathematical claim is correct. If there is an error, identify it precisely.

2. **Gap analysis:** Identify any logical gaps between steps — places where the proof sketch hand-waves or assumes something non-trivial without justification.

3. **The key conditional dependencies:** This proof appears to be conditional on:
   - The Hardy–Littlewood $k$-tuple conjecture (for D3/Gallagher's theorem)
   - Possibly stronger short-interval estimates for (D2)
   
   Clarify exactly what is assumed vs. proved.

4. **Comparison with known results:** How does this proof strategy compare with the existing literature? Is this essentially Gallagher's 1976 argument repackaged, or does the axiomatization/categorical framework add something new?

5. **Verdict:** Is this a valid conditional proof? If not, what is the most serious flaw? If so, state the precise theorem that has been proved.

6. **Write the clean proof:** If the strategy is sound, write a clean, self-contained proof (without the discovery engine's technique labels) that could appear in a research paper.
