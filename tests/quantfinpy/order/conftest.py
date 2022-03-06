"""Pytest fixtures for order testing."""

import pytest

from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.fx.spot import FXSpot
from quantfinpy.instrument.instrument import Instrument


@pytest.fixture(scope="module")
def default_instrument() -> Instrument:
    return FXSpot(Currency.USD, Currency.EUR)
