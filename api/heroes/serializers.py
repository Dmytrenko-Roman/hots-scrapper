from rest_framework import serializers
from heroes.models import Hero


class HeroSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    title = serializers.CharField(required=True, allow_blank=False, max_length=200)
    role = serializers.CharField(required=True, allow_blank=False, max_length=10)
    type = serializers.CharField(required=True, allow_blank=False, max_length=50)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    difficulty = serializers.CharField(required=True, allow_blank=False, max_length=10)
    card_portrait = serializers.CharField(required=True, allow_blank=False, max_length=100)
    franchise = serializers.CharField(required=True, allow_blank=False, max_length=20)
    href = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data):
        return Hero.objects.create(**validated_data)
