from fmp_py.fmp_base import FmpBase
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


"""
This class is used to retrieve financial statements data from the Financial Modeling Prep API.
Reference: https://site.financialmodelingprep.com/developer/docs#financial-statements

def income_statements(self, symbol: str, period: str = "annual") -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#income-statements-financial-statements

"""


class FmpFinancialStatements(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")):
        super().__init__(api_key)

    ################################
    # Income Statements
    ################################
    def income_statements(self, symbol: str, period: str = "annual"):
        """
        Retrieves the income statements for a given symbol and period.

        Args:
            symbol (str): The symbol of the company.
            period (str, optional): The period of the income statements. Defaults to "annual".

        Returns:
            pandas.DataFrame: A DataFrame containing the income statements data.

        Raises:
            ValueError: If an invalid period is provided.
            ValueError: If no data is found for the specified parameters.
        """

        periods_allowed = ["annual", "quarter"]

        if period not in periods_allowed:
            raise ValueError(f"Invalid period. Allowed periods: {periods_allowed}")

        url = f"v3/income-statement/{symbol}"
        params = {"period": period}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the specified parameters.")

        data_df = (
            pd.DataFrame(response)
            .rename(
                columns={
                    "symbol": "symbol",
                    "date": "date",
                    "reportedCurrency": "reported_currency",
                    "cik": "cik",
                    "fillingDate": "filling_date",
                    "acceptedDate": "accepted_date",
                    "calendarYear": "calendar_year",
                    "period": "period",
                    "revenue": "revenue",
                    "costOfRevenue": "cost_of_revenue",
                    "grossProfit": "gross_profit",
                    "grossProfitRatio": "gross_profit_ratio",
                    "researchAndDevelopmentExpenses": "research_and_development_expenses",
                    "generalAndAdministrativeExpenses": "general_and_administrative_expenses",
                    "sellingAndMarketingExpenses": "selling_and_marketing_expenses",
                    "sellingGeneralAndAdministrativeExpenses": "selling_general_and_administrative_expenses",
                    "otherExpenses": "other_expenses",
                    "operatingExpenses": "operating_expenses",
                    "costAndExpenses": "cost_and_expenses",
                    "interestExpense": "interest_expense",
                    "interestIncome": "interest_income",
                    "depreciationAndAmortization": "depreciation_and_amortization",
                    "ebitda": "ebitda",
                    "ebitdaratio": "ebitda_ratio",
                    "operatingIncome": "operating_income",
                    "operatingIncomeRatio": "operating_income_ratio",
                    "totalOtherIncomeExpensesNet": "total_other_income_expenses_net",
                    "incomeBeforeTax": "income_before_tax",
                    "incomeBeforeTaxRatio": "income_before_tax_ratio",
                    "incomeTaxExpense": "income_tax_expense",
                    "netIncome": "net_income",
                    "netIncomeRatio": "net_income_ratio",
                    "eps": "eps",
                    "epsdiluted": "epsdiluted",
                    "weightedAverageShsOut": "weighted_average_shs_out",
                    "weightedAverageShsOutDil": "weighted_average_shs_out_dil",
                    "link": "link",
                    "finalLink": "final_link",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "date": "datetime64[ns]",
                    "reported_currency": "str",
                    "cik": "str",
                    "filling_date": "datetime64[ns]",
                    "accepted_date": "datetime64[ns]",
                    "calendar_year": "int",
                    "period": "str",
                    "revenue": "int",
                    "cost_of_revenue": "int",
                    "gross_profit": "int",
                    "gross_profit_ratio": "float",
                    "research_and_development_expenses": "int",
                    "general_and_administrative_expenses": "int",
                    "selling_and_marketing_expenses": "int",
                    "selling_general_and_administrative_expenses": "int",
                    "other_expenses": "int",
                    "operating_expenses": "int",
                    "cost_and_expenses": "int",
                    "interest_expense": "int",
                    "interest_income": "int",
                    "depreciation_and_amortization": "int",
                    "ebitda": "int",
                    "ebitda_ratio": "float",
                    "operating_income": "int",
                    "operating_income_ratio": "float",
                    "total_other_income_expenses_net": "int",
                    "income_before_tax": "int",
                    "income_before_tax_ratio": "float",
                    "income_tax_expense": "int",
                    "net_income": "int",
                    "net_income_ratio": "float",
                    "eps": "float",
                    "epsdiluted": "float",
                    "weighted_average_shs_out": "int",
                    "weighted_average_shs_out_dil": "int",
                    "link": "str",
                    "final_link": "str",
                }
            )
        )

        return data_df.sort_values(by="date", ascending=True).reset_index(drop=True)
