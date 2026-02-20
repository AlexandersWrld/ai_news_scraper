import feedparser
import json
from pathlib import Path
from datetime import datetime

class AIScraper:
    def __init__(self):
        self.sources = {
            "TheVerge": "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml",
            "VentureBeat": "https://venturebeat.com/category/ai/feed/"
        }

    def fetch_news(self, source_key):
        """Parses the RSS feed of the selected source."""
        url = self.sources.get(source_key)
        if not url:
            raise ValueError(f"Source '{source_key}' not found.")
        
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries:
            articles.append({
                "title": entry.get("title"),
                "link": entry.get("link"),
                "date": entry.get("published") or entry.get("updated"),
                "summary": entry.get("summary", "No summary available.")
            })
        return articles

    def get_all(self):
        """Aggregates latest stories from all sources."""
        return {name: self.fetch_news(name) for name in self.sources}

    def save_to_json(self, filename=None):
        """Fetches all news and saves it to a JSON file."""
        data = self.get_all()
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
            filename = f"ai_news_{timestamp}.json"
        
        file_path = Path(filename)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        return str(file_path.absolute())