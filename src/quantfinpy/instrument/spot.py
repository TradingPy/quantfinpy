"""Interface for spot instruments."""

from __future__ import annotations

from quantfinpy.utils.abc import abstract_interface
from quantfinpy.instrument.instrument import Instrument


@abstract_interface
class SpotInstrument(Instrument):
    """Interface for spot instruments."""

    __slots__ = ()
