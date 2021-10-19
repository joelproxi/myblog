from django.db.models import fields
from django.forms.widgets import TextInput, Textarea
from blog.models import Comment
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=Textarea(attrs={'class': 'form-control', 'rows': 3}))
    class Meta:
        model = Comment
        fields = ['username', 'email', 'body']