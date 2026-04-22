"""Debug: verify that PDE.impose_constraints actually substitutes."""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

import sympy as sp
from monoquant.pdes import nse_3d_velocity


def main() -> None:
    pde = nse_3d_velocity(nu=1.0, drop_pressure=True)
    u1 = pde.fields[0].components[0].symbol
    u2 = pde.fields[0].components[1].symbol
    u3 = pde.fields[0].components[2].symbol
    x1, x2, x3 = pde.coords
    # Build a test expression containing Derivative(u3, x3).
    test_expr = u1 * sp.diff(u3, x3) + u2 ** 2 * sp.diff(u3, x3)
    print(f"test_expr = {test_expr}")
    print(f"constraints = {pde.constraints}")
    print(f"constraint atoms: {[a for a in sp.preorder_traversal(pde.constraints[0]) if isinstance(a, sp.Derivative)]}")
    out = pde.impose_constraints(test_expr)
    print(f"after impose_constraints: {out}")

    # Manual check: can we do the substitution by hand?
    atoms_in_expr = [sub for sub in sp.preorder_traversal(test_expr) if isinstance(sub, sp.Derivative)]
    print(f"atoms in test_expr: {atoms_in_expr}")
    print(f"ID(atoms[0]) in constraint? {atoms_in_expr[0] == pde.constraints[0].args[-1]}")
    # Dummy-swap manually:
    u3_x3_atom = [a for a in atoms_in_expr if "u3" in str(a)][0]
    dummy = sp.Symbol("_D")
    replaced = test_expr.xreplace({u3_x3_atom: dummy})
    print(f"after xreplace with dummy: {replaced}")
    # Now substitute dummy -> -u1_x1 - u2_x2
    u1_x1 = sp.diff(u1, x1)
    u2_x2 = sp.diff(u2, x2)
    out2 = replaced.subs(dummy, -u1_x1 - u2_x2)
    print(f"after manual subs: {out2}")


if __name__ == "__main__":
    main()
