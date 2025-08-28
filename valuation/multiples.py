import yfinance as yf

def get_valuation_metrics(ticker: str) -> dict:
    t = yf.Ticker(ticker)
    info = getattr(t, "info", {}) or {}
    fast = getattr(t, "fast_info", {}) or {}

    return {
        "market_cap": fast.get("market_cap"),
        "pe_forward": info.get("forwardPE"),
        "peg_ratio": info.get("pegRatio"),
        "price_to_book": info.get("priceToBook"),
        "ev_to_ebitda": info.get("enterpriseToEbitda"),
        "shares": fast.get("shares"),
        "currency": fast.get("currency", info.get("currency")),
    }

