"""Test cases for IRFixedLeg."""

import pandas as pd

from quantfinpy.data.cashflow.cashflow import FixedRateCashflow
from quantfinpy.data.cashflow.schedule import CashflowSchedule
from quantfinpy.instrument import IRFixedLeg


def test_ir_fixed_leg_ctor(
    default_cashflow_dates: pd.DatetimeIndex, default_fixed_cashflow: FixedRateCashflow
):
    # Creating a fixed swap leg.
    leg_cash_flows = CashflowSchedule.build_from_single_value_definition(
        default_cashflow_dates, default_fixed_cashflow
    )
    ir_fixed_leg = IRFixedLeg(leg_cash_flows)

    # Checking built fixed swap leg.
    assert isinstance(ir_fixed_leg, IRFixedLeg)
    assert ir_fixed_leg.scheduled_cashflows == leg_cash_flows
    assert ir_fixed_leg == IRFixedLeg.build_from_single_cashflow_definition(
        default_cashflow_dates, default_fixed_cashflow
    )
