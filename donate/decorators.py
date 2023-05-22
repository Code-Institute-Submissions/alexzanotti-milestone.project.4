from django.http import HttpResponseForbidden
from donate.models import Donation

def user_has_donated(function):
    def wrap(request, *args, **kwargs):
        try:
            donation = Donation.objects.get(profile__profile_user=request.user)
            if donation.donated:
                return function(request, *args, **kwargs)
            else:
                return HttpResponseForbidden()
        except Donation.DoesNotExist:
            return HttpResponseForbidden()
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap