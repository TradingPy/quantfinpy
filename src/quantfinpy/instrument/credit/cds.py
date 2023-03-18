"""Interface for credit default swaps."""

from datetime import date
from typing import Iterator, Sequence

from attrs import define
from pandas import DateOffset

from quantfinpy.data.cashflow.cashflow import FixedRateCashflow
from quantfinpy.data.cashflow.schedule import CashflowSchedule
from quantfinpy.instrument.cashflow.schedule import CashflowScheduleInstrument
from quantfinpy.instrument.credit.instrument import CreditInstrument
from quantfinpy.instrument.portfolio import Position
from quantfinpy.instrument.swap import Swap


@define(frozen=True)
class CDS(Swap):
    """Interface for credit default swaps, i.e. swap an instrument whose value might be affected by a credit event."""

    cds_spread: float
    """CDS spread, i.e. the insurance premium."""

    # TODO: derive payment tenor from payment dates assuming that tenor between dates is constant.
    @classmethod
    def create(
        cls,
        cds_spread: float,
        credit_instrument: CreditInstrument,
        payment_dates: Sequence[date],
        payment_tenor: DateOffset,
    ) -> "CDS":
        assert payment_dates[-1] <= credit_instrument.maturity, (
            f"Last payment date {payment_dates[-1]} is past the maturity of the underlying credit instrument "
            f"{credit_instrument.maturity}."
        )

        premium_cashflow = FixedRateCashflow(
            credit_instrument.notional,
            credit_instrument.currency,
            payment_tenor,
            cds_spread,
        )
        premium_cashflows = (
            CashflowScheduleInstrument.build_from_single_cashflow_definition(
                payment_dates, premium_cashflow
            )
        )
        return cls(
            (Position(premium_cashflows, -1.0), Position(credit_instrument, 1.0)),
            cds_spread,
        )

    @property
    def credit_instrument(self) -> CreditInstrument:
        """Credit instrument whose credit risk is to be swapped via the cds."""
        credit_instrument = self.positions[1].instrument
        assert isinstance(credit_instrument, CreditInstrument)
        return credit_instrument

    @property
    def premium_payments(self) -> CashflowSchedule:
        """Cds premium payments."""
        premium_payments = self.positions[0].instrument
        assert isinstance(premium_payments, CashflowScheduleInstrument)
        return premium_payments.scheduled_cashflows

    @property
    def payment_dates(self) -> Iterator[date]:
        """Cds premium payment dates."""
        return self.premium_payments.dates

    @property
    def payment_tenor(self) -> DateOffset:
        """Cds premium payments' tenor."""
        first_premium_payment = next(self.premium_payments.values)
        assert isinstance(first_premium_payment, FixedRateCashflow)
        return first_premium_payment.tenor
