"""Interface for IR swaptions, i.e. option on fixed float ir swaps."""

from attr import attrs

from quantfinpy.instrument.ir.swap.fixed_float import IRFixedFloatSwap
from quantfinpy.instrument.option import Option, OptionExerciseType, OptionSide


@attrs(slots=True, frozen=True, auto_attribs=True, init=False)
class IRSwaption(Option):
    """Option on IR FixedFloat swap."""

    def __init__(
        self,
        option_side: OptionSide,
        option_exercise: OptionExerciseType,
        swap: IRFixedFloatSwap,
        strike_rate: float,
    ):
        super().__init__(
            option_side,
            option_exercise,
            swap,
            strike_rate,
            swap.receiver_fixed_leg.starting_date,
        )
