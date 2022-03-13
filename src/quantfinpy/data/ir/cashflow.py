"""IR Cashflow interfaces and definitions."""

from attr import attrs

from quantfinpy.data.cashflow.cashflow import ProjectedCashflow
from quantfinpy.data.ir.curve import InterestRateCurveId


@attrs(frozen=True, slots=True, auto_attribs=True)
class FloatingRateCashflow(ProjectedCashflow):
    """Cashflow with a floating interest rate."""

    floating_ir_curve_id: InterestRateCurveId
    """Cash-flow's floating rate identified by its curve id."""
