"""3D NSE at higher basis (poly≤3, deriv≤2).

This is the real search: the class of functionals Φ[u] that includes:
  - ∫|u|²      (energy, degree 2, deriv 0)    — should come out monotone
  - ∫|∇u|²    (enstrophy, degree 2, deriv 1)  — decays under NSE in 3D BUT
                                                  not sign-controlled by itself
                                                  due to vortex stretching
  - ∫u·ω      (helicity, degree 2, deriv 1)   — CONSERVED (inviscid); decays
                                                  viscous
  - ∫|ω|²     (3D enstrophy, degree 2, deriv 1) — NOT monotone in 3D (that's
                                                   the whole Clay problem!)

This run may take minutes; don't kill it unless you see 'Traceback'.
"""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

import time

from monoquant import MonotoneSearch
from monoquant.pdes import nse_3d_velocity


def main() -> None:
    pde = nse_3d_velocity(nu=1.0, drop_pressure=True)
    print(f"PDE: {pde.name}  (pressure dropped — results are valid for pressure-"
          "compatible Φ only)\n")

    t0 = time.time()
    search = MonotoneSearch(
        pde=pde,
        max_poly_degree=2,
        max_derivative_order=2,
        find_decrease=True,
        find_conservation=True,
    )
    result = search.run()
    elapsed = time.time() - t0
    print(result.pretty_print())
    print(f"\n[elapsed: {elapsed:.1f}s]")


if __name__ == "__main__":
    main()
