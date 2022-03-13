"""Test cases for equity shares."""

from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.equity.share import EquityShare


def test_equity_share_ctor():
    # Building equity share for Google and quoted in USD.
    company: str = "Google"
    currency: Currency = Currency.USD
    share = EquityShare(company, currency)

    # Checking the built equity share.
    assert isinstance(share, EquityShare)
    assert share.currency == currency
    assert share.company == company
