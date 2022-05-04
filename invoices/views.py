""" View information for invoicing pages """

from django.shortcuts import render
from django.contrib import messages
from .models import InvoiceCustomer, Invoice
from .forms import InvoiceCustomerForm, InvoiceForm

# Create your views here.


def dashboard(request):
    """ View to return invoices page """

    user = request.user
    invoices = Invoice.objects.all()
    customers = InvoiceCustomer.objects.all()

    template = 'invoices/dashboard.html'
    context = {
        'user': user,
        'invoices': invoices,
        'customers': customers,
    }

    return render(request, template, context)


def customer(request):
    """ View to return customer form """

    if request.method == 'POST':
        form = InvoiceCustomerForm(request.POST)
        if form.is_valid():
            hold_form = form.save(commit=False)
            hold_form.user = request.user
            hold_form.save()
            messages.success(request, 'Updated successfully!')

    form = InvoiceCustomerForm()

    template = 'invoices/customer_form.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def invoice(request):
    """ View to return invoice form """

    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            hold_form = form.save(commit=False)
            hold_form.user = request.user
            hold_form.save()
            messages.success(request, 'Updated successfully!')

    form = InvoiceForm()

    template = 'invoices/invoice_form.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
