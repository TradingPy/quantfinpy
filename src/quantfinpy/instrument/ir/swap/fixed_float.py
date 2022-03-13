"""Interface for IR Swaps with 1 fixed rate swap leg and 1 floating rate swap leg."""

from attr import attrs

from quantfinpy.instrument.ir.swap.fixed_leg import IRFixedLeg
from quantfinpy.instrument.ir.swap.floating_leg import IRFloatingLeg
from quantfinpy.instrument.ir.swap.mixin import ReceiverIRFixedLegMixin
from quantfinpy.instrument.portfolio import Position
from quantfinpy.instrument.swap import Swap


@attrs(frozen=True, slots=True, auto_attribs=True, init=False)
class IRFixedFloatSwap(ReceiverIRFixedLegMixin, Swap):
    """Swap with 1 IR fixed leg and 1 IR Floating leg."""

    def __init__(
        self, receiver_fixed_leg: IRFixedLeg, payer_floating_leg: IRFloatingLeg
    ):
        object.__setattr__(
            self,
            "positions",
            (Position(receiver_fixed_leg, 1.0), Position(payer_floating_leg, -1.0)),
        )

    @property
    def payer_floating_leg(self) -> IRFloatingLeg:
        """Get underlying payer floating leg."""
        floating_leg = self.positions[1].instrument
        assert self.positions[1].quantity == -1.0
        assert isinstance(floating_leg, IRFloatingLeg)
        return floating_leg
