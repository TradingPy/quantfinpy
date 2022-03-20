"""Pricing of the forward value of financial instruments."""

from functools import singledispatch

from quantfinpy.data.cashflow.cashflow import ObservedCashflow
from quantfinpy.data.data import DataSet
from quantfinpy.instrument.instrument import Instrument
from quantfinpy.utils.schedule import ScheduledValues


@singledispatch
def forward_values(
    instrument: Instrument, data: DataSet
) -> ScheduledValues[ObservedCashflow]:
    """
    Compute the forward values of the provided instrument based on the provided data.
    The result is a cashflow schedule corresponding to the timeseries of forward values.

    :param instrument: instrument to value.
    :param data: data to be used to value the instrument.
    :return: timeseries of forward values.
    """
    raise NotImplementedError
