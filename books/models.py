from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=1000)


class Publisher(models.Model):
    name = models.CharField(max_length=1000)


class Category(models.Model):
    name = models.CharField(max_length=1000)


class Cover(models.Model):
    small_thumbnail = models.CharField(max_length=1000, blank=True, null=True)
    thumbnail = models.CharField(max_length=1000, blank=True, null=True)
    small = models.CharField(max_length=1000, blank=True, null=True)
    medium = models.CharField(max_length=1000, blank=True, null=True)
    large = models.CharField(max_length=1000, blank=True, null=True)


class Book(models.Model):
    id = models.CharField(max_length=1000, primary_key=True)
    etag = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, blank=True, null=True)
    authors = models.ManyToManyField(Author, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    cover = models.OneToOneField(
        Cover, on_delete=models.DO_NOTHING, blank=True, null=True)
    publisher = models.ForeignKey(
        Publisher,
        related_name="books",
        on_delete=models.DO_NOTHING,
        blank=True
    )
    date_published = models.CharField(max_length=200)
    link = models.CharField(max_length=1000)
