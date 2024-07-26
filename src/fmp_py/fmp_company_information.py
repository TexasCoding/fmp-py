# src/fmp_py/fmp_company_information.py
# Define the FmpCompanyInformation class that inherits from FmpBase.
import os
import re
from typing import List
import pandas as pd
from fmp_py.fmp_base import (
    FmpBase,
)
from fmp_py.models.company_information import (
    CompanyCoreInfo,
    CompanyMarketCap,
    CompanyProfile,
    StockPeers,
)

from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

CURRENT_DATE = datetime.now().date()
ONE_YEAR_BACK = CURRENT_DATE.replace(year=CURRENT_DATE.year - 1)


"""
The FmpCompanyInformation class provides methods for retrieving company information data from the Financial Modeling Prep API.
Reference: https://site.financialmodelingprep.com/developer/docs#company-information

def historical_market_cap(self, symbol: str, from_date: str = PREVIOUS_YEAR, to_date: str = CURRENT_YEAR, limit: int = 500) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#historical-market-cap-company-information

def all_countries(self) -> List[str]:
    Reference: https://site.financialmodelingprep.com/developer/docs#all-countries-company-information

def all_available_exchanges(self) -> List[str]:
    Reference: https://site.financialmodelingprep.com/developer/docs#all-available-exchanges
    
def all_available_industries(self) -> List[str]:
    Reference: https://site.financialmodelingprep.com/developer/docs#all-available-industries

def all_available_sectors(self) -> List[str]:
    Reference: https://site.financialmodelingprep.com/developer/docs#all-available-sectors
    
def analyst_recommendations(self, symbol: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#analyst-recommendation-company-information
    
def analyst_estimates(self, symbol: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#analyst-estimates-company-information
    
def company_core_info(self, symbol: str) -> CompanyCoreInfo:
    Reference: https://site.financialmodelingprep.com/developer/docs#core-info-company-information
    
def market_cap(self, symbol: str) -> CompanyMarketCap:
    Reference: https://site.financialmodelingprep.com/developer/docs#market-cap-company-information
    
def executives(self, symbol: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#executives-company-information
    
def stock_grade(self, symbol: str, limit: int = 20) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#stock-grade-company-information
    
def stock_screener(self,market_cap_more_than: int = None, market_cap_lower_than: int = None, price_more_than: int = None,
        price_lower_than: int = None, beta_more_than: float = None, beta_lower_than: float = None, volume_more_than: int = None,
        volume_lower_than: int = None, dividend_more_than: float = None, dividend_lower_than: float = None,
        is_etf: bool = None, is_fund: bool = None, is_actively_trading: bool = None, sector: str = None,
        industry: str = None, exchange: str = None, limit: int = 1000) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#stock-screener-company-information
    
def company_notes(self, symbol: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#company-notes-company-information
    
def historical_employee_count(self, symbol: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#historical-employee-company-information
    
def compensation_benchmark(self, year: int) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#compensation-benchmark-company-information
    
def executive_compensation(self, symbol: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#executive-compensation-company-information
    
def company_profile(self, symbol: str) -> CompanyProfile:
    Reference: https://site.financialmodelingprep.com/developer/docs#company-profile-company-information
    
def company_outlook(self, symbol: str) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#company-outlook-company-information
    
def stock_peers(self, symbol: str) -> StockPeers:
    Reference: https://site.financialmodelingprep.com/developer/docs#stock-peers-company-information
"""


