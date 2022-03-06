"""Cashflow interfaces and definitions."""

from attr import attrs

from quantfinpy.enum.currency import Currency
from quantfinpy.data.tenor import Tenor
from quantfinpy.data.ir.curve import InterestRateCurveId


@attrs(frozen=True, slots=True, auto_attribs=True)
class Cashflow:
    """Net balance of cash moving in or out."""

    notional: float
    """Cash notional."""
    currency: Currency
    """Cash's currency."""


@attrs(frozen=True, slots=True, auto_attribs=True)
class ProjectedCashflow(Cashflow):
    """Cashflow projected according to a specified tenor."""

    tenor: Tenor
    """Projection's tenor."""


@attrs(frozen=True, slots=True, auto_attribs=True)
class FixedRateCashflow(ProjectedCashflow):
    """Cashflow with a fixed interest rate."""

    rate: float
    """Cash-flow's fixed rate."""


@attrs(frozen=True, slots=True, auto_attribs=True)
class FloatingRateCashflow(ProjectedCashflow):
    """Cashflow with a floating interest rate."""

    floating_ir_curve_id: InterestRateCurveId
    """Cash-flow's floating rate identified by its curve id."""