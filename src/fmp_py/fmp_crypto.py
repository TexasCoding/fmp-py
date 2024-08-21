import pendulum
from fmp_py.fmp_base import FmpBase
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


class FmpCrypto(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")) -> None:
        super().__init__(api_key)

    ####################
    # Crypto Daily
    ####################
    def crypto_daily(self, symbol: str) -> pd.DataFrame:
        """
        Retrieves daily crypto data for a given symbol.
        Args:
            symbol (str): The symbol for the crypto pair.
        Returns:
            pd.DataFrame: A DataFrame containing the historical daily crypto data.
        Raises:
            ValueError: If no data is found for the given symbol.
        """

        clean_symbol = symbol.replace("/", "")
        url = f"v3/historical-price-full/{clean_symbol}"

        try:
            response = self.get_request(url)["historical"]
        except KeyError:
            raise ValueError(f"No data found for {symbol}")

        if not response:
            raise ValueError(f"No data found for {symbol}")

        data_df = (
            pd.DataFrame(response)
            .fillna(0)
            .rename(
                columns={
                    "date": "date",
                    "open": "open",
                    "high": "high",
                    "low": "low",
                    "close": "close",
                    "adjClose": "adj_close",
                    "volume": "volume",
                    "unadjustedVolume": "unadjusted_volume",
                    "change": "change",
                    "changePercent": "change_percent",
                    "vwap": "vwap",
                    "label": "label",
                    "changeOverTime": "change_over_time",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "open": "float",
                    "high": "float",
                    "low": "float",
                    "close": "float",
                    "adj_close": "float",
                    "volume": "int",
                    "unadjusted_volume": "int",
                    "change": "float",
                    "change_percent": "float",
                    "vwap": "float",
                    "label": "str",
                    "change_over_time": "float",
                }
            )
        )

        return data_df

    ####################
    # Intraday Crypto Quote
    ####################
    def intraday_crypto_quote(
        self, symbol: str, interval: str, from_date: str, to_date: str
    ) -> pd.DataFrame:
        """
        Retrieves intraday crypto quotes for a given symbol within a specified time interval.
        Args:
            symbol (str): The symbol of the crypto pair.
            interval (str): The time interval for the quotes. Must be one of: 1min, 5min, 15min, 30min, 1hour, 4hour, 1day, 1week, 1month.
            from_date (str): The starting date for the quotes in the format "YYYY-MM-DD".
            to_date (str): The ending date for the quotes in the format "YYYY-MM-DD".
        Returns:
            pd.DataFrame: A DataFrame containing the intraday crypto quotes with the following columns:
                - date: The date and time of the quote.
                - open: The opening price of the crypto pair.
                - high: The highest price of the crypto pair during the interval.
                - low: The lowest price of the crypto pair during the interval.
                - close: The closing price of the crypto pair.
                - volume: The trading volume during the interval.
        Raises:
            ValueError: If the from_date is greater than the to_date.
            ValueError: If an invalid interval is provided.
            ValueError: If no data is found for the given symbol.
        """

        from_date = pendulum.parse(from_date).format("YYYY-MM-DD")
        to_date = pendulum.parse(to_date).format("YYYY-MM-DD")
        if from_date > to_date:
            raise ValueError("from_date must be less than or equal to to_date")

        clean_symbol = symbol.replace("/", "")

        if interval not in [
            "1min",
            "5min",
            "15min",
            "30min",
            "1hour",
            "4hour",
            "1day",
            "1week",
            "1month",
        ]:
            raise ValueError(
                "Invalid interval. Please choose from: 1min, 5min, 15min, 30min, 1hour, 4hour, 1day, 1week, 1month"
            )

        url = f"v3/historical-chart/{interval}/{clean_symbol}"
        params = {"from": from_date, "to": to_date}

        response = self.get_request(url, params=params)

        if not response:
            raise ValueError(f"No data found for {symbol}")

        data_df = (
            pd.DataFrame(response)
            .fillna(0)
            .astype(
                {
                    "date": "datetime64[ns]",
                    "open": "float",
                    "high": "float",
                    "low": "float",
                    "close": "float",
                    "volume": "int",
                }
            )
        )

        return data_df

    ####################
    # Full crypto Quote
    ####################
    def full_crypto_quote(self, symbol: str) -> pd.DataFrame:
        """
        Retrieves the full crypto quote for a given symbol.
        Args:
            symbol (str): The symbol for the crypto quote.
        Returns:
            pd.DataFrame: A DataFrame containing the full crypto quote data.
        Raises:
            ValueError: If no data is found for the given symbol.
        """

        clean_symbol = symbol.replace("/", "")
        url = f"v3/quote/{clean_symbol}"

        response = self.get_request(url)

        if not response:
            raise ValueError(f"No data found for {symbol}")

        data_df = (
            pd.DataFrame(response)
            .fillna(0)
            .rename(
                columns={
                    "symbol": "symbol",
                    "name": "name",
                    "price": "price",
                    "changesPercentage": "changes_percentage",
                    "change": "change",
                    "dayLow": "day_low",
                    "dayHigh": "day_high",
                    "yearHigh": "year_high",
                    "yearLow": "year_low",
                    "marketCap": "market_cap",
                    "priceAvg50": "price_avg_50",
                    "priceAvg200": "price_avg_200",
                    "exhange": "exchange",
                    "volume": "volume",
                    "avgVolume": "avg_volume",
                    "open": "open",
                    "previousClose": "previous_close",
                    "eps": "eps",
                    "pe": "pe",
                    "earningsAnnouncement": "earnings_announcement",
                    "sharesOutstanding": "shares_outstanding",
                    "timestamp": "timestamp",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "name": "str",
                    "price": "float",
                    "changes_percentage": "float",
                    "change": "float",
                    "day_low": "float",
                    "day_high": "float",
                    "year_high": "float",
                    "year_low": "float",
                    "market_cap": "int",
                    "price_avg_50": "float",
                    "price_avg_200": "float",
                    "exchange": "str",
                    "volume": "int",
                    "avg_volume": "int",
                    "open": "float",
                    "previous_close": "float",
                    "eps": "float",
                    "pe": "float",
                    "earnings_announcement": "str",
                    "shares_outstanding": "int",
                }
            )
        )

        data_df["timestamp"] = pd.to_datetime(data_df["timestamp"], unit="s")

        return data_df

    ####################
    # crypto List
    ####################
    def crypto_list(self) -> pd.DataFrame:
        """
        Retrieves a list of available crypto currency pairs.
        Returns:
            pd.DataFrame: A DataFrame containing the following columns:
                - symbol: The symbol of the currency pair.
                - name: The name of the currency pair.
                - currency: The currency of the currency pair.
                - stock_exchange: The stock exchange of the currency pair.
                - exchange_short_name: The short name of the stock exchange.
        Raises:
            ValueError: If no data is found.
        """

        url = "v3/symbol/available-cryptocurrencies"
        response = self.get_request(url)

        if not response:
            raise ValueError("No data found")

        data_df = (
            pd.DataFrame(response)
            .fillna("")
            .rename(
                columns={
                    "symbol": "symbol",
                    "name": "name",
                    "currency": "currency",
                    "stockExchange": "stock_exchange",
                    "exchangeShortName": "exchange_short_name",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "name": "str",
                    "currency": "str",
                    "stock_exchange": "str",
                    "exchange_short_name": "str",
                }
            )
        )

        return data_df

    ####################
    # Full crypto Quote List
    ####################
    def full_crypto_quote_list(self) -> pd.DataFrame:
        """
        Retrieves a full list of crypto quotes.
        Returns:
            pd.DataFrame: A DataFrame containing the crypto quotes with the following columns:
                - symbol (str): The symbol of the crypto.
                - name (str): The name of the crypto.
                - price (float): The current price of the crypto.
                - changes_percentage (float): The percentage change in price.
                - change (float): The change in price.
                - day_low (float): The lowest price of the day.
                - day_high (float): The highest price of the day.
                - year_high (float): The highest price in the past year.
                - year_low (float): The lowest price in the past year.
                - market_cap (int): The market capitalization of the crypto.
                - price_avg_50 (float): The 50-day average price.
                - price_avg_200 (float): The 200-day average price.
                - exchange (str): The exchange where the crypto is traded.
                - volume (int): The trading volume of the crypto.
                - avg_volume (int): The average trading volume of the crypto.
                - open (float): The opening price of the crypto.
                - previous_close (float): The previous closing price of the crypto.
                - eps (float): The earnings per share of the crypto.
                - pe (float): The price-to-earnings ratio of the crypto.
                - earnings_announcement (str): The announcement date of the earnings.
                - shares_outstanding (int): The number of shares outstanding.
                - timestamp (datetime): The timestamp of the data.
        Raises:
            ValueError: If no data is found.
        """

        url = "v3/quotes/crypto"
        response = self.get_request(url)

        if not response:
            raise ValueError("No data found")

        data_df = (
            pd.DataFrame(response)
            .fillna(0)
            .rename(
                columns={
                    "symbol": "symbol",
                    "name": "name",
                    "price": "price",
                    "changesPercentage": "changes_percentage",
                    "change": "change",
                    "dayLow": "day_low",
                    "dayHigh": "day_high",
                    "yearHigh": "year_high",
                    "yearLow": "year_low",
                    "marketCap": "market_cap",
                    "priceAvg50": "price_avg_50",
                    "priceAvg200": "price_avg_200",
                    "exhange": "exchange",
                    "volume": "volume",
                    "avgVolume": "avg_volume",
                    "open": "open",
                    "previousClose": "previous_close",
                    "eps": "eps",
                    "pe": "pe",
                    "earningsAnnouncement": "earnings_announcement",
                    "sharesOutstanding": "shares_outstanding",
                    "timestamp": "timestamp",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "name": "str",
                    "price": "float",
                    "changes_percentage": "float",
                    "change": "float",
                    "day_low": "float",
                    "day_high": "float",
                    "year_high": "float",
                    "year_low": "float",
                    "market_cap": "int",
                    "price_avg_50": "float",
                    "price_avg_200": "float",
                    "exchange": "str",
                    "volume": "int",
                    "avg_volume": "int",
                    "open": "float",
                    "previous_close": "float",
                    "eps": "float",
                    "pe": "float",
                    "earnings_announcement": "str",
                    "shares_outstanding": "int",
                }
            )
        )

        data_df["timestamp"] = pd.to_datetime(data_df["timestamp"], unit="s")

        return data_df
