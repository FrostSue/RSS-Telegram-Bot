import logging
import feedparser
from typing import List, Dict


class RSSHandler:
    def __init__(self, feed_url: str):
        self.feed_url = feed_url
        self.logger = logging.getLogger(__name__)

    def fetch_new_entries(self, database) -> List[Dict]:
        try:
            feed = feedparser.parse(self.feed_url)
            new_entries = []

            for entry in reversed(feed.entries):
                entry_id = entry.get("id", entry.link)
                
                if not database.entry_exists(entry_id):
                    new_entry = {
                        "id": entry_id,
                        "title": entry.title,
                        "link": entry.link
                    }
                    new_entries.append(new_entry)
                    
                    database.add_entry(
                        entry_id, 
                        new_entry["title"], 
                        new_entry["link"]
                    )

            return new_entries

        except Exception as e:
            self.logger.error(f"RSS fetch hatası: {e}")
            return []
