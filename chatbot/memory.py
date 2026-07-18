import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Dimension of embeddings
dimension = 384

# Create FAISS index
index = faiss.IndexFlatL2(dimension)

# Memory storage
memory = []

# File names
INDEX_FILE = "memory/faiss_index.bin"
MEMORY_FILE = "memory/memory.pkl"


def save_memory(text):

    global memory, index

    # Convert text into embedding
    embedding = embedding_model.encode([text])

    # Convert to float32 (required by FAISS)
    embedding = np.array(embedding).astype("float32")

    # Store in FAISS
    index.add(embedding)

    # Store original text
    memory.append(text)

    # Save FAISS index
    faiss.write_index(index, INDEX_FILE)

    # Save text memory
    with open(MEMORY_FILE, "wb") as f:
        pickle.dump(memory, f)
def load_memory():

    global memory, index

    # Load FAISS index if it exists
    if os.path.exists(INDEX_FILE):
        index = faiss.read_index(INDEX_FILE)

    # Load text memory if it exists
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "rb") as f:
            memory = pickle.load(f)
def search_memory(query, top_k=3):

    # If there is no memory, return empty list
    if len(memory) == 0:
        return []

    # Convert query into embedding
    query_embedding = embedding_model.encode([query])

    query_embedding = np.array(query_embedding).astype("float32")

    # Search similar memories
    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:

        if idx < len(memory):

            results.append(memory[idx])

    return results
def delete_memory(old_text):

    global memory, index

    if old_text not in memory:
        return

    # Remove from list
    memory.remove(old_text)

    # Rebuild FAISS index
    index = faiss.IndexFlatL2(dimension)

    if len(memory) > 0:

        embeddings = embedding_model.encode(memory)
        embeddings = np.array(embeddings).astype("float32")

        index.add(embeddings)

    # Save updated index
    faiss.write_index(index, INDEX_FILE)

    # Save updated memory
    with open(MEMORY_FILE, "wb") as f:
        pickle.dump(memory, f)