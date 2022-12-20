# region imports
from AlgorithmImports import *
# endregion



class MyAlgorithm(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2015, 1, 1)
        self.SetEndDate(2022, 1, 1)
        # Set the cash we'd like to use for our strategy
        self.SetCash(10000)
        self.trade_quantity=100
        self.upper_value=28
        self.lower_value=72

        # Set the equity we'd like to trade
        self.symbol = self.AddEquity("TSLA").Symbol

        # Set the period for the RSI indicator
        self.rsi_period = 14

        # Create the RSI indicator
        self.rsi = self.RSI(self.symbol, self.rsi_period)

    def OnData(self, data):
        # Check if we have enough data to calculate the RSI indicator
        if not self.rsi.IsReady:
            return

        # Check if the RSI is above 70 (overbought)
        if self.rsi.Current.Value > self.lower_value:
            # If the RSI is overbought, place a sell order
            self.Liquidate()
        # Check if the RSI is below 30 (oversold)
        elif self.rsi.Current.Value < self.upper_value:
            # If the RSI is oversold, place a buy order
            self.MarketOrder(self.symbol, self.trade_quantity)

