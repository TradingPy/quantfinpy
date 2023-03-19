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
    """
    Interface for credit default swaps, i.e. swap an instrument whose value might be affected by a credit event.

    Example:
        >>> import pandas as pd
        >>> from quantfinpy.enum.currency import Currency
        >>> from quantfinpy.instrument.credit.bond import Bond
        >>> coupon_dates = (date(2023, 1, 1), date(2023, 4, 1), date(2023, 7, 1))
        >>> coupon_tenor = pd.DateOffset(months=3)
        >>> coupon_cashflow = FixedRateCashflow(1.0, Currency.USD, coupon_tenor, 0.01)
        >>> coupon_cashflows = CashflowSchedule.build_from_single_value_definition(coupon_dates, coupon_cashflow)
        >>> bond = Bond.create(
        ...     "Company",
        ...     1000000,
        ...     Currency.USD,
        ...     coupon_cashflows,
        ... )
        >>> # Building CDS as composition of a swapped credit instrument (here a bond) and the premium payment schedule.
        >>> payment_dates = coupon_dates
        >>> payment_tenor = coupon_tenor
        >>> cds_spread = 0.012
        >>> cds = CDS.create(cds_spread, bond, payment_dates, payment_tenor)
        >>>
        >>> all(map(lambda pair: pair[0] == pair[1], zip(cds.payment_dates, payment_dates)))
        True
        >>> cds.cds_spread
        0.012
        >>> cds.credit_instrument == bond
        True
        >>> cds.payment_tenor
        <DateOffset: months=3>
    """

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
        """
        Create CDS.

        :param cds_spread:
        :param credit_instrument:
        :param payment_dates:
        :param payment_tenor:
        :return: created CDS
        """
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
