"""Floating IR leg, i.e. schedule of cashflows associated to a floating rate or multiple floating rates."""

from attr import attrs

from quantfinpy.data.ir.cashflow import FloatingRateCashflow
from quantfinpy.instrument.ir.cashflow.schedule import CashflowScheduleInstrument


@attrs(slots=True, frozen=True, auto_attribs=True)
class IRFloatingLeg(CashflowScheduleInstrument):
    """IR Floating leg, i.e. schedule of floating rate cashflows."""

    def __attrs_post_init__(self) -> None:
        assert all(
            map(
                lambda cashflow: isinstance(cashflow, FloatingRateCashflow),
                self.scheduled_cashflows.values,
            )
        )
