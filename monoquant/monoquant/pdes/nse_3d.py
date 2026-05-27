"""3D incompressible Navier–Stokes (the Clay target) — velocity formulation.

∂_t u_i + u_j ∂_j u_i = −∂_i p + ν Δ u_i,   ∂_j u_j = 0

For the monotone-quantity search, pressure is recovered via Leray projection
p = Δ^{-1} ∂_i ∂_j (u_i u_j), a nonlocal operation. In v0.1 we include the
nonlinear transport term explicitly but we accept that for functionals Φ[u]
depending on u and its spatial derivatives, pressure contributes divergence-
form terms that vanish under IBP for many (but not all) Φ. Pressure-dependent
Φ cannot be correctly analysed in v0.1.

This v0.1 state is sufficient for searching the class of functionals that
Constantin–Fefferman, Chae, Beale–Kato–Majda, and the Perelman-analogue
literature all live in.
"""

from __future__ import annotations

import sympy as sp

from monoquant.pde import PDE, VectorField


def nse_3d_velocity(nu: float = 1.0, drop_pressure: bool = True) -> PDE:
    """3D incompressible NSE.

    If `drop_pressure=True` (default in v0.1), the pressure gradient is omitted
    from the symbolic RHS. This is VALID for functionals Φ[u] that integrate to
    a divergence-form pressure contribution (most classical monotone-quantity
    candidates fall in this class). The search result includes a warning when
    a candidate's pressure contribution cannot be verified.
    """
    u = VectorField("u", spatial_dim=3)
    coords = u.coords
    rhs_substitutions = {}
    for i, ui in enumerate(u.components):
        viscous = sp.Rational(str(nu)) * sum(
            sp.diff(ui.symbol, x, 2) for x in coords
        )
        transport = sum(
            u.components[j].symbol * sp.diff(ui.symbol, coords[j])
            for j in range(3)
        )
        rhs_i = viscous - transport
        if not drop_pressure:
            # A symbolic placeholder; not used in v0.1.
            p = sp.Function("p")(ui.t, *coords)
            rhs_i = rhs_i - sp.diff(p, coords[i])
        rhs_substitutions[sp.diff(ui.symbol, ui.t)] = rhs_i
    # divergence-free constraint
    div_u = u.divergence()
    return PDE(
        name="nse_3d_velocity",
        fields=[u],
        rhs_substitutions=rhs_substitutions,
        constraints=[div_u],
        scaling={"u": 1.0},  # u_λ = λ u(λ²t, λx)
        notes=(
            "3D incompressible NSE in velocity form. Pressure omitted in v0.1: "
            "valid for Φ whose pressure contribution integrates by parts to zero. "
            "Candidates returned should be reviewed for pressure-compatibility before use."
        ),
    )
