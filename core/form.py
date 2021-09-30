from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_image', 'email', 'username']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'featured_image']


    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class CommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ['body',]

        labels = {
            'body': 'Add a comment'
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})