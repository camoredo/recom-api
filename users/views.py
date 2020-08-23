from django.db import transaction
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from users.serializers import RegistrationSerializer, UserSerializer


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            obj = User.objects.create_user(
                serializer.data['username'],
                serializer.data['email'],
                password=serializer.data['password'])

            user_serializer = UserSerializer(instance=obj)

            headers = self.get_success_headers(user_serializer.data)
            return Response(
                user_serializer.data, status=status.HTTP_201_CREATED,
                headers=headers)

        return Response({
            'message': 'Registration failed.'
        }, status=status.HTTP_400_BAD_REQUEST)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
