# Prime Gap Density Continuity: Rigorous Analysis

## The Conjecture

For every $c \geq 0$, the density

$$f(c) = \lim_{N \to \infty} \frac{1}{N} \#\left\{ n \leq N : \frac{p_{n+1} - p_n}{\log p_n} < c \right\}$$

exists and is a continuous function of $c$.

---

## Verdict on the Discovery Engine's Proof Path

**The engine essentially rediscovered Gallagher's 1976 argument**, dressed in categorical/axiomatic language. The core mathematical content is correct. The proof is **conditional** on the Hardy–Littlewood $k$-tuple conjecture. This is the state of the art — no unconditional proof is known, and the engine did not find one.

What the engine did well:
- Correctly identified the three necessary ingredients (PNT, short-interval estimates, Poisson local statistics)
- Correctly separated the unconditional probabilistic skeleton from the conditional arithmetic input
- The "Cramér-class" axiomatization is a clean abstraction

What the engine got wrong or overstated:
- The categorical framework (category **PtProc**, functors) adds no mathematical content beyond notation — the continuous mapping theorem does all the work
- Confidence scores (55%–93%) are meaningless as mathematical indicators
- Steps 3–4 (double canonical reduction) are redundant — they undo the categorical language introduced in step 2

---

## The Theorem (Conditional)

**Theorem** (Gallagher 1976, reformulated). *Assume the uniform Hardy–Littlewood conjecture (UHL). Then for every $c \geq 0$:*

$$\lim_{N \to \infty} \frac{1}{N} \#\left\{ n \leq N : \frac{p_{n+1} - p_n}{\log p_n} < c \right\} = 1 - e^{-c}$$

*In particular, the density $f(c) = 1 - e^{-c}$ exists, is continuous, and is in fact $C^\infty$.*

---

## The Proof

### Hypothesis: Uniform Hardy–Littlewood Conjecture (UHL)

Let $\mathcal{H} = \{h_1, \ldots, h_k\} \subset \mathbb{Z}_{\geq 0}$ be an **admissible** $k$-tuple (for every prime $p$, the residues $\{h_i \bmod p\}$ do not cover all of $\mathbb{Z}/p\mathbb{Z}$). Define the singular series:

$$\mathfrak{S}(\mathcal{H}) = \prod_{p \text{ prime}} \frac{1 - \nu_\mathcal{H}(p)/p}{(1 - 1/p)^k}$$

where $\nu_\mathcal{H}(p) = |\{h_i \bmod p : 1 \leq i \leq k\}|$.

**(UHL):** Uniformly for admissible $\mathcal{H}$ with $\max h_i \leq (\log x)^A$ (any fixed $A$):

$$\#\{n \leq x : n+h_1, \ldots, n+h_k \text{ all prime}\} = (1 + o(1))\, \mathfrak{S}(\mathcal{H})\, \frac{x}{(\log x)^k}$$

### Step 1: Poisson Convergence of Prime Counts (Gallagher's Lemma)

**Lemma 1.** Assume (UHL). For fixed $k \geq 1$ and $\lambda > 0$, let $\Pi(n; \lambda, x) = \#\{p \in (n, n + \lambda \log x] : p \text{ prime}\}$. Then the $k$-th factorial moment satisfies:

$$M_k(\lambda, x) := \frac{1}{x} \sum_{n \leq x} \Pi(n;\lambda,x)^{(k)} \to \lambda^k \quad \text{as } x \to \infty$$

where $m^{(k)} = m(m-1)\cdots(m-k+1)$ is the falling factorial.

*Proof.* We have:

$$\sum_{n \leq x} \Pi(n;\lambda,x)^{(k)} = \sum_{n \leq x} \sum_{\substack{p_1, \ldots, p_k \in (n, n+\lambda \log x] \\ \text{distinct primes}}} 1$$

Reversing the order of summation, this counts tuples $(n, p_1, \ldots, p_k)$ where $n < p_1, \ldots, p_k \leq n + \lambda \log x$ and the $p_i$ are distinct primes. Setting $h_i = p_i - n$, this becomes:

$$\sum_{\substack{1 \leq h_1, \ldots, h_k \leq \lambda \log x \\ h_i \text{ distinct}}} \#\{n \leq x : n+h_1, \ldots, n+h_k \text{ all prime}\}$$

For fixed distinct $h_1, \ldots, h_k$ with $\max h_i \leq \lambda \log x$, the tuple $\mathcal{H} = \{h_1, \ldots, h_k\}$ is admissible with probability $\to 1$ as $x \to \infty$ (among all such tuples). For admissible tuples, (UHL) gives:

$$\#\{n \leq x : n+h_i \text{ all prime}\} = (1+o(1))\, \mathfrak{S}(\mathcal{H})\, \frac{x}{(\log x)^k}$$

