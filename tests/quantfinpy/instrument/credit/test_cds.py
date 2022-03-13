"""Test cases for cds."""

from datetime import date

import pandas as pd
from cytoolz.itertoolz import last  # pylint: disable=no-name-in-module

from quantfinpy.data.tenor import Tenor
from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.credit.cds import CDS
from quantfinpy.instrument.credit.instrument import CreditInstrument


def test_cds_ctor():
    # Building CDS as composition of swapped credit instrument (could be bond) and the premium payment schedule.
    reference_entity: str = "Company"
    payment_dates = pd.date_range(start=date.today(), periods=10, freq="3M")
    payment_tenor = Tenor(month=3)
    cds_spread = 0.012
    credit_instrument = CreditInstrument(
        reference_entity, last(payment_dates), 1.0, Currency.USD
    )
    cds = CDS(cds_spread, credit_instrument, payment_dates, payment_tenor)

    # Checking built CDS.
    assert isinstance(cds, CDS)
    assert all(
        map(
            lambda date_pair: date_pair[0] == date_pair[1],
            zip(cds.payment_dates, payment_dates),
        )
    )
    assert cds.cds_spread == cds_spread
    assert cds.credit_instrument == credit_instrument
    assert cds.payment_tenor == payment_tenor
