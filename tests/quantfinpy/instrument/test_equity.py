"""Test cases for equity instruments."""

import doctest

import quantfinpy.instrument.equity.option
import quantfinpy.instrument.equity.share


def test_doctest():
    assert doctest.testmod(quantfinpy.instrument.equity.share).failed == 0
    assert doctest.testmod(quantfinpy.instrument.equity.option).failed == 0
