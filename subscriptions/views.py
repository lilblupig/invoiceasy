""" View information for subscription pages """
# From https://testdriven.io/blog/django-stripe-subscriptions/

import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@login_required
def subscribe(request):
    """ View to return checkout page """
    return render(request, 'subscriptions/subscribe.html')


@csrf_exempt
def stripe_config(request):
    """ Handle Stripe AJAX request """
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    """ Create a checkout session """
    if request.method == 'GET':
        domain_url = 'https://8000-lilblupig-invoiceasy-1i26yyobyrv.ws-eu42.gitpod.io/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'subscriptions/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'subscriptions/cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@login_required
def success(request):
    """ Return page for succesful subscription """
    return render(request, 'subscriptions/success.html')


@login_required
def cancel(request):
    """ Return page for cancelled subscription """
    return render(request, 'subscriptions/cancel.html')
