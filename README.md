# Agentic-AI-Research-Assistant
An agentic AI-based research assistant for ingesting, summarizing, and querying academic papers with LLM-powered agents and embeddings.


An AI-powered Research Assistant System that helps researchers and students interact with scientific papers.
This project enables:

- PDF ingestion & text extraction
- Intelligent document chunking & FAISS vector search
- Literature scanning using NVIDIA embeddings
- Citation extraction & reference mapping
- LLM-powered structured summarization
- ArXiv API lookup for related academic papers
- Interactive Gradio UI for summarization & question answering


## **Features**

-PDF Reader – Extracts text from uploaded research papers.
-Embeddings + FAISS – Creates a searchable knowledge base of ingested papers.
-Citation Extractor – Parses reference sections to map citations.
-Summarization Agent – Generates structured summaries (title, authors, abstract, key findings, methods, results, limitations, conclusion).
-Web Lookup Agent – Searches related papers on ArXiv.
-Interactive Gradio App – Upload PDFs, get summaries, and ask questions.

## **System Architecture**

<img width="1280" height="693" alt="image" src="https://github.com/user-attachments/assets/422c5a2b-0021-4950-945e-fb49ad69376d" />


## **Installation**

Clone this repository and install dependencies:

```
git clone https://github.com/your-username/research-assistant.git
cd research-assistant

# Install dependencies
pip install faiss-cpu PyPDF2 langchain-nvidia-ai-endpoints langchain-community gradio requests 
```
