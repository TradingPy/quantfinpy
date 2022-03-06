"""Interfaces for tenors."""

import sys

import pandas as pd

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

Tenor: TypeAlias = pd.DateOffset
"""Tenor as an alias of pandas.DateOffset which supports the different temporal units."""
