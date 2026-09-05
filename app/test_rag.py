import sys

sys.path.append("app")

from rag import ask_question


question = "What is capital of france?"


answer, sources = ask_question(question)


print("\n================ RAG ANSWER ================\n")

print(answer)


print("\n================ SOURCES ================\n")


for i, source in enumerate(sources):

    print(f"Source {i + 1}:")
    print("File:", source["source"])
    print("Chunk:", source["chunk"])
    print()