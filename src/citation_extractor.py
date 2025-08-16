import re

class CitationExtractor:
    """Parses and retrieves citations from reference text."""

    def __init__(self, reference_text: str):
        self.update_references(reference_text)

    def update_references(self, new_reference_text: str):
        self.reference_text = new_reference_text
        self.citation_map = self._build_citation_map()

    def _build_citation_map(self):
        entries = re.split(r'(\[\s*\d+\s*\])', self.reference_text)
        citation_map, current_num, current_text = {}, None, []

        for part in entries:
            match = re.match(r'\[\s*(\d+)\s*\]', part)
            if match:
                if current_num is not None:
                    citation_map[current_num] = ' '.join(current_text).strip()
                current_num, current_text = match.group(1), []
            elif current_num is not None:
                current_text.append(part.strip())

        if current_num is not None:
            citation_map[current_num] = ' '.join(current_text).strip()
        return citation_map

    def extract_citation_numbers(self, chunks):
        numbers = {num for chunk in chunks for num in re.findall(r'\[(\d+)\]', chunk)}
        return list(numbers)

    def get_full_citations(self, citation_numbers):
        return [f"[{num}] {self.citation_map.get(num, 'Citation not found')}" for num in citation_numbers]
