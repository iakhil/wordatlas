from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length=50)
    player = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    meaning = models.TextField()


class WordAtlasUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    high_score = models.IntegerField(default=0)
