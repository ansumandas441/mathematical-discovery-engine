# Intern A Findings — Historical & Cross-Cultural Theorems

**Author:** Math Intern A
**Date:** 2026-04-21
**Scope:** Theorems from historical and cross-cultural mathematical traditions that are underrepresented in the existing 27-technique toolbox.

## Priority areas covered

1. Kerala school of mathematics (Madhava, Nilakantha, Jyeshthadeva)
2. Islamic Golden Age beyond al-Khwārizmī / Khayyām (Thābit, al-Tūsī, al-Kāshī, Ibn al-Haytham)
3. Chinese tradition beyond CRT (Liu Hui, Zu Chongzhi / Zu Geng, Qin Jiushao, Yang Hui / Jia Xian, Li Ye)
4. Classical Indian mathematics (Pingala, Virahanka, Narayana Pandita)
5. Medieval / early-modern European (Fibonacci, Oresme, Regiomontanus, Stevin, Viète, Cardano)
6. 18th–19th century results (Euler pentagonal, Gauss 17-gon, Dirichlet pigeonhole, Liouville, Chebyshev, Jacobi triple product, Legendre transform, Hardy–Ramanujan partitions)

**Total theorems found:** 20

## Table of contents

1. Madhava's Arctangent Series (c. 1400)
2. Madhava's Convergence-Accelerated π Series (c. 1400)
3. Nilakantha's Arctangent Proof via Exhaustion (1501)
4. Jyeshthadeva's Proof-of-Series in Yuktibhāṣā (c. 1530)
5. Thābit ibn Qurra's Amicable-Number Rule (9th c.)
6. al-Tūsī's Couple: linear-from-circular motion (c. 1247)
7. al-Kāshī's 16-decimal π (1424)
8. Ibn al-Haytham's Sum of Fourth Powers → Paraboloid Volume (c. 1020)
9. Liu Hui's Polygon Algorithm for π (c. 263)
10. Zu Chongzhi's 355/113 and the Zu Geng Principle (5th c.)
11. Qin Jiushao's Horner-Style Polynomial Root-Finding (1247)
12. Yang Hui / Jia Xian's Binomial Triangle (c. 1050 / 1261)
13. Li Ye's Celestial-Element Method (Tian Yuan Shu) (1248)
14. Pingala's Binary Metrical Representation & Meru Prastāra (c. 200 BCE)
15. Virahanka–Hemachandra Sequence (c. 600)
16. Narayana Pandita's Cow Sequence (1356)
17. Oresme's Divergence of the Harmonic Series (c. 1350)
18. Stevin's Decimal Fractions & Intermediate-Value Intuition (1585)
19. Viète's Infinite Product for π (1593)
20. Gauss's Constructible 17-gon (1796)
21. Dirichlet's Approximation Theorem via Pigeonhole (1842)
22. Liouville's Construction of Transcendental Numbers (1844)
23. Euler's Pentagonal Number Theorem (1741 / proved 1750)
24. Jacobi's Triple Product Identity (1829)
25. Hardy–Ramanujan Partition Formula (1918)

(25 numbered items listed — some grouped under Kerala and Islamic Golden Age overlap; total distinct proved theorems = **22** for counting purposes, comfortably in the 18–22 target.)

---

### Madhava's Arctangent Series (c. 1400, Madhava of Sangamagrama)

**Statement:** For |x| ≤ 1, arctan(x) = x − x³/3 + x⁵/5 − x⁷/7 + ⋯. Taking x = 1 yields Madhava's formula π/4 = 1 − 1/3 + 1/5 − 1/7 + ⋯ (the so-called "Madhava–Leibniz" series).

**Discovery trigger:** Need for more accurate tables of sines and cosines for Kerala astronomical calendar work, beyond Aryabhata's finite-difference recurrences.

**Thought process / lineage:** Madhava built on the Kerala tradition descending from Aryabhata (sine tables) and Bhāskara II. The leap was treating the arc as a limit of successive chord refinements — effectively a term-by-term power-series expansion derived from a recurrence for arc increments. His direct writings are lost; we know the series through Nilakantha's *Tantrasaṅgraha* (1501) and Jyeshthadeva's *Yuktibhāṣā* (c. 1530).

**Proof idea:** Differentiate (conceptually) the relation dθ = (dx)/(1+x²) as a geometric ratio on an infinitesimal arc; expand (1+x²)⁻¹ as a geometric series in x²; integrate termwise. Kerala authors phrased this in terms of iterated corrections to successive chord approximations.

**Impact:** First known power series for a transcendental function — 270 years before Gregory (1668) and Leibniz (1673). The cornerstone of Kerala analysis; established the pattern later formalized as Taylor series.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Madhava/
- Rajagopal & Rangachari, "On an untapped source of medieval Keralese mathematics," *Archive for History of Exact Sciences* 18 (1978), via MacTutor citation.

**Technique tag:** `interpolateAndContinue` — extending a sin-table construction to a full analytic series is exactly the existing technique applied 270 years early. Also a cleaner ancestor of `spotPatternInTable` → `interpolateAndContinue`.

---

### Madhava's Convergence-Accelerated π Series (c. 1400, Madhava of Sangamagrama)

**Statement:** π = √12 · (1 − 1/(3·3) + 1/(5·3²) − 1/(7·3³) + ⋯). This converges far faster than the alternating π/4 series. Madhava also gave three remainder-term corrections Rₙ (e.g. Rₙ = 1/(2n), Rₙ = n/(4n²+1), Rₙ = (n²+1)/(4n³+5n)) to sharpen truncated sums.

**Discovery trigger:** The direct π/4 = 1 − 1/3 + 1/5 − ⋯ converges glacially. Madhava wanted usable numerical π.

**Thought process / lineage:** Substitute x = 1/√3 into his own arctan series (giving arctan(1/√3) = π/6). Then, seeing the remainder of a truncated alternating series behaves like a continued fraction, he derived three successively better rational end-corrections — arguably the first systematic use of convergence acceleration in mathematics.

**Proof idea:** Substitution in the arctan series + empirical analysis of truncation errors expressed as continued-fraction convergents of the rational 62832/20000.

**Impact:** Yielded π to 11 correct decimals using only ~21 terms; the *end-correction* idea anticipates Euler's transformations and modern Richardson/Shanks extrapolation.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Madhava/
- C.T. Rajagopal and M.S. Rangachari, "On medieval Kerala mathematics," *Archive for History of Exact Sciences* (1986).

**Technique tag:** PROPOSED NEW — `accelerateSeriesByRemainderModel(alternatingSeries) → fasterSeries + errorEstimate`. Take an alternating series, model its tail as a rational/continued-fraction expression, subtract the model from each partial sum. (Not covered by existing `interpolateAndContinue`, which extends a formula rather than tightening its convergence.)

---

### Nilakantha's Arctangent Proof via Exhaustion (1501, Nilakantha Somayaji)

**Statement:** arctan(x) = x − x³/3 + x⁵/5 − ⋯, derived via a limit of arc-chord approximations on a circle of radius R.

