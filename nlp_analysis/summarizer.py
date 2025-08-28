from transformers import pipeline

_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str, max_len: int = 160) -> str:
    if not text or len(text.split()) < 30:
        return text
    out = _summarizer(text, max_length=max_len, min_length=60, do_sample=False)
    return out[0]["summary_text"]

