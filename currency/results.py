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
