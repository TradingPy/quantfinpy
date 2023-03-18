"""Interface for forward instruments."""

from datetime import date
from typing import Generic

from attrs import Attribute, define, field

from quantfinpy.instrument.derivative import Derivative, Underlying


@define(frozen=True)
class Forward(Derivative[Underlying], Generic[Underlying]):
    """Interface for forward instruments."""

    strike: float = field()
    """pre-agreed price for buying or selling the underlying at maturity."""
    maturity: date
    """end of life of the forward."""

    @strike.validator
    def check_strike(self, attribute: Attribute, value: float) -> None:  # type: ignore
        try:
            self.underlying.validate_value(value)
        except AssertionError as err:
            raise ValueError(
                f"Provided forward's strike {value} is not valid for underlying of type {type(self.underlying)}"
            ) from err
