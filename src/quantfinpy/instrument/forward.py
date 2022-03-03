"""Interface for forward instruments."""

from datetime import date
from attr import attrs


from quantfinpy.instrument.instrument import Instrument


@attrs(slots=True, frozen=True, auto_attribs=True)
class Forward(Instrument):
    """Interface for forward instruments."""

    underlying: Instrument
    strike: float
    maturity: date
