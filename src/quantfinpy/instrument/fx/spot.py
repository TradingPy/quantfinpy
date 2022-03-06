"""Interface for fx spot instruments."""

from attr import attrs

from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.spot import SpotInstrument


@attrs(slots=True, frozen=True, auto_attribs=True)
class FXSpot(SpotInstrument):
    """Interface for fx spot instruments."""

    domestic_currency: Currency
    """Domestic currency."""
    foreign_currency: Currency
    """Foreign currency."""
