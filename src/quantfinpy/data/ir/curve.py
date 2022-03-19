"""Interfaces for base interest rate curve id and object."""

from attr import attrs
from pandas import DateOffset

from quantfinpy.enum.currency import Currency
from quantfinpy.enum.ir_index import InterestRateIndex


@attrs(slots=True, auto_attribs=True, frozen=True)
class InterestRateCurveId:
    """Identify the different interest rate curve ids."""

    index: InterestRateIndex
    """Curve's index."""
    currency: Currency
    """Curve's currency."""
    tenor: DateOffset
    """Curve's tenor."""
