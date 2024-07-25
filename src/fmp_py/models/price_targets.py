from dataclasses import dataclass
from typing import List


@dataclass
class PriceTargetConsensus:
    symbol: str
    target_high: float
    target_low: float
    target_consensus: float
    target_median: float


@dataclass
class PriceTargetSummary:
    symbol: str
    last_month: int
    last_month_avg_price_target: float
    last_quarter: int
    last_quarter_avg_price_target: float
    last_year: int
    last_year_avg_price_target: float
    all_time: int
    all_time_avg_price_target: float
    publishers: List[str]
