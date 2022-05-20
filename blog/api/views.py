

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView

from blog.models import Comment, Post
from .serializers import AddPostSerializer, CommentSerializer, PostListSerializer, PostSerializer


@api_view(['POST', 'GET'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.select_related('category').all()
        serializer = PostListSerializer(posts, many=True , context={"request": request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AddPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

    
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view()
def category_detail(request, pk):
    return Response(pk)


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    

class CommentDetailUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    

# class CommentUpdateAPIView(UpdateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer