import streamlit as st
from data_ingestion.market_data import get_stock_data
from forecasting.time_series import forecast_prices
from nlp_analysis.summarizer import summarize_text
from nlp_analysis.sentiment import analyze_sentiment
from valuation.multiples import get_valuation_metrics
from backtest.momentum_strategy import momentum_strategy
from report.report_generator import generate_report

st.title("📊 AI Equity Research Agent")

ticker = st.text_input("Enter stock ticker (e.g., AAPL, MSFT)", "AAPL")

if st.button("Run Analysis") or ticker:
    try:
        st.subheader("Market Data")
        prices = get_stock_data(ticker)
        st.line_chart(prices.set_index("Date")["Close"])

        st.subheader("Momentum Backtest Signal")
        sig = momentum_strategy(prices)
        st.line_chart(sig.set_index("Date")[["SMA50", "SMA200"]])

        st.subheader("30-Day Forecast (Prophet)")
        fcst = forecast_prices(prices, periods=30)
        st.line_chart(fcst.set_index("ds")[["yhat"]])

        st.subheader("Valuation Metrics")
        metrics = get_valuation_metrics(ticker)
        st.json(metrics)

        st.subheader("NLP Summary & Sentiment (Demo text)")
        demo_text = f"{ticker} continues to demonstrate resilience with improving margins and revenue growth amid market volatility. Risks remain around macro trends and product cycles."
        summary = summarize_text(demo_text)
        sentiment = analyze_sentiment(demo_text)
        st.write(summary)
        st.write(sentiment)

        if st.button("Generate PDF Report"):
            fname = generate_report(ticker, summary, sentiment, metrics)
            st.success(f"Report generated in working directory: {fname}")

    except Exception as e:
        st.error(str(e))

