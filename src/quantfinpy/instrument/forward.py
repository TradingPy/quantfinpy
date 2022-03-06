"""Interface for forward instruments."""

from datetime import date

from attr import attrs

from quantfinpy.instrument.instrument import Instrument


@attrs(slots=True, frozen=True, auto_attribs=True)
class Forward(Instrument):
    """Interface for forward instruments."""

    underlying: Instrument
    """instrument to be bought or sold at maturity."""
    strike: float
    """pre-agreed price for buying or selling the underlying at maturity."""
    maturity: date
    """end of life of the forward."""
