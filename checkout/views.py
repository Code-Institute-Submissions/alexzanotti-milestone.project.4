from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
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
    }

    return render(request, template, context)
