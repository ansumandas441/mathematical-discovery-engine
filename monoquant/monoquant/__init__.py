"""MonoQuant — mechanized search for monotone quantities of evolution PDEs."""

__version__ = "0.1.0"

from monoquant.pde import PDE, ScalarField, VectorField
from monoquant.symbolic import TimeDerivativeEngine
from monoquant.invariants import PolynomialInvariantBasis, ScalingWeightBasis
from monoquant.sos import SOSSearch
from monoquant.search import MonotoneSearch, HierarchyConservationSearch, verify_functional
from monoquant.certificate import (
    MonotonicityCertificate,
    ConservationCertificate,
    InfeasibilityCertificate,
    SearchResult,
)

__all__ = [
    "PDE",
    "ScalarField",
    "VectorField",
    "TimeDerivativeEngine",
    "PolynomialInvariantBasis",
    "ScalingWeightBasis",
    "SOSSearch",
    "MonotoneSearch",
    "HierarchyConservationSearch",
    "verify_functional",
    "MonotonicityCertificate",
    "ConservationCertificate",
    "InfeasibilityCertificate",
    "SearchResult",
]
