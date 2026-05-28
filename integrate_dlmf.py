#!/usr/bin/env python3
"""
Integrate ~400 DLMF (Digital Library of Mathematical Functions) nodes
into the knowledge graph at knowledge_graph.json.

Covers all 36 chapters of NIST DLMF with key states, axioms, theorems,
and techniques plus cross-chapter connecting edges.
"""

import json
from collections import Counter

# ---------------------------------------------------------------------------
# 1. Load existing graph
# ---------------------------------------------------------------------------
with open('knowledge_graph.json') as f:
    graph = json.load(f)

existing_ids = {n['id'] for n in graph['nodes']}
print(f"Loaded graph: {len(graph['nodes'])} nodes, {len(graph['edges'])} edges")

# ---------------------------------------------------------------------------
# 2. Define ALL new DLMF nodes (~400 across 36 chapters)
# ---------------------------------------------------------------------------
new_nodes = [

    # ===================================================================
    # CHAPTER 1: ALGEBRAIC AND ANALYTIC METHODS (supplements)
    # ===================================================================
    {"id": "s_mellin_transform", "kind": "axiom", "name": "Mellin Transform",
     "type_signature": "",
     "description": "The integral transform M{f}(s) = integral_0^infty x^{s-1} f(x) dx, analytic in a vertical strip."},
    {"id": "s_faa_di_bruno_formula", "kind": "theorem", "name": "Faa di Bruno's Formula",
     "type_signature": "",
     "description": "Explicit formula for the n-th derivative of a composite function f(g(x)) as a sum over partitions involving Bell polynomials."},
    {"id": "s_leibniz_rule_integral", "kind": "theorem", "name": "Leibniz Integral Rule (Differentiation Under the Sign)",
     "type_signature": "",
     "description": "d/dx integral_{a(x)}^{b(x)} f(x,t) dt = f(x,b)b' - f(x,a)a' + integral partial_x f dt under suitable regularity."},

    # ===================================================================
    # CHAPTER 2: ASYMPTOTIC METHODS
    # ===================================================================
    {"id": "s_poincare_asymptotic_expansion", "kind": "axiom", "name": "Poincare Asymptotic Expansion",
     "type_signature": "",
     "description": "A formal series f(z) ~ sum a_n z^{-n} as z -> infty, where for each N the remainder is O(z^{-N}) in a given sector."},
    {"id": "s_watsons_lemma", "kind": "theorem", "name": "Watson's Lemma",
     "type_signature": "",
     "description": "If f(t) has an asymptotic expansion at t=0, then its Laplace-type integral admits term-by-term asymptotic integration as z -> infty."},
    {"id": "s_stokes_phenomenon", "kind": "state", "name": "Stokes Phenomenon",
     "type_signature": "",
     "description": "The discontinuous change in asymptotic expansion form as the argument crosses Stokes lines in the complex plane, where subdominant exponentials switch on or off."},
    {"id": "s_abel_plana_summation_formula", "kind": "theorem", "name": "Abel-Plana Summation Formula",
     "type_signature": "",
     "description": "Relates sum f(n) to integral f(t) dt plus a correction term involving f(it)-f(-it), converting sums to integrals without requiring derivatives."},
    {"id": "t_laplaces_method", "kind": "technique", "name": "Laplace's Method",
     "function_signature": "(Integral of e^{-z p(t)} q(t) dt, z -> infty) -> (Asymptotic expansion)",
     "description": "Obtains asymptotic expansions of Laplace-type integrals for large z by expanding about the minimum of the exponent."},
    {"id": "t_method_of_steepest_descents", "kind": "technique", "name": "Method of Steepest Descents",
     "function_signature": "(Contour integral with large parameter) -> (Asymptotic expansion via saddle-point deformation)",
     "description": "Deforms a contour integral through saddle points along paths of steepest descent to obtain asymptotic expansions."},
    {"id": "t_bleisteins_method", "kind": "technique", "name": "Bleistein's Method",
     "function_signature": "(Integral with coalescing critical points) -> (Uniform asymptotic expansion in Airy functions)",
     "description": "Obtains uniform asymptotic expansions when two stationary points coalesce, expressing results in terms of Airy functions."},
    {"id": "t_mellin_transform_asymptotics", "kind": "technique", "name": "Mellin Transform Asymptotics",
     "function_signature": "(Mellin-Barnes integral) -> (Asymptotic expansion by contour shifting)",
     "description": "Derives asymptotic expansions by shifting contours in Mellin-Barnes integrals and collecting residues."},
    {"id": "t_liouville_green_wkb_approximation", "kind": "technique", "name": "Liouville-Green (WKB) Approximation",
     "function_signature": "(Second-order ODE with large parameter) -> (Approximate exponential-integral solutions)",
     "description": "Constructs approximate solutions to d^2w/dz^2 = u^2 f(z) w for large u as f^{-1/4} exp(+/-u integral sqrt{f} dz)."},
    {"id": "t_fuchs_frobenius_theory", "kind": "technique", "name": "Fuchs-Frobenius Theory",
     "function_signature": "(ODE with regular singular point) -> (Generalized power series solutions via indicial equation)",
     "description": "Constructs solutions of linear ODEs near regular singular points as z^r sum a_n z^n where r satisfies the indicial equation."},
    {"id": "t_darboux_method", "kind": "technique", "name": "Darboux's Method",
     "function_signature": "(Generating function singularity) -> (Asymptotic formula for Taylor coefficients)",
     "description": "Extracts asymptotic behavior of Taylor coefficients from the singularity structure on the circle of convergence."},
    {"id": "t_exponentially_improved_asymptotics", "kind": "technique", "name": "Exponentially Improved Asymptotics",
     "function_signature": "(Optimally truncated Poincare series) -> (Re-expansion with exponentially small error)",
     "description": "Re-expands the remainder after optimal truncation to capture exponentially small terms beyond all algebraic orders."},
    {"id": "t_hyperasymptotics", "kind": "technique", "name": "Hyperasymptotics",
     "function_signature": "(Exponentially improved remainder) -> (Iterated re-expansion with super-exponential accuracy)",
     "description": "Iterates exponentially improved asymptotics to achieve successively more accurate approximations."},
    {"id": "s_borel_summation", "kind": "axiom", "name": "Borel Summation",
     "type_signature": "",
     "description": "Method assigning a value to a divergent series via Borel transform and Laplace integral: sum a_n z^n -> integral_0^infty e^{-t} (sum a_n (tz)^n/n!) dt."},

    # ===================================================================
    # CHAPTER 3: NUMERICAL METHODS
    # ===================================================================
    {"id": "t_clenshaw_curtis_quadrature", "kind": "technique", "name": "Clenshaw-Curtis Quadrature",
     "function_signature": "(Integrand on [-1,1]) -> (Numerical integral via Chebyshev-point interpolation)",
     "description": "Approximates definite integrals by interpolating at Chebyshev points and integrating the polynomial exactly."},
    {"id": "t_romberg_integration", "kind": "technique", "name": "Romberg Integration",
     "function_signature": "(Integrand, interval) -> (High-order numerical integral via Richardson extrapolation)",
     "description": "Accelerates the trapezoidal rule by systematic Richardson extrapolation on halved step sizes."},
    {"id": "t_pade_approximation", "kind": "technique", "name": "Pade Approximation",
     "function_signature": "(Power series) -> (Rational function matching maximum coefficients)",
     "description": "Approximates a function by a rational function whose Taylor expansion matches the given series to maximum order."},
    {"id": "t_chebyshev_expansion", "kind": "technique", "name": "Chebyshev Expansion",
     "function_signature": "(Function on [-1,1]) -> (Near-minimax polynomial in Chebyshev basis)",
     "description": "Expands a function in Chebyshev polynomials T_n(x) yielding near-optimal uniform polynomial approximations."},
    {"id": "t_minimax_rational_approximation", "kind": "technique", "name": "Minimax Rational Approximation",
     "function_signature": "(Function, degree bounds) -> (Rational function minimizing sup-norm error)",
     "description": "Constructs the rational approximation minimizing maximum absolute error, characterized by equioscillation."},
    {"id": "t_aitken_delta_squared_process", "kind": "technique", "name": "Aitken's Delta-Squared Process",
     "function_signature": "(Linearly convergent sequence) -> (Accelerated sequence)",
     "description": "Transforms a linearly convergent sequence via s'_n = s_n - (Delta s_n)^2/(Delta^2 s_n) to achieve faster convergence."},
    {"id": "t_wynn_epsilon_algorithm", "kind": "technique", "name": "Wynn's Epsilon Algorithm",
     "function_signature": "(Partial sums) -> (Pade-like accelerated approximations)",
     "description": "Computes sequence transformations equivalent to diagonal Pade approximants via a recursive triangular array."},
    {"id": "t_levin_transformation", "kind": "technique", "name": "Levin's Transformation",
     "function_signature": "(Slowly convergent series) -> (Accelerated sequence using remainder estimates)",
     "description": "A nonlinear sequence transformation accelerating convergence by using estimates of the general term's behavior."},
    {"id": "t_gauss_legendre_quadrature", "kind": "technique", "name": "Gauss-Legendre Quadrature",
     "function_signature": "(Integrand on [-1,1]) -> (Optimal n-point numerical integral)",
     "description": "Evaluates integral with optimal polynomial degree accuracy 2n-1 using zeros of Legendre polynomials as nodes."},
    {"id": "t_gauss_laguerre_quadrature", "kind": "technique", "name": "Gauss-Laguerre Quadrature",
     "function_signature": "(Integrand on [0,infty) with weight x^alpha e^{-x}) -> (Numerical integral)",
     "description": "Optimal quadrature for integrands with Laguerre weight using zeros of Laguerre polynomials."},
    {"id": "t_gauss_hermite_quadrature", "kind": "technique", "name": "Gauss-Hermite Quadrature",
     "function_signature": "(Integrand on R with weight e^{-x^2}) -> (Numerical integral)",
     "description": "Optimal quadrature for Gaussian-weighted integrals using zeros of Hermite polynomials."},

    # ===================================================================
    # CHAPTER 4: ELEMENTARY FUNCTIONS (supplements)
    # ===================================================================
    {"id": "s_lambert_w_function", "kind": "axiom", "name": "Lambert W-Function",
     "type_signature": "",
     "description": "The multivalued inverse of f(w) = we^w, with principal branch W_0 real-valued for x >= -1/e."},
    {"id": "s_gudermannian_function", "kind": "state", "name": "Gudermannian Function gd(x)",
     "type_signature": "",
     "description": "gd(x) = 2 arctan(tanh(x/2)), connecting circular and hyperbolic functions without complex numbers."},

    # ===================================================================
    # CHAPTER 5: GAMMA FUNCTION
    # ===================================================================
    {"id": "s_euler_mascheroni_constant", "kind": "axiom", "name": "Euler-Mascheroni Constant",
     "type_signature": "",
     "description": "The constant gamma = lim(sum 1/k - ln n) approx 0.5772, appearing in the digamma function psi(1) = -gamma."},
    {"id": "s_pochhammer_symbol", "kind": "axiom", "name": "Pochhammer Symbol (Rising Factorial)",
     "type_signature": "",
     "description": "The rising factorial (a)_n = a(a+1)...(a+n-1) = Gamma(a+n)/Gamma(a), fundamental to hypergeometric series."},
    {"id": "s_gamma_recurrence_relation", "kind": "theorem", "name": "Gamma Function Recurrence Relation",
     "type_signature": "",
     "description": "The functional equation Gamma(z+1) = z Gamma(z), generalizing n! = n(n-1)!."},
    {"id": "s_euler_reflection_formula", "kind": "theorem", "name": "Euler's Reflection Formula",
     "type_signature": "",
     "description": "Gamma(z) Gamma(1-z) = pi/sin(pi z), connecting Gamma at complementary arguments."},
    {"id": "s_legendre_duplication_formula", "kind": "theorem", "name": "Legendre Duplication Formula",
     "type_signature": "",
     "description": "Gamma(z) Gamma(z+1/2) = sqrt(pi) 2^{1-2z} Gamma(2z), relating Gamma at z and 2z."},
    {"id": "s_gauss_multiplication_formula", "kind": "theorem", "name": "Gauss Multiplication Formula",
     "type_signature": "",
     "description": "Product of Gamma(z+k/n) for k=0..n-1 equals (2pi)^{(n-1)/2} n^{1/2-nz} Gamma(nz)."},
    {"id": "s_bohr_mollerup_theorem", "kind": "theorem", "name": "Bohr-Mollerup Theorem",
     "type_signature": "",
     "description": "Gamma is the unique log-convex function on (0,infty) with f(1)=1 and f(x+1)=xf(x)."},
    {"id": "s_hankel_contour_integral_reciprocal_gamma", "kind": "theorem", "name": "Hankel's Contour Integral for 1/Gamma(z)",
     "type_signature": "",
     "description": "1/Gamma(z) = (1/2pi i) oint (-t)^{-z} e^{-t} dt over a Hankel contour, showing 1/Gamma is entire."},
    {"id": "s_binet_formula_log_gamma", "kind": "theorem", "name": "Binet's Formula for ln Gamma",
     "type_signature": "",
     "description": "Integral representation expressing the Stirling remainder of ln Gamma(z) as an explicit arctangent integral."},
    {"id": "s_polygamma_functions", "kind": "state", "name": "Polygamma Functions",
     "type_signature": "",
     "description": "The functions psi^{(n)}(z) = d^{n+1}/dz^{n+1} ln Gamma(z), with psi^{(0)} the digamma function."},
    {"id": "s_polygamma_recurrence_relation", "kind": "theorem", "name": "Polygamma Recurrence Relation",
     "type_signature": "",
     "description": "psi^{(n)}(z+1) = psi^{(n)}(z) + (-1)^n n!/z^{n+1}, reducing polygamma evaluation to a strip."},
    {"id": "s_polygamma_reflection_formula", "kind": "theorem", "name": "Polygamma Reflection Formula",
     "type_signature": "",
     "description": "psi^{(n)}(1-z) + (-1)^{n+1} psi^{(n)}(z) = (-1)^n pi d^n/dz^n cot(pi z)."},
    {"id": "s_barnes_g_function", "kind": "state", "name": "Barnes G-Function",
     "type_signature": "",
     "description": "Entire function satisfying G(z+1) = Gamma(z) G(z) with G(1)=1, a double gamma function."},
    {"id": "s_q_gamma_function", "kind": "state", "name": "q-Gamma Function",
     "type_signature": "",
     "description": "q-analog of Gamma defined via Gamma_q(z) = (q;q)_infty/(q^z;q)_infty (1-q)^{1-z}, reducing to Gamma(z) as q->1."},
    {"id": "s_reciprocal_gamma_entire", "kind": "state", "name": "Reciprocal Gamma as Entire Function",
     "type_signature": "",
     "description": "1/Gamma(z) is an entire function of order 1 with zeros at z = 0, -1, -2, ... and Weierstrass product representation."},
    {"id": "s_beta_integral_representation", "kind": "theorem", "name": "Beta Function Integral Representation",
     "type_signature": "",
     "description": "B(a,b) = integral_0^1 t^{a-1}(1-t)^{b-1} dt = Gamma(a)Gamma(b)/Gamma(a+b) for Re a, Re b > 0."},

    # ===================================================================
    # CHAPTER 6: EXPONENTIAL, LOGARITHMIC, SINE, AND COSINE INTEGRALS
    # ===================================================================
    {"id": "s_exponential_integral_E1", "kind": "axiom", "name": "Exponential Integral E_1(z)",
     "type_signature": "",
     "description": "E_1(z) = integral_z^infty e^{-t}/t dt, the principal exponential integral with logarithmic singularity at z=0."},
    {"id": "s_exponential_integral_Ei", "kind": "axiom", "name": "Exponential Integral Ei(x)",
     "type_signature": "",
     "description": "Ei(x) = P.V. integral_{-infty}^x e^t/t dt for real x, related to E_1 by Ei(x) = -E_1(-x) +/- i pi."},
    {"id": "s_sine_integral", "kind": "axiom", "name": "Sine Integral Si(z)",
     "type_signature": "",
     "description": "Si(z) = integral_0^z sin(t)/t dt, an entire odd function with Si(+infty) = pi/2."},
    {"id": "s_cosine_integral", "kind": "axiom", "name": "Cosine Integral Ci(z)",
     "type_signature": "",
     "description": "Ci(z) = -integral_z^infty cos(t)/t dt = gamma + ln z + integral_0^z (cos t -1)/t dt with branch point at origin."},
    {"id": "s_logarithmic_integral", "kind": "axiom", "name": "Logarithmic Integral li(x)",
     "type_signature": "",
     "description": "li(x) = integral_0^x dt/ln t = Ei(ln x), the offset logarithmic integral appearing in the prime number theorem."},

    # ===================================================================
    # CHAPTER 7: ERROR FUNCTIONS, DAWSON'S AND FRESNEL INTEGRALS
    # ===================================================================
    {"id": "s_error_function", "kind": "axiom", "name": "Error Function erf(z)",
     "type_signature": "",
     "description": "erf(z) = (2/sqrt(pi)) integral_0^z e^{-t^2} dt, the normalized incomplete Gaussian integral."},
    {"id": "s_complementary_error_function", "kind": "axiom", "name": "Complementary Error Function erfc(z)",
     "type_signature": "",
     "description": "erfc(z) = 1 - erf(z) = (2/sqrt(pi)) integral_z^infty e^{-t^2} dt, preferred for large arguments."},
    {"id": "s_faddeeva_function", "kind": "state", "name": "Faddeeva Function w(z)",
     "type_signature": "",
     "description": "w(z) = e^{-z^2} erfc(-iz), central to Voigt profile computation and plasma dispersion."},
    {"id": "s_dawsons_integral", "kind": "axiom", "name": "Dawson's Integral F(z)",
     "type_signature": "",
     "description": "F(z) = e^{-z^2} integral_0^z e^{t^2} dt, a one-sided Fourier-Laplace transform of the Gaussian."},
    {"id": "s_fresnel_cosine_integral", "kind": "axiom", "name": "Fresnel Cosine Integral C(z)",
     "type_signature": "",
     "description": "C(z) = integral_0^z cos(pi t^2/2) dt, an entire function whose plot forms the Cornu spiral."},
    {"id": "s_fresnel_sine_integral", "kind": "axiom", "name": "Fresnel Sine Integral S(z)",
     "type_signature": "",
     "description": "S(z) = integral_0^z sin(pi t^2/2) dt, companion to C(z) in the Cornu spiral."},
    {"id": "s_voigt_profile", "kind": "state", "name": "Voigt Profile",
     "type_signature": "",
     "description": "Convolution of Gaussian and Lorentzian line shapes V(x;sigma,gamma) = Re[w(z)]/(sigma sqrt(2pi)), central to spectroscopy."},

    # ===================================================================
    # CHAPTER 8: INCOMPLETE GAMMA AND RELATED FUNCTIONS
    # ===================================================================
    {"id": "s_lower_incomplete_gamma", "kind": "axiom", "name": "Lower Incomplete Gamma Function gamma(a,z)",
     "type_signature": "",
     "description": "gamma(a,z) = integral_0^z t^{a-1} e^{-t} dt, satisfying gamma(a,z) + Gamma(a,z) = Gamma(a)."},
    {"id": "s_upper_incomplete_gamma", "kind": "axiom", "name": "Upper Incomplete Gamma Function Gamma(a,z)",
     "type_signature": "",
     "description": "Gamma(a,z) = integral_z^infty t^{a-1} e^{-t} dt, related to E_n(z) = z^{n-1} Gamma(1-n,z)."},
    {"id": "s_regularized_incomplete_gamma", "kind": "state", "name": "Regularized Incomplete Gamma P(a,z) and Q(a,z)",
     "type_signature": "",
     "description": "P = gamma(a,z)/Gamma(a) and Q = Gamma(a,z)/Gamma(a) with P+Q=1, giving the chi-squared CDF."},
    {"id": "s_incomplete_beta_function", "kind": "axiom", "name": "Incomplete Beta Function B_x(a,b)",
     "type_signature": "",
     "description": "B_x(a,b) = integral_0^x t^{a-1}(1-t)^{b-1} dt, whose regularized form I_x gives the Beta CDF."},
    {"id": "s_generalized_exponential_integral", "kind": "state", "name": "Generalized Exponential Integral E_p(z)",
     "type_signature": "",
     "description": "E_p(z) = integral_1^infty e^{-zt}/t^p dt, extending E_1 to complex order via E_p(z) = z^{p-1} Gamma(1-p,z)."},

    # ===================================================================
    # CHAPTER 9: AIRY AND RELATED FUNCTIONS
    # ===================================================================
    {"id": "s_airy_differential_equation", "kind": "axiom", "name": "Airy Differential Equation",
     "type_signature": "",
     "description": "The ODE w'' - zw = 0, exhibiting a transition from oscillatory to exponential behavior at z=0."},
    {"id": "s_airy_function_ai", "kind": "axiom", "name": "Airy Function Ai(z)",
     "type_signature": "",
     "description": "The recessive solution of w'' = zw, defined by Ai(z) = (1/pi) integral_0^infty cos(t^3/3 + zt) dt."},
    {"id": "s_airy_function_bi", "kind": "axiom", "name": "Airy Function Bi(z)",
     "type_signature": "",
     "description": "The dominant solution of w'' = zw, exponentially growing as z -> +infty and linearly independent from Ai."},
    {"id": "s_scorer_function_gi", "kind": "state", "name": "Scorer Function Gi(z)",
     "type_signature": "",
     "description": "Particular solution of w'' - zw = 1/pi via Gi(z) = (1/pi) integral_0^infty sin(t^3/3 + zt) dt."},
    {"id": "s_scorer_function_hi", "kind": "state", "name": "Scorer Function Hi(z)",
     "type_signature": "",
     "description": "Particular solution of w'' - zw = 1/pi complementary to Gi, with Hi(z) - Gi(z) = Bi(z)."},
    {"id": "s_airy_integral_representation", "kind": "theorem", "name": "Airy Integral Representation",
     "type_signature": "",
     "description": "Ai(z) = (1/2pi i) integral exp(t^3/3 - zt) dt along a contour from infty e^{-pi i/3} to infty e^{pi i/3}."},

    # ===================================================================
    # CHAPTER 10: BESSEL FUNCTIONS
    # ===================================================================
    {"id": "s_bessel_differential_equation", "kind": "axiom", "name": "Bessel Differential Equation",
     "type_signature": "",
     "description": "The ODE z^2 w'' + z w' + (z^2 - nu^2) w = 0 with regular singularity at z=0 and irregular at infinity."},
    {"id": "s_bessel_function_j_nu", "kind": "axiom", "name": "Bessel Function J_nu(z)",
     "type_signature": "",
     "description": "Bessel function of the first kind, the solution regular at the origin defined by (z/2)^nu sum (-z^2/4)^k/(k! Gamma(nu+k+1))."},
    {"id": "s_bessel_function_y_nu", "kind": "axiom", "name": "Bessel Function Y_nu(z)",
     "type_signature": "",
     "description": "Bessel function of the second kind (Neumann function), singular at the origin, linearly independent from J_nu."},
    {"id": "s_hankel_functions", "kind": "state", "name": "Hankel Functions H_nu^{(1)}(z) and H_nu^{(2)}(z)",
     "type_signature": "",
     "description": "H_nu^{(1)} = J_nu + iY_nu and H_nu^{(2)} = J_nu - iY_nu, representing outgoing and incoming cylindrical waves."},
    {"id": "s_modified_bessel_function_i_nu", "kind": "axiom", "name": "Modified Bessel Function I_nu(z)",
     "type_signature": "",
     "description": "Modified Bessel function of the first kind, exponentially growing solution of z^2w'' + zw' - (z^2+nu^2)w = 0."},
    {"id": "s_modified_bessel_function_k_nu", "kind": "axiom", "name": "Modified Bessel Function K_nu(z)",
     "type_signature": "",
     "description": "Modified Bessel function of the second kind, exponentially decaying for large real positive z."},
    {"id": "s_spherical_bessel_functions", "kind": "state", "name": "Spherical Bessel Functions",
     "type_signature": "",
     "description": "Solutions j_n, y_n, h_n of the radial Helmholtz equation, related to Bessel functions by j_n(z) = sqrt(pi/(2z)) J_{n+1/2}(z)."},
    {"id": "s_kelvin_functions", "kind": "state", "name": "Kelvin Functions ber, bei, ker, kei",
     "type_signature": "",
     "description": "Real and imaginary parts of Bessel functions at complex arguments xe^{3pi i/4}, used in electromagnetic skin-effect calculations."},
    {"id": "s_mittag_leffler_function", "kind": "state", "name": "Mittag-Leffler Function E_{a,b}(z)",
     "type_signature": "",
     "description": "The entire function sum z^k/Gamma(ak+b) generalizing the exponential, fundamental in fractional calculus."},
    {"id": "t_hankel_transform", "kind": "technique", "name": "Hankel Transform",
     "function_signature": "(f(r), order nu) -> F(k) = integral_0^infty f(r) J_nu(kr) r dr",
     "description": "Integral transform with Bessel function kernel, the radial part of the 2D Fourier transform."},
    {"id": "s_bessel_addition_theorem", "kind": "theorem", "name": "Bessel Addition Theorem",
     "type_signature": "",
     "description": "Expresses J_0(R) in terms of J_n at component distances: J_0(|r-r'|) = sum epsilon_n J_n(r) J_n(r') cos n(theta-theta')."},
    {"id": "s_nicholson_integral", "kind": "theorem", "name": "Nicholson's Integral",
     "type_signature": "",
     "description": "J_nu(z)^2 + Y_nu(z)^2 = (8/pi^2) integral_0^infty K_0(2z sinh t) cosh(2nu t) dt."},
    {"id": "s_bessel_integral_representation_poisson", "kind": "theorem", "name": "Poisson Integral for Bessel Functions",
     "type_signature": "",
     "description": "J_nu(z) = (z/2)^nu/(sqrt(pi) Gamma(nu+1/2)) integral_0^pi cos(z cos theta) sin^{2nu}(theta) d theta for Re nu > -1/2."},

    # ===================================================================
    # CHAPTER 11: STRUVE AND RELATED FUNCTIONS
    # ===================================================================
    {"id": "s_struve_function_h_nu", "kind": "axiom", "name": "Struve Function H_nu(z)",
     "type_signature": "",
     "description": "Solution of the inhomogeneous Bessel equation with right-hand side (z/2)^{nu-1}/(sqrt(pi) Gamma(nu+1/2))."},
    {"id": "s_modified_struve_function_l_nu", "kind": "state", "name": "Modified Struve Function L_nu(z)",
     "type_signature": "",
     "description": "L_nu(z) = -ie^{-inu pi/2} H_nu(iz), solving the inhomogeneous modified Bessel equation."},
    {"id": "s_lommel_function_s", "kind": "axiom", "name": "Lommel Functions s_{mu,nu} and S_{mu,nu}",
     "type_signature": "",
     "description": "Particular solutions of the inhomogeneous Bessel equation z^2y'' + zy' + (z^2 - nu^2)y = z^{mu+1}."},
    {"id": "s_anger_function", "kind": "axiom", "name": "Anger Function",
     "type_signature": "",
     "description": "(1/pi) integral_0^pi cos(nu theta - z sin theta) d theta, generalizing J_nu to non-integer order."},
    {"id": "s_weber_function_e_nu", "kind": "axiom", "name": "Weber Function E_nu(z)",
     "type_signature": "",
     "description": "(1/pi) integral_0^pi sin(nu theta - z sin theta) d theta, companion to the Anger function."},

    # ===================================================================
    # CHAPTER 12: PARABOLIC CYLINDER FUNCTIONS
    # ===================================================================
    {"id": "s_parabolic_cylinder_equation", "kind": "axiom", "name": "Parabolic Cylinder Differential Equation",
     "type_signature": "",
     "description": "The ODE w'' + (nu + 1/2 - z^2/4)w = 0 from separation in parabolic coordinates."},
    {"id": "s_parabolic_cylinder_function_u", "kind": "axiom", "name": "Parabolic Cylinder Function U(a,z)",
     "type_signature": "",
     "description": "Standard solution decaying as z -> +infty, expressible via confluent hypergeometric functions."},
    {"id": "s_parabolic_cylinder_function_v", "kind": "axiom", "name": "Parabolic Cylinder Function V(a,z)",
     "type_signature": "",
     "description": "Companion solution growing as z -> +infty, linearly independent from U(a,z)."},
    {"id": "s_weber_parabolic_cylinder_d_nu", "kind": "state", "name": "Weber Parabolic Cylinder Function D_nu(z)",
     "type_signature": "",
     "description": "Classical notation D_nu(z) = U(-nu-1/2, z) for parabolic cylinder functions."},

    # ===================================================================
    # CHAPTER 13: CONFLUENT HYPERGEOMETRIC FUNCTIONS
    # ===================================================================
    {"id": "s_kummer_confluent_equation", "kind": "axiom", "name": "Kummer's Confluent Hypergeometric Equation",
     "type_signature": "",
     "description": "The ODE zw'' + (b-z)w' - aw = 0 with regular singularity at z=0 and irregular singularity at infinity."},
    {"id": "s_kummer_function_m", "kind": "axiom", "name": "Kummer Function M(a,b,z)",
     "type_signature": "",
     "description": "Confluent hypergeometric function 1F1(a;b;z) = sum (a)_k z^k/((b)_k k!), entire in z for b not a non-positive integer."},
    {"id": "s_tricomi_function_u", "kind": "axiom", "name": "Tricomi Function U(a,b,z)",
     "type_signature": "",
     "description": "Second confluent hypergeometric function with U(a,b,z) ~ z^{-a} as z -> infty, unique with this decay."},
    {"id": "s_kummer_transformation", "kind": "theorem", "name": "Kummer Transformation",
     "type_signature": "",
     "description": "M(a,b,z) = e^z M(b-a,b,-z), the fundamental symmetry of confluent hypergeometric functions."},
    {"id": "s_whittaker_differential_equation", "kind": "axiom", "name": "Whittaker Differential Equation",
     "type_signature": "",
     "description": "W'' + (-1/4 + kappa/z + (1/4-mu^2)/z^2)W = 0, alternative form of Kummer's equation."},
    {"id": "s_whittaker_function_m_kappa_mu", "kind": "state", "name": "Whittaker Function M_{kappa,mu}(z)",
     "type_signature": "",
     "description": "Whittaker function related to Kummer M by M_{kappa,mu} = e^{-z/2} z^{mu+1/2} M(mu-kappa+1/2, 2mu+1, z)."},
    {"id": "s_whittaker_function_w_kappa_mu", "kind": "state", "name": "Whittaker Function W_{kappa,mu}(z)",
     "type_signature": "",
     "description": "Whittaker function related to Tricomi U, the recessive solution decaying as z -> infty."},
    {"id": "s_confluent_hypergeometric_limit", "kind": "theorem", "name": "Confluent Hypergeometric Limit",
     "type_signature": "",
     "description": "1F1(a;b;z/b) -> 0F1(;a;z) as b -> infty, the confluence process merging regular singularities."},

    # ===================================================================
    # CHAPTER 14: LEGENDRE AND RELATED FUNCTIONS
    # ===================================================================
    {"id": "s_associated_legendre_equation", "kind": "axiom", "name": "Associated Legendre Differential Equation",
     "type_signature": "",
     "description": "(1-x^2)y'' - 2xy' + [nu(nu+1) - mu^2/(1-x^2)]y = 0, generalizing Legendre's equation with order mu."},
    {"id": "s_ferrers_function_p", "kind": "axiom", "name": "Ferrers Function P_nu^mu(x)",
     "type_signature": "",
     "description": "Associated Legendre function of the first kind on (-1,1), defined via the hypergeometric function."},
    {"id": "s_toroidal_functions", "kind": "state", "name": "Toroidal (Ring) Functions",
     "type_signature": "",
     "description": "Associated Legendre functions with half-integer degree P_{n-1/2}^m(cosh eta) for potential theory in toroidal geometry."},
    {"id": "s_conical_mehler_functions", "kind": "state", "name": "Conical (Mehler) Functions",
     "type_signature": "",
     "description": "Associated Legendre functions P_{-1/2+itau}^mu(x) with complex degree, arising in conical boundary problems."},
    {"id": "t_mehler_fock_transform", "kind": "technique", "name": "Mehler-Fock Transform",
     "function_signature": "(f(x) on (1,infty)) -> F(tau) = integral f(x) P_{-1/2+itau}(x) dx",
     "description": "Integral transform with conical function kernel for axially symmetric potential problems."},
    {"id": "s_legendre_function_second_kind", "kind": "axiom", "name": "Legendre Function of the Second Kind Q_nu(z)",
     "type_signature": "",
     "description": "Q_nu(z) = (pi/2)(cos nu pi P_nu(z) - P_{-nu-1}(z))/sin nu pi, singular at z = +/- 1."},
    {"id": "s_associated_legendre_addition_theorem", "kind": "theorem", "name": "Addition Theorem for Legendre Functions",
     "type_signature": "",
     "description": "P_n(cos gamma) = sum_{m} epsilon_m P_n^m(cos theta) P_n^m(cos theta') cos m(phi-phi') connecting P_n at composed angles."},

    # ===================================================================
    # CHAPTER 15: HYPERGEOMETRIC FUNCTION
    # ===================================================================
    {"id": "s_gauss_hypergeometric_function", "kind": "axiom", "name": "Gauss Hypergeometric Function 2F1(a,b;c;z)",
     "type_signature": "",
     "description": "sum (a)_k(b)_k z^k/((c)_k k!) analytic in |z|<1, satisfying a Fuchsian ODE with 3 regular singular points."},
    {"id": "s_hypergeometric_differential_equation", "kind": "axiom", "name": "Hypergeometric Differential Equation",
     "type_signature": "",
     "description": "z(1-z)w'' + [c-(a+b+1)z]w' - ab w = 0, the Fuchsian equation with regular singularities at 0, 1, infty."},
    {"id": "s_gauss_summation_theorem", "kind": "theorem", "name": "Gauss Summation Theorem",
     "type_signature": "",
     "description": "2F1(a,b;c;1) = Gamma(c)Gamma(c-a-b)/(Gamma(c-a)Gamma(c-b)) when Re(c-a-b) > 0."},
    {"id": "s_chu_vandermonde_identity", "kind": "theorem", "name": "Chu-Vandermonde Identity",
     "type_signature": "",
     "description": "2F1(-n,b;c;1) = (c-b)_n/(c)_n, a terminating Gauss summation."},
    {"id": "s_euler_transformation_hypergeometric", "kind": "theorem", "name": "Euler Transformation for 2F1",
     "type_signature": "",
     "description": "2F1(a,b;c;z) = (1-z)^{c-a-b} 2F1(c-a,c-b;c;z), a fundamental symmetry."},
    {"id": "s_pfaff_transformation", "kind": "theorem", "name": "Pfaff Transformation",
     "type_signature": "",
     "description": "2F1(a,b;c;z) = (1-z)^{-a} 2F1(a,c-b;c;z/(z-1)), mapping the argument fractionally."},
    {"id": "s_riemann_p_symbol", "kind": "axiom", "name": "Riemann Differential Equation and P-symbol",
     "type_signature": "",
     "description": "Most general second-order Fuchsian ODE with three regular singularities, encoded by the Riemann P-symbol."},
    {"id": "s_euler_integral_representation_2f1", "kind": "theorem", "name": "Euler Integral Representation for 2F1",
     "type_signature": "",
     "description": "2F1(a,b;c;z) = B(b,c-b)^{-1} integral_0^1 t^{b-1}(1-t)^{c-b-1}(1-zt)^{-a} dt for Re c > Re b > 0."},
    {"id": "s_kummer_24_solutions", "kind": "theorem", "name": "Kummer's 24 Solutions",
     "type_signature": "",
     "description": "The 24 solutions of the hypergeometric ODE obtained by transforming z -> z, 1-z, 1/z, 1/(1-z), z/(z-1), (z-1)/z and choosing exponents."},

    # ===================================================================
    # CHAPTER 16: GENERALIZED HYPERGEOMETRIC FUNCTIONS
    # ===================================================================
    {"id": "s_generalized_hypergeometric_pfq", "kind": "axiom", "name": "Generalized Hypergeometric Function pFq",
     "type_signature": "",
     "description": "pFq(a_1,...,a_p;b_1,...,b_q;z) = sum (a_1)_k...(a_p)_k z^k/((b_1)_k...(b_q)_k k!)."},
    {"id": "s_pfaff_saalschutz_theorem", "kind": "theorem", "name": "Pfaff-Saalschutz Summation Theorem",
     "type_signature": "",
     "description": "Evaluates terminating balanced 3F2 at z=1 as a ratio of Pochhammer symbols."},
    {"id": "s_dixon_summation_theorem", "kind": "theorem", "name": "Dixon's Summation Theorem",
     "type_signature": "",
     "description": "Evaluates well-poised 3F2(a,b,c;1+a-b,1+a-c;1) as a ratio of Gamma functions."},
    {"id": "s_dougall_summation_theorem", "kind": "theorem", "name": "Dougall Summation Theorem",
     "type_signature": "",
     "description": "Evaluates terminating very-well-poised 7F6(1) as a product of Pochhammer symbols."},
    {"id": "s_meijer_g_function", "kind": "axiom", "name": "Meijer G-Function",
     "type_signature": "",
     "description": "Mellin-Barnes contour integral unifying hypergeometric, Bessel, and other special functions as special cases."},
    {"id": "s_appell_function_f1", "kind": "axiom", "name": "Appell Function F_1",
     "type_signature": "",
     "description": "Two-variable hypergeometric function F_1(a;b,b';c;x,y) with coupled rising factorials."},
    {"id": "s_appell_functions_f2_f3_f4", "kind": "axiom", "name": "Appell Functions F_2, F_3, F_4",
     "type_signature": "",
     "description": "The remaining three Appell two-variable hypergeometric functions with distinct convergence regions."},
    {"id": "s_fox_h_function", "kind": "axiom", "name": "Fox H-Function",
     "type_signature": "",
     "description": "Generalization of the Meijer G-function with arbitrary powers in the Gamma factors, used in fractional calculus and statistics."},
    {"id": "s_bilateral_hypergeometric_series", "kind": "axiom", "name": "Bilateral Hypergeometric Series",
     "type_signature": "",
     "description": "pHq: sum from n=-infty to infty of (a_1)_n...(a_p)_n z^n/((b_1)_n...(b_q)_n), generalizing one-sided series."},
    {"id": "s_clausen_formula", "kind": "theorem", "name": "Clausen's Formula",
     "type_signature": "",
     "description": "[2F1(a,b;a+b+1/2;z)]^2 = 3F2(2a,2b,a+b;2a+2b,a+b+1/2;z), squaring identity for hypergeometric functions."},
    {"id": "s_whipple_transformation", "kind": "theorem", "name": "Whipple's Transformation",
     "type_signature": "",
     "description": "Relates a well-poised 7F6(1) to a balanced 4F3(1), connecting different types of hypergeometric series."},

    # ===================================================================
    # CHAPTER 17: q-HYPERGEOMETRIC AND RELATED FUNCTIONS
    # ===================================================================
    {"id": "s_q_pochhammer_symbol", "kind": "axiom", "name": "q-Pochhammer Symbol (a;q)_n",
     "type_signature": "",
     "description": "(a;q)_n = prod_{k=0}^{n-1} (1-aq^k) for finite n, and (a;q)_infty = prod_{k=0}^infty (1-aq^k)."},
    {"id": "s_q_binomial_coefficient", "kind": "axiom", "name": "q-Binomial Coefficient (Gaussian Binomial)",
     "type_signature": "",
     "description": "[n choose k]_q = (q;q)_n/((q;q)_k(q;q)_{n-k}), counting subspaces of F_q^n."},
    {"id": "s_q_derivative_operator", "kind": "axiom", "name": "q-Derivative Operator D_q",
     "type_signature": "",
     "description": "D_q f(z) = (f(z)-f(qz))/((1-q)z), the q-analog of differentiation reducing to f'(z) as q->1."},
    {"id": "s_q_integral_jackson", "kind": "axiom", "name": "q-Integral (Jackson Integral)",
     "type_signature": "",
     "description": "integral_0^a f(x) d_q x = a(1-q) sum f(aq^k) q^k, the inverse of the q-derivative."},
    {"id": "s_q_binomial_theorem", "kind": "theorem", "name": "q-Binomial Theorem",
     "type_signature": "",
     "description": "sum (a;q)_k z^k/(q;q)_k = (az;q)_infty/(z;q)_infty, the q-analog of the binomial series."},
    {"id": "s_basic_hypergeometric_function", "kind": "axiom", "name": "Basic Hypergeometric Function r+1-phi-s",
     "type_signature": "",
     "description": "q-analog of pFq with q-shifted factorials, converging for all z when s>r and |z|<1 when s=r."},
    {"id": "s_ramanujan_1_psi_1", "kind": "theorem", "name": "Ramanujan's 1-psi-1 Bilateral Summation",
     "type_signature": "",
     "description": "Evaluates the bilateral q-series sum (a;q)_n z^n/(b;q)_n as an infinite product of q-Pochhammer symbols."},
    {"id": "t_bailey_pairs_chain", "kind": "technique", "name": "Bailey Pairs and Bailey Chain",
     "function_signature": "(Bailey pair (alpha_n, beta_n)) -> (Infinitely many new q-series identities)",
     "description": "Iterative mechanism: the Bailey lemma produces new q-hypergeometric identities from existing Bailey pairs."},
    {"id": "s_jacobi_triple_product", "kind": "theorem", "name": "Jacobi Triple Product Identity",
     "type_signature": "",
     "description": "sum_{n=-infty}^infty z^n q^{n^2} = prod (1-q^{2n})(1+zq^{2n-1})(1+z^{-1}q^{2n-1}), fundamental to theta functions and partitions."},
    {"id": "s_q_exponential_functions", "kind": "state", "name": "q-Exponential Functions e_q and E_q",
     "type_signature": "",
     "description": "q-analogs of exp: e_q(z) = sum z^n/(q;q)_n = 1/(z;q)_infty and E_q(z) = sum q^{n(n-1)/2} z^n/(q;q)_n = (-z;q)_infty."},
    {"id": "s_rogers_ramanujan_identities", "kind": "theorem", "name": "Rogers-Ramanujan Identities",
     "type_signature": "",
     "description": "sum q^{n^2}/(q;q)_n = prod 1/((1-q^{5n+1})(1-q^{5n+4})) and sum q^{n^2+n}/(q;q)_n = prod 1/((1-q^{5n+2})(1-q^{5n+3}))."},

    # ===================================================================
    # CHAPTER 18: ORTHOGONAL POLYNOMIALS
    # ===================================================================
    {"id": "s_jacobi_polynomial", "kind": "axiom", "name": "Jacobi Polynomial P_n^{alpha,beta}(x)",
     "type_signature": "",
     "description": "Orthogonal polynomials on [-1,1] with weight (1-x)^alpha(1+x)^beta, the most general classical family on a finite interval."},
    {"id": "s_gegenbauer_polynomial", "kind": "state", "name": "Gegenbauer (Ultraspherical) Polynomial C_n^lambda(x)",
     "type_signature": "",
     "description": "Jacobi polynomials with alpha=beta=lambda-1/2, orthogonal with weight (1-x^2)^{lambda-1/2}."},
    {"id": "s_laguerre_polynomial", "kind": "axiom", "name": "Laguerre Polynomial L_n^alpha(x)",
     "type_signature": "",
     "description": "Orthogonal polynomials on [0,infty) with weight x^alpha e^{-x}, arising as hydrogen atom radial wavefunctions."},
    {"id": "s_christoffel_darboux_formula", "kind": "theorem", "name": "Christoffel-Darboux Formula",
     "type_signature": "",
     "description": "Closed form for the reproducing kernel sum p_k(x)p_k(y)/h_k as a ratio of consecutive polynomials."},
    {"id": "s_favard_theorem", "kind": "theorem", "name": "Favard's Theorem",
     "type_signature": "",
     "description": "Any polynomial sequence satisfying a three-term recurrence with positive coefficients is orthogonal with respect to some positive measure."},
    {"id": "s_hahn_polynomial", "kind": "axiom", "name": "Hahn Polynomial",
     "type_signature": "",
     "description": "Discrete orthogonal polynomials on {0,...,N} with hypergeometric weight, the discrete analog of Jacobi polynomials."},
    {"id": "s_wilson_polynomial", "kind": "axiom", "name": "Wilson Polynomial",
     "type_signature": "",
     "description": "The most general hypergeometric orthogonal polynomials (continuous variable), expressed as 4F3 series atop the Askey scheme."},
    {"id": "s_racah_polynomial", "kind": "axiom", "name": "Racah Polynomial",
     "type_signature": "",
     "description": "The most general discrete hypergeometric orthogonal polynomials, the discrete companion of Wilson polynomials."},
    {"id": "s_askey_scheme", "kind": "state", "name": "Askey Scheme",
     "type_signature": "",
     "description": "Hierarchical classification of hypergeometric orthogonal polynomials by limit relations, with Wilson and Racah at the top."},
    {"id": "s_askey_wilson_polynomial", "kind": "axiom", "name": "Askey-Wilson Polynomial",
     "type_signature": "",
     "description": "Most general q-hypergeometric orthogonal polynomial family defined as a 4_phi_3, atop the q-Askey scheme."},
    {"id": "s_krawtchouk_polynomial", "kind": "state", "name": "Krawtchouk Polynomial",
     "type_signature": "",
     "description": "Discrete orthogonal polynomials on {0,...,N} with binomial weight, characters of the Hamming scheme."},
    {"id": "s_meixner_polynomial", "kind": "state", "name": "Meixner Polynomial",
     "type_signature": "",
     "description": "Discrete orthogonal polynomials on non-negative integers with negative binomial weight."},
    {"id": "s_charlier_polynomial", "kind": "state", "name": "Charlier Polynomial",
     "type_signature": "",
     "description": "Discrete orthogonal polynomials on non-negative integers with Poisson weight."},
    {"id": "s_chebyshev_polynomial_first_kind", "kind": "axiom", "name": "Chebyshev Polynomial of the First Kind T_n(x)",
     "type_signature": "",
     "description": "T_n(cos theta) = cos(n theta), orthogonal on [-1,1] with weight (1-x^2)^{-1/2}, optimal for minimax approximation."},
    {"id": "s_chebyshev_polynomial_second_kind", "kind": "axiom", "name": "Chebyshev Polynomial of the Second Kind U_n(x)",
     "type_signature": "",
     "description": "U_n(cos theta) = sin((n+1)theta)/sin(theta), orthogonal on [-1,1] with weight (1-x^2)^{1/2}."},
    {"id": "s_meixner_pollaczek_polynomial", "kind": "state", "name": "Meixner-Pollaczek Polynomial P_n^lambda(x;phi)",
     "type_signature": "",
     "description": "Continuous orthogonal polynomials on R with weight |Gamma(lambda+ix)|^2 e^{(2phi-pi)x}, in the Askey scheme."},
    {"id": "s_continuous_hahn_polynomial", "kind": "state", "name": "Continuous Hahn Polynomial",
     "type_signature": "",
     "description": "Orthogonal polynomials on R with weight |Gamma(a+ix)Gamma(b+ix)|^2, between Wilson and Meixner-Pollaczek."},
    {"id": "s_continuous_dual_hahn_polynomial", "kind": "state", "name": "Continuous Dual Hahn Polynomial",
     "type_signature": "",
     "description": "Orthogonal polynomials on [0,infty) as a 3F2 at z=-1, dual to continuous Hahn polynomials."},
    {"id": "s_dual_hahn_polynomial", "kind": "state", "name": "Dual Hahn Polynomial",
     "type_signature": "",
     "description": "Discrete orthogonal polynomials dual to Hahn, related to 6j symbols in angular momentum theory."},
    {"id": "s_rodrigues_formula_general", "kind": "theorem", "name": "Rodrigues Formula (General)",
     "type_signature": "",
     "description": "p_n(x) = (1/(k_n w(x))) (d/dx)^n [w(x) sigma(x)^n], generating classical orthogonal polynomials from weight and classification."},
    {"id": "s_three_term_recurrence", "kind": "theorem", "name": "Three-Term Recurrence Relation",
     "type_signature": "",
     "description": "x p_n(x) = a_n p_{n+1}(x) + b_n p_n(x) + c_n p_{n-1}(x), the fundamental structure theorem for orthogonal polynomials."},

    # ===================================================================
    # CHAPTER 19: ELLIPTIC INTEGRALS
    # ===================================================================
    {"id": "s_complete_elliptic_integral_k", "kind": "axiom", "name": "Complete Elliptic Integral K(k)",
     "type_signature": "",
     "description": "K(k) = integral_0^{pi/2} d theta/sqrt(1-k^2 sin^2 theta), the quarter-period of Jacobian elliptic functions."},
    {"id": "s_complete_elliptic_integral_e", "kind": "axiom", "name": "Complete Elliptic Integral E(k)",
     "type_signature": "",
     "description": "E(k) = integral_0^{pi/2} sqrt(1-k^2 sin^2 theta) d theta, giving the arc length of an ellipse."},
    {"id": "s_complete_elliptic_integral_pi", "kind": "axiom", "name": "Complete Elliptic Integral Pi(n,k)",
     "type_signature": "",
     "description": "Pi(n,k) = integral_0^{pi/2} d theta/((1-n sin^2 theta) sqrt(1-k^2 sin^2 theta)), the third-kind integral."},
    {"id": "s_carlson_symmetric_rf", "kind": "axiom", "name": "Carlson Symmetric R_F(x,y,z)",
     "type_signature": "",
     "description": "R_F = (1/2) integral_0^infty [(t+x)(t+y)(t+z)]^{-1/2} dt, symmetric elliptic integral of the first kind."},
    {"id": "s_carlson_symmetric_rj", "kind": "axiom", "name": "Carlson Symmetric R_J(x,y,z,p)",
     "type_signature": "",
     "description": "R_J = (3/2) integral_0^infty [(t+x)(t+y)(t+z)]^{-1/2}(t+p)^{-1} dt, symmetric third-kind integral."},
    {"id": "s_carlson_symmetric_rd", "kind": "axiom", "name": "Carlson Symmetric R_D(x,y,z)",
     "type_signature": "",
     "description": "R_D = R_J(x,y,z,z), special case of R_J with E(k) = R_F(0,k'^2,1) - (k^2/3) R_D(0,k'^2,1)."},
    {"id": "s_carlson_symmetric_rc", "kind": "axiom", "name": "Carlson Symmetric R_C(x,y)",
     "type_signature": "",
     "description": "R_C(x,y) = R_F(x,y,y), degenerate symmetric integral reducing to inverse trig/hyperbolic functions."},
    {"id": "t_arithmetic_geometric_mean", "kind": "technique", "name": "Arithmetic-Geometric Mean M(a,g)",
     "function_signature": "(a_0, g_0) -> AGM limit M with K(k) = pi/(2M(1,k'))",
     "description": "Iterates a_{n+1}=(a_n+g_n)/2, g_{n+1}=sqrt(a_n g_n) with quadratic convergence to compute elliptic integrals."},
    {"id": "t_landen_transformation", "kind": "technique", "name": "Landen Transformation",
     "function_signature": "(Elliptic integral at modulus k) -> (Same value at reduced/increased modulus)",
     "description": "Modulus-changing substitution preserving elliptic integral values, enabling iterative computation."},
    {"id": "s_legendre_relation_elliptic", "kind": "theorem", "name": "Legendre's Relation for Elliptic Integrals",
     "type_signature": "",
     "description": "E(k)K'(k) + E'(k)K(k) - K(k)K'(k) = pi/2, the fundamental relation between complete elliptic integrals."},

    # ===================================================================
    # CHAPTER 20: THETA FUNCTIONS
    # ===================================================================
    {"id": "s_jacobi_theta_1", "kind": "axiom", "name": "Jacobi Theta Function theta_1(z,q)",
     "type_signature": "",
     "description": "The odd Jacobi theta function theta_1 = 2 sum (-1)^n q^{(n+1/2)^2} sin((2n+1)z), vanishing at z=0."},
    {"id": "s_jacobi_theta_2", "kind": "axiom", "name": "Jacobi Theta Function theta_2(z,q)",
     "type_signature": "",
     "description": "The even Jacobi theta function theta_2 = 2 sum q^{(n+1/2)^2} cos((2n+1)z)."},
    {"id": "s_jacobi_theta_3", "kind": "axiom", "name": "Jacobi Theta Function theta_3(z,q)",
     "type_signature": "",
     "description": "theta_3 = 1 + 2 sum q^{n^2} cos(2nz), the basic Jacobi theta function."},
    {"id": "s_jacobi_theta_4", "kind": "axiom", "name": "Jacobi Theta Function theta_4(z,q)",
     "type_signature": "",
     "description": "theta_4 = 1 + 2 sum (-1)^n q^{n^2} cos(2nz), related to theta_3 by a half-period shift."},
    {"id": "s_theta_function_heat_equation", "kind": "theorem", "name": "Theta Function Heat Equation",
     "type_signature": "",
     "description": "Jacobi theta functions satisfy 4pi i partial_tau theta = partial_z^2 theta, connecting them to heat kernels."},
    {"id": "s_jacobi_imaginary_transformation", "kind": "theorem", "name": "Jacobi Imaginary Transformation",
     "type_signature": "",
     "description": "theta_3(z|tau) = (-i tau)^{-1/2} exp(z^2/(pi i tau)) theta_3(z/tau | -1/tau), the modular transformation."},

    # ===================================================================
    # CHAPTER 21: MULTIDIMENSIONAL THETA FUNCTIONS
    # ===================================================================
    {"id": "s_riemann_theta_function", "kind": "axiom", "name": "Riemann Theta Function",
     "type_signature": "",
     "description": "Theta(z|Omega) = sum_{n in Z^g} exp(pi i n^T Omega n + 2pi i n^T z) for g-dimensional z and g x g Riemann matrix Omega."},
    {"id": "s_siegel_modular_group", "kind": "state", "name": "Siegel Modular Group Sp(2g,Z)",
     "type_signature": "",
     "description": "The group of transformations of genus-g Riemann matrices under which Riemann theta functions transform covariantly."},

    # ===================================================================
    # CHAPTER 22: JACOBIAN ELLIPTIC FUNCTIONS
    # ===================================================================
    {"id": "s_jacobian_sn", "kind": "axiom", "name": "Jacobian Elliptic Function sn(z,k)",
     "type_signature": "",
     "description": "The sine-amplitude function inverting F(phi,k), doubly periodic with periods 4K and 2iK'."},
    {"id": "s_jacobian_cn", "kind": "axiom", "name": "Jacobian Elliptic Function cn(z,k)",
     "type_signature": "",
     "description": "The cosine-amplitude function satisfying sn^2 + cn^2 = 1, doubly periodic with periods 4K and 2K+2iK'."},
    {"id": "s_jacobian_dn", "kind": "axiom", "name": "Jacobian Elliptic Function dn(z,k)",
     "type_signature": "",
     "description": "The delta-amplitude function satisfying dn^2 + k^2 sn^2 = 1, doubly periodic with periods 2K and 4iK'."},
    {"id": "s_jacobi_amplitude_function", "kind": "axiom", "name": "Jacobi Amplitude Function am(u,k)",
     "type_signature": "",
     "description": "am(u,k) = phi where u = F(phi,k), the inverse of the incomplete elliptic integral of the first kind."},
    {"id": "s_jacobi_twelve_elliptic_functions", "kind": "state", "name": "Twelve Jacobian Elliptic Functions",
     "type_signature": "",
     "description": "The twelve pq(z,k) functions (p,q in {s,c,d,n}) defined as ratios of any two of H, H_1, Theta, Theta_1 theta functions."},
    {"id": "s_jacobi_elliptic_addition_theorems", "kind": "theorem", "name": "Jacobi Elliptic Addition Theorems",
     "type_signature": "",
     "description": "sn(u+v) = (sn u cn v dn v + sn v cn u dn u)/(1-k^2 sn^2 u sn^2 v) and analogues for cn, dn."},

    # ===================================================================
    # CHAPTER 23: WEIERSTRASS ELLIPTIC AND MODULAR FUNCTIONS
    # ===================================================================
    {"id": "s_weierstrass_p_function", "kind": "axiom", "name": "Weierstrass Elliptic Function wp(z)",
     "type_signature": "",
     "description": "wp(z;omega_1,omega_2) = 1/z^2 + sum'_{m,n} [1/(z-Omega_{m,n})^2 - 1/Omega_{m,n}^2], the canonical elliptic function of order 2."},
    {"id": "s_weierstrass_sigma_function", "kind": "axiom", "name": "Weierstrass Sigma Function sigma(z)",
     "type_signature": "",
     "description": "Entire function with simple zeros at lattice points: sigma(z) = z prod' (1-z/Omega) exp(z/Omega + z^2/(2Omega^2))."},
    {"id": "s_weierstrass_zeta_function", "kind": "axiom", "name": "Weierstrass Zeta Function zeta(z)",
     "type_signature": "",
     "description": "zeta(z) = sigma'(z)/sigma(z) = 1/z + sum' [1/(z-Omega) + 1/Omega + z/Omega^2], a quasi-periodic meromorphic function."},
    {"id": "s_weierstrass_ode", "kind": "axiom", "name": "Weierstrass Differential Equation",
     "type_signature": "",
     "description": "(wp')^2 = 4 wp^3 - g_2 wp - g_3, the ODE defining wp in terms of invariants g_2, g_3."},
    {"id": "s_modular_discriminant_delta", "kind": "axiom", "name": "Modular Discriminant Delta(tau)",
     "type_signature": "",
     "description": "Delta = g_2^3 - 27 g_3^2 = (2pi)^{12} eta(tau)^{24}, a weight-12 cusp form vanishing iff the lattice degenerates."},
    {"id": "s_klein_j_invariant", "kind": "axiom", "name": "Klein j-Invariant j(tau)",
     "type_signature": "",
     "description": "j = 1728 g_2^3/Delta, the unique modular function for SL(2,Z) classifying isomorphism classes of elliptic curves."},
    {"id": "s_eisenstein_series_e2k", "kind": "axiom", "name": "Eisenstein Series E_{2k}(tau)",
     "type_signature": "",
     "description": "E_{2k}(tau) = 1 - (4k/B_{2k}) sum sigma_{2k-1}(n) q^n, modular forms of weight 2k for k >= 2."},
    {"id": "s_elliptic_modular_function_lambda", "kind": "axiom", "name": "Elliptic Modular Function lambda(tau)",
     "type_signature": "",
     "description": "lambda(tau) = theta_2(0,q)^4/theta_3(0,q)^4 = k^2, a modular function for Gamma(2) mapping H to C\\{0,1}."},

    # ===================================================================
    # CHAPTER 24: BERNOULLI AND EULER POLYNOMIALS
    # ===================================================================
    {"id": "s_bernoulli_polynomial", "kind": "axiom", "name": "Bernoulli Polynomial B_n(x)",
     "type_signature": "",
     "description": "Defined by te^{xt}/(e^t-1) = sum B_n(x) t^n/n!, with B_n(0) = B_n the Bernoulli numbers."},
    {"id": "s_euler_polynomial", "kind": "axiom", "name": "Euler Polynomial E_n(x)",
     "type_signature": "",
     "description": "Defined by 2e^{xt}/(e^t+1) = sum E_n(x) t^n/n!, with E_n(1/2) related to Euler numbers."},
    {"id": "s_genocchi_numbers", "kind": "state", "name": "Genocchi Numbers",
     "type_signature": "",
     "description": "G_n = 2(1-2^n)B_n, integers related to Bernoulli numbers with generating function 2t/(e^t+1)."},
    {"id": "s_bernoulli_euler_complement_formula", "kind": "theorem", "name": "Bernoulli-Euler Complement Formula",
     "type_signature": "",
     "description": "B_n(1-x) = (-1)^n B_n(x) and E_n(1-x) = (-1)^n E_n(x), reflection symmetries."},
    {"id": "s_euler_maclaurin_formula", "kind": "theorem", "name": "Euler-Maclaurin Summation Formula",
     "type_signature": "",
     "description": "sum f(k) = integral f(x)dx + f(a)/2 + f(b)/2 + sum B_{2k}/(2k)! (f^{(2k-1)}(b)-f^{(2k-1)}(a)) + R, bridging sums and integrals via Bernoulli numbers."},

    # ===================================================================
    # CHAPTER 25: ZETA AND RELATED FUNCTIONS
    # ===================================================================
    {"id": "s_hurwitz_zeta_function", "kind": "axiom", "name": "Hurwitz Zeta Function zeta(s,a)",
     "type_signature": "",
     "description": "zeta(s,a) = sum_{n=0}^infty (n+a)^{-s} for Re s > 1, generalizing Riemann zeta with zeta(s,1) = zeta(s)."},
    {"id": "s_polylogarithm", "kind": "axiom", "name": "Polylogarithm Li_s(z)",
     "type_signature": "",
     "description": "Li_s(z) = sum z^n/n^s for |z|<=1, generalizing -log(1-z)=Li_1(z) and extending to all s by analytic continuation."},
    {"id": "s_lerch_transcendent", "kind": "axiom", "name": "Lerch Transcendent Phi(z,s,a)",
     "type_signature": "",
     "description": "Phi(z,s,a) = sum z^n/(n+a)^s unifying Hurwitz zeta (z=1), polylogarithm (a=1), and Riemann zeta (z=1,a=1)."},
    {"id": "s_fermi_dirac_integral", "kind": "state", "name": "Fermi-Dirac Integral",
     "type_signature": "",
     "description": "F_s(x) = -Li_{s+1}(-e^x), standard integral for fermion energy distributions in quantum statistics."},
    {"id": "s_bose_einstein_integral", "kind": "state", "name": "Bose-Einstein Integral",
     "type_signature": "",
     "description": "G_s(x) = Li_{s+1}(e^x), the bosonic counterpart to the Fermi-Dirac integral."},
    {"id": "s_stieltjes_constants", "kind": "state", "name": "Stieltjes Constants",
     "type_signature": "",
     "description": "Coefficients gamma_n in the Laurent expansion zeta(s) = 1/(s-1) + sum (-1)^n gamma_n (s-1)^n/n! near s=1."},
    {"id": "s_dirichlet_beta_function", "kind": "axiom", "name": "Dirichlet Beta Function beta(s)",
     "type_signature": "",
     "description": "beta(s) = sum (-1)^n/(2n+1)^s = (1/4^s)(zeta(s,1/4) - zeta(s,3/4)), with beta(1) = pi/4."},
    {"id": "s_clausen_function", "kind": "state", "name": "Clausen Function Cl_2(theta)",
     "type_signature": "",
     "description": "Cl_2(theta) = -integral_0^theta ln|2 sin(t/2)| dt = sum sin(n theta)/n^2, related to the dilogarithm."},

    # ===================================================================
    # CHAPTER 26: COMBINATORIAL ANALYSIS
    # ===================================================================
    {"id": "s_bell_number", "kind": "axiom", "name": "Bell Number B_n",
     "type_signature": "",
     "description": "Number of partitions of {1,...,n}: B_n = sum S(n,k), with e.g.f. exp(e^x-1)."},
    {"id": "s_bell_polynomial", "kind": "axiom", "name": "Bell Polynomial B_{n,k}",
     "type_signature": "",
     "description": "Partial Bell polynomials B_{n,k}(x_1,...,x_{n-k+1}) appearing in Faa di Bruno's formula for composite derivatives."},
    {"id": "s_plane_partition", "kind": "axiom", "name": "Plane Partition",
     "type_signature": "",
     "description": "A 2D array of nonneg integers weakly decreasing along rows and columns, with MacMahon generating function prod(1-q^k)^{-k}."},
    {"id": "s_macmahon_box_formula", "kind": "theorem", "name": "MacMahon Box Formula",
     "type_signature": "",
     "description": "Number of plane partitions in an a x b x c box = prod_{i,j,k} (i+j+k-1)/(i+j+k-2)."},
    {"id": "t_twelvefold_way", "kind": "technique", "name": "Twelvefold Way",
     "function_signature": "(n objects, k boxes, constraint) -> Count",
     "description": "Classification of 12 counting problems by distinguishability of objects/boxes and mapping type."},
    {"id": "s_derangement_number", "kind": "axiom", "name": "Derangement Number D_n",
     "type_signature": "",
     "description": "Number of permutations with no fixed points: D_n = n! sum_{k=0}^n (-1)^k/k!, with D_n/n! -> 1/e."},
    {"id": "s_narayana_number", "kind": "axiom", "name": "Narayana Number N(n,k)",
     "type_signature": "",
     "description": "N(n,k) = (1/n) C(n,k) C(n,k-1), refining Catalan numbers by counting paths by number of peaks."},

    # ===================================================================
    # CHAPTER 27: FUNCTIONS OF NUMBER THEORY
    # ===================================================================
    {"id": "s_jordan_totient_function", "kind": "state", "name": "Jordan's Totient Function J_k(n)",
     "type_signature": "",
     "description": "J_k(n) = n^k prod_{p|n}(1-p^{-k}), counting k-tuples coprime to n; J_1 = Euler totient phi."},
    {"id": "s_ramanujan_tau_function", "kind": "axiom", "name": "Ramanujan Tau Function",
     "type_signature": "",
     "description": "tau(n) defined by Delta(q) = q prod(1-q^n)^{24} = sum tau(n)q^n, a multiplicative function."},
    {"id": "t_lambert_series", "kind": "technique", "name": "Lambert Series",
     "function_signature": "(Arithmetic function f) -> sum f(n) q^n/(1-q^n) = sum (sum_{d|n} f(d)) q^n",
     "description": "Converts between arithmetic functions and their summatory transforms via divisor sums."},
    {"id": "s_liouville_lambda_function", "kind": "state", "name": "Liouville Lambda Function lambda(n)",
     "type_signature": "",
     "description": "lambda(n) = (-1)^{Omega(n)} where Omega counts prime factors with multiplicity; Dirichlet series zeta(2s)/zeta(s)."},
    {"id": "s_von_mangoldt_function", "kind": "axiom", "name": "Von Mangoldt Function Lambda(n)",
     "type_signature": "",
     "description": "Lambda(n) = ln p if n=p^k for some prime p and k >= 1, else 0; Dirichlet series -zeta'(s)/zeta(s)."},
    {"id": "s_dedekind_sum", "kind": "state", "name": "Dedekind Sum s(h,k)",
     "type_signature": "",
     "description": "s(h,k) = sum_{r=1}^{k-1} ((r/k))((hr/k)) with sawtooth function ((x)), appearing in the transformation of log eta(tau)."},
    {"id": "s_ramanujan_sum", "kind": "state", "name": "Ramanujan Sum c_q(n)",
     "type_signature": "",
     "description": "c_q(n) = sum_{(a,q)=1} e^{2pi i an/q}, a multiplicative function of q used in Ramanujan expansions of arithmetic functions."},
    {"id": "s_kloosterman_sum", "kind": "state", "name": "Kloosterman Sum S(m,n;c)",
     "type_signature": "",
     "description": "S(m,n;c) = sum_{d mod c, gcd(d,c)=1} exp(2pi i(md+nd')/c), bounded by |S| <= d(c) sqrt(c) (Weil bound)."},

    # ===================================================================
    # CHAPTER 28: MATHIEU FUNCTIONS AND HILL'S EQUATION
    # ===================================================================
    {"id": "s_mathieu_equation", "kind": "axiom", "name": "Mathieu Equation",
     "type_signature": "",
     "description": "The ODE w'' + (a - 2q cos 2z)w = 0 arising from the wave equation in elliptic cylinder coordinates."},
    {"id": "s_mathieu_characteristic_values", "kind": "axiom", "name": "Mathieu Characteristic Values a_n(q), b_n(q)",
     "type_signature": "",
     "description": "Eigenvalues of Mathieu's equation for which periodic solutions of period pi or 2pi exist."},
    {"id": "s_mathieu_function_ce", "kind": "axiom", "name": "Mathieu Function ce_n(z,q)",
     "type_signature": "",
     "description": "Even periodic Mathieu eigenfunction with eigenvalue a_n(q), reducing to cos(nz) when q=0."},
    {"id": "s_mathieu_function_se", "kind": "axiom", "name": "Mathieu Function se_n(z,q)",
     "type_signature": "",
     "description": "Odd periodic Mathieu eigenfunction with eigenvalue b_n(q), reducing to sin(nz) when q=0."},
    {"id": "s_modified_mathieu_equation", "kind": "axiom", "name": "Modified Mathieu Equation",
     "type_signature": "",
     "description": "w'' - (a - 2q cosh 2z)w = 0 from Mathieu's equation by z -> iz, for radial separation."},
    {"id": "s_hill_equation", "kind": "axiom", "name": "Hill's Equation",
     "type_signature": "",
     "description": "The ODE w'' + Q(z)w = 0 with periodic Q, generalizing Mathieu's equation to arbitrary periodic potentials."},
    {"id": "s_hill_discriminant", "kind": "state", "name": "Hill Discriminant",
     "type_signature": "",
     "description": "Delta(lambda) = w_1(pi) + w_2'(pi), whose values +/-2 locate stability band edges of Hill's equation."},
    {"id": "s_mathieu_floquet_solution", "kind": "state", "name": "Mathieu-Floquet Solution",
     "type_signature": "",
     "description": "Solution of Mathieu's equation of the form e^{i nu z} P(z) with P periodic, where nu is the Floquet exponent."},

    # ===================================================================
    # CHAPTER 29: LAME FUNCTIONS
    # ===================================================================
    {"id": "s_lame_equation", "kind": "axiom", "name": "Lame Equation",
     "type_signature": "",
     "description": "d^2w/dz^2 + (h - nu(nu+1)k^2 sn^2(z,k))w = 0, a doubly-periodic potential eigenvalue problem."},
    {"id": "s_lame_polynomials", "kind": "axiom", "name": "Lame Polynomials",
     "type_signature": "",
     "description": "Polynomial solutions of the Lame equation for integer nu, classified into eight types by parity structure."},
    {"id": "s_ellipsoidal_harmonics", "kind": "state", "name": "Ellipsoidal Harmonics",
     "type_signature": "",
     "description": "Products of Lame functions in confocal ellipsoidal coordinates, generalizing spherical harmonics."},
    {"id": "s_lame_eigenvalues", "kind": "state", "name": "Lame Eigenvalues",
     "type_signature": "",
     "description": "The 2nu+1 eigenvalues h of Lame's equation for integer nu, organized by parity and node structure."},

    # ===================================================================
    # CHAPTER 30: SPHEROIDAL WAVE FUNCTIONS
    # ===================================================================
    {"id": "s_spheroidal_equation", "kind": "axiom", "name": "Spheroidal Differential Equation",
     "type_signature": "",
     "description": "d/dz[(1-z^2)dw/dz] + [lambda + gamma^2(1-z^2) - mu^2/(1-z^2)]w = 0 from Helmholtz in spheroidal coords."},
    {"id": "s_angular_spheroidal_wave_function", "kind": "axiom", "name": "Angular Spheroidal Wave Function Ps_n^m",
     "type_signature": "",
     "description": "Eigenfunction on [-1,1] reducing to Ferrers P_n^m when gamma=0, used in antenna and scattering theory."},
    {"id": "s_radial_spheroidal_wave_functions", "kind": "axiom", "name": "Radial Spheroidal Wave Functions",
     "type_signature": "",
     "description": "Four kinds of radial solutions analogous to spherical Bessel functions, for the exterior region."},
    {"id": "s_spheroidal_eigenvalues", "kind": "state", "name": "Spheroidal Eigenvalues lambda_n^m(gamma^2)",
     "type_signature": "",
     "description": "Eigenvalues of the angular spheroidal equation, reducing to n(n+1) when gamma=0."},
    {"id": "s_prolate_spheroidal_function", "kind": "state", "name": "Prolate Spheroidal Wave Function",
     "type_signature": "",
     "description": "Angular spheroidal function with gamma^2 > 0, bandlimited functions with maximal spatial concentration (Slepian)."},

    # ===================================================================
    # CHAPTER 31: HEUN FUNCTIONS
    # ===================================================================
    {"id": "s_heun_equation", "kind": "axiom", "name": "Heun's Equation",
     "type_signature": "",
     "description": "Most general second-order Fuchsian ODE with four regular singular points at {0, 1, a, infty}."},
    {"id": "s_heun_function", "kind": "axiom", "name": "Heun Function Hl",
     "type_signature": "",
     "description": "Local Frobenius solution Hl(a,q;alpha,beta,gamma,delta;z) analytic at z=0 with accessory parameter q."},
    {"id": "s_accessory_parameter", "kind": "axiom", "name": "Accessory Parameter",
     "type_signature": "",
     "description": "The parameter q in Heun's equation not determined by exponents, controlling global connection behavior."},
    {"id": "s_confluent_heun_equation", "kind": "axiom", "name": "Confluent Heun Equation",
     "type_signature": "",
     "description": "Heun equation with two regular singularities merged into one irregular, having three singularities total."},
    {"id": "s_biconfluent_heun_equation", "kind": "state", "name": "Biconfluent Heun Equation",
     "type_signature": "",
     "description": "Heun equation with three regular singularities merged into one irregular of rank 2 plus one regular."},
    {"id": "s_triconfluent_heun_equation", "kind": "state", "name": "Triconfluent Heun Equation",
     "type_signature": "",
     "description": "Maximally confluent Heun equation with one irregular singularity at infinity."},
    {"id": "s_heun_192_local_solutions", "kind": "state", "name": "Heun's 192 Local Solutions",
     "type_signature": "",
     "description": "The 192 = 4 x 48 local Frobenius solutions of Heun's equation at its four singular points, generalizing Kummer's 24."},

    # ===================================================================
    # CHAPTER 32: PAINLEVE TRANSCENDENTS
    # ===================================================================
    {"id": "s_painleve_equation_p1", "kind": "axiom", "name": "First Painleve Equation P_I",
     "type_signature": "",
     "description": "y'' = 6y^2 + z, the simplest Painleve transcendent with no free parameters."},
    {"id": "s_painleve_equation_p2", "kind": "axiom", "name": "Second Painleve Equation P_II",
     "type_signature": "",
     "description": "y'' = 2y^3 + zy + alpha, with Airy function solutions when alpha = n + 1/2."},
    {"id": "s_painleve_equation_p3", "kind": "axiom", "name": "Third Painleve Equation P_III",
     "type_signature": "",
     "description": "y'' = (y')^2/y - y'/z + (alpha y^2 + beta)/z + gamma y^3 + delta/y, with Bessel function solutions."},
    {"id": "s_painleve_equation_p4", "kind": "axiom", "name": "Fourth Painleve Equation P_IV",
     "type_signature": "",
     "description": "2yy'' = (y')^2 + 3y^4 + 8zy^3 + 4(z^2-alpha)y^2 + 2beta, with parabolic cylinder function solutions."},
    {"id": "s_painleve_equation_p5", "kind": "axiom", "name": "Fifth Painleve Equation P_V",
     "type_signature": "",
     "description": "Most complex Painleve equation with four parameters, with Whittaker/confluent hypergeometric solutions."},
    {"id": "s_painleve_equation_p6", "kind": "axiom", "name": "Sixth Painleve Equation P_VI",
     "type_signature": "",
     "description": "Most general Painleve equation with four parameters, containing P_I-P_V as coalescence limits."},
    {"id": "s_painleve_coalescence_cascade", "kind": "theorem", "name": "Painleve Coalescence Cascade",
     "type_signature": "",
     "description": "Limiting process P_VI->P_V->P_IV->P_II->P_I and P_V->P_III->P_II relating all six Painleve equations."},
    {"id": "t_backlund_transformations_painleve", "kind": "technique", "name": "Backlund Transformations for Painleve",
     "function_signature": "(Solution y(z; params)) -> (Solution y~(z; shifted params))",
     "description": "Rational transformations mapping Painleve solutions to solutions with shifted parameter values."},
    {"id": "s_isomonodromic_deformation_connection", "kind": "theorem", "name": "Isomonodromic Deformation Connection",
     "type_signature": "",
     "description": "Each Painleve equation is the compatibility condition for isomonodromic deformation of an associated linear system."},
    {"id": "s_painleve_property", "kind": "axiom", "name": "Painleve Property",
     "type_signature": "",
     "description": "An ODE has the Painleve property if all movable singularities of all solutions are poles (no movable branch points or essential singularities)."},
    {"id": "s_tracy_widom_distribution", "kind": "state", "name": "Tracy-Widom Distribution",
     "type_signature": "",
     "description": "F_2(s) = exp(-integral_s^infty (x-s) q(x)^2 dx) where q solves P_II with q(x) ~ Ai(x), distribution of largest eigenvalue of GUE."},

    # ===================================================================
    # CHAPTER 33: COULOMB FUNCTIONS
    # ===================================================================
    {"id": "s_coulomb_wave_equation", "kind": "axiom", "name": "Coulomb Wave Equation",
     "type_signature": "",
     "description": "d^2w/drho^2 + (1 - 2eta/rho - l(l+1)/rho^2)w = 0 for scattering in a Coulomb field."},
    {"id": "s_regular_coulomb_function", "kind": "axiom", "name": "Regular Coulomb Function F_l(eta,rho)",
     "type_signature": "",
     "description": "Regular solution vanishing at origin, normalized by the Gamow factor C_l(eta)."},
    {"id": "s_irregular_coulomb_functions", "kind": "axiom", "name": "Irregular Coulomb Functions G_l, H_l^{+/-}",
     "type_signature": "",
     "description": "Irregular solution G_l and Coulomb-Hankel functions H_l^{+/-} = G_l +/- iF_l for scattering theory."},
    {"id": "s_gamow_sommerfeld_factor", "kind": "state", "name": "Gamow-Sommerfeld Factor",
     "type_signature": "",
     "description": "C_0^2(eta) = 2pi eta/(e^{2pi eta}-1), the Coulomb barrier penetration probability for nuclear reactions."},
    {"id": "s_coulomb_phase_shift", "kind": "state", "name": "Coulomb Phase Shift sigma_l(eta)",
     "type_signature": "",
     "description": "sigma_l(eta) = arg Gamma(l+1+i eta), the phase shift from the long-range Coulomb potential."},

    # ===================================================================
    # CHAPTER 34: 3j, 6j, 9j SYMBOLS
    # ===================================================================
    {"id": "s_wigner_3j_symbol", "kind": "axiom", "name": "Wigner 3j Symbol",
     "type_signature": "",
     "description": "Coupling coefficient (j1 j2 j3; m1 m2 m3) for three angular momenta summing to zero total."},
    {"id": "s_6j_symbol", "kind": "axiom", "name": "6j Symbol (Racah Coefficient)",
     "type_signature": "",
     "description": "Recoupling coefficient {j1 j2 j3; l1 l2 l3} for three angular momenta, expressible as a 4F3 series."},
    {"id": "s_9j_symbol", "kind": "axiom", "name": "9j Symbol",
     "type_signature": "",
     "description": "Recoupling coefficient for four angular momenta, a sum of products of three 6j symbols."},
    {"id": "s_gaunt_coefficient", "kind": "state", "name": "Gaunt Coefficient",
     "type_signature": "",
     "description": "Integral of three spherical harmonics over the sphere, equal to a product of two 3j symbols."},
    {"id": "s_biedenharn_elliott_identity", "kind": "theorem", "name": "Biedenharn-Elliott Identity",
     "type_signature": "",
     "description": "Pentagon identity: sum of product of three 6j symbols over intermediate j equals a product of two 6j symbols."},
    {"id": "s_clebsch_gordan_coefficient", "kind": "axiom", "name": "Clebsch-Gordan Coefficient",
     "type_signature": "",
     "description": "C^{j,m}_{j_1,m_1,j_2,m_2} coupling two angular momenta j_1+j_2 to resultant j, related to 3j by phase and sqrt factor."},
    {"id": "s_wigner_d_matrix", "kind": "axiom", "name": "Wigner D-Matrix D^j_{m'm}(alpha,beta,gamma)",
     "type_signature": "",
     "description": "Matrix elements of rotation operators in angular momentum basis, D^j_{m'm} = e^{-im'alpha} d^j_{m'm}(beta) e^{-im gamma}."},

    # ===================================================================
    # CHAPTER 35: FUNCTIONS OF MATRIX ARGUMENT
    # ===================================================================
    {"id": "s_multivariate_gamma_function", "kind": "axiom", "name": "Multivariate Gamma Function Gamma_m(a)",
     "type_signature": "",
     "description": "Gamma_m(a) = pi^{m(m-1)/4} prod Gamma(a-(j-1)/2), arising in matrix variate distributions."},
    {"id": "s_zonal_polynomials", "kind": "axiom", "name": "Zonal Polynomials Z_kappa(T)",
     "type_signature": "",
     "description": "Symmetric polynomials in eigenvalues of symmetric matrix T, the spherical functions of GL(m)/O(m)."},
    {"id": "s_hypergeometric_matrix_argument", "kind": "axiom", "name": "Hypergeometric Function of Matrix Argument",
     "type_signature": "",
     "description": "pF_q with matrix argument via sum over partitions of zonal polynomial expansions."},
    {"id": "s_wishart_distribution", "kind": "state", "name": "Wishart Distribution",
     "type_signature": "",
     "description": "Distribution of S = X^T X for Gaussian X, with density involving |S|^{(n-p-1)/2} exp(-tr Sigma^{-1}S/2) / (Gamma_p(n/2) |Sigma|^{n/2})."},
    {"id": "s_jack_polynomial", "kind": "state", "name": "Jack Polynomial P_kappa^{(alpha)}",
     "type_signature": "",
     "description": "Symmetric polynomials generalizing Schur polynomials (alpha=1) and zonal polynomials (alpha=2), indexed by partitions."},

    # ===================================================================
    # CHAPTER 36: INTEGRALS WITH COALESCING SADDLES
    # ===================================================================
    {"id": "s_cuspoid_canonical_integral", "kind": "axiom", "name": "Cuspoid Canonical Integral Psi_K",
     "type_signature": "",
     "description": "Psi_K(x) = integral exp(i(t^{K+2} + x_K t^K + ... + x_1 t)) dt, the K-th cuspoid diffraction integral."},
    {"id": "s_pearcey_integral", "kind": "state", "name": "Pearcey Integral",
     "type_signature": "",
     "description": "The K=2 cuspoid integral integral exp(i(t^4 + x_2 t^2 + x_1 t)) dt, governing cusp diffraction."},
    {"id": "s_swallowtail_integral", "kind": "state", "name": "Swallowtail Canonical Integral",
     "type_signature": "",
     "description": "The K=3 cuspoid integral integral exp(i(t^5 + zt^3 + yt^2 + xt)) dt for swallowtail diffraction."},
    {"id": "s_elliptic_umbilic_catastrophe", "kind": "axiom", "name": "Elliptic Umbilic Catastrophe",
     "type_signature": "",
     "description": "Catastrophe with phase s^3 - 3st^2 + z(s^2+t^2) + ys + xt, possessing three-fold rotational symmetry."},
    {"id": "s_hyperbolic_umbilic_catastrophe", "kind": "axiom", "name": "Hyperbolic Umbilic Catastrophe",
     "type_signature": "",
     "description": "Catastrophe with phase s^3 + t^3 + zst + ys + xt, dual to the elliptic umbilic."},
    {"id": "s_butterfly_canonical_integral", "kind": "state", "name": "Butterfly Canonical Integral",
     "type_signature": "",
     "description": "The K=4 cuspoid integral with phase t^6 + x_4 t^4 + x_3 t^3 + x_2 t^2 + x_1 t, the butterfly catastrophe."},

    # ===================================================================
    # ADDITIONAL CROSS-CUTTING NODES
    # ===================================================================
    # Key transforms and techniques not yet present
    {"id": "t_hilbert_transform", "kind": "technique", "name": "Hilbert Transform",
     "function_signature": "(f(x)) -> H[f](x) = P.V. (1/pi) integral f(t)/(t-x) dt",
     "description": "Singular integral transform producing the analytic signal; maps cos to sin and connects real/imaginary parts of boundary values."},
    {"id": "t_abel_transform", "kind": "technique", "name": "Abel Transform",
     "function_signature": "(f(r)) -> F(y) = 2 integral_y^infty f(r) r dr/sqrt(r^2-y^2)",
     "description": "Integral transform for recovering radial profiles from projected data, inverse via Abel inversion formula."},
    {"id": "t_hankel_contour_method", "kind": "technique", "name": "Hankel Contour Method",
     "function_signature": "(Meromorphic integrand) -> (Sum of residues via keyhole contour)",
     "description": "Evaluates integrals and sums using a contour wrapping the negative real axis, fundamental for Gamma and 1/Gamma representations."},

    # Important special function relationships
    {"id": "s_bateman_function", "kind": "state", "name": "Bateman's Function k_nu(x)",
     "type_signature": "",
     "description": "k_nu(x) = (2/pi) integral_0^{pi/2} cos(x tan theta - nu theta) d theta, related to Bessel functions."},
    {"id": "s_wright_function", "kind": "state", "name": "Wright Function W_{lambda,mu}(z)",
     "type_signature": "",
     "description": "W_{lambda,mu}(z) = sum z^n/(n! Gamma(lambda n + mu)), generalizing Airy functions (lambda = +/-1/3) and Mittag-Leffler."},
    {"id": "s_fox_wright_psi_function", "kind": "state", "name": "Fox-Wright Psi Function",
     "type_signature": "",
     "description": "p_Psi_q: generalized hypergeometric series with Gamma ratios allowing non-unit increments, interpolating between pFq and H-function."},

    # Modular/automorphic supplements
    {"id": "s_dedekind_eta_function", "kind": "axiom", "name": "Dedekind Eta Function eta(tau)",
     "type_signature": "",
     "description": "eta(tau) = q^{1/24} prod_{n=1}^infty (1-q^n) for q=e^{2pi i tau}, a weight-1/2 modular form with multiplier system."},
    {"id": "s_weber_modular_function", "kind": "state", "name": "Weber Modular Functions f, f_1, f_2",
     "type_signature": "",
     "description": "f(tau) = e^{-pi i/24} eta((tau+1)/2)/eta(tau), algebraic at CM points and used in class field theory."},

    # Additional classical results
    {"id": "s_darboux_christoffel_kernel", "kind": "state", "name": "Darboux-Christoffel Kernel",
     "type_signature": "",
     "description": "K_n(x,y) = sum_{k=0}^n p_k(x) p_k(y)/h_k, the reproducing kernel whose diagonal gives the density of states."},
    {"id": "s_turán_inequality", "kind": "theorem", "name": "Turan Inequality for Orthogonal Polynomials",
     "type_signature": "",
     "description": "P_n(x)^2 - P_{n-1}(x) P_{n+1}(x) >= 0 for x in [-1,1], a universal positivity result for Legendre polynomials."},

    # Number theory supplements
    {"id": "s_dirichlet_character", "kind": "axiom", "name": "Dirichlet Character chi mod q",
     "type_signature": "",
     "description": "A completely multiplicative function chi: Z -> C with period q and chi(n) = 0 when gcd(n,q) > 1."},
    {"id": "s_gauss_sum", "kind": "axiom", "name": "Gauss Sum g(chi)",
     "type_signature": "",
     "description": "g(chi) = sum_{a=1}^q chi(a) e^{2pi ia/q}, with |g(chi)| = sqrt(q) for primitive chi."},
    {"id": "s_jacobi_sum", "kind": "axiom", "name": "Jacobi Sum J(chi_1, chi_2)",
     "type_signature": "",
     "description": "J(chi_1,chi_2) = sum_{a+b=1} chi_1(a) chi_2(b) = g(chi_1)g(chi_2)/g(chi_1 chi_2), product of Gauss sums."},

    # Functional equations
    {"id": "s_riemann_xi_function", "kind": "axiom", "name": "Riemann Xi Function xi(s)",
     "type_signature": "",
     "description": "xi(s) = (1/2)s(s-1) pi^{-s/2} Gamma(s/2) zeta(s), entire and satisfying xi(s) = xi(1-s)."},
    {"id": "s_functional_equation_hurwitz_zeta", "kind": "theorem", "name": "Functional Equation for Hurwitz Zeta",
     "type_signature": "",
     "description": "zeta(1-s,a) = Gamma(s)/(2pi)^s [e^{-pi is/2} F(a,s) + e^{pi is/2} F(-a,s)] with F the periodic zeta function."},

    # Statistical mechanics connections
    {"id": "s_partition_function_stat_mech", "kind": "state", "name": "Partition Function (Statistical Mechanics) Z",
     "type_signature": "",
     "description": "Z = sum_states exp(-E/kT), the normalizing factor in Boltzmann statistics from which thermodynamic quantities derive."},

    # Painleve-related
    {"id": "s_hamiltonians_painleve", "kind": "state", "name": "Painleve Hamiltonians",
     "type_signature": "",
     "description": "Each Painleve equation admits a Hamiltonian formulation y' = dH/dq, q' = -dH/dy with polynomial Hamiltonian H."},
    {"id": "s_painleve_tau_function", "kind": "state", "name": "Painleve Tau Function",
     "type_signature": "",
     "description": "tau(z) defined by d/dz ln tau = H(z), entire function whose zeros encode the poles of the Painleve transcendent."},

    # Separation of variables / coordinate systems
    {"id": "t_separation_of_variables", "kind": "technique", "name": "Separation of Variables in Coordinate Systems",
     "function_signature": "(PDE in orthogonal coordinates) -> (System of ODEs for each coordinate)",
     "description": "Decomposes PDEs into ODEs by exploiting coordinate symmetry; 11 coordinate systems separate the Helmholtz equation."},

    # Connection formulas
    {"id": "s_connection_formulas_hypergeometric", "kind": "theorem", "name": "Connection Formulas for 2F1",
     "type_signature": "",
     "description": "Express solutions at one singularity as linear combinations of solutions at another, with coefficients involving Gamma functions."},

    # Additional important identities
    {"id": "s_lipschitz_summation_formula", "kind": "theorem", "name": "Lipschitz Summation Formula",
     "type_signature": "",
     "description": "sum_{n=0}^infty (n+a)^{-s} e^{2pi in z} = Gamma(s)^{-1} sum_{n=-infty}^infty 1/(z-n+a)^s for Im z > 0, connecting Hurwitz zeta to periodic sums."},
    {"id": "s_ramanujan_master_theorem", "kind": "theorem", "name": "Ramanujan's Master Theorem",
     "type_signature": "",
     "description": "If f(x) = sum (-1)^n phi(n) x^n/n!, then integral_0^infty x^{s-1} f(x) dx = Gamma(s) phi(-s), a Mellin transform result."},

    # More orthogonal polynomial families
    {"id": "s_big_q_jacobi_polynomial", "kind": "state", "name": "Big q-Jacobi Polynomial",
     "type_signature": "",
     "description": "q-analog of Jacobi polynomials on a q-linear lattice, in the q-Askey scheme between Askey-Wilson and q-Hahn."},
    {"id": "s_little_q_jacobi_polynomial", "kind": "state", "name": "Little q-Jacobi Polynomial",
     "type_signature": "",
     "description": "Simpler q-analog of Jacobi polynomials on {q^k}, a limiting case of big q-Jacobi polynomials."},
    {"id": "s_al_salam_chihara_polynomial", "kind": "state", "name": "Al-Salam-Chihara Polynomial",
     "type_signature": "",
     "description": "q-orthogonal polynomials on [-1,1] defined as 3_phi_2, in the q-Askey scheme below Askey-Wilson."},
    {"id": "s_q_racah_polynomial", "kind": "state", "name": "q-Racah Polynomial",
     "type_signature": "",
     "description": "q-analog of Racah polynomials atop the discrete branch of the q-Askey scheme."},
    {"id": "s_q_hahn_polynomial", "kind": "state", "name": "q-Hahn Polynomial",
     "type_signature": "",
     "description": "q-analog of Hahn polynomials, discrete orthogonal on {1, q, ..., q^N}."},

    # Integral equations
    {"id": "s_volterra_integral_equation", "kind": "axiom", "name": "Volterra Integral Equation",
     "type_signature": "",
     "description": "f(x) = g(x) + lambda integral_a^x K(x,t) f(t) dt, with variable upper limit making it uniquely solvable."},
    {"id": "s_fredholm_integral_equation", "kind": "axiom", "name": "Fredholm Integral Equation",
     "type_signature": "",
     "description": "f(x) = g(x) + lambda integral_a^b K(x,t) f(t) dt, with fixed limits; solvability governed by Fredholm theory."},

    # Additional generating functions / transforms
    {"id": "s_appell_sequence", "kind": "state", "name": "Appell Sequence",
     "type_signature": "",
     "description": "A polynomial sequence {p_n} with d/dx p_n = n p_{n-1}, including Bernoulli, Euler, and Hermite polynomials."},
    {"id": "s_sheffer_sequence", "kind": "state", "name": "Sheffer Sequence",
     "type_signature": "",
     "description": "Polynomial sequence defined by generating function A(t) exp(x B(t)) = sum p_n(x) t^n/n!, generalizing Appell sequences."},

    # More Ch. 9/10/13 supplements
    {"id": "s_bessel_zeros", "kind": "state", "name": "Zeros of Bessel Functions",
     "type_signature": "",
     "description": "The positive zeros j_{nu,s} of J_nu(z) are real, simple, and interlace with zeros of J_{nu+1}; asymptotically j_{nu,s} ~ (s+nu/2-1/4)pi."},
    {"id": "s_debye_expansion_bessel", "kind": "theorem", "name": "Debye Asymptotic Expansion for Bessel Functions",
     "type_signature": "",
     "description": "Uniform large-order expansion J_nu(nu z) ~ (phi/sqrt(1-z^2))^{1/2} [Ai(nu^{2/3}phi)/(nu^{1/3})] sum, valid through the transition region."},
    {"id": "s_olver_uniform_asymptotics_bessel", "kind": "theorem", "name": "Olver Uniform Asymptotic Expansion",
     "type_signature": "",
     "description": "Uniform expansion of J_nu(nu z) valid for all z including the turning point, involving Airy functions and their derivatives."},

    # More Weierstrass/elliptic
    {"id": "s_weierstrass_addition_theorem", "kind": "theorem", "name": "Weierstrass Addition Theorem",
     "type_signature": "",
     "description": "wp(u+v) = -wp(u) - wp(v) + (1/4)((wp'(u)-wp'(v))/(wp(u)-wp(v)))^2, the algebraic addition law."},
    {"id": "s_abel_theorem_elliptic", "kind": "theorem", "name": "Abel's Theorem for Elliptic Functions",
     "type_signature": "",
     "description": "For an elliptic function f of order n, the sum of zeros minus sum of poles in a period parallelogram is a lattice point."},

    # More asymptotic techniques
    {"id": "t_stationary_phase_method", "kind": "technique", "name": "Method of Stationary Phase",
     "function_signature": "(Oscillatory integral integral e^{i lambda phi(x)} A(x) dx, lambda -> infty) -> (Asymptotic expansion)",
     "description": "Asymptotic evaluation of oscillatory integrals via contributions from critical points of the phase phi(x)."},
    {"id": "t_watson_transformation", "kind": "technique", "name": "Watson Transformation",
     "function_signature": "(Slowly convergent partial-wave series) -> (Contour integral in complex angular momentum)",
     "description": "Converts a sum over angular momentum into a contour integral, enabling asymptotic evaluation of scattering amplitudes."},

    # Analytic number theory functions
    {"id": "s_dirichlet_series", "kind": "axiom", "name": "Dirichlet Series",
     "type_signature": "",
     "description": "A series sum a_n n^{-s} converging in a half-plane Re s > sigma_c, with abscissae of convergence/absolute convergence."},
    {"id": "s_perron_formula", "kind": "theorem", "name": "Perron's Formula",
     "type_signature": "",
     "description": "sum_{n<=x} a_n = (1/2pi i) integral_{c-iT}^{c+iT} F(s) x^s/s ds + error, recovering partial sums from Dirichlet series."},

    # Matrix functions
    {"id": "s_matrix_exponential", "kind": "axiom", "name": "Matrix Exponential exp(A)",
     "type_signature": "",
     "description": "exp(A) = sum A^n/n!, the fundamental solution operator for dx/dt = Ax with exp((s+t)A) = exp(sA) exp(tA)."},

    # Probability-connected
    {"id": "s_marcenko_pastur_distribution", "kind": "state", "name": "Marchenko-Pastur Distribution",
     "type_signature": "",
     "description": "Limiting spectral distribution of Wishart matrices X^TX/n as p/n -> gamma, with density on [(1-sqrt(gamma))^2, (1+sqrt(gamma))^2]."},

    # More combinatorial
    {"id": "s_motzkin_number", "kind": "axiom", "name": "Motzkin Number M_n",
     "type_signature": "",
     "description": "Number of paths from (0,0) to (n,0) with steps (1,1), (1,-1), (1,0) staying nonneg; M_n = sum C(n,2k) C_k."},
    {"id": "s_schroder_number", "kind": "axiom", "name": "Schroder Number",
     "type_signature": "",
     "description": "Number of lattice paths from (0,0) to (n,n) with steps (1,0), (0,1), (1,1) not crossing the diagonal."},
]

