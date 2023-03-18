"""Interface for stop limit orders."""

from __future__ import annotations

from datetime import datetime

from attrs import define

from quantfinpy.order.limit import LimitOrder
from quantfinpy.order.order import Order


@define(frozen=True)
class StopLimitOrder(Order):
    """Interface for stop limit orders."""

    stop_price: float
    """stop price at which the order should be converted into a limit order."""
    limit: float
    """limit price for the limit order the stop-limit order transforms into."""

    def limit_order(self, stop_timestamp: datetime) -> LimitOrder:
        """
        Get the limit order the current instance transforms into once the stop price has been reached.

        :param stop_timestamp: time when the stop price is reached.
        :return: converted limit order.
        """
        return LimitOrder(self.instrument, self.quantity, stop_timestamp, self.limit)

    def stop_price_reached(self, market_price: float) -> bool:
        """
        Identify if the market price is past the order's stop price.

        :param market_price: observed market price. Usually top bid for sale and smallest ask for buy.
        :return: flag indicating if market price is past the stop price.
        """
        return self.side.limit_reached(market_price, self.stop_price)
