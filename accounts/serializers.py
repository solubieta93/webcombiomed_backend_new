from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_superuser']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_data, is_admin=False):
        print(validate_data)

        creator = User.objects.create_superuser if is_admin else User.objects.create_user
        user = creator(
            validate_data['username'],
            validate_data['email'],
            validate_data['password'])
        return user


class RegisterAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_data):
        user = User.objects.create_superuser(
            validate_data['username'],
            validate_data['email'],
            validate_data['password'])
        return user


class LoginSerializer(serializers.ModelSerializer):
    # username
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        # email
        fields = ('username', 'password')

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

