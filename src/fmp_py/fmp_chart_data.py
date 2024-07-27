import pandas as pd
from fmp_py.fmp_base import FmpBase
import os
from dotenv import load_dotenv

from fmp_py.fmp_historical_data import FmpHistoricalData
from ta.trend import SMAIndicator, EMAIndicator, WMAIndicator, ADXIndicator
from ta.momentum import RSIIndicator
from ta.volume import (
    VolumeWeightedAveragePrice,
    MFIIndicator,
    AccDistIndexIndicator,
    OnBalanceVolumeIndicator,
    ChaikinMoneyFlowIndicator,
    ForceIndexIndicator,
    EaseOfMovementIndicator,
    VolumePriceTrendIndicator,
    NegativeVolumeIndexIndicator,
)
from ta.volatility import AverageTrueRange, BollingerBands

load_dotenv()


class FmpChartData(FmpBase):
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

    ####################################
    # Negative Volume Index Indicator
    ####################################
    def nvi(self) -> None:
        """
        Calculates the Negative Volume Index (NVI) for the chart data.

        The Negative Volume Index (NVI) is a technical indicator that uses volume to predict
        changes in stock prices. It is calculated by summing the percentage changes in price
        on days with declining volume and subtracting the sum of the percentage changes on
        days with increasing volume.

        This method modifies the `chart` attribute of the object by adding a new column
        called "nvi" that contains the NVI values.

        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.nvi()
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart["nvi"] = (
            NegativeVolumeIndexIndicator(
                close=chart["close"], volume=chart["volume"], fillna=True
            )
            .negative_volume_index()
            .round(2)
            .astype(float)
        )
        self.chart = chart

    ####################################
    # Volume Price Trend Indicator
    ####################################
    def vpt(self) -> None:
        """
        Calculates the Volume Price Trend (VPT) indicator for the chart data.

        The Volume Price Trend (VPT) indicator measures the strength of a price trend by
        analyzing the relationship between volume and price. It is used to identify
        potential reversals or confirm the strength of a trend.

        This method modifies the `chart` attribute of the object by adding a new column
        called "vpt" that contains the calculated VPT values.

        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.vpt()
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart["vpt"] = (
            VolumePriceTrendIndicator(
                close=chart["close"],
                volume=chart["volume"],
                fillna=True,
            ).volume_price_trend()
        ).astype(int)
        self.chart = chart

    ####################################
    # SMA Ease of Movement Indicator
    ####################################
    def sma_eom(self, period: int = 14) -> None:
        """
        Calculates the Simple Moving Average (SMA) of the Ease of Movement (EOM) indicator.

        Args:
            period (int): The number of periods to consider for calculating the SMA. Default is 14.

        Returns:
            None

        """
        chart = self.chart.copy()
        chart[f"sma_eom{period}"] = (
            EaseOfMovementIndicator(
                high=chart["high"],
                low=chart["low"],
                volume=chart["volume"],
                window=period,
                fillna=True,
            )
            .sma_ease_of_movement()
            .round(2)
            .astype(float)
        )

        self.chart = chart

    ##################################
    # Ease of Movement Indicator
    ##################################
    def eom(self, period: int = 14) -> None:
        """
        Calculates the Ease of Movement (EOM) indicator for the given chart data.

        Parameters:
            period (int): The number of periods to consider for the EOM calculation. Default is 14.

        Returns:
            None

        Notes:
            - The EOM indicator measures the relationship between price change and volume.
            - It helps identify potential price reversals and divergences.

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.eom(14)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart[f"eom{period}"] = (
            EaseOfMovementIndicator(
                high=chart["high"],
                low=chart["low"],
                volume=chart["volume"],
                window=period,
                fillna=True,
            )
            .ease_of_movement()
            .round(2)
            .astype(float)
        )

        self.chart = chart

    ##################################
    # Force Index Indicator
    ##################################
    def fi(self, period: int = 13) -> None:
        """
        Calculates and adds the Force Index (FI) to the chart data.

        The Force Index is a technical indicator that measures the force behind price movements based on the combination of
        price change and trading volume. It helps identify strong trends and potential reversals.

        Args:
            period (int, optional): The period used to calculate the Force Index. Defaults to 13.

        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.fi(13)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart[f"fi{period}"] = (
            ForceIndexIndicator(
                close=chart["close"], volume=chart["volume"], window=period
            )
            .force_index()
            .round(2)
        ).astype(float)
        self.chart = chart

    #################################
    # Chaikin Money Flow Indicator
    #################################
    def cmf(self, period: int = 20) -> None:
        """
        Calculates the Chaikin Money Flow (CMF) indicator for the chart data.

        Args:
            period (int): The number of periods to consider for the CMF calculation. Default is 20.

        Returns:
            None. The CMF values are added as a new column 'cmf' to the chart data.

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.cmf()
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart["cmf"] = (
            ChaikinMoneyFlowIndicator(
                high=chart["high"],
                low=chart["low"],
                close=chart["close"],
                volume=chart["volume"],
                window=period,
                fillna=True,
            )
            .chaikin_money_flow()
            .round(2)
        ).astype(float)

        self.chart = chart

    #################################
    # On Balance Volume Indicator
    #################################
    def obv(self) -> None:
        """
        Calculates the On-Balance Volume (OBV) indicator for the chart data.

        The On-Balance Volume (OBV) indicator measures the cumulative buying and selling pressure based on the volume of trades.
        It is used to identify the strength of a trend and potential reversals.

        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.obv()
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart["obv"] = (
            OnBalanceVolumeIndicator(
                close=chart["close"],
                volume=chart["volume"],
                fillna=True,
            ).on_balance_volume()
        ).astype(int)

        self.chart = chart

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
            .astype(float)
        )

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
