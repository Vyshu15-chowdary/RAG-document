import sys

from pdf_processor import extract_text_from_pdf
from chunker import split_text_into_chunks
from embeddings import create_embeddings

pdf_path = "documents/sample.pdf"
text = extract_text_from_pdf(pdf_path)
chunks = split_text_into_chunks(text)
embeddings = create_embeddings(chunks)

print("Number of chunks:", len(chunks))
print("Number of embeddings:", len(embeddings))
print("Embedding dimension:", len(embeddings[0]))
print("\nFirst chunk:")
print(chunks[0])

print("\nFirst embedding:")
print(embeddings[0])