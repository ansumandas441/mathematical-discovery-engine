"""Hyperdissipative 3D NSE: ∂_t u + (u·∇)u = -∇p + ν(-Δ)^α u, ∇·u = 0.

For α ≥ 5/4, Katz-Pavlović 2002 / Tao 2009 prove global smoothness.
For α < 5/4 (including α = 1), global smoothness is OPEN.
α = 1.2 sits just below the 5/4 threshold — a live research zone.

This module exposes:
  - `nse_3d_hyperdissipative(alpha=1.2)` — the base equation
  - `nse_3d_multiscale(alpha1=1.2, alpha2=0.8)` — Variant A (two dissipation scales)
"""

from __future__ import annotations

import sympy as sp

from monoquant.pde import PDE, VectorField
from monoquant.fractional import FracLap


def nse_3d_hyperdissipative(
    alpha: float = 1.2,
    nu: float = 1.0,
    drop_pressure: bool = True,
) -> PDE:
    u = VectorField("u", spatial_dim=3)
    coords = u.coords
    rhs_substitutions = {}
    for i, ui in enumerate(u.components):
        viscous = -sp.Rational(str(nu)) * FracLap(ui.symbol, sp.Rational(str(alpha)))
        transport = sum(
            u.components[j].symbol * sp.diff(ui.symbol, coords[j])
            for j in range(3)
        )
        rhs_i = viscous - transport
        if not drop_pressure:
            p = sp.Function("p")(ui.t, *coords)
            rhs_i = rhs_i - sp.diff(p, coords[i])
        rhs_substitutions[sp.diff(ui.symbol, ui.t)] = rhs_i
    div_u = u.divergence()
    return PDE(
        name=f"nse_3d_hyperdissipative_alpha{alpha}",
        fields=[u],
        rhs_substitutions=rhs_substitutions,
        constraints=[div_u],
        scaling={"u": (2 * alpha - 1)},
        notes=(
            f"Hyperdissipative 3D NSE with dissipation order α = {alpha}. "
            f"Global smoothness: KNOWN for α ≥ 5/4; OPEN for α < 5/4. "
            f"α = {alpha} is the target of sub-problem SP4 from iter 4. "
            f"Pressure omitted under drop_pressure=True (safe for Φ whose pressure "
            "contribution integrates by parts to zero)."
        ),
    )


def nse_3d_multiscale(
    alpha1: float = 1.2,
    alpha2: float = 0.8,
    nu1: float = 1.0,
    nu2: float = 0.5,
    drop_pressure: bool = True,
) -> PDE:
    """Variant A: dual-scale dissipation.

    ∂_t u + (u·∇)u + ∇p = ν₁(-Δ)^{α1} u + ν₂(-Δ)^{α2} u

    Having two dissipation scales provides different physical regulation at
    low and high frequency. If α1 > 5/4 the high-frequency regulation alone
    gives smoothness; the interesting case is both α1, α2 < 5/4.
    """
    u = VectorField("u", spatial_dim=3)
    coords = u.coords
    rhs_substitutions = {}
    for i, ui in enumerate(u.components):
        viscous1 = -sp.Rational(str(nu1)) * FracLap(ui.symbol, sp.Rational(str(alpha1)))
        viscous2 = -sp.Rational(str(nu2)) * FracLap(ui.symbol, sp.Rational(str(alpha2)))
        transport = sum(
            u.components[j].symbol * sp.diff(ui.symbol, coords[j])
            for j in range(3)
        )
        rhs_i = viscous1 + viscous2 - transport
        if not drop_pressure:
            p = sp.Function("p")(ui.t, *coords)
            rhs_i = rhs_i - sp.diff(p, coords[i])
        rhs_substitutions[sp.diff(ui.symbol, ui.t)] = rhs_i
    div_u = u.divergence()
    return PDE(
        name=f"nse_3d_multiscale_a{alpha1}_a{alpha2}",
        fields=[u],
        rhs_substitutions=rhs_substitutions,
        constraints=[div_u],
        scaling={"u": (2 * max(alpha1, alpha2) - 1)},
        notes=(
            f"Multi-scale dissipation 3D NSE: ν₁ (-Δ)^{alpha1} + ν₂ (-Δ)^{alpha2}. "
            "Two-scale viscosity. If both α_i < 5/4, global smoothness is open."
        ),
    )
