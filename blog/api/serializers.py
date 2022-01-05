
from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    slug = serializers.SlugField(max_length=200)
    body = serializers.CharField()
    created = serializers.DateTimeField()