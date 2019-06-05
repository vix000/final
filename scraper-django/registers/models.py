from django.db import models
from users.models import MyUser


class Registry(models.Model):
    query_string = models.CharField('String that user was searching for', max_length=100)
    date = models.DateTimeField('query time', auto_now_add=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='registries')


class Entry(models.Model):
    name = models.CharField(
        'String that user was searching for', max_length=100)
    price = models.IntegerField()
    link = models.CharField(max_length=200)
    photo = models.CharField(blank=True, max_length=200)
