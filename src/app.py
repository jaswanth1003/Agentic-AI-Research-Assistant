import gradio as gr
from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings
from pdf_utils import read_pdf
from research_assistant import ResearchAssistantSystem

# Initialize NVIDIA LLaMA 3 endpoint
llm = ChatNVIDIA(model="meta/llama-3.1-8b-instruct")
embedding = NVIDIAEmbeddings(model="nvidia/nv-embed-v1", truncate="END")

# Initialize system
system = ResearchAssistantSystem(llm, embedding, chunk_size=2000)

def ingest_and_summarize(pdf_file, top_k=5):
    if pdf_file is None:
        return "Please upload a PDF."

    try:
        pdf_text = read_pdf(pdf_file.name)
        system.ingest_papers([pdf_text])
        return system.summarize(top_k=top_k)
    except Exception as e:
        return f"Error: {str(e)}"

def query_paper(query, top_k=5):
    if not system.vectorstore:
        return "No documents ingested yet. Upload a PDF first."

    try:
        result = system.answer_query(query, top_k=top_k)
        return result.get("raw_answer", str(result))
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("# 📄 Research Paper Assistant")
    gr.Markdown("Upload a PDF, get a structured summary, and ask questions.")

    with gr.Tab("Summarize Paper"):
        pdf_input = gr.File(label="Upload PDF", type="filepath")
        top_k_input = gr.Slider(1, 10, value=5, step=1, label="Chunks to use")
        summary_output = gr.Markdown()
        summarize_btn = gr.Button("Generate Summary")
        summarize_btn.click(ingest_and_summarize, inputs=[pdf_input, top_k_input], outputs=summary_output)

    with gr.Tab("Ask Questions"):
        query_input = gr.Textbox(label="Enter your question")
        answer_output = gr.Markdown()
        query_btn = gr.Button("Ask")
        query_btn.click(query_paper, inputs=[query_input], outputs=answer_output)

demo.launch()
