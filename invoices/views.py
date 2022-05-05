""" View information for invoicing pages """

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import InvoiceCustomer, Invoice
from .forms import InvoiceCustomerForm, InvoiceForm

# Create your views here.


@login_required()
def dashboard(request):
    """ View to return dashboard page """

    user = request.user
    invoices = Invoice.objects.filter(user_id__exact=user)
    customers = InvoiceCustomer.objects.filter(user_id__exact=user)

    template = 'invoices/dashboard.html'
    context = {
        'user': user,
        'invoices': invoices,
        'customers': customers,
    }

    return render(request, template, context)


@login_required()
def customer(request, customer_id):
    """ View to return customer form """

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

    if request.method == 'POST':
        # If invoice id == 0 save new instance
        if invoice_id == '0':
            form = InvoiceForm(request.POST)
        # Otherwise update existing invoice
        else:
            this_invoice = Invoice.objects.get(id=invoice_id)
            form = InvoiceForm(request.POST, instance=this_invoice)

        if form.is_valid():
            hold_form = form.save(commit=False)
            hold_form.user = request.user
            hold_form.save()
            messages.success(request, 'Invoice updated successfully!')

    # If invoice id == 0 render blank form
    if invoice_id == '0':
        form = InvoiceForm()
    # Else render form with invoice details
    else:
        this_invoice = Invoice.objects.get(id=invoice_id)
        form = InvoiceForm(instance=this_invoice)

    template = 'invoices/invoice_form.html'
    context = {
        'form': form,
        'invoice_id': invoice_id,
    }
    return render(request, template, context)
