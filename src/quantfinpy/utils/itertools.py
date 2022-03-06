"""Utils for iterators and iterables."""

from typing import Iterator, TypeVar

IteratorValueType = TypeVar("IteratorValueType")


def is_empty(iterator: Iterator[IteratorValueType]) -> bool:
    """
    Check whether provided iterator is empty.

    :param iterator: iterator whose emptiness is to be checked.
    :return: flag indicating if the provided iterator is empty.
    """
    return not any(map(lambda el: True, iterator))
