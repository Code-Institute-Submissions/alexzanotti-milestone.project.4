from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import Profile
import stripe


# Create your views here.


def donate(request):
    bag = request.session.get('bag', {})

    template = 'donate/donate.html'
    context = {
        'stripe_public_key': 'pk_test_51N6fG5HqHvT2PvVfoDyps16JYahKvD5EWT5r9pJJuxB5LvRCoqUrWa97j1AFxXEYbk6rVhIRKJmV3FVNSmbIcFe100qZsIuw07',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
