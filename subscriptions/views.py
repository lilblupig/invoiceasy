""" View information for subscription pages """

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required
def subscribe(request):
    """ View to return checkout page """
    return render(request, 'subscriptions/subscribe.html')
