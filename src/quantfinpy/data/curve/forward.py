"""Interfaces for forward curves and their ids."""

from datetime import date

from attrs import define

from quantfinpy.data.curve.curve import Curve, CurveId
from quantfinpy.data.data import map_data_class


@define(frozen=True)
class ForwardCurve(Curve):
    """Curve from which forward rates can be derived from."""

    def forward_rate(self, start_date: date, end_date: date) -> float:
        """
        Get the forward rate associated to the specified period.

        :param start_date: start of the period.
        :param end_date: end of the period.
        :return: forward rate.
        """
        raise NotImplementedError


@map_data_class(ForwardCurve)
@define(frozen=True)
class ForwardCurveId(CurveId):
    """Identify the different forward curve ids."""
