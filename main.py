from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

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

question = "What is the tallest sunflower?"
question_embedding = model.encode(question)

results = []
for i in range(len(chunks)):
    similarity = cos_sim(embeddings[i], question_embedding)
    results.append((similarity.item(),i))

ranked_result = sorted(results, reverse=True)
top_results = ranked_result[:3]

# for score, index in top_results:
#     print(score)
#     print(chunks[index])
#     print("--------")

context = ""
for score, index in top_results:
    context += chunks[index]

prompt = f"""
Answer the question using only the context below.

Question: {question}
Context: {context}
"""
print(prompt)
