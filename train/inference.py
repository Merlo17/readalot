from sentence_transformers import SentenceTransformer
import pickle
import torch
import numpy as np
from torch.nn.functional import cosine_similarity
from settings import EMBEDDING_DIM, OUTPUT_PATH, EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)
with open(OUTPUT_PATH, "rb") as f:
    X = pickle.load(f)
    abstracts, embeddings = X["abstracts"], X["embeddings"]

# text = "The dangerous effects of social media like TikTok"
# text = "Attention mechanism in transformer networks"
# text = "Farting cows are the main cause of methane in the atmosphere"
# text = "graph about the frozen movie"
# text = "how backpropagation works in neural networks"
text = "heart disease and cardiovascular problems"

text_embedding = torch.Tensor(model.encode(text)).reshape([1, EMBEDDING_DIM])
similarities = cosine_similarity(text_embedding, embeddings, dim=1)

best = np.argsort(similarities, axis=0)

for article in best[-3:]:
    print("\n##############")
    print(abstracts[article.item()])