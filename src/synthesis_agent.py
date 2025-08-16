import json

class SynthesisAgent:
    """Uses an LLM to create structured summaries."""

    def __init__(self, llm, max_chunk_size=3000):
        self.llm = llm
        self.max_chunk_size = max_chunk_size

    def _chunk_text(self, text):
        chunks, current_chunk = [], ""
        for line in text.split("\n"):
            if len(current_chunk) + len(line) + 1 > self.max_chunk_size:
                chunks.append(current_chunk)
                current_chunk = line
            else:
                current_chunk += "\n" + line
        if current_chunk:
            chunks.append(current_chunk)
        return chunks

    def _prompt_for_json(self, text_chunk):
        return (
            "You are a research assistant. Extract information and return JSON with keys: "
            "title, authors, abstract, key_findings, methods, results, limitations, conclusion.\n\n"
            f"Text:\n{text_chunk}"
        )

    def create_structured_summary(self, text):
        chunks = self._chunk_text(text)
        summaries = []
        for chunk in chunks:
            prompt = self._prompt_for_json(chunk)
            raw_text = self.llm.invoke(prompt).content
            try:
                summaries.append(json.loads(raw_text))
            except json.JSONDecodeError:
                summaries.append({"raw_summary": raw_text})

        merged = {k: " ".join([s.get(k, "") for s in summaries]) for k in
                  ["title", "authors", "abstract", "key_findings", "methods", "results", "limitations", "conclusion"]}
        return merged
