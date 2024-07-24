from fmp_py.fmp_base import FmpBase
import os
from dotenv import load_dotenv

from fmp_py.models.valuation import CompanyRating

load_dotenv()


"""
FmpValuation class inherits from FmpBase.
This class is used to interact with the Financial Modeling Prep API to retrieve valuation data.
https://site.financialmodelingprep.com/developer/docs#valuation

def company_rating(self, symbol: str) -> CompanyRating:
    Reference: https://site.financialmodelingprep.com/developer/docs#company-rating-company-information
"""


class FmpValuation(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")):
        super().__init__(api_key)

    def company_rating(self, symbol: str) -> CompanyRating:
        url = f"v3/rating/{symbol}"
        params = {"apikey": self.api_key}

        try:
            response = self.get_request(url, params)[0]
        except IndexError:
            raise ValueError("No data found in API response")

        data_dict = {
            "symbol": str(response.get("symbol")),
            "date": str(response.get("date")),
            "rating": str(response.get("rating")),
            "rating_score": int(response.get("ratingScore")),
            "rating_recommendation": str(response.get("ratingRecommendation")),
            "rating_details_dcf_score": int(response.get("ratingDetailsDCFScore")),
            "rating_details_dcf_recommendation": str(
                response.get("ratingDetailsDCFRecommendation")
            ),
            "rating_details_roe_score": int(response.get("ratingDetailsROEScore")),
            "rating_details_roe_recommendation": str(
                response.get("ratingDetailsROERecommendation")
            ),
            "rating_details_roa_score": int(response.get("ratingDetailsROAScore")),
            "rating_details_roa_recommendation": str(
                response.get("ratingDetailsROARecommendation")
            ),
            "rating_details_de_score": int(response.get("ratingDetailsDEScore")),
            "rating_details_de_recommendation": str(
                response.get("ratingDetailsDERecommendation")
            ),
            "rating_details_pe_score": int(response.get("ratingDetailsPEScore")),
            "rating_details_pe_recommendation": str(
                response.get("ratingDetailsPERecommendation")
            ),
            "rating_details_pb_score": int(response.get("ratingDetailsPBScore")),
            "rating_details_pb_recommendation": str(
                response.get("ratingDetailsPBRecommendation")
            ),
        }

        return CompanyRating(**data_dict)
