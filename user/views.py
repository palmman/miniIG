from django.shortcuts import render, redirect
from .models import Profile
from core.models import Post
from django.contrib.auth.decorators import login_required
from core.form import ProfileForm

# Create your views here.

@login_required(login_url='login')
def profile(request):

    userprofile = Profile.objects.get(user_id=request.user.id)
    post = Post.objects.filter(owner=userprofile.id)
    context = {
        'userprofile': userprofile,
        'post' : post,
    }
    return render(request, 'user/user.html', context)

def profile_feed(request, id):

    user = Profile.objects.get(pk=id)
    post = Post.objects.filter(owner_id=user.id)
    context = {
        'user': user,
        'post': post,
    }
    return render(request, 'user/user_profile.html', context)

@login_required(login_url='login')
def edit_profile(request):

    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    context = {
       'form':form,
    }
    return render(request, 'user/edit_profile.html', context)