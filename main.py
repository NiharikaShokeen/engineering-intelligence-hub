import os
from dotenv import load_dotenv
from openai import OpenAI
import re

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

#loads the variables from .env
load_dotenv()
#means:"Python, give me the value stored under OPENAI_API_KEY."
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_documents(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.endswith(".md"):
            with open(file_path) as file:
                text = file.read()
                documents.append(text)

    return documents



def chunk_text(text):
    chunks = text.split("##")

    #removes unnecessary whitespace and empty chunks
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

    # Combine the document title with the first section
    if len(chunks) > 1:
        chunks[1] = chunks[0] + "\n" + chunks[1]
        chunks = chunks[1:]

    return chunks


documents = load_documents("documents")
print(len(documents))

chunks = []
for document in documents:
    document_chunks = chunk_text(document)
    chunks.extend(document_chunks)

print("Number of chunks: ", len(chunks))

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)
print("Embedding shape:", embeddings.shape)

question = input("Ask a question: ")
question_embedding = model.encode(question)

results = []
for i in range(len(chunks)):
    similarity = cos_sim(embeddings[i], question_embedding)
    results.append((similarity.item(),i))

ranked_result = sorted(results, reverse=True)
top_results = ranked_result[:3]

for score, index in top_results:
    print(score)
    print(chunks[index])
    print("--------")


# for i, chunk in enumerate(chunks):
#     print(f"CHUNK {i}:")
#     print(chunk[:100])
#     print("--------")


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
