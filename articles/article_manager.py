class ArticleManager:
    def __init__(self):
        self.read_articles = set()
        self.favorite_articles = []

    def mark_as_read(self, article_id):
        self.read_articles.add(article_id)

    def add_to_favorites(self, article):
        self.favorite_articles.append(article)

    def remove_from_favorites(self, article):
        self.favorite_articles.remove(article)
