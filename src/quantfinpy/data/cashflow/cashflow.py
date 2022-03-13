"""Cashflow interfaces and definitions."""

from attr import attrs

from quantfinpy.data.tenor import Tenor
from quantfinpy.enum.currency import Currency


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
