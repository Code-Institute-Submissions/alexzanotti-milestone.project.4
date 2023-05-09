from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile


@login_required
def profile(request):
    profile = get_object_or_404(Profile, profile_user=request.user)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
