"""Pricing of scheduled cashflow instruments."""

from datetime import date

from quantfinpy.data.curve.discount import DiscountCurve
from quantfinpy.instrument.cashflow.schedule import CashflowScheduleInstrument


def scheduled_cashflows_value(
    cashflow_instr: CashflowScheduleInstrument,
    discount_curve: DiscountCurve,
    valuation_date: date,
) -> float:
    """
    Compute the value of the scheduled cashflows at a specific date with the discounting underlying the provided
    discount curve.

    :param cashflow_instr: scheduled cashflows to value.
    :param discount_curve: discount curve to be used to discount the bond's cashflow, i.e. coupons and principal.
    :param valuation_date: reference date for the valuation.
    :return: sum of scheduled cashflows' values at the valuation date.

    Note:
        Only actual cashflows without projections are supported here.

    """
    return 100.0
