"""Test cases for base order's interface."""

import pytest

from quantfinpy.instrument.instrument import Instrument
from quantfinpy.order.limit import LimitOrder
from quantfinpy.order.order import Order, OrderSide
from quantfinpy.order.stop_limit import StopLimitOrder


@pytest.mark.parametrize(["quantity", "expected_order_side"], [(1.0, OrderSide.BUY), (-1.0, OrderSide.SELL)])
def test_stop_limit_order_ctor(default_instrument: Instrument, quantity: float, expected_order_side: OrderSide):
    # Creating a stop limit order.
    stop_price: float = 1.0
    limit_price: float = stop_price + 1
    stop_limit_order = StopLimitOrder(default_instrument, quantity, stop_price, limit_price)

    # Checking built stop limit order.
    assert isinstance(stop_limit_order, Order)
    assert isinstance(stop_limit_order, StopLimitOrder)
    assert stop_limit_order.instrument == default_instrument
    assert stop_limit_order.quantity == quantity
    assert stop_limit_order.side == expected_order_side
    assert stop_limit_order.stop_price == stop_price
    assert stop_limit_order.limit == limit_price
    assert stop_limit_order.limit_order == LimitOrder(default_instrument, quantity, limit_price)


@pytest.mark.parametrize(["market_price", "stop_price"], [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)])
@pytest.mark.parametrize("quantity", [-1.0, 1.0])
def test_stop_order_stop_reached(default_instrument: Instrument, market_price: float, stop_price: float, quantity: float):
    # Creating the stop limit order whose limit_reached function is to be checked.
    limit_price: float = stop_price + 1
    stop_limit_order = StopLimitOrder(default_instrument, quantity, stop_price, limit_price)
    # Check that StopLimitOrder.limit_reached works in the same way as OrderSide.limit_reached (already tested)
    assert stop_limit_order.stop_price_reached(market_price) \
           == stop_limit_order.side.limit_reached(market_price, stop_price)
