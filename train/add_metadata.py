# Script for adding author and title to data.pickle

import pickle
import json
from settings import OUTPUT_PATH, DATASET_PATH

with open(OUTPUT_PATH, "rb") as f:
    data = pickle.load(f)
    abstracts, existing_embeddings = data["abstracts"], data["embeddings"]

authors = []
titles = []
with open(DATASET_PATH, "r", encoding='utf-8') as f:
    for i, row in enumerate(f.readlines()[:len(abstracts)]):
        row_data = json.loads(row)
        author, title = row_data['authors'], row_data['title']
        authors.append(author)
        titles.append(title)

with open("data_full.pickle", "wb") as f:
    pickle.dump({"abstracts": abstracts, "embeddings": existing_embeddings, "authors": authors, "titles": titles}, f)