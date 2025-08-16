import requests
import xml.etree.ElementTree as ET

class WebLookupAgent:
    """Search academic papers using the ArXiv API."""

    def lookup(self, query, limit=3):
        try:
            url = "http://export.arxiv.org/api/query"
            params = {"search_query": query, "start": 0, "max_results": limit}
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            root = ET.fromstring(response.content)
            ns = {"arxiv": "http://www.w3.org/2005/Atom"}
            entries = root.findall("arxiv:entry", ns)

            if not entries:
                return "No results found."

            results = []
            for entry in entries:
                title = entry.find("arxiv:title", ns).text.strip()
                authors = [a.find("arxiv:name", ns).text for a in entry.findall("arxiv:author", ns)]
                link_elem = entry.find("arxiv:id", ns) or entry.find("arxiv:link[@type='text/html']", ns)
                link = link_elem.text if link_elem is not None and link_elem.text else "No link"
                results.append(f"{title}\nAuthors: {', '.join(authors)}\nLink: {link}\n")
            return "\n".join(results)

        except Exception as e:
            return f"Web lookup failed: {e}"
