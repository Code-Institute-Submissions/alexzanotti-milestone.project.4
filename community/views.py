from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post, Comment
from .forms import CategoryForm, PostForm, CommentForm
from django.db.models import Count, Max
from django.urls import reverse


# Create your views here.


def check_superuser(user):
    return user.is_superuser


def user_is_author(user, obj):
    return obj.author == user.profile


def user_can_edit(user, obj):
    return user.is_superuser or user_is_author(user, obj)


def community(request):
    categories = Category.objects.annotate(
        num_posts=Count('post'),
        latest_post_date=Max('post__created_at')
    )
    return render(request, 'community/community.html', {'categories': categories})


def community_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category).annotate(comment_count=Count('comments'))
    return render(request, 'community/community_category.html', {'category': category, 'posts': posts})



def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by('created_at')
    return render(request, 'community/post_detail.html', {'post': post, 'comments': comments})


@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect(reverse('community:post_detail', args=[post.id]))
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'community/add_post.html', context)


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user.profile
            comment.post = post
            comment.save()
            return redirect(reverse('community:post_detail', args=[post.id]))
    else:
        form = CommentForm()

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'community/add_comment.html', context)


@user_passes_test(check_superuser, login_url='home')
def community_management(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    comments = Comment.objects.all()
    context = {
        'categories': categories,
        'posts': posts,
        'comments': comments,
    }
    return render(request, 'community/community_management.html', context)


@user_passes_test(check_superuser, login_url='home')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community:community_management')
    else:
        form = CategoryForm()
    return render(request, 'community/add_category.html', {'form': form})


@user_passes_test(check_superuser, login_url='home')
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('community:community_management')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'community/edit_category.html', {'form': form, 'category': category})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if not user_can_edit(request.user, post):
        return redirect('home')
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('community:community_management')
    else:
        form = PostForm(instance=post)
    return render(request, 'community/edit_post.html', {'form': form, 'post': post})


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if not user_can_edit(request.user, comment):
        return redirect('home')
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('community:community_management')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'community/edit_comment.html', {'form': form, 'comment': comment})


@user_passes_test(check_superuser, login_url='home')
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('community:community_management')


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if not user_can_edit(request.user, post):
        return redirect('home')
    post.delete()
    return redirect('community:community_management')


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if not user_can_edit(request.user, comment):
        return redirect('home')
    comment.delete()
    return redirect('community:community_management')


@login_required
def my_posts(request):
    user_posts = Post.objects.filter(author=request.user.profile)
    user_comments = Comment.objects.filter(author=request.user.profile)
    return render(request, 'community/my_posts.html', {'posts': user_posts, 'comments': user_comments})

