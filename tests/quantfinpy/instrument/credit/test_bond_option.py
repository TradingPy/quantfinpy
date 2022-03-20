"""Test cases for Bond option's interface."""

from datetime import date

import pytest

from quantfinpy.instrument.credit.bond import Bond
from quantfinpy.instrument.credit.bond_option import BondOption
from quantfinpy.instrument.option import OptionExerciseType, OptionSide


@pytest.mark.parametrize("option_side", OptionSide)
@pytest.mark.parametrize("exercise", OptionExerciseType)
def test_bond_option_ctor(
    default_bond: Bond, option_side: OptionSide, exercise: OptionExerciseType
):
    # Building Bond Option as option on default bond for a realistic strike and the maturity at the start of the bond.
    strike: float = 99.0
    maturity: date = next(default_bond.coupon_cashflows.dates)
    option = BondOption(default_bond, option_side, exercise, strike, maturity)

    # Checking the built bond option.
    assert isinstance(option, BondOption)
    assert option.side == option_side
    assert option.strike == strike
    assert option.maturity == maturity
    assert option.underlying == default_bond
    assert option.exercise_type == exercise
