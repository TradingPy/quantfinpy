"""Interface for IR Cap/Floors."""

from attrs import define

from quantfinpy.instrument.ir.swap.floating_leg import IRFloatingLeg
from quantfinpy.instrument.option import Option, OptionExerciseType, OptionSide


@define(frozen=True)
class CapFloor(Option[IRFloatingLeg]):
    """Interface for IR Cap/Floor, i.e. option on floating rate note."""

    @classmethod
    def create(
        cls,
        capfloor_side: OptionSide,
        capfloor_rate: float,
        floating_rate_note: IRFloatingLeg,
    ) -> "CapFloor":
        """
        Create capfloor.

        :param capfloor_side:
        :param capfloor_rate:
        :param floating_rate_note:
        :return: created capfloor
        """
        return cls(
            floating_rate_note,
            capfloor_side,
            OptionExerciseType.EUROPEAN,
            capfloor_rate,
            floating_rate_note.maturity,
        )
