import numpy as np
import pandas as pd
import pytest

from fmp_py.fmp_financial_statements import FmpFinancialStatements


@pytest.fixture
def fmp_financial_statements():
    return FmpFinancialStatements()


def test_fmp_financial_statements(fmp_financial_statements):
    assert isinstance(fmp_financial_statements, FmpFinancialStatements)


def test_fmp_financial_statements_cashflow_statements_as_reported(
    fmp_financial_statements,
):
    data = fmp_financial_statements.cashflow_statements_as_reported("AAPL", "annual")
    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert "date" in data.columns
    assert isinstance(data["date"][0], pd.Timestamp)
    assert isinstance(data["symbol"][0], str)
    assert isinstance(data["period"][0], str)
    assert isinstance(data["net_income_loss"][0], np.int64)

    assert isinstance(
        data["cash_cash_equivalents_restricted_cash_and_restricted_cash_equivalents"][
            0
        ],
        np.int64,
    )
    assert isinstance(data["depreciation_depletion_and_amortization"][0], np.int64)
    assert isinstance(data["share_based_compensation"][0], np.int64)
    assert isinstance(data["other_non_cash_income_expense"][0], np.int64)
    assert isinstance(data["increase_decrease_in_accounts_receivable"][0], np.int64)
    assert isinstance(data["increase_decrease_in_other_receivables"][0], np.int64)
    assert isinstance(data["increase_decrease_in_inventories"][0], np.int64)
    assert isinstance(data["increase_decrease_in_other_operating_assets"][0], np.int64)
    assert isinstance(data["increase_decrease_in_accounts_payable"][0], np.int64)
    assert isinstance(
        data["increase_decrease_in_other_operating_liabilities"][0], np.int64
    )

    assert isinstance(
        data["net_cash_provided_by_used_in_operating_activities"][0], np.int64
    )
    assert isinstance(
        data["payments_to_acquire_available_for_sale_securities_debt"][0], np.int64
    )
    assert isinstance(
        data[
            "proceeds_from_maturities_prepayments_and_calls_of_available_for_sale_securities"
        ][0],
        np.int64,
    )
    assert isinstance(
        data["proceeds_from_sale_of_available_for_sale_securities_debt"][0], np.int64
    )
    assert isinstance(
        data["payments_to_acquire_property_plant_and_equipment"][0], np.int64
    )
    assert isinstance(
        data["payments_for_proceeds_from_other_investing_activities"][0], np.int64
    )
    assert isinstance(
        data["net_cash_provided_by_used_in_investing_activities"][0], np.int64
    )
    assert isinstance(
        data["payments_related_to_tax_withholding_for_share_based_compensation"][0],
        np.int64,
    )
    assert isinstance(data["payments_of_dividends"][0], np.int64)
    assert isinstance(data["payments_for_repurchase_of_common_stock"][0], np.int64)

    assert isinstance(data["proceeds_from_issuance_of_long_term_debt"][0], np.int64)
    assert isinstance(data["repayments_of_long_term_debt"][0], np.int64)
    assert isinstance(data["proceeds_from_repayments_of_commercial_paper"][0], np.int64)
    assert isinstance(
        data["proceeds_from_payments_for_other_financing_activities"][0], np.int64
    )
    assert isinstance(
        data["net_cash_provided_by_used_in_financing_activities"][0], np.int64
    )
    assert isinstance(data["proceeds_from_issuance_of_common_stock"][0], np.int64)
    assert isinstance(data["payments_to_acquire_other_investments"][0], np.int64)
    assert isinstance(
        data[
            "cash_cash_equivalents_restricted_cash_and_restricted_cash_equivalents_period_increase_decrease_including_exchange_rate_effect"
        ][0],
        np.int64,
    )
    assert isinstance(data["income_taxes_paid_net"][0], np.int64)
    assert isinstance(data["interest_paid_net"][0], np.int64)


def test_fmp_financial_statements_cashflow_statements_as_reported_invalid_period(
    fmp_financial_statements,
):
    with pytest.raises(ValueError):
        fmp_financial_statements.cashflow_statements_as_reported("AAPL", "invalid")


