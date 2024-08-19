import numpy as np
import pytest
import pandas as pd
from fmp_py.fmp_quote import FmpQuote
from fmp_py.models.quote import (
    AftermarketTrade,
    AftermarketQuote,
    CryptoQuote,
    ForexQuote,
    FxPrice,
    RealtimeFullPrice,
    Quote,
    SimpleQuote,
    OtcQuote,
    PriceChange,
)


@pytest.fixture
def fmp_quote():
    return FmpQuote()


def test_fmp_quote_init(fmp_quote):
    assert isinstance(fmp_quote, FmpQuote)


def test_fmp_quote_fx_prices(fmp_quote):
    df = fmp_quote.fx_prices()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(df["ticker"][0], str)
    assert isinstance(df["bid"][0], np.float64)
    assert isinstance(df["ask"][0], np.float64)
    assert isinstance(df["open"][0], np.float64)
    assert isinstance(df["low"][0], np.float64)
    assert isinstance(df["high"][0], np.float64)
    assert isinstance(df["changes"][0], np.float64)
    assert isinstance(df["date"][0], pd.Timestamp)


def test_fmp_quote_fx_prices_no_results(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.fx_prices() == []


def test_fmp_quote_fx_price(fmp_quote):
    fx_price = fmp_quote.fx_price("EURUSD")
    assert isinstance(fx_price, FxPrice)
    assert fx_price.ticker == "EUR/USD"
    assert isinstance(fx_price.ticker, str)
    assert isinstance(fx_price.bid, float)
    assert isinstance(fx_price.ask, float)
    assert isinstance(fx_price.open, float)
    assert isinstance(fx_price.low, float)
    assert isinstance(fx_price.high, float)
    assert isinstance(fx_price.changes, float)
    assert isinstance(fx_price.date, str)


def test_fmp_quote_fx_price_invalid_symbol(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.fx_price("INVALID_SYMBOL")


def test_fmp_quote_all_live_full_stock_prices(fmp_quote):
    df = fmp_quote.all_live_full_stock_prices()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(df["symbol"][0], str)
    assert isinstance(df["ask_price"][0], np.float64)
    assert isinstance(df["ask_size"][0], np.int64)
    assert isinstance(df["bid_price"][0], np.float64)
    assert isinstance(df["bid_size"][0], np.int64)
    assert isinstance(df["last_sale_price"][0], np.float64)
    assert isinstance(df["last_sale_size"][0], np.int64)
    assert isinstance(df["last_sale_time"][0], pd.Timestamp)
    assert isinstance(df["fmp_last"][0], np.float64)
    assert isinstance(df["last_updated"][0], pd.Timestamp)


def test_fmp_quote_all_live_full_stock_prices_no_results(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.all_live_full_stock_prices() == []


def test_fmp_quote_live_full_stock_price(fmp_quote):
    quote = fmp_quote.live_full_stock_price("AAPL")
    assert isinstance(quote, RealtimeFullPrice)
    assert quote.symbol == "AAPL"
    assert isinstance(quote.symbol, str)
    assert isinstance(quote.ask_price, float)
    assert isinstance(quote.ask_size, int)
    assert isinstance(quote.bid_price, float)
    assert isinstance(quote.bid_size, int)
    assert isinstance(quote.last_sale_price, float)
    assert isinstance(quote.last_sale_size, int)
    assert isinstance(quote.last_sale_time, str)
    assert isinstance(quote.fmp_last, float)
    assert isinstance(quote.last_updated, str)


def test_fmp_quote_live_full_stock_price_invalid_symbol(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.live_full_stock_price("INVALID_SYMBOL")


def test_fmp_quote_last_crypto(fmp_quote):
    quote = fmp_quote.last_crypto("BTCUSD")
    assert isinstance(quote, CryptoQuote)
    assert quote.symbol == "BTCUSD"
    assert isinstance(quote.symbol, str)
    assert isinstance(quote.price, float)
    assert isinstance(quote.size, float)
    assert isinstance(quote.timestamp, str)


def test_fmp_quote_last_crypto_invalid_symbol(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.last_crypto("INVALID_SYMBOL")


def test_fmp_quote_last_forex(fmp_quote):
    quote = fmp_quote.last_forex("EURUSD")
    assert isinstance(quote, ForexQuote)
    assert quote.symbol == "EURUSD"
    assert isinstance(quote.symbol, str)
    assert isinstance(quote.bid, float)
    assert isinstance(quote.ask, float)
    assert isinstance(quote.timestamp, str)


def test_fmp_quote_last_forex_invalid_symbol(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.last_forex("INVALID_SYMBOL")


def test_fmp_quote_batch_trade(fmp_quote):
    df = fmp_quote.batch_trade(["AAPL", "MSFT"])
    assert isinstance(df, pd.DataFrame)
    assert isinstance(df["symbol"][0], str)
    assert isinstance(df["price"][0], np.float64)
    assert isinstance(df["size"][0], np.int64)
    assert isinstance(df["timestamp"][0], pd.Timestamp)


def test_fmp_quote_batch_trade_not_list(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.batch_trade("AAPL")


def test_fmp_quote_batch_trade_invalid_symbol(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.batch_trade(["INVAILD_SYMBOL"])


def test_fmp_quote_batch_quote(fmp_quote):
    df = fmp_quote.batch_quote(["AAPL", "MSFT"])
    assert isinstance(df, pd.DataFrame)
    assert isinstance(df["symbol"][0], str)
    assert isinstance(df["ask"][0], np.float64)
    assert isinstance(df["bid"][0], np.float64)
    assert isinstance(df["asize"][0], np.int64)
    assert isinstance(df["bsize"][0], np.int64)
    assert isinstance(df["timestamp"][0], pd.Timestamp)


def test_fmp_quote_batch_quote_not_list(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.batch_quote("AAPL")


def test_fmp_quote_batch_quote_invalid_symbol(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.batch_quote(["INVALID_SYMBOL"])


def test_fmp_quote_aftermarket_quote(fmp_quote):
    aftermarket_quote = fmp_quote.aftermarket_quote("AAPL")
    assert isinstance(aftermarket_quote, AftermarketQuote)
    assert isinstance(aftermarket_quote.symbol, str)
    assert isinstance(aftermarket_quote.ask, float)
    assert isinstance(aftermarket_quote.asize, int)
    assert isinstance(aftermarket_quote.bid, float)
    assert isinstance(aftermarket_quote.bsize, int)
    assert isinstance(aftermarket_quote.timestamp, str)


def test_fmp_quote_aftermarket_quote_invalid_symbol(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.aftermarket_quote("INVALID_SYMBOL")


def test_fmp_quote_aftermarket_trade(fmp_quote):
    aftermarket_trade = fmp_quote.aftermarket_trade("AAPL")
    assert isinstance(aftermarket_trade, AftermarketTrade)
    assert isinstance(aftermarket_trade.symbol, str)
    assert isinstance(aftermarket_trade.price, float)
    assert isinstance(aftermarket_trade.size, int)
    assert isinstance(aftermarket_trade.timestamp, str)


def test_fmp_quote_aftermarket_trade_invalid_symbol(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.aftermarket_trade("INVALID_SYMBOL")


def test_fmp_quote_stock_price_change(fmp_quote):
    price_change = fmp_quote.stock_price_change("AAPL")
    assert isinstance(price_change, PriceChange)
    assert isinstance(price_change.symbol, str)
    assert isinstance(price_change.day_1, float)
    assert isinstance(price_change.day_5, float)
    assert isinstance(price_change.month_1, float)
    assert isinstance(price_change.month_3, float)
    assert isinstance(price_change.month_6, float)
    assert isinstance(price_change.ytd, float)
    assert isinstance(price_change.year_1, float)
    assert isinstance(price_change.year_3, float)
    assert isinstance(price_change.year_5, float)
    assert isinstance(price_change.year_10, float)
    assert isinstance(price_change.max, float)


def test_fmp_quote_price_change_invalid_symbol(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.stock_price_change("INVALID_SYMBOL")


def test_fmp_quote_exchange_prices(fmp_quote):
    df = fmp_quote.exchange_prices("NASDAQ")
    assert isinstance(df, pd.DataFrame)
    assert "symbol" in df.columns
    assert "price" in df.columns
    assert "volume" in df.columns
    assert isinstance(df["symbol"][0], str)
    assert isinstance(df["price"][0], np.float64)
    assert isinstance(df["volume"][0], np.int64)
    assert isinstance(df["market_cap"][0], np.int64)
    assert isinstance(df["avg_volume"][0], np.int64)
    assert isinstance(df["shares_outstanding"][0], np.int64)
    assert isinstance(df["pe"][0], np.float64)
    assert isinstance(df["eps"][0], np.float64)
    assert isinstance(df["earnings_date"][0], pd.Timestamp)
    assert isinstance(df["datetime"][0], pd.Timestamp)
    assert isinstance(df["change"][0], np.float64)
    assert isinstance(df["change_percentage"][0], np.float64)
    assert isinstance(df["day_high"][0], np.float64)
    assert isinstance(df["day_low"][0], np.float64)
    assert isinstance(df["year_high"][0], np.float64)
    assert isinstance(df["year_low"][0], np.float64)
    assert isinstance(df["price_avg_50"][0], np.float64)
    assert isinstance(df["price_avg_200"][0], np.float64)
    assert isinstance(df["exchange"][0], str)
    assert isinstance(df["open"][0], np.float64)
    assert isinstance(df["previous_close"][0], np.float64)
    assert isinstance(df["name"][0], str)


def test_fmp_quote_exchange_prices_invalid_exchange(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.exchange_prices("INVALID_EXCHANGE")


def test_fmp_quote_otc_quote(fmp_quote):
    quote = fmp_quote.otc_quote("AAPL")
    assert isinstance(quote, OtcQuote)
    assert quote.symbol == "AAPL"
    assert isinstance(quote.symbol, str)
    assert isinstance(quote.prev_close, float)
    assert isinstance(quote.volume, int)
    assert isinstance(quote.high, float)
    assert isinstance(quote.low, float)
    assert isinstance(quote.open, float)
    assert isinstance(quote.last_sale_price, float)
    assert isinstance(quote.fmp_last, float)
    assert isinstance(quote.last_updated, str)


def test_fmp_quote_otc_quote_invalid_symbol(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.otc_quote("INVALID_SYMBOL")


def test_fmp_quote_simple_quote(fmp_quote):
    quote = fmp_quote.simple_quote("AAPL")
    assert isinstance(quote, SimpleQuote)
    assert quote.symbol == "AAPL"
    assert isinstance(quote.symbol, str)
    assert isinstance(quote.price, float)
    assert isinstance(quote.volume, int)


def test_fmp_quote_simple_quote_invalid_symbol(fmp_quote):
    with pytest.raises(ValueError):
        fmp_quote.simple_quote("INVALID_SYMBOL")


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
