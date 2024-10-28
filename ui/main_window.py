from PyQt5.QtWidgets import QMainWindow, QSplitter, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from ui.sidebar import Sidebar
from ui.article_card import ArticleCard

class MainWindow(QMainWindow):
    def __init__(self, feed_manager, rss_fetcher):
        super().__init__()

        self.feed_manager = feed_manager
        self.rss_fetcher = rss_fetcher

        feeds = self.feed_manager.load_feeds()
        articles = self.rss_fetcher.fetch_articles()

        self.setWindowTitle("RSS Reader")
        self.setGeometry(100, 100, 800, 600)

        # QSplitterでサイドバーと記事エリアを分割
        splitter = QSplitter(Qt.Horizontal)

        # サイドバーの初期化
        self.sidebar = Sidebar(feeds)

        # シグナル接続
        self.sidebar.feed_selected.connect(self.display_feed_articles)
        self.sidebar.show_all_feeds.connect(self.display_all_unread_articles)
        self.sidebar.show_favorites.connect(self.display_favorite_articles)
        self.sidebar.feed_added.connect(self.add_new_feed)

        # 記事エリアの設定
        self.article_container = QWidget()
        self.article_layout = QVBoxLayout()
        self.article_container.setLayout(self.article_layout)

        # QSplitterにウィジェットを追加
        splitter.addWidget(self.sidebar)
        splitter.addWidget(self.article_container)

        # サイドバーと記事エリアの伸縮モードを設定
        splitter.setStretchFactor(0, 3)  # サイドバーは初期設定で可変
        splitter.setStretchFactor(1, 200)  # 記事エリアは残りのスペースを占有

        # メインレイアウトにQSplitterを設定
        main_layout = QHBoxLayout()
        main_layout.addWidget(splitter)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # 初期表示
        self.articles = articles
        self.display_all_unread_articles()

    def display_feed_articles(self, feed_name):
        """選択されたフィードの未読記事を表示"""
        self.clear_article_layout()
        for article in self.articles:
            if article["feed_name"] == feed_name and not article.get("is_read", False):
                self.article_layout.addWidget(ArticleCard(article))

    def display_all_unread_articles(self):
        """全ての未読記事を表示"""
        self.clear_article_layout()
        for article in self.articles:
            if not article.get("is_read", False):
                self.article_layout.addWidget(ArticleCard(article))

    def display_favorite_articles(self):
        """お気に入りかつ未読の記事を表示"""
        self.clear_article_layout()
        for article in self.articles:
            if article.get("is_favorite", False) and not article.get("is_read", False):
                self.article_layout.addWidget(ArticleCard(article))

    def clear_article_layout(self):
        """記事エリアをクリア"""
        for i in reversed(range(self.article_layout.count())):
            widget = self.article_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

    def add_new_feed(self, url):
        """新しいRSSフィードを追加"""
        self.feed_manager.add_feed(url)