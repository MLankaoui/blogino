from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

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

    if request.method == 'POST':
        user = request.user
        content = request.POST['content']

        comment = Comment(user=user, post=post, content=content)
        comment.save()

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


@login_required
def create_post(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    if request.method == 'POST':
        title = request.POST['title']
        user = request.user
        content = request.POST['content']
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)

        post = Post(title=title, user=user, content=content, category=category)
        post.save()

        context['success'] = 'Post created successfully!'
    
    return render(request, 'landing/create_post.html', context)


@login_required
def dashboard(request):
    categories = Category.objects.all()
    user = request.user
    posts = Post.objects.filter(user=request.user)
    all_posts = Post.objects.all()

    context = {
        'categories': categories,
        'posts': posts,
        'user': user,
        'all_posts': all_posts,
    }
    return render(request, 'landing/dashboard.html', context)


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    categories = Category.objects.all()
    
    if post.user != request.user:
    messages.error(request, "You cant edit this post")
    return redirect('landing:dashboard')

    context = {
        'post': post,
        'categories': categories,
    }

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        category_id = request.POST['category']
        post.category = Category.objects.get(id=category_id)

        post.save()

        context['success'] = 'Post updated successfully!'

    return render(request, 'landing/edit_post.html', context)



@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
     if post.user != request.user:
        messages.error(request, "You cannot delete this post as it doesn't belog to you!")
        return redirect('landing:dashboard')
         
    post.delete()

    return redirect('landing:index')


@login_required
def logout_view(request):
    logout(request)
    return redirect('landing:index')


def signup_view(request):
    return redirect('landing:index')


@login_required
def create_category(request):
    if request.method == 'POST':
        name = request.POST['name']

        category = Category(name=name)
        category.save()

    return redirect('landing:dashboard')



@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()

    return redirect('landing:dashboard')



@login_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()

    return redirect('landing:dashboard')
