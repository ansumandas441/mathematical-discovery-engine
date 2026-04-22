"""Keller-Segel chemotaxis system.

Classical parabolic-elliptic form:
  ∂_t n = Δn - χ ∇·(n ∇c),
  -Δc = n - ⟨n⟩.

The 2D critical mass is 8π/χ. For a monotone-quantity search, conservation
of ∫n dx (mass) is trivial; the interesting questions involve ∫n log n
(entropy) and the free-energy ∫(n log n - ½nc) dx.

For v0.1 we expose a simplified scalar form that MonoQuant can handle:
  ∂_t n = Δn − ∇·(n ∇V(n))   with V a prescribed potential.

Fully coupled KS (with c coupled via elliptic equation) requires constraint
inversion beyond v0.1.
"""

from __future__ import annotations

import sympy as sp

from monoquant.pde import PDE, ScalarField


def keller_segel_simplified(chi: float = 1.0) -> PDE:
    """Scalar-only reduction: ∂_t n = Δn - χ ∇·(n ∇(n²/2))
    (assuming c ≈ n²/2 as a self-interaction proxy, i.e., local chemotactic)
    = Δn - χ (∇·(n·n∇n)) = Δn - χ ∇·(n²∇n) = Δn - χ ∂_x(n² n_x) in 1D.

    This is a toy 1D variant — full 2D Keller-Segel with elliptic chemoattractant
    coupling is v0.2.
    """
    n = ScalarField("n", spatial_dim=1)
    x = n.coords[0]
    laplacian = sp.diff(n.symbol, x, 2)
    chemotactic = sp.Rational(str(chi)) * sp.diff(n.symbol ** 2 * sp.diff(n.symbol, x), x)
    rhs = laplacian - chemotactic
    rhs_substitutions = {sp.diff(n.symbol, n.t): rhs}
    return PDE(
        name=f"keller_segel_simplified_chi{chi}",
        fields=[n],
        rhs_substitutions=rhs_substitutions,
        constraints=[],
        scaling={"n": 1.0},
        notes=(
            "Simplified 1D Keller-Segel with self-interaction c = n²/2. "
            "Full 2D KS requires elliptic coupling — v0.2 target. "
            "Known: ∫n dx conserved (mass); free-energy Ψ = ∫(n log n - ½nc) is "
            "monotone under fully-coupled KS below critical mass."
        ),
    )
