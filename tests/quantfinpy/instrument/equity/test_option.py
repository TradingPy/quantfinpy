"""Test cases for the interfaces of the different equity options."""

from datetime import date

import pytest

from quantfinpy.instrument.equity.option import EquityOption
from quantfinpy.instrument.equity.share import EquityShare
from quantfinpy.instrument.option import OptionExerciseType, OptionSide


@pytest.mark.parametrize("option_side", OptionSide)
@pytest.mark.parametrize("exercise", OptionExerciseType)
def test_equity_option_ctor(
    default_share: EquityShare, option_side: OptionSide, exercise: OptionExerciseType
):
    # Building Equity Option as option on equity share for a realistic strike and the maturity as today.
    strike: float = 99.0
    maturity: date = date.today()
    option = EquityOption(default_share, option_side, exercise, strike, maturity)

    # Checking the built equity option.
    assert isinstance(option, EquityOption)
    assert option.side == option_side
    assert option.strike == strike
    assert option.maturity == maturity
    assert option.underlying == default_share
    assert option.exercise_type == exercise
