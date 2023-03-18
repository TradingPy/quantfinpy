"""Interface for stop orders."""

from __future__ import annotations

from datetime import datetime

from attrs import define

from quantfinpy.order.market import MarketOrder
from quantfinpy.order.order import Order


@define(frozen=True)
class StopOrder(Order):
    """Interface for stop orders and board orders, by symmetry of the order's quantity."""

    stop_price: float
    """stop price at which the order should be converted into a market order."""

    def market_order(self, stop_timestamp: datetime) -> MarketOrder:
        """
        Get the market order the current instance transforms into once the stop price has been reached.

        :param stop_timestamp: timestamp for when the stop price is reached.
        :return: converted mkt order.
        """
        return MarketOrder(self.instrument, self.quantity, stop_timestamp)

    def stop_price_reached(self, market_price: float) -> bool:
        """
        Identify the market price is past the order's stop price.

        :param market_price: observed market price. Usually top bid for sale and smallest ask for buy.
        :return: flag indicating if market price is past the stop price.
        """
        return self.side.limit_reached(market_price, self.stop_price)
