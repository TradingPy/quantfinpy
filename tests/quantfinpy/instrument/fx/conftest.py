"""Pytest fixtures for fx instrument testing."""

import pytest

from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.fx.spot import FXSpot


@pytest.fixture(scope="module")
def default_fx_spot():
    return FXSpot(Currency.USD, Currency.EUR)
