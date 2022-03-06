"""Test cases for the different cashflow classes."""

from quantfinpy.enum.currency import Currency
from quantfinpy.data.tenor import Tenor
from quantfinpy.data.ir.curve import InterestRateCurveId, InterestRateIndex
from quantfinpy.data.ir.cashflow.cashflow import FixedRateCashflow, FloatingRateCashflow


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


def test_floating_rate_cashflow_ctor():
    # Building FloatingRateCashflow.
    notional = 1.0
    currency = Currency.USD
    tenor = Tenor(months=3)
    floating_rate_curve_id = InterestRateCurveId(InterestRateIndex.LIBOR, Currency.EUR, Tenor(day=2))
    cashflow = FloatingRateCashflow(notional, currency, tenor, floating_rate_curve_id)

    # Checking built FloatingRateCashflow.
    assert isinstance(cashflow, FloatingRateCashflow)
    assert cashflow.notional == notional
    assert cashflow.currency == currency
    assert cashflow.tenor == tenor
    assert cashflow.floating_ir_curve_id == floating_rate_curve_id
