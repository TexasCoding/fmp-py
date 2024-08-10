import os
from fmp_py.fmp_base import FmpBase
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
"""
This class is used to access the FMP dividends endpoints.
Reference: https://site.financialmodelingprep.com/developer/docs#dividends

def dividends_calendar(self, from_date, to_date):
    Reference: https://site.financialmodelingprep.com/developer/docs#dividends-calendar-dividends
    
def dividends_historical(self, symbol, from_date, to_date):
    Reference: https://site.financialmodelingprep.com/developer/docs#dividends-historical-dividends
"""


class FmpDividends(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")):
        super().__init__(api_key)

    def dividends_calendar(self, from_date, to_date):
        url = "v3/stock_dividend_calendar"
        params = {"from": from_date, "to": to_date}
        response = self.get_request(url=url, params=params)

        if not response:
            raise ValueError("Failed to fetch dividends calendar data.")

        data_df = pd.DataFrame(response)

        return self.fill_na(data_df)

    # def dividends_historical(self, symbol, from_date, to_date):
    #     """
    #     Reference: https://site.financialmodelingprep.com/developer/docs#dividends-historical-dividends
    #     """
    #     url = f"{self.base_url}/v3/historical/dividends/{symbol}?from={from_date}&to={to_date}&limit={limit}"
    #     return self._get_data(url)
