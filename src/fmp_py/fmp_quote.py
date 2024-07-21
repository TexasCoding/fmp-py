import pandas as pd
from fmp_py.fmp_base import FmpBase
import os
import pendulum
from dotenv import load_dotenv

from fmp_py.models.quote import OtcQuote, PriceChange, Quote, SimpleQuote

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
"""


class FmpQuote(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")):
        super().__init__(api_key)

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
