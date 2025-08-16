from PyPDF2 import PdfReader

def read_pdf(file_path: str) -> str:
    """Reads and extracts text from a PDF file."""
    reader = PdfReader(file_path)
    return "".join(page.extract_text() for page in reader.pages if page.extract_text())
