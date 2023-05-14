from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(user_signed_up)
def populate_profile(request, user, **kwargs):
    profile = Profile.objects.create(
        profile_user=user, profile_user_name=user.username, profile_email=user.email)
