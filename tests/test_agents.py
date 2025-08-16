from src.literature_scanner import LiteratureScanner
from src.web_lookup_agent import WebLookupAgent

class DummyEmbedder:
    def embed_query(self, text): return [0.1] * 10
    def embed_documents(self, texts): return [[0.1] * 10 for _ in texts]

def test_literature_scanner():
    scanner = LiteratureScanner(DummyEmbedder())
    scanner.ingest_documents(["This is a test document."])
    results = scanner.search_vectors("test")
    assert len(results) > 0

def test_web_lookup_agent():
    agent = WebLookupAgent()
    result = agent.lookup("quantum computing", limit=1)
    assert isinstance(result, str)
