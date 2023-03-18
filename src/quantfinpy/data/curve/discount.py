"""Interfaces for discount curves and their ids."""

from datetime import date

from attrs import define

from quantfinpy.data.curve.curve import Curve, CurveId
from quantfinpy.data.data import map_data_class


@define(frozen=True)
class DiscountCurve(Curve):
    """Curve from which discount factors can be derived from."""

    def discount_factor(self, start_date: date, end_date: date) -> float:
        """
        Get the discount factor associated to the specified period.

        :param start_date: start of the period.
        :param end_date: end of the period.
        :return: discount factor.
        """
        raise NotImplementedError


@map_data_class(DiscountCurve)
@define(frozen=True)
class DiscountCurveId(CurveId):
    """Identify the different discount curve ids."""
