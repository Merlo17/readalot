from flask import Flask, redirect, url_for, request, Response
import torch
import numpy as np
from sentence_transformers import SentenceTransformer
import asyncio
import pickle
from torch.nn.functional import cosine_similarity
from settings import EMBEDDING_MODEL, EMBEDDING_DIM, NUM_RESULTS, COS_SIM_BSIZE

app = Flask(__name__)
model = SentenceTransformer(EMBEDDING_MODEL)
model.eval()
device = "cpu"


pref_vector = torch.zeros([1, EMBEDDING_DIM]).to(device)            # The current preference vector, the documents are ordered according to cosine similarity wrt. this vector
current_paper_index = None                                          # The current article being shown to the user
next_paper_index = None                                             # Precalculated index of the next document when the user swipes, if this is none swiping is disallowed
prev_papers = []                                                    # Articles that have been seen already, don't show these again
candidate_papers = []                                               # These are used for left swipes, so there is no need to reorder the articles


with open("data_full.pickle", "rb") as f:
    X = pickle.load(f)
    abstracts, embeddings, authors, titles, doi, created = X["abstracts"], X["embeddings"], X["authors"], X["titles"], X["doi"], X["created"]

def format_output(paper_index):
    return {
        "title": titles[paper_index],
        "authors": authors[paper_index],
        "abstract": abstracts[paper_index].strip(),
        "doi": doi[paper_index],
        "created": created[paper_index]
    }

async def documents_ordered_by_similarity(a, b, device=device):
    global COS_SIM_BSIZE
    similarities = torch.zeros([b.shape[0]]).to(device)

    for i in range(0, b.shape[0], COS_SIM_BSIZE):
        batch = b[i : i+COS_SIM_BSIZE].to(device)
        new_similarities = cosine_similarity(a, batch, dim=1)
        similarities[i : i+COS_SIM_BSIZE] = new_similarities

    ordered_documents = np.flip(torch.argsort(similarities, axis=0).cpu().numpy())
    return ordered_documents[np.isin(ordered_documents, prev_papers) == False]

async def calculate_next_paper():
    global pref_vector, next_paper_index, embeddings, candidate_papers

    best = await documents_ordered_by_similarity(pref_vector, embeddings)
    candidate_papers = best

    for candidate in best:
        if candidate not in prev_papers:
            print("SET NEXT PAPER TO %s" % candidate)
            next_paper_index = candidate
            return
    exit("No more papers found")

@app.route("/start", methods = ['POST'])
async def start():
    global current_paper_index, next_paper_indexes, pref_vector, prev_papers, device

    if request.method == 'POST':
        # We now start a new session, clear previously shown papers
        prev_papers = []
        
        # Calculate ordering of documents wrt. query
        query = request.json['query']
        query_embedding = torch.Tensor(model.encode(query)).unsqueeze(0)
        pref_vector[:] = query_embedding.to(device)
        sorted_papers = await documents_ordered_by_similarity(pref_vector, embeddings)

        # Update server state
        current_paper_index = sorted_papers[0].item()
        pref_vector = torch.mean(torch.stack([pref_vector.squeeze(0).cpu(), embeddings[current_paper_index]]), dim=0, keepdim=False).unsqueeze(0).to(device)

        # Start calculating index of next paper to show async and return
        prev_papers.append(current_paper_index)
        asyncio.ensure_future(calculate_next_paper())

        return format_output(current_paper_index)
    else:
        return Response("Only post endpoint here", status=400)

@app.route('/swipe', methods = ['POST'])
async def swipe():
    global current_paper_index, prev_papers, next_paper_index, pref_vector, candidate_papers
    if request.method != 'POST':
        return "Only requests with method POST allowed"
    if current_paper_index is None:
        return "No current paper selected"
    if next_paper_index is None:
        return "Next paper not ready yet"

    # Set the current state of the server
    prev_papers.append(next_paper_index)
    current_paper_index = next_paper_index

    swipe_direction = request.json['swipeDirection']
    if swipe_direction == "right":
        # Update preference vector to be the mean of current and the document that was swiped right on
        pref_vector = torch.mean(torch.stack([pref_vector.squeeze(), embeddings[next_paper_index].to(device)]), dim=0, keepdim=False).unsqueeze(0)

        # Start calculating the index of next paper
        next_paper_index = None
        asyncio.ensure_future(calculate_next_paper())

    elif swipe_direction == "left":
        # Nothing to do here as we ignore left swipes, just pop the next paper from the previous ordering and move on
        candidate_papers = [paper for paper in candidate_papers if paper not in prev_papers]
        next_paper_index = candidate_papers[0]
        candidate_papers = candidate_papers[1:]
    
    return format_output(current_paper_index)
  
if __name__ == "__main__": 
    app.run(host="0.0.0.0", debug=True, port=8787)
