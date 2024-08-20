import numpy as np
import pandas as pd
import pytest

from fmp_py.fmp_company_information import FmpCompanyInformation
from fmp_py.models.company_information import (
    CompanyCoreInfo,
    CompanyMarketCap,
    CompanyProfile,
    StockPeers,
)


@pytest.fixture
def fmp_company_information():
    return FmpCompanyInformation()


def test_fmp_company_information_init(fmp_company_information):
    assert isinstance(fmp_company_information, FmpCompanyInformation)


def test_fmp_company_information_stock_peers(fmp_company_information):
    stock_peers = fmp_company_information.stock_peers("AAPL")
    assert isinstance(stock_peers, StockPeers)
    assert isinstance(stock_peers.symbol, str)
    assert isinstance(stock_peers.peers_list, list)


def test_fmp_company_information_stock_peers_invalid_symbol(fmp_company_information):
    with pytest.raises(ValueError):
        fmp_company_information.stock_peers("INVALID_SYMBOL")


def test_fmp_company_information_company_outlook(fmp_company_information):
    company_outlook = fmp_company_information.company_outlook("AAPL")
    assert isinstance(company_outlook, dict)


def test_fmp_company_information_company_outlook_invalid_symbol(
    fmp_company_information,
):
    with pytest.raises(ValueError):
        fmp_company_information.company_outlook("INVALID_SYMBOL")


def test_fmp_company_information_company_profile(fmp_company_information):
    company_profile = fmp_company_information.company_profile("AAPL")
    assert isinstance(company_profile, CompanyProfile)
    assert isinstance(company_profile.symbol, str)
    assert isinstance(company_profile.cik, str)
    assert isinstance(company_profile.company_name, str)
    assert isinstance(company_profile.exchange, str)
    assert isinstance(company_profile.industry, str)
    assert isinstance(company_profile.website, str)
    assert isinstance(company_profile.description, str)
    assert isinstance(company_profile.ceo, str)
    assert isinstance(company_profile.price, float)
    assert isinstance(company_profile.sector, str)
    assert isinstance(company_profile.full_time_employees, int)
    assert isinstance(company_profile.phone, str)
    assert isinstance(company_profile.address, str)
    assert isinstance(company_profile.city, str)
    assert isinstance(company_profile.state, str)
    assert isinstance(company_profile.country, str)
    assert isinstance(company_profile.zip, str)
    assert isinstance(company_profile.default_image, bool)
    assert isinstance(company_profile.image, str)
    assert isinstance(company_profile.ipo_date, str)
    assert isinstance(company_profile.dcf_diff, float)
    assert isinstance(company_profile.dcf, float)
    assert isinstance(company_profile.beta, float)
    assert isinstance(company_profile.is_etf, bool)
    assert isinstance(company_profile.is_actively_trading, bool)
    assert isinstance(company_profile.is_adr, bool)
    assert isinstance(company_profile.is_fund, bool)


def test_fmp_company_information_company_profile_invalid_symbol(
    fmp_company_information,
):
    with pytest.raises(ValueError):
        fmp_company_information.company_profile("INVALID_SYMBOL")


def test_fmp_company_information_executive_compensation(fmp_company_information):
    executive_compensation = fmp_company_information.executive_compensation("AAPL")
    assert isinstance(executive_compensation, pd.DataFrame)
    assert isinstance(executive_compensation.iloc[0]["symbol"], str)
    assert isinstance(executive_compensation.iloc[0]["cik"], str)
    assert isinstance(executive_compensation.iloc[0]["company_name"], str)
    assert isinstance(executive_compensation.iloc[0]["industry_title"], str)
    assert isinstance(executive_compensation.iloc[0]["name_and_position"], str)
    assert isinstance(executive_compensation.iloc[0]["year"], np.int64)
    assert isinstance(executive_compensation.iloc[0]["salary"], np.int64)
    assert isinstance(executive_compensation.iloc[0]["bonus"], np.int64)
    assert isinstance(executive_compensation.iloc[0]["stock_award"], np.int64)
    assert isinstance(
        executive_compensation.iloc[0]["incentive_plan_compensation"], np.int64
    )
    assert isinstance(
        executive_compensation.iloc[0]["all_other_compensation"], np.int64
    )
    assert isinstance(executive_compensation.iloc[0]["total"], np.int64)
    assert isinstance(executive_compensation.iloc[0]["accepted_date"], pd.Timestamp)
    assert isinstance(executive_compensation.iloc[0]["filing_date"], pd.Timestamp)


def test_fmp_company_information_executive_compensation_invalid_symbol(
    fmp_company_information,
):
    with pytest.raises(ValueError):
        fmp_company_information.executive_compensation("INVALID_SYMBOL")


