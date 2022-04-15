""" View information for profile pages """

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.


def profile(request):
    """ View to return profile information """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully!')

    form = UserProfileForm(instance=user_profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
