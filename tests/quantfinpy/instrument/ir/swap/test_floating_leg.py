"""Test cases for IRFloatingLeg."""

import pandas as pd

from quantfinpy.data.cashflow.cashflow import FloatingRateCashflow
from quantfinpy.data.cashflow.schedule import CashflowSchedule
from quantfinpy.instrument import IRFloatingLeg


def test_ir_floating_leg_ctor(
    default_cashflow_dates: pd.DatetimeIndex,
    default_floating_cashflow: FloatingRateCashflow,
):
    # Creating a floating swap leg.
    leg_cash_flows = CashflowSchedule.build_from_single_value_definition(
        default_cashflow_dates, default_floating_cashflow
    )
    ir_floating_leg = IRFloatingLeg(leg_cash_flows)

    # Checking built floating swap leg.
    assert isinstance(ir_floating_leg, IRFloatingLeg)
    assert ir_floating_leg.scheduled_cashflows == leg_cash_flows
    assert ir_floating_leg == IRFloatingLeg.build_from_single_cashflow_definition(
        default_cashflow_dates, default_floating_cashflow
    )
