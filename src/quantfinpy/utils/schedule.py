"""Interface and definition of generic scheduled values, i.e. time series."""

from __future__ import annotations

from datetime import date
from functools import singledispatchmethod
from itertools import chain
from typing import Any, Generic, Iterable, Iterator, Tuple, Type, TypeVar

from attr import attrs

from quantfinpy.utils.sort import assert_sorted_iterator

ValueType = TypeVar("ValueType", covariant=False)


ScheduledValuesSubClass = TypeVar("ScheduledValuesSubClass")


@attrs(frozen=True, slots=True, auto_attribs=True)
class ScheduledValues(Generic[ValueType]):
    """Scheduled values, i.e. timeseries."""

    schedule: Iterable[Tuple[date, ValueType]]

    def __attrs_post_init__(self) -> None:
        assert_sorted_iterator(self.dates)

    @property
    def dates(self) -> Iterator[date]:
        """Get schedule's dates."""
        return map(lambda dated_val: dated_val[0], self.schedule)

    @property
    def values(self) -> Iterator[ValueType]:
        """Get schedule's values."""
        return map(lambda dated_val: dated_val[1], self.schedule)

    @property
    def items(self) -> Iterator[Tuple[date, ValueType]]:
        """Get schedule's iterator."""
        return iter(self.schedule)

    @classmethod
    def build_from_single_value_definition(
        cls: Type[ScheduledValues[ValueType]],
        dates: Iterable[date],
        value: ValueType,
    ) -> ScheduledValues[ValueType]:
        """
        Build an instance of cls with the same value being associated to the specified dates.

        :param dates: schedule dates.
        :param value: value associated to the different schedule dates.
        :return: instance of specified cls.
        """
        return cls(tuple(map(lambda schedule_date: (schedule_date, value), dates)))

    @singledispatchmethod
    def __add__(self, other: Any) -> ScheduledValues[ValueType]:
        raise NotImplementedError

    @__add__.register(tuple)
    def _add_dated_value(
        self, other: Tuple[date, ValueType]
    ) -> "ScheduledValues[ValueType]":
        previous_iter = filter(lambda dated_val: dated_val[0] <= other[0], self.items)
        past_iter = filter(lambda dated_val: dated_val[0] > other[0], self.items)
        return self.__class__(tuple(chain(previous_iter, (other,), past_iter)))
