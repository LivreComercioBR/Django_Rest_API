from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser, UserManager):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=264, unique=True)
    password = models.CharField(max_length=264)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username