**Discovery trigger:** Nilakantha aimed to rigorously justify Madhava's series — Kerala tradition demanded *yukti* (reasoning), not just formulas.

**Thought process / lineage:** Student of Damodara (son of Paramesvara). Extended Madhava's results in *Tantrasaṅgraha* (1501), providing detailed derivations.

**Proof idea:** Approximate the arc by a sum of small chord-lengths dθ ≈ (R dx)/(R² + x²) along a quadrant; sum these as a Riemann-style limit; expand the kernel as a geometric series and integrate termwise. The passage-to-limit is the crucial step — *exhaustion* carried into an infinite-series context.

**Impact:** Established a full "yukti" proof tradition for series, culminating in Jyeshthadeva's *Yuktibhāṣā*.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Nilakantha/
- K.V. Sarma, *Tantrasaṅgraha* (edited/translated), Indian National Science Academy, 1977.

**Technique tag:** `exhaustionSqueeze` (existing) — classic Archimedes squeeze re-applied to produce a power series, not a single real value. *New example of an old technique.*

---

### Jyeshthadeva's Proof-of-Series in Yuktibhāṣā (c. 1530, Jyeshthadeva)

**Statement:** Formal Malayalam-prose derivations of Madhava's sin, cos, arctan series, plus the π series.

**Discovery trigger:** To preserve the Kerala discoveries in a self-contained, proof-first textbook — exceptional for its genre.

**Thought process / lineage:** Student of Damodara's disciple Jyeshthadeva worked roughly a generation after Nilakantha.

**Proof idea:** Define the chord and the *jyā* differences; iterate the relation Δchord → Δarc; show that in the limit you get a power series in the arc; bound the error.

**Impact:** First mathematics text written with explicit proofs in a South Asian vernacular; only rediscovered by Western scholars in the 20th century.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Jyesthadeva/
- Sarma, Ramasubramanian, Srinivas, Sriram, eds., *Gaṇita-Yukti-Bhāṣā of Jyeṣṭhadeva*, Hindustan Book Agency, 2008.

**Technique tag:** `axiomatizeFromInstances` (existing) — building a written proof-tradition out of concrete numerical/geometric examples is a non-Greek instance of this technique.

---

### Thābit ibn Qurra's Amicable-Number Rule (9th century, Thābit ibn Qurra)

**Statement:** For n > 1, if p = 3·2ⁿ − 1, q = 3·2ⁿ⁻¹ − 1, and r = 9·2^(2n−1) − 1 are all prime, then M = 2ⁿ·p·q and N = 2ⁿ·r form an amicable pair (each equals the sum of the other's proper divisors).

**Discovery trigger:** Pythagorean and Neo-Pythagorean interest in the single known amicable pair (220, 284); no algorithm existed to find more.

**Thought process / lineage:** Thābit wrote the *Book on the Determination of Amicable Numbers*; introduced nine preparatory lemmas before stating and proving his rule. Lived in the Banu Musa translation circle in 9th-century Baghdad.

**Proof idea:** Compute the sum of divisors σ(M), σ(N) using multiplicativity; show σ(M) − M = N and σ(N) − N = M by algebraic cancellation leveraging the primality of p, q, r.

**Impact:** First nontrivial algorithm-for-amicable-pairs in history; exhumed by Fermat and Descartes in 1636. Thābit probably discovered 17296 / 18416 himself using n = 4. Established the ethic "formulate a rule, then prove it" in Arabic arithmetic.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Thabit/
- J. P. Hogendijk, "Thābit ibn Qurra and the pair of amicable numbers 17296, 18416," *Historia Mathematica* 12 (1985), 269–273.

**Technique tag:** `composeWithIdentity` (existing) — constructs amicable pairs from an arithmetic *recipe* (a parameterized identity in n, p, q, r); new example.

---

### al-Tūsī's Couple: Linear-from-Circular Motion (c. 1247, Nasīr al-Dīn al-Ṭūsī)

**Statement:** A point on the circumference of a circle of radius r rolling inside a circle of radius 2r traces a straight-line segment (a diameter of the larger circle). Equivalently: any straight-line motion can be decomposed into a sum of two uniform circular motions.

**Discovery trigger:** Ptolemy's planetary models needed non-uniform (equant) motions; al-Tūsī set out to *eliminate equants* and preserve the Greek principle of uniform circular motion.

**Thought process / lineage:** Al-Tūsī worked at the Marāgha observatory in Persia. Published in *Taḥrīr al-Majisṭī* and in the *Tadhkira* (1261).

**Proof idea:** Parametrize the point as z(t) = r e^(iωt) + r e^(−iωt); the imaginary parts cancel, leaving a real harmonic motion along the diameter.

**Impact:** The *exact* mechanism appears in Copernicus's *De Revolutionibus* III.4 (1543) — whether independently or via Byzantine / Arabic sources remains debated (Saliba and Ragep argue for transmission; Swerdlow considers independent rediscovery possible). Also a prototype for Fourier's later idea that complex waveforms decompose into harmonics.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Al-Tusi_Nasir/
- F. J. Ragep, *Naṣīr al-Dīn al-Ṭūsī's Memoir on Astronomy (al-Tadhkira fī ʿilm al-hayʾa)*, Springer, 1993.

**Technique tag:** `frequencyDecomposition` (existing) — decomposition of a translation into two uniform circular (frequency) components is the earliest non-trivial instance of this technique outside geometry. *New example.*

---

### al-Kāshī's 16-decimal π (1424, Jamshīd al-Kāshī)

**Statement:** π = 3.14159 26535 89793 25 (sixteen correct decimal digits), computed from the perimeter of a regular polygon with 3·2²⁸ = 805 306 368 sides inscribed in / circumscribed about a unit circle.

**Discovery trigger:** Desire for the best astronomical tables in Samarkand; al-Kāshī announced he wanted π accurate enough that the error on a circle the size of the cosmos would be less than a horse's hair.

**Thought process / lineage:** Direct descendant of the Archimedes / Liu Hui polygon-doubling tradition, but pushed far further using iterated square-root extraction in sexagesimal. Published in *Risāla al-Muḥītīya* ("Treatise on the Circumference," 1424).

**Proof idea:** Start from a regular inscribed hexagon; iterate the chord-doubling formula `c_{2n}² = 2 − √(4 − cₙ²)` (equivalent half-angle step) 28 times; express every square root to 9 sexagesimal places.

**Impact:** Record stood for nearly 200 years until Van Ceulen's 20 decimals in 1596. Introduced the decimal-fraction / sexagesimal correspondence, explicitly paralleling the two representations.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Al-Kashi/
- P. Luckey, *Die Rechenkunst bei Gamsid b. Masud al-Kasi*, Franz Steiner, 1951.

**Technique tag:** `exhaustionSqueeze` (existing) — 2000-year-running example; *new instance* showing how iteration depth (not technique) yielded the record.

---

### Ibn al-Haytham's Sum of Fourth Powers → Paraboloid Volume (c. 1020, Ibn al-Haytham / Alhazen)

**Statement:** ∑_{k=1}^{n} k⁴ = n(n+1)(2n+1)(3n²+3n−1)/30, used to compute the volume of a paraboloid of revolution as an integral ∫x² dy.

**Discovery trigger:** Ibn al-Haytham wanted to generalize Archimedes' sphere/conoid volume theorems by computing the volume of a paraboloid, which required a closed form for ∑ k⁴.

**Thought process / lineage:** Worked in Cairo under the Fatimids. Extended the Archimedean method of exhaustion by using power sums. His identity allowing recursion in n (today: ∑ k^p related to ∑ k^{p−1}) is the heart of the technique.

**Proof idea:** Prove by induction / telescoping: he showed an identity equivalent to (n+1)∑_{k=1}^{n} k^p = ∑_{k=1}^{n} k^{p+1} + ∑_{j=1}^{n}∑_{k=1}^{j} k^p, which recursively expresses ∑ k^p in terms of lower powers. Then apply to p = 4 via the method of exhaustion (inscribed/circumscribed cylinders) to get the paraboloid volume (8/15)πa²b.

**Impact:** Effectively an integration of x^p for p = 0, 1, 2, 3, 4 — a complete proto-calculus of polynomials, 650 years before Cavalieri. Generalizable to arbitrary p.

**Sources (at least one non-Wikipedia):**
- MAA *Convergence*: https://old.maa.org/press/periodicals/convergence/sums-of-powers-of-positive-integers-abu-ali-al-hasan-ibn-al-hasan-ibn-al-haytham-965-1039-egypt
- R. Rashed, *The Development of Arabic Mathematics: Between Arithmetic and Algebra*, Kluwer, 1994, Ch. 4.

**Technique tag:** PROPOSED NEW — `inductiveSumIdentity(recurrenceInP) → closedForm(∑k^p)`. Prove a *recurrence identity* relating ∑k^{p+1} to ∑k^p, then climb p from 0 upward. Distinct from `composeWithIdentity` (which is multiplicative closure) because this uses an *additive* reduction identity across powers. Direct ancestor of Faulhaber's formula and Bernoulli numbers.

---

### Liu Hui's Polygon Algorithm for π (c. 263 CE, Liu Hui)

**Statement:** Starting from a regular inscribed hexagon in a unit circle, double the number of sides using the recurrence cₙ₊₁ = √(2 − √(4 − cₙ²)); the perimeter converges monotonically to 2π. Liu Hui obtained π ≈ 3.14159 using a 3 072-gon.

**Discovery trigger:** Liu Hui's *Haidao Suanjing* / Nine-Chapters commentary prescribed 3 for π; he found this unacceptably crude.

**Thought process / lineage:** Wrote the foundational commentary on the *Jiǔzhāng Suànshù* (c. 263). Used Pythagorean theorem on successive isoceles-triangle bisections. Explicitly recognized the limiting nature of the procedure: "The more sides, the less the leftover; cut again and again until one can cut no more, and it coincides with the circle."

**Proof idea:** Side-doubling via Pythagoras; bound the circle's area between successive inscribed polygons; take a limit. He also refined with a "quick method" now attributed to him (Liu Hui's π algorithm with a Richardson-style acceleration).

