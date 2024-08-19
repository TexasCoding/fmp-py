import numpy as np
import pandas as pd
import pytest

from fmp_py.fmp_forex import FmpForex


@pytest.fixture
def fmp_forex():
    return FmpForex()


def test_fmp_forex_init(fmp_forex):
    assert isinstance(fmp_forex, FmpForex)


def test_fmp_forex_forex_list(fmp_forex):
    result = fmp_forex.forex_list()
    assert not result.empty
    assert result.columns.to_list() == [
        "symbol",
        "name",
        "currency",
        "stock_exchange",
        "exchange_short_name",
    ]
    assert isinstance(result, pd.DataFrame)
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["name"].iloc[0], str)
    assert isinstance(result["currency"].iloc[0], str)
    assert isinstance(result["stock_exchange"].iloc[0], str)
    assert isinstance(result["exchange_short_name"].iloc[0], str)


def test_fmp_forex_full_forex_quote_list(fmp_forex):
    result = fmp_forex.full_forex_quote_list()
    assert result.columns.to_list() == [
        "symbol",
        "name",
        "price",
        "changes_percentage",
        "change",
        "day_low",
        "day_high",
        "year_high",
        "year_low",
        "market_cap",
        "price_avg_50",
        "price_avg_200",
        "exchange",
        "volume",
        "avg_volume",
        "open",
        "previous_close",
        "eps",
        "pe",
        "earnings_announcement",
        "shares_outstanding",
        "timestamp",
    ]
    assert isinstance(result, pd.DataFrame)
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["name"].iloc[0], str)
    assert isinstance(result["price"].iloc[0], float)
    assert isinstance(result["changes_percentage"].iloc[0], float)
    assert isinstance(result["change"].iloc[0], float)
    assert isinstance(result["day_low"].iloc[0], float)
    assert isinstance(result["day_high"].iloc[0], float)
    assert isinstance(result["year_high"].iloc[0], float)
    assert isinstance(result["year_low"].iloc[0], float)
    assert isinstance(result["market_cap"].iloc[0], np.int64)
    assert isinstance(result["price_avg_50"].iloc[0], float)
    assert isinstance(result["price_avg_200"].iloc[0], float)
    assert isinstance(result["exchange"].iloc[0], str)
    assert isinstance(result["volume"].iloc[0], np.int64)
    assert isinstance(result["avg_volume"].iloc[0], np.int64)
    assert isinstance(result["open"].iloc[0], float)
    assert isinstance(result["previous_close"].iloc[0], float)
    assert isinstance(result["eps"].iloc[0], float)
    assert isinstance(result["pe"].iloc[0], float)
    assert isinstance(result["earnings_announcement"].iloc[0], str)
    assert isinstance(result["shares_outstanding"].iloc[0], np.int64)
    assert isinstance(result["timestamp"].iloc[0], pd.Timestamp)
