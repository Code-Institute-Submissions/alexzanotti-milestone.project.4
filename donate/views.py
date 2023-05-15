from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from profiles.models import Profile
import os
import stripe


def donate(request):

    stripe_public_key = os.environ.get('STRIPE_PUBLIC_KEY')
    stripe_secret_key = os.environ.get('STRIPE_SECRET_KEY')

    stripe_total = 1000
    stripe.api_key = stripe_secret_key

    if request.method == 'POST':
        # Get the user's profile
        profile = Profile.objects.get(profile_user=request.user)

        # Update the user's donation status
        profile.donated = True
        profile.save()

        # Create the Stripe payment
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Redirect to the success page
        return redirect('donate_success')
    else:
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        template = 'donate/donate.html'
        context = {
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def donate_success(request):
    """ A view to render the donation success page """
    return render(request, 'donate/donate_success.html')