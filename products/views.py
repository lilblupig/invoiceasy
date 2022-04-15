""" View information for products and pricing pages """

from django.shortcuts import render
from .models import Plan

# Create your views here.


def pricing(request):
    """ View to return pricing information """

    plans = Plan.objects.all()

    context = {
        'plans': plans,
    }
    return render(request, 'products/pricing.html', context)