# ---------------------------------------------------------------------------
# 3. Add nodes, skipping any with existing IDs
# ---------------------------------------------------------------------------
added = 0
skipped = 0
for node in new_nodes:
    if node['id'] in existing_ids:
        skipped += 1
    else:
        graph['nodes'].append(node)
        existing_ids.add(node['id'])
        added += 1

print(f"Nodes: {added} added, {skipped} skipped (already existed)")

# ---------------------------------------------------------------------------
# 4. Create edges connecting new nodes to existing graph
# ---------------------------------------------------------------------------
max_eid = max(int(e['id'].replace('e_', '')) for e in graph['edges'])
eid = max_eid + 1
edges_added = 0

def add_edge(from_id, to_id, role, theorem_id=""):
    global eid, edges_added
    if from_id in existing_ids and to_id in existing_ids:
        graph['edges'].append({
            "id": f"e_{eid}",
            "from": from_id,
            "to": to_id,
            "role": role,
            "parameter_binding": {},
            "used_in_theorem": theorem_id
        })
        eid += 1
        edges_added += 1
    else:
        missing = []
        if from_id not in existing_ids:
            missing.append(f"from={from_id}")
        if to_id not in existing_ids:
            missing.append(f"to={to_id}")
        print(f"WARN edge skip: {', '.join(missing)}")

