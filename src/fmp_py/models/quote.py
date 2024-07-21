from dataclasses import dataclass


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
