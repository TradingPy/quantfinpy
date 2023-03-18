"""Test cases for market orders."""

from datetime import datetime

import pytest

from quantfinpy.instrument.instrument import Instrument
from quantfinpy.order.market import MarketOrder
from quantfinpy.order.order import Order, OrderSide


@pytest.mark.parametrize(
    ["quantity", "expected_order_side"], [(1.0, OrderSide.BUY), (-1.0, OrderSide.SELL)]
)
def test_mkt_order_ctor(
    default_instrument: Instrument, quantity: float, expected_order_side: OrderSide
):
    # Creating a market order.
    timestamp: datetime = datetime.utcnow()
    mkt_order = MarketOrder(default_instrument, quantity, timestamp)

    # Checking built market order.
    assert isinstance(mkt_order, Order)
    assert isinstance(mkt_order, MarketOrder)
    assert mkt_order.instrument == default_instrument
    assert mkt_order.quantity == quantity
    assert mkt_order.side == expected_order_side
    assert mkt_order.timestamp == timestamp
