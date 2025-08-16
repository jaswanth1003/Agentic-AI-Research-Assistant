import pytest
from src.pdf_utils import read_pdf
from src.citation_extractor import CitationExtractor

def test_read_pdf(tmp_path):
    # Create a temporary PDF file
    pdf_file = tmp_path / "test.pdf"
    c = canvas.Canvas(str(pdf_file))
    c.drawString(100, 750, "Hello PDF")
    c.save()

    text = read_pdf(str(pdf_file))
    assert "Hello PDF" in text

def test_citation_extractor():
    text = "[1] Smith et al. A study.\n[2] Doe et al. Another study."
    extractor = CitationExtractor(text)
    citations = extractor.get_full_citations(["1", "2"])
    assert "[1]" in citations[0]
    assert "Smith" in citations[0]
