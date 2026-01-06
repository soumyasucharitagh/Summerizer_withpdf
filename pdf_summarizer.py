from text_summarizer import summarize_text
import pdfplumber

MAX_CHARS = 3000  # safe limit for BART

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text


def chunk_text(text, max_chars=MAX_CHARS):
    chunks = []
    start = 0
    while start < len(text):
        end = start + max_chars
        chunks.append(text[start:end])
        start = end
    return chunks


def summarize_pdf(pdf_file):
    text = extract_text_from_pdf(pdf_file)

    if not text or len(text) < 500:
        return "PDF does not contain enough readable text."

    chunks = chunk_text(text)

    summaries = []
    for chunk in chunks[:5]:  # limit chunks to avoid timeout
        summary = summarize_text(chunk)
        summaries.append(summary)

    final_summary = " ".join(summaries)
    return final_summary
