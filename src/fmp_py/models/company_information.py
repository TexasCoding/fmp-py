from dataclasses import dataclass


@dataclass
class StockPeers:
    symbol: str
    peers_list: list[str]


@dataclass
class CompanyCoreInfo:
    cik: str
    symbol: str
    exchange: str
    sic_code: str
    sic_group: str
    sic_description: str
    state_location: str
    state_of_incorporation: str
    fiscal_year_end: str
    business_address: str
    mailing_address: str
    tax_idenfication_number: str
    registrant_name: str


@dataclass
class CompanyMarketCap:
    symbol: str
    market_cap: int
    date: str


@dataclass
class ExecutiveCompensation:
    symbol: str
    cik: str
    company_name: str
    industry: str
    accepted_date: str
    filing_date: str
    name_and_position: str
    year: str
    salary: float
    bonus: float
    stock_award: float
    incentive_plan_compensation: float
    all_other_compensation: float
    total: float
    url: str


@dataclass
class CompanyProfile:
    symbol: str
    price: float
    beta: float
    vol_avg: int
    mkt_cap: int
    last_div: int
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
    full_time_employees: int
    phone: str
    address: str
    city: str
    state: str
    zip: str
    dcf_diff: float
    dcf: float
    image: str
    ipo_date: str
    default_image: bool
    is_etf: bool
    is_actively_trading: bool
    is_adr: bool
    is_fund: bool
