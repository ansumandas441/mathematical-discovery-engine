"""Zoo validator: run MonoQuant on the new PDEs."""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

import time

from monoquant import MonotoneSearch
from monoquant.pdes import (
    kdv_equation,
    keller_segel_simplified,
    cahn_hilliard,
    camassa_holm,
)


def run(pde, deg: int, dord: int) -> None:
    print(f"\n=== {pde.name}  |  deg≤{deg}, deriv≤{dord} ===")
    t0 = time.time()
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
    print(f"[elapsed: {elapsed:.2f}s]")


def main() -> None:
    print("--------- KDV ---------")
    run(kdv_equation(), deg=4, dord=2)

    print("\n--------- KELLER-SEGEL (simplified) ---------")
    run(keller_segel_simplified(chi=1.0), deg=2, dord=1)
    run(keller_segel_simplified(chi=1.0), deg=3, dord=2)

    print("\n--------- CAHN-HILLIARD ---------")
    run(cahn_hilliard(gamma=1.0), deg=2, dord=1)
    run(cahn_hilliard(gamma=1.0), deg=3, dord=2)
    run(cahn_hilliard(gamma=1.0), deg=4, dord=2)

    print("\n--------- CAMASSA-HOLM (m-form approx) ---------")
    run(camassa_holm(), deg=2, dord=1)
    run(camassa_holm(), deg=3, dord=2)


if __name__ == "__main__":
    main()
