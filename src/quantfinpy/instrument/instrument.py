"""Financial instrument definition."""

from __future__ import annotations

from quantfinpy.utils.abc import abstract_interface


@abstract_interface
class Instrument:
    """Financial instrument's interface."""

    __slots__ = ()
