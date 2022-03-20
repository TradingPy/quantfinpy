"""Interface and definition of interest rate bond."""

from __future__ import annotations

from attr import attrs

from quantfinpy.data.cashflow.schedule import CashflowSchedule, schedule_maturity
from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.credit.instrument import CreditInstrument


@attrs(slots=True, frozen=True, auto_attribs=True, init=False)
class Bond(CreditInstrument):
    """Bond, i.e. schedule of coupon cashflows and repayment of notional at maturity."""

    coupon_cashflows: CashflowSchedule
    """scheduled coupon cashflows up to maturity."""

    def __init__(
        self,
        reference_entity: str,
        notional: float,
        currency: Currency,
        coupon_cashflows: CashflowSchedule,
    ) -> None:
        super().__init__(
            reference_entity, schedule_maturity(coupon_cashflows), notional, currency
        )
        object.__setattr__(self, "coupon_cashflows", coupon_cashflows)

    @classmethod
    def validate_value(cls, instrument_value: float) -> None:
        """
        Validate a specific bond value, i.e. checking positive.

        :param instrument_value: a bond value.
        """
        CreditInstrument.validate_value(instrument_value)
        assert (
            instrument_value >= 0.0
        ), f"A bond value is always positive, received {instrument_value}."
