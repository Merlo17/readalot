from sentence_transformers import SentenceTransformer
import pickle
import torch
import numpy as np
from torch.nn.functional import cosine_similarity
from settings import EMBEDDING_DIM, DATA_PATH, EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)
with open(DATA_PATH, "rb") as f:
    X = pickle.load(f)
    abstracts, embeddings = X["abstracts"], X["embeddings"]

text = "Microsoft employee of the month, victor pescaru"

text_embedding = torch.Tensor(model.encode(text)).reshape([1, EMBEDDING_DIM])
similarities = cosine_similarity(text_embedding, embeddings, dim=1)

best = np.argmax(similarities, axis=0)

print(abstracts[best.item()])