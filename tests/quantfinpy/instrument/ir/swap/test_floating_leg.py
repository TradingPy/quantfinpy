"""Test cases for IRFloatingLeg."""

from datetime import date

import pandas as pd

from quantfinpy.data.ir.cashflow.cashflow import FloatingRateCashflow
from quantfinpy.data.ir.cashflow.schedule import CashflowSchedule
from quantfinpy.data.ir.curve import InterestRateCurveId, InterestRateIndex
from quantfinpy.data.tenor import Tenor
from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.ir.swap.floating_leg import IRFloatingLeg


def test_ir_floating_leg_ctor():
    # Creating a floating swap leg.
    cashflow_dates = pd.date_range(start=date.today(), periods=10, freq="3M")
    notional = 1000.0
    currency = Currency.USD
    tenor = Tenor(months=3)
    floating_rate_curve_id = InterestRateCurveId(
        InterestRateIndex.LIBOR, currency, tenor
    )
    floating_rate_cashflow = FloatingRateCashflow(
        notional, currency, tenor, floating_rate_curve_id
    )
    leg_cash_flows = CashflowSchedule.build_from_single_value_definition(
        cashflow_dates, floating_rate_cashflow
    )
    ir_floating_leg = IRFloatingLeg(leg_cash_flows)

    # Checking built floating swap leg.
    assert isinstance(ir_floating_leg, IRFloatingLeg)
    assert ir_floating_leg.scheduled_cashflows == leg_cash_flows
    assert ir_floating_leg == IRFloatingLeg.build_from_single_cashflow_definition(
        cashflow_dates, floating_rate_cashflow
    )
