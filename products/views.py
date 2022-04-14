""" View information for products and pricing pages """

from django.shortcuts import render

# Create your views here.


def pricing(request):
    """ View to return index page """
    return render(request, 'products/pricing.html')
