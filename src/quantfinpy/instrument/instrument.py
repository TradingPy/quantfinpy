"""Financial instrument definition."""

from __future__ import annotations

from quantfinpy.utils.abc import abstract_interface


@abstract_interface
class Instrument:
    """Financial instrument's interface."""

    __slots__ = ()

    @classmethod
    def validate_value(cls, instrument_value: float) -> None:
        """
        Validate an instrument value according to the current instrument type.

        :param instrument_value: an instrument value.
        """
