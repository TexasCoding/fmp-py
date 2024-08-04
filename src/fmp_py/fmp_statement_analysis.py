# src/fmp_py/fmp_statement_analysis.py
# Define the FmpStatementAnalysis class
import pandas as pd
from fmp_py.fmp_base import FmpBase
import os
from dotenv import load_dotenv

from fmp_py.models.statement_analysis import FinancialScore, Ratios, KeyMetrics

load_dotenv()

"""
The FmpStatementAnalysis class provides methods for retrieving financial statement analysis data from the Financial Modeling Prep API.

API Reference:
    def financial_score(self, symbol: str) -> FinancialScore:
        Reference: https://site.financialmodelingprep.com/developer/docs#financial-score-statement-analysis
        
    def ratios(self, symbol: str, period: str = "annual", limit: int = 20) -> pd.DataFrame
        Reference: https://site.financialmodelingprep.com/developer/docs#ratios-statement-analysis
    
    def ratios_ttm(self, symbol: str) -> Ratios:
        Reference: https://site.financialmodelingprep.com/developer/docs#ratios-ttm-statement-analysis

    def key_metrics_ttm(self, symbol: str) -> KeyMetrics:
        Reference: https://site.financialmodelingprep.com/developer/docs#key-metrics-ttm-statement-analysis
        
    def key_metrics(self, symbol: str, period: str = "annual", limit: int = 20) -> pd.DataFrame:
        Reference: https://site.financialmodelingprep.com/developer/docs#key-metrics-statement-analysis'
    
    def cashflow_growth(self, symbol: str, period: str = "annual", limit: int = 20) -> pd.DataFrame:
        Reference: https://site.financialmodelingprep.com/developer/docs#cashflow-growth-statement-analysis
        
    def income_growth(self, symbol: str, period: str = "annual", limit: int = 20) -> pd.DataFrame:
        Reference: https://site.financialmodelingprep.com/developer/docs#income-growth-statement-analysis
        
    def balance_sheet_growth(self, symbol: str, period: str = "annual", limit: int = 20) -> pd.DataFrame:
        Reference: https://site.financialmodelingprep.com/developer/docs#balance-sheet-growth-statement-analysis
        
    def financial_growth(self, symbol: str, period: str = "annual", limit: int = 20) -> pd.DataFrame:
        Reference: https://site.financialmodelingprep.com/developer/docs#financial-growth-statement-analysis
        
    def owner_earnings(self, symbol: str) -> pd.DataFrame:
        Reference: https://site.financialmodelingprep.com/developer/docs#owner-earnings-statement-analysis
        
    def enterprise_values(self, symbol: str) -> pd.DataFrame:
        Reference: https://site.financialmodelingprep.com/developer/docs#enterprise-values-statement-analysis
"""


