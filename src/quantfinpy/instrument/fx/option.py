"""Interface for FX options."""

from attrs import define

from quantfinpy.instrument.fx.spot import FXSpot
from quantfinpy.instrument.option import Option


@define(frozen=True)
class FXOption(Option[FXSpot]):
    """FX option, i.e. option on FXSpot."""
