import numpy as np
import pandas as pd
import pytest

from fmp_py.fmp_statement_analysis import FmpStatementAnalysis
from fmp_py.models.statement_analysis import FinancialScore, KeyMetrics, Ratios


@pytest.fixture
def statement_analysis():
    return FmpStatementAnalysis()


def test_fmp_statement_analysis_initialization(statement_analysis):
    assert isinstance(statement_analysis, FmpStatementAnalysis)


def test_fmp_statement_analysis_key_metrics(statement_analysis):
    key_metrics = statement_analysis.key_metrics("AAPL")
    assert isinstance(key_metrics, pd.DataFrame)
    assert isinstance(key_metrics.iloc[0]["symbol"], str)
    assert isinstance(key_metrics.iloc[0]["date"], pd.Timestamp)
    assert isinstance(key_metrics.iloc[0]["period"], str)
    assert isinstance(key_metrics.iloc[0]["revenue_per_share"], np.float64)
    assert isinstance(key_metrics.iloc[0]["net_income_per_share"], np.float64)
    assert isinstance(key_metrics.iloc[0]["operating_cash_flow_per_share"], np.float64)
    assert isinstance(key_metrics.iloc[0]["free_cash_flow_per_share"], np.float64)
    assert isinstance(key_metrics.iloc[0]["cash_per_share"], np.float64)
    assert isinstance(key_metrics.iloc[0]["book_value_per_share"], np.float64)
    assert isinstance(key_metrics.iloc[0]["tangible_book_value_per_share"], np.float64)
    assert isinstance(key_metrics.iloc[0]["shareholders_equity_per_share"], np.float64)
    assert isinstance(key_metrics.iloc[0]["interest_debt_per_share"], np.float64)
    assert isinstance(key_metrics.iloc[0]["market_cap"], np.float64)
    assert isinstance(key_metrics.iloc[0]["enterprise_value"], np.float64)
    assert isinstance(key_metrics.iloc[0]["pe_ratio"], np.float64)
    assert isinstance(key_metrics.iloc[0]["price_to_sales_ratio"], np.float64)
    assert isinstance(key_metrics.iloc[0]["pocf_ratio"], np.float64)
    assert isinstance(key_metrics.iloc[0]["pfcf_ratio"], np.float64)
    assert isinstance(key_metrics.iloc[0]["pb_ratio"], np.float64)
    assert isinstance(key_metrics.iloc[0]["ptb_ratio"], np.float64)
    assert isinstance(key_metrics.iloc[0]["ev_to_sales"], np.float64)
    assert isinstance(key_metrics.iloc[0]["enterprise_value_over_ebitda"], np.float64)
    assert isinstance(key_metrics.iloc[0]["ev_to_operating_cash_flow"], np.float64)
    assert isinstance(key_metrics.iloc[0]["ev_to_free_cash_flow"], np.float64)
    assert isinstance(key_metrics.iloc[0]["earnings_yield"], np.float64)
    assert isinstance(key_metrics.iloc[0]["free_cash_flow_yield"], np.float64)
    assert isinstance(key_metrics.iloc[0]["debt_to_equity"], np.float64)
    assert isinstance(key_metrics.iloc[0]["debt_to_assets"], np.float64)
    assert isinstance(key_metrics.iloc[0]["net_debt_to_ebitda"], np.float64)
    assert isinstance(key_metrics.iloc[0]["current_ratio"], np.float64)
    assert isinstance(key_metrics.iloc[0]["interest_coverage"], np.float64)
    assert isinstance(key_metrics.iloc[0]["income_quality"], np.float64)
    assert isinstance(key_metrics.iloc[0]["dividend_yield"], np.float64)
    assert isinstance(key_metrics.iloc[0]["payout_ratio"], np.float64)
    assert isinstance(
        key_metrics.iloc[0]["sales_general_and_administrative_to_revenue"], np.float64
    )
    assert isinstance(
        key_metrics.iloc[0]["research_and_developement_to_revenue"], np.float64
    )
    assert isinstance(key_metrics.iloc[0]["intangibles_to_total_assets"], np.float64)
    assert isinstance(key_metrics.iloc[0]["capex_to_operating_cash_flow"], np.float64)
    assert isinstance(key_metrics.iloc[0]["capex_to_revenue"], np.float64)
    assert isinstance(key_metrics.iloc[0]["capex_to_depreciation"], np.float64)
    assert isinstance(
        key_metrics.iloc[0]["stock_based_compensation_to_revenue"], np.float64
    )
    assert isinstance(key_metrics.iloc[0]["graham_number"], np.float64)
    assert isinstance(key_metrics.iloc[0]["return_on_tangible_assets"], np.float64)
    assert isinstance(key_metrics.iloc[0]["graham_net_net"], np.float64)
    assert isinstance(key_metrics.iloc[0]["working_capital"], np.float64)
    assert isinstance(key_metrics.iloc[0]["tangible_asset_value"], np.float64)
    assert isinstance(key_metrics.iloc[0]["net_current_asset_value"], np.float64)
    assert isinstance(key_metrics.iloc[0]["invested_capital"], np.float64)
    assert isinstance(key_metrics.iloc[0]["average_receivables"], np.float64)
    assert isinstance(key_metrics.iloc[0]["average_payables"], np.float64)
    assert isinstance(key_metrics.iloc[0]["days_sales_outstanding"], np.float64)
    assert isinstance(key_metrics.iloc[0]["days_payables_outstanding"], np.float64)
    assert isinstance(key_metrics.iloc[0]["days_of_inventory_on_hand"], np.float64)
    assert isinstance(key_metrics.iloc[0]["receivables_turnover"], np.float64)
    assert isinstance(key_metrics.iloc[0]["payables_turnover"], np.float64)
    assert isinstance(key_metrics.iloc[0]["inventory_turnover"], np.float64)
    assert isinstance(key_metrics.iloc[0]["capex_per_share"], np.float64)


