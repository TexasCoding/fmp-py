from fmp_py.fmp_base import FmpBase
import os
import pendulum
from dotenv import load_dotenv

from fmp_py.models.quote import Quote

load_dotenv()

"""
def full_quote(self, symbol: str):
    Reference: https://site.financialmodelingprep.com/developer/docs#full-quote-quote

def quote_order(self, symbol: str):
    Reference: https://site.financialmodelingprep.com/developer/docs#quote-order-quote
"""


class FmpQuote(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")):
        super().__init__(api_key)

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