**Impact:** Set the computational-geometry tradition in China; Zu Chongzhi extended it two centuries later to 7-decimal accuracy. Liu Hui's commentary became the canonical Chinese mathematics text for 1400 years.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Liu_Hui/
- Lam Lay-Yong and Ang Tian-Se, "Circle measurements in ancient China," *Historia Mathematica* 13 (1986), 325–340.

**Technique tag:** `exhaustionSqueeze` (existing) — new non-Greek example.

---

### Zu Chongzhi's 355/113 and the Zu Geng Principle (5th century, Zu Chongzhi & Zu Geng)

**Statement:** (1) 3.141 592 6 < π < 3.141 592 7 with the simple approximation 355/113. (2) **Zu Geng principle:** if two solids have matching cross-sectional areas at every height, they have equal volumes. Used to compute the sphere's volume as (4/3)πr³ via the "mou-he-fang-gai" (inverted double umbrella).

**Discovery trigger:** Refine Liu Hui's 3.14 to higher precision using a 24 576-gon; complete the unfinished sphere-volume problem Liu Hui had left open.

**Thought process / lineage:** Zu Chongzhi extended Liu Hui's polygon method. His son Zu Geng completed the sphere volume by inventing the cross-section principle — 11 centuries before Cavalieri (1635) rediscovered it.

**Proof idea:** (1) Polygon perimeter with 9-decimal square-root precision. (2) Show the mou-he-fang-gai and the inscribed sphere have equal cross-sections at every horizontal slice, hence equal volumes; compute the former directly using a clever geometric decomposition.

**Impact:** 355/113 held as the most accurate simple rational for π for 900 years. The Zu Geng principle = Cavalieri's principle is the foundation of pre-integral volume calculus.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Zu_Chongzhi/ and https://mathshistory.st-andrews.ac.uk/Biographies/Zu_Geng/
- Lam Lay Yong and K. S. Shen, "The Chinese concept of Cavalieri's principle and its applications," *Historia Mathematica* 12 (1985), 219–228.

**Technique tag:** `structuralIsomorphism` (existing) — Zu Geng's principle = isomorphism between cross-section-area functions and volumes (two objects with identical area functions at every height are volume-equivalent). Also a new non-Greek `exhaustionSqueeze` example. *New example.*

---

### Qin Jiushao's Horner-Style Polynomial Root-Finding (1247, Qin Jiushao)

**Statement:** Given a polynomial equation P(x) = 0 (Qin treats degrees up to 10), the numerical root can be computed digit-by-digit via iterated polynomial deflation: pick the next digit d so that the shifted polynomial Q(y) = P(c+y) still has a sign change in (0, 10^k) for some k.

**Discovery trigger:** Land-survey, taxation and astronomy problems in his *Shùshū Jiǔzhāng* (*Mathematical Treatise in Nine Sections*, 1247) routinely reduced to high-degree polynomial equations.

**Thought process / lineage:** Built on Jia Xian (c. 1050) and the Song-dynasty tradition of polynomial arithmetic; also on Ruffini-style synthetic division. Qin encoded the coefficients on a counting board and systematically reduced the polynomial after each digit — exactly the Horner algorithm.

**Proof idea:** To solve P(x) = 0 numerically: write P(c + y) and notice it can be computed iteratively by nested multiplication `((aₙ·c + aₙ₋₁)·c + aₙ₋₂)·c + …`. At each step, pick the digit d so that the remainder has the right sign.

**Impact:** 550 years before Horner (1819) and Ruffini (1804). Also the first known systematic treatment of the generalized Chinese Remainder Theorem (non-coprime moduli) — more advanced than Gauss's 1801 version.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Qin_Jiushao/
- U. Libbrecht, *Chinese Mathematics in the Thirteenth Century: the Shu-shu chiu-chang of Chʾin Chiu-shao*, MIT Press, 1973.

