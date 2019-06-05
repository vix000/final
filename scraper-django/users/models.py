from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    address = models.CharField(max_length=255)