# ---- CHAPTER 2: Asymptotic Methods ----
# Laplace's Method
add_edge("s_poincare_asymptotic_expansion", "t_laplaces_method", "input")
add_edge("t_laplaces_method", "s_watsons_lemma", "output")

# Steepest Descents
add_edge("s_poincare_asymptotic_expansion", "t_method_of_steepest_descents", "input")
add_edge("t_method_of_steepest_descents", "s_stokes_phenomenon", "output")

# Bleistein -> Airy
add_edge("s_airy_function_ai", "t_bleisteins_method", "output")
add_edge("s_airy_function_bi", "t_bleisteins_method", "output")

# WKB -> Airy connection
add_edge("s_airy_function_ai", "t_liouville_green_wkb_approximation", "output")
add_edge("s_airy_function_bi", "t_liouville_green_wkb_approximation", "output")

# Mellin transform asymptotics
add_edge("s_mellin_transform", "t_mellin_transform_asymptotics", "input")

# Exponentially improved
add_edge("s_poincare_asymptotic_expansion", "t_exponentially_improved_asymptotics", "input")
add_edge("t_exponentially_improved_asymptotics", "s_stokes_phenomenon", "output")

# Hyperasymptotics
add_edge("s_stokes_phenomenon", "t_hyperasymptotics", "input")

