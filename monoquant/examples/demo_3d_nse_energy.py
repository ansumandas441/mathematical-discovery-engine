"""Verify that ∫(1/2)|u|² dx decays under 3D Navier-Stokes.

This is the no-search mode: we hand MonoQuant a specific Φ and ask whether it's
monotone. For 3D NSE this recovers Leray's energy inequality:
    (d/dt) ∫(1/2)|u|² dx = -ν ∫|∇u|² dx ≤ 0.
"""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

import sympy as sp

from monoquant import verify_functional
from monoquant.pdes import nse_3d_velocity


def main() -> None:
    pde = nse_3d_velocity(nu=1.0, drop_pressure=True)
    # Build Φ = (1/2) Σ u_i²  (kinetic energy density).
    phi = sp.Rational(1, 2) * sum(comp.symbol ** 2 for comp in pde.fields[0].components)
    print(f"PDE: {pde.name}")
    print(f"Candidate Φ = (1/2) |u|² = {phi}\n")
    result = verify_functional(pde, phi, verbose=True)
    print(f"\nVerdict: {result['status']}")


if __name__ == "__main__":
    main()
