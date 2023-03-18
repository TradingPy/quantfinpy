"""Interface for bond option."""

from attrs import define

from quantfinpy.instrument.credit.bond import Bond
from quantfinpy.instrument.option import Option


@define(frozen=True)
class BondOption(Option[Bond]):
    """Option whose underlying is a bond."""

    # TODO: might need to check that strike is within some specific bounds and maturity during the lifetime of the bond.
