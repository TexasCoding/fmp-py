from fmp_py.fmp_base import FmpBase
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


class FmpForex(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")) -> None:
        super().__init__(api_key)

    ####################
    # Forex List
    ####################
    def forex_list(self) -> pd.DataFrame:
        """
        Retrieves a list of available forex currency pairs.
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

        url = "v3/symbol/available-forex-currency-pairs"
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
    # Full Forex Quote List
    ####################
    def full_forex_quote_list(self) -> pd.DataFrame:
        """
        Retrieves a full list of forex quotes.
        Returns:
            pd.DataFrame: A DataFrame containing the forex quotes with the following columns:
                - symbol (str): The symbol of the forex.
                - name (str): The name of the forex.
                - price (float): The current price of the forex.
                - changes_percentage (float): The percentage change in price.
                - change (float): The change in price.
                - day_low (float): The lowest price of the day.
                - day_high (float): The highest price of the day.
                - year_high (float): The highest price in the past year.
                - year_low (float): The lowest price in the past year.
                - market_cap (int): The market capitalization of the forex.
                - price_avg_50 (float): The 50-day average price.
                - price_avg_200 (float): The 200-day average price.
                - exchange (str): The exchange where the forex is traded.
                - volume (int): The trading volume of the forex.
                - avg_volume (int): The average trading volume of the forex.
                - open (float): The opening price of the forex.
                - previous_close (float): The previous closing price of the forex.
                - eps (float): The earnings per share of the forex.
                - pe (float): The price-to-earnings ratio of the forex.
                - earnings_announcement (str): The announcement date of the earnings.
                - shares_outstanding (int): The number of shares outstanding.
                - timestamp (datetime): The timestamp of the data.
        Raises:
            ValueError: If no data is found.
        """

        url = "v3/quotes/forex"
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
