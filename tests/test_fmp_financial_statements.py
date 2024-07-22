import numpy as np
import pandas as pd
import pytest

from fmp_py.fmp_financial_statements import FmpFinancialStatements


@pytest.fixture
def fmp_financial_statements():
    return FmpFinancialStatements()


def test_fmp_financial_statements(fmp_financial_statements):
    assert isinstance(fmp_financial_statements, FmpFinancialStatements)


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
