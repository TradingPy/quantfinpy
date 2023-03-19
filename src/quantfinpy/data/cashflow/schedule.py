"""Cashflow schedule interface and specialisations."""

import sys
from datetime import date

import pandas as pd

from quantfinpy.data.cashflow.cashflow import Cashflow, ForwardCashflow
from quantfinpy.utils.schedule import ScheduledValues

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

CashflowSchedule: TypeAlias = ScheduledValues[Cashflow]
"""Schedule, i.e. timeseries, of cashflows."""


def schedule_maturity(cashflow_schedule: CashflowSchedule) -> date:
    """
    Identify the maturity date of the provided schedule.

    :param cashflow_schedule: schedule whose maturity date is to be identified.
    :return: maturity date.
    """
    last_cashflow_date, last_cashflow = cashflow_schedule.schedule[-1]
    assert isinstance(last_cashflow_date, date)
    if isinstance(last_cashflow, ForwardCashflow):
        last_cashflow_date_ts: pd.Timestamp = last_cashflow.tenor + last_cashflow_date  # type: ignore
        return last_cashflow_date_ts.date()
    return last_cashflow_date
