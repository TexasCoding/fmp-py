from typing import List
import pandas as pd
from fmp_py.fmp_base import FmpBase
import os
import pendulum
from dotenv import load_dotenv

from fmp_py.models.quote import (
    AftermarketTrade,
    AftermarketQuote,
    ForexQuote,
    FxPrice,
    CryptoQuote,
    OtcQuote,
    PriceChange,
    Quote,
    RealtimeFullPrice,
    SimpleQuote,
)

load_dotenv()

"""
def full_quote(self, symbol: str) -> Quote:
    Reference: https://site.financialmodelingprep.com/developer/docs#full-quote-quote

def quote_order(self, symbol: str) -> Quote:
    Reference: https://site.financialmodelingprep.com/developer/docs#quote-order-quote
    
def simple_quote(self, symbol: str) -> SimpleQuote:
    Reference: https://site.financialmodelingprep.com/developer/docs#simple-quote-quote
    
def otc_quote(self, symbol: str) -> OtcQuote:
    Reference: https://site.financialmodelingprep.com/developer/docs#otc-quote-quote

def exchange_prices(self, exchange: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#exchange-prices-quote
    
def stock_price_change(self, symbol: str) -> PriceChange:
    Reference: https://site.financialmodelingprep.com/developer/docs#stock-price-change-quote
    
def aftermarket_trade(self, symbol: str) -> AftermarketTrade:
    Reference: https://site.financialmodelingprep.com/developer/docs#aftermarket-trade-quote
    
def aftermarket_quote(self, symbol: str) -> AftermarketQuote:
    Reference: https://site.financialmodelingprep.com/developer/docs#aftermarket-quote-quote
    
def batch_quote(self, symbols: list) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#batch-quote-quote
    
def batch_trade(self, symbols: list) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#batch-trade-quote
    
def last_forex(self, symbol: str) -> ForexQuote:
    Reference: https://site.financialmodelingprep.com/developer/docs#last-forex-quote
    
def last_crypto(self, symbol: str) -> CryptoQuote:
    Reference: https://site.financialmodelingprep.com/developer/docs#last-crypto-quote
    
def live_full_stock_price(self, symbol: str) -> Quote:
    Reference: https://site.financialmodelingprep.com/developer/docs#real-time-full-price-quote
    
def all_live_full_stock_prices(self) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#all-realtime-full-prices-quote
    
def fx_price(self, symbol: str) -> FxPrice:
    Reference: https://site.financialmodelingprep.com/developer/docs#fx-price-quote
    
def fx_prices(self) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#all-fx-prices-quote
"""


