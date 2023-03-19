"""Interface for bond option."""

from attrs import define

from quantfinpy.instrument.credit.bond import Bond
from quantfinpy.instrument.option import Option


@define(frozen=True)
class BondOption(Option[Bond]):
    """
    Option whose underlying is a bond.

    Example:
        >>> from datetime import date
        >>> import pandas as pd
        >>> from quantfinpy.enum.currency import Currency
        >>> from quantfinpy.instrument.option import OptionExerciseType, OptionSide
        >>> from quantfinpy.data.cashflow.cashflow import FixedRateCashflow, ObservedCashflow
        >>> from quantfinpy.data.cashflow.schedule import CashflowSchedule
        >>> # Building Bond Option as option on bond for a realistic strike and the maturity
        >>> # at the start of the bond.
        >>> coupon_dates = (date(2023, 1, 1), date(2023, 4, 1), date(2023, 7, 1))
        >>> coupon_tenor = pd.DateOffset(months=3)
        >>> coupon_cashflow = FixedRateCashflow(1.0, Currency.USD, coupon_tenor, 0.01)
        >>> coupon_cashflows = CashflowSchedule.build_from_single_value_definition(coupon_dates,
        ...     coupon_cashflow)
        >>> bond = Bond.create(
        ...     "Company",
        ...     1000000,
        ...     Currency.USD,
        ...     coupon_cashflows,
        ... )
        >>> option_side, exercise, strike = OptionSide.CALL, OptionExerciseType.EUROPEAN, 90.0
        >>> option_maturity: date = date(2023, 2, 1)
        >>> option = BondOption(bond, option_side, exercise, strike, option_maturity)
        >>> option.side.name
        'CALL'
        >>> option.strike
        90.0
        >>> option.maturity
        datetime.date(2023, 2, 1)
        >>> option.underlying == bond
        True
        >>> option.exercise_type.name
        'EUROPEAN'

    """

    # TODO: might need to check that strike is within some specific bounds and maturity during the lifetime of the bond.
