import argparse
import sys
from ai_news_scraper.scraper import AIScraper

def main():
    parser = argparse.ArgumentParser(description="AI News Scraper CLI")
    parser.add_argument("--save", action="store_true", help="Save the scraped news to a JSON file")
    parser.add_argument("--filename", type=str, default=None, help="Specify output filename")
    
    args = parser.parse_args()
    scraper = AIScraper()

    try:
        if args.save:
            file_path = scraper.save_to_json(args.filename)
            print(f"✅ Success! Data saved to: {file_path}")
        else:
            news = scraper.get_all()
            for source, articles in news.items():
                print(f"\n--- {source.upper()} AI NEWS ---")
                for art in articles[:5]:
                    print(f"- {art['title']}\n  {art['link']}")
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()