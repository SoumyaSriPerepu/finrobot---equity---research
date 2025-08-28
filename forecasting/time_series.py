import pandas as pd
from prophet import Prophet

def forecast_prices(price_df: pd.DataFrame, periods: int = 30) -> pd.DataFrame:
    df = price_df.rename(columns={"Date": "ds", "Close": "y"})[["ds", "y"]].copy()
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=periods)
    fcst = model.predict(future)
    return fcst[["ds", "yhat", "yhat_lower", "yhat_upper"]]

