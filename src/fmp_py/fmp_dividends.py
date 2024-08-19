import os

import pendulum
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

    #############################
    # Dividends Calendar
    #############################
    def dividends_calendar(self, from_date: str, to_date: str) -> pd.DataFrame:
        """
        Retrieves the dividends calendar data for a specified date range.
        Args:
            from_date (str): The starting date of the date range in "YYYY-MM-DD" format.
            to_date (str): The ending date of the date range in "YYYY-MM-DD" format.
        Returns:
            pd.DataFrame: A DataFrame containing the dividends calendar data with the following columns:
                - date: The date of the dividend event.
                - label: The label of the dividend event.
                - adj_dividend: The adjusted dividend amount.
                - symbol: The symbol of the stock.
                - dividend: The dividend amount.
                - record_date: The record date of the dividend event.
                - payment_date: The payment date of the dividend event.
                - declaration_date: The declaration date of the dividend event.
        Raises:
            ValueError: If from_date is greater than to_date or if the request to fetch dividends calendar data fails.
        """

        from_date = pendulum.parse(from_date).format("YYYY-MM-DD")
        to_date = pendulum.parse(to_date).format("YYYY-MM-DD")
        if from_date > to_date:
            raise ValueError("from_date must be less than or equal to to_date")

        url = "v3/stock_dividend_calendar"
        params = {"from": from_date, "to": to_date}
        response = self.get_request(url=url, params=params)

        if not response:
            raise ValueError("Failed to fetch dividends calendar data.")

        data_df = (
            pd.DataFrame(response)
            .fillna(0)
            .rename(
                columns={
                    "date": "date",
                    "label": "label",
                    "adjDividend": "adj_dividend",
                    "symbol": "symbol",
                    "dividend": "dividend",
                    "recordDate": "record_date",
                    "paymentDate": "payment_date",
                    "declarationDate": "declaration_date",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "label": "str",
                    "adj_dividend": "float64",
                    "symbol": "str",
                    "dividend": "float64",
                    "record_date": "datetime64[ns]",
                    "payment_date": "datetime64[ns]",
                    "declaration_date": "datetime64[ns]",
                }
            )
            .sort_values(by="date", ascending=True)
            .reset_index(drop=True)
        )

        return data_df

    #############################
    # Dividends Historical
    #############################
    def dividends_historical(self, symbol: str) -> pd.DataFrame:
        """
        Fetches historical dividends data for a given stock symbol.
        Args:
            symbol (str): The stock symbol.
        Returns:
            pd.DataFrame: A DataFrame containing the historical dividends data.
        Raises:
            ValueError: If failed to fetch historical dividends data for the given symbol.
        """

        url = f"v3/historical-price-full/stock_dividend/{symbol}"

        response = self.get_request(url=url)["historical"]

        if not response:
            raise ValueError(f"Failed to fetch historical dividends data for {symbol}.")

        data_df = (
            pd.DataFrame(response)
            .fillna(0)
            .rename(
                columns={
                    "date": "date",
                    "label": "label",
                    "adjDividend": "adj_dividend",
                    "dividend": "dividend",
                    "recordDate": "record_date",
                    "paymentDate": "payment_date",
                    "declarationDate": "declaration_date",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "label": "str",
                    "adj_dividend": "float64",
                    "dividend": "float64",
                    "record_date": "datetime64[ns]",
                    "payment_date": "datetime64[ns]",
                    "declaration_date": "datetime64[ns]",
                }
            )
            .sort_values(by="date", ascending=True)
            .reset_index(drop=True)
        )
        data_df["symbol"] = symbol

        return data_df
