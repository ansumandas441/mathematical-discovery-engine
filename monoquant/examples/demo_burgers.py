"""Demo: 1D viscous Burgers. Expected conservation of ∫u dx, decay of ∫u² dx."""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

from monoquant import MonotoneSearch
from monoquant.pdes import burgers_equation


def main() -> None:
    pde = burgers_equation(nu=1.0)
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
