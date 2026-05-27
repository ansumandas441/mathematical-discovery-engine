# MonoQuant

**Mechanized Monotone-Quantity Search for Evolution PDEs**

MonoQuant searches for monotone (or conserved) functionals of a PDE's state —
the kind of quantity that Perelman's W-entropy is for Ricci flow, that enstrophy
is for 2D Navier–Stokes, that energy is for the heat equation. It does this
automatically:

1. Enumerate polynomial functionals Φ[u] invariant under the PDE's symmetry group
   (scaling, translation, rotation), up to bounded degree and derivative order.
2. Compute dΦ/dt along the PDE symbolically, using the chain rule, integration
   by parts, and any pointwise constraints (incompressibility, etc.).
3. Call a sum-of-squares / Positivstellensatz SDP solver to either
   - certify dΦ/dt ≤ 0 (monotone decay) or dΦ/dt ≡ 0 (conservation), or
   - return an infeasibility certificate proving no such Φ exists at the
     current (degree, scaling, weight) configuration.

## What it's for

B3 in the iter-4 Navier–Stokes portfolio. The near-term target is the
"Perelman-analogue for 3D NSE" question. The long-term target is any evolution
PDE where monotone quantities drive regularity theory — Ricci flow, mean
curvature flow, compressible Euler, Schrödinger, KdV, dispersive PDEs.

## What's in v0.1

- `monoquant.pde` — symbolic PDE class with right-hand-side and symmetries.
- `monoquant.invariants` — polynomial invariant basis enumeration.
- `monoquant.symbolic` — dΦ/dt engine with integration-by-parts.
- `monoquant.sos` — SDP Positivstellensatz interface (via CVXPY).
- `monoquant.certificate` — monotonicity / infeasibility certificate objects.

PDE instances included:
- Heat equation (recovers L² energy decay as sanity check).
- 1D Burgers (recovers L² energy decay; known shock singularity).
- Katz–Pavlović dyadic shell model (known blowup at α < 5/4).
- 2D Navier–Stokes, vorticity formulation (recovers enstrophy and energy).
- 3D Navier–Stokes, velocity formulation (the target — search at degrees 2–4).

## Quick start

```bash
source monoquant_venv/bin/activate
python examples/demo_heat.py           # recovers ∫ u² dx decay
python examples/demo_2d_nse.py         # recovers ∫ ω² dx conservation
python examples/demo_3d_nse.py         # search — reports findings
```

## What v0.2 will add

- SO(3) × scaling × translation invariants at higher degree (currently O(4))
- Leray-projection-aware IBP (needed for pressure-velocity coupling in 3D NSE)
- Export of SDP certificates to Lean 4 proof obligations
- Additional PDEs: Ricci flow, Schrödinger, KdV, compressible Euler

## Layout

```
monoquant/
├── monoquant/
│   ├── pde.py            # PDE base class
│   ├── invariants.py     # Symmetry-invariant polynomial enumeration
│   ├── symbolic.py       # d/dt with IBP
│   ├── sos.py            # SDP SOS interface
│   ├── certificate.py    # Result types
│   └── pdes/             # PDE instances
│       ├── heat.py
│       ├── burgers.py
│       ├── dyadic.py
│       ├── nse_2d.py
│       └── nse_3d.py
├── examples/
│   ├── demo_heat.py
│   ├── demo_burgers.py
│   ├── demo_dyadic.py
│   ├── demo_2d_nse.py
│   └── demo_3d_nse.py
└── tests/
```

## Provenance

Born of iter-4 (NSE session) as new-technique-node B3. The iter-4 portfolio
documented zero breakthroughs on Clay Navier–Stokes but flagged the need for
exactly this piece of infrastructure: a way to search the space of candidate
monotone quantities automatically rather than by human taste.
