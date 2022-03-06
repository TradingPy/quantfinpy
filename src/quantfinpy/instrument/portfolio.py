"""Interface for portfolio of instruments."""

from typing import Tuple

from attr import attrs

from quantfinpy.instrument.instrument import Instrument


@attrs(slots=True, frozen=True, auto_attribs=True)
class Position:
    """Position in an instrument, i.e. a specific quantity of an instrument."""

    instrument: Instrument
    """instrument."""
    quantity: float
    """quantity."""


@attrs(slots=True, frozen=True, auto_attribs=True)
class Portfolio(Instrument):
    """Interface for portfolio of instruments."""

    positions: Tuple[Position, ...]
    """portfolio's positions."""
