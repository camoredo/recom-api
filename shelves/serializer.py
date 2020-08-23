from rest_framework import serializers
from django.contrib.auth.models import User

from books.serializers import BookSerializer
from books.utils import GoogleBooksService
from shelves.models import RECOMMENDATION_STATUS_CHOICES
from users.serializers import UserSerializer


class RecommendSerializer(serializers.Serializer):
    book_id = serializers.CharField(max_length=1000)
    to_user = serializers.IntegerField()
    message = serializers.CharField(max_length=1000, required=False)
    is_anonymous = serializers.BooleanField(default=False)

    def validate_to_user(self, value):
        try:
            User.objects.get(pk=value)
            return value
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist")

    def validate_book_id(self, value):
        google_books_service = GoogleBooksService()

        if (google_books_service.get_book(value)):
            return value
        raise serializers.ValidationError("Book does not exist")


class RecommendationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    book = BookSerializer()
    to_user = UserSerializer()
    from_user = UserSerializer(required=False)
    message = serializers.CharField(max_length=1000, required=False)
    status = serializers.ChoiceField(
        choices=RECOMMENDATION_STATUS_CHOICES, read_only=True)
