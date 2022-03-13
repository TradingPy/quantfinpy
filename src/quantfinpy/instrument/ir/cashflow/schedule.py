"""Interface for all instruments derived from a schedule of cashflows."""

from datetime import date
from typing import Iterable

from attr import attrs

from quantfinpy.data.cashflow.cashflow import Cashflow
from quantfinpy.data.cashflow.schedule import CashflowSchedule
from quantfinpy.instrument.instrument import Instrument


@attrs(slots=True, frozen=True, auto_attribs=True)
class CashflowScheduleInstrument(Instrument):
    """Instrument wrapping a schedule of cashflows."""

    scheduled_cashflows: CashflowSchedule
    """scheduled cashflows."""

    @classmethod
    def build_from_single_cashflow_definition(
        cls, cashflow_dates: Iterable[date], cashflow: Cashflow
    ) -> "CashflowScheduleInstrument":
        """
        Create instance of CashflowScheduleInstrument with the same cashflow being distributed at the specified dates.

        :param cashflow_dates: cashflow dates.
        :param cashflow: cashflow distributed at the different cashflow dates.
        :return: CashflowScheduleInstrument with same cashflow distributed at specified dates.

        Note:
            This interface is more friendly to create a CashflowScheduleInstrument with constant cashflow definition
            without knowing about the CashflowSchedule interface.

        """
        scheduled_cash_flows = CashflowSchedule.build_from_single_value_definition(
            cashflow_dates, cashflow
        )
        return cls(scheduled_cash_flows)
