"""Test cases for scheduled cashflows."""

from itertools import repeat
from datetime import date
import pandas as pd

from quantfinpy.enum.currency import Currency
from quantfinpy.data.tenor import Tenor
from quantfinpy.data.ir.cashflow.cashflow import FixedRateCashflow
from quantfinpy.data.ir.cashflow.schedule import CashflowSchedule


def test_cashflow_schedule_ctor():
    # Building cashflow schedule as mapping between cashflow dates and cashflow values.
    cashflow_dates = pd.date_range(start=date.today(), periods=10, freq="3M")
    cashflow = FixedRateCashflow(1.0, Currency.USD, Tenor(months=3), 0.01)
    scheduled_cashflows = dict(zip(cashflow_dates, repeat(cashflow, cashflow_dates.size)))
    cashflow_schedule = CashflowSchedule(scheduled_cashflows)

    # Checking built cashflow_schedule.
    assert isinstance(cashflow_schedule, CashflowSchedule)
    assert cashflow_schedule.schedule == scheduled_cashflows
    assert all(map(lambda pair: pair[0] == pair[1], zip(cashflow_schedule.cashflows, scheduled_cashflows.values())))

    # Checking CashflowSchedule.build_from_single_cashflow_definition.
    cashflow_schedule_single_cashflow = CashflowSchedule.build_from_single_cashflow_definition(cashflow_dates, cashflow)
    assert cashflow_schedule == cashflow_schedule_single_cashflow
    # Assert that the scheduled cashflows only refer to the same cashflow instance (no duplication).
    assert all(map(lambda el: id(el) == id(cashflow), cashflow_schedule_single_cashflow.cashflows))
