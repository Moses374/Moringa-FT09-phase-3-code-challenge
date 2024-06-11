import unittest
from models.magazine import Magazine
from models.author import Author
from models.article import Article

class TestModels(unittest.TestCase):

    def test_magazine_invalid_name(self):
        with self.assertRaises(ValueError):
            Magazine(1, name="A")

    def test_magazine_invalid_category(self):
        with self.assertRaises(ValueError):
            Magazine(1, category="")

    def test_author_invalid_name(self):
        with self.assertRaises(ValueError):
            Author(1, name="")

    def test_article_invalid_title(self):
        with self.assertRaises(ValueError):
            Article(1, title="A", content="Valid content", author_id=1, magazine_id=1)

if __name__ == '__main__':
    unittest.main()
