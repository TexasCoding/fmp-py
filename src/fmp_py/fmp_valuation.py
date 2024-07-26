from fmp_py.fmp_base import FmpBase
import os
import pandas as pd

from dotenv import load_dotenv

from fmp_py.models.valuation import CompanyRating, DiscountedCashFlow

load_dotenv()


"""
FmpValuation class inherits from FmpBase.
This class is used to interact with the Financial Modeling Prep API to retrieve valuation data.
https://site.financialmodelingprep.com/developer/docs#valuation

def company_rating(self, symbol: str) -> CompanyRating:
    Reference: https://site.financialmodelingprep.com/developer/docs#company-rating-company-information
    
def discounted_cash_flow(self, symbol: str) -> DiscountedCashFlow:
    Reference: https://site.financialmodelingprep.com/developer/docs#discounted-cashflow-discounted-cash-flow
    
def advanced_dcf(self, symbol: str) -> pd.Dataframe:
    Reference: https://site.financialmodelingprep.com/developer/docs#advanced-dcf-discounted-cash-flow
    
def levered_dcf(self, symbol: str) -> pd.Dataframe:
    Reference: https://site.financialmodelingprep.com/developer/docs#levered-dcf-discounted-cash-flow
    
def historical_rating(self, symbol: str) -> pd.Dataframe:
    Reference: https://site.financialmodelingprep.com/developer/docs#historical-rating-company-information
"""


