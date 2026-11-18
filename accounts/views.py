from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Post

def home_view(request):
    categories = Category.objects.all()
    return render(request, 'accounts/home.html', {'categories': categories})

def category_detail_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all().order_by('-created_at')
    return render(request, 'accounts/category_detail.html', {'category': category, 'posts': posts})

@login_required
def create_post_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Post.objects.create(category=category, title=title, content=content, author=request.user)
            messages.success(request, 'Your post has been created!')
            return redirect('category_detail', slug=category.slug)
    return render(request, 'accounts/create_post.html', {'category': category})

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'accounts/post_detail.html', {'post': post})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

    return redirect('home')