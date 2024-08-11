import numpy as np
import pandas as pd
import pytest

from fmp_py.fmp_splits import FmpSplits


@pytest.fixture
def fmp_splits():
    return FmpSplits()


def test_fmp_splits_init(fmp_splits):
    assert isinstance(fmp_splits, FmpSplits)


def test_fmp_splits_stock_splits_calendar(fmp_splits):
    result = fmp_splits.stock_splits_calendar("2023-01-01", "2023-01-31")
    assert isinstance(result, pd.DataFrame)
    assert "date" in result.columns
    assert "label" in result.columns
    assert "symbol" in result.columns
    assert "numerator" in result.columns
    assert "denominator" in result.columns
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["label"].iloc[0], str)
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["numerator"].iloc[0], np.int64)
    assert isinstance(result["denominator"].iloc[0], np.int64)


def test_fmp_splits_stock_splits_calendar_invalid_date_range(fmp_splits):
    with pytest.raises(ValueError):
        fmp_splits.stock_splits_calendar("2023-01-31", "2023-01-01")


def test_fmp_splits_stock_splits_historical(fmp_splits):
    result = fmp_splits.stock_splits_historical("AAPL")
    assert isinstance(result, pd.DataFrame)
    assert "date" in result.columns
    assert "label" in result.columns
    assert "symbol" in result.columns
    assert "numerator" in result.columns
    assert "denominator" in result.columns
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["label"].iloc[0], str)
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["numerator"].iloc[0], np.int64)
    assert isinstance(result["denominator"].iloc[0], np.int64)


def test_fmp_splits_stock_splits_historical_invalid_symbol(fmp_splits):
    with pytest.raises(ValueError):
        fmp_splits.stock_splits_historical("INVALID_SYMBOL")
