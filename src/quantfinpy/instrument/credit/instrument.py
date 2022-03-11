"""Interface for basic credit instrument."""

from datetime import date

from attr import attrs

from quantfinpy.data.cashflow.cashflow import Cashflow
from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.instrument import Instrument


@attrs(slots=True, frozen=True, auto_attribs=True, init=False)
class CreditInstrument(Instrument):
    """Basic instrument underlying most credit instruments, similar to loan from a specific reference entity."""

    reference_entity: str
    """reference entity."""
    maturity: date
    """maturity."""
    repayment_cashflow: Cashflow
    """cashflow repaid at maturity."""

    def __init__(
        self, reference_entity: str, maturity: date, notional: float, currency: Currency
    ):
        object.__setattr__(self, "reference_entity", reference_entity)
        object.__setattr__(self, "maturity", maturity)
        object.__setattr__(self, "repayment_cashflow", Cashflow(notional, currency))

    @property
    def notional(self) -> float:
        """Get instrument's notional."""
        return self.repayment_cashflow.notional

    @property
    def currency(self) -> Currency:
        """Get instrument's currency."""
        return self.repayment_cashflow.currency
