"""Test cases for IR swaptions."""

import pytest

from quantfinpy.instrument.ir.option.swaption import IRSwaption
from quantfinpy.instrument.ir.swap.fixed_float import IRFixedFloatSwap
from quantfinpy.instrument.option import OptionExerciseType, OptionSide


@pytest.mark.parametrize("option_side", OptionSide)
@pytest.mark.parametrize("exercise", OptionExerciseType)
def test_ir_swaption_ctor(
    default_fixed_float_swap: IRFixedFloatSwap,
    option_side: OptionSide,
    exercise: OptionExerciseType,
):
    # Building IRSwaption as option on ir fixed float swap with a realistic strike and the maturity as today.
    strike_rate: float = 0.01
    option = IRSwaption.create(
        option_side, exercise, default_fixed_float_swap, strike_rate
    )

    # Checking the built swaption.
    assert isinstance(option, IRSwaption)
    assert option.side == option_side
    assert option.strike == strike_rate
    assert option.maturity == default_fixed_float_swap.receiver_fixed_leg.starting_date
    assert option.underlying == default_fixed_float_swap
    assert option.exercise_type == exercise
