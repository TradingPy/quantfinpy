"""Test cases for fx instruments."""

import doctest

import quantfinpy.instrument.fx.forward
import quantfinpy.instrument.fx.option
import quantfinpy.instrument.fx.spot


def test_doctest():
    assert doctest.testmod(quantfinpy.instrument.fx.spot).failed == 0
    assert doctest.testmod(quantfinpy.instrument.fx.option).failed == 0
    assert doctest.testmod(quantfinpy.instrument.fx.forward).failed == 0
