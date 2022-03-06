"""Test cases for IR bond."""

from datetime import date
from itertools import chain, repeat

import pandas as pd
from cytoolz.itertoolz import last  # pylint: disable=no-name-in-module

from quantfinpy.data.ir.cashflow.cashflow import Cashflow, FixedRateCashflow
from quantfinpy.data.tenor import Tenor
from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.ir.bond import IRBond


def test_ib_bond_ctor():
    # Building IRBond as sequence of coupon cashflows + a cashflow for the repayment at maturity.
    coupon_dates = pd.date_range(start=date.today(), periods=10, freq="3M")
    coupon_cashflow = FixedRateCashflow(1.0, Currency.USD, Tenor(month=3), 0.01)
    maturity = last(coupon_dates)
    repayment_coupon = Cashflow(1.0, Currency.USD)
    ir_bond = IRBond.build_explicit(
        coupon_cashflow, coupon_dates, maturity, repayment_coupon
    )

    # Checking built IR Bond.
    assert isinstance(ir_bond, IRBond)
    assert all(
        map(
            lambda date_pair: object.__eq__(*date_pair),
            zip(
                chain(coupon_dates, repeat(maturity, 1)),
                ir_bond.scheduled_cashflows.dates,
            ),
        )
    )
    assert all(
        map(
            lambda cashflow_pair: object.__eq__(*cashflow_pair),
            zip(
                chain(repeat(coupon_cashflow), repeat(repayment_coupon, 1)),
                ir_bond.scheduled_cashflows.values,
            ),
        )
    )
