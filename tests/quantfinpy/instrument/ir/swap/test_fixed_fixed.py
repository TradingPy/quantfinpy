"""Test cases for FixedFixed IR Swap."""

from datetime import date

import pandas as pd

from quantfinpy.data.cashflow.cashflow import FixedRateCashflow
from quantfinpy.data.tenor import Tenor
from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.ir.swap.fixed_fixed import IRFixedFixedSwap
from quantfinpy.instrument.ir.swap.fixed_leg import IRFixedLeg


def test_ir_fixed_fixed_swap_ctor():
    # Creating a cross currency swap around 2 fixed legs in 2 different currencies.

    cashflow_dates = pd.date_range(start=date.today(), periods=10, freq="3M")
    cashflow_tenor = Tenor(months=3)
    fixed_rate = 0.01

    receiver_currency = Currency.JPY
    receiver_notional = 100000.0
    receiver_cashflow = FixedRateCashflow(
        receiver_notional, receiver_currency, cashflow_tenor, fixed_rate
    )

    payer_currency = Currency.USD
    payer_notional = 1000.0
    payer_cashflow = FixedRateCashflow(
        payer_notional, payer_currency, cashflow_tenor, fixed_rate
    )

    receiver_leg = IRFixedLeg.build_from_single_cashflow_definition(
        cashflow_dates, receiver_cashflow
    )
    payer_leg = IRFixedLeg.build_from_single_cashflow_definition(
        cashflow_dates, payer_cashflow
    )
    ir_fixed_fixed_swap = IRFixedFixedSwap(receiver_leg, payer_leg)

    # Checking built swap.
    assert isinstance(ir_fixed_fixed_swap, IRFixedFixedSwap)
    assert ir_fixed_fixed_swap.receiver_fixed_leg == receiver_leg
    assert ir_fixed_fixed_swap.payer_fixed_leg == payer_leg
    assert list(
        map(lambda leg_position: leg_position.quantity, ir_fixed_fixed_swap.swap_legs)
    ) == [1.0, -1.0]
