"""Interfaces for equity shares."""

from attr import attrs

from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.instrument import Instrument


@attrs(frozen=True, slots=True, auto_attribs=True)
class EquityShare(Instrument):
    """Equity share."""

    company: str
    """company name."""
    currency: Currency
    """share's currency."""
