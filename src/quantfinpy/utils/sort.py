"""Utils related to sorting."""

from typing import Callable, Iterator, Optional, TypeVar

ElementType = TypeVar("ElementType")


def assert_sorted_iterator(
    iterator: Iterator[ElementType], increasing: bool = True
) -> None:
    """
    Assert that the provided iterator is sorted in the specified order, increasing or decreasing.

    :param iterator: iterator.
    :param increasing: flag to indicate if the checked order should be increasing.

    Note:
        Could check that the comparison operators are available via operator protocols.

    """
    previous_element: Optional[ElementType] = None
    comparison_check: Callable[[ElementType], bool] = (
        (lambda new_element: previous_element <= new_element)  # type: ignore
        if increasing
        else (lambda new_element: previous_element >= new_element)  # type: ignore
    )

    for element in iterator:
        if previous_element is not None:
            assert comparison_check(
                element
            ), f"new element {element} after {previous_element} doesn't follow the expect sort."
        previous_element = element
