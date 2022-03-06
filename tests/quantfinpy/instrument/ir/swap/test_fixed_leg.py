"""Test cases for IRFixedLeg."""

from datetime import date
import pandas as pd

from quantfinpy.enum.currency import Currency
from quantfinpy.data.ir.tenor import Tenor
from quantfinpy.data.ir.cashflow import FixedRateCashflow
from quantfinpy.data.ir.cashflow_schedule import DuplicatedCashflowSchedule
from quantfinpy.instrument.ir.swap.fixed_leg import IRFixedLeg


def test_ir_fixed_leg_ctor():
    # Creating a fixed swap leg.
    cashflow_dates = pd.date_range(start=date.today(), periods=10, freq="3M")
    notional = 1000.0
    currency = Currency.USD
    fixed_rate = 0.01
    cashflow_tenor = Tenor(months=3)
    fixed_rate_cashflow = FixedRateCashflow(notional, currency, cashflow_tenor, fixed_rate)
    leg_cash_flows = DuplicatedCashflowSchedule(cashflow_dates, fixed_rate_cashflow)
    ir_fixed_leg = IRFixedLeg(leg_cash_flows)

    # Checking built fixed swap leg.
    assert isinstance(ir_fixed_leg, IRFixedLeg)
    assert ir_fixed_leg.cashflows == leg_cash_flows
    assert ir_fixed_leg == IRFixedLeg.build_unique_cashflow_definition(cashflow_dates, fixed_rate_cashflow)
