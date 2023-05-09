from django.shortcuts import render, redirect
from .models import Category, Post, Comment
from .forms import CategoryForm, PostForm, CommentForm

# Create your views here.


def community(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'community/community.html', {'posts': posts})
