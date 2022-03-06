"""Cashflow schedule interface and specialisations."""

from typing import Mapping, Iterable, ValuesView
from datetime import date
from attr import attrs

from quantfinpy.data.ir.cashflow.cashflow import Cashflow
from quantfinpy.utils.schedule import ScheduledValues


@attrs(frozen=True, slots=True, auto_attribs=True)
class CashflowSchedule(ScheduledValues[Cashflow]):
    """Schedule, i.e. timeseries, of cashflows."""

    _schedule: Mapping[date, Cashflow]

    def __attrs_post_init__(self) -> None:
        self.validate()

    @property
    def schedule(self) -> Mapping[date, Cashflow]:
        """Get underlying schedule of cashflows."""
        return self._schedule

    @property
    def cashflows(self) -> ValuesView[Cashflow]:
        """Get underlying sequence of cashflows."""
        return self.schedule.values()

    @classmethod
    def build_from_single_cashflow_definition(
        cls, dates: Iterable[date], cashflow: Cashflow
    ) -> "CashflowSchedule":
        """
        Build an instance of scheduled cashflow with the same cashflow being distributed at specified dates.

        :param dates: cashflow dates.
        :param cashflow: cashflow being distributed at the different cashflow dates.
        :return: instance of CashflowSchedule.
        """
        return cls({cashflow_date: cashflow for cashflow_date in dates})
