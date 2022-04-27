""" View information for subscription pages """
# From https://testdriven.io/blog/django-stripe-subscriptions/

import datetime
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from products.models import Plan
from .models import StripeCustomer

# Create your views here.


@login_required
def subscribe(request, plan_id):
    """ View to return checkout page """

    plan = get_object_or_404(Plan, pk=plan_id)

    def make_date(date_value):
        """ Convert Stripe value to user friendly date """
        nice_date = datetime.datetime.fromtimestamp(date_value).strftime('%d-%m-%Y %H:%M:%S')
        return nice_date

    try:
        # Retrieve the subscription & product
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        subscription_start = make_date(subscription.current_period_start)
        subscription_end = make_date(subscription.current_period_end)
        product = stripe.Product.retrieve(subscription.plan.product)

        # Feel free to fetch any additional data from 'subscription' or 'product'
        # https://stripe.com/docs/api/subscriptions/object
        # https://stripe.com/docs/api/products/object

        return render(request, 'subscriptions/subscribe.html', {
            'subscription': subscription,
            'product': product,
            'subscription_start': subscription_start,
            'subscription_end': subscription_end,
        })

    # Show checkout page if not already subscribed
    except StripeCustomer.DoesNotExist:
        return render(request, 'subscriptions/subscribe.html', {'plan': plan})


@csrf_exempt
def stripe_config(request):
    """ Handle Stripe AJAX request """
    if request.method == 'GET':
        stripe_configs = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_configs, safe=False)


@csrf_exempt
def create_checkout_session(request):
    """ Create a checkout session """
    if request.method == 'GET':
        domain_url = settings.DOMAIN_URL
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


@csrf_exempt
def stripe_webhook(request):
    """ Create new StripeCustomer on subscription """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')

        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_subscription_id,
        )
        print(user.username + ' just subscribed.')

    return HttpResponse(status=200)
