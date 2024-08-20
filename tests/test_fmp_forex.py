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


def test_fmp_forex_full_forex_quote(fmp_forex):
    result = fmp_forex.full_forex_quote("EURUSD")
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


def test_fmp_forex_full_forex_quote_with_name(fmp_forex):
    result = fmp_forex.full_forex_quote("EUR/USD")
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


def test_fmp_forex_intraday_forex_quote_1min(fmp_forex):
    result = fmp_forex.intraday_forex_quote(
        symbol="EURUSD", interval="1min", from_date="2021-01-01", to_date="2021-01-02"
    )
    assert result.columns.to_list() == [
        "date",
        "open",
        "low",
        "high",
        "close",
        "volume",
    ]
    assert isinstance(result, pd.DataFrame)
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["open"].iloc[0], float)
    assert isinstance(result["low"].iloc[0], float)
    assert isinstance(result["high"].iloc[0], float)
    assert isinstance(result["close"].iloc[0], float)
    assert isinstance(result["volume"].iloc[0], np.int64)


def test_fmp_forex_intraday_forex_quote_5min(fmp_forex):
    result = fmp_forex.intraday_forex_quote(
        symbol="EURUSD", interval="5min", from_date="2021-01-01", to_date="2021-01-02"
    )
    assert result.columns.to_list() == [
        "date",
        "open",
        "low",
        "high",
        "close",
        "volume",
    ]
    assert isinstance(result, pd.DataFrame)
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["open"].iloc[0], float)
    assert isinstance(result["low"].iloc[0], float)
    assert isinstance(result["high"].iloc[0], float)
    assert isinstance(result["close"].iloc[0], float)
    assert isinstance(result["volume"].iloc[0], np.int64)


def test_fmp_forex_intraday_forex_quote_15min(fmp_forex):
    result = fmp_forex.intraday_forex_quote(
        symbol="EURUSD", interval="15min", from_date="2021-01-01", to_date="2021-01-02"
    )
    assert result.columns.to_list() == [
        "date",
        "open",
        "low",
        "high",
        "close",
        "volume",
    ]
    assert isinstance(result, pd.DataFrame)
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["open"].iloc[0], float)
    assert isinstance(result["low"].iloc[0], float)
    assert isinstance(result["high"].iloc[0], float)
    assert isinstance(result["close"].iloc[0], float)
    assert isinstance(result["volume"].iloc[0], np.int64)


def test_fmp_forex_intraday_forex_quote_30min(fmp_forex):
    result = fmp_forex.intraday_forex_quote(
        symbol="EURUSD", interval="30min", from_date="2021-01-01", to_date="2021-01-02"
    )
    assert result.columns.to_list() == [
        "date",
        "open",
        "low",
        "high",
        "close",
        "volume",
    ]
    assert isinstance(result, pd.DataFrame)
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["open"].iloc[0], float)
    assert isinstance(result["low"].iloc[0], float)
    assert isinstance(result["high"].iloc[0], float)
    assert isinstance(result["close"].iloc[0], float)
    assert isinstance(result["volume"].iloc[0], np.int64)


def test_fmp_forex_intraday_forex_quote_1hour(fmp_forex):
    result = fmp_forex.intraday_forex_quote(
        symbol="EURUSD", interval="1hour", from_date="2021-01-01", to_date="2021-01-02"
    )
    assert result.columns.to_list() == [
        "date",
        "open",
        "low",
        "high",
        "close",
        "volume",
    ]
    assert isinstance(result, pd.DataFrame)
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["open"].iloc[0], float)
    assert isinstance(result["low"].iloc[0], float)
    assert isinstance(result["high"].iloc[0], float)
    assert isinstance(result["close"].iloc[0], float)
    assert isinstance(result["volume"].iloc[0], np.int64)


def test_fmp_forex_intraday_forex_quote_4hour(fmp_forex):
    result = fmp_forex.intraday_forex_quote(
        symbol="EURUSD", interval="4hour", from_date="2021-01-01", to_date="2021-01-02"
    )
    assert result.columns.to_list() == [
        "date",
        "open",
        "low",
        "high",
        "close",
        "volume",
    ]
    assert isinstance(result, pd.DataFrame)
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["open"].iloc[0], float)
    assert isinstance(result["low"].iloc[0], float)
    assert isinstance(result["high"].iloc[0], float)
    assert isinstance(result["close"].iloc[0], float)
    assert isinstance(result["volume"].iloc[0], np.int64)