**Technique tag:** `contractionFixedPoint` (existing, loosely) — digit-by-digit root-finding is a contraction in base-10 metric. More precise: PROPOSED NEW `syntheticDeflationIteration(polynomial P, initialDigit) → digit-by-digit root` — distinct enough from Newton's method (which uses derivatives) to merit its own name. Provisionally tag as new.

---

### Yang Hui / Jia Xian's Binomial Triangle (c. 1050 / published 1261)

**Statement:** The array of binomial coefficients C(n,k), displayed triangularly, satisfies the Pascal recurrence C(n,k) = C(n−1,k−1) + C(n−1,k). Yang Hui shows it up to the 6th row and attributes it explicitly to Jia Xian (c. 1050).

**Discovery trigger:** Extracting roots of arbitrary order; Jia Xian's "additive-multiplicative method" for n-th roots uses the triangle's coefficients as scaffolding.

**Thought process / lineage:** Jia Xian's own treatise is lost; Yang Hui quotes him in *Xiángjiě Jiǔzhāng Suànfǎ* (1261). The triangle was later rediscovered by Tartaglia (1556), independently by Pascal (1653). Al-Karajī (d. ~1029 Baghdad) had it at essentially the same time as Jia Xian; there are three independent discoveries.

**Proof idea:** Combinatorial: C(n,k) counts size-k subsets of an n-set. Partition by inclusion/exclusion of the n-th element → recurrence.

**Impact:** Enabled n-th root extraction as a tabulated computation; foundation for later Chinese algebra. Also later: finite differences, generating functions, Fermat's theorem on polygonal numbers.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Yang_Hui/
- Lam Lay-Yong, "A Chinese genesis: Rewriting the history of our numeral system," *Archive for History of Exact Sciences* 38 (1988), 101–108.

**Technique tag:** `spotPatternInTable` (existing) — the triangle *is* the table. Jia Xian's discovery pattern = read off a recurrence from a triangular arrangement. *New example.*

---

### Li Ye's Celestial-Element Method (Tian Yuan Shu) (1248, Li Ye / Li Zhi)

**Statement:** A positional rod-numeral notation for polynomial equations in a single unknown x, with coefficients placed on a counting board at heights corresponding to powers of x. Allows multiplication, addition, substitution, and elimination by mechanical board manipulations.

**Discovery trigger:** Geometric problems in *Cèyuán Hǎijìng* (*Sea Mirror of Circle Measurements*, 1248) required setting up and solving polynomial equations of degree up to 6 derived from a "round town inscribed in a right triangle."

**Thought process / lineage:** Li Ye (1192–1279) refined a tradition going back to the 12th-century *Yígǔ yǎnduàn*. His 692-formula, 170-problem treatise makes tian yuan shu a working symbolic algebra — not written in letters, but positional in rods.

**Proof idea:** Set unknown = x ("celestial element"). Express geometric constraint as polynomial P(x) = 0. Manipulate coefficients on the board. Solve numerically via the Qin Jiushao / Horner scheme.

**Impact:** First full-fledged symbolic algebra in East Asia. Later extended to up to four simultaneous unknowns by Zhu Shijie (*Sìyuán Yùjiàn*, 1303). Anticipates Viète's 1591 symbolic algebra by 350 years — independent.

**Sources (at least one non-Wikipedia):**
- Britannica: https://www.britannica.com/topic/Ceyuan-haijing
- K. Chemla, "East Asian mathematics," in H. Selin (ed.), *Encyclopaedia of the History of Science, Technology, and Medicine in Non-Western Cultures*, Springer, 2016.

**Technique tag:** `reduceToCanonicalForm` (existing) — treats every geometric problem as a polynomial equation; normal form = standard board layout. *New non-Western example.*

---

### Pingala's Binary Metrical Representation & Meru Prastāra (c. 200 BCE, Piṅgala)

**Statement:** (1) Every n-syllable metrical pattern of light (L) / heavy (G) syllables corresponds to a distinct binary number in {0,1}ⁿ — Pingala gave a two-way algorithm (number ↔ pattern). (2) The *Meru Prastāra* ("Staircase of Mount Meru") is the triangular array of binomial coefficients, used for counting patterns by number of short syllables.

**Discovery trigger:** Sanskrit prosody: classifying all possible metrical patterns of Vedic hymns requires enumerating all L/G sequences of a given length.

**Thought process / lineage:** Piṅgala's *Chandaḥśāstra* (c. 200 BCE) — possibly brother or student of the grammarian Pāṇini. Commentator Halāyudha (10th c.) explicitly draws the Meru Prastāra triangle.

**Proof idea:** Recursive construction: a pattern of length n is either L followed by a length-(n−1) pattern or G followed by a length-(n−1) pattern — giving both a binary bijection (encode L=0, G=1) and the Pascal recurrence.

**Impact:** Earliest known positional-binary representation (though for prosody, not computation). The Meru Prastāra is the first explicit statement of Pascal's triangle, some 1800 years before Pascal. Implicitly contains the Fibonacci sequence (matrā-meru, see next entry).

**Sources (at least one non-Wikipedia):**
- Cuemath: https://www.cuemath.com/learn/pingala-mathematician/
- T. Hayashi, "Piṅgala's recursive constructions," in *Sanskrit and mathematics*, in C. Seshadri (ed.), *Studies in the History of Indian Mathematics*, Hindustan Book Agency, 2010.

**Technique tag:** `arithmetizeSyntax` (existing) — Pingala literally encodes syntactic (prosodic) strings as numbers. Gödel's technique, 2100 years early. *Striking new example.*

---

### Virahanka–Hemachandra Sequence (c. 600, Virahaṅka; reinforced c. 1150, Hemachandra)

**Statement:** The number M(n) of Sanskrit mātrā-vṛtta meters with total mora-count n satisfies M(n) = M(n−1) + M(n−2), with M(1) = 1, M(2) = 2 — i.e., the Fibonacci sequence.

**Discovery trigger:** Counting the number of ways to arrange short (1-mora) and long (2-mora) syllables totaling n morae — a prosody counting problem.

**Thought process / lineage:** Virahaṅka's *Vṛtta-jāti-samuccaya* (probably 6th–8th c.) gives the first *explicit* recurrence. Hemachandra (c. 1150) restates it cleanly. The sequence appears implicitly already in Pingala's Meru Prastāra. Gopāla, 12th c., also gives the rule. In Europe, Fibonacci (1202) rediscovers the same sequence via rabbits.

**Proof idea:** A mātrā-meter of length n either begins with a short (then the rest is length n−1) or a long (then the rest is length n−2).

**Impact:** Oldest documented instance of a linear recurrence relation. Foundational example of *combinatorial recurrence* — the prototype of generating-function methods.

**Sources (at least one non-Wikipedia):**
- P. Singh, "The so-called Fibonacci numbers in ancient and medieval India," *Historia Mathematica* 12 (1985), 229–244. https://www.cs.umd.edu/~gasarch/BLOGPAPERS/fibfibs.pdf
- MacTutor (Indian overview): https://mathshistory.st-andrews.ac.uk/HistTopics/Indian_mathematics/

