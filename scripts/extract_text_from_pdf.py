from PyPDF2 import PdfReader


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


pdf_text = extract_text_from_pdf("./docs/2025 EY Open Science AI Data Challenge Participant Guidance.pdf")
print(pdf_text)
