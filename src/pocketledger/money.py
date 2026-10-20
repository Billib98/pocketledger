"""Gestione degli importi con Decimal (mai float per i soldi)."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

CENT = Decimal("0.01")


def parse_amount(text: str) -> Decimal:
    """Converte una stringa come '12,50' o '12.50' in Decimal a 2 decimali.

    Solleva ValueError se il testo non è un importo valido.
    """
    cleaned = text.strip().replace(",", ".")
    if not cleaned:
        raise ValueError("importo vuoto")
    try:
        value = Decimal(cleaned)
    except InvalidOperation as exc:
        raise ValueError(f"importo non valido: {text!r}") from exc
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def format_amount(value: Decimal) -> str:
    """Formatta un importo come '1234.50' (due decimali, punto)."""
    return f"{value.quantize(CENT, rounding=ROUND_HALF_UP):.2f}"
