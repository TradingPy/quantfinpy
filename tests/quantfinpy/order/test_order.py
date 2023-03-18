"""Test cases for base order's interface."""

from datetime import datetime

import pytest

from quantfinpy.instrument.instrument import Instrument
from quantfinpy.order.order import Order, OrderSide


def test_order_null_quantity(default_instrument: Instrument):
    with pytest.raises(ValueError) as exc_info:
        Order(default_instrument, 0.0, datetime.utcnow())
    assert "An order shouldn't have null quantity." in str(exc_info.value)


@pytest.mark.parametrize(
    ["quantity", "expected_order_side"], [(1.0, OrderSide.BUY), (-1.0, OrderSide.SELL)]
)
def test_order_ctor(
    default_instrument: Instrument, quantity: float, expected_order_side: OrderSide
):
    limit_timestamp: datetime = datetime.utcnow()
    # Creating an order (basic one equivalent to a market order).
    order = Order(default_instrument, quantity, limit_timestamp)

    # Checking built order.
    assert isinstance(order, Order)
    assert order.instrument == default_instrument
    assert order.quantity == quantity
    assert order.side == expected_order_side
    assert order.timestamp == limit_timestamp


@pytest.mark.parametrize(
    ["market_price", "limit_price"], [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
)
@pytest.mark.parametrize("order_side", OrderSide)
def test_order_side_limit_reached(
    market_price: float, limit_price: float, order_side: OrderSide
):
    # Checking OrderSide.limit_reached for the buy side of an order.
    if order_side == OrderSide.BUY:
        assert (market_price <= limit_price) == order_side.limit_reached(
            market_price, limit_price
        )
    # Checking OrderSide.limit_reached for the sell side of an order.
    elif order_side == OrderSide.SELL:
        assert (market_price >= limit_price) == order_side.limit_reached(
            market_price, limit_price
        )
    # Checking that other order side values are not supported. Should have an explicit test if they do.
    else:
        with pytest.raises(NotImplementedError) as exc_info:
            order_side.limit_reached(market_price, limit_price)
        assert f"Can't tell if limit has been reached for {order_side}." == str(
            exc_info.value
        )