def test_fmp_company_information_compensation_benchmark(fmp_company_information):
    compensation_benchmark = fmp_company_information.compensation_benchmark(2023)
    assert isinstance(compensation_benchmark, pd.DataFrame)
    assert isinstance(compensation_benchmark.iloc[0]["industry_title"], str)
    assert isinstance(
        compensation_benchmark.iloc[0]["average_compensation"], np.float64
    )
    assert isinstance(compensation_benchmark.iloc[0]["year"], np.int64)


def test_fmp_company_information_historical_employee_count(fmp_company_information):
    employee_count = fmp_company_information.historical_employee_count("AAPL")
    assert isinstance(employee_count, pd.DataFrame)
    assert isinstance(employee_count.iloc[0]["symbol"], str)
    assert isinstance(employee_count.iloc[0]["filed_date"], pd.Timestamp)
    assert isinstance(employee_count.iloc[0]["acceptance_time"], pd.Timestamp)
    assert isinstance(employee_count.iloc[0]["period_of_report"], pd.Timestamp)
    assert isinstance(employee_count.iloc[0]["employee_count"], np.int64)
    assert isinstance(employee_count.iloc[0]["form_type"], str)
    assert isinstance(employee_count.iloc[0]["company_name"], str)
    assert isinstance(employee_count.iloc[0]["source"], str)


def test_fmp_company_information_historical_employee_count_invalid_symbol(
    fmp_company_information,
):
    with pytest.raises(ValueError):
        fmp_company_information.historical_employee_count("INVALID_SYMBOL")


def test_fmp_company_information_company_notes(fmp_company_information):
    notes = fmp_company_information.company_notes("AAPL")
    assert isinstance(notes, pd.DataFrame)
    assert isinstance(notes.iloc[0]["symbol"], str)
    assert isinstance(notes.iloc[0]["cik"], str)
    assert isinstance(notes.iloc[0]["title"], str)
    assert isinstance(notes.iloc[0]["exchange"], str)


def test_fmp_company_information_company_notes_invalid_symbol(fmp_company_information):
    with pytest.raises(ValueError):
        fmp_company_information.company_notes("INVALID_SYMBOL")


def test_fmp_company_information_stock_screener(fmp_company_information):
    stock_screener = fmp_company_information.stock_screener()
    assert isinstance(stock_screener, pd.DataFrame)
    assert isinstance(stock_screener.iloc[0]["symbol"], str)
    assert isinstance(stock_screener.iloc[0]["company_name"], str)
    assert isinstance(stock_screener.iloc[0]["exchange"], str)
    assert isinstance(stock_screener.iloc[0]["industry"], str)
    assert isinstance(stock_screener.iloc[0]["sector"], str)
    assert isinstance(stock_screener.iloc[0]["market_cap"], np.int64)
    assert isinstance(stock_screener.iloc[0]["price"], np.float64)
    assert isinstance(stock_screener.iloc[0]["beta"], np.float64)
    assert isinstance(stock_screener.iloc[0]["volume"], np.int64)
    assert isinstance(stock_screener.iloc[0]["last_annual_dividend"], np.float64)
    assert isinstance(stock_screener.iloc[0]["exchange_short_name"], str)
    assert isinstance(stock_screener.iloc[0]["country"], str)
    assert isinstance(stock_screener.iloc[0]["is_etf"], np.bool)
    assert isinstance(stock_screener.iloc[0]["is_actively_trading"], np.bool)


def test_fmp_company_information_stock_screener_check_limit(fmp_company_information):
    stock_screener = fmp_company_information.stock_screener(limit=10)
    assert len(stock_screener) == 10


def test_fmp_company_information_stock_screener_check_exchange(fmp_company_information):
    stock_screener = fmp_company_information.stock_screener(exchange="NASDAQ")
    assert stock_screener.iloc[0]["exchange_short_name"] == "NASDAQ"


def test_fmp_company_information_stock_screener_check_industry(fmp_company_information):
    stock_screener = fmp_company_information.stock_screener(industry="Biotechnology")
    assert stock_screener.iloc[0]["industry"] == "Biotechnology"


def test_fmp_company_information_stock_screener_check_sector(fmp_company_information):
    stock_screener = fmp_company_information.stock_screener(sector="Technology")
    assert stock_screener.iloc[0]["sector"] == "Technology"


def test_fmp_company_information_stock_screener_check_market_cap_less_than(
    fmp_company_information,
):
    stock_screener = fmp_company_information.stock_screener(
        market_cap_lower_than="1000000000"
    )
    assert stock_screener.iloc[0]["market_cap"] < 1000000000


def test_fmp_company_information_stock_screener_check_market_cap_more_than(
    fmp_company_information,
):
    stock_screener = fmp_company_information.stock_screener(
        market_cap_more_than="1000000000"
    )
    assert stock_screener.iloc[0]["market_cap"] > 1000000000


