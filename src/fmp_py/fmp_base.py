import os
from dotenv import load_dotenv
import requests

load_dotenv()
FMP_API_KEY = os.getenv("FMP_API_KEY", "")

FMP_BASE_URL = "https://financialmodelingprep.com/api/"
FMP_DAILY_HISTORY = "v3/historical-price-full/"
FMP_INTRADAY_HISTORY = "v3/historical-chart/"
# FMP_COMPANY_PROFILE = "v3/company/profile/"
# FMP_EXECUTIVE_COMPENSATION = "v4/governance/executive_compensation"
# FMP_COMPENSATION_BENCHMARK = "v4/executive-compensation-benchmark"
# FMP_COMPANY_NOTES = "v4/company-notes"
# FMP_EMPLOYEE_COUNT = "v4/historical/employee_count"


class FmpBase:
    def __init__(self, api_key: str = FMP_API_KEY) -> None:
        self.api_key = api_key

    def get_request(self, url: str, params: dict = None) -> dict:
        response = requests.get(f"{FMP_BASE_URL}{url}", params=params)
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}")
        return response.json()
