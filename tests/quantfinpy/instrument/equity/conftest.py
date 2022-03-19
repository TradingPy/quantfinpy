"""Pytest fixtures for equity instrument testing."""

import pytest

from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.equity.share import EquityShare


@pytest.fixture(scope="module")
def default_company() -> str:
    return "Google"


@pytest.fixture(scope="module")
def default_share(default_currency: Currency, default_company: str):
    return EquityShare(default_company, default_currency)
