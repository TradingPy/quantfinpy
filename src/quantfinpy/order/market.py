"""Interface for market orders."""

from __future__ import annotations

from attrs import define

from quantfinpy.order.order import Order


@define(frozen=True)
class MarketOrder(Order):
    """Interface for market orders."""
