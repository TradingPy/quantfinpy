"""Interface for fx forward instruments."""

from attr import attrs

from quantfinpy.instrument.forward import Forward
from quantfinpy.instrument.fx.spot import FXSpot


@attrs(slots=True, frozen=True, auto_attribs=True)
class FXForward(Forward):
    """Interface for fx forward instruments."""

    def __attrs_post_init__(self) -> None:
        assert isinstance(self.underlying, FXSpot)

    @property
    def underlying_fx_spot(self) -> FXSpot:
        """Get underlying fx spot instrument."""
        assert isinstance(self.underlying, FXSpot)
        return self.underlying
