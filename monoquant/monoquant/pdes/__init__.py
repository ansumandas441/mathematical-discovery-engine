from monoquant.pdes.heat import heat_equation
from monoquant.pdes.burgers import burgers_equation
from monoquant.pdes.nse_2d_vorticity import nse_2d_vorticity
from monoquant.pdes.nse_3d import nse_3d_velocity
from monoquant.pdes.dyadic import dyadic_shell
from monoquant.pdes.nse_3d_hyperdissipative import (
    nse_3d_hyperdissipative,
    nse_3d_multiscale,
)

__all__ = [
    "heat_equation",
    "burgers_equation",
    "nse_2d_vorticity",
    "nse_3d_velocity",
    "dyadic_shell",
    "nse_3d_hyperdissipative",
    "nse_3d_multiscale",
]
