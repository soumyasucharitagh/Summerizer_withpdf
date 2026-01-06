import pdfplumber
from text_summarizer import summarize_text

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text

def summarize_pdf(pdf_file):
    text = extract_text_from_pdf(pdf_file)

    if len(text) < 500:
        return "PDF content is too short to summarize."

    return summarize_text(text)

