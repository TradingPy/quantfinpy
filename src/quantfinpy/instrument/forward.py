"""Interface for forward instruments."""

from datetime import date

from attr import attrs

from quantfinpy.instrument.instrument import Instrument


@attrs(slots=True, frozen=True, auto_attribs=True)
class Forward(Instrument):
    """Interface for forward instruments."""

    underlying: Instrument
    """instrument to be bought or sold at maturity."""
    strike: float
    """pre-agreed price for buying or selling the underlying at maturity."""
    maturity: date
    """end of life of the forward."""

    def __attrs_post_init__(self) -> None:
        try:
            self.underlying.validate_value(self.strike)
        except AssertionError as err:
            raise ValueError(
                f"Provided strike {self.strike} is not valid for underlying of type {type(self.underlying)}"
            ) from err
