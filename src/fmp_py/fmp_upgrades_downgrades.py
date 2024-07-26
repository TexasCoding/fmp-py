import pandas as pd
import pendulum
from fmp_py.fmp_base import FmpBase
from fmp_py.models.upgrades_downgrades import UpgradesDowngrades

import os
from dotenv import load_dotenv

load_dotenv()


"""
The FmpUpgradesDowngrades class provides methods for retrieving upgrade/downgrade data from the Financial Modeling Prep API.
Reference: https://site.financialmodelingprep.com/developer/docs#upgrades-downgrades
    
def upgrades_downgrades(self, symbol: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#upgrades-downgrades-search
    
def upgrades_downgrades_rss_feed(self, page: int = 0) -> pd.DataFrame:
     Reference: https://site.financialmodelingprep.com/developer/docs#up-down-grades-rss-feed
     
def upgrades_downgrades_by_company(self, company: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#up-down-grades-by-company
    
def upgrades_downgrades_consensus(self, symbol: str) -> UpgradesDowngrades:
    Reference: https://site.financialmodelingprep.com/developer/docs#up-down-grades-consensus
"""


class FMPUpgradesDowngrades(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")) -> None:
        super().__init__(api_key)

    ############################
    # Upgrades Downgrades Consensus
    ############################
    def upgrades_downgrades_consensus(self, symbol: str) -> UpgradesDowngrades:
        """
        Retrieves the upgrades and downgrades consensus data for a given symbol.

        Args:
            symbol (str): The symbol of the stock.

        Returns:
            UpgradesDowngrades: An instance of the UpgradesDowngrades class containing the consensus data.

        Raises:
            ValueError: If no data is found for the specified parameters.
        """
        url = "v4/upgrades-downgrades-consensus"
        params = {"symbol": symbol, "apikey": self.api_key}

        try:
            response = self.get_request(url, params)[0]
        except IndexError:
            raise ValueError("No data found for the specified parameters.")

        data_dict = {
            "symbol": self.clean_value(response.get("symbol", ""), str),
            "strong_buy": self.clean_value(response.get("strongBuy", 0), int),
            "strong_sell": self.clean_value(response.get("strongSell", 0), int),
            "buy": self.clean_value(response.get("buy", 0), int),
            "sell": self.clean_value(response.get("sell", 0), int),
            "hold": self.clean_value(response.get("hold", 0), int),
            "consensus": self.clean_value(response.get("consensus", ""), str),
        }

        return UpgradesDowngrades(**data_dict)

    ############################
    # Upgrades Downgrades by Company
    ############################
    def upgrades_downgrades_by_company(self, company: str) -> pd.DataFrame:
        """
        Retrieves upgrades and downgrades grading data for a specific company.

        Args:
            company (str): The name of the company.

        Returns:
            pd.DataFrame: A DataFrame containing the upgrades and downgrades grading data for the specified company.

        Raises:
            ValueError: If no data is found for the specified company.
        """
        url = "v4/upgrades-downgrades-grading-company"
        params = {"company": company, "apikey": self.api_key}

        try:
            return self._process_data(url=url, params=params)
        except ValueError:
            raise ValueError(f"No data found for {company}.")

    ############################
    # Upgrades Downgrades RSS Feed
    ############################
    def upgrades_downgrades_rss_feed(self, page: int = 0) -> pd.DataFrame:
        """
        Retrieves the upgrades and downgrades RSS feed data from the Financial Modeling Prep API.

        Args:
            page (int): The page number of the RSS feed to retrieve. Default is 0.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the upgrades and downgrades data.

        Raises:
            ValueError: If no data is found for the specified parameters.
        """
        url = "v4/upgrades-downgrades-rss-feed"
        params = {"page": page, "apikey": self.api_key}

        try:
            return self._process_data(url=url, params=params)
        except ValueError:
            raise ValueError("No data found for the specified parameters.")

    ############################
    # Upgrades Downgrades
    ############################
    def upgrades_downgrades(self, symbol: str) -> pd.DataFrame:
        """
        Retrieves upgrades and downgrades data for a given symbol.

        Args:
            symbol (str): The symbol for which to retrieve upgrades and downgrades data.

        Returns:
            pd.DataFrame: A DataFrame containing the upgrades and downgrades data, sorted by published date.

        Raises:
            ValueError: If no data is found for the given symbol.
        """
        url = "v4/upgrades-downgrades"
        params = {"symbol": symbol, "apikey": self.api_key}

        try:
            return self._process_data(url=url, params=params)
        except ValueError:
            raise ValueError("No data found for the given symbol.")

    ############################
    # Private Methods
    ############################
    def _process_data(self, url: str, params: dict) -> pd.DataFrame:
        """
        Process the data obtained from the API response.

        Args:
            url (str): The URL for the API request.
            params (dict): The parameters for the API request.

        Returns:
            pd.DataFrame: A DataFrame containing the processed data.

        Raises:
            ValueError: If no data is found for the given symbol.
        """

        response = self.get_request(url=url, params=params)

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
                    "newsBaseURL": "news_base_url",
                    "newsPublisher": "news_publisher",
                    "newGrade": "new_grade",
                    "previousGrade": "previous_grade",
                    "gradingCompany": "grading_company",
                    "action": "action",
                    "priceWhenPosted": "price_when_posted",
                }
            )
        )

        data_df["published_date"] = data_df["published_date"].apply(
            lambda x: pendulum.parse(x).to_datetime_string()
        )

        return (
            data_df.sort_values("published_date", ascending=True)
            .reset_index(drop=True)
            .astype(
                {
                    "symbol": "str",
                    "published_date": "datetime64[ns]",
                    "news_url": "str",
                    "news_title": "str",
                    "news_base_url": "str",
                    "news_publisher": "str",
                    "new_grade": "str",
                    "previous_grade": "str",
                    "grading_company": "str",
                    "action": "str",
                    "price_when_posted": "float",
                }
            )
        )
