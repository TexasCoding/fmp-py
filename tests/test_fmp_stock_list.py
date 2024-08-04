import numpy as np
import pandas as pd
import pytest

from fmp_py.fmp_stock_list import FmpStockList


@pytest.fixture
def fmp_stock_list():
    return FmpStockList()


def test_fmp_stock_list_init(fmp_stock_list):
    assert isinstance(fmp_stock_list, FmpStockList)


def test_fmp_stock_list_available_indexes(fmp_stock_list):
    available_indexes = fmp_stock_list.available_indexes()
    assert isinstance(available_indexes, pd.DataFrame)
    assert isinstance(available_indexes.iloc[0]["symbol"], str)
    assert isinstance(available_indexes.iloc[0]["name"], str)
    assert isinstance(available_indexes.iloc[0]["currency"], str)
    assert isinstance(available_indexes.iloc[0]["stock_exchange"], str)
    assert isinstance(available_indexes.iloc[0]["exchange_short_name"], str)


def test_fmp_stock_list_available_indexes_no_data(fmp_stock_list):
    with pytest.raises(ValueError):
        fmp_stock_list.available_indexes() == []


def test_fmp_stock_list_exchange_symbols(fmp_stock_list):
    exchange_symbols = fmp_stock_list.exchange_symbols("NASDAQ")
    assert isinstance(exchange_symbols, pd.DataFrame)
    assert isinstance(exchange_symbols.iloc[0]["symbol"], str)
    assert isinstance(exchange_symbols.iloc[0]["name"], str)
    assert isinstance(exchange_symbols.iloc[0]["exchange"], str)
    assert isinstance(exchange_symbols.iloc[0]["price"], np.float64)
    assert isinstance(exchange_symbols.iloc[0]["change_percentage"], np.float64)
    assert isinstance(exchange_symbols.iloc[0]["change"], np.float64)
    assert isinstance(exchange_symbols.iloc[0]["day_low"], np.float64)
    assert isinstance(exchange_symbols.iloc[0]["day_high"], np.float64)
    assert isinstance(exchange_symbols.iloc[0]["year_high"], np.float64)
    assert isinstance(exchange_symbols.iloc[0]["year_low"], np.float64)
    assert isinstance(exchange_symbols.iloc[0]["market_cap"], np.int64)
    assert isinstance(exchange_symbols.iloc[0]["price_avg_50"], np.float64)
    assert isinstance(exchange_symbols.iloc[0]["price_avg_200"], np.float64)
    assert isinstance(exchange_symbols.iloc[0]["volume"], np.int64)
    assert isinstance(exchange_symbols.iloc[0]["avg_volume"], np.int64)
    assert isinstance(exchange_symbols.iloc[0]["open"], np.float64)
    assert isinstance(exchange_symbols.iloc[0]["previous_close"], np.float64)
    assert isinstance(exchange_symbols.iloc[0]["eps"], np.float64)
    assert isinstance(exchange_symbols.iloc[0]["pe"], np.float64)
    assert isinstance(exchange_symbols.iloc[0]["earnings_announcement"], pd.Timestamp)
    assert isinstance(exchange_symbols.iloc[0]["shares_outstanding"], np.float64)
    assert isinstance(exchange_symbols.iloc[0]["datetime"], pd.Timestamp)


def test_fmp_stock_list_exchange_symbols_no_data(fmp_stock_list):
    with pytest.raises(ValueError):
        fmp_stock_list.exchange_symbols("NASDAQ") == []


def test_fmp_stock_list_symbol_changes(fmp_stock_list):
    symbol_changes = fmp_stock_list.symbol_changes()
    assert isinstance(symbol_changes, pd.DataFrame)
    assert isinstance(symbol_changes.iloc[0]["date"], pd.Timestamp)
    assert isinstance(symbol_changes.iloc[0]["name"], str)
    assert isinstance(symbol_changes.iloc[0]["old_symbol"], str)
    assert isinstance(symbol_changes.iloc[0]["new_symbol"], str)


def test_fmp_stock_list_symbol_changes_no_data(fmp_stock_list):
    with pytest.raises(ValueError):
        fmp_stock_list.symbol_changes() == []


