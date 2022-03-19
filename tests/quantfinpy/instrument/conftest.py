"""Pytest fixtures for instrument testing."""

import pytest

from quantfinpy.enum.currency import Currency


@pytest.fixture(scope="module")
def default_currency() -> Currency:
    return Currency.USD
