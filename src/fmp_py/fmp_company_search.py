import pandas as pd
from fmp_py.fmp_base import FmpBase
import os
from dotenv import load_dotenv

load_dotenv()

"""
This class provides methods for searching for companies on Financial Modeling Prep (FMP).
https://site.financialmodelingprep.com/developer/docs#company-search

def general_search(self, query: str, exchange: str = None, limit: int = None) -> pd.DataFrame:
    Referance: https://site.financialmodelingprep.com/developer/docs#general-search-company-search
    
def ticker_search(self, query: str, limit: int = None, exchange: str = None) -> pd.DataFrame:
    Referance: https://site.financialmodelingprep.com/developer/docs#ticker-search-company-search
    
def name_search(self, query: str, limit: int = None, exchange: str = None) -> pd.DataFrame:
    Referance: https://site.financialmodelingprep.com/developer/docs#name-search-company-search
    
def cik_name_search(self,company_name: str) -> pd.DataFrame:
    Referance: https://site.financialmodelingprep.com/developer/docs#cik-name-search-company-search
    
def cik_search(self, cik: str) -> pd.DataFrame:
    Referance: https://site.financialmodelingprep.com/developer/docs#cik-search-company-search
    
def cusip_search(self, cusip: str) -> pd.DataFrame:
    Referance: https://site.financialmodelingprep.com/developer/docs#cusip-search-company-search
    
def isin_search(self, isin: str) -> pd.DataFrame:
    Referance: https://site.financialmodelingprep.com/developer/docs#isin-search-company-search
"""


