

from rest_framework import serializers

from blog.models import Category, Comment, Post


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    slug = serializers.SlugField()
    
    class Meta:
        model = Category
        fields = ['id', 'name']


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ( "id",
                "body",
                "post",
                "created",
                "author",)
        
        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'category', 'author', 'created', 'comments' ]
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=200)
    # slug = serializers.SlugField(max_length=200)
    # body = serializers.CharField()
    # created = serializers.DateTimeField()
    # # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # # category = serializers.StringRelatedField()
    category = CategorySerializer()
    
    # category = serializers.HyperlinkedRelatedField(view_name='category-detail', queryset=Category.objects.all())

class PostListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'category', 'author', 'created']

    category = CategorySerializer()
    
   
class AddPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = [ 'title', 'body', 'category', 'author']
 

