"""Cahn-Hilliard equation: ∂_t u = Δ(u³ - u - γΔu).

Gradient flow of Ginzburg-Landau energy F[u] = ∫(¼(u²-1)² + ½γ|∇u|²) dx.

Known monotone: F[u] itself (the free energy), along with ∫u dx (mass).
"""

from __future__ import annotations

import sympy as sp

from monoquant.pde import PDE, ScalarField


def cahn_hilliard(gamma: float = 1.0) -> PDE:
    u = ScalarField("u", spatial_dim=1)
    x = u.coords[0]
    # Chemical potential μ = u³ - u - γ Δu.
    mu = u.symbol ** 3 - u.symbol - sp.Rational(str(gamma)) * sp.diff(u.symbol, x, 2)
    # ∂_t u = Δ μ
    rhs = sp.diff(mu, x, 2)
    rhs_substitutions = {sp.diff(u.symbol, u.t): rhs}
    return PDE(
        name=f"cahn_hilliard_gamma{gamma}",
        fields=[u],
        rhs_substitutions=rhs_substitutions,
        constraints=[],
        scaling={"u": 0.0},
        notes=(
            "Cahn-Hilliard ∂_t u = Δ(u³ - u - γΔu). "
            "Gradient flow of ∫(¼(u²-1)² + ½γu_x²) dx — this free energy is monotone decreasing. "
            "Mass ∫u dx is conserved."
        ),
    )
