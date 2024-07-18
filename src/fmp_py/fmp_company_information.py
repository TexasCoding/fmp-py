import pandas as pd
from fmp_py.fmp_base import (
    FmpBase,
)
from fmp_py.models.company_information import CompanyProfile


class FmpCompanyInformation(FmpBase):
    def __init__(self):
        super().__init__()

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
