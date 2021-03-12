from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "Username is already being used")
        if len(value) > 100:
            raise serializers.ValidationError(
                "Username must not exceed 100 characters")
        return value

    def validate_password(self, value):
        if value.isdecimal():
            raise serializers.ValidationError(
                "Password should contain non-numeric characters")
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password should at least be 8 characters")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already being used")
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
