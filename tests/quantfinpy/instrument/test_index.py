"""Test cases for instrument indices."""

from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.equity.share import EquityShare
from quantfinpy.instrument.index import Index


def test_index_ctor():
    # Building the index as an equity index whose constituents are GAFA shares.
    constituents = tuple(
        map(
            EquityShare,
            ("GOOGLE", "AMAZON", "META", "APPLE"),
        )
    )
    index = Index(constituents)

    # Checking built index.
    assert isinstance(index, Index)
    assert index.constituents == constituents
