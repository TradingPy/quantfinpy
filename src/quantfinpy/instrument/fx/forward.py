"""Interface for fx forward instruments."""

from attr import attrs

from quantfinpy.instrument.forward import Forward
from quantfinpy.instrument.fx.spot import FXSpot


@attrs(slots=True, frozen=True, auto_attribs=True)
class FXForward(Forward[FXSpot]):
    """Interface for fx forward instruments."""
