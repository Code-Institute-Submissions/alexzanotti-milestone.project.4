from .forms import ProfileUpdateForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile


@login_required
def profile(request):
    profile = get_object_or_404(Profile, profile_user=request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            # Add a success message or redirect as needed

    else:
        form = ProfileUpdateForm(instance=profile)

    context = {'form': form}
    return render(request, 'profiles/profile.html', context)
