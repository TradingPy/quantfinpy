"""Test cases for the pricing of bonds."""
import math
from datetime import date
from math import exp
from typing import Dict, Tuple

import pandas as pd
from attr import attrs

# To import forward_values definition for Bond
# TODO: Find a way to register and dispatch without having unclear imports.
import quantfinpy.pricing.credit.bond  # noqa: F401
from quantfinpy.data.cashflow.cashflow import ObservedCashflow
from quantfinpy.data.cashflow.schedule import CashflowSchedule
from quantfinpy.data.curve.discount import DiscountCurve, DiscountCurveId
from quantfinpy.data.data import DataSet
from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.credit.bond import Bond
from quantfinpy.pricing.discount import discount_value


@attrs(slots=True, frozen=True, auto_attribs=True)
class ZeroRateDiscountCurve(DiscountCurve):
    zero_rates: Dict[Tuple[date, date], float]

    def discount_factor(self, start_date: date, end_date: date) -> float:
        return exp(
            -self.zero_rates[(start_date, end_date)]
            * (end_date - start_date)
            / pd.Timedelta(365, "D")
        )


def test_bond_present_value():
    reference_entity: str = "Company"
    valuation_date: pd.Timestamp = pd.Timestamp("2020-01-01")
    coupon_dates = pd.date_range(start="2020-07-01", periods=4, freq="6MS")
    coupon_cashflow = ObservedCashflow(3.0, Currency.USD)
    coupon_cashflows = CashflowSchedule.build_from_single_value_definition(
        coupon_dates, coupon_cashflow
    )
    repayment_coupon = ObservedCashflow(100.0, Currency.USD)
    bond = Bond.create(
        reference_entity,
        repayment_coupon.notional,
        repayment_coupon.currency,
        coupon_cashflows,
    )
    discount_curve_id = DiscountCurveId(Currency.USD)
    discount_curve = ZeroRateDiscountCurve(
        {
            (valuation_date, coupon_dates[0]): 0.05,
            (valuation_date, coupon_dates[1]): 0.058,
            (valuation_date, coupon_dates[2]): 0.064,
            (valuation_date, coupon_dates[3]): 0.068,
        }
    )

    computed_present_value = discount_value(
        bond,
        DataSet({discount_curve_id: discount_curve}),
        valuation_date,
        discount_curve_id,
    )
    assert math.isclose(computed_present_value, 98.368, rel_tol=1e-5)
