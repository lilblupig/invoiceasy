""" View information for profile pages """

from django.shortcuts import render

# Create your views here.


def profile(request):
    """ View to return profile information """

    return render(request, 'profiles/profile.html')