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

def balance_sheet_statements(self, symbol: str, period: str = "annual", limit: int = 20) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#balance-sheet-statements-financial-statements
    
def cashflow_statements(self, symbol: str, period: str = "annual", limit: int = 20) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#cashflow-statements-financial-statements
"""


class FmpFinancialStatements(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")):
        super().__init__(api_key)

    ############################
    # Cash Flow Statements
    ############################
    def cashflow_statements(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        """
        Retrieves the cash flow statements for a given symbol.

        Args:
            symbol (str): The stock symbol.
            period (str, optional): The period of the statements. Allowed values are "annual" and "quarter". Defaults to "annual".
            limit (int, optional): The maximum number of statements to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the cash flow statements.

        Raises:
            ValueError: If an invalid period is provided.
            ValueError: If no data is found for the specified parameters.
        """

        periods_allowed = ["annual", "quarter"]

        if period not in periods_allowed:
            raise ValueError(f"Invalid period. Allowed periods: {periods_allowed}")

        url = f"v3/cash-flow-statement/{symbol}"
        params = {"period": period, "limit": limit}

        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the specified parameters.")

        data_df = (
            pd.DataFrame(response)
            .rename(
                columns={
                    "date": "date",
                    "symbol": "symbol",
                    "reportedCurrency": "reported_currency",
                    "cik": "cik",
                    "fillingDate": "filling_date",
                    "acceptedDate": "accepted_date",
                    "calendarYear": "calendar_year",
                    "period": "period",
                    "netIncome": "net_income",
                    "depreciationAndAmortization": "depreciation_and_amortization",
                    "deferredIncomeTax": "deferred_income_tax",
                    "stockBasedCompensation": "stock_based_compensation",
                    "changeInWorkingCapital": "change_in_working_capital",
                    "accountsReceivables": "accounts_receivables",
                    "inventory": "inventory",
                    "accountsPayables": "accounts_payables",
                    "otherWorkingCapital": "other_working_capital",
                    "otherNonCashItems": "other_non_cash_items",
                    "netCashProvidedByOperatingActivities": "net_cash_provided_by_operating_activities",
                    "investmentsInPropertyPlantAndEquipment": "investments_in_property_plant_and_equipment",
                    "acquisitionsNet": "acquisitions_net",
                    "purchasesOfInvestments": "purchases_of_investments",
                    "salesMaturitiesOfInvestments": "sales_maturities_of_investments",
                    "otherInvestingActivites": "other_investing_activites",
                    "netCashUsedForInvestingActivites": "net_cash_used_for_investing_activites",
                    "debtRepayment": "debt_repayment",
                    "commonStockIssued": "common_stock_issued",
                    "commonStockRepurchased": "common_stock_repurchased",
                    "dividendsPaid": "dividends_paid",
                    "otherFinancingActivites": "other_financing_activites",
                    "netCashUsedProvidedByFinancingActivities": "net_cash_used_provided_by_financing_activities",
                    "effectOfForexChangesOnCash": "effect_of_forex_changes_on_cash",
                    "netChangeInCash": "net_change_in_cash",
                    "cashAtEndOfPeriod": "cash_at_end_of_period",
                    "cashAtBeginningOfPeriod": "cash_at_beginning_of_period",
                    "operatingCashFlow": "operating_cash_flow",
                    "capitalExpenditure": "capital_expenditure",
                    "freeCashFlow": "free_cash_flow",
                    "link": "link",
                    "finalLink": "final_link",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "symbol": "str",
                    "reported_currency": "str",
                    "cik": "str",
                    "filling_date": "datetime64[ns]",
                    "accepted_date": "datetime64[ns]",
                    "calendar_year": "int64",
                    "period": "str",
                    "net_income": "int",
                    "depreciation_and_amortization": "int",
                    "deferred_income_tax": "int",
                    "stock_based_compensation": "int",
                    "change_in_working_capital": "int",
                    "accounts_receivables": "int",
                    "inventory": "int",
                    "accounts_payables": "int",
                    "other_working_capital": "int",
                    "other_non_cash_items": "int",
                    "net_cash_provided_by_operating_activities": "int",
                    "investments_in_property_plant_and_equipment": "int",
                    "acquisitions_net": "int",
                    "purchases_of_investments": "int",
                    "sales_maturities_of_investments": "int",
                    "other_investing_activites": "int",
                    "net_cash_used_for_investing_activites": "int",
                    "debt_repayment": "int",
                    "common_stock_issued": "int",
                    "common_stock_repurchased": "int",
                    "dividends_paid": "int",
                    "other_financing_activites": "int",
                    "net_cash_used_provided_by_financing_activities": "int",
                    "effect_of_forex_changes_on_cash": "int",
                    "net_change_in_cash": "int",
                    "cash_at_end_of_period": "int",
                    "cash_at_beginning_of_period": "int",
                    "operating_cash_flow": "int",
                    "capital_expenditure": "int",
                    "free_cash_flow": "int",
                    "link": "str",
                    "final_link": "str",
                }
            )
        )

        return data_df.sort_values(by="date", ascending=True).reset_index(drop=True)

    ################################
    # Balance Sheet Statements
    ################################
    def balance_sheet_statements(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        """
        Retrieves the balance sheet statements for a given symbol.

        Args:
            symbol (str): The stock symbol.
            period (str, optional): The period of the statements. Defaults to "annual".
            limit (int, optional): The maximum number of statements to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the balance sheet statements.

        Raises:
            ValueError: If no data is found for the provided symbol.
        """
        periods_allowed = ["annual", "quarter"]

        if period not in periods_allowed:
            raise ValueError(f"Invalid period. Allowed periods: {periods_allowed}")

        url = f"v3/balance-sheet-statement/{symbol}"
        params = {"period": period, "limit": limit}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the provided symbol.")

        data_df = (
            pd.DataFrame(response)
            .rename(
                columns={
                    "date": "date",
                    "symbol": "symbol",
                    "reportedCurrency": "reported_currency",
                    "cik": "cik",
                    "fillingDate": "filling_date",
                    "acceptedDate": "accepted_date",
                    "calendarYear": "calendar_year",
                    "period": "period",
                    "cashAndCashEquivalents": "cash_and_cash_equivalents",
                    "shortTermInvestments": "short_term_investments",
                    "cashAndShortTermInvestments": "cash_and_short_term_investments",
                    "netReceivables": "net_receivables",
                    "inventory": "inventory",
                    "otherCurrentAssets": "other_current_assets",
                    "totalCurrentAssets": "total_current_assets",
                    "propertyPlantEquipmentNet": "property_plant_equipment_net",
                    "goodwill": "goodwill",
                    "intangibleAssets": "intangible_assets",
                    "goodwillAndIntangibleAssets": "goodwill_and_intangible_assets",
                    "longTermInvestments": "long_term_investments",
                    "taxAssets": "tax_assets",
                    "otherNonCurrentAssets": "other_non_current_assets",
                    "totalNonCurrentAssets": "total_non_current_assets",
                    "otherAssets": "other_assets",
                    "totalAssets": "total_assets",
                    "accountPayables": "account_payables",
                    "shortTermDebt": "short_term_debt",
                    "taxPayables": "tax_payables",
                    "deferredRevenue": "deferred_revenue",
                    "otherCurrentLiabilities": "other_current_liabilities",
                    "totalCurrentLiabilities": "total_current_liabilities",
                    "longTermDebt": "long_term_debt",
                    "deferredRevenueNonCurrent": "deferred_revenue_non_current",
                    "deferredTaxLiabilitiesNonCurrent": "deferred_tax_liabilities_non_current",
                    "otherNonCurrentLiabilities": "other_non_current_liabilities",
                    "totalNonCurrentLiabilities": "total_non_current_liabilities",
                    "otherLiabilities": "other_liabilities",
                    "capitalLeaseObligations": "capital_lease_obligations",
                    "totalLiabilities": "total_liabilities",
                    "commonStock": "common_stock",
                    "retainedEarnings": "retained_earnings",
                    "accumulatedOtherComprehensiveIncomeLoss": "accumulated_other_comprehensive_income_loss",
                    "totalStockholdersEquity": "total_stockholders_equity",
                    "totalEquity": "total_equity",
                    "totalLiabilitiesAndStockholdersEquity": "total_liabilities_and_stockholders_equity",
                    "minorityInterest": "minority_interest",
                    "totalLiabilitiesAndTotalEquity": "total_liabilities_and_total_equity",
                    "totalInvestments": "total_investments",
                    "totalDebt": "total_debt",
                    "netDebt": "net_debt",
                    "link": "link",
                    "finalLink": "final_link",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "symbol": "str",
                    "reported_currency": "str",
                    "cik": "str",
                    "filling_date": "datetime64[ns]",
                    "accepted_date": "datetime64[ns]",
                    "calendar_year": "int",
                    "period": "str",
                    "cash_and_cash_equivalents": "int",
                    "short_term_investments": "int",
                    "cash_and_short_term_investments": "int",
                    "net_receivables": "int",
                    "inventory": "int",
                    "other_current_assets": "int",
                    "total_current_assets": "int",
                    "property_plant_equipment_net": "int",
                    "goodwill": "int",
                    "intangible_assets": "int",
                    "goodwill_and_intangible_assets": "int",
                    "long_term_investments": "int",
                    "tax_assets": "int",
                    "other_non_current_assets": "int",
                    "total_non_current_assets": "int",
                    "other_assets": "int",
                    "total_assets": "int",
                    "account_payables": "int",
                    "short_term_debt": "int",
                    "tax_payables": "int",
                    "deferred_revenue": "int",
                    "other_current_liabilities": "int",
                    "total_current_liabilities": "int",
                    "long_term_debt": "int",
                    "deferred_revenue_non_current": "int",
                    "deferred_tax_liabilities_non_current": "int",
                    "other_non_current_liabilities": "int",
                    "total_non_current_liabilities": "int",
                    "other_liabilities": "int",
                    "capital_lease_obligations": "int",
                    "total_liabilities": "int",
                    "common_stock": "int",
                    "retained_earnings": "int",
                    "accumulated_other_comprehensive_income_loss": "int",
                    "total_stockholders_equity": "int",
                    "total_equity": "int",
                    "total_liabilities_and_stockholders_equity": "int",
                    "minority_interest": "int",
                    "total_liabilities_and_total_equity": "int",
                    "total_investments": "int",
                    "total_debt": "int",
                    "net_debt": "int",
                    "link": "str",
                    "final_link": "str",
                }
            )
        )
        return data_df.sort_values(by="date", ascending=True).reset_index(drop=True)

    ################################
    # Income Statements
    ################################
    def income_statements(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        """
        Retrieves the income statements for a given symbol.

        Args:
            symbol (str): The stock symbol.
            period (str, optional): The period of the income statements. Defaults to "annual".
            limit (int, optional): The maximum number of income statements to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the income statements data.

        Raises:
            ValueError: If an invalid period is provided.
            ValueError: If no data is found for the specified parameters.
        """

        periods_allowed = ["annual", "quarter"]

        if period not in periods_allowed:
            raise ValueError(f"Invalid period. Allowed periods: {periods_allowed}")

        url = f"v3/income-statement/{symbol}"
        params = {"period": period, "limit": limit}
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
