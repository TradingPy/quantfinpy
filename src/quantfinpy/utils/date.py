"""Utils for dates."""

from datetime import date

from pandas import DateOffset, Timedelta


def timedelta_from_offset(offset: DateOffset, ref_date: date) -> Timedelta:
    """
    Derive timedelta from offset for a specific date.

    :param offset: date offset.
    :param ref_date: reference date.
    :return: time delta between d and d + offset.
    """
    return (ref_date + offset) - ref_date  # type: ignore


def offset_timedelta_div(
    offset: DateOffset, time_delta: Timedelta, ref_date: date
) -> float:
    """
    Divide offset by a timedelta.

    :param offset: date offset to be divided.
    :param time_delta: timedelta to divide the offset.
    :param ref_date: reference date.
    :return: fraction value.
    """
    return timedelta_from_offset(offset, ref_date) / time_delta
