"""Test cases for itertools utils."""

from typing import Any, Iterable, Type

import numpy as np
import pandas as pd
import pytest

from quantfinpy.utils.itertools import is_empty


@pytest.mark.parametrize(
    "iterable_type", [list, set, tuple, dict, np.array, pd.Series, pd.DataFrame]
)
def test_is_empty(iterable_type: Type[Iterable[Any]]):
    empty_iterable = iterable_type(())
    assert is_empty(empty_iterable)
    assert is_empty(iter(empty_iterable))

    non_empty_iterable = iterable_type(((1, 2),))
    assert not is_empty(non_empty_iterable)
    assert not is_empty(iter(non_empty_iterable))
