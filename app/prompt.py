def create_prompt(question, retrieved_chunks):

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are a document question-answering assistant.

STRICT RULES:
1. Answer ONLY using the information provided in the context.
2. Do NOT use your own knowledge.
3. Do NOT add information that is not present in the context.
4. If the answer is not present in the context, say exactly:
"I could not find the answer in the document."

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt