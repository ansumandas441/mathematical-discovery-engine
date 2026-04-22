"""Systematic discovery sweep.

Scan (PDE × basis × Φ-family) looking for monotone/conserved quantities.
Emit a ledger of findings. Any NEW result (not in the PDE's literature list)
flags for human review.

v0.1 scope: polynomial Φ only. The sweep is honest about what it can reach.
"""

import sys
sys.path.insert(0, "/Users/primetrce/Documents/maths/monoquant")

import time
import sympy as sp

from monoquant import MonotoneSearch, verify_functional
from monoquant.pdes import (
    heat_equation,
    burgers_equation,
    kdv_equation,
    keller_segel_simplified,
    cahn_hilliard,
    camassa_holm,
    nse_2d_vorticity,
    nse_3d_hyperdissipative,
)


PDE_BUILDERS = [
    ("heat_1d", lambda: heat_equation(spatial_dim=1)),
    ("burgers_1d", lambda: burgers_equation(nu=1.0)),
    ("kdv_1d", lambda: kdv_equation()),
    ("ks_simplified", lambda: keller_segel_simplified(chi=1.0)),
    ("cahn_hilliard", lambda: cahn_hilliard(gamma=1.0)),
    ("camassa_holm", lambda: camassa_holm()),
    ("nse_2d_vort", lambda: nse_2d_vorticity(nu=1.0)),
    ("nse_3d_hyperdiss_1.2", lambda: nse_3d_hyperdissipative(alpha=1.2)),
]


def extract_unique_conservation_laws(result) -> list:
    """Strip trivial-divergence conservations: anything of the form u·u_x,
    u_x (which vanish on decay data), or a*divergence."""
    keepers = []
    seen = set()
    for cert in result.conserved:
        Phi = sp.simplify(cert.functional)
        key = str(Phi)
        if key in seen:
            continue
        seen.add(key)
        # Heuristic: if Φ has a clear `x_k`-derivative factor as a WHOLE TERM
        # then it's a divergence (will integrate to 0 on decay). We keep the
        # ones that are "bulk" (not total divergences).
        is_divergence = False
        if isinstance(Phi, sp.Add):
            # multi-term; often conservations are polynomial with mixed terms
            pass
        elif isinstance(Phi, sp.Mul):
            # single monomial
            has_deriv = any(isinstance(f, sp.Derivative) for f in Phi.args)
            has_bare = any(not isinstance(f, sp.Derivative) and not f.is_number for f in Phi.args)
            if has_deriv and has_bare:
                # could be a divergence; keep it (some are non-trivial)
                pass
            elif has_deriv and not has_bare:
                is_divergence = True
        elif isinstance(Phi, sp.Derivative):
            is_divergence = True
        keepers.append((Phi, is_divergence))
    return keepers


def main() -> None:
    print("=" * 70)
    print("  MONOQUANT SYSTEMATIC DISCOVERY SWEEP — v0.1")
    print("=" * 70)
    findings = []
    for name, builder in PDE_BUILDERS:
        pde = builder()
        for deg in [2, 3, 4]:
            for dord in [1, 2]:
                # Skip basis configurations that explode on multi-field PDEs.
                if name.startswith("nse_3d") and (deg > 2 or dord > 1):
                    continue
                if name == "nse_2d_vort" and (deg > 3 or dord > 1):
                    continue
                t0 = time.time()
                try:
                    search = MonotoneSearch(
                        pde=pde, max_poly_degree=deg, max_derivative_order=dord,
                        find_decrease=True, find_conservation=True, verbose=False,
                    )
                    result = search.run()
                    elapsed = time.time() - t0
                except Exception as e:
                    print(f"  [{name} deg≤{deg} d≤{dord}] ERROR: {type(e).__name__}: {e}")
                    continue
                n_cons = len(result.conserved)
                n_mono = len(result.monotone)
                n_cand = result.meta.get("candidates", "?")
                line = f"  [{name:25s} deg≤{deg} d≤{dord}] cand={n_cand:3d}  cons={n_cons:2d}  mono={n_mono}  [{elapsed:.2f}s]"
                print(line)
                findings.append({
                    "pde": name, "deg": deg, "dord": dord,
                    "n_cons": n_cons, "n_mono": n_mono,
                    "conservations": [str(c.functional) for c in result.conserved],
                    "monotones": [str(c.functional) for c in result.monotone],
                })
    print()
    print("=" * 70)
    print("  SUMMARY TABLE")
    print("=" * 70)
    print(f"{'PDE':28s} {'cons_max':>10s} {'mono_max':>10s}")
    pde_best = {}
    for f in findings:
        key = f["pde"]
        if key not in pde_best:
            pde_best[key] = {"cons": 0, "mono": 0, "best_cons_set": []}
        if f["n_cons"] > pde_best[key]["cons"]:
            pde_best[key]["cons"] = f["n_cons"]
            pde_best[key]["best_cons_set"] = f["conservations"]
        if f["n_mono"] > pde_best[key]["mono"]:
            pde_best[key]["mono"] = f["n_mono"]
    for name, d in pde_best.items():
        print(f"{name:28s} {d['cons']:>10d} {d['mono']:>10d}")

    print()
    print("=" * 70)
    print("  NOTABLE CONSERVATIONS (curated subset per PDE)")
    print("=" * 70)
    for name, d in pde_best.items():
        print(f"\n--- {name} ---")
        for phi_str in d["best_cons_set"][:6]:
            print(f"  Φ = {phi_str}")


if __name__ == "__main__":
    main()
