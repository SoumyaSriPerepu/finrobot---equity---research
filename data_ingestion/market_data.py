import yfinance as yf
import pandas as pd

def get_stock_data(ticker: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    if df.empty:
        raise ValueError(f"No data returned for {ticker}.")
    df = df.reset_index()
    return df[["Date", "Open", "High", "Low", "Close", "Volume"]]

