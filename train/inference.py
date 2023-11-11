from sentence_transformers import SentenceTransformer
import pickle
import torch
import numpy as np
from torch.nn.functional import cosine_similarity
from settings import EMBEDDING_DIM, OUTPUT_PATH, EMBEDDING_MODEL, COS_SIM_BSIZE, NUM_DOCUMENTS

def documents_ordered_by_similarity(a, b, device="cuda"):
    global COS_SIM_BSIZE

    similarities = torch.zeros([NUM_DOCUMENTS]).to(device)

    for i in range(0, NUM_DOCUMENTS, COS_SIM_BSIZE):
        batch = b[i : i+COS_SIM_BSIZE].to(device)
        new_similarities = cosine_similarity(a, batch, dim=1)
        similarities[i : i+COS_SIM_BSIZE] = new_similarities

    return np.flip(torch.argsort(similarities, axis=0).cpu().numpy())


device = "cuda"
model = SentenceTransformer(EMBEDDING_MODEL, device=device)
with open(OUTPUT_PATH, "rb") as f:
    X = pickle.load(f)
    abstracts, embeddings = X["abstracts"], X["embeddings"]

# text = "The dangerous effects of social media like TikTok"
# text = "Attention mechanism in transformer networks"
# text = "Farting cows are the main cause of methane in the atmosphere"
# text = "graph about the frozen movie"
# text = "how backpropagation works in neural networks"
text = "heart disease and cardiovascular problems"

text_embedding = torch.Tensor(model.encode(text)).unsqueeze(0).to(device)
best = documents_ordered_by_similarity(text_embedding, embeddings, device=device)

for article in best[:3]:
    print("\n##############")
    print(abstracts[article.item()])