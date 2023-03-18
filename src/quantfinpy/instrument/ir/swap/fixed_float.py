"""Interface for IR Swaps with 1 fixed rate swap leg and 1 floating rate swap leg."""

from attrs import define

from quantfinpy.instrument.ir.swap.fixed_leg import IRFixedLeg
from quantfinpy.instrument.ir.swap.floating_leg import IRFloatingLeg
from quantfinpy.instrument.ir.swap.mixin import ReceiverIRFixedLegMixin
from quantfinpy.instrument.portfolio import Position
from quantfinpy.instrument.swap import Swap


@define(frozen=True)
class IRFixedFloatSwap(ReceiverIRFixedLegMixin, Swap):
    """Swap with 1 IR fixed leg and 1 IR Floating leg."""

    @classmethod
    def create(
        cls, receiver_fixed_leg: IRFixedLeg, payer_floating_leg: IRFloatingLeg
    ) -> "IRFixedFloatSwap":
        return cls(
            (Position(receiver_fixed_leg, 1.0), Position(payer_floating_leg, -1.0)),
        )

    @property
    def payer_floating_leg(self) -> IRFloatingLeg:
        """Get underlying payer floating leg."""
        floating_leg = self.positions[1].instrument
        assert self.positions[1].quantity == -1.0
        assert isinstance(floating_leg, IRFloatingLeg)
        return floating_leg
