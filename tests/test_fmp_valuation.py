import numpy as np
import pandas as pd
import pytest

from fmp_py.fmp_valuation import FmpValuation
from fmp_py.models.valuation import CompanyRating, DiscountedCashFlow


@pytest.fixture
def fmp_valuation():
    return FmpValuation()


def test_fmp_valuation_init(fmp_valuation):
    assert isinstance(fmp_valuation, FmpValuation)


def test_fmp_valuation_historical_rating(fmp_valuation):
    historical_rating = fmp_valuation.historical_rating("AAPL")
    assert isinstance(historical_rating, pd.DataFrame)
    assert isinstance(historical_rating["date"][0], pd.Timestamp)
    assert isinstance(historical_rating["symbol"][0], str)
    assert isinstance(historical_rating["rating"][0], str)
    assert isinstance(historical_rating["rating_score"][0], np.int64)
    assert isinstance(historical_rating["rating_recommendation"][0], str)
    assert isinstance(historical_rating["rating_details_dcf_recommendation"][0], str)
    assert isinstance(historical_rating["rating_details_roe_score"][0], np.int64)
    assert isinstance(historical_rating["rating_details_roe_recommendation"][0], str)
    assert isinstance(historical_rating["rating_details_roa_score"][0], np.int64)
    assert isinstance(historical_rating["rating_details_roa_recommendation"][0], str)
    assert isinstance(historical_rating["rating_details_de_score"][0], np.int64)
    assert isinstance(historical_rating["rating_details_de_recommendation"][0], str)
    assert isinstance(historical_rating["rating_details_pe_score"][0], np.int64)
    assert isinstance(historical_rating["rating_details_pe_recommendation"][0], str)
    assert isinstance(historical_rating["rating_details_pb_score"][0], np.int64)


def test_fmp_valuation_historical_rating_invalid_symbol(fmp_valuation):
    with pytest.raises(ValueError):
        fmp_valuation.historical_rating("INVALID_SYMBOL")


def test_fmp_valuation_levered_dcf(fmp_valuation):
    valuation = fmp_valuation.levered_dcf("AAPL")
    assert isinstance(valuation, pd.DataFrame)
    assert isinstance(valuation["year"][0], np.int64)
    assert isinstance(valuation["symbol"][0], str)
    assert isinstance(valuation["revenue"][0], np.int64)
    assert isinstance(valuation["revenue_percentage"][0], np.float64)
    assert isinstance(valuation["capital_expenditure"][0], np.int64)
    assert isinstance(valuation["price"][0], np.float64)
    assert isinstance(valuation["beta"][0], np.float64)
    assert isinstance(valuation["diluted_shares_outstanding"][0], np.int64)
    assert isinstance(valuation["cost_of_debt"][0], np.float64)
    assert isinstance(valuation["tax_rate"][0], np.float64)
    assert isinstance(valuation["after_tax_cost_of_debt"][0], np.float64)
    assert isinstance(valuation["risk_free_rate"][0], np.float64)
    assert isinstance(valuation["market_risk_premium"][0], np.float64)
    assert isinstance(valuation["cost_of_equity"][0], np.float64)
    assert isinstance(valuation["total_debt"][0], np.int64)
    assert isinstance(valuation["total_equity"][0], np.int64)
    assert isinstance(valuation["total_capital"][0], np.int64)
    assert isinstance(valuation["debt_weighting"][0], np.float64)

    assert isinstance(valuation["equity_weighting"][0], np.float64)
    assert isinstance(valuation["wacc"][0], np.float64)
    assert isinstance(valuation["operating_cash_flow"][0], np.int64)
    assert isinstance(valuation["pv_lfcf"][0], np.int64)
    assert isinstance(valuation["sum_pv_lfcf"][0], np.int64)
    assert isinstance(valuation["long_term_growth_rate"][0], np.float64)
    assert isinstance(valuation["free_cash_flow"][0], np.int64)
    assert isinstance(valuation["terminal_value"][0], np.int64)
    assert isinstance(valuation["present_terminal_value"][0], np.int64)
    assert isinstance(valuation["enterprise_value"][0], np.int64)
    assert isinstance(valuation["net_debt"][0], np.int64)
    assert isinstance(valuation["equity_value"][0], np.int64)
    assert isinstance(valuation["equity_value_per_share"][0], np.float64)
    assert isinstance(valuation["free_cash_flow_t1"][0], np.int64)
    assert isinstance(valuation["operating_cash_flow_percentage"][0], np.float64)


def test_fmp_valuation_levered_dcf_invalid_symbol(fmp_valuation):
    with pytest.raises(ValueError):
        fmp_valuation.levered_dcf("INVALID_SYMBOL")


