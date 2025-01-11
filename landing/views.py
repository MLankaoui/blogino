from django.shortcuts import render, get_object_or_404
from .models import Category, Post

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

    context = {
        'post': post,
        'categories': categories,
    }
    return render(request, 'landing/post_detail.html', context)