"""1D viscous Burgers ∂_t u = ν u_xx − u u_x."""

from __future__ import annotations

import sympy as sp

from monoquant.pde import PDE, ScalarField


def burgers_equation(nu: float = 1.0, inviscid: bool = False) -> PDE:
    u = ScalarField("u", spatial_dim=1)
    x = u.coords[0]
    if inviscid:
        rhs = -u.symbol * sp.diff(u.symbol, x)
        name = "burgers_inviscid_1d"
    else:
        rhs = sp.Rational(str(nu)) * sp.diff(u.symbol, x, 2) - u.symbol * sp.diff(u.symbol, x)
        name = f"burgers_viscous_1d_nu{nu}"
    rhs_substitutions = {sp.diff(u.symbol, u.t): rhs}
    return PDE(
        name=name,
        fields=[u],
        rhs_substitutions=rhs_substitutions,
        constraints=[],
        scaling={"u": 1.0},  # u_λ(t, x) = λ u(λ²t, λx)
        notes=(
            "Viscous Burgers ∂_t u = νu_xx − u u_x. Known monotone: ∫ u² (energy); "
            "∫ u^{2k} for all k≥1 (by maximum principle + IBP). Inviscid develops shocks."
        ),
    )
