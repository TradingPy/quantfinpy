"""Enumerate the different currencies."""

from enum import Enum, auto


class Currency(Enum):
    """Enumeration of the different currencies."""

    USD = auto()
    """US dollar."""
    EUR = auto()
    """Euro."""
    GBP = auto()
    """British pound"""
    JPY = auto()
    """Japanese yen."""
