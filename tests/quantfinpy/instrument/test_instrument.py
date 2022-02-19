"""Test cases for financial instrument's interface."""

import pytest


from quantfinpy.instrument.instrument import Instrument


# Test instantiation of Instrument class. Should fail as it is intended to be an abstract interface.
def test_instrument_ctor():
    with pytest.raises(TypeError) as exc_info:
        instrument = Instrument()
    assert "only children of 'Instrument' may be instantiated." in str(exc_info.value)
