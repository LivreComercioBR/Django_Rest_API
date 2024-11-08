from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializer import UserSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


class CreateUser(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @extend_schema(parameters='username, email and password are required',
                   responses=UserSerializer)
    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username')
        email = self.request.query_params.get('email')
        password = self.request.query_params.get('password')
        if username is not None:
            username = queryset.filter(username=username)
        if email is not None:
            email = queryset.filter(email=email)
        if password is not None:
            password = queryset.filter(password=password)
        return queryset


class UserList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ListUsers(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UpdateUser(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_user(self, request):
        queryset = User.objects.all()
        username = request.query_params.get('username')
        email = request.query_params.get('email')
        password = request.query_params.get('password')

        if username is not None:
            username = queryset.filter(username=username)
        if email is not None:
            email = queryset.filter(email=email)
        if password is not None:
            password = queryset.filter(password=password)

        return queryset


class DeleteUser(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_user(self, request):
        queryset = User.objects.all()
        username = request.query_params.get('username')

        if username is not None:
            username = queryset.filter(username=username)

        return queryset
