"""Interface and definition of interest rate bond."""

from datetime import date
from itertools import chain, repeat
from typing import Iterable, Iterator, Optional, Tuple

from attr import attrs
from cytoolz.itertoolz import last  # pylint: disable=no-name-in-module

from quantfinpy.data.ir.cashflow.cashflow import Cashflow
from quantfinpy.data.ir.cashflow.schedule import CashflowSchedule
from quantfinpy.instrument.ir.cashflow.schedule import CashflowScheduleInstrument
from quantfinpy.utils.itertools import is_empty


@attrs(slots=True, frozen=True, auto_attribs=True)
class IRBond(CashflowScheduleInstrument):
    """IR Bond, i.e. schedule of coupon cashflows and repayment of notional at maturity."""

    maturity: date
    """Bond's maturity."""
    repayment_cashflow: Cashflow
    """Bond's notional to be repaid at maturity."""

    def __attrs_post_init__(self) -> None:
        maturity, last_cashflow = last(self.scheduled_cashflows.schedule)
        assert maturity == self.maturity
        assert last_cashflow == self.repayment_cashflow

    @classmethod
    def build_explicit(
        cls,
        coupon_cashflow: Optional[Cashflow],
        coupon_dates: Iterable[date],
        maturity: date,
        repayment_cashflow: Cashflow,
    ) -> "IRBond":
        """
        Build an ir bond based on an explicit definition of its coupon cashflows and the notional repayment at maturity.

        :param coupon_cashflow: cashflow distributed at each coupon date up to maturity.
            Optional to support no coupon case.
        :param coupon_dates: coupon dates. Empty date iterable if there is no coupon.
        :param maturity: bond's maturity. Must be past or equal to last coupon date.
        :param repayment_cashflow: cashflow repaid at maturity of the bond.
        :return: ir bond derived from the provided information.
        """
        # Assert that the coupon cashflow is defined if there is at least 1 coupon date.
        if not is_empty(iter(coupon_dates)):
            assert coupon_cashflow is not None
            coupon_cashflows: Iterator[Tuple[date, Cashflow]] = map(
                lambda coupon_date: (coupon_date, coupon_cashflow), coupon_dates  # type: ignore
            )
        else:
            coupon_cashflows = ()  # type: ignore

        # Initialise the bond's cashflow schedule with the coupon cashflows and chain them with the repayment cashflow.
        cashflow_schedule: Iterator[Tuple[date, Cashflow]] = chain(
            coupon_cashflows,
            repeat((maturity, repayment_cashflow), 1),
        )
        return IRBond(
            CashflowSchedule(tuple(cashflow_schedule)), maturity, repayment_cashflow
        )
