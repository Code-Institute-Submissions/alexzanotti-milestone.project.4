from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post, Comment
from .forms import CategoryForm, PostForm, CommentForm
from django.db.models import Count, Max

# Create your views here.

"""
def community(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'community/community.html', {'posts': posts})
"""


def community(request):
    categories = Category.objects.annotate(
        num_posts=Count('post'),
        latest_post_date=Max('post__created_at')
    )
    return render(request, 'community/community.html', {'categories': categories})


def community_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'community/community_category.html', {'category': category, 'posts': posts})
