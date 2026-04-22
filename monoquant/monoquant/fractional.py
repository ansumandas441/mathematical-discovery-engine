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

    Simplifications applied automatically:
      - FracLap(0, α) → 0
      - FracLap(u, 0) → u
      - FracLap(FracLap(u, α), β) → FracLap(u, α + β)  [composition]
      - FracLap(a*u + b*v, α) → a*FracLap(u, α) + b*FracLap(v, α)  [linearity
        over scalars; linearity over additions is handled by sympy's Add auto-
        distribution once we return a sum]

    Differentiation rule (via `_eval_derivative`):
      - ∂_x FracLap(u, α) = FracLap(∂_x u, α)  [FracLap commutes with ∂_x as
        Fourier multiplier]
    """

    nargs = 2

    @classmethod
    def eval(cls, arg, alpha):
        if arg == 0:
            return sp.Integer(0)
        if alpha == 0:
            return arg
        # Composition: FracLap(FracLap(u, α), β) = FracLap(u, α + β).
        if isinstance(arg, cls):
            inner, inner_alpha = arg.args
            return cls(inner, inner_alpha + alpha)
        # Linearity over addition: FracLap(a + b, α) = FracLap(a, α) + FracLap(b, α).
        if isinstance(arg, sp.Add):
            return sp.Add(*[cls(t, alpha) for t in arg.args])
        # Linearity over scalar * non-scalar: FracLap(c * f, α) = c * FracLap(f, α),
        # but only if c is truly scalar (no field content).
        if isinstance(arg, sp.Mul):
            scalar_part = sp.Integer(1)
            field_part = sp.Integer(1)
            for factor in arg.args:
                if factor.is_number or _is_pure_scalar(factor):
                    scalar_part *= factor
                else:
                    field_part *= factor
            if scalar_part != 1 and field_part != 1:
                return scalar_part * cls(field_part, alpha)
        return None  # keep unevaluated

    def _eval_derivative(self, s):
        """∂_s FracLap(u, α) = FracLap(∂_s u, α). Used by sympy's sp.diff."""
        inner, alpha = self.args
        # Differentiate inner; wrap result back in FracLap.
        d_inner = sp.diff(inner, s)
        if d_inner == 0:
            return sp.Integer(0)
        return FracLap(d_inner, alpha)

    def _sympystr(self, printer) -> str:
        return f"FracLap({printer.doprint(self.args[0])}, {printer.doprint(self.args[1])})"


def _is_pure_scalar(expr: sp.Expr) -> bool:
    """Return True if expr has no AppliedUndef or Derivative — it's a pure
    coefficient (numerical or symbolic constant)."""
    for sub in sp.preorder_traversal(expr):
        if isinstance(sub, (AppliedUndef, sp.Derivative, FracLap)):
            return False
    return True


def apply_fractional_ibp(expr: sp.Expr) -> sp.Expr:
    """Rewrite integrand factors using the self-adjoint fractional IBP identity:

        ∫ FracLap(f, α) · FracLap(g, β) dx = ∫ FracLap(f, (α+β)/2) · FracLap(g, (α+β)/2) dx
                                           (= ∫|FracLap(u, (α+β)/2)|² dx if f = g = u)

    Covered cases:
      (i) u_k · FracLap(u_k, α) → FracLap(u_k, α/2) ** 2
      (ii) FracLap(u_k, α) · FracLap(u_k, β) → FracLap(u_k, (α+β)/2) ** 2
      (iii) u_k · FracLap(f, α) where f = ∂^γ u_k: → FracLap(u_k, α/2) · FracLap(∂^γ u_k, α/2)

    These are global (under integral) identities. The pointwise rewrite is valid
    mod total divergence.
    """
    expr = sp.expand(expr)
    if isinstance(expr, sp.Add):
        return sp.Add(*[apply_fractional_ibp(t) for t in expr.args])
    if isinstance(expr, sp.Mul):
        args = list(expr.args)
        # Case (ii): two FracLap factors with the same underlying field.
        for i in range(len(args)):
            fi = args[i]
            if not isinstance(fi, FracLap):
                continue
            for j in range(i + 1, len(args)):
                fj = args[j]
                if not isinstance(fj, FracLap):
                    continue
                inner_i, alpha_i = fi.args
                inner_j, alpha_j = fj.args
                # Check same underlying AppliedUndef (ignore derivative orders
                # for now; only exact-match case).
                if _same_field_atom(inner_i, inner_j):
                    new_alpha = (alpha_i + alpha_j) / 2
                    if inner_i == inner_j:
                        new_factor = FracLap(inner_i, new_alpha) ** 2
                    else:
                        new_factor = FracLap(inner_i, new_alpha) * FracLap(inner_j, new_alpha)
                    remainder = sp.Mul(
                        *(args[:i] + args[i+1:j] + args[j+1:])
                    )
                    return sp.expand(remainder * new_factor)
        # Case (i): bare u_k * FracLap(u_k, α).
        for i, fi in enumerate(args):
            for j, fj in enumerate(args):
                if i == j:
                    continue
                if isinstance(fi, AppliedUndef) and isinstance(fj, FracLap):
                    inner = fj.args[0]
                    alpha = fj.args[1]
                    if isinstance(inner, AppliedUndef) and inner.func == fi.func:
                        new_factor = FracLap(fi, alpha / 2) ** 2
                        remainder = sp.Mul(
                            *(args[:min(i, j)] + args[min(i, j)+1:max(i, j)] + args[max(i, j)+1:])
                        )
                        return sp.expand(remainder * new_factor)
        return expr
    return expr


def _same_field_atom(a: sp.Expr, b: sp.Expr) -> bool:
    """True if a and b are either the same AppliedUndef or derivatives of the
    same field function."""
    if a == b:
        return True
    def _base_func(expr):
        if isinstance(expr, AppliedUndef):
            return expr.func
        if isinstance(expr, sp.Derivative):
            inner = expr.expr
            if isinstance(inner, AppliedUndef):
                return inner.func
        return None
    fa = _base_func(a)
    fb = _base_func(b)
    return fa is not None and fa == fb


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
