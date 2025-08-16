from src.research_assistant import ResearchAssistantSystem

class DummyLLM:
    def invoke(self, prompt): 
        class Response: content = '{"raw_answer": "Test response"}'
        return Response()

class DummyEmbedder:
    def embed_query(self, text): return [0.1] * 10
    def embed_documents(self, texts): return [[0.1] * 10 for _ in texts]

def test_ingest_and_query():
    system = ResearchAssistantSystem(DummyLLM(), DummyEmbedder())
    system.ingest_papers(["This is a dummy research paper."])
    summary = system.summarize()
    assert "Test response" not in summary  # summary should come from dummy LLM prompt
    answer = system.answer_query("What is this about?")
    assert "raw_answer" in answer
