"""Interface for forward instruments."""

from datetime import date
from typing import Generic

from attr import attrs

from quantfinpy.instrument.derivative import Derivative, UnderlyingType


@attrs(slots=True, frozen=True, auto_attribs=True)
class Forward(Derivative[UnderlyingType], Generic[UnderlyingType]):
    """Interface for forward instruments."""

    strike: float
    """pre-agreed price for buying or selling the underlying at maturity."""
    maturity: date
    """end of life of the forward."""

    def __attrs_post_init__(self) -> None:
        super().__attrs_post_init__()
        try:
            self.underlying.validate_value(self.strike)
        except AssertionError as err:
            raise ValueError(
                f"Provided strike {self.strike} is not valid for underlying of type {type(self.underlying)}"
            ) from err
