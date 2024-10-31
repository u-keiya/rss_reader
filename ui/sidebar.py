from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QPushButton, QLabel, QHBoxLayout, QInputDialog
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt, pyqtSignal

class Sidebar(QWidget):
    # シグナル定義
    feed_selected = pyqtSignal(str)  # フィード選択時
    show_all_feeds = pyqtSignal()    # 全フィード表示
    show_favorites = pyqtSignal()    # お気に入り記事表示
    feed_added = pyqtSignal(str)     # 新しいRSSフィードの追加

    def __init__(self, feeds, parent=None):
        super().__init__(parent)

        # メインレイアウト（縦方向）
        layout = QVBoxLayout()

        # 1. フィード一覧の表示（未読記事数付き）
        self.feed_list = QListWidget()
        for feed in feeds:
            item = QListWidgetItem(f"{feed['name']}")# ({feed['unread_count']})")
            item.setData(Qt.UserRole, feed['name'])  # フィード名をデータとして保持
            self.feed_list.addItem(item)

        # フィードのクリックイベント接続
        self.feed_list.itemClicked.connect(self.on_feed_clicked)

        # 2. 全フィード表示とお気に入り表示ボタン
        all_feeds_button = QPushButton("全てのフィード")
        all_feeds_button.clicked.connect(self.show_all_feeds.emit)  # シグナル送信

        favorites_button = QPushButton("お気に入り")
        favorites_button.clicked.connect(self.show_favorites.emit)  # シグナル送信

        # RSS追加ボタン
        add_feed_button = QPushButton("RSSの追加")
        add_feed_button.clicked.connect(self.add_feed_dialog)

        # 3. 設定と検索のアイコンボタン
        icon_layout = QHBoxLayout()
        settings_button = self.create_icon_button("設定", "/home/kunon/apps/rss_reader/ui/icons/settings.png")
        search_button = self.create_icon_button("検索", "/home/kunon/apps/rss_reader/ui/icons/search.png")

        icon_layout.addWidget(settings_button)
        icon_layout.addWidget(search_button)

        # メインレイアウトに要素を順番に追加
        layout.addWidget(QLabel("フィード"))
        layout.addWidget(self.feed_list)
        layout.addWidget(all_feeds_button)
        layout.addWidget(favorites_button)
        layout.addWidget(add_feed_button)
        layout.addLayout(icon_layout)

        self.setLayout(layout)

    def create_icon_button(self, tooltip, icon_path):
        """アイコンボタンを作成するヘルパー関数"""
        button = QPushButton()
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(24, 24))
        button.setToolTip(tooltip)
        button.setFixedSize(40, 40)
        return button

    def on_feed_clicked(self, item):
        """クリックされたフィード名をシグナルで送信"""
        feed_name = item.data(Qt.UserRole)
        self.feed_selected.emit(feed_name)

    def add_feed_dialog(self):
        """RSSフィードのURLを入力するダイアログを表示"""
        url, ok = QInputDialog.getText(self, "Add RSS", "URL:")
        if ok and url:
            self.feed_added.emit(url)  # シグナルを送信