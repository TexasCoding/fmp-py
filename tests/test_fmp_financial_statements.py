import numpy as np
import pandas as pd
import pytest

from fmp_py.fmp_financial_statements import FmpFinancialStatements


@pytest.fixture
def fmp_financial_statements():
    return FmpFinancialStatements()


def test_fmp_financial_statements(fmp_financial_statements):
    assert isinstance(fmp_financial_statements, FmpFinancialStatements)


def test_fmp_financial_statements_cashflow_statements(fmp_financial_statements):
    data = fmp_financial_statements.cashflow_statements("AAPL", "annual")
    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert "date" in data.columns
    assert isinstance(data["date"][0], pd.Timestamp)
    assert isinstance(data["symbol"][0], str)
    assert isinstance(data["reported_currency"][0], str)
    assert isinstance(data["cik"][0], str)
    assert isinstance(data["filling_date"][0], pd.Timestamp)
    assert isinstance(data["accepted_date"][0], pd.Timestamp)
    assert isinstance(data["calendar_year"][0], np.int64)
    assert isinstance(data["period"][0], str)
    assert isinstance(data["net_income"][0], np.int64)

    assert isinstance(data["depreciation_and_amortization"][0], np.int64)
    assert isinstance(data["deferred_income_tax"][0], np.int64)
    assert isinstance(data["stock_based_compensation"][0], np.int64)
    assert isinstance(data["change_in_working_capital"][0], np.int64)
    assert isinstance(data["accounts_receivables"][0], np.int64)
    assert isinstance(data["inventory"][0], np.int64)
    assert isinstance(data["accounts_payables"][0], np.int64)
    assert isinstance(data["other_working_capital"][0], np.int64)
    assert isinstance(data["other_non_cash_items"][0], np.int64)
    assert isinstance(data["net_cash_provided_by_operating_activities"][0], np.int64)

    assert isinstance(data["investments_in_property_plant_and_equipment"][0], np.int64)
    assert isinstance(data["acquisitions_net"][0], np.int64)
    assert isinstance(data["purchases_of_investments"][0], np.int64)
    assert isinstance(data["sales_maturities_of_investments"][0], np.int64)
    assert isinstance(data["other_investing_activites"][0], np.int64)
    assert isinstance(data["net_cash_used_for_investing_activites"][0], np.int64)
    assert isinstance(data["debt_repayment"][0], np.int64)
    assert isinstance(data["common_stock_issued"][0], np.int64)
    assert isinstance(data["common_stock_repurchased"][0], np.int64)
    assert isinstance(data["dividends_paid"][0], np.int64)

    assert isinstance(data["other_financing_activites"][0], np.int64)
    assert isinstance(
        data["net_cash_used_provided_by_financing_activities"][0], np.int64
    )
    assert isinstance(data["effect_of_forex_changes_on_cash"][0], np.int64)
    assert isinstance(data["net_change_in_cash"][0], np.int64)
    assert isinstance(data["cash_at_end_of_period"][0], np.int64)
    assert isinstance(data["cash_at_beginning_of_period"][0], np.int64)
    assert isinstance(data["operating_cash_flow"][0], np.int64)
    assert isinstance(data["capital_expenditure"][0], np.int64)
    assert isinstance(data["free_cash_flow"][0], np.int64)
    assert isinstance(data["link"][0], str)
    assert isinstance(data["final_link"][0], str)


def test_fmp_financial_statements_cashflow_statements_invalid_period(
    fmp_financial_statements,
):
    with pytest.raises(ValueError):
        fmp_financial_statements.cashflow_statements("AAPL", "invalid_period")


def test_fmp_financial_statements_cashflow_statements_invalid_symbol(
    fmp_financial_statements,
):
    with pytest.raises(ValueError):
        fmp_financial_statements.cashflow_statements("invalid_symbol", "annual")


