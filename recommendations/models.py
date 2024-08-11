# recommendations\models.py

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genres = models.TextField(max_length=255, default='Unknown')
    item_id = models.IntegerField(default=1, unique=True)

    def __str__(self):
        return self.title
