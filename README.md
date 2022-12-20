# Simple-RSI-strategy-on-TESLA-

This code creates an algorithm that inherits from QCAlgorithm, which is the base class for all QuantConnect algorithms. In the Initialize method, we set the cash and equity we want to use for our strategy, and create the momentum and exponential moving average (EMA) indicators. In the OnData method, we check the value of the momentum indicator and EMA and place a buy order if the momentum is positive and the EMA is above the current price, or a sell order if the momentum is negative and the EMA is below the current price.