def test_fmp_company_information_stock_screener_check_price_less_than(
    fmp_company_information,
):
    stock_screener = fmp_company_information.stock_screener(price_lower_than=100)
    assert stock_screener.iloc[0]["price"] < 100


def test_fmp_company_information_stock_screener_check_price_more_than(
    fmp_company_information,
):
    stock_screener = fmp_company_information.stock_screener(price_more_than=100)
    assert stock_screener.iloc[0]["price"] > 100


def test_fmp_company_information_stock_screener_check_beta_less_than(
    fmp_company_information,
):
    stock_screener = fmp_company_information.stock_screener(beta_lower_than=1)
    assert stock_screener.iloc[0]["beta"] < 1


def test_fmp_company_information_stock_grade(fmp_company_information):
    stock_grade = fmp_company_information.stock_grade("AAPL")
    assert isinstance(stock_grade, pd.DataFrame)
    assert isinstance(stock_grade.iloc[0]["symbol"], str)
    assert isinstance(stock_grade.iloc[0]["date"], pd.Timestamp)
    assert isinstance(stock_grade.iloc[0]["grading_company"], str)
    assert isinstance(stock_grade.iloc[0]["previous_grade"], str)
    assert isinstance(stock_grade.iloc[0]["new_grade"], str)


def test_fmp_company_information_stock_grade_invalid_symbol(fmp_company_information):
    with pytest.raises(ValueError):
        fmp_company_information.stock_grade("INVALID_SYMBOL")


def test_fmp_company_information_stock_grade_check_limit(fmp_company_information):
    stock_grade = fmp_company_information.stock_grade("AAPL", limit=1)
    assert len(stock_grade) == 1


def test_fmp_company_information_executives(fmp_company_information):
    executives = fmp_company_information.executives("AAPL")
    assert isinstance(executives, pd.DataFrame)
    assert isinstance(executives.iloc[0]["name"], str)
    assert isinstance(executives.iloc[0]["title"], str)
    assert isinstance(executives.iloc[0]["year_born"], np.int64)
    assert isinstance(executives.iloc[0]["currency_pay"], str)
    assert isinstance(executives.iloc[0]["gender"], str)
    assert isinstance(executives.iloc[0]["title_since"], pd.Timestamp)


def test_fmp_company_information_executives_invalid_symbol(fmp_company_information):
    with pytest.raises(ValueError):
        fmp_company_information.executives("INVALID_SYMBOL")


def test_fmp_company_information_market_cap(fmp_company_information):
    market_cap = fmp_company_information.market_cap("AAPL")
    assert isinstance(market_cap, CompanyMarketCap)
    assert isinstance(market_cap.symbol, str)
    assert isinstance(market_cap.market_cap, int)
    assert isinstance(market_cap.date, str)


def test_fmp_company_information_market_cap_invalid_symbol(fmp_company_information):
    with pytest.raises(ValueError):
        fmp_company_information.market_cap("INVALID_SYMBOL")


def test_fmp_company_information_company_core_info(fmp_company_information):
    core_info = fmp_company_information.company_core_info("AAPL")
    assert isinstance(core_info, CompanyCoreInfo)
    assert isinstance(core_info.symbol, str)
    assert isinstance(core_info.registrant_name, str)
    assert isinstance(core_info.exchange, str)
    assert isinstance(core_info.cik, str)
    assert isinstance(core_info.sic_code, str)
    assert isinstance(core_info.sic_group, str)
    assert isinstance(core_info.sic_description, str)
    assert isinstance(core_info.state_location, str)
    assert isinstance(core_info.state_of_incorporation, str)
    assert isinstance(core_info.fiscal_year_end, str)
    assert isinstance(core_info.business_address, str)
    assert isinstance(core_info.mailing_address, str)
    assert isinstance(core_info.tax_idenfication_number, str)


def test_fmp_company_information_company_core_info_invalid_symbol(
    fmp_company_information,
):
    with pytest.raises(ValueError):
        fmp_company_information.company_core_info("INVALID_SYMBOL")


def test_fmp_company_information_historical_market_cap(fmp_company_information):
    market_cap = fmp_company_information.historical_market_cap("AAPL")
    assert isinstance(market_cap, pd.DataFrame)
    assert isinstance(market_cap.iloc[0]["date"], pd.Timestamp)
    assert isinstance(market_cap.iloc[0]["market_cap"], np.int64)
    assert isinstance(market_cap.iloc[0]["symbol"], str)


def test_fmp_company_information_historical_market_cap_invalid_symbol(
    fmp_company_information,
):
    with pytest.raises(ValueError):
        fmp_company_information.historical_market_cap("INVALID_SYMBOL")


def test_fmp_company_information_historical_market_cap_invalid_from_date(
    fmp_company_information,
):
    with pytest.raises(ValueError):
        fmp_company_information.historical_market_cap("AAPL", from_date="INVALID_DATE")


