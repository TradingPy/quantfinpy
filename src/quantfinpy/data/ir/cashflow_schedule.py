"""Cashflow schedule interface and specialisations."""

from abc import ABC, abstractmethod
from typing import Mapping, Iterable, ValuesView
from datetime import date
from attr import attrs

from quantfinpy.data.ir.cashflow import Cashflow
from quantfinpy.utils.sort import assert_sorted_iterable


@attrs(frozen=True, slots=True, auto_attribs=True)
class CashflowSchedule(ABC):
    """Schedule, i.e. timeseries, of cashflows."""

    def __attrs_post_init__(self) -> None:
        assert_sorted_iterable(self.schedule.keys())

    @property
    @abstractmethod
    def schedule(self) -> Mapping[date, Cashflow]:
        """Get underlying schedule of cashflows."""

    @property
    def cashflows(self) -> ValuesView[Cashflow]:
        """Get underlying sequence of cashflows."""
        return self.schedule.values()


@attrs(frozen=True, slots=True, auto_attribs=True)
class FullCashflowSchedule(CashflowSchedule):
    """Fully defined cashflow schedule."""

    _schedule: Mapping[date, Cashflow]
    """Schedule of cashflows as a mapping between dates and cashflows."""

    @property
    def schedule(self) -> Mapping[date, Cashflow]:
        """Get underlying schedule of cashflows."""
        return self._schedule


@attrs(frozen=True, slots=True, auto_attribs=True)
class DuplicatedCashflowSchedule(CashflowSchedule):
    """Cashflow schedule with same cashflow at different dates."""

    _schedule_dates: Iterable[date]
    """Schedule dates."""

    cashflow: Cashflow
    """cashflow distributed at each schedule date."""

    @property
    def schedule(self) -> Mapping[date, Cashflow]:
        """Get underlying schedule of cashflows."""
        return {cashflow_date: self.cashflow for cashflow_date in self._schedule_dates}
