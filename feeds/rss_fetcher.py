import threading
import time

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
