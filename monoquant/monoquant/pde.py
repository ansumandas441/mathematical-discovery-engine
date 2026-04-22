"""PDE base class and field types."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Sequence, Tuple

import sympy as sp


@dataclass
class ScalarField:
    """A scalar field u(t, x1, ..., xd) with coordinates and a symbol."""

    name: str
    spatial_dim: int
    coords: Tuple[sp.Symbol, ...] = field(init=False)
    t: sp.Symbol = field(init=False)
    symbol: sp.Function = field(init=False)

    def __post_init__(self) -> None:
        self.t = sp.Symbol("t", real=True)
        self.coords = tuple(sp.Symbol(f"x{i+1}", real=True) for i in range(self.spatial_dim))
        self.symbol = sp.Function(self.name)(self.t, *self.coords)

    def partial(self, *orders: int) -> sp.Expr:
        """Return ∂^α u where orders is a multi-index over spatial coords."""
        expr = self.symbol
        for coord, order in zip(self.coords, orders):
            if order:
                expr = sp.diff(expr, coord, order)
        return expr

    def time_derivative(self) -> sp.Expr:
        return sp.diff(self.symbol, self.t)


@dataclass
class VectorField:
    """A vector field u=(u1,...,ud)(t,x1,...,xd)."""

    name: str
    spatial_dim: int
    components: Tuple[ScalarField, ...] = field(init=False)

    def __post_init__(self) -> None:
        self.components = tuple(
            ScalarField(name=f"{self.name}{i+1}", spatial_dim=self.spatial_dim)
            for i in range(self.spatial_dim)
        )
        # Share the time/coord symbols across components.
        t = self.components[0].t
        coords = self.components[0].coords
        for c in self.components[1:]:
            c.t = t
            c.coords = coords
            c.symbol = sp.Function(c.name)(t, *coords)

    @property
    def t(self) -> sp.Symbol:
        return self.components[0].t

    @property
    def coords(self) -> Tuple[sp.Symbol, ...]:
        return self.components[0].coords

    def __getitem__(self, i: int) -> ScalarField:
        return self.components[i]

    def divergence(self) -> sp.Expr:
        return sum(sp.diff(c.symbol, x) for c, x in zip(self.components, self.coords))


@dataclass
class PDE:
    """Base PDE.

    Subclass and override `rhs_substitutions` with the PDE's ∂_t u = F(u) map —
    a dict from ∂_t u (for each component / scalar) to its spatial expression.
    Also set `constraints` (list of identities like div u = 0) and `symmetries`.
    """

    name: str
    fields: Sequence[object]
    rhs_substitutions: Dict[sp.Expr, sp.Expr] = field(default_factory=dict)
    constraints: List[sp.Expr] = field(default_factory=list)
    # Parameter: dimension-of-scaling exponent per component. Used by invariants.py.
    scaling: Dict[str, float] = field(default_factory=dict)
    notes: str = ""

    @property
    def spatial_dim(self) -> int:
        f = self.fields[0]
        if isinstance(f, VectorField):
            return f.spatial_dim
        return f.spatial_dim  # ScalarField

    @property
    def coords(self) -> Tuple[sp.Symbol, ...]:
        f = self.fields[0]
        if isinstance(f, VectorField):
            return f.coords
        return f.coords

    @property
    def t(self) -> sp.Symbol:
        f = self.fields[0]
        if isinstance(f, VectorField):
            return f.t
        return f.t

    def apply_rhs(self, expr: sp.Expr) -> sp.Expr:
        """Substitute every ∂_t u in expr with its spatial RHS."""
        out = expr
        for lhs, rhs in self.rhs_substitutions.items():
            out = out.xreplace({lhs: rhs})
        return sp.expand(out)

    def impose_constraints(self, expr: sp.Expr) -> sp.Expr:
        """Eliminate one atom per constraint via algebraic rearrangement.

        For each constraint C = 0 that is LINEAR in its atoms with unit
        coefficients (e.g. ∂₁u₁ + ∂₂u₂ + ∂₃u₃ = 0), we pick the
        lexicographically-largest atom `a` appearing in C, and substitute
        `a → -(C - a)` throughout `expr`. We do NOT use sp.solve because
        sympy's solve does not handle Derivative-typed unknowns cleanly.
        """
        if not self.constraints:
            return sp.expand(expr)
        from sympy.core.function import AppliedUndef

        def _collect_derivs(e):
            """Collect top-level field-derivative atoms. When we see a
            Derivative(u_i, ...), we collect IT and do NOT descend into its
            `.expr` (which would return the bare u_i). This gives the set of
            'leaf' atoms appropriate for constraint elimination."""
            atoms = set()
            def _walk(node):
                if isinstance(node, sp.Derivative):
                    atoms.add(node)
                    return  # don't descend — the inner AppliedUndef is NOT a separate atom for constraint purposes
                if isinstance(node, AppliedUndef):
                    atoms.add(node)
                    return
                if hasattr(node, "args"):
                    for arg in node.args:
                        _walk(arg)
            _walk(e)
            return atoms

        out = sp.expand(expr)
        for c in self.constraints:
            c_expanded = sp.expand(c)
            atoms = _collect_derivs(c_expanded)
            if not atoms:
                continue
            # Dummy-swap: replace each atom by a unique Symbol, then the
            # substitution becomes a simple polynomial-variable rewrite.
            all_atoms_in_expr = _collect_derivs(out)
            all_atoms = sorted(atoms | all_atoms_in_expr, key=lambda e: str(e))
            dummy_of = {a: sp.Symbol(f"_A{i}") for i, a in enumerate(all_atoms)}
            back_of = {d: a for a, d in dummy_of.items()}
            c_dummy = c_expanded.xreplace(dummy_of)
            out_dummy = out.xreplace(dummy_of)
            # Choose the dummy corresponding to the chosen atom.
            chosen = sorted(atoms, key=lambda e: str(e))[-1]
            chosen_dummy = dummy_of[chosen]
            try:
                coeff = sp.Poly(c_dummy, chosen_dummy).nth(1)
            except (sp.polys.polyerrors.GeneratorsError, Exception):
                continue
            if coeff == 0:
                continue
            rest = sp.expand(c_dummy - coeff * chosen_dummy)
            replacement_dummy = sp.simplify(-rest / coeff)
            out_dummy_new = sp.expand(out_dummy.subs(chosen_dummy, replacement_dummy))
            # Substitute dummies back.
            out = sp.expand(out_dummy_new.xreplace(back_of))
        return out
