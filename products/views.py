""" View information for products and pricing pages """

from django.shortcuts import render, get_object_or_404
from .models import Plan


def pricing(request):
    """ View to return pricing information """
    # Get all the plans
    plans = Plan.objects.all()

    context = {
        'plans': plans,
    }

    return render(request, 'products/pricing.html', context)


def plan_detail(request, plan_id):
    """ View to return details about a specific plan """
    # Get information about chosen plan
    plan = get_object_or_404(Plan, pk=plan_id)

    # Store in session
    plan_stripe_id = plan.stripe_id
    plan_name = plan.name
    request.session.__setitem__('plan_stripe_id', plan_stripe_id)
    request.session.__setitem__('plan_name', plan_name)

    context = {
        'plan': plan,
    }

    return render(request, 'products/plan_detail.html', context)
