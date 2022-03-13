"""Utils for abstract interfaces."""

from typing import Type, TypeVar

AbstractClass = TypeVar("AbstractClass")
DerivedClass = TypeVar("DerivedClass")


def abstract_interface(abstract_class: Type[AbstractClass]) -> Type[AbstractClass]:
    """
    Class decorator for pure abstract interfaces.

    Adding __new__ function which prevents direct instantiation.

    :param abstract_class: class to be decorated.
    :return: decorated class.
    """
    # pylint: disable=unused-argument
    def __new__(cls: Type[DerivedClass], *args, **kwargs) -> DerivedClass:  # type: ignore
        if cls is abstract_class:
            raise TypeError(f"only children of '{cls.__name__}' may be instantiated.")
        return object.__new__(cls)

    setattr(abstract_class, "__new__", __new__)
    return abstract_class
