import pandas as pd
from fmp_py.fmp_base import FmpBase
import os
import pendulum
from dotenv import load_dotenv

load_dotenv()

pd.set_option("future.no_silent_downcasting", True)


"""
This module provides functions to retrieve earnings data from the Financial Modeling Prep API.
References:
    - https://site.financialmodelingprep.com/developer/docs#earnings
    
def earnings_surprises(self, symbol: str) -> pd.DataFrame:
    References: https://site.financialmodelingprep.com/developer/docs#earnings-surprises-earnings
    
def earnings_historical(self, symbol: str) -> pd.DataFrame:
    References: https://site.financialmodelingprep.com/developer/docs#earnings-historical-earnings

def earnings_calendar(self, from_date: str, to_date: str) -> pd.DataFrame:
    References: https://site.financialmodelingprep.com/developer/docs#earnings-calendar-earnings

def earnings_within_weeks(self, symbol: str, weeks_ahead: int = 2) -> bool:
    References: This function is not documented in the Financial Modeling Prep API documentation.
                It is a custom function that is not documented in the Financial Modeling Prep API documentation.

def earnings_confirmed(self, symbol: str, date: str) -> pd.DataFrame:
    References: https://site.financialmodelingprep.com/developer/docs#earnings-confirmed-earnings
"""


