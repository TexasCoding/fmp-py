import pandas as pd
from fmp_py.fmp_base import FmpBase
import os
import pendulum
from dotenv import load_dotenv

load_dotenv()


"""
This class provides methods for retrieving IPO calendar data from the Financial Modeling Prep API.
Ref: https://site.financialmodelingprep.com/developer/docs#ipo-calendar

def ipo_calendar_by_symbol(self, from_date: str, to_date: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#ipo-confirmed-ipo-calendar
    
def ipo_prospectus(self, from_date: str, to_date: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#ipo-prospectus-ipo-calendar

def ipo_confirmed(self, from_date: str, to_date: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#ipo-calender-by-ipo-calendar
"""


class FmpIpoCalendar(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")):
        super().__init__(api_key)

    #############################
    # IPO Calendar by Symbol
    #############################
    def ipo_calendar_by_symbol(self, from_date: str, to_date: str) -> pd.DataFrame:
        """
        Retrieves IPO calendar data for a specific symbol within a given date range.
        Args:
            from_date (str): The starting date of the date range in "YYYY-MM-DD" format.
            to_date (str): The ending date of the date range in "YYYY-MM-DD" format.
        Returns:
            pd.DataFrame: A DataFrame containing IPO calendar data for the specified symbol within the given date range.
        """

        from_date = pendulum.parse(from_date).format("YYYY-MM-DD")
        to_date = pendulum.parse(to_date).format("YYYY-MM-DD")
        if from_date > to_date:
            raise ValueError("from_date must be less than or equal to to_date")

        url = "v3/ipo_calendar"
        params = {"from": from_date, "to": to_date}

        response = self.get_request(url, params)

        if not response:
            raise ValueError("Error fetching IPO calendar data")

        data_df = (
            pd.DataFrame(response)
            .fillna(0)
            .rename(
                columns={
                    "date": "date",
                    "company": "company",
                    "symbol": "symbol",
                    "exchange": "exchange",
                    "actions": "actions",
                    "shares": "shares",
                    "priceRange": "price_range",
                    "marketCap": "market_cap",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "company": "str",
                    "symbol": "str",
                    "exchange": "str",
                    "actions": "str",
                    "shares": "int",
                    "price_range": "string",
                    "market_cap": "int",
                }
            )
            .sort_values(by="date", ascending=True)
            .reset_index(drop=True)
        )

        return data_df

    #############################
    # IPO Prspectus
    #############################
    def ipo_prospectus(self, from_date: str, to_date: str) -> pd.DataFrame:
        """
        Retrieves IPO prospectus data from the specified date range.
        Args:
            from_date (str): The starting date of the date range in "YYYY-MM-DD" format.
            to_date (str): The ending date of the date range in "YYYY-MM-DD" format.
        Returns:
            pd.DataFrame: A DataFrame containing IPO prospectus data with the following columns:
                - symbol (str): The symbol of the IPO.
                - cik (str): The CIK (Central Index Key) of the IPO.
                - form (str): The form type of the IPO.
                - filing_date (datetime64[ns]): The filing date of the IPO.
                - accepted_date (datetime64[ns]): The accepted date of the IPO.
                - ipo_date (datetime64[ns]): The IPO date.
                - price_public_per_share (float): The price per share for the public offering.
                - price_public_total (float): The total price for the public offering.
                - discounts_and_commissions_per_share (float): The discounts and commissions per share.
                - discounts_and_commissions_total (float): The total discounts and commissions.
                - proceeds_before_expenses_per_share (float): The proceeds per share before expenses.
                - proceeds_before_expenses_total (float): The total proceeds before expenses.
                - url (str): The URL of the IPO prospectus.
        Raises:
            ValueError: If from_date is greater than to_date or if there is an error fetching the IPO calendar data.
        """

        from_date = pendulum.parse(from_date).format("YYYY-MM-DD")
        to_date = pendulum.parse(to_date).format("YYYY-MM-DD")
        if from_date > to_date:
            raise ValueError("from_date must be less than or equal to to_date")

        url = "v4/ipo-calendar-prospectus"
        params = {"from": from_date, "to": to_date}

        response = self.get_request(url, params)

        if not response:
            raise ValueError("Error fetching IPO calendar data")

        data_df = (
            pd.DataFrame(response)
            .fillna("")
            .rename(
                columns={
                    "symbol": "symbol",
                    "cik": "cik",
                    "form": "form",
                    "filingDate": "filing_date",
                    "acceptedDate": "accepted_date",
                    "ipoDate": "ipo_date",
                    "pricePublicPerShare": "price_public_per_share",
                    "pricePublicTotal": "price_public_total",
                    "discountsAndCommissionsPerShare": "discounts_and_commissions_per_share",
                    "discountsAndCommissionsTotal": "discounts_and_commissions_total",
                    "proceedsBeforeExpensesPerShare": "proceeds_before_expenses_per_share",
                    "proceedsBeforeExpensesTotal": "proceeds_before_expenses_total",
                    "url": "url",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "cik": "str",
                    "form": "str",
                    "filing_date": "datetime64[ns]",
                    "accepted_date": "datetime64[ns]",
                    "ipo_date": "datetime64[ns]",
                    "price_public_per_share": "float",
                    "price_public_total": "float",
                    "discounts_and_commissions_per_share": "float",
                    "discounts_and_commissions_total": "float",
                    "proceeds_before_expenses_per_share": "float",
                    "proceeds_before_expenses_total": "float",
                    "url": "str",
                }
            )
            .sort_values(by="filing_date", ascending=True)
            .reset_index(drop=True)
        )

        return data_df

    #############################
    # IPO Confirmed
    #############################
    def ipo_confirmed(self, from_date: str, to_date: str) -> pd.DataFrame:
        """
        Retrieves the IPO calendar data for confirmed IPOs within the specified date range.
        Args:
            from_date (str): The start date of the date range in the format "YYYY-MM-DD".
            to_date (str): The end date of the date range in the format "YYYY-MM-DD".
        Returns:
            pd.DataFrame: A DataFrame containing the IPO calendar data for confirmed IPOs, sorted by filing date.
        Raises:
            ValueError: If from_date is greater than to_date or if there is an error fetching the IPO calendar data.
        """

        from_date = pendulum.parse(from_date).format("YYYY-MM-DD")
        to_date = pendulum.parse(to_date).format("YYYY-MM-DD")
        if from_date > to_date:
            raise ValueError("from_date must be less than or equal to to_date")

        url = "v4/ipo-calendar-confirmed"
        params = {"from": from_date, "to": to_date}

        response = self.get_request(url, params)

        if not response:
            raise ValueError("Error fetching IPO calendar data")

        data_df = (
            pd.DataFrame(response)
            .fillna("")
            .rename(
                columns={
                    "symbol": "symbol",
                    "cik": "cik",
                    "form": "form",
                    "filingDate": "filing_date",
                    "acceptedDate": "accepted_date",
                    "effectivenessDate": "effectiveness_date",
                    "url": "url",
                }
            )
            .astype(
                {
                    "symbol": "string",
                    "cik": "string",
                    "form": "string",
                    "filing_date": "datetime64[ns]",
                    "accepted_date": "datetime64[ns]",
                    "effectiveness_date": "datetime64[ns]",
                    "url": "string",
                }
            )
            .sort_values(by="filing_date", ascending=True)
            .reset_index(drop=True)
        )

        return data_df
