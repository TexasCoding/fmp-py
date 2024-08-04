import pandas as pd
import pytest

from fmp_py.fmp_upgrades_downgrades import FMPUpgradesDowngrades
from fmp_py.models.upgrades_downgrades import UpgradesDowngrades


@pytest.fixture
def fmp_upgrades_downgrades():
    return FMPUpgradesDowngrades()


def test_fmp_upgrades_downgrades_init(fmp_upgrades_downgrades):
    assert isinstance(fmp_upgrades_downgrades, FMPUpgradesDowngrades)


def test_fmp_upgrades_downgrades_consensus(fmp_upgrades_downgrades):
    upgrades_downgrades = fmp_upgrades_downgrades.upgrades_downgrades_consensus("AAPL")
    assert isinstance(upgrades_downgrades, UpgradesDowngrades)
    assert isinstance(upgrades_downgrades.symbol, str)
    assert isinstance(upgrades_downgrades.strong_buy, int)
    assert isinstance(upgrades_downgrades.buy, int)
    assert isinstance(upgrades_downgrades.hold, int)
    assert isinstance(upgrades_downgrades.sell, int)
    assert isinstance(upgrades_downgrades.strong_sell, int)
    assert isinstance(upgrades_downgrades.consensus, str)


def test_fmp_upgrades_downgrades_consensus_no_data(fmp_upgrades_downgrades):
    with pytest.raises(ValueError):
        fmp_upgrades_downgrades.upgrades_downgrades_consensus("AAPL1234567890")


def test_fmp_upgrades_downgrades_upgrades_downgrades_by_company(
    fmp_upgrades_downgrades,
):
    upgrades_downgrades = fmp_upgrades_downgrades.upgrades_downgrades_by_company(
        "Barclays"
    )
    assert isinstance(upgrades_downgrades, pd.DataFrame)
    assert len(upgrades_downgrades) > 0
    assert "symbol" in upgrades_downgrades.columns
    assert isinstance(upgrades_downgrades["symbol"][0], str)
    assert isinstance(upgrades_downgrades["published_date"][0], pd.Timestamp)
    assert isinstance(upgrades_downgrades["news_url"][0], str)
    assert isinstance(upgrades_downgrades["news_title"][0], str)
    assert isinstance(upgrades_downgrades["news_base_url"][0], str)
    assert isinstance(upgrades_downgrades["news_publisher"][0], str)
    assert isinstance(upgrades_downgrades["new_grade"][0], str)
    assert isinstance(upgrades_downgrades["previous_grade"][0], str)
    assert isinstance(upgrades_downgrades["grading_company"][0], str)
    assert isinstance(upgrades_downgrades["action"][0], str)
    assert isinstance(upgrades_downgrades["price_when_posted"][0], float)


def test_fmp_upgrades_downgrades_upgrades_downgrades_by_company_no_data(
    fmp_upgrades_downgrades,
):
    with pytest.raises(ValueError):
        fmp_upgrades_downgrades.upgrades_downgrades_by_company("AAPL1234567890")


def test_fmp_upgrades_downgrades_upgrades_downgrades(fmp_upgrades_downgrades):
    upgrades_downgrades = fmp_upgrades_downgrades.upgrades_downgrades("AAPL")
    assert isinstance(upgrades_downgrades, pd.DataFrame)
    assert len(upgrades_downgrades) > 0
    assert "symbol" in upgrades_downgrades.columns
    assert isinstance(upgrades_downgrades["symbol"][0], str)
    assert isinstance(upgrades_downgrades["published_date"][0], pd.Timestamp)
    assert isinstance(upgrades_downgrades["news_url"][0], str)
    assert isinstance(upgrades_downgrades["news_title"][0], str)
    assert isinstance(upgrades_downgrades["news_base_url"][0], str)
    assert isinstance(upgrades_downgrades["news_publisher"][0], str)
    assert isinstance(upgrades_downgrades["new_grade"][0], str)
    assert isinstance(upgrades_downgrades["previous_grade"][0], str)
    assert isinstance(upgrades_downgrades["grading_company"][0], str)
    assert isinstance(upgrades_downgrades["action"][0], str)
    assert isinstance(upgrades_downgrades["price_when_posted"][0], float)


def test_fmp_upgrades_downgrades_upgrades_downgrades_no_data(fmp_upgrades_downgrades):
    with pytest.raises(ValueError):
        fmp_upgrades_downgrades.upgrades_downgrades("AAPL1234567890")


def test_fmp_upgrades_downgrades_upgrades_downgrades_rss_feed(fmp_upgrades_downgrades):
    upgrades_downgrades = fmp_upgrades_downgrades.upgrades_downgrades_rss_feed("AAPL")
    assert isinstance(upgrades_downgrades, pd.DataFrame)
    assert len(upgrades_downgrades) > 0
    assert "symbol" in upgrades_downgrades.columns
    assert isinstance(upgrades_downgrades["symbol"][0], str)
    assert isinstance(upgrades_downgrades["published_date"][0], pd.Timestamp)
    assert isinstance(upgrades_downgrades["news_url"][0], str)
    assert isinstance(upgrades_downgrades["news_title"][0], str)
    assert isinstance(upgrades_downgrades["news_base_url"][0], str)
    assert isinstance(upgrades_downgrades["news_publisher"][0], str)
    assert isinstance(upgrades_downgrades["new_grade"][0], str)
    assert isinstance(upgrades_downgrades["previous_grade"][0], str)
    assert isinstance(upgrades_downgrades["grading_company"][0], str)
    assert isinstance(upgrades_downgrades["action"][0], str)
    assert isinstance(upgrades_downgrades["price_when_posted"][0], float)
