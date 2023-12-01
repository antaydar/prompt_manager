import streamlit as st

# Title
st.title("How can I help you today?")

# Initialize empty lists to store inputs
text_inputs = []
urls = []
pdfs = []
text_files = []

# Create a layout with two columns
col1, col2 = st.columns(2)

# Left column for Text Input
with col1:
    st.header("Text Input:")
    text_input = st.text_area("Enter your text here:")
    if st.button("Add Text"):
        text_inputs.append(text_input)

# Right column for URL, PDF, and Text File Inputs
with col2:
    st.header("Upload your URLs, PDFs, and Text Files:")

    # URLs
    url_input = st.text_input("Enter a URL:")
    if st.button("Add URL"):
        urls.append(url_input)

    # PDFs
    uploaded_pdfs = st.file_uploader("Upload PDF files:", type=["pdf"], accept_multiple_files=True)
    if st.button("Add PDFs"):
        for pdf_file in uploaded_pdfs:
            pdfs.append(pdf_file)

    # Text Files
    uploaded_text_files = st.file_uploader("Upload text files:", type=["txt"], accept_multiple_files=True)
    if st.button("Add Text Files"):
        for text_file in uploaded_text_files:
            text_files.append(text_file)

# Submit button
if st.button("Submit"):
    # You can process and store the inputs in a structured way here
    # For example, you can store them in dictionaries or lists as needed
    structured_data = {
        "Text Inputs": text_inputs,
        "URLs": urls,
        "PDFs": pdfs,
        "Text Files": text_files,
    }
    # Display the structured data
    st.write("Structured Data:", structured_data)

# You can add more functionality to handle and process the user inputs as needed.
