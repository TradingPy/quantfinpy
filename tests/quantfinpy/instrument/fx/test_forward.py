"""Test cases for fx forward instrument's interface."""

from datetime import date

from quantfinpy.instrument import FXForward, FXSpot


def test_forward_ctor(default_fx_spot: FXSpot):
    # Creating a fx forward as a forward on fx spot.
    strike: float = 1.0
    maturity: date = date.today()
    fx_fwd = FXForward(default_fx_spot, strike, maturity)

    # Checking built fx spot.
    assert isinstance(fx_fwd, FXForward)
    assert fx_fwd.underlying == default_fx_spot
    assert fx_fwd.strike == strike
    assert fx_fwd.maturity == maturity
