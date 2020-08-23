from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from decouple import config

from books.models import Author, Book, Category, Cover, Publisher


class GoogleBooksService():
    def __init__(self):
        self.service = build(
            'books', 'v1', developerKey=config('GOOGLE_API_KEY'))

    def get_book(self, id):
        request = self.service.volumes().get(volumeId=id)
        try:
            response = request.execute()
        except HttpError:
            response = None
        return response

    def search(self, query):
        request = self.service.volumes().list(q=query)
        return request.execute()


class Collection():
    def __init__(self):
        self.google_books_service = GoogleBooksService()

    def add_book(self, id):
        raw_book = self.google_books_service.get_book(id)

        publisher = self.get_or_add_publisher(
            raw_book['volumeInfo']['publisher'])

        cover = self.add_cover(
            raw_book['volumeInfo']['imageLinks'])

        book = Book.objects.create(
            id=id, etag=raw_book['etag'],
            title=raw_book['volumeInfo']['title'],
            cover=cover,
            publisher=publisher,
            date_published=raw_book['volumeInfo']['publishedDate'],
            link=raw_book['volumeInfo']['infoLink']
        )

        if 'description' in raw_book['volumeInfo']:
            book.description = raw_book['volumeInfo']['description'],

        if 'authors' in raw_book['volumeInfo']:
            for item in raw_book['volumeInfo']['authors']:
                author = self.get_or_add_author(item)
                book.authors.add(author)

        if 'categories' in raw_book['volumeInfo']:
            for item in raw_book['volumeInfo']['categories']:
                category = self.get_or_add_category(item)
                book.categories.add(category)
        book.save()

        return book

    def add_cover(self, images):
        cover = Cover()

        if 'smallThumbnail' in images:
            cover.small_thumbnail = images['smallThumbnail']

        if 'thumbnail' in images:
            cover.small_thumbnail = images['thumbnail']

        if 'small' in images:
            cover.small_thumbnail = images['small']

        if 'medium' in images:
            cover.small_thumbnail = images['medium']

        if 'large' in images:
            cover.small_thumbnail = images['large']
        cover.save()
        return cover

    def get_or_add_author(self, name):
        try:
            return Author.objects.get(name=name)
        except Author.DoesNotExist:
            author = Author.objects.create(name=name)
            return author

    def get_or_add_category(self, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            category = Category.objects.create(name=name)
            return category

    def get_or_add_publisher(self, name):
        try:
            return Publisher.objects.get(name=name)
        except Publisher.DoesNotExist:
            publisher = Publisher.objects.create(name=name)
            return publisher
