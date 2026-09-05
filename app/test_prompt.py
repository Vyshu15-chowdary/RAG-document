import sys

sys.path.append("app")

from embeddings import create_embeddings
from vector_store import collection
from prompt import create_prompt


question = "What is a document database?"


# Create question embedding
question_embedding = create_embeddings([question])[0]


# Retrieve relevant chunks
results = collection.query(
    query_embeddings=[question_embedding.tolist()],
    n_results=3
)


# Get retrieved documents
retrieved_chunks = results["documents"][0]


# Create prompt
prompt = create_prompt(question, retrieved_chunks)


print("\n================ PROMPT ================\n")
print(prompt)