from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("model-name")
embeddings = embedder.encode(["Hello World", "Hallo Welt", "Hola mundo"])
print(embeddings)