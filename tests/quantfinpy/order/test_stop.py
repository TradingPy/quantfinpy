"""Test cases for stop orders."""

import pytest

from quantfinpy.instrument.instrument import Instrument
from quantfinpy.order.order import Order, OrderSide
from quantfinpy.order.market import MarketOrder
from quantfinpy.order.stop import StopOrder


@pytest.mark.parametrize(["quantity", "expected_order_side"], [(1.0, OrderSide.BUY), (-1.0, OrderSide.SELL)])
def test_stop_order_ctor(default_instrument: Instrument, quantity: float, expected_order_side: OrderSide):
    stop_price: float = 1.0
    stop_order = StopOrder(default_instrument, quantity, stop_price)
    assert isinstance(stop_order, Order)
    assert isinstance(stop_order, StopOrder)
    assert stop_order.instrument == default_instrument
    assert stop_order.quantity == quantity
    assert stop_order.side == expected_order_side
    assert stop_order.stop_price == stop_price
    assert stop_order.market_order == MarketOrder(default_instrument, quantity)


@pytest.mark.parametrize(["market_price", "stop_price"], [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)])
@pytest.mark.parametrize("quantity", [-1.0, 1.0])
def test_stop_order_stop_reached(default_instrument: Instrument, market_price: float, stop_price: float,
                                 quantity: float):
    stop_order = StopOrder(default_instrument, quantity, stop_price)
    assert stop_order.stop_price_reached(market_price) == stop_order.side.limit_reached(market_price, stop_price)
