"""Interface for options."""

from datetime import date
from enum import Enum, auto
from typing import Generic

from attrs import Attribute, define, field

from quantfinpy.instrument.derivative import Derivative, Underlying


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


@define(frozen=True)
class Option(Derivative[Underlying], Generic[Underlying]):
    """Interface for options."""

    side: OptionSide
    """option's side, i.e. call for long and put for short."""
    exercise_type: OptionExerciseType
    """kind of exercise like european or american."""
    strike: float = field()
    """price at which the underlying may be bought or sold."""
    maturity: date
    """end of life of the option."""

    @strike.validator
    def check_strike(self, attribute: Attribute, value: float) -> None:  # type: ignore
        try:
            self.underlying.validate_value(value)
        except AssertionError as err:
            raise ValueError(
                f"Provided option's strike {value} is not valid for underlying of type {type(self.underlying)}"
            ) from err
