from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import OrderForm
from plans.models import Plan


def checkout(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            messages.success(request, 'Order successfully placed!')
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'There was an error with your submission.')
    else:
        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'plan': plan,
    }

    return render(request, template, context)
