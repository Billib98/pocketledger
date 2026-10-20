"""Riepiloghi sui movimenti."""

import calendar
from collections import defaultdict
from datetime import date
from decimal import Decimal

from .ledger import Ledger


def monthly_summary(ledger: Ledger, year: int, month: int) -> dict[str, Decimal]:
    """Totali di entrate e spese per il mese indicato.

    Restituisce {'income': ..., 'expenses': ..., 'net': ...}; le spese sono
    riportate come numero positivo.
    """
    first = date(year, month, 1)
    last = date(year, month, calendar.monthrange(year, month)[1])

    income = Decimal("0")
    expenses = Decimal("0")
    for tx in ledger.all():
        if first <= tx.day < last:
            if tx.amount > 0:
                income += tx.amount
            else:
                expenses += -tx.amount
    return {"income": income, "expenses": expenses, "net": income - expenses}


def by_category(ledger: Ledger) -> dict[str, Decimal]:
    """Somma degli importi per categoria (spese negative, entrate positive)."""
    totals: dict[str, Decimal] = defaultdict(Decimal)
    for tx in ledger.all():
        totals[tx.category] += tx.amount
    return dict(totals)
