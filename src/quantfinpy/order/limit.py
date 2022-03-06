"""Interface for limit orders."""

from __future__ import annotations

from attr import attrs

from quantfinpy.order.order import Order


@attrs(slots=True, frozen=True, auto_attribs=True)
class LimitOrder(Order):
    """Interface for limit orders."""

    limit: float
    """limit price at which the order should be executed."""

    def limit_reached(self, market_price: float) -> bool:
        """
        Identify if the market price is past the order's limit.

        :param market_price: observed market price. Usually top bid for sale and smallest ask for buy.
        :return: flag indicating if market price is past the limit.
        """
        return self.side.limit_reached(market_price, self.limit)
