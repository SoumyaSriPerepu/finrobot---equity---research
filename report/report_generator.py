from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_report(ticker: str, summary: str, sentiment: list, metrics: dict,
                    filename: str = "equity_report.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y = height - 72

    def line(txt, dy=20):
        nonlocal y
        c.drawString(72, y, str(txt))
        y -= dy

    c.setFont("Helvetica-Bold", 14)
    line(f"Equity Research Report — {ticker}")
    c.setFont("Helvetica", 10)
    line(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    c.setFont("Helvetica-Bold", 12)
    line("Summary:", 18)
    c.setFont("Helvetica", 10)
    for chunk in [summary[i:i+95] for i in range(0, len(summary), 95)]:
        line(chunk, 14)

    c.setFont("Helvetica-Bold", 12)
    line("Sentiment:", 18)
    c.setFont("Helvetica", 10)
    for s in sentiment:
        label = s.get("label") if isinstance(s, dict) else str(s)
        score = s.get("score") if isinstance(s, dict) else ""
        line(f"{label}: {round(score, 3) if score != '' else score}", 14)

    c.setFont("Helvetica-Bold", 12)
    line("Valuation Metrics:", 18)
    c.setFont("Helvetica", 10)
    for k, v in metrics.items():
        line(f"{k}: {v}", 14)

    c.showPage()
    c.save()
    return filename

