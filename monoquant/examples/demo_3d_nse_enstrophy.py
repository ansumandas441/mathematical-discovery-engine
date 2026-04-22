"""Test: does MonoQuant handle Φ = (1/2)|∇u|² for STANDARD 3D NSE?

In 3D NSE (not hyperdissipative), enstrophy is NOT monotone — that's the
heart of the Clay problem (vortex stretching drives enstrophy up).
But the symbolic engine should at least produce a derivation, not crash.
"""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

import sympy as sp

from monoquant import verify_functional
from monoquant.pdes import nse_3d_velocity


def main() -> None:
    pde = nse_3d_velocity(nu=1.0, drop_pressure=True)
    u = pde.fields[0]
    coords = pde.coords
    # Φ = (1/2) Σ_{i,j} (∂_j u_i)²
    phi = sp.Rational(1, 2) * sum(
        sp.diff(u.components[i].symbol, coords[j]) ** 2
        for i in range(3) for j in range(3)
    )
    print(f"PDE: {pde.name}")
    print(f"Φ = (1/2) Σ_{{ij}} (∂_j u_i)²  (classical 3D enstrophy)\n")
    try:
        result = verify_functional(pde, phi, verbose=True)
        print(f"\nVERDICT: {result['status']}")
    except Exception as e:
        print(f"\nERROR: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
