"""Abstract interface for all derivatives."""

from typing import Generic, Type, TypeVar

from attr import attrs

from quantfinpy.instrument.instrument import Instrument
from quantfinpy.utils.generic import identify_generic_specialization_types

UnderlyingType = TypeVar("UnderlyingType", bound=Instrument)


@attrs(slots=True, frozen=True, auto_attribs=True)
class Derivative(Instrument, Generic[UnderlyingType]):
    """Interface for derivative instruments."""

    __underlying: UnderlyingType
    """underlying instrument."""

    @classmethod
    def _underlying_type(cls) -> Type[Instrument]:
        underlying_type = identify_generic_specialization_types(cls, Derivative)[0]
        # Undefined case.
        if underlying_type is UnderlyingType:  # type: ignore
            return Instrument
        # Specialised case.
        return underlying_type

    @property
    def underlying(self) -> UnderlyingType:
        """Get option's underlying."""
        return self.__underlying

    def __attrs_post_init__(self) -> None:
        assert isinstance(self.underlying, self._underlying_type())
