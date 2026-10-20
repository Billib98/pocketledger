"""Registro dei movimenti."""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class Transaction:
    day: date
    amount: Decimal  # positivo = entrata, negativo = spesa
    category: str
    note: str = ""


class Ledger:
    def __init__(self) -> None:
        self._items: list[Transaction] = []

    def add(self, tx: Transaction) -> None:
        if tx.amount == 0:
            raise ValueError("un movimento non può avere importo zero")
        self._items.append(tx)

    def all(self) -> list[Transaction]:
        return sorted(self._items, key=lambda t: t.day)

    def balance(self) -> Decimal:
        return sum((t.amount for t in self._items), Decimal("0"))
