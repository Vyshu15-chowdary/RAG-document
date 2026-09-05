import sys

sys.path.append("app")

from llm import generate_answer


prompt = """
Explain what a document database is in simple words.
"""


answer = generate_answer(prompt)


print("\n================ ANSWER ================\n")
print(answer)