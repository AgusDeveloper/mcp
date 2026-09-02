import wikipedia
import sys
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("WikipediaSearch")

@mcp.tool()
def fetch_wikipedia_info(query: str) -> dict:
    """
    Search Wikipedia for a topic and return title, summary, and URL of the best match.
    """
    try:
        search_results = wikipedia.search(query)
        if not search_results:
            return {"error": "No results found for your query."}

        best_match = search_results[0]
        page = wikipedia.page(best_match)

        return {
            "title": page.title,
            "summary": page.summary,
            "url": page.url
        }

    except wikipedia.DisambiguationError as e:
        return {
            "error": f"Ambiguous topic. Try one of these: {', '.join(e.options[:5])}"
        }

    except wikipedia.PageError:
        return {
            "error": "No Wikipedia page could be loaded for this query."
        }


from mcp_section import get_section_content, list_wikipedia_sections

mcp.tool()(list_wikipedia_sections)
mcp.tool()(get_section_content)


# Run the MCP server
if __name__ == "__main__":
    print("Starting MCP Wikipedia Server...", file=sys.stderr)
    mcp.run(transport="stdio")