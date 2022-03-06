"""Interface for market orders."""

from __future__ import annotations

from attr import attrs

from quantfinpy.order.order import Order


@attrs(slots=True, frozen=True, auto_attribs=True)
class MarketOrder(Order):
    """Interface for market orders."""
