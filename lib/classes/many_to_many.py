class Author:
    def __init__(self, name):
        self._name = self._validate_name(name)
        self._articles = []

    @property
    def name(self):
        return self._name

    def _validate_name(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        return name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine.add_article(article)
        return article

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles)) if self._articles else None


class Magazine:
    def __init__(self, name, category):
        self._name = self._validate_name(name)
        self._category = self._validate_category(category)
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._validate_name(value)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = self._validate_category(value)

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        return name

    def _validate_category(self, category):
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        return category

    def articles(self):
        return self._articles

    def add_article(self, article):
        self._articles.append(article)

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1

        return [author for author, count in author_counts.items() if count > 2] if author_counts else None


class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not hasattr(self, '_title'):
            self._validate_title(value)
            self._title = value
        else:
            raise AttributeError("title cannot be changed after initialization")

    def _validate_title(self, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")

