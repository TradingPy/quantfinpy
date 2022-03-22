"""Test cases for equity shares."""

from quantfinpy.instrument.equity.share import EquityShare


def test_equity_share_ctor():
    # Building equity share for Google.
    company: str = "Google"
    share = EquityShare(company)

    # Checking the built equity share.
    assert isinstance(share, EquityShare)
    assert share.company == company
