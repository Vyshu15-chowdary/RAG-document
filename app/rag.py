import sys

sys.path.append("app")

from embeddings import create_embeddings
from vector_store import collection
from prompt import create_prompt
from llm import generate_answer


def ask_question(question):

    # 1. Convert question into embedding
    question_embedding = create_embeddings([question])[0]

    # 2. Search ChromaDB
    results = collection.query(
        query_embeddings=[question_embedding.tolist()],
        n_results=3
    )

    # 3. Get relevant chunks
    retrieved_chunks = results["documents"][0]

    # 4. Create prompt
    prompt = create_prompt(
        question,
        retrieved_chunks
    )

    # 5. Generate answer
    answer = generate_answer(prompt)

    # 6. Get source metadata
    sources = results["metadatas"][0]

    return answer, sources