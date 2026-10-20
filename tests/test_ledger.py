from datetime import date
from decimal import Decimal

import pytest

from pocketledger.ledger import Ledger, Transaction


def make(day, amount, category="varie"):
    return Transaction(day=day, amount=Decimal(amount), category=category)


def test_balance_sums_income_and_expenses():
    ledger = Ledger()
    ledger.add(make(date(2026, 1, 5), "100.00"))
    ledger.add(make(date(2026, 1, 6), "-30.25"))
    assert ledger.balance() == Decimal("69.75")


def test_all_is_sorted_by_date():
    ledger = Ledger()
    ledger.add(make(date(2026, 2, 1), "1"))
    ledger.add(make(date(2026, 1, 1), "2"))
    assert [t.day for t in ledger.all()] == [date(2026, 1, 1), date(2026, 2, 1)]


def test_zero_amount_rejected():
    with pytest.raises(ValueError):
        Ledger().add(make(date(2026, 1, 1), "0"))
