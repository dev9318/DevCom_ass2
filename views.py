from django.shortcuts import render
from .models import Post, Login
from django.utils import timezone
from .forms import loginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def login_new(request):
    form = loginForm()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/login.html', {'form': form,'posts':posts})
def user_login(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        password = request.POST.get('password')
        form = loginForm()
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        user = authenticate(author=author, password=password)
        if user:
            login(request,user)
            return render(request, 'blog/login.html', {'form': form,'posts':posts})
def post_new(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
