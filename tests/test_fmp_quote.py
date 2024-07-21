import pytest

from fmp_py.fmp_quote import FmpQuote
from fmp_py.models.quote import Quote


@pytest.fixture
def fmp_quote():
    return FmpQuote()


def test_fmp_quote_init(fmp_quote):
    assert isinstance(fmp_quote, FmpQuote)


def test_fmp_quote_quote_order(fmp_quote):
    quote = fmp_quote.quote_order("AAPL")
    assert isinstance(quote, Quote)
    assert quote.symbol == "AAPL"
    assert isinstance(quote.name, str)
    assert isinstance(quote.price, float)
    assert isinstance(quote.change_percentage, float)
    assert isinstance(quote.change, float)
    assert isinstance(quote.day_low, float)
    assert isinstance(quote.day_high, float)
    assert isinstance(quote.year_low, float)
    assert isinstance(quote.year_high, float)
    assert isinstance(quote.market_cap, int)
    assert isinstance(quote.price_avg_50, float)
    assert isinstance(quote.price_avg_200, float)
    assert isinstance(quote.volume, int)
    assert isinstance(quote.avg_volume, int)
    assert isinstance(quote.exchange, str)
    assert isinstance(quote.open, float)
    assert isinstance(quote.previous_close, float)
    assert isinstance(quote.eps, float)
    assert isinstance(quote.pe, float)
    assert isinstance(quote.earnings_date, str)
    assert isinstance(quote.shares_outstanding, int)
    assert isinstance(quote.timestamp, str)


def test_fmp_quote_quote_order_invalid_symbol(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.quote_order("INVALID_SYMBOL")


def test_fmp_quote_full_quote(fmp_quote):
    quote = fmp_quote.full_quote("AAPL")
    assert isinstance(quote, Quote)
    assert quote.symbol == "AAPL"
    assert isinstance(quote.name, str)
    assert isinstance(quote.price, float)
    assert isinstance(quote.change_percentage, float)
    assert isinstance(quote.change, float)
    assert isinstance(quote.day_low, float)
    assert isinstance(quote.day_high, float)
    assert isinstance(quote.year_low, float)
    assert isinstance(quote.year_high, float)
    assert isinstance(quote.market_cap, int)
    assert isinstance(quote.price_avg_50, float)
    assert isinstance(quote.price_avg_200, float)
    assert isinstance(quote.volume, int)
    assert isinstance(quote.avg_volume, int)
    assert isinstance(quote.exchange, str)
    assert isinstance(quote.open, float)
    assert isinstance(quote.previous_close, float)
    assert isinstance(quote.eps, float)
    assert isinstance(quote.pe, float)
    assert isinstance(quote.earnings_date, str)
    assert isinstance(quote.shares_outstanding, int)
    assert isinstance(quote.timestamp, str)


def test_fmp_quote_full_quote_invalid_symbol(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.full_quote("INVALID_SYMBOL")
