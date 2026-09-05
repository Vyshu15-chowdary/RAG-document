import sys

sys.path.append("app")

from embeddings import create_embeddings
from vector_store import collection


question = "What is a document database?"

question_embedding = create_embeddings([question])[0]

results = collection.query(
    query_embeddings=[question_embedding.tolist()],
    n_results=3
)


print("\nTop 3 relevant chunks:\n")


for i, document in enumerate(results["documents"][0]):

    metadata = results["metadatas"][0][i]

    print("-----------------------------")
    print(f"RESULT {i + 1}")
    print("-----------------------------")

    print("Source:", metadata["source"])
    print("Chunk:", metadata["chunk"])

    print("\nContent:")
    print(document)