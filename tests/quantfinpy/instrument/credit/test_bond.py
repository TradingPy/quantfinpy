"""Test cases for bond."""

from datetime import date

import pandas as pd
from cytoolz.itertoolz import last  # pylint: disable=no-name-in-module

from quantfinpy.data.cashflow.cashflow import Cashflow, FixedRateCashflow
from quantfinpy.data.cashflow.schedule import CashflowSchedule
from quantfinpy.data.tenor import Tenor
from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.credit.bond import Bond


def test_bond_ctor():
    # Building Bond as sequence of coupon cashflows + a cashflow for the repayment at maturity.
    reference_entity: str = "Company"
    coupon_dates = pd.date_range(start=date.today(), periods=10, freq="3M")
    coupon_cashflow = FixedRateCashflow(1.0, Currency.USD, Tenor(month=3), 0.01)
    coupon_cashflows = CashflowSchedule.build_from_single_value_definition(
        coupon_dates, coupon_cashflow
    )
    maturity = last(coupon_dates)
    repayment_coupon = Cashflow(1.0, Currency.USD)
    bond = Bond(
        reference_entity,
        maturity,
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
