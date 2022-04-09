"""Bond pricing."""


# To import forward_values definition for CashflowScheduleInstrument
# TODO: Find a way to register and dispatch without having unclear imports.
# pylint: disable=unused-import
import quantfinpy.pricing.cashflow.schedule
from quantfinpy.data.cashflow.cashflow import ObservedCashflow
from quantfinpy.data.data import DataSet
from quantfinpy.instrument.cashflow.schedule import CashflowScheduleInstrument
from quantfinpy.instrument.credit.bond import Bond
from quantfinpy.pricing.cashflow.cashflow import forward_value
from quantfinpy.pricing.forward import forward_values
from quantfinpy.utils.schedule import ScheduledValues


@forward_values.register
def __bond_forward_values(
    bond: Bond, data: DataSet
) -> ScheduledValues[ObservedCashflow]:
    coupon_values = forward_values(
        CashflowScheduleInstrument(bond.coupon_cashflows), data
    )

    return coupon_values + forward_value(bond.repayment_cashflow, data, bond.maturity)
