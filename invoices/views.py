""" View information for invoicing pages """

import datetime
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from subscriptions.models import StripeCustomer
from .models import InvoiceCustomer, Invoice
from .forms import InvoiceCustomerForm, InvoiceForm

# Create your views here.


@login_required()
def dashboard(request):
    """ View to return dashboard page """

    user = request.user
    invoices = Invoice.objects.filter(user_id__exact=user)
    customers = InvoiceCustomer.objects.filter(user_id__exact=user)
    subscribed = StripeCustomer.objects.filter(user=user).exists()

    def make_date(date_value):
        """ Convert Stripe value to user friendly date """
        nice_date = datetime.datetime.fromtimestamp(date_value).strftime('%d-%m-%Y')
        return nice_date

    try:
        # Retrieve the subscription & product
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        subscription_start = make_date(subscription.current_period_start)
        subscription_end = make_date(subscription.current_period_end)
        product = stripe.Product.retrieve(subscription.plan.product)
        cancelled = subscription.cancel_at_period_end

        context = {
            'subscription': subscription,
            'product': product,
            'subscription_start': subscription_start,
            'subscription_end': subscription_end,
            'user': user,
            'invoices': invoices,
            'customers': customers,
            'cancelled': cancelled,
            'subscribed': subscribed,
        }

    # Show checkout page if not already subscribed
    except StripeCustomer.DoesNotExist:
        subscription = 'No current subscription'
        context = {
            'subscription': subscription,
            'user': user,
            'invoices': invoices,
            'customers': customers,
            'subscribed': subscribed,
        }

    template = 'invoices/dashboard.html'

    return render(request, template, context)


@login_required()
def customer(request, customer_id):
    """ View to return customer form """

    subscribed = StripeCustomer.objects.filter(user=request.user).exists()
    if subscribed is False:
        messages.success(request, 'You cannot add new customers as you do not have a current subscription')
        return redirect('/invoices/')

    if request.method == 'POST':
        # If customer id == 0 save new instance
        if customer_id == '0':
            form = InvoiceCustomerForm(request.POST)
        # Otherwise update existing customer
        else:
            this_customer = InvoiceCustomer.objects.get(id=customer_id)
            form = InvoiceCustomerForm(request.POST, instance=this_customer)
        if form.is_valid():
            hold_form = form.save(commit=False)
            hold_form.user = request.user
            hold_form.save()
            messages.success(request, 'Customer updated successfully!')

    # If customer id == 0 render blank form
    if customer_id == '0':
        form = InvoiceCustomerForm()
    # Else render form with customer details
    else:
        this_customer = InvoiceCustomer.objects.get(id=customer_id)
        form = InvoiceCustomerForm(instance=this_customer)

    template = 'invoices/customer_form.html'
    context = {
        'form': form,
        'customer_id': customer_id,
    }
    return render(request, template, context)


@login_required()
def invoice(request, invoice_id):
    """ View to return invoice form """

    subscribed = StripeCustomer.objects.filter(user=request.user).exists()
    if subscribed is False:
        messages.success(request, 'You cannot add new invoices as you do not have a current subscription')
        return redirect('/invoices/')

    if request.method == 'POST':
        # If invoice id == 0 save new instance
        if invoice_id == '0':
            form = InvoiceForm(request.POST, user=request.user)
        # Otherwise update existing invoice
        else:
            this_invoice = Invoice.objects.get(id=invoice_id)
            form = InvoiceForm(request.POST, instance=this_invoice, user=request.user)

        if form.is_valid():
            hold_form = form.save(commit=False)
            hold_form.user = request.user
            hold_form.save()
            messages.success(request, 'Invoice updated successfully!')

    # If invoice id == 0 render blank form
    if invoice_id == '0':
        form = InvoiceForm(user=request.user)
    # Else render form with invoice details
    else:
        this_invoice = Invoice.objects.get(id=invoice_id)
        form = InvoiceForm(instance=this_invoice, user=request.user)

    template = 'invoices/invoice_form.html'
    context = {
        'form': form,
        'invoice_id': invoice_id,
    }
    return render(request, template, context)
