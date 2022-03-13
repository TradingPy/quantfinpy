"""Interface for credit default swaps."""

from datetime import date
from typing import Iterable, Iterator

from attr import attrs

from quantfinpy.data.cashflow.cashflow import FixedRateCashflow
from quantfinpy.data.cashflow.schedule import CashflowSchedule
from quantfinpy.data.tenor import Tenor
from quantfinpy.instrument.credit.instrument import CreditInstrument
from quantfinpy.instrument.ir.cashflow.schedule import CashflowScheduleInstrument
from quantfinpy.instrument.portfolio import Position
from quantfinpy.instrument.swap import Swap


@attrs(slots=True, frozen=True, auto_attribs=True, init=False)
class CDS(Swap):
    """Interface for credit default swaps, i.e. swap an instrument whose value might be affected by a credit event."""

    cds_spread: float
    """CDS spread, i.e. the insurance premium."""

    def __init__(
        self,
        cds_spread: float,
        credit_instrument: CreditInstrument,
        payment_dates: Iterable[date],
        payment_tenor: Tenor,
    ):
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
        super().__init__(
            (Position(premium_cashflows, -1.0), Position(credit_instrument, 1.0))
        )
        object.__setattr__(self, "cds_spread", cds_spread)

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
    def payment_tenor(self) -> Tenor:
        """Cds premium payments' tenor."""
        first_premium_payment = next(self.premium_payments.values)
        assert isinstance(first_premium_payment, FixedRateCashflow)
        return first_premium_payment.tenor
