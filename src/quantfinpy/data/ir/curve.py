"""Interfaces for base interest rate curve id and object."""

from attr import attrs
from pandas import DateOffset

from quantfinpy.data.curve.discount import DiscountCurveId
from quantfinpy.data.curve.forward import ForwardCurveId
from quantfinpy.enum.ir_index import InterestRateIndex


@attrs(slots=True, auto_attribs=True, frozen=True)
class IRForwardCurveId(ForwardCurveId):
    """Identify the different interest rate forward curve ids."""

    index: InterestRateIndex
    """Curve's index."""
    tenor: DateOffset
    """Curve's tenor."""


@attrs(slots=True, auto_attribs=True, frozen=True)
class IRDiscountCurveId(DiscountCurveId):
    """Identify the different interest rate discount curve ids."""

    forward_curve_id: IRForwardCurveId
    """Curve's forward curve id."""
