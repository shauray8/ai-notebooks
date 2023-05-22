from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModel

model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
transformer_model = SentenceTransformer(model_name)

def create_embeddings(prompt):
    embeddings = transformer_model.encode([prompt])
    return embeddings[0]

def decode_embeddings(prompt):
    embedding_ids = [int(id) for id in prompt]
    embeddings = tokenizer.decode(embedding_ids, skip_special_tokens=True)
    print(embeddings)
    return embeddings

decode_embeddings(create_embeddings("how are you"))