class FmpQuote(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")):
        super().__init__(api_key)

    ##########################
    # FX Prices
    ##########################
    def fx_prices(self) -> pd.DataFrame:
        """
        Retrieves foreign exchange prices from the API and returns them as a pandas DataFrame.

        Returns:
            pd.DataFrame: A DataFrame containing the foreign exchange prices.
        """
        url = "v3/fx"
        params = {"apikey": self.api_key}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("Error retrieving data")

        data_df = pd.DataFrame(response).astype(
            {
                "ticker": "str",
                "bid": "float",
                "ask": "float",
                "open": "float",
                "high": "float",
                "low": "float",
                "changes": "float",
                "date": "datetime64[ns]",
            }
        )

        return data_df.sort_values(by="ticker", ascending=True).reset_index(drop=True)

    ###########################
    # FX Prices
    ###########################
    def fx_price(self, symbol: str) -> FxPrice:
        """
        Retrieves the foreign exchange price for a given symbol.

        Args:
            symbol (str): The symbol of the foreign exchange.

        Returns:
            FxPrice: An instance of the FxPrice class containing the retrieved data.

        Raises:
            ValueError: If there is an error retrieving the data.
        """
        url = f"v3/fx/{symbol}"
        params = {"apikey": self.api_key}

        try:
            response = self.get_request(url, params)[0]
        except IndexError:
            raise ValueError("Error retrieving data")

        data_dict = {
            "ticker": str(response["ticker"]),
            "ask": float(response["ask"]),
            "bid": float(response["bid"]),
            "open": float(response["open"]),
            "low": float(response["low"]),
            "high": float(response["high"]),
            "changes": float(response["changes"]),
            "date": pendulum.parse(response["date"]).strftime("%Y-%m-%d %H:%M:%S"),
        }

        return FxPrice(**data_dict)

    ###########################
    # All Live Full Stock Prices
    ###########################
    def all_live_full_stock_prices(self) -> pd.DataFrame:
        """
        Retrieves all live full stock prices from the API.

        Returns:
            pd.DataFrame: A DataFrame containing the live full stock prices.
        """
        url = "v3/stock/full/real-time-price"
        params = {"apikey": self.api_key}

        response = self.get_request(url, params)

        if not response:
            raise ValueError("Error retrieving data")

        data_df = pd.DataFrame(response).rename(
            columns={
                "symbol": "symbol",
                "volume": "volume",
                "askPrice": "ask_price",
                "askSize": "ask_size",
                "bidPrice": "bid_price",
                "bidSize": "bid_size",
                "lastSalePrice": "last_sale_price",
                "lastSaleSize": "last_sale_size",
                "lastSaleTime": "last_sale_time",
                "fmpLast": "fmp_last",
                "lastUpdated": "last_updated",
            }
        )

        data_df["last_sale_time"] = pd.to_datetime(data_df["last_sale_time"], unit="ms")
        data_df["last_updated"] = pd.to_datetime(data_df["last_updated"], unit="ms")

        return (
            data_df.astype(
                {
                    "symbol": "str",
                    "volume": "int",
                    "ask_price": "float",
                    "ask_size": "int",
                    "bid_price": "float",
                    "bid_size": "int",
                    "last_sale_price": "float",
                    "last_sale_size": "int",
                    "last_sale_time": "datetime64[ns]",
                    "fmp_last": "float",
                    "last_updated": "datetime64[ns]",
                }
            )
            .sort_values(["symbol"], ascending=True)
            .reset_index(drop=True)
        )

    ###########################
    # Live Full Stock Price
    ###########################
    def live_full_stock_price(self, symbol: str) -> RealtimeFullPrice:
        """
        Retrieves the real-time full stock price for a given symbol.

        Args:
            symbol (str): The stock symbol.

        Returns:
            RealtimeFullPrice: An instance of the RealtimeFullPrice class containing the retrieved data.

        Raises:
            ValueError: If there is an error retrieving the data.
        """
        url = f"v3/stock/full/real-time-price/{symbol}"
        params = {"apikey": self.api_key}

        try:
            response = self.get_request(url, params)[0]
        except IndexError as e:
            raise ValueError(f"Error retrieving data: {e}")

        data_dict = {
            "symbol": str(response["symbol"]),
            "volume": int(response["volume"]),
            "ask_price": float(response["askPrice"]),
            "ask_size": int(response["askSize"]),
            "bid_price": float(response["bidPrice"]),
            "bid_size": int(response["bidSize"]),
            "last_sale_price": float(response["lastSalePrice"]),
            "last_sale_size": int(response["lastSaleSize"]),
            "last_sale_time": pendulum.from_timestamp(
                response["lastSaleTime"] / 1000, tz="America/New_York"
            ).strftime("%Y-%m-%d %H:%M:%S"),
            "fmp_last": float(response["fmpLast"]),
            "last_updated": pendulum.from_timestamp(
                response["lastUpdated"] / 1000, tz="America/New_York"
            ).strftime("%Y-%m-%d %H:%M:%S"),
        }

        return RealtimeFullPrice(**data_dict)

    ###########################
    # Last Crypto
    ###########################
    def last_crypto(self, symbol: str) -> CryptoQuote:
        """
        Retrieves the last quote for a given cryptocurrency symbol.

        Args:
            symbol (str): The symbol of the cryptocurrency.

        Returns:
            CryptoQuote: An instance of the CryptoQuote class representing the last quote.

        Raises:
            ValueError: If there is an error retrieving the data or if no data is found for the symbol.
        """

        url = f"v4/crypto/last/{symbol}"
        params = {"apikey": self.api_key}
        try:
            response = self.get_request(url, params)
        except Exception as e:
            raise ValueError(f"Error retrieving data: {e}")

        if not response:
            raise ValueError(f"No data found for symbol: {symbol}")

        print(response["size"])

        data_dict = {
            "symbol": str(response["symbol"]),
            "price": float(response["price"]),
            "size": float(response["size"]),
            "timestamp": pendulum.from_timestamp(
                response["timestamp"] / 1000, tz="America/New_York"
            ).strftime("%Y-%m-%d %H:%M:%S"),
        }

        return CryptoQuote(**data_dict)

    ###########################
    # Last Forex
    ###########################
    def last_forex(self, symbol: str) -> ForexQuote:
        """
        Retrieves the last forex quote for the given symbol.

        Args:
            symbol (str): The symbol of the forex pair.

        Returns:
            ForexQuote: An instance of the ForexQuote class representing the last forex quote.

        Raises:
            ValueError: If no data is found for the given symbol.
        """
        url = f"v4/forex/last/{symbol}"
        params = {"apikey": self.api_key}

        try:
            response = self.get_request(url, params)
        except Exception as e:
            raise ValueError(f"Error retrieving data: {e}")

        if not response:
            raise ValueError("No data found for the given symbol")

        data_dict = {
            "symbol": str(response["symbol"]),
            "ask": float(response["ask"]),
            "bid": float(response["bid"]),
            "timestamp": pendulum.from_timestamp(
                response["timestamp"], tz="America/New_York"
            ).strftime("%Y-%m-%d %H:%M:%S"),
        }

        return ForexQuote(**data_dict)

    ###########################
    # Batch Trade
    ###########################
    def batch_trade(self, symbols: List[str]) -> pd.DataFrame:
        """
        Retrieves batch pre and post-market trade data for the given symbols.

        Args:
            symbols (List[str]): A list of symbols for which to retrieve trade data.

        Returns:
            pd.DataFrame: A DataFrame containing the trade data for the given symbols.

        Raises:
            ValueError: If symbols is not a list of symbols.
            ValueError: If no data is found for the given symbols.
        """

        if isinstance(symbols, str):
            raise ValueError("symbols must be a list of symbols")

        url = f"v4/batch-pre-post-market-trade/{','.join(symbols)}"
        params = {"apikey": self.api_key}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the given symbols")

        data_df = pd.DataFrame(response)

        data_df["timestamp"] = pd.to_datetime(data_df["timestamp"], unit="ms")

        return data_df.astype(
            {
                "timestamp": "datetime64[ns]",
                "symbol": "str",
                "price": "float",
                "size": "int",
            }
        )

    ###########################
    # Batch Quote
    ###########################
    def batch_quote(self, symbols: List[str]) -> pd.DataFrame:
        """
        Retrieves batch pre and post-market quotes for the given symbols.

        Args:
            symbols (List[str]): A list of symbols for which to retrieve quotes.

        Returns:
            pd.DataFrame: A DataFrame containing the batch quotes data.

        Raises:
            ValueError: If `symbols` is not a list of symbols.
            ValueError: If no data is found for the given symbols.
        """

        if isinstance(symbols, str):
            raise ValueError("symbols must be a list of symbols")

        url = f"v4/batch-pre-post-market/{','.join(symbols)}"
        params = {"apikey": self.api_key}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the given symbols")

        data_df = pd.DataFrame(response)

        data_df["timestamp"] = pd.to_datetime(data_df["timestamp"], unit="ms")

        return data_df.astype(
            {
                "timestamp": "datetime64[ns]",
                "ask": "float",
                "bid": "float",
                "asize": "int",
                "bsize": "int",
                "symbol": "str",
            }
        )

    ###########################
    # Aftermarket Quote
    ###########################
    def aftermarket_quote(self, symbol: str) -> AftermarketQuote:
        """
        Retrieves aftermarket quote data for a given symbol.

        Args:
            symbol (str): The symbol for which to retrieve the aftermarket quote.

        Returns:
            AftermarketQuote: An instance of the AftermarketQuote class containing the quote data.

        Raises:
            ValueError: If the symbol is invalid or not found.

        """
        url = f"v4/pre-post-market/{symbol}"
        params = {"apikey": self.api_key}

        try:
            response = self.get_request(url, params)
            data_dict = {
                "symbol": str(response["symbol"]),
                "ask": float(response["ask"]),
                "bid": float(response["bid"]),
                "asize": int(response["asize"]),
                "bsize": int(response["bsize"]),
                "timestamp": pendulum.from_timestamp(
                    response["timestamp"] / 1000, tz="America/New_York"
                ).strftime("%Y-%m-%d %H:%M:%S"),
            }
        except KeyError:
            raise ValueError(f"Invalid symbol: {symbol}")

        return AftermarketQuote(**data_dict)

    ###########################
    # Aftermarket Trade
    ###########################
    def aftermarket_trade(self, symbol: str) -> AftermarketTrade:
        """
        Retrieves aftermarket trade data for a given symbol.

        Args:
            symbol (str): The symbol for which to retrieve aftermarket trade data.

        Returns:
            AftermarketTrade: An instance of the AftermarketTrade class containing the retrieved data.

        Raises:
            ValueError: If no data is found for the specified symbol.
        """
        url = f"v4/pre-post-market-trade/{symbol}"
        params = {"apikey": self.api_key}

        try:
            response = self.get_request(url, params)
            data_dict = {
                "symbol": str(response["symbol"]),
                "price": float(response["price"]),
                "size": int(response["size"]),
                "timestamp": pendulum.from_timestamp(
                    response["timestamp"] / 1000, tz="America/New_York"
                ).strftime("%Y-%m-%d %H:%M:%S"),
            }
        except KeyError:
            raise ValueError(f"No data found for symbol: {symbol}")

        if not response:
            raise ValueError(f"No data found for symbol: {symbol}")

        return AftermarketTrade(**data_dict)

    ###########################
    # Stock Price Change
    ###########################
    def stock_price_change(self, symbol: str) -> PriceChange:
        """
        Retrieves the price change information for a given stock symbol.

        Args:
            symbol (str): The stock symbol for which to retrieve the price change information.

        Returns:
            PriceChange: An object containing the price change information for the specified stock symbol.

        Raises:
            ValueError: If no data is found for the specified stock symbol.
        """
        url = f"v3/stock-price-change/{symbol}"
        params = {"apikey": self.api_key}
        try:
            response = self.get_request(url, params)[0]
        except IndexError:
            raise ValueError(f"No data found for symbol: {symbol}")

        return PriceChange(
            symbol=str(response["symbol"]),
            day_1=float(response["1D"]),
            day_5=float(response["5D"]),
            month_1=float(response["1M"]),
            month_3=float(response["3M"]),
            month_6=float(response["6M"]),
            ytd=float(response["ytd"]),
            year_1=float(response["1Y"]),
            year_3=float(response["3Y"]),
            year_5=float(response["5Y"]),
            year_10=float(response["10Y"]),
            max=float(response["max"]),
        )

    ###########################
    # Exchange Prices
    ###########################
    def exchange_prices(self, exchange: str) -> pd.DataFrame:
        url = f"v3/quotes/{exchange}"
        params = {"apikey": self.api_key}

        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the given exchange.")

        data_df = pd.DataFrame(response)

        data_df["marketCap"] = data_df["marketCap"].fillna(0)
        data_df["volume"] = data_df["volume"].fillna(0)
        data_df["avgVolume"] = data_df["avgVolume"].fillna(0)
        data_df["sharesOutstanding"] = data_df["sharesOutstanding"].fillna(0)
        data_df["earningsAnnouncement"] = pd.to_datetime(
            data_df["earningsAnnouncement"].fillna("1970-02-28T21:00:00.000+0000"),
            format="%Y-%m-%dT%H:%M:%S.%f%z",
        ).dt.tz_convert(None)
        data_df["timestamp"] = pd.to_datetime(data_df["timestamp"], unit="s")

        return (
            data_df.rename(
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
                    "earningsAnnouncement": "earnings_date",
                    "sharesOutstanding": "shares_outstanding",
                    "timestamp": "datetime",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "name": "str",
                    "price": "float",
                    "change_percentage": "float",
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
                    "earnings_date": "datetime64[ms]",
                    "shares_outstanding": "int",
                    "datetime": "datetime64[ns]",
                }
            )
            .fillna(0)
            .sort_values(by="symbol", ascending=True)
            .reset_index(drop=True)
        )

    ###########################
    # OTC Quote
    ###########################
    def otc_quote(self, symbol: str) -> OtcQuote:
        """
        Retrieves real-time OTC quote for a given symbol.

        Args:
            symbol (str): The symbol for which to retrieve the quote.

        Returns:
            OtcQuote: An instance of the OtcQuote class containing the quote information.

        Raises:
            ValueError: If no data is found for the given symbol.
        """
        url = f"v3/otc/real-time-price/{symbol}"
        params = {"apikey": self.api_key}

        try:
            response = self.get_request(url, params)[0]
        except IndexError:
            raise ValueError(f"No data found for symbol: {symbol}")

        return OtcQuote(
            prev_close=float(response["prevClose"]),
            high=float(response["high"]),
            low=float(response["low"]),
            open=float(response["open"]),
            volume=int(response["volume"]),
            last_sale_price=float(response["lastSalePrice"]),
            fmp_last=float(response["fmpLast"]),
            last_updated=pendulum.parse(response["lastUpdated"]).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            symbol=str(response["symbol"]),
        )

    ###########################
    # Simple Quote
    ###########################
    def simple_quote(self, symbol: str) -> SimpleQuote:
        """
        Retrieves a simple quote for the specified symbol.

        Args:
            symbol (str): The symbol of the stock or security.

        Returns:
            SimpleQuote: An instance of the SimpleQuote class containing the symbol, price, and volume.

        Raises:
            ValueError: If the symbol is invalid.

        """
        url = f"v3/quote-short/{symbol}"
        params = {"apikey": self.api_key}
        try:
            response = self.get_request(url, params)[0]
        except IndexError:
            raise ValueError(f"Invalid symbol: {symbol}")

        return SimpleQuote(
            symbol=str(response["symbol"]),
            price=float(response["price"]),
            volume=int(response["volume"]),
        )

    ###########################
    # Quote Order
    ###########################
    def quote_order(self, symbol: str) -> Quote:
        """
        Retrieves the quote order for a given symbol.

        Args:
            symbol (str): The symbol for which to retrieve the quote order.

        Returns:
            Quote: The quote order for the specified symbol.
        """
        url = f"v3/quote-order/{symbol}"
        return self._process_quote(url)

    ##########################
    # Full Quote
    ##########################
    def full_quote(self, symbol: str) -> Quote:
        """
        Retrieves the full quote for a given symbol.

        Args:
            symbol (str): The symbol of the stock or security.

        Returns:
            Quote: The full quote information for the specified symbol.
        """
        url = f"v3/quote/{symbol}"
        return self._process_quote(url)

    ##########################
    # Helper Methods
    ##########################
    def _process_quote(self, url: str) -> Quote:
        """
        Process the quote data retrieved from the API response.

        Args:
            url (str): The URL used to retrieve the quote data.

        Returns:
            Quote: An instance of the Quote class containing the processed quote data.

        Raises:
            ValueError: If no data is found for the given symbol.
        """
        params = {"apikey": self.api_key}
        try:
            response = self.get_request(url, params)[0]
        except IndexError:
            raise ValueError("No data found for the given symbol.")

        data_dict = {
            "symbol": str(response["symbol"]),
            "name": str(response["name"]),
            "price": float(response["price"]),
            "change_percentage": float(response["changesPercentage"]),
            "change": float(response["change"]),
            "day_low": float(response["dayLow"]),
            "day_high": float(response["dayHigh"]),
            "year_low": float(response["yearLow"]),
            "year_high": float(response["yearHigh"]),
            "market_cap": int(response["marketCap"]),
            "price_avg_50": float(response["priceAvg50"]),
            "price_avg_200": float(response["priceAvg200"]),
            "volume": int(response["volume"]),
            "avg_volume": int(response["avgVolume"]),
            "exchange": str(response["exchange"]),
            "open": float(response["open"]),
            "previous_close": float(response["previousClose"]),
            "eps": float(response["eps"]),
            "pe": float(response["pe"]),
            "earnings_date": pendulum.parse(response["earningsAnnouncement"]).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "shares_outstanding": int(response["sharesOutstanding"]),
            "timestamp": pendulum.from_timestamp(response["timestamp"]).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }

        return Quote(**data_dict)
