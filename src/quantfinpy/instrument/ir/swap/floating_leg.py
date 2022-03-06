"""Floating IR leg, i.e. schedule of cashflows associated to a floating rate or multiple floating rates."""

from typing import Iterable
from datetime import date
from attr import attrs

from quantfinpy.instrument.instrument import Instrument
from quantfinpy.data.ir.cashflow import FloatingRateCashflow
from quantfinpy.data.ir.cashflow_schedule import (
    CashflowSchedule,
    DuplicatedCashflowSchedule,
)


@attrs(slots=True, frozen=True, auto_attribs=True)
class IRFloatingLeg(Instrument):
    """IR Floating leg, i.e. schedule of floating rate cashflows."""

    cashflows: CashflowSchedule
    """Floating rate cashflows per date."""

    def __attrs_post_init__(self) -> None:
        assert all(
            map(
                lambda cashflow: isinstance(cashflow, FloatingRateCashflow),
                self.cashflows.cashflows,
            )
        )

    @classmethod
    def build_unique_cashflow_definition(
        cls, cashflow_dates: Iterable[date], cashflow: FloatingRateCashflow
    ) -> "IRFloatingLeg":
        """
        Create instance of IRFixedLeg with same floating rate cashflows being distributed at the specified dates.

        :param cashflow_dates: cashflow dates.
        :param cashflow: cashflow distributed at the different cashflow dates.
        :return: ir floating leg with same floating rate cashflow distributed at specified dates.

        Note:
            this interface is more friendly to create an ir floating leg with constant cashflow definition without
            knowing about the different schedules.
        """
        leg_cash_flows = DuplicatedCashflowSchedule(cashflow_dates, cashflow)
        return cls(leg_cash_flows)
