import pandas as pd
from fmp_py.fmp_base import FmpBase
import os
from dotenv import load_dotenv

from fmp_py.models.statement_analysis import FinancialScore, Ratios, KeyMetrics

load_dotenv()


class FmpStatementAnalysis(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")) -> None:
        super().__init__(api_key)

    ##############################
    # Financial Score
    ##############################
    def financial_score(self, symbol: str) -> FinancialScore:
        url = "v4/score"
        params = {"symbol": symbol, "apikey": self.api_key}
        response = self.get_request(url, params)
        data_df = (
            pd.DataFrame(response)
            .rename(
                columns={
                    "symbol": "symbol",
                    "altmanZScore": "altman_z_score",
                    "piotroskiScore": "piotroski_score",
                    "workingCapital": "working_capital",
                    "totalAssets": "total_assets",
                    "retainedEarnings": "retained_earnings",
                    "ebit": "ebit",
                    "marketCap": "market_cap",
                    "totalLiabilities": "total_liabilities",
                    "revenue": "revenue",
                }
            )
            .astype(
                {
                    "altman_z_score": "float",
                    "piotroski_score": "int",
                    "working_capital": "int",
                    "total_assets": "int",
                    "retained_earnings": "int",
                    "ebit": "int",
                    "market_cap": "int",
                    "total_liabilities": "int",
                    "revenue": "int",
                }
            )
            .iloc[0]
        )

        return FinancialScore(**data_df.to_dict())

    ##############################
    # Ratios TTM
    ##############################
    def ratios_ttm(self, symbol: str) -> Ratios:
        url = f"v3/ratios-ttm/{symbol}"
        params = {"apikey": self.api_key}
        response = self.get_request(url, params)

        data_df = (
            pd.DataFrame(response)
            .rename(
                columns={
                    "dividendYielTTM": "dividend_yield_ttm",
                    "dividendYielPercentageTTM": "dividend_yield_percentage_ttm",
                    "peRatioTTM": "pe_ratio_ttm",
                    "pegRatioTTM": "peg_ratio_ttm",
                    "payoutRatioTTM": "payout_ratio_ttm",
                    "currentRatioTTM": "current_ratio_ttm",
                    "quickRatioTTM": "quick_ratio_ttm",
                    "cashRatioTTM": "cash_ratio_ttm",
                    "daysOfSalesOutstandingTTM": "days_of_sales_outstanding_ttm",
                    "daysOfInventoryOutstandingTTM": "days_of_inventory_outstanding_ttm",
                    "operatingCycleTTM": "operating_cycle_ttm",
                    "daysOfPayablesOutstandingTTM": "days_of_payables_outstanding_ttm",
                    "cashConversionCycleTTM": "cash_conversion_cycle_ttm",
                    "grossProfitMarginTTM": "gross_profit_margin_ttm",
                    "operatingProfitMarginTTM": "operating_profit_margin_ttm",
                    "pretaxProfitMarginTTM": "pretax_profit_margin_ttm",
                    "netProfitMarginTTM": "net_profit_margin_ttm",
                    "effectiveTaxRateTTM": "effective_tax_rate_ttm",
                    "returnOnAssetsTTM": "return_on_assets_ttm",
                    "returnOnEquityTTM": "return_on_equity_ttm",
                    "returnOnCapitalEmployedTTM": "return_on_capital_employed_ttm",
                    "netIncomePerEBTTTM": "net_income_per_ebt_ttm",
                    "ebtPerEbitTTM": "ebt_per_ebit_ttm",
                    "ebitPerRevenueTTM": "ebit_per_revenue_ttm",
                    "debtRatioTTM": "debt_ratio_ttm",
                    "debtEquityRatioTTM": "debt_equity_ratio_ttm",
                    "longTermDebtToCapitalizationTTM": "longterm_debt_to_capitalization_ttm",
                    "totalDebtToCapitalizationTTM": "total_debt_to_capitalization_ttm",
                    "interestCoverageTTM": "interest_coverage_ttm",
                    "cashFlowToDebtRatioTTM": "cash_flow_to_debt_ratio_ttm",
                    "companyEquityMultiplierTTM": "company_equity_multiplier_ttm",
                    "receivablesTurnoverTTM": "receivables_turnover_ttm",
                    "payablesTurnoverTTM": "payables_turnover_ttm",
                    "inventoryTurnoverTTM": "inventory_turnover_ttm",
                    "fixedAssetTurnoverTTM": "fixed_asset_turnover_ttm",
                    "assetTurnoverTTM": "asset_turnover_ttm",
                    "operatingCashFlowPerShareTTM": "operating_cash_flow_per_share_ttm",
                    "freeCashFlowPerShareTTM": "free_cash_flow_per_share_ttm",
                    "cashPerShareTTM": "cash_per_share_ttm",
                    "operatingCashFlowSalesRatioTTM": "operating_cash_flow_sales_ratio_ttm",
                    "freeCashFlowOperatingCashFlowRatioTTM": "free_cash_flow_operating_cash_flow_ratio_ttm",
                    "cashFlowCoverageRatiosTTM": "cash_flow_coverage_ratios_ttm",
                    "shortTermCoverageRatiosTTM": "short_term_coverage_ratios_ttm",
                    "capitalExpenditureCoverageRatioTTM": "capital_expenditure_coverage_ratio_ttm",
                    "dividendPaidAndCapexCoverageRatioTTM": "dividend_paid_and_capex_coverage_ratio_ttm",
                    "priceBookValueRatioTTM": "price_book_value_ratio_ttm",
                    "priceToBookRatioTTM": "price_to_book_ratio_ttm",
                    "priceToSalesRatioTTM": "price_to_sales_ratio_ttm",
                    "priceEarningsRatioTTM": "price_earnings_ratio_ttm",
                    "priceToFreeCashFlowsRatioTTM": "price_to_free_cash_flows_ratio_ttm",
                    "priceToOperatingCashFlowsRatioTTM": "price_to_operating_cash_flows_ratio_ttm",
                    "priceCashFlowRatioTTM": "price_cash_flow_ratio_ttm",
                    "priceEarningsToGrowthRatioTTM": "price_earnings_to_growth_ratio_ttm",
                    "priceSalesRatioTTM": "price_sales_ratio_ttm",
                    "enterpriseValueMultipleTTM": "enterprise_value_multiple_ttm",
                    "priceFairValueTTM": "price_fair_value_ttm",
                    "dividendPerShareTTM": "dividend_per_share_ttm",
                }
            )
            .astype(
                {
                    "dividend_yield_ttm": "float",
                    "dividend_yield_percentage_ttm": "float",
                    "pe_ratio_ttm": "float",
                    "peg_ratio_ttm": "float",
                    "payout_ratio_ttm": "float",
                    "current_ratio_ttm": "float",
                    "quick_ratio_ttm": "float",
                    "cash_ratio_ttm": "float",
                    "days_of_sales_outstanding_ttm": "float",
                    "days_of_inventory_outstanding_ttm": "float",
                    "operating_cycle_ttm": "float",
                    "days_of_payables_outstanding_ttm": "float",
                    "cash_conversion_cycle_ttm": "float",
                    "gross_profit_margin_ttm": "float",
                    "operating_profit_margin_ttm": "float",
                    "pretax_profit_margin_ttm": "float",
                    "net_profit_margin_ttm": "float",
                    "effective_tax_rate_ttm": "float",
                    "return_on_assets_ttm": "float",
                    "return_on_equity_ttm": "float",
                    "return_on_capital_employed_ttm": "float",
                    "net_income_per_ebt_ttm": "float",
                    "ebt_per_ebit_ttm": "float",
                    "ebit_per_revenue_ttm": "float",
                    "debt_ratio_ttm": "float",
                    "debt_equity_ratio_ttm": "float",
                    "longterm_debt_to_capitalization_ttm": "float",
                    "total_debt_to_capitalization_ttm": "float",
                    "interest_coverage_ttm": "float",
                    "cash_flow_to_debt_ratio_ttm": "float",
                    "company_equity_multiplier_ttm": "float",
                    "receivables_turnover_ttm": "float",
                    "payables_turnover_ttm": "float",
                    "inventory_turnover_ttm": "float",
                    "fixed_asset_turnover_ttm": "float",
                    "asset_turnover_ttm": "float",
                    "operating_cash_flow_per_share_ttm": "float",
                    "free_cash_flow_per_share_ttm": "float",
                    "cash_per_share_ttm": "float",
                    "operating_cash_flow_sales_ratio_ttm": "float",
                    "free_cash_flow_operating_cash_flow_ratio_ttm": "float",
                    "cash_flow_coverage_ratios_ttm": "float",
                    "short_term_coverage_ratios_ttm": "float",
                    "capital_expenditure_coverage_ratio_ttm": "float",
                    "dividend_paid_and_capex_coverage_ratio_ttm": "float",
                    "price_book_value_ratio_ttm": "float",
                    "price_to_book_ratio_ttm": "float",
                    "price_to_sales_ratio_ttm": "float",
                    "price_earnings_ratio_ttm": "float",
                    "price_to_free_cash_flows_ratio_ttm": "float",
                    "price_to_operating_cash_flows_ratio_ttm": "float",
                    "price_cash_flow_ratio_ttm": "float",
                    "price_earnings_to_growth_ratio_ttm": "float",
                    "price_sales_ratio_ttm": "float",
                    "enterprise_value_multiple_ttm": "float",
                    "price_fair_value_ttm": "float",
                    "dividend_per_share_ttm": "float",
                }
            )
            .iloc[0]
        )

        return Ratios(**data_df.to_dict())

    ##############################
    # Ratios
    ##############################
    def ratios(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        url = f"v3/ratios/{symbol}"
        params = {"period": period, "limit": limit, "apikey": self.api_key}
        response = self.get_request(url, params)

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
        url = f"v3/key-metrics-ttm/{symbol}"
        params = {"apikey": self.api_key}
        response = self.get_request(url, params)

        data_df = (
            pd.DataFrame(response)
            .rename(
                columns={
                    "revenuePerShareTTM": "revenue_per_share_ttm",
                    "netIncomePerShareTTM": "net_income_per_share_ttm",
                    "operatingCashFlowPerShareTTM": "operating_cash_flow_per_share_ttm",
                    "freeCashFlowPerShareTTM": "free_cash_flow_per_share_ttm",
                    "cashPerShareTTM": "cash_per_share_ttm",
                    "bookValuePerShareTTM": "book_value_per_share_ttm",
                    "tangibleBookValuePerShareTTM": "tangible_book_value_per_share_ttm",
                    "shareholdersEquityPerShareTTM": "shareholders_equity_per_share_ttm",
                    "interestDebtPerShareTTM": "interest_debt_per_share_ttm",
                    "marketCapTTM": "market_cap_ttm",
                    "enterpriseValueTTM": "enterprise_value_ttm",
                    "peRatioTTM": "pe_ratio_ttm",
                    "priceToSalesRatioTTM": "price_to_sales_ratio_ttm",
                    "pocfratioTTM": "pocf_ratio_ttm",
                    "pfcfRatioTTM": "pfcf_ratio_ttm",
                    "pbRatioTTM": "pb_ratio_ttm",
                    "ptbRatioTTM": "ptb_ratio_ttm",
                    "evToSalesTTM": "ev_to_sales_ttm",
                    "enterpriseValueOverEBITDATTM": "enterprise_value_over_ebitda_ttm",
                    "evToOperatingCashFlowTTM": "ev_to_operating_cash_flow_ttm",
                    "evToFreeCashFlowTTM": "ev_to_free_cash_flow_ttm",
                    "earningsYieldTTM": "earnings_yield_ttm",
                    "freeCashFlowYieldTTM": "free_cash_flow_yield_ttm",
                    "debtToEquityTTM": "debt_to_equity_ttm",
                    "debtToAssetsTTM": "debt_to_assets_ttm",
                    "netDebtToEBITDATTM": "net_debt_to_ebitda_ttm",
                    "currentRatioTTM": "current_ratio_ttm",
                    "interestCoverageTTM": "interest_coverage_ttm",
                    "incomeQualityTTM": "income_quality_ttm",
                    "dividendYieldTTM": "dividend_yield_ttm",
                    "dividendYieldPercentageTTM": "dividend_yield_percentage_ttm",
                    "payoutRatioTTM": "payout_ratio_ttm",
                    "salesGeneralAndAdministrativeToRevenueTTM": "sales_general_and_administrative_to_revenue_ttm",
                    "researchAndDevelopementToRevenueTTM": "research_and_developement_to_revenue_ttm",
                    "intangiblesToTotalAssetsTTM": "intangibles_to_total_assets_ttm",
                    "capexToOperatingCashFlowTTM": "capex_to_operating_cash_flow_ttm",
                    "capexToRevenueTTM": "capex_to_revenue_ttm",
                    "capexToDepreciationTTM": "capex_to_depreciation_ttm",
                    "stockBasedCompensationToRevenueTTM": "stock_based_compensation_to_revenue_ttm",
                    "grahamNumberTTM": "graham_number_ttm",
                    "roicTTM": "roic_ttm",
                    "grahamNetNetTTM": "graham_net_net_ttm",
                    "returnOnTangibleAssetsTTM": "return_on_tangible_assets_ttm",
                    "workingCapitalTTM": "working_capital_ttm",
                    "tangibleAssetValueTTM": "tangible_asset_value_ttm",
                    "netCurrentAssetValueTTM": "net_current_asset_value_ttm",
                    "investedCapitalTTM": "invested_capital_ttm",
                    "averageReceivablesTTM": "average_receivables_ttm",
                    "averagePayablesTTM": "average_payables_ttm",
                    "averageInventoryTTM": "average_inventory_ttm",
                    "daysSalesOutstandingTTM": "days_sales_outstanding_ttm",
                    "daysPayablesOutstandingTTM": "days_payables_outstanding_ttm",
                    "daysOfInventoryOnHandTTM": "days_of_inventory_on_hand_ttm",
                    "receivablesTurnoverTTM": "receivables_turnover_ttm",
                    "payablesTurnoverTTM": "payables_turnover_ttm",
                    "inventoryTurnoverTTM": "inventory_turnover_ttm",
                    "capexPerShareTTM": "capex_per_share_ttm",
                    "roeTTM": "roe_ttm",
                    "dividendPerShareTTM": "dividend_per_share_ttm",
                    "debtToMarketCapTTM": "debt_to_market_cap_ttm",
                }
            )
            .astype(
                {
                    "debt_to_market_cap_ttm": "float",
                    "dividend_per_share_ttm": "float",
                    "graham_net_net_ttm": "float",
                    "return_on_tangible_assets_ttm": "float",
                    "revenue_per_share_ttm": "float",
                    "net_income_per_share_ttm": "float",
                    "operating_cash_flow_per_share_ttm": "float",
                    "free_cash_flow_per_share_ttm": "float",
                    "cash_per_share_ttm": "float",
                    "book_value_per_share_ttm": "float",
                    "tangible_book_value_per_share_ttm": "float",
                    "shareholders_equity_per_share_ttm": "float",
                    "interest_debt_per_share_ttm": "float",
                    "market_cap_ttm": "int",
                    "enterprise_value_ttm": "float",
                    "pe_ratio_ttm": "float",
                    "price_to_sales_ratio_ttm": "float",
                    "pocf_ratio_ttm": "float",
                    "pfcf_ratio_ttm": "float",
                    "pb_ratio_ttm": "float",
                    "ptb_ratio_ttm": "float",
                    "ev_to_sales_ttm": "float",
                    "enterprise_value_over_ebitda_ttm": "float",
                    "ev_to_operating_cash_flow_ttm": "float",
                    "ev_to_free_cash_flow_ttm": "float",
                    "earnings_yield_ttm": "float",
                    "free_cash_flow_yield_ttm": "float",
                    "debt_to_equity_ttm": "float",
                    "debt_to_assets_ttm": "float",
                    "net_debt_to_ebitda_ttm": "float",
                    "current_ratio_ttm": "float",
                    "interest_coverage_ttm": "float",
                    "income_quality_ttm": "float",
                    "dividend_yield_ttm": "float",
                    "dividend_yield_percentage_ttm": "float",
                    "payout_ratio_ttm": "float",
                    "sales_general_and_administrative_to_revenue_ttm": "float",
                    "research_and_developement_to_revenue_ttm": "float",
                    "intangibles_to_total_assets_ttm": "float",
                    "capex_to_operating_cash_flow_ttm": "float",
                    "capex_to_revenue_ttm": "float",
                    "capex_to_depreciation_ttm": "float",
                    "stock_based_compensation_to_revenue_ttm": "float",
                    "graham_number_ttm": "float",
                    "roic_ttm": "float",
                    "working_capital_ttm": "float",
                    "tangible_asset_value_ttm": "float",
                    "net_current_asset_value_ttm": "float",
                    "invested_capital_ttm": "float",
                    "average_receivables_ttm": "int",
                    "average_payables_ttm": "int",
                    "average_inventory_ttm": "int",
                    "days_sales_outstanding_ttm": "float",
                    "days_payables_outstanding_ttm": "float",
                    "days_of_inventory_on_hand_ttm": "float",
                    "receivables_turnover_ttm": "float",
                    "payables_turnover_ttm": "float",
                    "inventory_turnover_ttm": "float",
                    "capex_per_share_ttm": "float",
                    "roe_ttm": "float",
                }
            )
        ).iloc[0]

        return KeyMetrics(**data_df.to_dict())

    ##############################
    # Key Metrics
    ##############################
    def key_metrics(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        url = f"v3/key-metrics/{symbol}"
        params = {"period": period, "limit": limit, "apikey": self.api_key}
        response = self.get_request(url, params)

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
