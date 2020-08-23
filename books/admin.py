from django.contrib import admin

from books.models import Author, Book, Category, Cover, Publisher
# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Cover)
admin.site.register(Publisher)
