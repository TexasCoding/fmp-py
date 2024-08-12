import pandas as pd
import pytest
from fmp_py.fmp_chart_data import FmpChartData


@pytest.fixture
def fmp():
    return FmpChartData(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")


def test_fmp_chart_data_init(fmp):
    assert isinstance(fmp, FmpChartData)


def test_fmp_chart_data_return_chart(fmp):
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "close" in fmp_chart.columns
    assert "volume" in fmp_chart.columns
    assert "open" in fmp_chart.columns
    assert "high" in fmp_chart.columns
    assert "low" in fmp_chart.columns


def test_fmp_chart_data_nvi(fmp):
    fmp.nvi()
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "nvi" in fmp_chart.columns


def test_fmp_chart_data_sma(fmp):
    fmp.sma(14)
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "sma14" in fmp_chart.columns


def test_fmp_chart_data_ema(fmp):
    fmp.ema(14)
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "ema14" in fmp_chart.columns


def test_fmp_chart_data_rsi(fmp):
    fmp.rsi(14)
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "rsi14" in fmp_chart.columns


def test_fmp_chart_data_vwap(fmp):
    fmp.vwap()
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "vwap" in fmp_chart.columns


def test_fmp_chart_data_bb(fmp):
    fmp.bb(20, 2)
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "bb_hband" in fmp_chart.columns
    assert "bb_lband" in fmp_chart.columns
    assert "bb_mband" in fmp_chart.columns
    assert "bb_wband" in fmp_chart.columns
    assert "bb_pband" in fmp_chart.columns
    assert "bb_hband_ind" in fmp_chart.columns
    assert "bb_lband_ind" in fmp_chart.columns


def test_fmp_chart_data_mfi(fmp):
    fmp.mfi(14)
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "mfi14" in fmp_chart.columns


def test_fmp_chart_data_ao(fmp):
    fmp.ao()
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "ao" in fmp_chart.columns


def test_fmp_chart_data_wr(fmp):
    fmp.wr(14)
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "wr14" in fmp_chart.columns


def test_fmp_chart_data_uo(fmp):
    fmp.uo()
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "uo" in fmp_chart.columns


def test_fmp_chart_data_tsi(fmp):
    fmp.tsi(25, 13)
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "tsi" in fmp_chart.columns


def test_fmp_chart_data_stoch(fmp):
    fmp.stoch(14)
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "stoch14" in fmp_chart.columns
    assert "stoch14_sig" in fmp_chart.columns


def test_fmp_chart_data_srsi(fmp):
    fmp.srsi(14)
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "srsi14" in fmp_chart.columns
    assert "srsi14_d" in fmp_chart.columns
    assert "srsi14_k" in fmp_chart.columns


def test_fmp_chart_data_roc(fmp):
    fmp.roc(12)
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "roc12" in fmp_chart.columns


def test_fmp_chart_data_kama(fmp):
    fmp.kama(10)
    fmp_chart = fmp.return_chart()
    assert isinstance(fmp_chart, pd.DataFrame)
    assert "kama10" in fmp_chart.columns
