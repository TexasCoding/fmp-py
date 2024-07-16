from dataclasses import dataclass


@dataclass
class CompanyProfile:
    symbol: str
    price: float
    beta: float
    vol_avg: int
    mkt_cap: int
    last_div: float
    range: str
    changes: float
    company_name: str
    currency: str
    cik: str
    isin: str
    cusip: str
    exchange: str
    exchange_short_name: str
    industry: str
    website: str
    description: str
    ceo: str
    sector: str
    country: str
    full_time_employees: str
    phone: str
    address: str
    city: str
    state: str
    zip: str
    dcf_iff: float
    dcf: float
    image: str
    ipo_date: str
    default_image: bool
    is_etf: bool
    is_actively_trading: bool
    is_adr: bool
    is_fund: bool
