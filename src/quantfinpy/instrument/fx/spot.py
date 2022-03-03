"""Interface for fx spot instruments."""

from attr import attrs


from quantfinpy.instrument.spot import SpotInstrument
from quantfinpy.enum.currency import Currency


@attrs(slots=True, frozen=True, auto_attribs=True)
class FXSpot(SpotInstrument):
    """Interface for fx spot instruments."""

    domestic_currency: Currency
    foreign_currency: Currency
