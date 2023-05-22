from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from profiles.models import Profile
from donate.models import Donation
import os
import stripe
from .decorators import user_has_donated


def donate(request):

    stripe_public_key = os.environ.get('STRIPE_PUBLIC_KEY')
    stripe_secret_key = os.environ.get('STRIPE_SECRET_KEY')

    stripe_total = 1000
    stripe.api_key = stripe_secret_key

    has_donated = False
    if request.method == 'POST':
        # Get the user's profile
        profile = Profile.objects.get(profile_user=request.user)

        # Create or update the user's donation status
        donation, created = Donation.objects.get_or_create(
            profile=profile,
            defaults={'donated': True},
        )
        if not created:
            donation.donated = True
            donation.save()

        has_donated = True

        # Create the Stripe payment
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Redirect to the success page
        return redirect('donate_success')
    else:
        if request.user.is_authenticated:
            # check if the user has a donation
            try:
                donation = Donation.objects.get(profile=Profile.objects.get(profile_user=request.user))
                has_donated = donation.donated
            except Donation.DoesNotExist:
                has_donated = False

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        template = 'donate/donate.html'
        context = {
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
            'has_donated': has_donated,
        }

        return render(request, template, context)


@user_has_donated
def donate_success(request):
    """ A view to render the donation success page """
    return render(request, 'donate/donate_success.html')