from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post, Comment
from .forms import CategoryForm, PostForm, CommentForm
from django.db.models import Count, Max

# Create your views here.


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


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by('created_at')
    return render(request, 'community/post_detail.html', {'post': post, 'comments': comments})


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'community/add_post.html', context)


def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user.profile
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'community/add_comment.html', context)
