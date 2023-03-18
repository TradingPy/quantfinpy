"""Interfaces for equity shares."""

from attrs import define

from quantfinpy.instrument.instrument import Instrument


@define(frozen=True)
class EquityShare(Instrument):
    """Equity share."""

    company: str
    """company name."""

    @classmethod
    def validate_value(cls, instrument_value: float) -> None:
        """
        Validate a specific share value, i.e. checking positive.

        :param instrument_value: a share value.
        """
        Instrument.validate_value(instrument_value)
        assert (
            instrument_value >= 0.0
        ), f"A share value is always positive, received {instrument_value}."
