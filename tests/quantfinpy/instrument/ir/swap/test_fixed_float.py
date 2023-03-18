"""Test cases for FixedFloat IR Swap."""

from quantfinpy.instrument import IRFixedFloatSwap, IRFixedLeg, IRFloatingLeg


def test_ir_fixed_float_swap_ctor(
    default_fixed_leg: IRFixedLeg, default_floating_leg: IRFloatingLeg
):
    # Creating an ir fixed float swap around a fixed swap leg and a floating swap leg.
    ir_fixed_float_swap = IRFixedFloatSwap.create(
        default_fixed_leg, default_floating_leg
    )

    # Checking built swap.
    assert isinstance(ir_fixed_float_swap, IRFixedFloatSwap)
    assert ir_fixed_float_swap.receiver_fixed_leg == default_fixed_leg
    assert ir_fixed_float_swap.payer_floating_leg == default_floating_leg
    assert list(
        map(lambda leg_position: leg_position.quantity, ir_fixed_float_swap.swap_legs)
    ) == [1.0, -1.0]
