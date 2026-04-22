"""High-level search orchestrator (v0.1.2).

Pipeline:
  1. Enumerate polynomial functional basis Φ = Σ c_i m_i(u, ∂u, ...).
  2. Compute pointwise ∂_t Φ using the PDE RHS.
  3. CONSERVATION phase: apply Euler–Lagrange operator E_u to ∂_t Φ. Require
     E_u(∂_t Φ) ≡ 0 as a polynomial identity in the field-derivative atoms.
     Solve the resulting linear system in the coefficients c_i; each solution
     is a conservation law.
  4. MONOTONICITY phase: apply one-pass IBP (pushing highest-order derivatives
     off) to produce a canonical sign-testable integrand Q(c; atoms). Call SDP
     SOS solver for c with −Q a sum of squares. Report monotone Φ or
     infeasibility.

The split is important: conservation is a LINEAR exact condition (E_u ≡ 0);
monotonicity is a semidefinite sign condition on an IBP'd canonical form.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Set

import numpy as np
import sympy as sp

from monoquant.pde import PDE, ScalarField, VectorField
from monoquant.invariants import PolynomialInvariantBasis, Monomial
from monoquant.symbolic import TimeDerivativeEngine
from monoquant.sos import SOSSearch
from monoquant.certificate import (
    ConservationCertificate,
    InfeasibilityCertificate,
    MonotonicityCertificate,
    SearchResult,
)


def verify_functional(pde: PDE, phi: sp.Expr, verbose: bool = True) -> Dict:
    """Given a SPECIFIC Φ, compute dΦ/dt, apply IBP + kernel-filter, and
    classify as CONSERVED / DECREASE / INCREASE / SIGN-UNCERTAIN.

    This is the "no-search" mode: just verify a candidate. Fast and works for
    large PDEs where full enumeration is infeasible (like 3D NSE).
    """
    from monoquant.symbolic import TimeDerivativeEngine, _flat_fields
    engine = TimeDerivativeEngine(pde)
    if verbose:
        print(f"[verify] Φ = {phi}")
        print(f"[verify] computing pointwise ∂_t Φ along {pde.name} ...", flush=True)
    dphi = engine.dphi_dt_pointwise(phi)
    # Check conservation via Euler–Lagrange.
    fields = _flat_fields(pde)
    is_conserved = True
    el_residues = []
    for f in fields:
        E = sp.expand(engine.euler_lagrange(dphi, f))
        el_residues.append(E)
        if E != 0:
            is_conserved = False
    if is_conserved:
        if verbose:
            print(f"[verify] ✓ CONSERVED: dΦ/dt ≡ 0 (mod total divergence).")
        return {"status": "CONSERVED", "dphi_dt_pointwise": dphi}
    # IBP reduce & kernel-filter.
    Q = engine.integrate_by_parts(dphi, passes=2)
    # Apply PDE constraints (e.g. divergence-free for NSE).
    Q = pde.impose_constraints(Q)
    # Iterate IBP + constraints once more to clean up any exposed total derivatives.
    Q = engine.integrate_by_parts(Q, passes=2)
    Q = pde.impose_constraints(Q)
    # Apply the fractional-Laplacian IBP rule: u_i · FracLap(u_i, α) → FracLap(u_i, α/2)²
    from monoquant.fractional import apply_fractional_ibp, fractional_laplacian_sign_test
    Q = apply_fractional_ibp(Q)
    # Drop pointwise total-derivatives.
    Q_filtered = _kernel_filter_static(Q, pde, engine)
    if verbose:
        print(f"[verify] Q (after IBP + kernel-filter) = {sp.simplify(Q_filtered)}")
    # Try SDP sign test (no free coefs — coefs are {}).
    atoms = engine._collect_atoms(Q_filtered)
    if not atoms:
        if verbose:
            print(f"[verify] ✓ CONSERVED (Q reduces to 0 after IBP + kernel-filter).")
        return {"status": "CONSERVED", "dphi_dt_pointwise": dphi}
    # Fractional-Laplacian-aware sign test: recognises FracLap(u, β)² ≥ 0 and
    # drops transport-like cross-terms that integrate to zero under div-free.
    frac_sign = fractional_laplacian_sign_test(Q_filtered, pde=pde)
    if frac_sign != "MIXED":
        if verbose:
            print(f"[verify] fractional-Laplacian sign: {frac_sign}")
        return {
            "status": f"CERTIFIED-{frac_sign}",
            "dphi_dt_pointwise": dphi,
            "dphi_dt_reduced": Q_filtered,
        }
    # Heuristic sign: test that -Q ≥ 0 for random atom assignments.
    sign = _heuristic_sign_test(Q_filtered, atoms)
    if verbose:
        print(f"[verify] heuristic sign of Q: {sign}")
    return {
        "status": f"PROBABLE-{sign}",
        "dphi_dt_pointwise": dphi,
        "dphi_dt_reduced": Q_filtered,
        "euler_lagrange_residues": el_residues,
    }


def _kernel_filter_static(Q: sp.Expr, pde: PDE, engine) -> sp.Expr:
    """Same as MonotoneSearch._kernel_filter but callable statically."""
    from monoquant.symbolic import _flat_fields
    Q = sp.expand(Q)
    atoms = engine._collect_atoms(Q)
    if not atoms:
        return Q
    dummy_of = {a: sp.Symbol(f"__kf{i}") for i, a in enumerate(atoms)}
    back_of = {d: a for a, d in dummy_of.items()}
    Q_dummy = Q.xreplace(dummy_of)
    try:
        poly = sp.Poly(Q_dummy, *dummy_of.values())
    except sp.polys.polyerrors.GeneratorsError:
        return Q
    fields = _flat_fields(pde)
    kept = sp.Integer(0)
    for mono, coef_expr in zip(poly.monoms(), poly.coeffs()):
        M = sp.Integer(1)
        for exponent, dummy in zip(mono, dummy_of.values()):
            if exponent:
                atom = back_of[dummy]
                M = M * atom ** exponent
        all_zero = True
        for f in fields:
            E = engine.euler_lagrange(M, f)
            if sp.simplify(E) != 0:
                all_zero = False
                break
        if all_zero:
            continue
        kept = kept + sp.expand(coef_expr) * M
    return sp.expand(kept)


def _heuristic_sign_test(Q: sp.Expr, atoms: List[sp.Expr], n_samples: int = 50) -> str:
    """Sample random values for atoms and check the sign of Q.

    Returns DECREASE if Q ≤ 0 on all samples, INCREASE if ≥ 0, MIXED otherwise.
    This is a probabilistic sign test (not a proof), useful when the basis
    for a formal SDP is too large.
    """
    import random
    saw_pos = False
    saw_neg = False
    dummy_of = {a: sp.Symbol(f"__s{i}") for i, a in enumerate(atoms)}
    Q_dummy = Q.xreplace(dummy_of)
    syms = list(dummy_of.values())
    for _ in range(n_samples):
        vals = {s: random.uniform(-2.0, 2.0) for s in syms}
        try:
            v = float(Q_dummy.xreplace(vals))
        except Exception:
            continue
        if v > 1e-10:
            saw_pos = True
        elif v < -1e-10:
            saw_neg = True
        if saw_pos and saw_neg:
            return "MIXED"
    if saw_pos and not saw_neg:
        return "INCREASE"
    if saw_neg and not saw_pos:
        return "DECREASE"
    return "ZERO"


@dataclass
class MonotoneSearch:
    pde: PDE
    max_poly_degree: int = 2
    max_derivative_order: int = 1
    find_decrease: bool = True
    find_conservation: bool = True
    verbose: bool = True
    tolerance: float = 1e-7

    def run(self) -> SearchResult:
        result = SearchResult()
        basis = PolynomialInvariantBasis(
            pde=self.pde,
            max_poly_degree=self.max_poly_degree,
            max_derivative_order=self.max_derivative_order,
        )
        monomials = basis.enumerate()
        result.meta = {
            "pde": self.pde.name,
            "basis": (
                f"poly_deg≤{self.max_poly_degree}, "
                f"deriv_order≤{self.max_derivative_order}"
            ),
            "candidates": len(monomials),
        }
        self._log(f"[{self.pde.name}] enumerated {len(monomials)} basis monomials.")

        engine = TimeDerivativeEngine(self.pde)
        coefs = [m.coefficient_symbol for m in monomials]
        phi_pointwise = sum(
            m.coefficient_symbol * m.as_expr(self.pde) for m in monomials
        )
        self._log(f"[{self.pde.name}] computing ∂_t Φ pointwise ...")
        dphi = engine.dphi_dt_pointwise(phi_pointwise)

        if self.find_conservation:
            result.conserved.extend(
                self._conservation_phase(dphi, coefs, monomials, engine)
            )

        if self.find_decrease:
            result.monotone, infeas = self._monotonicity_phase(
                dphi, coefs, monomials, engine, result.conserved
            )
            result.infeasibilities.extend(infeas)

        return result

    # ---------- conservation via Euler–Lagrange ----------

    def _conservation_phase(
        self,
        dphi: sp.Expr,
        coefs: List[sp.Symbol],
        monomials: List[Monomial],
        engine: TimeDerivativeEngine,
    ) -> List[ConservationCertificate]:
        self._log(f"[{self.pde.name}] conservation phase: applying E_u ...")
        fields = _flat_fields(self.pde)
        # Build combined EL conditions across all fields.
        linear_eqs: List[sp.Expr] = []
        for f in fields:
            E = engine.euler_lagrange(dphi, f)
            E = sp.expand(E)
            atoms = engine._collect_atoms(E)
            if not atoms:
                continue
            dummy_of = {a: sp.Symbol(f"__a{i}") for i, a in enumerate(atoms)}
            E_dummy = E.xreplace(dummy_of)
            try:
                poly = sp.Poly(E_dummy, *dummy_of.values())
            except sp.polys.polyerrors.GeneratorsError:
                continue
            for coef_expr in poly.coeffs():
                linear_eqs.append(sp.expand(coef_expr))
        if not linear_eqs:
            # Every Φ in basis is conserved (trivially).
            certs = []
            for m in monomials:
                certs.append(
                    ConservationCertificate(
                        functional=m.as_expr(self.pde),
                        pde_name=self.pde.name,
                        identity_reduction=sp.Integer(0),
                        notes="No EL residue — each basis monomial conserved.",
                    )
                )
            return certs
        # Reduce redundant equations and solve in coefs.
        linear_eqs = _dedupe(linear_eqs)
        self._log(
            f"[{self.pde.name}] conservation phase: "
            f"{len(linear_eqs)} EL residue equations in {len(coefs)} coefs."
        )
        sol = sp.solve(linear_eqs, coefs, dict=True)
        if not sol:
            return []
        sol = sol[0]
        constrained = set(sol.keys())
        free = [c for c in coefs if c not in constrained]
        certs: List[ConservationCertificate] = []
        seen: Set[str] = set()
        for free_c in free:
            sub = {c: sol.get(c, c) for c in coefs}
            for other in free:
                if other == free_c:
                    continue
                for c in coefs:
                    if hasattr(sub[c], "subs"):
                        sub[c] = sub[c].subs(other, 0)
            for c in coefs:
                if hasattr(sub[c], "subs"):
                    sub[c] = sub[c].subs(free_c, 1)
            phi_expr = sum(
                sub[m.coefficient_symbol] * m.as_expr(self.pde) for m in monomials
            )
            phi_expr = sp.simplify(phi_expr)
            if phi_expr == 0:
                continue
            key = str(phi_expr)
            if key in seen:
                continue
            seen.add(key)
            certs.append(
                ConservationCertificate(
                    functional=phi_expr,
                    pde_name=self.pde.name,
                    identity_reduction=sp.Integer(0),
                    notes="E_u(∂_t Φ) ≡ 0 in the jet variables.",
                )
            )
        return certs

    # ---------- monotonicity via IBP + SOS ----------

    def _monotonicity_phase(
        self,
        dphi: sp.Expr,
        coefs: List[sp.Symbol],
        monomials: List[Monomial],
        engine: TimeDerivativeEngine,
        conservation_certs: List[ConservationCertificate],
    ) -> (List[MonotonicityCertificate], List[InfeasibilityCertificate]):
        self._log(f"[{self.pde.name}] monotonicity phase: IBP + kernel-filter + SDP-SOS ...")
        Q = engine.integrate_by_parts(dphi, passes=2)
        # Kernel-filter: any atom-monomial M with E_u(M) = 0 (all fields) is a
        # pointwise total-divergence and contributes nothing to ∫Q dx. Drop it.
        Q = self._kernel_filter(Q, engine)
        atoms = engine._collect_atoms(Q)
        if not atoms:
            return [], []
        search = SOSSearch(q_expr=Q, coefs=coefs, atoms=atoms)
        sdp_result = search.solve()
        monos: List[MonotonicityCertificate] = []
        infeas: List[InfeasibilityCertificate] = []
        status = sdp_result.get("status", "unknown")
        c_vals = sdp_result.get("coefs")
        if c_vals is not None and status in ("optimal", "optimal_inaccurate"):
            # Project out conservation-law directions from c_vals so the
            # reported Φ is minimal mod total-derivatives.
            c_proj = _project_out_conservation(
                c_vals, monomials, conservation_certs, self.pde
            )
            # Round tiny numerical noise to zero.
            c_proj = _threshold(c_proj, tol=1e-4)
            phi_repr = sum(
                float(c_proj[i]) * monomials[i].as_expr(self.pde)
                for i in range(len(monomials))
            )
            phi_repr = sp.nsimplify(phi_repr, rational=True, tolerance=1e-3)
            if phi_repr != 0:
                monos.append(
                    MonotonicityCertificate(
                        functional=phi_repr,
                        pde_name=self.pde.name,
                        sign="decrease",
                        sos_certificate={"coefs": [float(x) for x in c_proj]},
                        notes="SDP-SOS (projected orthogonal to conservation laws).",
                    )
                )
        else:
            infeas.append(
                InfeasibilityCertificate(
                    pde_name=self.pde.name,
                    basis_description=(
                        f"poly_deg≤{self.max_poly_degree}, "
                        f"deriv_order≤{self.max_derivative_order}"
                    ),
                    target="dΦ/dt ≤ 0 (after one-pass IBP, SOS on atoms)",
                    sdp_status=str(status),
                )
            )
        return monos, infeas

    # ---------- utilities ----------

    def _kernel_filter(self, Q: sp.Expr, engine: TimeDerivativeEngine) -> sp.Expr:
        """Drop any atom-monomial whose E_u vanishes on every field.

        Such monomials are pointwise total-divergences and cannot contribute
        to the sign of ∫Q dx. Removing them sharpens the SDP search.
        """
        Q = sp.expand(Q)
        atoms = engine._collect_atoms(Q)
        if not atoms:
            return Q
        dummy_of = {a: sp.Symbol(f"__k{i}") for i, a in enumerate(atoms)}
        back_of = {d: a for a, d in dummy_of.items()}
        Q_dummy = Q.xreplace(dummy_of)
        try:
            poly = sp.Poly(Q_dummy, *dummy_of.values())
        except sp.polys.polyerrors.GeneratorsError:
            return Q
        fields = _flat_fields(self.pde)
        kept = sp.Integer(0)
        for mono, coef_expr in zip(poly.monoms(), poly.coeffs()):
            # Reconstruct the atom-monomial.
            M = sp.Integer(1)
            for exponent, dummy in zip(mono, dummy_of.values()):
                if exponent:
                    atom = back_of[dummy]
                    M = M * atom ** exponent
            # Test: is E_u(M) = 0 for every field?
            all_zero = True
            for f in fields:
                E = engine.euler_lagrange(M, f)
                if sp.simplify(E) != 0:
                    all_zero = False
                    break
            if all_zero:
                continue  # drop it
            kept = kept + sp.expand(coef_expr) * M
        return sp.expand(kept)

    def _log(self, msg: str) -> None:
        if self.verbose:
            print(msg, flush=True)


def _flat_fields(pde: PDE) -> List[ScalarField]:
    flat: List[ScalarField] = []
    for f in pde.fields:
        if isinstance(f, VectorField):
            flat.extend(f.components)
        else:
            flat.append(f)
    return flat


def _project_out_conservation(
    c_vals: np.ndarray,
    monomials: List[Monomial],
    conservation_certs: List[ConservationCertificate],
    pde: PDE,
) -> np.ndarray:
    """Project c_vals orthogonal (in basis coords) to each conservation vector.

    For each conservation cert with functional C = Σ a_i m_i, compute the
    coefficient vector a in the basis and subtract its component from c_vals.
    """
    if not conservation_certs:
        return np.asarray(c_vals, dtype=float).copy()
    cons_vectors: List[np.ndarray] = []
    for cert in conservation_certs:
        v = _basis_projection(cert.functional, monomials, pde)
        if v is None:
            continue
        cons_vectors.append(v)
    c = np.asarray(c_vals, dtype=float).copy()
    for v in cons_vectors:
        norm_sq = float(v @ v)
        if norm_sq < 1e-14:
            continue
        c = c - (c @ v) / norm_sq * v
    return c


def _basis_projection(
    func_expr: sp.Expr, monomials: List[Monomial], pde: PDE
) -> Optional[np.ndarray]:
    """Return a float-vector v with func_expr = Σ v_i · monomial_i (if expressible)."""
    if not monomials:
        return None
    from monoquant.symbolic import _collect_field_derivatives
    mono_exprs = [m.as_expr(pde) for m in monomials]
    all_atoms: Set[sp.Expr] = set()
    for me in mono_exprs + [func_expr]:
        for a in _collect_field_derivatives(me, pde):
            all_atoms.add(a)
    all_atoms_sorted = sorted(all_atoms, key=lambda e: str(e))
    if not all_atoms_sorted:
        return None
    dummy_of = {a: sp.Symbol(f"__bp{i}") for i, a in enumerate(all_atoms_sorted)}
    mono_dummy = [sp.expand(me.xreplace(dummy_of)) for me in mono_exprs]
    func_dummy = sp.expand(func_expr.xreplace(dummy_of))
    try:
        polys = [sp.Poly(md, *dummy_of.values()) for md in mono_dummy]
        target_poly = sp.Poly(func_dummy, *dummy_of.values())
    except sp.polys.polyerrors.GeneratorsError:
        return None
    all_signatures: Set[tuple] = set()
    for p in polys + [target_poly]:
        all_signatures.update(p.monoms())
    sig_list = sorted(all_signatures)
    A = np.zeros((len(sig_list), len(monomials)), dtype=float)
    b = np.zeros(len(sig_list), dtype=float)
    for j, p in enumerate(polys):
        d = dict(zip(p.monoms(), p.coeffs()))
        for i, sig in enumerate(sig_list):
            v = d.get(sig, sp.Integer(0))
            try:
                A[i, j] = float(v)
            except (TypeError, ValueError):
                return None
    d = dict(zip(target_poly.monoms(), target_poly.coeffs()))
    for i, sig in enumerate(sig_list):
        v = d.get(sig, sp.Integer(0))
        try:
            b[i] = float(v)
        except (TypeError, ValueError):
            return None
    try:
        sol, *_ = np.linalg.lstsq(A, b, rcond=None)
    except np.linalg.LinAlgError:
        return None
    return sol


def _threshold(v: np.ndarray, tol: float = 1e-4) -> np.ndarray:
    out = v.copy()
    out[np.abs(out) < tol] = 0.0
    return out


def _dedupe(exprs: List[sp.Expr]) -> List[sp.Expr]:
    seen: Set[str] = set()
    out: List[sp.Expr] = []
    for e in exprs:
        e = sp.expand(e)
        if e == 0:
            continue
        key = str(e)
        if key in seen:
            continue
        seen.add(key)
        out.append(e)
    return out
