import pandas as pd
from fmp_py.fmp_base import FmpBase

# from typing import Dict, Any
import os
from dotenv import load_dotenv

load_dotenv()


class FmpHistoricalData(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")) -> None:
        """
        Initialize the FmpHistoricalData class.

        Args:
            api_key (str): The API key for Financial Modeling Prep.
        """
        super().__init__(api_key)

    ############################
    # Historical Daily Prices
    ############################
    def daily_history(self, symbol: str, from_date: str, to_date: str) -> pd.DataFrame:
        """
        Retrieves daily historical data for a given symbol within a specified date range.

        Args:
            symbol (str): The symbol of the stock or asset.
            from_date (str): The starting date of the historical data in the format 'YYYY-MM-DD'.
            to_date (str): The ending date of the historical data in the format 'YYYY-MM-DD'.

        Returns:
            pd.DataFrame: A DataFrame containing the daily historical data for the specified symbol.
        """
        url = f"v3/historical-price-full/{symbol}"
        params = {"from": from_date, "to": to_date}
        response = self.get_request(url, params)

        data = response.get("historical", [])

        if not data:
            return pd.DataFrame()

        data_df = self._prepare_data(pd.DataFrame(data))
        return data_df.sort_values(by="date").set_index("date")[
            ["open", "high", "low", "close", "volume", "vwap"]
        ]

    ############################
    # Intraday Historical Prices
    ############################
    def intraday_history(
        self, symbol: str, interval: str, from_date: str, to_date: str
    ) -> pd.DataFrame:
        """
        Retrieves intraday historical data for a given symbol within a specified time interval.

        Args:
            symbol (str): The stock or asset symbol.
            interval (str): The time interval for the data. Must be one of: ['1min', '5min', '15min', '30min', '1hour', '4hour'].
            from_date (str): The starting date for the data in the format 'YYYY-MM-DD'.
            to_date (str): The ending date for the data in the format 'YYYY-MM-DD'.

        Returns:
            pd.DataFrame: A DataFrame containing the intraday historical data for the specified symbol and time interval.
        """
        interval_options = ["1min", "5min", "15min", "30min", "1hour", "4hour"]
        if interval not in interval_options:
            raise ValueError(f"Interval must be one of: {interval_options}")

        url = f"v3/historical-chart/{interval}/{symbol}"
        params = {"from": from_date, "to": to_date}
        response = self.get_request(url, params)

        if not response:
            return pd.DataFrame()

        data_df = self._prepare_data(pd.DataFrame(response))
        return data_df.sort_values(by="date").set_index("date")

    ############################
    # Prepare Data
    ############################
    def _prepare_data(self, data_df: pd.DataFrame) -> pd.DataFrame:
        """
        Prepare data by calculating VWAP and converting data types.

        Args:
            data_df (pd.DataFrame): Raw data.

        Returns:
            pd.DataFrame: Prepared data.
        """
        data_df["vwap"] = self._calc_vwap(data_df)
        data_df = data_df.astype(
            {
                "date": "datetime64[ns]",
                "open": "float",
                "high": "float",
                "low": "float",
                "close": "float",
                "volume": "int",
                "vwap": "float",
            }
        )
        return self._round_prices(data_df)

    ############################
    # Round Prices
    ############################
    def _round_prices(self, data_df: pd.DataFrame) -> pd.DataFrame:
        """
        Round prices to 2 decimal places.

        Args:
            data_df (pd.DataFrame): DataFrame with price data.

        Returns:
            pd.DataFrame: DataFrame with rounded price data.
        """
        price_columns = ["open", "high", "low", "close"]
        data_df[price_columns] = data_df[price_columns].round(2)
        return data_df

    ############################
    # VWAP Calculation
    ############################
    def _calc_vwap(self, data_df: pd.DataFrame) -> pd.Series:
        """
        Calculate the Volume Weighted Average Price (VWAP).

        Args:
            data_df (pd.DataFrame): DataFrame with price and volume data.

        Returns:
            pd.Series: VWAP values.
        """
        vwap = (
            ((data_df["high"] + data_df["low"] + data_df["close"]) / 3)
            * data_df["volume"]
        ).cumsum() / data_df["volume"].cumsum()
        return vwap.round(2)


# # src/fmp_py/fmp_historical_data.py
# # Define the FmpHistoricalData class that inherits from FmpBase.
# import pandas as pd
# from fmp_py.fmp_base import FmpBase


# class FmpHistoricalData(FmpBase):
#     def __init__(self) -> None:
#         super().__init__()

#     ############################
#     # Historical Daily Prices
#     ############################
#     def daily_history(self, symbol: str, from_date: str, to_date: str) -> pd.DataFrame:
#         """
#         Retrieves the daily historical data for a given symbol within a specified date range.

#         Args:
#             symbol (str): The symbol of the stock or asset.
#             from_date (str): The starting date of the historical data in the format 'YYYY-MM-DD'.
#             to_date (str): The ending date of the historical data in the format 'YYYY-MM-DD'.

#         Returns:
#             pd.DataFrame: A DataFrame containing the daily historical data for the specified symbol.

#         """
#         url = f"v3/historical-price-full/{symbol}"

#         params = {"from": from_date, "to": to_date, "apikey": self.api_key}

#         response = self.get_request(url=url, params=params)
#         data = response.get("historical", [])

#         if not data:
#             return pd.DataFrame()

#         data_df = pd.DataFrame(data)

#         data_df = self._prepare_data(data_df).sort_values(by="date").set_index("date")

#         return data_df[["open", "high", "low", "close", "volume", "vwap"]]

#     ############################
#     # Intraday Historical Prices
#     ############################
#     def intraday_history(
#         self, symbol: str, interval: str, from_date: str, to_date: str
#     ) -> dict:
#         """
#         Retrieves intraday historical data for a given symbol within a specified time interval.

#         Args:
#             symbol (str): The symbol of the stock or security.
#             interval (str): The time interval for the data. Must be one of: ["1min", "5min", "15min", "30min", "1hour", "4hour"].
#             from_date (str): The starting date for the data in the format "YYYY-MM-DD".
#             to_date (str): The ending date for the data in the format "YYYY-MM-DD".

#         Returns:
#             dict: A dictionary containing the intraday historical data for the specified symbol and time interval.
#         """
#         interval_options = ["1min", "5min", "15min", "30min", "1hour", "4hour"]
#         if interval not in interval_options:
#             raise ValueError(f"Interval must be one of: {interval_options}")

#         url = f"v3/historical-chart/{interval}/{symbol}"

#         params = {"from": from_date, "to": to_date, "apikey": self.api_key}

#         response = self.get_request(url=url, params=params)
#         if not response:
#             return pd.DataFrame()

#         data_df = pd.DataFrame(response)

#         data_df = self._prepare_data(data_df)

#         return data_df.sort_values(by="date").set_index("date")

#     ############################
#     # Prepare Data
#     ############################
#     def _prepare_data(self, data_df: dict) -> pd.DataFrame:
#         """
#         Prepare the data by calculating VWAP and converting the data types.

#         Args:
#             data_df (dict): A dictionary containing the historical data.

#         Returns:
#             pd.DataFrame: The prepared data with VWAP calculated and data types converted.
#         """
#         data_df["vwap"] = self._calc_vwap(data_df)
#         data_df = data_df.astype(
#             {
#                 "date": "datetime64[ns]",
#                 "open": "float",
#                 "high": "float",
#                 "low": "float",
#                 "close": "float",
#                 "volume": "int",
#                 "vwap": "float",
#             }
#         )

#         data_df = self._round_prices(data_df)

#         return data_df

#     ############################
#     # Round Prices
#     ############################
#     def _round_prices(self, data_df: pd.DataFrame) -> pd.DataFrame:
#         """
#         Round the prices in the given DataFrame to two decimal places.

#         Args:
#             data_df (pd.DataFrame): The DataFrame containing the prices to be rounded.

#         Returns:
#             pd.DataFrame: The DataFrame with rounded prices.
#         """
#         data_df = data_df.copy()

#         prices_cols = ["open", "high", "low", "close"]

#         data_df[prices_cols] = data_df[prices_cols].round(2)

#         return data_df

#     ############################
#     # VWAP Calculation
#     ############################
#     def _calc_vwap(self, data_df: pd.DataFrame) -> pd.Series:
#         """
#         Calculate the Volume Weighted Average Price (VWAP) for the given DataFrame.

#         Args:
#             data_df (pd.DataFrame): The DataFrame containing the historical data.

#         Returns:
#             pd.Series: The VWAP values rounded to 2 decimal places.
#         """
#         copy_df = data_df.copy()
#         copy_df["vwap"] = (
#             ((copy_df["high"] + copy_df["low"] + copy_df["close"]) / 3)
#             * copy_df["volume"]
#         ).cumsum() / copy_df["volume"].cumsum()
#         return copy_df["vwap"].round(2)
