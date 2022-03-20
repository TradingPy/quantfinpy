"""Interfaces for data objects, ids and sets."""

from typing import Callable, ClassVar, Mapping, Type, TypeVar

from attr import attrs


@attrs(slots=True, frozen=True, auto_attribs=True)
class Data:
    """Interface for a data object."""


@attrs(slots=True, frozen=True, auto_attribs=True)
class DataId:
    """Identify a data object."""

    data_class: ClassVar[Type[Data]] = Data


DecoratedDataIdType = TypeVar("DecoratedDataIdType", bound=Type[DataId])


def map_data_class(
    data_type: Type[Data],
) -> Callable[[DecoratedDataIdType], DecoratedDataIdType]:
    """
    Decorate data id classes with their associated data type.

    :param data_type: data class to be associated to the wrapped data id classes.
    :return: data id class decorator.
    """

    def wrapper(data_id_class: DecoratedDataIdType) -> DecoratedDataIdType:
        setattr(data_id_class, "data_class", data_type)
        return data_id_class

    return wrapper


@attrs(slots=True, frozen=True, auto_attribs=True)
class DataSet:
    """Mapping between data ids and data objects."""

    mapping: Mapping[DataId, Data]
    """Id to object mapping."""

    def __attrs_post_init__(self) -> None:
        for data_id, data in self.mapping.items():
            assert isinstance(data, data_id.data_class)

    # TODO: support strongly typed get.
    def __getitem__(self, data_id: DataId) -> Data:
        return self.mapping[data_id]
