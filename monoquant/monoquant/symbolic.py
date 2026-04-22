"""Symbolic d/dt engine, IBP reduction, and Euler–Lagrange operator.

Approach (v0.1.2): split the pipeline into two distinct checks.

  - **Conservation check**: apply the Euler–Lagrange operator E_u to the
    pointwise ∂_t φ. E_u(L) ≡ 0 (identically in the jet variables) iff L is a
    total spatial divergence, i.e. ∫L dx is a conserved quantity for
    decaying-at-infinity data.

  - **Monotonicity check**: apply one pass of IBP (pushing every spatial
    derivative off the "highest-order" factor onto the rest) to produce a
    candidate pointwise sign-testable integrand, then hand to SDP SOS.

This split avoids the ping-pong that a naive "iterated IBP" encounters and
relies on the classical fact that E_u is the *unique* (up to scale) linear
operator whose kernel is exactly the spatial divergences.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Set, Tuple

import sympy as sp
from sympy.core.function import AppliedUndef

from monoquant.pde import PDE, ScalarField, VectorField


@dataclass
class TimeDerivativeEngine:
    pde: PDE

    # ---------- pointwise time derivative ----------

    def dphi_dt_pointwise(self, phi: sp.Expr) -> sp.Expr:
        atoms = self._collect_atoms(phi)
        if not atoms:
            return sp.Integer(0)
        dummy_of = {a: sp.Symbol(f"_D_{i}") for i, a in enumerate(atoms)}
        back_of = {d: a for a, d in dummy_of.items()}
        phi_dummy = phi.xreplace(dummy_of)
        total = sp.Integer(0)
        for atom in atoms:
            d_sym = dummy_of[atom]
            partial = sp.diff(phi_dummy, d_sym)
            rhs_version = self._time_derivative_of_atom(atom)
            total += partial.xreplace(back_of) * rhs_version
        return sp.expand(total)

    def _time_derivative_of_atom(self, atom: sp.Expr) -> sp.Expr:
        fields = _flat_fields(self.pde)
        coords = self.pde.coords
        t = self.pde.t
        # Case 1: atom = FracLap(u_i, β). FracLap commutes with ∂_t, so
        #   ∂_t FracLap(u_i, β) = FracLap(∂_t u_i, β) = FracLap(F_i, β).
        from monoquant.fractional import FracLap
        if isinstance(atom, FracLap):
            inner, beta = atom.args
            # inner should be an AppliedUndef u_i(t, x, ...).
            for f in fields:
                if _is_derivative_of_function(inner, f.symbol):
                    alpha = _extract_spatial_multi_index(inner, coords)
                    rhs = self.pde.rhs_substitutions.get(sp.diff(f.symbol, t))
                    if rhs is None:
                        raise ValueError(
                            f"No RHS for ∂_t {f.symbol}; check pde.rhs_substitutions."
                        )
                    # Apply α-many spatial derivatives to rhs, then wrap in FracLap.
                    inner_t = rhs
                    for x, order in zip(coords, alpha):
                        if order:
                            inner_t = sp.diff(inner_t, x, order)
                    inner_t = sp.expand(inner_t)
                    # FracLap distributes over sums (linear).
                    return _distribute_fraclap(inner_t, beta)
            # Fall through if FracLap's inner isn't a field.
        # Case 2: atom = Derivative(u_i, α). Standard route.
        for f in fields:
            base = f.symbol
            if _is_derivative_of_function(atom, base):
                alpha = _extract_spatial_multi_index(atom, coords)
                rhs = self.pde.rhs_substitutions.get(sp.diff(base, t))
                if rhs is None:
                    raise ValueError(
                        f"No RHS for ∂_t {base}; add it to pde.rhs_substitutions."
                    )
                out = rhs
                for x, order in zip(coords, alpha):
                    if order:
                        out = sp.diff(out, x, order)
                return sp.expand(out)
        return sp.diff(atom, t)

    # ---------- Euler–Lagrange operator: conservation test ----------

    def euler_lagrange(self, integrand: sp.Expr, field) -> sp.Expr:
        """Compute E_u(L) = Σ_α (−∂)^α [ ∂L / ∂(∂^α u) ].

        `field` is a ScalarField. Sum over all multi-indices α of spatial
        derivatives with |α| ≤ max order appearing in `integrand`.
        """
        coords = self.pde.coords
        base = field.symbol
        # Identify max derivative order of `field` in integrand.
        max_order = _max_derivative_order_of_field(integrand, base, coords)
        if max_order < 0:
            return sp.Integer(0)
        from itertools import product as iproduct
        result = sp.Integer(0)
        for total in range(max_order + 1):
            for alpha in _multi_indices(len(coords), total):
                # Build ∂^α u target expression.
                target = base
                for x, k in zip(coords, alpha):
                    if k:
                        target = sp.diff(target, x, k)
                # Use dummy substitution to differentiate w.r.t. ∂^α u.
                dummy = sp.Symbol("__dL")
                # Replace target by dummy everywhere it appears, then diff.
                L_dummy = integrand.xreplace({target: dummy})
                partial = sp.diff(L_dummy, dummy)
                partial = partial.xreplace({dummy: target})
                # Apply (−∂)^α.
                sign = (-1) ** total
                term = partial
                for x, k in zip(coords, alpha):
                    for _ in range(k):
                        term = sp.diff(term, x)
                result += sign * term
        return sp.expand(result)

    # ---------- one-pass IBP (for sign-test canonical form) ----------

    def integrate_by_parts(self, integrand: sp.Expr, passes: int = 1) -> sp.Expr:
        """Apply a bounded number of IBP passes.

        Each pass: for every term in the Add, if the term is a Mul containing a
        factor D^α u_i with |α| maximal among that term's factors, peel off ONE
        derivative (in the first direction with positive order) onto the rest of
        the term with a sign flip.

        Boundary terms dropped (decaying-at-infinity).
        """
        current = sp.expand(integrand)
        for _ in range(passes):
            new = sp.Add(
                *[_ibp_one_term(t, self.pde.coords) for t in _as_addends(current)]
            )
            new = sp.expand(new)
            if new == current:
                break
            current = new
        return current

    # ---------- introspection ----------

    def _collect_atoms(self, expr: sp.Expr) -> List[sp.Expr]:
        return _collect_field_derivatives(expr, self.pde)


# ======================== helpers ========================

def _flat_fields(pde: PDE) -> List[ScalarField]:
    flat: List[ScalarField] = []
    for f in pde.fields:
        if isinstance(f, VectorField):
            flat.extend(f.components)
        else:
            flat.append(f)
    return flat


def _collect_field_derivatives(expr: sp.Expr, pde: PDE) -> List[sp.Expr]:
    from monoquant.fractional import FracLap
    fields = _flat_fields(pde)
    names = {f.symbol.func.__name__ for f in fields}
    t_sym = pde.t
    atoms: Set[sp.Expr] = set()
    # Custom walk: don't descend into FracLap — treat it as an atomic marker.
    def _walk(node):
        if isinstance(node, FracLap):
            atoms.add(node)
            return
        if isinstance(node, AppliedUndef) and node.func.__name__ in names:
            atoms.add(node)
            return
        if isinstance(node, sp.Derivative):
            inner = node.expr
            if isinstance(inner, AppliedUndef) and inner.func.__name__ in names:
                t_order = 0
                for var, k in node.variable_count:
                    if var == t_sym:
                        t_order = int(k)
                if t_order == 0:
                    atoms.add(node)
                    return
        if hasattr(node, "args"):
            for arg in node.args:
                _walk(arg)
    _walk(expr)
    return sorted(atoms, key=lambda e: str(e))


def _is_derivative_of_function(atom: sp.Expr, base) -> bool:
    if isinstance(atom, AppliedUndef):
        return atom.func == base.func
    if isinstance(atom, sp.Derivative):
        inner = atom.expr
        return isinstance(inner, AppliedUndef) and inner.func == base.func
    return False


def _extract_spatial_multi_index(atom: sp.Expr, coords) -> Tuple[int, ...]:
    alpha = [0] * len(coords)
    if isinstance(atom, sp.Derivative):
        for var, k in atom.variable_count:
            if var in coords:
                alpha[coords.index(var)] = int(k)
    return tuple(alpha)


def _max_derivative_order_of_field(expr: sp.Expr, base, coords) -> int:
    max_order = -1
    for sub in sp.preorder_traversal(expr):
        if isinstance(sub, AppliedUndef) and sub.func == base.func:
            max_order = max(max_order, 0)
        elif isinstance(sub, sp.Derivative):
            inner = sub.expr
            if isinstance(inner, AppliedUndef) and inner.func == base.func:
                t_order = 0
                spatial_order = 0
                for var, k in sub.variable_count:
                    if var in coords:
                        spatial_order += int(k)
                    else:
                        t_order = int(k)
                if t_order == 0:
                    max_order = max(max_order, spatial_order)
    return max_order


def _multi_indices(d: int, order: int) -> List[Tuple[int, ...]]:
    if d == 1:
        return [(order,)]
    out: List[Tuple[int, ...]] = []
    for first in range(order + 1):
        for rest in _multi_indices(d - 1, order - first):
            out.append((first,) + rest)
    return out


def _as_addends(expr: sp.Expr) -> List[sp.Expr]:
    if isinstance(expr, sp.Add):
        return list(expr.args)
    return [expr]


def _distribute_fraclap(expr: sp.Expr, beta) -> sp.Expr:
    """Apply FracLap(·, β) to each additive term of `expr`.

    FracLap is linear: FracLap(a + b, β) = FracLap(a, β) + FracLap(b, β).
    FracLap also commutes with spatial derivatives: FracLap(∂_x u, β) =
    ∂_x FracLap(u, β). We use this to push FracLap inward, producing a
    clean sum of `FracLap(<elementary atom>, β)` terms.
    """
    from monoquant.fractional import FracLap
    expr = sp.expand(expr)
    if isinstance(expr, sp.Add):
        return sp.Add(*[_distribute_fraclap(t, beta) for t in expr.args])
    # Single term. Pull out numeric coefficient.
    c, rest = expr.as_coeff_mul()
    # If rest is empty, FracLap of constant = 0 (for β > 0).
    if not rest:
        if beta == 0:
            return sp.Integer(int(c)) if c == int(c) else expr
        return sp.Integer(0)
    # For a product of atoms, FracLap(Π a_i, β) is NOT generally Π FracLap(a_i, β)
    # — it's a nonlocal operator. We keep FracLap wrapping the whole product.
    return c * FracLap(sp.Mul(*rest), beta)


def _ibp_one_term(term: sp.Expr, coords) -> sp.Expr:
    """Peel one derivative off the highest-order derivative factor in `term`,
    ONLY when doing so strictly lowers the max-derivative-order statistic.

    This rules out oscillation on terms where the max-derivative-order is
    already 1 (e.g. transport terms like u_i u_j ∂_j u_k in NSE): those are
    handled by constraint substitution, not IBP.
    """
    if isinstance(term, sp.Add):
        return sp.Add(*[_ibp_one_term(t, coords) for t in term.args])
    if not isinstance(term, sp.Mul):
        return term
    args = list(term.args)
    best_i, best_order = -1, -1
    for i, f in enumerate(args):
        if isinstance(f, sp.Derivative):
            order = sum(int(k) for v, k in f.variable_count if v in coords)
            if order > best_order:
                best_order = order
                best_i = i
    if best_i == -1 or best_order <= 1:
        return term  # don't IBP if nothing to do or if max-order is already 1
    f = args[best_i]
    # Pick the direction with positive order (preferring lower-index coord).
    chosen_coord = None
    for var, k in f.variable_count:
        if var in coords and int(k) >= 1:
            chosen_coord = var
            break
    if chosen_coord is None:
        return term
    new_order = {v: int(k) for v, k in f.variable_count}
    new_order[chosen_coord] -= 1
    if new_order[chosen_coord] == 0:
        del new_order[chosen_coord]
    if not new_order:
        reduced = f.expr
    else:
        reduced = sp.Derivative(f.expr, *[(v, n) for v, n in new_order.items()]).doit()
    remainder = sp.Mul(*(args[:best_i] + args[best_i + 1:]))
    return -sp.diff(remainder, chosen_coord) * reduced
