from sentence_transformers import SentenceTransformer
import json
import pickle
import torch
import os
from settings import NUM_DOCUMENTS, EMBEDDING_DIM, DATA_PATH, EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

abstracts = []
if os.path.exists(DATA_PATH):
    with open("data.pickle", "rb") as f:
        data = pickle.load(f)
        abstracts, existing_embeddings = data["abstracts"], data["embeddings"]
        num_existing = existing_embeddings.shape[0]

embeddings = torch.FloatTensor(NUM_DOCUMENTS, EMBEDDING_DIM)
for i in range(num_existing):
    embeddings[i] = existing_embeddings[i]

with open("arxiv.json", "r", encoding='utf-8') as f:
    for i, row in enumerate(f.readlines()[num_existing:NUM_DOCUMENTS]):
        if i % 1000 == 0:
            print("Writing %s" % str(i+num_existing))

        abstract = str(json.loads(row)['abstract'])
        embedding = torch.FloatTensor(model.encode(abstract))

        abstracts.append(abstract)
        embeddings[i+num_existing, :] = embedding
    
with open("data.pickle", "wb") as f:
    pickle.dump({"abstracts": abstracts, "embeddings": embeddings}, f)
