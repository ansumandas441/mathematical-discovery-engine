"""Hyperdissipative 3D NSE at α = 1.2.

This is the real discovery experiment from iter-4 sub-problem SP4:
  - Tao 2009 proved α ≥ 5/4 implies global smoothness.
  - α = 1 is the Clay problem (open).
  - α = 1.2 sits in the gap — live research zone.

We verify:
  (a) Φ = ½|u|²  — L² energy. Should be CERTIFIED-DECREASE.
  (b) Φ = ½|u|² with Variant A (multi-scale dissipation).
"""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

import sympy as sp

from monoquant import verify_functional
from monoquant.pdes import nse_3d_hyperdissipative, nse_3d_multiscale


def run_base(alpha: float) -> None:
    print(f"\n=== HYPERDISSIPATIVE 3D NSE at α = {alpha} ===")
    pde = nse_3d_hyperdissipative(alpha=alpha, nu=1.0, drop_pressure=True)
    print(f"PDE: {pde.name}")
    print(f"Notes: {pde.notes}\n")
    # Candidate Φ: (1/2)|u|².
    phi = sp.Rational(1, 2) * sum(c.symbol ** 2 for c in pde.fields[0].components)
    print("Candidate Φ = (1/2) Σ u_i²  (L² kinetic energy density)")
    result = verify_functional(pde, phi, verbose=True)
    print(f"VERDICT: {result['status']}")


def run_multiscale(alpha1: float, alpha2: float) -> None:
    print(f"\n=== MULTI-SCALE DISSIPATION: (-Δ)^{alpha1} + (-Δ)^{alpha2} ===")
    pde = nse_3d_multiscale(alpha1=alpha1, alpha2=alpha2)
    print(f"PDE: {pde.name}")
    print(f"Notes: {pde.notes}\n")
    phi = sp.Rational(1, 2) * sum(c.symbol ** 2 for c in pde.fields[0].components)
    print("Candidate Φ = (1/2) Σ u_i²  (L² kinetic energy density)")
    result = verify_functional(pde, phi, verbose=True)
    print(f"VERDICT: {result['status']}")


def main() -> None:
    # Base case: α = 1.2
    run_base(alpha=1.2)
    # Variant A: multi-scale dissipation at α1=1.2, α2=0.8
    run_multiscale(alpha1=1.2, alpha2=0.8)
    # Also test at the Clay-critical α = 1.0 and at the Tao-safe α = 1.25
    run_base(alpha=1.0)
    run_base(alpha=1.25)


if __name__ == "__main__":
    main()
