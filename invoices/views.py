""" View information for invoicing pages """

import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from subscriptions.models import StripeCustomer
from utils.utils import make_date
from .models import InvoiceCustomer, Invoice
from .forms import InvoiceCustomerForm, InvoiceForm


@login_required()
def dashboard(request):
    """ View to return dashboard page """

    # Get user and create invoices and customers, check subscription
    user = request.user
    invoices = Invoice.objects.filter(
        user_id__exact=user).select_related('customer_code')
    customers = InvoiceCustomer.objects.filter(user_id__exact=user)
    subscribed = StripeCustomer.objects.filter(user=user).exists()

    try:
        # Retrieve the subscription & product for Dashboard
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(
            stripe_customer.stripeSubscriptionId)
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

    # Set the subscription for Dashboard where no subs in place
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
    # Prevent non-owners from accessing material
    if customer_id != '0':
        user_id = request.user.id
        owner_id = InvoiceCustomer.objects.get(id=customer_id).user_id
        if user_id != owner_id:
            messages.info(
                request,
                'You cannot access this item.'
            )
            return redirect('/invoices/')

    subscribed = StripeCustomer.objects.filter(user=request.user).exists()
    if subscribed is False:
        messages.info(
            request,
            'You cannot add new customers as you do not have a subscription'
        )
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
    # Prevent non-owners from accessing material
    if invoice_id != '0':
        user_id = request.user.id
        owner_id = Invoice.objects.get(id=invoice_id).user_id
        if user_id != owner_id:
            messages.info(
                request,
                'You cannot access this item.'
            )
            return redirect('/invoices/')

    subscribed = StripeCustomer.objects.filter(user=request.user).exists()
    if subscribed is False:
        messages.info(
            request,
            'You cannot add new invoices as you do not have a subscription'
        )
        return redirect('/invoices/')

    if request.method == 'POST':
        # If invoice id == 0 save new instance
        if invoice_id == '0':
            form = InvoiceForm(request.POST, user=request.user)
        # Otherwise update existing invoice
        else:
            this_invoice = Invoice.objects.get(id=invoice_id)
            form = InvoiceForm(
                request.POST,
                instance=this_invoice,
                user=request.user
            )

        if form.is_valid():
            hold_form = form.save(commit=False)

            # If VAT registered, calculate VAT and gross
            subscriber = get_object_or_404(UserProfile, user=request.user)
            if subscriber.vat_number:
                vat = hold_form.invoice_subtotal * 0.2
                gross = hold_form.invoice_subtotal + vat
            # Otherwise set VAT to nil and gross to subtotal value
            else:
                vat = 0.00
                gross = hold_form.invoice_subtotal

            hold_form.invoice_vat = vat
            hold_form.invoice_gross = gross
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


@login_required()
def delete_invoice(request, invoice_id):
    """ View to delete an invoice """
    # Prevent non-owners from accessing material
    user_id = request.user.id
    owner_id = Invoice.objects.get(id=invoice_id).user_id
    if user_id != owner_id:
        messages.info(
            request,
            'You cannot access this item.'
        )
        return redirect('/invoices/')

    subscribed = StripeCustomer.objects.filter(user=request.user).exists()
    if subscribed is False:
        messages.info(
            request,
            'You cannot delete invoices as you do not have a subscription'
        )
        return redirect('/invoices/')

    Invoice.objects.filter(id=invoice_id).delete()
    return redirect('/invoices/')


@login_required()
def delete_customer(request, customer_id):
    """ View to delete a customer and all invoices """
    # Prevent non-owners from accessing material
    user_id = request.user.id
    owner_id = InvoiceCustomer.objects.get(id=customer_id).user_id
    if user_id != owner_id:
        messages.info(
            request,
            'You cannot access this item.'
        )
        return redirect('/invoices/')

    subscribed = StripeCustomer.objects.filter(user=request.user).exists()
    if subscribed is False:
        messages.info(
            request,
            'You cannot delete customers as you do not have a subscription'
        )
        return redirect('/invoices/')

    InvoiceCustomer.objects.filter(id=customer_id).delete()
    return redirect('/invoices/')
