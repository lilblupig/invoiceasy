""" View information for invoicing pages """

from django.shortcuts import render

# Create your views here.


def invoices(request):
    """ View to return invoices page """
    return render(request, 'invoices/invoices.html')