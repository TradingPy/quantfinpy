"""Test cases for the basic cashflow classes."""

from pandas import DateOffset

from quantfinpy.data.cashflow.cashflow import FixedRateCashflow, FloatingRateCashflow
from quantfinpy.data.ir.curve import IRForwardCurveId
from quantfinpy.enum.currency import Currency


def test_fixed_rate_cashflow_ctor():
    # Building FixedRateCashflow.
    notional = 1.0
    currency = Currency.USD
    tenor = DateOffset(months=3)
    fixed_rate = 0.01
    cashflow = FixedRateCashflow(notional, currency, tenor, fixed_rate)

    # Checking built FixedRateCashflow.
    assert isinstance(cashflow, FixedRateCashflow)
    assert cashflow.notional == notional
    assert cashflow.currency == currency
    assert cashflow.tenor == tenor
    assert cashflow.rate == fixed_rate


def test_floating_rate_cashflow_ctor(default_ir_fwd_curve_id: IRForwardCurveId):
    # Building FloatingRateCashflow.
    notional = 1.0
    currency = Currency.USD
    tenor = DateOffset(months=3)
    cashflow = FloatingRateCashflow(notional, currency, tenor, default_ir_fwd_curve_id)

    # Checking built FloatingRateCashflow.
    assert isinstance(cashflow, FloatingRateCashflow)
    assert cashflow.notional == notional
    assert cashflow.currency == currency
    assert cashflow.tenor == tenor
    assert cashflow.forward_curve_id == default_ir_fwd_curve_id
