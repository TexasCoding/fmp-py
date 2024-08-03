import pandas as pd
from fmp_py.fmp_base import FmpBase
import os
from dotenv import load_dotenv

load_dotenv()


class FmpEarnings(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")):
        super().__init__(api_key)

    def earnings_calendar(self, from_date: str, to_date: str) -> pd.DataFrame:
        url = "v3/earning_calendar"
        params = {"from": from_date, "to": to_date}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("Error fetching earnings calendar data")

        return pd.DataFrame(response)

    def earnings_historical(self, symbol: str) -> pd.DataFrame:
        url = f"v3/historical/earning_calendar/{symbol}"
        response = self.get_request(url)

        if not response:
            raise ValueError("Error fetching earnings historical data")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "date": "date",
                    "symbol": "symbol",
                    "eps": "eps",
                    "revenue": "revenue",
                    "epsEstimated": "eps_estimated",
                    "revenueEstimated": "revenue_estimated",
                    "time": "time",
                    "updatedFromDate": "updated_from_date",
                    "fiscalDateEnding": "fiscal_date_ending",
                }
            )
            .fillna(0)
            .astype(
                {
                    "date": "datetime64[ns]",
                    "time": "str",
                    "updated_from_date": "datetime64[ns]",
                    "fiscal_date_ending": "datetime64[ns]",
                    "eps": "float",
                    "revenue": "int",
                    "eps_estimated": "float",
                    "revenue_estimated": "int",
                }
            )
            .sort_values(by="date", ascending=True)
        )
