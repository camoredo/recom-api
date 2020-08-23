from rest_framework import serializers

from books.models import Author, Publisher, Category, Cover


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover
        fields = ['id', 'small_thumbnail', 'thumbnail',
                  'small', 'medium', 'large', 'extra_large']


class BookSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=1000)
    etag = serializers.CharField(max_length=1000)
    title = serializers.CharField(max_length=1000)
    description = serializers.CharField(max_length=1000)
    authors = AuthorSerializer(many=True)
    categories = CategorySerializer(required=False, many=True)
    cover = CoverSerializer()
    publisher = PublisherSerializer()
    date_published = serializers.DateTimeField()
    link = serializers.DateTimeField()
