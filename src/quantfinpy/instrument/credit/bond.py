"""Interface and definition of interest rate bond."""

from __future__ import annotations

from datetime import date

from attr import attrs
from cytoolz.itertoolz import last  # pylint: disable=no-name-in-module

from quantfinpy.data.cashflow.schedule import CashflowSchedule
from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.credit.instrument import CreditInstrument


@attrs(slots=True, frozen=True, auto_attribs=True, init=False)
class Bond(CreditInstrument):
    """Bond, i.e. schedule of coupon cashflows and repayment of notional at maturity."""

    coupon_cashflows: CashflowSchedule
    """schedule coupon cashflows up to maturity."""

    def __init__(
        self,
        reference_entity: str,
        maturity: date,
        notional: float,
        currency: Currency,
        coupon_cashflows: CashflowSchedule,
    ) -> None:
        super().__init__(reference_entity, maturity, notional, currency)
        object.__setattr__(self, "coupon_cashflows", coupon_cashflows)

        coupon_date, _ = last(self.coupon_cashflows.schedule)
        assert coupon_date <= self.maturity
