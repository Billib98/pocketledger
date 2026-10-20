from datetime import date
from decimal import Decimal

from pocketledger.ledger import Ledger, Transaction
from pocketledger.report import by_category, monthly_summary


def tx(day, amount, category):
    return Transaction(day=day, amount=Decimal(amount), category=category)


def test_monthly_summary_mid_month():
    ledger = Ledger()
    ledger.add(tx(date(2026, 3, 10), "200", "stipendio"))
    ledger.add(tx(date(2026, 3, 12), "-50", "spesa"))
    result = monthly_summary(ledger, 2026, 3)
    assert result == {
        "income": Decimal("200"),
        "expenses": Decimal("50"),
        "net": Decimal("150"),
    }


def test_monthly_summary_ignores_other_months():
    ledger = Ledger()
    ledger.add(tx(date(2026, 2, 10), "-20", "spesa"))
    ledger.add(tx(date(2026, 4, 10), "-30", "spesa"))
    result = monthly_summary(ledger, 2026, 3)
    assert result["expenses"] == Decimal("0")


def test_by_category_totals():
    ledger = Ledger()
    ledger.add(tx(date(2026, 3, 1), "-10", "spesa"))
    ledger.add(tx(date(2026, 3, 2), "-5", "spesa"))
    ledger.add(tx(date(2026, 3, 3), "100", "stipendio"))
    assert by_category(ledger) == {
        "spesa": Decimal("-15"),
        "stipendio": Decimal("100"),
    }