# Stationary phase
add_edge("s_poincare_asymptotic_expansion", "t_stationary_phase_method", "input")
add_edge("t_stationary_phase_method", "s_fresnel_cosine_integral", "output")
add_edge("t_stationary_phase_method", "s_fresnel_sine_integral", "output")

# ---- CHAPTER 3: Numerical Methods ----
# Gauss quadratures from orthogonal polynomials
add_edge("s_legendre_polynomial", "t_gauss_legendre_quadrature", "input")
add_edge("s_laguerre_polynomial", "t_gauss_laguerre_quadrature", "input")
add_edge("s_hermite_polynomial", "t_gauss_hermite_quadrature", "input")

# Chebyshev expansion
add_edge("s_chebyshev_polynomial_first_kind", "t_chebyshev_expansion", "input")
add_edge("t_chebyshev_expansion", "t_clenshaw_curtis_quadrature", "input")

# Pade from series
add_edge("s_generalized_hypergeometric_pfq", "t_pade_approximation", "input")

# Wynn -> Pade connection
add_edge("t_wynn_epsilon_algorithm", "t_pade_approximation", "output")

# ---- CHAPTER 5: Gamma Function ----
# Gamma recurrence
add_edge("s_gamma_function", "t_fuchs_frobenius_theory", "input")

