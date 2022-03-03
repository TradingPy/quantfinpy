"""Test cases for market orders."""

import pytest

from quantfinpy.instrument.instrument import Instrument
from quantfinpy.order.order import Order, OrderSide
from quantfinpy.order.market import MarketOrder


@pytest.mark.parametrize(["quantity", "expected_order_side"], [(1.0, OrderSide.BUY), (-1.0, OrderSide.SELL)])
def test_mkt_order_ctor(default_instrument: Instrument, quantity: float, expected_order_side: OrderSide):
    mkt_order = MarketOrder(default_instrument, quantity)
    assert isinstance(mkt_order, Order)
    assert isinstance(mkt_order, MarketOrder)
    assert mkt_order.instrument == default_instrument
    assert mkt_order.quantity == quantity
    assert mkt_order.side == expected_order_side
