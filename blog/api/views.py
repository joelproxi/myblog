
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

from blog.models import Post
from .serializers import PostSerializer


@api_view()
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True )
    return Response(serializer.data)


@api_view()
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    serializer = PostSerializer(post)
    # print(serializer.data)
    return Response(serializer.data)
