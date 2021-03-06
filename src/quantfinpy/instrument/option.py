"""Interface for options."""

from datetime import date
from enum import Enum, auto
from typing import Generic

from attr import attrs

from quantfinpy.instrument.derivative import Derivative, UnderlyingType


class OptionSide(Enum):
    """Enumerate the potential sides of options."""

    CALL = auto()
    """Long side, i.e. buying the underlying at maturity."""
    PUT = auto()
    """Short side, i.e. selling the underlying at maturity."""


class OptionExerciseType(Enum):
    """Enumerate the different exercise types for options."""

    EUROPEAN = auto()
    """Exercise at maturity."""
    AMERICAN = auto()
    """Exercise at any time up to maturity."""


@attrs(slots=True, frozen=True, auto_attribs=True)
class Option(Derivative[UnderlyingType], Generic[UnderlyingType]):
    """Interface for options."""

    side: OptionSide
    """option's side, i.e. call for long and put for short."""
    exercise_type: OptionExerciseType
    """kind of exercise like european or american."""
    strike: float
    """price at which the underlying may be bought or sold."""
    maturity: date
    """end of life of the option."""

    def __attrs_post_init__(self) -> None:
        super().__attrs_post_init__()
        try:
            self.underlying.validate_value(self.strike)
        except AssertionError as err:
            raise ValueError(
                f"Provided strike {self.strike} is not valid for underlying of type {type(self.underlying)}"
            ) from err
