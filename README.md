# AI Equity Research Agent

End-to-end, browser-deployable project:
- Fetches market data
- Momentum signal (SMA 50/200)
- 30-day forecast (Prophet)
- NLP summary (BART) + sentiment (FinBERT)
- Generates a PDF equity report

## Run (options)
- **GitHub Codespaces:** Open with Codespaces → `pip install -r requirements.txt` → `streamlit run app.py`
- **Streamlit Cloud:** Deploy this repo; set Python 3.11 and use `pip install -r requirements.txt` as build step; command: `streamlit run app.py`

> Note: Streamlit Cloud may need additional build time for `prophet`/`torch`.
