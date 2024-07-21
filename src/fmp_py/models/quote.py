from dataclasses import dataclass


@dataclass
class AftermarketQuote:
    symbol: str
    ask: float
    bid: float
    asize: float
    bsize: int
    timestamp: str


@dataclass
class AftermarketTrade:
    symbol: str
    price: float
    size: int
    timestamp: str


@dataclass
class PriceChange:
    symbol: str
    day_1: float
    day_5: float
    month_1: float
    month_3: float
    month_6: float
    ytd: float
    year_1: float
    year_3: float
    year_5: float
    year_10: float
    max: float


@dataclass
class OtcQuote:
    prev_close: float
    high: float
    low: float
    open: float
    volume: int
    last_sale_price: float
    fmp_last: float
    last_updated: str
    symbol: str


@dataclass
class SimpleQuote:
    symbol: str
    price: float
    volume: int


@dataclass
class Quote:
    symbol: str
    name: str
    price: float
    change_percentage: float
    change: float
    day_low: float
    day_high: float
    year_low: float
    year_high: float
    market_cap: int
    price_avg_50: float
    price_avg_200: float
    volume: int
    avg_volume: int
    exchange: str
    open: float
    previous_close: float
    eps: float
    pe: float
    earnings_date: str
    shares_outstanding: int
    timestamp: str
