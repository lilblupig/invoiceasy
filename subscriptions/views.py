""" View information for subscription pages """

from django.shortcuts import render

# Create your views here.


def subscribe(request):
    """ View to return checkout page """
    return render(request, 'subscriptions/subscribe.html')
