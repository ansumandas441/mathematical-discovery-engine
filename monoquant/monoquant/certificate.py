"""Result objects emitted by the search engine."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

import sympy as sp


@dataclass
class MonotonicityCertificate:
    """Φ is monotone: dΦ/dt ≤ 0."""

    functional: sp.Expr
    pde_name: str
    sign: str  # "decrease" or "conserved" or "increase"
    sos_certificate: Optional[Dict] = None
    notes: str = ""

    def __repr__(self) -> str:
        return (
            f"MonotonicityCertificate(pde={self.pde_name!r}, sign={self.sign!r}, "
            f"Φ={self.functional})"
        )


@dataclass
class ConservationCertificate:
    """Φ is conserved: dΦ/dt ≡ 0."""

    functional: sp.Expr
    pde_name: str
    identity_reduction: sp.Expr  # the expression that reduced to 0
    notes: str = ""

    def __repr__(self) -> str:
        return (
            f"ConservationCertificate(pde={self.pde_name!r}, Φ={self.functional})"
        )


@dataclass
class InfeasibilityCertificate:
    """No Φ in the given basis satisfies the monotonicity target."""

    pde_name: str
    basis_description: str
    target: str  # e.g. "dΦ/dt <= 0 supercritical scaling"
    sdp_status: str  # solver's termination status
    notes: str = ""

    def __repr__(self) -> str:
        return (
            f"InfeasibilityCertificate(pde={self.pde_name!r}, "
            f"basis={self.basis_description}, status={self.sdp_status!r})"
        )


@dataclass
class SearchResult:
    """Bundle of outcomes from one search run."""

    monotone: List[MonotonicityCertificate] = field(default_factory=list)
    conserved: List[ConservationCertificate] = field(default_factory=list)
    infeasibilities: List[InfeasibilityCertificate] = field(default_factory=list)
    meta: Dict = field(default_factory=dict)

    def pretty_print(self) -> str:
        lines = []
        lines.append(f"=== SearchResult: {self.meta.get('pde', '?')} ===")
        lines.append(f"Basis: {self.meta.get('basis', '?')}")
        lines.append(f"Candidates enumerated: {self.meta.get('candidates', '?')}")
        if self.monotone:
            lines.append(f"\nMonotone (dΦ/dt ≤ 0): {len(self.monotone)}")
            for c in self.monotone:
                lines.append(f"  Φ = {sp.simplify(c.functional)}   [{c.sign}]")
        if self.conserved:
            lines.append(f"\nConserved (dΦ/dt ≡ 0): {len(self.conserved)}")
            for c in self.conserved:
                lines.append(f"  Φ = {sp.simplify(c.functional)}")
        if self.infeasibilities:
            lines.append(f"\nInfeasibilities: {len(self.infeasibilities)}")
            for c in self.infeasibilities:
                lines.append(f"  target={c.target}  status={c.sdp_status}")
        if not (self.monotone or self.conserved or self.infeasibilities):
            lines.append("\n(no outputs)")
        return "\n".join(lines)
