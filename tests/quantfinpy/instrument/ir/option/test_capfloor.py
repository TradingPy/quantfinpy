"""Test cases for IR caps and floors."""

import pytest

from quantfinpy.instrument import CapFloor, IRFloatingLeg
from quantfinpy.instrument.option import OptionExerciseType, OptionSide


@pytest.mark.parametrize("option_side", OptionSide)
def test_ir_capfloor_ctor(default_floating_leg: IRFloatingLeg, option_side: OptionSide):
    # Building Capfloor as option on floating rate note (IRFloatingLeg) with a realistic capfloor rate.
    capfloor_rate: float = 0.01
    option = CapFloor.create(option_side, capfloor_rate, default_floating_leg)

    # Checking the built capfloor.
    assert isinstance(option, CapFloor)
    assert option.side == option_side
    assert option.strike == capfloor_rate
    assert option.maturity == default_floating_leg.maturity
    assert option.underlying == default_floating_leg
    # european in the way that each caplet/floorlet are european options.
    assert option.exercise_type == OptionExerciseType.EUROPEAN
