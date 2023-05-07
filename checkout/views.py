from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import OrderForm
from plans.models import Plan  # Assuming your Plan model is in the 'plans' app


def checkout(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            messages.success(request, 'Order successfully placed!')
            # Replace 'success_page' with the actual name of your success page's URL pattern
            return redirect(reverse('success_page'))
        else:
            messages.error(
                request, 'There was an error with your submission. Please check your information and try again.')
    else:
        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'plan': plan,  # Add the plan to the context
    }

    return render(request, template, context)
