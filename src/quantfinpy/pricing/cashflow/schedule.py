"""Pricing of scheduled cashflow instruments."""


from quantfinpy.data.cashflow.cashflow import ObservedCashflow
from quantfinpy.data.data import DataSet
from quantfinpy.instrument.cashflow.schedule import CashflowScheduleInstrument
from quantfinpy.pricing.cashflow.cashflow import forward_value
from quantfinpy.pricing.forward import forward_values
from quantfinpy.utils.schedule import ScheduledValues


@forward_values.register
def __cashflow_schedule_forward_values(
    cashflows: CashflowScheduleInstrument, data: DataSet
) -> ScheduledValues[ObservedCashflow]:
    return ScheduledValues(
        tuple(
            map(
                lambda dated_cashflow: forward_value(
                    dated_cashflow[1], data, dated_cashflow[0]
                ),
                cashflows.scheduled_cashflows.items,
            )
        )
    )