class FmpValuation(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")):
        super().__init__(api_key)

    ############################
    # Historical Rating
    ############################
    def historical_rating(self, symbol: str) -> pd.DataFrame:
        """
        Retrieves the historical rating data for a given symbol.

        Args:
            symbol (str): The symbol of the stock.

        Returns:
            pd.DataFrame: A DataFrame containing the historical rating data, sorted by date in ascending order.
        """

        url = f"v3/historical-rating/{symbol}"
        params = {"apikey": self.api_key}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found in API response")

        data_df = (
            pd.DataFrame(response)
            .rename(
                columns={
                    "symbol": "symbol",
                    "date": "date",
                    "rating": "rating",
                    "ratingScore": "rating_score",
                    "ratingRecommendation": "rating_recommendation",
                    "ratingDetailsDCFScore": "rating_details_dcf_score",
                    "ratingDetailsDCFRecommendation": "rating_details_dcf_recommendation",
                    "ratingDetailsROEScore": "rating_details_roe_score",
                    "ratingDetailsROERecommendation": "rating_details_roe_recommendation",
                    "ratingDetailsROAScore": "rating_details_roa_score",
                    "ratingDetailsROARecommendation": "rating_details_roa_recommendation",
                    "ratingDetailsDEScore": "rating_details_de_score",
                    "ratingDetailsDERecommendation": "rating_details_de_recommendation",
                    "ratingDetailsPEScore": "rating_details_pe_score",
                    "ratingDetailsPERecommendation": "rating_details_pe_recommendation",
                    "ratingDetailsPBScore": "rating_details_pb_score",
                    "ratingDetailsPBRecommendation": "rating_details_pb_recommendation",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "date": "datetime64[ns]",
                    "rating": "str",
                    "rating_score": "int",
                    "rating_recommendation": "str",
                    "rating_details_dcf_score": "int",
                    "rating_details_dcf_recommendation": "str",
                    "rating_details_roe_score": "int",
                    "rating_details_roe_recommendation": "str",
                    "rating_details_roa_score": "int",
                    "rating_details_roa_recommendation": "str",
                    "rating_details_de_score": "int",
                    "rating_details_de_recommendation": "str",
                    "rating_details_pe_score": "int",
                    "rating_details_pe_recommendation": "str",
                    "rating_details_pb_score": "int",
                    "rating_details_pb_recommendation": "str",
                }
            )
        )

        return data_df.sort_values(by=["date"], ascending=True).reset_index(drop=True)

    ############################
    # Levered DCF
    ############################
    def levered_dcf(self, symbol: str) -> pd.DataFrame:
        """
        Calculate the levered discounted cash flow (DCF) for a given symbol.

        Parameters:
        symbol (str): The symbol of the stock for which to calculate the DCF.

        Returns:
        pd.DataFrame: A DataFrame containing the DCF data for the given symbol, sorted by year in ascending order.
        """

        url = "v4/advanced_levered_discounted_cash_flow"
        params = {"symbol": symbol, "apikey": self.api_key}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found in API response")

        data_df = (
            pd.DataFrame(response)
            .rename(
                columns={
                    "year": "year",  # int
                    "symbol": "symbol",  # str
                    "revenue": "revenue",  # int
                    "revenuePercentage": "revenue_percentage",  # float
                    "capitalExpenditure": "capital_expenditure",  # int
                    "capitalExpenditurePercentage": "capital_expenditure_percentage",  # float
                    "price": "price",  # float
                    "beta": "beta",  # float
                    "dilutedSharesOutstanding": "diluted_shares_outstanding",  # int
                    "costofDebt": "cost_of_debt",  # float
                    "taxRate": "tax_rate",  # float
                    "afterTaxCostOfDebt": "after_tax_cost_of_debt",  # float
                    "riskFreeRate": "risk_free_rate",  # float
                    "marketRiskPremium": "market_risk_premium",  # float
                    "costOfEquity": "cost_of_equity",  # float
                    "totalDebt": "total_debt",  # int
                    "totalEquity": "total_equity",  # int
                    "totalCapital": "total_capital",  # int
                    "debtWeighting": "debt_weighting",  # float
                    "equityWeighting": "equity_weighting",  # float
                    "wacc": "wacc",  # float
                    "operatingCashFlow": "operating_cash_flow",  # int
                    "pvLfcf": "pv_lfcf",  # int
                    "sumPvLfcf": "sum_pv_lfcf",  # int
                    "longTermGrowthRate": "long_term_growth_rate",  # float
                    "freeCashFlow": "free_cash_flow",  # int
                    "terminalValue": "terminal_value",  # int
                    "presentTerminalValue": "present_terminal_value",  # int
                    "enterpriseValue": "enterprise_value",  # int
                    "netDebt": "net_debt",  # int
                    "equityValue": "equity_value",  # int
                    "equityValuePerShare": "equity_value_per_share",  # float
                    "freeCashFlowT1": "free_cash_flow_t1",  # int
                    "operatingCashFlowPercentage": "operating_cash_flow_percentage",  # float
                }
            )
            .astype(
                {
                    "year": "int",
                    "symbol": "str",
                    "revenue": "int",
                    "revenue_percentage": "float",
                    "capital_expenditure": "int",
                    "capital_expenditure_percentage": "float",
                    "price": "float",
                    "beta": "float",
                    "diluted_shares_outstanding": "int",
                    "cost_of_debt": "float",
                    "tax_rate": "float",
                    "after_tax_cost_of_debt": "float",
                    "risk_free_rate": "float",
                    "market_risk_premium": "float",
                    "cost_of_equity": "float",
                    "total_debt": "int",
                    "total_equity": "int",
                    "total_capital": "int",
                    "debt_weighting": "float",
                    "equity_weighting": "float",
                    "wacc": "float",
                    "operating_cash_flow": "int",
                    "pv_lfcf": "int",
                    "sum_pv_lfcf": "int",
                    "long_term_growth_rate": "float",
                    "free_cash_flow": "int",
                    "terminal_value": "int",
                    "present_terminal_value": "int",
                    "enterprise_value": "int",
                    "net_debt": "int",
                    "equity_value": "int",
                    "equity_value_per_share": "float",
                    "free_cash_flow_t1": "int",
                    "operating_cash_flow_percentage": "float",
                }
            )
        )

        return data_df.sort_values(by=["year"], ascending=True).reset_index(drop=True)

    ############################
    # Advanced DCF
    ############################
    def advanced_dcf(self, symbol: str) -> pd.DataFrame:
        """
        Retrieves advanced discounted cash flow (DCF) data for a given symbol.

        Args:
            symbol (str): The symbol of the stock or company.

        Returns:
            pd.DataFrame: A DataFrame containing the DCF data, sorted by year in ascending order.

        Raises:
            ValueError: If no data is found in the API response.
        """
        url = "v4/advanced_discounted_cash_flow"
        params = {"symbol": symbol, "apikey": self.api_key}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found in API response")

        data_df = (
            pd.DataFrame(response)
            .rename(
                columns={
                    "year": "year",  # str
                    "symbol": "symbol",  # str
                    "revenue": "revenue",  # int
                    "revenuePercentage": "revenue_percentage",  # float
                    "ebitda": "ebitda",  # int
                    "ebitdaPercentage": "ebitda_percentage",  # float
                    "ebit": "ebit",  # int
                    "ebitPercentage": "ebit_percentage",  # float
                    "depreciation": "depreciation",  # int
                    "depreciationPercentage": "depreciation_percentage",  # float
                    "totalCash": "total_cash",  # int
                    "totalCashPercentage": "total_cash_percentage",  # float
                    "receivables": "receivables",  # int
                    "receivablesPercentage": "receivables_percentage",  # float
                    "inventories": "inventories",  # int
                    "inventoriesPercentage": "inventories_percentage",  # float
                    "payable": "payable",  # int
                    "payablePercentage": "payable_percentage",  # float
                    "capitalExpenditure": "capital_expenditure",  # int
                    "capitalExpenditurePercentage": "capital_expenditure_percentage",  # float
                    "price": "price",  # float
                    "beta": "beta",  # float
                    "dilutedSharesOutstanding": "diluted_shares_outstanding",  # int
                    "costofDebt": "cost_of_debt",  # float
                    "taxRate": "tax_rate",  # float
                    "afterTaxCostOfDebt": "after_tax_cost_of_debt",  # float
                    "riskFreeRate": "risk_free_rate",  # float
                    "marketRiskPremium": "market_risk_premium",  # float
                    "costOfEquity": "cost_of_equity",  # float
                    "totalDebt": "total_debt",  # int
                    "totalEquity": "total_equity",  # int
                    "totalCapital": "total_capital",  # int
                    "debtWeighting": "debt_weighting",  # float
                    "equityWeighting": "equity_weighting",  # float
                    "wacc": "wacc",  # float
                    "taxRateCash": "tax_rate_cash",  # int
                    "ebiat": "ebiat",  # int
                    "ufcf": "ufcf",  # int
                    "sumPvUfcf": "sum_pv_ufcf",  # int
                    "longTermGrowthRate": "long_term_growth_rate",  # float
                    "terminalValue": "terminal_value",  # int
                    "presentTerminalValue": "present_terminal_value",  # int
                    "enterpriseValue": "enterprise_value",  # int
                    "netDebt": "net_debt",  # int
                    "equityValue": "equity_value",  # int
                    "equityValuePerShare": "equity_value_per_share",  # float
                    "freeCashFlowT1": "free_cash_flow_t1",  # int
                }
            )
            .astype(
                {
                    "year": "int",
                    "symbol": "str",
                    "revenue": "int",
                    "revenue_percentage": "float",
                    "ebitda": "int",
                    "ebitda_percentage": "float",
                    "ebit": "int",
                    "ebit_percentage": "float",
                    "depreciation": "int",
                    "depreciation_percentage": "float",
                    "total_cash": "int",
                    "total_cash_percentage": "float",
                    "receivables": "int",
                    "receivables_percentage": "float",
                    "inventories": "int",
                    "inventories_percentage": "float",
                    "payable": "int",
                    "payable_percentage": "float",
                    "capital_expenditure": "int",
                    "capital_expenditure_percentage": "float",
                    "price": "float",
                    "beta": "float",
                    "diluted_shares_outstanding": "int",
                    "cost_of_debt": "float",
                    "tax_rate": "float",
                    "after_tax_cost_of_debt": "float",
                    "risk_free_rate": "float",
                    "market_risk_premium": "float",
                    "cost_of_equity": "float",
                    "total_debt": "int",
                    "total_equity": "int",
                    "total_capital": "int",
                    "debt_weighting": "float",
                    "equity_weighting": "float",
                    "wacc": "float",
                    "tax_rate_cash": "int",
                    "ebiat": "int",
                    "ufcf": "int",
                    "sum_pv_ufcf": "int",
                    "long_term_growth_rate": "float",
                    "terminal_value": "int",
                    "present_terminal_value": "int",
                    "enterprise_value": "int",
                    "net_debt": "int",
                    "equity_value": "int",
                    "equity_value_per_share": "float",
                    "free_cash_flow_t1": "int",
                }
            )
        )

        return data_df.sort_values(by=["year"], ascending=True).reset_index(drop=True)

    ############################
    # Discounted Cash Flow
    ############################
    def discounted_cash_flow(self, symbol: str) -> DiscountedCashFlow:
        """
        Calculates the discounted cash flow (DCF) for a given symbol.

        Parameters:
        symbol (str): The symbol of the stock.

        Returns:
        DiscountedCashFlow: An object containing the DCF information.

        Raises:
        ValueError: If no data is found in the API response.
        """

        url = f"v3/discounted-cash-flow/{symbol}"
        params = {"apikey": self.api_key}
        try:
            response = self.get_request(url, params)[0]
        except IndexError:
            raise ValueError("No data found in API response")

        return DiscountedCashFlow(
            symbol=self.clean_value(response.get("symbol"), str),
            date=self.clean_value(response.get("date"), str),
            dcf=self.clean_value(response.get("dcf"), float),
            stock_price=self.clean_value(response.get("Stock Price"), float),
        )

    ############################
    # Company Rating
    ############################
    def company_rating(self, symbol: str) -> CompanyRating:
        """
        Retrieves the rating information for a given company symbol.

        Args:
            symbol (str): The symbol of the company.

        Returns:
            CompanyRating: An object containing the rating information for the company.

        Raises:
            ValueError: If no data is found in the API response.
        """

        url = f"v3/rating/{symbol}"
        params = {"apikey": self.api_key}

        try:
            response = self.get_request(url, params)[0]
        except IndexError:
            raise ValueError("No data found in API response")

        data_dict = {
            "symbol": self.clean_value(response.get("symbol"), str),
            "date": self.clean_value(response.get("date"), str),
            "rating": self.clean_value(response.get("rating"), str),
            "rating_score": self.clean_value(response.get("ratingScore"), int),
            "rating_recommendation": self.clean_value(
                response.get("ratingRecommendation"), str
            ),
            "rating_details_dcf_score": self.clean_value(
                response.get("ratingDetailsDCFScore"), int
            ),
            "rating_details_dcf_recommendation": self.clean_value(
                response.get("ratingDetailsDCFRecommendation"), str
            ),
            "rating_details_roe_score": self.clean_value(
                response.get("ratingDetailsROEScore"), int
            ),
            "rating_details_roe_recommendation": self.clean_value(
                response.get("ratingDetailsROERecommendation"), str
            ),
            "rating_details_roa_score": self.clean_value(
                response.get("ratingDetailsROAScore"), int
            ),
            "rating_details_roa_recommendation": self.clean_value(
                response.get("ratingDetailsROARecommendation"), str
            ),
            "rating_details_de_score": self.clean_value(
                response.get("ratingDetailsDEScore"), int
            ),
            "rating_details_de_recommendation": self.clean_value(
                response.get("ratingDetailsDERecommendation"), str
            ),
            "rating_details_pe_score": self.clean_value(
                response.get("ratingDetailsPEScore"), int
            ),
            "rating_details_pe_recommendation": self.clean_value(
                response.get("ratingDetailsPERecommendation"), str
            ),
            "rating_details_pb_score": self.clean_value(
                response.get("ratingDetailsPBScore"), int
            ),
            "rating_details_pb_recommendation": self.clean_value(
                response.get("ratingDetailsPBRecommendation"), str
            ),
        }

        return CompanyRating(**data_dict)
