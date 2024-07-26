from dataclasses import dataclass


@dataclass
class UpgradesDowngrades:
    symbol: str
    strong_buy: int
    buy: int
    hold: int
    sell: int
    strong_sell: int
    consensus: str
