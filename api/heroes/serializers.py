from rest_framework import serializers
from heroes.models import Hero


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = [
            "name",
            "title",
            "role",
            "type",
            "description",
            "difficulty",
            "card_portrait",
            "franchise",
            "href",
        ]

    def create(self, validated_data):
        return Hero.objects.create(**validated_data)
