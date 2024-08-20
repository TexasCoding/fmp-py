import pandas as pd
import pytest

from fmp_py.fmp_dividends import FmpDividends


@pytest.fixture
def fmp_dividends():
    return FmpDividends()


def test_fmp_dividends_init(fmp_dividends):
    assert isinstance(fmp_dividends, FmpDividends)


def test_fmp_dividends_calendar(fmp_dividends):
    result = fmp_dividends.dividends_calendar(
        from_date="2023-01-01", to_date="2023-01-31"
    )
    assert isinstance(result, pd.DataFrame)
    assert "date" in result.columns
    assert "label" in result.columns
    assert "adj_dividend" in result.columns
    assert "symbol" in result.columns
    assert "dividend" in result.columns
    assert "record_date" in result.columns
    assert "payment_date" in result.columns
    assert "declaration_date" in result.columns
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["label"].iloc[0], str)
    assert isinstance(result["adj_dividend"].iloc[0], float)
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["dividend"].iloc[0], float)
    assert isinstance(result["record_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["payment_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["declaration_date"].iloc[0], pd.Timestamp)


def test_fmp_dividends_calendar_invalid_date(fmp_dividends):
    with pytest.raises(Exception):
        fmp_dividends.dividends_calendar(from_date="2023-01-01", to_date="2022-01-01")


def test_fmp_dividends_historical(fmp_dividends):
    result = fmp_dividends.dividends_historical("AAPL")
    assert isinstance(result, pd.DataFrame)
    assert "date" in result.columns
    assert "label" in result.columns
    assert "adj_dividend" in result.columns
    assert "symbol" in result.columns
    assert "dividend" in result.columns
    assert "record_date" in result.columns
    assert "payment_date" in result.columns
    assert "declaration_date" in result.columns
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["label"].iloc[0], str)
    assert isinstance(result["adj_dividend"].iloc[0], float)
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["dividend"].iloc[0], float)
    assert isinstance(result["record_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["payment_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["declaration_date"].iloc[0], pd.Timestamp)


def test_fmp_dividends_historical_invalid_symbol(fmp_dividends):
    with pytest.raises(Exception):
        fmp_dividends.dividends_historical("INVALID_SYMBOL")
