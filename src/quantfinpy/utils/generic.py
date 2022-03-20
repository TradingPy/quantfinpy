"""Utils for python generic classes."""

from typing import Tuple, get_args, get_origin


def find_generic_specialization_parent_class(cls: type, generic_class: type) -> type:
    """
    Find the parent class of class cls which is a specialization of the specified generic class.

    :param cls: class which derives from a specialization of generic class.
    :param generic_class: a generic class.
    :return: generic specialization.

    """

    def valid_origin(base: type) -> bool:
        # TODO: check that the generic types of base match the generic types of generic class.
        return issubclass(get_origin(base), generic_class)  # type: ignore

    return next(filter(valid_origin, cls.__orig_bases__))  # type: ignore


def identify_generic_specialization_types(
    cls: type, generic_class: type
) -> Tuple[type, ...]:
    """
    Identify the types of the specialization of generic class the class cls derives from.

    :param cls: class which derives from a specialization of generic class.
    :param generic_class: a generic class.
    :return: specialization types.
    """
    return get_args(find_generic_specialization_parent_class(cls, generic_class))
