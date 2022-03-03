"""Enumerate the different currencies."""

from enum import Enum, auto


class Currency(Enum):
    """Enumeration of the different currencies."""

    USD = auto()
    EUR = auto()
    GBP = auto()
    JPY = auto()
