"""Interface for Equity options."""

from attr import attrs

from quantfinpy.instrument.equity.share import EquityShare
from quantfinpy.instrument.option import Option


@attrs(slots=True, frozen=True, auto_attribs=True)
class EquityOption(Option):
    """Equity option, i.e. option on Equity share."""

    def __attrs_post_init__(self) -> None:
        super().__attrs_post_init__()
        assert isinstance(self.underlying, EquityShare)
