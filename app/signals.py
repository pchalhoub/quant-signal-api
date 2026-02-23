import requests
import pandas as pd
from app.config import settings

def fetch_daily_prices(ticker: str):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "apikey": settings.ALPHA_VANTAGE_API_KEY,
        "outputsize": "compact"
    }

    r = requests.get(url, params=params)
    data = r.json()["Time Series (Daily)"]

    df = pd.DataFrame(data).T
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()

    df["close"] = df["4. close"].astype(float)

    return df[["close"]]

def compute_signals(df):
    df["returns"] = df["close"].pct_change()

    momentum_30d = df["close"].iloc[-1] / df["close"].iloc[-30] - 1
    volatility_30d = df["returns"].iloc[-30:].std() * (252 ** 0.5)

    return {
        "momentum_30d": float(momentum_30d),
        "volatility_30d": float(volatility_30d)
    }