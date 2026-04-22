"""Katz-Pavlović dyadic shell model: N=3, alpha=0 (no dissipation).

Expected: ∑ a_n² is conserved.
"""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

from monoquant import MonotoneSearch
from monoquant.pdes import dyadic_shell


def main() -> None:
    pde = dyadic_shell(N=3, alpha=0.0, lam=2.0)
    print(f"PDE: {pde.name}")
    print(f"Notes: {pde.notes}\n")
    search = MonotoneSearch(
        pde=pde,
        max_poly_degree=2,
        max_derivative_order=0,
        find_decrease=True,
        find_conservation=True,
    )
    result = search.run()
    print(result.pretty_print())


if __name__ == "__main__":
    main()
