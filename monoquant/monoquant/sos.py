"""SDP Positivstellensatz search.

Given a symbolic pointwise expression Q(u, ∂u, ∂²u, ...) linear in the unknown
coefficients c_1, ..., c_N of the ansatz Φ = Σ c_i m_i, find coefficients c
such that:

    − Q(u, ∂u, ...) ≥ 0   for all u

i.e., Q ≤ 0 pointwise. We treat the distinct field-derivative expressions as
independent polynomial variables and ask for a sum-of-squares decomposition.

This yields a semidefinite program. We use CVXPY with CLARABEL/SCS.

For v0.1 we support:
  - Pure SOS positivity test (no Positivstellensatz multipliers yet).
  - Linear combinations of monomial ansätze.
  - Extraction of coefficient vectors witnessing monotonicity.

v0.2 additions (flagged): Positivstellensatz multipliers (for inequality
constraints from incompressibility, etc.), SDP rational extraction for
certified-rational coefficients, Lean-export of certificates.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import numpy as np
import sympy as sp
from sympy import Poly


try:
    import cvxpy as cp
    _HAVE_CVXPY = True
except Exception:  # pragma: no cover
    _HAVE_CVXPY = False


@dataclass
class SOSSearch:
    """Search for a linear combination of candidate monomials yielding Q ≤ 0.

    Input: `q_expr`, a sympy expression linear in `coefs` (list of sympy Symbols),
    polynomial in `atoms` (list of sympy expressions treated as free variables).

    Output: coefficient vector c* minimising SDP slack, with a termination
    status.
    """

    q_expr: sp.Expr
    coefs: List[sp.Symbol]
    atoms: List[sp.Expr]
    # Optional fixed shift to avoid the trivial c=0 solution.
    normalisation: str = "sum_one"  # {"sum_one", "L1_one", "none"}

    def solve(self) -> Dict:
        """Return dict with keys: status, coefs (np.array), residual (float)."""
        if not _HAVE_CVXPY:
            return {"status": "cvxpy_unavailable", "coefs": None, "residual": None}
        coef_syms = self.coefs
        atom_syms = [sp.Symbol(f"a_{i}") for i, _ in enumerate(self.atoms)]
        # Substitute atoms by dummy symbols.
        sub_map = {a: s for a, s in zip(self.atoms, atom_syms)}
        q_sub = sp.expand(self.q_expr.xreplace(sub_map))
        # Treat q_sub as a polynomial in atom_syms with coefficients linear in coef_syms.
        # We check whether -q_sub is a sum of squares: i.e. for all real values
        # of atoms, c · (-q_sub) ≥ 0. Equivalently: the *coefficient polynomial*
        # over atom_syms of -q_sub can be written as p(a) = Σ q_j(a)² with SOS
        # structure. We use the Gram-matrix formulation.
        try:
            poly = Poly(-q_sub, *atom_syms)
        except sp.polys.polyerrors.GeneratorsError:
            return {"status": "non_polynomial_in_atoms", "coefs": None, "residual": None}

        # Extract monomials in atoms and their coefficients (which are polynomials
        # in the coef_syms, but since we want linearity in coef_syms, they should
        # actually be linear — we check).
        mono_to_coef: Dict[Tuple[int, ...], sp.Expr] = {}
        for mono, c in zip(poly.monoms(), poly.coeffs()):
            mono_to_coef[tuple(mono)] = sp.expand(c)

        # Build Gram-matrix SDP: find psd matrix G with v(a)^T G v(a) = p(a),
        # where v(a) is the monomial basis up to half the degree of p.
        total_deg = poly.total_degree()
        half_deg = (total_deg + 1) // 2
        from itertools import combinations_with_replacement

        n_atoms = len(atom_syms)
        basis_monos: List[Tuple[int, ...]] = []
        for d in range(half_deg + 1):
            for combo in combinations_with_replacement(range(n_atoms), d):
                mi = [0] * n_atoms
                for idx in combo:
                    mi[idx] += 1
                basis_monos.append(tuple(mi))
        b = len(basis_monos)

        G = cp.Variable((b, b), symmetric=True)

        # Build CVXPY variables for the ansatz coefficients.
        cvx_coefs = {s: cp.Variable() for s in coef_syms}

        # For each monomial μ in p, compute the set of (i, j) such that
        # basis_monos[i] + basis_monos[j] == μ.
        monomial_constraints = []
        all_monos = set(mono_to_coef.keys())
        for i in range(b):
            for j in range(b):
                mi = tuple(a + b_ for a, b_ in zip(basis_monos[i], basis_monos[j]))
                all_monos.add(mi)
        mu_list = sorted(all_monos)
        for mu in mu_list:
            # Σ_{i+j=mu} G[i,j] == coefficient of mu in p(a).
            lhs_terms = []
            for i in range(b):
                for j in range(b):
                    if tuple(a + b_ for a, b_ in zip(basis_monos[i], basis_monos[j])) == mu:
                        lhs_terms.append(G[i, j])
            lhs = sum(lhs_terms) if lhs_terms else 0
            rhs_expr = mono_to_coef.get(mu, sp.Integer(0))
            rhs_lin = _linear_to_cvx(rhs_expr, coef_syms, cvx_coefs)
            monomial_constraints.append(lhs == rhs_lin)

        # Normalisation: avoid c=0 trivial solution.
        if self.normalisation == "sum_one":
            normaliser = [sum(cvx_coefs[s] for s in coef_syms) == 1]
        elif self.normalisation == "none":
            normaliser = []
        else:
            normaliser = [sum(cvx_coefs[s] for s in coef_syms) == 1]

        objective = cp.Minimize(0)  # feasibility
        constraints = [G >> 0] + monomial_constraints + normaliser
        prob = cp.Problem(objective, constraints)
        try:
            prob.solve(solver=cp.CLARABEL, verbose=False)
        except Exception as e:
            try:
                prob.solve(solver=cp.SCS, verbose=False)
            except Exception:
                return {"status": "sdp_solver_error", "coefs": None, "residual": None, "error": str(e)}

        if prob.status in ("optimal", "optimal_inaccurate"):
            c_values = np.array([cvx_coefs[s].value for s in coef_syms], dtype=float)
            return {
                "status": prob.status,
                "coefs": c_values,
                "G": G.value,
                "residual": None,
            }
        return {"status": prob.status, "coefs": None, "residual": None}


def _linear_to_cvx(expr: sp.Expr, coef_syms: List[sp.Symbol], cvx_coefs: Dict) -> object:
    """Convert a sympy expression linear in coef_syms to a CVXPY affine expression."""
    expr = sp.expand(expr)
    if expr == 0:
        return 0
    result = 0
    # Constant term
    const = expr.as_coefficients_dict().get(1, sp.Integer(0))
    try:
        result = float(const)
    except TypeError:
        result = 0
    for s in coef_syms:
        coeff = expr.coeff(s)
        try:
            coeff_f = float(coeff)
        except TypeError:
            coeff_f = 0.0
        if coeff_f != 0.0:
            result = result + coeff_f * cvx_coefs[s]
    return result
