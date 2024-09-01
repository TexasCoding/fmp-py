import pandas as pd
from fmp_py.fmp_base import FmpBase
import os
from dotenv import load_dotenv

from fmp_py.fmp_historical_data import FmpHistoricalData
from ta.trend import (
    SMAIndicator,
    EMAIndicator,
    WMAIndicator,
    ADXIndicator,
    MACD,
    VortexIndicator,
    TRIXIndicator,
    MassIndex,
    CCIIndicator,
    DPOIndicator,
    KSTIndicator,
    # IchimokuIndicator,
    # PSARIndicator,
    # STCIndicator,
    # AroonIndicator,
)
from ta.momentum import (
    RSIIndicator,
    StochRSIIndicator,
    StochasticOscillator,
    TSIIndicator,
    UltimateOscillator,
    WilliamsRIndicator,
    AwesomeOscillatorIndicator,
    KAMAIndicator,
    ROCIndicator,
    # PercentagePriceOscillator,
    # PercentageVolumeOscillator,
)
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
from ta.volatility import (
    AverageTrueRange,
    BollingerBands,
    # KeltnerChannel,
    # DonchianChannel,
    # UlcerIndex,
)

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

        # Bollinger Channel High Band
        chart["bb_hband"] = (
            BollingerBands(
                close=chart["close"],
                window=period,
                window_dev=std,
                fillna=True,
            )
            .bollinger_hband()
            .round(2)
        ).astype(float)

        # Bollinger Channel Middle Band
        chart["bb_mband"] = (
            BollingerBands(
                close=chart["close"],
                window=period,
                window_dev=std,
                fillna=True,
            )
            .bollinger_mavg()
            .round(2)
        ).astype(float)

        # Bollinger Channel Low Band
        chart["bb_lband"] = (
            BollingerBands(
                close=chart["close"],
                window=period,
                window_dev=std,
                fillna=True,
            )
            .bollinger_lband()
            .round(2)
        ).astype(float)

        # Bollinger Channel Indicator Crossing High Band (binary).
        # It returns 1, if close is higher than bollinger_hband. Else, it returns 0.
        chart["bb_hband_ind"] = (
            BollingerBands(
                close=chart["close"],
                window=period,
                window_dev=std,
                fillna=True,
            )
            .bollinger_hband_indicator()
            .astype(int)
        )

        # Bollinger Channel Indicator Crossing Low Band (binary).
        # It returns 1, if close is lower than bollinger_lband. Else, it returns 0.
        chart["bb_lband_ind"] = (
            BollingerBands(
                close=chart["close"],
                window=period,
                window_dev=std,
                fillna=True,
            )
            .bollinger_lband_indicator()
            .astype(int)
        )

        # Bollinger Channel Band Width
        chart["bb_wband"] = (
            BollingerBands(
                close=chart["close"],
                window=period,
                window_dev=std,
                fillna=True,
            )
            .bollinger_wband()
            .round(2)
        ).astype(float)

        # Bollinger Channel Percentage Band
        chart["bb_pband"] = (
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
    # BXTRender Indicator
    #####################################
    def bxtrender(
        self,
        short_p1: int = 5,
        short_p2: int = 20,
        short_p3: int = 15,
        long_p1: int = 20,
        long_p2: int = 15,
    ) -> None:
        """
        Calculates the BXTrend indicator for the given chart data.

        Parameters:
            short_p1 (int): The window size for the first short-term EMA calculation. Default is 5.
            short_p2 (int): The window size for the second short-term EMA calculation. Default is 20.
            short_p3 (int): The window size for the RSI calculation. Default is 15.
            long_p1 (int): The window size for the long-term EMA calculation. Default is 20.
            long_p2 (int): The window size for the RSI calculation. Default is 15.

        Returns:
            None
        """
        chart = self.chart.copy()
        chart["short_term_xtrender"] = (
            RSIIndicator(
                (
                    EMAIndicator(close=chart["close"], window=short_p1).ema_indicator()
                    - EMAIndicator(
                        close=chart["close"], window=short_p2
                    ).ema_indicator()
                ),
                window=short_p3,
            ).rsi()
            - 50
        )

        chart["long_term_xtrender"] = (
            RSIIndicator(
                EMAIndicator(close=chart["close"], window=long_p1).ema_indicator(),
                window=long_p2,
            ).rsi()
            - 50
        )

        def t3(src, length):
            xe1_1 = EMAIndicator(src, length).ema_indicator()
            xe2_1 = EMAIndicator(xe1_1, length).ema_indicator()
            xe3_1 = EMAIndicator(xe2_1, length).ema_indicator()
            xe4_1 = EMAIndicator(xe3_1, length).ema_indicator()
            xe5_1 = EMAIndicator(xe4_1, length).ema_indicator()
            xe6_1 = EMAIndicator(xe5_1, length).ema_indicator()
            b_1 = 0.7
            c1_1 = -b_1 * b_1 * b_1
            c2_1 = 3 * b_1 * b_1 + 3 * b_1 * b_1 * b_1
            c3_1 = -6 * b_1 * b_1 - 3 * b_1 - 3 * b_1 * b_1 * b_1
            c4_1 = 1 + 3 * b_1 + b_1 * b_1 * b_1 + 3 * b_1 * b_1
            return c1_1 * xe6_1 + c2_1 * xe5_1 + c3_1 * xe4_1 + c4_1 * xe3_1

        chart["ma_short_term_trend"] = t3(chart["close"], 5)

        self.chart = chart.dropna()

    #####################################
    # KST Oscillator (KST)
    #####################################
    def kst(
        self,
        roc1: int = 10,
        roc2: int = 15,
        roc3: int = 20,
        roc4: int = 30,
        window1: int = 10,
        window2: int = 10,
        window3: int = 10,
        window4: int = 15,
        nsig: int = 9,
    ) -> None:
        """
        Calculates the Know Sure Thing (KST) indicator and adds it to the chart data.

        Parameters:
        - roc1 (int): Rate of Change (ROC) for the first time period (default: 10)
        - roc2 (int): Rate of Change (ROC) for the second time period (default: 15)
        - roc3 (int): Rate of Change (ROC) for the third time period (default: 20)
        - roc4 (int): Rate of Change (ROC) for the fourth time period (default: 30)
        - window1 (int): Moving average window for the first time period (default: 10)
        - window2 (int): Moving average window for the second time period (default: 10)
        - window3 (int): Moving average window for the third time period (default: 10)
        - window4 (int): Moving average window for the fourth time period (default: 15)
        - nsig (int): Signal line window (default: 9)

        Returns:
        None

        Notes:
            - The KST indicator is a momentum oscillator that measures the strength of a trend.
            - The KST indicator is commonly used to identify overbought and oversold conditions.

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.kst(10, 15, 20, 30, 10, 10, 10, 15, 9)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()

        chart["kst"] = (
            KSTIndicator(
                close=chart["close"],
                roc1=roc1,
                roc2=roc2,
                roc3=roc3,
                roc4=roc4,
                window1=window1,
                window2=window2,
                window3=window3,
                window4=window4,
                nsig=nsig,
                fillna=True,
            )
            .kst()
            .round(2)
            .astype(float)
        )

        chart["kst_sig"] = (
            KSTIndicator(
                close=chart["close"],
                roc1=roc1,
                roc2=roc2,
                roc3=roc3,
                roc4=roc4,
                window1=window1,
                window2=window2,
                window3=window3,
                window4=window4,
                nsig=nsig,
                fillna=True,
            )
            .kst_sig()
            .round(2)
            .astype(float)
        )
        self.chart = chart

    ######################################
    # Detrended Price Oscillator (DPO)
    ######################################
    def dpo(self, period: int = 20) -> None:
        """
        Calculates the Detrended Price Oscillator (DPO) for the given period.

        Parameters:
        - period (int): The number of periods to consider for the calculation. Default is 20.

        Returns:
        None

        Notes:
            - The DPO is a momentum indicator that measures the difference between the close price and the previous close price.
            - The DPO is commonly used to determine the strength of a trend.

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.dpo(20)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart[f"dpo{period}"] = (
            DPOIndicator(
                close=chart["close"],
                window=period,
                fillna=True,
            )
            .dpo()
            .round(2)
            .astype(float)
        )
        self.chart = chart

    ######################################
    # Commodity Channel Index (CCI)
    ######################################
    def cci(self, period: int = 20, constant: float = 0.015) -> None:
        """
        Calculates the Commodity Channel Index (CCI) for the given period and constant.

        Parameters:
            period (int): The number of periods to consider for calculating CCI. Default is 20.
            constant (float): The constant multiplier used in the CCI formula. Default is 0.015.

        Returns:
            None

        Notes:
            - The CCI is a momentum-based oscillator that measures the deviation of an asset's price from its statistical mean.
            - The CCI is used to identify overbought and oversold levels, as well as potential trend reversals.

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.cci(14, 0.015)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart[f"cci{period}"] = (
            CCIIndicator(
                high=chart["high"],
                low=chart["low"],
                close=chart["close"],
                window=period,
                constant=constant,
                fillna=True,
            )
            .cci()
            .round(2)
            .astype(float)
        )

        self.chart = chart

    ######################################
    # Mass Index (MI) Indicator
    ######################################
    def mi(self, period_fast: int = 9, period_slow: int = 25) -> None:
        """
        Calculates the Mass Index (MI) for the chart data.

        The Mass Index is a technical indicator used to identify potential reversals in the market.
        It is calculated based on the high and low prices of the chart data.

        Parameters:
            period_fast (int): The number of periods to use for the fast EMA calculation. Default is 9.
            period_slow (int): The number of periods to use for the slow EMA calculation. Default is 25.

        Returns:
            None

        Notes:
            - The Mass Index is a trend following momentum indicator that uses the high and low price to identify trend reversals based on range expansions.
            - The Mass Index is calculated by using the high and low price to calculate the range of the chart data.
            - The Mass Index is typically used with a 9-day and 25-day EMA.

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.mi(9, 25)
            >>> print(fmp.return_chart())

        """
        chart = self.chart.copy()
        chart["mi"] = (
            MassIndex(
                high=chart["high"],
                low=chart["low"],
                window_slow=period_slow,
                window_fast=period_fast,
                fillna=True,
            )
            .mass_index()
            .round(2)
            .astype(float)
        )

        self.chart = chart

    #####################################
    # Triple Exponential Moving Average
    #####################################
    def trix(self, period: int = 15) -> None:
        """
        Calculate the TRIX (Triple Exponential Moving Average) indicator for the given period.

        Args:
            period (int): The number of periods to consider for the TRIX calculation. Default is 15.

        Returns:
            None

        Notes:
            - The TRIX indicator is a momentum indicator that shows the speed and direction of price changes.
            - The TRIX indicator is commonly used to identify overbought and oversold conditions.
            - The TRIX indicator is a multiplicative indicator, which means that the TRIX value is multiplied by the close price.

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.trix(14)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart[f"trix{period}"] = (
            TRIXIndicator(
                close=chart["close"],
                window=period,
                fillna=True,
            )
            .trix()
            .round(2)
            .astype(float)
        )

        self.chart = chart

    #####################################
    # Vortex Indicator
    #####################################
    def vi(self, period: int = 14) -> None:
        """
        Calculates the Vortex Indicator (VI) for the given period and updates the chart data.

        Parameters:
        - period (int): The number of periods to consider when calculating the VI. Default is 14.

        Returns:
        None

        Example:
        >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
        >>> fmp.vi(14)
        >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart[f"vi{period}"] = (
            VortexIndicator(
                high=chart["high"],
                low=chart["low"],
                close=chart["close"],
                window=period,
                fillna=True,
            )
            .vortex_indicator_diff()
            .round(2)
            .astype(float)
        )
        self.chart = chart

    #####################################
    # MACD
    #####################################
    def macd(self, fast: int = 12, slow: int = 26, signal: int = 9) -> None:
        """
        Calculate the Moving Average Convergence Divergence (MACD) indicators for the chart data.

        Args:
            fast (int): The number of periods for the fast moving average. Default is 12.
            slow (int): The number of periods for the slow moving average. Default is 26.
            signal (int): The number of periods for the signal line. Default is 9.

        Returns:
            None

        This method calculates the MACD, MACD signal line, and MACD histogram (MACD difference) for the chart data.
        The calculated values are added as new columns to the chart DataFrame.

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.macd(12, 26, 9)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart["macd"] = (
            MACD(
                close=chart["close"],
                window_fast=fast,
                window_slow=slow,
                window_sign=signal,
                fillna=True,
            )
            .macd()
            .round(2)
            .astype(float)
        )
        chart["macd_signal"] = (
            MACD(
                close=chart["close"],
                window_fast=fast,
                window_slow=slow,
                window_sign=signal,
                fillna=True,
            )
            .macd_signal()
            .round(2)
            .astype(float)
        )

        chart["macd_diff"] = (
            MACD(
                close=chart["close"],
                window_fast=fast,
                window_slow=slow,
                window_sign=signal,
                fillna=True,
            )
            .macd_diff()
            .round(2)
            .astype(float)
        )

        self.chart = chart

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
    ######################## Momentum INDICATORS #############################
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
        chart = self.chart.copy()
        chart[f"rsi{period}"] = (
            RSIIndicator(close=chart["close"], window=period, fillna=True)
            .rsi()
            .round(2)
        ).astype(float)
        self.chart = chart

    #####################################
    # Stochastic RSI
    #####################################
    def srsi(self, period: int = 14, smooth1: int = 3, smooth2: int = 3) -> None:
        """
        Calculates the Stochastic RSI (Relative Strength Index) for the given period.
        Parameters:
            period (int): The number of periods to consider for the calculation. Default is 14.
            smooth1 (int): The number of periods to use for smoothing the Stochastic RSI. Default is 3.
            smooth2 (int): The number of periods to use for smoothing the Stochastic RSI's signal line. Default is 3.
        Returns:
            None
        """

        chart = self.chart.copy()
        chart[f"srsi{period}"] = (
            StochRSIIndicator(
                close=chart["close"],
                window=period,
                smooth1=smooth1,
                smooth2=smooth2,
                fillna=True,
            )
            .stochrsi()
            .round(2)
        ).astype(float)

        chart[f"srsi{period}_d"] = (
            StochRSIIndicator(
                close=chart["close"],
                window=period,
                smooth1=smooth1,
                smooth2=smooth2,
                fillna=True,
            )
            .stochrsi_d()
            .round(2)
        ).astype(float)

        chart[f"srsi{period}_k"] = (
            StochRSIIndicator(
                close=chart["close"],
                window=period,
                smooth1=smooth1,
                smooth2=smooth2,
                fillna=True,
            )
            .stochrsi_k()
            .round(2)
        ).astype(float)

        self.chart = chart

    #####################################
    # Stochastic Oscillator
    #####################################
    def stoch(self, period: int = 14, smooth: int = 3) -> None:
        """
        Calculates the Stochastic Oscillator for the given period.

        Parameters:
            period (int): The number of periods to consider for the calculation. Default is 14.
            smooth (int): The number of periods to use for smoothing the Stochastic Oscillator. Default is 3.

        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.stoch(14, 3)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart[f"stoch{period}"] = (
            StochasticOscillator(
                high=chart["high"],
                low=chart["low"],
                close=chart["close"],
                window=period,
                smooth_window=smooth,
                fillna=True,
            )
            .stoch()
            .round(2)
        ).astype(float)

        chart[f"stoch{period}_sig"] = (
            StochasticOscillator(
                high=chart["high"],
                low=chart["low"],
                close=chart["close"],
                window=period,
                smooth_window=smooth,
                fillna=True,
            )
            .stoch_signal()
            .round(2)
        ).astype(float)

        self.chart = chart

    #####################################
    # True Strength Index
    #####################################
    def tsi(self, period_slow: int = 25, period_fast: int = 13) -> None:
        """
        Calculates the True Strength Index (TSI) for the given chart data.
        Parameters:
            period_slow (int): The number of periods to use for the slow TSI calculation. Default is 25.
            period_fast (int): The number of periods to use for the fast TSI calculation. Default is 13.
        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.tsi(25, 13)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart["tsi"] = (
            TSIIndicator(
                close=chart["close"],
                window_slow=period_slow,
                window_fast=period_fast,
                fillna=True,
            )
            .tsi()
            .round(2)
        ).astype(float)

        self.chart = chart

    #####################################
    # Ultimate Oscillator
    #####################################
    def uo(
        self,
        period1: int = 7,
        period2: int = 14,
        period3: int = 28,
        weight1: float = 4.0,
        weight2: float = 2.0,
        weight3: float = 1.0,
    ) -> None:
        """
        Calculate the Ultimate Oscillator (UO) for the given chart data.
        Parameters:
            period1 (int): The number of periods to use for the first UO calculation. Default is 7.
            period2 (int): The number of periods to use for the second UO calculation. Default is 14.
            period3 (int): The number of periods to use for the third UO calculation. Default is 28.
            weight1 (float): The weight to apply to the first UO calculation. Default is 4.0.
            weight2 (float): The weight to apply to the second UO calculation. Default is 2.0.
            weight3 (float): The weight to apply to the third UO calculation. Default is 1.0.
        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.uo(7, 14, 28, 4.0, 2.0, 1.0)
            >>> print(fmp.return
        """
        chart = self.chart.copy()
        chart["uo"] = (
            UltimateOscillator(
                high=chart["high"],
                low=chart["low"],
                close=chart["close"],
                window1=period1,
                window2=period2,
                window3=period3,
                weight1=weight1,
                weight2=weight2,
                weight3=weight3,
                fillna=True,
            )
            .ultimate_oscillator()
            .round(2)
        ).astype(float)

        self.chart = chart

    #####################################
    # Williams %R
    #####################################
    def wr(self, period: int = 14) -> None:
        """
        Calculate the Williams %R for the given chart data.
        Parameters:
            period (int): The number of periods to consider for the calculation. Default is 14.
        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.wr(14)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart[f"wr{period}"] = (
            WilliamsRIndicator(
                high=chart["high"],
                low=chart["low"],
                close=chart["close"],
                lbp=period,
                fillna=True,
            )
            .williams_r()
            .round(2)
        ).astype(float)

        self.chart = chart

    ###############################
    # Awesome Oscillator
    ###############################
    def ao(self, period1: int = 5, period2: int = 34) -> None:
        """
        Calculate the Awesome Oscillator (AO) for the given chart data.
        Parameters:
            period1 (int): The number of periods to use for the first AO calculation. Default is 5.
            period2 (int): The number of periods to use for the second AO calculation. Default is 34.
        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.ao(5, 34)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart["ao"] = (
            AwesomeOscillatorIndicator(
                high=chart["high"],
                low=chart["low"],
                window1=period1,
                window2=period2,
                fillna=True,
            )
            .awesome_oscillator()
            .round(2)
        ).astype(float)

        self.chart = chart

    ####################################
    # Kaufman's Adaptive Moving Average
    ####################################
    def kama(self, period: int = 10, pow1: int = 2, pow2: int = 30) -> None:
        """
        Calculate the Kaufman's Adaptive Moving Average (KAMA) for the given chart data.
        Parameters:
            period (int): The number of periods to consider for the calculation. Default is 10.
            pow1 (int): The number of periods to consider for the first power factor. Default is 2.
            pow2 (int): The number of periods to consider for the second power factor. Default is 30.
        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.kama(10, 2, 30)
            >>> print(fmp.return_chart
        """
        chart = self.chart.copy()
        chart[f"kama{period}"] = (
            KAMAIndicator(
                close=chart["close"],
                window=period,
                pow1=pow1,
                pow2=pow2,
                fillna=True,
            )
            .kama()
            .round(2)
        ).astype(float)

        self.chart = chart

    #####################################
    # Rate of Change (ROC)
    #####################################
    def roc(self, period: int = 12) -> None:
        """
        Calculate the Rate of Change (ROC) for the given chart data.
        Parameters:
            period (int): The number of periods to consider for the calculation. Default is 12.
        Returns:
            None

        Example:
            >>> fmp = FmpCharts(symbol="AAPL", from_date="2021-01-01", to_date="2021-01-10")
            >>> fmp.roc(12)
            >>> print(fmp.return_chart())
        """
        chart = self.chart.copy()
        chart[f"roc{period}"] = (
            ROCIndicator(
                close=chart["close"],
                window=period,
                fillna=True,
            )
            .roc()
            .round(2)
        ).astype(float)

        self.chart = chart

    def return_chart(self) -> pd.DataFrame:
        return self.chart
