"""Interface and definition of generic scheduled values, i.e. time series."""

from __future__ import annotations

from datetime import date
from functools import singledispatchmethod
from itertools import chain
from typing import Any, Generic, Iterable, Iterator, Sequence, Tuple, Type, TypeVar

from attr import attrs

from quantfinpy.utils.sort import assert_sorted_iterator

Value = TypeVar("Value", covariant=False)


ScheduledValuesSubClass = TypeVar("ScheduledValuesSubClass")


@attrs(frozen=True, slots=True, auto_attribs=True)
class ScheduledValues(Generic[Value]):
    """Scheduled values, i.e. timeseries."""

    schedule: Sequence[Tuple[date, Value]]

    def __attrs_post_init__(self) -> None:
        assert_sorted_iterator(self.dates)

    @property
    def dates(self) -> Iterator[date]:
        """Get schedule's dates."""
        return map(lambda dated_val: dated_val[0], self.schedule)

    @property
    def values(self) -> Iterator[Value]:
        """Get schedule's values."""
        return map(lambda dated_val: dated_val[1], self.schedule)

    @property
    def items(self) -> Iterator[Tuple[date, Value]]:
        """Get schedule's iterator."""
        return iter(self.schedule)

    @classmethod
    def build_from_single_value_definition(
        cls: Type[ScheduledValues[Value]],
        dates: Iterable[date],
        value: Value,
    ) -> ScheduledValues[Value]:
        """
        Build an instance of cls with the same value being associated to the specified dates.

        :param dates: schedule dates.
        :param value: value associated to the different schedule dates.
        :return: instance of specified cls.
        """
        return cls(tuple(map(lambda schedule_date: (schedule_date, value), dates)))

    @singledispatchmethod
    def __add__(self, other: Any) -> ScheduledValues[Value]:
        raise NotImplementedError

    @__add__.register(tuple)
    def _add_dated_value(self, other: Tuple[date, Value]) -> "ScheduledValues[Value]":
        previous_iter = filter(lambda dated_val: dated_val[0] <= other[0], self.items)
        past_iter = filter(lambda dated_val: dated_val[0] > other[0], self.items)
        return self.__class__(tuple(chain(previous_iter, (other,), past_iter)))
