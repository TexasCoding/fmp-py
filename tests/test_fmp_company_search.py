import numpy as np
import pandas as pd
import pytest

from fmp_py.fmp_company_search import FmpCompanySearch


@pytest.fixture
def fmp_company_search():
    return FmpCompanySearch()


def test_fmp_company_search_isin_search(fmp_company_search):
    search_results = fmp_company_search.isin_search("US0378331005")
    assert isinstance(search_results, pd.DataFrame)
    assert len(search_results) > 0
    assert "symbol" in search_results.columns
    assert "company_name" in search_results.columns
    assert isinstance(search_results["symbol"].iloc[0], str)
    assert isinstance(search_results["company_name"].iloc[0], str)
    assert isinstance(search_results["currency"].iloc[0], str)
    assert isinstance(search_results["exchange"].iloc[0], str)
    assert isinstance(search_results["exchange_short_name"].iloc[0], str)
    assert isinstance(search_results["city"].iloc[0], str)
    assert isinstance(search_results["country"].iloc[0], str)
    assert isinstance(search_results["website"].iloc[0], str)
    assert isinstance(search_results["industry"].iloc[0], str)
    assert isinstance(search_results["description"].iloc[0], str)
    assert isinstance(search_results["sector"].iloc[0], str)
    assert isinstance(search_results["full_time_employees"].iloc[0], np.int64)
    assert isinstance(search_results["phone"].iloc[0], str)
    assert isinstance(search_results["address"].iloc[0], str)
    assert isinstance(search_results["state"].iloc[0], str)
    assert isinstance(search_results["zip"].iloc[0], str)
    assert isinstance(search_results["price"].iloc[0], np.float64)
    assert isinstance(search_results["beta"].iloc[0], np.float64)
    assert isinstance(search_results["default_image"].iloc[0], np.bool)
    assert isinstance(search_results["is_actively_trading"].iloc[0], np.bool)
    assert isinstance(search_results["is_adr"].iloc[0], np.bool)
    assert isinstance(search_results["is_etf"].iloc[0], np.bool)
    assert isinstance(search_results["is_fund"].iloc[0], np.bool)


def test_fmp_company_search_isin_search_invalid_isin(fmp_company_search):
    with pytest.raises(ValueError):
        fmp_company_search.isin_search("invalid_isin")


def test_fmp_company_search_cik_name_search(fmp_company_search):
    search_results = fmp_company_search.cik_name_search("apple")
    assert isinstance(search_results, pd.DataFrame)
    assert len(search_results) > 0
    assert "cik" in search_results.columns
    assert "name" in search_results.columns
    assert isinstance(search_results["cik"].iloc[0], str)
    assert isinstance(search_results["name"].iloc[0], str)


def test_fmp_company_search_cik_name_search_invalid_company_name(fmp_company_search):
    with pytest.raises(ValueError):
        fmp_company_search.cik_name_search("invalid_company_name")


def test_fmp_company_search_cik_search(fmp_company_search):
    search_results = fmp_company_search.cik_search("0001067983")
    assert isinstance(search_results, pd.DataFrame)
    assert len(search_results) > 0
    assert "cik" in search_results.columns
    assert "name" in search_results.columns
    assert isinstance(search_results["cik"].iloc[0], str)
    assert isinstance(search_results["name"].iloc[0], str)


def test_fmp_company_search_cik_search_invalid_cik(fmp_company_search):
    with pytest.raises(ValueError):
        fmp_company_search.cik_search("invalid_cik")


def test_fmp_company_search_name_search(fmp_company_search):
    search_results = fmp_company_search.name_search("apple")
    assert isinstance(search_results, pd.DataFrame)
    assert len(search_results) > 0
    assert "symbol" in search_results.columns
    assert "name" in search_results.columns
    assert "currency" in search_results.columns
    assert "stock_exchange" in search_results.columns
    assert "exchange_short_name" in search_results.columns
    assert isinstance(search_results["symbol"].iloc[0], str)
    assert isinstance(search_results["name"].iloc[0], str)
    assert isinstance(search_results["currency"].iloc[0], str)
    assert isinstance(search_results["stock_exchange"].iloc[0], str)


def test_fmp_company_search_name_search_with_limit(fmp_company_search):
    search_results = fmp_company_search.name_search("apple", limit=10)
    assert len(search_results) == 10


def test_fmp_company_search_name_search_with_exchange(fmp_company_search):
    search_results = fmp_company_search.name_search("apple", exchange="NASDAQ")
    assert len(search_results) > 0
    assert search_results["stock_exchange"].str.contains("NASDAQ").all()


def test_fmp_company_search_name_search_with_invalid_exchange(fmp_company_search):
    with pytest.raises(ValueError):
        fmp_company_search.name_search("apple", exchange="INVALID_EXCHANGE")


def test_fmp_company_search_name_search_with_no_results(fmp_company_search):
    with pytest.raises(ValueError):
        fmp_company_search.name_search("INVALID_QUERY")


def test_fmp_company_search_ticker_search(fmp_company_search):
    search_results = fmp_company_search.ticker_search("apple")
    assert isinstance(search_results, pd.DataFrame)
    assert len(search_results) > 0
    assert "symbol" in search_results.columns
    assert "name" in search_results.columns
    assert "currency" in search_results.columns
    assert "stock_exchange" in search_results.columns
    assert "exchange_short_name" in search_results.columns
    assert isinstance(search_results["symbol"].iloc[0], str)
    assert isinstance(search_results["name"].iloc[0], str)
    assert isinstance(search_results["currency"].iloc[0], str)
    assert isinstance(search_results["stock_exchange"].iloc[0], str)
    assert isinstance(search_results["exchange_short_name"].iloc[0], str)


def test_fmp_company_search_ticker_search_with_limit(fmp_company_search):
    search_results = fmp_company_search.ticker_search("apple", limit=10)
    assert len(search_results) == 10


def test_fmp_company_search_ticker_search_with_invalid_exchange(fmp_company_search):
    with pytest.raises(ValueError):
        fmp_company_search.ticker_search("apple", exchange="invalid_exchange")


def test_fmp_company_search_ticker_search_with_no_data(fmp_company_search):
    with pytest.raises(ValueError):
        fmp_company_search.ticker_search("invalid_query")


def test_fmp_company_search_general_search(fmp_company_search):
    search_results = fmp_company_search.general_search("apple")
    assert isinstance(search_results, pd.DataFrame)
    assert len(search_results) > 0
    assert "symbol" in search_results.columns
    assert "name" in search_results.columns
    assert "currency" in search_results.columns
    assert "stock_exchange" in search_results.columns
    assert "exchange_short_name" in search_results.columns
    assert isinstance(search_results["symbol"].iloc[0], str)
    assert isinstance(search_results["name"].iloc[0], str)
    assert isinstance(search_results["currency"].iloc[0], str)
    assert isinstance(search_results["stock_exchange"].iloc[0], str)
    assert isinstance(search_results["exchange_short_name"].iloc[0], str)


def test_fmp_company_search_general_search_invalid_exchange(fmp_company_search):
    with pytest.raises(ValueError):
        fmp_company_search.general_search("apple", exchange="invalid_exchange")


def test_fmp_company_search_general_search_check_limit(fmp_company_search):
    search_results = fmp_company_search.general_search("apple", limit=1)
    assert len(search_results) == 1


def test_fmp_company_search_general_search_no_results(fmp_company_search):
    with pytest.raises(ValueError):
        fmp_company_search.general_search("invalid_query")
