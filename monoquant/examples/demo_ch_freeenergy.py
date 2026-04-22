"""Cahn-Hilliard free energy test.

Known: the Ginzburg-Landau free energy
    F[u] = ∫(¼(u²-1)² + ½γ|∇u|²) dx
       = ∫(¼u⁴ - ½u² + ¼ + ½γu_x²) dx
is monotone decreasing under Cahn-Hilliard ∂_t u = Δμ, μ = u³ - u - γΔu.

Proof: dF/dt = ∫μ·Δμ dx = -∫|∇μ|² dx ≤ 0.

Verify with MonoQuant.
"""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

import sympy as sp

from monoquant import verify_functional
from monoquant.pdes import cahn_hilliard


def main() -> None:
    pde = cahn_hilliard(gamma=1.0)
    u = pde.fields[0].symbol
    x = pde.coords[0]
    gamma = sp.Rational(1, 1)
    # Free energy density (drop constant +1/4 term — doesn't affect monotonicity).
    F = sp.Rational(1, 4) * u ** 4 - sp.Rational(1, 2) * u ** 2 + sp.Rational(1, 2) * gamma * sp.diff(u, x) ** 2
    print(f"Candidate Φ = Ginzburg-Landau free energy density")
    print(f"  F = {F}\n")
    result = verify_functional(pde, F, verbose=True)
    print(f"\nVERDICT: {result['status']}")


if __name__ == "__main__":
    main()
