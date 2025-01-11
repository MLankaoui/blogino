from django.shortcuts import render, get_object_or_404
from .models import Category, Post, Comment

# Create your views here.
def index(request):
    categories = Category.objects.all()
    posts = Post.objects.order_by('-created_at')[:4]

    context = {
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'landing/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    categories = Category.objects.all()
    comments = Comment.objects.filter(post=post)

    context = {
        'post': post,
        'categories': categories,
        'comments': comments,
    }
    return render(request, 'landing/post_detail.html', context)


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    categories = Category.objects.all()
    posts = Post.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'landing/category.html', context)