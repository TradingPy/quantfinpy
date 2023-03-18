"""Interface for basic credit instrument."""

from datetime import date

from attrs import define

from quantfinpy.data.cashflow.cashflow import ObservedCashflow
from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.instrument import Instrument


@define(frozen=True)
class CreditInstrument(Instrument):
    """Basic instrument underlying most credit instruments, similar to loan from a specific reference entity."""

    reference_entity: str
    """reference entity."""
    maturity: date
    """maturity."""
    repayment_cashflow: ObservedCashflow
    """cashflow repaid at maturity."""

    @property
    def notional(self) -> float:
        """Get instrument's notional."""
        return self.repayment_cashflow.notional

    @property
    def currency(self) -> Currency:
        """Get instrument's currency."""
        return self.repayment_cashflow.currency
