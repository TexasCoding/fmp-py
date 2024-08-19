import pandas as pd
import pendulum
from fmp_py.fmp_base import FmpBase
import os
from dotenv import load_dotenv

load_dotenv()

"""
Retrieves Stock Spilts Data from Financial Modeling Prep API
References:
    - https://site.financialmodelingprep.com/developer/docs#splits

def stock_splits_calendar(self, from_date: str, to_date: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#splits-calendar-splits
    
def stock_splits_historical(self, symbol: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#splits-historical-splits
"""


class FmpSplits(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")) -> None:
        super().__init__(api_key)

    ##########################################
    # Stock Splits Histrorical
    ##########################################
    def stock_splits_historical(self, symbol: str) -> pd.DataFrame:
        """
        Retrieves historical stock splits data for a given symbol.
        Args:
            symbol (str): The stock symbol.
        Returns:
            pd.DataFrame: A DataFrame containing the historical stock splits data.
        """

        url = f"v3/historical-price-full/stock_split/{symbol}"
        response = self.get_request(url)["historical"]

        if not response:
            raise ValueError(
                f"Error fetching stock splits historical data for {symbol}"
            )

        data_df = (
            pd.DataFrame(response)
            .fillna(0)
            .rename(
                columns={
                    "date": "date",
                    "label": "label",
                    "numerator": "numerator",
                    "denominator": "denominator",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "label": "str",
                    "numerator": "int",
                    "denominator": "int",
                }
            )
            .sort_values(by="date", ascending=True)
            .reset_index(drop=True)
        )
        data_df["symbol"] = symbol

        return data_df

    ########################################
    # Stock Splits Calendar
    ########################################
    def stock_splits_calendar(self, from_date: str, to_date: str) -> pd.DataFrame:
        """
        Retrieves the stock splits calendar for a given date range.
        Args:
            from_date (str): The start date of the date range in "YYYY-MM-DD" format.
            to_date (str): The end date of the date range in "YYYY-MM-DD" format.
        Returns:
            pd.DataFrame: A DataFrame containing the stock splits calendar data with the following columns:
                - date: The date of the stock split.
                - label: The label of the stock split.
                - symbol: The symbol of the stock.
                - numerator: The numerator of the stock split ratio.
                - denominator: The denominator of the stock split ratio.
        Raises:
            ValueError: If from_date is greater than to_date or if no data is found for the given date range.
        """

        from_date = pendulum.parse(from_date).format("YYYY-MM-DD")
        to_date = pendulum.parse(to_date).format("YYYY-MM-DD")
        if from_date > to_date:
            raise ValueError("from_date must be less than or equal to to_date")

        url = "v3/stock_split_calendar"
        params = {"from": from_date, "to": to_date}
        response = self.get_request(url=url, params=params)

        if not response:
            raise ValueError("No data found for the given date range")

        data_df = (
            pd.DataFrame(response)
            .fillna(0)
            .rename(
                columns={
                    "date": "date",
                    "label": "label",
                    "symbol": "symbol",
                    "numerator": "numerator",
                    "denominator": "denominator",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "label": "str",
                    "symbol": "str",
                    "numerator": "int",
                    "denominator": "int",
                }
            )
            .sort_values(by="date", ascending=True)
            .reset_index(drop=True)
        )

        return data_df
