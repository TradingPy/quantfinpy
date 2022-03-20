"""Interface for Equity options."""

from attr import attrs

from quantfinpy.instrument.equity.share import EquityShare
from quantfinpy.instrument.option import Option


@attrs(slots=True, frozen=True, auto_attribs=True)
class EquityOption(Option[EquityShare]):
    """Equity option, i.e. option on Equity share."""
