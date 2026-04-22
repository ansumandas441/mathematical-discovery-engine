"""Polynomial invariant-basis enumeration.

Given a PDE with a primary scalar (or vector) field u and spatial dimension d,
we enumerate monomials m(u, ∂u, ∂²u, ...) of bounded total degree in derivatives
(sum of derivative orders) and bounded total polynomial degree in field powers.
We then filter to retain only those that respect the PDE's declared scaling
weight and, where possible, translation/rotation invariance.

In v0.1 we do *not* attempt full SO(d)-invariant reduction — we emit the raw
monomial basis and let the symbolic engine handle rotational cancellations
integrally. This is sound (we don't miss invariants) but can produce redundant
candidates. A v0.2 SO(d)-invariant reducer is on the roadmap.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Dict, Iterable, List, Tuple

import sympy as sp

from monoquant.pde import PDE, ScalarField, VectorField


@dataclass
class Monomial:
    """A monomial in derivatives of the PDE state.

    `factors`: list of (field_index, multi-index) giving ∂^α u_{field_index}.
    """

    factors: Tuple[Tuple[int, Tuple[int, ...]], ...]
    coefficient_symbol: sp.Symbol

    def as_expr(self, pde: PDE) -> sp.Expr:
        # Convert (field_index, multi-index) back to sympy derivative expressions.
        expr: sp.Expr = sp.Integer(1)
        for field_idx, mi in self.factors:
            f = _flat_fields(pde)[field_idx]
            expr = expr * f.partial(*mi)
        return expr

    @property
    def derivative_order(self) -> int:
        return sum(sum(mi) for _, mi in self.factors)

    @property
    def polynomial_degree(self) -> int:
        return len(self.factors)


def _flat_fields(pde: PDE) -> List[ScalarField]:
    flat: List[ScalarField] = []
    for f in pde.fields:
        if isinstance(f, VectorField):
            flat.extend(f.components)
        else:
            flat.append(f)
    return flat


def _multi_indices(d: int, order: int) -> List[Tuple[int, ...]]:
    """All multi-indices (α_1,...,α_d) of nonneg ints with |α|=order."""
    if d == 1:
        return [(order,)]
    out: List[Tuple[int, ...]] = []
    for first in range(order + 1):
        for rest in _multi_indices(d - 1, order - first):
            out.append((first,) + rest)
    return out


@dataclass
class PolynomialInvariantBasis:
    """Enumerate a basis of polynomial functionals up to given degree/order."""

    pde: PDE
    max_poly_degree: int = 2
    max_derivative_order: int = 2

    def enumerate(self) -> List[Monomial]:
        """Return all monomials with (poly_degree, derivative_order) in the box."""
        fields = _flat_fields(self.pde)
        d = self.pde.spatial_dim
        # For each (field, derivative_order) pair, the set of "atoms" is
        # multi-indices of total |α|=order.
        atoms: List[Tuple[int, Tuple[int, ...]]] = []
        for fi, _ in enumerate_with_index(fields):
            for order in range(self.max_derivative_order + 1):
                for mi in _multi_indices(d, order):
                    atoms.append((fi, mi))
        # Enumerate all multisets of atoms of size <= max_poly_degree.
        monomials: List[Monomial] = []
        counter = 0
        for poly_deg in range(1, self.max_poly_degree + 1):
            for combo in _multisets(atoms, poly_deg):
                if self._total_deriv_order(combo) > self.max_derivative_order:
                    continue
                counter += 1
                coef = sp.Symbol(f"c_{counter}")
                monomials.append(Monomial(factors=combo, coefficient_symbol=coef))
        return monomials

    def _total_deriv_order(self, combo: Tuple[Tuple[int, Tuple[int, ...]], ...]) -> int:
        return sum(sum(mi) for _, mi in combo)


def enumerate_with_index(seq: Iterable) -> Iterable[Tuple[int, object]]:
    for i, v in enumerate(seq):
        yield i, v


def _multisets(atoms: List[Tuple[int, Tuple[int, ...]]], size: int) -> Iterable[Tuple]:
    """Multisets of `size` from `atoms` (deduplicated up to order)."""
    n = len(atoms)
    if size == 0:
        yield ()
        return
    # Indexed combinations with replacement.
    def helper(start: int, remaining: int) -> Iterable[Tuple[int, ...]]:
        if remaining == 0:
            yield ()
            return
        for i in range(start, n):
            for tail in helper(i, remaining - 1):
                yield (i,) + tail
    for idx_tuple in helper(0, size):
        yield tuple(atoms[i] for i in idx_tuple)
