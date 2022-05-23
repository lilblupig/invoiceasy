""" View information for subscription pages """
# From https://testdriven.io/blog/django-stripe-subscriptions/

import datetime
import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from profiles.models import UserProfile
from .models import StripeCustomer

# Create your views here.


@login_required
def subscribe(request):
    """ View to return checkout page """

    def make_date(date_value):
        """ Convert Stripe value to user friendly date """
        nice_date = datetime.datetime.fromtimestamp(date_value).strftime(
            '%d-%m-%Y')
        return nice_date

    try:
        # Retrieve the subscription & product
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(
            stripe_customer.stripeSubscriptionId)
        subscription_start = make_date(subscription.current_period_start)
        subscription_end = make_date(subscription.current_period_end)
        product = stripe.Product.retrieve(subscription.plan.product)
        cancelled = subscription.cancel_at_period_end

        # https://stripe.com/docs/api/subscriptions/object
        # https://stripe.com/docs/api/products/object

        context = {
            'subscription': subscription,
            'product': product,
            'subscription_start': subscription_start,
            'subscription_end': subscription_end,
            'cancelled': cancelled,
        }

        return render(request, 'subscriptions/subscribe.html', context)

    # Show checkout page if not already subscribed
    except StripeCustomer.DoesNotExist:

        plan_name = request.session.__getitem__('plan_name')

        context = {
            'plan_name': plan_name,
        }

        return render(request, 'subscriptions/subscribe.html', context)


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
        plan_stripe_id = request.session.__getitem__('plan_stripe_id')
        customer = UserProfile.objects.get(user=request.user)
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None, # Remove ternary statement?
                success_url=domain_url + 'subscriptions/success?session_id={CHECKOUT_SESSION_ID}', # No idea about this!
                cancel_url=domain_url + 'subscriptions/abort/',
                payment_method_types=['card'],
                mode='subscription',
                customer_email=customer.email,
                line_items=[
                    {
                        'price': plan_stripe_id,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@login_required
def success(request):
    """ Return page for successful subscription """
    subscribed = StripeCustomer.objects.filter(user=request.user).exists()
    if subscribed is False:
        messages.info(
            request,
            'You cannot view this page as you do not have a subscription'
        )
        return redirect('/invoices/')
    return render(request, 'subscriptions/success.html')


@login_required
def abort(request):
    """ Return page for aborted subscription """
    return render(request, 'subscriptions/abort.html')


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


@login_required()
def cancel(request):
    """ Cancel subscription effective from end of current period """
    subscribed = StripeCustomer.objects.filter(user=request.user).exists()
    if subscribed is False:
        messages.info(
            request,
            'You cannot view this page as you do not have a subscription'
        )
        return redirect('/invoices/')

    stripe_customer = StripeCustomer.objects.get(user=request.user)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    subscription = stripe_customer.stripeSubscriptionId

    if request.method == 'POST':
        stripe.Subscription.modify(
            subscription,
            cancel_at_period_end=True
        )

        return redirect('/invoices/')

    return render(request, 'subscriptions/cancel.html')


@login_required()
def reactivate(request):
    """ Reactivate subscription if still valid """
    subscribed = StripeCustomer.objects.filter(user=request.user).exists()
    if subscribed is True:
        messages.info(
            request,
            'You cannot view this page as you already have a subscription'
        )
        return redirect('/invoices/')

    stripe_customer = StripeCustomer.objects.get(user=request.user)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    subscription = stripe_customer.stripeSubscriptionId

    stripe.Subscription.modify(
        subscription,
        cancel_at_period_end=False
    )

    messages.success(request, 'Subscription reactivated successfully!')

    return redirect('/invoices/')
