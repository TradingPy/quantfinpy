"""Pytest fixtures for IR instrument testing."""

from datetime import date

import pandas as pd
import pytest
from pandas import DateOffset

from quantfinpy.data.cashflow.cashflow import FixedRateCashflow
from quantfinpy.data.cashflow.schedule import CashflowSchedule
from quantfinpy.data.ir.cashflow import FloatingRateCashflow
from quantfinpy.data.ir.curve import InterestRateCurveId, InterestRateIndex
from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.ir.swap.fixed_float import IRFixedFloatSwap
from quantfinpy.instrument.ir.swap.fixed_leg import IRFixedLeg
from quantfinpy.instrument.ir.swap.floating_leg import IRFloatingLeg


@pytest.fixture(scope="module")
def default_cashflow_dates() -> pd.DatetimeIndex:
    return pd.date_range(start=date.today(), periods=10, freq="3M")


@pytest.fixture(scope="module")
def default_projected_cashflow_tenor() -> DateOffset:
    return DateOffset(months=3)


@pytest.fixture(scope="module")
def default_ir_curve_index() -> InterestRateIndex:
    return InterestRateIndex.LIBOR


@pytest.fixture(scope="module")
def default_ir_curve_id(
    default_currency: Currency,
    default_projected_cashflow_tenor: DateOffset,
    default_ir_curve_index: InterestRateIndex,
) -> InterestRateCurveId:
    return InterestRateCurveId(
        default_ir_curve_index, default_currency, default_projected_cashflow_tenor
    )


@pytest.fixture(scope="module")
def default_fixed_cashflow(
    default_currency: Currency, default_projected_cashflow_tenor: DateOffset
) -> FixedRateCashflow:
    return FixedRateCashflow(
        1.0, default_currency, default_projected_cashflow_tenor, 0.01
    )


@pytest.fixture(scope="module")
def default_floating_cashflow(
    default_currency: Currency,
    default_projected_cashflow_tenor: DateOffset,
    default_ir_curve_id: InterestRateCurveId,
) -> FloatingRateCashflow:
    return FloatingRateCashflow(
        1.0, default_currency, default_projected_cashflow_tenor, default_ir_curve_id
    )


@pytest.fixture(scope="module")
def default_fixed_leg(
    default_cashflow_dates: pd.DatetimeIndex, default_fixed_cashflow: FixedRateCashflow
) -> IRFixedLeg:
    leg_cash_flows = CashflowSchedule.build_from_single_value_definition(
        default_cashflow_dates, default_fixed_cashflow
    )
    return IRFixedLeg(leg_cash_flows)


@pytest.fixture(scope="module")
def default_floating_leg(
    default_cashflow_dates: pd.DatetimeIndex,
    default_floating_cashflow: FloatingRateCashflow,
) -> IRFloatingLeg:
    leg_cash_flows = CashflowSchedule.build_from_single_value_definition(
        default_cashflow_dates, default_floating_cashflow
    )
    return IRFloatingLeg(leg_cash_flows)


@pytest.fixture(scope="module")
def default_fixed_float_swap(
    default_fixed_leg: IRFixedLeg, default_floating_leg: IRFloatingLeg
) -> IRFixedFloatSwap:
    return IRFixedFloatSwap(default_fixed_leg, default_floating_leg)
