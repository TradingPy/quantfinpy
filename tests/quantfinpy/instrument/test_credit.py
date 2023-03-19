"""Test cases for credit instruments."""

import doctest

import quantfinpy.instrument.credit.bond
import quantfinpy.instrument.credit.bond_option
import quantfinpy.instrument.credit.cds


def test_doctest():
    assert doctest.testmod(quantfinpy.instrument.credit.bond).failed == 0
    assert doctest.testmod(quantfinpy.instrument.credit.bond_option).failed == 0
    assert doctest.testmod(quantfinpy.instrument.credit.cds).failed == 0
