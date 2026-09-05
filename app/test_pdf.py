import sys
sys.path.append("app")

from pdf_processor import extract_text_from_pdf

pdf_path = "documents/sample.pdf"

text = extract_text_from_pdf(pdf_path)
print(text)