class FmpCompanyInformation(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")):
        super().__init__(api_key)

    ############################
    # Stock Peers
    ############################
    def stock_peers(self, symbol: str) -> StockPeers:
        """
        Retrieves a list of stock peers for the given symbol.

        Args:
            symbol (str): The symbol of the stock.

        Returns:
            StockPeers: An instance of the StockPeers class containing the symbol and a list of peers.

        Raises:
            ValueError: If no stock peers are found for the given symbol.
        """
        url = "v4/stock_peers"
        params = {"symbol": symbol, "apikey": self.api_key}

        try:
            response = self.get_request(url=url, params=params)[0]
        except IndexError:
            raise ValueError("No stock peers found for the given symbol.")

        data_dict = {
            "symbol": response["symbol"],
            "peers_list": response["peersList"],
        }

        return StockPeers(**data_dict)

    ############################
    # Company Outlook
    ############################
    def company_outlook(self, symbol: str) -> dict:
        """
        Retrieves the company outlook for the given symbol.

        Args:
            symbol (str): The stock symbol of the company.

        Returns:
            dict: The company outlook information.

        Raises:
            ValueError: If no company outlook is found for the given symbol.
        """
        url = "v4/company-outlook"
        params = {"symbol": symbol, "apikey": self.api_key}
        response = self.get_request(url=url, params=params)

        if not response["profile"]:
            raise ValueError("No company outlook found for the given symbol.")

        return response

    ############################
    # All available exchanges
    ############################
    def all_available_exchanges(self) -> List[str]:
        """
        Retrieves a list of all available exchanges.

        Returns:
        List[str]: A list of all available exchanges.
        """
        url = "v3/exchanges-list"
        params = {"apikey": self.api_key}
        response = self.get_request(url=url, params=params)

        return response

    ############################
    # All available industries
    ############################
    def all_available_industries(self) -> List[str]:
        """
        Retrieves a list of all available industries.

        Returns:
        List[str]: A list of all available industries.
        """
        url = "v3/industries-list"
        params = {"apikey": self.api_key}
        response = self.get_request(url=url, params=params)

        return response

    ############################
    # All available sectors
    ############################
    def all_available_sectors(self) -> List[str]:
        """
        Retrieves a list of all available sectors.

        Returns:
        List[str]: A list of all available sectors.
        """
        url = "v3/sectors-list"
        params = {"apikey": self.api_key}
        response = self.get_request(url=url, params=params)

        return response

    ############################
    # Analyst Recommendations
    ############################
    def analyst_recommendations(self, symbol: str) -> pd.DataFrame:
        """
        Retrieves the analyst recommendations for a given symbol.

        Args:
            symbol (str): The symbol of the company.

        Returns:
            pd.DataFrame: A DataFrame containing the analyst recommendations.
        """
        url = f"v3/analyst-stock-recommendations/{symbol}"
        params = {"apikey": self.api_key}

        response = self.get_request(url=url, params=params)

        if not response:
            raise ValueError("No data found for the given symbol.")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "analystRatingsStrongBuy": "analyst_ratings_strong_buy",
                    "analystRatingsbuy": "analyst_ratings_buy",
                    "analystRatingsStrongSell": "analyst_ratings_strong_sell",
                    "analystRatingsSell": "analyst_ratings_sell",
                    "analystRatingsHold": "analyst_ratings_hold",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "date": "datetime64[ns]",
                    "analyst_ratings_strong_buy": "int",
                    "analyst_ratings_buy": "int",
                    "analyst_ratings_strong_sell": "int",
                    "analyst_ratings_sell": "int",
                    "analyst_ratings_hold": "int",
                }
            )
        )

    ############################
    # Analyst Estimates
    ############################
    def analyst_estimates(
        self, symbol: str, period: str = "annual", limit: int = 30
    ) -> pd.DataFrame:
        """
        Retrieves analyst estimates for a given symbol.

        Args:
            symbol (str): The symbol of the company.
            period (str, optional): The period for which to retrieve estimates. Defaults to "annual".
            limit (int, optional): The maximum number of estimates to retrieve. Defaults to 30.

        Returns:
            pd.DataFrame: A DataFrame containing the analyst estimates.

        Raises:
            ValueError: If the provided period is not one of ["annual", "quarter"].
        """
        period_options = ["annual", "quarter"]

        if period not in period_options:
            raise ValueError(f"period must be one of {period_options}")

        url = f"v3/analyst-estimates/{symbol}"
        params = {"period": period, "limit": limit, "apikey": self.api_key}

        response = self.get_request(url=url, params=params)

        if not response:
            raise ValueError("No data found for the given symbol.")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "estimatedRevenueLow": "estimated_revenue_low",
                    "estimatedRevenueHigh": "estimated_revenue_high",
                    "estimatedRevenueAvg": "estimated_revenue_avg",
                    "estimatedEbitdaLow": "estimated_ebitda_low",
                    "estimatedEbitdaHigh": "estimated_ebitda_high",
                    "estimatedEbitdaAvg": "estimated_ebitda_avg",
                    "estimatedEbitLow": "estimated_ebit_low",
                    "estimatedEbitHigh": "estimated_ebit_high",
                    "estimatedEbitAvg": "estimated_ebit_avg",
                    "estimatedNetIncomeLow": "estimated_net_income_low",
                    "estimatedNetIncomeHigh": "estimated_net_income_high",
                    "estimatedNetIncomeAvg": "estimated_net_income_avg",
                    "estimatedSgaExpenseLow": "estimated_sga_expense_low",
                    "estimatedSgaExpenseHigh": "estimated_sga_expense_high",
                    "estimatedSgaExpenseAvg": "estimated_sga_expense_avg",
                    "estimatedEpsAvg": "estimated_eps_avg",
                    "estimatedEpsLow": "estimated_eps_low",
                    "estimatedEpsHigh": "estimated_eps_high",
                    "numberAnalystEstimatedRevenue": "number_analyst_estimated_revenue",
                    "numberAnalystsEstimatedEps": "number_analysts_estimated_eps",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "date": "datetime64[ns]",
                    "estimated_revenue_low": "int",
                    "estimated_revenue_high": "int",
                    "estimated_revenue_avg": "int",
                    "estimated_ebitda_low": "int",
                    "estimated_ebitda_high": "int",
                    "estimated_ebitda_avg": "int",
                    "estimated_ebit_low": "int",
                    "estimated_ebit_high": "int",
                    "estimated_ebit_avg": "int",
                    "estimated_net_income_low": "int",
                    "estimated_net_income_high": "int",
                    "estimated_net_income_avg": "int",
                    "estimated_sga_expense_low": "int",
                    "estimated_sga_expense_high": "int",
                    "estimated_sga_expense_avg": "int",
                    "estimated_eps_avg": "float",
                    "estimated_eps_low": "float",
                    "estimated_eps_high": "float",
                    "number_analyst_estimated_revenue": "int",
                    "number_analysts_estimated_eps": "int",
                }
            )
        )

    ############################
    # All Countries
    ############################
    def all_countries(self) -> List[str]:
        """
        Retrieves a list of all countries.

        Returns:
        List[str]: A list of all countries.
        """
        url = "v3/get-all-countries"
        params = {"apikey": self.api_key}
        response = self.get_request(url=url, params=params)

        return response

    ############################
    # Historical Market Capitalization
    ############################
    def historical_market_cap(
        self,
        symbol: str,
        from_date: str = ONE_YEAR_BACK.strftime("%Y-%m-%d"),
        to_date: str = CURRENT_DATE.strftime("%Y-%m-%d"),
        limit: int = 500,
    ) -> pd.DataFrame:
        """
        Retrieves the historical market capitalization for a given symbol.

        Parameters:
        symbol (str): The stock symbol of the company.

        Returns:
        pd.DataFrame: A DataFrame containing the historical market capitalization.
        """
        date_str = r"^\d{4}-\d{2}-\d{2}$"
        if not re.match(date_str, from_date) or not re.match(date_str, to_date):
            raise ValueError("dates must be in the format 'YYYY-MM-DD'")

        url = f"v3/historical-market-capitalization/{symbol}"
        params = {
            "from": from_date,
            "to": to_date,
            "limit": limit,
            "apikey": self.api_key,
        }

        response = self.get_request(url=url, params=params)
        if not response:
            raise ValueError("No data found for the given symbol.")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "symbol": "symbol",
                    "date": "date",
                    "marketCap": "market_cap",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "date": "datetime64[ns]",
                    "market_cap": "int",
                }
            )
            .sort_values(by="date", ascending=True)
            .reset_index(drop=True)
        )

    ############################
    # Company Core Information
    ############################
    def company_core_info(self, symbol: str) -> CompanyCoreInfo:
        """
        Retrieves the core information for a given symbol.

        Args:
            symbol (str): The symbol of the company.

        Returns:
            CompanyCoreInfo: An object containing the core information of the company.

        Raises:
            ValueError: If there is an error parsing the response.

        """
        url = "v4/company-core-information"
        params = {"symbol": symbol, "apikey": self.api_key}

        try:
            response: dict = self.get_request(url=url, params=params)[0]
        except IndexError:
            raise ValueError("No data found for the given symbol.")

        if not response:
            raise ValueError("No data found for the given symbol.")

        data_dict = {
            "cik": self.clean_value(response.get("cik", ""), str),
            "symbol": self.clean_value(response.get("symbol", ""), str),
            "exchange": self.clean_value(response.get("exchange", ""), str),
            "sic_code": self.clean_value(response.get("sicCode", ""), str),
            "sic_group": self.clean_value(response.get("sicGroup", ""), str),
            "sic_description": self.clean_value(
                response.get("sicDescription", ""), str
            ),
            "state_location": self.clean_value(response.get("stateLocation", ""), str),
            "state_of_incorporation": self.clean_value(
                response.get("stateOfIncorporation", ""), str
            ),
            "fiscal_year_end": self.clean_value(response.get("fiscalYearEnd", ""), str),
            "business_address": self.clean_value(
                response.get("businessAddress", ""), str
            ),
            "mailing_address": self.clean_value(
                response.get("mailingAddress", ""), str
            ),
            "tax_idenfication_number": self.clean_value(
                response.get("taxIdentificationNumber", ""), str
            ),
            "registrant_name": self.clean_value(
                response.get("registrantName", ""), str
            ),
        }

        return CompanyCoreInfo(**data_dict)

    ############################
    # Market Capitalization
    ############################
    def market_cap(self, symbol: str) -> CompanyMarketCap:
        """
        Retrieves the market capitalization for a given symbol.

        Args:
            symbol (str): The symbol of the company.

        Returns:
            CompanyMarketCap: An object containing the symbol, market capitalization, and date.

        Raises:
            ValueError: If there is an error parsing the response.

        """
        url = f"v3/market-capitalization/{symbol}"
        params = {"apikey": self.api_key}

        try:
            response: dict = self.get_request(url=url, params=params)[0]
        except IndexError:
            raise ValueError("No data found for the given symbol.")

        if not response:
            raise ValueError("No data found for the given symbol.")

        data_dict = {
            "symbol": self.clean_value(response.get("symbol", ""), str),
            "market_cap": self.clean_value(response.get("marketCap", 0.0), int),
            "date": self.clean_value(response.get("date", ""), str),
        }

        return CompanyMarketCap(**data_dict)

    ############################
    # Executives
    ############################
    def executives(self, symbol: str) -> pd.DataFrame:
        """
        Retrieves the executives information for a given symbol.

        Parameters:
        symbol (str): The stock symbol of the company.

        Returns:
        pd.DataFrame: A DataFrame containing the executives information.
        """
        url = f"v3/key-executives/{symbol}"
        params = {"apikey": self.api_key}
        response = self.get_request(url=url, params=params)

        if not response:
            raise ValueError("No data found for the given symbol.")

        data_df = pd.DataFrame(response).rename(
            columns={
                "currencyPay": "currency_pay",
                "yearBorn": "year_born",
                "titleSince": "title_since",
            }
        )

        data_df["title_since"] = data_df["title_since"].fillna("1900-01-01")
        data_df["pay"] = data_df["pay"].fillna(0)
        data_df["year_born"] = data_df["year_born"].fillna(0)

        data_df = data_df.astype(
            {
                "title": "str",
                "name": "str",
                "pay": "int",
                "year_born": "int",
                "currency_pay": "str",
                "gender": "str",
                "title_since": "datetime64[ns]",
            }
        )

        return data_df.sort_values(by="title_since", ascending=False)

    ############################
    # Stock Grade
    ############################
    def stock_grade(self, symbol: str, limit: int = 20) -> pd.DataFrame:
        """
        Retrieves the stock grade information for a given symbol.

        Args:
            symbol (str): The stock symbol.
            limit (int, optional): The maximum number of grades to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the stock grade information, with columns renamed and data types converted.
        """

        url = f"v3/grade/{symbol}"
        params = {"limit": limit, "apikey": self.api_key}
        response = self.get_request(url=url, params=params)

        if not response:
            raise ValueError("No data found for the given symbol.")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "gradingCompany": "grading_company",
                    "previousGrade": "previous_grade",
                    "newGrade": "new_grade",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                }
            )
        )

    ############################
    # Stock Screener
    ############################
    def stock_screener(
        self,
        market_cap_more_than: int = None,
        market_cap_lower_than: int = None,
        price_more_than: int = None,
        price_lower_than: int = None,
        beta_more_than: float = None,
        beta_lower_than: float = None,
        volume_more_than: int = None,
        volume_lower_than: int = None,
        dividend_more_than: float = None,
        dividend_lower_than: float = None,
        is_etf: bool = None,
        is_fund: bool = None,
        is_actively_trading: bool = None,
        sector: str = None,
        industry: str = None,
        exchange: str = None,
        limit: int = 1000,
    ) -> pd.DataFrame:
        """
        Retrieves a DataFrame of stock information based on the specified criteria.

        Args:
            market_cap_more_than (int, optional): Filter stocks with market cap greater than this value.
            market_cap_lower_than (int, optional): Filter stocks with market cap lower than this value.
            price_more_than (int, optional): Filter stocks with price greater than this value.
            price_lower_than (int, optional): Filter stocks with price lower than this value.
            beta_more_than (float, optional): Filter stocks with beta greater than this value.
            beta_lower_than (float, optional): Filter stocks with beta lower than this value.
            volume_more_than (int, optional): Filter stocks with volume greater than this value.
            volume_lower_than (int, optional): Filter stocks with volume lower than this value.
            dividend_more_than (float, optional): Filter stocks with dividend greater than this value.
            dividend_lower_than (float, optional): Filter stocks with dividend lower than this value.
            is_etf (bool, optional): Filter stocks that are ETFs.
            is_fund (bool, optional): Filter stocks that are funds.
            is_actively_trading (bool, optional): Filter stocks that are actively trading.
            sector (str, optional): Filter stocks by sector.
            industry (str, optional): Filter stocks by industry.
            exchange (str, optional): Filter stocks by exchange.
            limit (int, optional): Limit the number of results returned (default is 1000).

        Returns:
            pandas.DataFrame: DataFrame containing the stock information.

        """
        url = "v3/stock-screener"
        params = {
            "marketCapMoreThan": market_cap_more_than,
            "marketCapLowerThan": market_cap_lower_than,
            "priceMoreThan": price_more_than,
            "priceLowerThan": price_lower_than,
            "betaMoreThan": beta_more_than,
            "betaLowerThan": beta_lower_than,
            "volumeMoreThan": volume_more_than,
            "volumeLowerThan": volume_lower_than,
            "dividendMoreThan": dividend_more_than,
            "dividendLowerThan": dividend_lower_than,
            "isEtf": is_etf,
            "isFund": is_fund,
            "isActivelyTrading": is_actively_trading,
            "sector": sector,
            "industry": industry,
            "exchange": exchange,
            "limit": limit,
            "apikey": self.api_key,
        }

        response = self.get_request(url=url, params=params)

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "companyName": "company_name",
                    "marketCap": "market_cap",
                    "lastAnnualDividend": "last_annual_dividend",
                    "exchangeShortName": "exchange_short_name",
                    "isActivelyTrading": "is_actively_trading",
                    "isEtf": "is_etf",
                    "isFund": "is_fund",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "company_name": "str",
                    "sector": "str",
                    "industry": "str",
                    "country": "str",
                    "is_etf": "bool",
                    "is_actively_trading": "bool",
                    "exchange": "str",
                    "exchange_short_name": "str",
                    "market_cap": "int",
                    "price": "float",
                    "volume": "int",
                    "last_annual_dividend": "float",
                    "beta": "float",
                }
            )
        )

    ############################
    # Company Notes
    ############################
    def company_notes(self, symbol: str) -> pd.DataFrame:
        """
        Retrieves the company notes for a given symbol.

        Parameters:
        symbol (str): The stock symbol of the company.

        Returns:
        pd.DataFrame: A DataFrame containing the company notes.
        """
        url = "v4/company-notes"
        params = {"symbol": symbol, "apikey": self.api_key}
        response = self.get_request(url=url, params=params)

        if not response:
            raise ValueError("No company notes found for the given symbol.")

        return pd.DataFrame(response).astype(
            {"symbol": "str", "cik": "str", "title": "str", "exchange": "str"}
        )

    ############################
    # Historical Employee Count
    ############################
    def historical_employee_count(self, symbol: str) -> pd.DataFrame:
        """
        Retrieves the historical employee count for a given symbol.

        Parameters:
        symbol (str): The stock symbol of the company.

        Returns:
        pd.DataFrame: A DataFrame containing the historical employee count.
        """
        url = "v4/historical/employee_count"
        params = {"symbol": symbol, "apikey": self.api_key}
        response = self.get_request(url=url, params=params)

        if not response:
            raise ValueError("No historical employee count found for the given symbol.")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "filingDate": "filed_date",
                    "acceptanceTime": "acceptance_time",
                    "periodOfReport": "period_of_report",
                    "employeeCount": "employee_count",
                    "formType": "form_type",
                    "companyName": "company_name",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "cik": "str",
                    "company_name": "str",
                    "form_type": "str",
                    "source": "str",
                    "filed_date": "datetime64[ns]",
                    "acceptance_time": "datetime64[ns]",
                    "period_of_report": "datetime64[ns]",
                    "employee_count": "int",
                }
            )
        )

    ############################
    # Compensation Benchmark
    ############################
    def compensation_benchmark(self, year: int = CURRENT_DATE.year) -> pd.DataFrame:
        """
        Retrieves compensation benchmark data for a specific year.

        Args:
            year (int): The year for which to retrieve the compensation benchmark data.

        Returns:
            pd.DataFrame: A DataFrame containing the compensation benchmark data.

        """
        url = "v4/executive-compensation-benchmark"
        params = {"year": year, "apikey": self.api_key}
        response = self.get_request(url=url, params=params)

        return (
            (
                pd.DataFrame(response)
                .rename(
                    columns={
                        "industryTitle": "industry_title",
                        "averageCompensation": "average_compensation",
                    }
                )
                .astype(
                    {
                        "average_compensation": "float",
                        "year": "int",
                        "industry_title": "str",
                    }
                )
            )
            .sort_values(by="industry_title", ascending=False)
            .reset_index(drop=True)
        )

    ############################
    # Executive Compensation
    ############################
    def executive_compensation(self, symbol: str) -> pd.DataFrame:
        url = "v4/governance/executive_compensation"

        params = {"symbol": symbol, "apikey": self.api_key}

        response = self.get_request(url=url, params=params)

        if not response:
            raise ValueError("No executive compensation found for the given symbol.")

        data_df = pd.DataFrame(response)
        data_df = data_df.rename(
            columns={
                "companyName": "company_name",
                "acceptedDate": "accepted_date",
                "filingDate": "filing_date",
                "nameAndPosition": "name_and_position",
                "industryTitle": "industry_title",
            }
        ).astype(
            {
                "cik": "str",
                "symbol": "str",
                "company_name": "str",
                "industry_title": "str",
                "name_and_position": "str",
                "year": "int",
                "salary": "int",
                "bonus": "int",
                "stock_award": "int",
                "incentive_plan_compensation": "int",
                "all_other_compensation": "int",
                "total": "int",
                "accepted_date": "datetime64[ns]",
                "filing_date": "datetime64[ns]",
            }
        )

        return data_df.sort_values(by="year", ascending=True).reset_index(drop=True)

    ############################
    # Company Profile
    ############################
    def company_profile(self, symbol: str) -> CompanyProfile:
        """
        Retrieves the company profile information for a given symbol symbol.

        Args:
            symbol (str): The symbol symbol of the company.

        Returns:
            CompanyProfile: A dataclass object containing the company profile information.
        """
        url = f"v3/company/profile/{symbol}"
        params = {"apikey": self.api_key}
        response: dict = self.get_request(url=url, params=params)

        if not response:
            raise ValueError("No company profile found for the given symbol.")

        data = response.get("profile", {})

        data_dict = {
            "symbol": self.clean_value(data.get("symbol", ""), str),
            "price": self.clean_value(data.get("price", 0.0), float),
            "beta": self.clean_value(data.get("beta", 0.0), float),
            "vol_avg": self.clean_value(data.get("volAvg", 0), int),
            "mkt_cap": self.clean_value(data.get("mktCap", 0), int),
            "last_div": self.clean_value(data.get("lastDiv", 0), int),
            "range": self.clean_value(data.get("range", ""), str),
            "changes": self.clean_value(data.get("changes", 0.0), float),
            "company_name": self.clean_value(data.get("companyName", ""), str),
            "currency": self.clean_value(data.get("currency", ""), str),
            "cik": self.clean_value(data.get("cik", ""), str),
            "isin": self.clean_value(data.get("isin", ""), str),
            "cusip": self.clean_value(data.get("cusip", ""), str),
            "exchange": self.clean_value(data.get("exchange", ""), str),
            "exchange_short_name": self.clean_value(
                data.get("exchangeShortName", ""), str
            ),
            "industry": self.clean_value(data.get("industry", ""), str),
            "website": self.clean_value(data.get("website", ""), str),
            "description": self.clean_value(data.get("description", ""), str),
            "ceo": self.clean_value(data.get("ceo", ""), str),
            "sector": self.clean_value(data.get("sector", ""), str),
            "country": self.clean_value(data.get("country", ""), str),
            "full_time_employees": self.clean_value(
                data.get("fullTimeEmployees", 0), int
            ),
            "phone": self.clean_value(data.get("phone", ""), str),
            "address": self.clean_value(data.get("address", ""), str),
            "city": self.clean_value(data.get("city", ""), str),
            "state": self.clean_value(data.get("state", ""), str),
            "zip": self.clean_value(data.get("zip", ""), str),
            "dcf_diff": self.clean_value(data.get("dcfDiff", 0.0), float),
            "dcf": self.clean_value(data.get("dcf", 0.0), float),
            "image": self.clean_value(data.get("image", ""), str),
            "ipo_date": self.clean_value(data.get("ipoDate", ""), str),
            "default_image": self.clean_value(data.get("defaultImage", False), bool),
            "is_etf": self.clean_value(data.get("isEtf", False), bool),
            "is_actively_trading": self.clean_value(
                data.get("isActivelyTrading", False), bool
            ),
            "is_adr": self.clean_value(data.get("isAdr", False), bool),
            "is_fund": self.clean_value(data.get("isFund", False), bool),
        }

        return CompanyProfile(**data_dict)
