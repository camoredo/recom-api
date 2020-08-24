from django.db import transaction
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from books.models import Book
from books.utils import Collection
from shelves.models import Recommendation
from shelves.permissions import IsAuthenticatedOrCreateOnly
from shelves.serializer import RecommendationSerializer, RecommendSerializer


class RecommendView(APIView):
    permission_classes = (IsAuthenticatedOrCreateOnly,)

    def post(self, request, *args, **kwargs):
        serializer = RecommendSerializer(data=request.data)
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

            if (not serializer.data['is_anonymous']
                    and request.user.is_authenticated):
                obj.from_user = request.user

            obj.save()

            recommendation_serializer = RecommendationSerializer(instance=obj)
            return Response(
                recommendation_serializer.data, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Failed to send recommendation'
        }, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        serializer = RecommendationSerializer(
            request.user.recommendations, many=True)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED)
