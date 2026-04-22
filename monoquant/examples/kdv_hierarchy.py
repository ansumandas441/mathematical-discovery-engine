"""KdV hierarchy enumeration via the scaling-weight prefilter.

For each target scaling weight W ∈ {2, 4, 6, ...}, enumerate all monomials of
exact weight W, solve the Euler–Lagrange linear system, and report the
conservation laws. Group the laws into:

  - trivial: the integrand itself is a total derivative (E_u(φ) ≡ 0). These
    contribute 0 to the functional integral — not real conservation content.
  - nontrivial: distinct conservation laws modulo IBP equivalence. At weight
    W = 2n, KdV has (generically) exactly ONE new nontrivial Hamiltonian H_n
    (plus wedge/product echoes of lower H's, which also show up).

Reference (Drazin–Johnson / Miura–Gardner–Kruskal 1968 convention):
  W=2:  H_1 = ∫ u dx                       (mass)
  W=4:  H_2 = ∫ u² dx                      (momentum)
  W=6:  H_3 = ∫ (u³ − ½ u_x²) dx           (Miura)
  W=8:  H_4 = ∫ (5u⁴ − 10 u u_x² + u_xx²) dx  (Miura–Gardner 1968)
  W=10: H_5 = ∫ (... higher order ...) dx
  ...

Note: MonoQuant finds the conservation-law space. For each weight, we print all
independent solutions of E_u(∂_t Φ) ≡ 0, then classify.
"""

import sys
import time

sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

import sympy as sp

from monoquant import HierarchyConservationSearch
from monoquant.pdes import kdv_equation
from monoquant.symbolic import TimeDerivativeEngine


def classify_conservation(phi: sp.Expr, engine: TimeDerivativeEngine, pde) -> str:
    """Trivial iff E_u(phi) ≡ 0 directly (i.e. the integrand is already a
    total spatial derivative, so ∫phi dx = 0 on decay data).
    """
    for f in pde.fields:
        E = sp.expand(engine.euler_lagrange(phi, f))
        if E != 0:
            return "nontrivial"
    return "trivial"


def verify_by_el_of_dt(phi: sp.Expr, engine: TimeDerivativeEngine, pde) -> bool:
    """Independent check: compute ∂_t φ, apply E_u to each field, expect 0."""
    dphi = engine.dphi_dt_pointwise(phi)
    for f in pde.fields:
        E = sp.expand(engine.euler_lagrange(dphi, f))
        if E != 0:
            return False
    return True


def canonicalize_sign(phi: sp.Expr) -> sp.Expr:
    """Prefer the sign with positive leading rational coefficient for u^n."""
    # Find coefficient of highest power of u (the 'leading' nonlinear term).
    # If negative, flip sign.
    try:
        u_sym = None
        for a in phi.atoms(sp.core.function.AppliedUndef):
            u_sym = a
            break
        if u_sym is None:
            return phi
        # Expand, find the term with maximum power of u (no derivatives).
        expr = sp.expand(phi)
        max_pow = 0
        best_coef = None
        if isinstance(expr, sp.Add):
            terms = expr.args
        else:
            terms = [expr]
        for t in terms:
            # Does t contain ONLY powers of u (no derivatives)?
            has_deriv = any(isinstance(a, sp.Derivative) for a in sp.preorder_traversal(t))
            if has_deriv:
                continue
            # Coefficient of u^n
            poly = sp.Poly(t, u_sym)
            deg = poly.total_degree()
            if deg > max_pow:
                max_pow = deg
                best_coef = poly.LC()
        if best_coef is not None and best_coef < 0:
            return -phi
        return phi
    except Exception:
        return phi


def main() -> None:
    pde = kdv_equation()
    engine = TimeDerivativeEngine(pde)
    print(f"PDE: {pde.name}")
    print(f"Scaling: u_λ(t, x) = λ² u(λ³t, λx)   →   [u]=2, [∂_x^k u]=2+k")
    print(f"{pde.notes}\n")

    # Track summary per weight.
    summary = []
    # Weights to scan. W=2..16 should reach H_1..H_8.
    weights = [2, 4, 6, 8, 10, 12, 14, 16]

    for W in weights:
        t0 = time.time()
        # Bound per-deriv order by W (the heaviest single-atom has this weight).
        search = HierarchyConservationSearch(
            pde=pde,
            weight=W,
            max_poly_degree=max(8, W // 2 + 2),
            max_derivative_order=W,
            base_weight={"u": 2},
            verbose=False,
        )
        result = search.run()
        elapsed = time.time() - t0
        basis_size = result.meta["candidates"]
        laws = result.conserved
        # Classify each law.
        trivial = []
        nontrivial = []
        for c in laws:
            phi = sp.expand(c.functional)
            kind = classify_conservation(phi, engine, pde)
            if kind == "trivial":
                trivial.append(phi)
            else:
                nontrivial.append(canonicalize_sign(phi))
        print(f"=" * 72)
        print(f"W = {W} (expected H_{W//2})")
        print(f"   basis size: {basis_size}  |  total laws: {len(laws)}  "
              f"|  nontrivial: {len(nontrivial)}  |  trivial (∫=0): {len(trivial)}"
              f"  |  time: {elapsed:.2f}s")
        if nontrivial:
            print(f"   Nontrivial conservation laws (integrand is NOT a total derivative):")
            for phi in nontrivial:
                # Double-check via the direct ∂_t φ → E_u path.
                ok = verify_by_el_of_dt(phi, engine, pde)
                mark = "✓" if ok else "✗"
                print(f"      [{mark}] {phi}")
        if trivial:
            print(f"   Trivial laws (integrand = total derivative; ∫φ dx = 0):")
            for phi in trivial:
                print(f"      {phi}")
        summary.append({
            "W": W,
            "basis_size": basis_size,
            "total_laws": len(laws),
            "nontrivial": len(nontrivial),
            "trivial": len(trivial),
            "time_s": elapsed,
            "laws": nontrivial,
        })
        # Combinatorial guard rail — stop if basis > 500 or time > 10 min.
        if basis_size > 500:
            print(f"\n[stop] basis size {basis_size} > 500; combinatorics too large.")
            break
        if elapsed > 600:
            print(f"\n[stop] weight {W} took {elapsed:.0f}s > 10 min; stopping.")
            break

    print("\n" + "=" * 72)
    print("SUMMARY TABLE")
    print(f"{'W':>4} {'n (H_n)':>8} {'basis':>7} {'laws':>5} {'nontriv':>8} {'trivial':>8} {'time (s)':>10}")
    for s in summary:
        print(
            f"{s['W']:>4} {s['W']//2:>8} {s['basis_size']:>7} "
            f"{s['total_laws']:>5} {s['nontrivial']:>8} {s['trivial']:>8} {s['time_s']:>10.2f}"
        )


if __name__ == "__main__":
    main()
