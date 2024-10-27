from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from ui.sidebar import Sidebar
from ui.article_card import ArticleCard

class MainWindow(QMainWindow):
    def __init__(self, feeds, articles):
        super().__init__()
        self.setWindowTitle("RSS Reader")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # サイドバーの初期化とシグナル接続
        self.sidebar = Sidebar(feeds)
        self.sidebar.feed_selected.connect(self.display_feed_articles)
        self.sidebar.show_all_feeds.connect(self.display_all_unread_articles)
        self.sidebar.show_favorites.connect(self.display_favorite_articles)

        self.article_container = QWidget()
        self.article_layout = QVBoxLayout()
        self.article_container.setLayout(self.article_layout)

        layout.addWidget(self.sidebar)
        layout.addWidget(self.article_container)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.articles = articles
        self.display_all_unread_articles()

    def display_feed_articles(self, feed_name):
        """選択されたフィードの未読記事のみ表示"""
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
        """お気に入りかつ未読の記事のみ表示"""
        self.clear_article_layout()
        for article in self.articles:
            if article.get("is_favorite", False) and not article.get("is_read", False):
                self.article_layout.addWidget(ArticleCard(article))

    def clear_article_layout(self):
        """現在のレイアウトをクリア"""
        for i in reversed(range(self.article_layout.count())):
            widget = self.article_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)
