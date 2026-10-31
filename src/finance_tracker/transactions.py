"""Transaction domain model and operations for the final project."""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class Transaction:
    date: date
    description: str
    amount: Decimal
    category: str
    kind: str  # "income" or "expense"


def balance(transactions: list[Transaction]) -> Decimal:
    """Return income minus expenses."""
    raise NotImplementedError("Complete the final project")
