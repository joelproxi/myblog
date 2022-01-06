
from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    slug = serializers.SlugField(max_length=200)
    body = serializers.CharField()
    created = serializers.DateTimeField()
    total_post = serializers.SerializerMethodField(source='get_total_post')
    
    def get_total_post(self, obj):
        return Post.objects.all().count()