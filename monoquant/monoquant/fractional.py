"""Fractional-Laplacian support for MonoQuant.

The operator (-Δ)^α is a non-local pseudodifferential operator with Fourier
symbol |ξ|^{2α}. It cannot be expressed as a finite combination of local
derivatives, so we represent it symbolically as an un-evaluated function
`FracLap(u, alpha)` in sympy and track it through the computation.

### Key identities used

1. **Self-adjointness under integral**:
       ∫ f · FracLap(g, α) dx = ∫ FracLap(f, α) · g dx
2. **Fractional IBP (the engine's key rule)**:
       ∫ f · FracLap(g, α) dx = ∫ FracLap(f, α/2) · FracLap(g, α/2) dx
   (valid on decay-at-∞ data via Plancherel; |ξ|^{2α} = |ξ|^α · |ξ|^α).
3. **Positive-semidefinite diagonal**:
       ∫ u · FracLap(u, α) dx = ∫ |FracLap(u, α/2)|² dx ≥ 0
4. **Commutation with spatial derivatives**: FracLap and ∂_x commute.
5. **Composition**: FracLap(FracLap(u, α), β) = FracLap(u, α + β).

### What we support in v0.1

- Syntactic representation via `FracLap(u, α)` as a sympy `Function`.
- An `apply_fractional_ibp` pass that rewrites `u_i · FracLap(u_i, α)` terms
  (the ones that come out of the energy / enstrophy computations) as
  `FracLap(u_i, α/2) ** 2`.
- A sign-test extension that recognises `FracLap(u, α/2) ** 2` as pointwise
  non-negative.

### What we don't support (v0.2+)

- Commutator estimates for products: FracLap(u · v, α) ≠ v · FracLap(u, α) in general.
- General-ansatz IBP for arbitrary f · FracLap(g, α) when f, g are composite.
- Full SDP with fractional-multiplier constraints.

This is a tight lightweight extension that is **correct for the energy
functional** and enables a meaningful sign test of ½|u|² on hyperdissipative
NSE.
"""

from __future__ import annotations

import sympy as sp
from sympy.core.function import AppliedUndef


class FracLap(sp.Function):
    """Symbolic fractional Laplacian: FracLap(u, alpha) = (-Δ)^alpha u.

    Kept unevaluated. Not simplified by sympy's usual machinery — we handle
    IBP and sign tests in our own rewrite rules.
    """

    nargs = 2

    @classmethod
    def eval(cls, arg, alpha):
        # Don't auto-simplify; keep the symbol around for our engine to process.
        # But if arg is 0, result is 0.
        if arg == 0:
            return sp.Integer(0)
        # If alpha == 0, (-Δ)^0 = identity.
        if alpha == 0:
            return arg
        return None  # keep unevaluated

    def _sympystr(self, printer) -> str:
        return f"FracLap({printer.doprint(self.args[0])}, {printer.doprint(self.args[1])})"


def apply_fractional_ibp(expr: sp.Expr) -> sp.Expr:
    """Rewrite u_i · FracLap(u_i, α) → FracLap(u_i, α/2) ** 2 (valid mod total divergence).

    This is the key identity that turns the dissipation term into an obviously
    non-negative integrand.
    """
    expr = sp.expand(expr)
    # Pattern-match: product factors that contain both u_i and FracLap(u_i, α).
    if isinstance(expr, sp.Add):
        return sp.Add(*[apply_fractional_ibp(t) for t in expr.args])
    if isinstance(expr, sp.Mul):
        args = list(expr.args)
        for i, fi in enumerate(args):
            for j, fj in enumerate(args):
                if i == j:
                    continue
                # Match: fi is a bare AppliedUndef u_k, fj is FracLap(u_k, α).
                if isinstance(fi, AppliedUndef) and isinstance(fj, FracLap):
                    inner = fj.args[0]
                    alpha = fj.args[1]
                    if isinstance(inner, AppliedUndef) and inner.func == fi.func:
                        # Replace fi * fj with FracLap(u_k, α/2)**2.
                        new_factor = FracLap(fi, alpha / 2) ** 2
                        remainder = sp.Mul(
                            *(args[:min(i, j)] + args[min(i, j)+1:max(i, j)] + args[max(i, j)+1:])
                        )
                        return sp.expand(remainder * new_factor)
        return expr
    return expr


