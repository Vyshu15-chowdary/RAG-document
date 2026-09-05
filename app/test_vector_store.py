import sys 

sys.path.append("app")

from pdf_processor import extract_text_from_pdf
from chunker import split_text_into_chunks
from embeddings import create_embeddings
from vector_store import store_chunks,collection

pdf_path = "documents/sample.pdf"
text = extract_text_from_pdf(pdf_path)
chunks = split_text_into_chunks(text)
embeddings = create_embeddings(chunks)
store_chunks(
    chunks,
    embeddings,
    source="sample.pdf"
)

print("Total chunks in chromaDB:",collection.count())