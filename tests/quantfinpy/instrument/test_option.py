"""Test cases for option's interface."""

from datetime import date
import pytest

from quantfinpy.instrument.option import Option, OptionSide, OptionExerciseType
from quantfinpy.instrument.fx.spot import FXSpot
from quantfinpy.enum.currency import Currency


@pytest.mark.parametrize("option_side", OptionSide)
@pytest.mark.parametrize("exercise_type", OptionExerciseType)
def test_option_ctor(option_side: OptionSide, exercise_type: OptionExerciseType):
    fx_spot = FXSpot(Currency.USD, Currency.EUR)
    strike: float = 1.0
    maturity: date = date.today()
    fx_option = Option(option_side, exercise_type, fx_spot, 1.0, maturity)
    assert isinstance(fx_option, Option)
    assert fx_option.side == option_side
    assert fx_option.exercise_type == exercise_type
    assert fx_option.underlying == fx_spot
    assert fx_option.strike == strike
    assert fx_option.maturity == maturity