def test_fmp_financial_statements_cashflow_statements_as_reported_with_limit(
    fmp_financial_statements,
):
    data = fmp_financial_statements.cashflow_statements_as_reported(
        "AAPL", "annual", limit=4
    )
    assert isinstance(data, pd.DataFrame)
    assert len(data) == 4


def test_fmp_financial_statements_cashflow_statements_as_reported_invalid_symbol(
    fmp_financial_statements,
):
    with pytest.raises(ValueError):
        fmp_financial_statements.cashflow_statements_as_reported("INVALID", "annual")


def test_fmp_financial_statements_balance_sheet_statements_as_reported(
    fmp_financial_statements,
):
    data = fmp_financial_statements.balance_sheet_statements_as_reported(
        "AAPL", "annual"
    )
    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert "date" in data.columns
    assert isinstance(data["date"][0], pd.Timestamp)
    assert isinstance(data["symbol"][0], str)
    assert isinstance(data["period"][0], str)
    assert isinstance(data["cash_and_cash_equivalents_at_carrying_value"][0], np.int64)

    assert isinstance(data["marketable_securities_current"][0], np.int64)
    assert isinstance(data["accounts_receivable_net_current"][0], np.int64)
    assert isinstance(data["non_trade_receivables_current"][0], np.int64)
    assert isinstance(data["inventory_net"][0], np.int64)
    assert isinstance(data["other_assets_current"][0], np.int64)
    assert isinstance(data["assets_current"][0], np.int64)
    assert isinstance(data["marketable_securities_non_current"][0], np.int64)
    assert isinstance(data["property_plant_and_equipment_net"][0], np.int64)
    assert isinstance(data["other_assets_non_current"][0], np.int64)
    assert isinstance(data["assets_non_current"][0], np.int64)

    assert isinstance(data["assets"][0], np.int64)
    assert isinstance(data["accounts_payable_current"][0], np.int64)
    assert isinstance(data["other_liabilities_current"][0], np.int64)
    assert isinstance(data["contract_with_customer_liability_current"][0], np.int64)
    assert isinstance(data["long_term_debt_current"][0], np.int64)
    assert isinstance(data["liabilities_current"][0], np.int64)
    assert isinstance(data["long_term_debt_non_current"][0], np.int64)
    assert isinstance(data["other_liabilities_non_current"][0], np.int64)
    assert isinstance(data["liabilities_non_current"][0], np.int64)
    assert isinstance(data["liabilities"][0], np.int64)

    assert isinstance(data["common_stock_shares_outstanding"][0], np.int64)
    assert isinstance(data["common_stock_shares_issued"][0], np.int64)
    assert isinstance(
        data["common_stocks_including_additional_paid_in_capital"][0], np.int64
    )
    assert isinstance(data["retained_earnings_accumulated_deficit"][0], np.int64)
    assert isinstance(
        data["accumulated_other_comprehensive_income_loss_net_of_tax"][0], np.int64
    )
    assert isinstance(data["stockholders_equity"][0], np.int64)
    assert isinstance(data["liabilities_and_stockholders_equity"][0], np.int64)
    assert isinstance(data["common_stock_par_or_stated_value_per_share"][0], np.float64)
    assert isinstance(data["common_stock_shares_authorized"][0], np.int64)


def test_fmp_financial_statements_balance_sheet_statements_as_reported_with_limit(
    fmp_financial_statements,
):
    data = fmp_financial_statements.balance_sheet_statements_as_reported(
        "AAPL", "annual", limit=1
    )
    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert len(data) == 1


def test_fmp_financial_statements_balance_sheet_statements_as_reported_invalid_period(
    fmp_financial_statements,
):
    with pytest.raises(ValueError):
        fmp_financial_statements.balance_sheet_statements_as_reported("AAPL", "invalid")


def test_fmp_financial_statements_balance_sheet_statements_as_reported_invalid_symbol(
    fmp_financial_statements,
):
    with pytest.raises(ValueError):
        fmp_financial_statements.balance_sheet_statements_as_reported(
            "INVALID_SYMBOL", "annual"
        )


