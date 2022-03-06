"""Test cases for fx forward instrument's interface."""

from datetime import date

from quantfinpy.instrument.fx.forward import FXForward
from quantfinpy.instrument.fx.spot import FXSpot
from quantfinpy.enum.currency import Currency


def test_forward_ctor():
    # Creating a fx forward as a forward on fx spot.
    fx_spot = FXSpot(Currency.USD, Currency.EUR)
    strike: float = 1.0
    maturity: date = date.today()
    fx_fwd = FXForward(fx_spot, 1.0, maturity)

    # Checking built fx spot.
    assert isinstance(fx_fwd, FXForward)
    assert fx_fwd.underlying == fx_spot
    assert fx_fwd.underlying_fx_spot == fx_spot
    assert fx_fwd.strike == strike
    assert fx_fwd.maturity == maturity
