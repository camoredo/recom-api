from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from books.serializers import QuerySerializer
from books.utils import GoogleBooksService


class SearchView(RetrieveAPIView):
    serializer_class = QuerySerializer

    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = GoogleBooksService()

        return Response(
            service.search(serializer.data['query']),
            status=status.HTTP_201_CREATED)
