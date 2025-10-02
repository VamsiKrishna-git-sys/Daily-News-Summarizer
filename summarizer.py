from transformers import pipeline

# Load once (expensive)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_len=500, min_len=50):
    if not text.strip():
        return "No content available."
    try:
        summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as e:
        return f"Error summarizing: {e}"
