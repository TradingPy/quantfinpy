"""Interface for Equity options."""

from attrs import define

from quantfinpy.instrument.equity.share import EquityShare
from quantfinpy.instrument.option import Option


@define(frozen=True)
class EquityOption(Option[EquityShare]):
    """
    Equity option, i.e. option on Equity share.

    Example:
        >>> from datetime import date
        >>> from quantfinpy.instrument.option import OptionExerciseType, OptionSide
        >>> # Building Equity Option as option on equity share for a realistic strike and the maturity
        >>> # as March 1st 2023.
        >>> strike: float = 99.0
        >>> maturity: date = date(2023, 3, 1)
        >>> share = EquityShare("Company")
        >>> option = EquityOption(share, OptionSide.CALL, OptionExerciseType.EUROPEAN, strike, maturity)
        >>> option.side.name
        'CALL'
        >>> option.strike
        99.0
        >>> option.maturity
        datetime.date(2023, 3, 1)
        >>> option.underlying == share
        True
        >>> option.exercise_type.name
        'EUROPEAN'
    """
