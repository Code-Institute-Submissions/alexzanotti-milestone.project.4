from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Plan, Category, Comment
from .forms import CategoryForm, PlanForm, CommentForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.


def plans(request):
    """ A view to render the plans page """

    plans = Plan.objects.all()
    query = None
    categories = Category.objects.all()
    sort_by = 'default'

    if request.GET:
        if 'category' in request.GET:
            selected_categories = request.GET['category'].split(',')
            plans = plans.filter(category__name__in=selected_categories)
            categories = Category.objects.filter(name__in=selected_categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('plans:plans'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(
                category__name__icontains=query)
            plans = plans.filter(queries)

        sort_by = request.GET.get('sort_by')

        if sort_by and sort_by != 'default':
            if '_' in sort_by:
                sort_parts = sort_by.split('_')
                sort_field, order = sort_parts[0], sort_parts[1]
                if order == 'desc':
                    sort_field = f'-{sort_field}'
                if sort_field in ['category', '-category', 'name', '-name']:
                    plans = plans.order_by(sort_field)

    context = {
        'plans': plans,
        'search_term': query,
        'current_categories': categories,
        'current_sort_by': sort_by,
    }

    return render(request, 'plans/plans.html', context)


def plan_description(request, plan_id):
    """ A view to show the sales page for each individual plan """

    plan = get_object_or_404(Plan, pk=plan_id)
    comments = Comment.objects.filter(plan=plan)
    form = CommentForm()

    context = {
        'plan': plan,
        'comments': comments,
        'form': form
    }

    return render(request, 'plans/plan_description.html', context)



def plan_management(request):
    categories = Category.objects.all()
    plans = Plan.objects.all()

    return render(request, 'plans/plan_management.html', {'categories': categories, 'plans': plans})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plans:plan_management')
    else:
        form = CategoryForm()

    return render(request, 'plans/add_category.html', {'form': form})


def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('plans:plan_management')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'plans/edit_category.html', {'form': form, 'category': category})


def delete_category(request, category_id):
    if request.method == 'POST':
        category = get_object_or_404(Category, pk=category_id)
        category.delete()
        messages.success(
            request, f'Category "{category.name}" has been deleted!')
        return redirect('plans:plan_management')
    return redirect('plans:plan_management')


@login_required
def add_plan(request):
    if request.method == "POST":
        form = PlanForm(request.POST, request.FILES)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.author = request.user.profile
            plan.save()
            return redirect(reverse('plans:plan_description', args=[plan.id]))
    else:
        form = PlanForm()

    context = {
        'form': form,
    }
    return render(request, 'plans/add_plan.html', context)


@login_required
def edit_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('plans:plan_management')
    else:
        form = PlanForm(instance=plan)
    return render(request, 'plans/edit_plan.html', {'form': form, 'plan': plan})


def delete_plan(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)
    plan.delete()
    messages.success(request, 'Plan deleted successfully!')
    return redirect('plans:plan_management')


@login_required
def add_comment(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user.profile
            comment.plan = plan
            comment.save()
            return redirect(reverse('plans:plan_description', args=[plan.id]))
    else:
        form = CommentForm()

    context = {
        'form': form,
        'plan': plan,
    }
    return render(request, 'plans/add_comment.html', context)


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('plans:plan_management')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'plans/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('plans:plan_management')


@login_required
def my_plans(request):
    user_plans = Plan.objects.filter(author=request.user.profile)
    user_comments = Comment.objects.filter(author=request.user.profile)
    return render(request, 'plans/my_plans.html', {'plans': user_plans, 'comments': user_comments})
