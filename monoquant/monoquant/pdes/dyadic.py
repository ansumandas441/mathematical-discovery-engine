"""Katz-Pavlović dyadic shell model.

∂_t a_n = λ^{2n} a_n (hyperdissipation if any) + λ^n a_{n-1}² − λ^{n+1} a_n a_{n+1}

For v0.1 we expose only a small-n window (n=0..N) as a finite ODE system.
"""

from __future__ import annotations

import sympy as sp

from monoquant.pde import PDE, ScalarField


def dyadic_shell(N: int = 4, alpha: float = 1.0, lam: float = 2.0) -> PDE:
    """Katz-Pavlović dyadic shells a_0, ..., a_N.

    We embed in a 1D PDE framework by treating each a_n as an independent
    ScalarField (no spatial dependence is meaningful; shell models are ODE
    systems). The spatial_dim is formally 1 but the PDE is interpreted
    pointwise (no IBP performed).
    """
    fields = [ScalarField(f"a{n}", spatial_dim=1) for n in range(N + 1)]
    # Share time / coord symbols across shells.
    t = fields[0].t
    x = fields[0].coords[0]
    for f in fields[1:]:
        f.t = t
        f.coords = (x,)
        f.symbol = sp.Function(f.name)(t, x)
    rhs_substitutions = {}
    for n in range(N + 1):
        a_n = fields[n].symbol
        a_nm1 = fields[n - 1].symbol if n > 0 else sp.Integer(0)
        a_np1 = fields[n + 1].symbol if n < N else sp.Integer(0)
        rhs = lam ** n * a_nm1 ** 2 - lam ** (n + 1) * a_n * a_np1
        if alpha > 0:
            rhs = rhs - lam ** (2 * alpha * n) * a_n  # hyperdissipative term
        rhs_substitutions[sp.diff(a_n, t)] = rhs
    return PDE(
        name=f"dyadic_shell_N{N}_alpha{alpha}",
        fields=fields,
        rhs_substitutions=rhs_substitutions,
        constraints=[],
        scaling={f.name: 0.0 for f in fields},
        notes=(
            "Katz-Pavlović shell model. ∑ a_n² is conserved without dissipation; "
            "blows up at α < 5/4 per Cheskidov."
        ),
    )
