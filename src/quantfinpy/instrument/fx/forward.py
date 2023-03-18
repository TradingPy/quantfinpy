"""Interface for fx forward instruments."""

from attrs import define

from quantfinpy.instrument.forward import Forward
from quantfinpy.instrument.fx.spot import FXSpot


@define(frozen=True)
class FXForward(Forward[FXSpot]):
    """Interface for fx forward instruments."""
