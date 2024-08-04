from typing import List
import pandas as pd
from fmp_py.fmp_base import FmpBase
import os
from dotenv import load_dotenv

load_dotenv()

"""
Defines the FmpStockList class that inherits from FmpBase.
This class is used to interact with the Financial Modeling Prep API to retrieve stock lists.
https://site.financialmodelingprep.com/developer/docs#stock-list


def stock_list(self) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#symbol-list-stock-list
    
def exchange_traded_fund_search(self) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#exchange-traded-fund-search-stock-list
    
def statement_symbols_list(self) -> List[str]:
    Reference: https://site.financialmodelingprep.com/developer/docs#statement-symbols-list-stock-list
    
def tradable_stocks_search(self) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs/tradable-list-api
    
def commitment_of_traders_report(self) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs/cot-symbols-list-api
    
def cik_list(self) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs/cik-list-stock-list
    
def euronext_symbols(self) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs/euronext-prices-api
    
def symbol_changes(self) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs/symbol-change-api
    
def exchange_symbols(self) -> pd.DataFrame:
    Reference:https://site.financialmodelingprep.com/developer/docs#exchange-symbols-stock-list
    
def available_indexes(self) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#available-indexes
"""


class FmpStockList(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")) -> None:
        super().__init__(api_key)

    #################################
    # Available Indexes
    #################################
    def available_indexes(self) -> pd.DataFrame:
        """
        Retrieves a DataFrame of available indexes from the API.

        Returns:
            pd.DataFrame: A DataFrame containing the available indexes.
                The DataFrame columns include 'symbol', 'name', 'currency',
                'stock_exchange', and 'exchange_short_name'.
        """
        url = "v3/symbol/available-indexes"
        params = {"apikey": self.api_key}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found in API response.")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "symbol": "symbol",
                    "name": "name",
                    "currency": "currency",
                    "stockExchange": "stock_exchange",
                    "exchangeShortName": "exchange_short_name",
                }
            )
            .sort_values(by="symbol", ascending=True)
            .reset_index(drop=True)
        )

    #################################
    # Exchange Symbols
    #################################
    def exchange_symbols(self, exchange: str) -> pd.DataFrame:
        """
        Retrieves a DataFrame of stock symbols for a specific exchange.

        Args:
            exchange (str): The exchange for which to retrieve stock symbols.

        Returns:
            pd.DataFrame: A DataFrame containing the stock symbols and their corresponding data.

        Raises:
            ValueError: If no data is found in the API response.
        """

        url = f"v3/symbol/{exchange}"
        params = {"apikey": self.api_key}
        response = self.get_request(url, params)
        if not response:
            raise ValueError("No data found in API response.")

        data_df = pd.DataFrame(response).rename(
            columns={
                "symbol": "symbol",
                "name": "name",
                "price": "price",
                "changesPercentage": "change_percentage",
                "change": "change",
                "dayLow": "day_low",
                "dayHigh": "day_high",
                "yearHigh": "year_high",
                "yearLow": "year_low",
                "marketCap": "market_cap",
                "priceAvg50": "price_avg_50",
                "priceAvg200": "price_avg_200",
                "exchange": "exchange",
                "volume": "volume",
                "avgVolume": "avg_volume",
                "open": "open",
                "previousClose": "previous_close",
                "eps": "eps",
                "pe": "pe",
                "earningsAnnouncement": "earnings_announcement",
                "sharesOutstanding": "shares_outstanding",
                "timestamp": "datetime",
            }
        )

        data_df["datetime"] = pd.to_datetime(data_df["datetime"], unit="ns")
        data_df["earnings_announcement"] = data_df["earnings_announcement"].fillna(
            "1970-01-01 00:00:00"
        )
        data_df["earnings_announcement"] = pd.to_datetime(
            data_df["earnings_announcement"], errors="coerce"
        )
        data_df["market_cap"] = data_df["market_cap"].fillna(0)
        data_df["volume"] = data_df["volume"].fillna(0)
        data_df["avg_volume"] = data_df["avg_volume"].fillna(0)

        return (
            data_df.fillna(0)
            .astype(
                {
                    "symbol": "string",
                    "name": "string",
                    "price": "float64",
                    "change_percentage": "float64",
                    "change": "float64",
                    "day_low": "float64",
                    "day_high": "float64",
                    "year_high": "float64",
                    "year_low": "float64",
                    "market_cap": "int",
                    "price_avg_50": "float64",
                    "price_avg_200": "float64",
                    "exchange": "string",
                    "volume": "int",
                    "avg_volume": "int",
                    "open": "float64",
                    "previous_close": "float64",
                    "eps": "float64",
                    "pe": "float64",
                    "earnings_announcement": "datetime64[ns]",
                    "shares_outstanding": "float64",
                    "datetime": "datetime64[ns]",
                }
            )
            .sort_values(by="symbol", ascending=True)
            .reset_index(drop=True)
        )

    #################################
    # Symbol Changes
    #################################
    def symbol_changes(self) -> pd.DataFrame:
        """
        Retrieves the symbol changes from the API and returns them as a pandas DataFrame.

        Returns:
            pd.DataFrame: A DataFrame containing the symbol changes, with columns for date, name, old symbol, and new symbol.
        """
        url = "v4/symbol_change"
        params = {"apikey": self.api_key}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found in API response.")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "date": "date",
                    "name": "name",
                    "oldSymbol": "old_symbol",
                    "newSymbol": "new_symbol",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "name": "str",
                    "old_symbol": "str",
                    "new_symbol": "str",
                }
            )
            .sort_values(by="date", ascending=True)
            .reset_index(drop=True)
        )

    #################################
    # Euronext Symbols
    #################################
    def euronext_symbols(self) -> pd.DataFrame:
        """
        Retrieves a DataFrame of available symbols on the Euronext stock exchange.

        Returns:
            pd.DataFrame: A DataFrame containing the available symbols on the Euronext stock exchange.

        Raises:
            ValueError: If no data is found in the API response.
        """
        url = "v3/symbol/available-euronext"
        params = {"apikey": self.api_key}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found in API response.")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "symbol": "symbol",
                    "name": "name",
                    "currency": "currency",
                    "stockExchange": "stock_exchange",
                    "exchangeShortName": "exchange_short_name",
                }
            )
            .sort_values(by="symbol", ascending=True)
            .reset_index(drop=True)
        )

    #################################
    # CIK List
    #################################
    def cik_list(self) -> pd.DataFrame:
        """
        Retrieves the CIK (Central Index Key) list from the API.

        Returns:
            pd.DataFrame: A DataFrame containing the CIK list.

        Raises:
            ValueError: If no data is found in the API response.
        """
        url = "v3/cik_list"
        params = {"apikey": self.api_key}

        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found in API response.")

        return (
            pd.DataFrame(response)
            .sort_values(by="name", ascending=True)
            .reset_index(drop=True)
        )

    #################################
    # Commitment of Traders Report
    #################################
    def commitment_of_traders_report(self) -> pd.DataFrame:
        """
        Retrieves the commitment of traders report from the API and returns it as a pandas DataFrame.

        Returns:
            pd.DataFrame: The commitment of traders report data.

        Raises:
            ValueError: If no data is found in the API response.
        """
        url = "v4/commitment_of_traders_report/list"
        params = {"apikey": self.api_key}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found in API response.")

        return pd.DataFrame(response)

    #################################
    # Tradable Stocks Search
    #################################
    def tradable_stocks_search(self) -> pd.DataFrame:
        url = "v3/available-traded/list"
        return self._process_data(url)

    #################################
    # Statement Symbols List
    #################################
    def statement_symbols_list(self) -> List[str]:
        """
        Retrieves a list of financial statement symbols.

        Returns:
            A list of financial statement symbols.

        Raises:
            ValueError: If no data is found in the API response.
        """
        url = "v3/financial-statement-symbol-lists"
        params = {"apikey": self.api_key}
        response: List[str] = self.get_request(url, params)

        if len(response) == 0:
            raise ValueError("No data found in API response")

        return response

    #################################
    # Exchange Traded Fund Search
    #################################
    def exchange_traded_fund_search(self) -> pd.DataFrame:
        """
        Retrieves a list of exchange-traded funds (ETFs) from the API.

        Returns:
            pd.DataFrame: A DataFrame containing the ETF data, with columns for symbol, name, price, exchange,
            exchange_short_name, and type. The DataFrame is sorted by symbol in ascending order and has its index reset.

        Raises:
            ValueError: If no data is found in the API response.
        """
        url = "v3/etf/list"
        return self._process_data(url)

    #################################
    # Stock List
    #################################
    def stock_list(self) -> pd.DataFrame:
        """
        Retrieves a list of stocks from the API.

        Returns:
            pd.DataFrame: A DataFrame containing the stock information with the following columns:
                - symbol: The stock symbol.
                - name: The name of the stock.
                - exchange: The stock exchange where the stock is traded.
                - price: The current price of the stock.
                - exchange_short_name: The short name of the stock exchange.
                - type: The type of the stock.
        """
        url = "v3/stock/list"
        return self._process_data(url)

    #################################
    # _Process Data
    #################################
    def _process_data(self, url: str) -> pd.DataFrame:
        """
        Process the data returned from the API.

        Args:
            url (str): The URL to make the API request.

        Returns:
            pd.DataFrame: Processed data as a pandas DataFrame.

        Raises:
            ValueError: If no data is returned from the API.
        """
        params = {"apikey": self.api_key}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data returned from API")

        return (
            (
                pd.DataFrame(response)
                .rename(
                    columns={
                        "symbol": "symbol",
                        "name": "name",
                        "exchange": "exchange",
                        "price": "price",
                        "exchangeShortName": "exchange_short_name",
                        "type": "type",
                    }
                )
                .astype(
                    {
                        "symbol": "str",
                        "name": "str",
                        "exchange": "str",
                        "price": "float",
                        "exchange_short_name": "str",
                        "type": "str",
                    }
                )
            )
            .sort_values(by=["symbol"], ascending=True)
            .reset_index(drop=True)
        )
