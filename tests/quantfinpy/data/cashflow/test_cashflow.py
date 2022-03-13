"""Test cases for the basic cashflow classes."""

from quantfinpy.data.cashflow.cashflow import FixedRateCashflow
from quantfinpy.data.tenor import Tenor
from quantfinpy.enum.currency import Currency


def test_fixed_rate_cashflow_ctor():
    # Building FixedRateCashflow.
    notional = 1.0
    currency = Currency.USD
    tenor = Tenor(months=3)
    fixed_rate = 0.01
    cashflow = FixedRateCashflow(notional, currency, tenor, fixed_rate)

    # Checking built FixedRateCashflow.
    assert isinstance(cashflow, FixedRateCashflow)
    assert cashflow.notional == notional
    assert cashflow.currency == currency
    assert cashflow.tenor == tenor
    assert cashflow.rate == fixed_rate
