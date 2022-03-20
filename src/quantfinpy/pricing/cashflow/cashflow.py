"""Pricing of a cashflow."""

from datetime import date
from functools import singledispatch
from math import exp
from typing import Tuple

from pandas import Timedelta

from quantfinpy.data.cashflow.cashflow import (
    Cashflow,
    FixedRateCashflow,
    FloatingRateCashflow,
    ForwardCashflow,
    ObservedCashflow,
)
from quantfinpy.data.data import DataSet
from quantfinpy.utils.date import offset_timedelta_div


@singledispatch
def forward_value(
    cashflow: Cashflow, data: DataSet, cashflow_date: date
) -> Tuple[date, ObservedCashflow]:
    """
    Compute the forward value of the cashflow based on the provided data.

    :param cashflow: cashflow to value.
    :param data: data set used for the valuation.
    :param cashflow_date: cashflow date.
    :return: forward value wrapped into an observed cashflow.
    """
    raise NotImplementedError(f"Forward value for {type(cashflow)} is not supported.")


@forward_value.register
def __observed_forward_value(
    cashflow: ObservedCashflow, data: DataSet, cashflow_date: date
) -> Tuple[date, ObservedCashflow]:
    return cashflow_date, cashflow


def __forward_cashflow_forward_value(
    cashflow: ForwardCashflow, forward_rate: float, cashflow_date: date
) -> Tuple[date, ObservedCashflow]:
    projected_cashflow_date = cashflow_date + cashflow.tenor  # type: ignore
    return projected_cashflow_date, ObservedCashflow(
        cashflow.notional * exp(forward_rate), cashflow.currency
    )


@forward_value.register
def __fixed_rate_forward_value(
    cashflow: FixedRateCashflow, data: DataSet, cashflow_date: date
) -> Tuple[date, ObservedCashflow]:
    day_count_fraction = offset_timedelta_div(
        cashflow.tenor, Timedelta(365, "D"), cashflow_date
    )
    return __forward_cashflow_forward_value(
        cashflow, cashflow.rate * day_count_fraction, cashflow_date
    )


@forward_value.register
def __floating_rate_forward_value(
    cashflow: FloatingRateCashflow, data: DataSet, cashflow_date: date
) -> Tuple[date, ObservedCashflow]:
    rate = data[cashflow.forward_curve_id].forward_rate(  # type: ignore
        cashflow_date, cashflow_date + cashflow.tenor  # type: ignore
    )
    return __forward_cashflow_forward_value(cashflow, rate, cashflow_date)
