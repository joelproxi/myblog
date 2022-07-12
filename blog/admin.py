from typing import List
from django.contrib import admin


from .models import Category, Comment, Post
# Register your models here.

admin.site.register(Category)


@admin.register(Post)
class PostAmdin(admin.ModelAdmin):
    list_display = ('title', 'status','tags', 'created', 'publish', 'author')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body')
    ordering = ('author', 'status', 'publish')
    list_filter = ('author', 'created', 'publish')
    list_editable: List[str] = ['status', 'tags',]


@admin.register(Comment)
class Comments(admin.ModelAdmin):
    list_display = [ 'created']
