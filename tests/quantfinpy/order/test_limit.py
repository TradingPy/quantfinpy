"""Test cases for limit orders."""

import pytest

from quantfinpy.instrument.instrument import Instrument
from quantfinpy.order.order import Order, OrderSide
from quantfinpy.order.limit import LimitOrder


@pytest.mark.parametrize(["quantity", "expected_order_side"], [(1.0, OrderSide.BUY), (-1.0, OrderSide.SELL)])
def test_limit_order_ctor(default_instrument: Instrument, quantity: float, expected_order_side: OrderSide):
    # Creating a limit order.
    limit_price: float = 1.0
    limit_order = LimitOrder(default_instrument, quantity, limit_price)

    # Checking built limit order.
    assert isinstance(limit_order, Order)
    assert isinstance(limit_order, LimitOrder)
    assert limit_order.instrument == default_instrument
    assert limit_order.quantity == quantity
    assert limit_order.side == expected_order_side
    assert limit_order.limit == limit_price


@pytest.mark.parametrize(["market_price", "limit_price"], [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)])
@pytest.mark.parametrize("quantity", [-1.0, 1.0])
def test_limit_order_limit_reached(default_instrument: Instrument, market_price: float, limit_price: float,
                                   quantity: float):
    # Creating the limit order whose limit_reached function is to be checked.
    limit_order = LimitOrder(default_instrument, quantity, limit_price)
    # Check that LimitOrder.limit_reached works in the same way as OrderSide.limit_reached (already tested)
    assert limit_order.limit_reached(market_price) == limit_order.side.limit_reached(market_price, limit_price)
