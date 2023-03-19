"""Interface for FX options."""

from attrs import define

from quantfinpy.instrument.fx.spot import FXSpot
from quantfinpy.instrument.option import Option


@define(frozen=True)
class FXOption(Option[FXSpot]):
    """
    FX option, i.e. option on FXSpot.

    Example:
        >>> from datetime import date
        >>> from quantfinpy.enum.currency import Currency
        >>> from quantfinpy.instrument.option import OptionExerciseType, OptionSide
        >>> # Building Equity Option as option on equity share for a realistic strike and the maturity as today.
        >>> strike: float = 1.10
        >>> maturity: date = date(2023, 1, 1)
        >>> fx_spot = FXSpot(Currency.USD, Currency.EUR)
        >>> option = FXOption(fx_spot, OptionSide.CALL, OptionExerciseType.EUROPEAN, strike, maturity)
        >>> option.side.name
        'CALL'
        >>> option.strike
        1.1
        >>> option.maturity
        datetime.date(2023, 1, 1)
        >>> option.underlying
        FXSpot(domestic_currency=<Currency.USD: 1>, foreign_currency=<Currency.EUR: 2>)
        >>> option.exercise_type.name
        'EUROPEAN'
    """
