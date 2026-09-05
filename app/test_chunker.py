import sys

sys.path.append("app")

from pdf_processor import extract_text_from_pdf
from chunker import split_text_into_chunks

pdf_path = "documents/sample.pdf"

text = extract_text_from_pdf(pdf_path)
chunks = split_text_into_chunks(text)
print("Total characters:",len(text))
print("Total chunks:",len(chunks))

for i,chunk in enumerate(chunks):
    print("\n----------------------")
    print(f"Chunk {i+1}:")
    print(chunk)