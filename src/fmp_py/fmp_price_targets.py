import json
import pendulum
from fmp_py.fmp_base import FmpBase
from dotenv import load_dotenv
import os
import pandas as pd

from fmp_py.models.price_targets import PriceTargetConsensus, PriceTargetSummary

load_dotenv()

"""
The FmpPriceTargets class provides methods for retrieving price targets data from the Financial Modeling Prep API.
Reference: https://site.financialmodelingprep.com/developer/docs#price-targets

def price_target(self, symbol: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#price-target
    
def price_target_summary(self, symbol: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#price-target-summary
    
def price_target_consensus(self, symbol: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#price-target-consensus
"""


class FmpPriceTargets(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")) -> None:
        super().__init__(api_key)

    ############################
    # Price Target Consensus
    ############################
    def price_target_consensus(self, symbol: str) -> PriceTargetConsensus:
        """
        Retrieves the price target consensus for a given symbol.

        Args:
            symbol (str): The symbol of the stock.

        Returns:
            PriceTargetConsensus: An object containing the price target consensus information.

        Raises:
            ValueError: If no data is found for the specified parameters.
        """
        url = "v4/price-target-consensus"
        params = {"symbol": symbol, "apikey": self.api_key}

        try:
            response = self.get_request(url, params)[0]
        except IndexError:
            raise ValueError("No data found for the specified parameters.")

        return PriceTargetConsensus(
            symbol=str(response.get("symbol", "")),
            target_high=float(response.get("targetHigh", 0)),
            target_low=float(response.get("targetLow", 0)),
            target_consensus=float(response.get("targetConsensus", 0)),
            target_median=float(response.get("targetMedian", 0)),
        )

    ############################
    # Price Target Summary
    ############################
    def price_target_summary(self, symbol: str) -> PriceTargetSummary:
        url = "v4/price-target-summary"
        params = {"symbol": symbol, "apikey": self.api_key}

        try:
            response = self.get_request(url, params)[0]
        except IndexError:
            raise ValueError("No data found for the specified parameters.")

        return PriceTargetSummary(
            symbol=str(response.get("symbol", "")),
            last_month=int(response.get("lastMonth", 0)),
            last_month_avg_price_target=float(
                response.get("lastMonthAvgPriceTarget", 0)
            ),
            last_quarter=int(response.get("lastQuarter", 0)),
            last_quarter_avg_price_target=float(
                response.get("lastQuarterAvgPriceTarget", 0)
            ),
            last_year=int(response.get("lastYear", 0)),
            last_year_avg_price_target=float(response.get("lastYearAvgPriceTarget", 0)),
            all_time=int(response.get("allTime", 0)),
            all_time_avg_price_target=float(response.get("allTimeAvgPriceTarget", 0)),
            publishers=json.loads(response.get("publishers", [])),
        )

    ############################
    # Price Target
    ############################
    def price_target(self, symbol: str) -> pd.DataFrame:
        """
        Retrieves the price target data for a given symbol.

        Args:
            symbol (str): The symbol for which to retrieve the price target data.

        Returns:
            pd.DataFrame: A DataFrame containing the price target data, sorted by published date.

        Raises:
            ValueError: If no data is found for the given symbol.
        """
        url = "v4/price-target"
        params = {"symbol": symbol, "apikey": self.api_key}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the given symbol.")

        data_df = (
            pd.DataFrame(response)
            .fillna(0)
            .rename(
                columns={
                    "symbol": "symbol",
                    "publishedDate": "published_date",
                    "newsURL": "news_url",
                    "newsTitle": "news_title",
                    "analystName": "analyst_name",
                    "priceTarget": "price_target",
                    "adjPriceTarget": "adj_price_target",
                    "priceWhenPosted": "price_when_posted",
                    "newsPublisher": "news_publisher",
                    "newsBaseURL": "news_base_url",
                    "analystCompany": "analyst_company",
                }
            )
        )

        data_df["published_date"] = data_df["published_date"].apply(
            lambda x: pendulum.parse(x).to_datetime_string()
        )

        return (
            data_df.astype(
                {
                    "symbol": "str",
                    "published_date": "datetime64[ns]",
                    "news_url": "str",
                    "news_title": "str",
                    "analyst_name": "str",
                    "price_target": "float",
                    "adj_price_target": "float",
                    "price_when_posted": "float",
                    "news_publisher": "str",
                    "news_base_url": "str",
                    "analyst_company": "str",
                }
            )
            .sort_values(by="published_date", ascending=True)
            .reset_index(drop=True)
        )
