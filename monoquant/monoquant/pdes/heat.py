"""Heat equation ∂_t u = Δu on ℝ^d."""

from __future__ import annotations

import sympy as sp

from monoquant.pde import PDE, ScalarField


def heat_equation(spatial_dim: int = 1) -> PDE:
    u = ScalarField("u", spatial_dim=spatial_dim)
    laplacian = sum(sp.diff(u.symbol, x, 2) for x in u.coords)
    rhs_substitutions = {sp.diff(u.symbol, u.t): laplacian}
    return PDE(
        name=f"heat_{spatial_dim}d",
        fields=[u],
        rhs_substitutions=rhs_substitutions,
        constraints=[],
        scaling={"u": 0.0},  # Many choices possible; we use a neutral weight.
        notes="∂_t u = Δu. Many monotone quantities: ∫u² (energy), ∫|∇u|² (dissipation rate), etc.",
    )
