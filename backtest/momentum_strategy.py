import pandas as pd

def momentum_strategy(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["SMA50"] = out["Close"].rolling(50).mean()
    out["SMA200"] = out["Close"].rolling(200).mean()
    out["Signal"] = (out["SMA50"] > out["SMA200"]).astype(int)
    return out

