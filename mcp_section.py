import wikipedia
import sys

def list_wikipedia_sections(topic: str) -> dict:
    """
    Return a list of section titles from the Wikipedia page of a given topic.
    """
    try:
        page = wikipedia.page(topic)
        sections = page.sections
        return {"sections": sections}
    except Exception as e:
        return {"error": str(e)}

def get_section_content(topic: str, section_title: str) -> dict:
    """
    Return the content of a specific section in a Wikipedia article.
    """
    try:
        page = wikipedia.page(topic)
        content = page.section(section_title)
        if content:
            return {"content": content}
        else:
            return {"error": f"Section '{section_title}' not found in article '{topic}'."}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print("Run mcp_server.py instead.", file=sys.stderr)