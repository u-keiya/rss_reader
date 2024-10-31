import threading
import time
import feedparser

class RSSFetcher:
    def __init__(self, feed_manager, interval=300):
        self.feed_manager = feed_manager
        self.interval = interval  # デフォルトは5分

    def start_fetching(self):
        threading.Thread(target=self.fetch_loop, daemon=True).start()

    def fetch_loop(self):
        while True:
            self.feed_manager.fetch_articles()
            time.sleep(self.interval)
    
    def fetch_articles(self):
        articles = []
        for feed in self.feed_manager.load_feeds():
            feed = feedparser.parse(feed["url"])
            articles.extend(feed.entries)
        return articles