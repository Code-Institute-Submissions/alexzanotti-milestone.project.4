from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Plan, Category

# Create your views here.

"""
def plans(request):
     A view to render the plans page 

    plans = Plan.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(
                category__name__icontains=query)
            plans = plans.filter(queries)

    context = {
        'plans': plans,
        'search_term': query,
    }

    return render(request, 'plans/plans.html', context)
"""


def plans(request):
    """ A view to render the plans page """

    plans = Plan.objects.all()
    query = None
    categories = Category.objects.all()

    if request.GET:
        if 'category' in request.GET:
            selected_categories = request.GET['category'].split(',')
            plans = plans.filter(category__name__in=selected_categories)
            categories = Category.objects.filter(name__in=selected_categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('plans'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(
                category__name__icontains=query)
            plans = plans.filter(queries)

    context = {
        'plans': plans,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'plans/plans.html', context)



def plan_sales_page(request, plan_id):
    """ A view to show the sales page for each individual plan """

    plan = get_object_or_404(Plan, pk=plan_id)

    context = {
        'plan': plan,
    }

    return render(request, 'plans/plan_sales_page.html/', context)
