"""Abstract interface for all derivatives."""

from typing import Generic, Type, TypeVar

from attrs import define

from quantfinpy.instrument.instrument import Instrument
from quantfinpy.utils.generic import identify_generic_specialization_types

Underlying = TypeVar("Underlying", bound=Instrument)


@define(frozen=True)
class Derivative(Instrument, Generic[Underlying]):
    """Interface for derivative instruments."""

    __underlying: Underlying
    """underlying instrument."""

    @classmethod
    def _underlying_type(cls) -> Type[Instrument]:
        underlying_type = identify_generic_specialization_types(cls, Derivative)[0]
        # Undefined case.
        if underlying_type is Underlying:  # type: ignore
            return Instrument
        # Specialised case.
        return underlying_type

    @property
    def underlying(self) -> Underlying:
        """Get option's underlying."""
        return self.__underlying

    def __attrs_post_init__(self) -> None:
        assert isinstance(self.underlying, self._underlying_type())
