"""Interface and definition of generic scheduled values, i.e. time series."""

from abc import abstractmethod
from datetime import date
from typing import Mapping, Protocol, TypeVar, runtime_checkable

from quantfinpy.utils.sort import assert_sorted_iterable

ValueType = TypeVar("ValueType", covariant=True)


@runtime_checkable
class ScheduledValues(Protocol[ValueType]):
    """Generic interface for scheduled values, i.e. time series."""

    __slots__ = ()

    @property
    @abstractmethod
    def schedule(self) -> Mapping[date, ValueType]:
        """Get underlying schedule of values."""

    def validate(self) -> None:
        """Validate internal schedule definition."""
        assert_sorted_iterable(self.schedule.keys())
