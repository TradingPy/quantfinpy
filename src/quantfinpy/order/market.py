"""Interface for market orders."""

from __future__ import annotations

from attrs import define

from quantfinpy.order.order import Order


@define(frozen=True)
class MarketOrder(Order):
    """
    Interface for market orders.

    Example:
        >>> from datetime import datetime
        >>> from quantfinpy.instrument import EquityShare
        >>> from quantfinpy.order import OrderSide
        >>>
        >>> instrument, quantity, timestamp = EquityShare("Apple"), 1.0, datetime(2023, 1, 1)
        >>> buy_order = MarketOrder(instrument, quantity, timestamp)
        >>> buy_order.instrument
        EquityShare(company='Apple')
        >>> buy_order.quantity
        1.0
        >>> buy_order.timestamp
        datetime.datetime(2023, 1, 1, 0, 0)
        >>> buy_order.side.name
        'BUY'
        >>> sell_order = MarketOrder(instrument, -quantity, timestamp)
        >>> sell_order.side.name
        'SELL'
    """
