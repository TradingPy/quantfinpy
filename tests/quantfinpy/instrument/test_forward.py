"""Test cases for forward instrument's interface."""

from datetime import date

from quantfinpy.instrument.forward import Forward
from quantfinpy.instrument.fx.spot import FXSpot
from quantfinpy.enum.currency import Currency


def test_forward_ctor():
    # Creating the forward instrument as a forward on a fx spot.
    fx_spot = FXSpot(Currency.USD, Currency.EUR)
    strike: float = 1.0
    maturity: date = date.today()
    fx_fwd = Forward(fx_spot, 1.0, maturity)

    # Checking built forward.
    assert isinstance(fx_fwd, Forward)
    assert fx_fwd.underlying == fx_spot
    assert fx_fwd.strike == strike
    assert fx_fwd.maturity == maturity
