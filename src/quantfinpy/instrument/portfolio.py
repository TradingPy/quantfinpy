"""Interface for portfolio of instruments."""

from typing import Tuple

from attrs import define

from quantfinpy.instrument.instrument import Instrument


@define(frozen=True)
class Position:
    """Position in an instrument, i.e. a specific quantity of an instrument."""

    instrument: Instrument
    """instrument."""
    quantity: float
    """quantity."""


@define(frozen=True)
class Portfolio(Instrument):
    """Interface for portfolio of instruments."""

    positions: Tuple[Position, ...]
    """portfolio's positions."""
