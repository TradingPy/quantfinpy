"""Bond pricing."""

from datetime import date

from quantfinpy.data.curve.discount import DiscountCurve
from quantfinpy.instrument.cashflow.schedule import CashflowScheduleInstrument
from quantfinpy.instrument.credit.bond import Bond
from quantfinpy.pricing.cashflow.schedule import scheduled_cashflows_value


def bond_value(
    bond: Bond, discount_curve: DiscountCurve, valuation_date: date
) -> float:
    """
    Compute the value of the bond at a specific date.

    :param bond: bond to value.
    :param discount_curve: discount curve to be used to discount the bond's cashflow, i.e. coupons and principal.
    :param valuation_date: reference date for the valuation.
    :return: bond's value at the valuation date.

    Note:
        Only actual coupons without projections are supported here.

    """
    coupon_value = scheduled_cashflows_value(
        CashflowScheduleInstrument(bond.coupon_cashflows),
        discount_curve,
        valuation_date,
    )
    principal_value = (
        discount_curve.discount_factor(valuation_date, bond.maturity) * bond.notional
    )

    return coupon_value + principal_value