def test_fmp_financial_statements_cashflow_statements_check_limit(
    fmp_financial_statements,
):
    cashflow_statement = fmp_financial_statements.cashflow_statements(
        "AAPL", "annual", limit=1
    )
    assert len(cashflow_statement) == 1


def test_fmp_financial_statements_balance_sheet_statements(fmp_financial_statements):
    data = fmp_financial_statements.balance_sheet_statements("AAPL", "annual")
    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert "date" in data.columns
    assert isinstance(data["date"][0], pd.Timestamp)
    assert isinstance(data["symbol"][0], str)
    assert isinstance(data["reported_currency"][0], str)
    assert isinstance(data["cik"][0], str)
    assert isinstance(data["filling_date"][0], pd.Timestamp)
    assert isinstance(data["accepted_date"][0], pd.Timestamp)
    assert isinstance(data["calendar_year"][0], np.int64)
    assert isinstance(data["period"][0], str)
    assert isinstance(data["cash_and_short_term_investments"][0], np.int64)

    assert isinstance(data["cash_and_short_term_investments"][0], np.int64)
    assert isinstance(data["net_receivables"][0], np.int64)
    assert isinstance(data["inventory"][0], np.int64)
    assert isinstance(data["other_current_assets"][0], np.int64)
    assert isinstance(data["total_current_assets"][0], np.int64)
    assert isinstance(data["property_plant_equipment_net"][0], np.int64)
    assert isinstance(data["goodwill"][0], np.int64)
    assert isinstance(data["intangible_assets"][0], np.int64)
    assert isinstance(data["goodwill_and_intangible_assets"][0], np.int64)
    assert isinstance(data["long_term_investments"][0], np.int64)

    assert isinstance(data["tax_assets"][0], np.int64)
    assert isinstance(data["other_non_current_assets"][0], np.int64)
    assert isinstance(data["total_non_current_assets"][0], np.int64)
    assert isinstance(data["other_assets"][0], np.int64)
    assert isinstance(data["total_assets"][0], np.int64)
    assert isinstance(data["account_payables"][0], np.int64)
    assert isinstance(data["short_term_debt"][0], np.int64)
    assert isinstance(data["tax_payables"][0], np.int64)
    assert isinstance(data["deferred_revenue"][0], np.int64)
    assert isinstance(data["other_current_liabilities"][0], np.int64)

    assert isinstance(data["total_current_liabilities"][0], np.int64)
    assert isinstance(data["long_term_debt"][0], np.int64)
    assert isinstance(data["deferred_revenue_non_current"][0], np.int64)
    assert isinstance(data["deferred_tax_liabilities_non_current"][0], np.int64)
    assert isinstance(data["other_non_current_liabilities"][0], np.int64)
    assert isinstance(data["total_non_current_liabilities"][0], np.int64)
    assert isinstance(data["other_liabilities"][0], np.int64)
    assert isinstance(data["capital_lease_obligations"][0], np.int64)
    assert isinstance(data["total_liabilities"][0], np.int64)
    assert isinstance(data["common_stock"][0], np.int64)

    assert isinstance(data["retained_earnings"][0], np.int64)
    assert isinstance(data["accumulated_other_comprehensive_income_loss"][0], np.int64)
    assert isinstance(data["total_stockholders_equity"][0], np.int64)
    assert isinstance(data["total_equity"][0], np.int64)
    assert isinstance(data["total_liabilities_and_stockholders_equity"][0], np.int64)
    assert isinstance(data["minority_interest"][0], np.int64)
    assert isinstance(data["total_liabilities_and_total_equity"][0], np.int64)
    assert isinstance(data["total_investments"][0], np.int64)
    assert isinstance(data["total_debt"][0], np.int64)
    assert isinstance(data["net_debt"][0], np.int64)

    assert isinstance(data["link"][0], str)
    assert isinstance(data["final_link"][0], str)


def test_fmp_financial_statements_balance_sheet_statements_invalid_symbol(
    fmp_financial_statements,
):
    with pytest.raises(ValueError):
        fmp_financial_statements.balance_sheet_statements("INVALID", "annual")


