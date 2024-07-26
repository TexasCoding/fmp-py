import numpy as np
import pandas as pd
import pytest

from fmp_py.fmp_price_targets import FmpPriceTargets
from fmp_py.models.price_targets import PriceTargetConsensus, PriceTargetSummary


@pytest.fixture
def fmp_price_targets():
    return FmpPriceTargets()


def test_fmp_price_targets_init(fmp_price_targets):
    assert isinstance(fmp_price_targets, FmpPriceTargets)


def test_fmp_price_targets_price_target_consensus(fmp_price_targets):
    data = fmp_price_targets.price_target_consensus("AAPL")
    assert isinstance(data, PriceTargetConsensus)
    assert isinstance(data.symbol, str)
    assert isinstance(data.target_high, float)
    assert isinstance(data.target_low, float)
    assert isinstance(data.target_consensus, float)
    assert isinstance(data.target_median, float)


def test_fmp_price_targets_price_target_consensus_invalid_symbol(fmp_price_targets):
    with pytest.raises(ValueError):
        fmp_price_targets.price_target_consensus("INVALID_SYMBOL")


def test_fmp_price_targets_price_target_summary(fmp_price_targets):
    data = fmp_price_targets.price_target_summary("AAPL")
    assert isinstance(data, PriceTargetSummary)
    assert isinstance(data.symbol, str)
    assert isinstance(data.last_month, int)
    assert isinstance(data.last_month_avg_price_target, float)
    assert isinstance(data.last_quarter, int)
    assert isinstance(data.last_quarter_avg_price_target, float)
    assert isinstance(data.last_year, int)
    assert isinstance(data.last_year_avg_price_target, float)
    assert isinstance(data.all_time, int)
    assert isinstance(data.all_time_avg_price_target, float)
    assert isinstance(data.publishers, list)


def test_fmp_price_targets_price_target_summary_invalid_symbol(fmp_price_targets):
    with pytest.raises(ValueError):
        fmp_price_targets.price_target_summary("INVALID_SYMBOL")


def test_fmp_price_targets_price_target(fmp_price_targets):
    data = fmp_price_targets.price_target("AAPL")
    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert "symbol" in data.columns
    assert isinstance(data["symbol"][0], str)
    assert isinstance(data["published_date"][0], pd.Timestamp)
    assert isinstance(data["news_url"][0], str)
    assert isinstance(data["news_title"][0], str)
    assert isinstance(data["analyst_name"][0], str)
    assert isinstance(data["price_target"][0], np.float64)
    assert isinstance(data["adj_price_target"][0], np.float64)
    assert isinstance(data["price_when_posted"][0], np.float64)
    assert isinstance(data["news_publisher"][0], str)
    assert isinstance(data["news_base_url"][0], str)
    assert isinstance(data["analyst_company"][0], str)


def test_fmp_price_targets_price_target_invalid_symbol(fmp_price_targets):
    with pytest.raises(ValueError):
        fmp_price_targets.price_target("INVALID_SYMBOL")
