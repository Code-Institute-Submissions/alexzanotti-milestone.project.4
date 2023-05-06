from django.shortcuts import render, get_object_or_404
from .models import Plan

# Create your views here.


def plans(request):
    """ A view to render the plans page """

    plans = Plan.objects.all()

    context = {
        'plans': plans,
    }

    return render(request, 'plans/plans.html', context)


def plan_sales_page(request, plan_id):
    """ A view to show the sales page for each individual plan """

    plan = get_object_or_404(Plan, pk=plan_id)

    context = {
        'plan': plan,
    }

    return render(request, 'plans/plan_sales_page.html/', context)
