"""Cashflow interfaces and definitions."""

from typing import Optional

from attr import attrs
from pandas import DateOffset

from quantfinpy.data.curve.forward import ForwardCurveId
from quantfinpy.enum.currency import Currency


@attrs(frozen=True, slots=True, auto_attribs=True)
class Cashflow:
    """Net balance of cash moving in or out."""

    notional: float
    """Cash notional."""
    currency: Currency
    """Cash's currency."""


@attrs(frozen=True, slots=True, auto_attribs=True)
class ObservedCashflow(Cashflow):
    """Observed cashflow."""


@attrs(frozen=True, slots=True, auto_attribs=True)
class ForwardCashflow(Cashflow):
    """Cashflow projected over a specified tenor."""

    tenor: DateOffset
    """Projection's tenor."""


@attrs(frozen=True, slots=True, auto_attribs=True)
class FixedRateCashflow(ForwardCashflow):
    """Cashflow with a fixed forward rate."""

    rate: float
    """Cash-flow's fixed forward rate."""


@attrs(frozen=True, slots=True, auto_attribs=True)
class FloatingRateCashflow(ForwardCashflow):
    """Cashflow with a floating forward rate."""

    forward_curve_id: ForwardCurveId
    """Cash-flow's floating rate identified by its curve id."""
    spread: Optional[float] = None
    """Spread over the floating forward rate."""
