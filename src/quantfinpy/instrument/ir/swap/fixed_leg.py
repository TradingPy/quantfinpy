"""Fixed IR leg, i.e. schedule of cashflows associated to a fixed rate or multiple fixed rates."""

from typing import Iterable
from datetime import date
from attr import attrs

from quantfinpy.instrument.spot import SpotInstrument
from quantfinpy.data.ir.cashflow import FixedRateCashflow
from quantfinpy.data.ir.cashflow_schedule import (
    CashflowSchedule,
    DuplicatedCashflowSchedule,
)


@attrs(slots=True, frozen=True, auto_attribs=True)
class IRFixedLeg(SpotInstrument):
    """IR Fixed leg, i.e. schedule of fixed rate cashflows."""

    cashflows: CashflowSchedule
    """Fixed rate cashflows per date."""

    def __attrs_post_init__(self) -> None:
        assert all(
            map(
                lambda cashflow: isinstance(cashflow, FixedRateCashflow),
                self.cashflows.cashflows,
            )
        )

    @classmethod
    def build_unique_cashflow_definition(
        cls, cashflow_dates: Iterable[date], cashflow: FixedRateCashflow
    ) -> "IRFixedLeg":
        """
        Create instance of IRFixedLeg with same fixed rate cashflows being distributed at the specified dates.

        :param cashflow_dates: cashflow dates.
        :param cashflow: cashflow distributed at the different cashflow dates.
        :return: ir fixed leg with same fixed rate cashflow distributed at specified dates.

        Note:
            this interface is more friendly to create an ir fixed leg with constant cashflow definition without knowing
            about the different schedules.
        """
        leg_cash_flows = DuplicatedCashflowSchedule(cashflow_dates, cashflow)
        return cls(leg_cash_flows)