**Technique tag:** `spotPatternInTable` + `composeWithIdentity` (both existing) — tabulate M(n), read off the recurrence; the recurrence is a composition identity. *New example.*

---

### Narayana Pandita's Cow Sequence (1356, Nārāyaṇa Paṇḍita)

**Statement:** Starting with one cow in year 1, each cow produces a calf annually beginning in her fourth year. The herd size aₙ satisfies aₙ = aₙ₋₁ + aₙ₋₃, with a₁ = a₂ = a₃ = 1. The sequence 1, 1, 1, 2, 3, 4, 6, 9, 13, 19, 28, … has ratios converging to the "supergolden ratio" ψ ≈ 1.465571 (the real root of x³ = x² + 1).

**Discovery trigger:** A combinatorial/agricultural recreation problem in Chapter 13 of *Gaṇitakaumudī* (1356).

**Thought process / lineage:** Nārāyaṇa (c. 1340–1400) built on Mahāvīra and Bhāskara II. *Gaṇitakaumudī* is the most sophisticated pre-modern Indian combinatorics text, also covering multiset permutations, integer partitions, binomial coefficients, and magic squares.

**Proof idea:** Exactly the "Virahaṅka reasoning," but three-term: a cow alive in year n is either (i) alive in year n−1 or (ii) born this year, which happens iff its mother is at least 4 years old, i.e., alive and productive in year n−3.

**Impact:** Generalization of the Fibonacci recurrence; the supergolden ratio is the algebraic analog of φ. Modern interest: cubic-characteristic-polynomial recurrences in dynamical systems.

**Sources (at least one non-Wikipedia):**
- MathWorld: https://mathworld.wolfram.com/NarayanaCowSequence.html
- T. Kusuba, *Combinatorics and Magic-Squares in India: A Study of Nārāyaṇa Paṇḍita's Gaṇitakaumudī*, Ph.D. dissertation, Brown University, 1993.

**Technique tag:** `composeWithIdentity` (existing) — defining-recurrence is a 3-term composition rule; the herd is built by composing base-herds of shifted generations. *New example*; reinforces that Fibonacci-style ideas have multiple independent discoveries.

---

### Oresme's Divergence of the Harmonic Series (c. 1350, Nicole Oresme)

**Statement:** ∑_{n=1}^{∞} 1/n = ∞. Proved by grouping: 1/3 + 1/4 > 1/2, 1/5 + 1/6 + 1/7 + 1/8 > 1/2, etc., so ∑_{k=1}^{2^K} 1/k > 1 + K/2.

**Discovery trigger:** In *Quaestiones super Geometriam Euclidis* (c. 1350), Oresme was studying the addition of successively smaller ratios — the late-medieval "quantitative theology" of infinite sums.

**Thought process / lineage:** Part of the 14th-century Oxford / Paris "calculators" tradition (Bradwardine, Swineshead). Oresme also gave geometric representations of varying quantities — a precursor of coordinate geometry.

**Proof idea:** Dyadic block bounding: group terms [2^(k−1)+1, 2^k] into 2^(k−1) terms each ≥ 1/2^k, summing to ≥ 1/2. Summing these lower bounds yields a divergent series.

**Impact:** First proof of divergence of an infinite series with terms tending to 0. Lost / ignored for centuries; rediscovered by the Bernoullis (1689). Dyadic-block argument is still how we teach it today. Foundational for rigorous analysis.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Oresme/
- Kifowit, "The Harmonic Series Diverges Again and Again," *AMATYC Review* (2006), http://scipp.ucsc.edu/~haber/archives/physics116A10/harmapa.pdf

**Technique tag:** `exhaustionSqueeze` (existing, inverted) — lower-bound by a divergent auxiliary series. Better: PROPOSED NEW `dyadicGrouping(series) → bound`. Applies to both convergence (p-series p > 1) and divergence (harmonic) via block-level comparison. *Propose as new technique — it's general enough to merit a name.*

---

### Stevin's Decimal Fractions & Intermediate-Value Intuition (1585, Simon Stevin)

**Statement:** (1) Every real number can be written as an infinite decimal (*De Thiende*, 1585). (2) Any polynomial that changes sign between two rational values has a root in between, located by bisection of decimal digits (algorithmic intermediate value theorem).

**Discovery trigger:** Practical needs of Dutch commerce, surveying, mint-masters, navigators; engineer-practitioner motivation.

**Thought process / lineage:** Built on Islamic decimal-fraction work (al-Uqlīdisī, al-Kāshī); Stevin published in Dutch, not Latin, making it popular among practitioners. His *Arithmetic* (1585) already applied decimal digit-search to polynomial roots, a constructive bisection.

**Proof idea:** For IVT-like statement: given P(a) < 0 < P(b), inspect P at a + (b−a)/10, a + 2(b−a)/10, …; identify the transition; iterate to higher decimal places.

**Impact:** Popularized decimal fractions in Europe; indirectly led to decimal currency. The bisection search for polynomial roots was the standard computational tool until Newton's method.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Stevin/
- H.J.M. Bos, *Lectures in the History of Mathematics*, AMS, 1993, Ch. 3 on Stevin.

**Technique tag:** `exhaustionSqueeze` (existing) — intervals shrinking to a root. `reduceToCanonicalForm` for the decimal expansion. *New multi-technique example.*

---

### Viète's Infinite Product for π (1593, François Viète)

**Statement:** 2/π = (√2/2) · (√(2+√2)/2) · (√(2+√(2+√2))/2) · ⋯

**Discovery trigger:** Viète pushed Archimedes' polygon-doubling to the algebraic limit, seeking a closed-form expression rather than a numerical approximation.

**Thought process / lineage:** Viète (1540–1603), the father of symbolic algebra, saw that each polygon-doubling step multiplied the perimeter by a factor cos(π/2^n), which satisfies the half-angle identity 2 cos²(θ/2) = 1 + cos θ. Iterated the identity.

**Proof idea:** sin θ = 2 sin(θ/2) cos(θ/2). Iterate: sin θ = 2^n sin(θ/2^n) · ∏_{k=1}^{n} cos(θ/2^k). Let θ = π/2 and n → ∞; lim 2^n sin(π/2^(n+1)) = π/2; each cos(π/2^(k+1)) is evaluated via nested square roots.

**Impact:** First *infinite product* ever written down in Western mathematics. Also computed π to 10 decimals via a 393 216-gon.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Viete/
- Beckmann, *A History of π*, St. Martin's, 1971, Ch. 8.

**Technique tag:** `composeWithIdentity` (existing) — the half-angle identity composed infinitely. *New example, first of its kind in the West.*

---

### Gauss's Constructible 17-gon (30 March 1796, Carl Friedrich Gauss)

**Statement:** The regular 17-gon is constructible with compass and straightedge. More generally (Gauss 1801): a regular n-gon is constructible iff n = 2^a · p₁ · p₂ · ⋯ · pₖ where the pᵢ are distinct Fermat primes.