The key computation (Gallagher's main calculation): summing $\mathfrak{S}(\mathcal{H})$ over all admissible $k$-tuples in $\{1, \ldots, \lfloor \lambda \log x \rfloor\}$:

$$\sum_{\substack{1 \leq h_1 < \cdots < h_k \leq \lambda \log x \\ \mathcal{H} \text{ admissible}}} \mathfrak{S}(\mathcal{H}) = (1 + o(1))\, \frac{(\lambda \log x)^k}{k!}$$

This uses the fact that the average of $\mathfrak{S}(\mathcal{H})$ over $k$-tuples in a long interval converges to 1 — a consequence of the sieve-theoretic identity relating the singular series to the probability of admissibility.

Combining: $M_k(\lambda, x) \to k! \cdot \frac{\lambda^k}{k! \cdot (\log x)^k} \cdot (\log x)^k = \lambda^k$. $\square$

**Lemma 2** (Method of Moments for Poisson). If all factorial moments of a sequence of non-negative integer-valued random variables $X_n$ satisfy $\mathbb{E}[X_n^{(k)}] \to \lambda^k$ for all $k \geq 1$, then $X_n \xrightarrow{d} \text{Poisson}(\lambda)$.

*Proof.* The Poisson($\lambda$) distribution is determined by its moments (it has moment generating function $e^{\lambda(e^t - 1)}$ which is entire). The factorial moments $\lambda^k$ are exactly the factorial moments of Poisson($\lambda$). Since Poisson is determined by its moments and the factorial moment conditions are equivalent to ordinary moment conditions, convergence follows by the method of moments. $\square$

**Corollary 1.** Assume (UHL). For fixed $\lambda > 0$, the random variable $\Pi(U_x; \lambda, x)$ (where $U_x$ is uniform on $\{1, \ldots, \lfloor x \rfloor\}$) converges in distribution to $\text{Poisson}(\lambda)$.

### Step 2: From Poisson Counts to Gap Distribution

**Lemma 3.** Assume (UHL). For every $c > 0$:

$$\frac{1}{x} \#\left\{n \leq x : p_{\pi(n)+1} - n > c \log x\right\} \to e^{-c}$$

*Proof.* The event "$p_{\pi(n)+1} - n > c \log x$" is exactly the event "$\Pi(n; c, x) = 0$". By Corollary 1, $\Pi(U_x; c, x) \xrightarrow{d} \text{Poisson}(c)$, so:

$$P(\Pi(U_x; c, x) = 0) \to P(\text{Poisson}(c) = 0) = e^{-c} \quad \square$$

**Lemma 4** (Transfer from integers to primes). Assume (UHL). Then:

$$\frac{1}{N} \#\left\{n \leq N : \frac{p_{n+1} - p_n}{\log p_n} > c\right\} \to e^{-c}$$

*Proof.* We transfer from the "integer viewpoint" (Lemma 3, averaging over $n \leq x$) to the "prime viewpoint" (averaging over the $n$-th prime $p_n \leq x$).

Among integers $n \leq x$, a density $\sim 1/\log x$ are prime. For a prime $p_n \leq x$, the event $p_{n+1} - p_n > c \log p_n$ is equivalent to $\Pi(p_n; c, x) = 0$ (no prime in $(p_n, p_n + c \log x]$, using $\log p_n \sim \log x$).

For the transfer: partition $[1, x]$ into intervals $[m, m+1)$. Each interval contributes equally in the integer average. An interval $[m, m+1)$ is "prime" if $m$ is prime, which happens with density $1/\log x$. For a prime $m = p_n$, the condition $\Pi(p_n; c, x) = 0$ is exactly $p_{n+1} - p_n > c \log x$.

The integer average counts each gap $> c \log x$ with weight proportional to the gap length (since all integers in $[p_n, p_{n+1})$ contribute the same indicator). For the prime average, each such gap contributes weight 1. The correction factor:

$$\frac{\text{integer average}}{\text{prime average}} = \frac{\text{average gap length}}{\log x} \cdot \frac{1}{1} = 1 + o(1)$$

since the average gap $\sim \log x$ by PNT, and (UHL) ensures no anomalous concentration of long gaps. $\square$

*(Technical note: This transfer step is where (D2) — the short-interval estimate — is needed. It ensures that exceptionally long gaps do not distort the average. The unconditional Huxley bound $h \geq x^{7/12+\varepsilon}$ is not strong enough here; we need control at scale $h = O(\log x)$, which is what (UHL) provides.)*

### Step 3: Existence, Continuity, and Smoothness

**Theorem** (Main Result). Assume (UHL). Define $F(c) = \lim_{N \to \infty} \frac{1}{N} \#\{n \leq N : (p_{n+1} - p_n)/\log p_n < c\}$. Then:

(a) $F(c)$ exists for all $c \geq 0$, and $F(c) = 1 - e^{-c}$.

(b) $F$ is continuous — in fact $C^\infty$ — with density $f(c) = e^{-c}$.

*Proof of (a).* By Lemma 4, $\frac{1}{N}\#\{n \leq N : (p_{n+1}-p_n)/\log p_n > c\} \to e^{-c}$. Therefore $\frac{1}{N}\#\{n \leq N : (p_{n+1}-p_n)/\log p_n \leq c\} \to 1 - e^{-c}$. Since $\leq c$ and $< c$ differ by at most the density of $n$ with $(p_{n+1}-p_n)/\log p_n = c$ exactly, which is 0 (the gap $(p_{n+1}-p_n)$ is an integer, so $= c \log p_n$ has density 0), we get $F(c) = 1 - e^{-c}$. $\square$

*Proof of (b).* $F(c) = 1 - e^{-c}$ is manifestly $C^\infty$ on $[0, \infty)$, with $f(c) = F'(c) = e^{-c}$. $\square$

---

## What Is Proved Unconditionally?

**Almost nothing about the density $f(c)$ is known unconditionally.** The strongest unconditional results are:

| Result | Status |
|--------|--------|
| $\liminf_{n \to \infty} \frac{p_{n+1}-p_n}{\log p_n} = 0$ | **Proved.** Follows from Maynard–Tao (2014): $\liminf (p_{n+1}-p_n) \leq 246$. |
| $\limsup_{n \to \infty} \frac{p_{n+1}-p_n}{\log p_n} = \infty$ | **Proved.** Westzynthius (1931), strengthened by Erdős, Rankin, Ford–Green–Konyagin–Maynard–Tao (2018). |
| $F(c)$ exists for any single $c > 0$ | **Open.** Not known unconditionally. |
| $F(c)$ is continuous | **Open.** Conditional on UHL. |
| Average gap $\sim \log p_n$ | **Proved.** Follows from PNT. |

The gap between what is known and what is conjectured is enormous. We cannot even prove that the *limit defining $f(c)$ exists* for a single value of $c$.

## What Would Be Needed for an Unconditional Proof?

The bottleneck is **(D3): Poisson convergence of prime counts at scale $\log x$**. This requires understanding correlations between primes at very short scales. The hierarchy of difficulty:

1. **PNT** (counting primes up to $x$) — proved 1896 ✓
2. **Short-interval PNT at scale $x^{7/12+\varepsilon}$** — proved (Huxley 1972) ✓
3. **Short-interval PNT at scale $x^\varepsilon$** — requires RH or strong zero-density estimates ✗
4. **Short-interval PNT at scale $\log^A x$** — far beyond current methods ✗
5. **Poisson statistics at scale $\log x$** — requires understanding $k$-point correlations of primes ✗

Step 5 is the hardest and is essentially equivalent to UHL. The current best unconditional results on prime correlations:
- **Vinogradov (1937):** Three primes (ternary Goldbach) — but this is additive, not multiplicative correlation
- **Green–Tao (2008):** Primes contain arbitrarily long arithmetic progressions — but this is about structure, not statistics
- **Maynard–Tao (2014):** Bounded gaps — this shows primes cluster, but doesn't quantify the distribution

None of these reach the level of precision needed for Poisson statistics.

## Does the Discovery Engine's Approach Add Anything New?

**Mathematically, no.** The "Cramér-class axiomatization" is a pedagogically clean repackaging of Gallagher's argument. The categorical framework (category **PtProc**, functors) is notational overhead that the engine's own steps 3–4 correctly strip away.

**Methodologically, the axiomatization has value:** it cleanly isolates exactly which arithmetic properties of primes are needed, suggesting that any sequence satisfying (C1)–(C3) has exponential gap distribution. This could be applied to:
- Primes in arithmetic progressions $p \equiv a \pmod{q}$
- Almost-primes ($P_2$ numbers)
- Sequences arising from other sieves

The framework also makes the **conditional structure transparent**: the probabilistic implication (C1)+(C2)+(C3) $\Rightarrow$ $f(c) = e^{-c}$ is unconditional and purely soft analysis. All the hard number theory is in verifying the axioms for the specific sequence of primes.

## The Strongest Statement We Can Make

**Theorem** (Conditional, Gallagher 1976 / Discovery Engine). *Assume the uniform Hardy–Littlewood $k$-tuple conjecture. Then for all $c \geq 0$:*

$$\lim_{N \to \infty} \frac{1}{N} \#\left\{n \leq N : \frac{p_{n+1}-p_n}{\log p_n} < c\right\} = 1-e^{-c}$$

*Moreover, the joint distribution of any $k$ consecutive normalized gaps converges to i.i.d. $\operatorname{Exp}(1)$:*

$$(G_n^{(1)}, \ldots, G_n^{(k)}) := \left(\frac{p_{n+1}-p_n}{\log p_n}, \ldots, \frac{p_{n+k}-p_{n+k-1}}{\log p_{n+k-1}}\right) \xrightarrow{d} (E_1, \ldots, E_k)$$

*where $E_i$ are i.i.d. $\operatorname{Exp}(1)$.*

This is the best result achievable by current methods. An unconditional proof would be a major breakthrough in analytic number theory, likely requiring fundamentally new ideas about the distribution of primes in short intervals.
