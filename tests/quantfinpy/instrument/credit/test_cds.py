"""Test cases for cds."""

from datetime import date

import pandas as pd
from pandas import DateOffset

from quantfinpy.instrument.credit.bond import Bond
from quantfinpy.instrument.credit.cds import CDS


def test_cds_ctor(default_bond: Bond):
    # Building CDS as composition of a swapped credit instrument (here a bond) and the premium payment schedule.
    payment_dates = pd.date_range(start=date.today(), periods=10, freq="3M")
    payment_tenor = DateOffset(month=3)
    cds_spread = 0.012
    cds = CDS.create(cds_spread, default_bond, payment_dates, payment_tenor)

    # Checking built CDS.
    assert isinstance(cds, CDS)
    assert all(
        map(
            lambda date_pair: date_pair[0] == date_pair[1],
            zip(cds.payment_dates, payment_dates),
        )
    )
    assert cds.cds_spread == cds_spread
    assert cds.credit_instrument == default_bond
    assert cds.payment_tenor == payment_tenor
