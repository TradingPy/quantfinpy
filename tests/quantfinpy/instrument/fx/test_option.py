"""Test cases for FX options."""

from datetime import date

import pytest

from quantfinpy.instrument.fx.option import FXOption
from quantfinpy.instrument.fx.spot import FXSpot
from quantfinpy.instrument.option import OptionExerciseType, OptionSide


@pytest.mark.parametrize("option_side", OptionSide)
@pytest.mark.parametrize("exercise", OptionExerciseType)
def test_option_ctor(
    default_fx_spot: FXSpot, option_side: OptionSide, exercise: OptionExerciseType
):
    # Building Equity Option as option on equity share for a realistic strike and the maturity as today.
    strike: float = 1.10
    maturity: date = date.today()
    option = FXOption(default_fx_spot, option_side, exercise, strike, maturity)

    # Checking the built equity option.
    assert isinstance(option, FXOption)
    assert option.side == option_side
    assert option.strike == strike
    assert option.maturity == maturity
    assert option.underlying == default_fx_spot
    assert option.exercise_type == exercise
