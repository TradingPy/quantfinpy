"""Pytest fixtures for equity instrument testing."""

import pytest

from quantfinpy.instrument import EquityShare


@pytest.fixture(scope="module")
def default_company() -> str:
    return "Google"


@pytest.fixture(scope="module")
def default_share(default_company: str):
    return EquityShare(default_company)
