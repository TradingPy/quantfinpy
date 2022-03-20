"""Interface for IR Cap/Floors."""

from attr import attrs

from quantfinpy.instrument.ir.swap.floating_leg import IRFloatingLeg
from quantfinpy.instrument.option import Option, OptionExerciseType, OptionSide


@attrs(frozen=True, slots=True, auto_attribs=True, init=False)
class CapFloor(Option[IRFloatingLeg]):
    """Interface for IR Cap/Floor, i.e. option on floating rate note."""

    def __init__(
        self,
        capfloor_side: OptionSide,
        capfloor_rate: float,
        floating_rate_note: IRFloatingLeg,
    ):
        super().__init__(
            floating_rate_note,
            capfloor_side,
            OptionExerciseType.EUROPEAN,
            capfloor_rate,
            floating_rate_note.maturity,
        )
