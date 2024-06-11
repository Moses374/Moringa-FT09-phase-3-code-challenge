from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                       (self.title, self.content, self.author_id, self.magazine_id))
        self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @property
    def title(self):
        if not hasattr(self, '_title'):
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT title FROM articles WHERE id = ?", (self.id,))
            result = cursor.fetchone()
            conn.close()
            if result:
                self._title = result[0]
            else:
                raise ValueError("Title not found in database")
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        if not (5 <= len(value) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value

    @property
    def content(self):
        if not hasattr(self, '_content'):
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT content FROM articles WHERE id = ?", (self.id,))
            result = cursor.fetchone()
            conn.close()
            if result:
                self._content = result[0]
            else:
                raise ValueError("Content not found in database")
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise ValueError("Content must be a string")
        self._content = value

    def __repr__(self):
        return f'<Article {self.title}>'
