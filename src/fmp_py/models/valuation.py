from dataclasses import dataclass


@dataclass
class DiscountedCashFlow:
    symbol: str
    date: str
    dcf: float
    stock_price: float


@dataclass
class CompanyRating:
    symbol: str
    date: str
    rating: str
    rating_score: int
    rating_recommendation: str
    rating_details_dcf_score: int
    rating_details_dcf_recommendation: str
    rating_details_roe_score: int
    rating_details_roe_recommendation: str
    rating_details_roa_score: int
    rating_details_roa_recommendation: str
    rating_details_de_score: int
    rating_details_de_recommendation: str
    rating_details_pe_score: int
    rating_details_pe_recommendation: str
    rating_details_pb_score: int
    rating_details_pb_recommendation: str
