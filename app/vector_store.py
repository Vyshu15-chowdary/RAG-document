import chromadb


client = chromadb.PersistentClient(path="vectorstore")

collection = client.get_or_create_collection(
    name="documents"
)


def store_chunks(chunks, embeddings, source="sample.pdf"):

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    metadatas = [
        {
            "source": source,
            "chunk": i
        }
        for i in range(len(chunks))
    ]

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    print(f"{len(chunks)} chunks stored successfully.")