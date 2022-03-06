"""Interface for swap instruments."""

from typing import Tuple

from attr import attrs

from quantfinpy.instrument.portfolio import Portfolio, Position


@attrs(slots=True, frozen=True, auto_attribs=True)
class Swap(Portfolio):
    """Interface for swap instruments."""

    @property
    def swap_legs(self) -> Tuple[Position, ...]:
        """Get the internal swap legs, i.e. the exchanged instrument positions."""
        return self.positions
