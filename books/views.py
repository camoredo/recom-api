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
        query_params = {
            "query": request.query_params.get('query'),
            "page": request.query_params.get('page')
        }
        serializer = self.get_serializer(data=query_params)
        serializer.is_valid(raise_exception=True)
        service = GoogleBooksService()

        return Response(
            service.search(
                query=serializer.data['query'], page=serializer.data['page']),
            status=status.HTTP_201_CREATED)
