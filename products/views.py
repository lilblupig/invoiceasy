""" View information for products and pricing pages """

from django.shortcuts import render, get_object_or_404
from .models import Plan

# Create your views here.


def pricing(request):
    """ View to return pricing information """

    plans = Plan.objects.all()

    context = {
        'plans': plans,
    }
    return render(request, 'products/pricing.html', context)


def plan_detail(request, plan_id):
    """ View to return details about a specific plan """

    plan = get_object_or_404(Plan, pk=plan_id)

    context = {
        'plan': plan,
    }
    return render(request, 'products/plan_detail.html', context)
