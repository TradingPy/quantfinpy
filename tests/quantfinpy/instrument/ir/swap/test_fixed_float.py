"""Test cases for FixedFloat IR Swap."""

from datetime import date
import pandas as pd

from quantfinpy.enum.currency import Currency
from quantfinpy.data.ir.tenor import Tenor
from quantfinpy.data.ir.curve import InterestRateIndex, InterestRateCurveId
from quantfinpy.data.ir.cashflow import FixedRateCashflow, FloatingRateCashflow
from quantfinpy.instrument.ir.swap.fixed_leg import IRFixedLeg
from quantfinpy.instrument.ir.swap.floating_leg import IRFloatingLeg
from quantfinpy.instrument.ir.swap.fixed_float import IRFixedFloatSwap


def test_ir_fixed_float_swap_ctor():
    # Creating an ir fixed float swap around a fixed swap leg and a floating swap leg.

    cashflow_dates = pd.date_range(start=date.today(), periods=10, freq="3M")
    notional = 1000.0
    currency = Currency.USD
    fixed_rate = 0.01
    cashflow_tenor = Tenor(months=3)
    floating_rate_curve_id = InterestRateCurveId(InterestRateIndex.LIBOR, currency, cashflow_tenor)
    fixed_rate_cashflow = FixedRateCashflow(notional, currency, cashflow_tenor, fixed_rate)
    floating_rate_cashflow = FloatingRateCashflow(notional, currency, cashflow_tenor, floating_rate_curve_id)

    ir_fixed_leg = IRFixedLeg.build_unique_cashflow_definition(cashflow_dates, fixed_rate_cashflow)
    ir_floating_leg = IRFloatingLeg.build_unique_cashflow_definition(cashflow_dates, floating_rate_cashflow)
    ir_fixed_float_swap = IRFixedFloatSwap(ir_fixed_leg, ir_floating_leg)

    # Checking built swap.
    assert isinstance(ir_fixed_float_swap, IRFixedFloatSwap)
    assert ir_fixed_float_swap.fixed_leg == ir_fixed_leg
    assert ir_fixed_float_swap.floating_leg == ir_floating_leg
    assert list(map(lambda leg_position: leg_position.quantity, ir_fixed_float_swap.swap_legs)) == [1.0, -1.0]
