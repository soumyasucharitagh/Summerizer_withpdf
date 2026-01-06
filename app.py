import streamlit as st
from PIL import Image

from models.text_summarizer import summarize_text
from models.pdf_summarizer import summarize_pdf
from models.image_captioning import generate_caption

st.set_page_config(page_title="ML Multi App", layout="wide")

st.title("🧠 Multi-Model ML Application")

option = st.sidebar.selectbox(
    "Choose a task",
    ["Text Summarization", "PDF Summarization", "Image Captioning"]
)

# ================= TEXT =================
if option == "Text Summarization":
    st.header("📝 Text Summarization")

    text = st.text_area("Enter text", height=250)

    if st.button("Summarize"):
        if text.strip():
            with st.spinner("Summarizing..."):
                summary = summarize_text(text)
            st.subheader("Summary")
            st.write(summary)
        else:
            st.warning("Please enter some text.")

# ================= PDF =================
elif option == "PDF Summarization":
    st.header("📄 PDF Summarization")

    uploaded_pdf = st.file_uploader(
        "Upload a PDF", type=["pdf"]
    )

    if st.button("Summarize PDF"):
        if uploaded_pdf:
            with st.spinner("Processing PDF..."):
                summary = summarize_pdf(uploaded_pdf)
            st.subheader("Summary")
            st.write(summary)
        else:
            st.warning("Please upload a PDF file.")

# ================= IMAGE =================
elif option == "Image Captioning":
    st.header("🖼 Image Captioning")

    uploaded_image = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image:
        image = Image.open(uploaded_image).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Generate Caption"):
            with st.spinner("Generating caption..."):
                caption = generate_caption(image)
            st.subheader("Caption")
            st.write(caption)
