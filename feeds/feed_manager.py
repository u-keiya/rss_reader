import json
import re
import feedparser

class FeedManager:
    def __init__(self, storage_file="data/feeds.json"):
        self.storage_file = storage_file
        self.feeds = self.load_feeds()

    def load_feeds(self):
        with open(self.storage_file, "r") as f:
            return json.load(f)

    def add_feed(self, url):
        feed = feedparser.parse(url)
        feed_name = feed.feed.get("title", "不明なメディア名")
        print(feed_name)
        self.feeds.append({"name": feed_name, "url": url})
        self.save_feeds()
    
    def delete_feed(self, url):
        pass
        #seld.feeds

    def save_feeds(self):
        with open(self.storage_file, "w") as f:
            json.dump(self.feeds, f)