def test_fmp_company_information_historical_market_cap_invalid_to_date(
    fmp_company_information,
):
    with pytest.raises(ValueError):
        fmp_company_information.historical_market_cap("AAPL", to_date="INVALID_DATE")


def test_fmp_company_information_historical_market_cap_limit_check(
    fmp_company_information,
):
    market_cap = fmp_company_information.historical_market_cap("AAPL", limit=5)
    assert len(market_cap) == 5


def test_fmp_company_information_all_countries(fmp_company_information):
    countries = fmp_company_information.all_countries()
    assert isinstance(countries, list)
    assert isinstance(countries[0], str)


def test_fmp_company_information_analyst_estimates(fmp_company_information):
    estimates = fmp_company_information.analyst_estimates("AAPL")
    assert isinstance(estimates, pd.DataFrame)
    assert isinstance(estimates.iloc[0]["symbol"], str)
    assert isinstance(estimates.iloc[0]["date"], pd.Timestamp)
    assert isinstance(estimates.iloc[0]["estimated_revenue_low"], np.int64)
    assert isinstance(estimates.iloc[0]["estimated_revenue_high"], np.int64)
    assert isinstance(estimates.iloc[0]["estimated_revenue_avg"], np.int64)
    assert isinstance(estimates.iloc[0]["estimated_ebitda_low"], np.int64)
    assert isinstance(estimates.iloc[0]["estimated_ebitda_high"], np.int64)
    assert isinstance(estimates.iloc[0]["estimated_ebitda_avg"], np.int64)
    assert isinstance(estimates.iloc[0]["estimated_ebit_low"], np.int64)
    assert isinstance(estimates.iloc[0]["estimated_ebit_high"], np.int64)
    assert isinstance(estimates.iloc[0]["estimated_ebit_avg"], np.int64)
    assert isinstance(estimates.iloc[0]["estimated_net_income_low"], np.int64)
    assert isinstance(estimates.iloc[0]["estimated_net_income_high"], np.int64)
    assert isinstance(estimates.iloc[0]["estimated_net_income_avg"], np.int64)
    assert isinstance(estimates.iloc[0]["estimated_sga_expense_low"], np.int64)
    assert isinstance(estimates.iloc[0]["estimated_sga_expense_high"], np.int64)
    assert isinstance(estimates.iloc[0]["estimated_sga_expense_avg"], np.int64)
    assert isinstance(estimates.iloc[0]["estimated_eps_avg"], np.float64)
    assert isinstance(estimates.iloc[0]["estimated_eps_low"], np.float64)
    assert isinstance(estimates.iloc[0]["estimated_eps_high"], np.float64)
    assert isinstance(estimates.iloc[0]["number_analyst_estimated_revenue"], np.int64)
    assert isinstance(estimates.iloc[0]["number_analysts_estimated_eps"], np.int64)


def test_fmp_company_information_analyst_estimates_invalid_symbol(
    fmp_company_information,
):
    with pytest.raises(ValueError):
        fmp_company_information.analyst_estimates("INVALID_SYMBOL")


def test_fmp_company_information_analyst_estimates_invalid_period(
    fmp_company_information,
):
    with pytest.raises(ValueError):
        fmp_company_information.analyst_estimates("AAPL", period="invalid_period")


def test_all_available_exchanges(fmp_company_information):
    exchanges = fmp_company_information.all_available_exchanges()
    assert isinstance(exchanges, list)
    assert len(exchanges) > 0


def test_all_available_industries(fmp_company_information):
    industries = fmp_company_information.all_available_industries()
    assert isinstance(industries, list)
    assert len(industries) > 0


def test_all_available_sectors(fmp_company_information):
    sectors = fmp_company_information.all_available_sectors()
    assert isinstance(sectors, list)
    assert len(sectors) > 0


def test_analyst_recommendations(fmp_company_information):
    recommendations = fmp_company_information.analyst_recommendations("AAPL")
    assert isinstance(recommendations, pd.DataFrame)
    assert isinstance(recommendations.iloc[0]["symbol"], str)
    assert isinstance(recommendations.iloc[0]["date"], pd.Timestamp)
    assert isinstance(recommendations.iloc[0]["analyst_ratings_strong_buy"], np.int64)
    assert isinstance(recommendations.iloc[0]["analyst_ratings_buy"], np.int64)
    assert isinstance(recommendations.iloc[0]["analyst_ratings_strong_sell"], np.int64)
    assert isinstance(recommendations.iloc[0]["analyst_ratings_sell"], np.int64)
    assert isinstance(recommendations.iloc[0]["analyst_ratings_hold"], np.int64)


def test_analyst_recommendations_invalid_symbol(fmp_company_information):
    with pytest.raises(ValueError):
        fmp_company_information.analyst_recommendations("INVALID_SYMBOL")
