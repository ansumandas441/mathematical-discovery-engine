"""Smoke test: basis enumeration and pointwise d/dt for heat equation."""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

import sympy as sp
from monoquant.pdes import heat_equation
from monoquant.invariants import PolynomialInvariantBasis
from monoquant.symbolic import TimeDerivativeEngine


def main() -> None:
    pde = heat_equation(spatial_dim=1)
    print(f"PDE: {pde.name}")
    basis = PolynomialInvariantBasis(
        pde=pde,
        max_poly_degree=2,
        max_derivative_order=1,
    )
    mons = basis.enumerate()
    print(f"Enumerated {len(mons)} monomials:")
    for m in mons:
        print(f"  coef={m.coefficient_symbol}  expr={m.as_expr(pde)}  "
              f"poly_deg={m.polynomial_degree}  deriv_order={m.derivative_order}")

    print("\nBuilding ansatz Φ = Σ c_i m_i ...")
    phi = sum(m.coefficient_symbol * m.as_expr(pde) for m in mons)
    print(f"Φ = {phi}")

    print("\nComputing pointwise ∂_t Φ ...")
    engine = TimeDerivativeEngine(pde)
    dphi = engine.dphi_dt_pointwise(phi)
    print(f"∂_t Φ (pointwise) = {dphi}")

    print("\nIntegrating by parts ...")
    dphi_ibp = engine.integrate_by_parts(dphi)
    print(f"∂_t Φ (after IBP) = {dphi_ibp}")


if __name__ == "__main__":
    main()
