"""Demo: 2D NSE vorticity. Expected:
  - Conservation of ∫ω dx (vanishes for decay-at-∞)
  - Decay of ∫ω² dx (enstrophy)
"""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

from monoquant import MonotoneSearch
from monoquant.pdes import nse_2d_vorticity


def main() -> None:
    pde = nse_2d_vorticity(nu=1.0)
    print(f"PDE: {pde.name}")
    print(f"Notes: {pde.notes}\n")

    search = MonotoneSearch(
        pde=pde,
        max_poly_degree=2,
        max_derivative_order=1,
        find_decrease=True,
        find_conservation=True,
    )
    result = search.run()
    print(result.pretty_print())


if __name__ == "__main__":
    main()
