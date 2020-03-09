from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    round = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    goals = models.TextField(blank=True)
    squad = models.TextField()
    cards = models.TextField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title
