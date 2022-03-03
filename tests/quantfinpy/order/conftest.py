"""Pytest fixtures for order testing."""

import pytest

from quantfinpy.instrument.instrument import Instrument
from quantfinpy.instrument.fx.spot import FXSpot
from quantfinpy.enum.currency import Currency


@pytest.fixture(scope="module")
def default_instrument() -> Instrument:
    return FXSpot(Currency.USD, Currency.EUR)