def test_fmp_financial_statements_income_statements_as_reported(
    fmp_financial_statements,
):
    data = fmp_financial_statements.income_statements_as_reported("AAPL", "annual")
    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert "date" in data.columns
    assert isinstance(data["date"][0], pd.Timestamp)
    assert isinstance(data["symbol"][0], str)
    assert isinstance(data["period"][0], str)
    assert isinstance(
        data["revenue_from_contract_with_customer_excluding_assessed_tax"][0], np.int64
    )

    assert isinstance(data["cost_of_goods_and_services_sold"][0], np.int64)
    assert isinstance(data["gross_profit"][0], np.int64)
    assert isinstance(data["research_and_development_expense"][0], np.int64)
    assert isinstance(data["selling_general_and_administrative_expense"][0], np.int64)
    assert isinstance(data["operating_expenses"][0], np.int64)
    assert isinstance(data["operating_income_loss"][0], np.int64)
    assert isinstance(data["non_operating_income_expense"][0], np.int64)
    assert isinstance(
        data[
            "income_loss_from_continuing_operations_before_income_taxes_extraordinary_items_non_controlling_interest"
        ][0],
        np.int64,
    )
    assert isinstance(data["income_tax_expense_benefit"][0], np.int64)
    assert isinstance(data["net_income_loss"][0], np.int64)

    assert isinstance(data["earnings_per_share_basic"][0], np.float64)
    assert isinstance(data["earnings_per_share_diluted"][0], np.float64)
    assert isinstance(
        data["weighted_average_number_of_shares_outstanding_basic"][0], np.int64
    )
    assert isinstance(
        data["weighted_average_number_of_diluted_shares_outstanding"][0], np.int64
    )
    assert isinstance(
        data[
            "other_comprehensive_income_loss_foreign_currency_transaction_and_translation_adjustment_net_of_tax"
        ][0],
        np.int64,
    )
    assert isinstance(
        data[
            "other_comprehensive_income_loss_derivative_instrument_gain_loss_before_reclassification_after_tax"
        ][0],
        np.int64,
    )
    assert isinstance(
        data[
            "other_comprehensive_income_loss_derivative_instrument_gain_loss_reclassification_after_tax"
        ][0],
        np.int64,
    )
    assert isinstance(
        data[
            "other_comprehensive_income_loss_derivative_instrument_gain_loss_after_reclassification_and_tax"
        ][0],
        np.int64,
    )
    assert isinstance(
        data[
            "other_comprehensive_income_unrealized_holding_gain_loss_on_securities_arising_during_period_net_of_tax"
        ][0],
        np.int64,
    )
    assert isinstance(
        data[
            "other_comprehensive_income_loss_reclassification_adjustment_from_aoci_for_sale_of_securities_net_of_tax"
        ][0],
        np.int64,
    )

    assert isinstance(
        data[
            "other_comprehensive_income_loss_available_for_sale_securities_adjustment_net_of_tax"
        ][0],
        np.int64,
    )
    assert isinstance(
        data[
            "other_comprehensive_income_loss_net_of_tax_portion_attributable_to_parent"
        ][0],
        np.int64,
    )
    assert isinstance(data["comprehensive_income_net_of_tax"][0], np.int64)


def test_fmp_financial_statements_income_statements_as_reported_with_limit(
    fmp_financial_statements,
):
    data = fmp_financial_statements.income_statements_as_reported(
        "AAPL", "annual", limit=1
    )
    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert len(data) == 1


def test_fmp_financial_statements_income_statements_as_reported_invalid_period(
    fmp_financial_statements,
):
    with pytest.raises(ValueError):
        fmp_financial_statements.income_statements_as_reported("AAPL", "invalid")


def test_fmp_financial_statements_income_statements_as_reported_invalid_symbol(
    fmp_financial_statements,
):
    with pytest.raises(ValueError):
        fmp_financial_statements.income_statements_as_reported(
            "INVALID_SYMBOL", "anunual"
        )


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