def test_fmp_valuation_advanced_dcf(fmp_valuation):
    adcf = fmp_valuation.advanced_dcf("AAPL")
    assert isinstance(adcf, pd.DataFrame)
    assert isinstance(adcf["year"][0], np.int64)
    assert isinstance(adcf["symbol"][0], str)
    assert isinstance(adcf["revenue"][0], np.int64)
    assert isinstance(adcf["revenue_percentage"][0], np.float64)

    assert isinstance(adcf["ebitda"][0], np.int64)
    assert isinstance(adcf["ebitda_percentage"][0], np.float64)
    assert isinstance(adcf["ebit"][0], np.int64)
    assert isinstance(adcf["depreciation"][0], np.int64)
    assert isinstance(adcf["depreciation_percentage"][0], np.float64)
    assert isinstance(adcf["total_cash"][0], np.int64)
    assert isinstance(adcf["total_cash_percentage"][0], np.float64)
    assert isinstance(adcf["receivables"][0], np.int64)
    assert isinstance(adcf["receivables_percentage"][0], np.float64)
    assert isinstance(adcf["inventories"][0], np.int64)

    assert isinstance(adcf["inventories_percentage"][0], np.float64)
    assert isinstance(adcf["payable"][0], np.int64)
    assert isinstance(adcf["payable_percentage"][0], np.float64)
    assert isinstance(adcf["capital_expenditure"][0], np.int64)
    assert isinstance(adcf["capital_expenditure_percentage"][0], np.float64)
    assert isinstance(adcf["price"][0], np.float64)
    assert isinstance(adcf["beta"][0], np.float64)
    assert isinstance(adcf["diluted_shares_outstanding"][0], np.int64)
    assert isinstance(adcf["cost_of_debt"][0], np.float64)
    assert isinstance(adcf["tax_rate"][0], np.float64)

    assert isinstance(adcf["after_tax_cost_of_debt"][0], np.float64)
    assert isinstance(adcf["risk_free_rate"][0], np.float64)
    assert isinstance(adcf["market_risk_premium"][0], np.float64)
    assert isinstance(adcf["cost_of_equity"][0], np.float64)
    assert isinstance(adcf["total_debt"][0], np.int64)
    assert isinstance(adcf["total_equity"][0], np.int64)
    assert isinstance(adcf["total_capital"][0], np.int64)
    assert isinstance(adcf["debt_weighting"][0], np.float64)
    assert isinstance(adcf["equity_weighting"][0], np.float64)
    assert isinstance(adcf["wacc"][0], np.float64)

    assert isinstance(adcf["tax_rate_cash"][0], np.int64)
    assert isinstance(adcf["ebiat"][0], np.int64)
    assert isinstance(adcf["ufcf"][0], np.int64)
    assert isinstance(adcf["sum_pv_ufcf"][0], np.int64)
    assert isinstance(adcf["long_term_growth_rate"][0], np.float64)
    assert isinstance(adcf["terminal_value"][0], np.int64)
    assert isinstance(adcf["present_terminal_value"][0], np.int64)
    assert isinstance(adcf["enterprise_value"][0], np.int64)
    assert isinstance(adcf["net_debt"][0], np.int64)
    assert isinstance(adcf["equity_value"][0], np.int64)

    assert isinstance(adcf["equity_value_per_share"][0], np.float64)
    assert isinstance(adcf["free_cash_flow_t1"][0], np.int64)


def test_fmp_valuation_advanced_dcf_invalid_symbol(fmp_valuation):
    with pytest.raises(ValueError):
        fmp_valuation.advanced_dcf("INVALID_SYMBOL")


def test_fmp_valuation_discounted_cash_flow(fmp_valuation):
    valuation = fmp_valuation.discounted_cash_flow("AAPL")
    assert isinstance(valuation, DiscountedCashFlow)
    assert valuation.symbol == "AAPL"
    assert isinstance(valuation.date, str)
    assert isinstance(valuation.dcf, float)
    assert isinstance(valuation.stock_price, float)


def test_fmp_valuation_discounted_cash_flow_invalid_symbol(fmp_valuation):
    with pytest.raises(ValueError):
        fmp_valuation.discounted_cash_flow("INVALID_SYMBOL")


def test_fmp_valuation_company_rating(fmp_valuation):
    valuation = fmp_valuation.company_rating("AAPL")
    assert isinstance(valuation, CompanyRating)
    assert valuation.symbol == "AAPL"
    assert isinstance(valuation.date, str)
    assert isinstance(valuation.rating, str)
    assert isinstance(valuation.rating_score, int)
    assert isinstance(valuation.rating_recommendation, str)
    assert isinstance(valuation.rating_details_dcf_score, int)
    assert isinstance(valuation.rating_details_dcf_recommendation, str)
    assert isinstance(valuation.rating_details_roe_score, int)
    assert isinstance(valuation.rating_details_roe_recommendation, str)
    assert isinstance(valuation.rating_details_roa_score, int)
    assert isinstance(valuation.rating_details_roa_recommendation, str)
    assert isinstance(valuation.rating_details_de_score, int)
    assert isinstance(valuation.rating_details_de_recommendation, str)
    assert isinstance(valuation.rating_details_pe_score, int)
    assert isinstance(valuation.rating_details_pe_recommendation, str)
    assert isinstance(valuation.rating_details_pb_score, int)
    assert isinstance(valuation.rating_details_pb_recommendation, str)


def test_fmp_valuation_company_rating_invalid_symbol(fmp_valuation):
    with pytest.raises(ValueError):
        fmp_valuation.company_rating("INVALID_SYMBOL")
