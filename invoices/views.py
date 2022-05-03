""" View information for invoicing pages """

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import InvoiceCustomer
from .forms import InvoiceCustomerForm

# Create your views here.


def invoices(request):
    """ View to return invoices page """
    return render(request, 'invoices/invoices.html')


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
