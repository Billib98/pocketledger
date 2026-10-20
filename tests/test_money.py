from decimal import Decimal

import pytest

from pocketledger.money import format_amount, parse_amount


def test_parse_with_comma():
    assert parse_amount("12,50") == Decimal("12.50")


def test_parse_with_dot_and_spaces():
    assert parse_amount("  7.5 ") == Decimal("7.50")


def test_parse_rounds_half_up():
    assert parse_amount("1.005") == Decimal("1.01")


def test_parse_empty_raises():
    with pytest.raises(ValueError):
        parse_amount("   ")


def test_parse_garbage_raises():
    with pytest.raises(ValueError):
        parse_amount("abc")


def test_format_two_decimals():
    assert format_amount(Decimal("3")) == "3.00"
