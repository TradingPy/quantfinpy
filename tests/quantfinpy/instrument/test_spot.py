"""Test cases for spot instrument's interface."""

import pytest

from quantfinpy.instrument.spot import SpotInstrument


# Test instantiation of SpotInstrument class. Should fail as it is intended to be an abstract interface.
def test_spot_instrument_ctor():
    with pytest.raises(TypeError) as exc_info:
        SpotInstrument()
    assert "only children of 'SpotInstrument' may be instantiated." in str(exc_info.value)
