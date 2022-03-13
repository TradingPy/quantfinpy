"""Mixin classes for IR swaps."""


from quantfinpy.instrument.ir.swap.fixed_leg import IRFixedLeg


class ReceiverIRFixedLegMixin:
    """Mixin class for IR swaps with a receiving IR fixed leg."""

    __slots__ = ()

    def __init_subclass__(cls) -> None:
        if not hasattr(cls, "positions"):
            raise Exception(f"class {cls.__name__} is missing 'positions' attribute.")

    @property
    def receiver_fixed_leg(self) -> IRFixedLeg:
        """Get underlying receiver fixed leg."""
        fixed_leg = self.positions[0].instrument  # type: ignore
        assert self.positions[0].quantity == 1.0  # type: ignore
        assert isinstance(fixed_leg, IRFixedLeg)
        return fixed_leg
