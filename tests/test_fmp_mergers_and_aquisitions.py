import pytest
import pandas as pd

from fmp_py.fmp_mergers_and_aquisitions import FmpMergersAndAquisitions


@pytest.fixture
def fmp_mergers_and_aquisitions():
    return FmpMergersAndAquisitions()


def test_fmp_mergers_and_aquisitions_init(fmp_mergers_and_aquisitions):
    assert isinstance(fmp_mergers_and_aquisitions, FmpMergersAndAquisitions)


def test_fmp_mergers_and_aquisitions_ma_rss_feed(fmp_mergers_and_aquisitions):
    result = fmp_mergers_and_aquisitions.ma_rss_feed()
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert result.columns.tolist() == [
        "company_name",
        "cik",
        "symbol",
        "targeted_company_name",
        "targeted_cik",
        "targeted_symbol",
        "transaction_date",
        "acceptance_time",
        "url",
    ]
    assert isinstance(result["company_name"].iloc[0], str)
    assert isinstance(result["cik"].iloc[0], str)
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["targeted_company_name"].iloc[0], str)
    assert isinstance(result["targeted_cik"].iloc[0], str)
    assert isinstance(result["targeted_symbol"].iloc[0], str)
    assert isinstance(result["transaction_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["acceptance_time"].iloc[0], pd.Timestamp)
    assert isinstance(result["url"].iloc[0], str)


def test_fmp_mergers_and_aquisitions_ma_rss_feed_by_page(fmp_mergers_and_aquisitions):
    result = fmp_mergers_and_aquisitions.ma_rss_feed(page=1)
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert result.columns.tolist() == [
        "company_name",
        "cik",
        "symbol",
        "targeted_company_name",
        "targeted_cik",
        "targeted_symbol",
        "transaction_date",
        "acceptance_time",
        "url",
    ]
    assert isinstance(result["company_name"].iloc[0], str)
    assert isinstance(result["cik"].iloc[0], str)
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["targeted_company_name"].iloc[0], str)
    assert isinstance(result["targeted_cik"].iloc[0], str)
    assert isinstance(result["targeted_symbol"].iloc[0], str)
    assert isinstance(result["transaction_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["acceptance_time"].iloc[0], pd.Timestamp)
    assert isinstance(result["url"].iloc[0], str)


def test_fmp_mergers_and_aquisitions_search_ma(fmp_mergers_and_aquisitions):
    result = fmp_mergers_and_aquisitions.search_ma(name="test")
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert result.columns.tolist() == [
        "company_name",
        "cik",
        "symbol",
        "targeted_company_name",
        "targeted_cik",
        "targeted_symbol",
        "transaction_date",
        "acceptance_time",
        "url",
    ]
    assert isinstance(result["company_name"].iloc[0], str)
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["targeted_company_name"].iloc[0], str)
    assert isinstance(result["targeted_cik"].iloc[0], str)
    assert isinstance(result["targeted_symbol"].iloc[0], str)
    assert isinstance(result["transaction_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["acceptance_time"].iloc[0], pd.Timestamp)
    assert isinstance(result["url"].iloc[0], str)
