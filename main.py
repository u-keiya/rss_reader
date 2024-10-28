import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from feeds.feed_manager import FeedManager
from feeds.rss_fetcher import RSSFetcher

def main():
    # アプリケーションの初期化
    app = QApplication(sys.argv)

    # フィードと記事の管理
    feed_manager = FeedManager()
    feeds = feed_manager.load_feeds()

    # フィードが登録されている場合、記事を取得
    rss_fetcher = RSSFetcher(feed_manager)
    articles = rss_fetcher.fetch_articles()

    # メインウィンドウを初期化し、表示
    window = MainWindow(feeds, articles)
    window.show()

    # アプリケーションの実行と終了処理
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
