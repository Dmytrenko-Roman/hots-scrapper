from django.db import models


class Hero(models.Model):
    name = models.TextField()
    title = models.TextField()
    role = models.TextField()
    type = models.TextField()
    description = models.TextField()
    difficulty = models.TextField()
    card_portrait = models.TextField()
    franchise = models.TextField()
    href = models.TextField()

    class Meta:
        ordering = ["franchise"]
