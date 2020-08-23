from django.db import transaction
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from books.models import Book
from books.utils import Collection
from shelves.models import Recommendation
from shelves.serializer import RecommendationSerializer, RecommendSerializer


class RecommendView(CreateAPIView):
    serializer_class = RecommendSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            try:
                book = Book.objects.get(pk=serializer.data['book_id'])
            except Book.DoesNotExist:
                book = Collection().add_book(serializer.data['book_id'])

            receiver = User.objects.get(pk=serializer.data['to_user'])

            obj = Recommendation.objects.create(
                book=book,
                to_user=receiver)

            if 'message' in serializer.data:
                obj.message = serializer.data['message']

            obj.save()

            recommdation_serializer = RecommendationSerializer(instance=obj)

            headers = self.get_success_headers(recommdation_serializer.data)
            return Response(
                recommdation_serializer.data, status=status.HTTP_201_CREATED,
                headers=headers)
        return Response({
            'message': 'Failed to send recommendation'
        }, status=status.HTTP_400_BAD_REQUEST)
