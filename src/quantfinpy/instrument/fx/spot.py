"""Interface for fx spot instruments."""

from attrs import define

from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.spot import SpotInstrument


@define(frozen=True)
class FXSpot(SpotInstrument):
    """
    Interface for fx spot instruments.

    Example:
        >>> fx_spot = FXSpot(Currency.USD, Currency.EUR)
        >>> fx_spot.domestic_currency.name
        'USD'
        >>> fx_spot.foreign_currency.name
        'EUR'
    """

    domestic_currency: Currency
    """Domestic currency."""
    foreign_currency: Currency
    """Foreign currency."""

    @classmethod
    def validate_value(cls, instrument_value: float) -> None:
        """
        Validate a specific fx spot value, i.e. checking strictly positive.

        :param instrument_value: a fx spot value.
        """
        SpotInstrument.validate_value(instrument_value)
        assert (
            instrument_value > 0.0
        ), f"FX spot is always strictly positive, received {instrument_value}."