def test_fmp_forex_intraday_forex_quote_1day(fmp_forex):
    result = fmp_forex.intraday_forex_quote(
        symbol="EURUSD", interval="1day", from_date="2020-11-01", to_date="2021-01-02"
    )
    assert result.columns.to_list() == [
        "date",
        "open",
        "low",
        "high",
        "close",
        "volume",
    ]
    assert isinstance(result, pd.DataFrame)
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["open"].iloc[0], float)
    assert isinstance(result["low"].iloc[0], float)
    assert isinstance(result["high"].iloc[0], float)
    assert isinstance(result["close"].iloc[0], float)
    assert isinstance(result["volume"].iloc[0], np.int64)


def test_fmp_forex_intraday_forex_quote_1week(fmp_forex):
    result = fmp_forex.intraday_forex_quote(
        symbol="EURUSD", interval="1week", from_date="2021-01-01", to_date="2021-01-02"
    )
    assert result.columns.to_list() == [
        "date",
        "open",
        "low",
        "high",
        "close",
        "volume",
    ]
    assert isinstance(result, pd.DataFrame)
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["open"].iloc[0], float)
    assert isinstance(result["low"].iloc[0], float)
    assert isinstance(result["high"].iloc[0], float)
    assert isinstance(result["close"].iloc[0], float)
    assert isinstance(result["volume"].iloc[0], np.int64)


def test_fmp_forex_intraday_forex_quote_1month(fmp_forex):
    result = fmp_forex.intraday_forex_quote(
        symbol="EURUSD", interval="1month", from_date="2021-01-01", to_date="2021-01-02"
    )
    assert result.columns.to_list() == [
        "date",
        "open",
        "low",
        "high",
        "close",
        "volume",
    ]
    assert isinstance(result, pd.DataFrame)
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["open"].iloc[0], float)
    assert isinstance(result["low"].iloc[0], float)
    assert isinstance(result["high"].iloc[0], float)
    assert isinstance(result["close"].iloc[0], float)
    assert isinstance(result["volume"].iloc[0], np.int64)


def test_fmp_forex_intraday_forex_quote_wrong_interval(fmp_forex):
    with pytest.raises(ValueError):
        fmp_forex.intraday_forex_quote(
            symbol="EURUSD",
            interval="wrong",
            from_date="2021-01-01",
            to_date="2021-01-02",
        )


def test_fmp_forex_intraday_forex_quote_wrong_date(fmp_forex):
    with pytest.raises(ValueError):
        fmp_forex.intraday_forex_quote(
            symbol="EURUSD",
            interval="1min",
            from_date="2021-02-01",
            to_date="2021-01-01",
        )


def test_fmp_forex_intraday_forex_quote_wrong_symbol(fmp_forex):
    with pytest.raises(ValueError):
        fmp_forex.intraday_forex_quote(
            symbol="WRONG",
            interval="1min",
            from_date="2021-01-01",
            to_date="2021-01-02",
        )


def test_fmp_forex_forex_daily(fmp_forex):
    result = fmp_forex.forex_daily("EURUSD")
    assert result.columns.to_list() == [
        "date",
        "open",
        "high",
        "low",
        "close",
        "adj_close",
        "volume",
        "unadjusted_volume",
        "change",
        "change_percent",
        "vwap",
        "label",
        "change_over_time",
    ]
    assert isinstance(result, pd.DataFrame)
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["open"].iloc[0], float)
    assert isinstance(result["low"].iloc[0], float)
    assert isinstance(result["high"].iloc[0], float)
    assert isinstance(result["close"].iloc[0], float)
    assert isinstance(result["adj_close"].iloc[0], float)
    assert isinstance(result["volume"].iloc[0], np.int64)
    assert isinstance(result["unadjusted_volume"].iloc[0], np.int64)
    assert isinstance(result["change"].iloc[0], float)
    assert isinstance(result["change_percent"].iloc[0], float)
    assert isinstance(result["vwap"].iloc[0], float)
    assert isinstance(result["label"].iloc[0], str)
    assert isinstance(result["change_over_time"].iloc[0], float)


def test_fmp_forex_forex_daily_wrong_symbol(fmp_forex):
    with pytest.raises(ValueError):
        fmp_forex.forex_daily("WRONG")
