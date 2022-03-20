"""Interface for bond option."""

from attr import attrs

from quantfinpy.instrument.credit.bond import Bond
from quantfinpy.instrument.option import Option


@attrs(slots=True, frozen=True, auto_attribs=True)
class BondOption(Option[Bond]):
    """Option whose underlying is a bond."""

    # TODO: might need to check that strike is within some specific bounds and maturity during the lifetime of the bond.
