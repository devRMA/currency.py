from datetime import datetime

from dataclasses import dataclass

from currency.currencies import CurrencyEnum


@dataclass
class CurrencyResult:
    """
    Class for storing currency result

    Attributes
    ----------
    currency: `CurrencyEnum`
        Currency base
    currency_to: `CurrencyEnum`
        Currency to
    name: `str`
        Currency exchange name
    high: `float`
        The highest price
    low: `float`
        The lowest price
    variation: `float`
        The variation of the price
    variation_percent: `float`
        The variation percentage of the price
    buy: `float`
        The buy price
    sell: `float`
        The sell price
    timestamp: `int`
        The timestamp of the price update
    updated_at: `datetime`
        An alias to `timestamp` but in `datetime` format
    """
    currency: CurrencyEnum
    currency_to: CurrencyEnum
    name: str
    high: float
    low: float
    variation: float
    variation_percentage: float
    buy: float
    sell: float
    timestamp: int
    updated_at: datetime

    def __eq__(self, other: object) -> bool:
        if isinstance(other, CurrencyResult):
            return all(
                [
                    self.currency == other.currency,
                    self.currency_to == other.currency_to,
                    self.timestamp == other.timestamp
                ]
            )
        return False

    def __lt__(self, other: object) -> bool:
        if isinstance(other, CurrencyResult):
            return self.sell < other.sell
        return False

    def __le__(self, other: object) -> bool:
        if isinstance(other, CurrencyResult):
            return self.sell <= other.sell
        return False

    def __str__(self) -> str:
        return f'{self.currency} -> {self.currency_to}: {self.sell}'

    def __float__(self) -> float:
        return self.sell
