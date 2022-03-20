"""Interface for FX options."""

from attr import attrs

from quantfinpy.instrument.fx.spot import FXSpot
from quantfinpy.instrument.option import Option


@attrs(slots=True, frozen=True, auto_attribs=True)
class FXOption(Option[FXSpot]):
    """FX option, i.e. option on FXSpot."""
