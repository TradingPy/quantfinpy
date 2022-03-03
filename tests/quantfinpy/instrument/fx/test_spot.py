"""Test cases for fx spot's interface."""

from quantfinpy.instrument.fx.spot import FXSpot
from quantfinpy.enum.currency import Currency


def test_fx_spot_ctor():
    domestic_ccy: Currency = Currency.USD
    foreign_ccy: Currency = Currency.EUR
    fx_spot = FXSpot(domestic_ccy, foreign_ccy)

    assert isinstance(fx_spot, FXSpot)
    assert fx_spot.domestic_currency == domestic_ccy
    assert fx_spot.foreign_currency == foreign_ccy