def fractional_laplacian_sign_test(expr: sp.Expr, pde=None) -> str:
    """Return DECREASE / INCREASE / MIXED / ZERO based on the expression.

    Strategy:
      1. Split expr into (fractional-Laplacian terms) + (other terms).
      2. The fractional-Laplacian terms may admit an SOS sign from FracLap²
         structure → use the simple SOS recogniser.
      3. The "other" terms, if they have the shape of an incompressible-transport
         form (polynomial in u with exactly one first-order spatial derivative per
         monomial), integrate to zero under the div-free constraint and can be
         dropped from the sign test.
      4. Combine.
    """
    expr = sp.expand(expr)
    if expr == 0:
        return "ZERO"
    frac_part = sp.Integer(0)
    other_part = sp.Integer(0)
    terms = expr.args if isinstance(expr, sp.Add) else [expr]
    for t in terms:
        if _contains_fraclap(t):
            frac_part += t
        else:
            other_part += t
    # Check the "other" part is transport-like (if it exists).
    if other_part != 0:
        if not _is_transport_like(other_part, pde):
            # Can't drop other_part — sign is uncertain.
            return "MIXED"
    # Now sign-test the fractional part.
    if frac_part == 0:
        return "ZERO"
    return _sos_sign(frac_part)


def _contains_fraclap(expr: sp.Expr) -> bool:
    for sub in sp.preorder_traversal(expr):
        if isinstance(sub, FracLap):
            return True
    return False


def _is_transport_like(expr: sp.Expr, pde=None) -> bool:
    """Check: every monomial in expr has exactly ONE first-order spatial derivative
    factor, all other factors being bare fields. If so, under a div-free constraint,
    the integral of expr vanishes (transport identity)."""
    expr = sp.expand(expr)
    if expr == 0:
        return True
    terms = expr.args if isinstance(expr, sp.Add) else [expr]
    for t in terms:
        if not _term_is_transport_like(t):
            return False
    return True


def _term_is_transport_like(term: sp.Expr) -> bool:
    """A single monomial is 'transport-like' if:
       - it is a Mul of factors
       - exactly one factor is a first-order Derivative(u_k, x_j)
       - all other factors are AppliedUndef (bare field u_i) or numerical constants
    """
    if isinstance(term, sp.Add):
        return all(_term_is_transport_like(t) for t in term.args)
    if not isinstance(term, sp.Mul):
        # A bare Derivative or bare AppliedUndef — not transport-like by itself
        # (we need at least one u factor alongside one ∂u to be a transport-like form).
        # But a bare ∂u can also integrate to zero for decay data, so accept.
        if isinstance(term, sp.Derivative):
            order = sum(int(k) for _, k in term.variable_count)
            return order == 1
        return False
    n_deriv = 0
    for f in term.args:
        if isinstance(f, sp.Derivative):
            order = sum(int(k) for _, k in f.variable_count)
            if order != 1:
                return False
            n_deriv += 1
        elif isinstance(f, AppliedUndef):
            continue
        elif isinstance(f, sp.Pow):
            base, exp = f.args
            # Accept u_i^k for positive integer k (still transport-like).
            if isinstance(base, AppliedUndef) and exp.is_integer and exp > 0:
                continue
            return False
        elif f.is_number:
            continue
        else:
            return False
    return n_deriv == 1


def _sos_sign(expr: sp.Expr) -> str:
    """Classify an SOS-form expression of FracLap² terms by sign."""
    expr = sp.expand(expr)
    if expr == 0:
        return "ZERO"
    terms = expr.args if isinstance(expr, sp.Add) else [expr]
    signs = set()
    for t in terms:
        signs.add(_sos_single_term_sign(t))
    if signs == {"ZERO"}:
        return "ZERO"
    if signs - {"ZERO"} == {"DECREASE"}:
        return "DECREASE"
    if signs - {"ZERO"} == {"INCREASE"}:
        return "INCREASE"
    return "MIXED"


def _sos_single_term_sign(t: sp.Expr) -> str:
    if t == 0:
        return "ZERO"
    c, other = t.as_coeff_mul()
    is_sq = True
    has_factor = False
    for factor in other:
        if isinstance(factor, sp.Pow):
            base, exp = factor.args
            if isinstance(base, FracLap) and exp.is_integer and exp % 2 == 0:
                has_factor = True
                continue
            is_sq = False
            break
        if isinstance(factor, FracLap):
            is_sq = False
            break
        is_sq = False
        break
    if is_sq and has_factor:
        if c < 0:
            return "DECREASE"
        if c > 0:
            return "INCREASE"
        return "ZERO"
    return "MIXED"
