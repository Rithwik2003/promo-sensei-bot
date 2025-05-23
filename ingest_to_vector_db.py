import faiss
from sentence_transformers import SentenceTransformer
import json
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_offers(file_path="offers.json"):
    with open(file_path) as f:
        return json.load(f)

def ingest(offers):
    texts = [offer['description'] for offer in offers]
    embeddings = model.encode(texts)
    
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    
    faiss.write_index(index, "offers_index.faiss")

    with open("offers_meta.json", "w") as f:
        json.dump(offers, f)

if __name__ == "__main__":
    offers = load_offers()
    ingest(offers)