# Polygamma -> digamma
add_edge("s_polygamma_functions", "t_fuchs_frobenius_theory", "input")

# Stirling
add_edge("s_asymptotic_expansion_of_the_gamma_function", "t_laplaces_method", "output")

# ---- CHAPTER 6-7: Integrals ----
# Exponential integral relations
add_edge("s_upper_incomplete_gamma", "t_fuchs_frobenius_theory", "output")

# Error function -> incomplete gamma
add_edge("s_error_function", "t_fuchs_frobenius_theory", "output")

# ---- CHAPTER 9: Airy ----
# Airy equation -> Frobenius
add_edge("s_airy_differential_equation", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_airy_function_ai", "output")
add_edge("t_fuchs_frobenius_theory", "s_airy_function_bi", "output")

# ---- CHAPTER 10: Bessel ----
# Bessel equation -> Frobenius
add_edge("s_bessel_differential_equation", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_bessel_function_j_nu", "output")
add_edge("t_fuchs_frobenius_theory", "s_bessel_function_y_nu", "output")

# Hankel transform
add_edge("s_bessel_function_j_nu", "t_hankel_transform", "input")

# Spherical bessel -> regular bessel
add_edge("s_bessel_function_j_nu", "t_fuchs_frobenius_theory", "input")

# ---- CHAPTER 13: Confluent Hypergeometric ----
add_edge("s_kummer_confluent_equation", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_kummer_function_m", "output")
add_edge("t_fuchs_frobenius_theory", "s_tricomi_function_u", "output")

# Kummer -> special cases
add_edge("s_kummer_function_m", "t_fuchs_frobenius_theory", "output")

# ---- CHAPTER 14: Legendre ----
add_edge("s_associated_legendre_equation", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_ferrers_function_p", "output")
add_edge("t_fuchs_frobenius_theory", "s_legendre_function_second_kind", "output")

# Mehler-Fock
add_edge("s_conical_mehler_functions", "t_mehler_fock_transform", "input")

# ---- CHAPTER 15: Hypergeometric ----
add_edge("s_hypergeometric_differential_equation", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_gauss_hypergeometric_function", "output")

# ---- CHAPTER 16: Generalized Hypergeometric ----
# Meijer G-function -> Mellin-Barnes
add_edge("s_meijer_g_function", "t_mellin_transform_asymptotics", "input")

# ---- CHAPTER 17: q-Hypergeometric ----
add_edge("s_basic_hypergeometric_function", "t_bailey_pairs_chain", "input")
add_edge("t_bailey_pairs_chain", "s_ramanujan_1_psi_1", "output")
add_edge("t_bailey_pairs_chain", "s_rogers_ramanujan_identities", "output")

# Jacobi triple product -> theta functions
add_edge("s_jacobi_triple_product", "t_bailey_pairs_chain", "output")

# ---- CHAPTER 18: Orthogonal Polynomials ----
# Three-term recurrence
add_edge("s_three_term_recurrence", "t_fuchs_frobenius_theory", "input")

# Askey scheme connections
# Wilson -> Jacobi
add_edge("s_wilson_polynomial", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_jacobi_polynomial", "output")

# Jacobi special cases
add_edge("s_jacobi_polynomial", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_gegenbauer_polynomial", "output")
add_edge("t_fuchs_frobenius_theory", "s_chebyshev_polynomial_first_kind", "output")
add_edge("t_fuchs_frobenius_theory", "s_chebyshev_polynomial_second_kind", "output")

# ---- CHAPTER 19: Elliptic Integrals ----
add_edge("s_elliptic_integral", "t_arithmetic_geometric_mean", "input")
add_edge("t_arithmetic_geometric_mean", "s_complete_elliptic_integral_k", "output")

add_edge("s_elliptic_integral", "t_landen_transformation", "input")
add_edge("s_jacobian_sn", "t_landen_transformation", "input")

# ---- CHAPTER 20: Theta ----
# Theta -> Jacobi elliptic
add_edge("s_jacobi_theta_1", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_jacobian_sn", "output")

# ---- CHAPTER 22: Jacobian Elliptic ----
add_edge("s_jacobian_sn", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_jacobian_cn", "output")
add_edge("t_fuchs_frobenius_theory", "s_jacobian_dn", "output")

# ---- CHAPTER 23: Weierstrass ----
add_edge("s_weierstrass_ode", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_weierstrass_p_function", "output")

# Dedekind eta -> modular discriminant
add_edge("s_dedekind_eta_function", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_modular_discriminant_delta", "output")

# ---- CHAPTER 27: Number Theory ----
add_edge("s_mobius_function", "t_lambert_series", "input")
add_edge("t_lambert_series", "s_jordan_totient_function", "output")
add_edge("t_lambert_series", "s_ramanujan_tau_function", "output")

# Ramanujan tau -> modular discriminant
add_edge("s_ramanujan_tau_function", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_modular_discriminant_delta", "output")

# ---- CHAPTER 28: Mathieu ----
add_edge("s_mathieu_equation", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_mathieu_function_ce", "output")
add_edge("t_fuchs_frobenius_theory", "s_mathieu_function_se", "output")
add_edge("s_hill_equation", "t_fuchs_frobenius_theory", "input")

# ---- CHAPTER 29: Lame ----
add_edge("s_lame_equation", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_lame_polynomials", "output")

# ---- CHAPTER 30: Spheroidal ----
add_edge("s_spheroidal_equation", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_angular_spheroidal_wave_function", "output")

# ---- CHAPTER 31: Heun ----
add_edge("s_heun_equation", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_heun_function", "output")

# ---- CHAPTER 32: Painleve ----
add_edge("s_painleve_equation_p2", "t_backlund_transformations_painleve", "input")
add_edge("s_painleve_equation_p6", "t_backlund_transformations_painleve", "input")
add_edge("t_backlund_transformations_painleve", "s_painleve_equation_p1", "output")

# Painleve P_II -> Airy
add_edge("s_airy_function_ai", "t_backlund_transformations_painleve", "output")

# Painleve P_II -> Tracy-Widom
add_edge("s_painleve_equation_p2", "t_backlund_transformations_painleve", "input")
add_edge("t_backlund_transformations_painleve", "s_tracy_widom_distribution", "output")

# Coalescence cascade edges
add_edge("s_painleve_equation_p6", "t_backlund_transformations_painleve", "input")
add_edge("t_backlund_transformations_painleve", "s_painleve_equation_p5", "output")
add_edge("s_painleve_equation_p5", "t_backlund_transformations_painleve", "input")
add_edge("t_backlund_transformations_painleve", "s_painleve_equation_p4", "output")
add_edge("s_painleve_equation_p4", "t_backlund_transformations_painleve", "input")
add_edge("t_backlund_transformations_painleve", "s_painleve_equation_p3", "output")

# ---- CHAPTER 33: Coulomb ----
add_edge("s_coulomb_wave_equation", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_regular_coulomb_function", "output")
add_edge("t_fuchs_frobenius_theory", "s_irregular_coulomb_functions", "output")

# ---- CHAPTER 34: 3j/6j/9j ----
add_edge("s_wigner_3j_symbol", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_clebsch_gordan_coefficient", "output")
# 6j -> Racah polynomial
add_edge("s_6j_symbol", "t_fuchs_frobenius_theory", "input")
add_edge("t_fuchs_frobenius_theory", "s_racah_polynomial", "output")

# ---- CHAPTER 36: Catastrophe ----
add_edge("s_airy_function_ai", "t_stationary_phase_method", "output")
add_edge("t_stationary_phase_method", "s_pearcey_integral", "output")
add_edge("t_stationary_phase_method", "s_swallowtail_integral", "output")

# ---- Cross-chapter: Darboux method ----
add_edge("s_catalan_number", "t_darboux_method", "input")
add_edge("t_darboux_method", "s_poincare_asymptotic_expansion", "output")

# ---- Cross-chapter: Separation of variables ----
add_edge("s_bessel_differential_equation", "t_separation_of_variables", "output")
add_edge("s_mathieu_equation", "t_separation_of_variables", "output")
add_edge("s_spheroidal_equation", "t_separation_of_variables", "output")
add_edge("s_lame_equation", "t_separation_of_variables", "output")

# ---- Transforms connections ----
# Hilbert transform -> error function
add_edge("s_error_function", "t_hilbert_transform", "output")

# Abel transform -> Abel-Plana
add_edge("s_abel_plana_summation_formula", "t_abel_transform", "output")

# Hankel contour -> reciprocal gamma
add_edge("s_gamma_function", "t_hankel_contour_method", "input")
add_edge("t_hankel_contour_method", "s_hankel_contour_integral_reciprocal_gamma", "output")

# Watson transformation -> Bessel
add_edge("s_bessel_function_j_nu", "t_watson_transformation", "input")
add_edge("t_watson_transformation", "s_hankel_functions", "output")

# ---- Zeta / Number theory connections ----
add_edge("s_riemann_zeta_function", "t_mellin_transform_asymptotics", "input")
add_edge("t_mellin_transform_asymptotics", "s_hurwitz_zeta_function", "output")

add_edge("s_hurwitz_zeta_function", "t_mellin_transform_asymptotics", "input")
add_edge("t_mellin_transform_asymptotics", "s_lerch_transcendent", "output")
add_edge("t_mellin_transform_asymptotics", "s_polylogarithm", "output")

# Perron formula
add_edge("s_dirichlet_series", "t_mellin_transform_asymptotics", "input")

# Bernoulli -> Euler-Maclaurin
add_edge("s_bernoulli_number", "t_romberg_integration", "input")

print(f"Edges added: {edges_added}")

# ---------------------------------------------------------------------------
# 5. Validate
# ---------------------------------------------------------------------------
print("\nValidating...")
node_ids = {n['id'] for n in graph['nodes']}

# Check edge endpoints
edge_errors = 0
for e in graph['edges']:
    if e['from'] not in node_ids:
        edge_errors += 1
        print(f"  ERROR: edge {e['id']} from={e['from']} missing")
    if e['to'] not in node_ids:
        edge_errors += 1
        print(f"  ERROR: edge {e['id']} to={e['to']} missing")

# Check for duplicate node IDs
id_counts = Counter(n['id'] for n in graph['nodes'])
dupes = {k: v for k, v in id_counts.items() if v > 1}
if dupes:
    print(f"  DUPLICATE IDs found: {dupes}")
    seen = set()
    deduped = []
    for n in graph['nodes']:
        if n['id'] not in seen:
            seen.add(n['id'])
            deduped.append(n)
    graph['nodes'] = deduped
    print(f"  Removed {sum(v-1 for v in dupes.values())} duplicates")

# Check for duplicate edge IDs
eid_counts = Counter(e['id'] for e in graph['edges'])
edge_dupes = {k: v for k, v in eid_counts.items() if v > 1}
if edge_dupes:
    print(f"  DUPLICATE edge IDs: {edge_dupes}")

# Validate JSON serialization
try:
    json.dumps(graph)
    print("  JSON serialization: OK")
except Exception as ex:
    print(f"  JSON serialization FAILED: {ex}")

print(f"  Edge errors: {edge_errors}")

# ---------------------------------------------------------------------------
# 6. Update metadata and write
# ---------------------------------------------------------------------------
if 'metadata' not in graph:
    graph['metadata'] = {}
graph['metadata']['dlmf_integration'] = {
    "date": "2026-05-28",
    "source": "NIST DLMF (https://dlmf.nist.gov/), all 36 chapters",
    "new_node_count": added,
    "new_edge_count": edges_added,
    "skipped_existing": skipped,
    "edge_errors": edge_errors
}

with open('knowledge_graph.json', 'w') as f:
    json.dump(graph, f, indent=2, ensure_ascii=False)

print(f"\nFinal graph: {len(graph['nodes'])} nodes, {len(graph['edges'])} edges")
print("Written to knowledge_graph.json")