class FmpEarnings(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")):
        super().__init__(api_key)

    #############################
    # Earnings Surprises
    #############################
    def earnings_surprises(self, symbol: str) -> pd.DataFrame:
        """
        Retrieves the earnings surprises for a given symbol.
        Args:
            symbol (str): The symbol of the stock.
        Returns:
            pd.DataFrame: A DataFrame containing the earnings surprises data.
        """
        url = f"v3/earnings-surprises/{symbol}"
        response = self.get_request(url)

        if not response:
            raise ValueError("Error fetching earnings surprises data")

        data_df = (
            (
                pd.DataFrame(response)
                .fillna(0)
                .rename(
                    columns={
                        "symbol": "symbol",
                        "date": "date",
                        "actualEarningResult": "actual_earning_result",
                        "estimatedEarning": "estimated_earning",
                    }
                )
                .astype(
                    {
                        "symbol": "string",
                        "date": "datetime64[ns]",
                        "actual_earning_result": "float",
                        "estimated_earning": "float",
                    }
                )
            )
            .sort_values(by="date", ascending=True)
            .reset_index(drop=True)
        )

        return data_df

    #############################
    # Earnings Confirmed
    #############################
    def earnings_confirmed(self, from_date: str, to_date: str) -> pd.DataFrame:
        """
        Fetches the confirmed earnings calendar data from the specified date range.
        Args:
            from_date (str): The starting date of the range in the format 'YYYY-MM-DD'.
            to_date (str): The ending date of the range in the format 'YYYY-MM-DD'.
        Returns:
            pd.DataFrame: A DataFrame containing the fetched earnings calendar data, with the following columns:
                - symbol: The symbol of the company.
                - exchange: The exchange where the company is listed.
                - time: The time of the earnings release.
                - when: The time period of the earnings release (e.g., 'Before Market Open', 'After Market Close').
                - date: The date of the earnings release.
                - publication_date: The publication date of the earnings release.
                - title: The title of the earnings release.
                - url: The URL of the earnings release.
        Raises:
            ValueError: If there is an error fetching the earnings calendar data.
        """
        from_date = pendulum.parse(from_date).format("YYYY-MM-DD")
        to_date = pendulum.parse(to_date).format("YYYY-MM-DD")
        if from_date > to_date:
            raise ValueError("from_date must be less than or equal to to_date")

        url = "v4/earning-calendar-confirmed"
        params = {"from": from_date, "to": to_date}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("Error fetching earnings calendar data")

        data_df = (
            (
                pd.DataFrame(response)
                .fillna(0)
                .rename(
                    columns={
                        "symbol": "symbol",
                        "exchange": "exchange",
                        "time": "time",
                        "when": "when",
                        "date": "date",
                        "publicationDate": "publication_date",
                        "title": "title",
                        "url": "url",
                    }
                )
                .astype(
                    {
                        "symbol": "string",
                        "exchange": "string",
                        "time": "string",
                        "when": "string",
                        "date": "datetime64[ns]",
                        "publication_date": "datetime64[ns]",
                        "title": "string",
                        "url": "string",
                    }
                )
            )
            .sort_values(by="date", ascending=True)
            .reset_index(drop=True)
        )

        return data_df

    #############################
    # Earnings Calendar
    #############################
    def earnings_calendar(self, from_date: str, to_date: str) -> pd.DataFrame:
        """
        Retrieves the earnings calendar data from the specified date range.
        Args:
            from_date (str): The starting date of the earnings calendar data in "YYYY-MM-DD" format.
            to_date (str): The ending date of the earnings calendar data in "YYYY-MM-DD" format.
        Returns:
            pd.DataFrame: A DataFrame containing the earnings calendar data with the following columns:
                - date: The date of the earnings release.
                - symbol: The symbol of the company.
                - eps: The earnings per share.
                - eps_estimated: The estimated earnings per share.
                - time: The time of the earnings release.
                - revenue: The revenue.
                - revenue_estimated: The estimated revenue.
                - fiscal_date_ending: The fiscal date ending.
                - updated_from_date: The updated from date.
        Raises:
            ValueError: If from_date is greater than to_date or if there is an error fetching the earnings calendar data.
        """

        from_date = pendulum.parse(from_date).format("YYYY-MM-DD")
        to_date = pendulum.parse(to_date).format("YYYY-MM-DD")
        if from_date > to_date:
            raise ValueError("from_date must be less than or equal to to_date")

        url = "v3/earning_calendar"
        params = {"from": from_date, "to": to_date}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("Error fetching earnings calendar data")

        data_df = (
            pd.DataFrame(response)
            .fillna(0)
            .rename(
                columns={
                    "date": "date",
                    "symbol": "symbol",
                    "eps": "eps",
                    "epsEstimated": "eps_estimated",
                    "time": "time",
                    "revenue": "revenue",
                    "revenueEstimated": "revenue_estimated",
                    "fiscalDateEnding": "fiscal_date_ending",
                    "updatedFromDate": "updated_from_date",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "symbol": "string",
                    "eps": "float",
                    "eps_estimated": "float",
                    "time": "string",
                    "revenue": "int",
                    "revenue_estimated": "int",
                    "fiscal_date_ending": "datetime64[ns]",
                    "updated_from_date": "datetime64[ns]",
                }
            )
            .sort_values(by="date", ascending=True)
            .reset_index(drop=True)
        )

        return data_df

    #############################
    # Earnings Historical
    #############################
    def earnings_historical(self, symbol: str) -> pd.DataFrame:
        """
        Fetches historical earnings data for a given symbol.
        Args:
            symbol (str): The symbol for which to fetch earnings data.
        Returns:
            pd.DataFrame: A DataFrame containing the historical earnings data, with the following columns:
                - date (datetime64[ns]): The date of the earnings release.
                - symbol (str): The symbol of the company.
                - eps (float): The earnings per share.
                - revenue (int): The revenue.
                - eps_estimated (float): The estimated earnings per share.
                - revenue_estimated (int): The estimated revenue.
                - time (str): The time of the earnings release.
                - updated_from_date (datetime64[ns]): The date from which the data was last updated.
                - fiscal_date_ending (datetime64[ns]): The fiscal date ending.
        Raises:
            ValueError: If there is an error fetching the earnings historical data.
        """

        url = f"v3/historical/earning_calendar/{symbol}"
        response = self.get_request(url)

        if not response:
            raise ValueError("Error fetching earnings historical data")

        data_df = (
            pd.DataFrame(response)
            .fillna(0)
            .rename(
                columns={
                    "date": "date",
                    "symbol": "symbol",
                    "eps": "eps",
                    "revenue": "revenue",
                    "epsEstimated": "eps_estimated",
                    "revenueEstimated": "revenue_estimated",
                    "time": "time",
                    "updatedFromDate": "updated_from_date",
                    "fiscalDateEnding": "fiscal_date_ending",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "time": "str",
                    "updated_from_date": "datetime64[ns]",
                    "fiscal_date_ending": "datetime64[ns]",
                    "eps": "float",
                    "revenue": "int",
                    "eps_estimated": "float",
                    "revenue_estimated": "int",
                },
                errors="ignore",
            )
            .sort_values(by="date", ascending=True)
        )

        return data_df

    #############################
    # Earnings Within Weeks
    #############################
    def earnings_within_weeks(self, symbol: str, weeks_ahead: int = 2) -> bool:
        """
        Checks if there are earnings within a specified number of weeks ahead.
        Args:
            symbol (str): The symbol of the stock.
            weeks_ahead (int, optional): The number of weeks ahead to check for earnings. Defaults to 2.
        Returns:
            bool: True if there are earnings within the specified number of weeks ahead, False otherwise.
        """

        try:
            earnings_history = self.earnings_historical(symbol)

            todays_date = pd.to_datetime(pendulum.today().to_date_string())
            future_date = pd.to_datetime(
                pendulum.today().add(weeks=weeks_ahead).to_date_string()
            )

            earnings_history = earnings_history[earnings_history["date"] >= todays_date]
            earnings_history = earnings_history[earnings_history["date"] <= future_date]

            if earnings_history.empty:
                return False

        except ValueError:
            return False

        return True
