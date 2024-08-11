import numpy as np
import pandas as pd
import pytest

from fmp_py.fmp_ipo_calendar import FmpIpoCalendar


@pytest.fixture
def fmp_ipo_calendar():
    return FmpIpoCalendar()


def test_fmp_ipo_calendar_init(fmp_ipo_calendar):
    assert isinstance(fmp_ipo_calendar, FmpIpoCalendar)


def test_fmp_ipo_calendar_ipo_calendar_by_symbol(fmp_ipo_calendar):
    from_date = "2023-01-01"
    to_date = "2023-01-31"
    result = fmp_ipo_calendar.ipo_calendar_by_symbol(from_date, to_date)
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert "date" in result.columns
    assert "company" in result.columns
    assert "symbol" in result.columns
    assert "exchange" in result.columns
    assert "actions" in result.columns
    assert "shares" in result.columns
    assert "price_range" in result.columns
    assert "market_cap" in result.columns
    assert isinstance(result["date"].iloc[0], pd.Timestamp)
    assert isinstance(result["company"].iloc[0], str)
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["exchange"].iloc[0], str)
    assert isinstance(result["actions"].iloc[0], str)
    assert isinstance(result["shares"].iloc[0], np.int64)
    assert isinstance(result["price_range"].iloc[0], str)
    assert isinstance(result["market_cap"].iloc[0], np.int64)


def test_fmp_ipo_calendar_ipo_calendar_by_symbol_invalid_date_range(fmp_ipo_calendar):
    from_date = "2023-01-31"
    to_date = "2023-01-01"
    with pytest.raises(ValueError):
        fmp_ipo_calendar.ipo_calendar_by_symbol(from_date, to_date)


def test_fmp_ipo_calendar_ipo_prospectus(fmp_ipo_calendar):
    result = fmp_ipo_calendar.ipo_prospectus(
        from_date="2023-01-01", to_date="2023-01-31"
    )
    assert isinstance(result, pd.DataFrame)
    assert "symbol" in result.columns
    assert "cik" in result.columns
    assert "form" in result.columns
    assert "filing_date" in result.columns
    assert "accepted_date" in result.columns
    assert "ipo_date" in result.columns
    assert "price_public_per_share" in result.columns
    assert "price_public_total" in result.columns
    assert "discounts_and_commissions_per_share" in result.columns
    assert "discounts_and_commissions_total" in result.columns
    assert "proceeds_before_expenses_per_share" in result.columns
    assert "proceeds_before_expenses_total" in result.columns
    assert "url" in result.columns
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["cik"].iloc[0], str)
    assert isinstance(result["form"].iloc[0], str)
    assert isinstance(result["filing_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["accepted_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["ipo_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["price_public_per_share"].iloc[0], float)
    assert isinstance(result["price_public_total"].iloc[0], float)
    assert isinstance(result["discounts_and_commissions_per_share"].iloc[0], float)
    assert isinstance(result["discounts_and_commissions_total"].iloc[0], float)
    assert isinstance(result["proceeds_before_expenses_per_share"].iloc[0], float)
    assert isinstance(result["proceeds_before_expenses_total"].iloc[0], float)
    assert isinstance(result["url"].iloc[0], str)


def test_fmp_ipo_calendar_ipo_prspectus_invalid_date_range(fmp_ipo_calendar):
    with pytest.raises(ValueError):
        fmp_ipo_calendar.ipo_prospectus(from_date="2023-01-31", to_date="2023-01-01")


def test_fmp_ipo_calendar_ipo_confirmed(fmp_ipo_calendar):
    result = fmp_ipo_calendar.ipo_confirmed(
        from_date="2023-01-01", to_date="2023-01-31"
    )
    assert isinstance(result, pd.DataFrame)
    assert "symbol" in result.columns
    assert "cik" in result.columns
    assert "form" in result.columns
    assert "filing_date" in result.columns
    assert "accepted_date" in result.columns
    assert "effectiveness_date" in result.columns
    assert "url" in result.columns
    assert isinstance(result["symbol"].iloc[0], str)
    assert isinstance(result["cik"].iloc[0], str)
    assert isinstance(result["form"].iloc[0], str)
    assert isinstance(result["filing_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["accepted_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["effectiveness_date"].iloc[0], pd.Timestamp)
    assert isinstance(result["url"].iloc[0], str)


def test_fmp_ipo_calendar_ipo_confirmed_invalid_date_range(fmp_ipo_calendar):
    with pytest.raises(ValueError):
        fmp_ipo_calendar.ipo_confirmed(from_date="2023-01-31", to_date="2023-01-01")
