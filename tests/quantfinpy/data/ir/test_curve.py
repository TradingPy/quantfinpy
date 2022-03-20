"""Test cases for IR curves."""

from pandas import DateOffset

from quantfinpy.data.ir.curve import IRForwardCurveId
from quantfinpy.enum.currency import Currency
from quantfinpy.enum.ir_index import InterestRateIndex


def test_ir_forward_curve_id_ctor(
    default_currency: Currency,
    default_ir_index: InterestRateIndex,
    default_tenor: DateOffset,
):
    # Building the ir fwd curve id.
    ir_fwd_curve_id = IRForwardCurveId(
        default_currency, default_ir_index, default_tenor
    )

    # Checking the built curve id.
    assert isinstance(ir_fwd_curve_id, IRForwardCurveId)
    assert ir_fwd_curve_id.currency == default_currency
    assert ir_fwd_curve_id.tenor == default_tenor
    assert ir_fwd_curve_id.index == default_ir_index
