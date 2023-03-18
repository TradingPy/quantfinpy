"""Floating IR leg, i.e. schedule of cashflows associated to a floating rate or multiple floating rates."""

from attrs import define

from quantfinpy.data.cashflow.cashflow import FloatingRateCashflow
from quantfinpy.instrument.cashflow.schedule import CashflowScheduleInstrument


@define(frozen=True)
class IRFloatingLeg(CashflowScheduleInstrument):
    """IR Floating leg, i.e. schedule of floating rate cashflows."""

    def __attrs_post_init__(self) -> None:
        assert all(
            map(
                lambda cashflow: isinstance(cashflow, FloatingRateCashflow),
                self.scheduled_cashflows.values,
            )
        )
