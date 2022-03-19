"""Utils for iterators and iterables."""

from typing import Any, Iterable


def is_empty(iterable: Iterable[Any]) -> bool:
    """
    Check whether provided iterable is empty.

    :param iterable: iterable whose emptiness is to be checked.
    :return: flag indicating if the provided iterable is empty.
    """
    return not any(map(lambda el: True, iterable))
