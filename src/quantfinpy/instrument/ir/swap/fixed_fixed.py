"""Interface for IR Swaps with 2 fixed rate swap legs."""

from attrs import define

from quantfinpy.instrument.ir.swap.fixed_leg import IRFixedLeg
from quantfinpy.instrument.ir.swap.mixin import ReceiverIRFixedLegMixin
from quantfinpy.instrument.portfolio import Position
from quantfinpy.instrument.swap import Swap


@define(frozen=True)
class IRFixedFixedSwap(ReceiverIRFixedLegMixin, Swap):
    """Swap with 2 IR fixed legs."""

    @classmethod
    def create(
        cls, receiver_fixed_leg: IRFixedLeg, payer_fixed_leg: IRFixedLeg
    ) -> "IRFixedFixedSwap":
        """
        Create ir fixed-fixed swap.

        :param receiver_fixed_leg:
        :param payer_fixed_leg:
        :return: created swap.
        """
        return cls(
            (Position(receiver_fixed_leg, 1.0), Position(payer_fixed_leg, -1.0)),
        )

    @property
    def payer_fixed_leg(self) -> IRFixedLeg:
        """Get underlying payer fixed leg."""
        fixed_leg = self.positions[1].instrument
        assert self.positions[1].quantity == -1.0
        assert isinstance(fixed_leg, IRFixedLeg)
        return fixed_leg