def test_fmp_statement_analysis_key_metrics_invalid_symbol(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.key_metrics("INVALID")


def test_fmp_statement_analysis_key_metrics_invalid_period(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.key_metrics("AAPL", period="INVALID")


def test_fmp_statement_analysis_key_metrics_limit_check(statement_analysis):
    metrics = statement_analysis.key_metrics("AAPL", limit=10)
    assert len(metrics) == 10


def test_fmp_statement_analysis_key_metrics_ttm(statement_analysis):
    key_metrics = statement_analysis.key_metrics_ttm("AAPL")
    assert isinstance(key_metrics, KeyMetrics)
    assert isinstance(key_metrics.revenue_per_share_ttm, float)
    assert isinstance(key_metrics.net_income_per_share_ttm, float)
    assert isinstance(key_metrics.operating_cash_flow_per_share_ttm, float)
    assert isinstance(key_metrics.free_cash_flow_per_share_ttm, float)
    assert isinstance(key_metrics.cash_per_share_ttm, float)
    assert isinstance(key_metrics.book_value_per_share_ttm, float)
    assert isinstance(key_metrics.tangible_book_value_per_share_ttm, float)
    assert isinstance(key_metrics.shareholders_equity_per_share_ttm, float)
    assert isinstance(key_metrics.interest_debt_per_share_ttm, float)
    assert isinstance(key_metrics.market_cap_ttm, float)
    assert isinstance(key_metrics.enterprise_value_ttm, float)
    assert isinstance(key_metrics.pe_ratio_ttm, float)
    assert isinstance(key_metrics.price_to_sales_ratio_ttm, float)
    assert isinstance(key_metrics.pocf_ratio_ttm, float)
    assert isinstance(key_metrics.pfcf_ratio_ttm, float)
    assert isinstance(key_metrics.pb_ratio_ttm, float)
    assert isinstance(key_metrics.ptb_ratio_ttm, float)
    assert isinstance(key_metrics.ev_to_sales_ttm, float)
    assert isinstance(key_metrics.enterprise_value_over_ebitda_ttm, float)
    assert isinstance(key_metrics.debt_to_market_cap_ttm, float)
    assert isinstance(key_metrics.ev_to_operating_cash_flow_ttm, float)
    assert isinstance(key_metrics.dividend_per_share_ttm, float)
    assert isinstance(key_metrics.ev_to_free_cash_flow_ttm, float)
    assert isinstance(key_metrics.earnings_yield_ttm, float)
    assert isinstance(key_metrics.free_cash_flow_yield_ttm, float)
    assert isinstance(key_metrics.debt_to_equity_ttm, float)
    assert isinstance(key_metrics.debt_to_assets_ttm, float)
    assert isinstance(key_metrics.net_debt_to_ebitda_ttm, float)
    assert isinstance(key_metrics.graham_net_net_ttm, float)
    assert isinstance(key_metrics.return_on_tangible_assets_ttm, float)
    assert isinstance(key_metrics.current_ratio_ttm, float)
    assert isinstance(key_metrics.interest_coverage_ttm, float)
    assert isinstance(key_metrics.income_quality_ttm, float)
    assert isinstance(key_metrics.dividend_yield_ttm, float)
    assert isinstance(key_metrics.dividend_yield_percentage_ttm, float)
    assert isinstance(key_metrics.payout_ratio_ttm, float)
    assert isinstance(
        key_metrics.sales_general_and_administrative_to_revenue_ttm, float
    )
    assert isinstance(key_metrics.research_and_developement_to_revenue_ttm, float)
    assert isinstance(key_metrics.intangibles_to_total_assets_ttm, float)
    assert isinstance(key_metrics.capex_to_operating_cash_flow_ttm, float)
    assert isinstance(key_metrics.capex_to_revenue_ttm, float)
    assert isinstance(key_metrics.capex_to_depreciation_ttm, float)
    assert isinstance(key_metrics.stock_based_compensation_to_revenue_ttm, float)
    assert isinstance(key_metrics.graham_number_ttm, float)
    assert isinstance(key_metrics.roic_ttm, float)
    assert isinstance(key_metrics.working_capital_ttm, float)
    assert isinstance(key_metrics.tangible_asset_value_ttm, float)
    assert isinstance(key_metrics.net_current_asset_value_ttm, float)
    assert isinstance(key_metrics.invested_capital_ttm, float)
    assert isinstance(key_metrics.average_receivables_ttm, int)
    assert isinstance(key_metrics.average_payables_ttm, int)
    assert isinstance(key_metrics.average_inventory_ttm, int)
    assert isinstance(key_metrics.days_sales_outstanding_ttm, float)
    assert isinstance(key_metrics.days_payables_outstanding_ttm, float)
    assert isinstance(key_metrics.days_of_inventory_on_hand_ttm, float)
    assert isinstance(key_metrics.receivables_turnover_ttm, float)
    assert isinstance(key_metrics.payables_turnover_ttm, float)
    assert isinstance(key_metrics.inventory_turnover_ttm, float)
    assert isinstance(key_metrics.capex_per_share_ttm, float)
    assert isinstance(key_metrics.roe_ttm, float)


def test_fmp_statement_analysis_key_metrics_ttm_invalid_symbol(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.key_metrics_ttm("INVALID_SYMBOL")


def test_fmp_statement_analysis_ratios(statement_analysis):
    ratios = statement_analysis.ratios("AAPL")
    assert isinstance(ratios, pd.DataFrame)
    assert isinstance(ratios.iloc[0]["symbol"], str)
    assert isinstance(ratios.iloc[0]["date"], pd.Timestamp)
    assert isinstance(ratios.iloc[0]["period"], str)
    assert isinstance(ratios.iloc[0]["current_ratio"], np.float64)
    assert isinstance(ratios.iloc[0]["quick_ratio"], np.float64)
    assert isinstance(ratios.iloc[0]["cash_ratio"], np.float64)
    assert isinstance(ratios.iloc[0]["days_of_sales_outstanding"], np.float64)
    assert isinstance(ratios.iloc[0]["days_of_inventory_outstanding"], np.float64)
    assert isinstance(ratios.iloc[0]["operating_cycle"], np.float64)
    assert isinstance(ratios.iloc[0]["days_of_payables_outstanding"], np.float64)
    assert isinstance(ratios.iloc[0]["cash_conversion_cycle"], np.float64)
    assert isinstance(ratios.iloc[0]["gross_profit_margin"], np.float64)
    assert isinstance(ratios.iloc[0]["operating_profit_margin"], np.float64)
    assert isinstance(ratios.iloc[0]["pretax_profit_margin"], np.float64)
    assert isinstance(ratios.iloc[0]["net_profit_margin"], np.float64)
    assert isinstance(ratios.iloc[0]["effective_tax_rate"], np.float64)
    assert isinstance(ratios.iloc[0]["return_on_assets"], np.float64)
    assert isinstance(ratios.iloc[0]["return_on_equity"], np.float64)
    assert isinstance(ratios.iloc[0]["return_on_capital_employed"], np.float64)
    assert isinstance(ratios.iloc[0]["net_income_per_ebt"], np.float64)
    assert isinstance(ratios.iloc[0]["ebt_per_ebit"], np.float64)
    assert isinstance(ratios.iloc[0]["ebit_per_revenue"], np.float64)
    assert isinstance(ratios.iloc[0]["debt_ratio"], np.float64)
    assert isinstance(ratios.iloc[0]["debt_equity_ratio"], np.float64)
    assert isinstance(ratios.iloc[0]["longterm_debt_to_capitalization"], np.float64)
    assert isinstance(ratios.iloc[0]["total_debt_to_capitalization"], np.float64)
    assert isinstance(ratios.iloc[0]["interest_coverage"], np.float64)
    assert isinstance(ratios.iloc[0]["cash_flow_to_debt_ratio"], np.float64)
    assert isinstance(ratios.iloc[0]["company_equity_multiplier"], np.float64)
    assert isinstance(ratios.iloc[0]["receivables_turnover"], np.float64)
    assert isinstance(ratios.iloc[0]["payables_turnover"], np.float64)
    assert isinstance(ratios.iloc[0]["inventory_turnover"], np.float64)
    assert isinstance(ratios.iloc[0]["asset_turnover"], np.float64)
    assert isinstance(ratios.iloc[0]["fixed_asset_turnover"], np.float64)


def test_fmp_statement_analysis_ratios_invalid_symbol(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.ratios("invalid_symbol")


def test_fmp_statement_analysis_ratios_invalid_period(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.ratios("AAPL", period="invalid_period")


def test_fmp_statement_analysis_ratios_limit_check(statement_analysis):
    ratios = statement_analysis.ratios("AAPL", limit=10)
    assert len(ratios) == 10


def test_fmp_statement_analysis_ratios_ttm(statement_analysis):
    ratios_ttm = statement_analysis.ratios_ttm("AAPL")
    assert isinstance(ratios_ttm, Ratios)
    assert isinstance(ratios_ttm.dividend_yield_ttm, float)
    assert isinstance(ratios_ttm.dividend_yield_percentage_ttm, float)
    assert isinstance(ratios_ttm.pe_ratio_ttm, float)
    assert isinstance(ratios_ttm.peg_ratio_ttm, float)
    assert isinstance(ratios_ttm.payout_ratio_ttm, float)
    assert isinstance(ratios_ttm.current_ratio_ttm, float)
    assert isinstance(ratios_ttm.quick_ratio_ttm, float)
    assert isinstance(ratios_ttm.cash_ratio_ttm, float)
    assert isinstance(ratios_ttm.days_of_sales_outstanding_ttm, float)
    assert isinstance(ratios_ttm.days_of_inventory_outstanding_ttm, float)
    assert isinstance(ratios_ttm.operating_cycle_ttm, float)
    assert isinstance(ratios_ttm.days_of_payables_outstanding_ttm, float)
    assert isinstance(ratios_ttm.cash_conversion_cycle_ttm, float)
    assert isinstance(ratios_ttm.gross_profit_margin_ttm, float)
    assert isinstance(ratios_ttm.operating_profit_margin_ttm, float)
    assert isinstance(ratios_ttm.pretax_profit_margin_ttm, float)
    assert isinstance(ratios_ttm.net_profit_margin_ttm, float)
    assert isinstance(ratios_ttm.effective_tax_rate_ttm, float)
    assert isinstance(ratios_ttm.return_on_assets_ttm, float)
    assert isinstance(ratios_ttm.return_on_equity_ttm, float)
    assert isinstance(ratios_ttm.return_on_capital_employed_ttm, float)
    assert isinstance(ratios_ttm.net_income_per_ebt_ttm, float)
    assert isinstance(ratios_ttm.ebt_per_ebit_ttm, float)
    assert isinstance(ratios_ttm.ebit_per_revenue_ttm, float)
    assert isinstance(ratios_ttm.debt_ratio_ttm, float)
    assert isinstance(ratios_ttm.debt_equity_ratio_ttm, float)
    assert isinstance(ratios_ttm.longterm_debt_to_capitalization_ttm, float)
    assert isinstance(ratios_ttm.total_debt_to_capitalization_ttm, float)
    assert isinstance(ratios_ttm.interest_coverage_ttm, float)
    assert isinstance(ratios_ttm.cash_flow_to_debt_ratio_ttm, float)
    assert isinstance(ratios_ttm.company_equity_multiplier_ttm, float)
    assert isinstance(ratios_ttm.receivables_turnover_ttm, float)
    assert isinstance(ratios_ttm.payables_turnover_ttm, float)
    assert isinstance(ratios_ttm.inventory_turnover_ttm, float)
    assert isinstance(ratios_ttm.fixed_asset_turnover_ttm, float)
    assert isinstance(ratios_ttm.asset_turnover_ttm, float)
    assert isinstance(ratios_ttm.operating_cash_flow_per_share_ttm, float)
    assert isinstance(ratios_ttm.cash_per_share_ttm, float)
    assert isinstance(ratios_ttm.operating_cash_flow_sales_ratio_ttm, float)
    assert isinstance(ratios_ttm.free_cash_flow_operating_cash_flow_ratio_ttm, float)
    assert isinstance(ratios_ttm.cash_flow_coverage_ratios_ttm, float)
    assert isinstance(ratios_ttm.short_term_coverage_ratios_ttm, float)
    assert isinstance(ratios_ttm.capital_expenditure_coverage_ratio_ttm, float)
    assert isinstance(ratios_ttm.dividend_paid_and_capex_coverage_ratio_ttm, float)
    assert isinstance(ratios_ttm.price_book_value_ratio_ttm, float)
    assert isinstance(ratios_ttm.price_to_book_ratio_ttm, float)
    assert isinstance(ratios_ttm.price_to_sales_ratio_ttm, float)
    assert isinstance(ratios_ttm.price_to_free_cash_flows_ratio_ttm, float)
    assert isinstance(ratios_ttm.price_earnings_ratio_ttm, float)
    assert isinstance(ratios_ttm.price_to_operating_cash_flows_ratio_ttm, float)
    assert isinstance(ratios_ttm.price_cash_flow_ratio_ttm, float)
    assert isinstance(ratios_ttm.price_earnings_to_growth_ratio_ttm, float)
    assert isinstance(ratios_ttm.price_sales_ratio_ttm, float)
    assert isinstance(ratios_ttm.enterprise_value_multiple_ttm, float)
    assert isinstance(ratios_ttm.price_fair_value_ttm, float)
    assert isinstance(ratios_ttm.dividend_per_share_ttm, float)


def test_fmp_statement_analysis_ratios_ttm_invalid_symbol(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.ratios_ttm("INVALID_SYMBOL")


def test_fmp_statement_analysis_financial_score(statement_analysis):
    financial_score = statement_analysis.financial_score("AAPL")
    assert isinstance(financial_score, FinancialScore)
    assert isinstance(financial_score.symbol, str)
    assert isinstance(financial_score.altman_z_score, float)
    assert isinstance(financial_score.piotroski_score, int)
    assert isinstance(financial_score.working_capital, int)
    assert isinstance(financial_score.total_assets, int)
    assert isinstance(financial_score.retained_earnings, int)
    assert isinstance(financial_score.ebit, int)
    assert isinstance(financial_score.market_cap, int)
    assert isinstance(financial_score.total_liabilities, int)
    assert isinstance(financial_score.revenue, int)


def test_fmp_statement_analysis_financial_score_invalid_symbol(statement_analysis):
    with pytest.raises(Exception):
        statement_analysis.financial_score("INVALID_SYMBOL")


def test_fmp_statement_analysis_cashflow_growth(statement_analysis):
    cashflow_growth = statement_analysis.cashflow_growth("AAPL")
    assert isinstance(cashflow_growth, pd.DataFrame)
    assert isinstance(cashflow_growth.iloc[0]["symbol"], str)
    assert isinstance(cashflow_growth.iloc[0]["date"], pd.Timestamp)
    assert isinstance(cashflow_growth.iloc[0]["period"], str)
    assert isinstance(cashflow_growth.iloc[0]["calendar_year"], np.int64)
    assert isinstance(cashflow_growth.iloc[0]["growth_net_income"], np.float64)
    assert isinstance(
        cashflow_growth.iloc[0]["growth_depreciation_and_amortization"], np.float64
    )
    assert isinstance(
        cashflow_growth.iloc[0]["growth_stock_based_compensation"], np.float64
    )
    assert isinstance(
        cashflow_growth.iloc[0]["growth_change_in_working_capital"], np.float64
    )
    assert isinstance(
        cashflow_growth.iloc[0]["growth_accounts_receivables"], np.float64
    )
    assert isinstance(cashflow_growth.iloc[0]["growth_inventory"], np.float64)
    assert isinstance(cashflow_growth.iloc[0]["growth_accounts_payables"], np.float64)
    assert isinstance(
        cashflow_growth.iloc[0]["growth_other_working_capital"], np.float64
    )
    assert isinstance(
        cashflow_growth.iloc[0]["growth_other_non_cash_items"], np.float64
    )
    assert isinstance(
        cashflow_growth.iloc[0]["growth_net_cash_provided_by_operating_activities"],
        np.float64,
    )
    assert isinstance(
        cashflow_growth.iloc[0]["growth_investments_in_property_plant_and_equipment"],
        np.float64,
    )
    assert isinstance(cashflow_growth.iloc[0]["growth_acquisitions_net"], np.float64)
    assert isinstance(
        cashflow_growth.iloc[0]["growth_purchases_of_investments"], np.float64
    )
    assert isinstance(
        cashflow_growth.iloc[0]["growth_sales_maturities_of_investments"], np.float64
    )
    assert isinstance(
        cashflow_growth.iloc[0]["growth_net_cash_used_for_investing_activities"],
        np.float64,
    )
    assert isinstance(cashflow_growth.iloc[0]["growth_debt_repayment"], np.float64)
    assert isinstance(cashflow_growth.iloc[0]["growth_common_stock_issued"], np.float64)
    assert isinstance(
        cashflow_growth.iloc[0]["growth_common_stock_repurchased"], np.float64
    )
    assert isinstance(cashflow_growth.iloc[0]["growth_dividends_paid"], np.float64)
    assert isinstance(
        cashflow_growth.iloc[0][
            "growth_net_cash_used_provided_by_financing_activities"
        ],
        np.float64,
    )
    assert isinstance(
        cashflow_growth.iloc[0]["growth_effect_of_forex_changes_on_cash"], np.float64
    )
    assert isinstance(cashflow_growth.iloc[0]["growth_net_change_in_cash"], np.float64)
    assert isinstance(
        cashflow_growth.iloc[0]["growth_cash_at_end_of_period"], np.float64
    )
    assert isinstance(
        cashflow_growth.iloc[0]["growth_cash_at_beginning_of_period"], np.float64
    )
    assert isinstance(cashflow_growth.iloc[0]["growth_operating_cash_flow"], np.float64)
    assert isinstance(cashflow_growth.iloc[0]["growth_capital_expenditure"], np.float64)
    assert isinstance(cashflow_growth.iloc[0]["growth_free_cash_flow"], np.float64)
    assert isinstance(
        cashflow_growth.iloc[0]["growth_other_investing_activites"], np.float64
    )
    assert isinstance(
        cashflow_growth.iloc[0]["growth_other_financing_activites"], np.float64
    )


def test_fmp_statement_analysis_cashflow_growth_invaild_symbol(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.cashflow_growth("INVALID_SYMBOL")


def test_fmp_statement_analysis_cashflow_growth_invaild_period(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.cashflow_growth("AAPL", period="INVALID_PERIOD")


def test_fmp_statement_analysis_cashflow_growth_limit_check(statement_analysis):
    cashflow_growth = statement_analysis.cashflow_growth("AAPL", limit=10)
    assert len(cashflow_growth) == 10


def test_fmp_statement_analysis_income_growth(statement_analysis):
    income_growth = statement_analysis.income_growth("AAPL")
    assert isinstance(income_growth, pd.DataFrame)
    assert isinstance(income_growth.iloc[0]["symbol"], str)
    assert isinstance(income_growth.iloc[0]["date"], pd.Timestamp)
    assert isinstance(income_growth.iloc[0]["period"], str)
    assert isinstance(income_growth.iloc[0]["growth_revenue"], np.float64)
    assert isinstance(income_growth.iloc[0]["growth_cost_of_revenue"], np.float64)
    assert isinstance(income_growth.iloc[0]["growth_gross_profit"], np.float64)
    assert isinstance(income_growth.iloc[0]["growth_gross_profit_ratio"], np.float64)
    assert isinstance(
        income_growth.iloc[0]["growth_research_and_development_expenses"], np.float64
    )
    assert isinstance(
        income_growth.iloc[0]["growth_general_and_administrative_expenses"], np.float64
    )
    assert isinstance(
        income_growth.iloc[0]["growth_selling_and_marketing_expenses"], np.float64
    )
    assert isinstance(income_growth.iloc[0]["growth_other_expenses"], np.float64)
    assert isinstance(income_growth.iloc[0]["growth_operating_expenses"], np.float64)
    assert isinstance(income_growth.iloc[0]["growth_cost_and_expenses"], np.float64)
    assert isinstance(income_growth.iloc[0]["growth_interest_expense"], np.float64)
    assert isinstance(
        income_growth.iloc[0]["growth_depreciation_and_amortization"], np.float64
    )
    assert isinstance(income_growth.iloc[0]["growth_ebitda"], np.float64)
    assert isinstance(income_growth.iloc[0]["growth_ebitda_ratio"], np.float64)
    assert isinstance(income_growth.iloc[0]["growth_operating_income"], np.float64)
    assert isinstance(
        income_growth.iloc[0]["growth_operating_income_ratio"], np.float64
    )
    assert isinstance(
        income_growth.iloc[0]["growth_total_other_income_expenses_net"], np.float64
    )
    assert isinstance(income_growth.iloc[0]["growth_income_before_tax"], np.float64)
    assert isinstance(
        income_growth.iloc[0]["growth_income_before_tax_ratio"], np.float64
    )
    assert isinstance(income_growth.iloc[0]["growth_income_tax_expense"], np.float64)
    assert isinstance(income_growth.iloc[0]["growth_net_income"], np.float64)
    assert isinstance(income_growth.iloc[0]["growth_net_income_ratio"], np.float64)
    assert isinstance(income_growth.iloc[0]["growth_eps"], np.float64)
    assert isinstance(income_growth.iloc[0]["growth_eps_diluted"], np.float64)
    assert isinstance(
        income_growth.iloc[0]["growth_weighted_average_shs_out"], np.float64
    )
    assert isinstance(
        income_growth.iloc[0]["growth_weighted_average_shs_out_dil"], np.float64
    )


def test_fmp_statement_analysis_income_growth_invaild_symbol(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.income_growth("INVALID_SYMBOL")


def test_fmp_statement_analysis_income_growth_invalid_period(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.income_growth("AAPL", period="INVALID_PERIOD")


def test_fmp_statement_analysis_income_growth_limit_check(statement_analysis):
    income_growth = statement_analysis.income_growth("AAPL", limit=10)
    assert len(income_growth) == 10


def test_fmp_statement_analysis_enterprise_values(statement_analysis):
    enterprise_values = statement_analysis.enterprise_values("AAPL")
    assert isinstance(enterprise_values, pd.DataFrame)
    assert isinstance(enterprise_values.iloc[0]["symbol"], str)
    assert isinstance(enterprise_values.iloc[0]["date"], pd.Timestamp)
    assert isinstance(enterprise_values.iloc[0]["stock_price"], np.float64)
    assert isinstance(enterprise_values.iloc[0]["number_of_shares"], np.int64)
    assert isinstance(enterprise_values.iloc[0]["market_capitalization"], np.int64)
    assert isinstance(
        enterprise_values.iloc[0]["minus_cash_and_cash_equivalents"], np.int64
    )
    assert isinstance(enterprise_values.iloc[0]["add_total_debt"], np.int64)
    assert isinstance(enterprise_values.iloc[0]["enterprise_value"], np.int64)


def test_fmp_statement_analysis_enterprise_values_invalid_symbol(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.enterprise_values("INVALID_SYMBOL")


def test_fmp_statement_analysis_owner_earnings(statement_analysis):
    owner_earnings = statement_analysis.owner_earnings("AAPL")
    assert isinstance(owner_earnings, pd.DataFrame)
    assert isinstance(owner_earnings.iloc[0]["symbol"], str)
    assert isinstance(owner_earnings.iloc[0]["date"], pd.Timestamp)
    assert isinstance(owner_earnings.iloc[0]["average_ppe"], np.float64)
    assert isinstance(owner_earnings.iloc[0]["maintenance_capex"], np.int64)
    assert isinstance(owner_earnings.iloc[0]["owners_earnings"], np.int64)
    assert isinstance(owner_earnings.iloc[0]["growth_capex"], np.int64)
    assert isinstance(owner_earnings.iloc[0]["owners_earnings_per_share"], np.float64)


def test_fmp_statement_analysis_owner_earnings_invalid_symbol(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.owner_earnings("INVALID_SYMBOL")


def test_fmp_statement_analysis_financial_growth(statement_analysis):
    financial_growth = statement_analysis.financial_growth("AAPL")
    assert isinstance(financial_growth, pd.DataFrame)
    assert isinstance(financial_growth.iloc[0]["symbol"], str)
    assert isinstance(financial_growth.iloc[0]["date"], pd.Timestamp)
    assert isinstance(financial_growth.iloc[0]["calendar_year"], np.int64)
    assert isinstance(financial_growth.iloc[0]["period"], str)
    assert isinstance(financial_growth.iloc[0]["revenue_growth"], np.float64)
    assert isinstance(financial_growth.iloc[0]["gross_profit_growth"], np.float64)
    assert isinstance(financial_growth.iloc[0]["ebit_growth"], np.float64)
    assert isinstance(financial_growth.iloc[0]["operating_income_growth"], np.float64)
    assert isinstance(financial_growth.iloc[0]["net_income_growth"], np.float64)
    assert isinstance(financial_growth.iloc[0]["eps_growth"], np.float64)
    assert isinstance(financial_growth.iloc[0]["eps_diluted_growth"], np.float64)
    assert isinstance(
        financial_growth.iloc[0]["weighted_average_shares_growth"], np.float64
    )
    assert isinstance(
        financial_growth.iloc[0]["weighted_average_shares_diluted_growth"], np.float64
    )
    assert isinstance(
        financial_growth.iloc[0]["dividends_per_share_growth"], np.float64
    )
    assert isinstance(
        financial_growth.iloc[0]["operating_cash_flow_growth"], np.float64
    )
    assert isinstance(financial_growth.iloc[0]["free_cash_flow_growth"], np.float64)
    assert isinstance(
        financial_growth.iloc[0]["ten_y_revenue_growth_per_share"], np.float64
    )
    assert isinstance(
        financial_growth.iloc[0]["five_y_revenue_growth_per_share"], np.float64
    )
    assert isinstance(
        financial_growth.iloc[0]["three_y_revenue_growth_per_share"], np.float64
    )
    assert isinstance(
        financial_growth.iloc[0]["ten_y_operating_cf_growth_per_share"], np.float64
    )
    assert isinstance(
        financial_growth.iloc[0]["five_y_operating_cf_growth_per_share"], np.float64
    )
    assert isinstance(
        financial_growth.iloc[0]["three_y_operating_cf_growth_per_share"], np.float64
    )
    assert isinstance(
        financial_growth.iloc[0]["ten_y_net_income_growth_per_share"], np.float64
    )
    assert isinstance(
        financial_growth.iloc[0]["five_y_net_income_growth_per_share"], np.float64
    )
    assert isinstance(
        financial_growth.iloc[0]["three_y_net_income_growth_per_share"], np.float64
    )
    assert isinstance(
        financial_growth.iloc[0]["ten_y_shareholders_equity_growth_per_share"],
        np.float64,
    )
    assert isinstance(
        financial_growth.iloc[0]["five_y_shareholders_equity_growth_per_share"],
        np.float64,
    )
    assert isinstance(
        financial_growth.iloc[0]["three_y_shareholders_equity_growth_per_share"],
        np.float64,
    )
    assert isinstance(
        financial_growth.iloc[0]["ten_y_dividend_per_share_growth_per_share"],
        np.float64,
    )
    assert isinstance(
        financial_growth.iloc[0]["five_y_dividend_per_share_growth_per_share"],
        np.float64,
    )
    assert isinstance(
        financial_growth.iloc[0]["three_y_dividend_per_share_growth_per_share"],
        np.float64,
    )
    assert isinstance(financial_growth.iloc[0]["receivables_growth"], np.float64)
    assert isinstance(financial_growth.iloc[0]["inventory_growth"], np.float64)
    assert isinstance(financial_growth.iloc[0]["asset_growth"], np.float64)
    assert isinstance(
        financial_growth.iloc[0]["book_value_per_share_growth"], np.float64
    )
    assert isinstance(financial_growth.iloc[0]["debt_growth"], np.float64)
    assert isinstance(financial_growth.iloc[0]["rdexpense_growth"], np.float64)
    assert isinstance(financial_growth.iloc[0]["sgaexpenses_growth"], np.float64)


def test_fmp_statement_analysis_financial_growth_invalid_symbol(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.financial_growth("INVALID_SYMBOL")


def test_fmp_statement_analysis_financial_growth_invalid_period(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.financial_growth("AAPL", period="INVALID_PERIOD")


def test_fmp_statement_analysis_financial_growth_limit_check(statement_analysis):
    financial_growth = statement_analysis.financial_growth("AAPL", limit=10)
    assert len(financial_growth) == 10


def test_fmp_statement_analysis_balance_sheet_growth(statement_analysis):
    balance_sheet_growth = statement_analysis.balance_sheet_growth("AAPL")
    assert isinstance(balance_sheet_growth, pd.DataFrame)
    assert isinstance(balance_sheet_growth.iloc[0]["symbol"], str)
    assert isinstance(balance_sheet_growth.iloc[0]["date"], pd.Timestamp)
    assert isinstance(balance_sheet_growth.iloc[0]["calendar_year"], np.int64)
    assert isinstance(balance_sheet_growth.iloc[0]["period"], str)
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_cash_and_cash_equivalents"], np.float64
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_short_term_investments"], np.float64
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_cash_and_short_term_investments"],
        np.float64,
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_net_receivables"], np.float64
    )
    assert isinstance(balance_sheet_growth.iloc[0]["growth_inventory"], np.float64)
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_total_current_assets"], np.float64
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_property_plant_equipment_net"], np.float64
    )
    assert isinstance(balance_sheet_growth.iloc[0]["growth_goodwill"], np.float64)
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_intangible_assets"], np.float64
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_goodwill_and_intangible_assets"],
        np.float64,
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_long_term_investments"], np.float64
    )
    assert isinstance(balance_sheet_growth.iloc[0]["growth_tax_assets"], np.float64)
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_other_current_assets"], np.float64
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_total_non_current_assets"], np.float64
    )
    assert isinstance(balance_sheet_growth.iloc[0]["growth_other_assets"], np.float64)
    assert isinstance(balance_sheet_growth.iloc[0]["growth_total_assets"], np.float64)
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_short_term_debt"], np.float64
    )
    assert isinstance(balance_sheet_growth.iloc[0]["growth_tax_payables"], np.float64)
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_deferred_revenue"], np.float64
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_other_current_liabilities"], np.float64
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_total_current_liabilities"], np.float64
    )
    assert isinstance(balance_sheet_growth.iloc[0]["growth_long_term_debt"], np.float64)
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_deferred_revenue_non_current"], np.float64
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_deferrred_tax_liabilities_non_current"],
        np.float64,
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_other_non_current_liabilities"], np.float64
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_total_non_current_liabilities"], np.float64
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_total_liabilities"], np.float64
    )
    assert isinstance(balance_sheet_growth.iloc[0]["growth_common_stock"], np.float64)
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_retained_earnings"], np.float64
    )
    assert isinstance(
        balance_sheet_growth.iloc[0][
            "growth_accumulated_other_comprehensive_income_loss"
        ],
        np.float64,
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_othertotal_stockholders_equity"],
        np.float64,
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_total_stockholders_equity"], np.float64
    )
    assert isinstance(
        balance_sheet_growth.iloc[0][
            "growth_total_liabilities_and_stockholders_equity"
        ],
        np.float64,
    )
    assert isinstance(
        balance_sheet_growth.iloc[0]["growth_total_investments"], np.float64
    )
    assert isinstance(balance_sheet_growth.iloc[0]["growth_total_debt"], np.float64)
    assert isinstance(balance_sheet_growth.iloc[0]["growth_net_debt"], np.float64)


def test_fmp_statement_analysis_balance_sheet_growth_invalid_symbol(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.balance_sheet_growth("INVALID_SYMBOL")


def test_fmp_statement_analysis_balance_sheet_growth_invalid_period(statement_analysis):
    with pytest.raises(ValueError):
        statement_analysis.balance_sheet_growth("AAPL", period="INVALID_PERIOD")


def test_fmp_statement_analysis_balance_sheet_growth_limit_check(statement_analysis):
    balance_sheet_growth = statement_analysis.balance_sheet_growth("AAPL", limit=10)
    assert len(balance_sheet_growth) == 10
