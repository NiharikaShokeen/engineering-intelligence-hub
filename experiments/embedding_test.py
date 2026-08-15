from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Why are hydrangeas blue?",
    "Hydrangea flowers can become blue depending on soil pH.",
    "Sunflowers are harvested for their edible seeds."
]

embeddings = model.encode(sentences)

print(embeddings.shape)

print(cos_sim(embeddings[0], embeddings[1]))
print(cos_sim(embeddings[0], embeddings[2]))
