from tortoise.models import Model
from tortoise import fields


class Hero(Model):
    name = fields.TextField(pk=True)
    title = fields.TextField()
    role = fields.TextField()
    type = fields.TextField()
    description = fields.TextField()
    difficulty = fields.TextField()
    card_portrait = fields.TextField(unique=True)
    franchise = fields.TextField()
    href = fields.TextField()
