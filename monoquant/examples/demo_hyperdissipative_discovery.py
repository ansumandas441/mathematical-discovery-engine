"""Discovery experiment: hunt for NEW monotone quantities of hyperdissipative 3D NSE.

Already-known monotone for Φ = ½|u|²: Leray fractional energy inequality.
Here we try other candidate functionals at α = 1.2 — the sub-5/4-Clay zone.
"""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

import sympy as sp

from monoquant import verify_functional
from monoquant.pdes import nse_3d_hyperdissipative
from monoquant.fractional import FracLap


def try_functional(pde, phi, label: str) -> None:
    print(f"\n--- Candidate Φ: {label} ---")
    print(f"Φ = {phi}")
    try:
        result = verify_functional(pde, phi, verbose=False)
        print(f"VERDICT: {result['status']}")
        if "dphi_dt_reduced" in result:
            reduced = result["dphi_dt_reduced"]
            n_terms = len(reduced.args) if isinstance(reduced, sp.Add) else 1
            print(f"  (Q has {n_terms} terms after reduction)")
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")


def main() -> None:
    alpha = 1.2
    pde = nse_3d_hyperdissipative(alpha=alpha, nu=1.0, drop_pressure=True)
    print(f"PDE: {pde.name}  (α = {alpha})\n")

    u1 = pde.fields[0].components[0].symbol
    u2 = pde.fields[0].components[1].symbol
    u3 = pde.fields[0].components[2].symbol
    x1, x2, x3 = pde.coords

    # (1) L² energy — known DECREASE.
    phi1 = sp.Rational(1, 2) * (u1**2 + u2**2 + u3**2)
    try_functional(pde, phi1, "(1/2) |u|²  (L² energy)")

    # (2) L⁴ — scaling-different functional.
    phi2 = sp.Rational(1, 4) * (u1**2 + u2**2 + u3**2) ** 2
    try_functional(pde, phi2, "(1/4) |u|⁴  (L⁴ norm)")

    # (3) Ḣ^α/2 Sobolev (FracLap-based).
    beta = sp.Rational(6, 10)  # α/2
    phi3 = sp.Rational(1, 2) * (
        FracLap(u1, beta) ** 2 + FracLap(u2, beta) ** 2 + FracLap(u3, beta) ** 2
    )
    try_functional(pde, phi3, "(1/2) Σ |FracLap(u_i, α/2)|²  (Ḣ^{α/2} Sobolev)")

    # (4) Enstrophy analogue in fractional form: Ḣ^{1/2}.
    beta = sp.Rational(1, 2)
    phi4 = sp.Rational(1, 2) * (
        FracLap(u1, beta) ** 2 + FracLap(u2, beta) ** 2 + FracLap(u3, beta) ** 2
    )
    try_functional(pde, phi4, "(1/2) Σ |FracLap(u_i, 1/2)|²  (Ḣ^{1/2} Sobolev)")

    # (5) Enstrophy: ∫|∇u|² — should relate to fractional Sobolev.
    grad_sq = sum(sp.diff(u, x) ** 2 for u in [u1, u2, u3] for x in [x1, x2, x3])
    phi5 = sp.Rational(1, 2) * grad_sq
    try_functional(pde, phi5, "(1/2) |∇u|²  (classical enstrophy)")

    # (6) Linear combination: energy + enstrophy.
    phi6 = phi1 + phi5
    try_functional(pde, phi6, "(1/2) |u|² + (1/2) |∇u|²  (energy + enstrophy)")

    # (7) Higher-order: ∫|(-Δ)u|² = (Ḣ²).
    phi7 = sp.Rational(1, 2) * (
        FracLap(u1, 1) ** 2 + FracLap(u2, 1) ** 2 + FracLap(u3, 1) ** 2
    )
    try_functional(pde, phi7, "(1/2) Σ |FracLap(u_i, 1)|²  (Ḣ¹ via FracLap)")

    # (8) Mixed scaling.
    phi8 = u1 * u2 + u2 * u3 + u3 * u1  # symmetric cross-term
    try_functional(pde, phi8, "u·[off-diagonal mixing]  (non-standard)")

    # (9) Pure cubic — expected NOT monotone.
    phi9 = u1**3 + u2**3 + u3**3
    try_functional(pde, phi9, "Σ u_i³  (pure cubic)")


if __name__ == "__main__":
    main()
