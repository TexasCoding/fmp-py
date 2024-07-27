import pandas as pd
from fmp_py.fmp_base import FmpBase
import os
from dotenv import load_dotenv

from fmp_py.fmp_historical_data import FmpHistoricalData
from ta.trend import SMAIndicator, EMAIndicator, WMAIndicator, ADXIndicator
from ta.momentum import RSIIndicator
from ta.volume import VolumeWeightedAveragePrice, MFIIndicator, AccDistIndexIndicator
from ta.volatility import AverageTrueRange, BollingerBands

load_dotenv()


class FmpCharts(FmpBase):
    def __init__(
        self,
        symbol: str,
        from_date: str,
        to_date: str,
        interval: str = "1day",
        api_key: str = os.getenv("FMP_API_KEY"),
    ) -> None:
        super().__init__(api_key)
        self.chart = FmpHistoricalData().intraday_history(
            symbol=symbol, interval=interval, from_date=from_date, to_date=to_date
        )

    ##########################################################################
    ########################### VOLUME INDICATORS ############################
    ##########################################################################

    #################################
    # Accumulated Distribution Index
    #################################
    def adi(self, period: int = 14) -> None:
        """
        Calculates the Accumulation/Distribution Index (ADI) for the given period.

        Args:
            period (int, optional): The number of periods to consider. Defaults to 14.

        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.adi(14)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart[f"adi{period}"] = (
            AccDistIndexIndicator(
                high=chart["high"],
                low=chart["low"],
                close=chart["close"],
                volume=chart["volume"],
                fillna=True,
            ).acc_dist_index()
        ).astype(int)
        self.chart = chart

    #################################
    # Money Flow Index
    #################################
    def mfi(self, period: int = 14) -> None:
        """
        Calculates the Money Flow Index (MFI) for the given period.

        Parameters:
            period (int): The number of periods to consider when calculating the MFI. Default is 14.

        Returns:
            None

        Notes:
            The Money Flow Index (MFI) is a momentum oscillator that measures the strength and
            direction of money flowing in and out of a security. It uses price and volume data
            to identify overbought or oversold conditions in the market.

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.mfi(14)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart[f"mfi{period}"] = (
            MFIIndicator(
                high=chart["high"],
                low=chart["low"],
                close=chart["close"],
                volume=chart["volume"],
                window=period,
                fillna=True,
            )
            .money_flow_index()
            .round(2)
        )
        self.chart = chart

    #################################
    # Volume Weighted Average Price
    #################################
    def vwap(self) -> None:
        """
        Calculates the Volume Weighted Average Price (VWAP) for the given chart data.

        The VWAP is a trading indicator that gives the average price at which a security has traded throughout the day,
        weighted by the volume of each trade. It is often used by traders to determine the fair value of a security
        and to identify potential buying or selling opportunities.

        This method calculates the VWAP for the chart data and adds it as a new column named 'vwap' to the chart DataFrame.

        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.vwap()
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart["vwap"] = (
            VolumeWeightedAveragePrice(
                high=chart["high"],
                low=chart["low"],
                close=chart["close"],
                volume=chart["volume"],
                fillna=True,
            )
            .volume_weighted_average_price()
            .round(2)
        ).astype(float)
        self.chart = chart

    ##########################################################################
    ######################## VOLATILITY INDICATORS ###########################
    ##########################################################################

    #####################################
    # Bollinger Bands
    #####################################
    def bb(self, period: int = 20, std: int = 2) -> None:
        """
        Calculates Bollinger Bands and related indicators for the given period and standard deviation.

        Args:
            period (int): The number of periods to consider for calculating the Bollinger Bands. Default is 20.
            std (int): The number of standard deviations to use for the Bollinger Bands. Default is 2.

        Returns:
            None

        Modifies:
            Updates the 'chart' attribute of the object with the calculated Bollinger Bands and related indicators.

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.bb(20, 2)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()

        chart[f"bb_h{period}"] = (
            BollingerBands(
                close=chart["close"],
                window=period,
                window_dev=std,
                fillna=True,
            )
            .bollinger_hband()
            .round(2)
        ).astype(float)

        chart[f"bb_m{period}"] = (
            BollingerBands(
                close=chart["close"],
                window=period,
                window_dev=std,
                fillna=True,
            )
            .bollinger_mavg()
            .round(2)
        ).astype(float)

        chart[f"bb_l{period}"] = (
            BollingerBands(
                close=chart["close"],
                window=period,
                window_dev=std,
                fillna=True,
            )
            .bollinger_lband()
            .round(2)
        ).astype(float)

        chart[f"bb_h{period}_ind"] = (
            BollingerBands(
                close=chart["close"],
                window=period,
                window_dev=std,
                fillna=True,
            )
            .bollinger_hband_indicator()
            .astype(int)
        )

        chart[f"bb_l{period}_ind"] = (
            BollingerBands(
                close=chart["close"],
                window=period,
                window_dev=std,
                fillna=True,
            )
            .bollinger_lband_indicator()
            .astype(int)
        )

        chart[f"bb_w{period}"] = (
            BollingerBands(
                close=chart["close"],
                window=period,
                window_dev=std,
                fillna=True,
            )
            .bollinger_wband()
            .round(2)
        ).astype(float)

        chart[f"bb_p{period}"] = (
            BollingerBands(
                close=chart["close"],
                window=period,
                window_dev=std,
                fillna=True,
            )
            .bollinger_pband()
            .round(2)
        ).astype(float)

        self.chart = chart

    #####################################
    # Average True Range
    #####################################
    def atr(self, period: int = 14) -> None:
        """
        Calculates the Average True Range (ATR) for the given period.

        Parameters:
            period (int): The number of periods to consider for calculating the ATR. Default is 14.

        Returns:
            None

        Notes:
            - The ATR is a volatility indicator that measures the average range between the high and low prices over a specified period.
            - The ATR is commonly used to determine the volatility of an asset and to set stop-loss and take-profit levels.

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.atr(14)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart[f"atr{period}"] = (
            AverageTrueRange(
                high=chart["high"],
                low=chart["low"],
                close=chart["close"],
                window=period,
                fillna=True,
            )
            .average_true_range()
            .round(2)
        ).astype(float)
        self.chart = chart

    ##########################################################################
    ########################## TREND INDICATORS ##############################
    ##########################################################################

    #####################################
    # Waddah Attar Explosion
    #####################################
    def waddah_attar_explosion(
        self,
        n_fast: int = 20,
        n_slow: int = 40,
        channel_period: int = 20,
        mul: float = 2.0,
        sensitivity: int = 150,
    ) -> None:
        """
        Calculate Waddah Attar Explosion indicator.
        Args:
            df (pd.DataFrame): DataFrame containing historical data with columns 'close', 'high', 'low'.
            n_fast (int): Period for the fast EMA.
            n_slow (int): Period for the slow EMA.
            channel_period (int): Period for calculating the Bollinger Bands.
            mul (float): Multiplier for the Bollinger Bands.
            sensitivity (int): Sensitivity factor for explosion value.
        Returns:
            pd.DataFrame: DataFrame containing the Waddah Attar Explosion values.

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.waddah_attar_explosion(n_fast=20, n_slow=40, channel_period=20, mul=2.0, sensitivity=150)
            >>> print(fmp.return_chart())
        """
        df = self.chart.copy()

        # Calculate the MACD
        def calc_macd(close: pd.Series, n_fast: int, n_slow: int) -> pd.Series:
            fast_ma = EMAIndicator(close=close, window=n_fast).ema_indicator()
            slow_ma = EMAIndicator(close=close, window=n_slow).ema_indicator()
            return fast_ma - slow_ma

        # Calculate the Bollinger Bands
        def calc_bb_bands(close: pd.Series, channel_period: int, mul: float):
            bb = BollingerBands(close=close, window=channel_period, window_dev=mul)
            return bb.bollinger_hband(), bb.bollinger_lband()

        macd_diff = calc_macd(df["close"], n_fast, n_slow) - calc_macd(
            df["close"].shift(1), n_fast, n_slow
        )
        explosion = macd_diff * sensitivity

        bb_upper, bb_lower = calc_bb_bands(df["close"], channel_period, mul)
        explosion_band = bb_upper - bb_lower

        df["wae_value"] = explosion
        df["wae_explosion"] = explosion_band

        # Fill NaNs and round the values
        df["wae_value"] = df["wae_value"].fillna(df["wae_value"].mean()).round(2)
        df["wae_explosion"] = (
            df["wae_explosion"].fillna(df["wae_explosion"].mean()).round(2)
        )

        # Calculate the uptrend
        df["wae_uptrend"] = (
            (df["wae_value"] > df["wae_value"].shift(1))
            & (df["wae_value"] > 0)
            & (df["wae_value"] > df["wae_explosion"])
        ).astype(int)

        self.chart = df

    #####################################
    # Average Directional Movement Index
    #####################################
    def adx(self, period: int = 14) -> None:
        """
        Calculates the Average Directional Index (ADX) for the given period.

        Parameters:
        - period (int): The number of periods to consider when calculating the ADX. Default is 14.

        Returns:
        None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.adx(14)
            >>> print(fmp.return_chart())
        """

        chart = self.chart.copy()
        chart[f"adx{period}"] = (
            ADXIndicator(
                high=chart["high"],
                low=chart["low"],
                close=chart["close"],
                window=period,
                fillna=True,
            )
            .adx()
            .round(2)
        ).astype(float)

        chart[f"adx{period}_neg"] = (
            ADXIndicator(
                high=chart["high"],
                low=chart["low"],
                close=chart["close"],
                window=period,
                fillna=True,
            )
            .adx_neg()
            .round(2)
        ).astype(float)

        chart[f"adx{period}_pos"] = (
            ADXIndicator(
                high=chart["high"],
                low=chart["low"],
                close=chart["close"],
                window=period,
                fillna=True,
            )
            .adx_pos()
            .round(2)
        ).astype(float)

        self.chart = chart

    #####################################
    # Weighted Moving Average
    #####################################
    def wma(self, period: int = 14) -> None:
        """
        Calculates the Weighted Moving Average (WMA) for the given period.

        Args:
            period (int): The number of periods to consider for the WMA calculation. Default is 14.

        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.wma(14)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart[f"wma{period}"] = (
            WMAIndicator(
                close=chart["close"],
                window=period,
                fillna=True,
            )
            .wma()
            .round(2)
        )

        self.chart = chart

    #####################################
    # Simple Moving Average
    #####################################
    def sma(self, period: int = 14) -> None:
        """
        Calculates the Simple Moving Average (SMA) for the given period.

        Args:
            period (int): The number of periods to consider for calculating the SMA. Default is 14.

        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.sma(14)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart[f"sma{period}"] = (
            SMAIndicator(
                close=chart["close"],
                window=period,
                fillna=True,
            )
            .sma_indicator()
            .round(2)
        ).astype(float)
        self.chart = chart

    #####################################
    # Exponential Moving Average
    #####################################
    def ema(self, period: int = 14) -> None:
        """
        Calculates the Exponential Moving Average (EMA) for the given period.

        Args:
            period (int): The number of periods to consider for the EMA calculation. Default is 14.

        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.ema(14)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart[f"ema{period}"] = (
            EMAIndicator(close=chart["close"], window=period, fillna=True)
            .ema_indicator()
            .round(2)
        ).astype(float)
        self.chart = chart

    ##########################################################################
    ########################## TREND INDICATORS ##############################
    ##########################################################################

    #####################################
    # Relative Strength Index
    #####################################
    def rsi(self, period: int = 14) -> None:
        """
        Calculates the Relative Strength Index (RSI) for the given period.

        Parameters:
            period (int): The number of periods to consider when calculating RSI. Default is 14.

        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.rsi(14)
            >>> print(fmp.return_chart())
        """
        change = self.chart.copy()
        change[f"rsi{period}"] = (
            RSIIndicator(close=change["close"], window=period, fillna=True)
            .rsi()
            .round(2)
        ).astype(float)
        self.chart = change

    def return_chart(self) -> pd.DataFrame:
        return self.chart
