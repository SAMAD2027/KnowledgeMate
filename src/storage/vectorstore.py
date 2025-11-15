import faiss
import numpy as np

class VectorStore:
    """
    Simple vector store for embedding-based retrieval
    """
    def __init__(self, dim=128):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.vectors = []
        self.metadata = []

    def add(self, vector: np.ndarray, meta: dict):
        self.index.add(np.array([vector]).astype('float32'))
        self.vectors.append(vector)
        self.metadata.append(meta)

    def search(self, query_vector: np.ndarray, top_k=3):
        D, I = self.index.search(np.array([query_vector]).astype('float32'), top_k)
        results = [self.metadata[i] for i in I[0] if i < len(self.metadata)]
        return results
