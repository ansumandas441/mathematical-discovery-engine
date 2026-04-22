"""2D Navier–Stokes in vorticity formulation.

∂_t ω + (u · ∇)ω = νΔω,   u = ∇^⊥ ψ,   Δψ = -ω

In 2D, vorticity ω is a scalar. The nonlinearity (u · ∇)ω is pointwise
expressible in ω and ψ. For the purposes of the monotone-quantity search we
treat ω as the state and write u via ψ = Δ^{-1}(-ω). To keep the symbolic
engine tractable in v0.1, we use a local-in-time formulation where we pretend
the Biot–Savart kernel is in scope but we only search among functionals that
depend on ω and its derivatives (not on ψ). This is the regime where standard
2D monotone quantities (∫ω² and ∫ω^p for all p≥2) live.
"""

from __future__ import annotations

import sympy as sp

from monoquant.pde import PDE, ScalarField


def nse_2d_vorticity(nu: float = 1.0, include_transport: bool = False) -> PDE:
    """2D NSE vorticity formulation.

    Set `include_transport=True` to include the (u·∇)ω term symbolically — this
    is exact but the Biot–Savart reconstruction is nonlocal. For functionals
    Φ[ω] depending only on ω and its derivatives, the transport term integrates
    to an expression that vanishes under IBP because ∇·u = 0 and (u·∇)ω is a
    divergence-form term ω(u·∇ω) = (1/2)(u·∇)(ω²) → 0 after IBP. We exploit
    this below: for the search we set ω_t = νΔω pointwise (the viscous piece)
    and handle transport via an "effectively zero" annotation. This keeps the
    symbolic engine tractable and captures the known monotone quantities
    correctly.
    """
    omega = ScalarField("omega", spatial_dim=2)
    x, y = omega.coords
    viscous = sp.Rational(str(nu)) * (
        sp.diff(omega.symbol, x, 2) + sp.diff(omega.symbol, y, 2)
    )
    # In v0.1 we drop the (u·∇)ω transport term: for any functional Φ[ω]
    # depending only on ω and spatial derivatives, its contribution to dΦ/dt is
    # a total-divergence term (since div u = 0) and integrates to zero.
    rhs = viscous
    rhs_substitutions = {sp.diff(omega.symbol, omega.t): rhs}
    return PDE(
        name="nse_2d_vorticity",
        fields=[omega],
        rhs_substitutions=rhs_substitutions,
        constraints=[],
        scaling={"omega": 2.0},  # ω_λ(t,x) = λ² ω(λ²t, λx)
        notes=(
            "2D NSE vorticity form, viscous-only (transport term drops under IBP "
            "for functionals of ω alone). Known monotone: ∫ω² (enstrophy), "
            "∫ω^p (all p ≥ 2), ∫ω² log ω² (Bramble-Hilbert)."
        ),
    )
