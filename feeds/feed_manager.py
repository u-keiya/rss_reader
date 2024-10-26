import json
import feedparser

class FeedManager:
    def __init__(self, storage_file="data/storage.json"):
        self.storage_file = storage_file
        self.feeds = self.load_feeds()

    def load_feeds(self):
        with open(self.storage_file, "r") as f:
            return json.load(f).get("feeds", [])

    def add_feed(self, url):
        self.feeds.append(url)
        self.save_feeds()

    def save_feeds(self):
        with open(self.storage_file, "w") as f:
            json.dump({"feeds": self.feeds}, f)

    def fetch_articles(self):
        articles = []
        for url in self.feeds:
            feed = feedparser.parse(url)
            articles.extend(feed.entries)
        return articles