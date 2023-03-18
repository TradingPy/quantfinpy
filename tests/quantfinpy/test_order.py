"""Test cases for order module."""

import doctest

import quantfinpy.order


def test_doctest():
    assert doctest.testmod(quantfinpy.order.market).failed == 0
    assert doctest.testmod(quantfinpy.order.limit).failed == 0
    assert doctest.testmod(quantfinpy.order.stop).failed == 0
    assert doctest.testmod(quantfinpy.order.stop_limit).failed == 0
