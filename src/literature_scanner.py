from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

class LiteratureScanner:
    """Deterministic document chunking and FAISS indexing."""

    def __init__(self, embedding_function):
        self.embedding_model = embedding_function
        self.vector_store = None
        self.chunks = []

    def ingest_documents(self, docs):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        self.chunks = [chunk for doc in docs for chunk in text_splitter.split_text(doc)]
        self.vector_store = FAISS.from_texts(self.chunks, self.embedding_model)
        print(f"Indexed {len(self.chunks)} text chunks.")

    def search_vectors(self, query, k=3):
        if not self.vector_store:
            raise ValueError("No documents ingested yet.")
        return self.vector_store.similarity_search(query, k=k)
