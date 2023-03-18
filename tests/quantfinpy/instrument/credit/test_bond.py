"""Test cases for bond."""

from datetime import date

import pandas as pd
from pandas import DateOffset

from quantfinpy.data.cashflow.cashflow import FixedRateCashflow, ObservedCashflow
from quantfinpy.data.cashflow.schedule import CashflowSchedule
from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.credit.bond import Bond


def test_bond_ctor():
    # Building Bond as sequence of coupon cashflows + a cashflow for the repayment at maturity.
    reference_entity: str = "Company"
    coupon_dates = pd.date_range(start=date.today(), periods=10, freq="3M")
    coupon_tenor = DateOffset(months=3)
    coupon_cashflow = FixedRateCashflow(1.0, Currency.USD, coupon_tenor, 0.01)
    coupon_cashflows = CashflowSchedule.build_from_single_value_definition(
        coupon_dates, coupon_cashflow
    )
    maturity = coupon_dates[-1] + coupon_tenor
    repayment_coupon = ObservedCashflow(1.0, Currency.USD)
    bond = Bond.create(
        reference_entity,
        repayment_coupon.notional,
        repayment_coupon.currency,
        coupon_cashflows,
    )

    # Checking built Bond.
    assert isinstance(bond, Bond)
    assert bond.coupon_cashflows == coupon_cashflows
    assert bond.maturity == maturity
    assert bond.repayment_cashflow == repayment_coupon
    assert bond.reference_entity == reference_entity
