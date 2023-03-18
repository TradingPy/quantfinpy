"""Interface for instrument indices."""

from typing import Tuple

from attrs import define

from quantfinpy.instrument.instrument import Instrument


@define(frozen=True)
class Index(Instrument):
    """Instrument index, i.e. set of instruments."""

    constituents: Tuple[Instrument, ...]
    """index's constituents."""
