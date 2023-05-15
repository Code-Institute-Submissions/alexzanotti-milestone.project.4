from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import Profile
import stripe


# Create your views here.


stripe.api_key = 'your-secret-key'


def donate(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            token = request.POST.get('stripeToken')
            try:
                charge = stripe.Charge.create(
                    amount=1000,  # amount in cents
                    currency='usd',
                    description='Donation',
                    source=token,
                )
                profile = Profile.objects.get(profile_user=request.user)
                profile.has_donated = True
                profile.save()

                messages.success(request, 'Thank you for your donation!')
                return redirect('donate')

            except stripe.error.CardError as e:
                messages.error(
                    request, 'There was an error processing your donation. ' + e.user_message)
                return redirect('donate')
        else:
            messages.error(
                request, 'You need to log in or create an account before making a donation.')
            return redirect('login')
    else:
        return render(request, 'donate/donate.html')


def donate(request):
    bag = request.session.get('bag', {})

    order_form = OrderForm()
    template = 'donate/donate.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51N6fG5HqHvT2PvVfoDyps16JYahKvD5EWT5r9pJJuxB5LvRCoqUrWa97j1AFxXEYbk6rVhIRKJmV3FVNSmbIcFe100qZsIuw07',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
