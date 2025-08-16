import json
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document

class ResearchAssistantSystem:
    """Main coordinator for ingestion, summarization, and querying."""

    def __init__(self, llm, embedding, chunk_size=2000):
        self.llm = llm
        self.embedding = embedding
        self.chunk_size = chunk_size
        self.vectorstore = None
        self.documents = []

    def _chunk_text(self, text):
        return [text[i:i + self.chunk_size] for i in range(0, len(text), self.chunk_size)]

    def ingest_papers(self, docs):
        self.documents.extend(docs)
        all_chunks = [chunk for doc in docs for chunk in self._chunk_text(doc)]
        documents = [Document(page_content=chunk) for chunk in all_chunks]
        self.vectorstore = FAISS.from_documents(documents, self.embedding)
        print(f"Ingested {len(docs)} documents, total chunks: {len(all_chunks)}")

    def summarize(self, top_k=5):
        if not self.vectorstore:
            return {"error": "No documents ingested."}

        summaries = []
        for doc in self.documents:
            combined_text = "\n".join(self._chunk_text(doc)[:top_k])
            prompt = (
                "You are a research assistant. Generate a structured summary.\n\n"
                f"Text:\n{combined_text}"
            )
            raw_summary = self.llm.invoke(prompt).content
            summaries.append(raw_summary.strip())

        return "\n\n---\n\n".join(summaries)

    def answer_query(self, query, top_k=5):
        if not self.vectorstore:
            return {"error": "No documents ingested."}
        relevant_chunks = self.vectorstore.similarity_search(query, k=top_k)
        combined_text = "\n".join([doc.page_content for doc in relevant_chunks])
        prompt = (
            f"You are a research assistant. Question: {query}\n\n"
            f"Text:\n{combined_text}\n\n"
            "Answer the query based only on this text."
        )
        raw_answer = self.llm.invoke(prompt).content
        try:
            return json.loads(raw_answer)
        except json.JSONDecodeError:
            return {"raw_answer": raw_answer}
