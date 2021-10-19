
from django.shortcuts import render, get_object_or_404
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,

)
from django.views import generic
from .models import Category, Comment, Post
from blog.forms import CommentForm

# Create your views here.


def post_list(request, category=None):
    posts = Post.published.all()
    categories = Category.objects.all()
    if category:
        category = get_object_or_404(Category, slug=category)
        posts = posts.filter(category=category).order_by("publish")
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'page': page,
        'categories': categories,
        'category': category,
    }
    return render(request, 'blog/post/list.html', context)

# class PostListView(generic.ListView):
#     queryset = Post.objects.all()
#     paginate_by = 2
#     template_name = 'blog/post/list.html'
#     context_object_name = 'posts'


def post_detail(request, year: int, month: int, day: int, slug: str):
    post = get_object_or_404(Post, slug=slug, status='published',
                             publish__year=year, publish__month=month, publish__day=day)
    comments = Comment.objects.filter(post=post.id)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            username = comment_form.cleaned_data['username']
            email = comment_form.cleaned_data['email']
            body = comment_form.cleaned_data['body']
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post/detail.html', {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'new_comment': new_comment,
        'comment_form': comment_form,
    })
