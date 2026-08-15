import os
from dotenv import load_dotenv
from openai import OpenAI

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

#loads the variables from .env
load_dotenv()
#means:"Python, give me the value stored under OPENAI_API_KEY."
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_doc(file_path):
    with open(file_path) as file:
        text = file.read()

    return text


def chunk_text(text):
    chunks = text.split("##")
    return chunks


text = load_doc("documents/flowers.md")
chunks = chunk_text(text)
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)

question = input("Ask a question: ")
question_embedding = model.encode(question)

results = []
for i in range(len(chunks)):
    similarity = cos_sim(embeddings[i], question_embedding)
    results.append((similarity.item(),i))

ranked_result = sorted(results, reverse=True)
top_results = ranked_result[:3]


context = ""
for score, index in top_results:
    context += chunks[index]

prompt = f"""
Answer the question using only the context below.

Question: {question}
Context: {context}
"""

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)
print(response.output_text)