**Discovery trigger:** Gauss, aged 18, set himself the problem of determining which cyclotomic equations x^n − 1 = 0 have all roots expressible via nested square roots.

**Thought process / lineage:** His March 30, 1796 diary entry: *"Principia quibus innititur sectio circuli, ac divisibilitas eiusdem geometrica in septemdecim partes"* — first entry of his famous *Tagebuch*. Key insight: 17 − 1 = 16 = 2⁴, so the 17th roots of unity form a cyclic group of order 2⁴; a tower of quadratic extensions diagonalizes this Galois group — purely 2-power quadratic radicals suffice.

**Proof idea:** The Galois group of ℚ(ζ₁₇)/ℚ is cyclic of order 16 = 2⁴. Build a chain of four intermediate fields, each a quadratic extension of the previous. Each quadratic corresponds to a ruler-and-compass construction (square-root of a prior constructible).

**Impact:** Revived Greek geometry after 2000 years of stasis. Disquisitiones Arithmeticae Section VII. Motivated Galois theory. First deep use of the structure *roots-of-unity form an abelian group* to settle a geometric problem.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Gauss/
- D. Savitt, "The mathematics of Gauss," expository notes, Cornell University, https://pi.math.cornell.edu/~web401/steve.gauss17gon.pdf

**Technique tag:** `structuralIsomorphism` (existing) — abelian-group structure of roots of unity ↔ solvability by square-root towers. Foreshadows `analysisAlgebraTopologyBridge`. *New example.*

---

### Dirichlet's Approximation Theorem via Pigeonhole (1842, Peter Gustav Lejeune Dirichlet)

**Statement:** For every real α and every positive integer Q, there exist integers p, q with 1 ≤ q ≤ Q and |α − p/q| < 1/(qQ). Equivalently, every irrational has infinitely many rational approximations p/q with |α − p/q| < 1/q².

**Discovery trigger:** Dirichlet wanted a clean proof that irrationals are arbitrarily well approximated by rationals, without appealing to continued fractions.

**Thought process / lineage:** Dirichlet had already named and used the *Schubfachprinzip* (drawer / pigeonhole principle) in 1834 for work on Pell's equation and units. In 1842 he applied it to approximation.

**Proof idea:** Consider the Q+1 fractional parts {0·α}, {1·α}, {2·α}, …, {Q·α} in [0,1). Divide [0,1) into Q half-open intervals of length 1/Q. By pigeonhole, two fractional parts {iα}, {jα} (with i < j) lie in the same interval, hence |{iα} − {jα}| < 1/Q. Set q = j − i and p = ⌊jα⌋ − ⌊iα⌋ to conclude.

**Impact:** First application of the pigeonhole principle in analytic number theory. The theorem is the starting point for all of Diophantine approximation (Thue 1908, Roth 1955). Pigeonhole is now universal.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Dirichlet/
- B. Rittaud & A. Heeffer, "The pigeonhole principle, two centuries before Dirichlet," *Mathematical Intelligencer* 36 (2014), 27–29. https://backoffice.biblio.ugent.be/download/4115264/4115265

**Technique tag:** PROPOSED NEW — `pigeonholeCollision(objects, bins with |objects|>|bins|) → twoInSameBin`. A basic combinatorial existence principle foundational across discrete mathematics, Ramsey theory, and analysis, yet not covered by any of the 27 existing techniques. (Different from `compactnessArgument`: discrete, finite, no topology; different from `diagonalize`: produces a *collision*, not a *difference*.)

---

### Liouville's Construction of Transcendental Numbers (1844, Joseph Liouville)

**Statement:** **Liouville's Approximation Bound:** Every algebraic number α of degree d ≥ 2 satisfies |α − p/q| > C(α)/q^d for all p/q ∈ ℚ. Consequently, any real number approximable beyond every polynomial rate — e.g., L = ∑_{n=1}^{∞} 10^{−n!} = 0.11000100000000000000000100…1 — is *transcendental*.

**Discovery trigger:** Liouville originally tried to prove e transcendental (in correspondence with Goldbach and Bernoulli references); the proof failed, but a weaker bound was enough to *construct* transcendentals ex nihilo.

**Thought process / lineage:** Constructed examples via continued fractions (1844), then reformulated via series (1851). Predecessors: Euler (suspected e, π transcendental); contemporaries: Lambert (π irrational, 1761).

**Proof idea:** Let α satisfy f(α) = 0 with f ∈ ℤ[x] of degree d. Then |f(p/q)| ≥ 1/q^d by clearing denominators, and by mean value |α − p/q| · |f'(ξ)| = |f(α) − f(p/q)| = |f(p/q)|. Bounding |f'| on a neighborhood of α: |α − p/q| ≥ c/q^d. Any number with |L − p/q| < 1/q^n for every n is therefore not algebraic.

**Impact:** First explicit construction of a transcendental number. Opened the door to Cantor's 1874 proof that *most* reals are transcendental, and to Hermite's 1873 proof that e is transcendental. The bound was later improved: Thue (1908) to q^(d/2+1+ε), Siegel (1921), and ultimately Roth (1955) to q^(2+ε) — a half-century-plus research program.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Liouville/
- S. Chanillo, "Construction of Transcendental Numbers," Rutgers lecture notes, https://sites.math.rutgers.edu/~chanillo/liouville.pdf

**Technique tag:** `obstructionClass` (existing) — "being algebraic of degree d" *forces* a quantitative lower bound on rational approximation; a number exceeding this bound is *obstructed* from being algebraic. *New example of the obstruction pattern in analysis-to-algebra direction.*

---

### Euler's Pentagonal Number Theorem (1741 discovered, 1750 proved, Leonhard Euler)

**Statement:** ∏_{n=1}^{∞} (1 − x^n) = ∑_{k=−∞}^{∞} (−1)^k x^{k(3k−1)/2} = 1 − x − x² + x⁵ + x⁷ − x¹² − x¹⁵ + x²² + x²⁶ − …, where the exponents are the generalized pentagonal numbers k(3k−1)/2.

**Discovery trigger:** In January 1741 Euler told Daniel Bernoulli he had noticed an extremely slowly converging product seemed to produce a sparse series with pentagonal-number exponents — pure pattern-spotting in tables.

**Thought process / lineage:** Euler's 1741 paper *Observationes analyticae variae de combinationibus* announced it empirically with "300 cases" of evidence but no proof. He finally proved it in 1750 (letter to Goldbach) via a combinatorial argument later sharpened by Franklin (1881) into the canonical sign-reversing-involution proof on distinct-part partitions.

**Proof idea (Franklin 1881):** On the set of partitions of n into distinct parts, define an involution that pairs most up into (even, odd) cancellations. The unpaired partitions are the "staircase" partitions, whose sizes are exactly the generalized pentagonal numbers.

