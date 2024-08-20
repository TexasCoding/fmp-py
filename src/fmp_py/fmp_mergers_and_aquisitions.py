import pandas as pd
from fmp_py.fmp_base import FmpBase
import os
from dotenv import load_dotenv

load_dotenv()


"""
The FmpMergersAndAquisitions class provides methods for retrieving mergers and acquisitions data from the Financial Modeling Prep API.
Refer to the official documentation (https://site.financialmodelingprep.com/developer/docs#mergers-&-acquisitions) for more information.

def ma_rss_feed(self, page: int = 0) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#m&a-rss-feed-mergers-&-acquisitions

def search_ma(self, query: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#search-m&a-mergers-&-acquisitions
"""


class FmpMergersAndAquisitions(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")) -> None:
        super().__init__(api_key)

    #####################################
    # Mergers and Acquisitions Search
    #####################################
    def search_ma(self, name: str) -> pd.DataFrame:
        """
        Retrieves mergers and acquisitions data based on a search name.

        Args:
            name (str): The search name of company.

        Returns:
            pd.DataFrame: A DataFrame containing the mergers and acquisitions data.
        """
        url = "v4/mergers-acquisitions/search"
        params = {"name": name}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the specified parameters.")

        data_df = (
            pd.DataFrame(response)
            .fillna("")
            .rename(
                columns={
                    "companyName": "company_name",
                    "symbol": "symbol",
                    "targetedCompanyName": "targeted_company_name",
                    "targetedCik": "targeted_cik",
                    "targetedSymbol": "targeted_symbol",
                    "transactionDate": "transaction_date",
                    "acceptanceTime": "acceptance_time",
                    "url": "url",
                }
            )
            .astype(
                {
                    "company_name": "str",
                    "symbol": "str",
                    "targeted_company_name": "str",
                    "targeted_cik": "str",
                    "targeted_symbol": "str",
                    "transaction_date": "datetime64[ns]",
                    "acceptance_time": "datetime64[ns]",
                    "url": "str",
                }
            )
        )
        return data_df

    #####################################
    # Mergers and Acquisitions RSS Feed
    #####################################
    def ma_rss_feed(self, page: int = 0) -> pd.DataFrame:
        """
        Retrieves mergers and acquisitions data from the RSS feed.

        Args:
            page (int): The page number for the RSS feed.

        Returns:
            pd.DataFrame: A DataFrame containing the mergers and acquisitions data.
        """
        url = "v4/mergers-acquisitions-rss-feed"
        params = {"page": page}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the specified parameters.")

        data_df = (
            pd.DataFrame(response)
            .fillna("")
            .rename(
                columns={
                    "companyName": "company_name",
                    "symbol": "symbol",
                    "targetedCompanyName": "targeted_company_name",
                    "targetedCik": "targeted_cik",
                    "targetedSymbol": "targeted_symbol",
                    "transactionDate": "transaction_date",
                    "acceptanceTime": "acceptance_time",
                    "url": "url",
                }
            )
            .astype(
                {
                    "company_name": "str",
                    "symbol": "str",
                    "targeted_company_name": "str",
                    "targeted_cik": "str",
                    "targeted_symbol": "str",
                    "transaction_date": "datetime64[ns]",
                    "acceptance_time": "datetime64[ns]",
                    "url": "str",
                }
            )
        )
        return data_df