class FmpCompanySearch(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")):
        super().__init__(api_key)

    ############################
    # ISIN Search
    ############################
    def isin_search(self, isin: str) -> pd.DataFrame:
        """
        Searches for a company using its ISIN (International Securities Identification Number).

        Args:
            isin (str): The ISIN of the company to search for.

        Returns:
            pd.DataFrame: A DataFrame containing the company information.

        Raises:
            ValueError: If no data is found for the specified parameters.
        """

        url = "v4/search/isin"
        params = {"isin": isin}

        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the specified parameters.")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "symbol": "symbol",
                    "price": "price",
                    "beta": "beta",
                    "volAvg": "vol_avg",
                    "mktCap": "mkt_cap",
                    "lastDiv": "last_div",
                    "range": "range",
                    "changes": "changes",
                    "companyName": "company_name",
                    "currency": "currency",
                    "cik": "cik",
                    "isin": "isin",
                    "cusip": "cusip",
                    "exchange": "exchange",
                    "exchangeShortName": "exchange_short_name",
                    "industry": "industry",
                    "website": "website",
                    "description": "description",
                    "ceo": "ceo",
                    "sector": "sector",
                    "fullTimeEmployees": "full_time_employees",
                    "phone": "phone",
                    "address": "address",
                    "city": "city",
                    "state": "state",
                    "zip": "zip",
                    "dcfDiff": "dcf_diff",
                    "dcf": "dcf",
                    "image": "image",
                    "ipoDate": "ipo_date",
                    "defaultImage": "default_image",
                    "isEtf": "is_etf",
                    "isActivelyTrading": "is_actively_trading",
                    "isAdr": "is_adr",
                    "isFund": "is_fund",
                }
            )
            .astype(
                {
                    "price": "float",
                    "beta": "float",
                    "vol_avg": "int",
                    "mkt_cap": "int",
                    "last_div": "int",
                    "changes": "float",
                    "full_time_employees": "int",
                    "dcf_diff": "float",
                    "dcf": "float",
                    "is_etf": "bool",
                    "is_actively_trading": "bool",
                    "is_adr": "bool",
                    "is_fund": "bool",
                    "default_image": "bool",
                    "ipo_date": "datetime64[ns]",
                }
            )
        )

    ############################
    # CUSIP Search
    ############################
    def cusip_search(self, cusip: str) -> pd.DataFrame:
        """
        Search for a company using its CUSIP identifier.

        Parameters:
        cusip (str): The CUSIP identifier of the company to search for.

        Returns:
        pd.DataFrame: A DataFrame containing the response data.

        Raises:
        ValueError: If no data is found for the specified parameters.
        """
        url = f"v3/cusip/{cusip}"
        response = self.get_request(url)

        if not response:
            raise ValueError("No data found for the specified parameters.")

        return pd.DataFrame(response)

    ############################
    # CIK Search
    ############################
    def cik_search(self, cik: str) -> pd.DataFrame:
        """
        Retrieves company information based on the specified CIK (Central Index Key).

        Args:
            cik (str): The CIK of the company.

        Returns:
            pd.DataFrame: A DataFrame containing the company information.

        Raises:
            ValueError: If no data is found for the specified parameters.
        """
        url = f"v3/cik/{cik}"
        response = self.get_request(url)

        if not response:
            raise ValueError("No data found for the specified parameters.")

        return pd.DataFrame(response)

    ############################
    # CIK Name Search
    ############################
    def cik_name_search(
        self,
        company_name: str,
    ) -> pd.DataFrame:
        """
        Searches for a company's CIK (Central Index Key) based on its name.

        Args:
            company_name (str): The name of the company to search for.

        Returns:
            pd.DataFrame: A DataFrame containing the response data.

        Raises:
            ValueError: If no data is found for the specified parameters.
        """
        url = f"v3/cik-search/{company_name}"
        response = self.get_request(url)

        if not response:
            raise ValueError("No data found for the specified parameters.")

        return pd.DataFrame(response)

    ############################
    # Name Search
    ############################
    def name_search(
        self, query: str, limit: int = None, exchange: str = None
    ) -> pd.DataFrame:
        """
        Search for company names based on the specified query.

        Args:
            query (str): The search query.
            limit (int, optional): The maximum number of results to return. Defaults to None.
            exchange (str, optional): The exchange to search within. Defaults to None.

        Returns:
            pd.DataFrame: A DataFrame containing the search results with columns:
                - symbol: The company symbol.
                - name: The company name.
                - currency: The currency in which the company operates.
                - stock_exchange: The stock exchange where the company is listed.
                - exchange_short_name: The short name of the exchange.

        Raises:
            ValueError: If an invalid exchange is provided.
            ValueError: If no data is found for the specified parameters.
        """
        url = "v3/search-name"
        return self._process_search_data(url, query, exchange, limit)

    ############################
    # Ticker Search
    ############################
    def ticker_search(
        self, query: str, limit: int = None, exchange: str = None
    ) -> pd.DataFrame:
        """
        Search for tickers based on the specified query, limit, and exchange.

        Args:
            query (str): The search query.
            limit (int, optional): The maximum number of results to return. Defaults to None.
            exchange (str, optional): The exchange to search for tickers. Defaults to None.

        Returns:
            pd.DataFrame: A DataFrame containing the search results with columns:
                - symbol: The ticker symbol.
                - name: The company name.
                - currency: The currency in which the stock is traded.
                - stock_exchange: The stock exchange where the stock is listed.
                - exchange_short_name: The short name of the exchange.

        Raises:
            ValueError: If an invalid exchange is provided.
            ValueError: If no data is found for the specified parameters.
        """
        url = "v3/search"
        return self._process_search_data(url, query, exchange, limit)

    ############################
    # General Search
    ############################
    def general_search(
        self, query: str, exchange: str = None, limit: int = None
    ) -> pd.DataFrame:
        """
        Perform a general search for companies based on the specified query.

        Args:
            query (str): The search query.
            exchange (str, optional): The exchange to filter the search results. Defaults to None.
            limit (int, optional): The maximum number of search results to return. Defaults to None.

        Returns:
            pd.DataFrame: A DataFrame containing the search results with the following columns:
                - symbol: The company symbol.
                - name: The company name.
                - currency: The currency in which the company is traded.
                - stock_exchange: The stock exchange where the company is listed.
                - exchange_short_name: The short name of the exchange.

        Raises:
            ValueError: If an invalid exchange is provided.
            ValueError: If no data is found for the specified parameters.
        """
        url = "v3/search"
        return self._process_search_data(url, query, exchange, limit)

    def _process_search_data(
        self, url: str, query: str, exchange: str, limit: int
    ) -> pd.DataFrame:
        if exchange and exchange not in self._available_exchanges():
            raise ValueError(
                f"Invalid exchange: {exchange}. Please choose from {self._available_exchanges()}."
            )

        params = {"query": query, "limit": limit, "exchange": exchange}

        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the specified parameters.")

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
            .sort_values(by="symbol")
            .reset_index(drop=True)
        )

    ############################
    # Available Exchanges
    ############################
    @staticmethod
    def _available_exchanges() -> list:
        """
        Returns a list of available exchanges.

        Returns:
            list: A list of available exchanges.
        """
        return [
            "AMEX",
            "AMS",
            "AQS",
            "ASX",
            "ATH",
            "BER",
            "BME",
            "BRU",
            "BSE",
            "BUD",
            "BUE",
            "CAI",
            "CBOE",
            "CNQ",
            "CPH",
            "DFM",
            "DOH",
            "DUS",
            "DXE",
            "ETF",
            "EURONEXT",
            "HAM",
            "HEL",
            "HKSE",
            "ICE",
            "IOB",
            "IST",
            "JKT",
            "JNB",
            "JPX",
            "KLS",
            "KOE",
            "KSC",
            "KUW",
            "LSE",
            "MCX",
            "MEX",
            "MIL",
            "MUN",
            "NASDAQ",
            "NEO",
            "NIM",
            "NSE",
            "NYSE",
            "NZE",
            "OEM",
            "OQB",
            "OQX",
            "OSL",
            "OTC",
            "PNK",
            "PRA",
            "RIS",
            "SAO",
            "SAU",
            "SES",
            "SET",
            "SGO",
            "SHH",
            "SHZ",
            "SIX",
            "STO",
            "STU",
            "TAI",
            "TLV",
            "TSX",
            "TSXV",
            "TWO",
            "VIE",
            "VSE",
            "WSE",
            "XETRA",
        ]
