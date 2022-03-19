"""Interface for FX options."""

from attr import attrs

from quantfinpy.instrument.fx.spot import FXSpot
from quantfinpy.instrument.option import Option


@attrs(slots=True, frozen=True, auto_attribs=True)
class FXOption(Option):
    """FX option, i.e. option on FXSpot."""

    def __attrs_post_init__(self) -> None:
        super().__attrs_post_init__()
        assert isinstance(self.underlying, FXSpot)