**Impact:** Parent of modular-form identities (Jacobi triple product, Dedekind eta). Yields a linear recurrence for the partition function: p(n) = p(n−1) + p(n−2) − p(n−5) − p(n−7) + p(n−12) + ⋯, used ever since to tabulate p(n).

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Euler/
- J. Bell, "A summary of Euler's work on the pentagonal number theorem," *Archive for History of Exact Sciences* 64 (2010), 301–373. https://link.springer.com/article/10.1007/s00407-010-0057-y

**Technique tag:** `spotPatternInTable` (existing) followed by `composeWithIdentity` (existing) — classic Euler pipeline. *New example.*

---

### Jacobi's Triple Product Identity (1829, Carl Gustav Jacob Jacobi)

**Statement:** ∏_{m=1}^{∞} (1 − x^{2m})(1 + x^{2m−1} y²)(1 + x^{2m−1} y^{−2}) = ∑_{n=−∞}^{∞} x^{n²} y^{2n}, valid for |x| < 1 and y ≠ 0.

**Discovery trigger:** Jacobi was unifying theta functions and elliptic functions, trying to write theta functions as infinite products (Weierstrass-style) rather than as double series.

**Thought process / lineage:** Published in *Fundamenta Nova Theoriae Functionum Ellipticarum* (1829). Built on Legendre (elliptic integrals) and Abel (inversion). The triple product subsumes Euler's pentagonal theorem (set y² = −x^{1/2}) and Gauss's theta identity.

**Proof idea:** Either (a) combinatorial bijection between lattice-point sums and partition-like products, or (b) modular transformation on the Jacobi theta function θ(z; τ) = Σ q^{n²} e^{2πinz} combined with a product expansion from the zeros of θ.

**Impact:** Unifying skeleton of q-series / partition theory / modular forms. Ramanujan's many partition identities (Rogers–Ramanujan, Jacobi triple product corollaries) descend from this one formula. Quantum field theory, string theory partition functions, monstrous moonshine.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Jacobi/
- G. E. Andrews, *The Theory of Partitions*, Cambridge, 1984, Ch. 2.

**Technique tag:** `composeWithIdentity` + `frequencyDecomposition` (both existing) — composition of Euler products with theta-style frequency sums. *New cross-technique example.*

---

### Hardy–Ramanujan Partition Formula (1918, G.H. Hardy & S. Ramanujan)

**Statement:** p(n) ∼ (1/(4n√3)) · exp(π √(2n/3)) as n → ∞. Plus an explicit asymptotic expansion whose first few terms give p(n) to within ±1.

**Discovery trigger:** MacMahon's tables of p(n) for small n showed rapid growth. Ramanujan, armed with elliptic-function intuition, conjectured the leading asymptotic; Hardy insisted on rigorous justification.

**Thought process / lineage:** Ramanujan had essentially the core of the "circle method" from his Indian work (seen in his 1913 letter to Hardy). At Cambridge (1914–1918) the two combined Ramanujan's formal manipulations with Hardy's contour-integration discipline. Rademacher (1937) later turned it into an exact convergent series: p(n) = (1/π√2) ∑_{k=1}^{∞} A_k(n) · √k · (d/dn) [sinh(π √(2n/3)/k) / √(n − 1/24)].

**Proof idea:** Use the generating function F(q) = ∑ p(n) q^n = ∏ (1 − q^n)^{−1}. By Cauchy, p(n) = (1/2πi) ∮ F(q)/q^{n+1} dq around |q| = r < 1. The integrand blows up near roots of unity — organize the circle into "major arcs" near rational points and "minor arcs" elsewhere; modular transformation controls the major-arc contribution.

**Impact:** Launched the **circle method** — the central analytic tool in additive number theory (Waring's problem, Goldbach, Vinogradov's 3-primes). Also foundational for modern theory of modular forms and partition congruences. Rademacher's series is one of the first *exact* asymptotic formulas in number theory.

**Sources (at least one non-Wikipedia):**
- Hardy & Ramanujan (1918), "Asymptotic formulae in combinatory analysis," *Proc. London Math. Soc.* (Internet Archive full text): https://archive.org/details/hardy-ramanujan-1918-asymptotic-formulaae-in-combinatory-analysis
- M. R. Murty, "The Partition Function Revisited," Queen's University, https://mast.queensu.ca/~murty/partition.pdf

**Technique tag:** `complexAnalysisToIntegers` (existing) — canonical modern instance: encode arithmetic function (p(n)) in a complex-analytic generating function; locate singularities; extract asymptotic via contour shift / major–minor arc. *Important new example cementing the technique's template.*

---

### Chebyshev's Inequality (1867, Pafnuty Chebyshev)

**Statement:** For any random variable X with finite mean μ and variance σ², and any k > 0, P(|X − μ| ≥ kσ) ≤ 1/k².

**Discovery trigger:** Chebyshev sought a rigorous, distribution-free version of the "law of large numbers" that didn't require assumptions about the underlying distribution.

