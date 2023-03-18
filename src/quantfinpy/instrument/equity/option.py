"""Interface for Equity options."""

from attrs import define

from quantfinpy.instrument.equity.share import EquityShare
from quantfinpy.instrument.option import Option


@define(frozen=True)
class EquityOption(Option[EquityShare]):
    """Equity option, i.e. option on Equity share."""
