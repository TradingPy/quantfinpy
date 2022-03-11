"""Fixed IR leg, i.e. schedule of cashflows associated to a fixed rate or multiple fixed rates."""

from attr import attrs

from quantfinpy.data.cashflow.cashflow import FixedRateCashflow
from quantfinpy.instrument.ir.cashflow.schedule import CashflowScheduleInstrument


@attrs(slots=True, frozen=True, auto_attribs=True)
class IRFixedLeg(CashflowScheduleInstrument):
    """IR Fixed leg, i.e. schedule of fixed rate cashflows."""

    def __attrs_post_init__(self) -> None:
        assert all(
            map(
                lambda cashflow: isinstance(cashflow, FixedRateCashflow),
                self.scheduled_cashflows.values,
            )
        )
