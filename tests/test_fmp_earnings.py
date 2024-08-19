import pytest
import pandas as pd
import numpy as np
from fmp_py.fmp_earnings import FmpEarnings


@pytest.fixture
def fmp_earnings():
    return FmpEarnings()


def test_fmp_earnings_init(fmp_earnings):
    assert isinstance(fmp_earnings, FmpEarnings)


def test_fmp_earnings_surprises(fmp_earnings):
    result = fmp_earnings.earnings_surprises("AAPL")
    assert isinstance(result, pd.DataFrame)
    assert "symbol" in result.columns
    assert "date" in result.columns
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["estimated_earning"].iloc[0], float)
    assert isinstance(result["actual_earning_result"].iloc[0], float)


def test_fmp_earnings_surprises_invalid_symbol(fmp_earnings):
    with pytest.raises(Exception):
        fmp_earnings.earnings_surprises("INVALID_SYMBOL")


def test_fmp_earnings_confirmed(fmp_earnings):
    result = fmp_earnings.earnings_confirmed("2023-04-18", "2024-04-18")
    assert isinstance(result, pd.DataFrame)
    assert "symbol" in result.columns
    assert "date" in result.columns
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["publication_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["time"].iloc[0], str)
    assert isinstance(result["when"].iloc[0], str)
    assert isinstance(result["title"].iloc[0], str)


def test_fmp_earnings_confirmed_invalid_date(fmp_earnings):
    with pytest.raises(Exception):
        fmp_earnings.earnings_confirmed("2023-04-18", "2022-04-18")


def test_fmp_earnings_calendar(fmp_earnings):
    result = fmp_earnings.earnings_calendar("2023-04-18", "2024-04-18")
    assert isinstance(result, pd.DataFrame)
    assert "symbol" in result.columns
    assert "date" in result.columns
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["fiscal_date_ending"].iloc[0], pd.Timestamp)
    assert isinstance(result["updated_from_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["time"].iloc[0], str)
    assert isinstance(result["revenue_estimated"].iloc[0], np.int64)
    assert isinstance(result["revenue"].iloc[0], np.int64)
    assert isinstance(result["eps"].iloc[0], np.float64)
    assert isinstance(result["eps_estimated"].iloc[0], np.float64)


def test_fmp_earnings_calendar_invalid_date(fmp_earnings):
    with pytest.raises(Exception):
        fmp_earnings.earnings_calendar("2023-04-18", "2022-04-18")


def test_fmp_earnings_historical(fmp_earnings):
    result = fmp_earnings.earnings_historical("AAPL")
    assert isinstance(result, pd.DataFrame)
    assert "symbol" in result.columns
    assert "date" in result.columns
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["fiscal_date_ending"].iloc[0], pd.Timestamp)
    assert isinstance(result["updated_from_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["revenue"].iloc[0], np.int64)
    assert isinstance(result["eps"].iloc[0], np.float64)
    assert isinstance(result["eps_estimated"].iloc[0], np.float64)


def test_fmp_earnings_historical_invalid_symbol(fmp_earnings):
    with pytest.raises(Exception):
        fmp_earnings.earnings_historical("INVALID_SYMBOL")


def test_fmp_earning_within_weeks(fmp_earnings):
    result = fmp_earnings.earnings_within_weeks("AAPL", 2)
    assert isinstance(result, bool)


def test_fmp_earning_within_weeks_invalid_symbol(fmp_earnings):
    result = fmp_earnings.earnings_within_weeks("INVALID_SYMBOL", 2)
    assert not result
