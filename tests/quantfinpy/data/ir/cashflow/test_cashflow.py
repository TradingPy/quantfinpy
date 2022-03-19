"""Test cases for the different ir cashflow classes."""

from pandas import DateOffset

from quantfinpy.data.ir.cashflow import FloatingRateCashflow
from quantfinpy.data.ir.curve import InterestRateCurveId, InterestRateIndex
from quantfinpy.enum.currency import Currency


def test_floating_rate_cashflow_ctor():
    # Building FloatingRateCashflow.
    notional = 1.0
    currency = Currency.USD
    tenor = DateOffset(months=3)
    floating_rate_curve_id = InterestRateCurveId(
        InterestRateIndex.LIBOR, Currency.EUR, DateOffset(day=2)
    )
    cashflow = FloatingRateCashflow(notional, currency, tenor, floating_rate_curve_id)

    # Checking built FloatingRateCashflow.
    assert isinstance(cashflow, FloatingRateCashflow)
    assert cashflow.notional == notional
    assert cashflow.currency == currency
    assert cashflow.tenor == tenor
    assert cashflow.floating_ir_curve_id == floating_rate_curve_id
