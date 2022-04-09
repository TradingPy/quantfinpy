"""Pricing of discounted valuation."""

from datetime import date
from typing import Iterator

from quantfinpy.data.cashflow.cashflow import ObservedCashflow
from quantfinpy.data.curve.discount import DiscountCurve, DiscountCurveId
from quantfinpy.data.data import DataSet
from quantfinpy.instrument.instrument import Instrument
from quantfinpy.pricing.forward import forward_values
from quantfinpy.utils.schedule import ScheduledValues


def discount_value(
    instrument: Instrument,
    data: DataSet,
    valuation_date: date,
    discounting_curve_id: DiscountCurveId,
) -> float:
    """
    Compute the discounted value of the provided instrument based on the provided data.

    :param instrument: instrument to value.
    :param data: data to be used to value the instrument.
    :param valuation_date: date to use in the discounting of the future values.
    :param discounting_curve_id: id of the discount curve to be used to discount future values.
    :return: discount value.
    """
    discount_curve: DiscountCurve = data[discounting_curve_id]  # type: ignore

    def discount_observed_cashflow(
        cashflow_date: date, cashflow: ObservedCashflow
    ) -> float:
        return cashflow.notional * discount_curve.discount_factor(
            valuation_date, cashflow_date
        )

    forward_value_schedule: ScheduledValues[ObservedCashflow] = forward_values(
        instrument, data
    )
    discounted_values: Iterator[float] = map(
        lambda dated_cashflow: discount_observed_cashflow(*dated_cashflow),
        filter(
            lambda dated_cashflow: dated_cashflow[0] >= valuation_date,
            forward_value_schedule.items,
        ),
    )

    return sum(discounted_values)
