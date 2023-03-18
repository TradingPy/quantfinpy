"""Interface for limit orders."""

from __future__ import annotations

from attrs import define

from quantfinpy.order.order import Order


@define(frozen=True)
class LimitOrder(Order):
    """
    Interface for limit orders.

    Example:
        >>> from datetime import datetime
        >>> from quantfinpy.instrument import EquityShare
        >>> from quantfinpy.order import OrderSide
        >>>
        >>> instrument, quantity, timestamp, limit = EquityShare("Apple"), 1.0, datetime(2023, 1, 1), 100
        >>> buy_order = LimitOrder(instrument, quantity, timestamp, limit)
        >>> buy_order.instrument
        EquityShare(company='Apple')
        >>> buy_order.quantity
        1.0
        >>> buy_order.timestamp
        datetime.datetime(2023, 1, 1, 0, 0)
        >>> buy_order.limit
        100
        >>> buy_order.side.name
        'BUY'
        >>> sell_order = LimitOrder(instrument, -quantity, timestamp, limit)
        >>> sell_order.side.name
        'SELL'
    """

    limit: float
    """limit price at which the order should be executed."""

    def limit_reached(self, market_price: float) -> bool:
        """
        Identify if the market price is past the order's limit.

        :param market_price: observed market price. Usually top bid for sale and smallest ask for buy.
        :return: flag indicating if market price is past the limit.

        Example:
            >>> from datetime import datetime
            >>> from quantfinpy.instrument import EquityShare
            >>>
            >>> instrument, quantity, timestamp, limit = EquityShare("Apple"), 1.0, datetime(2023, 1, 1), 100
            >>> buy_order = LimitOrder(instrument, quantity, timestamp, limit)
            >>> buy_order.limit_reached(101)
            False
            >>> buy_order.limit_reached(99)
            True
            >>> sell_order = LimitOrder(instrument, -quantity, timestamp, limit)
            >>> sell_order.limit_reached(101)
            True
            >>> sell_order.limit_reached(99)
            False
        """
        return self.side.limit_reached(market_price, self.limit)