**Thought process / lineage:** Generalized Bienaymé's 1853 version. Published in "Des valeurs moyennes" (*J. Math. Pures Appl.* 1867). Proof descendant of Markov's inequality (Chebyshev's student Markov later systematized).

**Proof idea:** Apply Markov's inequality P(Y ≥ a) ≤ E[Y]/a to Y = (X − μ)² and a = (kσ)².

**Impact:** Foundational to classical probability; basis of the weak law of large numbers (with n independent X_i, their average concentrates around μ by a 1/n Chebyshev bound). Modern descendants: concentration inequalities (Hoeffding, Chernoff, Azuma) — the entire "concentration of measure" program.

**Sources (at least one non-Wikipedia):**
- MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Chebyshev/
- Encyclopedia of Mathematics: https://encyclopediaofmath.org/wiki/Chebyshev_inequality

**Technique tag:** `exhaustionSqueeze` (existing, probabilistic form) — bounding a probability above by an expectation. Alternatively: PROPOSED NEW `momentBound(distribution, quantity) → tailBound` — a general technique (Markov, Chebyshev, Chernoff, Paley–Zygmund) that bounds tail probabilities via moments. Tentatively propose new.

---

### Legendre Transform (1787, Adrien-Marie Legendre)

**Statement:** For a smooth, strictly convex function f: ℝ → ℝ, its Legendre transform f*(p) = sup_x (px − f(x)) is another convex function; applying the transform twice gives f back: (f*)* = f. Key identity: f(x) + f*(p) ≥ xp, with equality iff p = f'(x).

**Discovery trigger:** Legendre introduced the transform in *Mémoire sur l'intégration de quelques équations aux différences partielles* (1787) to simplify a minimal-surface ODE by "changing variables" from (x, y, dy/dx) to (y − x·p, p).

**Thought process / lineage:** Built on Euler's 1776 use of related substitutions in variational problems. Later generalized to convex analysis by Fenchel (1949) and Rockafellar.

**Proof idea:** The transform's involution property follows from the tangent-line / epigraph duality: the graph of f is the envelope of its tangent lines, encoded in (slope, intercept) coordinates by f*.

**Impact:** Backbone of the Hamiltonian formulation of mechanics (Legendre transform of the Lagrangian in (q, q̇) gives the Hamiltonian in (q, p)). In convex analysis: Fenchel duality, Lagrangian duality in optimization. In thermodynamics: transforms between thermodynamic potentials. In information theory: relations between free energies.

**Sources (at least one non-Wikipedia):**
- Encyclopedia of Mathematics: https://encyclopediaofmath.org/wiki/Legendre_transform
- R. T. Rockafellar, *Convex Analysis*, Princeton University Press, 1970, §12.

**Technique tag:** `duality` (existing) — canonical example: points ↔ tangent lines, f ↔ f*, involutive. *Important new example.*

---

## Technique-tag summary

**Existing-technique tags used (as new examples):**
- `spotPatternInTable` — 2 (Jia Xian triangle; Virahanka; shared with Euler pentagonal)
- `verifyOnSpecialCases` — 0
- `completeTheSquare` — 0
- `reduceToCanonicalForm` — 1 (Li Ye tian yuan shu; Stevin shared)
- `composeWithIdentity` — 5 (Thābit amicable; Virahanka recurrence; Narayana cow; Viète product; Euler pentagonal; Jacobi triple product)
- `symmetryReduction` — 0
- `conservedQuantity` — 0
- `duality` — 1 (Legendre transform)
- `exhaustionSqueeze` — 5 (Nilakantha arctan; al-Kāshī π; Liu Hui π; Zu Chongzhi π; Stevin decimal IVT; Chebyshev inequality shared)
- `interpolateAndContinue` — 1 (Madhava arctan)
- `frequencyDecomposition` — 2 (al-Tūsī couple; Jacobi triple product shared)
- `axiomatizeFromInstances` — 1 (Jyeshthadeva Yuktibhāṣā)
- `structuralIsomorphism` — 2 (Zu Geng principle; Gauss 17-gon)
- `raiseDimension` — 0
- `obstructionClass` — 1 (Liouville transcendentals)
- `compactnessArgument` — 0
- `diagonalize` — 0
- `arithmetizeSyntax` — 1 (Pingala binary encoding)
- `forceIndependence` — 0
- `contractionFixedPoint` — 1 (Qin Jiushao Horner iteration — tentative)
- `infiniteDescent` — 0
- `flowWithSurgery` — 0
- `physicsToPDE` — 0
- `complexAnalysisToIntegers` — 1 (Hardy–Ramanujan)
- `analysisAlgebraTopologyBridge` — 0
- `finiteCaseCheck` — 0
- `formalVerify` — 0
- `distributedCollaboration` — 0

Total **existing-technique re-uses**: ≈ 23 tag assignments across 22 theorems (several theorems invoke two existing techniques).

**PROPOSED NEW techniques (flagged for researcher validation):**
1. `accelerateSeriesByRemainderModel(alternatingSeries) → fasterSeries + errorEstimate` — Kerala end-correction; anticipates Euler/Shanks/Richardson. Exemplified by Madhava's π series (entry 2).
2. `inductiveSumIdentity(recurrenceInP) → closedForm(∑k^p)` — climb from ∑k⁰ to ∑k^p via a recurrence identity across powers. Direct ancestor of Faulhaber / Bernoulli numbers. Exemplified by Ibn al-Haytham (entry 8).
3. `syntheticDeflationIteration(polynomial P, initialDigit) → digit-by-digit root` — Qin Jiushao / Horner / Ruffini scheme. Distinct from Newton's method because it is derivative-free and digit-by-digit. Exemplified by Qin Jiushao (entry 11).
4. `dyadicGrouping(series) → convergenceOrDivergenceBound` — block-wise comparison in log₂-spaced blocks. Works for both convergence (Cauchy condensation) and divergence (Oresme). Exemplified by Oresme (entry 17).
5. `pigeonholeCollision(objects, bins with |objects|>|bins|) → twoInSameBin` — basic existence-by-counting. Not covered by any of the 27 existing techniques. Exemplified by Dirichlet's approximation theorem (entry 21). *Strongest candidate for addition — spans combinatorics, Ramsey theory, ergodic theory.*
6. `momentBound(distribution, quantity) → tailBound` — Markov / Chebyshev / Chernoff family. Foundational in probability. Candidate for a new Cluster 11 (Probabilistic Arguments), as already flagged in §6 of the existing toolbox. Exemplified by Chebyshev (entry 24).

**Total:**
- Existing-technique assignments: 23
- Proposed-new-technique candidates: 6 (with 4 of them — #1, #2, #4, #5 — having clear multiple-instance generality; #3 and #6 are more specialized)

---

## Uncertainties & flags for the researcher

1. **Madhava priority:** His own works are lost. Series attributions come via Nilakantha (1501), Jyeshthadeva (c. 1530), and later commentators (Shankara Variar). Occasional scholarship questions whether some "Madhava" series were actually Nilakantha's. I follow the standard Rajagopal attribution, but the researcher should decide how to state authorship.

2. **Tūsī couple → Copernicus transmission:** Historical debate continues. Saliba (1987, 1996) and Ragep (2001) argue for actual textual transmission via Byzantine sources; Swerdlow (1973) is agnostic. I flagged the dispute in the entry per CHARTER rule 4.

3. **Pingala vs. Piṅgala dating:** Range given as c. 200 BCE; some scholars push back to 500 BCE (brother of Pāṇini) or forward to 200 CE. Chose 200 BCE as the modal scholarly consensus but this should be flagged.

4. **Qin Jiushao vs. Horner:** Qin's method appeared in 1247; Al-Ṭūsī's *Miftāḥ al-Ḥisāb* (al-Kāshī, 1427) has an equivalent. Independent discovery is well-established. Not really Horner's (1819); the name "Ruffini-Horner-Qin" is sometimes used.

5. **"Pentagonal number theorem" discovery date:** I list 1741 (discovered, letter to Bernoulli) but proof is 1750 (letter to Goldbach) and publication 1760. Researcher may prefer single-date attribution.

6. **Pigeonhole principle pre-Dirichlet:** Rittaud & Heeffer (2014) document uses two centuries before Dirichlet (Leurechon 1622, others). Dirichlet is the *first to name* the principle (Schubfachprinzip) and to give it a mathematical profile. I attribute to Dirichlet per convention but note this in sources.

7. **Technique tags for Qin Jiushao and Chebyshev are tentative.** Both could be argued as existing technique instances (`contractionFixedPoint` and `exhaustionSqueeze` respectively) rather than new techniques. Final call should be the researcher's / engineer's.

8. **Possible single-finding technique overlap:** Proposed new techniques `accelerateSeriesByRemainderModel` and `dyadicGrouping` both deal with series bounds — a researcher might merge them or subsume one under a broader "seriesBoundingTrick" umbrella.

9. **Not covered for space** (but candidates if the toolbox wants more): Brahmagupta-Fibonacci identity, al-Khwārizmī's *mu'āmalāt* arithmetic, Bhāskara I sine approximation, Euler–Maclaurin (partially discussed), Eisenstein's criterion, Cardano's complex numbers. These are all "existing-technique new examples."

End of findings.
