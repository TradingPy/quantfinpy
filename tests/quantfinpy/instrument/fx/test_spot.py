"""Test cases for fx spot's interface."""

from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.fx.spot import FXSpot


def test_fx_spot_ctor():
    # Creating a fx spot.
    domestic_ccy: Currency = Currency.USD
    foreign_ccy: Currency = Currency.EUR
    fx_spot = FXSpot(domestic_ccy, foreign_ccy)

    # Checking built fx spot.
    assert isinstance(fx_spot, FXSpot)
    assert fx_spot.domestic_currency == domestic_ccy
    assert fx_spot.foreign_currency == foreign_ccy
