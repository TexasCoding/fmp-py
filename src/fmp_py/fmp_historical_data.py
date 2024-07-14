import pandas as pd
from fmp_py.fmp_base import FmpBase, FMP_DAILY_HISTORY, FMP_INTRADAY_HISTORY


class FmpHistoricalData(FmpBase):
    def __init__(self) -> None:
        super().__init__()

    ############################
    # Historical Daily Prices
    ############################
    def daily_history(self, symbol: str, from_date: str, to_date: str) -> pd.DataFrame:
        """
        Retrieves the daily historical data for a given symbol within a specified date range.

        Args:
            symbol (str): The symbol of the stock or asset.
            from_date (str): The starting date of the historical data in the format 'YYYY-MM-DD'.
            to_date (str): The ending date of the historical data in the format 'YYYY-MM-DD'.

        Returns:
            pd.DataFrame: A DataFrame containing the daily historical data for the specified symbol.

        """
        url = f"{FMP_DAILY_HISTORY}{symbol}?from={from_date}&to={to_date}&apikey={self.api_key}"
        response = self.get_request(url)
        data = response.get("historical", [])

        if not data:
            return pd.DataFrame()

        data_df = pd.DataFrame(data).drop(
            columns=[
                "adjClose",
                "change",
                "changeOverTime",
                "changePercent",
                "label",
                "unadjustedVolume",
                "vwap",
            ]
        )
        
        self._prepare_data(data_df)

        self._round_prices(data_df)

        return data_df.sort_values(by="date").set_index("date")

    ############################
    # Intraday Historical Prices
    ############################
    def intraday_history(
        self, symbol: str, interval: str, from_date: str, to_date: str
    ) -> dict:
        """
        Retrieves intraday historical data for a given symbol within a specified time interval.

        Args:
            symbol (str): The symbol of the stock or security.
            interval (str): The time interval for the data. Must be one of: ["1min", "5min", "15min", "30min", "1hour", "4hour"].
            from_date (str): The starting date for the data in the format "YYYY-MM-DD".
            to_date (str): The ending date for the data in the format "YYYY-MM-DD".

        Returns:
            dict: A dictionary containing the intraday historical data for the specified symbol and time interval.
        """

        interval_options = ["1min", "5min", "15min", "30min", "1hour", "4hour"]

        if interval not in interval_options:
            raise ValueError(f"Interval must be one of: {interval_options}")

        url = f"{FMP_INTRADAY_HISTORY}{interval}/{symbol}?from={from_date}&to={to_date}&apikey={self.api_key}"
        response = self.get_request(url)
        if not response:
            return pd.DataFrame()

        data_df = pd.DataFrame(response)

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

        self._round_prices(data_df)

        return data_df.sort_values(by="date").set_index("date")

    ############################
    # Prepare Data
    ############################
    def _prepare_data(self, data_df: dict) -> pd.DataFrame:
        """
        Prepare the data by calculating VWAP and converting the data types.

        Args:
            data_df (dict): A dictionary containing the historical data.

        Returns:
            pd.DataFrame: The prepared data with VWAP calculated and data types converted.
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

        return data_df

    ############################
    # Round Prices
    ############################
    def _round_prices(self, data_df: pd.DataFrame) -> pd.DataFrame:
        """
        Round the prices in the given DataFrame to two decimal places.

        Args:
            data_df (pd.DataFrame): The DataFrame containing the prices to be rounded.

        Returns:
            pd.DataFrame: The DataFrame with rounded prices.
        """
        data_df[
            [
                "open",
                "high",
                "low",
                "close",
            ]
        ] = data_df[
            [
                "open",
                "high",
                "low",
                "close",
            ]
        ].round(2)

        return data_df

    ############################
    # VWAP Calculation
    ############################
    def _calc_vwap(self, data_df: pd.DataFrame) -> pd.Series:
        """
        Calculate the Volume Weighted Average Price (VWAP) for the given DataFrame.

        Args:
            data_df (pd.DataFrame): The DataFrame containing the historical data.

        Returns:
            pd.Series: The VWAP values rounded to 2 decimal places.
        """
        copy_df = data_df.copy()
        copy_df["vwap"] = (
            ((copy_df["high"] + copy_df["low"] + copy_df["close"]) / 3)
            * copy_df["volume"]
        ).cumsum() / copy_df["volume"].cumsum()
        return copy_df["vwap"].round(2)
