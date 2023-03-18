"""Interface for stop limit orders."""

from __future__ import annotations

from datetime import datetime

from attrs import define

from quantfinpy.order.limit import LimitOrder
from quantfinpy.order.order import Order


@define(frozen=True)
class StopLimitOrder(Order):
    """
    Interface for stop limit orders.

    Example:
        >>> from datetime import datetime
        >>> from quantfinpy.instrument import EquityShare
        >>> from quantfinpy.order import OrderSide
        >>>
        >>> instrument, quantity, timestamp, stop, limit = EquityShare("Apple"), 1.0, datetime(2023, 1, 1), 100, 99
        >>> buy_order = StopLimitOrder(instrument, quantity, timestamp, stop, limit)
        >>> buy_order.instrument
        EquityShare(company='Apple')
        >>> buy_order.quantity
        1.0
        >>> buy_order.timestamp
        datetime.datetime(2023, 1, 1, 0, 0)
        >>> buy_order.stop_price
        100
        >>> buy_order.limit
        99
        >>> buy_order.side.name
        'BUY'
        >>> sell_order = StopLimitOrder(instrument, -quantity, timestamp, stop, limit)
        >>> sell_order.side.name
        'SELL'
    """

    stop_price: float
    """stop price at which the order should be converted into a limit order."""
    limit: float
    """limit price for the limit order the stop-limit order transforms into."""

    def limit_order(self, stop_timestamp: datetime) -> LimitOrder:
        """
        Get the limit order the current instance transforms into once the stop price has been reached.

        :param stop_timestamp: time when the stop price is reached.
        :return: converted limit order.

        Example:
            >>> from datetime import datetime
            >>> from quantfinpy.instrument import EquityShare
            >>> from quantfinpy.order import OrderSide
            >>>
            >>> instrument, quantity, timestamp, stop, limit = EquityShare("Apple"), 1.0, datetime(2023, 1, 1), 100, 99
            >>> stop_order = StopLimitOrder(instrument, quantity, timestamp, stop, limit)
            >>> limit_order = stop_order.limit_order(datetime(2023, 1, 2))
            >>> limit_order.instrument
            EquityShare(company='Apple')
            >>> limit_order.quantity
            1.0
            >>> limit_order.timestamp
            datetime.datetime(2023, 1, 2, 0, 0)
            >>> limit_order.limit
            99
            >>> limit_order.side.name
            'BUY'
        """
        return LimitOrder(self.instrument, self.quantity, stop_timestamp, self.limit)

    def stop_price_reached(self, market_price: float) -> bool:
        """
        Identify if the market price is past the order's stop price.

        :param market_price: observed market price. Usually top bid for sale and smallest ask for buy.
        :return: flag indicating if market price is past the stop price.

        Example:
            >>> from datetime import datetime
            >>> from quantfinpy.instrument import EquityShare
            >>>
            >>> instrument, quantity, timestamp, stop, limit = EquityShare("Apple"), 1.0, datetime(2023, 1, 1), 100, 99
            >>> buy_order = StopLimitOrder(instrument, quantity, timestamp, stop, limit)
            >>> buy_order.stop_price_reached(101)
            False
            >>> buy_order.stop_price_reached(99)
            True
            >>> sell_order = StopLimitOrder(instrument, -quantity, timestamp, stop, limit)
            >>> sell_order.stop_price_reached(101)
            True
            >>> sell_order.stop_price_reached(99)
            False
        """
        return self.side.limit_reached(market_price, self.stop_price)
