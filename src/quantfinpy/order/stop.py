"""Interface for stop orders."""

from __future__ import annotations

from datetime import datetime

from attrs import define

from quantfinpy.order.market import MarketOrder
from quantfinpy.order.order import Order


@define(frozen=True)
class StopOrder(Order):
    """
    Interface for stop orders and board orders, by symmetry of the order's quantity.

    Example:
        >>> from datetime import datetime
        >>> from quantfinpy.instrument import EquityShare
        >>> from quantfinpy.order import OrderSide
        >>>
        >>> instrument, quantity, timestamp, stop_price = EquityShare("Apple"), 1.0, datetime(2023, 1, 1), 100
        >>> buy_order = StopOrder(instrument, quantity, timestamp, stop_price)
        >>> buy_order.instrument
        EquityShare(company='Apple')
        >>> buy_order.quantity
        1.0
        >>> buy_order.timestamp
        datetime.datetime(2023, 1, 1, 0, 0)
        >>> buy_order.stop_price
        100
        >>> buy_order.side.name
        'BUY'
        >>> sell_order = StopOrder(instrument, -quantity, timestamp, stop_price)
        >>> sell_order.side.name
        'SELL'
    """

    stop_price: float
    """stop price at which the order should be converted into a market order."""

    def market_order(self, stop_timestamp: datetime) -> MarketOrder:
        """
        Get the market order the current instance transforms into once the stop price has been reached.

        :param stop_timestamp: timestamp for when the stop price is reached.
        :return: converted mkt order.

        Example:
            >>> from datetime import datetime
            >>> from quantfinpy.instrument import EquityShare
            >>> from quantfinpy.order import OrderSide
            >>>
            >>> instrument, quantity, timestamp, stop = EquityShare("Apple"), 1.0, datetime(2023, 1, 1), 100
            >>> stop_order = StopOrder(instrument, quantity, timestamp, stop)
            >>> mkt_order = stop_order.market_order(datetime(2023, 1, 2))
            >>> mkt_order.instrument
            EquityShare(company='Apple')
            >>> mkt_order.quantity
            1.0
            >>> mkt_order.timestamp
            datetime.datetime(2023, 1, 2, 0, 0)
            >>> mkt_order.side.name
            'BUY'
        """
        return MarketOrder(self.instrument, self.quantity, stop_timestamp)

    def stop_price_reached(self, market_price: float) -> bool:
        """
        Identify the market price is past the order's stop price.

        :param market_price: observed market price. Usually top bid for sale and smallest ask for buy.
        :return: flag indicating if market price is past the stop price.

        Example:
            >>> from datetime import datetime
            >>> from quantfinpy.instrument import EquityShare
            >>>
            >>> instrument, quantity, timestamp, stop = EquityShare("Apple"), 1.0, datetime(2023, 1, 1), 100
            >>> buy_order = StopOrder(instrument, quantity, timestamp, stop)
            >>> buy_order.stop_price_reached(101)
            False
            >>> buy_order.stop_price_reached(99)
            True
            >>> sell_order = StopOrder(instrument, -quantity, timestamp, stop)
            >>> sell_order.stop_price_reached(101)
            True
            >>> sell_order.stop_price_reached(99)
            False
        """
        return self.side.limit_reached(market_price, self.stop_price)
