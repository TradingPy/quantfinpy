"""Interface for IR swaptions, i.e. option on fixed float ir swaps."""

from attrs import define

from quantfinpy.instrument.ir.swap.fixed_float import IRFixedFloatSwap
from quantfinpy.instrument.option import Option, OptionExerciseType, OptionSide


@define(frozen=True)
class IRSwaption(Option[IRFixedFloatSwap]):
    """Option on IR FixedFloat swap."""

    @classmethod
    def create(
        cls,
        option_side: OptionSide,
        option_exercise: OptionExerciseType,
        swap: IRFixedFloatSwap,
        strike_rate: float,
    ) -> "IRSwaption":
        return cls(
            swap,
            option_side,
            option_exercise,
            strike_rate,
            swap.receiver_fixed_leg.starting_date,
        )
