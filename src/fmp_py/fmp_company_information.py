from typing import List
import pandas as pd
from fmp_py.fmp_base import (
    FmpBase,
)
from fmp_py.models.company_information import (
    CompanyCoreInfo,
    CompanyMarketCap,
    CompanyProfile,
)

from datetime import datetime

CURRENT_YEAR = datetime.now().year
PREVIOUS_YEAR = CURRENT_YEAR - 1


class FmpCompanyInformation(FmpBase):
    def __init__(self):
        super().__init__()

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
        from_date: str = PREVIOUS_YEAR,
        to_date: str = CURRENT_YEAR,
        limit: int = 500,
    ) -> pd.DataFrame:
        """
        Retrieves the historical market capitalization for a given symbol.

        Parameters:
        symbol (str): The stock symbol of the company.

        Returns:
        pd.DataFrame: A DataFrame containing the historical market capitalization.
        """
        url = f"v3/historical-market-capitalization/{symbol}"
        params = {
            "from": from_date,
            "to": to_date,
            "limit": limit,
            "apikey": self.api_key,
        }

        response = self.get_request(url=url, params=params)

        return pd.DataFrame(response)

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

        response = self.get_request(url=url, params=params)

        try:
            return CompanyCoreInfo(
                cik=response[0].get("cik", ""),
                symbol=response[0].get("symbol", ""),
                exchange=response[0].get("exchange", ""),
                sic_code=response[0].get("sicCode", ""),
                sic_group=response[0].get("sicGroup", ""),
                sic_description=response[0].get("sicDescription", ""),
                state_location=response[0].get("stateLocation", ""),
                state_of_incorporation=response[0].get("stateOfIncorporation", ""),
                fiscal_year_end=response[0].get("fiscalYearEnd", ""),
                business_address=response[0].get("businessAddress", ""),
                mailing_address=response[0].get("mailingAddress", ""),
                tax_idenfication_number=response[0].get("taxIdentificationNumber", ""),
                registrant_name=response[0].get("registrantName", ""),
            )
        except Exception as e:
            raise ValueError(f"Error parsing response: {e}")

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

        response = self.get_request(url=url, params=params)

        try:
            return CompanyMarketCap(
                symbol=response[0].get("symbol", ""),
                market_cap=response[0].get("marketCap", 0.0),
                date=response[0].get("date", ""),
            )
        except Exception as e:
            raise ValueError(f"Error parsing response: {e}")

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

        data_df = pd.DataFrame(response).rename(
            columns={
                "currencyPay": "currency_pay",
                "yearBorn": "year_born",
                "titleSince": "title_since",
            }
        )

        data_df["title_since"] = (
            pd.to_datetime(data_df["title_since"], unit="s")
            if data_df["title_since"].dtype == "int64"
            else ""
        )

        return data_df.fillna("")

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
    ):
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

        return pd.DataFrame(response)

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

        return pd.DataFrame(response)

    ############################
    # Compensation Benchmark
    ############################
    def compensation_benchmark(self, year: int) -> pd.DataFrame:
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
                }
            )
        )

    ############################
    # Executive Compensation
    ############################
    def executive_compensation(self, symbol: str) -> pd.DataFrame:
        url = "v4/governance/executive_compensation"

        params = {"symbol": symbol, "apikey": self.api_key}

        response = self.get_request(url=url, params=params)

        data_df = pd.DataFrame(response)
        data_df = data_df.rename(
            columns={
                "companyName": "company_name",
                "acceptedDate": "accepted_date",
                "filingDate": "filing_date",
                "nameAndPosition": "name_and_position",
                "industryTitle": "industry",
            }
        ).astype(
            {
                "salary": "float",
                "bonus": "float",
                "stock_award": "float",
                "incentive_plan_compensation": "float",
                "all_other_compensation": "float",
                "total": "float",
                "accepted_date": "datetime64[ns]",
                "filing_date": "datetime64[ns]",
            }
        )

        return data_df

    def company_profile(self, ticker: str) -> CompanyProfile:
        """
        Retrieves the company profile information for a given ticker symbol.

        Args:
            ticker (str): The ticker symbol of the company.

        Returns:
            CompanyProfile: A dataclass object containing the company profile information.
        """
        url = f"v3/company/profile/{ticker}"
        params = {"apikey": self.api_key}
        response = self.get_request(url=url, params=params)
        data = response.get("profile", {})

        if not data:
            return CompanyProfile()

        return CompanyProfile(
            symbol=ticker.upper(),
            price=data.get("price", 0.0),
            beta=data.get("beta", 0.0),
            vol_avg=data.get("volAvg", 0),
            mkt_cap=data.get("mktCap", 0),
            last_div=data.get("lastDiv", 0.0),
            range=data.get("range", ""),
            changes=data.get("changes", 0.0),
            company_name=data.get("companyName", ""),
            currency=data.get("currency", ""),
            cik=data.get("cik", ""),
            isin=data.get("isin", ""),
            cusip=data.get("cusip", ""),
            exchange=data.get("exchange", ""),
            exchange_short_name=data.get("exchangeShortName", ""),
            industry=data.get("industry", ""),
            website=data.get("website", ""),
            description=data.get("description", ""),
            ceo=data.get("ceo", ""),
            sector=data.get("sector", ""),
            country=data.get("country", ""),
            full_time_employees=data.get("fullTimeEmployees", ""),
            phone=data.get("phone", ""),
            address=data.get("address", ""),
            city=data.get("city", ""),
            state=data.get("state", ""),
            zip=data.get("zip", ""),
            dcf_iff=data.get("dcfDiff", 0.0),
            dcf=data.get("dcf", 0.0),
            image=data.get("image", ""),
            ipo_date=data.get("ipoDate", ""),
            default_image=data.get("defaultImage", False),
            is_etf=data.get("isEtf", False),
            is_actively_trading=data.get("isActivelyTrading", False),
            is_adr=data.get("isAdr", False),
            is_fund=data.get("isFund", False),
        )
