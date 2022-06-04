from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    role = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    description = models.TextField()
    difficulty = models.CharField(max_length=10)
    card_portrait = models.CharField(max_length=100)
    franchise = models.CharField(max_length=20)
    href = models.CharField(max_length=100)

    class Meta:
        ordering = ["franchise"]
