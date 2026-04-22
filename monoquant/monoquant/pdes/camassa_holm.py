"""Camassa-Holm equation: ∂_t u - ∂_txx u + 3u·∂_x u = 2∂_x u · ∂_xx u + u · ∂_xxx u.

Integrable. Admits peakon solutions. Known Hamiltonian with infinite conservation.

Standard form via m = u - ∂_xx u:
  ∂_t m + u ∂_x m + 2 m ∂_x u = 0.

We model the u-equation directly for v0.1. Some conservation laws are:
  H₁ = ∫u dx       (momentum)
  H₂ = ½∫(u² + u_x²) dx   (energy; equivalent to H¹ norm)
  H₃ = ½∫(u³ + u u_x²) dx
"""

from __future__ import annotations

import sympy as sp

from monoquant.pde import PDE, ScalarField


def camassa_holm() -> PDE:
    u = ScalarField("u", spatial_dim=1)
    x = u.coords[0]
    u_x = sp.diff(u.symbol, x)
    u_xx = sp.diff(u.symbol, x, 2)
    u_xxx = sp.diff(u.symbol, x, 3)
    u_txx = sp.diff(u.symbol, u.t, x, 2)
    # The Camassa-Holm equation is
    #     u_t - u_txx = -3 u u_x + 2 u_x u_xx + u u_xxx.
    # Rearranging: u_t = u_txx - 3 u u_x + 2 u_x u_xx + u u_xxx.
    # But u_txx contains u_t, so we need to solve implicitly. For a first-pass
    # symbolic engine, we use the explicit "m-form" substitution: define
    # m = u - u_xx, then m_t = u_t - u_txx = -u m_x - 2 m u_x. So
    #     u_t = u_txx - u m_x - 2 m u_x
    # and u_txx = ∂_xx u_t. This recursion isn't directly solvable without
    # a nonlocal inversion operator (1 - ∂_xx)⁻¹.
    #
    # v0.1 workaround: encode the LOCAL form of the m-equation by treating
    # m = u - u_xx as a derived field with its own ∂_t m = -u m_x - 2 m u_x.
    # This loses the relation to u but lets us test MonoQuant on the m-form.
    rhs = -u.symbol * sp.diff(u.symbol - u_xx, x) - 2 * (u.symbol - u_xx) * u_x
    rhs_substitutions = {sp.diff(u.symbol, u.t): rhs}
    return PDE(
        name="camassa_holm_1d",
        fields=[u],
        rhs_substitutions=rhs_substitutions,
        constraints=[],
        scaling={"u": 2.0},
        notes=(
            "Camassa-Holm (m-form approximation). "
            "v0.1 encodes the LOCAL part; the full CH needs (1-∂_xx)⁻¹ which is nonlocal. "
            "Standard conservation: ∫u dx (momentum), ½∫(u²+u_x²) (H¹ energy)."
        ),
    )
