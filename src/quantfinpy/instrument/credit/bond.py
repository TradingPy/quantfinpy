"""Interface and definition of interest rate bond."""

from __future__ import annotations

from attrs import define

from quantfinpy.data.cashflow.cashflow import ObservedCashflow
from quantfinpy.data.cashflow.schedule import CashflowSchedule, schedule_maturity
from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.credit.instrument import CreditInstrument


@define(frozen=True)
class Bond(CreditInstrument):
    """Bond, i.e. schedule of coupon cashflows and repayment of notional at maturity."""

    coupon_cashflows: CashflowSchedule
    """scheduled coupon cashflows up to maturity."""

    @classmethod
    def create(
        cls,
        reference_entity: str,
        notional: float,
        currency: Currency,
        coupon_cashflows: CashflowSchedule,
    ) -> "Bond":
        return cls(
            reference_entity,
            schedule_maturity(coupon_cashflows),
            ObservedCashflow(notional, currency),
            coupon_cashflows,
        )

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
