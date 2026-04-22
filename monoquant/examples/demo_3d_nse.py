"""Demo: 3D NSE search. Expected at deg≤2 deriv≤1:
  - Conservation of ∫u_i dx (momentum components, in the v0.1 no-pressure mode)
  - Decay of ∫|u|² dx (energy)

Higher-degree outputs (beyond v0.1 basis): enstrophy ∫|∇u|², helicity ∫u·ω.
"""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

import time

from monoquant import MonotoneSearch
from monoquant.pdes import nse_3d_velocity


def main() -> None:
    pde = nse_3d_velocity(nu=1.0, drop_pressure=True)
    print(f"PDE: {pde.name}")
    print(f"Notes: {pde.notes}\n")

    t0 = time.time()
    search = MonotoneSearch(
        pde=pde,
        max_poly_degree=2,
        max_derivative_order=1,
        find_decrease=True,
        find_conservation=True,
    )
    result = search.run()
    elapsed = time.time() - t0
    print(result.pretty_print())
    print(f"\n[elapsed: {elapsed:.2f}s]")


if __name__ == "__main__":
    main()
