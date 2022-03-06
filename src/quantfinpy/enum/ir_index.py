"""Enumerate the different interest rate indices."""

from enum import Enum, auto


class InterestRateIndex(Enum):
    """Enumeration of the different interest rate indices."""

    OIS = auto()
    """Overnight Index Swap rate."""
    LIBOR = auto()
    """London Interbank Offered Rate."""
