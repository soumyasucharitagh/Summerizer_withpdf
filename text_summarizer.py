import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    summarizer = pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )
    return summarizer


def summarize_text(text, max_length=150, min_length=40):
    summarizer = load_model()

    summary = summarizer(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )

    return summary[0]["summary_text"]
