"""Interface for IR Swaps with 2 fixed rate swap legs."""

from attr import attrs

from quantfinpy.instrument.ir.swap.fixed_leg import IRFixedLeg
from quantfinpy.instrument.ir.swap.mixin import ReceiverIRFixedLegMixin
from quantfinpy.instrument.portfolio import Position
from quantfinpy.instrument.swap import Swap


@attrs(frozen=True, slots=True, auto_attribs=True, init=False)
class IRFixedFixedSwap(ReceiverIRFixedLegMixin, Swap):
    """Swap with 2 IR fixed legs."""

    def __init__(self, receiver_fixed_leg: IRFixedLeg, payer_fixed_leg: IRFixedLeg):
        object.__setattr__(
            self,
            "positions",
            (Position(receiver_fixed_leg, 1.0), Position(payer_fixed_leg, -1.0)),
        )

    @property
    def payer_fixed_leg(self) -> IRFixedLeg:
        """Get underlying payer fixed leg."""
        fixed_leg = self.positions[1].instrument
        assert self.positions[1].quantity == -1.0
        assert isinstance(fixed_leg, IRFixedLeg)
        return fixed_leg
