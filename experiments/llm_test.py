question = "What is the tallest sunflower?"

context = """
The tallest sunflower on record achieved 10.9 m (35 ft 9 in).

The plant has an erect rough-hairy stem, reaching typical heights
of 3 metres (10 feet).
"""

prompt = f"""
Answer the question using only the context below.

Question:
{question}

Context:
{context}
"""

print(prompt)