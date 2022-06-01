from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

class Hero(Model):
    name = fields.TextField(pk=True)
    title = fields.TextField()
    role = fields.TextField()
    type = fields.TextField()
    description = fields.TextField()
    difficulty = fields.TextField()
    card_portrait = fields.TextField()
    franchise = fields.TextField()
    href = fields.TextField()

    def __str__(self):
        return self.name


hero_pydantic = pydantic_model_creator(cls=Hero, name="Hero")
hero_pydantic_in = pydantic_model_creator(cls=Hero, name="Hero", exclude_readonly=True)
