"""Interface for IR Swaps with 1 fixed rate swap leg and 1 floating rate swap leg."""

from attr import attrs

from quantfinpy.instrument.portfolio import Position
from quantfinpy.instrument.swap import Swap
from quantfinpy.instrument.ir.swap.fixed_leg import IRFixedLeg
from quantfinpy.instrument.ir.swap.floating_leg import IRFloatingLeg


@attrs(frozen=True, slots=True, auto_attribs=True, init=False)
class IRFixedFloatSwap(Swap):
    """Swap with 1 IR fixed leg and 1 IR Floating leg."""

    def __init__(self, fixed_leg: IRFixedLeg, floating_leg: IRFloatingLeg):
        object.__setattr__(
            self, "positions", (Position(fixed_leg, 1.0), Position(floating_leg, -1.0))
        )

    @property
    def fixed_leg(self) -> IRFixedLeg:
        """Get underlying fixed leg."""
        fixed_leg = self.positions[0].instrument
        assert isinstance(fixed_leg, IRFixedLeg)
        return fixed_leg

    @property
    def floating_leg(self) -> IRFloatingLeg:
        """Get underlying floating leg."""
        floating_leg = self.positions[1].instrument
        assert isinstance(floating_leg, IRFloatingLeg)
        return floating_leg
