"""Pytest fixtures for credit instrument testing."""

from datetime import date

import pandas as pd
import pytest
from pandas import DateOffset

from quantfinpy.data.cashflow.cashflow import Cashflow, FixedRateCashflow
from quantfinpy.data.cashflow.schedule import CashflowSchedule
from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.credit.bond import Bond


@pytest.fixture(scope="module")
def default_reference_entity() -> str:
    return "Company"


@pytest.fixture(scope="module")
def default_coupon_tenor() -> DateOffset:
    return DateOffset(months=3)


@pytest.fixture(scope="module")
def default_coupon_dates() -> pd.DatetimeIndex:
    return pd.date_range(start=date.today(), periods=10, freq="3M")


@pytest.fixture(scope="module")
def default_fixed_coupon(
    default_currency: Currency, default_coupon_tenor: DateOffset
) -> FixedRateCashflow:
    return FixedRateCashflow(1.0, default_currency, default_coupon_tenor, 0.01)


@pytest.fixture(scope="module")
def default_fixed_coupon_schedule(
    default_coupon_dates: pd.DatetimeIndex, default_fixed_coupon: FixedRateCashflow
) -> CashflowSchedule:
    return CashflowSchedule.build_from_single_value_definition(
        default_coupon_dates, default_fixed_coupon
    )


@pytest.fixture(scope="module")
def default_repayment_cashflow(default_currency: Currency) -> Cashflow:
    return Cashflow(1.0, default_currency)


@pytest.fixture(scope="module")
def default_bond(
    default_reference_entity: str,
    default_repayment_cashflow: Cashflow,
    default_fixed_coupon_schedule: CashflowSchedule,
) -> Bond:
    return Bond.create(
        default_reference_entity,
        default_repayment_cashflow.notional,
        default_repayment_cashflow.currency,
        default_fixed_coupon_schedule,
    )
