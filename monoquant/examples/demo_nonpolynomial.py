"""Non-polynomial Φ candidates on simple PDEs.

These test the v0.2 non-polynomial extension: MonoQuant should now accept
Φ = n·log(n) (Boltzmann entropy), Φ = u²·log(1+u²) (logarithmic perturbation),
and similar non-polynomial functionals.
"""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

import sympy as sp

from monoquant import verify_functional
from monoquant.pdes import (
    heat_equation,
    keller_segel_simplified,
    burgers_equation,
)


def test(pde, phi, label: str) -> None:
    print(f"\n--- {label} ---")
    print(f"  Φ = {phi}")
    try:
        result = verify_functional(pde, phi, verbose=False)
        print(f"  VERDICT: {result['status']}")
        if 'dphi_dt_reduced' in result:
            reduced = result['dphi_dt_reduced']
            if isinstance(reduced, sp.Add):
                n = len(reduced.args)
            else:
                n = 1
            print(f"  Q has {n} terms")
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")


def main() -> None:
    # Heat equation: entropy ∫u·log u (on u > 0 regime) should be MONOTONE.
    pde = heat_equation(spatial_dim=1)
    u = pde.fields[0].symbol

    test(pde, u * sp.log(u), "Heat: Boltzmann entropy ∫ u log u")
    test(pde, sp.log(1 + u**2), "Heat: smoothed log(1 + u²)")
    test(pde, sp.exp(-u**2), "Heat: Gaussian ∫ exp(-u²)")
    test(pde, u ** 4, "Heat: L⁴ (polynomial baseline)")

    # Burgers: same family.
    pde = burgers_equation(nu=1.0)
    u = pde.fields[0].symbol
    test(pde, u * sp.log(u**2 + 1), "Burgers: u·log(u²+1) (smoothed variant)")
    test(pde, u ** 4, "Burgers: L⁴ norm")
    test(pde, u ** 6, "Burgers: L⁶ norm")

    # Simplified Keller-Segel: entropy ∫ n log n.
    pde = keller_segel_simplified(chi=1.0)
    n = pde.fields[0].symbol
    test(pde, n * sp.log(n), "Keller-Segel (simplified): entropy ∫ n log n")
    test(pde, n ** 2 / 2, "Keller-Segel: L² baseline")


if __name__ == "__main__":
    main()
