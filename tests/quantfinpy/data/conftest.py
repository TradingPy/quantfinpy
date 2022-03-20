"""Pytest fixtures for data testing."""

import pytest
from pandas import DateOffset

from quantfinpy.data.cashflow.cashflow import FixedRateCashflow
from quantfinpy.data.ir.curve import IRForwardCurveId
from quantfinpy.enum.currency import Currency
from quantfinpy.enum.ir_index import InterestRateIndex


@pytest.fixture(scope="module")
def default_currency() -> Currency:
    return Currency.USD


@pytest.fixture(scope="module")
def default_ir_index() -> InterestRateIndex:
    return InterestRateIndex.LIBOR


@pytest.fixture(scope="module")
def default_tenor() -> DateOffset:
    return DateOffset(months=3)


@pytest.fixture(scope="module")
def default_fixed_cashflow(
    default_currency: Currency, default_tenor: DateOffset
) -> FixedRateCashflow:
    return FixedRateCashflow(1.0, default_currency, default_tenor, 0.01)


@pytest.fixture(scope="module")
def default_ir_fwd_curve_id(
    default_currency: Currency,
    default_ir_index: InterestRateIndex,
    default_tenor: DateOffset,
) -> IRForwardCurveId:
    return IRForwardCurveId(default_currency, default_ir_index, default_tenor)