def test_fmp_financial_statements_balance_sheet_statements_invalid_period(
    fmp_financial_statements,
):
    with pytest.raises(ValueError):
        fmp_financial_statements.balance_sheet_statements("AAPL", "invalid")


def test_fmp_financial_statements_balance_sheet_limit_check(fmp_financial_statements):
    balance_sheets = fmp_financial_statements.balance_sheet_statements(
        "AAPL", "annual", limit=1
    )
    assert len(balance_sheets) == 1


def test_fmp_financial_statements_income_statements(fmp_financial_statements):
    data = fmp_financial_statements.income_statements("AAPL", "annual")
    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert "date" in data.columns
    assert isinstance(data["date"][0], pd.Timestamp)
    assert isinstance(data["symbol"][0], str)
    assert isinstance(data["reported_currency"][0], str)
    assert isinstance(data["cik"][0], str)
    assert isinstance(data["filling_date"][0], pd.Timestamp)
    assert isinstance(data["accepted_date"][0], pd.Timestamp)
    assert isinstance(data["calendar_year"][0], np.int64)
    assert isinstance(data["period"][0], str)
    assert isinstance(data["revenue"][0], np.int64)
    assert isinstance(data["cost_of_revenue"][0], np.int64)
    assert isinstance(data["gross_profit"][0], np.int64)
    assert isinstance(data["gross_profit_ratio"][0], np.float64)
    assert isinstance(data["research_and_development_expenses"][0], np.int64)
    assert isinstance(data["general_and_administrative_expenses"][0], np.int64)
    assert isinstance(data["selling_and_marketing_expenses"][0], np.int64)
    assert isinstance(data["selling_general_and_administrative_expenses"][0], np.int64)
    assert isinstance(data["other_expenses"][0], np.int64)
    assert isinstance(data["operating_expenses"][0], np.int64)
    assert isinstance(data["cost_and_expenses"][0], np.int64)
    assert isinstance(data["interest_expense"][0], np.int64)
    assert isinstance(data["interest_income"][0], np.int64)
    assert isinstance(data["depreciation_and_amortization"][0], np.int64)
    assert isinstance(data["ebitda"][0], np.int64)
    assert isinstance(data["ebitda_ratio"][0], np.float64)
    assert isinstance(data["operating_income"][0], np.int64)
    assert isinstance(data["operating_income_ratio"][0], np.float64)
    assert isinstance(data["total_other_income_expenses_net"][0], np.int64)
    assert isinstance(data["income_before_tax"][0], np.int64)
    assert isinstance(data["income_before_tax_ratio"][0], np.float64)
    assert isinstance(data["income_tax_expense"][0], np.int64)
    assert isinstance(data["net_income"][0], np.int64)
    assert isinstance(data["net_income_ratio"][0], np.float64)
    assert isinstance(data["eps"][0], np.float64)
    assert isinstance(data["epsdiluted"][0], np.float64)
    assert isinstance(data["weighted_average_shs_out"][0], np.int64)
    assert isinstance(data["weighted_average_shs_out_dil"][0], np.int64)
    assert isinstance(data["link"][0], str)
    assert isinstance(data["final_link"][0], str)


def test_fmp_financial_statements_income_statements_invalid_symbol(
    fmp_financial_statements,
):
    with pytest.raises(ValueError):
        fmp_financial_statements.income_statements("INVALID_SYMBOL", "annual")


def test_fmp_financial_statements_income_statements_invalid_period(
    fmp_financial_statements,
):
    with pytest.raises(ValueError):
        fmp_financial_statements.income_statements("AAPL", "invalid_period")


def test_fmp_financial_statements_income_statements_check_limit(
    fmp_financial_statements,
):
    statements = fmp_financial_statements.income_statements("AAPL", "annual", limit=1)
    assert len(statements) == 1
