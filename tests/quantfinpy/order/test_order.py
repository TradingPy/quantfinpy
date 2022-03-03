"""Test cases for base order's interface."""

import pytest

from quantfinpy.instrument.instrument import Instrument
from quantfinpy.order.order import Order, OrderSide


def test_order_null_quantity(default_instrument: Instrument):
    with pytest.raises(ValueError) as exc_info:
        Order(default_instrument, 0.0)
    assert "An order shouldn't have null quantity." in str(exc_info.value)


@pytest.mark.parametrize(["quantity", "expected_order_side"], [(1.0, OrderSide.BUY), (-1.0, OrderSide.SELL)])
def test_order_ctor(default_instrument: Instrument, quantity: float, expected_order_side: OrderSide):
    order = Order(default_instrument, quantity)
    assert isinstance(order, Order)
    assert order.instrument == default_instrument
    assert order.quantity == quantity
    assert order.side == expected_order_side


@pytest.mark.parametrize(["market_price", "limit_price"], [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)])
@pytest.mark.parametrize("order_side", OrderSide)
def test_order_side_limit_reached(market_price: float, limit_price: float, order_side: OrderSide):
    if order_side == OrderSide.BUY:
        assert (market_price <= limit_price) == order_side.limit_reached(market_price, limit_price)
    elif order_side == OrderSide.SELL:
        assert (market_price >= limit_price) == order_side.limit_reached(market_price, limit_price)
    else:
        with pytest.raises(NotImplementedError) as exc_info:
            order_side.limit_reached(market_price, limit_price)
        assert f"Can't tell if limit has been reached for {order_side}." == str(exc_info.value)
