import os
from dotenv import load_dotenv
import requests

load_dotenv()
FMP_API_KEY = os.getenv("FMP_API_KEY", "")

FMP_BASE_URL = "https://financialmodelingprep.com/api/"
FMP_DAILY_HISTORY = "v3/historical-price-full/"
FMP_INTRADAY_HISTORY = "v3/historical-chart/"
FMP_COMPANY_PROFILE = "v3/company/profile/"


class FmpBase:
    def __init__(self, api_key: str = FMP_API_KEY) -> None:
        self.api_key = api_key

    def get_request(self, url: str) -> dict:
        response = requests.get(f"{FMP_BASE_URL}{url}")
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}")
        return response.json()
