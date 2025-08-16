from langchain.embeddings.base import Embeddings

class NvidiaEmbeddingsWrapper(Embeddings):
    """LangChain-compatible NVIDIA embeddings wrapper."""

    def __init__(self, embedder):
        self.embedder = embedder

    def embed_documents(self, texts):
        return [self.embedder.embed_query(text) for text in texts]

    def embed_query(self, text):
        return self.embedder.embed_query(text)
