"""Base interfaces for all curves and their ids."""

from attr import attrs

from quantfinpy.data.data import Data, DataId, map_data_class
from quantfinpy.enum.currency import Currency


@attrs(slots=True, frozen=True, auto_attribs=True)
class Curve(Data):
    """Base class for all the curves."""


@map_data_class(Curve)
@attrs(slots=True, frozen=True, auto_attribs=True)
class CurveId(DataId):
    """Base class for all the curve ids."""

    currency: Currency
    """Curve's currency."""
