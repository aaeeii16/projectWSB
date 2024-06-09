import yfinance as yf
import pandas as pd
from datetime import datetime

def getStockData(stockTicker: object, inputPeriod: object) -> object:

    my_ticker = yf.Ticker(stockTicker)
    current_df = my_ticker.history(period=inputPeriod)

    return current_df
    return my_ticker