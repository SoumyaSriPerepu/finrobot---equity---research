from transformers import pipeline

_finbert = pipeline("sentiment-analysis", model="ProsusAI/finbert")

def analyze_sentiment(text: str):
    if not text:
        return [{"label": "NEUTRAL", "score": 0.0}]
    return _finbert(text if isinstance(text, list) else [text])

