"""Korteweg-de Vries equation: ∂_t u + 6u·∂_x u + ∂³_x u = 0.

KdV is a completely integrable PDE with infinitely many conservation laws:
  - ∫u dx          (mass)
  - ∫u² dx         (momentum)
  - ∫(u³ - ½(∂_x u)²) dx   (energy; Miura)
  - ∫(5u⁴ - 10u(∂_x u)² + (∂²_x u)²) dx   (4th conservation)
  - ... infinitely many

A systematic search should rediscover these. A perfect validator for MonoQuant.
"""

from __future__ import annotations

import sympy as sp

from monoquant.pde import PDE, ScalarField


def kdv_equation() -> PDE:
    u = ScalarField("u", spatial_dim=1)
    x = u.coords[0]
    # Canonical KdV with coefficient 6.
    rhs = -6 * u.symbol * sp.diff(u.symbol, x) - sp.diff(u.symbol, x, 3)
    rhs_substitutions = {sp.diff(u.symbol, u.t): rhs}
    return PDE(
        name="kdv_1d",
        fields=[u],
        rhs_substitutions=rhs_substitutions,
        constraints=[],
        scaling={"u": 2.0},  # u_λ(t,x) = λ² u(λ³t, λx)
        notes=(
            "KdV ∂_t u + 6u·u_x + u_xxx = 0. Integrable; infinite conservation laws. "
            "Standard-basis rediscovery targets: ∫u, ∫u², ∫(u³ − ½u_x²), ..."
        ),
    )
