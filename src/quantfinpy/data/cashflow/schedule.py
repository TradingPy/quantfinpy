"""Cashflow schedule interface and specialisations."""

import sys

from quantfinpy.data.cashflow.cashflow import Cashflow
from quantfinpy.utils.schedule import ScheduledValues

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

CashflowSchedule: TypeAlias = ScheduledValues[Cashflow]
"""Schedule, i.e. timeseries, of cashflows."""
