from .models import Post, Comment
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.contrib.auth.models import User
from user.models import Profile
from django.db.models import Q

from .form import CustomUserCreationForm, PostForm, ProfileForm, CommentForm

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-created')
    context = {
        'posts' : posts,
    }
    return render(request, 'core/home.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        messages.success(request, 'You are Logged in.')
        return redirect('profile')
    else:
        messages.error(request, 'Username or Password not invalid')

    return render(request, 'core/login.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')

def register(request):

    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Thank you for registration.')
            login(request, user)
            return redirect('profile')
        else:
            messages.success(request, 'Error during registration.')
    context = {
        'form':form,
    }
    return render(request, 'core/register.html', context)

@login_required(login_url='login')
def create_post(request):
    profile = request.user.profile
    form = PostForm()
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            project = form.save()
            project.owner = profile
            project.save()
            return redirect('profile')
    context = {
        'form':form,
    }
    return render(request, 'core/create_post.html',context)

def post(request, id):

    post = Post.objects.get(pk=id)
    
    comments = Comment.objects.filter(post_id=post.id)

    count = comments.count()

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.post = post
        comment.owner = request.user.profile
        comment.save()


        messages.success(request, 'Your review was successfully.')
        return redirect('post', pk=post.id)
    
    context = {
        'post':post,
        'comments': comments,
        'count': count,
        'form': form,
    }
    
    return render(request, 'core/post.html', context)
    
    