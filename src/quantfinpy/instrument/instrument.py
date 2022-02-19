"""Financial instrument definition."""

from abc import ABC


class Instrument(ABC):
    """Financial instrument's interface."""

    __slots__ = ()

    def __new__(cls, *args, **kwargs):
        if cls is Instrument:
            raise TypeError(f"only children of '{cls.__name__}' may be instantiated.")
        return object.__new__(cls, *args, **kwargs)
