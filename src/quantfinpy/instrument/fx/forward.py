"""Interface for fx forward instruments."""

from attrs import define

from quantfinpy.instrument.forward import Forward
from quantfinpy.instrument.fx.spot import FXSpot


@define(frozen=True)
class FXForward(Forward[FXSpot]):
    """
    Interface for fx forward instruments.

    Example:
        >>> from datetime import date
        >>> from quantfinpy.enum.currency import Currency
        >>> # Creating a fx forward as a forward on fx spot.
        >>> strike: float = 1.0
        >>> maturity: date = date(2023, 1, 1)
        >>> fx_spot = FXSpot(Currency.USD, Currency.EUR)
        >>> fx_fwd = FXForward(fx_spot, strike, maturity)
        >>> fx_fwd.underlying
        FXSpot(domestic_currency=<Currency.USD: 1>, foreign_currency=<Currency.EUR: 2>)
        >>> fx_fwd.strike
        1.0
        >>> fx_fwd.maturity
        datetime.date(2023, 1, 1)
    """
