from django.db.models import fields
from django.forms.widgets import TextInput, Textarea
from blog.models import Comment
from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=Textarea(attrs={'class': 'form-control', 'rows': 3}))
    
    class Meta:
        model = Comment
        fields = [ 'body']
        

class SearchPost(forms.Form):
    query = forms.CharField(max_length=200)
    
    class Meta:
        fields = [ 'query']
        
        

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'tags',)
        

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(max_length=500, widget=forms.Textarea)
    