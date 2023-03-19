"""Interface and definition of interest rate bond."""

from __future__ import annotations

from attrs import define

from quantfinpy.data.cashflow.cashflow import ObservedCashflow
from quantfinpy.data.cashflow.schedule import CashflowSchedule, schedule_maturity
from quantfinpy.enum.currency import Currency
from quantfinpy.instrument.credit.instrument import CreditInstrument


@define(frozen=True)
class Bond(CreditInstrument):
    """
    Bond, i.e. schedule of coupon cashflows and repayment of notional at maturity.

    Example:
        >>> import pandas as pd
        >>> from datetime import date
        >>> from quantfinpy.data.cashflow.cashflow import FixedRateCashflow, ObservedCashflow
        >>> from quantfinpy.data.cashflow.schedule import CashflowSchedule
        >>>
        >>> # Building Bond as sequence of coupon cashflows + a cashflow for the repayment at maturity.
        >>> reference_entity: str = "Company"
        >>> coupon_dates = pd.date_range(start=date(2023, 1, 1), periods=2, freq="3M")
        >>> coupon_tenor = pd.DateOffset(months=3)
        >>> coupon_cashflow = FixedRateCashflow(1.0, Currency.USD, coupon_tenor, 0.01)
        >>> coupon_cashflows = CashflowSchedule.build_from_single_value_definition(coupon_dates, coupon_cashflow)
        >>> maturity = coupon_dates[-1] + coupon_tenor
        >>> repayment_coupon = ObservedCashflow(1.0, Currency.USD)
        >>> bond = Bond.create(
        ...     reference_entity,
        ...     repayment_coupon.notional,
        ...     repayment_coupon.currency,
        ...     coupon_cashflows,
        ... )
        >>> bond.coupon_cashflows == coupon_cashflows
        True
        >>> bond.maturity
        datetime.date(2023, 7, 30)
        >>> bond.repayment_cashflow
        ObservedCashflow(notional=1.0, currency=<Currency.USD: 1>)
        >>> bond.reference_entity
        'Company'
    """

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
        """
        Create bond instrument according to the specified cashflows.

        :param reference_entity:
        :param notional:
        :param currency:
        :param coupon_cashflows:
        :return: created bond
        """
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
