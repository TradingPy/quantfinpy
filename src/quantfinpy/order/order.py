"""Base interface for all the kinds of orders."""

from __future__ import annotations

from enum import Enum, auto

from attr import attrs

from quantfinpy.instrument.instrument import Instrument


class OrderSide(Enum):
    """Enumerate the long/sort sides that an order can be associated with."""

    BUY = auto()
    SELL = auto()

    def limit_reached(self, market_price: float, limit_price: float) -> bool:
        """
        Identify if the market price is past the specified limit price.

        :param market_price: observed market price. Usually top bid for sale and smallest ask for buy.
        :param limit_price: specified limit price.
        :return: flag indicating if market price is past the limit.
        """
        if self == OrderSide.BUY:
            return market_price <= limit_price
        if self == OrderSide.SELL:
            return market_price >= limit_price
        raise NotImplementedError(f"Can't tell if limit has been reached for {self}.")


@attrs(slots=True, frozen=True, auto_attribs=True)
class Order:
    """Base interface for all the kinds of orders."""

    instrument: Instrument
    """instrument to be bought or sold. Could be replaced with instrument id in the future."""
    quantity: float
    """quantity of the instrument to be bought or sold. Positive for long position and negative for short."""

    def __attrs_post_init__(self) -> None:
        if self.quantity == 0.0:
            raise ValueError("An order shouldn't have null quantity.")

    @property
    def side(self) -> OrderSide:
        """Get order's side, like BUY or SELL."""
        if self.quantity > 0:
            return OrderSide.BUY
        return OrderSide.SELL
