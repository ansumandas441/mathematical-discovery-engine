"""KdV: validate by rediscovering the infinite-conservation-law tower.

Expected at low basis:
  degree≤2, deriv≤0:  ∫u dx conserved (mass)
  degree≤2, deriv≤1:  ∫u² dx conserved (momentum)
  degree≤3, deriv≤1:  ∫(u³ - ½u_x²) dx conserved (energy; Miura-transform invariant)
  degree≤4, deriv≤2:  ∫(5u⁴ - 10u·u_x² + u_xx²) dx ...
"""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

import time

from monoquant import MonotoneSearch
from monoquant.pdes import kdv_equation


def main() -> None:
    pde = kdv_equation()
    print(f"PDE: {pde.name}")
    print(f"Notes: {pde.notes}\n")

    for deg, dord in [(2, 0), (2, 1), (3, 1), (3, 2)]:
        t0 = time.time()
        print(f"\n=== Search at poly_degree≤{deg}, deriv_order≤{dord} ===")
        search = MonotoneSearch(
            pde=pde,
            max_poly_degree=deg,
            max_derivative_order=dord,
            find_decrease=True,
            find_conservation=True,
            verbose=False,
        )
        result = search.run()
        elapsed = time.time() - t0
        print(result.pretty_print())
        print(f"[elapsed: {elapsed:.1f}s]")


if __name__ == "__main__":
    main()
