from fastmcp import FastMCP
from ai_news_scraper.scraper import AIScraper

# Initialize MCP Server
mcp = FastMCP("AI News Scraper")

# Initialize the scraper logic
scraper = AIScraper()

@mcp.tool()
def get_ai_news_by_source(source_key: str) -> str:
    """
    Fetches the latest AI news articles from a specific source.
    Available sources: 'TheVerge', 'VentureBeat'.
    """
    try:
        articles = scraper.fetch_news(source_key)
        # Format for the AI to read easily
        result = f"--- Latest news from {source_key} ---\n"
        for art in articles[:5]:
            result += f"- {art['title']}\n  Link: {art['link']}\n"
        return result
    except Exception as e:
        return f"Error fetching news: {str(e)}"

@mcp.tool()
def get_all_ai_news() -> dict:
    """
    Fetches and aggregates the latest AI stories from all supported news outlets.
    """
    try:
        return scraper.get_all()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()