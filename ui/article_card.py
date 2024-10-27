import webbrowser
from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QDialog
)
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt

"""
card
+------------------------------------------+
| [サムネイル画像]                         |
+------------------------------------------+
| タイトル                                 |
| 公開日時                                |
| 記事の概要（省略表示）                   |
+------------------------------------------+
|                             [☆ お気に入り] |
+------------------------------------------+

popup
+------------------------------+
| タイトル（クリックでリンク） |
+------------------------------+
| 記事の全サマリー             |
|                              |
+------------------------------+
| [Close]                      |
+------------------------------+
"""

class ArticleCard(QWidget):
    def __init__(self, article, parent=None):
        super().__init__(parent)

        # 記事データを保持
        self.article = article
        self.is_read = article.get("is_read", False)
        self.is_favorite = article.get("is_favorite", False)

        # カード全体のレイアウト（縦方向）
        main_layout = QVBoxLayout()

        # サムネイル画像の設定
        thumbnail = QLabel(self)
        pixmap = QPixmap(article.get("thumbnail", ""))
        if not pixmap.isNull():
            thumbnail.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio))
        else:
            thumbnail.setText("No Image")
            thumbnail.setAlignment(Qt.AlignCenter)

        # 記事情報のレイアウト
        info_layout = QVBoxLayout()
        title_label = QLabel(article.get("title", "No Title"), self)
        title_label.setWordWrap(True)
        title_label.setStyleSheet("font-weight: bold;" if not self.is_read else "")
        title_label.setCursor(QCursor(Qt.PointingHandCursor))

        date_label = QLabel(article.get("published", "No Date"), self)
        summary_label = QLabel(article.get("summary", "No Summary"), self)
        summary_label.setWordWrap(True)
        summary_label.setMaximumHeight(70)

        # お気に入りボタンの追加
        self.favorite_button = QPushButton(self)
        self.update_favorite_button()  # 初期状態に応じたラベルの設定
        self.favorite_button.clicked.connect(self.toggle_favorite)  # イベント接続

        # レイアウトに要素を追加
        info_layout.addWidget(title_label)
        info_layout.addWidget(date_label)
        info_layout.addWidget(summary_label)

        # ボタン用のレイアウト（横方向）
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # ボタンを右側に寄せる
        button_layout.addWidget(self.favorite_button)

        # メインレイアウトに要素を順番に追加
        main_layout.addWidget(thumbnail)  # サムネイルを上に配置
        main_layout.addLayout(info_layout)  # 記事情報を追加
        main_layout.addLayout(button_layout)  # ボタンレイアウトを追加

        self.setLayout(main_layout)  # メインレイアウトを適用

        # イベント接続
        self.mousePressEvent = self.show_popup  # カードクリック時のイベント

    def toggle_favorite(self):
        """お気に入り状態をトグルする"""
        self.is_favorite = not self.is_favorite
        self.update_favorite_button()  # ボタンのラベルを更新
        print(f"お気に入り状態: {self.is_favorite}")

    def update_favorite_button(self):
        """お気に入りボタンのラベルを更新"""
        if self.is_favorite:
            self.favorite_button.setText("★ お気に入り")
        else:
            self.favorite_button.setText("☆ お気に入り")

    def show_popup(self, event):
        """記事の詳細を表示するポップアップウィンドウを開く"""
        popup = QDialog(self)
        popup.setWindowTitle(self.article.get("title", "No Title"))
        popup.setGeometry(300, 300, 400, 300)

        popup_layout = QVBoxLayout()

        title_label = QLabel(self.article.get("title", "No Title"), popup)
        title_label.setStyleSheet("font-weight: bold; color: blue;")
        title_label.setCursor(QCursor(Qt.PointingHandCursor))
        title_label.mousePressEvent = self.open_in_browser  # ブラウザで開くイベント

        summary_label = QLabel(self.article.get("summary", "No Summary"), popup)
        summary_label.setWordWrap(True)

        close_button = QPushButton("Close", popup)
        close_button.clicked.connect(popup.close)

        popup_layout.addWidget(title_label)
        popup_layout.addWidget(summary_label)
        popup_layout.addWidget(close_button)

        popup.setLayout(popup_layout)
        popup.exec_()

    def open_in_browser(self, event):
        """記事のリンクをブラウザで開く"""
        url = self.article.get("link", "#")
        if url != "#":
            webbrowser.open(url)
        else:
            print("リンクがありません")
