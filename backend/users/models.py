from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    #codeforces_username
    cf_handle = models.CharField(max_length=255, unique=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []