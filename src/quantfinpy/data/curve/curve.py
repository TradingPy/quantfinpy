"""Base interfaces for all curves and their ids."""

from attrs import define

from quantfinpy.data.data import Data, DataId, map_data_class
from quantfinpy.enum.currency import Currency


@define(frozen=True)
class Curve(Data):
    """Base class for all the curves."""


@map_data_class(Curve)
@define(frozen=True)
class CurveId(DataId):
    """Base class for all the curve ids."""

    currency: Currency
    """Curve's currency."""
