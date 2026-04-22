"""Demo: recover known monotone quantities for the 1D heat equation.

Expected output:
  - Conservation: ∫u dx (mass)
  - Decrease:     ∫u² dx (energy)
  - At higher degree: ∫(u_x)² dx, ∫u² log u²... (these are beyond v0.1 basis)
"""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

from monoquant import MonotoneSearch
from monoquant.pdes import heat_equation


def main() -> None:
    pde = heat_equation(spatial_dim=1)
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
