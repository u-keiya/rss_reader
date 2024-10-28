import json

class FeedManager:
    def __init__(self, storage_file="data/storage.json"):
        self.storage_file = storage_file

    def load_feeds(self):
        with open(self.storage_file, "r") as f:
            return json.load(f).get("feeds", [])

    def add_feed(self, url):
        self.feeds.append(url)
        self.save_feeds()

    def save_feeds(self):
        with open(self.storage_file, "w") as f:
            json.dump({"feeds": self.feeds}, f)