class FmpStatementAnalysis(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")) -> None:
        super().__init__(api_key)

    ##############################
    # Enterprise Values
    ##############################
    def enterprise_values(self, symbol: str) -> pd.DataFrame:
        """
        Retrieves the enterprise values data for a given stock symbol.

        Args:
            symbol (str): The stock symbol.

        Returns:
            pd.DataFrame: A DataFrame containing the enterprise values data.

        Raises:
            ValueError: If no data is found for the given symbol.
        """
        url = f"v3/enterprise-values/{symbol}"
        params = {"apikey": self.api_key}

        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the given symbol.")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "symbol": "symbol",
                    "date": "date",
                    "stockPrice": "stock_price",
                    "numberOfShares": "number_of_shares",
                    "marketCapitalization": "market_capitalization",
                    "minusCashAndCashEquivalents": "minus_cash_and_cash_equivalents",
                    "addTotalDebt": "add_total_debt",
                    "enterpriseValue": "enterprise_value",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "date": "datetime64[ns]",
                    "stock_price": "float",
                    "number_of_shares": "int",
                    "market_capitalization": "int",
                    "minus_cash_and_cash_equivalents": "int",
                    "add_total_debt": "int",
                    "enterprise_value": "int",
                }
            )
            .sort_values("date", ascending=True)
            .reset_index(drop=True)
        )

    ##############################
    # Owner Earnings
    ##############################

    def owner_earnings(self, symbol: str) -> pd.DataFrame:
        """
        Retrieves the owner's earnings data for a given stock symbol.

        Args:
            symbol (str): The stock symbol.

        Returns:
            pd.DataFrame: A DataFrame containing the owner's earnings data.

        Raises:
            ValueError: If no data is found for the given symbol.
        """
        url = "v4/owner_earnings"
        params = {"symbol": symbol, "apikey": self.api_key}

        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the given symbol.")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "symbol": "symbol",
                    "date": "date",
                    "averagePPE": "average_ppe",
                    "maintenanceCapex": "maintenance_capex",
                    "ownersEarnings": "owners_earnings",
                    "growthCapex": "growth_capex",
                    "ownersEarningsPerShare": "owners_earnings_per_share",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "date": "datetime64[ns]",
                    "average_ppe": "float",
                    "maintenance_capex": "int",
                    "owners_earnings": "int",
                    "growth_capex": "int",
                    "owners_earnings_per_share": "float",
                }
            )
            .sort_values(by="date", ascending=False)
            .reset_index(drop=True)
        )

    ##############################
    # Financial Growth
    ##############################
    def financial_growth(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        """
        Retrieves the financial growth data for a given stock symbol.

        Args:
            symbol (str): The stock symbol.
            period (str, optional): The period of the data (e.g., "annual", "quarterly"). Defaults to "annual".
            limit (int, optional): The maximum number of records to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the financial growth data.

        Raises:
            ValueError: If the period is not "annual" or "quarterly".
            ValueError: If no data is found for the given symbol.
        """
        if period not in ["annual", "quarterly"]:
            raise ValueError("Invalid period. Must be either 'annual' or 'quarterly'.")

        url = f"v3/financial-growth/{symbol}"
        params = {"period": period, "limit": limit, "apikey": self.api_key}

        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the given symbol.")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "symbol": "symbol",
                    "date": "date",
                    "calendarYear": "calendar_year",
                    "period": "period",
                    "revenueGrowth": "revenue_growth",
                    "grossProfitGrowth": "gross_profit_growth",
                    "ebitgrowth": "ebit_growth",
                    "operatingIncomeGrowth": "operating_income_growth",
                    "netIncomeGrowth": "net_income_growth",
                    "epsgrowth": "eps_growth",
                    "epsdilutedGrowth": "eps_diluted_growth",
                    "weightedAverageSharesGrowth": "weighted_average_shares_growth",
                    "weightedAverageSharesDilutedGrowth": "weighted_average_shares_diluted_growth",
                    "dividendsperShareGrowth": "dividends_per_share_growth",
                    "operatingCashFlowGrowth": "operating_cash_flow_growth",
                    "freeCashFlowGrowth": "free_cash_flow_growth",
                    "tenYRevenueGrowthPerShare": "ten_y_revenue_growth_per_share",
                    "fiveYRevenueGrowthPerShare": "five_y_revenue_growth_per_share",
                    "threeYRevenueGrowthPerShare": "three_y_revenue_growth_per_share",
                    "tenYOperatingCFGrowthPerShare": "ten_y_operating_cf_growth_per_share",
                    "fiveYOperatingCFGrowthPerShare": "five_y_operating_cf_growth_per_share",
                    "threeYOperatingCFGrowthPerShare": "three_y_operating_cf_growth_per_share",
                    "tenYNetIncomeGrowthPerShare": "ten_y_net_income_growth_per_share",
                    "fiveYNetIncomeGrowthPerShare": "five_y_net_income_growth_per_share",
                    "threeYNetIncomeGrowthPerShare": "three_y_net_income_growth_per_share",
                    "tenYShareholdersEquityGrowthPerShare": "ten_y_shareholders_equity_growth_per_share",
                    "fiveYShareholdersEquityGrowthPerShare": "five_y_shareholders_equity_growth_per_share",
                    "threeYShareholdersEquityGrowthPerShare": "three_y_shareholders_equity_growth_per_share",
                    "tenYDividendperShareGrowthPerShare": "ten_y_dividend_per_share_growth_per_share",
                    "fiveYDividendperShareGrowthPerShare": "five_y_dividend_per_share_growth_per_share",
                    "threeYDividendperShareGrowthPerShare": "three_y_dividend_per_share_growth_per_share",
                    "receivablesGrowth": "receivables_growth",
                    "inventoryGrowth": "inventory_growth",
                    "assetGrowth": "asset_growth",
                    "bookValueperShareGrowth": "book_value_per_share_growth",
                    "debtGrowth": "debt_growth",
                    "rdexpenseGrowth": "rdexpense_growth",
                    "sgaexpensesGrowth": "sgaexpenses_growth",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "date": "datetime64[ns]",
                    "calendar_year": "int",
                    "period": "str",
                    "revenue_growth": "float",
                    "gross_profit_growth": "float",
                    "ebit_growth": "float",
                    "operating_income_growth": "float",
                    "net_income_growth": "float",
                    "eps_growth": "float",
                    "eps_diluted_growth": "float",
                    "weighted_average_shares_growth": "float",
                    "weighted_average_shares_diluted_growth": "float",
                    "dividends_per_share_growth": "float",
                    "operating_cash_flow_growth": "float",
                    "free_cash_flow_growth": "float",
                    "ten_y_revenue_growth_per_share": "float",
                    "five_y_revenue_growth_per_share": "float",
                    "three_y_revenue_growth_per_share": "float",
                    "ten_y_operating_cf_growth_per_share": "float",
                    "five_y_operating_cf_growth_per_share": "float",
                    "three_y_operating_cf_growth_per_share": "float",
                    "ten_y_net_income_growth_per_share": "float",
                    "five_y_net_income_growth_per_share": "float",
                    "three_y_net_income_growth_per_share": "float",
                    "ten_y_shareholders_equity_growth_per_share": "float",
                    "five_y_shareholders_equity_growth_per_share": "float",
                    "three_y_shareholders_equity_growth_per_share": "float",
                    "ten_y_dividend_per_share_growth_per_share": "float",
                    "five_y_dividend_per_share_growth_per_share": "float",
                    "three_y_dividend_per_share_growth_per_share": "float",
                    "receivables_growth": "float",
                    "inventory_growth": "float",
                    "asset_growth": "float",
                    "book_value_per_share_growth": "float",
                    "debt_growth": "float",
                    "rdexpense_growth": "float",
                    "sgaexpenses_growth": "float",
                }
            )
            .sort_values("date", ascending=True)
            .reset_index(drop=True)
        )

    ############################
    # Balance Sheet Growth
    ############################
    def balance_sheet_growth(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        """
        Retrieves the balance sheet growth data for a given symbol.

        Args:
            symbol (str): The stock symbol.
            period (str, optional): The period of the data. Can be 'annual' or 'quarterly'. Defaults to 'annual'.
            limit (int, optional): The maximum number of records to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the balance sheet growth data.

        Raises:
            ValueError: If an invalid period is provided.
            ValueError: If no data is found for the given symbol.
        """

        if period not in ["annual", "quarterly"]:
            raise ValueError("Invalid period. Please choose 'annual' or 'quarterly'.")

        url = f"v3/balance-sheet-statement-growth/{symbol}"
        params = {"period": period, "limit": limit, "apikey": self.api_key}

        response = self.get_request(url=url, params=params)

        if not response:
            raise ValueError("No data found for the given symbol.")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "date": "date",
                    "symbol": "symbol",
                    "calendarYear": "calendar_year",
                    "period": "period",
                    "growthCashAndCashEquivalents": "growth_cash_and_cash_equivalents",
                    "growthShortTermInvestments": "growth_short_term_investments",
                    "growthCashAndShortTermInvestments": "growth_cash_and_short_term_investments",
                    "growthNetReceivables": "growth_net_receivables",
                    "growthInventory": "growth_inventory",
                    "growthOtherCurrentAssets": "growth_other_current_assets",
                    "growthTotalCurrentAssets": "growth_total_current_assets",
                    "growthPropertyPlantEquipmentNet": "growth_property_plant_equipment_net",
                    "growthGoodwill": "growth_goodwill",
                    "growthIntangibleAssets": "growth_intangible_assets",
                    "growthGoodwillAndIntangibleAssets": "growth_goodwill_and_intangible_assets",
                    "growthLongTermInvestments": "growth_long_term_investments",
                    "growthTaxAssets": "growth_tax_assets",
                    "growthOtherNonCurrentAssets": "growth_other_non_current_assets",
                    "growthTotalNonCurrentAssets": "growth_total_non_current_assets",
                    "growthOtherAssets": "growth_other_assets",
                    "growthTotalAssets": "growth_total_assets",
                    "growthAccountPayables": "growth_account_payables",
                    "growthShortTermDebt": "growth_short_term_debt",
                    "growthTaxPayables": "growth_tax_payables",
                    "growthDeferredRevenue": "growth_deferred_revenue",
                    "growthOtherCurrentLiabilities": "growth_other_current_liabilities",
                    "growthTotalCurrentLiabilities": "growth_total_current_liabilities",
                    "growthLongTermDebt": "growth_long_term_debt",
                    "growthDeferredRevenueNonCurrent": "growth_deferred_revenue_non_current",
                    "growthDeferrredTaxLiabilitiesNonCurrent": "growth_deferrred_tax_liabilities_non_current",
                    "growthOtherNonCurrentLiabilities": "growth_other_non_current_liabilities",
                    "growthTotalNonCurrentLiabilities": "growth_total_non_current_liabilities",
                    "growthOtherLiabilities": "growth_other_liabilities",
                    "growthTotalLiabilities": "growth_total_liabilities",
                    "growthCommonStock": "growth_common_stock",
                    "growthRetainedEarnings": "growth_retained_earnings",
                    "growthAccumulatedOtherComprehensiveIncomeLoss": "growth_accumulated_other_comprehensive_income_loss",
                    "growthOthertotalStockholdersEquity": "growth_othertotal_stockholders_equity",
                    "growthTotalStockholdersEquity": "growth_total_stockholders_equity",
                    "growthTotalLiabilitiesAndStockholdersEquity": "growth_total_liabilities_and_stockholders_equity",
                    "growthTotalInvestments": "growth_total_investments",
                    "growthTotalDebt": "growth_total_debt",
                    "growthNetDebt": "growth_net_debt",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "symbol": "str",
                    "calendar_year": "int",
                    "period": "str",
                    "growth_cash_and_cash_equivalents": "float",
                    "growth_short_term_investments": "float",
                    "growth_cash_and_short_term_investments": "float",
                    "growth_net_receivables": "float",
                    "growth_inventory": "float",
                    "growth_other_current_assets": "float",
                    "growth_total_current_assets": "float",
                    "growth_property_plant_equipment_net": "float",
                    "growth_goodwill": "float",
                    "growth_intangible_assets": "float",
                    "growth_goodwill_and_intangible_assets": "float",
                    "growth_long_term_investments": "float",
                    "growth_tax_assets": "float",
                    "growth_other_non_current_assets": "float",
                    "growth_total_non_current_assets": "float",
                    "growth_other_assets": "float",
                    "growth_total_assets": "float",
                    "growth_account_payables": "float",
                    "growth_short_term_debt": "float",
                    "growth_tax_payables": "float",
                    "growth_deferred_revenue": "float",
                    "growth_other_current_liabilities": "float",
                    "growth_total_current_liabilities": "float",
                    "growth_long_term_debt": "float",
                    "growth_deferred_revenue_non_current": "float",
                    "growth_deferrred_tax_liabilities_non_current": "float",
                    "growth_other_non_current_liabilities": "float",
                    "growth_total_non_current_liabilities": "float",
                    "growth_other_liabilities": "float",
                    "growth_total_liabilities": "float",
                    "growth_common_stock": "float",
                    "growth_retained_earnings": "float",
                    "growth_accumulated_other_comprehensive_income_loss": "float",
                    "growth_othertotal_stockholders_equity": "float",
                    "growth_total_stockholders_equity": "float",
                    "growth_total_liabilities_and_stockholders_equity": "float",
                    "growth_total_investments": "float",
                    "growth_total_debt": "float",
                    "growth_net_debt": "float",
                }
            )
            .sort_values("date", ascending=True)
            .reset_index(drop=True)
        )

    ##############################
    # Income Growth
    ##############################
    def income_growth(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        """
        Retrieves the income statement growth data for a given symbol.

        Args:
            symbol (str): The stock symbol.
            period (str, optional): The period of the data (e.g., "annual", "quarter"). Defaults to "annual".
            limit (int, optional): The number of data points to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the income statement growth data.

        Raises:
            ValueError: If the provided period is invalid.
            ValueError: If no data is found for the given symbol.
        """
        if period not in ["annual", "quarter"]:
            raise ValueError("Invalid period. Must be 'annual' or 'quarter'.")

        url = f"v3/income-statement-growth/{symbol}"
        params = {"period": period, "limit": limit, "apikey": self.api_key}

        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the provided symbol.")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "date": "date",
                    "symbol": "symbol",
                    "calendarYear": "calendar_year",
                    "period": "period",
                    "growthRevenue": "growth_revenue",
                    "growthCostOfRevenue": "growth_cost_of_revenue",
                    "growthGrossProfit": "growth_gross_profit",
                    "growthGrossProfitRatio": "growth_gross_profit_ratio",
                    "growthResearchAndDevelopmentExpenses": "growth_research_and_development_expenses",
                    "growthGeneralAndAdministrativeExpenses": "growth_general_and_administrative_expenses",
                    "growthSellingAndMarketingExpenses": "growth_selling_and_marketing_expenses",
                    "growthOtherExpenses": "growth_other_expenses",
                    "growthOperatingExpenses": "growth_operating_expenses",
                    "growthCostAndExpenses": "growth_cost_and_expenses",
                    "growthInterestExpense": "growth_interest_expense",
                    "growthDepreciationAndAmortization": "growth_depreciation_and_amortization",
                    "growthEBITDA": "growth_ebitda",
                    "growthEBITDARatio": "growth_ebitda_ratio",
                    "growthOperatingIncome": "growth_operating_income",
                    "growthOperatingIncomeRatio": "growth_operating_income_ratio",
                    "growthTotalOtherIncomeExpensesNet": "growth_total_other_income_expenses_net",
                    "growthIncomeBeforeTax": "growth_income_before_tax",
                    "growthIncomeBeforeTaxRatio": "growth_income_before_tax_ratio",
                    "growthIncomeTaxExpense": "growth_income_tax_expense",
                    "growthNetIncome": "growth_net_income",
                    "growthNetIncomeRatio": "growth_net_income_ratio",
                    "growthEPS": "growth_eps",
                    "growthEPSDiluted": "growth_eps_diluted",
                    "growthWeightedAverageShsOut": "growth_weighted_average_shs_out",
                    "growthWeightedAverageShsOutDil": "growth_weighted_average_shs_out_dil",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "symbol": "str",
                    "calendar_year": "int",
                    "period": "str",
                    "growth_revenue": "float",
                    "growth_cost_of_revenue": "float",
                    "growth_gross_profit": "float",
                    "growth_gross_profit_ratio": "float",
                    "growth_research_and_development_expenses": "float",
                    "growth_general_and_administrative_expenses": "float",
                    "growth_selling_and_marketing_expenses": "float",
                    "growth_other_expenses": "float",
                    "growth_operating_expenses": "float",
                    "growth_cost_and_expenses": "float",
                    "growth_interest_expense": "float",
                    "growth_depreciation_and_amortization": "float",
                    "growth_ebitda": "float",
                    "growth_ebitda_ratio": "float",
                    "growth_operating_income": "float",
                    "growth_operating_income_ratio": "float",
                    "growth_total_other_income_expenses_net": "float",
                    "growth_income_before_tax": "float",
                    "growth_income_before_tax_ratio": "float",
                    "growth_income_tax_expense": "float",
                    "growth_net_income": "float",
                    "growth_net_income_ratio": "float",
                    "growth_eps": "float",
                    "growth_eps_diluted": "float",
                    "growth_weighted_average_shs_out": "float",
                    "growth_weighted_average_shs_out_dil": "float",
                }
            )
            .sort_values("date", ascending=True)
            .reset_index(drop=True)
        )

    ##############################
    # Cash Flow Growth
    ##############################
    def cashflow_growth(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        """
        Retrieves the cash flow growth data for the given stock symbol and period.

        Args:
            symbol (str): The stock symbol to retrieve the cash flow growth data for.
            period (str, optional): The period to retrieve the data for, either 'annual' or 'quarter'. Defaults to 'annual'.
            limit (int, optional): The maximum number of records to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the cash flow growth data for the given stock symbol and period.

        Raises:
            ValueError: If the period is not 'annual' or 'quarter'.
            ValueError: If no data is found for the given symbol and period.
        """
        if period not in ["annual", "quarter"]:
            raise ValueError("Invalid period. Please choose 'annual' or 'quarter'.")

        url = f"v3/cash-flow-statement-growth/{symbol}"
        params = {"period": period, "limit": limit, "apikey": self.api_key}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the given symbol and period.")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "symbol": "symbol",
                    "date": "date",
                    "period": "period",
                    "calendarYear": "calendar_year",
                    "growthNetIncome": "growth_net_income",
                    "growthDepreciationAndAmortization": "growth_depreciation_and_amortization",
                    "growthStockBasedCompensation": "growth_stock_based_compensation",
                    "growthChangeInWorkingCapital": "growth_change_in_working_capital",
                    "growthAccountsReceivables": "growth_accounts_receivables",
                    "growthInventory": "growth_inventory",
                    "growthAccountsPayables": "growth_accounts_payables",
                    "growthOtherWorkingCapital": "growth_other_working_capital",
                    "growthOtherNonCashItems": "growth_other_non_cash_items",
                    "growthNetCashProvidedByOperatingActivites": "growth_net_cash_provided_by_operating_activities",
                    "growthInvestmentsInPropertyPlantAndEquipment": "growth_investments_in_property_plant_and_equipment",
                    "growthAcquisitionsNet": "growth_acquisitions_net",
                    "growthPurchasesOfInvestments": "growth_purchases_of_investments",
                    "growthSalesMaturitiesOfInvestments": "growth_sales_maturities_of_investments",
                    "growthNetCashUsedForInvestingActivites": "growth_net_cash_used_for_investing_activities",
                    "growthDebtRepayment": "growth_debt_repayment",
                    "growthCommonStockIssued": "growth_common_stock_issued",
                    "growthCommonStockRepurchased": "growth_common_stock_repurchased",
                    "growthDeferredIncomeTax": "growth_deferred_income_tax",
                    "growthDividendsPaid": "growth_dividends_paid",
                    "growthNetCashUsedProvidedByFinancingActivities": "growth_net_cash_used_provided_by_financing_activities",
                    "growthEffectOfForexChangesOnCash": "growth_effect_of_forex_changes_on_cash",
                    "growthNetChangeInCash": "growth_net_change_in_cash",
                    "growthCashAtEndOfPeriod": "growth_cash_at_end_of_period",
                    "growthCashAtBeginningOfPeriod": "growth_cash_at_beginning_of_period",
                    "growthOperatingCashFlow": "growth_operating_cash_flow",
                    "growthCapitalExpenditure": "growth_capital_expenditure",
                    "growthFreeCashFlow": "growth_free_cash_flow",
                    "growthOtherInvestingActivites": "growth_other_investing_activites",
                    "growthOtherFinancingActivites": "growth_other_financing_activites",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "date": "datetime64[ns]",
                    "period": "str",
                    "calendar_year": "int",
                    "growth_net_income": "float",
                    "growth_depreciation_and_amortization": "float",
                    "growth_stock_based_compensation": "float",
                    "growth_change_in_working_capital": "float",
                    "growth_accounts_receivables": "float",
                    "growth_inventory": "float",
                    "growth_accounts_payables": "float",
                    "growth_other_working_capital": "float",
                    "growth_other_non_cash_items": "float",
                    "growth_net_cash_provided_by_operating_activities": "float",
                    "growth_investments_in_property_plant_and_equipment": "float",
                    "growth_acquisitions_net": "float",
                    "growth_purchases_of_investments": "float",
                    "growth_sales_maturities_of_investments": "float",
                    "growth_net_cash_used_for_investing_activities": "float",
                    "growth_debt_repayment": "float",
                    "growth_common_stock_issued": "float",
                    "growth_common_stock_repurchased": "float",
                    "growth_deferred_income_tax": "float",
                    "growth_dividends_paid": "float",
                    "growth_net_cash_used_provided_by_financing_activities": "float",
                    "growth_effect_of_forex_changes_on_cash": "float",
                    "growth_net_change_in_cash": "float",
                    "growth_cash_at_end_of_period": "float",
                    "growth_cash_at_beginning_of_period": "float",
                    "growth_operating_cash_flow": "float",
                    "growth_capital_expenditure": "float",
                    "growth_free_cash_flow": "float",
                    "growth_other_investing_activites": "float",
                }
            )
            .sort_values("date", ascending=True)
            .reset_index(drop=True)
        )

    ##############################
    # Financial Score
    ##############################
    def financial_score(self, symbol: str) -> FinancialScore:
        """
        Retrieves the financial score for a given symbol.

        Args:
            symbol (str): The symbol of the company.

        Returns:
            FinancialScore: An object containing the financial score data.

        Raises:
            ValueError: If the symbol is invalid.
        """
        url = "v4/score"
        params = {"symbol": symbol, "apikey": self.api_key}

        try:
            response: dict = self.get_request(url, params)[0]
        except IndexError:
            raise ValueError("Invalid symbol")

        data_dict = {
            "symbol": self.clean_value(response.get("symbol", ""), str),
            "altman_z_score": self.clean_value(
                response.get("altmanZScore", 0.0), float
            ),
            "piotroski_score": self.clean_value(response.get("piotroskiScore", 0), int),
            "working_capital": self.clean_value(response.get("workingCapital", 0), int),
            "total_assets": self.clean_value(response.get("totalAssets", 0), int),
            "retained_earnings": self.clean_value(
                response.get("retainedEarnings", 0), int
            ),
            "ebit": self.clean_value(response.get("ebit", 0), int),
            "market_cap": self.clean_value(response.get("marketCap", 0), int),
            "total_liabilities": self.clean_value(
                response.get("totalLiabilities", 0), int
            ),
            "revenue": self.clean_value(response.get("revenue", 0), int),
        }

        return FinancialScore(**data_dict)

    ##############################
    # Ratios TTM
    ##############################
    def ratios_ttm(self, symbol: str) -> Ratios:
        """
        Retrieves the trailing twelve months (TTM) financial ratios for a given symbol.

        Args:
            symbol (str): The symbol of the company.

        Returns:
            Ratios: An instance of the Ratios class containing the TTM financial ratios.

        Raises:
            ValueError: If the symbol is invalid.
        """
        url = f"v3/ratios-ttm/{symbol}"
        params = {"apikey": self.api_key}

        try:
            response: dict = self.get_request(url, params)[0]
        except IndexError:
            raise ValueError("Invalid symbol")

        data_dict = {
            "dividend_yield_ttm": self.clean_value(
                response.get("dividendYielTTM", 0), float
            ),
            "dividend_yield_percentage_ttm": self.clean_value(
                response.get("dividendYielPercentageTTM", 0), float
            ),
            "pe_ratio_ttm": self.clean_value(response.get("peRatioTTM", 0), float),
            "peg_ratio_ttm": self.clean_value(response.get("pegRatioTTM", 0), float),
            "payout_ratio_ttm": self.clean_value(
                response.get("payoutRatioTTM", 0), float
            ),
            "current_ratio_ttm": self.clean_value(
                response.get("currentRatioTTM", 0), float
            ),
            "quick_ratio_ttm": self.clean_value(
                response.get("quickRatioTTM", 0), float
            ),
            "cash_ratio_ttm": self.clean_value(response.get("cashRatioTTM", 0), float),
            "days_of_sales_outstanding_ttm": self.clean_value(
                response.get("daysOfSalesOutstandingTTM", 0), float
            ),
            "days_of_inventory_outstanding_ttm": self.clean_value(
                response.get("daysOfInventoryOutstandingTTM", 0), float
            ),
            "operating_cycle_ttm": self.clean_value(
                response.get("operatingCycleTTM", 0), float
            ),
            "days_of_payables_outstanding_ttm": self.clean_value(
                response.get("daysOfPayablesOutstandingTTM", 0), float
            ),
            "cash_conversion_cycle_ttm": self.clean_value(
                response.get("cashConversionCycleTTM", 0), float
            ),
            "gross_profit_margin_ttm": self.clean_value(
                response.get("grossProfitMarginTTM", 0), float
            ),
            "operating_profit_margin_ttm": self.clean_value(
                response.get("operatingProfitMarginTTM", 0), float
            ),
            "pretax_profit_margin_ttm": self.clean_value(
                response.get("pretaxProfitMarginTTM", 0), float
            ),
            "net_profit_margin_ttm": self.clean_value(
                response.get("netProfitMarginTTM", 0), float
            ),
            "effective_tax_rate_ttm": self.clean_value(
                response.get("effectiveTaxRateTTM", 0), float
            ),
            "return_on_assets_ttm": self.clean_value(
                response.get("returnOnAssetsTTM", 0), float
            ),
            "return_on_equity_ttm": self.clean_value(
                response.get("returnOnEquityTTM", 0), float
            ),
            "return_on_capital_employed_ttm": self.clean_value(
                response.get("returnOnCapitalEmployedTTM", 0), float
            ),
            "net_income_per_ebt_ttm": self.clean_value(
                response.get("netIncomePerEBTTTM", 0), float
            ),
            "ebt_per_ebit_ttm": self.clean_value(
                response.get("ebtPerEbitTTM", 0), float
            ),
            "ebit_per_revenue_ttm": self.clean_value(
                response.get("ebitPerRevenueTTM", 0), float
            ),
            "debt_ratio_ttm": self.clean_value(response.get("debtRatioTTM", 0), float),
            "debt_equity_ratio_ttm": self.clean_value(
                response.get("debtEquityRatioTTM", 0), float
            ),
            "longterm_debt_to_capitalization_ttm": self.clean_value(
                response.get("longTermDebtToCapitalizationTTM", 0), float
            ),
            "total_debt_to_capitalization_ttm": self.clean_value(
                response.get("totalDebtToCapitalizationTTM", 0), float
            ),
            "interest_coverage_ttm": self.clean_value(
                response.get("interestCoverageTTM", 0), float
            ),
            "cash_flow_to_debt_ratio_ttm": self.clean_value(
                response.get("cashFlowToDebtRatioTTM", 0), float
            ),
            "company_equity_multiplier_ttm": self.clean_value(
                response.get("companyEquityMultiplierTTM", 0), float
            ),
            "receivables_turnover_ttm": self.clean_value(
                response.get("receivablesTurnoverTTM", 0), float
            ),
            "payables_turnover_ttm": self.clean_value(
                response.get("payablesTurnoverTTM", 0), float
            ),
            "inventory_turnover_ttm": self.clean_value(
                response.get("inventoryTurnoverTTM", 0), float
            ),
            "fixed_asset_turnover_ttm": self.clean_value(
                response.get("fixedAssetTurnoverTTM", 0), float
            ),
            "asset_turnover_ttm": self.clean_value(
                response.get("assetTurnoverTTM", 0), float
            ),
            "operating_cash_flow_per_share_ttm": self.clean_value(
                response.get("operatingCashFlowPerShareTTM", 0), float
            ),
            "free_cash_flow_per_share_ttm": self.clean_value(
                response.get("freeCashFlowPerShareTTM", 0), float
            ),
            "cash_per_share_ttm": self.clean_value(
                response.get("cashPerShareTTM", 0), float
            ),
            "operating_cash_flow_sales_ratio_ttm": self.clean_value(
                response.get("operatingCashFlowSalesRatioTTM", 0), float
            ),
            "free_cash_flow_operating_cash_flow_ratio_ttm": self.clean_value(
                response.get("freeCashFlowOperatingCashFlowRatioTTM", 0), float
            ),
            "cash_flow_coverage_ratios_ttm": self.clean_value(
                response.get("cashFlowCoverageRatiosTTM", 0), float
            ),
            "short_term_coverage_ratios_ttm": self.clean_value(
                response.get("shortTermCoverageRatiosTTM", 0), float
            ),
            "capital_expenditure_coverage_ratio_ttm": self.clean_value(
                response.get("capExCoverageRatioTTM", 0), float
            ),
            "dividend_paid_and_capex_coverage_ratio_ttm": self.clean_value(
                response.get("dividendPaidAndCapExCoverageRatioTTM", 0), float
            ),
            "price_book_value_ratio_ttm": self.clean_value(
                response.get("priceBookValueRatioTTM", 0), float
            ),
            "price_to_book_ratio_ttm": self.clean_value(
                response.get("priceToBookRatioTTM", 0), float
            ),
            "price_to_sales_ratio_ttm": self.clean_value(
                response.get("priceToSalesRatioTTM", 0), float
            ),
            "price_earnings_ratio_ttm": self.clean_value(
                response.get("priceEarningsRatioTTM", 0), float
            ),
            "price_to_free_cash_flows_ratio_ttm": self.clean_value(
                response.get("priceToFreeCashFlowsRatioTTM", 0), float
            ),
            "price_to_operating_cash_flows_ratio_ttm": self.clean_value(
                response.get("priceToOperatingCashFlowsRatioTTM", 0), float
            ),
            "price_cash_flow_ratio_ttm": self.clean_value(
                response.get("priceCashFlowRatioTTM", 0), float
            ),
            "price_earnings_to_growth_ratio_ttm": self.clean_value(
                response.get("priceEarningsToGrowthRatioTTM", 0), float
            ),
            "price_sales_ratio_ttm": self.clean_value(
                response.get("priceSalesRatioTTM", 0), float
            ),
            "enterprise_value_multiple_ttm": self.clean_value(
                response.get("enterpriseValueMultipleTTM", 0), float
            ),
            "price_fair_value_ttm": self.clean_value(
                response.get("priceFairValueTTM", 0), float
            ),
            "dividend_per_share_ttm": self.clean_value(
                response.get("dividendPerShareTTM", 0), float
            ),
        }

        return Ratios(**data_dict)

    ##############################
    # Ratios
    ##############################
    def ratios(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        """
        Retrieve financial ratios for a given symbol.

        Args:
            symbol (str): The symbol of the company.
            period (str, optional): The period of the ratios. Defaults to "annual".
            limit (int, optional): The maximum number of ratios to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the financial ratios.

        Raises:
            ValueError: If the period is not 'annual' or 'quarter'.
            ValueError: If no data is found for the symbol.
        """

        if period not in ["annual", "quarter"]:
            raise ValueError("Period must be either 'annual' or 'quarter'")

        url = f"v3/ratios/{symbol}"
        params = {"period": period, "limit": limit, "apikey": self.api_key}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for this symbol")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "date": "date",
                    "symbol": "symbol",
                    "currentRatio": "current_ratio",
                    "quickRatio": "quick_ratio",
                    "cashRatio": "cash_ratio",
                    "daysOfSalesOutstanding": "days_of_sales_outstanding",
                    "daysOfInventoryOutstanding": "days_of_inventory_outstanding",
                    "operatingCycle": "operating_cycle",
                    "daysOfPayablesOutstanding": "days_of_payables_outstanding",
                    "cashConversionCycle": "cash_conversion_cycle",
                    "grossProfitMargin": "gross_profit_margin",
                    "operatingProfitMargin": "operating_profit_margin",
                    "pretaxProfitMargin": "pretax_profit_margin",
                    "netProfitMargin": "net_profit_margin",
                    "effectiveTaxRate": "effective_tax_rate",
                    "returnOnAssets": "return_on_assets",
                    "returnOnEquity": "return_on_equity",
                    "returnOnCapitalEmployed": "return_on_capital_employed",
                    "netIncomePerEBT": "net_income_per_ebt",
                    "ebtPerEbit": "ebt_per_ebit",
                    "ebitPerRevenue": "ebit_per_revenue",
                    "debtRatio": "debt_ratio",
                    "debtEquityRatio": "debt_equity_ratio",
                    "longTermDebtToCapitalization": "longterm_debt_to_capitalization",
                    "totalDebtToCapitalization": "total_debt_to_capitalization",
                    "interestCoverage": "interest_coverage",
                    "cashFlowToDebtRatio": "cash_flow_to_debt_ratio",
                    "companyEquityMultiplier": "company_equity_multiplier",
                    "receivablesTurnover": "receivables_turnover",
                    "payablesTurnover": "payables_turnover",
                    "inventoryTurnover": "inventory_turnover",
                    "fixedAssetTurnover": "fixed_asset_turnover",
                    "assetTurnover": "asset_turnover",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "current_ratio": "float",
                    "quick_ratio": "float",
                    "cash_ratio": "float",
                    "days_of_sales_outstanding": "float",
                    "days_of_inventory_outstanding": "float",
                    "operating_cycle": "float",
                    "days_of_payables_outstanding": "float",
                    "cash_conversion_cycle": "float",
                    "gross_profit_margin": "float",
                    "operating_profit_margin": "float",
                    "pretax_profit_margin": "float",
                    "net_profit_margin": "float",
                    "effective_tax_rate": "float",
                    "return_on_assets": "float",
                    "return_on_equity": "float",
                    "return_on_capital_employed": "float",
                    "net_income_per_ebt": "float",
                    "ebt_per_ebit": "float",
                    "ebit_per_revenue": "float",
                    "debt_ratio": "float",
                    "debt_equity_ratio": "float",
                    "longterm_debt_to_capitalization": "float",
                    "total_debt_to_capitalization": "float",
                    "interest_coverage": "float",
                    "cash_flow_to_debt_ratio": "float",
                    "company_equity_multiplier": "float",
                    "receivables_turnover": "float",
                    "payables_turnover": "float",
                    "inventory_turnover": "float",
                    "fixed_asset_turnover": "float",
                    "asset_turnover": "float",
                }
            )
        ).sort_values("date", ascending=True)

    ##############################
    # Key Metrics TTM
    ##############################
    def key_metrics_ttm(self, symbol: str) -> KeyMetrics:
        """
        Retrieves the key metrics for a given symbol over the trailing twelve months (TTM).

        Args:
            symbol (str): The stock symbol for which to retrieve the key metrics.

        Returns:
            KeyMetrics: An instance of the KeyMetrics class containing the key metrics data.

        Raises:
            ValueError: If no data is found for the given symbol.
        """
        url = f"v3/key-metrics-ttm/{symbol}"
        params = {"apikey": self.api_key}

        try:
            response = self.get_request(url, params)[0]
        except IndexError:
            raise ValueError("No data found for this symbol")

        data_dict = {
            "debt_to_market_cap_ttm": self.clean_value(
                response.get("debtToMarketCapTTM", 0.0), float
            ),
            "dividend_per_share_ttm": self.clean_value(
                response.get("dividendPerShareTTM", 0.0), float
            ),
            "graham_net_net_ttm": self.clean_value(
                response.get("grahamNetNetTTM", 0.0), float
            ),
            "return_on_tangible_assets_ttm": self.clean_value(
                response.get("returnOnTangibleAssetsTTM", 0.0), float
            ),
            "revenue_per_share_ttm": self.clean_value(
                response.get("revenuePerShareTTM", 0.0), float
            ),
            "net_income_per_share_ttm": self.clean_value(
                response.get("netIncomePerShareTTM", 0.0), float
            ),
            "operating_cash_flow_per_share_ttm": self.clean_value(
                response.get("operatingCashFlowPerShareTTM", 0.0), float
            ),
            "free_cash_flow_per_share_ttm": self.clean_value(
                response.get("freeCashFlowPerShareTTM", 0.0), float
            ),
            "cash_per_share_ttm": self.clean_value(
                response.get("cashPerShareTTM", 0.0), float
            ),
            "book_value_per_share_ttm": self.clean_value(
                response.get("bookValuePerShareTTM", 0.0), float
            ),
            "tangible_book_value_per_share_ttm": self.clean_value(
                response.get("tangibleBookValuePerShareTTM", 0.0), float
            ),
            "shareholders_equity_per_share_ttm": self.clean_value(
                response.get("shareholdersEquityPerShareTTM", 0.0), float
            ),
            "interest_debt_per_share_ttm": self.clean_value(
                response.get("interestDebtPerShareTTM", 0.0), float
            ),
            "market_cap_ttm": self.clean_value(
                response.get("marketCapTTM", 0.0), float
            ),
            "enterprise_value_ttm": self.clean_value(
                response.get("enterpriseValueTTM", 0.0), float
            ),
            "pe_ratio_ttm": self.clean_value(response.get("peRatioTTM", 0.0), float),
            "price_to_sales_ratio_ttm": self.clean_value(
                response.get("priceToSalesRatioTTM", 0.0), float
            ),
            "pocf_ratio_ttm": self.clean_value(
                response.get("pocfratioTTM", 0.0), float
            ),
            "pfcf_ratio_ttm": self.clean_value(
                response.get("pfcfRatioTTM", 0.0), float
            ),
            "pb_ratio_ttm": self.clean_value(response.get("pbRatioTTM", 0.0), float),
            "ptb_ratio_ttm": self.clean_value(response.get("ptbRatioTTM", 0.0), float),
            "ev_to_sales_ttm": self.clean_value(
                response.get("evToSalesTTM", 0.0), float
            ),
            "enterprise_value_over_ebitda_ttm": self.clean_value(
                response.get("enterpriseValueOverEBITDATTM", 0.0), float
            ),
            "ev_to_operating_cash_flow_ttm": self.clean_value(
                response.get("evToOperatingCashFlowTTM", 0.0), float
            ),
            "ev_to_free_cash_flow_ttm": self.clean_value(
                response.get("evToFreeCashFlowTTM", 0.0), float
            ),
            "earnings_yield_ttm": self.clean_value(
                response.get("earningsYieldTTM", 0.0), float
            ),
            "free_cash_flow_yield_ttm": self.clean_value(
                response.get("freeCashFlowYieldTTM", 0.0), float
            ),
            "debt_to_equity_ttm": self.clean_value(
                response.get("debtToEquityTTM", 0.0), float
            ),
            "debt_to_assets_ttm": self.clean_value(
                response.get("debtToAssetsTTM", 0.0), float
            ),
            "net_debt_to_ebitda_ttm": self.clean_value(
                response.get("netDebtToEBITDATTM", 0.0), float
            ),
            "current_ratio_ttm": self.clean_value(
                response.get("currentRatioTTM", 0.0), float
            ),
            "interest_coverage_ttm": self.clean_value(
                response.get("interestCoverageTTM", 0.0), float
            ),
            "income_quality_ttm": self.clean_value(
                response.get("incomeQualityTTM", 0.0), float
            ),
            "dividend_yield_ttm": self.clean_value(
                response.get("dividendYieldTTM", 0.0), float
            ),
            "dividend_yield_percentage_ttm": self.clean_value(
                response.get("dividendYieldPercentageTTM", 0.0), float
            ),
            "payout_ratio_ttm": self.clean_value(
                response.get("payoutRatioTTM", 0.0), float
            ),
            "sales_general_and_administrative_to_revenue_ttm": self.clean_value(
                response.get("salesGeneralAndAdministrativeToRevenueTTM", 0.0), float
            ),
            "research_and_developement_to_revenue_ttm": self.clean_value(
                response.get("researchAndDevelopementToRevenueTTM", 0.0), float
            ),
            "intangibles_to_total_assets_ttm": self.clean_value(
                response.get("intangiblesToTotalAssetsTTM", 0.0), float
            ),
            "capex_to_operating_cash_flow_ttm": self.clean_value(
                response.get("capexToOperatingCashFlowTTM", 0.0), float
            ),
            "capex_to_revenue_ttm": self.clean_value(
                response.get("capexToRevenueTTM", 0.0), float
            ),
            "capex_to_depreciation_ttm": self.clean_value(
                response.get("capexToDepreciationTTM", 0.0), float
            ),
            "stock_based_compensation_to_revenue_ttm": self.clean_value(
                response.get("stockBasedCompensationToRevenueTTM", 0.0), float
            ),
            "graham_number_ttm": self.clean_value(
                response.get("grahamNumberTTM", 0.0), float
            ),
            "roic_ttm": self.clean_value(response.get("roicTTM", 0.0), float),
            "working_capital_ttm": self.clean_value(
                response.get("workingCapitalTTM", 0.0), float
            ),
            "tangible_asset_value_ttm": self.clean_value(
                response.get("tangibleAssetValueTTM", 0.0), float
            ),
            "net_current_asset_value_ttm": self.clean_value(
                response.get("netCurrentAssetValueTTM", 0.0), float
            ),
            "invested_capital_ttm": self.clean_value(
                response.get("investedCapitalTTM", 0.0), float
            ),
            "average_receivables_ttm": self.clean_value(
                response.get("averageReceivablesTTM", 0), int
            ),
            "average_payables_ttm": self.clean_value(
                response.get("averagePayablesTTM", 0.0), int
            ),
            "average_inventory_ttm": self.clean_value(
                response.get("averageInventoryTTM", 0), int
            ),
            "days_payables_outstanding_ttm": self.clean_value(
                response.get("daysPayablesOutstandingTTM", 0.0), float
            ),
            "days_sales_outstanding_ttm": self.clean_value(
                response.get("daysSalesOutstandingTTM", 0.0), float
            ),
            "days_of_inventory_on_hand_ttm": self.clean_value(
                response.get("daysOfInventoryOnHandTTM", 0.0), float
            ),
            "receivables_turnover_ttm": self.clean_value(
                response.get("receivablesTurnoverTTM", 0.0), float
            ),
            "payables_turnover_ttm": self.clean_value(
                response.get("payablesTurnoverTTM", 0.0), float
            ),
            "inventory_turnover_ttm": self.clean_value(
                response.get("inventoryTurnoverTTM", 0.0), float
            ),
            "capex_per_share_ttm": self.clean_value(
                response.get("capexPerShareTTM", 0.0), float
            ),
            "roe_ttm": self.clean_value(response.get("roeTTM", 0.0), float),
        }

        return KeyMetrics(**data_dict)

    ##############################
    # Key Metrics
    ##############################
    def key_metrics(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        """
        Retrieves key metrics for a given symbol.

        Args:
            symbol (str): The stock symbol.
            period (str, optional): The period for which to retrieve the metrics. Defaults to "annual".
            limit (int, optional): The maximum number of metrics to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the key metrics.

        Raises:
            ValueError: If the period is not "annual" or "quarter".
            ValueError: If no data is found for the symbol.
        """
        if period not in ["annual", "quarter"]:
            raise ValueError("Period must be either 'annual' or 'quarter'")

        url = f"v3/key-metrics/{symbol}"
        params = {"period": period, "limit": limit, "apikey": self.api_key}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for this symbol")

        return (
            pd.DataFrame(response)
            .rename(
                columns={
                    "calendarYear": "calendar_year",
                    "revenuePerShare": "revenue_per_share",
                    "netIncomePerShare": "net_income_per_share",
                    "operatingCashFlowPerShare": "operating_cash_flow_per_share",
                    "freeCashFlowPerShare": "free_cash_flow_per_share",
                    "cashPerShare": "cash_per_share",
                    "bookValuePerShare": "book_value_per_share",
                    "tangibleBookValuePerShare": "tangible_book_value_per_share",
                    "shareholdersEquityPerShare": "shareholders_equity_per_share",
                    "interestDebtPerShare": "interest_debt_per_share",
                    "marketCap": "market_cap",
                    "enterpriseValue": "enterprise_value",
                    "peRatio": "pe_ratio",
                    "priceToSalesRatio": "price_to_sales_ratio",
                    "pocfratio": "pocf_ratio",
                    "pfcfRatio": "pfcf_ratio",
                    "pbRatio": "pb_ratio",
                    "ptbRatio": "ptb_ratio",
                    "evToSales": "ev_to_sales",
                    "enterpriseValueOverEBITDA": "enterprise_value_over_ebitda",
                    "evToOperatingCashFlow": "ev_to_operating_cash_flow",
                    "evToFreeCashFlow": "ev_to_free_cash_flow",
                    "earningsYield": "earnings_yield",
                    "freeCashFlowYield": "free_cash_flow_yield",
                    "debtToEquity": "debt_to_equity",
                    "debtToAssets": "debt_to_assets",
                    "netDebtToEBITDA": "net_debt_to_ebitda",
                    "currentRatio": "current_ratio",
                    "interestCoverage": "interest_coverage",
                    "incomeQuality": "income_quality",
                    "dividendYield": "dividend_yield",
                    "payoutRatio": "payout_ratio",
                    "salesGeneralAndAdministrativeToRevenue": "sales_general_and_administrative_to_revenue",
                    "researchAndDdevelopementToRevenue": "research_and_developement_to_revenue",
                    "intangiblesToTotalAssets": "intangibles_to_total_assets",
                    "capexToOperatingCashFlow": "capex_to_operating_cash_flow",
                    "capexToRevenue": "capex_to_revenue",
                    "capexToDepreciation": "capex_to_depreciation",
                    "stockBasedCompensationToRevenue": "stock_based_compensation_to_revenue",
                    "grahamNumber": "graham_number",
                    "returnOnTangibleAssets": "return_on_tangible_assets",
                    "grahamNetNet": "graham_net_net",
                    "workingCapital": "working_capital",
                    "tangibleAssetValue": "tangible_asset_value",
                    "netCurrentAssetValue": "net_current_asset_value",
                    "investedCapital": "invested_capital",
                    "averageReceivables": "average_receivables",
                    "averagePayables": "average_payables",
                    "averageInventory": "average_inventory",
                    "daysSalesOutstanding": "days_sales_outstanding",
                    "daysPayablesOutstanding": "days_payables_outstanding",
                    "daysOfInventoryOnHand": "days_of_inventory_on_hand",
                    "receivablesTurnover": "receivables_turnover",
                    "payablesTurnover": "payables_turnover",
                    "inventoryTurnover": "inventory_turnover",
                    "capexPerShare": "capex_per_share",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "calendar_year": "int",
                    "revenue_per_share": "float",
                    "net_income_per_share": "float",
                    "operating_cash_flow_per_share": "float",
                    "free_cash_flow_per_share": "float",
                    "cash_per_share": "float",
                    "book_value_per_share": "float",
                    "tangible_book_value_per_share": "float",
                    "shareholders_equity_per_share": "float",
                    "interest_debt_per_share": "float",
                    "market_cap": "float",
                    "enterprise_value": "float",
                    "pe_ratio": "float",
                    "price_to_sales_ratio": "float",
                    "pocf_ratio": "float",
                    "pfcf_ratio": "float",
                    "pb_ratio": "float",
                    "ptb_ratio": "float",
                    "ev_to_sales": "float",
                    "enterprise_value_over_ebitda": "float",
                    "ev_to_operating_cash_flow": "float",
                    "ev_to_free_cash_flow": "float",
                    "earnings_yield": "float",
                    "free_cash_flow_yield": "float",
                    "debt_to_equity": "float",
                    "debt_to_assets": "float",
                    "net_debt_to_ebitda": "float",
                    "current_ratio": "float",
                    "interest_coverage": "float",
                    "income_quality": "float",
                    "dividend_yield": "float",
                    "payout_ratio": "float",
                    "sales_general_and_administrative_to_revenue": "float",
                    "research_and_developement_to_revenue": "float",
                    "intangibles_to_total_assets": "float",
                    "capex_to_operating_cash_flow": "float",
                    "capex_to_revenue": "float",
                    "capex_to_depreciation": "float",
                    "stock_based_compensation_to_revenue": "float",
                    "graham_number": "float",
                    "return_on_tangible_assets": "float",
                    "graham_net_net": "float",
                    "working_capital": "float",
                    "tangible_asset_value": "float",
                    "net_current_asset_value": "float",
                    "invested_capital": "float",
                    "average_receivables": "float",
                    "average_payables": "float",
                    "days_sales_outstanding": "float",
                    "days_payables_outstanding": "float",
                    "days_of_inventory_on_hand": "float",
                    "receivables_turnover": "float",
                    "payables_turnover": "float",
                    "inventory_turnover": "float",
                    "capex_per_share": "float",
                }
            )
            .sort_values("date", ascending=True)
            .reset_index(drop=True)
        )
