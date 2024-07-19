import pytest
from unittest.mock import patch
from fmp_py.fmp_historical_data import FmpHistoricalData
import pandas as pd


@pytest.fixture
def mock_response_daily():
    return {
        "historical": [
            {
                "date": "2023-01-01",
                "open": 100,
                "high": 110,
                "low": 90,
                "close": 105,
                "volume": 1000,
            },
            {
                "date": "2023-01-02",
                "open": 106,
                "high": 115,
                "low": 105,
                "close": 110,
                "volume": 1500,
            },
        ]
    }


@pytest.fixture
def mock_response_intraday():
    return [
        {
            "date": "2023-01-01 09:30:00",
            "open": 100,
            "high": 110,
            "low": 90,
            "close": 105,
            "volume": 1000,
        },
        {
            "date": "2023-01-01 09:31:00",
            "open": 106,
            "high": 115,
            "low": 105,
            "close": 110,
            "volume": 1500,
        },
    ]


def test_fmp_historical_data_initialization():
    fmp = FmpHistoricalData()
    assert hasattr(
        fmp, "api_key"
    ), "FmpHistoricalData class should have an attribute 'api_key'"


@patch.object(FmpHistoricalData, "get_request")
def test_daily_history(mock_get_request, mock_response_daily):
    mock_get_request.return_value = mock_response_daily

    fmp = FmpHistoricalData()
    symbol = "AAPL"
    from_date = "2023-01-01"
    to_date = "2023-01-02"
    data = fmp.daily_history(symbol, from_date, to_date)

    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert "vwap" in data.columns


@patch.object(FmpHistoricalData, "get_request")
def test_intraday_history(mock_get_request, mock_response_intraday):
    mock_get_request.return_value = mock_response_intraday

    fmp = FmpHistoricalData()
    symbol = "AAPL"
    interval = "1min"
    from_date = "2023-01-01"
    to_date = "2023-01-01"
    data = fmp.intraday_history(symbol, interval, from_date, to_date)

    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert "vwap" in data.columns


def test_prepare_data():
    fmp = FmpHistoricalData()
    data_df = pd.DataFrame(
        {
            "date": ["2023-01-01", "2023-01-02"],
            "open": [100, 106],
            "high": [110, 115],
            "low": [90, 105],
            "close": [105, 110],
            "volume": [1000, 1500],
        }
    )

    prepared_data = fmp._prepare_data(data_df.copy())
    assert "vwap" in prepared_data.columns
    assert prepared_data["vwap"].dtype == "float"
    assert prepared_data["date"].dtype == "datetime64[ns]"


def test_calc_vwap():
    fmp = FmpHistoricalData()
    data_df = pd.DataFrame(
        {
            "date": ["2023-01-01", "2023-01-02"],
            "open": [100, 106],
            "high": [110, 115],
            "low": [90, 105],
            "close": [105, 110],
            "volume": [1000, 1500],
        }
    )

    vwap = fmp._calc_vwap(data_df)
    expected_vwap = pd.Series([101.67, 106.67])
    pd.testing.assert_series_equal(vwap.round(2), expected_vwap)


def test_round_prices():
    fmp = FmpHistoricalData()
    data_df = pd.DataFrame(
        {
            "date": ["2023-01-01", "2023-01-02"],
            "open": [100.123, 106.456],
            "high": [110.789, 115.101],
            "low": [90.112, 105.991],
            "close": [105.553, 110.234],
            "volume": [1000, 1500],
        }
    )

    rounded_data = fmp._round_prices(data_df)
    assert rounded_data["open"].iloc[0] == 100.12
    assert rounded_data["high"].iloc[1] == 115.10
    assert rounded_data["low"].iloc[0] == 90.11
    assert rounded_data["close"].iloc[1] == 110.23
