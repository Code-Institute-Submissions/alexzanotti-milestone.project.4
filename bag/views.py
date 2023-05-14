from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

from django.contrib import messages

from plans.models import Plan

# Create your views here.


def add_to_bag(request, item_id):
    """ Add a single quantity of the specified plan to the shopping bag """

    bag = request.session.get('bag', {})

    if item_id not in bag:
        bag[item_id] = 1

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect('checkout:checkout')
