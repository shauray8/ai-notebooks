from sentence_transformers import SentenceTransformer
sentences = ["Twenty Dresses by Nykaa Fashion Navy Blue Slogan Printed Crop Tshirt (L)"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
print(embeddings)
