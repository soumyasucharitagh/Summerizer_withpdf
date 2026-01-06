from transformers import pipeline

# Load once (important for Streamlit performance)
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_text(text, max_length=150, min_length=40):
    summary = summarizer(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )
    return summary[0]['summary_text']
