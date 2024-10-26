from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from ui.sidebar import Sidebar
from ui.article_card import ArticleCard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RSS Reader")
        self.setGeometry(100, 100, 800, 600)

        # メインレイアウト
        layout = QVBoxLayout()
        self.sidebar = Sidebar()
        self.article_list = QWidget()  # 記事カードをリスト化するエリア

        layout.addWidget(self.sidebar)
        layout.addWidget(self.article_list)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