def test_fmp_stock_list_euronext_symbols(fmp_stock_list):
    euronext_symbols = fmp_stock_list.euronext_symbols()
    assert isinstance(euronext_symbols, pd.DataFrame)
    assert isinstance(euronext_symbols.iloc[0]["symbol"], str)
    assert isinstance(euronext_symbols.iloc[0]["name"], str)
    assert isinstance(euronext_symbols.iloc[0]["currency"], str)
    assert isinstance(euronext_symbols.iloc[0]["stock_exchange"], str)
    assert isinstance(euronext_symbols.iloc[0]["exchange_short_name"], str)


def test_fmp_stock_list_euronext_symbols_no_data(fmp_stock_list):
    with pytest.raises(ValueError):
        fmp_stock_list.euronext_symbols() == []


def test_fmp_stock_list_cik_list(fmp_stock_list):
    cik_list = fmp_stock_list.cik_list()
    assert isinstance(cik_list, pd.DataFrame)
    assert isinstance(cik_list.iloc[0]["cik"], str)
    assert isinstance(cik_list.iloc[0]["name"], str)


def test_fmp_stock_list_cik_list_no_data(fmp_stock_list):
    with pytest.raises(ValueError):
        fmp_stock_list.cik_list() == []


def test_fmp_stock_list_commitment_of_traders_report(fmp_stock_list):
    cot_list = fmp_stock_list.commitment_of_traders_report()
    assert isinstance(cot_list, pd.DataFrame)
    assert isinstance(cot_list.iloc[0]["trading_symbol"], str)
    assert isinstance(cot_list.iloc[0]["short_name"], str)


def test_fmp_stock_list_commitment_of_traders_report_no_data(fmp_stock_list):
    with pytest.raises(ValueError):
        fmp_stock_list.commitment_of_traders_report() == []


def test_fmp_stock_list_tradable_stocks_search(fmp_stock_list):
    tradable_stocks_list = fmp_stock_list.tradable_stocks_search()
    assert isinstance(tradable_stocks_list, pd.DataFrame)
    assert isinstance(tradable_stocks_list.iloc[0]["symbol"], str)
    assert isinstance(tradable_stocks_list.iloc[0]["name"], str)
    assert isinstance(tradable_stocks_list.iloc[0]["price"], float)
    assert isinstance(tradable_stocks_list.iloc[0]["exchange"], str)
    assert isinstance(tradable_stocks_list.iloc[0]["exchange_short_name"], str)


def test_fmp_stock_list_tradable_stocks_search_no_data(fmp_stock_list):
    with pytest.raises(ValueError):
        fmp_stock_list.tradable_stocks_search() == []


def test_fmp_stock_list_statement_symbols_list(fmp_stock_list):
    statement_symbols_list = fmp_stock_list.statement_symbols_list()
    assert isinstance(statement_symbols_list, list)
    assert isinstance(statement_symbols_list[0], str)


def test_fmp_stock_list_exchange_traded_fund_search(fmp_stock_list):
    etf_list = fmp_stock_list.exchange_traded_fund_search()
    assert isinstance(etf_list, pd.DataFrame)
    assert isinstance(etf_list.iloc[0]["symbol"], str)
    assert isinstance(etf_list.iloc[0]["name"], str)
    assert isinstance(etf_list.iloc[0]["price"], float)
    assert isinstance(etf_list.iloc[0]["exchange"], str)
    assert isinstance(etf_list.iloc[0]["exchange_short_name"], str)
    assert isinstance(etf_list.iloc[0]["type"], str)


def test_fmp_stock_list_exchange_traded_fund_search_no_data(fmp_stock_list):
    with pytest.raises(ValueError):
        fmp_stock_list.exchange_traded_fund_search() == []


def test_fmp_stock_list_stock_list(fmp_stock_list):
    stock_list = fmp_stock_list.stock_list()
    assert isinstance(stock_list, pd.DataFrame)
    assert isinstance(stock_list.iloc[0]["symbol"], str)
    assert isinstance(stock_list.iloc[0]["name"], str)
    assert isinstance(stock_list.iloc[0]["exchange"], str)
    assert isinstance(stock_list.iloc[0]["price"], float)
    assert isinstance(stock_list.iloc[0]["exchange_short_name"], str)
    assert isinstance(stock_list.iloc[0]["type"], str)


def test_fmp_stock_list_stock_list_no_data(fmp_stock_list):
    with pytest.raises(ValueError):
        fmp_stock_list.stock_list() == []
