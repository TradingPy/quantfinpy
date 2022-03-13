"""Interface for instrument indices."""

from typing import Iterable

from attr import attrs

from quantfinpy.instrument.instrument import Instrument


@attrs(slots=True, frozen=True, auto_attribs=True)
class Index(Instrument):
    """Instrument index, i.e. set of instruments."""

    constituents: Iterable[Instrument]
    """index's constituents."""
